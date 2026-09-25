# PREREG · **EL CONTRATO DEL CUERPO** y el primer acto corporal de extremo a extremo

Cuatro encargos. **Dos son de laboratorio húmedo y no se pueden ejecutar aquí, y no se simulan:**
V3 (ratón entero vitrificado) y la medida de `s` (canales a 0,5/1/2/3 mm). De esos dos se hace lo único
honesto: **apretar su prior con literatura**. **Los otros dos sí se ejecutan enteros** con datos en disco.

## TRIADA

**(1) INVENTARIO.** `data/antropo/caesar-norm-nh-fitted-meshes/`: **4.073 cuerpos humanos completos**, malla
ajustada de **6.449 vértices en correspondencia**. `data/antropo/male.csv` + `female.csv`: **6.068 sujetos ×
91 medidas**. `data/corazon/spatial/`: **4.247 posiciones de tejido cardíaco humano real**. Nada de esto se ha
usado nunca para un contrato: C-003 midió identificación y especificación, **no contrato**.

**(2) MATEMÁTICA · el contrato, escrito antes.** Se reutiliza **el mismo álgebra** del nervioso, sin inventar
nada:

```
Omega = 1 - corr(x_origen, x_destino)      sobre la DESVIACION personal del cuerpo generico
suelo = Omega(origen, origen remedido a la resolucion de lectura, 100 um)
impostor = direcciones de destino PERMUTADAS   (CLAUDE.md: nunca «otra persona»)
A = raiz(Omega_imp / Omega_acto)           el contrato existe <=> **A > 1**
```

El acto corporal: **leer** a 100 µm (cuantización) → **enviar** (sin pérdida) → **fabricar** con error de
colocación σ → **verificar** con el propio contrato.

**(3) MATE.** `banco.om` del nervioso (la misma función Ω), `composicion.py`, el motor del cuerpo. Cero
cómputo nuevo pesado.

## Predicciones con número

- **P-B1.** `Ω_imp` (permutar direcciones) sobre el cuerpo saldrá **≈ 1,00 ± 0,10** → la universalidad del
  impostor se extiende a la geometría corporal. *Si sale muy por debajo de 1, el impostor corporal no es
  universal y hay que decirlo.*
- **P-B2.** El suelo a 100 µm de remedida será **< 1e-3**.
- **P-B3.** `Ω_acto` con lectura y colocación a 100 µm será **< 0,01**, y por tanto **A > 5**.
- **P-B4 · la que decide el marco.** El contrato geométrico **existirá y no será vinculante**: la forma del
  cuerpo sobrevive al acto con holgura. *Entonces el contrato que manda en el cuerpo no es un Ω de forma: son
  los niveles V1–V5.* **Si A sale < 1, esta predicción cae y el contrato geométrico pasa a ser el cuello.**
- **P-B5.** El mismo contrato sobre **tejido humano real** (corazón, 4.247 posiciones) dará también **A > 1**,
  con 2 espacios × 3 semillas (regla madre).
- **P-B6.** El acto corporal **pasará el contrato de fidelidad** (`Ω ≤ 0,05`) en 6/6 celdas — al revés que el
  acto del nervioso, que falla por 3,6×–9,7×.
