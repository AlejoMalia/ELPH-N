"""D-666 · la cola del impostor MEDIDA, no extrapolada.  FAR <= 3/k (regla de tres)."""
import numpy as np, time
from scipy.optimize import linear_sum_assignment
rng=np.random.default_rng(11); N=50; L=176.0
O=rng.uniform(12,188,(N,2))
def omega(A,B):
    D=np.hypot(*(A[:,None,:]-B[None,:,:]).T).T
    r,c=linear_sum_assignment(D); return float(np.median(D[r,c]))/L
acto=omega(O,O+rng.normal(0,0.141,O.shape))
lo,hi=O.min(0),O.max(0); K=3_000_000
mn=np.inf; bajo=0; s=s2=0.0; t=time.time(); hist=[]
for i in range(K):
    om=omega(O, rng.uniform(lo,hi,O.shape))
    s+=om; s2+=om*om; mn=min(mn,om); bajo+= om<=acto
    if (i+1) in (32,2_000,100_000,1_000_000,3_000_000): hist.append((i+1,mn,bajo))
mu=s/K; sd=(s2/K-mu*mu)**.5
print(f"  Om_acto={acto:.6f}   impostor: media {mu:.5f} sigma {sd:.5f}   ({time.time()-t:.0f} s)\n")
print(f"  {'k':>10} {'min observado':>14} {'sigmas':>8} {'bajo el acto':>13} {'FAR afirmable':>15}")
for k,m,b in hist:
    print(f"  {k:>10} {m:>14.5f} {(mu-m)/sd:>8.1f} {b:>13} {'<= %.1e'%(3/k) if b==0 else '%.1e'%(b/k):>15}")
print(f"\n  d' = {(mu-acto)/sd:.1f}")
print(f"  el acto esta a {(mu-acto)/sd:.1f} sigma; el impostor mas cercano de 3e6, a {(mu-mn)/sd:.1f} sigma")
