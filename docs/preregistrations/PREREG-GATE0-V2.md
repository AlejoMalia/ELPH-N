# PREREG-GATE-0 v2 · **la única pregunta de la que cuelga la arquitectura**

**D-622 · 2026-09-19.** Sustituye al GATE-0 de D-610, que se escribió para una arquitectura que ya
no existe: allí había *dos escáneres corregidos contra tres fiduciales*; **desde D-612 no hay
escáneres, hay dos bandejas del mismo lote y una cámara.**

## La pregunta, en una línea

> **¿El desacuerdo entre dos bandejas del mismo programa CNC CRECE con la separación?**

```
D(r) = | (p_i - p_j)_A  -  (p_i - p_j)_B |  =  C * r^alpha
```

| `α` | qué significa | consecuencia |
|--:|:--|:--|
| **≈ 1** | campo **suave** (gradiente, térmico) | la afín local lo mata como `(r/L)²` · **PASA** |
| ≈ 0,5 | paseo aleatorio espacial | sólo da `√(r/L)` · intermedio |
| **≈ 0** | error **independiente** por sitio | **caen D-616 y D-621** |

**PREDICCIÓN PREINSCRITA: `α` = 1,0 ± 0,2**, porque el error dominante de una placa CNC de lote
común es **escala térmica**, que es exactamente un gradiente lineal.

## TRIADA

**INVENTARIO.** De las siete afirmaciones sobre las que se apoya la máquina, **tres están medidas
(en banco sintético) y cuatro no lo están en absoluto**. De esas cuatro, `α` es la única de la que
cuelgan otras decisiones enteras. *La literatura de error volumétrico de máquina-herramienta lo
respalda —el error es fuertemente dependiente de la posición y de origen térmico— y hay un argumento
más fuerte que cualquier cifra: **toda la disciplina de compensación volumétrica existe porque el
campo es modelable**. Si el error fuera independiente por punto no habría nada que compensar. Eso
mueve `α` de SUPUESTO a LITERATURA, pero **no lo cierra en nuestro montaje barato.***

**MATEMÁTICA.** Escrita arriba, antes del dato. Y el instrumento **ya está validado** sobre campos de
`α` conocido: recupera **1,00 ± 0,00** para gradiente térmico, **0,49 ± 0,29** para paseo aleatorio y
**0,01 ± 0,30** para ruido independiente.

**MATE.** Se reutiliza `maquina.py` entero: la misma calibración, la misma lectura de siluetas, el
mismo emparejamiento por asignación. **Código nuevo: 40 líneas** (`maquina/code/gate0.py`).

## Cuántos fiduciales · **medido, no estimado**

`σ_α` **se satura en 0,15**: más fiduciales no ayudan porque los pares no son independientes, salen
todos de `n` puntos.

| fiduciales | `σ_α` |
|--:|--:|
| 9 | 0,32 |
| **25** | **0,18** |
| 49 | 0,15 |

**No importa**, porque la decisión que se necesita es `α` ≥ 0,8 contra `α` < 0,35, que están a **3σ**.
**Con 25 fiduciales y un solo par de bandejas basta.** Lo que queda ambiguo —distinguir `α` = 0 de
`α` = 0,5— no cambia ninguna decisión.

## Tres medidas por el mismo dinero · **M2 y M3 eran gratis y no las pedía**

| | qué | de dónde sale | antes → después |
|:--|:--|:--|:--|
| **M1** | `α`, el exponente | ajuste `D(r) = C·r^α` | LITERATURA → **MEDIDO** |
| **M2** | **el acuerdo absoluto** | la **amplitud** `C` a `r` = escala | PRESUPUESTO → **MEDIDO** |
| **M3** | **la repetibilidad del lector** | `N` disparos de la **misma placa quieta** | SIMULADO → **MEDIDO** |

Las tres salen de los mismos ficheros. Con 4.000 px sobre 200 mm el centroide de un fiducial de
4 mm da **0,71 µm**, así que **M3 puede juzgar el 0,52 µm declarado en D-613**.

**De las cuatro afirmaciones físicas de la máquina, tres pasan a MEDIDO por 25 €.** La cuarta —el
asiento de 8–14 nm— necesita bolas y asientos: **+79 €**.

## Montaje · **~25 €, una tarde**

1. **Dos placas** de aluminio 200×200×10, **mismo fichero CNC, mismo material, mismo lote**, grabadas
   en la misma sujeción con **25 fiduciales** en rejilla de paso 35 mm.
2. Cámara sobre columna a 1,5 m, retroiluminación, **sin tocar el enfoque entre las dos placas**.
3. **M3 primero:** 20 disparos de la placa A **sin tocar nada**. La dispersión de los centroides
   **es** la repetibilidad del lector.
4. `python3 maquina.py calibrar` · una foto de cada placa · `python3 gate0.py A.png B.png`
   → `α` (M1) y la amplitud `C` (M2) en `gate0.json`.

## Qué refuta qué

| resultado | lectura |
|:--|:--|
| **`α` ≥ 0,8** | **la predicción acierta.** La jerarquía funciona, el acuerdo del humano pasa con 19× |
| 0,35 ≤ `α` < 0,8 | la jerarquía da `√(r/L)`: el humano **sigue fallando**, hay que bajar `σ` |
| **`α` < 0,35** | **D-621 cae entero** y el acuerdo vuelve a fallar 34×. La arquitectura necesita Invar o artefacto certificado, y el precio se va de 260 € a decenas de miles |

**Y una salvedad honesta: esto no valida el asiento (8–14 nm), ni el lector (0,52 µm), ni el acuerdo
absoluto (7,9 µm).** Valida **la estructura espacial** del desacuerdo, que es de lo que cuelgan dos
decisiones enteras. Los otros tres siguen sin medir.
