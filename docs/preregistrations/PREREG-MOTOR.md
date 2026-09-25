# PREREG · **MOTOR DEL CUERPO** · fusionar los procesos en un solo sistema de fórmulas

Idea del investigador: muchos procesos que hasta ahora se calculaban por separado **ya no son
independientes**. Si son identidades, deben salir de **un solo motor** con pocas anclas, como
`jacobiano.py` hace con el nervioso (18 anclas → 16 derivadas, κ(J) = 54,6).

## TRIADA

**(1) INVENTARIO.** Los números del cuerpo están repartidos en D-521 a D-530 y en cinco scripts
(`cuerpo.py`, `vivo.py`, `tejido.py`, `vasos.py`, `cierre.py`). **Nada de esto está fusionado, y varias
cifras se han escrito tres veces.**

**(2) MATEMÁTICA · qué es ancla y qué es identidad, escrito antes.**

Son **identidades** (no datos): `n_módulos = V_cuerpo/V_módulo` · `L_impresa = V/s²` ·
`terminales = V/s³` · `generaciones = log₂(terminales)` · `t_impresión = E_c·V/(P·η)` ·
`ΔP = 128μLQ/(πd⁴)` · `volumen de cultivo = N_células/densidad` ·
`duplicaciones = log₂(N/N₀)` · `equipos = t_ensamblaje/isquemia_fría` ·
`ΔT_vitrificación = 10·log(t_montaje/t_ventana)/log(Q10)` · `τ = r²/α` ·
`ΔT_exotermo = ΔH·[M]/(ρ·Cp)`.

Y hay una **fusión de tres en uno**: los 100 µm del límite de difusión, los 100 µm de resolución de
lectura (D-355) y los < 100 µm de distancia al capilar (D-356) **son la misma ancla**, `d_irrig`.

**(3) MATE.** Se reutiliza entero el aparato de BLINDAJE: jacobiano de elasticidades + aritmética de
intervalos. Cero cómputo nuevo pesado, cero nervioso.

## Predicciones con número

- **P-M1.** El motor tendrá **≤ 15 anclas** y **≥ 24 derivadas** → **≥ 1,7 cifras derivadas por ancla**.
- **P-M2.** `κ(J) < 10³` — el mismo criterio de buen condicionamiento que el marco nervioso.
- **P-M3.** Las tres anclas que más mueven el sistema incluirán **`s`** (entra al cuadrado y al cubo) y
  **`V_cuerpo`**.
- **P-M4.** **≥ 8 derivadas** saldrán con banda **< 2×** — sería la primera medida de consolidación del
  **cuerpo**, equivalente a la capa C del nervioso.
- **P-M5.** Al menos **3 cifras** que hoy están escritas por separado colapsan en identidades.
