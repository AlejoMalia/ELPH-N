"""Deteccion de trabajo cuyo resultado ya esta decidido antes de ejecutarlo.

La idea, del investigador: "reconocimiento de patrones de mate y proyeccion al
jaque". En ajedrez, 'mate en 3' no es una inferencia estadistica -- es una
DEMOSTRACION: se reconoce una estructura que fuerza el resultado, y no hace
falta jugar la partida.

Analogo exacto aqui: si dos puntos de una rejilla construyen el MISMO objeto con
la MISMA semilla, su Psi es identico bit a bit. No hay que simularlos.

DISTINCION IMPORTANTE frente a lib/secuencial.py:

  secuencial.py  mira resultados parciales -> es inferencia -> gasta alpha,
                 exige frontera PREINSCRITA (D-107).
  mate.py        mira la ESTRUCTURA antes de ejecutar -> es demostracion ->
                 no gasta nada y no toca el protocolo. Deduplicar calculos
                 identicos no cambia ningun resultado, solo evita repetirlo.

Por eso mate.py se puede aplicar a un experimento en vuelo y secuencial.py no.
"""
import hashlib
import numpy as np

__all__ = ['huella', 'agrupar_identicos', 'independientes_de', 'informe']


def huella(*objetos):
    """Hash estable de arrays/escalares. Misma huella => mismo objeto."""
    h = hashlib.blake2b(digest_size=16)
    for o in objetos:
        a = np.ascontiguousarray(np.asarray(o))
        h.update(str(a.dtype).encode())
        h.update(str(a.shape).encode())
        h.update(a.tobytes())
    return h.hexdigest()


def agrupar_identicos(constructor, rejilla):
    """Agrupa los puntos de `rejilla` que producen objetos identicos.

    `constructor(punto)` debe devolver el objeto (o tupla) que se simulara.
    Se ejecuta una vez por punto -- barato frente a simular.

    Devuelve {huella: [puntos...]}. Un grupo de tamano > 1 es un MATE: basta
    ejecutar uno y copiar el resultado a los demas.
    """
    grupos = {}
    for p in rejilla:
        grupos.setdefault(huella(*np.atleast_1d(constructor(p))), []).append(p)
    return grupos


def independientes_de(etapas, parametro):
    """Etapas cuyo resultado NO depende de `parametro`.

    `etapas` es {nombre: (parametros de los que depende)}. Si una etapa no
    depende del parametro que barre la rejilla, se calcula UNA vez y se
    reutiliza -- el ahorro grande suele estar aqui, no en las coincidencias
    numericas.
    """
    return [n for n, deps in etapas.items() if parametro not in deps]


def informe(etapas, parametro, n_valores, coste=None):
    """Cuenta cuanto de una rejilla es redundante. `coste` = {etapa: unidades}."""
    coste = coste or {n: 1 for n in etapas}
    fijas = independientes_de(etapas, parametro)
    c_fijo = sum(coste[n] for n in fijas)
    c_var = sum(coste[n] for n in etapas if n not in fijas)
    actual = n_valores * (c_fijo + c_var)
    minimo = c_fijo + n_valores * c_var
    return {'etapas_fijas': fijas,
            'coste_actual': actual, 'coste_minimo': minimo,
            'redundancia': 1 - minimo / actual if actual else 0.0}
