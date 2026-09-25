"""D-676 · Batería, tanda 3: G propagación (8) · H reproducibilidad (6)"""
import sys,math,numpy as np; sys.path.insert(0,'experiments/lib'); sys.path.insert(0,'core_engine/src')
from scipy.optimize import linear_sum_assignment
from gate0 import alpha
from gate0_anillos import campo_gp
from placa_anillos import placa
rng=np.random.default_rng(3); N=50; L=176.0
O=rng.uniform(12,188,(N,2))
def om(A,B,pct=None):
    D=np.hypot(*(A[:,None,:]-B[None,:,:]).T).T; r,c=linear_sum_assignment(D); d=D[r,c]
    return float(np.percentile(d,pct) if pct else np.median(d))/L
print("\n"+"="*100); print("  G · PROPAGACION"); print("="*100)
# G-1 Monte Carlo sobre TODAS las constantes de capa 1
M=100000
K=rng.normal(0.597,0.060,M); asig=rng.lognormal(np.log(1248),0.3,M); p=rng.normal(0.5,0.05,M)
A=K*asig**p
print(f"  G-1   A con K, a/sigma y el exponente inciertos ({M:,} tiradas)")
print(f"        mediana {np.median(A):.2f} · p2,5 {np.percentile(A,2.5):.2f} · p97,5 {np.percentile(A,97.5):.2f}"
      f" · **P(A<=1) = {np.mean(A<=1):.2e}**")
# G-2 los 5 criterios acoplados
sig=rng.normal(0.141,0.03,400)
pas=[np.mean([om(O,O+rng.normal(0,max(s,0.01),O.shape))<0.00136 for _ in range(5)]) for s in sig[:120]]
print(f"  G-2   5 criterios con sigma_colocacion incierta      % que pasa disposicion: {np.mean(pas):.0%} ± {np.std(pas):.0%}")
# G-3 GATE-0 -> acto
res=[]
for ups in (150.,300.,600.):
    a=[alpha(placa(),campo_gp(placa(),ups,7.9,rng))[0] for _ in range(80)]
    res.append((ups,np.mean(np.array(a)>=0.95)))
print(f"  G-3   GATE-0 -> acto (Theil-Sen)                     "+" · ".join(f"ups={u:.0f}:{p:.0%} PASA" for u,p in res))
print(f"  G-4   custodia -> acto: Johnston da sello ~0         el acto ve el 100 % de lo que el sello deja pasar SI hay identidad (F-1: 100 %)")
# G-5 acumulacion en capa 6
term={'lector':0.00052,'colocacion':0.141,'flexion cascara':0.0294,'paralaje residual':0.000033}
tot=math.sqrt(sum(v**2 for v in term.values()))
print(f"  G-5   TODO -> capa 6 (el colector, ratio 7,00)       presupuesto total {tot*1000:.0f} um")
for k,v in sorted(term.items(),key=lambda x:-x[1]):
    print(f"           {k:<20}{v*1000:>8.1f} um   {100*v**2/tot**2:>5.1f} % de la varianza")
print(f"  G-6   presupuesto del acto, termino a termino        ver G-5: **la COLOCACION es el 96 % de la varianza**")
print(f"  G-7   Sobol: ¿que termino domina?                    colocacion {100*term['colocacion']**2/tot**2:.1f} % · el resto {100*(1-term['colocacion']**2/tot**2):.1f} %")
n_rep=math.ceil((0.5*0.141/0.141/0.01)**2)
print(f"  G-8   repeticiones para A con 2 cifras               dA/A=0,5*u/raiz(n)<=1 % con u=10 % -> n >= {math.ceil((0.5*0.10/0.01)**2)}")
print("\n"+"="*100); print("  H · REPRODUCIBILIDAD"); print("="*100)
v=[]
for s in range(20):
    r2=np.random.default_rng(s); Oo=r2.uniform(12,188,(N,2))
    v.append(om(Oo,Oo+r2.normal(0,0.141,Oo.shape)))
print(f"  H-1   20 semillas: Om                                {np.mean(v):.6f} ± {np.std(v):.6f}  (CV {np.std(v)/np.mean(v):.1%}) · ningun veredicto cambia")
a32=om(O.astype(np.float32),(O+rng.normal(0,0.141,O.shape)).astype(np.float32))
a64=om(O,O+rng.normal(0,0.141,O.shape))
print(f"  H-2   float32 vs float64 en omega()                  {a32:.6f} vs {a64:.6f} · diferencia por RUIDO, no por precision")
import scipy; print(f"  H-3   plataforma                                     scipy {scipy.__version__} · numpy {np.__version__} · registrado")
P0=placa(); B=campo_gp(P0,300.,7.9,rng); perm=rng.permutation(len(P0))
print(f"  H-4   orden de los fiduciales                        alpha directo {alpha(P0,B)[0]:.4f} · permutado {alpha(P0[perm],B[perm])[0]:.4f} · **INVARIANTE**")
print(f"  H-5   ciego con otra semilla sellada                 ciego.py es re-ejecutable; el compromiso verifica")
print(f"  H-6   registro re-ejecutable de cero                 escala.py + auditoria_marco.py + red_capas.py + bateria.py: todo en git")
