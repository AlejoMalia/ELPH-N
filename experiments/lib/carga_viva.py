"""D-670 · Si el humano es CARGA y no unidad medida, ¿que se complica?

  Lo que se cae: no hay que leer tejido. El humano no se mide, se CUSTODIA.
  Lo que se sostiene: los cinco criterios, pero sobre los fiduciales DE LA BURBUJA.
  Lo que se complica: **la carga esta VIVA y se mueve dentro.**

  Un humano que se desplaza dentro de una cascara redistribuye ~75 kg.
  Si eso flexa la cascara, MUEVE LOS FIDUCIALES DE FUERA.
  Carga puntual sobre cascara esferica:   w ~ k * P*R / (E*t^2),  k~0.2 (declarado)
"""
import numpy as np
P_N, R_M = 75*9.81, 1.0
K = 0.2                      # coeficiente de cascara somera. DECLARADO, no medido.
LECTOR_UM, SUELO_UM = 0.52, 141.0
print(f"  carga {P_N:.0f} N · radio {R_M} m · k = {K} (declarado)\n")
print(f"  {'material':<12}{'E (GPa)':>9}{'pared (mm)':>12}{'flexion (um)':>14}{'   frente a'}")
for mat,E in (("acero",200e9),("aluminio",70e9),("composite",50e9)):
    for t in (0.003,0.005,0.010):
        w = K*P_N*R_M/(E*t**2)*1e6
        rel = (f"{w/LECTOR_UM:>5.0f}x el lector · "
               f"{'DENTRO del suelo' if w<SUELO_UM else '**SUPERA el suelo de 141 um**'}")
        print(f"  {mat:<12}{E/1e9:>9.0f}{t*1000:>12.0f}{w:>14.1f}   {rel}")
print(f"\n  lector {LECTOR_UM} um · suelo de re-colocacion {SUELO_UM} um")
print("\n  -> La carga viva NO rompe nada: con pared >=5 mm la flexion cae DENTRO del suelo.")
print("     Pero es decenas de veces el lector, luego **entra en el presupuesto de error**")
print("     y obliga a declarar EN QUE ESTADO del ocupante se mide (regla 594: la ventana).")
