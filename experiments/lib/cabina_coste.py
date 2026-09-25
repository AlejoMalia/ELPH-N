"""D-689 · Q5-Q8 · coste, energía, control y materiales de la cabina."""
import math
G,K,SUELO=9.81,0.5,141e-6
MAT={  # nombre: (rho kg/m3, E Pa, EUR/kg, comentario)
 "acero 316L":      (7850.,200e9, 7.,"commodity · sin DBTT · soldable y conformable"),
 "aluminio 5083":   (2700., 70e9, 5.,"commodity · sin DBTT · muy conformable"),
 "titanio Ti-6Al-4V":(4430.,114e9,45.,"caro, no commodity"),
 "composite CFRP":  (1600., 70e9,60.,"caro · y NO es monolitico: se lamina"),
}
print("  "+"="*100); print("  Q5 · COSTE POR MATERIAL Y TAMANO"); print("  "+"="*100)
print("\n  La pared la fija la flexion por carga viva: t = raiz(k m g (L/2)/(E x suelo))")
print("  luego  t ~ 1/raiz(E)  y  masa ~ rho/raiz(E). **Esa es la figura de merito.**\n")
print(f"  {'material':<20}{'rho/raiz(E)':>13}{'   relativo al acero'}")
base=7850./math.sqrt(200e9)
for m,(r,E,p,c) in MAT.items():
    f=r/math.sqrt(E)
    print(f"  {m:<20}{f:>13.5f}{f/base:>15.2f}x")
print()
CASOS=[(0.3,1.,"caja 30 cm · 1 kg"),(1.26,75.,"1 persona"),(2.15,375.,"5 personas"),(4.0,5000.,"1 elefante")]
print(f"  {'cabina':<22}{'material':<20}{'pared':>9}{'masa':>10}{'COSTE material':>16}")
for L,m,nom in CASOS:
    for mat,(r,E,p,c) in MAT.items():
        t=max(max(0.7e5*(L/2)/(2*200e6),0.004), math.sqrt(K*m*G*(L/2)/(E*SUELO)))+0.0015
        M=r*4*math.pi*(L/2)**2*t
        print(f"  {nom:<22}{mat:<20}{t*1000:>7.1f}mm{M:>8.0f}kg{M*p:>14,.0f} EUR")
    print()
print("  "+"="*100); print("  Q6 · GASTO DE ENERGIA · ¿quien consume de verdad?"); print("  "+"="*100)
print(f"\n  {'concepto':<40}{'potencia':>12}{'en un acto de 95 min':>24}")
for c,P,nota in (("cabina: sensores, luz, comms, ventilacion",100.,"a bordo, almacenada"),
                 ("sala de metrologia a +-1 K (36 m2)",3000.,"clima, continuo"),
                 ("lector optico + computo",300.,"solo durante la lectura"),
                 ("grua (10 ciclos x 3 min)",5000.,"intermitente")):
    print(f"  {c:<40}{P:>10.0f} W{P*95/60/1000:>20.2f} kWh   {nota}")
tot=(100+3000+300)*95/60/1000+5000*30/60/1000
print(f"\n  TOTAL de estacion por acto: **{tot:.1f} kWh**  frente a los **0,124 kWh** de la cabina")
print(f"  -> **la ESTACION consume {tot/0.124:.0f} veces mas que la CABINA.**")
print(f"  -> y eso es SIN contar el transito, que para 1 persona a Berlin son {0.01e12/3.6e6:.0f} kWh.")
print(f"     **El transito es {0.01e12/3.6e6/tot:.0f} veces la estacion. El orden es: transito >> estacion >> cabina.**")
print("\n  ¿depende de lo que lleva dentro? SI, por DOS vias:")
print("     masa -> energia de transito (E ~ M v^2/2)          **lineal en la masa**")
print("     masa -> tamano de cabina -> sala mas grande        **la sala escala como L^2**")
print("  ¿y la cabina en si? NO: 100 W son 100 W lleve un tornillo o un elefante.")
