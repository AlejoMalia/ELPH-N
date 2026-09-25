# PREREG-GATE0 · ¿pueden DOS medidas del mismo objeto corregirse contra fiduciales?

**Fecha:** 2026-09-19 · Cero nervioso. **Predicciones antes de correr.**

## Lo que mata

**La máquina universal exige que DOS máquinas midan el MISMO contrato.** Si el sistemático entre dos medidas
no se puede corregir por debajo del suelo, **cada máquina mide su propio contrato y la arquitectura no existe.**

D-608 lo cifró: sistemático entre dos escáneres del mismo modelo **200–600 µm**, y la corrección afín contra
tres fiduciales debe dejarlo **bajo 35 µm**.

## Lo que SÍ puedo probar hoy, y lo que NO

**Tengo:** Open3D DemoICPPointClouds — **tres escaneos del mismo escenario físico desde poses distintas, con
las matrices de alineación publicadas.**

**Lo que eso NO es:** dos aparatos distintos. Es **el mismo sensor en dos poses**. *Se declara antes de correr:
esta prueba acota el sistemático de POSE, no el de DISPOSITIVO.*

**Lo que sí contesta, y es lo que decide:** tras una alineación rígida conocida, **¿queda un residuo que una
corrección afín estimada con pocos puntos pueda quitar?** Si la respuesta es no —si el residuo lo domina la
geometría vista de forma distinta y no un error global— **entonces los fiduciales no pueden salvar dos
máquinas, y el GATE-0 real fallaría por la misma razón.**

## Predicciones

- **P-G1** · el residuo tras la alineación rígida es **10–20 mm** (mediana), coherente con los 15,0 mm que ya
  medimos en D-600.
- **P-G2** · una corrección **afín de 12 parámetros** estimada con puntos emparejados reduce el residuo
  **1,5–3×**.
- **P-G3** · **NO llegará a 35 µm**, y la razón será que **el residuo lo domina la diferencia de superficie
  vista, no un error global corregible**. *Si P-G3 falla y sí baja mucho, mejor para la máquina.*
- **P-G4** · el residuo **no mejora al añadir más parámetros** (afín → proyectivo): si el error no es global,
  más grados de libertad no lo quitan.


> ### ⚠ REGLA DE DECISIÓN CORREGIDA (D-649)
> El umbral original `α` ≥ 0,80 **era demasiado laxo**. La simulación extremo a extremo mide que a
> `α` = 0,80 **el acto sólo sale bien el 10 % de las veces**, y que el veredicto PASA tiene una
> **fiabilidad del 46 %**, mientras que el VETO acierta al **98,7 %**. La causa: la amplitud `C`
> también manda — los falsos aprobados son campos con `α` ∈ [0,80–0,85] **y `C` > 15 µm**.
>
> ```
> VETO       si alpha < 0,35                   · fiable al 98,7 %
> PASA       si alpha >= 0,95  Y  D(176 mm) <= 35 um   · corregido en D-669:
>            el umbral NO puede ir sobre C. [C] = um*mm^(-alpha) y alpha se AJUSTA,
>            luego un umbral fijo sobre C no es dimensionalmente valido. Medido:
>            "C <= 12 um" no mordia NUNCA (0 de 1800 campos simulados).
> INTERMEDIO todo lo demas                     · NO basta para lanzar el acto
> ```
>
> **GATE-0 es un VETO fiable y un VISTO BUENO malo.** **M2 ya mide `C` — sólo faltaba meterlo en la
> regla de decisión.**
---

## RIESGO DEL CONSUMIDOR · declarado (D-654, marco JCGM 106)

**Hasta ahora este documento declaraba un solo riesgo.** JCGM 106 exige los dos, y el que faltaba
**no hay que simularlo: sale de un teorema.**

### Por qué

`Ω` es la **mediana** de las distancias, y **la mediana tiene punto de ruptura 50 %**: no se mueve
mientras menos de `n/2` unidades estén mal.

> **El riesgo del consumidor del criterio 1, para cualquier defecto que afecte a menos de la mitad de
> las unidades, es exactamente 1.**

| criterio | punto de ruptura | detecta desde |
|:--|--:|:--|
| 1 · disposición (mediana) | **50 %** | 25 de 50 — **no ve nada por debajo** |
| 2 · inventario (p98) | **2 %** | **1** de 50 |
| 3 · recuento | 1/`n` | 1 de 50 |
| 4 · identidad (máx) | 1/`n` | 1 de 50 |
| 5 · contrato `A` > 1 | 50 % | hereda la mediana |

**Tres de los cinco tienen punto de ruptura 50 %. El sistema depende de los dos que no.** Y eso
explica de una vez por qué el control permutado pasa la disposición: **no es el umbral, es el
estimador.**

### El peor caso, medido

El defecto que maximiza el riesgo del consumidor no mueve muchas unidades: mueve **una, poco**.

| desplazamiento de UNA unidad | `P`(detectar) | **riesgo del consumidor** |
|--:|--:|--:|
| 0,3 mm | 0 % | **100 %** |
| 0,5 mm | 20 % | 80 % |
| **1,0 mm** | **95 %** | **5 %** |
| 1,5 mm | 100 % | 0 % |

**Referencia externa:** la IAEA fija su alarma perdida en **β = 10 %**. Nosotros estábamos en **100 %
en el peor caso, sin haberlo calculado.**

### Criterio de aceptación nuevo

```
SUELO DE DETECCION DECLARADO: el sistema detecta al >= 90 % un defecto de UNA
unidad desplazada **1,0 mm** con sigma_colocacion = 141 um.
Para bajarlo a 0,3 mm hace falta **sigma <= 42 um** (el micromanipulador de 14 um
de D-616 lo cumple con 3x).
```

**Todo acto certificado declara su suelo de detección junto a su `A`.** Un `A` sin suelo de
detección no dice qué defectos pasarían.

---

## PROTOCOLO CORREGIDO (D-653) · la placa se GIRA

**M3 eran 20 disparos de la placa quieta, que miden SÓLO el ruido de la cámara.** El PTB calibra las
placas de bolas por **multi-orientación**:

```
M3'  · 5 disparos a 0 grados, 5 a 90, 5 a 180, 5 a 270
       -> la parte que ROTA con la placa es el error de la PLACA
       -> la parte que NO rota es el error de la CAMARA
       **dos numeros por el mismo dinero**
```

---

## PROTOCOLO DE TRES PLACAS (D-658) · Whitworth, 1830s

**Fallo del diseño anterior, y era grave:** con **dos** placas sólo se mide su **diferencia**, y
**si comparten un error común la diferencia NO LO VE**. Pero la cancelación en modo común de D-612
**se basa precisamente en que ese error común existe**. *Estaba midiendo la cancelación con un
instrumento ciego a lo que cancela.*

```
  D_AB = e_A - e_B   ·   D_BC = e_B - e_C   ·   D_CA = e_C - e_A

  con 2 placas: 1 ecuacion, 2 incognitas  ->  INDETERMINADO
  con 3 placas: 3 ecuaciones + condicion de suma  ->  e_A, e_B, e_C DETERMINADOS
```

**Con TRES placas comparadas por pares, el error de cada una sale por separado, sin patrón externo.**
Y girándolas 90° se revela el alabeo. **Es el método de los tres planos de Whitworth, de los años
1830**, y el marco moderno de toda la familia es **Evans, Hocken & Estler, CIRP Annals 45 (1996)
617-634**: *«medida exacta sin referencia a un artefacto calibrado externamente»*.

| | antes | **ahora** |
|:--|:--|:--|
| placas | 2 | **3** |
| coste | — | **+45 €** |
| qué mide | la **diferencia** | **el error de cada placa** |
| hipótesis del lote común (D-612) | **asumida** | **CONTRASTADA** |

**Y eso es lo que compra los 45 €: la hipótesis más frágil de toda la máquina pasa de asumida a
comprobable.**

---

## PROTOCOLO CORREGIDO OTRA VEZ (D-664) · la placa deja de ser una REJILLA

**M3′ (girar 0/90/180/270) no puede hacer lo que dice.** El método multi-paso tiene **supresión de
armónicos**: con `n` posiciones, **los armónicos múltiplos de `n` NO se separan**. Con `n` = 4
quedamos ciegos a **4θ, 8θ, 12θ** — y **4θ es justamente el error de perpendicularidad X/Y y de
desajuste de escala entre ejes de una fresadora de 3 ejes**, el sistemático dominante del artefacto
que M3′ existe para caracterizar.

**Medido** (`experiments/lib/hsp_m3.py`), con placa |4θ| = 1,000 µm y cámara |4θ| = 0,600 µm:

| protocolo | disparos | placa estimada | cámara estimada | |
|:--|--:|--:|--:|:--|
| **n = 4 × 5** *(el actual)* | 20 | **0,131** | **1,390** | el 4θ de la placa se le carga a la cámara |
| n = 5 × 4 | 20 | **1,000** | **0,598** | exacto |

**Y la causa no es el número de giros: es la GEOMETRÍA de la placa.** El multi-paso exige que tras
girar **cada fiducial caiga donde estaba otro**. Una **rejilla cuadrada sólo admite giros de 90°**,
luego `n` = 4 es el único posible y el 4θ es inalcanzable por construcción.

Las dos placas del programa son rejillas: **25 fiduciales en `linspace(15,185,5)`** (5×5) y
**9 en la máquina** (3×3).

```
PLACA NUEVA · 5 ANILLOS x 5 FIDUCIALES a 72 grados,  radios linspace(26, 124)
                                          (experiments/lib/placa_anillos.py)
```

> **Corregido en D-667:** la primera version ponia los anillos en `linspace(20, 85)` y
> **r_max = 85 frente a un borde util en r = 124: extrapolaba.** Medido, extrapolar `r^4`
> cuesta **5x** (1,79 um frente a 0,35). El anillo exterior DEBE alcanzar la esquina util.
> **Arreglar el armonico y romper el borde habria sido un cambio a peor.**

| | rejilla 5×5 | **5 anillos × 5** |
|:--|:--|:--|
| giros válidos | 2, 4 | **5** |
| armónicos ciegos | **4, 8, 12** | 5, 10 — **el 4θ se separa** |
| separaciones distintas *(para ajustar `α` en M1)* | 14 | **35** |
| rango de separación | 42–240 mm | **16–162 mm** |

**Mismo número de disparos, mismo coste, misma tarde.** Es un cambio en el programa CNC de una placa
que aún no está cortada. **Mejor para M1 y para M3′ a la vez.**

**Método, con nombre y cita:** esto es *error separation / self-calibration*, no una invención
nuestra — [Evans, Hocken & Estler, *CIRP Annals* **45**(2) 617-634 (1996)](https://www.nist.gov/publications/self-calibration-reversal-redundancy-error-separation-and-absolute-testing);
la versión reducida sobre **placa de bolas circular no calibrada** es
[Keller & Stein, *Meas. Sci. Technol.* **34** 065015 (2023)](https://doi.org/10.1088/1361-6501/acc265).
**Keller & Stein usan placa CIRCULAR. Nosotros llegamos a la rejilla por descuido.**
