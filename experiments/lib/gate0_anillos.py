"""D-669 · GATE-0 SIMULADO: placa de anillos frente a rejilla, sobre campo GP.

  ESTO NO ES EL GATE-0. El GATE-0 son 25 EUR de banco y sigue en 0 %.
  Esto decide si la placa nueva mide mejor ANTES de cortarla.
"""
import sys, os, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../core_engine/src'))
sys.path.insert(0, os.path.dirname(__file__))
from gate0 import alpha, veredicto
from placa_anillos import placa

def campo_gp(P, ups, sigma_um, rng, nucleo='gauss'):
    """desplazamiento correlacionado: u(x) ~ GP con longitud de correlacion ups"""
    d = np.linalg.norm(P[:,None]-P[None,:], axis=2)
    C = np.exp(-(d/ups)**2) if nucleo=='gauss' else np.exp(-d/ups)
    L = np.linalg.cholesky(C + 1e-9*np.eye(len(P)))
    return P + (sigma_um*1e-3)*np.column_stack([L@rng.normal(size=len(P)) for _ in range(2)])

def rejilla():
    g = np.linspace(15., 185., 5); return np.array([[x,y] for x in g for y in g])

if __name__ == "__main__":
    rng = np.random.default_rng(5); T = 400; SIG = 7.9   # amplitud CNC nominal
    for ups in (300., 150.):
        print(f"\n  campo GP gaussiano, upsilon = {ups:.0f} mm, sigma_CNC = {SIG} um   ({T} realizaciones)")
        print(f"  {'placa':<16}{'pares':>7}{'alpha medido':>18}{'C (um)':>10}{'% PASA (>=0,95)':>18}")
        for nom, P in (("rejilla 5x5", rejilla()), ("5 anillos x 5", placa())):
            A=[];Cs=[]
            for _ in range(T):
                B = campo_gp(P, ups, SIG, rng)
                a,c,_,n = alpha(P,B)
                if np.isfinite(a): A.append(a); Cs.append(c*1e3)
            A=np.array(A)
            print(f"  {nom:<16}{n:>7}{np.mean(A):>12.3f} ± {np.std(A):.3f}"
                  f"{np.median(Cs):>10.1f}{100*np.mean(A>=0.95):>17.0f} %")
