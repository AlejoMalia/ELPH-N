"""D-676 · Batería, tanda 1: A sensibilidad (18) · C triangulación (11) · E acoplamiento (15)"""
import sys, math, numpy as np; sys.path.insert(0,'experiments/lib')
from alpha_gp import alpha_efectiva
A_ACT, OM_ACT, OM_IMP, K3, g = 7.80, 0.000816, 0.04993, 0.597, 3.0
SIG_COL, SIG_LEC, L_CAM, R_BOLA = 0.141, 0.00052, 1500.0, 12.70
AL=[]; F=[]   # alarmas, hallazgos
def P(n,t,r,flag=""):
    print(f"  {n:<6}{t:<52}{r}")
    if flag=="!": AL.append((n,t,r))
    if flag=="*": F.append((n,t,r))

print("\n" + "="*104); print("  A · SENSIBILIDAD"); print("="*104)
P("A-2","g mal en 1 (3->4): efecto sobre psi y su frontera",
  f"psi x1,33 · A(psi=1) 0,786->{(4*K3**4)**.25:.3f}, sigue <1")
n=np.arange(4,60); lig=3*n-6; gl=3*n
P("A-3","n_min: ligaduras 3n-6 vs 3n grados de libertad",
  f"deficit constante = 6 (los 6 del cuerpo rigido) para todo n; n>=49 viene de la PRECISION, no del rango","*")
P("A-4","clase 2 tratada como 3 (phi 0->1)","no es error de contrato: es COSTE. Mueves masa que no hacia falta")
P("A-7","K_DELTA 1-6 -> umbral (1+K*disp*raiz2)*suelo","SIM (tanda 2)")
for p in (90,95,98,99,99.9):
    pass
P("A-8","PCT_INV: punto de ruptura = 1 - p/100",
  "p90->10 % · p95->5 % · p98->2 % · p99->1 % · p99,9->0,1 %")
P("A-9","N_SUELO_MIN: error relativo de delta = 1/raiz(2(n-1))",
  " · ".join(f"n={n}:{100/math.sqrt(2*(n-1)):.0f}%" for n in (5,10,25,50)) + "  -> n=10 da 24 %","!")
P("A-10","N_IMP: cota 3/k y CPU a 84 us",
  " · ".join(f"k={k:.0e}:{3/k:.0e} en {84e-6*k:.0f}s" for k in (1e4,1e5,1e6,3e6)))
P("A-11","tolerancia identidad = media brecha minima",
  f"brecha min de 50 diam en [6,18] mm = {12/49:.3f} mm -> tol {12/49/2*1000:.0f} um, y el lector da 0,52 um: margen x{12/49/2*1000/0.52:.0f}")
P("A-12","L_CAM: paralaje propto 1/L",
  " · ".join(f"L={L/1000:.1f}m:{400*1500/L:.0f}um" for L in (750.,1500.,3000.)))
P("A-13","campo: alpha con upsilon=300",
  " · ".join(f"{r:.0f}mm:{alpha_efectiva(300.,'gauss',16.,r):.3f}" for r in (100.,176.,249.,400.)))
P("A-14","N_FID: incertidumbre de la afin propto 1/raiz(N)",
  f"9->25 fiduciales baja el error de ajuste x{math.sqrt(25/9):.2f}")
P("A-15","R0 de referencia: D(r0)=C r0^alpha",
  " · ".join(f"r0={r:.0f}:{7.2*(r/176)**0.97:.1f}um" for r in (88.,176.,249.)) + " -> el veredicto SI depende de r0","!")
P("A-16","D0_MAX 35 um","SIM (tanda 2)")
P("A-17","sigma_colocacion: suelo de deteccion propto sigma",
  " · ".join(f"sig={s:.0f}um:{1.0*s/141:.2f}mm" for s in (14.,50.,141.,300.)))
P("A-18","Archard K 1e-4 a 1e-1: volumen desgastado propto K",
  "factor 1000 en desgaste. La conclusion de D-6xx aguanto POR SUERTE (ya registrado)")
P("A-20","onset 500 G/s de Eiband: t_subida a 45 g",
  f"{45/500*1000:.0f} ms de subida frente a {44:.0f} ms de plato -> **la subida es comparable al plato**","*")

print("\n" + "="*104); print("  C · TRIANGULACION"); print("="*104)
P("C-1","K_d: derivado 0,597 vs medido D-605 0,56",f"desvio {abs(0.597-0.56)/0.597*100:.1f} % -> A x{0.56/0.597:.3f} = {A_ACT*0.56/0.597:.2f}. Concuerdan")
P("C-2","n_min: Maxwell 1864 (3n-6) vs banco 2D/3D","misma formula, dos rutas, 162 anos aparte. CONCUERDAN")
P("C-3","Ahlswede-Dueck vs nuestro FAR","ID crece doblemente exponencial -> nuestro 1e-6 con 25 unidades es CONSERVADOR")
P("C-4","delta: 1/raiz(n) derivado vs dispersion medida","CONCUERDAN (D-614): delta=0,30 solo vale n>=50")
P("C-5","puntos de ruptura teoricos vs banco","mediana 50 % / p98 2 % / max 1/n: los tres verificados en banco")
P("C-6","sigma_lector: nuestro 0,52 vs EURAMET 0,5 um",f"desvio {abs(0.52-0.5)/0.5*100:.0f} %. **Estamos al nivel de un NMI**","*")
P("C-7","alpha: nucleo GP (D-668) vs ajuste (D-669)",f"GP a ups=300 predice 0,973 · ajuste medido 0,969. desvio {abs(.973-.969)/.973*100:.1f} %","*")
P("C-9","109 g Hertz (bolas) vs 45 g Eiband (humano)",f"el humano limita {109/45:.1f}x antes. Coherente: tejido vs acero")
P("C-11","A: mediana 11,8 · minimo 7,8 · FAR<=1e-6","tres rutas, el mismo signo. La mediana sobreestima x1,5")
P("C-13","presion: Armstrong 6,3 kPa vs OCHMO 34,5 kPa",f"OCHMO es {34.5/6.3:.1f}x mas conservador: uno es ebullicion, otro es INDEFINIDO. No son el mismo limite","!")
P("C-14","UHMS 113 inc/135 muertes vs 37 buzos 0 muertes","el segundo es EMERGENCIA controlada; el primero incluye fuego. No promediar")

print("\n" + "="*104); print("  E · ACOPLAMIENTO  (la red)"); print("="*104)
P("E-1","1->2 ley A mal 10 % -> los 5 criterios","solo mueve el criterio 5 (contrato). Los otros 4 son independientes de la ley","*")
P("E-2","1->3 n_min mal -> fiduciales","n_min afecta a las UNIDADES, no a los fiduciales. ACOPLAMIENTO NULO: celda a revisar","!")
P("E-3","1->4 phi mal -> custodia","si phi=0 no hay criterio de IDENTIDAD, y la custodia pierde su mejor detector (Johnston)","*")
P("E-4","1->5 g mal -> A en el acto","g no entra en A, entra en psi. A invariante")
P("E-5","1->6 clase 3 -> envolvente","clase 3 obliga phi=1 -> hay masa que acelerar -> Eiband aplica. SIN clase 3 no hay envolvente","*")
P("E-6","2->3 suelo mal -> veredicto GATE-0","el suelo no entra en GATE-0 (alpha es adimensional). NULO")
P("E-7","2->4 delta mal -> falsas alarmas","delta x2 -> umbral x2 -> el 100 % de los defectos de 1,0 mm se pierden","!")
P("E-8","2->5 cual de los 5 domina el fallo","identidad y p98 (ruptura 1/n y 2 %). La mediana NO ve nada bajo el 50 %")
P("E-9","2->6 el ciego -> monitorizacion del ocupante","aplicable: sellar el registro de OCHMO con compromiso. COSTE 0, no hecho","*")
P("E-10","3->4 paralaje sin corregir -> sello violado","400 um de paralaje > 141 um de suelo -> **un sello violado podria pasar**","!")
P("E-11","3->5 alpha<0,95 -> A en el acto","de la curva D-649: alpha 0,80 da 10 % de exito; 1,00 da 97,5 %")
P("E-12","3->6 flexion de cascara -> lectura","29 um (acero 5 mm) sobre 141 de suelo = 21 % del presupuesto","*")
P("E-13","4->5 sello batido -> los 5 criterios","Johnston: el sello cae siempre; los criterios lo cazan por re-medida. ESTA es la defensa")
P("E-14","4->6 fuego -> envolvente fisiologica","el fuego consume O2 y sube T: ataca ppO2 Y la banda termica A LA VEZ","*")
P("E-15","6->4 envolvente -> custodia","13,5 psi/min limita la velocidad de transferencia, luego limita el PROTOCOLO de custodia","*")

print("\n" + "="*104)
print(f"  ALARMAS ({len(AL)}):")
for n,t,r in AL: print(f"    {n}  {t}")
print(f"\n  HALLAZGOS ({len(F)}):")
for n,t,r in F: print(f"    {n}  {t}")
