# PREREG · el programa del investigador: proyectar capas cruzadas · TRIADA paso 1 primero

## Lo que el INVENTARIO contesta sin correr nada

### 1 · «completar A y C proyectando dimensiones» — **NO se puede**

- **C (60 %)** está topada por **medida**, no por método. Las 4 cifras anchas las dominan
  `FFN`, `N_sinapsis` y `τ_lisis`, **las tres de laboratorio** (D-468). La **regla 142** ya lo
  dice: *declarar una constante no consolida; la consolidación la paga el laboratorio.*
  **Ninguna proyección mueve C.**
- **A (85 %)** le falta el punto de operación de Ω, y **D-481 demostró que NO es derivable**:
  `A` es lineal en `log(e_conn)` con R² = 0,9987, **y una recta no tiene rodilla.**
  **Ninguna proyección mueve A.**

**Las dos respuestas son negativas y están ya medidas. No se gasta cómputo en ellas.**

### 2 · «la sinergia D×E» — **YA está medida, y es que E es despreciable**

**TOLERA (D-466) fue exactamente esa proyección**: 12 celdas de `e_conn` × `σ*`. Resultado:
**la colocación perfecta vale 0,8 puntos.** A σ\* = 1,412 µm, `f* = 1,37e-4` — **un orden por
debajo del error de lectura.** La sinergia que se busca no existe **en ese modelo de error**.

### 3 · Lo que SÍ está sin hacer, y es la puerta de F

**D-435 dice que si el error de colocación es DERIVA CORRELACIONADA (λ = 410 µm) en vez de ruido
blanco por célula, la exigencia pasa de 1,4 µm a 20 µm.** Eso **nunca se ha combinado con D.**

Y el aparato para hacerlo lo construí hoy: **el campo de distorsión suave de D-487 ES el modelo
de deriva correlacionada de E.**

```
F  =  D (error de lectura)  x  E (deriva CORRELACIONADA, no ruido blanco)
```

**Eso es un acto completo con los dos modelos de error realistas, y es la capa F, que estaba
al 0 %.**

## TRIADA paso 2 · predicciones, escritas antes

- **P-F1 · la deriva correlacionada a σ\* = 20 µm con λ = 410 µm dará una contribución a Ω
  MENOR que el ruido blanco a σ\* = 1,4 µm.** Es la afirmación de D-435 y nunca se comprobó
  junto con la lectura. Predigo razón **< 1,0**, central **0,3**.
- **P-F2 · D y E compondrán SUB-aditivamente**, razón ∈ [0,70 , 0,95], central **0,80**.
  *Referencia interna: D-424 midió solo-lectura 0,02499 + solo-colocación 0,04689 = 0,07188
  frente a las dos juntas 0,05769 → razón 0,803. Debe reproducirse.*
- **P-F3 · el acto completo F con `Π` = 0,0258 y deriva correlacionada fallará, pero por MENOS
  que el 1,86× de D sola:** predigo **[1,3× , 1,86×]**.
- **P-F4 · G no «surgirá sola».** La mitad filosófica está **fuera de alcance por decisión**
  (D-433), no por falta de datos. La operativa sí es definible, pero exige F cerrada.

## TRIADA paso 3 · MATE

Arnés de `estocastico.py` (REF y suelo compartidos) + campo gaussiano suave de `distorsion.py`.
Se cronometra una corrida antes de estimar (regla 127).
