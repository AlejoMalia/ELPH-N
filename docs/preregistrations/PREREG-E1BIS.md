# PREREG-E1BIS · **el primer experimento del programa sobre materia**

**Fecha:** 2026-09-18 · Sólo cuerpo humano completo. Cero nervioso.
**Lo que se juega:** la única pregunta que `A` = 15,08 (D-571) **no puede** contestar.

## La pregunta, en una línea

> **D-571 demostró que SI el campo de deformación es suave, el desajuste grasa/músculo sale casi gratis
> (`Ω` = 0,0044, `A` = 15,08). ¿Es suave el campo que produce el secado REAL, o desgarra?**

Eso no lo contesta ninguna simulación, porque la simulación **impuso** la suavidad. Lo contesta la materia.

## TRIADA

**INVENTARIO.** Tenemos la maquinaria de contrato completa (`om`, `arquitectura`, `permuta` en
`experiments/lib/` y `CONTRATO-CUERPO/`), el método de D-571 para **restar el movimiento común** a la escala
de registro declarada (2 arquitecturas), y las fracciones de agua por tejido. **No hace falta software nuevo:
el análisis ya está escrito.** Lo único que falta es el tejido.

**MATEMÁTICA — escrita antes de comprar nada.** El encogimiento sale del balance de masa con
`ρ_sólido` = 1,35 g/cm³:

| | agua | encogimiento lineal | masa final |
|:--|--:|--:|--:|
| **magro** (músculo) | 75 % | **1,716×** | 0,25× |
| **tocino** (adiposo) | 15 % | **1,074×** | 0,85× |

```
desajuste en la interfaz = **37,4 %**      perdida de masa de la loncha = **45 %**
```

Y el secado, **por las caras** (una loncha no tiene perfusión):

| espesor | tiempo de secado |
|--:|--:|
| 3 mm | **0,16 h** |
| 5 mm | 0,43 h |
| 10 mm | 1,74 h |

**MATE.** Se reutiliza `elastico.py` sin tocarlo: mismo `Ω`, mismo impostor, misma escala de registro.

## Montaje · **~100 €, una tarde**

**Es más barato que E1 y ataca algo que E1 no toca.**

1. **Panceta fresca** cortada en lonchas de **3 mm** — tiene capas alternas de magro y tocino con interfaz
   limpia. Es el único tejido de carnicería con la geometría exacta del problema.
2. **Marcar una rejilla** de puntos (tinta indeleble, paso ~2 mm) sobre la superficie.
3. **Fotografiar** a resolución conocida con una regla en el plano (≥ 10 px/mm).
4. **Secar** en desecador o estufa a 40 °C hasta masa constante. Pesar antes y después.
5. **Fotografiar** seco.
6. **Rehidratar** en solución salina, **en 7 pasos** de gradiente creciente (D-572), 10 min cada uno.
7. **Fotografiar** rehidratado. Pesar.

## Matriz de condiciones · **idea del investigador** · convierte el experimento en una dosis-respuesta

**Una sola condición da un sí/no. Cinco condiciones ordenadas dan una CURVA**, y por nuestra propia regla 322
una dosis-respuesta vale mucho más que un binario del mismo tamaño: es mucho más difícil de explicar por
artefacto. **Mismo tejido, mismo análisis, cinco tratamientos.**

| `T` | régimen | `p_vap` rel | `t` secado (3 mm) | gradiente | **predicción** |
|--:|:--|--:|--:|--:|:--|
| **−20 °C** | **sublimación (vacío)** | 0,05 | 34 min | **1,0×** | **sin encogimiento → `A` > 10** |
| 4 °C | capilar, frío | 0,35 | 15 min | 2,9× | `A` > 4 |
| 20 °C | capilar, ambiente | 1,00 | 9 min | 5,2× | `A` = 2–4 |
| 40 °C | capilar, estufa | 3,16 | 6 min | 9,7× | `A` = 1,2–2 |
| **70 °C** | **desnaturalización** | 13,34 | 3 min | 21,0× | **`A` < 1,5 · CONTROL NEGATIVO** |

**El gradiente de humedad crece monótonamente con `T`, y con él la tensión diferencial. La predicción del
marco es que `A` DECRECE monótonamente.**

> **Y el control negativo es lo que de verdad añade tu idea: la carne cocida a 70 °C está desnaturalizada, es
> irreversible por definición. Si ese caso NO da `A` < 1,5, la medida está rota y no hay que creerse ninguna
> de las otras filas.** Sin control negativo, un `A` alto podría ser insensibilidad del instrumento.

**Coste añadido: cero.** Es la misma panceta, el mismo análisis y un horno que ya existe en cualquier cocina.

## Predicciones · se juzgan por el número

- **P-B1** · el magro encoge **1,60–1,85×** lineal y el tocino **1,03–1,15×**. *Valida el balance de masa
  sobre materia por primera vez.*
- **P-B2** · pérdida de masa de la loncha **40–50 %**.
- **P-B3** · el desajuste medido en la interfaz cae entre **30 y 45 %**, confirmando el 37,4 % derivado.
- **P-B4** · **la que importa**: tras rehidratar, el campo residual —restado el movimiento común a 2
  arquitecturas— es **SUAVE** en la fila de 4 °C: `Ω` < **0,05** y `A` > **4**.
- **P-B6** · **`A` decrece MONÓTONAMENTE** de −20 °C a 70 °C, sin inversiones.
- **P-B7** · **el control negativo de 70 °C da `A` < 1,5.** *Si no, la medida está rota y el resto no vale.*
- **P-B5** · la recuperación dimensional tras rehidratar es **≥ 85 %** del original.
- **P-B8** · **la contracción del magro es ANISÓTROPA**: razón transversal/axial entre **1,3 y 2,3**.
  *Si sale 1,0, el modelo isótropo era correcto y `A` = 15,08 se sostiene. Si sale > 1,5, el campo tiene
  estructura a escala de arquitectura y COMPRIMIR vuelve a estar en duda* **(D-582)**.

## Qué se mide en cada pieza · lista cerrada

| dimensión | por qué |
|:--|:--|
| **largo · ancho · grosor**, por separado | **prueba la isotropía** — la raíz cúbica la suponía |
| masa antes / seca / rehidratada | balance de masa (P-B1, P-B2) |
| temperatura interna y superficial | convierte el gradiente de nominal en **medido** |
| rejilla fotografiada en las 3 fases | `Ω` y `A` — **la medida principal** |
| orientación de la fibra (‖ y ⊥ a la rejilla) | separa anisotropía de desajuste grasa/músculo |
| pardeamiento (foto) | **marcador de régimen**: dice cuándo se cruzó a lo irreversible |

**Fuera, y por qué:** *distancia a la fuente* — el calentamiento radiante mete un gradiente **espacial** que se
confunde con el diferencial que queremos medir (regla 329); para el contrato, condiciones **uniformes**.
*Textura* — `Ω` contesta lo mismo mejor; se anota sólo si sale gratis.

## Qué refuta qué

| resultado | lectura |
|:--|:--|
| `A` > 4 y sin desgarro visible | **el campo es suave: D-571 se sostiene sobre materia** |
| `A` < 1,5, o delaminación en la interfaz | **el campo desgarra: `A` = 15,08 era un artefacto de imponer suavidad**, y COMPRIMIR vuelve a fallar |
| P-B1 falla | **el balance de masa está mal**, y con él toda la §2 del marco |

## Lo que este experimento sí hace

**Es el primero del programa que toca materia.** Mueve `validación contra materia` de **0 %** a un número
distinto de cero: valida **el balance de masa, el desajuste diferencial y la naturaleza del campo** — 3 de las
12 condiciones del marco LCER.

**Lo que NO hace:** no toca trehalosa, ni vidrio, ni vasculatura, ni arranque. **Un experimento no cierra un
marco.**
