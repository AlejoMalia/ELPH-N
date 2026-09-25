# PREREG · cerrar la capa A · la métrica del contrato

## TRIADA paso 1 · INVENTARIO — los cuatro huecos son uno

| hueco | decisión |
|:--|:--|
| el punto de operación de Ω no es derivable | D-481 (recta, R² = 0,9987) |
| el contrato no es portable | D-500 (dividir por el suelo: 65,0 → 52,5 pts, e invierte el orden) |
| el contrato es manipulable subiendo el suelo | D-496 (×56 → pasa, cegando el instrumento) |
| `Ω ≤ 0,05` significa cosas distintas por tejido | el suelo varía 15× entre y 5,23× dentro |

**Los cuatro son el mismo hueco: la métrica del contrato es la equivocada.**
Ya cerrados: `d_medio`/`d_mínimo` (D-493), λ/d (D-497), columnas nulas (D-501).

## TRIADA paso 2 · la forma cerrada, ANTES de correr

Requisitos de una métrica `M` del contrato:

| | requisito |
|:--|:--|
| **(a) no manipulable** | empeora cuando empeora el instrumento |
| **(b) portable** | el mismo umbral significa lo mismo en cada tejido |
| **(c) umbral derivado** | no elegido a mano |

| candidata | (a) | (b) | (c) |
|:--|:--|:--|:--|
| Ω absoluto | ✓ | **✗** el suelo varía 15× | **✗** declarado |
| `Ω̃ = Ω/suelo = ⱎ²` | **✗** manipulable (D-496) | **✗** medido: 52,5 pts (D-500) | ✗ |
| **`A = ⱎ_imp/ⱎ_acto`** | **✓** medido: 1,840 → 1,433 al cegar (D-496) | **?** | **✓** `A > 1` es axioma de `CLAUDE.md` |

**Y aquí está la forma cerrada que decide (b):**

```
A = sqrt(Om_imp/suelo) / sqrt(Om_acto/suelo) = **sqrt(Om_imp/Om_acto)**
```

**El suelo se CANCELA exactamente.** Luego `A` es inmune por construcción a la variación de
suelo que mató a Ω y a Ω̃ — **algebraicamente, no por suerte.**

## Predicciones

- **P-A1 · el suelo se cancela exactamente**: `A` calculada como `√(Ω_imp/Ω_acto)` y como
  `ⱎ_imp/ⱎ_acto` coincidirán a precisión de máquina (< 1e-12).
- **P-A2 · la dispersión de `A` ENTRE espacios será menor que la de Ω̃.** Ω dio 65,0 pts de
  dispersión en R y Ω̃ dio 52,5. Predigo que **la dispersión relativa de `A` < 35 %**.
- **P-A3 · pero `A` NO será constante**: `Ω_imp` depende de la estructura del espacio (medido:
  ⱎ_imp 4,32 sintético frente a 14,21 en H01). Predigo dispersión ∈ [15 % , 60 %].
- **P-A4 · el ORDEN de dificultad será estable bajo `A`**, al revés que bajo Ω̃, que lo invirtió
  (malecns peor en absoluto y mejor en relativo).
- **P-A5 · la dispersión DENTRO de un espacio (semillas) será menor para `A` que para el suelo**
  (que variaba 5,23×), porque el cociente cancela el factor común.

---

# PREREG 2 · ¿beneficia el cierre de A a las otras capas?

## La vía concreta

`b_D` y `b_E` se ajustaron sobre `log(Ω − suelo)` frente a `log(Π)`. **El suelo varía 5,23 % por
semilla** (D-500). A `Π` pequeño, `Ω ≈ suelo` y la resta domina el punto: **eso pivota la
pendiente.** D-503 aporta un normalizador **sin ruido**: `Ω_imp` = 0,983 ± 0,41 %.

## Predicciones

- **P-B1 · ajustar `Ω/Ω_imp` frente a `Π` (sin restar el suelo) bajará la dispersión ENTRE
  espacios de `b_D` de 48,5 % a < 25 %.** *Si acierta, la no-portabilidad de D era un artefacto
  de la resta del suelo y D recupera su ley.*
- **P-B2 · también bajará la dispersión DENTRO de un espacio** (era 10,8 %), porque se quita del
  ajuste una magnitud ruidosa.
- **P-B3 · `b_E` seguirá portable** con el nuevo ajuste (ya lo era al 5,1 %).
- **P-B4 · los valores de `b` cambiarán**: sin restar el suelo la curva es más plana a `Π`
  pequeño, luego predigo `b` MENOR que con resta.
