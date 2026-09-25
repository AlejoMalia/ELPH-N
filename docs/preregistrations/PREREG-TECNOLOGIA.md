# PREREG-TECNOLOGIA · diseñar lo que no se puede comprar

**Fecha:** 2026-09-19 · Cero nervioso. **Predicciones antes de calcular.**

## Los tres huecos de `docs/MAQUINA-PERFECTA.md`

| hueco | lo que propuso el agente | por qué no basta |
|:--|:--|:--|
| **nido cinemático** | 10.000 **conos** en Invar, 1.500–5.000 € | **un cono NO es cinemático** |
| **artefacto de acuerdo** | Invar con 3 esferas certificadas, 4–15 k€ | es catálogo, no diseño |
| **lector** | luz estructurada metrológica, 60–120 k€ | ídem |

## MATEMÁTICA — antes de buscar un solo paper

**1 · El cono está mal.** Una bola en un cono apoya en **una circunferencia**: es
**sobredeterminado**, y dónde se para lo decide el rozamiento, no la geometría. **Tres puntos fijan el centro
de una esfera exactamente** — tres contactos, tres grados de libertad. *Es el asiento cinemático clásico.*

**Repetibilidad de un asiento de tres puntos**, por Hertz: `δ` = (9`F²`/(16`E*²R`))^⅓, con
`E*` = `E`/(2(1−`ν²`)) y `F` = `mg`/3 por contacto.

**2 · El acuerdo entre estaciones no hay que hacerlo PEQUEÑO: hay que hacerlo COMÚN.** Si las dos placas
salen del **mismo programa de CNC, el mismo material y el mismo lote**, su distorsión está **correlacionada**,
y lo correlacionado **se cancela en `Ω`** porque el origen mide y el destino construye con el mismo error.

**3 · Y el lector se cae entero si el nido es discreto.** Con sitios a paso `p`, la lectura deja de ser
**metrología** y pasa a ser **clasificación**: sólo hay que distinguir qué sitio ocupa cada bola.
**La exigencia pasa de `σ_z` ≤ 5,7 µm a «distinguir sitios separados `p`».**

## Predicciones

- **P-T1** · el asiento de tres puntos con bola de acero de 25,4 mm repite por debajo de **100 nm**,
  **10× mejor** que el micrómetro que pide el diseño.
- **P-T2** · el nido de tres puntos cuesta **menos de 100 €**, contra los 1.500–5.000 € del de conos.
- **P-T3** · con paso de 2 mm, el lector exigido baja de **`σ_z` ≤ 5,7 µm** a **≥ 200 µm**, o sea
  **una cámara de 30–80 €** en vez de un escáner de 60–120 k€: **factor ≥ 1.000×**.
- **P-T4 · y el precio de todo esto, que es el que hay que decir:** al hacer el objeto **discreto por
  construcción**, el acto deja de demostrar **colocación** y pasa a demostrar **asignación**.
  *`N` mejora y lo que se demuestra empeora.* **Predigo que el experimento sigue siendo clase 2 —la
  disposición se mide, no se diseña— pero que `colocar` deja de ser una condición medida.**
