# PREREG · capa G · la cuenca de D-513 estaba MAL PLANTEADA: el arnés es CAÓTICO

**Escrito antes de correr `g_caos.py`.** El investigador pide llevar G al 100 % con papers.

## TRIADA

**(1) INVENTARIO.** D-513 midió G con **un espacio, una semilla** (H01, sd 31) —incumple la
regla madre— y con el acto **inventado** (`Π` = 3e-3, `σ*/esp` = 0,1407). Su techo declarado fue
*«el suelo del criterio es alto (0,098)»*: la misma red, perturbada un 2 %, ya divergía.

**(2) MATEMÁTICA · lo que dice la literatura, escrito antes.**

- **Sompolinsky, Crisanti y Sommers (PRL 1988):** una red aleatoria `ẋ = −x + J·tanh(x)` pasa
  a **caos** cuando la ganancia efectiva supera 1. El arnés fija `g = 4/ρ`: **ganancia 4**. La
  dinámica libre de D-513 es caótica, y **en caos no hay cuencas de punto fijo**: el suelo de
  0,098 no es ruido del instrumento, es **sensibilidad a condiciones iniciales**. El criterio
  «misma cuenca en dinámica libre» **está mal planteado**, no fallado.
- **Rajan, Abbott y Sompolinsky (PRE 2010):** la entrada **suprime el caos** con una transición
  de fase. Eso explica la regla 194 (Ω 0,134 dirigido → 0,584 libre) **sin hipótesis nueva**.
- **Abarbanel, Rulkov y Sushchik (PRE 1996) · sistema auxiliar:** dos copias idénticas con
  condiciones iniciales distintas, bajo la misma entrada, **convergen si y sólo si** hay
  **sincronización generalizada** — la respuesta es función de la historia de entrada y no del
  estado inicial. Criterio: **todos los exponentes de Lyapunov condicionales < 0**.
- **Parfit (1984):** lo que importa no es la identidad estricta sino la **conexión psicológica
  (relación R), que es GRADUAL**; en la fisión (dos réplicas) la identidad deja de ser
  transitiva.

**La definición operativa corregida:** *la persona es el FUNCIONAL entrada→salida*. Origen y
destino son la misma persona operativa si (G1) cada uno tiene sincronización generalizada con su
entrada, (G2) su respuesta no depende de la condición inicial, y (G3) el impostor no la reproduce.
**La fidelidad (cuánto se parecen) es de F/B, no de G.**

**(3) MATE.** `predice.eb` (tres espacios), el constructor de red y del acto de `predice.py`.

## Diseño · regla madre

3 espacios (H01, corazón, maleCNS) × **3 semillas** · acto **REAL** de D-517 (`Π` = 0,01554,
`σ*/esp` = 0,01559) · sin ruido dinámico (criterio puro) · 600 pasos · 8 pares de condiciones
iniciales · Lyapunov máximo por Benettin (δ = 1e-7, renormalizado cada paso, 300 de transitorio
+ 600 de medida, float64).

## Predicciones con número

- **P-G1 · caos libre.** `λ_libre` > 0 en **≥ 7 de 9** celdas.
- **P-G2 · la entrada lo suprime.** `λ_cond` < 0 en **9 de 9**.
- **P-G3 · el suelo del instrumento cae.** `Ω_aux` (misma red, misma entrada, condiciones
  iniciales distintas) < **1e-3** en 9/9 — **≥ 98× por debajo** del 0,098 de D-513.
- **P-G4 · la persona no depende del estado inicial.** `Ω(O_a, D_b)/Ω(O_a, D_a)` ∈ [0,9 , 1,1]
  en **≥ 8 de 9**.
- **P-G5 · discrimina.** AUC destino/impostor = **1,000** en 9/9.
- **P-G6 · fisión (Parfit), el número.** Dos réplicas independientes `D1`, `D2`:
  `Ω(D1,D2)/Ω(O,D)` ∈ **[1,6 , 2,0]** — con errores independientes `corr(D1,D2) ≈ corr(O,D)²`,
  que a Ω = 0,21 da **1,79**. *La relación R es gradual y la identidad no es transitiva.*

## Qué retira cada resultado

| si sale | se retira |
|:--|:--|
| `λ_libre` < 0 en la mayoría | la lectura «D-513 estaba mal planteada» — y D-513 queda en pie |
| `λ_cond` > 0 en alguna celda | la sincronización generalizada en ese espacio: G no se define ahí |
| `Ω_aux` ≥ 0,01 | la afirmación de que el instrumento gana resolución |

---

## ADDENDUM · escrito tras ver las 9 celdas y ANTES de las semillas 71 y 91

Cuatro de seis predicciones fallaron (P-G1, P-G3, P-G4, P-G6). Dos regularidades aparecieron
**post-hoc** y **no se publican como hallazgo hasta replicarlas con semillas nuevas**:

- **P-G7 · ley aditiva del estado inicial.** `Ω(O_a,D_b) − Ω(O_a,D_a) ≤ 1,2 × Ω_aux` en **6 de 6**
  celdas nuevas. *Léase: el acto no añade dependencia del estado inicial más allá de la que ya
  tiene el origen consigo mismo.*
- **P-G8 · fisión no transitiva y sub-independiente.** `Ω(D1,D2)/Ω(O,D)` ∈ **(1,0 , 2,0]** en
  **6 de 6**.
- **P-G9 · la dinámica libre no puede certificar ni al origen consigo mismo.** `Ω_aux,libre` > 0,9
  en **6 de 6**.
