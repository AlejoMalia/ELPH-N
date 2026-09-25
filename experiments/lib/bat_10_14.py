"""D-681 · Baterias 10 (FMEA cruzado) · 11 (tasa de fallo) · 12 (contradicciones)
   · 13 (coste marginal) · 14 (frontera del mapa).  Coste 0."""
import math,sys; sys.path.insert(0,'experiments/lib')
from alpha_gp import alpha_efectiva
print("\n"+"="*104);print("  BATERIA 10 · FMEA CRUZADO  (modos de fallo estandar vs nuestras 28 afirmaciones)");print("="*104)
FMEA=[("sobrepresion","SI","OCHMO 34,5-103 kPa + 13,5 psi/min"),
      ("colapso por vacio / subpresion","**NO**","no hay criterio de pandeo externo"),
      ("fatiga por ciclado","**NO**","cada acto es un ciclo de presion. No contado"),
      ("corrosion / degradacion","**NO**","solo Archard (desgaste), no corrosion"),
      ("fractura fragil a baja T","**NO**","la banda termica es FISIOLOGICA, no del MATERIAL"),
      ("fallo de soldadura/union","**NO**","la cascara se supone monolitica"),
      ("fallo de sello","SI","B1-B4 + Johnston + permeacion"),
      ("choque termico","**NO**","no hay criterio de gradiente"),
      ("impacto externo","SI","choque (pico,duracion,onset)"),
      ("FUEGO","SI","NFPA 99 + IMCA D 024 (D-672, tropezado)"),
      ("fallo de soportes / anclaje","**NO**","el transporte supone la carga sujeta, no la cabina"),
      ("cargas en boquillas/penetraciones","**NO**","toda cabina tiene pasamuros. No modelado"),
      ("atmosfera toxica","SI","OCHMO [V2 6025] contaminacion"),
      ("perdida de energia / soporte vital","**NO**","no hay criterio de autonomia"),
      ("atrapamiento / egreso","**NO**","no hay criterio de apertura desde dentro"),
      ("evento medico del ocupante","**NO**","la envolvente es ambiental, no clinica")]
cub=sum(1 for _,s,_ in FMEA if s=="SI")
for m,s,n in FMEA: print(f"  {m:<34}{s:<8}{n}")
print(f"\n  **CUBIERTOS {cub}/{len(FMEA)} = {100*cub/len(FMEA):.0f} %.  FALTAN {len(FMEA)-cub} MODOS DE FALLO.**")
print("  P3 SE CUMPLE, y por mucho: el fuego no era el unico que habiamos tropezado.")
print("\n"+"="*104);print("  BATERIA 11 · TASA DE FALLO OPERACIONAL");print("="*104)
print(f"  {'fuente':<40}{'n':>8}{'eventos':>9}{'cota 95 % (regla de tres)':>28}")
for f,n,e in (("TUP: buzos en emergencia (1975-2013)",37,0),("UHMS: incidentes en 75 anos",None,113),
              ("nuestro acto",0,0)):
    if n and e==0: c=f"<= {3/n:.1%}"
    elif n==0: c="SIN DATO: n = 0"
    else: c="SIN DENOMINADOR PUBLICADO"
    print(f"  {f:<40}{str(n) if n is not None else '?':>8}{e:>9}{c:>28}")
print(f"\n  -> **P1 SE CUMPLE: la mejor cifra publicada NO acota la mortalidad por debajo del 8,1 %.**")
print("     'Cero muertes en 37 buzos' suena perfecto y significa 'como mucho 1 de cada 12'.")
print("     Para afirmar 1e-3 harian falta 3.000 transferencias documentadas.")
print("     **La tasa se declara como el FAR: cota + n. Nunca como 'no ha pasado nunca'.**")
print("\n"+"="*104);print("  BATERIA 12 · CIERRE DE LAS TRES CONTRADICCIONES");print("="*104)
print("""  12-1 ASTM D3332 (exp 1) vs Eiband (0,46)
       RESUELTA POR ALCANCE: no se contradicen, se aplican a SUSTRATOS distintos.
       Eiband -> el OCUPANTE (tejido, dano por energia).  D3332 -> la CARGA inerte
       (embalaje, dano por Delta-v).  **Se declara cual rige cada uno. Y rige el menor.**
  12-2 K_DELTA = 3 usado sin comprobar n (regla 414)
       RESUELTA: delta = K x dispersion x raiz(2) YA depende de n a traves de la
       dispersion medida del suelo. Lo que faltaba era la GUARDA: abortar si n < N_SUELO_MIN.
       Ya esta en maquina.py (raise SystemExit). **La contradiccion era del REGISTRO, no del codigo.**
  12-3 GATE-0 sin suelo de re-colocacion (regla 413)
       **VIVA Y REAL.** gate0.py compara dos LECTURAS de fiduciales; la regla 413 exige
       que el suelo salga de RE-COLOCAR. Arreglo: M3' debe incluir desmontar y volver a
       montar la placa entre tandas. **Coste 0: es un paso mas del protocolo, no hardware.**""")
print("\n"+"="*104);print("  BATERIA 13 · COSTE MARGINAL");print("="*104)
print(f"  El minimo del marco es min(0,0,0) sobre tres condiciones de banco.")
print(f"  {'compra':<28}{'coste':>8}{'mueve el MINIMO':>18}{'   valor real'}")
for c,p in (("GATE-0",25),("B1-B4",100),("el acto",534)):
    print(f"  {c:<28}{p:>7} E{'NO (sigue 0)':>18}   {'OPCION DE VETO' if c=='GATE-0' else 'ninguno aislado'}")
print(f"  {'los tres juntos':<28}{659:>7} E{'0 -> ~85 %':>18}   el unico paquete que mueve algo")
print(f"\n  P2 SE CUMPLE: ninguna compra aislada mueve el minimo. Pero el GATE-0 tiene OPCION:")
print(f"  25 EUR compran la posibilidad de no gastar 634.  Umbral: P(veto) > 25/634 = {25/634:.1%}")
print(f"\n  {'upsilon real':>14}{'P(VETO) medida':>18}{'ahorro esperado':>18}{'   ¿vale los 25 E?'}")
for u,pv in ((50.,0.38),(100.,0.00),(300.,0.00)):
    print(f"  {u:>12.0f} mm{pv:>17.0%}{pv*634:>16.0f} E   {'SI' if pv>25/634 else 'NO — y es informacion igual'}")
print("\n  -> **El GATE-0 no se compra por el ahorro: se compra porque es el UNICO dato")
print("     que mide upsilon, y upsilon es la pared que bloquea 60 de 66 celdas del mapa.**")
print("\n"+"="*104);print("  BATERIA 14 · FRONTERA DEL MAPA · ¿que hace falta para ganar UNA celda?");print("="*104)
for L,nom in ((1.0,"HUMANO en cabina de 1 m"),(3.0,"HUMANO en cabina de 3 m")):
    for u in [100*1.05**i for i in range(200)]:
        if alpha_efectiva(u,'gauss',16.,L*1000*0.9)>=0.95: break
    print(f"\n  {nom}")
    print(f"     hoy: alpha = {alpha_efectiva(300.,'gauss',16.,L*1000*0.9):.3f}   ->   hace falta upsilon >= {u:.0f} mm")
    print(f"     proceso que lo da: UNA operacion que conforme la pieza entera (D-680)")
    print(f"       embuticion profunda · hidroconformado · repulsado (spinning) · molde unico")
    print(f"     **ENSAYO PARA COMPROBARLO: medir upsilon sobre DOS piezas ya conformadas.**")
    print(f"       no hace falta fabricar nada: vale cualquier par de piezas del mismo utillaje.")
    print(f"       Instrumento: el mismo lector del GATE-0. Coste estimado: 2 piezas + 1 tarde.")
print("\n  -> **El mapa deja de ser un diagnostico y pasa a ser un PLAN: un solo ensayo,")
print("     medir upsilon sobre dos piezas conformadas, decide 60 celdas de golpe.**")
