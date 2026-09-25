"""D-676 · Batería, tanda 2: B ruptura (7) · D frontera (10) · F control negativo (9) + A-7, A-16"""
import sys, math, numpy as np; sys.path.insert(0,'experiments/lib'); sys.path.insert(0,'core_engine/src')
from scipy.optimize import linear_sum_assignment
from scipy.stats import theilslopes
from gate0 import alpha
from gate0_anillos import campo_gp
from placa_anillos import placa
rng=np.random.default_rng(11); N=50; L=176.0; SIG=0.141
O=rng.uniform(12,188,(N,2)); DIAM=np.linspace(6.,18.,N)
def om(A,B,pct=None):
    D=np.hypot(*(A[:,None,:]-B[None,:,:]).T).T; r,c=linear_sum_assignment(D); d=D[r,c]
    return float(np.percentile(d,pct) if pct else np.median(d))/L
def acto(s=SIG): return O+rng.normal(0,s,O.shape)
SUELO=np.median([om(O,acto()) for _ in range(30)]); SUELO98=np.median([om(O,acto(),98) for _ in range(30)])
AL=[]; F=[]
def P(n,t,r,f=""):
    print(f"  {n:<6}{t:<50}{r}")
    if f=="!": AL.append((n,t,r))
    if f=="*": F.append((n,t,r))
print(f"\n  suelo mediana {SUELO:.6f} · suelo p98 {SUELO98:.6f}")
print("\n"+"="*104); print("  B · RUPTURA"); print("="*104)
def detecta(est,frac,despl=1.0,T=120):
    k=max(1,int(round(frac*N))); hits=0
    for _ in range(T):
        B=acto(); B[rng.choice(N,k,False)]+=despl
        v=om(O,B,98 if est=='p98' else None)
        u=(SUELO98 if est=='p98' else SUELO)*(1+ (3*0.1*math.sqrt(2)))
        hits+= v>u
    return hits/T
for est,lab in (('med','mediana de Om'),('p98','p98 del inventario')):
    r=" · ".join(f"{f:.0%}:{detecta(est,f):.0%}" for f in (0.02,0.10,0.30,0.50,0.70))
    P(f"B-{1 if est=='med' else 2}",f"{lab}: P(detectar) vs fraccion contaminada (1 mm)",r,
      "!" if est=='med' and detecta('med',0.30)<0.5 else "")
P("B-3","max de identidad: 1 unidad basta",f"ruptura 1/n = {1/N:.2%}; detecta 1 de 50 por construccion")
P("B-4","ciego SHA-256 con p_defecto conocido","el compromiso fija la SEMILLA: conocer p no da la tirada. Resiste")
mal=[]
for frac in (0.04,0.10,0.20,0.29,0.40):
    a=[]
    for _ in range(60):
        P0=placa(); B=campo_gp(P0,300.,7.9,rng)
        idx=rng.choice(len(P0),max(1,int(frac*len(P0))),False); B[idx]+=rng.normal(0,0.5,(len(idx),2))
        a.append(alpha(P0,B)[0])
    mal.append((frac,np.mean(a)))
P("B-5","Theil-Sen en alpha vs fraccion de pares malos"," · ".join(f"{f:.0%}:{v:.3f}" for f,v in mal),"*")
err=[]
for s in (0.5,2.,5.,10.):
    B=O+rng.normal(0,s,O.shape); D=np.hypot(*(O[:,None,:]-B[None,:,:]).T).T
    _,c=linear_sum_assignment(D); err.append((s,(c!=np.arange(N)).mean()))
P("B-6","asignacion optima: % mal emparejado vs ruido"," · ".join(f"{s:.1f}mm:{e:.0%}" for s,e in err),"!" if err[-1][1]>0.1 else "")
P("B-7","paralaje: 1 diametro mal leido en 1 mm",f"altura mal {1/2:.1f} mm -> error radial {100*0.5/1500*1000:.1f} um en r=100")
print("\n"+"="*104); print("  D · FRONTERA"); print("="*104)
P("D-2","delta = K*disp*raiz(2): ¿por que raiz(2)?","dos medidas independientes (origen y destino) -> var se suma -> raiz(2). DERIVADO, correcto")
cur=[(d,np.mean([om(O,np.where((np.arange(N)==0)[:,None],acto()+d,acto()))>SUELO*1.42 for _ in range(150)])) for d in (0.3,0.5,1.0,1.5,2.0)]
P("D-4","riesgo del consumidor: curva completa (1 unidad)"," · ".join(f"{d}mm:{p:.0%}" for d,p in cur),"*")
ac=[]
for ups in (50.,100.,200.,300.,500.,1000.):
    a=[alpha(placa(),campo_gp(placa(),ups,7.9,rng))[0] for _ in range(60)]
    ac.append((ups,np.mean(a),np.mean(np.array(a)>=0.95),np.mean(np.array(a)<0.35)))
P("D-5b","GATE-0: curva continua PASA/VETO vs upsilon"," · ".join(f"{u:.0f}:{m:.2f}({p:.0%}P,{v:.0%}V)" for u,m,p,v in ac),"*")
P("D-6","el VETO alpha<0,35: ¿donde esta el 98,7 %?",f"a ups<=50 mm el VETO se dispara el {ac[0][3]:.0%}. Por debajo de 50 el campo es ruido")
d0=[(s,np.mean([alpha(placa(),campo_gp(placa(),300.,s,rng))[1]*1e3*176**0.97>35 for _ in range(60)])) for s in (7.9,15.,25.,50.)]
P("D-7","D(176)<=35 um: discriminacion vs sigma_CNC"," · ".join(f"{s:.0f}um:{p:.0%}" for s,p in d0),"*")
P("D-8","suelo 1,0 mm al 90 %: ver D-4","la curva de D-4 ES esta")
P("D-9","choque: superficie (pico,dur,onset)","Eiband da 2 ejes medidos + onset 500 G/s. La superficie 3D NO esta publicada: hueco","!")
P("D-15","bulbo humedo 21,9-33,7 C: ¿nos aplica?","es limite de DISIPACION a largo plazo; en burbuja con ECLSS no aplica: manda OCHMO","*")
print("\n"+"="*104); print("  F · CONTROL NEGATIVO"); print("="*104)
UMB=SUELO*1.42; UMB98=SUELO98*1.42
def caso(f,lab,extra=None):
    ok=0
    for _ in range(150):
        B=acto(); d=DIAM.copy(); B,d=f(B,d)
        v1=om(O,B)>UMB; v2=om(O,B,98)>UMB98; v3=len(B)!=N
        v4=(np.abs(np.sort(d)-np.sort(DIAM)).max()>0.122) if len(d)==N else True
        ok+= (v1 or v2 or v3 or v4)
    return ok/150
P("F-1","permutacion de 2 adyacentes",f"{caso(lambda B,d:(B,d[[1,0]+list(range(2,N))]),''):.0%} rechazo")
P("F-2","desplazamiento 12 mm a alveolo vecino",f"{caso(lambda B,d:(np.r_[[B[0]+12],B[1:]],d),''):.0%} rechazo")
P("F-3","sustraccion de 1",f"{caso(lambda B,d:(B[1:],d[1:]),''):.0%} rechazo")
P("F-4","ADICION de 1 (nunca probado)",f"{caso(lambda B,d:(np.r_[B,[rng.uniform(12,188,2)]],np.r_[d,[9.]]),''):.0%} rechazo","*")
P("F-5","dos defectos que se compensan (nunca probado)",
  f"{caso(lambda B,d:(np.r_[[B[0]+1.0],[B[1]-1.0],B[2:]],d),''):.0%} rechazo","*")
P("F-7","placa girada 72 y vuelta: ¿cierra el lazo?","rotacion exacta de n=5 sobre 25 fiduciales: residuo maquina, 0 por construccion")
P("F-10","impostor a 3,1 sigma","Om_imp_min=0,0499 vs Om_acto=0,0008 -> factor 61. RECHAZADO con holgura")
P("F-12","atmosfera fuera de banda 59 min (ventana horaria)",
  f"media horaria de 59 min a 4 mmHg + 1 a 0 = {(59*4+0)/60:.2f} mmHg > 3 -> SE DETECTA. Pero 44 min a 4 da {(44*4)/60:.2f}: NO","!")
print("\n"+"="*104); print("  A · los dos que faltaban"); print("="*104)
kd=[(k,np.mean([om(O,acto())>SUELO*(1+k*0.1*math.sqrt(2)) for _ in range(200)])) for k in (1,2,3,4,6)]
P("A-7","K_DELTA: % de falsos vetos sobre acto limpio"," · ".join(f"K={k}:{p:.1%}" for k,p in kd),"!" if kd[2][1]>0.02 else "*")
P("A-16","D0_MAX: ver D-7","la curva de D-7 ES esta")
print("\n"+"="*104); print(f"  ALARMAS ({len(AL)}):")
for n,t,r in AL: print(f"    {n}  {t}  ->  {r}")
print(f"\n  HALLAZGOS ({len(F)}):")
for n,t,r in F: print(f"    {n}  {t}  ->  {r}")
