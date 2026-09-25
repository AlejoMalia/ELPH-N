"""D-685 · EL TIEMPO REAL DE UN ACTO. El transito es solo una parte, y casi nunca la mayor."""
import math,sys; sys.path.insert(0,'experiments/lib')
G=9.81; N_SUELO=10
def t_manejo(m):                       # DECLARADO, no medido
    return 0.5 if m<25 else (3.0 if m<1000 else 8.0)      # minutos por re-colocacion
def t_prep(n_ocup, m):                 # sujecion Eiband + sellado + rampa de presion
    return (0 if n_ocup==0 else 4.0*n_ocup) + 2.0 + 14.5/13.5
def t_verif(m):                        # lectura + Omega + FAR con N_IMP=1e5 + identidad
    return t_manejo(m) + 100_000*84e-6/60 + 1.0
CARGAS=[("1 tornillo",0.01,0),("1 persona",232.,1),("5 personas",1330.,5),
        ("1 elefante",21456.,0),("2 elefantes",50656.,0)]
RUTAS=[("Londres-Berlin",930e3),("Londres-Sidney",17_000e3),("orbita baja",400e3),
       ("Tierra-Luna",384_400e3),("Tierra-Marte",55e9)]
def fmt(t): return f"{t:.1f} min" if t<120 else (f"{t/60:.1f} h" if t<2880 else f"{t/1440:.1f} d")
print("\n  "+"="*110)
print("  EL ACTO COMPLETO A 9 g · suelo(A) + prep + TRANSITO + suelo(B) + verificacion\n")
print(f"  {'carga':<12}{'ruta':<17}{'suelo x2':>10}{'prep':>8}{'TRANSITO':>12}{'verif':>9}{'TOTAL':>11}{'% vuelo':>9}")
print("  "+"-"*110)
for nom,m,n in CARGAS:
    tm=t_manejo(m); ts=2*N_SUELO*tm; tp=t_prep(n,m); tv=t_verif(m)
    for rn,d in RUTAS:
        tt=(7800./(9*G))/60 if rn=='orbita baja' else 2*math.sqrt(d/(9*G))/60
        tot=ts+tp+tt+tv
        print(f"  {nom:<12}{rn:<17}{fmt(ts):>10}{tp:>6.1f} m{fmt(tt):>12}{tv:>7.1f} m{fmt(tot):>11}{100*tt/tot:>8.1f}%")
    print()
print("  "+"="*110)
print("  P2 · ¿A QUE DISTANCIA el transito empieza a dominar?\n")
for nom,m,n in CARGAS:
    tf=2*N_SUELO*t_manejo(m)+t_prep(n,m)+t_verif(m)
    d=9*G*(tf*60/2)**2
    print(f"  {nom:<12} coste fijo {fmt(tf):>9}  ->  el transito iguala al resto a **{d/1e6:>10,.0f} miles de km**"
          f"   ({'mas alla de la Luna' if d>384.4e6 else 'antes de la Luna'})")
print("\n  -> **Por debajo de esa distancia, el viaje es lo de menos.**")
