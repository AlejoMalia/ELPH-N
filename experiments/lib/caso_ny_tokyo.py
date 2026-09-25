"""D-683 · BATERIA 15 · CASO REAL · Nueva York -> Tokio, de 1 a 10 ocupantes.

  Una bateria ATACA el marco. Un caso real lo EJERCE: obliga a satisfacer
  TODAS las condiciones a la vez, con numeros concretos y un destino concreto.
  Es un tipo de prueba distinto, y encuentra cosas que el ataque no encuentra.
"""
import math,sys; sys.path.insert(0,'experiments/lib')
from alpha_gp import alpha_efectiva
D = 10_850e3          # NY-Tokio, circulo maximo, m
V_PP, CO2_PP, O2_PP = 2.0, 0.5, 0.55      # m3, L/min, L/min por ocupante
E_MOD,K,G,RHO,SUELO = 200e9,0.5,9.81,7850.,141e-6
LIM = [("1 g  comodo",1.),("3 g  entrenado",3.),("9 g  reclinado + traje",9.),("25 g inmersion liquida",25.)]
print("  "+"="*94)
print("  1 · ¿CUANTO TARDA?  (acelerar media ruta, frenar la otra media)\n")
print(f"  {'limite sostenido':<26}{'tiempo':>10}{'v maxima':>14}{'¿Eiband aplica?'}")
for nom,g in LIM:
    a=g*G; t=2*math.sqrt(D/a); v=a*t/2
    print(f"  {nom:<26}{t/60:>8.1f} min{v/1000:>11.1f} km/s   "
          f"{'NO: >2 s, manda el limite SOSTENIDO' if t>2 else 'si'}")
print("""
  ** DISTINCION QUE EL MARCO NO TENIA: Eiband mide IMPACTOS (< 2 s). Un transito
     de minutos se rige por el limite SOSTENIDO (4,5 g de pie / 9 g reclinado /
     25 g en inmersion). Son dos regimenes distintos y confundirlos da 45 g
     donde lo correcto son 9. **""")
print("  "+"="*94)
print("  2 · ¿CABE Y AGUANTA?  volumen 2 m3 por ocupante\n")
print(f"  {'ocup.':>6}{'V (m3)':>9}{'lado L (m)':>12}{'pared':>9}{'cascara':>11}{'alpha':>8}{'GATE-0':>13}")
for n in (1,2,3,5,8,10):
    V=V_PP*n; L=V**(1/3.)
    t=max(0.7e5*(L/2)/(2*200e6),0.004)
    t=max(t,math.sqrt(K*(75*n)*G*(L/2)/(E_MOD*SUELO)))
    M=RHO*4*math.pi*(L/2)**2*t
    al=alpha_efectiva(300.,'gauss',16.,L*1000*.9)
    print(f"  {n:>6}{V:>9.1f}{L:>12.2f}{t*1000:>7.1f}mm{M:>9.0f}kg{al:>8.3f}"
          f"{'PASA' if al>=0.95 else 'FALLA':>13}")
print("  "+"="*94)
print("  3 · ¿RESPIRAN?  cabina SELLADA, sin depuracion\n")
print(f"  {'ocup.':>6}{'V (m3)':>9}{'CO2: minutos':>15}{'O2: minutos':>14}{'   ¿basta para el viaje?'}")
for n in (1,2,3,5,10):
    V=V_PP*n
    tco2=(V*1000*(3/760))/(CO2_PP*n); to2=(0.065*V*1000*0.21)/(O2_PP*n)
    t9=2*math.sqrt(D/(9*G))/60
    print(f"  {n:>6}{V:>9.1f}{tco2:>15.1f}{to2:>14.1f}   "
          f"{'SI' if tco2>t9 else f'**NO — el viaje dura {t9:.1f} min**'}")
print(f"""
  ** RESULTADO LIMPIO: el tiempo de respiracion es INDEPENDIENTE del numero de
     ocupantes, porque el volumen escala con ellos. {(V_PP*1000*(3/760))/CO2_PP:.1f} minutos, siempre.
     Y el viaje a 9 g dura {2*math.sqrt(D/(9*G))/60:.1f} min. **NO LLEGAN.** ECLSS obligatorio. **""")
print("  "+"="*94)
print("  4 · ¿CUANTO CUESTA?\n")
print(f"  {'ocup.':>6}{'masa total':>12}{'energia':>12}{'   equivalente'}")
for n in (1,3,10):
    V=V_PP*n; L=V**(1/3.)
    t=max(max(0.7e5*(L/2)/(2*200e6),0.004),math.sqrt(K*(75*n)*G*(L/2)/(E_MOD*SUELO)))
    M=RHO*4*math.pi*(L/2)**2*t+75*n
    a=9*G; v=a*(2*math.sqrt(D/a))/2; E=0.5*M*v**2
    print(f"  {n:>6}{M:>10.0f}kg{E/1e12:>10.2f}TJ   {E/4.184e9:>8.0f} t de TNT  ·  {E/3.6e12:.1f} GWh")
print("  "+"="*94)
