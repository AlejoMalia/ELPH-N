# PREREG · **el coste de laminar** y **la predicción del demostrador**

Dos pruebas con cota cerrada. Ninguna necesita laboratorio. Cero nervioso.

## TRIADA

**(1) INVENTARIO.** D-541: el cuerpo se lamina en **9 losas de 9 × 30 × 30 cm** porque el espesor crítico de
vitrificación es 9,0 cm. El demostrador propuesto lee en BM18 (**8–25 µm**). D-539: el contrato de arquitectura
está medido sobre histología cardíaca humana a 4,10 µm/px, y exige **20× más fino que la arquitectura**.

**(2) MATEMÁTICA · escrita antes.**

*Coste de laminar.* Cortar en 9 losas crea **8 planos internos**. Por cada plano:
- **vasos que hay que suturar**: los de calibre suficiente. Con Murray (`N(r) ∝ r⁻³`) y conservación de
  caudal, el número que cruza un plano lo fija el caudal distal: `N = (Q_distal/Q_total)·(r_aorta/r)³`.
- **capilares seccionados**: `área del plano × densidad capilar`. **Esos no se suturan.**
- **superficie de herida interna**: `8 × área`, que se compara con la superficie corporal (1,9 m²).

*Demostrador.* El contrato ya está medido a 5, 10, 25, 50 y 100 µm sobre tejido real. **BM18 lee a 8–25 µm.**
Basta leer la tabla de D-539 en ese punto: **no hay que correr nada nuevo.**

**(3) MATE.** `barato.py` de D-539 y la geometría de D-541.

## Predicciones con número

**Laminar**

- **P-L1.** Vasos a suturar por plano: **entre 5 y 20**; en total **40–160**, no los 8 que se dijo.
- **P-L2.** Capilares seccionados por plano: **10⁷–10⁸**; en total **≥ 10⁸**, es decir **≥ 1 %** de los 10¹⁰
  del cuerpo.
- **P-L3 · la que decide.** La superficie de herida interna será **comparable a la superficie corporal**:
  predigo entre **0,3× y 1×** de los 1,9 m² de piel. *Si sale de ese orden, la laminación deja de ser un
  detalle de montaje y pasa a ser el problema principal de la arquitectura.*

**Demostrador**

- **P-D1.** A la resolución de BM18 (8–25 µm), `Ω` del acto estará **entre 0,09 y 0,39** — muy por encima del
  contrato de 0,05.
- **P-D2.** `A` estará entre **1,6 y 3,3**: el contrato **existe** pero **no pasa fidelidad**.
- **P-D3 · el aviso.** **El demostrador, tal y como está especificado, fallaría su propia verificación**, y no
  por la fabricación: **por leer a 8–25 µm cuando su contrato exige 5 µm.** *Si me equivoco y pasa, la
  exigencia de 20× de D-539 estaba mal.*
