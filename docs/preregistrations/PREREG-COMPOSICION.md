# PREREG · **la ley de composición del acto corporal**

El marco físico (D-545) lista 16 condiciones y exige que **todas** pasen. Pero **no dice cómo se combinan los
errores de los pasos** cuando todos ocurren a la vez. Sin eso el marco está incompleto: tiene condiciones y no
tiene álgebra.

## TRIADA

**(1) INVENTARIO.** El lado nervioso ya tiene su ley: **unión sub-aditiva con razón 0,78**, medida en dos
substratos (D-424, D-489) y **validada fuera de muestra** (D-511: mejora la predicción 3,44× frente a sumar).
**El cuerpo no tiene ninguna.** Y el aparato para medirla existe: `barato.py` de D-539, sobre histología
cardíaca humana real a 4,10 µm/px.

**(2) MATEMÁTICA · escrita antes.** Dos pasos del acto corporal degradan la arquitectura:

- **leer** a resolución `q` → pierde lo que no muestrea;
- **fabricar** con error de colocación `σ` → desplaza lo que coloca.

Si la unión es sub-aditiva con razón `r`:

```
Omega_ambos  =  max( max(Om_leer, Om_fab) , r · (Om_leer + Om_fab) )
```

`r` = 1 sería aditivo (los errores no se solapan); `r` = 0,5 sería la mitad. **La predicción del marco es que
`r` sale igual que en el nervioso**, porque la sub-aditividad se declaró física y no ajuste.

**(3) MATE.** `barato.py` entero. El desplazamiento se aplica con un campo suave, igual que el acto de
`predice.py`. Cero medida nueva de dato: es el mismo tejido.

## Predicciones con número

- **P-K1.** La composición será **sub-aditiva**: `Ω_ambos < Ω_leer + Ω_fab` en **≥ 8 de 9** celdas.
- **P-K2 · la que importa.** La razón `r` caerá en **[0,70 , 0,90]** — **la misma banda que el 0,78 del
  nervioso**. *Si sale fuera, la sub-aditividad no es una constante del acto sino del substrato, y hay que
  decirlo.*
- **P-K3.** Sumar en vez de componer **sobreestimará** `Ω` por un factor **≥ 1,3×** de media.
- **P-K4.** El término dominante será **la lectura** para `q` ≥ 10 µm y **la colocación** para `σ` ≥ 50 µm;
  habrá al menos una celda donde se cruzan.
