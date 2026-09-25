# PREREG · proyectar ι sin experimento de banco

Escrito **antes** de correr. 2026-09-12.

## Por qué NO el Gemelo Digital tal cual

El método 2 del investigador mide el desacuerdo entre dos instrumentos virtuales pasados por
**mi** segmentador. El error *reproducible* que saldría mezcla **ambigüedad del tejido** con
**sesgo sistemático de mi algoritmo**, y mi algoritmo sería crudo. `ι` saldría bajo por la
razón equivocada y no significaría nada. **Se descarta por diseño, no por coste.**

## Lo que sí se puede medir: la descomposición por RELACIÓN SEÑAL/RUIDO

`ι` = fracción del error que es del **instrumento**. Un error es instrumental exactamente
cuando la señal está por debajo de lo que el instrumento resuelve a esa dosis. Eso es medible
sobre CREMI **sin segmentar nada**:

- `Δ` = contraste de la membrana en el contacto (niveles de gris) — **medible**
- `σ` = ruido de disparo a dosis D — **modelable, `σ ∝ D^(−1/2)`**
- `A` = área de contacto en vóxeles — **ya medida hoy** (mediana 644, CAGE50/D-465)

La detección integra sobre el contacto entero, así que

```
d'(contacto) = (Δ/σ) · √A        ·        φ(D) = P(d' < 5)   [criterio de Rose]
```

`φ(D)` es la fracción de contactos que el instrumento **no puede** resolver a dosis D: el error
instrumental. Y entonces **`ι(D) = min(1, φ(D)/e1)`** con `e1 = 3e-3`.

## Y la consecuencia que esto abre: fraccionamiento de dosis

Tres lecturas a `D/3` cuestan **la misma dosis total** que una a `D`. Con ruido de disparo
`inst(D/3) = √3·inst(D)`, el voto por mayoría da `3·(√3·inst)² = 9·inst²`, luego fraccionar gana
cuando `9·inst(D)² < inst(D)`, es decir **`inst(D) < 1/9 = 0,111`**.

## Predicciones

- **P-G1 · `φ` a la dosis nativa de CREMI ∈ [1e-5 , 1e-2], central 1e-3** → `ι_nativo` central
  **0,33**, por debajo del umbral 0,8515.
- **P-G2 · `φ` sube al bajar la dosis; la dosis a la que `ι ≥ 0,8515` estará por DEBAJO de la
  nativa en un factor ∈ [2 , 50].**
- **P-G3 · la condición de fraccionamiento `inst < 0,111` se cumplirá a la dosis nativa** → tres
  lecturas a `D/3` baten a una a `D` **sin gastar más dosis**.
- **P-G4 · el contraste medido `Δ/σ` por vóxel a dosis nativa estará en [2 , 15], central 6.**

*Si P-G1 falla por arriba (φ > 1e-2 → ι = 1), la cadena cierra sola y no hace falta banco.*

## Método 1 del investigador (IAA de MICrONS/Hemibrain): LITERATURA, no verificable aquí

Desacuerdo entre revisores expertos 5–15 % → `1−ι ∈ [0,05 , 0,15]` → **`ι ∈ [0,85 , 0,95]`**.
Se registra como **cota externa citada por el investigador**, con estado evidencial LITERATURA.
Cae justo sobre `ι* = 0,8515`: el filo del cuchillo.

---

# PREREG 2 · ¿está el error CONCENTRADO en un canal? · el canal de CORTE, medido

Reformulación del investigador: ι no es un escalar, es un **vector de 5 canales**, cada uno
apagable por una **intervención distinta**. Consecuencia inmediata: la condición es sobre una
**suma absoluta**, y hay que apagar el **99,727 %** del error. **Si los 5 canales pesaran igual,
apagar cuatro dejaría 73× por encima.** Luego hace falta que **UN canal concentre ≥ 99,73 %**.

CREMI es ssTEM a 40×4×4 nm: **10× anisotrópico**. La anisotropía en z **es** el canal de corte.
Se mide barriendo z con xy fijo y comparando con el barrido de xy (ya hecho, D-467).

- **P-5a · degradar z hará MÁS daño por unidad de resolución perdida que degradar xy.**
- **P-5b · extrapolando a isotropía, el canal de CORTE explicará entre el 20 % y el 60 % de
  `e_conn`, central 40 % — muy por debajo del 99,73 % que haría falta.**
- **P-5c · ningún canal aislado llegará al 99,73 %.** *Si alguno llega, ese canal es el programa
  entero.*

---

# PREREG 3 · ¿INTERACTÚAN los canales? · y remedida de ADM con el criterio relativo

## A · interacción entre canales (idea del investigador: tabla 5-D con correlaciones)

Si los canales son **aditivos**, `e1 = Σeᵢ` y la tabla 5-D colapsa a 5 números sueltos. Si
**interactúan**, apagar dos da más (o menos) que la suma. Medible sobre CREMI para los dos
canales que controlo: **corte (z)** y **óptica (xy)**.

- **P-I1 · serán fuertemente SUB-aditivos**: `e(ambos) < e(z)+e(xy)`, razón ∈ [0,50 , 0,90],
  central **0,70**. Razón: el error es de **omisión** (regla 144), y si z ya borró una
  adyacencia, que xy la borre otra vez no añade nada.
- **P-I2 · y eso es MALA noticia**: con sub-aditividad, apagar un canal **recupera menos** que su
  magnitud en solitario, porque el otro vuelve a romper lo que el primero arregló.

## B · remedida de ADM con el criterio relativo

El contrato absoluto Ω ≤ 0,05 sobre suelo 0,01374 equivale a **ⱎ ≤ √(0,05/0,01374) = 1,908**.
Ésa es la traducción invariante al ruido. Se barre `e_conn` a `p_fallo = 0,30` buscando el
máximo con `ⱎ_p95 ≤ 1,908`.

- **P-B1 · `ADM_relativo` ∈ [3e-3 , 3e-2], central 1e-2** — es decir **21× mayor** que el
  4,65e-4 absoluto.
- **P-B2 · aun así no llegará a `e1` = 0,1705**: faltará un factor ∈ [5 , 60].
  *Si `ADM_relativo` ≥ 0,1705, el contrato se cumple HOY y el programa cambia de fase.*

---

# PREREG 4 · ¿está resuelta la LECTURA? · propagación de las tres blandas

El «2,1× del contrato» apila **tres factores no medidos**. Se propagan en vez de suponerlos.

| factor | central | rango | por qué es blando |
|:--|--:|:--|:--|
| `p_fallo` (ruido de liberación) | 0,30 | **[0,10 , 0,50]** | literatura; `ADM` es función de él |
| eficacia de ExM (queda del error) | 0,152 | **[0,08 , 0,40]** | ANALOGÍA de CREMI, no medida en gel |
| `e1` | 0,1705 | **[0,1705 , 0,35]** | cota INFERIOR: v117 ya traía proofreading |

- **P-R1 · P(la lectura queda resuelta) ∈ [0,10 , 0,40], central 0,25.**
- **P-R2 · el factor que más pesa será la eficacia de ExM**, porque es el único con un rango de
  5× y entra multiplicando directo.
- **P-R3 · si ExM se midiera y saliera en su valor central, P subiría por encima de 0,60.**

---

# PREREG 5 · índices de Sobol sobre el árbol del veredicto de lectura

Las entradas del árbol son **continuas**, no encendibles: la versión rigurosa de «cómo
interactúan» son **Sobol de primer orden `S_i`** (efecto propio) y **totales `S_Ti`** (con todas
sus interacciones). **`S_Ti − S_i` es la parte que sólo existe al cruzarse.**

Modelo, todo él ajustado a medidas de esta sesión:
`grado = 4·N_sin/(N_cel+N_sin)` · `suelo ∝ grado^(−0,6366)` (D-424) · escala con `p_fallo`
(D-469) · `Ω = suelo + 2,0531·e_conn^0,6388` (R²=0,99869, D-477) · `ADM` de invertir esa ley
con `ⱎ ≤ √(Ω_c/0,01374)` · `e_final = e1·ExM`.

Rangos: `Ω_c` [0,03 , 0,10] · `p_fallo` [0,10 , 0,50] · `N_sin` [1e14 , 5e14] ·
`e1` [0,1705 , 0,35] · `ExM` [0,08 , 0,40] · `k` [0,137 , 0,144].

**Razonamiento previo (elasticidades a mano):** `ADM ∝ Ω_c^1,565` y `∝ suelo^1,565`, luego el
contrato aporta ~6,9×, `p_fallo` ~6,9×, ExM 5×, `e1` 2,05×, `N_sin` 1,24×, `k` ~1.

- **P-S1 · dominarán `p_fallo` y `Ω_c`, NO la eficacia de ExM.** *Si es así, el hallazgo es que
  **la decisión sin auditar compite con todo lo medido**.*
- **P-S2 · la parte de interacción `Σ(S_Ti − S_i)` será grande, entre 0,20 y 0,50.**
- **P-S3 · `k` saldrá ≈ 0** (control: valida el método, porque f\* ya es despreciable).
