# PREREG-VEREDICTO · el instrumento que dirá si hubo teletransporte

**Fecha:** 2026-09-19 · Cero nervioso.
**Se escribe ANTES de que exista el dato**, para que no se pueda ajustar después.

## Qué es esto

El dato que demuestra un teletransporte es **`Ω_acto` ≤ suelo**, con control negativo que falle, veredicto a
ciegas y fichero procedente de una medida. **El análisis que produce ese número se escribe ahora y se valida
sobre materia sintética**, donde conozco la respuesta — igual que validamos el simulador térmico contra las
criobolsas antes de usarlo (regla 257).

## El observable

Empaquetamiento granular de 10×10×10 = **1.000 granos**, mezcla conductor/aislante cerca de `p_c` ≈ 0,31.

| | qué es |
|:--|:--|
| **salida** | el campo de etiquetas 3D: qué tipo de grano hay en cada posición |
| **`Ω`** | 1 − corr(origen, destino) |
| **suelo** | dos lecturas del **mismo** montaje, con error de clasificación del µCT |
| **impostor** | las **posiciones permutadas** — una dirección equivocada |
| **prueba binaria** | ¿conduce el montaje? (percolación de la fase conductora) |

## MATEMÁTICA — antes de correr

Si se colocan mal `k` granos de `n`, la correlación cae ≈ `1 − 2k/n` para etiquetas binarias equiprobables,
luego **`Ω_acto` ≈ 2k/n**. Con `Ω_imp` ≈ 1, la banda es `A` ≈ √(n/2k). **El límite de detección `A` = 1,5 cae
en `k/n` ≈ 0,22.**

## Predicciones

- **P-D1** · con **cero error de colocación**, `Ω_acto` = suelo dentro de 1,3×. *El acto perfecto es
  indistinguible de volver a medir.*
- **P-D2** · el impostor da `Ω` > **0,9**.
- **P-D3** · el límite de detección (`A` = 1,5) está en **18–26 %** de granos mal colocados.
- **P-D4** · **la prueba binaria y el contrato son COMPLEMENTARIOS**: con pocos errores la binaria es más
  sensible (un grano puede cortar la percolación), con muchos se satura y el contrato sigue midiendo.
  *Si las dos se comportan igual, una de las dos sobra.*

## Lo que esto NO es

**No es el experimento.** Es el instrumento del veredicto, validado sobre materia sintética.
`validación contra materia` sigue en **0 %**.
