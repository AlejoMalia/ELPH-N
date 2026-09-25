"""D-679 · BATERIA 6 · ESCALA DE CABINA · tornillo / humano / elefante · cubo 30 cm y 3 m

  La pregunta del investigador: si la cabina es MAS GRANDE que el objeto,
  ¿se reduce la dificultad, o el tamano de cabina tambien influye?

  MATEMATICA antes de correr. Cuatro cosas escalan con el lado L de la cabina,
  y NO en la misma direccion:

    Om = error_absoluto / L          -> L grande, Om PEQUENO   ** MAS FACIL **
    alpha(L) con upsilon fijo        -> L grande, alpha BAJO   ** MAS DIFICIL **
    t_pared = dP R / (2 sigma_adm)   -> t propto L
    M_cascara propto rho R^2 t       -> **propto L^3**          ** MAS CARO **
    w = k P R/(E t^2), t propto L    -> w propto P/L            ** MAS FACIL **

  PREDICCION: hay un OPTIMO. Por debajo manda alpha (el GATE-0 no discrimina
  en campos pequenos, 4-12); por encima manda la masa (L^3).
"""
import sys,math,numpy as np; sys.path.insert(0,'experiments/lib')
from alpha_gp import alpha_efectiva
SIG_COL, UPS, DP, SIG_ADM, RHO = 141e-6, 0.300, 0.7e5, 200e6, 7850.   # m, m, Pa, Pa, kg/m3
E, KSH, G = 200e9, 0.5, 9.81
CARGA = {"tornillo":(0.010,0.05),"humano":(75.,1.2),"elefante":(5000.,4.0)}   # masa kg, lado min m
def linea(L, m_carga):
    t = max(DP*(L/2)/(2*SIG_ADM), 0.004)          # espesor, minimo 4 mm (D-674)
    M = RHO*4*math.pi*(L/2)**2*t
    Om = SIG_COL/L
    al = alpha_efectiva(UPS*1000, 'gauss', 16., max(L*1000*0.9,20.))
    w  = KSH*m_carga*G*(L/2)/(E*t**2)
    return t,M,Om,al,w
print("  "+"="*100)
print(f"  {'cabina':>8}{'pared':>8}{'M cascara':>12}{'Om':>11}{'alpha':>8}{'veredicto':>12}{'flexion (um) con...':>24}")
print(f"  {'(m)':>8}{'(mm)':>8}{'(kg)':>12}{'':>11}{'':>8}{'GATE-0':>12}{'tornillo':>9}{'humano':>8}{'elef.':>7}")
print("  "+"-"*100)
for L in (0.3,0.5,1.0,1.5,2.0,3.0,5.0,8.0):
    t,M,Om,al,_=linea(L,0)
    ws=[linea(L,m)[4]*1e6 for m,_ in CARGA.values()]
    v='PASA' if al>=0.95 else ('VETO' if al<0.35 else 'INTERMEDIO')
    cab=[k for k,(m,l) in CARGA.items() if l<=L*0.8]
    print(f"  {L:>8.1f}{t*1000:>8.1f}{M:>12.0f}{Om:>11.2e}{al:>8.3f}{v:>12}"
          f"{ws[0]:>9.2f}{ws[1]:>8.1f}{ws[2]:>7.0f}   cabe: {','.join(cab) if cab else '-'}")
print("  "+"="*100)
print("\n  LOS DOS CUBOS QUE PREGUNTAS:\n")
for L,nom in ((0.3,"cubo 30x30x30 cm"),(3.0,"cubo 3x3x3 m")):
    t,M,Om,al,_=linea(L,0)
    print(f"  {nom}")
    print(f"     pared {t*1000:.1f} mm · cascara {M:.0f} kg · Om = {Om:.2e} · alpha = {al:.3f} -> "
          f"{'PASA' if al>=0.95 else 'INTERMEDIO'}")
    for k,(m,l) in CARGA.items():
        cabe = l <= L*0.8
        w=linea(L,m)[4]*1e6
        print(f"     {k:<10} {'CABE   ' if cabe else 'NO CABE'} · flexion {w:>8.1f} um "
              f"{'(supera el suelo de 141)' if w>141 else ''}")
    print()
print("  RELACION CLAVE (la respuesta a la pregunta):")
r=(SIG_COL/0.3)/(SIG_COL/3.0)
print(f"     Om(30 cm)/Om(3 m) = {r:.0f}  ->  **la cabina de 3 m es {r:.0f} veces mas FACIL de certificar**")
print(f"     con EXACTAMENTE el mismo hardware. Om se normaliza por L: el error no cambia, el campo si.")
print(f"     Pero alpha cae de {alpha_efectiva(300,'gauss',16.,270.):.3f} a {alpha_efectiva(300,'gauss',16.,2700.):.3f}: "
      f"el GATE-0 se vuelve IMPOSIBLE.")
