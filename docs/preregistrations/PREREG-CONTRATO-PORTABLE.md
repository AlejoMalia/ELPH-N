# PREREG · ¿se puede hacer el contrato COMPARABLE entre tejidos?

## El problema (D-499)

`Ω ≤ 0,05` no significa lo mismo si el suelo varía 15× entre tejidos del mismo cuerpo
(corazón 0,00246 · H01 0,00483 · malecns 0,03687).

## Las dos piezas que hay que volver adimensionales

1. **el UMBRAL**: `Ω̃ = Ω/suelo = ⱎ²` en vez de Ω absoluto
2. **el ACTO**: σ\* = `k · d(espacio)` — cada espacio con **su propio espaciado**, que es la
   regla del marco (`k` es el único π de Buckingham, D-406)

**Sólo si las DOS son adimensionales puede el contrato ser portable.** Hasta hoy el umbral era
absoluto y el acto usaba un σ\* fijo en µm.

## Predicciones, escritas ANTES

Tres espacios: **corazón humano** (Visium 2D) · **H01** (corteza humana) · **malecns** (CNS mosca).
Mismo acto adimensional: `e_conn` = 3e-3 y σ\* = `k`·espaciado propio.

- **P-A1 · con el umbral ABSOLUTO (Ω ≤ 0,05), R se dispersará > 60 puntos** entre los tres.
- **P-A2 · con el umbral RELATIVO (Ω̃ ≤ 3,64 = 0,05/0,01374), R se dispersará < 30 puntos.**
- **P-A3 · pero NO menos de 10 puntos**: el umbral relativo solo no basta, porque la respuesta
  del acto depende de ρ y de la geometría.
- **P-A4 · con el acto TAMBIÉN adimensional (σ\* = k·d propio), R se dispersará < 15 puntos.**
  *Ése es el hallazgo si acierta: el contrato ES portable cuando el umbral Y el acto son
  adimensionales. Si falla, el contrato no es portable y hay que declarar TOL por clase de
  tejido.*
- **P-A5 · el suelo NO correlacionará con el espaciado** (corazón 137 px vs H01 1,55 µm son
  unidades distintas): el suelo depende de ρ, no de la geometría.
