# PREREG · ¿existe máquina que coloque a σ* ≤ 204 nm?

## TRIADA paso 2 · las cotas, ANTES de mirar catálogos

Dos preguntas distintas y hay que separarlas:

1. **precisión**: ¿hay tecnología con 204 nm de precisión de colocación?
2. **permanencia**: ¿se QUEDA ahí? Una célula en fluido difunde por Brownian.

**La segunda nadie la ha planteado en este programa**, y es una cota cerrada:
`⟨x²⟩ = 2Dt` con `D = kT/(6πηr)` (Stokes-Einstein), r = 5 µm, T = 310 K.

### Predicciones

- **P-M1 · la precisión de 204 nm la alcanza tecnología existente** (polimerización de dos
  fotones ~100-200 nm, pinzas ópticas ~100 nm). **No es el bloqueo.** Y sobre una célula de
  10 µm, 204 nm son **2 % de precisión relativa** — nada exótico.
- **P-M2 · en agua (η = 1e-3 Pa·s) el tiempo hasta salirse de 204 nm será < 1 s**, central
  **0,5 s**. *Si es así, el cuerpo entero tendría que montarse en ese tiempo, o inmovilizar
  cada célula al instante.*
- **P-M3 · con la tinta del marco (`mu_bioink` = 0,1 Pa·s, 100× el agua) el tiempo sube ~100×,
  a ~46 s.**
- **P-M4 · la tasa de colocación exigida en esa ventana superará por ≥ 100× cualquier sistema
  paralelo demostrado.**
- **P-M5 · y aparecerá una arista NUEVA en la red**: la viscosidad compra tiempo contra Brownian
  pero el esfuerzo de corte mata células — **eso es exactamente `Q_boquilla = τ/µ`, una de las
  cuatro cifras anchas de C.** *La tolerancia de E quedaría acoplada a una cifra de C que nadie
  había conectado con ella.*
