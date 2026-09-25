"""Cache compartida entre obreros para el trabajo que MATE demuestra identico.

MOTIVACION (idea del investigador, D-113): en un pool, cada obrero es un
proceso aparte y recalcula TODO desde cero. Cuando D-108 demuestra que una
etapa no depende del parametro barrido, los N obreros calculan N veces el
mismo objeto, bit a bit. En F-1 eso era el 75 % del coste.

  D-108 (mate.py)      DETECTA que el trabajo es redundante.
  D-113 (compartir.py) LO EVITA: el primero calcula, los demas leen.

EL PELIGRO, y por que la clave es un hash y no un nombre:

  Una cache mal indexada es el peor fallo posible en este programa: devuelve
  numeros plausibles y silenciosos. Ya llevamos siete fallos de instrumento y
  los que mas dano hicieron fueron los CALLADOS (D-092, D-106).

  Por eso la clave es el hash de TODO de lo que depende el objeto: tarea, K,
  semillas, el grafo entero y el CODIGO FUENTE de las funciones implicadas.
  Si cambia cualquier cosa, la clave cambia y la cache falla en frio. No hay
  invalidacion manual que se pueda olvidar.

USO:
    from compartir import cache_compartida
    curva, conds = cache_compartida(
        clave_de=[TAREA, K_STIM, N_SEEDS, aristas, inspect.getsource(curva_a)],
        calcular=lambda: (curva_a(), condiciones_fijas()),
        dir_cache=RESULTS / '.compartido')
"""
import hashlib
import os
import pickle
import time
from pathlib import Path

import numpy as np

__all__ = ['huella_de', 'cache_compartida']

ESPERA_MAX = 3600.0        # s. Si el que calcula muere, el resto no se cuelga.


def huella_de(partes):
    """Hash estable de una lista heterogenea (str, num, array, DataFrame)."""
    h = hashlib.blake2b(digest_size=20)
    for p in partes:
        if hasattr(p, 'values'):                 # DataFrame / Series
            p = p.values
        if isinstance(p, np.ndarray):
            a = np.ascontiguousarray(p)
            h.update(str(a.dtype).encode()); h.update(str(a.shape).encode())
            h.update(a.tobytes())
        else:
            h.update(repr(p).encode())
        h.update(b'|')
    return h.hexdigest()


def cache_compartida(clave_de, calcular, dir_cache, etiqueta='compartido',
                     verificar=False):
    """Devuelve calcular(), calculandolo UNA sola vez entre todos los obreros.

    `clave_de`   lista con TODO de lo que depende el resultado. Debe incluir el
                 codigo fuente de las funciones (inspect.getsource): si el
                 calculo cambia, la clave cambia.
    `verificar`  recalcula aunque haya cache y comprueba que coincide bit a
                 bit. Se usa la primera vez que un experimento la estrena.

    El reparto usa mkdir, atomico en POSIX: exactamente un obrero calcula; el
    resto espera y lee. Si el que calcula muere, el cerrojo caduca y otro
    lo intenta -- nadie se queda colgado para siempre.
    """
    dir_cache = Path(dir_cache); dir_cache.mkdir(parents=True, exist_ok=True)
    k = huella_de(clave_de)
    fich = dir_cache / f'{etiqueta}_{k}.pkl'
    lock = dir_cache / f'{etiqueta}_{k}.lock'

    if fich.exists() and not verificar:
        with open(fich, 'rb') as f:
            return pickle.load(f)

    try:
        os.mkdir(lock)
    except FileExistsError:
        t0 = time.time()
        while time.time() - t0 < ESPERA_MAX:
            if fich.exists():
                with open(fich, 'rb') as f:
                    return pickle.load(f)
            if not lock.exists():                # el que calculaba murio
                return cache_compartida(clave_de, calcular, dir_cache,
                                        etiqueta, verificar)
            time.sleep(2.0)
        raise TimeoutError(f'{etiqueta}: espera de cache agotada ({ESPERA_MAX}s)')

    try:
        val = calcular()
        if verificar and fich.exists():
            with open(fich, 'rb') as f:
                prev = pickle.load(f)
            if huella_de([repr(prev)]) != huella_de([repr(val)]):
                raise AssertionError(
                    f'{etiqueta}: la cache NO reproduce el calculo. '
                    f'La clave no captura alguna dependencia.')
        tmp = fich.with_suffix('.tmp')
        with open(tmp, 'wb') as f:
            pickle.dump(val, f)
        os.replace(tmp, fich)                    # publicacion atomica
        return val
    finally:
        try:
            os.rmdir(lock)
        except OSError:
            pass
