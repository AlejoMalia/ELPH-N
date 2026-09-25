import numpy as np
rng=np.random.default_rng(11)
# MATEMATICA antes de correr (TRIADA):
#  A = sqrt(Om_imp_MEDIANA / Om_acto) contesta "?estoy mas cerca que un impostor TIPICO?"
#  El contrato necesita "?estoy mas cerca que el impostor MAS CERCANO?"
#  PREDICCION: el minimo de k impostores BAJA con k, luego A no es un numero fijo:
#              depende de cuantos impostores dibujes. Un numero que depende de k no es una cota.
N=50; L=176.0
O = rng.uniform(12,188,(N,2))
def omega(A,B):
    from scipy.optimize import linear_sum_assignment
    D=np.hypot(*(A[:,None,:]-B[None,:,:]).T).T
    r,c=linear_sum_assignment(D); return float(np.median(D[r,c]))/L
acto = omega(O, O+rng.normal(0,0.141,O.shape))
print(f"  Om_acto = {acto:.6f}\n")
imp = np.array([omega(O, rng.uniform(O.min(0),O.max(0),O.shape)) for _ in range(2000)])
print(f"  {'k impostores':>14}  {'mediana':>10} {'MINIMO':>10}   {'A(mediana)':>11} {'A(minimo)':>10}")
for k in (32,100,1000,2000):
    s=imp[:k]
    print(f"  {k:>14}  {np.median(s):10.5f} {s.min():10.5f}   "
          f"{np.sqrt(np.median(s)/acto):11.1f} {np.sqrt(s.min()/acto):10.1f}")
# lo que hace Daugman: no un cociente, una TASA en la cola
mu,sd = imp.mean(), imp.std()
from math import erf,sqrt
far = 0.5*(1+erf((acto-mu)/(sd*sqrt(2))))
print(f"\n  impostor: media {mu:.5f}  sigma {sd:.5f}  ->  min observado {imp.min():.5f} ({(mu-imp.min())/sd:.1f} sigma)")
print(f"  TASA DE FALSA ACEPTACION  P(Om_imp <= Om_acto) = {far:.3e}   <- la cifra del gremio")
print(f"  d' de Daugman = |mu_imp - mu_acto| / sqrt((s_i^2+s_a^2)/2) ~ {(mu-acto)/sd:.1f}")
