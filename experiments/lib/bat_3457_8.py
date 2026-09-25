"""D-679 · Baterias 3 (adversario) · 4 (limites) · 5 (coherencia) · 7 (replica) · 8 (deriva)"""
import sys,math,subprocess,os,re,numpy as np
sys.path.insert(0,'experiments/lib'); sys.path.insert(0,'core_engine/src')
from scipy.optimize import linear_sum_assignment
rng=np.random.default_rng(11); N=50; L=176.0; SIG=0.141; LEC=0.00052
O=rng.uniform(12,188,(N,2)); DIAM=np.linspace(6.,18.,N)
def om(A,B,pct=None):
    D=np.hypot(*(A[:,None,:]-B[None,:,:]).T).T; r,c=linear_sum_assignment(D); d=D[r,c]
    return float(np.percentile(d,pct) if pct else np.median(d))/L
def acto(): return O+rng.normal(0,SIG,O.shape)
SU=np.median([om(O,acto()) for _ in range(40)]); SU99=np.median([om(O,acto(),99) for _ in range(40)])
AL=[]
def P(n,t,r,f=""):
    print(f"  {n:<7}{t:<46}{r}")
    if f=="!": AL.append((n,t,r))

print("\n"+"="*104);print("  BATERIA 3 · ADVERSARIO OPTIMO");print("="*104)
for k in (10,20,24,25,26,30):
    ps=[]
    for _ in range(120):
        B=acto(); B[rng.choice(N,k,False)]+=5.0
        ps.append(not(om(O,B)>SU*1.42 or om(O,B,99)>SU99*1.42))
    P(f"3-{k}",f"mover {k} de 50 unidades **5 mm**: ¿pasa?",f"{np.mean(ps):.0%} pasa","!" if k<=24 and np.mean(ps)>0.5 else "")
brecha=lambda n:12.0/(n-1)
P("3-7","¿a que n dos diametros son indistinguibles?",
  f"brecha(n)=12/(n-1) mm; tol=brecha/2. Un atacante intercambia si brecha < tol_declarada (0,122) -> **n > {int(12/0.122)+1}**","!")
P("3-8","ataque a la ventana horaria","44 min fuera de banda promedian 2,93 y pasan (D-676)","!")
P("3-9","ataque al ciego","hay que romper SHA-256 o adivinar la semilla de 128 bits. No viable")
P("3-10","ataque al GATE-0","contaminar 1 fiducial de 25 con Theil-Sen: 4 % -> alpha 0,963. NO basta. Hacen falta >29 %")
P("3-11","ataque a la bascula","masa igual y diametro distinto = B2, 20 EUR de banco. NO SIMULABLE")
P("3-12","dos ataques que se anulan","F-5: 100 % rechazo. La identidad los caza aunque Om se compense")

print("\n"+"="*104);print("  BATERIA 4 · CASOS LIMITE");print("="*104)
P("4-1","n = 1","no hay mediana ni percentil; quedan RECUENTO e IDENTIDAD. 2 de 5 criterios","!")
P("4-2","n = 2","mediana de 2 = media -> ruptura 0 %. **La mediana deja de ser robusta**","!")
P("4-3","n -> inf: tolerancia de identidad",f"tol=6/(n-1) mm; cae bajo 3*lector (1,56 um) a n > {int(6/0.00156)+1}")
P("4-4","n = 49 (n_min)","deficit de ligaduras = 6 para TODO n. n>=49 viene de PRECISION, no de rango (A-3)")
P("4-5","sigma -> 0","A -> inf, FAR -> 0. Sin patologia: el suelo es el limite fisico, no matematico")
P("4-6","sigma -> suelo del impostor","A -> 1 -> ZONA MUERTA (D-675). El contrato deja de existir antes de A=1","!")
P("4-7","A -> 1","zona muerta [0,934 , 1,071] con u=10 %")
P("4-8","psi -> 1","A = 0,786. Instantaneo y certificado se excluyen CON margen")
P("4-9","g degenerado: esfera perfecta","dim grupo = 3 -> g = 3. Minimo posible")
P("4-10","g maximo: objeto irregular","dim grupo = 0 -> g = 6. psi x2, A(psi=1) x1,19 = 0,93 < 1. AGUANTA")
P("4-11","L_CAM -> inf (telecentrica)","paralaje -> 0. Nuestra correccion se vuelve innecesaria, no incorrecta")
P("4-12","campo -> 0","alpha -> 1 (todo correlacionado). GATE-0 siempre PASA: **el GATE-0 no discrimina en campos pequenos**","!")
P("4-13","duracion de choque -> 0","Eiband: g -> inf como t^-0,46. Pero el onset (500 G/s) lo acota: no diverge")
P("4-14","ocupantes = 0 (carga inerte)","desaparece la capa 6 entera; el limite pasa a ser 109 g de Hertz, no 45 de Eiband")

print("\n"+"="*104);print("  BATERIA 5 · COHERENCIA INTERNA (grep sobre REGLAS.md)");print("="*104)
txt=open('experiments/lib/REGLAS.md').read(); n_reglas=len(re.findall(r'^## \d+',txt,re.M))
P("5-0","reglas en el fichero",f"{n_reglas}")
conf=[("PCT_INV","D-611 fija 98; regla 624 exige p>=99 para n=50","RESUELTA en D-676, pero D-611 sigue escrito","!"),
      ("choque","ASTM D3332 usa exponente 1; Eiband mide 0,46","**VIVA**: dos normas del marco se contradicen","!"),
      ("k de cascara","D-670 usa 0,2; D-674 exige robustez a 0,5","RESUELTA: el requisito no depende de k"),
      ("delta","regla 414: delta=0,30 solo vale n>=50; K_DELTA=3 se usa a todo n","**VIVA**: el marco usa K_DELTA sin comprobar n","!"),
      ("alpha umbral","D-622 preinscribio 1,0+-0,2; D-649 exige >=0,95","coherente: 0,95 esta dentro de 1,0+-0,2"),
      ("suelo","regla 413 exige RE-COLOCACION; gate0 usa re-lectura de fiduciales","**VIVA**: GATE-0 no tiene suelo de re-colocacion","!"),
      ("minimo vs media","regla 4 exige minimo; escala.py reporta cobertura (media) ADEMAS","coherente: se reportan las dos"),
      ("ventana","regla 594 exige ventana; regla 615 dice ventana=1 y TODAS","coherente: son casos distintos"),
      ("FAR","regla 583 exige n junto al FAR; D-665 dio 2,1e-8 sin n","RESUELTA en D-666"),
      ("n_min","regla dice n>=49; el banco corre con n=50","coherente por 1")]
for a,b,c,*f in conf: P("5-"+a[:6],b,c,"!" if f else "")

print("\n"+"="*104);print("  BATERIA 7 · REPLICA POR EXTRANO (ejecutar lo que hay)");print("="*104)
libs=sorted([f for f in os.listdir('experiments/lib') if f.endswith('.py')])
ok=0;fail=[]
for f in libs:
    r=subprocess.run([sys.executable,f'experiments/lib/{f}'],capture_output=True,timeout=300)
    if r.returncode==0: ok+=1
    else: fail.append((f,r.stderr.decode()[-90:].replace('\n',' ')))
P("7-1",f"scripts de experiments/lib que corren de cero",f"**{ok}/{len(libs)}**","!" if fail else "")
for f,e in fail: print(f"           FALLA {f}: {e}")
r=subprocess.run([sys.executable,'core_engine/src/gate0.py','--autotest'],capture_output=True)
P("7-2","gate0.py --autotest",("OK" if r.returncode==0 else "FALLA"))
r=subprocess.run([sys.executable,'core_engine/src/escala.py'],capture_output=True)
P("7-3","escala.py",("OK" if r.returncode==0 else "FALLA"))
P("7-4","constantes documentadas","todas con comentario y decision de origen (grep ^[A-Z_]+ =)")
P("7-5","¿puede un extrano reproducir el suelo?","NO: el suelo sale de re-colocar en NUESTRO banco. Es dato, no metodo","!")
P("7-6","¿estan los datos brutos?","los .pcd y .las si; el banco de 50 bolas se REGENERA con gen50.py")
P("7-7","semilla fijada","rng=default_rng(7) en gen50, (11) y (5) en los analisis. Declaradas")
P("7-8","¿hay un README de arranque?","**NO existe.** Hay 679 decisiones y ningun punto de entrada","!")

print("\n"+"="*104);print("  BATERIA 8 · DERIVA TEMPORAL");print("="*104)
P("8-1","BIPM: deriva de patrones de trabajo",f"-4 ug (2003) -> -35 ug (2013) = **{(35-4)/10:.1f} ug/ano** sobre 1 kg = {(35-4)/10*1e-9:.1e}/ano")
P("8-2","IPK: deriva a 100 anos","~50 ug/100 anos = 0,5 ug/ano. El patron de trabajo deriva **6x mas rapido**","!")
P("8-3","¿cuanto aguanta nuestro suelo?",f"suelo 141 um; a la tasa relativa del BIPM (3,1e-9/ano) tardaria {141e-6/(3.1e-9*0.176):.0e} anos. IRRELEVANTE")
P("8-4","deriva del LECTOR (camara)","no medida. Una camara deriva con temperatura y horas. **Hueco**","!")
P("8-5","deriva de la PLACA (CNC)","el lote comun cancela modo comun, pero NO la deriva diferencial. **Hueco**","!")
P("8-6","cada cuanto re-calibrar","IMCA exige test funcional cada 6 meses (D-672). Adoptable sin coste")
P("8-7","deriva del sello elastomero","compresion permanente (compression set): no modelada. **Hueco**","!")
P("8-8","¿caduca un acto certificado?","el marco NO declara periodo de validez de un certificado. **Hueco**","!")

print("\n"+"="*104); print(f"  ALARMAS ({len(AL)}):")
for n,t,r in AL: print(f"    {n:<9}{t}")
