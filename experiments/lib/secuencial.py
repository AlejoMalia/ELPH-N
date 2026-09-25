"""Parada temprana con el error controlado.

DOS reglas distintas, y confundirlas es el modo clasico de fabricar resultados:

  1. parar_por_precision()  -- mira SOLO el error estandar, nunca el resultado.
     Es SEGURA y no gasta nada: no puede sesgar la estimacion porque la decision
     de parar es independiente del valor estimado.

  2. FronteraOBF            -- mira el resultado para decidir si parar. Eso es
     'optional stopping'. Medido en simulacion, espiar 25 veces con alpha=0,05
     convierte el 5 % prometido en un 26-32 % de falsos positivos. La frontera
     de O'Brien-Fleming lo evita EXIGIENDO MAS al principio, de modo que el
     alpha global se conserva.

REGLA DEL PROGRAMA: la frontera se PREINSCRIBE antes de mirar ningun dato, igual
que b* se elige sin mirar ningun Psi. Calibrarla despues de ver resultados la
invalida por completo.
"""
import numpy as np

__all__ = ['parar_por_precision', 'FronteraOBF', 'calibrar_obf']


def parar_por_precision(muestras, se_objetivo, k_min=30, k_max=None):
    """Devuelve el K minimo con SE = sigma/sqrt(K) <= se_objetivo.

    No mira la media, solo la dispersion: por eso es segura sin gastar alpha.
    """
    x = np.asarray(muestras, dtype=float)
    if x.size < k_min:
        return None
    k_max = k_max or x.size
    for k in range(k_min, min(k_max, x.size) + 1):
        if x[:k].std(ddof=1) / np.sqrt(k) <= se_objetivo:
            return k
    return None


class FronteraOBF:
    """Frontera de grupo secuencial tipo O'Brien-Fleming.

        z_k > c * sqrt(K/k)

    Exigente al principio, ~normal al final. `c` se calibra por simulacion para
    el alpha global deseado y el numero de revisiones -- y se FIJA antes de mirar
    datos reales.
    """

    def __init__(self, K, revisiones=10, c=None, alpha=0.05):
        self.K = int(K)
        self.puntos = np.linspace(K // revisiones, K, revisiones).astype(int)
        self.c = float(c) if c is not None else calibrar_obf(K, revisiones, alpha)
        self.alpha = alpha

    def umbral(self, k):
        return self.c * np.sqrt(self.K / k)

    def cruza(self, muestras):
        """(parar, k, z) evaluando la frontera en cada revision alcanzada."""
        x = np.asarray(muestras, dtype=float)
        for k in self.puntos:
            if x.size < k:
                break
            s = x[:k].std(ddof=1)
            if s == 0:
                continue
            z = x[:k].mean() / (s / np.sqrt(k))
            if abs(z) > self.umbral(k):
                return True, int(k), float(z)
        return False, int(x.size), float('nan')

    def tabla(self):
        return [(int(k), float(self.umbral(k))) for k in self.puntos]


def calibrar_obf(K, revisiones=10, alpha=0.05, N=40000, seed=0):
    """Busca c tal que la probabilidad de cruzar bajo H0 sea alpha."""
    from scipy.optimize import brentq
    puntos = np.linspace(K // revisiones, K, revisiones).astype(int)
    cs = np.cumsum(np.random.default_rng(seed).standard_normal((N, K)), axis=1)

    def err(c):
        r = np.zeros(N, dtype=bool)
        for k in puntos:
            r |= np.abs(cs[:, k - 1] / np.sqrt(k)) > c * np.sqrt(K / k)
        return r.mean() - alpha

    return float(brentq(err, 1.2, 4.0, xtol=1e-3))
