"""D-707 · Elasticidad de los limbos frente a ruta, masa y aceleracion."""
import math
G=9.81
def tau(d,a=9.): return 2*math.sqrt(d/(a*G))/60.
def t_manejo(M): return 0.5 if M<25 else (3.0 if M<1000 else (8.0 if M<20000 else 15.0))
RUT=[('Londres-Berlin',930e3),('Londres-Sidney',17_000e3),('orbita baja',400e3),
     ('Tierra-Luna',384_400e3),('Tierra-Marte',55e9)]
CAR=[('1 tornillo',1.),('1 persona',232.),('5 personas',1330.),('1 elefante',21456.)]
CO2=15.8
print("\n  "+"="*100)
print("  1 · LAS ELASTICIDADES, DERIVADAS")
print("  "+"="*100)
print("""
     L4 jurisdiccional = tau = 2 raiz(d/(a g))
        e(L4, d) = **+0,50**    doblar la distancia multiplica L4 por 1,41
        e(L4, a) = **-0,50**    doblar la aceleracion lo divide por 1,41
        e(L4, m) = **0,00**     **NO DEPENDE DE LA MASA. Ni un poco.**

     L5 irreversibilidad = 0,70 tau          mismas elasticidades que L4
     L2 custodia = prep + tau + apertura     mixta, y **acotada por el CO2**
     L1 juridico = tau + T_B(m)              mixta: ruta por tau, masa por manejo
     L3 identidad = L1
     L6 reserva  = operacional, no fisica
""")
print("  -> **El limbo mas peligroso (L4) es el unico que NO depende de la masa.**")
print("     Un tornillo y un elefante tienen exactamente el mismo L4 en la misma ruta.")
print("\n  "+"="*100); print("  2 · PROYECCION · L4 (el peor) por ruta"); print("  "+"="*100)
print(f"\n  {'ruta':<20}{'L4 = transito':>16}{'x Berlin':>11}{'mitigacion':>13}{'   ¿supera el CO2?'}")
b=tau(930e3)
for n,d in RUT:
    t=(7800./(9*G))/60 if n=='orbita baja' else tau(d)
    tt=f"{t:.1f} min" if t<120 else f"{t/60:.1f} h"
    print(f"  {n:<20}{tt:>16}{t/b:>10.1f}x{'NULA':>13}   " + ('**SI: L2 y L4 se FUNDEN**' if t>CO2 else 'no'))
d_merge=9*G*(CO2*60/2)**2
print(f"\n  -> **umbral de fusion: {d_merge/1e3:,.0f} km.** Por encima, el transito supera el")
print(f"     reloj de CO2, hace falta ECLSS, y **L2 deja de ser 10 min y pasa a ser TODO")
print(f"     el transito**: los dos peores limbos se funden en uno solo, con mitigacion nula.")
print(f"     Londres-Sidney esta a 17.000 km: **justo por debajo. La Luna, muy por encima.**")
print("\n  "+"="*100); print("  3 · EXPOSICION TOTAL E por ruta y carga"); print("  "+"="*100)
print(f"\n  {'':<20}" + "".join(f"{c:>14}" for c,_ in CAR))
for n,d in RUT:
    t=(7800./(9*G))/60 if n=='orbita baja' else tau(d)
    fila=""
    for c,m in CAR:
        tm=t_manejo(m); TB=tm+0.14+1.0
        L1=t+TB; L2=min(t+2,CO2) if t<CO2 else t; L4=t; L5=0.7*t
        E=0.1*L1+0.5*L2+0.1*L1+1.0*L4+0.8*L5
        fila+=f"{E:>13.1f}"
    print(f"  {n:<20}{fila}")
print(f"\n  -> la columna apenas cambia con la carga y **la fila cambia con la ruta como raiz(d)**:")
print(f"     **la exposicion es un problema de RUTA, no de CARGA.**")
print(f"  -> de Berlin a Marte la exposicion se multiplica por **{(tau(55e9)*2.4)/(tau(930e3)*2.4+0.5*CO2*0+2.0):.0f}**")
