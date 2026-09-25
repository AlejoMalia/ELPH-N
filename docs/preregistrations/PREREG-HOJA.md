# PREREG-HOJA · la primera `A` sobre un acto físico real

**Fecha:** 2026-09-19 · Cero nervioso. **Escrito ANTES de tener los ficheros.**

## El dato

**Bömer et al. 2024, GigaScience** — [10.1093/gigascience/giae035](https://doi.org/10.1093/gigascience/giae035) ·
datos en GigaDB [10.5524/102530](https://doi.org/10.5524/102530) y en Sketchfab (@GigaDB), **CC Attribution**.

| colección | qué es | `n` |
|:--|:--|--:|
| **Sugar Beet · Leaf Point Cloud** | **la MEDIDA**: LiDAR sobre las hojas de una remolacha real | **12** |
| **Sugar Beet · Leaf** | **la RECONSTRUCCIÓN**: la malla que se fabrica | **12** |
| Sugar Beet · Beet | la raíz | 3 |

> **Clase 2 verificada**: el fichero vino de una medida de una planta real, no de un plano (regla 342).
> **Y 12 hojas son 132 pares de impostor** — la mitad de la ecuación que nadie ha calculado nunca.

## Qué se puede y qué no

| | ¿se puede? |
|:--|:--|
| **acto** `Ω`(nube_i, malla_i) | **sí**, 12 valores |
| **impostor** `Ω`(nube_i, malla_j), `i≠j` | **sí**, **132 valores** |
| **suelo** | **NO**: no hay dos medidas de la misma hoja. *Se declara un proxy y se marca* |

**Y hay que decir qué acto es:** esto mide **leer → reconstruir en digital**, no la impresión física.
`validación contra materia` **sigue en 0 %**. *Lo que daría es la primera `A` medida sobre un par
medida-reconstrucción de un objeto real.*

## MATEMÁTICA — antes de correr

Alineación rígida por ICP, y `Ω` = 1 − corr sobre el campo de distancia firmada muestreado en una rejilla
común. `A` = √(`Ω_imp`/`Ω_acto`).

## Predicciones

- **P-H1** · `A` > **2**: la malla de la hoja *i* se parece a su nube mucho más que a la de otra hoja.
- **P-H2** · `A` será **menor que el 8,17 de la histología**, porque doce hojas de la misma planta son
  **impostores parecidos**: el impostor caerá por debajo de 0,9, no cerca de 1.
- **P-H3** · la dispersión del impostor entre los 132 pares será **grande** (las hojas difieren mucho en
  tamaño), y habrá que publicar **mediana y rango**, no media.
- **P-H4** · sin suelo medido, el `A` publicado es **una cota inferior**, no el valor.

## Qué hace falta para correrlo

Los **24 ficheros** (12 nubes + 12 mallas) en `experiments/HOJA/data/`, en OBJ, PLY o STL.
**Sketchfab exige cuenta gratuita para descargar; eso lo hace el investigador.**

---

# ADENDA · sólo hay 8 nubes, ninguna malla · **y aun así salen las tres cifras**

**Lo descargado:** 8 ficheros `.las`, **las ocho son nubes de puntos**. Sin mallas, **la reconstrucción de los
autores no la tenemos**. *Confirmación del lector: `leaf_02` tiene 12.569 puntos, exactamente lo que la API de
Sketchfab declara para «Leaf 02 Point Cloud».*

## Pero el contrato se puede cerrar entero, porque la reconstrucción la hacemos NOSOTROS

| | cómo | qué mide |
|:--|:--|:--|
| **SUELO** | dos **mitades aleatorias** de la misma nube | dos muestreos independientes del **mismo** objeto |
| **ACTO** | nube original contra **nuestra reconstrucción** a resolución `v` | `leer → reconstruir`, con el acto **nuestro** |
| **IMPOSTOR** | hoja `i` contra hoja `j` | **28 pares** con 8 hojas |

**Y se declara qué acto es:** la medida es de ellos —LiDAR sobre una planta real, clase 2—; **la reconstrucción
es nuestra.** `validación contra materia` **sigue en 0 %**: no hemos fabricado nada.

## Lo que esto permite y no estaba previsto

**Medir `k_muestreo` sobre un tercer sustrato.** El marco usa arq/12 (histología humana, `[M]`) y arq/25
(granular, `[L]`). **Aquí se puede medir: a qué resolución de vóxel el acto deja de distinguirse del suelo.**
*Regla 302 puesta a prueba por tercera vez.*

## Predicciones · escritas antes de correr

- **P-H5** · el **suelo** (mitades aleatorias) da `Ω` < **0,05**.
- **P-H6** · el **impostor** entre hojas distintas da `Ω` > **0,30** — *menor que en histología, porque ocho
  hojas de la misma planta son impostores parecidos*.
- **P-H7** · **`A` > 3**.
- **P-H8** · el acto **degrada monótonamente** al engordar el vóxel, y **cruza el suelo** en `v` entre
  **arq/8 y arq/30**, con `arq` = tamaño de la hoja.
