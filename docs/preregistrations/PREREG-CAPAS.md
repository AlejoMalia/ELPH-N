# PREREG · proyectar las capas como dimensiones sobre el veredicto de F

## El riesgo, escrito antes

**Las capas no son objetos del mismo tipo:** D y E son magnitudes de error (se **componen**),
A es un umbral (se **compara**), C es incertidumbre de las cifras (se **propaga**), B está
cerrada (es una **referencia fija**), G está fuera. **Una matriz 6×6 cruzándolas sin más sería
la novena inconmensurabilidad del programa.**

**La versión bien planteada:** todo entra en **F**. Se hace Sobol con el veredicto de F como
salida y un parámetro por capa.

## Por qué esta vez SÍ puede haber interacción

D-483 midió `S_ij` = 0,0000 exacto y lo delaté como **teorema de mi álgebra**: el modelo era
multiplicativo y en log es aditivo. **Aquí la composición D×E es una UNIÓN SUB-ADITIVA**
(`max ≤ unión ≤ suma`, razón medida 0,77–0,80 en dos substratos), **que no es multiplicativa.**
Luego la interacción, si existe, puede aparecer.

## Parámetros, uno por capa

| capa | parámetro | rango | procedencia |
|:--|:--|:--|:--|
| **A** | `Ω_c` | [0,03 , 0,10] | envolvente de D-481 |
| **B** | — | **fijo** | cerrada (D-433) |
| **C** | `e_C` (incertidumbre residual) | [0 , 0,40] | 4 cifras anchas de 10 |
| **D** | `Π` = `e1`×ExM | [0,0136 , 0,0624] | D-486 |
| **E** | `d` para la tolerancia | [1,55 , 12,77] µm | **la conflación de D-490** |
| **F** | razón de unión `r` | [0,769 , 0,803] | medida en dos substratos |
| — | `p_fallo` | [0,10 , 0,50] | biología |

## Predicciones

- **P-C1 · esta vez la interacción total será NO nula**: predigo ∈ [0,05 , 0,30], central 0,15.
  *Si vuelve a salir 0,0000, el modelo sigue siendo multiplicativo y hay que decirlo.*
- **P-C2 · la capa dominante será E**, no D, porque la conflación de `d` la movió 8,2× hoy.
  Predigo `S₁(E) > S₁(D)`.
- **P-C3 · la capa F (razón de unión) aportará < 0,05**, porque su rango medido es estrecho
  (0,769–0,803).
- **P-C4 · existirá al menos un par de capas con `S_ij` > 0,03.** *Ésa sería la sinergia que el
  investigador busca, y sería la primera medida del programa.*
