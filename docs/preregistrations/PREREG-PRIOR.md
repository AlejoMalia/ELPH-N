# PREREG · PRIOR ANTROPOMÉTRICO · ¿cuánto compra de verdad saber sexo, edad, altura y peso?

Idea del investigador: una prelectura barata a partir de cuatro números que rellene la composición del cuerpo y
ahorre lectura. **La pregunta medible es: cuántos BITS de la especificación corporal compra ese prior.**

## TRIADA

**(1) INVENTARIO.** `data/antropo/male.csv` y `female.csv` = **ANSUR II**, con `Age`, `stature`, `weightkg`,
`Gender` **y ~93 medidas antropométricas más**. **El prior se puede medir, no estimar.**

**(2) MATEMÁTICA.** Bits que ahorra un prior que explica una fracción `R²` de la varianza de una magnitud
gaussiana: `Δbits = ½·log₂(1/(1−R²))`. Sumado sobre las 93 medidas da **el valor del prior en bits**, que es la
unidad del portador (D-330).

**(3) MATE.** Regresión lineal por mínimos cuadrados y el aparato de identificación de `docs/CAPAS.md` (C-003).

## Predicciones con número

- **P-P1.** El prior de 4 números explica **≥ 70 %** de la varianza media de las 93 medidas; mediana de `R²`
  ≥ 0,60.
- **P-P2.** Valor del prior: **60–150 bits** en total.
- **P-P3.** **El prior NO destruye la identificación:** con el residuo (lo que el prior no explica) la
  identificación top-1 entre los 6.068 a σ = 1 mm seguirá por encima del **95 %**. *Es decir: el prior se lleva
  el tamaño, y la identidad vive en el residuo.*
- **P-P4 · defecto del cascade propuesto.** En una rejilla realista de (edad, altura, peso, sexo), el residuo
  `proteína = magra − agua − hueso` del código sale **negativo en ≥ 5 %** de los casos: las tres fórmulas son
  regresiones independientes y **no imponen balance de masa**.
- **P-P5.** Calculando los elementos **desde los compartimentos** (como hace la primera versión) en vez de con
  una tabla fija (como hace la segunda), el oxígeno varía **≥ 2 puntos porcentuales** entre un joven delgado y
  un mayor obeso. *La tabla fija pierde exactamente la individualización que el prior aporta.*
