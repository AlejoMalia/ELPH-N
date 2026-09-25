"""D-664 corregido en D-667 · la placa de fiduciales del GATE-0.

  El multi-paso exige que al girar cada fiducial caiga DONDE ESTABA OTRO.
  Una rejilla cuadrada solo admite 90 grados -> n=4 -> ciega a 4t, que es la
  perpendicularidad X/Y de una fresadora de 3 ejes (D-664).

  Y el error en el BORDE no lo pone la topologia: lo pone si los puntos
  ALCANZAN el borde. Extrapolar r^4 cuesta 5x (D-667).

  PERO un anillo de radio R cae en x = 100+R: en una placa cuadrada de 200 mm
  NO PUEDE pasar de r=88, mientras que las esquinas de la rejilla llegan a 120,2.
  **Un reparto circular no alcanza las esquinas de un campo cuadrado. Nunca.**
  Luego o el CAMPO UTIL se hace redondo, o no hay giros. Keller & Stein usan
  placa circular: ahora se ve por que. El campo pasa a ser r <= 88 (D-667).
  Cuesta un 21 % de area; las 50 bolas siguen cabiendo al 25 % de ocupacion.
"""
import numpy as np
L, M, N_ANILLOS = 200.0, 5, 5           # campo, fiduciales por anillo, anillos
# D-721 · FASE ESCALONADA. El giro de n=5 exige que al rotar 72 grados cada fiducial
# caiga donde estaba otro, y **eso lo cumple CADA ANILLO POR SEPARADO**, sea cual sea
# su fase: un anillo de 5 puntos equiespaciados se mapea en si mismo. Luego la fase de
# cada anillo era un grado de libertad GRATIS que la placa ponia a cero en los cinco.
# El resultado era que los 25 fiduciales caian en 5 RADIOS: sin pares cortos fuera de
# un radio (ajuste anisotropo) y con solo 34 separaciones distintas de las 59 posibles.
FASE = 2*np.pi / (M*N_ANILLOS)          # 14,4 grados entre anillos consecutivos
C = np.array([L/2, L/2])
R_BORDE = 88.0                          # maximo que cabe en la placa: 100+88 = 188

def placa(radios=None):
    radios = np.linspace(26.0, R_BORDE, N_ANILLOS) if radios is None else radios
    return np.array([C + R*np.array([np.cos(2*np.pi*k/M + i*FASE),
                                     np.sin(2*np.pi*k/M + i*FASE)])
                     for i, R in enumerate(radios) for k in range(M)])

if __name__ == "__main__":
    import itertools
    P = placa(); r = np.hypot(*(P-C).T)
    d = [np.hypot(*(P[i]-P[j])) for i, j in itertools.combinations(range(len(P)), 2)]
    print(f"  {len(P)} fiduciales · r {r.min():.0f}-{r.max():.0f} mm "
          f"({'CUBRE' if r.max() >= R_BORDE-1 else 'EXTRAPOLA'} el borde r={R_BORDE:.0f})")
    R = np.array([[np.cos(2*np.pi/M), -np.sin(2*np.pi/M)],
                  [np.sin(2*np.pi/M),  np.cos(2*np.pi/M)]])
    Q = (R @ (P - C).T).T + C
    inv = all(np.min(np.linalg.norm(P - q, axis=1)) < 1e-9 for q in Q)
    print(f"  giro n=5 (72 grados) {'VALIDO' if inv else 'ROTO'} con fase escalonada de "
          f"{np.degrees(FASE):.1f} grados · armonicos ciegos 5 y 10 · el 4t SE SEPARA")
    print(f"  {len(set(np.round(d,1)))} separaciones distintas para ajustar alpha (la rejilla daba 14)")
    print(f"  CAMPO UTIL REDONDO r <= {R_BORDE:.0f} mm: -21 % de area, 50 bolas al 25 % de ocupacion")
