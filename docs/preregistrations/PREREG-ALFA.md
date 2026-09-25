# PREREG · medir α, el exponente del campo de distorsión de ExM · umbral 0,8

## TRIADA paso 1 · INVENTARIO

Nada en los 15 datasets del disco mide α: ninguno es un gel de ExM. **Hace falta dato externo.**

## TRIADA paso 2 · la reformulación física, ANTES de bajar nada

α no es un parámetro libre: es el **exponente de Hurst del campo de desplazamiento** de un gel
elástico con hinchamiento heterogéneo. Y la elasticidad lo acota:

- **por debajo de la longitud de correlación `ξ` de la heterogeneidad del gel**, el campo es
  localmente afín → el desplazamiento relativo crece **lineal: α = 1**
- **por encima de `ξ`**, los desplazamientos se descorrelacionan → **α = 0,5** (paseo aleatorio)
- muy por encima, satura → α → 0

**Luego α no hay que medirlo directamente: basta saber si `ξ` está por encima o por debajo de la
escala de la adyacencia, 320 nm.**

```
ξ > 320 nm   ->  alpha = 1     ->  Pi/Pi_max = 1,86x
ξ < 320 nm   ->  alpha = 0,5   ->  Pi/Pi_max = 4,22x - 6,08x
```

`ξ` en un gel de poliacrilato/acrilamida es la escala de la malla y de la densidad de
entrecruzamiento. **Predicción P-α1: `ξ` estará entre 10 y 100 nm**, es decir **muy por debajo
de 320 nm**, luego **α ≈ 0,5 y ExM falla por 4,22×–6,08×.**

*Razón:* el tamaño de malla de un hidrogel de acrilamida al 4-10 % está en la decena de nm, y es
precisamente por eso que ExM conserva la forma a escala de micras pero no a escala de decenas de
nm — que es el hecho experimental conocido como «distorsión residual del 1-4 %».

- **P-α1 · `ξ` ∈ [10 , 100] nm → α ≈ 0,5 → ExM NO cumple, falla por 4,2×–6,1×.**
- **P-α2 · el umbral α = 0,8 exigiría `ξ` ≳ 200 nm**, dos órdenes por encima de la malla.
- **P-α3 · si se midiera α en un dataset real de pan-ExM, saldría en [0,4 , 0,7], no ≥ 0,8.**

**Consecuencia de método:** si P-α1 y P-α2 aciertan, **bajar S-BIAD2200 no cambia la decisión**,
porque la física de la malla ya la decide. El dato sólo haría falta si la predicción de `ξ`
fuera incierta a ambos lados del umbral — y no lo es: hay dos órdenes de margen.

## TRIADA paso 3 · MATE

Se reutiliza la ley `e_conn ~ δ^1,2809` (D-487) y la escala `δ(L) ~ δ_glob·(L/L_glob)^α`. Cero
descargas si los pasos 1 y 2 deciden.
