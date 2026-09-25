# PREREG · las cuatro invenciones del investigador + la restricción equivocada

Escrito **antes** de correr. 2026-09-12.

## TRIADA paso 1 · INVENTARIO — y un hallazgo previo a las cuatro vías

`experiments/CAPA-D/code/landauer.py:29` fija el presupuesto como
`Q = 70 kg × 3500 J/kg/K × 0,1 K = 2,45e4 J`. **Es un criterio de HABITABILIDAD: no cocinar a
alguien vivo.** De ahí salen el 92.000× (EM 4 nm), el 736× (EM 20 nm) y el 2,35× (rayos X).

**En un teletransporte el cuerpo de origen SE CONSUME.** Nada hay que mantener vivo. La
restricción físicamente correcta para una lectura destructiva no es el calentamiento global
del cuerpo, sino **el daño por radiación antes de la medida**: cuánta dosis aguanta la
estructura sin destruirse mientras la mides. Es local, por vóxel, y obedece dos leyes opuestas:

- **dosis REQUERIDA** para resolver a `d` (criterio de Rose / estadística de fotones):
  `D_req ∝ d^(−4)`
- **dosis TOLERADA** antes de que el daño borre la estructura a esa escala (Howells et al.
  2009): `D_tol ∝ d`, del orden de **1e8 Gy a 10 nm** en material biológico vitrificado

El límite real del programa es **el cruce de las dos curvas**, y es una RESOLUCIÓN, no una razón
de energías.

- **P-D1 · el cruce caerá en [5 , 20] nm**, central **10 nm**.
- **P-D2 · con la restricción correcta, EM a 4 nm estará excedido por un factor en [10 , 1e4]**,
  no por 92.000× — el 92.000× mide otra cosa.
- **P-D3 · el presupuesto de habitabilidad y el de daño diferirán en ≥ 3 órdenes de magnitud.**
  *Si difieren poco, mi objeción no vale y el 92.000× se mantiene.*

## Las cuatro vías, evaluadas contra la restricción CORRECTA

### Vía 1 · ExM — **la que puede cerrarlo**
Expandir 10× lleva la resolución requerida en el gel de 4 nm a 40 nm. Como `D_req ∝ d^(−4)`:
- **P-1 · la reducción de dosis requerida será 10⁴ = 10.000×**, y además el material irradiado
  es gel muerto, no tejido vivo.
- **P-1b · el problema real de ExM NO es la dosis sino la ISOTROPÍA**: la deformación del gel.
  Predicción: la distorsión tolerable para preservar `e_conn ≤ 4,65e-4` será **< 1 % de
  deformación local**, muy por debajo del 1–4 % que la literatura de ExM reporta. *Ése es el
  número que decide la vía, y la matemática difeomórfica del investigador es la correcta.*

### Vía 2 · ghost imaging / sensado compresivo — **cota cerrada, se cierra sin correr**
CS reduce el número de MEDIDAS, no el número de FOTONES por unidad de información. La ganancia
máxima es la razón de escasez `N/s`. **Ya la medimos hoy** en CAGE50: la fracción de vóxeles con
interfaz a 32 nm es **0,1335**.
- **P-2 · ganancia máxima de CS = 1/0,1335 = 7,5×.** Contra un hueco de 4 órdenes: **falla**.

### Vía 3 · barcoding molecular — **no la mata ninguna cota obvia**
Elimina la dosis por completo: secuenciar no irradia. Los dos frenos reales:
- **P-3a · colisiones de códigos.** Con `N_cel = 3,36e13`, la longitud mínima para que las
  colisiones no superen `e_conn` admisible será **L ≥ 28 bases**. MAPseq usa 30-meros.
  Predicción: **el barcode NO es el cuello de botella**.
- **P-3b · el cuello será el VOLUMEN DE SECUENCIACIÓN**: `N_sin = 3e14` pares a leer.
  Predicción: **≥ 1.000 corridas de secuenciador**, es decir un problema industrial, no físico.

### Vía 4 · reescribir el contrato con ruido biológico — **barata y decisiva, se corre**
La sinapsis biológica falla espontáneamente el 10–50 % de las veces. Si la dinámica es invariante
a eso, un error topológico de 3e-3 puede ser irrelevante.
**El observable correcto NO es R contra 0,05 fijo, sino ⱎ y A**, porque añadir ruido sube el
SUELO y el contrato se mide contra el suelo.
- **P-4a · añadir fallo de liberación `p_fail` sube el suelo más rápido que Ω del acto**, así que
  **A NO mejorará**: predigo `A(p_fail=0,3) / A(0) ∈ [0,7 , 1,1]`, central **0,9**.
- **P-4b · si A mejora ≥ 1,3×, el contrato SE PUEDE reescribir y la vía 4 gana.**
