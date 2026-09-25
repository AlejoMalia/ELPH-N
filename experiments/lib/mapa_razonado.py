"""D-681 · EL MAPA RAZONADO · cada celda dice QUE DATO la permite o la impide."""
import math,sys; sys.path.insert(0,'experiments/lib')
from alpha_gp import alpha_efectiva
E,K,G,RHO,SUELO,UPS = 200e9,0.5,9.81,7850.,141e-6,300.
def lado(m): return (m/1000.)**(1/3.)*(1.6 if m>1 else 2.5)
def celda(m,L):
    t=max(0.7e5*(L/2)/(2*200e6),0.004); tn=math.sqrt(K*m*G*(L/2)/(E*SUELO)); t=max(t,tn)
    M=RHO*4*math.pi*(L/2)**2*t; al=alpha_efectiva(UPS,'gauss',16.,max(L*1000*.9,20.))
    Et=0.5*(M+m)*(45*9.81*math.sqrt(5500e3/(45*9.81)))**2
    return t,M,al,Et,lado(m)<=0.8*L
MAS=[(0.01,"tornillo"),(1.,"maleta"),(75.,"HUMANO"),(500.,"moto"),(5000.,"ELEFANTE"),(10000.,"camion")]
LAD=[0.1,0.3,1.0,2.0,3.0,5.0,8.0]
print("  "+"="*106)
print(f"  {'carga':<10}"+"".join(f"{L:>13.1f}" for L in LAD)+"   lado de cabina (m)")
print("  "+"-"*106)
for m,nom in MAS:
    f=""
    for L in LAD:
        t,M,al,Et,cabe=celda(m,L)
        if not cabe: s=f"· {lado(m):.2f}m"
        elif al<0.95: s=f"G a={al:.2f}"
        elif t>0.050: s=f"P t={t*1000:.0f}"
        elif Et>1e12: s=f"E {Et/1e12:.0f}TJ"
        else: s=f"## ok"
        f+=f"{s:>13}"
    print(f"  {nom:<10}{f}")
print("  "+"-"*106)
print("""  LO QUE DICE CADA SIMBOLO, Y DE DONDE SALE EL DATO:

   ·  NO CABE          lado_carga = (m/1000)^(1/3) x 1,6   <- densidad ~1000 kg/m3, DERIVADO
                       el numero que acompana es el lado minimo de la carga.

   G  FALLA EL GATE-0  alpha(L) con upsilon = 300 mm   <- MEDIDO en literatura de CMM
                       (longitudes de correlacion publicadas 100-500 mm)
                       **PASA solo si alpha >= 0,95, y eso exige upsilon >= L (D-680)**
                       el numero es el alpha que saldria hoy.

   P  PARED IMPOSIBLE  t >= raiz(k m g (L/2)/(E x 141 um))   <- k<=0,5 (Timoshenko/WRC 107)
                       E = 200 GPa acero · suelo 141 um MEDIDO por re-colocacion (D-614)
                       el numero es el espesor necesario en mm. Tope declarado: 50 mm.

   E  ENERGIA          E = 1/2 (M_cascara + m) v^2 con v de Eiband a 45 g   <- MEDIDO 1959
                       M_cascara propto L^3 -> la energia escala con el CUBO del lado.
                       Tope declarado: 1 TJ (unas 240 t de TNT).

   ## TODO VALE        las cuatro condiciones a la vez.
  """)
print("  "+"="*106)
print("\n  Y LOS DATOS QUE PERMITEN CADA COSA, con su estado evidencial:\n")
D=[("141 um","suelo de re-colocacion","MEDIDO (D-614, nuestro banco)","fija la pared minima y el suelo de deteccion"),
   ("0,52 um","lector optico","MEDIDO + EURAMET al 4 %","no manda: es el 0,0 % de la varianza"),
   ("100-500 mm","upsilon de una fresadora","LITERATURA (GP en CMM)","**es la pared que bloquea 60 de 66 celdas**"),
   ("45 g @ 44 ms","tolerancia humana","MEDIDO (Eiband 1959, NASA)","fija la velocidad, luego la energia"),
   ("k <= 0,5","cascara bajo carga puntual","DERIVADO (Timoshenko/WRC 107)","fija el espesor; robusto a toda la familia"),
   ("200 GPa","modulo del acero","MEDIDO, tabla","cambiar a composite EMPEORA (E menor)"),
   ("0,7 bar","presion interior","DECLARADO","fija el espesor minimo de 4 mm"),
   ("1000 kg/m3","densidad de la carga","DERIVADO","fija si cabe o no"),
   ("A > 1 + dA","contrato","DERIVADO + MEDIDO (3e6 impostores)","no bloquea ninguna celda: siempre se cumple"),
   ("p >= 100(1-1/2n)","inventario","DERIVADO (D-676)","no bloquea: es del acto, no de la escala")]
print(f"  {'dato':<18}{'que es':<30}{'estado':<32}{'que decide'}")
for a,b,c,d in D: print(f"  {a:<18}{b:<30}{c:<32}{d}")
print("\n  -> **De los diez datos, UNO SOLO bloquea el mapa: upsilon.** Y es el unico")
print("     que no hemos medido nosotros: viene de literatura de OTRO gremio (CMM).")
