"""D-668 · alpha deja de ser SOLO nuestro: sale del nucleo del proceso gaussiano.

  El gremio de la metrologia de CMM no publica "D(r)=C r^alpha": modela el campo
  de error como un PROCESO GAUSSIANO con una longitud de correlacion upsilon
  (100-500 mm tipicos). Pero las dos cosas son la MISMA, y el puente es la
  FUNCION DE ESTRUCTURA:

      D(r) = || u(x) - u(x+r) ||  ->  D^2(r) = 2 d [C(0) - C(r)]

  nucleo gaussiano    C = s^2 exp(-(r/u)^2)  ->  r<<u:  D ~ r      ALPHA = 1
  nucleo exponencial  C = s^2 exp(-r/u)      ->  r<<u:  D ~ r^0,5  ALPHA = 0,5

  => nuestro umbral alpha>=0,95 EXIGE un campo diferenciable en media cuadratica.
     Un campo de correlacion exponencial da 0,5 y NO PASA NUNCA.
"""
import numpy as np
def alpha_efectiva(ups, nucleo, rmin=16., rmax=176.):
    r = np.geomspace(rmin, rmax, 60)
    C = np.exp(-(r/ups)**2) if nucleo == 'gauss' else np.exp(-r/ups)
    D = np.sqrt(np.maximum(2*(1-C), 1e-300))
    return np.polyfit(np.log(r), np.log(D), 1)[0]

if __name__ == "__main__":
    print("  alpha que MEDIRIA el GATE-0 sobre separaciones de 16 a 176 mm:\n")
    print(f"  {'upsilon (mm)':>13} {'nucleo gaussiano':>18} {'nucleo exponencial':>20}   veredicto GATE-0")
    for u in (100., 200., 300., 500., 1000., 3000.):
        a, b = alpha_efectiva(u,'gauss'), alpha_efectiva(u,'exp')
        v = 'PASA' if a >= 0.95 else ('VETO' if a < 0.35 else 'INTERMEDIO')
        print(f"  {u:>13.0f} {a:>18.3f} {b:>20.3f}   gauss: {v:<10} exp: "
              f"{'PASA' if b>=0.95 else ('VETO' if b<0.35 else 'INTERMEDIO')}")
    print("\n  -> Con nucleo EXPONENCIAL el GATE-0 no pasa NUNCA, a ninguna upsilon.")
    print("  -> Con nucleo GAUSSIANO hace falta upsilon >> nuestro campo.")
    for lim in (0.95,):
        for u in np.geomspace(100,20000,400):
            if alpha_efectiva(u,'gauss') >= lim:
                print(f"  -> alpha>=0,95 exige upsilon >= {u:.0f} mm = {u/176:.1f} veces el campo.")
                break
