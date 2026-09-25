"""
INSTRUMENTO DE MEDIDA - modulo compartido por todos los experimentos.

Toda degradacion de pesos del programa pasa por aqui. Ningun experimento
implementa su propia cuantizacion o poda: eso es lo que produjo los tres bugs
de D-029, D-037 y las invalidaciones de P-11, P-14, P-15 y P-16.

REGLAS DE DISENO (P-21, obligatorias):

  1. El 0 es un nivel representable. w = 0  =>  q(w) = 0, siempre.
  2. Rejilla simetrica respecto a 0: misma resolucion en + y en -.
  3. Monotonia del error en espacio de pesos: al bajar bits o subir % de poda,
     el error de Frobenius NO baja.

PROHIBIDO como default: linspace(min(w), max(w), 2**b) sin anclar el cero.
Ese era el bug de D-037: con rango asimetrico ningun nivel cae en cero, los
pesos pequenos se van a un valor != 0, y PODARLOS CORRIGE ese sesgo -> la
fidelidad SUBE al podar. Parece un hallazgo y es un artefacto.

REGLA DE INVALIDACION: cualquier resultado obtenido con un cuantizador que no
represente el cero queda invalidado. Sin excepcion y sin reinterpretacion: hay
que reejecutar.
"""
import numpy as np
import scipy.sparse as sp

__all__ = ['quantize_arr', 'quantize', 'prune_mask', 'degrade',
           'weight_fidelity', 'guardian', 'ESQUEMA']

ESQUEMA = 'simetrico_anclado_en_cero_v1'


# ----------------------------------------------------------------------------
# Cuantizacion
# ----------------------------------------------------------------------------

def quantize_arr(w, bits):
    """Cuantizacion simetrica con el cero representable.

        L = 2**(bits-1) - 1          pasos positivos
        s = max|w| / L               escala
        q = s * clip(round(w/s), -L, L)

    Niveles: {-L, ..., -1, 0, 1, ..., L} * s  ->  2L+1 niveles, y el 0 esta
    SIEMPRE entre ellos. w = 0 => q = 0 exactamente.

    bits >= 2 obligatorio: con bits = 1 seria L = 0 y todo colapsaria a cero.
    """
    w = np.asarray(w, dtype=np.float64)
    if bits < 2:
        raise ValueError(f'bits debe ser >= 2 (recibido {bits}): con 1 bit con '
                         'signo no hay ningun nivel distinto de cero')
    if w.size == 0:
        return w.copy()
    L = 2 ** (bits - 1) - 1
    amax = np.abs(w).max()
    if amax == 0:
        return np.zeros_like(w)
    s = amax / L
    return s * np.clip(np.round(w / s), -L, L)


def quantize_magnitud(w, bits):
    """Cuantizacion SIN signo para magnitudes estrictamente positivas.

    quantize_arr() es simetrica: reserva la mitad del codigo para negativos.
    Aplicarla a una magnitud |w| >= 0 gasta la mitad del presupuesto en niveles
    que no se usan, de modo que 'b bits' rinden en realidad b-1. Ademas su
    escala arranca en cero, asi que con b pequeno las magnitudes bajas caen a 0
    y la arista DESAPARECE, mezclando el eje de resolucion de peso con el de
    poda -- que P-28 mantiene separados.

    Esta version reparte 2**bits niveles uniformemente sobre [min(w), max(w)],
    de forma que ningun valor se anula y b bits son b bits.

        bits = 1  ->  2 niveles     bits = 4  ->  16 niveles
    """
    w = np.asarray(w, dtype=np.float64)
    if bits < 1:
        raise ValueError(f'bits debe ser >= 1 (recibido {bits})')
    if w.size == 0:
        return w.copy()
    if (w < 0).any():
        raise ValueError('quantize_magnitud espera valores no negativos; '
                         'para datos con signo usa quantize_arr')
    lo, hi = float(w.min()), float(w.max())
    if hi == lo:
        return w.copy()
    L = 2 ** bits - 1                      # 2**bits niveles => L pasos
    s = (hi - lo) / L
    return lo + s * np.clip(np.round((w - lo) / s), 0, L)


def escala(M, g):
    """M * g conservando dispersion. Sustituye a csr(M.toarray() * g) (D-140).

    Equivalente EXACTO en valores —verificado a g = 0 · 0,02 · 0,15 · 1 · 2,5—
    y **103x mas rapido**. Densificar una matriz n x n para multiplicarla por un
    escalar es gratuito a 300 nodos (0,4 % del tiempo, por eso no se toco en su
    momento) y **prohibitivo a 161.869**: 105 GB frente a 0,03 GB.

    `eliminate_zeros()` es imprescindible: escalar por 0 en disperso deja los
    ceros EXPLICITOS, y el resto del programa cuenta `nnz` para la tasa. Sin
    esta linea, g = 0 daria una tasa falsa.
    """
    out = (M * float(g)).tocsr().astype(np.float32)
    out.eliminate_zeros()
    return out


def quantize(M, bits):
    """Version sparse de quantize_arr. Conserva la estructura."""
    if not sp.issparse(M):
        return quantize_arr(M, bits)
    out = M.copy().tocoo()
    if out.data.size == 0:
        return out.tocsr()
    out.data = quantize_arr(out.data, bits).astype(np.float32)
    return out.tocsr()


# ----------------------------------------------------------------------------
# Poda
# ----------------------------------------------------------------------------

def prune_mask(data, frac):
    """Poda por RANGO: elimina exactamente floor(frac * n) entradas, las de
    menor |valor|, con desempate DETERMINISTA por indice.

    No usa umbral de cuantil: `|d| >= quantile(|d|, frac)` conserva todos los
    empates en el umbral, y tras cuantizar los empates son masivos. Ese era el
    bug de D-029: pedir 20 % de poda borraba el 4,4 %, y a 2 bits las podas de
    20/35/50 % daban la red IDENTICA.
    """
    data = np.asarray(data)
    n = data.size
    k = int(np.floor(frac * n))
    keep = np.ones(n, dtype=bool)
    if k <= 0:
        return keep
    order = np.lexsort((np.arange(n), np.abs(data)))   # menor magnitud primero
    keep[order[:k]] = False
    return keep


def degrade(M, bits, frac):
    """Cuantiza y luego poda. Devuelve sparse con la misma forma.

    La fraccion de poda se cuenta sobre las entradas ORIGINALES almacenadas,
    no sobre las que sobreviven a la cuantizacion. Es la definicion
    preregistrada y `test_instrumento.T3` la comprueba.
    """
    if not sp.issparse(M):
        M = sp.csr_matrix(np.asarray(M, dtype=np.float32))
    out = M.copy().tocoo()
    if out.data.size == 0:
        return out.tocsr()
    d = quantize_arr(out.data, bits)
    keep = prune_mask(d, frac)
    return sp.csr_matrix((d[keep].astype(np.float32),
                          (out.row[keep], out.col[keep])), shape=M.shape)


# ----------------------------------------------------------------------------
# Guardian
# ----------------------------------------------------------------------------

def weight_fidelity(ref_mats, deg_mats):
    """Fidelidad en ESPACIO DE PESOS: 1 - ||W_ref - W_deg||_F / ||W_ref||_F.

    Se mide sobre los pesos, NUNCA sobre la salida de la red no lineal. Usar
    otra metrica de salida como control fue el error que invalido P-11 dos
    veces: un control sujeto al mismo problema que debe detectar no es control.
    """
    a = np.vstack([m.toarray() if sp.issparse(m) else np.asarray(m)
                   for m in ref_mats])
    b = np.vstack([m.toarray() if sp.issparse(m) else np.asarray(m)
                   for m in deg_mats])
    na = np.linalg.norm(a)
    return float(1.0 - np.linalg.norm(a - b) / (na + 1e-12))


def guardian(mats, bits_grid, prune_grid, tol=0.02):
    """T5 - guardian POR RED, a ejecutar ANTES de calcular ninguna Psi.

    Comprueba que el error en espacio de pesos es monotono no decreciente a lo
    largo de cada eje por separado:
        eje Q: poda fija, bits decrecientes
        eje P: bits fijos, poda creciente

    Nunca sobre un eje colapsado tipo bits*(1-poda): ese proxy dice que
    "32 bits con 35 % de poda" conserva mas informacion que "8 bits sin poda",
    lo cual es falso y fabrica inversiones que no son de la metrica.

    Devuelve dict con 'pasa'. Si pasa=False, NO se calcula Psi.
    """
    wf = {}
    for b in bits_grid:
        for p in prune_grid:
            wf[(b, p)] = weight_fidelity(mats, [degrade(m, b, p) for m in mats])

    inv, worst, detalle = 0, 0.0, []
    for p in prune_grid:
        seq = [wf[(b, p)] for b in bits_grid]
        bad = [(i, j) for i in range(len(seq)) for j in range(i + 1, len(seq))
               if seq[j] - seq[i] > tol]
        if bad:
            inv += len(bad)
            worst = max(worst, max(seq[j] - seq[i] for i, j in bad))
        detalle.append(('Q', f'poda={p:.2f}', [round(v, 4) for v in seq],
                        len(bad)))
    for b in bits_grid:
        seq = [wf[(b, p)] for p in prune_grid]
        bad = [(i, j) for i in range(len(seq)) for j in range(i + 1, len(seq))
               if seq[j] - seq[i] > tol]
        if bad:
            inv += len(bad)
            worst = max(worst, max(seq[j] - seq[i] for i, j in bad))
        detalle.append(('P', f'bits={b}', [round(v, 4) for v in seq], len(bad)))

    vals = list(wf.values())
    return {'pasa': bool(inv == 0), 'inversiones': inv,
            'magnitud_max': round(worst, 6),
            'rango': round(max(vals) - min(vals), 6),
            'fidelidad': {f'{b}_{p}': round(v, 6) for (b, p), v in wf.items()},
            'detalle': detalle, 'esquema': ESQUEMA}


# ----------------------------------------------------------------------------
# P-32: condiciones aleatorizadas, por BANDERA EXPLICITA
# ----------------------------------------------------------------------------

class Condicion:
    """Una condicion experimental, con bandera explicita de aleatorizacion.

    P-32. C2 (sigma <= umbral) disparo tres veces sobre condiciones que son
    aleatorias POR DISENO -- los barajados, y M0 (grafo Erdos-Renyi generado de
    nuevo en cada semilla). En esas condiciones la varianza alta no es un
    defecto: ES la informacion que aportan.

    La regla anterior clasificaba por PREFIJO DE NOMBRE ('CTRL_'), asi que M0
    entraba como medicion. Es la segunda vez que una clasificacion basada en
    nombres falla en este programa; la primera fue la lista GABA (D-050).

    REGLA: `aleatorizada` se declara en la DEFINICION de la condicion, junto a
    su nivel de manifiesto. Nunca se infiere del nombre.
    """

    __slots__ = ('nombre', 'nivel', 'shuffle', 'aleatorizada')

    def __init__(self, nombre, nivel, shuffle=None, aleatorizada=False):
        self.nombre = nombre
        self.nivel = nivel
        self.shuffle = shuffle
        self.aleatorizada = bool(aleatorizada)

    def __repr__(self):
        return (f'Condicion({self.nombre!r}, nivel={self.nivel}, '
                f'shuffle={self.shuffle!r}, aleatorizada={self.aleatorizada})')


def condiciones_estandar():
    """Las seis condiciones del nucleo, con su bandera declarada.

    M0 es ALEATORIZADA: genera un grafo Erdos-Renyi distinto en cada semilla.
    Que no empiece por 'CTRL_' no la hace una medicion.
    """
    return [
        Condicion('M0_sin_topologia', 0, None, aleatorizada=True),
        Condicion('M1_topologia', 1, None, aleatorizada=False),
        Condicion('M2_signo', 2, None, aleatorizada=False),
        Condicion('M3_gaps', 3, None, aleatorizada=False),
        Condicion('CTRL_shuffle_signo', 2, 'signo', aleatorizada=True),
        Condicion('CTRL_shuffle_gap', 3, 'gap', aleatorizada=True),
    ]


def sigma_de_medicion(resultados, condiciones, claves=('delta_std', 'psi_b_std')):
    """Sigma maxima sobre las condiciones NO aleatorizadas. Es la que juzga C2."""
    det = [c.nombre for c in condiciones if not c.aleatorizada]
    vals = [resultados[n][k] for n in det if n in resultados
            for k in claves if k in resultados[n]]
    return max(vals) if vals else 0.0


# ----------------------------------------------------------------------------
# PUNTO OPERATIVO b*  --  sustituye al "codo" clasico
# ----------------------------------------------------------------------------
#
# El codo clasico mezclaba dos capas:
#   (a) un presupuesto de informacion, bien definido en ESPACIO DE PESOS
#   (b) un umbral sobre Psi de SALIDA, que [MEDIDO] no es monotona
#
# Exigia que bajar bits no subiera Psi, y eso es falso. De ahi la crisis.
#
# La sustitucion separa las capas:
#   Capa A  presupuesto en pesos, monotono por construccion y verificado por
#           el guardian. Es la variable independiente.
#   Capa B  Psi de salida se REPORTA; no elige el punto operativo.
#   Capa C  Delta se mide en b*, con A y B a la MISMA tasa.
#
# REGLA DE LABORATORIO: el instrumento elige o valida la tasa; Psi solo puntua
# A y B a esa tasa. Si Psi sube al degradar, eso se reporta como propiedad de
# la metrica o de la red -- nunca se usa para "buscar el codo optimo".

def tasa(mats, bits, frac, n_edges=None):
    """Longitud de descripcion: entradas NO NULAS x bits / aristas originales."""
    if n_edges is None:
        n_edges = sum(m.nnz for m in mats)
    nz = sum(int((degrade(m, bits, frac).tocoo().data != 0).sum()) for m in mats)
    return nz * bits / max(n_edges, 1)


def celdas_degeneradas(mats, bits_grid, prune_grid):
    """Una celda es degenerada si podar no elimina ninguna entrada NO NULA:
    es un duplicado de otra con menos poda y no aporta punto de rejilla."""
    nnz = {}
    for b in bits_grid:
        for p in prune_grid:
            nnz[(b, p)] = sum(
                int((degrade(m, b, p).tocoo().data != 0).sum()) for m in mats)
    degen = []
    for b in bits_grid:
        prev = nnz[(b, prune_grid[0])]
        for p in prune_grid[1:]:
            if prev - nnz[(b, p)] == 0:
                degen.append((b, p))
            prev = nnz[(b, p)]
    return degen, nnz


def punto_operativo(mats, bits_grid, prune_grid, umbral_fidelidad=0.70):
    """b* -- el punto de comparacion, elegido SIN mirar ninguna Psi de salida.

    Regla: la celda de MENOR TASA cuya fidelidad EN ESPACIO DE PESOS sea
    >= umbral_fidelidad, excluidas las degeneradas.

    Como la fidelidad en pesos es monotona (garantizado por el guardian), el
    minimo existe, es unico y es interpretable. Ninguna propiedad de la salida
    de la red interviene en la eleccion.

    Devuelve dict con la celda, su tasa, su fidelidad de pesos y el error de
    Frobenius -- la linea que todo informe debe publicar.
    """
    degen, nnz = celdas_degeneradas(mats, bits_grid, prune_grid)
    n_edges = sum(m.nnz for m in mats)
    cand = []
    for b in bits_grid:
        for p in prune_grid:
            if (b, p) in degen:
                continue
            wf = weight_fidelity(mats, [degrade(m, b, p) for m in mats])
            cand.append({'bits': b, 'poda': p,
                         'tasa': nnz[(b, p)] * b / max(n_edges, 1),
                         'fidelidad_pesos': wf, 'error_F': 1.0 - wf})
    admisibles = [c for c in cand if c['fidelidad_pesos'] >= umbral_fidelidad]
    if not admisibles:
        return {'b_estrella': None, 'motivo': 'ninguna celda alcanza el umbral',
                'umbral_fidelidad': umbral_fidelidad, 'candidatas': cand,
                'degeneradas': [list(x) for x in degen]}
    best = min(admisibles, key=lambda c: c['tasa'])
    return {'b_estrella': (best['bits'], best['poda']),
            'tasa': best['tasa'], 'fidelidad_pesos': best['fidelidad_pesos'],
            'error_F': best['error_F'], 'umbral_fidelidad': umbral_fidelidad,
            'elegido_sin_mirar_psi': True,
            'degeneradas': [list(x) for x in degen], 'candidatas': cand}


def linea_de_informe(po, psi_a=None):
    """La linea que P-34 (D-061) obliga a publicar en todo informe."""
    if po.get('b_estrella') is None:
        return 'b* = NO DEFINIDO (' + po.get('motivo', '') + ')'
    b, p = po['b_estrella']
    s = (f"b* = ({b} bits, poda {p:.2f}) · tasa = {po['tasa']:.3f} bits/arista · "
         f"error_F = {po['error_F']:.4f}")
    if psi_a is not None:
        s += f" · Psi_A = {psi_a:.4f}"
    return s
