"""
METODOS OPERATIVOS DEL MARCO — formulas para calcular mas rapido, no para
sustituir la medida.

Todas son de MEDIDA, DISENO EXPERIMENTAL o PREDICCION LOCAL. Ninguna afirma
nada sobre dominios no medidos: eso lo prohibe la §7 de docs/MARCO.md.

  1  tasa(), envolvente(), b_estrella_adaptativo()   presupuesto
  2  regla_K()                                       cuantos estimulos
  3  rasgos_estructurales()                          proxy del efecto del signo
  4  admisible()                                     nivel 0 cuantificado
  5  delta_peor_caso()                               suficiencia sin elegir tarea

Autoprueba:  python3 lib/metodos.py
"""
import math
from collections import defaultdict

import numpy as np

# ---------------------------------------------------------------------------
# 1. PRESUPUESTO
# ---------------------------------------------------------------------------

def tasa(nnz, bits, n_aristas):
    """Bits por arista efectivos: entradas no nulas x profundidad / aristas."""
    return nnz * bits / n_aristas


def envolvente(puntos, menor_es_mejor=True):
    """Envolvente monotona por construccion sobre una familia de codificadores.

    puntos: [(tasa, valor), ...]. Devuelve [(tasa, envolvente)] ordenado.

    Es la magnitud correcta y el punto suelto NO lo es (D-100): comparar en una
    celda concreta mezcla lo que aporta la pieza con lo afortunado que sea ese
    codificador. La monotonia no se comprueba, se sigue del extremo.
    """
    o = sorted(puntos, key=lambda p: p[0])
    mejor = math.inf if menor_es_mejor else -math.inf
    out = []
    for r, v in o:
        mejor = min(mejor, v) if menor_es_mejor else max(mejor, v)
        out.append((r, mejor))
    return out


def b_estrella_adaptativo(fidelidad, tasa_de, bits_grid, prune_grid,
                          umbral=0.70, degeneradas=()):
    """b* con barrido ADAPTATIVO. Devuelve (b*, evaluaciones).

    `fidelidad(bits, poda) -> float`  y  `tasa_de(bits, poda) -> float`, ambas
    baratas: espacio de pesos, sin simular.

    Replica exactamente la regla de `instrumento.punto_operativo`: la celda de
    MENOR TASA con fidelidad >= umbral, excluidas las degeneradas, elegida SIN
    mirar ninguna Psi (§3.5 del marco).

    El ahorro viene de que la fidelidad DECRECE monotonamente con la poda a
    profundidad fija -- verificado sobre los 15 experimentos con candidatas
    guardadas. Eso permite biseccion en vez de evaluar las cuatro podas.

    Se usa la TASA REAL, no `bits x (1 - poda)`: la tasa depende de cuantas
    entradas NO NULAS sobreviven, que no es lo mismo que la fraccion podada.
    """
    ev = 0
    mejor, mejor_tasa = None, math.inf
    deg = set(map(tuple, degeneradas))
    for b in sorted(bits_grid):
        lo, hi, cand = 0, len(prune_grid) - 1, None
        while lo <= hi:                       # biseccion sobre la poda
            mid = (lo + hi) // 2
            p = prune_grid[mid]
            if (b, p) in deg:
                hi = mid - 1; continue
            ev += 1
            if fidelidad(b, p) >= umbral:
                cand = mid; lo = mid + 1      # cabe podar mas
            else:
                hi = mid - 1
        if cand is None:
            continue
        p = prune_grid[cand]
        r = tasa_de(b, p)
        if r < mejor_tasa:
            mejor, mejor_tasa = (b, p), r
    return mejor, ev


def fidelidad_decrece_con_poda(fidelidad, bits_grid, prune_grid):
    """Comprueba el supuesto que hace valida la biseccion. Si falla en algun
    experimento, la busqueda adaptativa NO es aplicable ahi y hay que barrer."""
    fallos = []
    for b in bits_grid:
        v = [fidelidad(b, p) for p in sorted(prune_grid)]
        for i in range(len(v) - 1):
            if v[i + 1] > v[i] + 1e-12:
                fallos.append((b, sorted(prune_grid)[i], sorted(prune_grid)[i + 1]))
    return (not fallos), fallos


# ---------------------------------------------------------------------------
# 2. CUANTOS ESTIMULOS — y por que no es 1/sqrt(K)
# ---------------------------------------------------------------------------

# MEDIDO en mosca CXinv, mismo circuito, mismas semillas, solo cambia K:
#     condicion        K=500     K=2000    factor
#     M1 (estable)     0.0061    0.0027     2.3x   <- coincide con 1/sqrt(K)
#     M2 (inestable)   0.0956    0.0031    30.7x   <- NO
#
# La sigma que mide C4 es DISPERSION ENTRE SEMILLAS, no error de la media. Hay
# dos regimenes:
#   estable    el ajuste (gw, gg) cae en la misma celda para todas las semillas
#              -> sigma la domina el ruido de estimacion de Psi ~ 1/sqrt(K)
#   inestable  el argmax salta de celda segun la semilla
#              -> sigma la domina ese salto, y COLAPSA al estabilizarse
#
# Por eso mas SEMILLAS no sirve y mas ESTIMULOS si (D-095).

REGIMEN_ESTABLE, REGIMEN_INESTABLE = 'estable', 'inestable'


def diagnosticar_regimen(sigmas_por_condicion, factor=5.0, sigma_relevante=0.009):
    """Que regimen domina, comparando cada condicion con LAS DEMAS.

    Cada condicion se compara con la MEDIANA DE LAS OTRAS, no con la mediana
    del conjunto. Con solo dos condiciones -- el caso de mosca y humano, que no
    tienen M3 -- la mediana del conjunto cae ENTRE los dos valores y ningun
    atipico puede superarla por `factor`. La validacion contra M-4 lo destapo:
    sigma(M1)=0,0061 y sigma(M2)=0,0956 se clasificaban como estables.

    `sigma_relevante` es un SUELO ABSOLUTO: una condicion con sigma muy por
    debajo del tope de C4 (0,03) no se marca aunque supere a las demas por el
    factor. La validacion lo destapo con raton FF, donde sigma(M1)=0,0006 es
    seis veces sigma(M2)=0,0001 y las dos son irrelevantes. Una razon alta
    entre numeros diminutos no es inestabilidad: es aritmetica.

    Devuelve (regimen, condiciones_inestables).
    """
    v = dict(sigmas_por_condicion)
    if len(v) < 2:
        return REGIMEN_ESTABLE, []
    malas = []
    for k, s in v.items():
        otras = [x for kk, x in v.items() if kk != k]
        ref = float(np.median(otras))
        if ref > 0 and s >= factor * ref and s >= sigma_relevante:
            malas.append(k)
    return (REGIMEN_INESTABLE if malas else REGIMEN_ESTABLE), sorted(malas)


def regla_K(K0, sigma0, sigma_obj, regimen=None, diagnostico=None):
    """Cuantos estimulos hacen falta. Devuelve (K, confianza).

    ACTUALIZADA (D-115). La version anterior solo distinguia ESTABLE/INESTABLE y
    aplicaba la potencia clasica. Los registros del programa muestran que sigma
    NO obedece una sola ley, sino TRES, y aplicar la clasica a las otras dos da
    consejo equivocado -- gastar 4x el computo sobre un suelo no sirve de nada.

    Medido en el unico par directo a dos K (M-4, CXinv, K 500 -> 2000):

      MUESTREO  M1:   0,0061 -> 0,0027   2,3x   (clasica predice 2,0x)  OK
      SUELO     M0:   0,0064 -> 0,0059   1,1x   -- mas K NO lo baja
                CTRL: 0,0348 -> 0,0265   1,3x
      FALLO     M2:   0,0956 -> 0,0031  30,7x   -- K lo cura, y de sobra

    Pasa `diagnostico` de diagnostico_sigma() cuando lo tengas: es lo que
    distingue los tres casos SIN simular. `regimen` se mantiene por
    compatibilidad con las llamadas antiguas.
    """
    if sigma_obj <= 0 or sigma0 <= 0:
        raise ValueError('sigmas deben ser positivas')
    clasico = K0 * (sigma0 / sigma_obj) ** 2

    if diagnostico == 'SUELO':
        return None, ('inutil: sigma tiene SUELO. Mas K no la baja. '
                      'Hay que rehacer el estimador, no gastar computo')
    if diagnostico == 'FALLO':
        # el unico caso medido se curo con 4x K0 y sobro por un factor 10
        return int(math.ceil(min(clasico, 4 * K0))), (
            'buena: firma de modo de fallo. 4x K0 basto en el unico caso '
            'medido (30,7x de caida donde la potencia predecia 2x)')
    if diagnostico == 'MUESTREO' or regimen == REGIMEN_ESTABLE:
        return int(math.ceil(clasico)), 'alta'
    return int(math.ceil(min(clasico, 4 * K0))), 'baja: extrapolacion no fiable'


def diagnostico_sigma(sigmas_por_parametro, sigmas_estables=(), umbral=0.03,
                      k_pares=None):
    """Decide si subir K arreglara una sigma que dispara C2. SIN simular la rejilla.

    TRES regimenes, medidos en el programa:

      MUESTREO  sigma ~ 1/sqrt(K).   M1 (M-4): 0,0061 -> 0,0027   2,3x
      SUELO     casi no baja.        M0: 1,1x · CTRL: 1,3x · **M4 (F-1): 1,00x**
      FALLO     se desploma.         M2 (M-4): 0,0956 -> 0,0031  30,7x

    CORRECCION D-119, aprendida a golpes: la **rugosidad sola no basta**. La
    version anterior clasificaba por lo erratica que fuera la serie y dio FALLO
    para M4 de F-1 (rugosidad 1,51 y 2,12). **Era SUELO**: subir K de 500 a 2000
    dejo sigma en **1,00x y 1,02x**, ni siquiera el 2,0x de la potencia clasica.
    Esa equivocacion costo 40 minutos de computo que no podian dar nada.

    **Sin sigma medida a DOS K distintas no hay diagnostico, solo sospecha.**
    Por eso ahora se devuelve INDETERMINADO y se exige un punto a otra K -- que
    es barato -- antes de comprometer la rejilla entera.

    `k_pares`  [(sigma, K), (sigma, K)] de la MISMA condicion a dos K distintas.

    Devuelve (diagnostico, rugosidad, nota).
    """
    v = np.asarray([x for x in sigmas_por_parametro if x is not None], dtype=float)
    if v.size < 3:
        return 'INDETERMINADO', float('nan'), 'hacen falta >= 3 puntos'
    rango = v.max() - v.min()
    if rango <= 0:
        return 'SUELO', 1.0, 'sigma constante: no depende del parametro'
    rug = float(np.abs(np.diff(v)).sum() / rango)
    if v.max() <= umbral:
        return 'SIN PROBLEMA', rug, f'ninguna sigma pasa de {umbral}'

    est = np.asarray(list(sigmas_estables), dtype=float) if len(sigmas_estables) else None
    contraste = ''
    if est is not None and est.size:
        contraste = (f'; condiciones sanas en los mismos puntos: '
                     f'{est.min():.4f}-{est.max():.4f}')

    if k_pares is None or len(k_pares) < 2:
        pista = ' (la rugosidad sugiere FALLO, pero no basta)' if rug >= 1.4 else ''
        return ('INDETERMINADO', rug,
                f'rugosidad {rug:.2f}{pista}. SIN sigma a dos K distintas no se '
                f'separa FALLO de SUELO. Correr UN punto a otra K antes de '
                f'comprometer la rejilla{contraste}')

    (s1, K1), (s2, K2) = sorted(k_pares, key=lambda x: x[1])[:2]
    razon = s1 / s2 if s2 else float('inf')
    esperado = (K2 / K1) ** 0.5
    if razon < 1.3:
        return ('SUELO', rug,
                f'sigma cayo {razon:.2f}x de K={K1} a K={K2} cuando la potencia '
                f'predecia {esperado:.1f}x. Mas K NO sirve: hay que rehacer el '
                f'ESTIMADOR{contraste}')
    if razon > 2 * esperado:
        return ('FALLO', rug,
                f'sigma cayo {razon:.1f}x, muy por encima del {esperado:.1f}x '
                f'clasico: modo de fallo que K cura{contraste}')
    return ('MUESTREO', rug,
            f'sigma cayo {razon:.2f}x, cerca del {esperado:.1f}x clasico: ruido '
            f'de muestreo. K = K0*(s/obj)^2{contraste}')


M_UNIVERSAL = 6.539          # IC 95% bootstrap: [5.27, 8.37] sobre 22 curvas
R_ESTRELLA_POR_ORGANISMO = {  # D-132: el contrato es constante del ORGANISMO
    'gusano': 2.16,           # n=8   ·  C. elegans
    'raton': 2.40,            # n=3   ·  MICrONS
    'mosca': 3.00,            # n=11  ·  FlyWire + MaleCNS
}
"""Usar R* del organismo predice la curva MEJOR (RMSE 0,136) que medir el del
propio circuito (0,1424): la mediana es menos ruidosa que una medida unica
cuantizada por la rejilla. Mezclar organismos empeora un 49 %."""
UMBRAL_D_ESTRELLA = 0.30     # D <= 0,30 define R*, la tasa de referencia


def ley_tasa_distorsion(R, R_estrella, m=M_UNIVERSAL):
    """Distorsion normalizada predicha, SIN simular (D-131).

        D(u) = 1 / (1 + u^m),   u = R / R*

    Derivada de las **22 curvas tasa-distorsion unicas** ya guardadas en el
    programa (58 ficheros, deduplicados). Cada `curva_a` tiene 20 celdas medidas
    y **de cada una solo se usaba un punto, b\***; la ley usa las 20.

    **Validacion dejando-una-curva-fuera: RMSE = 0,143** frente a 0,333 de
    predecir la media -- **2,3x mejor**. No es precisa; es util.

    **m = 6,5 significa ACANTILADO, no rampa:**

    | R / R* | calidad conservada |
    |---:|---:|
    | 0,50 | **1 %** |
    | 0,80 | 19 % |
    | 1,00 | 50 % |
    | 1,25 | 81 % |
    | 2,00 | **99 %** |

    **El manifiesto no se degrada suavemente.** Por debajo de 0,8 R* no queda
    casi nada; por encima de 1,25 R*, casi todo. Eso tiene una consecuencia de
    diseno: **no hay «version economica» util de un manifiesto.** O se paga la
    tasa o no se obtiene funcion.

    Uso: con UNA medida (R*) se predice la curva entera, sustituyendo 19 celdas
    simuladas por un numero.
    """
    u = np.asarray(R, dtype=float) / float(R_estrella)
    return 1.0 / (1.0 + u ** m)


def tasa_para_distorsion(D_objetivo, R_estrella, m=M_UNIVERSAL):
    """Inversa: que tasa hace falta para una distorsion dada. R = R* (1/D - 1)^(1/m)."""
    D = float(D_objetivo)
    if not 0 < D < 1:
        raise ValueError('D debe estar en (0, 1)')
    return float(R_estrella) * (1.0 / D - 1.0) ** (1.0 / m)


def psi_desde_fidelidad(F):
    """Fidelidad funcional predicha desde la fidelidad ESTRUCTURAL (D-142).

        Psi ~= F

    **Cero parametros.** Sobre **426 pares (F, Psi)** de 22 circuitos y 3
    organismos, cruzando por primera vez las dos superficies que el programa
    guardaba por separado:

    | modelo | RMSE | parametros |
    |---|---:|---|
    | **Psi = F** | **0,1263** | **ninguno** |
    | Psi = a·F + b | 0,1257 | 2 (a = 0,974, b = +0,030) |
    | Psi = F^k | 0,1268 | 1 (k = 1,019) |
    | predecir la media | 0,2244 | — |

    **La identidad es tan buena como cualquier ajuste.** Sesgo +0,011. Por
    organismo: gusano 0,0996 · mosca 0,1445 · raton 0,1170.

    **Por que importa:** F es lo que un escaner o un ensamblador **entrega
    fisicamente** —fidelidad en espacio de pesos—; Psi es lo que **funciona**.
    Que sean iguales significa:

    > **La funcion se puede predecir desde la estructura, sin simular.** Un
    > proceso que entregue fidelidad de pesos F producira fidelidad funcional
    > ~F.

    Eso conecta las especificaciones fisicas de las Fases VII-VIII con el
    resultado funcional, que es el puente que al programa le faltaba.

    **DOMINIO (D-147): vale para ELIMINAR, no para CORROMPER.**

    | familia de error | ¿vale Psi = F? |
    |---|---|
    | cuantizacion, poda, deteccion, colocacion | **SI** — 426 pares, RMSE 0,126 |
    | **corrupcion de signo** | **NO** — a 3,2 % de error, F = 0,66 y Psi = 0,95 |

    Invertir el signo de una arista la mueve **2w** en espacio de pesos frente a
    **w** de omitirla, y Frobenius eleva al cuadrado: **4x por arista**. Pero
    **la red compensa funcionalmente**, asi que **F sobrepenaliza el error de
    signo**. Para el signo, usar su propia sensibilidad (D-136: dDelta/de = 1,571).
    """
    return float(F)


def coste_experimento(n_sims, K, n_aristas, obreros=1, nstep=250):
    """Horas de reloj que costara, ANTES de lanzarlo.

    Calibrada con los dos experimentos completos de esta noche, medidos con
    reloj y no estimados (que fallaron tres veces seguidas):

      F-1  gusano  448 nodos  7.379 aristas  3.930 sim x K=500   -> 50 min/punto
      M-7  mosca   319 nodos  5.157 aristas  2.490 sim x K=2000  -> 58 min/punto

    Modelo fisico: cada simulacion son `nstep` productos matriz-vector sobre la
    matriz dispersa, por cada uno de los K estimulos. Luego

        coste ~ n_sims * K * nstep * n_aristas

    La constante sale de esos dos puntos. HONESTIDAD SOBRE SU PRECISION: los
    dos dan constantes que difieren 1,5x, asi que la prediccion vale +-25 %.
    El modelo simplifica -- la mayoria de simulaciones del Equipo B usan
    NSTEP_FIT=100, no 250 -- y con dos puntos no se puede afinar mas.

    Aun asi es mucho mejor que estimar a ojo: esta noche estime el mismo punto
    de F-1 en 20 min, luego 50, luego 4 h. La formula da +-25 %.
    """
    C = 1.860e-13          # horas por (sim * K * paso * arista), medido
    horas = C * n_sims * K * nstep * n_aristas
    return horas / max(1, obreros)


# ---------------------------------------------------------------------------
# 3. PROXY DEL EFECTO DEL SIGNO — rasgos del grafo, sin simular
# ---------------------------------------------------------------------------

def rasgos_estructurales(pre, post, inhibitorios, nodos):
    """Rasgos calculables del grafo, SIN ejecutar el pipeline.

    Es la situacion de un dominio nuevo: se tiene el grafo y se quiere decidir
    si merece la pena medirlo.

    MEDIDO (PROY, dejando-uno-fuera): la fraccion de ARISTAS con presinaptico
    inhibitorio predice el efecto del signo a 0,50x la linea base, mientras que
    la fraccion de NODOS inhibitorios es PEOR que predecir la media.
    No es cuantas inhibitorias hay: es cuanto cableado poseen.
    """
    n, m = len(nodos), len(pre)
    inh = set(inhibitorios)
    aristas = set(zip(pre, post))
    outd, ind = defaultdict(int), defaultdict(int)
    for a, b in zip(pre, post):
        outd[a] += 1; ind[b] += 1
    grados = np.array([outd[x] + ind[x] for x in nodos], dtype=float)
    g_inh = np.array([outd[x] + ind[x] for x in nodos if x in inh], dtype=float)
    return {
        'N': n, 'aristas': m, 'densidad': m / (n * n),
        'grado_medio': float(grados.mean()) if n else 0.0,
        'pct_nodos_inhib': 100.0 * len(inh & set(nodos)) / n if n else 0.0,
        'pct_aristas_inhib': 100.0 * sum(1 for p in pre if p in inh) / max(1, m),
        'reciprocidad': 100.0 * sum(1 for a, b in aristas
                                    if (b, a) in aristas) / max(1, len(aristas)),
        'concentracion_inhib': (float(g_inh.mean() / grados.mean())
                                if len(g_inh) and grados.mean() else 0.0),
    }


# ---------------------------------------------------------------------------
# 4. NIVEL 0 CUANTIFICADO
# ---------------------------------------------------------------------------

def admisible(n_iny, n_lec, vias_directas, pct_aristas_inhib, cobertura,
              n_min=4, vias_min=10, inhib_min=1.0, inhib_max=99.0):
    """Nivel 0 como funcion. Coste: microsegundos. Ahorro: corridas enteras.

    Cada criterio existe porque algo se rompio por el:
      n_min          canales vacios o de un solo elemento
      vias_min       T0 de E-2/E-3 tiene CERO vias directas: la senal debe
                     atravesar la red entera. No se prohibe -- se CLASIFICA
                     aparte, porque no es comparable con las demas
      inhib_min      Pinky100: el signo presente SIN VARIANZA (D-072) y los
                     circuitos de gusano con %I = 0 (D-089)
      cobertura      D-050: 15 de 26 nombres no coincidian, en silencio
    """
    fallos = []
    if n_iny < n_min: fallos.append(f'inyeccion {n_iny} < {n_min}')
    if n_lec < n_min: fallos.append(f'lectura {n_lec} < {n_min}')
    if not (inhib_min <= pct_aristas_inhib <= inhib_max):
        fallos.append(f'aristas inhibitorias {pct_aristas_inhib:.1f} % fuera '
                      f'de [{inhib_min}, {inhib_max}]: el signo no es testeable')
    if cobertura < 100.0:
        fallos.append(f'cobertura nominal {cobertura:.1f} % < 100 %')
    clase = ('directa' if vias_directas >= vias_min else
             'sin_via_directa' if vias_directas == 0 else 'via_debil')
    return {'admisible': not fallos, 'fallos': fallos, 'clase_via': clase,
            'comparable_con_directas': clase == 'directa'}


# ---------------------------------------------------------------------------
# 5. SUFICIENCIA SIN ELEGIR TAREA
# ---------------------------------------------------------------------------

def delta_peor_caso(deltas_por_tarea, excluidas=()):
    """Delta^wc(M) = max sobre tareas. La suficiencia se reporta ASI, no en una
    tarea elegida a mano.

    `deltas_por_tarea`: {tarea: {manifiesto: delta}}. `excluidas`: tareas
    invalidadas, que se declaran y no se promedian.
    """
    tareas = [t for t in deltas_por_tarea if t not in excluidas]
    if not tareas:
        raise ValueError('todas las tareas excluidas')
    mani = set().union(*(deltas_por_tarea[t].keys() for t in tareas))
    wc = {M: max(deltas_por_tarea[t][M] for t in tareas
                 if M in deltas_por_tarea[t]) for M in mani}
    peor = {M: max(tareas, key=lambda t: deltas_por_tarea[t].get(M, -math.inf))
            for M in mani}
    return {'delta_wc': wc, 'tarea_peor': peor, 'tareas_usadas': sorted(tareas),
            'excluidas': sorted(excluidas)}


# ---------------------------------------------------------------------------

def _autoprueba():
    ok = True
    def chk(c, m):
        nonlocal ok
        print(f'  [{"PASA " if c else "FALLA"}] {m}'); ok &= bool(c)

    print('1. ENVOLVENTE')
    e = envolvente([(3, 0.5), (1, 0.4), (2, 0.9), (4, 0.2)])
    chk([v for _, v in e] == sorted([v for _, v in e], reverse=True),
        f'monotona no creciente por construccion: {[round(v,2) for _,v in e]}')
    chk(e[0] == (1, 0.4), 'el punto de menor tasa se conserva')

    print('\n2. b* ADAPTATIVO')
    fid = lambda b, p: min(1.0, b / 8.0) * (1 - p)      # decrece con la poda
    tas = lambda b, p: b * (1 - p)
    bg, pg = (32, 8, 5, 4, 3), (0.0, 0.20, 0.35, 0.50)
    b, ev = b_estrella_adaptativo(fid, tas, bg, pg, 0.70)
    chk(b is not None, f'encuentra b* = {b}')
    chk(ev < len(bg) * len(pg), f'{ev} evaluaciones frente a {len(bg)*len(pg)} '
        f'de la rejilla entera')

    print('\n3. REGIMEN Y REGLA DE K')
    r, malas = diagnosticar_regimen({'M1': 0.0061, 'M2': 0.0956})
    chk(r == REGIMEN_INESTABLE and malas == ['M2'],
        f'caza M-4 con SOLO DOS condiciones (mosca no tiene M3): {r} {malas}')
    r2, _ = diagnosticar_regimen({'M1': 0.0027, 'M2': 0.0031})
    chk(r2 == REGIMEN_ESTABLE, 'y no dispara con M-4b, ya estabilizado')
    r3, _ = diagnosticar_regimen({'M1': 0.0006, 'M2': 0.0001})
    chk(r3 == REGIMEN_ESTABLE,
        'ni con raton FF: razon 6x entre cifras irrelevantes NO es inestabilidad')
    K, c = regla_K(500, 0.0956, 0.03, REGIMEN_INESTABLE)
    chk(c.startswith('baja'), f'marca confianza baja en regimen inestable (K={K})')
    K2, c2 = regla_K(500, 0.0061, 0.003, REGIMEN_ESTABLE)
    chk(c2 == 'alta' and K2 > 500, f'regla clasica en estable: K={K2}')

    print('\n4. ADMISIBLE')
    a = admisible(20, 50, 0, 5.0, 100.0)
    chk(a['clase_via'] == 'sin_via_directa',
        'clasifica T0 aparte por tener cero vias directas')
    b_ = admisible(8, 26, 4, 0.0, 100.0)
    chk(not b_['admisible'], 'rechaza %I = 0 (Pinky100 / gusano)')
    c_ = admisible(6, 8, 12, 5.2, 78.9)
    chk(not c_['admisible'], 'rechaza cobertura nominal < 100 % (D-050)')

    print('\n5. PEOR CASO')
    w = delta_peor_caso({'T1': {'M1': .5, 'M2': .2}, 'T2': {'M1': .7, 'M2': .1}},
                        excluidas=())
    chk(w['delta_wc'] == {'M1': .7, 'M2': .2}, f"peor caso: {w['delta_wc']}")
    chk(w['tarea_peor']['M1'] == 'T2', 'identifica la tarea que manda')

    print('\n' + ('METODOS EN VERDE' if ok else 'HAY FALLOS'))
    return 0 if ok else 1


if __name__ == '__main__':
    raise SystemExit(_autoprueba())
