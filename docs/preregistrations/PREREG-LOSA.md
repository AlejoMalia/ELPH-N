# PREREG-LOSA · la única condición «al filo» del marco, atacada con geometría real

**Fecha:** 2026-09-18 · **Sólo cuerpo humano completo.** Cero nervioso.

## 0 · Qué está en blanco y por qué

El marco físico tiene **una condición en `N` = 1,000**: el espesor de la losa de tronco (`L/L_crítico` =
9,0/9,0). Un marco serio no opera en `N` = 1 (D-545). Y ese 9,0 cm sale de una **cota cerrada 1D que supone
que la losa se enfría SÓLO por sus dos caras cortadas** (D-541). **Una losa real está sumergida entera: también
se enfría por su piel lateral.** Ahí decide la geometría, no la ley — que es el único caso en que simular no es
circular (D-551).

## 1 · TRIADA

**INVENTARIO.** El simulador está escrito y **validado contra las tres criobolsas publicadas** dentro de
1,20–1,30× con sesgo constante (D-551, regla 257). Las secciones reales de CAESAR están medidas en
`experiments/SIM-ENFRIA/results/anatomia.json`. No hay que medir nada nuevo.

**MATEMÁTICA — escrita antes de correr.** Para una losa de espesor `e` = 9 cm y anchura `W`, el radio
hidráulico de la sección vertical es `L_C = eW/(2e+2W)` frente a `e/2` en el caso 1D de dos caras. Con la tasa
∝ `L_C⁻²`:

| | `L_C` | ganancia | `N` predicho |
|:--|--:|--:|--:|
| 1D, dos caras cortadas (D-541) | 4,50 cm | — | 1,000 |
| losa 9 × 44 cm (calibre mínimo del abdomen) | **3,74 cm** | **1,45×** | **0,83** |
| losa 9 × 71 cm (anchura con brazos) | **3,99 cm** | 1,27× | 0,89 |

**MATE.** Se reutiliza `simula()` de `SIM-ENFRIA/code/enfria2d.py` sin tocarla.

## 2 · Predicciones · se juzgan por el número, no por el signo

- **P-L1** · la losa de 9 × 44 cm se enfría **1,35–1,55×** más rápido que la cota 1D de dos caras.
- **P-L2** · `N` del espesor de losa cae de 1,000 a **0,80–0,87**: **la condición al filo pasa**.
- **P-L3** · la ganancia **decrece** al ensanchar la losa: la de 9 × 71 cm gana menos que la de 9 × 44 cm.
- **P-L4** · el espesor crítico de losa sube de 9,0 cm a **10,5–11,5 cm**, lo que baja el número de losas
  de tronco de 6 a 5 si se rediseña.

## 3 · Lo que este experimento NO puede cerrar, y se declara antes

**El indeciso del muslo (26,6 cm, 1,23×) no se cierra simulando en 3D.** Cota cerrada: la profundidad de
penetración axial en el tiempo de vitrificación es `√(αt)` = √(1,3e-7 · 1,4e4) = **4,3 cm**, frente a los ~40 cm
de longitud del muslo. **La conducción axial no llega al centro del muslo**, así que una simulación 3D dará el
mismo número que la 2D. El indeciso del muslo es **DESCONOCIDA que exige medir**, no simular: sale del sesgo
20–30 % del simulador, y sólo lo cierra un enfriamiento instrumentado en pieza real (regla 229).

**Y sigue sin moverse la `validación contra materia` = 0 %.** Esto mueve `cumplimiento`, no evidencia.
