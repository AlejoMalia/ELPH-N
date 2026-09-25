# PREREG-OBJETO · el contrato del objeto, medido sobre materia no biológica

**Fecha:** 2026-09-18 · Meta nueva: **teletransporte físico real y completo de OBJETOS**. Cero nervioso.

## INVENTARIO — y aquí está la sorpresa

El dataset son **4,2 GB y es 100 % biológico… salvo `data/memristor/`**, que contiene:

- `dang_fatigue_2025_fatigue_conductance.parquet` — **20 canales × 201 medidas** de conductancia bajo fatiga
- `bismuth_perovskite_2026_resistance_states.parquet` — 58 estados de resistencia (HRS/LRS) por composición
- ciclos I–V y trazas de conductancia cuantizada

> **Un array de memristores es un objeto cuyo ESTADO no se deriva de su diseño.** Dos dispositivos idénticos
> de fábrica tienen estados distintos, porque el estado es historia. **Es exactamente la clase 2 del contrato
> del objeto (D-585) — y lo tenemos medido en disco.**

## MATEMÁTICA — antes de calcular

Se aplica el contrato tal cual, sin cambiar una línea: `Ω` = 1 − corr(origen, destino), `A` = √(`Ω_imp`/`Ω_acto`),
**el contrato existe ⟺ `A` > 1**. Y el **impostor es una dirección equivocada**: permutar los canales.

**La pregunta que decide la clase del objeto:** ¿importa QUÉ canal es cada uno, o sólo la distribución?

- Si permutar canales **rompe** el contrato → el array es **POSICIONAL**: cada canal tiene dirección.
- Si permutar **no cambia nada** → es **COMPOSICIONAL**: basta reproducir la distribución.

*Es la misma pregunta que D-521 hizo sobre el cuerpo, aplicada a un objeto.*

## Predicciones

- **P-O1** · el **suelo** (dos medidas consecutivas del mismo dispositivo) da `Ω` < **0,05**.
- **P-O2** · el **impostor** (canales permutados) da `Ω` > **0,5**.
- **P-O3** · **`A` > 3: el array es POSICIONAL** — la identidad del canal es parte del objeto.
- **P-O4** · al avanzar la fatiga, `Ω` del acto **crece monótonamente**: *el contrato detecta la degradación
  del objeto sin que nadie se lo diga.*

## Lo que esto es y lo que no

**Es la primera vez que el programa mide su contrato sobre materia NO BIOLÓGICA.** No es un teletransporte:
es el **suelo y la banda** del contrato para esta clase de objeto, que es lo que hay que tener antes de
intentar el acto. **Y no mueve `validación contra materia`**: el dato es de otros, medido por otros.
