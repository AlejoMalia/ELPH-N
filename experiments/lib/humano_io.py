"""Cargador y simulador de los circuitos corticales humanos (H01 / Shapson-Coe).

Extraido de HUMANO/humano.py SIN ejecucion a nivel de modulo, para que otros
experimentos puedan importarlo sin repagar la corrida entera (misma razon que banco.py).
"""
import json
from pathlib import Path
import numpy as np, pandas as pd, scipy.sparse as sp
from banco import om, rho, rho_pot                                # noqa: F401
from instrumento import escala

RAIZ = Path(__file__).resolve().parent.parent
KK, SEEDS, CONTRATO, F, BITS = 200, 4, 0.05, 125, 3
CIRC = [('H4-h01-oficial', 'FF'), ('H4-h01-oficial', 'INF'),
        ('H4-h01-oficial', 'FB')]     # los unicos con signo POR ARISTA medido


def carga(exp, circ):
    m = json.loads((RAIZ/exp/'results'/'circuitos_meta.json').read_text())[circ]
    d = pd.read_csv(RAIZ/exp/'results'/f'{circ}.csv')
    nod = [int(x) for x in m['nodos']]; idx = {b: i for i, b in enumerate(nod)}
    pre = [int(x) for x in d.pre_root_id]; post = [int(x) for x in d.post_root_id]
    w = list(d[d.columns[2]])
    if 'signo' in d.columns:
        sg = np.array([-1.0 if int(x) == 1 else 1.0 for x in d.signo], np.float32)
    elif m.get('nt_por_nodo'):
        nt = {int(k): v for k, v in m['nt_por_nodo'].items()}
        # D-175 avisa de que el programa usa TRES definiciones de inhibicion distintas.
        # Aqui se aceptan las dos vocabularios que aparecen en el repositorio y se
        # DECLARA cual es cual. H2 usa 'inhibitorio_por_tipo'; no reconocerlo hacia que
        # todo saliera excitatorio (0,0 % de inhibicion) y que M1 y M2 salieran iguales.
        INH = ('gaba', 'glutamate', 'inhibitorio_por_tipo')
        sg = np.array([-1.0 if nt.get(int(a)) in INH else 1.0
                       for a in pre], np.float32)
    else:
        return None      # sin signo medido no se corre: no se inventa
    # los metadatos humanos NO congelan s0 (los de mosca si). Se usa la mediana y se
    # DECLARA: es la escala del tanh, y aqui no viene verificada por la puerta.
    s0 = float(m.get('s0', np.median(w)))
    return dict(nom=f'{circ}', n=len(nod), m=len(w), idx=idx, s0=s0,
                ia=np.fromiter((idx[a] for a in pre), int, len(w)),
                ib=np.fromiter((idx[b] for b in post), int, len(w)),
                sg=sg, mg=np.tanh(np.asarray(w, float)/s0).astype(np.float32),
                sen=np.array([idx[int(x)] for x in m['inyeccion'] if int(x) in idx]),
                rd=np.array([idx[int(x)] for x in m['lectura'] if int(x) in idx]),
                w=np.asarray(w, float))


def W_de(c, nivel, ent=None, mask=None, seed=3):
    rng = np.random.default_rng(700+seed)
    ia, ib, sg, mg = c['ia'], c['ib'], c['sg'], c['mg']
    if mask is not None:
        ia, ib, sg, mg = ia[mask], ib[mask], sg[mask], mg[mask]
    M = len(ia)
    if nivel == 0:
        r, cc = rng.integers(0, c['n'], M), rng.integers(0, c['n'], M)
        d = np.ones(M, np.float32)
    else:
        s_ = sg.copy()
        if nivel == 'ctrl':
            s_ = s_[rng.permutation(M)]; nivel = 2
        if nivel < 2:
            s_ = np.ones(M, np.float32)
        mag = mg if nivel >= 4 else 1.0
        d = (s_*mag).astype(np.float32)
        if ent is not None:
            d = np.where(ent, d, 1.0).astype(np.float32)
        r, cc = ib, ia
    W = sp.csr_matrix((d, (r, cc)), shape=(c['n'], c['n']), dtype=np.float32)
    g = 4.0/max(rho(W), 1e-9)
    return escala(W, g), g


def corre(c, tramos, st, gref, seed, mask=None):
    X = np.zeros((KK, c['n']), np.float32); r = np.random.default_rng(seed)
    for W, g, pasos in tramos:
        if pasos <= 0:
            continue
        U = np.zeros((KK, c['n']), np.float32); U[:, c['sen']] = st*g/gref
        for _ in range(pasos):
            dX = (-X + np.tanh((W @ X.T).T + U))*0.1
            dX += r.normal(0, 0.02*g, X.shape).astype(np.float32)*0.1
            X = X + dX
    return X[:, c['rd']]


