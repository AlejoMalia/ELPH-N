# PREREG · derivar el umbral de FIDELIDAD con 90 personas reales

## TRIADA paso 1 · el dato existe y nunca se usó

`data/dinamico/` es la base **ECG-ID: 90 personas, ~20 registros cada una**, 500 Hz, 20 s, con
edad y sexo. **Señal CORPORAL, no nerviosa** — el espacio que `CLAUDE.md` prefiere.

D-481 probó que el umbral de fidelidad **no se deriva por dentro del marco**. Pero D-370 lo acotó
en gusano midiendo «yo conmigo» frente a «otro individuo». **Aquí se puede hacer en humano.**

## Por qué esta vez SÍ es conmensurable

D-485 retractó el intento de D-484 porque comparaba **el impostor** (dirección permutada) con
**otro individuo** — magnitudes distintas. **Aquí las dos medidas son del MISMO espacio, el
MISMO observable y la MISMA definición de Ω:**

- `Ω_yo`  = 1 − corr(plantilla de latido, dos registros **de la misma persona**)
- `Ω_otro` = 1 − corr(plantilla de latido, **dos personas distintas**)

## Predicciones

- **P-F1 · `Ω_yo` ∈ [0,005 , 0,10], central 0,03.**
- **P-F2 · `Ω_otro` ∈ [0,20 , 0,80], central 0,45**, y la razón `Ω_otro/Ω_yo` > 5.
- **P-F3 · el umbral de fidelidad derivado como media geométrica en ⱎ entre los dos extremos
  caerá dentro de un factor 3 del `Ω` = 0,05 declarado.** *Si acierta, el 0,05 deja de ser una
  elección: pasa a ser el centro de la escala humana de identidad, medido en 90 personas.*
- **P-F4 · la separación será limpia**: AUC entre las distribuciones de `Ω_yo` y `Ω_otro` > 0,90.

---

# PREREG 2 · ¿qué `R` alcanza una PERSONA REAL contra sí misma?

D-502 exige `R ≥ 95 %` al acto. **Nadie ha comprobado qué `R` alcanza una persona real
comparada consigo misma.** Los 804 pares intra-persona de ECG-ID lo contestan.

- **P-R1 · la fracción de `Ω_yo` ≤ 0,05 caerá en [0,60 , 0,90], central 0,78.**
- **P-R2 · ninguna persona de las 88 alcanzará `R` = 95 %** contra sí misma con el umbral 0,05.
  *Si es así, exigir 95 % al acto es exigir más de lo que la biología entrega* (regla 147).
- **P-R3 · el `R` que alcanza el percentil 95 de las personas define el umbral derivado**, y será
  **< 95 %**.
- **P-R4 · con el umbral derivado 0,0419 en vez de 0,05, `R` bajará menos de 5 puntos** (la
  distribución es muy sesgada: la mediana está en 0,0104).
