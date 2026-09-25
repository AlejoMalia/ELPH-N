"""Agregacion de horquillas entre tareas, SIN simular. Formulas del investigador.

  H_k        = max_t Delta_t(M_k) - min_t Delta_t(M_k)
  H_k^+-     propagacion a lo bruto del peor caso de los extremos
  h_k        = H_k / mediana_t Delta_t(M_k)     (comparable entre manifiestos)
  delta_pieza(t)                                (efecto de cada pieza por tarea)
  descomposicion tipo ANOVA: varianza entre tareas vs entre manifiestos

Todo sale del JSON. Cero computo.
"""
import numpy as np

__all__ = ['horquilla', 'horquilla_relativa', 'efecto_pieza',
           'orden_consistente', 'descomposicion', 'error_composicion']


def horquilla(deltas, sigmas=None, z=2.0):
    """H = max - min entre tareas, con propagacion de incertidumbre.

    Sin sigmas devuelve (H, nan, nan). Con sigmas devuelve el intervalo
    pesimista: el maximo empujado hacia arriba y el minimo hacia abajo, que es
    la cota superior de H, y la contraria para la inferior.
    """
    d = np.asarray(list(deltas), dtype=float)
    H = float(d.max() - d.min())
    if sigmas is None:
        return H, float('nan'), float('nan')
    s = np.asarray(list(sigmas), dtype=float)
    i_max, i_min = int(d.argmax()), int(d.argmin())
    H_sup = (d[i_max] + z * s[i_max]) - (d[i_min] - z * s[i_min])
    H_inf = max(0.0, (d[i_max] - z * s[i_max]) - (d[i_min] + z * s[i_min]))
    return H, float(H_inf), float(H_sup)


def horquilla_relativa(deltas, eps=1e-9):
    """h = H / mediana. Comparable entre manifiestos de escala distinta."""
    d = np.asarray(list(deltas), dtype=float)
    return float((d.max() - d.min()) / (np.median(d) + eps))


def efecto_pieza(delta_a, delta_b):
    """Cuanto cierra la pieza que separa dos manifiestos: Delta(a) - Delta(b)."""
    return float(delta_a - delta_b)


def orden_consistente(d1, d2, d3):
    """1 si Delta(M3) < Delta(M2) < Delta(M1) en esa tarea. P-20 midio que falla."""
    return bool(d3 < d2 < d1)


def descomposicion(matriz):
    """Varianza entre TAREAS frente a entre MANIFIESTOS (tipo ANOVA informal).

    `matriz[t][k]` = Delta de la tarea t con el manifiesto k.

    Si al anadir una pieza la varianza ENTRE TAREAS cae mucho, la horquilla era
    pobreza del manifiesto. Si casi no cae, es estructural a la tarea (R5).

    Devuelve (var_entre_tareas, var_entre_manifiestos, fraccion_tarea).
    NO es una identidad exacta: es descriptivo, y asi se declara.
    """
    M = np.asarray(matriz, dtype=float)          # filas tareas, columnas manif.
    v_t = float(np.mean(np.var(M, axis=0)))      # variacion entre tareas, a M fijo
    v_m = float(np.mean(np.var(M, axis=1)))      # variacion entre manifiestos
    return v_t, v_m, float(v_t / (v_t + v_m)) if (v_t + v_m) else float('nan')


def error_composicion(todo, partes, pesos=None):
    """Cuanto se pierde al estimar un circuito desde sus partes (D-133).

    Medido sobre la unica particion limpia que tenemos —los dos hemisferios del
    complejo central de MaleCNS, que reparten 319 nodos en 158 y 156 sin
    solape— con la **interfaz llevandose el 53,2 % de las aristas**:

    | manifiesto | todo | partes | error rel |
    |---|---:|---:|---:|
    | M0 aleatorio | 0,9601 | 0,9242 | 3,7 % |
    | **M1 topologia** | 1,1087 | 1,1072 | **0,1 %** |
    | **M2 + signo** | 0,0147 | 0,0458 | **211 %** |
    | CTRL barajado | 0,4528 | 0,4664 | 3,0 % |

    **M0, M1 y el control componen. Solo M2 falla — y falla mucho.**

    **Lectura mecanica:** M1 usa solo topologia, y partir el circuito no destruye
    su topologia efectiva. M2 anade el **signo**, y ahi la interfaz si aporta:
    **el todo reconstruye 3,1x mejor que sus partes.**

    > **La interfaz importa para el SIGNO, no para la topologia.** Partir un
    > sistema nervioso destruye informacion de signo que cruza la particion.

    **Consecuencia para A3:** un enfoque de «manifiestos locales + reglas de
    interfaz» **subestima la calidad alcanzable** si trata la interfaz como
    topologia. La regla de interfaz tiene que llevar **signo**, no solo quien
    conecta con quien.

    n = 1 particion. Es una hipotesis con un caso, no una ley.
    """
    p = np.asarray(list(partes), dtype=float)
    w = np.asarray(list(pesos), dtype=float) if pesos is not None else np.ones(len(p))
    est = float((p * w).sum() / w.sum())
    err = abs(est - float(todo))
    rel = err / abs(float(todo)) if todo else float('inf')
    return est, err, rel
