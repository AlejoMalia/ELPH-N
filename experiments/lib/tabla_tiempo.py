"""D-686 · EL FACTOR TIEMPO · tabla masa x distancia. Formulas 36-38."""
import math,sys; sys.path.insert(0,'experiments/lib')
G,E_MOD,K,RHO,SUELO,N_SUELO = 9.81,200e9,0.5,7850.,141e-6,10
def t_manejo(M):                      # DECLARADO · regimenes discretos de manipulacion
    if M < 25:    return 0.5          # a mano
    if M < 1000:  return 3.0          # polipasto
    if M < 20000: return 8.0          # grua
    return 15.0                       # grua pesada
def cabina(m):
    L=max(0.1,(m/1000.)**(1/3.)*2.0)                      # lado util
    t=max(max(0.7e5*(L/2)/(2*200e6),0.004), math.sqrt(K*m*G*(L/2)/(E_MOD*SUELO)))
    return L, RHO*4*math.pi*(L/2)**2*t + m                # lado, masa TOTAL
def T(m, n_oc=0):                     # f.36 · coste fijo, SOLO masa
    L,M=cabina(m)
    return 2*N_SUELO*t_manejo(M) + (4.0*n_oc + 2.0 + 14.5/13.5) + (t_manejo(M) + 0.14 + 1.0)
def tau(d,a=9.):  return 2*math.sqrt(d/(a*G))/60.         # f.28 · SOLO ruta
def d_cruce(m,a=9.): return a*G*(T(m)*60/2)**2            # f.37
def fmt(t): return f"{t:.1f}m" if t<120 else (f"{t/60:.1f}h" if t<2880 else f"{t/1440:.0f}d")
MAS=[(0.001,"1 g"),(0.005,"5 g"),(0.010,"10 g"),(0.020,"20 g"),(0.050,"50 g"),(0.100,"100 g"),
     (0.5,"500 g"),(1.,"1 kg"),(2.,"2 kg"),(5.,"5 kg"),(10.,"10 kg"),(25.,"25 kg"),
     (75.,"75 kg · persona"),(100.,"100 kg"),(500.,"500 kg"),(1000.,"1 t"),(5000.,"5 t · elefante"),
     (20000.,"20 t"),(50000.,"50 t"),(100000.,"100 t")]
RUT=[("1 km",1e3),("10 km",10e3),("100 km",100e3),("Berlin 930 km",930e3),
     ("Tokio 10.850",10_850e3),("Sidney 17.000",17_000e3),("Luna 384.400",384_400e3),
     ("Marte 55e6",55e9)]
print("\n  "+"="*118)
print("  TIEMPO TOTAL DEL ACTO a 9 g   ·   T(m) + tau(d)   ·   entre parentesis, el % que es VUELO\n")
print(f"  {'carga':<17}{'T(m) fijo':>10}",end="")
for rn,_ in RUT: print(f"{rn:>13}",end="")
print()
print("  "+"-"*118)
for m,nom in MAS:
    tf=T(m, 1 if m==75. else 0)
    print(f"  {nom:<17}{fmt(tf):>10}",end="")
    for rn,d in RUT:
        tt=tau(d); tot=tf+tt
        print(f"{fmt(tot)+f'({100*tt/tot:.0f}%)':>13}",end="")
    print()
print("  "+"="*118)
print("\n  P1 · LA DISTANCIA DE CRUCE ES UNA ESCALERA, no una curva\n")
print(f"  {'carga':<17}{'masa TOTAL':>13}{'regimen':>16}{'T(m)':>9}{'d* de cruce':>16}")
prev=None
for m,nom in MAS:
    L,M=cabina(m); tm=t_manejo(M)
    reg={0.5:"a mano",3.0:"polipasto",8.0:"grua",15.0:"grua pesada"}[tm]
    d=d_cruce(m)
    salto=" <-- SALTO" if prev is not None and reg!=prev else ""
    print(f"  {nom:<17}{M:>11.0f}kg{reg:>16}{fmt(T(m,1 if m==75. else 0)):>9}{d/1e3:>13,.0f} km{salto}")
    prev=reg
