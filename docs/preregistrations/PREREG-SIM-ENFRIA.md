# PREREG · **simulación de enfriamiento sobre anatomía real** · y su validación previa

**Por qué simular aquí y no en otro sitio:** el marco ha fallado **dos veces** con el enfriamiento (D-539: 32 cm
por suponer superficie a temperatura fija; D-540/541: de 38 a 9 cm al leer los métodos). Las dos veces el error
fue de **geometría y condición de contorno**, que es justo lo que una cota cerrada no puede dar. **Simular aquí
no es circular: la geometría no está en la ley, está en el dominio.**

## TRIADA

**(1) INVENTARIO.** `data/antropo/caesar-norm-nh-fitted-meshes/`: **4.073 cuerpos humanos reales** con 6.449
vértices. De ahí sale una **sección transversal anatómica de verdad**, no una losa idealizada. Y hay un dato
publicado contra el que validar: criobolsas de **5,5 / 6,5 / 10,5 cm** de espesor, `K` = 2,006 °C·cm²/min,
`h` = 100 W/m²K.

**(2) MATEMÁTICA.** `∂T/∂t = α∇²T` con contorno de Robin `−k ∂T/∂n = h(T − T_baño)`. Propiedades del tejido
con crioprotector: α = 1,3e-7 m²/s, k ≈ 0,5 W/m·K. **Número de Biot** `Bi = h·L/k` ≈ 9–20 → conducción
dominante, la convección aporta poco: **si el simulador reproduce `K` = 2,006, el modelo está bien; si sale
mucho más rápido, falta física en el montaje real y hay que decirlo.**

**(3) MATE.** numpy en diferencias finitas. **Nada que instalar.**

## Predicciones con número

- **P-E1 · la validación, que es la que decide si el resto vale.** El simulador sobre la bolsa de 0,5 L
  (espesor 5,5 cm) dará una tasa dentro de **2×** de la implícita en `K` (1,39 °C/min). *Si sale > 5× más
  rápido, el montaje real tiene física que el modelo no tiene —contacto imperfecto, vapor, convección natural
  en el baño— y entonces la anatomía no se simula: se declara no simulable con este modelo.*
- **P-E2.** Una sección anatómica real enfría **más rápido** que la losa infinita de su mismo espesor, por
  efecto de borde: factor **1,2×–2×**.
- **P-E3.** A criterio de `CCR` = 0,1 °C/min: **brazo y pierna vitrifican, el tórax no.**
- **P-E4.** El espesor crítico que salga de la anatomía real estará entre **9 y 20 cm** — es decir, **entre el
  valor empírico del agente y mi cota idealizada**.
