"""Banco de simulacion fisica. SIN ejecucion al importar.

Extraido de payload_especies.py, que se ejecutaba entero al importarlo: 60 s por
script. Con cuatro corridas en paralelo eran 4 minutos tirados. Regla del programa:
cada experimento debe dejar el siguiente mas barato.
"""
import json, math
from pathlib import Path
import numpy as np, pandas as pd, scipy.sparse as sp

RAIZ = Path(__file__).resolve().parent.parent
META = RAIZ / 'M4-tarea-invertida' / 'results'
INH = ('gaba', 'glutamate')
SIGMA = 0.02


def rho(W):
    """Autovalor dominante EXACTO (ARPACK). Es el que hay que usar.

    D-228: rho_pot arranca de un vector aleatorio con semilla fija EN ORDEN DE NODO, asi
    que NO es invariante al reetiquetado (sd 0,43-2,87 % entre permutaciones) y ademas
    va sesgado -2,4 % a +3,1 % frente al autovalor exacto. Como rho fija g = 4/rho -- el
    punto de operacion de todo el programa -- eso mueve Omega hasta 0,0044, que es 3,4x
    su propio ruido. Esta version tiene sd 3,6e-12 entre reetiquetados.
    """
    import scipy.sparse.linalg as _sl
    W = sp.csr_matrix(W).astype(np.float64)
    if W.shape[0] < 3 or W.nnz == 0:
        return float(abs(np.linalg.eigvals(W.toarray())).max()) if W.nnz else 0.0
    try:
        return float(abs(_sl.eigs(W, k=1, which='LM', return_eigenvectors=False,
                                  maxiter=20000, tol=1e-10)[0]))
    except Exception:
        return rho_pot(W)          # si ARPACK no converge, se declara y se sigue


def rho_pot(W, it=250):
    """OBSOLETO -- no invariante al reetiquetado y sesgado. Ver rho() y D-228.
    Se conserva sin tocar para poder reproducir los resultados anteriores a D-228."""
    x = np.random.default_rng(7).normal(0, 1, W.shape[0]).astype(np.float32)
    x /= np.linalg.norm(x); lam = 0.0
    for _ in range(it):
        y = W @ x; n = np.linalg.norm(y)
        if n < 1e-20:
            return 0.0
        x = y / n; lam = n
    return float(lam)


def om(a, b):
    x, y = a.ravel(), b.ravel()
    return 1.0 if x.std() < 1e-9 or y.std() < 1e-9 else 1 - float(np.corrcoef(x, y)[0, 1])


class Banco:
    """Un circuito con su tarea, listo para escribir por etapas."""

    def __init__(self, nombre='CXladoL_dir', n_iny=None):
        m_ = json.loads((META / 'circuitos_meta.json').read_text())[nombre]
        d = pd.read_csv(META / f'{nombre}.csv')
        nt = {int(k): v for k, v in m_['nt_por_nodo'].items()}
        self.nod = [int(x) for x in m_['nodos']]
        self.idx = {b: i for i, b in enumerate(self.nod)}
        self.n = len(self.nod)
        self.S0 = m_['s0']
        pre, post, w = list(d.pre_root_id), list(d.post_root_id), list(d.syn_count)
        self.m = len(w)
        self.ia = np.fromiter((self.idx[int(a)] for a in pre), int, self.m)
        self.ib = np.fromiter((self.idx[int(b)] for b in post), int, self.m)
        self.sg = np.array([-1.0 if nt.get(int(a)) in INH else 1.0 for a in pre],
                           np.float32)
        self.mg = np.tanh(np.asarray(w, float) / self.S0).astype(np.float32)
        iny = [int(x) for x in m_['inyeccion'] if int(x) in self.idx]
        if n_iny:
            iny = iny[:n_iny]
        self.sen = np.array([self.idx[b] for b in iny])
        self.rd = np.array([self.idx[b] for b in m_['lectura']
                            if int(x := b) in self.idx])
        self._Wf, self.gf = self.W(np.ones(self.m, bool))
        self._orden = None
        self._dist = None

    def W(self, ent, mask=None):
        d = np.where(ent, self.sg * self.mg, 1.0).astype(np.float32)
        ia, ib = self.ia, self.ib
        if mask is not None:
            d, ia, ib = d[mask], ia[mask], ib[mask]
        W = sp.csr_matrix((d, (ib, ia)), shape=(self.n, self.n), dtype=np.float32)
        g = 4.0 / max(rho_pot(W), 1e-9)
        from instrumento import escala
        return escala(W, g), g

    def estimulo(self, K=200, semilla=0x5A17):
        return (np.random.default_rng(semilla).normal(0, 1, (K, len(self.sen)))
                .astype(np.float32) * self.gf)

    def corre(self, tramos, st, seed, mask=None):
        K = st.shape[0]
        X = np.zeros((K, self.n), np.float32); r = np.random.default_rng(seed)
        for ent, pasos in tramos:
            if pasos <= 0:
                continue
            W, g = self.W(ent, mask)
            U = np.zeros((K, self.n), np.float32); U[:, self.sen] = st * g / self.gf
            for _ in range(pasos):
                dX = (-X + np.tanh((W @ X.T).T + U)) * 0.1
                dX += r.normal(0, SIGMA*g, X.shape).astype(np.float32) * 0.1
                X = X + dX
        return X[:, self.rd]

    def referencia(self, st, semillas=4, pasos=250, mask=None):
        return [self.corre([(np.ones(self.m, bool), pasos)], st, 100+s, mask)
                for s in range(semillas)]

    def orden_localidad(self):
        """orden BFS desde el nodo de mayor grado (R10)."""
        if self._orden is None:
            gr = np.zeros(self.n, int)
            for a, b in zip(self.ia, self.ib):
                gr[a] += 1; gr[b] += 1
            U = sp.csr_matrix((np.ones(self.m), (self.ia, self.ib)),
                              shape=(self.n, self.n)); U = U + U.T
            bfs = sp.csgraph.breadth_first_order(U, int(np.argmax(gr)),
                                                 directed=False,
                                                 return_predecessors=False)
            pos = np.full(self.n, self.n, int)
            for i, v in enumerate(bfs):
                pos[v] = i
            self._orden = np.argsort(np.maximum(pos[self.ia], pos[self.ib]),
                                     kind='stable')
        return self._orden

    def dist_inyeccion(self):
        if self._dist is None:
            A = sp.csr_matrix((np.ones(self.m), (self.ia, self.ib)),
                              shape=(self.n, self.n))
            self._dist = np.min(sp.csgraph.shortest_path(
                A, method='D', unweighted=True, indices=self.sen), axis=0)
        return self._dist
