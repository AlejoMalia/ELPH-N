"""La funcion del acto, unica para todo el programa (D-290).

Extraida de ACTO/code/acto_ref.py SIN ejecucion a nivel de modulo, para que T4 y lo que
venga corran LA MISMA tuberia y no otro camino de codigo. Cualquier cambio aqui cambia
T1, T2, T3 y T4 a la vez, que es exactamente lo que se quiere.

Aplica el procedimiento del contrato en orden (docs/CONTRATO-SISTEMA.md):
    1 suelo   2 H declarada ANTES del veredicto   3 c = Omega - suelo   4 suelo+c <= 0,05
con control de discriminacion (D-279) y la ventana de escritura GLOBAL (D-288).
"""
import numpy as np, scipy.sparse as sp
from banco import om, rho
from instrumento import escala as esc

SD, CONTRATO = 8, 0.05                                # 8 semillas (D-282)
BITS, P_LIB, N_RED, VENT = 6, 0.90, 16, 8             # HOJA v2 CONGELADA
MILO = (lambda G: -0.009107*G + 4.782321, 50.0, 225.0)


def sigma_lineal(d, dev):
    """sigma absoluto por arista: par diferencial sobre un modelo sigma_G(G) publicado."""
    f, gmin, gmax = dev; R = gmax-gmin
    wn = d/max(abs(d).max(), 1e-12)
    return np.sqrt(f(gmin+(1+wn)/2*R)**2 + f(gmin+(1-wn)/2*R)**2)/R*abs(d).max()


def acto(nom, n, ia, ib, d0, sen, rd, KK, ejes=('bits', 'disp', 'lib', 'vent'),
         sigma_fn=None, sesgo_fn=None):
    """sigma_fn(d) -> sigma absoluto por arista (por defecto, MILO).
    sesgo_fn(d) -> desplazamiento DETERMINISTA del peso (deriva media; SONOS la tiene)."""
    """Una reinstanciacion completa. Devuelve el procedimiento del contrato entero."""
    M = len(d0)

    def W_(d):
        A = sp.csr_matrix((d.astype(np.float32), (ib, ia)), shape=(n, n), dtype=np.float32)
        g = 4.0/max(rho(A), 1e-9)
        return esc(A, g), g

    A0, g0 = W_(d0)
    st = np.random.default_rng(0x5A17).normal(0, 1, (KK, len(sen))).astype(np.float32)*g0
    sB = np.random.default_rng(0xB0B).normal(0, 1, (KK, len(sen))).astype(np.float32)*g0

    def cor(A, g, ent, seed, hoja=False):
        X = np.zeros((KK, n), np.float32); r = np.random.default_rng(seed)
        U = np.zeros((KK, n), np.float32); U[:, sen] = ent*g/g0
        base = A.data.copy(); Ax = A.copy()
        for t in range(250):
            if hoja:
                fr = (min(1.0, (t+1)/VENT) if t < VENT else 1.0) if 'vent' in ejes else 1.0
                lb = (r.binomial(N_RED, P_LIB, A.nnz)/(N_RED*P_LIB)) if 'lib' in ejes else 1.0
                Ax.data = base*fr*lb                       # ventana GLOBAL (D-288)
            dX = (-X + np.tanh((Ax @ X.T).T + U))*0.1
            dX += r.normal(0, 0.02*g, X.shape).astype(np.float32)*0.1
            X = X + dX
        return X[:, rd]

    # --- 1 y 2 del procedimiento: suelo, y H DECLARADA ANTES del veredicto
    REF = [cor(A0, g0, st, 100+s) for s in range(SD)]
    suelo = float(np.mean([om(REF[s], cor(A0, g0, st, 500+s)) for s in range(SD)]))
    H = (CONTRATO-suelo)/CONTRATO
    disc = float(np.mean([om(REF[s], cor(A0, g0, sB, 500+s)) for s in range(SD)]))
    # --- el paquete pasa por la hoja
    d = d0.copy()
    if 'bits' in ejes:
        lo, hi = d.min(), d.max()
        d = lo + np.round((d-lo)/(hi-lo)*(2**BITS-1))/(2**BITS-1)*(hi-lo)
    sW = np.zeros(M)
    if 'disp' in ejes and (sigma_fn is not None or sesgo_fn is not None):
        if sesgo_fn is not None:
            d = sesgo_fn(d)                     # deriva MEDIA, deterministica
        sW = (sigma_fn(d) if sigma_fn is not None else np.zeros(M))/np.sqrt(N_RED)
    elif 'disp' in ejes:
        f, gmin, gmax = MILO; Rg = gmax-gmin
        wn = d/max(abs(d).max(), 1e-12)
        sW = np.sqrt(f(gmin+(1+wn)/2*Rg)**2+f(gmin+(1-wn)/2*Rg)**2)/Rg/np.sqrt(N_RED)*abs(d).max()
    vs = []
    for s in range(SD):
        Ah, gh = W_(d + np.random.default_rng(2200+s).normal(0, 1, M)*sW)
        vs.append(om(REF[s], cor(Ah, gh, st, 500+s, hoja=True)))
    omg = float(np.mean(vs))
    # --- 3 y 4 del procedimiento
    c = omg-suelo
    return dict(nom=nom, n=int(n), m=int(M), p=int(len(sen)), q=int(len(rd)),
                suelo=suelo, H=H, omega=omg, c=c, disc=disc,
                discrimina=bool(disc > 0.5),
                certifica=bool(suelo+c <= CONTRATO and disc > 0.5))
