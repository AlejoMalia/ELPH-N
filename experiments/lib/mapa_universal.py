"""D-680 · BATERIA 9 · EL MAPA UNIVERSAL · ¿DONDE vale el marco?

  Idea del investigador: poner el enfoque en una ESCALA UNIVERSAL, del tornillo
  al elefante. No es una lista de casos: es un DIAGRAMA DE FASES del marco.

  Ejes: masa de la carga (10 g - 10 t)  x  lado de la cabina (0,1 - 10 m)
  Para cada celda se comprueban CINCO condiciones, todas ya derivadas:

    C   cabe la carga            lado_carga <= 0,8 L
    G   GATE-0 pasa              alpha(L, upsilon=300 mm) >= 0,95
    F   flexion < suelo          k m g (L/2)/(E t^2) <= 141 um   con t >= 4 mm
    E   energia asumible         E_total <= 1 TJ (Nueva York-Londres a 45 g)
    P   pared fabricable         t <= 50 mm
"""
import math, sys; sys.path.insert(0,'experiments/lib')
from alpha_gp import alpha_efectiva
E_MOD,K,G,RHO,SUELO = 200e9,0.5,9.81,7850.,141e-6
def lado_carga(m): return (m/1000.)**(1/3.)*1.6 if m>1 else (m/1000.)**(1/3.)*2.5
def celda(m,L):
    t=max(0.7e5*(L/2)/(2*200e6),0.004)
    t_nec=math.sqrt(K*m*G*(L/2)/(E_MOD*SUELO))
    t=max(t,t_nec)
    M=RHO*4*math.pi*(L/2)**2*t
    al=alpha_efectiva(300.,'gauss',16.,max(L*1000*0.9,20.))
    Etot=0.5*(M+m)*(45*9.81*2*math.sqrt(5500e3/(45*9.81))/2)**2
    return dict(C=lado_carga(m)<=0.8*L, Gg=al>=0.95, F=t_nec<=t, Ee=Etot<=1e12, P=t<=0.050,
                t=t,M=M,al=al,E=Etot)
MASAS=[(0.01,"tornillo"),(1.,"maleta"),(75.,"HUMANO"),(500.,"moto"),(5000.,"ELEFANTE"),(10000.,"camion")]
LADOS=[0.1,0.2,0.3,0.5,1.0,1.5,2.0,3.0,5.0,8.0,10.0]
print("  "+"="*96)
print(f"  {'carga':<11}" + "".join(f"{L:>7.1f}" for L in LADOS) + "   lado de cabina (m)")
print("  "+"-"*96)
for m,nom in MASAS:
    fila=""
    for L in LADOS:
        c=celda(m,L)
        if not c['C']: s="·"                      # no cabe
        elif all((c['Gg'],c['F'],c['Ee'],c['P'])): s="##"   # TODO vale
        elif not c['Gg'] and all((c['F'],c['Ee'],c['P'])): s="G"  # solo falla GATE-0
        elif not c['P']: s="P"
        elif not c['Ee']: s="E"
        else: s="?"
        fila+=f"{s:>7}"
    print(f"  {nom:<11}{fila}")
print("  "+"-"*96)
print("  ##  todo vale   ·   G  solo falla el GATE-0   ·   P  pared > 50 mm   ·   E  energia > 1 TJ   ·   ·  no cabe")
print("  "+"="*96)
print("\n  LECTURA DEL MAPA:\n")
ok=[(m,nom,L) for m,nom in MASAS for L in LADOS if all(celda(m,L)[k] for k in ('C','Gg','F','Ee','P'))]
print(f"  Celdas donde TODO vale: {len(ok)} de {len(MASAS)*len(LADOS)}")
for m,nom,L in ok: print(f"      {nom:<10} en cabina de {L} m")
print(f"\n  -> **El marco solo vale hoy en una franja: cargas pequenas en cabinas <= 0,3 m.**")
print(f"     Y el cuello es SIEMPRE el mismo: el GATE-0. Por eso casi todo el mapa es 'G'.")
for m,nom in (75.,"HUMANO"),(5000.,"ELEFANTE"):
    Lmin=next(L for L in LADOS if celda(m,L)['C'])
    c=celda(m,Lmin)
    for u in [100*1.1**i for i in range(120)]:
        if alpha_efectiva(u,'gauss',16.,Lmin*1000*0.9)>=0.95: break
    print(f"\n  {nom}: cabina minima {Lmin} m · pared {c['t']*1000:.1f} mm · cascara {c['M']:.0f} kg")
    print(f"      alpha actual {c['al']:.3f} -> **necesita upsilon >= {u:.0f} mm = {u/(Lmin*1000):.1f}x la cabina**")
    print(f"      energia {c['E']/1e12:.2f} TJ para Nueva York-Londres a 45 g")
