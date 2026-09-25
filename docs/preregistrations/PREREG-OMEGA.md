# PREREG · derivar el contrato Ω · escrito ANTES

## TRIADA paso 1 · INVENTARIO — cuál de los cuatro métodos vale aquí

| método del investigador | veredicto | por qué |
|:--|:--|:--|
| **3 · estabilidad / bifurcación** | **VALE, y es el mejor** | el marco YA es un sistema dinámico iterado (`corre()`: mapa tanh a 250 pasos). El umbral de decidibilidad es medible. |
| **1 · rodilla de Pareto** | **VALE** | tengo `A(e_conn)` medida en 6 puntos (D-477). La rodilla es un punto de máxima curvatura: único, no elegido. |
| 2 · rate-distortion | **parcial** | la parte de **percolación** sí es derivable y dura (`f_c = 1 − 1/z`); la parte de Shannon exigiría una capacidad de canal que no tengo medida. Se usa sólo la percolación. |
| 4 · Bayes empírico | **CIRCULAR — se descarta** | los datos «consolidados» se generaron **usando Ω ≤ 0,05 como criterio de PASA**. Inferir Ω de ellos es leer mi propia declaración de vuelta. Es el caso más limpio de circularidad de toda la sesión. |

**Se derivan TRES cotas por caminos independientes y se triangulan.**

## TRIADA paso 2 · las cotas, escritas antes de correr

`Ω = 1 − corr(salida_origen, salida_destino)` · ley medida `Ω = suelo + 2,0531·e_conn^0,6388`
(R² = 0,99869, D-480).

1. **Cota de EXISTENCIA (percolación).** Por debajo de grado medio 1 el componente gigante
   muere: `f_c = 1 − 1/z`. Con z = 3,268 → **f_c = 0,694**. Se **mide** sobre el grafo real
   además de calcularse (triangulación fórmula ↔ medida).
2. **Cota de DECIDIBILIDAD (`A` = 1).** El marco declara *«el contrato existe ⟺ A > 1»*
   (`CLAUDE.md`). **El Ω donde `A` = 1 es el punto en que llegar al sitio correcto deja de ser
   distinguible de llegar a una dirección equivocada.** Es una cota derivada del propio axioma.
3. **Punto de OPERACIÓN (rodilla de Pareto).** Máxima curvatura de `A` frente a `log e_conn`.

### Predicciones

- **P-Ω1 · `f_c` medido ∈ [0,60 , 0,75]**; la fórmula da 0,694.
- **P-Ω2 · `A` = 1 en `e_conn` ∈ [0,15 , 0,45], central 0,26** → **`Ω_A1` ∈ [0,7 , 1,1]**.
  *Sería 14–22× más flojo que el 0,05 declarado.*
- **P-Ω3 · la rodilla caerá en `e_conn` ∈ [3e-3 , 3e-2]** → `Ω_rodilla` ∈ [0,05 , 0,30].
- **P-Ω4 · el Ω = 0,05 declarado corresponde a `e_conn` ≈ 2,4e-3**, y eso debería coincidir con
  el «el contrato tolera 3,0e-3» de D-373/E2. *Si coinciden, el 0,05 es autoconsistente aunque
  no derivado.*

**Salvedad grande, escrita antes:** `A` = 1 es una cota de **sentido**, no el contrato. Dice
dónde el acto deja de significar algo, no dónde es aceptable. **Derivar el techo no deriva el
punto de operación**; para eso está la rodilla, y aun así la elección final dentro de las cotas
puede seguir siendo una decisión — pero una decisión **entre cotas derivadas**, que es otra cosa
que un número sin procedencia.

---

# PREREG 6 · ¿depende `e1` del GRADO? · el acoplamiento que mi Sobol no tenía

El investigador pregunta si la lectura varía según el árbol. **En mi modelo de D-480, `e1` era
una entrada INDEPENDIENTE: no dependía del grado, ni de `N_sin`, ni de nada.** La interacción
salió 0,0026 en parte **porque se la quité por construcción**.

Hay razón para pensar que sí depende: D-447 estableció que *«a grado 3,27 no hay redundancia
local que explotar»* — lo que implica que **más grado = más corregible = `e_conn` menor**. Y
D-465 midió que la precisión del prior está topada por la **tasa base** (0,84 %), que sube con
la densidad.

**Si `e1` depende del grado, `N_sinapsis` toca las dos mitades después de todo, y mi
retractación de D-480 era prematura.**

Medible hoy: estratificar los lugares de CREMI por su grado y medir `e_conn` **dentro** de cada
estrato, al degradar igual a todos.

- **P-L1 · `e_conn` BAJA al subir el grado del lugar**, con exponente ∈ [−0,8 , −0,1],
  central **−0,4**.
- **P-L2 · sobre la envolvente de `N_sin` (grado 2,99 → 3,75), `e1` variará entre 1,05× y 1,4×.**
- **P-L3 · con el acoplamiento dentro, el índice de Sobol de `N_sin` sube de 0,0026 a [0,01 ,
  0,10].** *Si sube por encima de 0,10, mi retractación de D-480 estaba mal y `N_sin` vuelve a
  ser prioritaria.*

---

# PREREG 7 · tabla de rangos e interacciones por pares del árbol

Propuesta del investigador: proyectar el rango de fluctuación de cada dimensión y cómo
interactúa con las demás, para obtener límites y un foco.

- **P-T1 · todos los índices de segundo orden `S_ij` saldrán < 0,01**, coherente con la
  interacción total de 0,0036 (D-482). *La tabla de interacciones será una tabla de ceros, y eso
  es el resultado: los límites se componen multiplicando.*
- **P-T2 · el orden del tornado coincidirá con Sobol**: `Ω_c` > `p_fallo` > ExM > `e1` > `N_sin`
  > `k`.
- **P-T3 · ninguna dimensión sola, llevada a su extremo favorable con las demás en su central,
  llegará a P = 100 %.** La que más subirá será `Ω_c`, y predigo **P ∈ [70 % , 95 %]**.
- **P-T4 · existirá un PAR cuya esquina favorable conjunta supere P = 90 %**, y será
  `Ω_c` × `p_fallo`.

---

# PREREG 8 · confrontación EXTERNA de los dos actores dominantes

Idea del investigador: enfrentar `Ω_c` y `p_fallo` con datos que **se relacionen con el árbol
pero no formen parte de él**. Los datos elegidos —**ninguno usado para construir el árbol**:

- **D-370/gusano de Witvliet**: adultos 7 y 8, 147 neuronas comunes. Mide `suelo` (el mismo
  gusano, otra semilla) = **0,0044** · contrato 0,05 = **3,37 ⱎ** · **entre dos gusanos SANOS =
  0,4905 = 10,54 ⱎ**.
- **D-422/planeta denso**: suelo de simulación limpia = **0,00108**.
- **siete exponentes** medidos en experimentos sin relación entre sí.

### Predicciones

- **P-X1 · `p_fallo`.** La razón entre el suelo de un espacio biológico REAL consigo mismo y el
  de la simulación limpia mide el ruido intrínseco de la biología. Predigo que implica
  **`p_fallo` ∈ [0,20 , 0,55], central 0,32** — *lo que validaría el 0,30 que elegí en D-477
  desde datos que nunca lo tocaron.*
- **P-X2 · `Ω_c`.** El contrato debe caer entre «yo conmigo» (1 ⱎ) y «otro individuo sano»
  (10,54 ⱎ). Predigo que el 0,05 declarado cae **dentro de un factor 2 de la media geométrica**
  de esos dos extremos. *Si acierta, el contrato arbitrario estaba en el centro de la escala
  biológica sin que nadie lo supiera.*
- **P-X3 · el exponente.** Los siete exponentes independientes serán compatibles con una sola
  constante, y esa constante será **2/3 = 0,6667** (λ₂ de un euclidiano 3D).
