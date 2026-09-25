# PREREG-TRES · las tres cosas que una simulación SÍ puede cerrar

**Fecha:** 2026-09-18 · Sólo cuerpo humano completo. Cero nervioso.
**Declarado antes de correr:** esto mueve `cumplimiento`. La **validación contra materia sigue en 0 %**.

## A · CAUDAL — verificar las 1.000 boquillas

**INVENTARIO.** Afirmación sin verificar de otro agente: 1.000 boquillas de 400 µm a 10 µL/s → 70 L en 1,94 h
con τ < 15 Pa. Tenemos Poiseuille, el `s` de Krogh y el coste vascular del hígado (0,51 km en 7,1 h, D-549).

**MATEMÁTICA — antes de correr.** 1.000 × 10 µL/s = 10 mL/s = 36 L/h → **70 L en 1,94 h: la aritmética cuadra**.
Lo que hay que comprobar es el régimen: cizalla de pared `γ̇ = 4Q/πR³`, presión `ΔP = 8ηLQ/πR⁴`, y sobre todo
**si ese caudal incluye el árbol vascular**, porque una boquilla de 400 µm no puede hacer un canal de 10 µm.

**Predicciones**
- **P-A1** · `γ̇` en la boquilla = **1.400–1.800 s⁻¹**, por encima del umbral habitual de daño celular (~1.000 s⁻¹).
- **P-A2** · `ΔP` = **1–3 bar**: irrelevante, la bomba no es el problema.
- **P-A3** · **el 1,94 h es SÓLO relleno de parénquima.** El árbol vascular exige otro cabezal y su tiempo es
  **≥ 20× mayor** que el del relleno para el mismo módulo.

## B · ERROR DE DEPOSICIÓN EN MATERIAL

**INVENTARIO.** Exactitud de platina 1,0 µm (LITERATURA, catálogo). Tolerancia contractual `σ*` = 1,65 µm
(D-547). **La desviación del filamento YA depositado no tiene cifra publicada: DESCONOCIDA.**

**MATEMÁTICA — antes de correr.** Tres contribuciones: (1) gravedad sobre el filamento en un fluido de esfuerzo
umbral, gobernada por `Y = τ_y/(Δρ g R)` —queda quieto si `Y` ≫ 0,14—; (2) hinchamiento a la salida de boquilla,
razón 1,1–1,2 en fluidos adelgazantes; (3) exactitud de platina, 1,0 µm.

**Predicciones**
- **P-B1** · `Y` ≫ 100: **la gravedad es irrelevante**, el baño sostiene el filamento.
- **P-B2** · domina el **hinchamiento**: `σ_dep` = **10–40 µm** con boquilla de 400 µm.
- **P-B3** · por tanto `N = σ_dep/1,65 µm` = **6–25: la condición de precisión FALLA en material**, aunque la
  platina pase. *Esto contradice el pase de D-549 y, si sale, es una retractación.*

## C · INOSCULACIÓN A ESCALA DE INTERFAZ

**INVENTARIO.** 48 h con margen 2× sobre isquemia (D-543). Herida de **2,06 m²** en 8 piezas (D-558).
`s/2` de Krogh por tejido: 50 µm corazón, 280 µm músculo.

**MATEMÁTICA — antes de correr.** El área **no entra**: la inosculación ocurre en paralelo por unidad de área.
Lo que decide es el **hueco de aposición**: mientras no se inoscula, la franja de interfaz es avascular, así que
tiene que ser más delgada que la distancia de difusión `s/2`. Criterio: `hueco + capa dañada < s/2`.

**Predicciones**
- **P-C1** · el área de 2,06 m² **no cambia el tiempo**: sigue 48 h.
- **P-C2** · la tolerancia de aposición exigida es **< 100 µm en corazón** y < 560 µm en músculo — es decir,
  **el tejido más exigente fija el requisito**, y es sub-milimétrico.
- **P-C3** · en frío (4 °C) el margen se multiplica por `Q10`: la condición pasa con **≥ 4×**.
