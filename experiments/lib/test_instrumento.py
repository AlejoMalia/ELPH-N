"""
P-21 - BATERIA DE PRUEBAS DEL INSTRUMENTO.

Casos con resultado CONOCIDO DE ANTEMANO. Si alguno falla, no se calcula
ninguna Psi ni se publica ninguna tabla de Delta. Sale con codigo != 0 para
que pueda bloquear en CI o en un script.

Cada prueba lleva anotado el bug real que habria detectado. T2 y T4 fallan con
el cuantizador viejo (D-037); T3 falla con la poda vieja (D-029). Una bateria
que no falla con el codigo defectuoso no prueba nada, asi que ambas versiones
se ejecutan y se comprueba que la vieja SUSPENDE.
"""
import sys
import numpy as np
import scipy.sparse as sp
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from instrumento import (quantize_arr, quantize, prune_mask, degrade,
                         weight_fidelity, guardian, ESQUEMA,
                         Condicion, condiciones_estandar, sigma_de_medicion,
                         punto_operativo, celdas_degeneradas, linea_de_informe)
from biologia import (GABA, SENSORIALES_ANFIDIALES, MOTORAS_EXCITATORIAS,
                      validar_cobertura, CoberturaIncompleta,
                      resumen_cobertura)

BITS_GRID = (32, 8, 4, 2)
PRUNE_GRID = (0.0, 0.20, 0.35, 0.50)
FALLOS = []


def check(cond, tid, msg):
    estado = 'PASA' if cond else 'FALLA'
    if not cond:
        FALLOS.append(f'{tid}: {msg}')
    print(f'  [{estado}] {tid}  {msg}')
    return cond


# ----------------------------------------------------------------------------
# Implementaciones VIEJAS, conservadas solo para probar que la bateria muerde
# ----------------------------------------------------------------------------

def quantize_viejo(w, bits):
    """Rejilla uniforme min..max. NO ancla el cero. Bug de D-037."""
    w = np.asarray(w, dtype=np.float64)
    if bits >= 32 or w.size == 0:
        return w.copy()
    lo, hi = w.min(), w.max()
    if hi <= lo:
        return w.copy()
    lv = 2 ** bits - 1
    return np.round((w - lo) / (hi - lo) * lv) / lv * (hi - lo) + lo


def prune_viejo(data, frac):
    """Umbral de cuantil con `>=`. Conserva todos los empates. Bug de D-029."""
    data = np.asarray(data)
    if frac <= 0 or data.size == 0:
        return np.ones(data.size, dtype=bool)
    return np.abs(data) >= np.quantile(np.abs(data), frac)


# ----------------------------------------------------------------------------
# Redes de prueba: distribuciones deliberadamente distintas
# ----------------------------------------------------------------------------

def redes_de_prueba():
    rng = np.random.default_rng(21)
    n, m = 200, 4000
    out = {}
    for nombre, gen in (
        ('gaussiana_simetrica', lambda: rng.normal(0, 1, m)),
        ('asimetrica_desplazada', lambda: rng.lognormal(1.0, 0.8, m) - 0.5),
        ('sigmoide_Fases_II_IV', lambda: (
            1 / (1 + np.exp(-0.85 * (rng.lognormal(1.0, 0.8, m) - 2.5)))
            * rng.choice([2.0, 1.0, 0.6], m)
            * np.where(rng.random(m) < 0.8, 1.0, -1.0))),
        ('bimodal_lejos_de_cero', lambda: rng.choice([-1.0, 1.0], m)
            + rng.normal(0, 0.05, m)),
        ('concentrada_en_cero', lambda: rng.normal(0, 0.02, m)),
    ):
        r, c = rng.integers(0, n, m), rng.integers(0, n, m)
        out[nombre] = sp.csr_matrix((gen().astype(np.float32), (r, c)),
                                    shape=(n, n))
    return out


def monotona(seq, tol=0.02):
    """seq ordenada de MENOS a MAS degradado; devuelve nº de inversiones."""
    return sum(1 for i in range(len(seq)) for j in range(i + 1, len(seq))
               if seq[j] - seq[i] > tol)


# ----------------------------------------------------------------------------
# T1 .. T6
# ----------------------------------------------------------------------------

def T1_maxima_resolucion():
    print('\nT1 - cuantizar a maxima resolucion no cambia la red')
    ok = True
    for nombre, M in redes_de_prueba().items():
        d = M.tocoo().data.astype(np.float64)
        q = quantize_arr(d, 32)
        err = np.linalg.norm(d - q) / (np.linalg.norm(d) + 1e-12)
        ok &= check(err < 1e-6, 'T1', f'{nombre}: error relativo {err:.2e}')
    return ok


def T2_cero_representable():
    print('\nT2 - el 0 es representable (w=0 => q=0)')
    w = np.array([-3.0, -0.1, 0.0, 0.1, 2.0])
    ok = True
    for b in (2, 3, 4, 8):
        q = quantize_arr(w, b)
        ok &= check(q[2] == 0.0, 'T2',
                    f'bits={b}: q(0)={q[2]:+.4f}  niveles={np.unique(q).size}')
    # simetria de la rejilla
    for b in (2, 3, 4):
        q = quantize_arr(np.linspace(-1, 1, 999), b)
        lv = np.unique(q)
        ok &= check(np.allclose(lv, -lv[::-1]), 'T2',
                    f'bits={b}: rejilla simetrica ({lv.size} niveles)')
    # el viejo DEBE fallar, si no la bateria no muerde
    qv = quantize_viejo(w, 2)
    ok &= check(qv[2] != 0.0, 'T2',
                f'el cuantizador VIEJO suspende como debe: q(0)={qv[2]:+.4f}')
    return ok


def T3_poda_exacta():
    print('\nT3 - la poda elimina exactamente la fraccion pedida')
    rng = np.random.default_rng(3)
    ok = True
    for nombre, gen in (('sin empates', lambda: rng.normal(0, 1, 1000)),
                        ('con empates masivos',
                         lambda: rng.choice([-1.0, 0.0, 1.0], 1000))):
        d = gen()
        for f in PRUNE_GRID:
            k = prune_mask(d, f)
            real = 1 - k.sum() / d.size
            ok &= check(abs(real - f) < 1e-9, 'T3',
                        f'{nombre}: pedido {f:.2f} -> real {real:.4f}')
    # el viejo DEBE fallar con empates
    d = np.round(rng.normal(0, 1, 1000) * 2) / 2
    reales = [1 - prune_viejo(d, f).sum() / d.size for f in PRUNE_GRID]
    ok &= check(any(abs(r - f) > 0.03 for r, f in zip(reales, PRUNE_GRID)),
                'T3', f'la poda VIEJA suspende como debe: '
                      f'{[round(r, 3) for r in reales]} vs {list(PRUNE_GRID)}')
    return ok


def T4_monotonia_en_pesos():
    print('\nT4 - el error en espacio de pesos es monotono en toda distribucion')
    ok = True
    for nombre, M in redes_de_prueba().items():
        wf = {(b, p): weight_fidelity([M], [degrade(M, b, p)])
              for b in BITS_GRID for p in PRUNE_GRID}
        inv = sum(monotona([wf[(b, p)] for b in BITS_GRID]) for p in PRUNE_GRID)
        inv += sum(monotona([wf[(b, p)] for p in PRUNE_GRID]) for b in BITS_GRID)
        ok &= check(inv == 0, 'T4', f'{nombre}: {inv} inversiones')
    return ok


def T4b_el_viejo_suspende():
    print('\nT4b - el instrumento VIEJO suspende T4 (si no, la bateria no sirve)')

    def degrade_viejo(M, b, f):
        o = M.copy().tocoo()
        d = quantize_viejo(o.data.astype(np.float64), b)
        k = prune_viejo(d, f)
        return sp.csr_matrix((d[k].astype(np.float32), (o.row[k], o.col[k])),
                             shape=M.shape)

    total = 0
    for nombre, M in redes_de_prueba().items():
        wf = {(b, p): weight_fidelity([M], [degrade_viejo(M, b, p)])
              for b in BITS_GRID for p in PRUNE_GRID}
        inv = sum(monotona([wf[(b, p)] for b in BITS_GRID]) for p in PRUNE_GRID)
        inv += sum(monotona([wf[(b, p)] for p in PRUNE_GRID]) for b in BITS_GRID)
        total += inv
        print(f'      {nombre}: {inv} inversiones con el instrumento viejo')
    return check(total > 0, 'T4b',
                 f'el instrumento viejo acumula {total} inversiones')


def T5_guardian_por_red():
    print('\nT5 - el guardian por red pasa en todas las distribuciones')
    ok = True
    for nombre, M in redes_de_prueba().items():
        g = guardian([M], BITS_GRID, PRUNE_GRID)
        ok &= check(g['pasa'], 'T5', f'{nombre}: inversiones={g["inversiones"]} '
                                     f'rango={g["rango"]:.4f}')
    return ok


def T6_red_lineal_trivial():
    """Si la metrica es sana, en una red LINEAL (sin saturacion) la fidelidad
    de salida debe degradarse monotonamente. Es el unico test que toca la
    dinamica, y sirve de cordura para el resto del pipeline."""
    print('\nT6 - red lineal trivial: la salida degrada monotonamente')
    rng = np.random.default_rng(6)
    n = 100
    W = sp.csr_matrix((rng.normal(0, 1 / np.sqrt(n), n * n)
                       .astype(np.float32).reshape(n, n)))
    X = rng.normal(0, 1, size=(50, n)).astype(np.float32)
    ref = X @ W.toarray().T
    vals = []
    for b in BITS_GRID:
        for p in PRUNE_GRID:
            Y = X @ degrade(W, b, p).toarray().T
            a = ref / (np.linalg.norm(ref, axis=1, keepdims=True) + 1e-12)
            c = Y / (np.linalg.norm(Y, axis=1, keepdims=True) + 1e-12)
            vals.append(((b, p), float((a * c).sum(axis=1).mean())))
    d = dict(vals)
    inv = sum(monotona([d[(b, p)] for b in BITS_GRID]) for p in PRUNE_GRID)
    inv += sum(monotona([d[(b, p)] for p in PRUNE_GRID]) for b in BITS_GRID)
    rango = max(d.values()) - min(d.values())
    ok = check(inv == 0, 'T6', f'{inv} inversiones en la salida lineal')
    ok &= check(rango >= 0.15, 'T6',
                f'rango de la salida = {rango:.4f} (la metrica es sensible)')
    return ok


def T7_listas_nominales():
    """El cuarto bug de la serie (D-050) no estaba en la degradacion sino en
    la CONSTRUCCION de la red: la lista GABAergica usaba DD1..DD6/VD1..VD13 y
    el dataset nombra DD01..DD06/VD01..VD13. 15 de 26 no coincidian, en
    silencio. La bateria probaba el instrumento de degradar y no el de
    construir. T7 cierra ese hueco."""
    print('\nT7 - las listas nominales cubren el dataset al 100 %')
    import pandas as pd
    csv = (Path(__file__).resolve().parent.parent / 'fase-V' / 'results'
           / 'herm_full_edgelist.csv')
    if not csv.exists():
        return check(False, 'T7', f'no encuentro {csv}')
    df = pd.read_csv(csv)
    df.columns = [c.strip() for c in df.columns]
    for c in ('Source', 'Target'):
        df[c] = df[c].astype(str).str.strip()
    presentes = set(df.Source) | set(df.Target)

    ok = True
    for etiqueta, lst in (('GABA', sorted(GABA)),
                          ('sensoriales', SENSORIALES_ANFIDIALES),
                          ('motoras_excitatorias', MOTORAS_EXCITATORIAS)):
        try:
            cob = validar_cobertura(lst, presentes, etiqueta)
            ok &= check(True, 'T7', f'{etiqueta}: {cob:.0%} '
                                    f'({len(lst)} nombres)')
        except CoberturaIncompleta as e:
            ok &= check(False, 'T7', str(e))

    # la bateria debe MORDER: la lista vieja, con un digito, tiene que fallar
    vieja = ({f'DD{i}' for i in range(1, 7)} | {f'VD{i}' for i in range(1, 14)}
             | {'AVL', 'DVB', 'RIS', 'RMED', 'RMEV', 'RMEL', 'RMER'})
    try:
        validar_cobertura(sorted(vieja), presentes, 'GABA_vieja')
        ok &= check(False, 'T7', 'la lista GABA VIEJA deberia suspender y pasa')
    except CoberturaIncompleta:
        ok &= check(True, 'T7', 'la lista GABA VIEJA suspende como debe')
    return ok


def T8_banderas_aleatorizadas():
    """P-32. C2 disparo tres veces sobre condiciones aleatorias por diseno.
    La regla clasificaba por prefijo de nombre, y M0 -- que genera un grafo
    Erdos-Renyi nuevo en cada semilla -- no empieza por 'CTRL_'. T8 exige que
    la bandera este en la DEFINICION, no en el nombre."""
    print('\nT8 - las condiciones aleatorizadas llevan bandera explicita')
    conds = condiciones_estandar()
    ok = True
    esperado = {'M0_sin_topologia': True, 'M1_topologia': False,
                'M2_signo': False, 'M3_gaps': False,
                'CTRL_shuffle_signo': True, 'CTRL_shuffle_gap': True}
    for c in conds:
        ok &= check(c.aleatorizada == esperado[c.nombre], 'T8',
                    f'{c.nombre}: aleatorizada={c.aleatorizada}')
    # M0 NO empieza por CTRL_ y aun asi debe estar marcada
    m0 = next(c for c in conds if c.nombre == 'M0_sin_topologia')
    ok &= check(m0.aleatorizada and not m0.nombre.startswith('CTRL_'), 'T8',
                'M0 esta marcada pese a no llamarse CTRL_ (el bug de D-054)')
    # la regla vieja, por prefijo, DEBE fallar
    vieja = {c.nombre: c.nombre.startswith('CTRL_') for c in conds}
    ok &= check(vieja['M0_sin_topologia'] != esperado['M0_sin_topologia'], 'T8',
                'la regla VIEJA por prefijo suspende como debe')
    # sigma_de_medicion ignora las aleatorizadas
    fake = {c.nombre: {'delta_std': 0.9 if c.aleatorizada else 0.01,
                       'psi_b_std': 0.9 if c.aleatorizada else 0.01}
            for c in conds}
    s = sigma_de_medicion(fake, conds)
    ok &= check(abs(s - 0.01) < 1e-9, 'T8',
                f'sigma_de_medicion ignora las aleatorizadas: {s:.4f}')
    return ok


def T9_punto_operativo():
    """El codo clasico mezclaba presupuesto (bien definido en pesos) con un
    umbral sobre Psi de salida (no monotona). T9 comprueba que b* se elige SIN
    tocar la dinamica: solo con el error en espacio de pesos."""
    print('\nT9 - b* se elige sin mirar ninguna Psi de salida')
    ok = True
    for nombre, M in redes_de_prueba().items():
        po = punto_operativo([M], BITS_GRID, PRUNE_GRID)
        ok &= check(po.get('b_estrella') is not None, 'T9',
                    f'{nombre}: {linea_de_informe(po)}')
        if po.get('b_estrella'):
            # b* debe ser la MENOR tasa entre las admisibles
            adm = [c for c in po['candidatas']
                   if c['fidelidad_pesos'] >= po['umbral_fidelidad']]
            ok &= check(abs(min(c['tasa'] for c in adm) - po['tasa']) < 1e-9,
                        'T9', f'{nombre}: b* es la menor tasa admisible')
            # y no puede ser una celda degenerada
            ok &= check(list(po['b_estrella']) not in po['degeneradas'], 'T9',
                        f'{nombre}: b* no es una celda degenerada')
    # determinismo: dos llamadas dan lo mismo
    M = redes_de_prueba()['gaussiana_simetrica']
    a, b = punto_operativo([M], BITS_GRID, PRUNE_GRID), \
        punto_operativo([M], BITS_GRID, PRUNE_GRID)
    ok &= check(a['b_estrella'] == b['b_estrella'], 'T9', 'b* es determinista')
    return ok


def main():
    print('=' * 72)
    print('P-21 - BATERIA DEL INSTRUMENTO')
    print(f'esquema de cuantizacion: {ESQUEMA}')
    print('=' * 72)
    for fn in (T1_maxima_resolucion, T2_cero_representable, T3_poda_exacta,
               T4_monotonia_en_pesos, T4b_el_viejo_suspende,
               T5_guardian_por_red, T6_red_lineal_trivial,
               T7_listas_nominales, T8_banderas_aleatorizadas,
               T9_punto_operativo):
        fn()
    print('\n' + '=' * 72)
    if FALLOS:
        print(f'BATERIA EN ROJO - {len(FALLOS)} fallo(s):')
        for f in FALLOS:
            print(f'  - {f}')
        print('\nNO se calcula ninguna Psi ni se publica ninguna tabla de Delta.')
        return 1
    print('BATERIA EN VERDE - el instrumento puede usarse para medir.')
    print('Recuerda: el guardian por red (T5) se ejecuta ADEMAS antes de cada')
    print('Curva A, sobre la red real y el barrido concreto que se vaya a usar.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
