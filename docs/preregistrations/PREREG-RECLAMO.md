# PREREG · F como RECLAMO hacia atrás · presupuesto de error por capas

## El giro

Todo lo de hoy ha sido propagación **hacia delante** (anclas → cifras → veredicto). Un
**reclamo** es hacia atrás: F exige `Ω_acto ≤ Ω_max`, y ese total hay que **repartirlo** entre
las capas que contribuyen. Es un **presupuesto de error de ingeniería**, y el marco no lo tiene.

D-494 lo hizo a medias y con un orden arbitrario (E primero, luego D). **Aquí se hace bien: por
cada capa, qué tendría que entregar para que P(contrato) ≥ 0,95, con las demás en su
distribución medida.**

## Campana: log-normal, no normal

Las contribuciones a Ω son **positivas y se componen multiplicativamente**. Una gaussiana
directa pondría masa en Ω < 0. Se usa **gaussiana sobre el logaritmo** (log-normal), con las
dispersiones medidas hoy.

## Distribuciones, todas medidas

| capa | magnitud | rango |
|:--|:--|:--|
| A | `Ω_c` | [0,03 , 0,10] |
| D | `Π` | [0,0136 , 0,0624] |
| E | `σ*` | 0,2212 µm ±2,6 % (`d_min` ±0,748 %, `k` ±2,5 %) |
| F | `r` (unión) | [0,769 , 0,803] |
| bio | `p_fallo` | [0,10 , 0,50] |

Substrato: **H01, corteza humana real** (suelo 0,00483, `Ω_E ~ σ*^1,6525`, `Ω_D ~ Π^0,6388`).

## Predicciones

- **P-R1 · el reclamo sobre D será `Π` ≤ ~1e-4**, es decir **≥ 250× por debajo de lo medido**.
- **P-R2 · el reclamo sobre E será σ\* ≤ ~200 nm** — apenas por debajo de donde ya estamos
  (221 nm). **E está casi en su techo absoluto.**
- **P-R3 · el reclamo sobre A será `Ω_c` ≥ 0,25**, o sea **5× más flojo que el declarado** pero
  **todavía dentro del techo de decidibilidad (0,901, D-481)**.
- **P-R4 · ninguna capa sola puede satisfacer el reclamo**; habrá que repartirlo.
