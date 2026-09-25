# PREREG · cerrar el defecto de la capa A: separar `d_medio` de `d_mínimo`

## TRIADA paso 1 · INVENTARIO

- **C no se puede mover sin laboratorio.** D-490 lo midió: las 5 anclas medibles de los 15
  datasets dan **+0 puntos**, porque las 4 que dominan las cifras anchas (`FFN`, `N_sin`,
  `τ_lisis`, `L_neurita`) no están en disco.
- **El Ω de A no es derivable.** D-481: `A` es lineal en `log(e_conn)`, R² = 0,9987.
- **Lo que SÍ se puede cerrar hoy: el defecto de `d`.** D-490 lo destapó y `jacobiano.py` lo
  sigue teniendo: un solo símbolo `d_celula` alimenta la cadena de **CONTAR** y la de **TOLERAR**.
- Y el dato para arreglarlo **está en disco**: H01, 16.087 células con posiciones 3D → `d_mínimo`
  se **mide**, con su propia incertidumbre, en vez de derivarse de `V/N`.

## TRIADA paso 2 · predicciones, ANTES de tocar el código

- **P-A1 · los centrales cambian mucho**: σ\* de 1,797 → **0,218 µm** (8,2×) y fiduciales de
  1,31e10 → **7,33e12** (559×).
- **P-A2 · la consolidación NO sube: +0 puntos.** Razón: las cifras de la cadena de tolerancia
  (`sigma_um` 1,20×, `sigma_cuerpo` 1,28×, `fiduciales` 1,42×, `d_celula` 1,15×) **ya pasaban**
  por debajo de 2×. Cambiar su central no cambia su banda.
- **P-A3 · pero la BANDA de la cadena de tolerancia se ESTRECHA**, porque `d_mínimo` se mide
  directamente sobre 16.087 células reales mientras `d_medio` venía de `V_cuerpo` (±14,3 %) y
  `N_celulas` (±10,7 %). Predigo `sigma_um` de 1,20× a **≤ 1,10×**.
- **P-A4 · ninguna cifra cambiará de veredicto** (ninguna cruza el 2× en ninguna dirección).
  *Si alguna lo cruza, el defecto era peor de lo que parece.*

**Y lo declaro explícitamente: el valor de esto NO son puntos de consolidación. Es que dos
centrales del marco estaban equivocados por 8,2× y 559×.** Quitar el defecto es cerrar A en el
sentido de corrección, no de anchura.
