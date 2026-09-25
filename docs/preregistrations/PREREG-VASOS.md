# PREREG · VASCULARIZAR A ESCALA DE MÓDULO · 100 % cuerpo

De D-526 quedan dos cosas en el módulo geométrico: **montar con vasos** y **arrancar**. Aquí la primera.
Lo demostrado: **4 mm de espesor perfundible (~0,31 mL)**. Lo exigido: **un módulo de 2 L** (D-522).
**6.400× en volumen.** La pregunta es si ese 6.400× es de verdad el factor que hay que salvar.

## TRIADA

**(1) INVENTARIO.** D-526: límite de difusión 100–200 µm por tres rutas; la microvasculatura **se
autoensambla** a partir de canales impresos; 11.000 km de capilar en el cuerpo, que **no se imprimen**.
D-522: 35 módulos de 2 L. D-356: andamio vascular, fracción vascular ~5 % (EXTERNA).

**(2) MATEMÁTICA · escrita antes de buscar nada.**

- **El 6.400× en volumen NO es el factor de dificultad.** Si lo que se imprime es una **rejilla de canales**
  separados `s` y el resto se autoensambla, la longitud impresa es `L = V/s²` — **lineal en volumen**, y el
  espesor deja de ser una barrera. Con `s` = 1–2 mm y V = 2 L: `L` = **0,5–2 km por módulo**.
- **La jerarquía es logarítmica.** Con ley de Murray (`r_{n+1} = r_n·2^(−1/3)`), pasar de una arteria nutricia
  de `r₀` a terminales de 100 µm cuesta `N = 3·log₂(r₀/r_term)` generaciones. Con `r₀` = 2 mm: **N ≈ 13**,
  y **2¹³ ≈ 8.200 terminales**. *Multiplicar el volumen por 6.400 añade sólo `log₂(6400)/3` ≈ **4
  generaciones**.*
- **Perfusión.** Un módulo de 2 L de músculo en reposo consume del orden de 2–4 mL de sangre/min por 100 g →
  **40–80 mL/min**. Poiseuille dice si una sola nutricia de 2 mm lo sostiene.

**(3) MATE.** `tejido.py`, `vivo.py`, `cuerpo.py`. Cero cómputo pesado, cero nervioso.

## Predicciones con número

- **P-Va1.** La longitud impresa por módulo sale **0,5–2 km**, y para el cuerpo entero **17–70 km**.
- **P-Va2.** A velocidades de bioimpresión publicadas, imprimir un módulo tarda **< 1 semana**, y los 35
  módulos **caben en el año de montaje**. *Si no cabe, la vascularización pasa a ser el cuello del montaje.*
- **P-Va3.** La jerarquía completa del módulo son **≈ 13 generaciones** y **< 10⁴ terminales impresos**: el
  salto de 0,31 mL a 2 L son **≈ 4 generaciones más**, no 6.400 veces más trabajo.
- **P-Va4.** Una sola arteria nutricia de **2 mm** basta para los 40–80 mL/min del módulo, con caída de presión
  **< 20 mmHg** en el tramo grande.
- **P-Va5 · la que decide.** El cuello **no** será la impresión sino **la distancia que la microvasculatura
  autoensamblada es capaz de salvar** entre canales: si la literatura la sitúa en ~1 mm, `s` no puede subir y
  `L` se queda donde está; si llega a varios mm, `L` cae con el cuadrado.
