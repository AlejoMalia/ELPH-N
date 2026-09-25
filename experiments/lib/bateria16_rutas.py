"""D-684 · BATERIA 16 · 5 cargas x 5 trayectos. Coste 0."""
import math,sys; sys.path.insert(0,'experiments/lib')
from alpha_gp import alpha_efectiva
G,E_MOD,K,RHO,SUELO = 9.81,200e9,0.5,7850.,141e-6
CO2_MIN = 15.8                                  # formula 29, independiente de n
CARGAS=[("1 tornillo",0.01,0.02,0),("1 persona",75.,1.26,1),("5 personas",375.,2.15,5),
        ("1 elefante",5000.,4.0,0),("2 elefantes",10000.,5.0,0)]
RUTAS=[("Londres-Berlin",930e3,False),("Londres-Sidney",17_000e3,False),
       ("orbita baja (LEO)",400e3,True),("Tierra-Luna",384_400e3,False),
       ("Tierra-Marte",55_000e3*1000,False)]
def caso(m,L,n,d,leo,g):
    a=g*G
    if leo:
        v=7800.; t=v/a; E_m=0.5*v**2+G*400e3        # llegar CON velocidad orbital
    else:
        t=2*math.sqrt(d/a); v=a*t/2; E_m=0.5*v**2
    tp=max(max(0.7e5*(L/2)/(2*200e6),0.004), math.sqrt(K*m*G*(L/2)/(E_MOD*SUELO)))
    M=RHO*4*math.pi*(L/2)**2*tp + m
    return t/60., M, E_m*M, alpha_efectiva(300.,'gauss',16.,max(L*1000*.9,20.)), v
print("\n  "+"="*108)
print(f"  A 9 g SOSTENIDOS (reclinado + traje).  CO2 en cabina sellada: {CO2_MIN} min\n")
print(f"  {'carga':<12}{'ruta':<20}{'tiempo':>11}{'v max':>11}{'masa':>10}{'energia':>11}{'alpha':>7}   VEREDICTO")
print("  "+"-"*108)
for nom,m,L,n in CARGAS:
    for rn,d,leo in RUTAS:
        t,M,E,al,v = caso(m,L,n,d,leo,9.)
        ok_g = al>=0.95; ok_co2 = (n==0) or (t<CO2_MIN)
        v_txt = f"{v/1000:.1f} km/s"
        t_txt = f"{t:.1f} min" if t<120 else f"{t/60:.1f} h"
        ver = ("PASA" if ok_g else "GATE-0") + ("" if ok_co2 else " + CO2")
        print(f"  {nom:<12}{rn:<20}{t_txt:>11}{v_txt:>11}{M:>9.0f}kg{E/1e12:>9.2f}TJ{al:>7.3f}   {ver}")
    print()
print("  "+"="*108)
print("  ¿Y SI SE VA COMODO, A 1 g?\n")
print(f"  {'ruta':<20}{'tiempo a 1 g':>15}{'¿cabe en 15,8 min?':>22}{'   soporte vital'}")
for rn,d,leo in RUTAS:
    t=(7800./G)/60. if leo else 2*math.sqrt(d/G)/60.
    tt=f"{t:.1f} min" if t<120 else (f"{t/60:.1f} h" if t<2880 else f"{t/1440:.1f} dias")
    print(f"  {rn:<20}{tt:>15}{'SI' if t<CO2_MIN else 'NO':>22}   {'sellada basta' if t<CO2_MIN else 'ECLSS OBLIGATORIO'}")
print("\n  "+"="*108)
print("  LA ORBITA BAJA ES DISTINTA Y VALE LA PENA MIRARLA\n")
v=7800.
print(f"     E/m minima = v^2/2 + g h = {0.5*v**2/1e6:.1f} + {G*400e3/1e6:.1f} = **{(0.5*v**2+G*400e3)/1e6:.1f} MJ/kg**")
print(f"     **Irreducible: no baja por ir mas despacio.** En todos los demas trayectos la")
print(f"     energia depende de cuanto aprietes; aqui la fija el DESTINO.")
for nom,m,L,n in CARGAS:
    t,M,E,al,_=caso(m,L,n,400e3,True,9.)
    print(f"     {nom:<12} masa total {M:>7.0f} kg -> {E/1e9:>8.1f} GJ = {E/3.6e12:.3f} GWh")
