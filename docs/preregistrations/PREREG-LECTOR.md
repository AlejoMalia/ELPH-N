# PREREG-LECTOR · inventar el lector, no elegirlo

**Fecha:** 2026-09-19 · Cero nervioso. **Predicciones antes de simular.**

## El hueco que queda

D-612 cerró el nido (79 €) y el acuerdo (0 €). **Pero el lector sigue costando 60–120 k€**, y con nido
discreto se cae sólo porque **el acto deja de demostrar colocación** (regla 408). **Para demostrar colocación
hace falta medir posiciones CONTINUAS a `σ` ≤ 3 µm sobre 200 mm.**

## La idea, y no es un catálogo

> **No hace falta un escáner 3D. Hacen falta los CENTROS de 25 ESFERAS de diámetro conocido.**

Eso no es metrología de superficie: **es estimación de centroide sobre una forma fuertemente restringida.**
La silueta de una esfera es **un círculo**, y el centro de un círculo se localiza **muy por debajo del píxel**
porque lo determinan **todos los píxeles del borde a la vez**.

**Y la Z sale gratis:** si las bolas descansan sobre un plano conocido, `z` = plano + radio. **No hay que
medirla.**

## MATEMÁTICA — antes de simular

Con `N_b` píxeles de borde, cada uno localizando el borde con desviación `σ_b`, el centro promedia:

```
sigma_centro ~ sigma_b / raiz(N_b)
```

Bola de 25,4 mm a 50 µm/px → **508 px de diámetro, ~1.600 px de borde**. Con `σ_b` = 0,3 px:
`σ_centro` ≈ 0,3/40 = **0,0075 px = 0,37 µm**.

**Y el enemigo real no es el ruido: es la DISTORSIÓN DE LENTE**, que es sistemática y grande.
Contra ella: **fiduciales en la MISMA imagen** y corrección polinómica — y lo que quede es común a las dos
estaciones si usan el mismo modelo (regla 406).

## Predicciones

- **P-L1** · el ajuste de círculo sobre una bola de 508 px con SNR 50 localiza el centro a **< 0,02 px**,
  es decir **< 1 µm**. *8× mejor que el escáner de 60–120 k€.*
- **P-L2** · la distorsión radial de una lente barata (2 %) da **> 2 mm** de error en el borde del campo:
  **catastrófica sin corregir**.
- **P-L3** · una corrección polinómica con **9 fiduciales** la deja **por debajo de 5 µm**.
- **P-L4** · el límite final **lo pone la corrección de distorsión, no el centroide** — es decir, `σ_final`
  será **≥ 3×** `σ_centroide`.
