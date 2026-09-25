# PREREG · CAPAS D y E cerradas con LITERATURA (regla 196)

**Escrito ANTES de correr `de_lit.py`.** El investigador pide llevar D y E al 100 %. D-515
estableció que el bloqueo no era «laboratorio» sino **no haber buscado el valor publicado**.
Aquí se aplica lo mismo a D (lectura) y E (colocación).

## TRIADA

**(1) INVENTARIO.** Nada nuevo en disco. Lo que hay: `e1` = 0,17047 (MICrONS v117 vs v1822,
D-400, declarada COTA INFERIOR porque v117 ya llevaba proofreading), supervivencia a ExM
0,1516 (CREMI, D-486), ley de distorsión `e_conn ~ δ^1,2809` con `e_conn(16 nm)` = 0,0872
(D-487), `Π_max` = 0,01386, `σ*` = 124,6 nm, `lugares` = 5,825e14, unión sub-aditiva r = 0,78.

**(2) MATEMÁTICA.** Tres cotas cerradas, sin simular:

- **e_conn desde precisión/exhaustividad publicadas.** Con p = r, el Jaccard de conjuntos de
  aristas es `J = p/(2−p)` y `e_conn = 1 − J = 2(1−p)/(2−p)`. Es la MISMA definición de D-400.
- **α de la distorsión de ExM.** Si la literatura da el RMS como **porcentaje de la distancia
  medida**, entonces δ ∝ L y **α = 1 MEDIDO**, no barrido. D-487 dejó α libre y el rango salió
  22,7× de ancho (3,3×–75×).
- **Área de colocación.** `A = lugares / densidad_sitios`, y con la arquitectura de 608 etapas
  de D-492, `densidad_por_etapa = lugares / (608 × sección corporal)`.

**(3) MATE.** Se reutilizan `predice.py` (la unión), `jacobiano.py` (la propagación) y las
leyes `Ω_D ~ Π^0,52` y `Ω_E ~ σ*^2,1`. Cero cómputo nuevo pesado.

## Los valores de literatura que entran, con su procedencia

| magnitud | valor publicado | fuente |
|:--|:--|:--|
| **suelo del segmentador, conectoma binario** | **97 % precisión Y exhaustividad**, «menos del 3 % de conexiones perdidas o mal detectadas» | SynEM, Staffler 2017 eLife · SBEM corteza L4 ratón, 11,24×11,24×28 nm |
| distorsión de ExM | **1–3 % de la distancia medida, entre 0 y 40 µm** (tejido) | proExM / ExM de *C. elegans* |
| colocación de origami de ADN | **13,8 nm (1σ)**, rendimiento 90–94 % | colocación dirigida por sitio |
| densidad de sitios | **2e6 sitios en 117×117 µm = 1,46e10 /cm²** | nanomatrices de molécula única |
| tiempo de montaje | **60 min, UNA incubación para el chip entero** | ídem |

## Predicciones, escritas antes de correr

**Capa D**

- **P-D1.** `e_conn` del suelo del segmentador saldrá **0,0583** (de p = 0,97). *Predigo que
  esto MEJORA `e1` = 0,17047 por un factor entre 2,5× y 3,5×* — porque `e1` está declarada
  cota inferior de lo *corregido en cinco años*, no del error del segmentador.
- **P-D2.** Con `e1` → suelo del segmentador, `Π` = 0,0583 × 0,1516 = **0,00883**, que queda
  **POR DEBAJO** de `Π_max` = 0,01386. *Predigo margen de 1,5×–1,6×.*
- **P-D3.** Pero al añadir el canal de distorsión del gel (D-487) con α = 1, la unión
  sub-aditiva **vuelve a fallar**. Predigo el hueco final en **[1,2 , 4,0]×**, central ~2,2×.
  *Es decir: D no cierra, pero el rango pasa de 22,7× de ancho a menos de 4×.*
- **P-D4 · la que decide la rama.** D-486 dejó abierta la vía «recomputar el alineamiento y que
  el suelo del segmentador quede bajo 0,0139». **Predigo que la literatura la CIERRA EN
  NEGATIVO**: el mejor suelo publicado (0,0583) está **4,2× por encima** de 0,0139. Si sale
  por debajo, la vía queda abierta y hay que decirlo.

**Capa E**

- **P-E1.** La colocación de origami de ADN cumple `σ*` = 124,6 nm con margen **9,0×**, y es
  la primera modalidad de la tabla de E que cumple **sin ser serie** (el haz de electrones
  cumple a 10 nm pero es serie).
- **P-E2.** El área total exigida será **~4,0 m²** de sustrato estampado. *Predigo que eso son
  menos de 100 obleas de 300 mm — es decir, escala de fábrica existente, no de física nueva.*
- **P-E3.** Repartida en las 608 etapas de D-492, la densidad exigida por etapa quedará
  **por debajo** de los 1,46e10/cm² demostrados. Predigo un margen de entre 5× y 50×.
- **P-E4.** La tasa exigida por D-492 (7,33e11 /s) **no la cumple una sola oblea**. Predigo que
  hacen falta entre 10² y 10³ obleas en paralelo. *Si sale más de 10⁴, la vía no sirve.*
- **P-E5 · el riesgo declarado.** La colocación de origami es **PLANAR** y el cuerpo es 3D.
  Predigo que la arquitectura de 608 etapas —derivada de forma independiente por el invariante
  `Q × ventana`— es exactamente el puente, y que esa coincidencia **no la busqué**: las dos
  cifras salieron de cadenas distintas.

## Qué retira cada resultado

| si sale | se retira |
|:--|:--|
| suelo del segmentador < 0,0139 | la afirmación de que D está bloqueada |
| suelo del segmentador > `e1` = 0,17047 | la sustitución: `e1` se queda |
| área > 10³ m² | la vía de origami para E |
| margen de σ* < 1 | la vía de origami para E |
