# PREREG · las cuatro vías del investigador · escrito ANTES de correr

Fecha 2026-09-12. Régimen declarado para todo lo de aquí: **{disperso (grado 3,268), con
colocación}**, bits 8, d=12,77 µm. Nada se exporta fuera de esa etiqueta (regla 117).

## TRIADA paso 1 · INVENTARIO — qué ya estaba en disco

| vía | ¿contestada en disco? |
|:--|:--|
| 1 · tolerar e_conn (H∞ / andamio) | **NO.** Y por un fallo mío: `m1_decimacion.py:22` rotula el régimen como `e_conn=3e-3` pero la línea 107 inyecta `TOL=3e-4`. **El 98,8 % de D-455 se midió con un orden de magnitud MENOS error de lectura del físicamente alcanzable.** Etiqueta falsa. |
| 2 · inversión conjunta rayos X + EM | **PARCIAL.** El recorte de 1036× de D-465 se midió sobre la segmentación de verdad de campo a 4 nm, **no sobre una reconstrucción a 50 nm**. La jaula real nunca se ha medido. |
| 3 · huellas por paseo aleatorio | **SÍ, por cota cerrada.** No hace falta correr. Ver abajo. |
| 4 · cobrar lo gratis con SQP | **SÍ, es aritmética.** D-464 ya da 3,8× → 2,0×. Montar un SQP para evaluar constantes declaradas es exactamente lo que TRIADA paso 2 prohíbe. |

**Se corren dos experimentos, no cuatro.** Dos se cierran con cota o con aritmética.

## TRIADA paso 2 · MATEMÁTICA — las cotas, con su cifra

### Vía 3 · la ventana del paseo está VACÍA — cota cerrada, sin correr

Un paseo de profundidad L desde un lugar alcanza `z^L` lugares y `z^L·z/2` adyacencias.

- **Para ser INFORMATIVO** sobre una adyacencia concreta, el paseo tiene que poder rodearla:
  necesita alcanzar el grafo, `z^L ≳ N` → `L ≥ log(N)/log(z)`.
  - banco N=1.200 → **L ≥ 6,0**
  - cuerpo N=10¹⁴ → **L ≥ 27,2**
- **Para ser LIMPIO**, la bola no puede contener más de un error, o la huella de la arista en
  duda queda enterrada en el ruido de las demás: `sqrt(z^L·(z/2)·e_conn) < 1` →
  `z^L < 2/(z·e_conn)` = 2/(3,268·3e-3) = 204 → **L < 4,48**.

**4,48 < 6,0 < 27,2. La ventana es vacía a escala de banco y a escala de cuerpo.**
Predicción **P-V3: cualquier inmersión por paseo aleatorio sobre la adyacencia sola da
AUC ≤ 0,54**, coherente con el 0,506 medido (D-447). Complemento: con C = 0,135/3,706 = 0,0364,
una arista verdadera tiene `C·(z−1)` = **0,083 vecinos comunes esperados**; la fracción máxima
de aristas perdidas recuperable por evidencia de triángulo es `1−e^(−0,083)` = **8,0 %**.

*Salvedad honesta:* la parte de la vía 3 que usa `L_tramo` y la geometría de la rama **no** es
una función de la adyacencia sola, y la cota no la toca. Pero eso ya está medido y es el área
de contacto (AUC 0,9599, D-465), topada por la tasa base al 7,4 % de precisión (regla 139).

### Vía 4 · aritmética, no SQP

Declarar bits=8 baja la exigencia sobre `N_sinapsis` de **3,8× a 2,0×** (D-464). El portador
límite de 600 TB es una restricción de igualdad sobre constantes ya fijadas: el SQP tendría
**cero grados de libertad** tras inyectarlas. Se cobra por declaración, no por solver.

### Vía 1 · experimento TOLERA · ¿existe una σ\* que compre el e_conn físico?

Barrido `e_conn × σ*` sobre el arnés exacto de m1 a m=1. Predicciones:

- **P-1a · a e_conn=3e-3 con σ\*=1,412 (colocación actual): R cae por debajo del 95 %.**
  Cifra central predicha **R = 55 %**, intervalo [40 %, 70 %].
- **P-1b · a e_conn=3e-3 con colocación PERFECTA (σ\*=0): R sigue por debajo del 95 %.**
  Cifra central predicha **R = 72 %**, intervalo [60 %, 85 %]. *Si P-1b falla y R ≥ 95 %, la
  vía 1 del investigador FUNCIONA y el andamio compra la lectura.*
- **P-1c · no existe σ\* en (0, 1,412] que restaure el 95 % a e_conn=3e-3.**
- **P-1d · el contrato sigue existiendo (A > 1) en todas las celdas**, aunque el acto no lo cumpla.

### Vía 2 · experimento CAGE50 · la jaula a 50 nm, medida

Se degrada la segmentación de CREMI a vóxel de 48 nm (agregando 12×12×1 sobre 4×4×40 nm) y se
define **vóxel CANDIDATO** = bloque fino que contiene ≥2 etiquetas de neurona (por él pasa una
interfaz). La propuesta de inversión conjunta dice: imagina a resolución EM **sólo** los
candidatos.

- **P-2a · la fracción de volumen candidato será ALTA.** El neuropilo está lleno de membranas: a
  48 nm una neurita de ~300 nm tiene ~6 vóxeles de diámetro, de los que la cáscara de 1 vóxel es
  `1−(2/3)²` = **56 %**. Predicción **fracción ∈ [0,40 , 0,80]**, central **0,56**.
- **P-2b · la reducción de dosis = 1/fracción ∈ [1,25× , 2,5×], central 1,8× —
  POR DEBAJO del 2,35× que falta.** *Si sale > 2,35×, la vía 2 cierra el hueco térmico y es la
  vía que decide el programa.*
- **P-2c · el recall del sitio sináptico dentro de la jaula se mantendrá ≥ 95 %** (las sinapsis
  son interfaces por definición).
- **P-2d · el recorte en espacio de PARES caerá de 1036× a [20× , 200×]** al fundirse neuritas
  apuestas.

## TRIADA paso 3 · MATE ×3

1. `comarca.npz` y la selección ponderada por peso: se cargan **una vez**, no por celda.
2. **REF y suelo se calculan UNA vez** y se comparten por las 12 celdas del barrido — es el
   80 % del coste. Sólo `acto()` es por celda.
3. El volumen de CREMI se submuestrea `[::3,::4,::4]` como en E1 (D-374), una sola vez, y la
   agregación a 48 nm es un `reshape` vectorizado, no un bucle.

**Regla 127: se cronometra una unidad antes de estimar el total.** Nada de escalado lineal.

---

# PREREG 2 · EM20 · ¿cumple el contrato una lectura a 20 nm dentro de la jaula?

La única casilla que D-466 dejó viva: EM a 20 nm sobre jaula de 32 nm baja la dosis de 736× a
**100,6×**. Si además `e_conn` a 20 nm fuera ≤ **4,65e-4** (el máximo admisible medido en
TOLERA), el programa tendría una modalidad. **Se mide sobre CREMI, no se supone.**

- **P-3a · `e_conn` (Jaccard) a 20 nm será ≥ 0,05**, es decir **≥ 100× por encima del
  admisible 4,65e-4.** Cifra central predicha **0,35**, intervalo [0,05 , 0,80].
- **P-3b · el error dominante será FALSA FUSIÓN** (aristas de más), no omisión: a 20 nm la
  hendidura sináptica (~20 nm) no se resuelve y neuritas apuestas se funden. Predigo
  **FP > FN**, razón ≥ 3.
- **P-3c · la jaula NO arregla esto.** Restringir a la jaula deja `e_conn` dentro de 1,5× del
  valor sin jaula: la jaula acota DÓNDE mirar, no CON QUÉ resolución.
- **P-3d · el número de neuronas distinguibles caerá ≥ 20 %** frente a la verdad de campo.

*Si P-3a falla y `e_conn` ≤ 4,65e-4, hay modalidad y el programa cambia de fase.*
