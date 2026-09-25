# PREREG-ESTRES · ¿sobrevive el criterio a los modos de fallo de la MATERIA?

**Fecha:** 2026-09-19 · Cero nervioso. **Predicciones antes de correr.**

## Por qué

**Comprar la lista no garantiza el acto.** El acto digital de D-602 usó **voxelización limpia**: una
degradación determinista y sin sorpresas. **La materia tiene modos de fallo que ese modelo no tiene.**

> **Antes de gastar 1.178–2.227 €, hay que saber a qué nivel de cada fallo REAL el criterio se rompe.**
> Eso da un **presupuesto de tolerancias** que la máquina tiene que cumplir — y si alguno es inalcanzable,
> el gasto no tiene sentido.

## Los cuatro modos de fallo, sobre las nubes LiDAR reales

| modo | qué simula |
|:--|:--|
| **σ de colocación** | el colocador no pone la unidad donde dice el fichero |
| **pérdida de unidades** | una unidad se cae, se pierde o no se coloca |
| **contaminación** | entra materia que no estaba en el origen |
| **deriva** | el objeto cambia entre leer y verificar (regla T1) |

## MATEMÁTICA — antes de correr

El suelo medido es **0,00339** y el mejor impostor **0,04232**. Con el criterio corregido de D-608
—`Ω_acto` ≤ (1+δ)·mediana(suelo) con **δ = 0,30 preinscrito**— el umbral es **0,00441**.

Para un desplazamiento aleatorio de amplitud `σ` sobre una nube de espaciado `s`, `Ω_d` crece como `σ`/`s`
mientras `σ` ≪ `s`. Con `s` ≈ 0,64 mm del LiDAR y umbral 0,00441 sobre un suelo de 0,00339:
**el margen en `Ω` es 1,30×, luego `σ_max` ≈ 0,30·`s` ≈ 190 µm.**

## Predicciones

- **P-E1** · `σ` tolerable **150–250 µm**. *Si sale menor que los 141 µm que la máquina alcanza, **el
  demostrador no cierra y no hay que comprarlo**.*
- **P-E2** · la **pérdida** es el modo más severo: **una sola unidad de 25 perdida (4 %) rompe el criterio**,
  porque `ⱎ` = max no perdona (regla 352).
- **P-E3** · la **contaminación** es **menos severa que la pérdida** a igual fracción: añadir material donde
  no había daña menos que quitarlo donde había.
- **P-E4** · la **deriva** tolerable es ≥ 10× el suelo, así que **no es el cuello** en un objeto de acero.
