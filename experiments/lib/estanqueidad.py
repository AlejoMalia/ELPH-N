"""D-668 · O2 a traves del sello, con la banda de la NASA como criterio de fallo.

  Permeacion (UC Components, 1e-8 sccm*cm/(s*cm2*atm)):  N2: EPDM 6-7 · FKM 0,05-0,7
  La tabla NO trae O2 (el listado externo lo daba por hecho y no esta).
  O2 permea tipicamente 3-4x mas que N2 en elastomeros -> se acota con x4. DECLARADO.

  Criterio de fallo: NASA OCHMO-TB-002 [V2 6005], ppO2 en 145-155 mmHg.
  Salir de la banda = perder 10/155 = 6,5 % del O2.
"""
V_M3, D_SELLO_M, CORDON_CM, CONTACTO_CM = 2.0, 1.0, 1.0, 0.3
DP_O2_ATM = 0.21              # burbuja a 1 atm de aire, exterior en vacio
A = 3.1416*D_SELLO_M*100*CORDON_CM
O2_TOTAL = V_M3*1e6*0.21      # cm3 STP
print(f"  burbuja {V_M3} m3 · sello D={D_SELLO_M} m, cordon {CORDON_CM} cm, contacto {CONTACTO_CM} cm")
print(f"  area de permeacion {A:.0f} cm2 · O2 a bordo {O2_TOTAL:.0f} cm3 STP · dp {DP_O2_ATM} atm\n")
print(f"  {'material':<10}{'P(N2)':>10}{'P(O2)~4xN2':>13}{'fuga':>16}{'salir de la banda NASA':>26}")
for mat,pn2 in (("EPDM",6.5e-8),("FKM/Viton",4e-9)):
    po2=4*pn2
    q=po2*A*DP_O2_ATM/CONTACTO_CM          # cm3 STP/s
    dias=0.065*O2_TOTAL/(q*86400)
    print(f"  {mat:<10}{pn2*1e8:>9.2f}e-8{po2*1e8:>12.2f}e-8{q*86400:>12.2f} cm3/d{dias:>20.0f} dias ({dias/365:.0f} a)")
print("\n  -> La PERMEACION no es el cuello: tarda anos. El cuello es la FUGA")
print("     ALREDEDOR del sello, que es otra magnitud y se presupuesta aparte (regla 571).")
