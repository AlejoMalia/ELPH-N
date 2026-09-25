# PREREG · CIERRE DE LAS 7 CAPAS · escrito antes de correr

El investigador pide llevar las siete capas al 100 %. **Antes de medir, lo que cada capa necesita
y si es alcanzable por medida:**

| capa | % | qué falta | ¿alcanzable hoy? |
|:--|--:|:--|:--|
| A | 98 | transferir el umbral a un **segundo espacio humano** | sólo si hay dato humano; `hdmea` es **rata** (comprobado: *Rattus norvegicus*, cultivo E18) |
| B | 75 | que el acto **pase** fidelidad | depende de `Π` (D) |
| C | 77,8 | `L_tramo` 3,2× y `p_costura` 9,5× · dominadas por `FFN` (±50 %) y `L_neurita` (10 ± 5 mm) | **sí por literatura** si hay ≥ 12 fusiones publicadas y una media de neurita con n |
| D | 70 | `Π` ≤ 2,81e-3; mejor valor publicado 3,1× fuera | **matemática de redundancia** + correlación de errores publicada |
| E | 75 | exponente de dos puntos · apilado 3D · analogía origami→célula | literatura (cinética de sitio, ensamblaje de células por ADN) |
| F | 80 | que el acto pase | depende de D |
| G | 75 | resolución en corazón · ramificación · filosófico | **medida** (corazón) + **cruce con D** (ramificación) + tejido real (`hdmea`) |

## MATEMÁTICA · predicciones con número

### G · corazón (medida)
La convergencia del sistema auxiliar cae como `e^(λ_cond·T)`. Con `λ_cond` = −0,029…−0,039 y T = 60
unidades, el suelo quedó en 0,010–0,087. **A T = 400 unidades (4.000 pasos) el factor adicional es
`e^(−0,033·340)` ≈ 1e-5.**
- **P-7G1.** `Ω_aux` en corazón < **5e-3** en **5 de 5** semillas (salvo filas multiestables).
- **P-7G2.** La razón `Ω(O_a,D_b)/Ω(O_a,D_a)` ∈ [0,9 , 1,1] en **5 de 5**.

### G · ramificación (cruce D → G, matemática)
La lectura de D (EM, ExM) **destruye el tejido**: el origen no sobrevive al acto. La ramificación de
Parfit exige **dos sucesores**, que sólo aparecen si se **fabrica dos veces** desde una lectura.
- **P-7G3.** Con la regla **DECLARADA** «una fabricación por lectura», el acto real no puede
  ramificar. *No es medida: es consecuencia de que la modalidad de D sea destructiva.*

### G y A · tejido REAL (`hdmea`, 12 cultivos × 3-4 sesiones, entrada `o` de 32 electrodos)
Persona = funcional entrada→salida. Perfil = respuesta media por estado oculto × electrodo.
- **P-7G4.** `Ω` entre sesiones de un mismo cultivo < `Ω` del impostor (permutación de direcciones)
  en **12 de 12** cultivos, con AUC = 1,0.
- **P-7G5.** La conexión es **gradual**: `Ω(ses1, ses_k)` **crece** con k en ≥ 9 de 12 cultivos.
- **P-7A1.** `Ω_imp` (permutación) = 0,98 ± 0,05 — universalidad en tejido vivo.

### C · literatura
- **P-7C1.** `L_neurita` media publicada con n ≥ 20 da ε (SEM, regla 202) ≤ 15 %.
- **P-7C2.** Si aparece una tasa de fusión automática con **≥ 12 sucesos**, `L_tramo` baja de 2×.

### E · cinética de SITIO, no de retícula
El exponente −3,97 salía del ensamblaje de **retícula** (cooperativo). La colocación en sitio es de
**primer orden**: `f = 1 − e^(−k·C·t)`. Con el dato de colocación publicado (40 % de sitios a 5 min,
110 pM): `k·C` = 1,70e-3 /s → **k = 1,55e7 /M/s**.
- **P-7E1.** La C para 90 % de ocupación en 16 s (montaje de 1 año) sale **≈ 9 nM**; la de 30 días,
  **≈ 110 nM**. Las dos dentro del rango rutinario (≤ 100 nM… la de 30 días en el filo).
- **P-7E2.** `k` estará dentro del rango publicado de hibridación en superficie (1e5–1e7 /M/s).
- **P-7E3 · F → E.** Invirtiendo `Ω_E ~ (σ/esp)^2,1` con los `cE` medidos, la σ que E **tolera por sí
  sola** (Ω_E ≤ 0,05) será **> 100 nm** → el origami (13,8 nm) sobra por > 7×.

### D · redundancia
Con k lecturas y una fracción **h** de aristas «difíciles» donde todas fallan juntas:
`Π_k ≈ h + C(k,⌈k/2⌉)·q^⌈k/2⌉`. **El requisito deja de ser `Π` y pasa a ser `h` ≤ 2,81e-3.**
- **P-7D1.** Con errores independientes (h = 0) y `e` = 0,0204 (LICONN), **3 lecturas bastan**
  (3e² = 1,25e-3).
- **P-7D2.** La literatura de acuerdo entre anotadores dará **h > 2,81e-3** — es decir, la
  redundancia **no** cierra D sola. *Si da menos, D cierra por matemática.*

## ADDENDUM · diseño de `hdmea` fijado antes de calcular (tras comprobar el formato, sin mirar respuestas)

Comprobado: **la secuencia de entrada `o` (256 ensayos × 32 electrodos) es IDÉNTICA entre las sesiones
de un cultivo** y distinta entre cultivos; 4 estados ocultos `s`. Dirección de un lugar = **posición
(x, y) del electrodo** — la ciudad en el globo.

- Respuesta: cuentas por electrodo en la ventana **[+10 , +300) ms** del inicio de cada ensayo.
- Electrodos: los presentes en **todas** las sesiones del cultivo, con ≥ 0,5 espigas/ensayo de media.
- **Perfil funcional** = respuesta media por estado `s` × electrodo, **centrada por electrodo** (se quita
  el mapa de tasas: queda sólo lo que depende de la entrada).
- Suelo = ensayos impares vs pares de la MISMA sesión · entre sesiones = impares de `a` vs pares de `b` ·
  impostor = perfil de `b` con las direcciones de electrodo permutadas (100 permutaciones).
- `A` = √(Ω_imp / Ω_entre).

## ADDENDUM 2 · tras ver `hdmea` en la ventana [10,300) ms — y ANTES de la ventana tardía

**P-7G4 (4/12), P-7G5 (3/12) y P-7A1 (Ω_imp 0,55 ± 0,34) FALLAN.** El diagnóstico post-hoc: el 60–85 %
de la varianza funcional es **modo común** (ráfagas de red, idéntico en todos los electrodos). Una
dirección equivocada **no puede** delatarse en la parte de la salida que no depende de la dirección.
Quitándolo (doble centrado), post-hoc: Ω_imp = 0,9974 ± 0,0090 y entre < impostor en 9/9.

**Confirmación preinscrita en datos DISJUNTOS: ventana tardía [300 , 900) ms**, mismos 12 cultivos, mismas
reglas + **mínimo 20 electrodos activos** (fijado ahora):
- **P-7A2.** Ω_imp (doble centrado) a **≤ 3 %** de 0,98337 en **≥ 8 de los cultivos válidos**.
- **P-7G6.** entre sesiones < impostor en **todos** los válidos.
- **P-7G7.** entre/suelo **≤ 2,0×** (la persona funcional persiste entre sesiones cerca del suelo).

## ADDENDUM 3 · corazón · antes de la prueba de fase

**P-7G1 FALLA:** a 4.000 pasos el suelo del corazón NO baja (0,0763 → 0,0766; 0,0812 → 0,0803). No era
convergencia lenta. Diagnóstico: la sincronización generalizada es **todo-o-nada por patrón de
entrada** — donde sincroniza, `Ω_aux` ≈ 1e-10; y en corazón **no sincroniza el 38–91 %** de las entradas
(H01 13–25 %, maleCNS 23–31 %). Con `λ_cond` ≈ −0,03, la hipótesis es **ciclo límite**: dos copias en la
misma órbita con fase distinta no convergen nunca (exponente nulo a lo largo de la órbita).

**Coincide con CAPAS C-002:** el estado dinámico del corazón real es *«una fase sobre un atractor»*
(7 bits por oscilador, medido en ECG-ID).

- **P-7G8.** Comparando la respuesta **promediada en fase** (media de los últimos 300 de 1.000 pasos),
  `Ω_aux` en corazón < **5e-3** en **≥ 4 de 5** semillas.
- **P-7G9.** Con la misma observable, `Ω(O_a,D_b)/Ω(O_a,D_a)` ∈ [0,9 , 1,1] en **≥ 4 de 5**.

## ADDENDUM 4 · tras fallar P-7G8 y P-7G9 (la media de fase no cambia nada: NO es ciclo límite)

Es **multiestabilidad bajo entrada**: para muchas entradas la red tiene varios atractores fijos. Entonces la
persona operativa = estructura + **qué atractor**. Eso es un coste en bits que el portador debe llevar.
- **P-7G10.** Contando atractores distintos por patrón de entrada (16 arranques), la entropía media será
  **≤ 2 bits por patrón** en los tres espacios, y **mayor en corazón** que en H01 y maleCNS.
