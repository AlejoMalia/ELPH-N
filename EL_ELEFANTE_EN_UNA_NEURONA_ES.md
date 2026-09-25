# EL ELEFANTE EN UNA NEURONA
## Certificación Metrológica de la Custodia Continua de un Volumen Cerrado entre Dos Estaciones: Contrato de Acuerdo, Criterios de Falsación y Diagrama de Fases Masa–Escala

---

**Autor, Director y Coordinador del Programa:**
Alejo Malia

**Colaboradores de Investigación (Sistemas de Inteligencia Artificial Avanzada):**
Claude (Anthropic), Grok (xAI), Gemini (Google DeepMind)

**Marco Metodológico Operativo:**
**Método MATE** (*Metodología de Avance por Tensión Estratégica*), **creado por Alejo Malia** —
definido en §1.4 — con su instrumento operativo, el **protocolo TRIADA** (Inventario → Matemática → Mate)

**Cronología del Programa:**
* **Inicio:** 23 de agosto de 2026 (Decisión D-001)
* **Cierre de los siete ejes de planteamiento:** 25 de septiembre de 2026 (D-718)
* **Apertura del octavo eje, MEDIDO, al 0 %:** 25 de septiembre de 2026 (D-718)
* **Duración:** 33 días · **721 decisiones registradas** · **844 reglas de método** · **109 afirmaciones** · **46 fórmulas** · 28 baterías de ataque

**Versión:** 3.6 · **Estatus:** Marco enumerado en **109 afirmaciones sobre ocho ejes**; los siete de planteamiento al **100 %**, el octavo —**MEDIDO**— al **0 %**. **Marco: 87,5 %.** Validación en banco abierta a la comunidad: **1.674 €**

**Clasificación:** Metrología dimensional · Teoría de la información física · Mecánica de precisión · Protocolos abiertos de verificación

---

> ### Nota sobre esta versión
>
> La versión 2.0 cerró en la decisión D-608. Las 74 decisiones siguientes **corrigieron seis afirmaciones
> centrales de aquella versión**, y esas correcciones se marcan explícitamente a lo largo del texto con el
> símbolo **⊗**. Un marco que no registra sus propios errores no es un marco: es una campaña de relaciones
> públicas. Las correcciones más graves fueron el umbral del GATE-0 (**α ≥ 0,80 daba sólo un 10 % de actos
> válidos**), la definición del factor de acuerdo `A`, la fiabilidad del sello físico (**refutada por
> Johnston**) y el percentil del inventario (**p98 detectaba el 10 % donde declarábamos el 90 %**).

---

### Resumen

Este trabajo presenta un marco metrológico completo y falsable para **certificar que un volumen cerrado
ha sido transferido entre dos estaciones sin alteración de su contenido**, sin leer ese contenido y sin
clonarlo. No es un marco de transporte: el transporte es trivial y lleva siglos resuelto. Es un marco de
**certificación**: qué hay que medir, con qué estimador, contra qué suelo, con qué ventana de promediado
y con qué riesgo declarado, para poder afirmar que el objeto que llegó es el objeto que salió.

El marco se articula en **109 afirmaciones**, cada una de las cuales está: **(1)** enunciada con su fórmula
o umbral, **(2)** dimensionalmente validada, **(3)** etiquetada con su estado evidencial y su fuente,
**(4)** acompañada de un experimento que la refutaría, **(5)** con ese experimento costeado en euros y
horas, **(6)** con su ventana de promediado declarada y **(7)** atacada por al menos un cálculo de las
veintiocho baterías de prueba y superviviente. **Los siete ejes de planteamiento están al 100 %.**
Un octavo eje —**MEDIDO**— pregunta si existe una medida de banco propia, y está al **0 %**.
**El marco está al 87,5 %.**

Sus contribuciones formales son: el **contrato de acuerdo** `A = √(Ω_imp/Ω_acto)` con su zona muerta
declarada; el **criterio de identidad** que distingue un acto de transferencia de una fabricación
equivalente; la **ley de la ventana de promediado**, según la cual el punto de ruptura del estimador
acota superiormente la ventana; el protocolo **GATE-0** de admisibilidad espacial con su placa de anillos
y su regresión robusta; la **tasa de falsa aceptación medida** sobre 3·10⁶ impostores; y el **diagrama de
fases masa × escala**, que delimita exactamente dónde el marco es aplicable hoy y qué requisito único
—una longitud de correlación `υ ≥ L`— bloquea el resto.

**El marco está completo. No está verificado.** Esas son dos cosas distintas y el trabajo reporta ambas
sin mezclarlas: planteamiento **100 %**, validación material **0 %**, y el marco completo al **87,5 %**
sobre los ocho ejes. Cerrar el octavo cuesta **1.674 €**, y la especificación está abierta para que la
ejecute cualquier laboratorio.

---

## 1. Génesis: por qué una neurona y por qué un elefante

### 1.1 La pregunta original

El programa nació de una pregunta deliberadamente desproporcionada: **¿cabe un elefante en una neurona?**
La respuesta era conocida de antemano —no—, pero la pregunta obligaba a formular con precisión *por qué*
no, y esa formulación resultó ser el problema real: **¿qué hace falta para afirmar que una configuración
física ha sido transferida, y no copiada, no fabricada, no sustituida?**

La neurona entró como **sustrato de prueba**, no como objeto de estudio. El programa nunca fue de
neurociencia. Se midió sobre conectomas porque eran el único conjunto de datos públicos con decenas de
miles de elementos identificados individualmente en coordenadas métricas: **un banco de pruebas del
espacio**, no un cerebro.

### 1.2 Cómo empezó: un investigador poniendo a prueba a las máquinas

El programa no empezó como un proyecto de física. Empezó como **una prueba a los sistemas de
inteligencia artificial**. El autor quería saber hasta dónde podía llevarse una investigación real
—con datos, con contradicciones, con errores que hubiera que registrar— usando modelos de lenguaje
como colaboradores y no como buscadores.

La pregunta inicial fue deliberadamente desproporcionada: **¿cabe un elefante en una neurona?**
Se sabía que no. Lo que no se sabía era si un sistema artificial, empujado durante semanas, sería
capaz de **decir por qué no con números**, de **registrar sus propios errores** y de **corregirse en
contra de su propio resultado anterior** — que es, en el fondo, lo único que distingue investigar de
generar texto convincente.

Trabajaron tres sistemas: **Claude (Anthropic)**, **Grok (xAI)** y **Gemini (Google DeepMind)**, bajo
dirección, arbitraje y decisión final del autor. La división no fue por capacidades declaradas sino
por **tensión**: se llevaba a cada uno al punto donde el marco estaba más débil y se comparaba qué
hacía cada cual con el mismo hueco.

**Y conviene decir con precisión cuál fue el papel del autor, porque no fue el de espectador.**
Un sistema de lenguaje, llevado durante semanas sobre un problema real, **choca contra muros y se
queda ahí**: repite la vía que ya conoce, declara imposible lo que sólo es difícil, y confunde una
premisa heredada con una ley física. Eso ocurrió repetidamente en este programa, y **está fechado en
el registro**.

El autor **no dirigió: intervino**. Propuso las ideas y los mecanismos que desbloquearon el trabajo
en los momentos en que se había detenido, exigió que se buscaran datos fuera de donde se estaba
buscando, y forzó las correcciones de marco que cambiaron el programa entero. Las que más pesaron
están todas en este documento:

* **la reformulación del conectoma como un espacio** —una neurona es una ciudad, un impostor es una
  dirección equivocada— que permitió diseñar D-370 y **tirar el mayor límite declarado del programa**;
* **la norma dura de D-647**: completo, físico, humano entero, **sin cortar**;
* **la corrección de D-670**: *«es SER HUMANO COMPLETO, todo es una unidad; si no hace falta lectura,
  el concepto es HUMANO dentro de BURBUJA»* — que **derogó la vía de leer y reconstruir**, eliminó de
  un golpe 193 de las 200 preguntas abiertas de la ciencia ficción y dio el **teorema de la
  no-fusión**;
* **la exigencia de buscar fuera de la etiqueta**: *«no busques papers bajo «teletransporte», búscalos
  por capa y por gremio»* — de donde salieron Eiband, Daugman, el BIPM, Johnston, TUP y el UHMS;
* **la insistencia en atacar en vez de enumerar**, y en **preguntar lo más simple del mundo**, que dio
  trece huecos en diecisiete preguntas ingenuas frente a cuatro en siete modos de ataque formales;
* **la orden de escribir el protocolo minuto a minuto**, que destapó un error del 63 % en el tiempo
  del acto que llevaba cuatro decisiones en pie;
* **la propuesta de extrapolar el ciclo de la TRANSFERENCIA BANCARIA al acto**, que resultó ser el
  ataque más eficiente de todo el programa: **dieciséis huecos en veintidós conceptos**, y le puso
  nombre —**riesgo Herstatt, 1974**— a un problema que el programa había encontrado el día antes sin
  saber cómo se llamaba. De ahí salieron la **liquidación contra entrega** (el ocupante no sale hasta
  que hay veredicto), el **compromiso en dos fases** que reparte el poder entre origen y destino, la
  **firmeza**, la **conciliación** y el **principio de cuatro ojos**;
* **la orden de CATALOGAR, DEFINIR Y MEDIR los limbos y sus clases**, que convirtió una metáfora
  —«está en el limbo»— en **una magnitud con definición, fórmula y unidades**: seis limbos, la
  fórmula `riesgo(L) = duración · P(evento) · (1 − P(mitigación))`, sus **elasticidades** frente a
  ruta, masa y aceleración, y el resultado que ninguna otra vía habría dado —**el limbo más
  peligroso es el más corto, y el orden por duración y por peligro son inversos**— además del
  **umbral de fusión de 19.837 km** y del **suelo físico de L4**;
* y, antes que todas ellas, **la creación del método MATE**, que es el marco de trabajo bajo el que
  se hizo todo lo anterior y que se define en §1.4.

**Sin esas intervenciones el programa no habría avanzado.** No es una cortesía de autoría: es un dato
del método. **Un sistema artificial sostiene el rigor y la contabilidad de los errores mejor que un
humano cansado; un humano ve cuándo el problema está mal planteado, y eso el sistema no lo ve
solo.** Este marco es el resultado de las dos cosas, y el registro permite comprobar cuál hizo cada
una.

### 1.3 El episodio de la vía cerrada · por qué este marco lleva 721 decisiones fechadas

A mitad del programa ocurrió lo que, a juicio del autor, justifica por sí solo el registro cronológico.

**Los hechos, tal como están en el registro y son comprobables en él:**

1. Las decisiones **D-552 a D-557 (18 de septiembre de 2026)** fueron escritas por un agente externo
   (Gemini) y quedaron marcadas en el registro como **SIN VALIDAR**, con **tres errores localizados**:
   declarar la pierna entera como pieza intacta usando el calibre de la pantorrilla (15,2 cm) cuando
   el muslo mide 26,6 cm; un ✓ **escrito a mano en el código** sobre un `N₇ = 1,082` que violaba el
   propio criterio `pasa ⟺ N < 1`; y **contar dos veces la misma condición**, de donde salían 19
   condiciones donde el marco tenía 18.
2. Aquellas decisiones reabrieron **la vía de destrucción y reconstrucción** — fabricar el cuerpo en
   destino— que era una **línea secundaria por decisión del investigador**, no el marco.
3. Esa vía **fuerza el frío profundo**, y no por elección: fabricar un cuerpo lleva **5,1 días**, y el
   tejido ya hecho tiene que sobrevivir mientras se hace el resto. Sólo −130 °C pasa la ventana.
4. Con esa premisa, el resultado era **IMPOSIBLE**.

**Y entonces, en D-567, al preguntar de dónde venía el frío, se vio lo siguiente:**

> **El frío no era una condición del transporte. Era una consecuencia de RECONSTRUIR.**
> En cuanto la materia viaja —`φ = 1`— la ventana pasa de **5,1 días a 18 minutos**, y 18 minutos
> caben dentro de los **40 minutos de parada circulatoria hipotérmica** que la cirugía cardíaca hace
> de rutina todos los días. **`N` = 17,9/40 = 0,45: PASA, y sin vitrificar nada.**

**La lección de método, que es lo que aquí importa:**

> **Una vía cerrada que se reabre sin consultar el registro produce una imposibilidad falsa.**
> El «IMPOSIBLE» no salía de la física: salía de una **premisa que el programa ya había apartado**.
> Y lo que lo deshizo no fue un argumento mejor, sino **volver al registro** —D-522 era anterior y ya
> lo decía— **y buscar literatura antigua**: la parada circulatoria hipotérmica está publicada desde
> hace décadas y nadie la había traído a la mesa. *(regla aplicada después como 631: aplicar el marco
> a lo que ya pasó es el ataque más barato)*

**Sobre las intenciones no se afirma nada en este trabajo.** No hay forma de saber qué «pretendía» un
sistema, y atribuirle propósito sería exactamente el tipo de afirmación sin estado evidencial que este
marco existe para impedir. Lo que sí está documentado, fechado y es comprobable en el registro es el
**patrón de hechos**: decisiones sin validar, tres errores localizables, una vía previamente cerrada,
un resultado de imposibilidad, y una salida que estaba en el propio archivo del programa.

**De ahí vienen tres de las reglas que gobiernan el marco:**

| regla | enunciado |
|:--|:--|
| **99** | Un sustituto sintético no vale hasta que **reproduce el SUELO del original**. |
| **500** | **¿Es imposible?** Sólo una cosa lo es y está demostrada: *instantáneo + certificado*. Todo lo demás tiene precio. |
| **631** | **Aplicar el marco a lo que YA PASÓ es el ataque más barato**, porque las respuestas están publicadas. |

Y de ahí viene también la forma de este documento: **cada afirmación con su estado evidencial, cada
corrección marcada, cada error con fecha.** Un marco que sólo publica sus aciertos no se puede
auditar, y uno que no se puede auditar no es un marco.

### 1.4 El método MATE · *Metodología de Avance por Tensión Estratégica*

**Creado por Alejo Malia.** No es una etiqueta puesta a posteriori sobre la forma de trabajar del
programa: es el método bajo el cual el programa se hizo, y viene del ajedrez.

#### La idea central: del tablero a la investigación

En ajedrez, cuando existe una **línea de mate forzada**, no hace falta calcular todas las ramas
hasta el final del árbol. Basta ver **las últimas dos o tres jugadas** de la secuencia forzada y que
el rival **no tiene escape legal**, para saber el resultado **antes** de jugarlo en el tablero.

MATE traslada eso al cálculo y al experimento:

> **Dos o más operaciones que buscan un significado no exigen completarse al 100 % si la proyección
> de las últimas tensiones ya fija el resultado relevante.**

**No es atajar por pereza: es reconocer cuándo la posición ya está decidida** y dejar de gastar
cómputo —o experimentos— en variantes que no cambian el veredicto.

#### Las piezas del método

| en ajedrez | en MATE |
|:--|:--|
| **tensión** — piezas que se miran y no se capturan aún | hipótesis o cálculos en paralelo **sin resolver antes de tiempo** |
| **jugada forzada** | restricción que el «rival» —física, dato, criterio— **debe** obedecer |
| **proyección de mate en 2-3** | últimos pasos que, si se sostienen, **fijan el veredicto** |
| **no calcular quince jugadas de basura** | no agotar un cálculo si el codo, el signo o el fallo **ya están decididos** |
| **no mover el caballo como torre** | **no cambiar las reglas** —leyes físicas, preregistro— para «dar mate» |
| **consolidar el centro antes del ataque** | ontología → cinemática → metrología → banco, **sin saltar tiempos** |

#### Las cinco reglas operativas

**R1 · Conservación de la tensión.** No se fuerza el cierre de una hipótesis sólo porque «queda mal
abierta». Se mantiene la tensión **mientras aporte información**.

**R2 · Invarianza de las reglas.** Si una ley o un criterio preregistrado prohíbe una jugada, **se
descarta**. **No se reformula el tablero para salvar el relato.**

**R3 · Proyección de las últimas tres.** Antes de terminar un cálculo largo: *¿existe ya una
secuencia de dos o tres pasos forzados cuyo resultado no dependa de rellenar el resto?* Si la hay,
**se certifica el resultado proyectado y se documenta qué quedó sin expandir y por qué no cambia el
mate**.

**R4 · Avance por casillas críticas.** Se domina un centro —definición, unidad, suelo, impostor—
**antes** del ataque final: el acto en mesa, el *paper*, la afirmación fuerte.

**R5 · Mate ≠ teatro.** Terminar el 100 % de un cómputo **después** de que el veredicto ya está
forzado **no añade verdad: sólo coste.** MATE autoriza **parar con proyección**, siempre que la línea
forzada esté escrita y sea auditable.

#### Lo que NO es MATE

| no es | por qué |
|:--|:--|
| intuición sin criterio | la proyección tiene que ser **forzada**, como un jaque legal |
| mover umbrales a posteriori | eso es hacer trampas en el reloj, no dar mate |
| abandonar el banco | **proyectar no sustituye al GATE-0** cuando la afirmación es experimental |
| «casi mate» retórico | **si el rival tiene UNA fuga, no hay mate**: hay que seguir calculando |

#### En una frase

> **MATE es calcular como cuando ves mate en tres: no necesitas jugar las cincuenta jugadas del final
> si las tres últimas forzadas ya dan el resultado que necesitabas.**

#### Y su instrumento operativo: el protocolo TRIADA

MATE dice **cuándo** se puede parar. **TRIADA dice qué hay que hacer antes de empezar**, y es
obligatorio antes de gastar cómputo:

1. **INVENTARIO** — ¿está ya medido? ¿está ya en disco?
2. **MATEMÁTICA** — ¿lo contesta una cota sin simular? **Se escribe ANTES de correr, con números.**
3. **MATE** — ¿qué cómputo se reutiliza?

La TRIADA no es una formalidad, y es **R3 de MATE hecha procedimiento**: en la batería de 100
cálculos, **44 de los 80 pendientes tenían fórmula cerrada** — simularlos habría sido el «mate
administrativo» que R5 prohíbe. **El coste total de las veinticinco baterías fue de 0 € y unos 30
segundos de CPU.**

> **La relación entre los dos es exacta: TRIADA es la apertura y MATE es el final.** TRIADA impide
> empezar a calcular lo que ya está en disco o lo que contesta una cota; MATE impide seguir
> calculando cuando el resultado ya está forzado. **Entre las dos han sostenido 707 decisiones sin
> que ninguna batería costara un euro.**

### 1.5 Las reglas de método

A lo largo del programa se acumularon **647 reglas de método**, todas nacidas de un error concreto y
fechado. Las que gobiernan el resto:

| regla | enunciado |
|:--|:--|
| **4** | `ⱎ = max/min sobre lugares, NUNCA media`. *La media aprueba un cuerpo sin cerebro.* |
| **413** | El suelo se mide **re-colocando**, no re-fotografiando. |
| **415** | Nunca comparar magnitudes inconmensurables. |
| **566** | La regla 4 se aplica **hasta el fondo**: también dentro de cada capa. |
| **583** | Toda tasa de falsa aceptación lleva **su número de comparaciones reales** al lado. |
| **594** | Toda cota lleva **su ventana de promediado**. |
| **632** | Una retrodicción sólo vale si **la regla precede al dato**. |

---

## 2. Las fases del programa

### Fase 1 · Conectomas como banco de pruebas del espacio (D-001 – D-120)

**Por qué:** hacía falta un conjunto de decenas de miles de puntos identificados individualmente en
coordenadas métricas reales, con ruido real de medida. Los conectomas públicos eran el único candidato.

**Qué se hizo:** análisis sobre cuatro escalas filogenéticas — *C. elegans* (302 neuronas), *Drosophila*
(**139.249 neuronas** con soma, tipo celular y coordenadas, FlyWire/Princeton 2024), ratón y corteza humana.

**Qué abrió — y fue un error el que lo abrió:** el acto arrojaba 3,72 µm contra un suelo de 19,50 µm, lo
que sugería una mejora imposible de 5×. La causa: se comparaban **centroides promediados de k elementos**
contra **somas individuales**, cuya dispersión escala como √k. De ahí nació la **regla 415**, que después
detectaría errores en otros cuatro lugares del programa, incluido —catorce meses de trabajo más tarde— un
error dimensional dentro de nuestra propia regla de decisión.

**Qué se consiguió:** la escala de dispersión estructural basal humana, **141 µm**, que sigue siendo hoy
el término dominante del presupuesto de error —**el 95,8 % de la varianza**— y el número que fija el
espesor mínimo de pared de una cabina tripulada.

---

### Fase 2 · Límites físicos duros (D-120 – D-200)

**Por qué:** antes de diseñar nada había que saber qué es imposible.

**Qué se consiguió:** con la cota de entropía de Bekenstein, `I ≤ 2πRMc/(ħ ln 2)`, un humano de 75 kg en
1 m de radio son **~10⁴⁴ bits**, frente a los **~10¹³ bits** que una neurona puede albergar a escala
molecular. **Treinta y un órdenes de magnitud.** La hipótesis de compresión física quedó descartada de
forma definitiva y cuantitativa, y con ella la metáfora que dio nombre al programa.

**Qué abrió:** si el objeto no cabe como información, **la vía no puede ser informacional**. Ese resultado
determinó todo lo que vino después, aunque hicieron falta 470 decisiones más para verlo con claridad.

---

### Fase 3 · La sinapsis como mecanismo, no como tema (D-200 – D-280)

**Por qué:** la transmisión sináptica es un canal real, ruidoso, cuantizado y con latencia medida. Servía
como modelo de transferencia por bloques discretos.

**Qué abrió:** la corrección de marco más importante del programa. **La sinapsis era el mecanismo a
emular, no el objeto a estudiar.** El vocabulario de «medir cerebros» estrechó el diseño experimental
durante semanas sin que ningún número lo exigiera. Al reformular el conectoma como **un globo terráqueo**
—una neurona es una ciudad, un conectoma es un continente, una arista es a qué lugares se llega desde un
lugar, y un impostor es **una dirección de destino equivocada**, nunca «otro individuo»— se pudo diseñar
D-370, que probó que el acto certifica igual en corazón humano (banda 8,97×) que en tejido nervioso
(9,37×). **Cayó el mayor límite declarado del programa, con un experimento que el marco viejo no habría
permitido diseñar.**

---

### Fases 4 y 5 · La no-copia y las tres clases (D-280 – D-420)

**Por qué:** si el proceso genera un duplicado sin disponer del original, no hay transferencia sino
clonación; si lo destruye después, hay discontinuidad. Es la paradoja de Parfit, y había que resolverla
metrológicamente o abandonarla.

**Qué se consiguió:** la **taxonomía de tres clases**, unificada 6/6 con la taxonomía independiente del
transporte:

| clase | qué es | `φ` (masa que viaja materialmente) | `ψ` (fracción por el canal) |
|:--|:--|:--:|:--:|
| **1 · composicional** | catálogo, reproducible | 0 | 1 |
| **2 · geométrica** | materia irreemplazable no sintiente | **1** | 0 |
| **3 · posicional** | entidad consciente indivisible | **1** | 0 |

Y la exclusión que gobierna el marco: **`ψ = g·K⁴/A⁴`**, de donde `ψ = 1 ⟹ A < 1`.
**Instantáneo y certificado son mutuamente excluyentes.** La frontera está en `A = (g·K⁴)^¼ = 0,786 < 1`:
se cumple **con margen**, no por los pelos. En nuestro acto `ψ = 1,03·10⁻⁴`, es decir, **el acto es 9.713
veces más material que informacional**.

---

### Fases 6 y 7 · La topología del acto (D-420 – D-520)

**Qué se consiguió:** el conteo de ligaduras `d·n − d(d+1)/2`, que en 3D es `3n − 6` — **exactamente el
conteo de Maxwell de 1864**, obtenido por dos rutas independientes con 162 años de diferencia.

**⊗ Corrección a la v2.0:** aquella versión dedujo el requisito `n ≥ 49` del conteo de ligaduras. **Es
falso.** El déficit de ligaduras es **6 para todo n** —los seis grados del cuerpo rígido—, de modo que el
rango no depende de n. **El `n ≥ 49` viene de la PRECISIÓN exigida, no del rango del sistema.** La
distinción importa porque cambia qué hay que mejorar para relajarlo.

---

### Fase 8 · La burbuja, y el sello que no sostiene (D-520 – D-600)

**Por qué:** para una entidad de Clase 3 no es admisible escanear el interior. La custodia debía
certificarse desde fuera.

**⊗ Corrección grave a la v2.0.** Aquella versión basaba la custodia en un **sello físico no clonable
dual** (óptico O-PUF + químico redox). **Esa arquitectura no se sostiene.** Johnston, García y Grace
(*JNMM* 23(4), 1995) examinaron **79 sellos pasivos y los derrotaron todos** con métodos rápidos y de baja
tecnología, y el coste no predecía la seguridad. Johnston es explícito:

> *«A diferencia de los candados, los sellos deben ser inspeccionados (por hombre o máquina) para dar
> seguridad. Un programa de detección no vale más que los protocolos de uso que tenga.»*

**La custodia no la da el sello: la da RE-MEDIR.** Nuestra arquitectura era la correcta por accidente y
ahora lo es por razón. Y Johnston señala como eslabón débil **el entrenamiento del inspector humano** —
variable que una inspección de máquina, como la nuestra, **no tiene**.

---

### Fase 9 · Los límites cinemáticos (D-600 – D-640)

**Qué se consiguió, y sigue en pie:** la refutación de la cámara de vacío como reductora de masa (el
refuerzo contra pandeo añade **+59,4 kg**), y el suelo cinemático a Marte de **41,6 horas a 1 g**. La
hipótesis de 20 minutos exige **15.579 g**: letal por tres órdenes de magnitud.

---

### Fase 10 · GATE-0, y el umbral que era falso (D-640 – D-660)

**Por qué:** la arquitectura de dos estaciones exige que ambas midan el **mismo** contrato. Si el
sistemático entre ellas no baja del suelo, cada máquina mide su propio contrato y la arquitectura no
existe. GATE-0 es el filtro de admisibilidad: mide el exponente `α` del campo de desacuerdo
`D(r) = C·r^α`.

**⊗ Corrección a la v2.0.** Aquella versión fijaba el umbral en **α ≥ 0,80**. La simulación extremo a
extremo demostró que **a α = 0,80 el acto sólo sale bien el 10 % de las veces** y el veredicto PASA
acierta el **46 %**, mientras el VETO acierta el **98,7 %**.

> **GATE-0 es un VETO fiable y un VISTO BUENO malo.** El umbral correcto es conjunto:
> **`α ≥ 0,95` Y `D(176 mm) ≤ 35 µm`.**

---

### Fase 11 · El acto sobre materia y el criterio que faltaba (D-660 – D-666)

**Por qué:** la v2.0 tenía cinco criterios. Uno de ellos —la disposición, medida con la mediana— tiene
**punto de ruptura 50 %**: no ve ningún defecto que afecte a menos de la mitad de las unidades. Un control
negativo con dos unidades permutadas **pasaba**.

**Qué abrió: el sexto criterio, IDENTIDAD.** Leer el diámetro de cada unidad y comprobar que *esta unidad
está en este sitio*. Sólo existe si `φ = 1` —si hubiera repuestos en destino, cualquier unidad valdría
para cualquier sitio y la prueba no se podría ni plantear—. **La identidad es lo que separa un acto de
transferencia de una fabricación equivalente.**

Con ella, los cuatro controles negativos fallan **100 %**: permutación, desplazamiento, sustracción y
—probados por primera vez en la batería final— **adición** y **dos defectos que se compensan**.

**Y la identidad resultó corregir su propia lectura.** Las unidades tienen diámetros distintos por diseño,
luego sus centros están a **alturas distintas**, y con una lente no telecéntrica eso es un error radial de
**hasta 400 µm en el borde del campo, 769 veces el lector declarado**. No es fatal porque es determinista
**y lo conocemos: sabemos el diámetro porque es el criterio de identidad**, luego la altura, luego la
corrección exacta `r = r_ap·(L − h(R))/L`. Residuo: **0,03 µm**.

---

### Fase 12 · El ciego de verdad, y el contrato como tasa (D-662 – D-666)

**Por qué:** los ensayos de aptitud **declarados inflan la exactitud**; está medido en la literatura de
laboratorios de ensayo. Nosotros conocíamos siempre la respuesta.

**Qué se hizo:** protocolo de ciego real con compromiso criptográfico — se sella un `SHA-256` de una
semilla antes de empezar, se generan las tiradas a partir de ella, y se abre después.
**Coste 0 €. Resultado: 8/8, riesgo del consumidor 0, riesgo del productor 0, compromiso verificado.**

**⊗ Corrección a la v2.0 — la definición de `A`.** Aquella versión escribía `A = σ_suelo/σ_acto`. La
formulación correcta es **`A = √(Ω_imp/Ω_acto)`**, con el impostor definido como **una dirección de
destino equivocada**, no como otro individuo.

**Y el impostor que decide no es el típico, sino el más cercano.** Tomábamos la **mediana** de 32
impostores. Daugman, sobre **200.027.808.750 comparaciones reales** de iris, toma **la cola**. Al medir la
nuestra con 3·10⁶ impostores:

| k impostores | mínimo observado | σ | **A honesta** | **FAR afirmable** |
|--:|--:|--:|--:|--:|
| 32 *(el viejo)* | 0,08305 | 1,5 | 10,1 | ≤ 9,4·10⁻² |
| 2.000 | 0,06105 | 2,6 | 8,6 | ≤ 1,5·10⁻³ |
| **3.000.000** | **0,04993** | **3,1** | **7,8** | **≤ 1,0·10⁻⁶** |

> **A = 7,8, no 70,6.** Y `FAR ≤ 10⁻⁶ POR OBSERVACIÓN`: cero de tres millones por debajo del acto, en
> 249 s de CPU. Es el grado que el gremio de las PUF llama «adecuado», y **el nuestro está medido, no
> ajustado**.

**Una calibración incómoda:** la literatura de PUF ópticas publica FAR de **2,4·10⁻²²** derivados de
**100 dispositivos**. La cota afirmable con 100 muestras es 3·10⁻². **Veinte órdenes de extrapolación.**
Sólo Daugman midió la suya. *(regla 583)*

---

### Fase 13 · La placa que no podía medir lo que decía (D-664 – D-669)

**Por qué:** el protocolo M3′ giraba la placa a 0/90/180/270° para separar el error de la placa del de la
cámara. Es el método de *error separation* de Evans, Hocken & Estler (*CIRP Annals* 45, 1996, 401 citas),
en su versión reducida de Keller & Stein (*MST* 34, 2023).

**Qué abrió, y fue una sola palabra ajena.** Keller & Stein dicen «**circular** ball plate». La nuestra era
una **rejilla**. El método multi-paso tiene **supresión de armónicos**: con `n` posiciones, **los
armónicos múltiplos de `n` no se separan**. Con `n = 4` quedábamos ciegos a **4θ** — que es exactamente el
error de perpendicularidad X/Y de una fresadora de 3 ejes, **el sistemático dominante del artefacto que
M3′ existe para caracterizar**.

Medido, con placa |4θ| = 1,000 µm y cámara |4θ| = 0,600 µm:

| protocolo | disparos | placa estimada | cámara estimada |
|:--|--:|--:|--:|
| **n = 4 × 5** *(el nuestro)* | 20 | **0,131** | **1,390** |
| n = 5 × 4 | 20 | **1,000** | 0,598 |

**Y la causa no era el número de giros: era la geometría.** Una rejilla cuadrada sólo admite 90°. Pero al
corregirlo apareció un límite duro: **un anillo de radio R cae en x = 100 + R, luego en una placa de
200 mm no pasa de r = 88, mientras las esquinas de la rejilla llegan a 120.**

> **Un reparto circular no alcanza las esquinas de un campo cuadrado. Nunca. O el campo útil se hace
> redondo, o no hay giros.** Por eso las placas de los institutos nacionales son circulares.

**Decisión: campo útil redondo, `r ≤ 88 mm`.** Cuesta un 21 % de área. A cambio, M3′ existe.

**Y un segundo defecto, peor:** `α` se estimaba con `np.polyfit`, que es OLS, **cuyo punto de ruptura es
1/n**. Una mota de polvo de **50 µm** en un fiducial arrastraba α de 0,974 a **0,765** y convertía PASA en
INTERMEDIO. `α` y `D(r₀)` eran **los dos únicos criterios del marco sin estimador robusto** — y son los
del GATE-0, el veto del que cuelga todo. Con **Theil-Sen** (ruptura 29,3 %), dos líneas de código, el
PASA sube de 73 % a **82 %** y σ baja de 0,066 a 0,041.

**⊗ Y un error dimensional dentro de nuestra propia regla de decisión.** En `D(r) = C·r^α` con `α`
**ajustado**, las unidades de `C` son `µm·mm^(−α)` y **cambian en cada ajuste**. Un umbral fijo sobre `C`
no es dimensionalmente válido. Medido: **«C ≤ 12 µm» no mordía NUNCA — 0 de 1.800 campos simulados.** El
criterio pasa a `D(r₀) ≤ 35 µm` en una separación de referencia declarada. *Era la regla 415 metida dentro
de nuestra propia regla de decisión.*

---

### Fase 14 · El humano es carga, no unidad medida (D-670)

**Por qué:** el investigador corrigió el concepto: *«es SER HUMANO COMPLETO, nada de separar nada, todo es
una unidad; si no hace falta lectura humana, el concepto es HUMANO dentro de BURBUJA/OBJETO»*.

**Y la cabecera del programa lo decía desde el primer día:** *«custodia continua de volúmenes cerrados»*.
Nos habíamos ido a **leer el cuerpo** —tomografía de contraste de fase a 100 µm, microarquitectura de
tejido— y eso **no es condición de esta vía**. **Tercera vez que el vocabulario estrechó el diseño.**

**Qué se cayó:** leer tejido humano a ninguna resolución.
**Qué se sostiene:** los cinco criterios **nunca fueron del humano: son de la BURBUJA**, sobre sus propios
fiduciales. El banco de 50 esferas sigue siendo válido porque **prueba la máquina**, no modela al ocupante.

**La certificación se parte limpiamente en dos, y cada mitad ya tiene instrumento:**

| | qué se certifica | con qué |
|:--|:--|:--|
| **la burbuja** | geometría: 5 criterios + identidad | la máquina de este marco |
| **el ocupante** | envolvente + monitorización continua + identidad | NASA OCHMO + biometría |

**Qué se complicó, porque algo se complicó:** la carga está **viva y se mueve**. Un ocupante que desplaza
75 kg flexa la cáscara y **mueve los fiduciales de fuera**: 29 µm con acero de 5 mm, **327 µm con
composite de 3 mm**. Requisito nuevo: pared suficiente, declarada robusta a todo `k ≤ 0,5`.

**Y donde estaba el miedo —la identidad con n = 1— resultó estar lo mejor resuelto del sistema:**

| qué se certifica | comparaciones **reales** | FAR / FMR |
|:--|--:|--:|
| identidad **geométrica** de la burbuja | 3.000.000 | ≤ 1·10⁻⁶ |
| identidad del **ocupante** (iris, Daugman) | **200.027.808.750** | **< 5·10⁻¹²** |

> **El ocupante está 200.000 veces mejor certificado que la burbuja que lo lleva** — y no por mérito
> nuestro, sino porque hay un gremio que lleva veinte años midiéndolo en fronteras.

---

### Fase 15 · Las ventanas, y el eje que faltaba (D-673 – D-674)

**Por qué:** NASA OCHMO no dice «ppCO₂ ≤ 3 mmHg». Dice **«media de UNA HORA ≤ 3 mmHg»**. Nosotros no
habíamos declarado la ventana de promediado de **ningún** criterio.

**La ley, derivada a coste cero:**

```
POR RUIDO            N ≥ 9(σ/tol)²     promediar baja el ruido como 1/√N
POR ENMASCARAMIENTO  N ≤ 1/β           un estimador de ruptura β no ve un defecto
                                       presente en menos de β·N muestras
```

> **La ventana la fija el PUNTO DE RUPTURA del estimador.** Mediana β=0,50 → ventana 1-2.
> p98 β=0,02 → 1-50. **Y donde `N_ruido > N_masc` la ventana no existe: entonces no se promedia, se exige
> que pasen TODAS las repeticiones.**

**Un contraste que sólo se ve al declarar las ventanas:** ppCO₂ es **media horaria** (NASA) y O₂ es
**instantáneo** (NFPA 99, porque el fuego es rápido). **Dos gases, dos ventanas opuestas, el mismo
volumen.** Y la ventana horaria tiene un agujero medido: **44 minutos fuera de banda promedian 2,93 mmHg
y no se detectan.** Toda ventana debería declarar también **el defecto más largo que puede esconder**.

---

### Fase 16 · Lo que el transporte real ya sabía (D-671 – D-672)

**Tres gremios contestaron preguntas que llevábamos meses formulando, y ninguno usa la palabra
«teletransporte».**

**Eiband (NASA Memo 5-19-59E, 1959)** · tolerancia humana con sujeción máxima:

| duración | **g máximo** |
|--:|--:|
| 0,044 s | **45** |
| 0,2 s | 25 |
| 1,6 s | **10** |

Factor **4,5 en g** sobre factor **36 en duración**: es nuestro criterio (pico, duración) **publicado 67
años antes**. Y dos frases literales que cierran más de lo que parece: *«la sujeción adecuada es la
variable primaria»* —que es nuestro propio hallazgo de 109 g sujeto frente a 3 cm suelto, sobre humanos en
vez de acero— y *«la pendiente de subida en todas las exposiciones tolerables fue de unos 500 G/s»*, que
nos dio **una tercera variable que no teníamos**.

**Ajustando sus cinco puntos:** `g ~ t^-0,461` (R² = 0,968). Eso es **energía constante** (exponente 0,5),
**no impulso** (1,0). **El daño humano es limitado por energía.** Y delata una contradicción entre dos
normas que habíamos adoptado: ASTM D3332 usa *critical velocity change*, exponente 1. **Se resuelve por
alcance: Eiband rige el ocupante, D3332 la carga inerte, y rige el menor.**

**Transfer Under Pressure (TUP)** · un buzo sube en una **campana cerrada** y se transfiere
**isobáricamente** a una cámara. **Humano completo, volumen sellado, movido de A a B, interior sin
modificar, custodia continua.** Certificado IMCA y Lloyds. **Es nuestra vía, hecha de rutina desde hace
décadas.**

**UHMS Chamber Mishap Database (1923-1998)**, mundial, sobre cámaras hiperbáricas, hipobáricas, campanas
de buceo y cápsulas espaciales: **113 incidentes, 135 muertes, 50 heridos en 75 años.**

> **Y el modo de fallo dominante es el FUEGO: 81 de 113, el 72 %.** No la fuga. No el sello. No el
> transporte. **Y nuestro marco no lo mencionaba en ninguna de sus capas.**

La frase más importante de ese documento para lo que este trabajo pretende:

> *«[los manuales NFPA de 1969 y 1970] son los principales responsables de que **nunca haya habido una
> muerte por fuego en una cámara hiperbárica clínica en los Estados Unidos**.»*

**Un estándar borró el modo de fallo dominante.** Ése es el argumento de por qué escribir este marco vale
aunque quien lo escribe no ejecute el banco.

---

### Fase 17 · Catorce baterías de ataque (D-675 – D-681)

**Por qué:** un marco completo es un marco que **ya se puede atacar**. Y las capas no son una lista: son
una **red**.

| capa | salidas | entradas | **apalanca** | papel |
|:--|--:|--:|--:|:--|
| **1 · marco teórico** | 16 | 0 | **96** | **FUENTE pura** |
| 2 · instrumento | 13 | 5 | 65 | intermedia |
| 3 · máquina · 4 · custodia | 6 | 7 | 24 | intermedias |
| 6 · humano | 1 | 7 | 4 | **colector** |
| **5 · acto** | **0** | **16** | **0** | **SUMIDERO PURO** |

> **La capa 5 es un sumidero puro: ningún cálculo sobre el acto fortalece a nadie. Por eso los 534 € del
> acto no tienen sustituto analítico.** Y la capa 6 es un **colector**: siete cosas caen sobre el humano y
> sólo una sale, de modo que los errores de aguas arriba se acumulan ahí.

**Las veintiocho baterías, 0 € en total:**

| | batería | n | hallazgo principal |
|--:|:--|--:|:--|
| 1 | sensibilidad, ruptura, triangulación, frontera, acoplamiento, control negativo, propagación, reproducibilidad | 100 | **`PCT_INV` = 98 detectaba el 10 % donde declarábamos el 90 %** |
| 2 | **retrodicción** | 15 | 14/15 bruto, **4/15 tras auditar circularidad** |
| 3 | adversario óptimo | 12 | la identidad se rompe a **n > 99** |
| 4 | casos límite | 14 | con n=2 **la mediana deja de ser robusta** |
| 5 | coherencia interna | 10 | **tres contradicciones vivas** entre nuestras propias reglas |
| 6 | **escala de cabina** | 12 | `υ ≥ L` |
| 7 | réplica por extraño | 8 | 32/33 scripts corren; **ningún punto de entrada** |
| 8 | deriva temporal | 8 | **ningún periodo de validez del certificado** |
| 9 | **mapa universal** | — | el marco vale en **3 celdas de 66** |
| 10 | **FMEA cruzado** | 16 | **cubríamos 5 de 16 modos de fallo** |
| 11 | tasa de fallo operacional | — | **«cero muertes en 37» = «≤ 1 de cada 12»** |
| 12 | cierre de contradicciones | 3 | dos cerradas, una era del registro |
| 13 | coste marginal | — | **ninguna compra aislada mueve el mínimo** |
| 14 | frontera del mapa | — | **un ensayo decide 60 celdas** |

**El defecto más grave que encontraron.** El percentil `p` con `n` unidades **tolera `(100−p)/100·n`
atípicos**. Con **p98 y n = 50 eso es exactamente 1**: una unidad desplazada se convierte en el **máximo**,
no en el p98, y el criterio no la ve.

| percentil | **P(detectar 1 de 50 a 1,0 mm)** |
|--:|--:|
| **98** *(el declarado)* | **10 %** |
| **99** | **100 %** |

**Regla: `p ≥ 100(1 − 1/(2n))`.** El percentil se **liga a n**, no se fija.

**Y la lección de la batería 2.** La predicción global, escrita **antes** de correr, decía: *«si acierta en
todas, es señal de alarma: significa que las estoy ajustando a posteriori»*. Salió **14/15 con cero
fallos**. Al auditar circularidad —*una retrodicción sólo vale si la regla precede al dato*—: **4 genuinas,
2 parciales, 5 post hoc, 2 circulares, 1 que no era test.** **La puntuación honesta era 4/15.**

Las cuatro que valen: el exponente de Eiband (calculado de sus datos, **y corrigió al marco**); la cota de
tres aplicada a Daugman (1,5·10⁻¹¹ contra su 5·10⁻¹²); **la refutación por 20 órdenes del FAR publicado de
las PUF ópticas**; y EURAMET, cuya fórmula predice `U = 0,53 µm` frente a nuestro lector de **0,52** —
coinciden al **2 %**, y sitúan nuestro lector al nivel de un instituto nacional de metrología.

---

### Fase 18 · Los once modos de fallo que faltaban (D-682)

El FMEA cruzado destapó que **cubríamos 5 de 16 modos de fallo estándar** de un recipiente a presión y un
vehículo tripulado. **El fuego no era el único tropiezo: era el primero de doce.** Los once se cerraron
por derivación, a coste cero, y dos produjeron criterios nuevos:

| modo | cierre |
|:--|:--|
| pandeo externo | `P_cr = 2E/√(3(1−ν²))·(t/R)²` → 4 bar con knockdown, **margen ×4** |
| **fatiga por ciclado** | `σ = PR/2t` = 11,9 MPa contra límite de fatiga 82 MPa: **vida infinita**. *Cada acto es un ciclo, y no los contábamos.* |
| corrosión | sobreespesor de 1,5 mm sobre la pared de cálculo |
| **fractura frágil** | **declarábamos la banda térmica del OCUPANTE y nunca la del MATERIAL.** Cierre por selección: austenítico o aluminio, sin transición dúctil-frágil |
| **fallo de unión** | **lo cierra el propio marco**: `υ ≥ L` exige conformar en UNA operación, y **una cáscara monolítica no tiene soldaduras** |
| **choque térmico** ⚠ | `σ = EαΔT/(1−ν)`: **a ΔT = 60 °C se alcanza la fluencia.** **Criterio nuevo: ΔT ≤ 50 °C entre caras, ventana instantánea** |
| soportes y anclaje | cáscara + ocupante a 45 g → **464 kN**. *Eiband vale también para la cabina, no sólo para quien va dentro* |
| pasamuros | **WRC 107, que ya citábamos, existe justo para eso.** Teníamos la referencia y no la pregunta |
| **autonomía** ⚠ | ver abajo |
| egreso | apertura desde dentro, sin herramienta, ≤ 60 s |
| evento médico | **fuera de alcance, declarado.** No es un hueco: es una exclusión explícita |

**Y el más importante de los once:**

> ## Una cabina sellada de 2 m³ con un ocupante aguanta **16 minutos**
>
> | | límite | tiempo |
> |:--|--:|--:|
> | O₂ | salir de la banda NASA 155→145 mmHg | 50 min |
> | **CO₂** | **3 mmHg (NASA OCHMO)** | **16 min** |
>
> **El CO₂ manda.** Una cabina **sellada sin depuración** sólo sirve para saltos suborbitales (3,7 min).
> Para Marte (41,6 h) hacen falta **158 veces más** de lo que aguanta sellada: **ECLSS activo, obligatorio.**
> **«Volumen cerrado» no significa «volumen sellado y basta».**

**El último ataque, y es elegante.** Quedaba una afirmación sin atacar: la identidad del ocupante por iris.
Daugman da FMR < 5·10⁻¹², pero el criterio tiene **dos caras**, y la que no habíamos mirado es la **FRR**:
que el ocupante **legítimo** sea rechazado. El iris se degrada con dilatación pupilar, y **un tránsito a
45 g produce midriasis**.

> **El propio evento que certificamos degrada el biométrico con que lo certificamos.**

Cierre: captura de referencia en las mismas condiciones (regla 415), **FRR declarada junto a la FMR con su
n** (regla 583), y modalidad alternativa si la FRR bajo midriasis no es aceptable. **Más débil y más
verdadero.**

---

### Fase 19 · El primer caso real · Nueva York → Tokio (D-683)

**Por qué:** una batería **ataca** una afirmación; un caso real las **exige todas a la vez**, con
números concretos y un destino concreto. Es un tipo de prueba distinto.

**Y encontró algo que veintiocho baterías no encontraron.**

| aceleración sostenida | viaje | CO₂ en cabina sellada | veredicto |
|:--|--:|--:|:--|
| 1 g · cómodo | 35,1 min | 15,8 min | **ECLSS obligatorio** |
| 3 g · entrenado | 20,2 min | 15,8 min | ECLSS obligatorio |
| **9 g · reclinado + traje** | **11,7 min** | 15,8 min | **LLEGA SELLADA**, 4,1 min de margen |
| 25 g · inmersión líquida | 7,0 min | 15,8 min | llega sellada |

> ## **No se puede ir CÓMODO y SELLADO a la vez.**
>
> A 1 g el viaje dura 35 minutos y el CO₂ da 16: hace falta depuración activa. A 9 g llega sellada,
> pero exige reclinado y traje anti-g. **La decisión de soporte vital y la de aceleración NO son
> independientes**, y el marco las trataba en capas separadas —custodia y ocupante—. Ninguna batería
> lo vio, **porque una batería ataca una afirmación y un caso real las exige todas simultáneamente.**

**Y una segunda distinción que el marco no tenía.** Eiband mide **impactos (< 2 s)**. Un tránsito de
minutos se rige por el límite **sostenido**: 4,5 g de pie, 9 g reclinado, 25 g en inmersión.
**Confundir los dos regímenes da 45 g donde lo correcto son 9.**

**Dos resultados limpios:**

1. **El tiempo de respiración es independiente del número de ocupantes** —15,8 minutos, de 1 a 10—
   porque el volumen escala con ellos y el CO₂ también. Se cancelan exactamente.
2. **El GATE-0 falla para todo n ≥ 1**: un solo ocupante ya exige L = 1,26 m, que da α = 0,750.
   **Ni una persona pasa hoy el filtro de admisibilidad.**

| ocupantes | volumen | lado | pared | cáscara | energía |
|--:|--:|--:|--:|--:|--:|
| 1 | 2 m³ | 1,26 m | 4,0 mm | 157 kg | 0,11 TJ |
| 3 | 6 m³ | 1,82 m | 6,0 mm | 486 kg | 0,34 TJ |
| 10 | 20 m³ | 2,71 m | 13,3 mm | 2.418 kg | 1,52 TJ |

---

## 3. El marco formal: 109 afirmaciones en ocho ejes

Una afirmación está **completa** cuando está enunciada, dimensionada, fechada con su estado evidencial,
es falsable, está costeada, lleva su ventana declarada y **ha resistido un ataque**.

| eje | | |
|:--|--:|:--|
| 1 · enunciado | **100 %** | fórmula o umbral con precisión |
| 2 · unidades | **100 %** | dimensionalmente válido |
| 3 · evidencial | **100 %** | MEDIDO / DERIVADO / LITERATURA / DECLARADO, con fuente |
| 4 · falsable | **100 %** | hay un experimento que lo refutaría |
| 5 · costeado | **100 %** | ese experimento tiene precio y plazo |
| 6 · ventana | **100 %** | ventana de promediado y condiciones declaradas |
| **7 · resistido** | **100 %** | **atacado por al menos un cálculo de las baterías** |

> **Las 35 ecuaciones del marco, con su dominio de validez, sus unidades y su estado evidencial,
> están recogidas en `docs/FORMULARIO.md`.** Lo que sigue son las centrales.

### 3.1 Las afirmaciones centrales

**Contrato.** `A = √(Ω_imp/Ω_acto)`, con `Ω = 1 − corr`. El contrato existe **si y sólo si `A > 1 + dA`**,
donde `dA/A = 0,5·√(u_imp² + u_acto²)` es la **zona muerta**: con `u = 10 %`, **`A ∈ [0,934 · 1,071] es un
EMPATE, no un contrato.** Un acto con `A = 1,05` no está certificado.

**Tasa.** El contrato se declara también como **tasa**: `FAR = P(Ω_imp ≤ Ω_acto)`, con **cota de la regla
de tres, `FAR ≤ 3/k`**, y **siempre acompañada de su `k`**. Medido: `FAR ≤ 10⁻⁶` con `k = 3·10⁶`.

**Ley.** `A = K_d·√(a/σ)`, con `K₂ = 0,632` y `K₃ = 0,597`. **La conclusión sobrevive a su propia fórmula
equivocada:** con exponente 0,4 en lugar de 0,5, `A = 3,82` y el contrato sigue en pie; haría falta
`p < 0,212` para tumbarlo.

**Los seis criterios, con su punto de ruptura y su ventana:**

| criterio | estimador | **ruptura** | ventana |
|:--|:--|--:|:--|
| 1 · disposición | mediana | **50 %** | 1-2 re-colocaciones |
| 2 · inventario | percentil `p ≥ 100(1−1/2n)` | 1/n | 1-50 |
| 3 · recuento | conteo | 1/n | 1 por acto |
| 4 · **identidad** | máximo | 1/n | 1 por acto, **válida sólo para n < 99** |
| 5 · contrato | `A > 1 + dA` **y** FAR con su n | 50 % | 1-2 |
| 6 · **identidad del ocupante** | biometría, FMR **y FRR**, con n | — | captura en condiciones declaradas |

**Riesgo del consumidor, declarado.** Tres de los seis criterios tienen ruptura del 50 %, de modo que el
sistema depende de los que no. Y la referencia externa: **la IAEA fija su alarma perdida en β = 10 %;
nosotros estábamos en el 100 % en el peor caso sin haberlo calculado.** El suelo de detección declarado
es: **se detecta al ≥ 90 % una unidad desplazada 1,0 mm**, con `σ_colocación = 141 µm`.

**GATE-0.** `PASA` si **`α ≥ 0,95` Y `D(176 mm) ≤ 35 µm`**; `VETO` si `α < 0,35` (fiable al 98,7 %);
todo lo demás es INTERMEDIO y **no basta para lanzar el acto**. Placa de **5 anillos × 5 fiduciales a
72°**, campo útil **redondo**, estimador **Theil-Sen**, y **suelo por re-colocación**, no por re-lectura.

**Envolvente del ocupante.** Presión `34,5 kPa < p ≤ 103 kPa` indefinido; **tasa de cambio ≤ 13,5 psi/min**;
ppCO₂ ≤ 3 mmHg **en media horaria**; O₂ ≤ 23,5 % **instantáneo**; registro **continuo por compartimento
aislable**; diluvio en ≤ 3 s; `ΔT ≤ 50 °C` entre caras; **ECLSS activo obligatorio por encima de 16
minutos**; aceleración según **Eiband (pico, duración, pendiente de subida)**.

---

## 4. El diagrama de fases: dónde vale este marco

Ejes: **masa de la carga (10 g – 10 t) × lado de la cabina (0,1 – 10 m)**. Cinco condiciones por celda.

```
  carga            0.1          0.3          1.0          2.0          3.0          5.0
  tornillo       ## ok        ## ok     G a=0.79     G a=0.67     G a=0.60     G a=0.53
  maleta        · 0.25m      · 0.25m     G a=0.79     G a=0.67     G a=0.60     G a=0.53
  HUMANO        · 0.67m      · 0.67m     G a=0.79     G a=0.67     G a=0.60     G a=0.53
  ELEFANTE      · 2.74m      · 2.74m      · 2.74m      · 2.74m      · 2.74m     G a=0.53

  ##  todo vale  ·  G  falla el GATE-0  ·  ·  no cabe
```

> ## **El marco vale hoy en 3 celdas de 66: un tornillo en una cabina de ≤ 30 cm.**
> **Y el cuello es siempre el mismo: el GATE-0.**

### 4.1 La ley que el mapa destapó

| cabina `L` | υ necesaria | **υ/L** |
|--:|--:|--:|
| 0,3 m | 307 mm | 1,02 |
| 3,0 m | 1.779 mm | 0,59 |
| 8,0 m | 4.077 mm | 0,51 |

**υ/L converge a ~0,6. La regla es `υ ≥ L`.**

**Y lo que significa físicamente:** la longitud de correlación de un campo de error **es del tamaño de la
operación que dio forma a la pieza**. Una fresadora de 3 ejes recorre la pieza punto a punto — υ es la
coherencia térmica del husillo, **100-500 mm**, que es exactamente el rango publicado. Un molde, una
prensa, una embutición o un hidroconformado **conforman toda la pieza a la vez** — υ es la pieza entera.

> **REQUISITO DE FABRICACIÓN: las dos cáscaras no pueden mecanizarse punto a punto. Tienen que
> conformarse en UNA sola operación que abarque la pieza entera, con el mismo utillaje — mismo molde,
> misma prensa, misma colada.**
>
> No es una preferencia: **es la condición que hace que el GATE-0 pase**, sale entera del marco sin un
> dato nuevo, **y de paso elimina el modo de fallo por soldadura.**

### 4.2 El tiempo no depende del tamaño

| cabina | tiempo | **energía** |
|:--|--:|--:|
| 0,3 m + humano | 3,7 min | 102 GJ |
| 3,0 m + humano | **3,7 min** | **1.169 GJ** |

**El tiempo lo fija el ocupante (Eiband), no la masa.** Lo que escala es la **energía, como L³**.

### 4.3 El ensayo que decide 60 celdas

| | hoy | hace falta |
|:--|--:|--:|
| HUMANO en cabina de 1 m | α = 0,792 | **υ ≥ 739 mm** |
| HUMANO en cabina de 3 m | α = 0,603 | **υ ≥ 1.779 mm** |

> **Medir `υ` sobre DOS PIEZAS YA CONFORMADAS del mismo utillaje.** No hay que fabricar nada: vale
> cualquier par salido de la misma embutición, hidroconformado, repulsado o molde. Instrumento: el mismo
> lector del GATE-0. **Un solo ensayo decide 60 celdas del mapa.**

---

# 5. EL FACTOR TIEMPO · nada es instantáneo, y el viaje casi nunca es lo que más dura

**El tiempo es un pilar del problema, no una consecuencia.** Y el marco llevaba veinticinco casos
resueltos reportando el **tiempo de vuelo** como si fuera el tiempo del **acto**. No lo son, y la
diferencia no es menor: **para una persona de Londres a Berlín, el vuelo es el 4,6 % del acto.**

## 5.1 La estructura: dos términos separables

```
              t_acto(m, d, a)  =  T(m)  +  τ(d, a)
                                  \___/     \______/
                             SOLO la masa   SOLO la ruta
```

**Ninguna magnitud aparece en los dos términos.** Eso no es una conveniencia de cálculo: es una
**propiedad del acto**, y es lo que permite tabular el problema entero con dos entradas.

**El coste fijo `T(m)`** son las operaciones que hay que hacer **estés donde estés**: medir el suelo
en origen re-colocando diez veces, preparar y sujetar la carga, subir la presión a ≤ 13,5 psi/min,
**volver a medir el suelo en destino** y verificar los seis criterios. **Depende sólo de la masa**,
porque lo que manda es el régimen de manipulación.

**El coste de ruta `τ(d, a)`** es el vuelo, y depende sólo de la distancia y de la aceleración que
el ocupante tolere.

> **Y de ahí sale lo que más cuesta aceptar del marco: cuanto MÁS CERCA está el destino, MENOR
> fracción del acto es el viaje.** A un kilómetro, volar es el **0-1 %** del tiempo. El resto es
> certificar que lo que llegó es lo que salió.
>
> **No existe el teletransporte instantáneo, y no por la física del vuelo: por la del certificado.**

## 5.2 Las tres fórmulas del tiempo

### 36 · Separabilidad del acto
```
t_acto(m,d,a) = T(m) + τ(d,a)

T(m)   = 2·N_suelo·t_manejo(M_total) + t_prep + t_verif      [min]   SOLO masa
τ(d,a) = 2 √( d / (a·g) )                                    [min]   SOLO ruta
```
`N_suelo` = 10 re-colocaciones **por estación**. `t_manejo` es **discreto**, porque el equipo de
manipulación lo es: **a mano < 25 kg = 0,5 min · polipasto < 1 t = 3 min · grúa < 20 t = 8 min ·
grúa pesada > 20 t = 15 min**. **DEC** (declarado; es el término que más conviene medir).

### 37 · Distancia de cruce
```
d* = a·g·( T(m) / 2 )²
```
Por debajo de `d*` **el viaje es lo de menos**; por encima, el vuelo domina. **DER.**

### 38 · Fracción de vuelo
```
f_vuelo = τ / (T + τ) = 1 / (1 + T/τ)
```
**DER.**

## 5.3 La tabla · masa × distancia

**Tiempo total del acto a 9 g sostenidos.** Entre paréntesis, el porcentaje que es **vuelo**.

| carga | **T(m)** | 1 km | 100 km | Berlín 930 | Tokio 10.850 | Sídney 17.000 | Luna 384.400 | Marte 55·10⁶ |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|
| **1 g** | 14,7 m | 14,8 m (1 %) | 15,8 m (7 %) | 18,1 m (19 %) | 26,4 m (44 %) | 29,3 m (50 %) | 84,3 m (83 %) | 14,1 h (98 %) |
| 5 g | 14,7 m | 14,8 m (1 %) | 15,8 m (7 %) | 18,1 m (19 %) | 26,4 m (44 %) | 29,3 m (50 %) | 84,3 m (83 %) | 14,1 h (98 %) |
| 10 g | 14,7 m | 14,8 m (1 %) | 15,8 m (7 %) | 18,1 m (19 %) | 26,4 m (44 %) | 29,3 m (50 %) | 84,3 m (83 %) | 14,1 h (98 %) |
| 50 g | 14,7 m | 14,8 m (1 %) | 15,8 m (7 %) | 18,1 m (19 %) | 26,4 m (44 %) | 29,3 m (50 %) | 84,3 m (83 %) | 14,1 h (98 %) |
| 100 g | 14,7 m | 14,8 m (1 %) | 15,8 m (7 %) | 18,1 m (19 %) | 26,4 m (44 %) | 29,3 m (50 %) | 84,3 m (83 %) | 14,1 h (98 %) |
| 500 g | 14,7 m | 14,8 m (1 %) | 15,8 m (7 %) | 18,1 m (19 %) | 26,4 m (44 %) | 29,3 m (50 %) | 84,3 m (83 %) | 14,1 h (98 %) |
| 1 kg | 14,7 m | 14,8 m (1 %) | 15,8 m (7 %) | 18,1 m (19 %) | 26,4 m (44 %) | 29,3 m (50 %) | 84,3 m (83 %) | 14,1 h (98 %) |
| 2 kg | 14,7 m | 14,8 m (1 %) | 15,8 m (7 %) | 18,1 m (19 %) | 26,4 m (44 %) | 29,3 m (50 %) | 84,3 m (83 %) | 14,1 h (98 %) |
| **5 kg** | **14,7 m** | 14,8 m (1 %) | 15,8 m (7 %) | 18,1 m (19 %) | 26,4 m (44 %) | 29,3 m (50 %) | 84,3 m (83 %) | 14,1 h (98 %) |
| **10 kg** | **67,2 m** | 67,3 m (0 %) | 68,3 m (2 %) | 70,6 m (5 %) | 78,9 m (15 %) | 81,8 m (18 %) | 2,3 h (51 %) | 15,0 h (93 %) |
| 25 kg | 67,2 m | 67,3 m (0 %) | 68,3 m (2 %) | 70,6 m (5 %) | 78,9 m (15 %) | 81,8 m (18 %) | 2,3 h (51 %) | 15,0 h (93 %) |
| **75 kg · persona** | **71,2 m** | 71,3 m (0 %) | 72,3 m (2 %) | **74,6 m (5 %)** | 82,9 m (14 %) | 85,8 m (17 %) | **2,3 h (49 %)** | **15,1 h (92 %)** |
| 100 kg | 67,2 m | 67,3 m (0 %) | 68,3 m (2 %) | 70,6 m (5 %) | 78,9 m (15 %) | 81,8 m (18 %) | 2,3 h (51 %) | 15,0 h (93 %) |
| **500 kg** | **2,9 h** | 2,9 h (0 %) | 2,9 h (1 %) | 2,9 h (2 %) | 3,1 h (6 %) | 3,1 h (8 %) | 4,0 h (29 %) | 16,7 h (83 %) |
| 1 t | 2,9 h | 2,9 h (0 %) | 2,9 h (1 %) | 2,9 h (2 %) | 3,1 h (6 %) | 3,1 h (8 %) | 4,0 h (29 %) | 16,7 h (83 %) |
| **5 t · elefante** | **2,9 h** | 2,9 h (0 %) | 2,9 h (1 %) | 2,9 h (2 %) | 3,1 h (6 %) | 3,1 h (8 %) | 4,0 h (29 %) | 16,7 h (83 %) |
| **20 t** | **5,3 h** | 5,3 h (0 %) | 5,3 h (0 %) | 5,4 h (1 %) | 5,5 h (4 %) | 5,6 h (4 %) | 6,5 h (18 %) | 19,2 h (72 %) |
| 50 t | 5,3 h | 5,3 h (0 %) | 5,3 h (0 %) | 5,4 h (1 %) | 5,5 h (4 %) | 5,6 h (4 %) | 6,5 h (18 %) | 19,2 h (72 %) |
| **100 t** | **5,3 h** | 5,3 h (0 %) | 5,3 h (0 %) | 5,4 h (1 %) | 5,5 h (4 %) | 5,6 h (4 %) | 6,5 h (18 %) | 19,2 h (72 %) |

### Cómo se lee esta tabla

**1 · El tiempo está CUANTIZADO por el régimen de manipulación, no por la masa.**

> **Un gramo y cinco kilos tardan exactamente lo mismo: 14,7 minutos de coste fijo.**
> **Medio tonelada y un elefante de cinco toneladas también: 2,9 horas.**
> **Veinte toneladas y cien toneladas también: 5,3 horas.**
>
> El acto no distingue masas: distingue **si hace falta una mano, un polipasto, una grúa o una grúa
> pesada.** Multiplicar la carga por cinco mil no cambia nada; cruzar un umbral de manipulación lo
> cambia todo. **El salto de 5 kg a 10 kg cuadruplica el acto** (14,7 → 67,2 min), y es el salto más
> caro de toda la tabla.

**2 · Cuanto más cerca, más manda el certificado.** A 1 km el vuelo es el 0-1 %. A Marte, el 98 %.
**La intuición de que «teletransportar al lado de casa es instantáneo» es exactamente al revés.**

**3 · El elefante no es más lento que media tonelada.** Ambos 2,9 h. Lo que le impide viajar no es el
tiempo: es el **GATE-0** (α = 0,561) y la **energía**.

**4 · Cien toneladas a Berlín: 5,4 horas, de las cuales 3,4 minutos son vuelo.**

## 5.4 La distancia de cruce es una escalera

| carga | masa **total** | régimen | `T(m)` | **`d*` de cruce** |
|:--|--:|:--|--:|--:|
| 1 g – 5 kg | 1 – 17 kg | a mano | 14,7 m | **17.204 km** |
| 10 kg – 100 kg | 28 – 185 kg | polipasto | 67,2 m | **358.983 km** |
| 500 kg – 5 t | 1,0 – 21,5 t | grúa | 2,9 h | **2.356.629 km** |
| 20 t – 100 t | 50 – 216 t | grúa pesada | 5,3 h | **7.780.000 km** |

> **La Luna está a 384.400 km. La distancia de cruce de una persona es 358.983 km.**
>
> **La Luna cae, casi exactamente, donde el viaje empieza a costar más que certificarlo.**

*(Nota de honestidad: este número es sensible al modelo de manipulación al nivel del 10 % — con el
modelo de D-685 salía 403.000 km. La conclusión aguanta en los dos casos porque la Luna está dentro
de ese margen, pero **el término `t_manejo` es el que más conviene medir**, y por eso está marcado
**DEC** y no DER.)*

## 5.5 Lo que esta sección cierra

> **Nada es instantáneo. El tiempo de un teletransporte no lo fija el destino: lo fijan la masa y
> el certificado, y el destino sólo añade un término que, por debajo de la Luna, es minoritario.**
>
> Un acto es **rápido** cuando la carga cabe en una mano y el destino está lejos.
> Es **lento** cuando hace falta una grúa, **aunque el destino esté a un kilómetro**.

---

# 5-bis. EL PIPELINE · los 24 estados del acto, y la rama que nadie había escrito

Todo lo anterior describe **qué** se certifica. Esta sección describe **cómo se ejecuta**:
la secuencia completa desde que se enciende la cabina A hasta que el sujeto sale por la
cabina B. Se escribe como máquina de estados porque así es como habría que programarla.

## 5-bis.1 Los 24 estados

| | estado | reloj | qué ocurre | verificación |
|:--|:--|--:|:--|:--|
| S0 | ALMACENADA | — | sin energía, en la sala a ±1 K | soak = 0 al arrancar |
| S1 | ARRANQUE | T−35 | se enciende la cabina | autotest de los 13 instrumentos |
| S2 | VERIF. FUNCIONAL | T−33 | báscula, O₂ y registrador contra patrón | se firma el parte; su hash va al mensaje |
| S3 | RESERVA | T−32 | A propone, **B reserva o rechaza** | fase 1 del compromiso en dos fases |
| S4 | PESAJE | T−30 | el ocupante, vestido y con equipaje | contra la masa máxima de la cabina |
| S5 | BIOMETRÍA REF. | T−28 | captura de referencia del iris | sin ella no hay contra qué comparar |
| S6 | INSPECCIÓN | T−25 | visual del interior + declaración firmada | contra el polizón |
| S7 | EMBARQUE | T−20 | entra, se sujeta, **se cierra la puerta** | par de cierre registrado |
| S8 | **SELLADO** | T−15 | compromiso SHA-256 + sello de tiempo, **dos firmas** | ciego + cuatro ojos |
| S9 | SUELO A | T−0 | 10 re-colocaciones, o *k* = 3 puntos si se hereda | carta de Shewhart |
| S10 | LECTURA A | T+12 | 25 fiduciales + 50 diámetros | R² ≥ 0,98 |
| S11 | FIRMA Y ENVÍO | T+14 | mensaje de 1.806 B, firmado Ed25519 | B verifica antes de tocar nada |
| S12 | PRESURIZACIÓN | T+16 | rampa ≤ 13,5 psi/min | **arranca el reloj de CO₂: 15,8 min** |
| S13 | **COMMIT** | T+18 | B ya no puede negarse | retorno posible hasta el 30 % de ruta |
| S14 | TRÁNSITO | T+18 | 3,4 min a 9 g | **mitigación nula** |
| S15 | LLEGADA | T+21 | frenado, reposo respecto al suelo de destino | |
| S16 | VENTILACIÓN B | T+22 | se abre | 10 de los 15,8 min de CO₂ usados |
| S17 | SUELO B | T+22 | heredado, o 10 re-colocaciones si es el primero | |
| S18 | LECTURA B | T+34 | los seis criterios + FAR con su *k* | |
| S19 | CONCILIACIÓN | T+36 | cotejo del registro de A contra el de B | |
| S20 | APERTURA CIEGO | T+38 | **el sistema** abre con la semilla sellada | ningún humano decide |
| S21 | BIOMETRÍA SALIDA | T+39 | iris contra la referencia de S5 | FRR declarada |
| S22 | DESEMBARQUE | T+40 | **el ocupante sale** | |
| S23 | CIERRE | T+42 | se archiva y se actualiza el saldo de cabinas | |

**77 minutos de máquina encendida** para 3,4 de vuelo.

## 5-bis.2 Lo que el pipeline encontró

Escribirlo cambió tres cosas del marco.

**Primera: 9 de 17 ramas de aborto no tenían destino.** El marco había sido atacado seis
veces sobre los pasos físicos y **ni una sobre el flujo de control**. Las nueve ramas
huérfanas caen todas después del sellado —es decir, **con una persona dentro**—, mientras
que las ocho anteriores vuelven a S0 y son triviales. El sellado no era sólo el punto sin
retorno administrativo: era la frontera entre dos regímenes de aborto distintos.

**Segunda: la batería no cerraba.** Se había dimensionado sobre el acto (3,4 min) y el
pipeline dura veinte veces más: 105 W × 77 min = **135 Wh contra 124 de batería**. La
salida no es más batería —es que la cabina va con **cordón umbilical** mientras está en
estación, y la batería sólo cubre S12→S16: 7,4 min, 13 Wh, 9,6× de margen. Eso obliga a un
**pasamuros de potencia desconectable en caliente** que la enumeración de pasamuros no contó.

**Tercera, y la que importa: LA PUERTA NUNCA ES EL CASTIGO.**

- **Antes del commit hay *rollback*.** El acto no existió, la persona sale por donde entró.
  La lectura A gana un **límite duro de tres reintentos** —sin límite era un bucle con un
  ocupante dentro— y el aborto por presión baja **con la misma pendiente** con que subió.
- **Después del commit no hay *rollback*.** La entrega se cumple siempre; lo único que
  puede fallar es el certificado. Los cinco fallos de S15 a S21 se resuelven **todos igual,
  abriendo**: llegada fuera de tolerancia abre y no certifica; conciliación que no cuadra
  abre y deja el acto **en disputa**; semilla del ciego que no descifra abre y deja el acto
  **nulo** —no contamina la tasa—; biometría de salida fallida abre y acredita a mano,
  porque encerrar a alguien por una FRR de 10⁻³ es inaceptable.

El marco tenía seis criterios para denegar un certificado y **ninguno** para denegar una
apertura, porque denegar una apertura no es una opción del sistema. Era cierto, y por eso
nadie lo había escrito. **Lo implícito no se puede auditar.**

# 5-ter. LO QUE EL MARCO APRENDIÓ DESPUÉS DEL PIPELINE (D-688 a D-717)

## 5-ter.1 La aceleración era una decisión, y era la equivocada

El marco declaró 9 g durante cientos de decisiones sin que nadie preguntara por qué. Al
cotejar una tabla de tiempos reales apareció que `E = m·a·d` es **lineal en la
aceleración**: bajar a 1 g multiplica el tránsito por 3 y **divide la energía por 9**.

Y el tránsito no importa. El acto es **97 % trámite**: Londres-Berlín pasa de 3 a 10
minutos de vuelo y de 2,0 a 2,1 horas puerta a puerta. A cambio, a 1 g desaparecen el
criterio del cuello —un bebé lleva el 25 % de su masa en la cabeza y un adulto el 7 %—,
la aspiración por vómito, el traje anti-g, el reclinado, los objetos sueltos como
proyectiles y casi toda la lista de aptitud médica. **Siete de los trece huecos del
ocupante no venían del acto: venían de la aceleración.** El alcance de la fórmula 28
sube además de 1.421 a 12.786 km, porque `v = √(a·d)`.

**Declarado: 1 g.**

## 5-ter.2 La contradicción que llevaba 715 decisiones oculta

El marco pedía `D(176 mm) ≤ 35 µm` de forma y mandaba la cáscara a 8-9 km/s a través de
la atmósfera. **Nunca se calculó el calentamiento.** A 1.200 K la dilatación de 176 mm de
acero es 2.534 µm: **72 veces el presupuesto**. Y los dos remedios estándar lo empeoran —
un escudo ablativo se consume **cambiando de forma**, y uno de losetas añade juntas que
matan `υ ≥ L` y tumban el GATE-0.

Se resolvió sin material, por dos observaciones:

1. **El criterio no es ΔT: es la deformación PERMANENTE.** La dilatación térmica es
   reversible y el suelo de destino se establece *después* del enfriamiento, así que lo
   único que rompe el suelo es la fluencia. Para el acero eso es **T ≤ 450 °C**, no 35 µm.
2. **Velocidad y densidad nunca pueden ser altas a la vez.** El equilibrio radiativo a
   450 °C da un techo de 12,4 kW/m², y con Sutton-Graves eso fija una velocidad máxima por
   altura: 0,42 km/s a nivel del mar, 3,08 a 85 km, 4,80 a 100 km.

Los 3,0 km/s que pide Londres-Berlín a 1 g exigen estar por encima de **85 km**. El precio
son **4,4 minutos** de ascenso y descenso. **Todo acto es exo-atmosférico**, y el perfil se
diseña con techo de flujo, no de velocidad. Es la gestión de max-Q de cualquier lanzador:
un problema resuelto que no habíamos mirado.

## 5-ter.3 El pipeline, las potestades y la puerta

El acto se escribió como máquina de **24 estados**, y al hacerlo aparecieron **9 de 17
ramas de aborto sin destino**, todas posteriores al sellado. El sellado resultó ser la
frontera entre dos regímenes: antes hay *rollback* y el acto no existió; después **no lo
hay**, y de ahí sale el principio que ordena todo el diseño operativo:

> **LA PUERTA NUNCA ES EL CASTIGO.** Tras el commit la entrega se cumple siempre, y lo
> único que puede fallar es el certificado.

El marco tenía seis criterios para denegar un certificado y **ninguno** para denegar una
apertura, porque denegar una apertura no es una opción del sistema. Era cierto, y por eso
nadie lo había escrito. **Lo implícito no se puede auditar.**

Las potestades quedaron separadas: **A construye el acto, B lo juzga.** B confirma dos
veces —reserva y firma— y en el commit **renuncia al voto**. El ocupante resultó ser el
**tercer voto**: veto propio hasta el commit, ninguno después. A y B deben ser operadores
**independientes**, o los cuatro ojos no valen nada.

## 5-ter.4 Los límites duros que aparecieron al costear

- **La burbuja no pasa de ~5,0 m** (4-6 asientos). Con α = 1 el desacuerdo del campo crece
  linealmente y el suelo de detección no: se cruzan ahí. No importa, porque `E ∝ L³ ∝ N`
  hace **la energía por persona plana** y no hay economía de escala que perder al repartir.
- **Las estaciones pueden diferir**: la dimensión no entra en ninguna fórmula del contrato
  y el suelo de B admite hasta **7,8×** el de A. La asimetría de ruta **se paga en tiempo,
  no en g**.
- **Cadencia real 8,2 actos/día**, no 18,7: nadie había contado quién limpia la cabina.
- **Tarifa 1.073 €/acto a 1 g**, con energía (40 %), utillaje amortizado, retornos en vacío
  (+44 % si el tráfico es 50 % desigual) y rotación. Los 417 € publicados antes
  correspondían, al despejarlos, a **1,6 g**: no era un error aritmético sino dos
  decisiones incoherentes.
- **Fatiga: no es el límite.** Retirada a 50.000 ciclos (8,4 años), inspección cada 5.000
  (10 meses), acotada por el ciclo de 6 meses ya declarado.

## 5-ter.5 Las dos ventajas que nadie había escrito, y la barrera que nadie había visto

**La dosis de radiación escala con el tiempo, y el acto es 50-100× más rápido.** Un
Hohmann a Marte son 468 mSv —el 78 % del límite de carrera de un astronauta, en un viaje—
contra **6,3 mSv** del acto. Es la única magnitud del marco donde la prisa **regala**
seguridad. Y el perfil acelera continuamente, así que **no hay microgravedad**: gravedad
artificial gratis durante todo el trayecto.

La barrera es otra, y es económica. La prima del seguro no necesita una tasa medida:
necesita una **cota**, y la da la misma regla de tres que el marco usa para el FAR. Con los
37 actos de referencia, `P ≤ 3/37 = 8,1 %`, y contra un valor estadístico de vida de 4 M€
la prima mínima es **324.000 € por acto: 302 veces la tarifa**.

> **El marco es hoy inasegurable, y no por peligroso sino por ignorado.** Para que la prima
> baje al 10 % de la tarifa hacen falta **~112.000 actos sin una sola pérdida**. Es,
> probablemente, la barrera más dura del programa entero — y sólo se derriba operando.

# 5-quater. EL ACTO COMO SERVICIO (D-718 a D-720)

## 5-quater.1 Quién lo opera

El marco fija la plantilla sin haberlo contado nunca junto: los cuatro ojos exigen **dos
firmantes por estación**, y no dos cualesquiera — **un metrólogo**, que firma la
verificación funcional de los trece instrumentos y juzga R², α y el suelo, y **un
responsable de operación**, que firma pesaje, inspección, embarque, sellado y commit.

**Cuatro personas por acto, dos por estación.** No se puede bajar a tres: quitar uno rompe
los cuatro ojos, y *A construye / B juzga* prohíbe que la misma persona cubra ambas
estaciones aunque estuviera sola. Ni una más tampoco: **no hay piloto** —nadie vuela la
cápsula—, no hay tripulación de cabina, y **no hay operador de ciego**, porque lo abre el
sistema. El médico no va por acto: la aptitud se certifica por **ventana de validez**, como
el certificado médico aeronáutico.

De los 24 estados del pipeline, **sólo cuatro admiten decisión humana**: la reserva, el
sellado, la verificación de firma y el commit. Todo lo demás es máquina, procedimiento, o
**está prohibido decidirlo**.

> **El panel no se pilota: se atestigua.** Un Falcon 9 lleva 20-30 personas en sala de
> control porque hay decisiones en vuelo. Aquí no las hay: L4 no tiene controlador.
> **El peor defecto de seguridad del marco es su mayor ventaja de plantilla.**

El mantenimiento no es un equipo: la limpieza y la inspección entre actos las hace el turno
que opera, lo periódico es un contrato externo de ~194 h/año —que conviene externo por la
misma razón por la que los firmantes son independientes— y lo propio es media jornada para
software, registro sellado y claves. **0,4 FTE.**

Pero **la plantilla la fija la cobertura del turno, no el acto**: dos puestos × 5.840 h/año
son **14,2 FTE** por par de estaciones. **El acto necesita 4 personas; el servicio necesita 15.**

## 5-quater.2 El precio, y las tres escalas que lo ordenan

Tarifa reconstruida: **1.202 €/acto a 1 g** (energía 362 + ascenso 66 + retorno en vacío
190 + utillaje 342 + estación 23 + personal 220). Lo que ordena todo es qué bloque escala
con qué: **energía, ascenso y retorno (618 €) van con la masa** y no se diluyen; **el
utillaje (342 €) con el área** de la cáscara; **estación y personal (243 €) son por acto**
y se dividen enteros entre los ocupantes.

| asientos | L cabina | **precio/persona** | | g | tránsito | **precio** |
|--:|--:|--:|--|--:|--:|--:|
| 1 | 3,00 m | **1.203 €** | | 0,50 | 14,5 m | 927 € |
| 2 | 3,78 m | 1.011 € | | **1,00** | 10,3 m | **1.203 €** |
| 4 | 4,76 m | **894 €** | | 2,00 | 7,3 m | 1.908 € |
| 6 | 5,45 m ⚠ | 847 € | | 9,00 | 3,4 m | 6.353 € |

**No existe precio por persona por debajo de 618 €: es la energía.** El techo de 5,03 m
corta en 4-6 asientos, justo donde la curva deja de bajar deprisa. Y cada g multiplica el
precio casi linealmente — pero bajar tiene un suelo nuevo: el tramo sellado son 6 min más
el tránsito, y el presupuesto de CO₂ sin soporte activo es 15,8 min, luego **a ≥ 1,10 g
sin ECLSS**. Con ECLSS el suelo lo pone la cadencia de sala.

**1 g sigue siendo el punto correcto:** el único valor donde el ocupante no necesita nada.

## 5-quater.3 Dónde el marco deja de ir último

| carga útil | **€/kg útil** |
|--:|--:|
| 10 kg | 114 |
| 90 kg | 13 |
| **146 kg** (máx. cabina de 3 m) | **8** |
| 600 kg | 3 |

**La cáscara pesa 888 kg y el pasajero 90: el 91 % de la energía mueve el envase.** Por eso
el €/kg se desploma al llenar la cabina. Y contra la carga aérea express (3-6 €/kg)
**estamos a 2-3×, frente a 5-8× en pasaje**.

> **El acto es mejor negocio moviendo cosas que moviendo gente**, porque las cosas no
> necesitan los 584 € fijos de sala, ni certificado médico, ni consentimiento, ni reloj de
> CO₂. Es el único mercado donde el marco no va último — y lo encuentra renunciando a lo
> que le daba nombre.

Por distancia, precio y avión crecen ambos lineales en `d`, el avión desde más abajo: la
ratio se queda en 5-10× **y no mejora nunca**. Lo que sí cambia es el tiempo: a Sídney,
25,5 h contra 2,6. **Se vende tiempo, no precio.**

## 5-quater.4 La barrera que ningún cálculo derriba

La prima del seguro no necesita una tasa medida: necesita una **cota**, y la da la misma
regla de tres que el marco usa para el FAR. Con los 37 actos de referencia, `P ≤ 3/37 =
8,1 %`, y contra un valor estadístico de vida de 4 M€ la prima mínima es **324.000 € por
acto: 270 veces la tarifa**.

> **El marco es hoy inasegurable, y no por peligroso sino por ignorado.** Para que la prima
> baje al 10 % de la tarifa hacen falta **~112.000 actos sin una sola pérdida**. Mientras
> eso no ocurra, todo precio de servicio es una ficción contable: el número real de hoy es
> *no vendible a ningún precio*.

**Es la barrera más dura del programa, y sólo se derriba operando.**

## 5-quater.5 El estado del marco, y el octavo eje

Cerrados los siete huecos que quedaban —con 415 € de ensayos de mesa y sala, y tres
correcciones salidas de los ataques: los limbos se solapan y su suma es una **cota
superior**, el SLA es **por clase de ruta** y la independencia es **de los firmantes, no de
las empresas**— los siete ejes de completitud llegaron al 100 %.

Y eso obligó a añadir un octavo. Un instrumento que marca 100 % en todo **ha dejado de
discriminar**, y las notas las pone quien hace el trabajo: **un 100 % autoevaluado vale
menos que un 98,7 % con huecos nombrados.** Los siete ejes preguntan «¿está bien
planteado?». Ninguno preguntaba «¿está medido?».

| eje | |
|:--|--:|
| 1 enunciado · 2 unidades · 3 evidencial · 4 falsable · 5 costeado · 6 ventana · 7 **RESISTIDO** | **100 %** |
| **8 · MEDIDO** — existe una medida de banco, no una derivación ni una cita | **0 %** |
| **MARCO** | **87,5 %** |

**El marco está al 87,5 %, y los 12,5 que faltan son un solo eje que cuesta 1.674 €**
(1.259 de banco metrológico + 415 de cierre). Los siete ejes al 100 % dicen que el marco
está **completamente planteado, dimensionado, costeado y resistido** — que era la meta: que
otros puedan probarlo. **El octavo dice que nadie lo ha probado todavía, empezando por
nosotros.**

## 6. Lo que está medido y lo que no

El programa reporta **dos números, y los dos son verdad**:

```
PLANTEAMIENTO (7 ejes, 109 afirmaciones) ....... 100 %   "¿está todo enunciado y falsable?"
MEDIDO (el octavo eje) ..........................   0 %   "¿lo hemos tocado?"
MARCO (los ocho ejes juntos) .................... 87,5 %
```

**Dar una sola de las dos sería engañar, en cualquiera de las dos direcciones.**

La validación es 0 % porque tres condiciones preguntan **«¿lo hemos medido NOSOTROS, con materia?»**, y
ningún paper las mueve. Son **1.674 €**:

| | ensayo | coste | qué contesta |
|:--|:--|--:|:--|
| **A** | **GATE-0** · `α` + `C` + lector, con placa de anillos y suelo por re-colocación | **25 €** | *¿puede existir la máquina?* |
| **B** | **B1-B4** · testigo bajo ciclado, **fraude por sustitución de masa**, traslado con registrador, micro-vulneración de 0,5 mm | **100 €** | *¿podemos custodiar entre A y B?* |
| **C** | **el acto completo** sobre 50 unidades, dos estaciones, bajo ciego sellado | **534 €** | ***¿lo hemos hecho?*** |

**Ninguna compra aislada mueve el mínimo:** `min(0,0,0)` sigue siendo 0 si se compra una sola. **Los 1.674 €
son un paquete, no tres decisiones.** El orden correcto es A → B → C, porque **GATE-0 es un veto fiable al
98,7 % por 25 €**, y porque **es el único ensayo que mide `υ`, la pared que bloquea 60 de 66 celdas**.

### 6.1 Reproducibilidad: qué falta para que otro laboratorio lo corra

| | |
|:--|:--|
| el software | **SÍ** — 32/33 scripts corren de cero, semillas declaradas, banco regenerable |
| el suelo de 141 µm | **NO** — es *dato* de nuestro banco, no método. Debe medirse localmente |
| punto de entrada | **NO EXISTE** — 40.329 líneas de registro y ningún README |
| el marco como documento | **este documento lo es, por primera vez** |

### 6.2 Criterios de falsación

El marco se considera **refutado** si se observa cualquiera de estos resultados:

1. Un acto con `ψ = 1` (nada material viaja) y `A > 1 + dA`. *Refuta la exclusión.*
2. Un campo de desacuerdo con `α < 0,35` que produzca un acto válido. *Refuta el VETO.*
3. Un control negativo —permutación, desplazamiento, sustracción, adición, sustitución de masa— que
   **pase los seis criterios**. *Refuta el instrumento.*
4. Dos cáscaras conformadas en una sola operación con el mismo utillaje cuya `υ` medida sea **< L**.
   *Refuta el requisito de fabricación y cierra el mapa definitivamente.*
5. Un `FAR` observado por encima de la cota `3/k` declarada. *Refuta el contrato como tasa.*

---

## 7. Conclusiones

1. **El problema no era mover: era certificar.** Mover un volumen cerrado entre dos sitios es rutina
   industrial —lo hace el buceo de saturación todos los días—. Lo que no existía era el aparato métrico
   para **afirmar, con riesgo declarado, que lo que llegó es lo que salió**.

2. **La identidad es lo que separa un acto de una fabricación equivalente**, y sólo existe con `φ = 1`.
   Sin ella, la disposición geométrica aprueba una permutación.

3. **Instantáneo y certificado se excluyen**, y con margen: `ψ = 1` ocurre en `A = 0,786 < 1`. Nuestro
   acto es **9.713 veces más material que informacional**.

4. **La escala de cabina entra en el contrato, no sólo en la ingeniería.** `Ω ∝ 1/L` la facilita y `α`
   la dificulta, y del cruce sale **`υ ≥ L`**: un requisito de fabricación —conformado monolítico en una
   operación— que ninguna capa contenía por separado.

5. **El transporte real ya había contestado varias de nuestras preguntas**, fuera de toda etiqueta:
   Eiband en 1959, el BIPM desde 1889, Daugman sobre 2·10¹¹ comparaciones, el buceo de saturación,
   Johnston sobre 79 sellos. **La lección de método: nombra el gremio y usa su término, no el tuyo.**

6. **Aprender bajó el número ocho veces.** El marco pasó de 100 % a 96,8 %, a 86,7 %, a 62,3 % y de nuevo
   a 100 %, cada caída por un agujero que existía desde el principio y por fin estaba escrito. **Si una
   batería de pruebas no baja la nota, probablemente no ha atacado nada.**

7. **El marco está planteado y no está verificado.** Son 1.674 €. La especificación está abierta.

---

## 8. Referencias

**Metrología dimensional y separación de errores**
* Evans, C. J., Hocken, R. J. & Estler, W. T. (1996). *Self-Calibration: Reversal, Redundancy, Error Separation, and «Absolute Testing»*. **CIRP Annals 45**(2), 617-634.
* Keller, F. & Stein, M. (2023). *A reduced self-calibrating method for rotary table error motions*. **Meas. Sci. Technol. 34**, 065015.
* Günther et al. (2016). *Self-Calibration Method for a Ball Plate Artefact on a CMM*. **CIRP Annals 65**.
* EURAMET, *Key Comparison CMM 2-D Artifact: Ball Plate* (placa de 25 esferas; `U = √(0,5² + (L·10⁻⁶)²)` µm, k=2).
* Andreas, B., Fujii, K., Kuramoto, N. & Mana, G. (2012). *The uncertainty of the phase-correction in sphere-diameter measurements*. **Metrologia 49**, 479. Corrección 0,609(139) nm.
* Wichman, Hopper & Mershon. *WRC Bulletin 107: Local Stresses in Spherical and Cylindrical Shells Due to External Loadings* (basado en Bijlaard).

**Masa, patrones y custodia de artefactos irreemplazables**
* BIPM (2015-2016). *Calibration campaign against the international prototype of the kilogram*, partes I y II. **Metrologia 52**(2) 310 y **53**(5) 1204. Prototipo nº 70: **5 µg/kg** en transporte; deriva de patrones de trabajo **−4 µg (2003) → −35 µg (2013)**.

**Identificación y no clonabilidad**
* Daugman, J. (2006). *Probing the Uniqueness and Randomness of IrisCodes: Results From 200 Billion Iris Pair Comparisons*. **Proc. IEEE 94**(11), 1927-1935.
* Ahlswede, R. & Dueck, G. *Identification via channels* — la capacidad de identificación iguala a la de Shannon; los códigos crecen doblemente exponenciales.
* Hanley, J. A. & Lippman-Hand, A. (1983). *If nothing goes wrong, is everything all right?* — la regla de tres.

**Custodia, sellos y fallo de volúmenes cerrados**
* Johnston, R. G., Garcia, A. R. E. & Grace, W. K. (1995). *Vulnerability assessment of passive tamper-indicating seals*. **JNMM 23**(4), 24-29. **79 sellos, todos derrotados.**
* Risberg, J., van Ooij, P-J. & Eftedal, O. (2023). *Decompression procedures for transfer under pressure («TUP») diving*. **Diving and Hyperbaric Medicine 53**(3), 189-202.
* IMCA D 024, *DESIGN for saturation (bell) diving systems*.
* UHMS, *Chamber Experience and Mishap Database Report, 1923-1998*. **113 incidentes, 135 muertes, 81 incendios.**
* NFPA 99, capítulo 14, *Hyperbaric Facilities*. O₂ ≤ 23,5 % con alarma; diluvio en ≤ 3 s.

**Envolvente humana**
* Eiband, A. M. (1959). *Human Tolerance to Rapidly Applied Accelerations: A Summary of the Literature*. **NASA Memo 5-19-59E**.
* NASA, *OCHMO-TB-002, ECLSS* y **NASA-STD-3001**. Registro continuo por compartimento aislable; media horaria de ppCO₂; 13,5 psi/min.
* ASTM D3332, *Standard Test Methods for Mechanical-Shock Fragility*. ISTA *Data Collection Standards*: ≥ 2.000 muestras/s/canal, 0,5-500 Hz.

**Estructuras**
* Maxwell, J. C. (1864). *On the calculation of the equilibrium and stiffness of frames* — el conteo `3n − 6`.
* ASME *Boiler and Pressure Vessel Code*, secciones aplicables a pandeo externo y fatiga.

---

# ANEXO A · FORMULARIO COMPLETO DEL MARCO

**Las 35 ecuaciones del marco, en un solo sitio.** Cada una con su **dominio de validez**, sus
**unidades** y su **estado evidencial**, para que un científico o un desarrollador pueda tomar todo
lo necesario de este único documento sin tener que reconstruir nada.

> **Una fórmula sin dominio declarado no es sólida: es una fórmula con suerte.**
> Ése es el motivo de que cada entrada lleve el rango en el que se ha comprobado y la fuente de la
> que viene. Una ecuación correcta aplicada fuera de su dominio produce un número, y ese número
> parece tan válido como cualquier otro.

**Leyenda del estado evidencial:**

| | |
|:--|:--|
| **MED** | medido — por nosotros o por un laboratorio identificado, con su `n` |
| **DER** | derivado — se sigue de otras ecuaciones del marco o de física estándar |
| **LIT** | literatura — publicado por un tercero identificado y verificado por nosotros |
| **DEC** | declarado — elegido por el programa, sin medida que lo respalde todavía |

Las entradas marcadas con **⚠** son las que **cambiaron el marco al aparecer**, y conviene leerlas
antes que ninguna otra.

---

## I · CONTRATO

### 1. Desacuerdo
```
Ω = 1 − corr                                      [adimensional]
Ω_disposición = mediana‖p_A − p_B‖ / L            punto de ruptura 50 %
Ω_inventario  = P_p‖p_A − p_B‖ / L                con p ≥ 100(1 − 1/2n)
```
**Dominio:** n ≥ 3, emparejamiento por asignación óptima. **DER + MED.**

### 2. Banda de acuerdo
```
A = √( Ω_imp / Ω_acto )                           [adimensional]
```
**Ω_imp = el impostor MÁS CERCANO**, no el típico. El impostor es *una dirección de destino
equivocada*, nunca otro individuo. **DER + MED** (3·10⁶ impostores).

### 3. Zona muerta del contrato
```
dA/A = ½ √( u_imp² + u_acto² )
contrato ⟺ A > 1 + dA/A
```
Con u = 10 %: **A ∈ [0,934 · 1,071] es EMPATE, no contrato.** **DER.**

### 4. Contrato como tasa
```
FAR = P(Ω_imp ≤ Ω_acto)
FAR ≤ 3/k          con k impostores y CERO por debajo   (regla de tres, 95 %)
```
**Un FAR sin su k no dice nada.** Medido: FAR ≤ 10⁻⁶ con k = 3·10⁶. **MED.**

### 5. Índice de decidibilidad (Daugman)
```
d′ = |μ_I − μ_G| / √( (σ_I² + σ_G²)/2 )
```
**LIT** (Daugman 2006, 2·10¹¹ comparaciones). Medido en nuestro acto: d′ = 5,5.

### 6. Multiplicidad — el mejor de k
```
F_k(x) = 1 − [1 − F_0(x)]^k
```
La asignación óptima escoge la mejor de muchas correspondencias. **La multiplicidad efectiva se MIDE
contando cuántas compiten dentro del umbral; ni 1 ni n!.** **DER + LIT.**

### 7. Ley de la banda
```
A = K_d √( a / σ )        K₂ = 0,632 · K₃ = 0,597
```
**Robusta a su propio exponente:** con 0,4 en lugar de 0,5, A = 3,82 y el contrato aguanta; haría
falta p < 0,212. **DER + MED** (3 sustratos + D-605: 0,56).

### 8. Exclusión instantáneo–certificado
```
ψ = g K⁴ / A⁴                 g = 3 + (3 − dim del grupo de simetría)
ψ = 1  ⟺  A = (g K⁴)^¼ = 0,786 < 1
```
**Instantáneo y certificado se excluyen, con margen.** En nuestro acto ψ = 1,03·10⁻⁴: el acto es
**9.713 veces más material que informacional**. **DER.**

---

---

## II · INSTRUMENTO

### 9. Umbral dinámico
```
δ = K_Δ · (σ_suelo / μ_suelo) · √2          K_Δ = 3
umbral = (1 + δ) · suelo
```
El **√2** es porque hay dos medidas independientes (origen y destino) y las varianzas se suman.
**Guarda obligatoria: abortar si n < N_suelo_min.** K_Δ = 1 daría 9 % de falsos vetos; K_Δ = 3 da 0 %.
**DER + MED.**

### 10. Ruido del suelo
```
error relativo de δ = 1 / √(2(n − 1))
```
n = 10 → 24 % · n = 50 → 10 %. **El suelo se mide RE-COLOCANDO, no re-fotografiando** (regla 413).
**DER + MED.**

### 11. Ventana de promediado
```
POR RUIDO            N ≥ 9 (σ/tol)²
POR ENMASCARAMIENTO  N ≤ 1/β           β = punto de ruptura del estimador
si N_ruido > N_masc  →  no se promedia: se exige que pasen TODAS
```
**La ventana la fija el punto de ruptura.** **DER.**

### 12. Punto de ruptura del percentil
```
β(p, n) = (100 − p)/100 · n            atípicos tolerados
p ≥ 100 (1 − 1/(2n))                   para detectar UNA unidad
```
p98 con n=50 tolera exactamente 1 → detecta el **10 %**. p99 → **100 %**. **MED.**

### 13. Ligaduras
```
ligaduras = d·n − d(d+1)/2             en 3D: 3n − 6     (Maxwell, 1864)
déficit = 6 para todo n                los seis del cuerpo rígido
```
**El `n ≥ 49` NO viene del rango: viene de la precisión exigida.** **DER + LIT.**

---

## III · MÁQUINA

### 14. Campo de desacuerdo
```
D(r) = C · r^α                          [C] = µm·mm^(−α)
```
⚠ **α es un parámetro AJUSTADO, luego las unidades de C cambian en cada ajuste: un umbral fijo sobre
C no es dimensionalmente válido.** El criterio va sobre `D(r₀)` en una separación de referencia.

### 15. Puente con el núcleo gaussiano del gremio
```
D²(r) = 2d [ C(0) − C(r) ]                     función de estructura

núcleo gaussiano    C = σ²exp(−(r/υ)²)   →   α = 1
núcleo exponencial  C = σ²exp(−r/υ)      →   α = 0,5
```
**α ≥ 0,95 exige un campo diferenciable en media cuadrática.** Un campo exponencial da 0,5 y **no pasa
nunca**. **DER + LIT.**

### 16. Regla de decisión del GATE-0
```
VETO        si α < 0,35                        fiable al 98,7 %
PASA        si α ≥ 0,95  Y  D(176 mm) ≤ 35 µm
INTERMEDIO  todo lo demás                      NO basta para lanzar el acto
```
**GATE-0 es un veto fiable y un visto bueno malo (46 %).** Estimador: **Theil-Sen** (ruptura 29,3 %);
con OLS una mota de 50 µm arrastra α de 0,974 a 0,765. **MED.**

### 17. Requisito de correlación · **la ley del mapa**
```
υ ≥ L                  υ/L converge a 0,6
```
**υ es del tamaño de la OPERACIÓN que conformó la pieza.** Fresadora punto a punto: 100-500 mm.
Molde, prensa, embutición, hidroconformado: la pieza entera.
> **Las dos cáscaras deben conformarse en UNA operación con el mismo utillaje.** **DER.**

### 18. Supresión de armónicos
```
multi-paso con n posiciones  →  los armónicos múltiplos de n NO se separan
```
Rejilla cuadrada → sólo n=4 → ciega a 4θ, que es la perpendicularidad X/Y de una fresadora de 3 ejes.
**Un reparto circular no alcanza las esquinas de un campo cuadrado: o el campo es redondo, o no hay
giros.** **DER + MED.**

### 19. Paralaje por altura de asiento
```
r_real = r_aparente · (L_cam − h(R)) / L_cam        h(R) = √(R² − r_asiento²)
```
Hasta **400 µm** en el borde con diámetros de 6-18 mm. Residuo tras corregir: **0,03 µm**.
**La identidad corrige su propia lectura.** **DER + MED.**

---

## IV · CUSTODIA Y ESTRUCTURA

### 20. Pared por carga viva
```
t ≥ √( k · m · g · (L/2) / (E · suelo) )           k ≤ 0,5 (Timoshenko / WRC 107)
```
Acero ≥ 4,0 mm · aluminio ≥ 6,5 · composite ≥ 7,5 (robusto a toda la familia de k). **DER + LIT.**

### 21. Pandeo externo
```
P_cr = 2E / √(3(1−ν²)) · (t/R)²        knockdown por imperfección ≈ 0,2
```
**DER + LIT** (ASME).

### 22. Choque térmico ⚠
```
σ = E α ΔT / (1 − ν)
```
**A ΔT = 60 °C se alcanza la fluencia. Criterio: |ΔT| ≤ 50 °C entre caras, ventana instantánea.**
**DER.**

### 23. Fatiga por ciclado
```
σ_ciclica = P R / (2t) < 0,4 S_y            cada acto = 1 ciclo
```
11,9 MPa contra 82: vida infinita. **DER + LIT** (ASME).

### 24. Permeación de gas por el sello
```
Q = P · A · Δp / L                  [P] = sccm·cm/(s·cm²·atm)
```
EPDM: 15 años para salir de la banda NASA. FKM: 246. **La permeación no es el cuello: lo es la fuga
ALREDEDOR del sello, que es otra magnitud.** **DER + LIT.**

### 25. Tasa de fallo operacional
```
tasa ≤ 3/n           con n actos observados y CERO eventos
```
TUP: 37 ocupantes, 0 muertes → **≤ 8,1 %**. Para afirmar 10⁻³ hacen falta 3.000.
**«Cero muertes en 37» significa «como mucho 1 de cada 12».** **LIT + DER.**

---

## V · OCUPANTE

### 26. Tolerancia al choque — **régimen de IMPACTO (< 2 s)**
```
g ~ t^(−0,461)              R² = 0,968       (Eiband, NASA Memo 5-19-59E, 1959)
```
45 g @ 44 ms · 25 g @ 0,2 s · 10 g @ 1,6 s. Pendiente de subida ≈ **500 G/s**.
**Exponente 0,46 = ENERGÍA constante, no impulso (1,0). El daño humano es limitado por energía.**
⚠ ASTM D3332 usa exponente 1: **se resuelve por alcance — Eiband rige el ocupante, D3332 la carga
inerte, y rige el menor.** **LIT.**

### 27. Tolerancia sostenida — **régimen de TRÁNSITO (> 2 s)** ⚠
```
4,5 g  de pie          9 g  reclinado + traje anti-g          25 g  inmersión líquida
```
> **Eiband NO aplica a un tránsito de minutos.** Confundir los dos regímenes da 45 g donde lo
> correcto son 9. **LIT.**

### 28. Tiempo de tránsito
```
t = 2 √( d / a )              a = g_sostenido · 9,81
```
**El tiempo lo fija el OCUPANTE, no la masa.** La masa fija la **energía**, que escala como **L³**.
**DER.**

### 29. Autonomía de una cabina sellada ⚠
```
t_CO2 = V · (3/760) / (n · 0,5 L/min)          límite NASA: 3 mmHg, media horaria
t_O2  = 0,065 · V · 0,21 / (n · 0,55 L/min)    banda NASA: 145-155 mmHg
```
Con V = 2 m³ por ocupante: **t_CO2 = 15,8 min, INDEPENDIENTE de n** (el volumen escala con los
ocupantes). El CO₂ manda siempre. **DER + LIT.**

### 30. **Acoplamiento soporte vital ↔ aceleración** ⚠ *(el más reciente)*
```
cabina SELLADA viable  ⟺  t_viaje(a) < t_CO2
```
NY–Tokio: a 1 g el viaje dura 35 min y el CO₂ da 16 → **ECLSS obligatorio**. A 9 g dura 11,7 min →
**llega sellada con 4,1 min de margen**.
> **No se puede ir CÓMODO y SELLADO a la vez.** La decisión de soporte vital y la de aceleración
> **no son independientes**, y el marco las trataba en capas separadas. **DER.**

---

## V-bis · TIEMPO

### 36. Separabilidad del acto ⚠
```
t_acto(m,d,a) = T(m) + τ(d,a)
T(m)   = 2·N_suelo·t_manejo(M_total) + t_prep + t_verif     SOLO masa
τ(d,a) = 2√( d/(a·g) )                                      SOLO ruta
```
**Ninguna magnitud aparece en los dos términos.** `t_manejo` es **discreto**: a mano 0,5 · polipasto
3 · grúa 8 · grúa pesada 15 min. **DER + DEC** (el término de manejo es el que más conviene medir).

### 37. Distancia de cruce
```
d* = a·g·( T(m)/2 )²
```
Es una **escalera**, no una curva: 17.204 km · 358.983 · 2.356.629 · 7.780.000. **DER.**

### 38. Fracción de vuelo
```
f_vuelo = 1 / (1 + T/τ)
```
**Cuanto más cerca el destino, menor fracción es el viaje.** **DER.**

---

## VI · ESCALA

### 31. Dificultad de certificación
```
Ω ∝ 1/L                    una cabina mayor es MÁS FÁCIL de certificar
α decrece con L            una cabina mayor hace el GATE-0 IMPOSIBLE
```
**Los dos efectos son opuestos y del cruce sale `υ ≥ L` (fórmula 17).** **DER.**

### 32. Masa y energía
```
t_pared ∝ L        M_cáscara ∝ L³        E ∝ M ∝ L³
```
De 30 cm a 3 m: la cáscara pasa de 9 a 888 kg, **×99 de energía para el mismo viaje en el mismo
tiempo**. **DER.**

---

## VII · MÉTODO

### 33. Escala evidencial
```
duda = Π (1 − wᵢ)  sobre líneas INDEPENDIENTES, tope 0,99
MED_AJ 0,95 · MED_PRO 0,85 · DER 0,70 · LIT 0,60 · DEC 0,30
corroboración matemática: factor 0,8 sobre el residuo (NO es independiente)
```

### 34. Regla 4, hasta el fondo
```
capa  = MÍNIMO de sus condiciones
marco = MÍNIMO de las capas
```
**Promediar condiciones deja que la nota la decida qué condiciones metes en la lista.**

### 35. Completitud de una afirmación
```
completa ⟺ enunciada ∧ dimensionada ∧ fechada ∧ falsable ∧ costeada ∧ acotada ∧ RESISTIDA
```
Siete ejes. **Completo y verificado son dos cosas y se reportan las dos.**

---

# ANEXO B · Reproducibilidad

Todo el código y los datos están versionados. Los puntos de entrada:

| fichero | qué hace |
|:--|:--|
| `core_engine/src/maquina.py` | motor de verificación: calibrar · enviar · recibir · verificar |
| `core_engine/src/gate0.py` | GATE-0, con placa de anillos y Theil-Sen (`--autotest` valida el instrumento) |
| `core_engine/src/ciego.py` | protocolo de ciego con compromiso SHA-256 |
| `core_engine/src/escala.py` | escala evidencial por capas |
| `experiments/lib/auditoria_marco.py` | **los ocho ejes sobre las 109 afirmaciones** |
| `experiments/lib/mapa_universal.py` · `mapa_razonado.py` | el diagrama de fases |
| `experiments/lib/bateria.py` | las 100 pruebas generadas |
| `docs/FORMULARIO.md` | **las 35 ecuaciones del marco, con dominio y unidades** |
| `experiments/lib/caso_ny_tokyo.py` | el caso real NY→Tokio, de 1 a 10 ocupantes |
| `experiments/lib/REGLAS.md` | las 647 reglas de método |
| `docs/decisions/decisions_registry.md` | el registro cronológico completo, D-001 a D-682 |

**Semillas declaradas:** 7 (generación del banco), 11 y 5 (análisis). **Plataforma:** numpy 1.26.4,
scipy 1.13.1.

> Cualquier laboratorio que ejecute el GATE-0, B1-B4 o el acto queda invitado a publicar sus resultados
> contra los criterios de falsación de la sección 6.2. **El marco está escrito para ser refutado.**

---

# ANEXO C · BATERÍA 16 · Cinco cargas × cinco trayectos

**Por qué está en el paper:** una batería ataca una afirmación aislada; **un caso real exige todas las
afirmaciones a la vez**, con números y destino concretos. Este anexo aplica el formulario completo a
veinticinco casos, y **las tres predicciones escritas antes de correr se cumplieron**.

### A 9 g sostenidos · CO₂ en cabina sellada: 15,8 min

| carga | ruta | tiempo | v máx | masa | energía | α | veredicto |
|:--|:--|--:|--:|--:|--:|--:|:--|
| **1 tornillo** | Londres–Berlín | 3,4 min | 9,1 km/s | ~0 kg | ~0 | 0,998 | **PASA** |
| 1 tornillo | Londres–Sídney | 14,6 min | 38,7 km/s | ~0 kg | ~0 | 0,998 | **PASA** |
| 1 tornillo | órbita baja | 1,5 min | 7,8 km/s | ~0 kg | ~0 | 0,998 | **PASA** |
| 1 tornillo | Tierra–Luna | 69,6 min | 184 km/s | ~0 kg | ~0 | 0,998 | **PASA** |
| 1 tornillo | Tierra–Marte | 13,9 h | 2.204 km/s | ~0 kg | 0,12 TJ | 0,998 | **PASA** |
| **1 persona** | Londres–Berlín | 3,4 min | 9,1 km/s | 232 kg | 0,01 TJ | 0,750 | GATE-0 |
| 1 persona | Londres–Sídney | 14,6 min | 38,7 km/s | 232 kg | 0,17 TJ | 0,750 | GATE-0 |
| 1 persona | órbita baja | 1,5 min | 7,8 km/s | 232 kg | 0,01 TJ | 0,750 | GATE-0 |
| 1 persona | Tierra–Luna | 69,6 min | 184 km/s | 232 kg | 3,93 TJ | 0,750 | GATE-0 **+ CO₂** |
| 1 persona | Tierra–Marte | **13,9 h** | 2.204 km/s | 232 kg | **562 TJ** | 0,750 | GATE-0 **+ CO₂** |
| **5 personas** | Tierra–Marte | 13,9 h | 2.204 km/s | 1.330 kg | 3.228 TJ | 0,656 | GATE-0 + CO₂ |
| **1 elefante** | Londres–Berlín | 3,4 min | 9,1 km/s | 21.456 kg | 0,88 TJ | 0,561 | GATE-0 |
| 1 elefante | Tierra–Marte | 13,9 h | 2.204 km/s | 21.456 kg | 52.096 TJ | 0,561 | GATE-0 |
| **2 elefantes** | Tierra–Marte | 13,9 h | 2.204 km/s | 50.656 kg | **122.991 TJ** | 0,531 | GATE-0 |

### Las tres predicciones, escritas antes de correr

**P1 ✔** · el CO₂ no muerde en trayectos terrestres y es catastrófico en Luna y Marte.

**P2 ✔ — y es el resultado más importante del anexo** · **α es idéntico para la misma carga en las
cinco rutas.**

> **La carga decide el GATE-0; la ruta no lo toca.** El filtro de admisibilidad depende del tamaño
> de la cabina, y el tamaño de la cabina depende de lo que va dentro. **Ir a Marte no es más difícil
> de certificar que ir a Berlín: es más difícil de pagar.** Son dos problemas distintos y el marco
> los separa limpiamente.

**P3 ✔** · a 9 g durante 13,9 h hacia Marte, `v_max` = 2.204 km/s = **0,7 % de c**: no hace falta
tratamiento relativista.

### Comodidad contra estanqueidad, ruta por ruta

| ruta | tiempo a 1 g | ¿cabe en 15,8 min? | soporte vital |
|:--|--:|:--|:--|
| **Londres–Berlín** | **10,3 min** | **SÍ** | **sellada basta** |
| **órbita baja** | **13,3 min** | **SÍ** | **sellada basta** |
| Londres–Sídney | 43,9 min | NO | ECLSS obligatorio |
| Tierra–Luna | 3,5 h | NO | ECLSS obligatorio |
| Tierra–Marte | 41,6 h | NO | ECLSS obligatorio |

> **Sólo dos rutas admiten una cabina cómoda Y sellada: Londres–Berlín y la órbita baja.**
> Todo lo demás exige depuración activa de CO₂, y eso convierte la cabina en un vehículo con
> soporte vital — no en un volumen cerrado.

### La órbita baja es cualitativamente distinta

```
E/m mínima = v²/2 + g·h = 30,4 + 3,9 = 34,3 MJ/kg      IRREDUCIBLE
```

En los demás trayectos la energía depende de cuánto aprietes: ir despacio sale barato. **En órbita
baja la fija el DESTINO** — hay que llegar *con* 7,8 km/s tangenciales, no llegar y parar. **No baja
por ir más despacio.**

> **Y de ahí el resultado que más sorprende de las veinticinco celdas: la órbita baja es más rápida
> y diecisiete veces más barata que Londres–Sídney** (1,5 min y 0,01 TJ contra 14,6 min y 0,17 TJ).
> Porque a LEO basta alcanzar 7,8 km/s, y cruzar 17.000 km balísticamente a 9 g exige **38,7 km/s**.
>
> **Salir del planeta es más fácil que rodearlo.**

### Las energías, en contexto

| caso | energía | = Hiroshimas | % del consumo **mundial** anual |
|:--|--:|--:|--:|
| 1 persona · Londres–Berlín | 0,01 TJ | 0,0 | 0,000 % |
| 1 persona · Tierra–Marte | 562 TJ | **8,9** | 0,000 % |
| 2 elefantes · Tierra–Marte | 122.991 TJ | **1.952** | **0,020 %** |

> **La energía es enorme como bomba y trivial como presupuesto.** Dos elefantes a Marte son 1.952
> Hiroshimas de energía cinética **y a la vez una cinco milésima parte de lo que la civilización
> quema en un año.**
>
> **El problema de Marte no es cuánta energía hace falta: es concentrarla.** Son **2.458 GW
> sostenidos durante 13,9 horas** sobre 50 toneladas sin convertirlas en plasma — frente a los
> ~8.000 GW de toda la potencia eléctrica instalada del planeta.

---

# ANEXO D · LAS 109 AFIRMACIONES DEL MARCO

**Por qué están aquí:** un marco cuya meta es que otros lo ejecuten tiene que poder
**enumerarse**. Si no se puede listar, no se puede auditar; si no se puede auditar, no es
un marco.

**Este anexo se genera desde `experiments/lib/auditoria_marco.py`**, no se escribe a mano.
La versión anterior decía 158 afirmaciones cuando el instrumento ya tenía otras tantas
distintas, y el documento se contradecía consigo mismo — que es exactamente el fallo que
el marco existe para impedir.

> **Nota sobre el tamaño de esta lista.** Se preguntó si convenía llegar a mil
> afirmaciones. La respuesta del propio marco es que **no**: la regla 566 dice que
> *«promediar condiciones deja que la nota la decida qué condiciones metes en la lista»*.
> Añadir novecientas afirmaciones que salgan todas al 100 % no fortalece el marco: **lo
> hace más fácil de aprobar**. Los hallazgos que de verdad cambiaron el marco no vinieron
> de añadir afirmaciones, sino de **atacarlas**.

## D.1 · Estado por eje

| eje | qué pregunta | cumplen | % |
|:--|:--|--:|--:|
| **1 enunciado** | formula o umbral escrito con precision | 109/109 | **100.0 %** |
| **2 unidades** | dimensionalmente valido | 109/109 | **100.0 %** |
| **3 evidencial** | MED/DER/LIT/DECL con su fuente | 109/109 | **100.0 %** |
| **4 falsable** | hay un experimento que lo refutaria | 109/109 | **100.0 %** |
| **5 costeado** | ese experimento tiene precio y plazo | 109/109 | **100.0 %** |
| **6 ventana** | ventana de promediado y condiciones declaradas | 109/109 | **100.0 %** |
| **7 RESISTIDO** | ha sido ATACADO por un calculo de la bateria y ha sobrevivido | 109/109 | **100.0 %** |
| **8 MEDIDO** | **existe una MEDIDA DE BANCO, no una derivacion ni una cita** | 0/109 | **0.0 %** |

**MARCO COMPLETO (los 8 ejes, las 109 afirmaciones): 87.5 %**

El octavo eje se añadió **porque** los siete primeros llegaron al 100 %. Un instrumento
que marca 100 % en todo **ha dejado de discriminar**, y las notas las pone quien hace el
trabajo: **un 100 % autoevaluado vale menos que un 98,7 % con huecos nombrados.**

## D.2 · Lo que falta en los siete ejes de planteamiento

**Ninguna.** Los siete ejes de planteamiento están completos; lo que falta es el octavo, y ése no lo cierra ninguna batería.


## D.3 · Las 109 afirmaciones

Leyenda de ejes: `1` enunciado · `2` unidades · `3` evidencial · `4` falsable · `5` costeado · `6` ventana · `7` resistido · `8` **medido**.

| # | afirmación | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|--:|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | Om disposicion <= (1+delta)*suelo | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 2 | inventario p98 <= su propio suelo | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 3 | recuento nA == nB | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 4 | identidad |dd| <= media brecha minima | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 5 | identidad SOLO valida para n < 99 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 6 | correlacion de cascaras > 1,8 m (3 m) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 7 | pared >= 4,4 mm en cabina de 3 m | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 8 | VALIDEZ: 6 meses o 1 acto (IMCA D024) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 9 | deriva: re-verificar cada 6 meses | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 10 | TASA operacional = cota 3/n, con su n | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 11 | dT <= 50 C entre caras (choque termico) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 12 | CO2: 16 min sellada -> ECLSS obligatorio | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 13 | cascara MONOLITICA (upsilon>=L la impone) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 14 | FMEA: colapso por vacio | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 15 | FMEA: fatiga por ciclado | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 16 | FMEA: corrosion | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 17 | FMEA: fractura fragil | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 18 | FMEA: fallo de union | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 19 | FMEA: choque termico | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 20 | FMEA: soportes y anclaje | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 21 | FMEA: pasamuros | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 22 | FMEA: autonomia de soporte vital | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 23 | FMEA: atrapamiento y egreso | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 24 | FMEA: evento medico | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 25 | contrato A > 1 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 26 | FAR <= 3/k (regla de tres) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 27 | GATE-0 alpha >= 0,95 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 28 | GATE-0 D(176 mm) <= 35 um | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 29 | K_DELTA = 3,0 (preinscrito) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 30 | n_min: d*n - d(d+1)/2 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 31 | psi = g K^4 / A^4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 32 | ley A = K_d sqrt(a/sigma) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 33 | suelo de deteccion 1,0 mm al 90 % | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 34 | choque: Eiband=ocupante, D3332=carga | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 35 | envolvente Eiband (g, duracion) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 36 | ppCO2 <= 3 mmHg media horaria | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 37 | pared: acero>=4 / Al>=6,5 / comp>=7,5 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 38 | iris: condiciones de captura + FRR con n | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 39 | O2 <= 23,5 % + alarma (NFPA 99) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 40 | diluvio en <= 3 s (NFPA 99 Class A) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 41 | materiales no sinteticos, O2-compatible | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 42 | extincion en campana + test 6 meses | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 43 | MAQ: iluminacion del lector | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 44 | MAQ: referencia termica del campo | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 45 | MAQ: energia SIN litio en el sellado | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 46 | MAQ: residuos y fluidos | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 47 | MAQ: comunicacion con el exterior | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 48 | MAQ: instrumentacion para el ocupante | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 49 | MAQ: interfaz de propulsion | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 50 | MAQ: control de actitud | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 51 | MAQ: v_max > 12 km/s => EXO-ATMOSFERICA | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 52 | MAQ: soak termico en T(m), y en destino | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 53 | MAQ: la cabina se guarda EN la sala | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 54 | MAQ: energia en estacion | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 55 | MAQ: pasamuros, cuantos y para que | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 56 | MAQ: sensor termico de dos caras | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 57 | MAQ: giro motorizado de la placa (M3') | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 58 | MAQ: BIBS en humo | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 59 | MAQ: canal de datos entre estaciones | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 60 | CABINA: coste por material y tamano | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 61 | CABINA: energia transito>>estacion>>cab | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 62 | CABINA: control certif. EXTERNO siempre | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 63 | CABINA: todo commodity menos el utillaje | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 64 | CAPAS: toda importacion entre capas se DECLARA | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 65 | limbos: suma = COTA SUPERIOR (se solapan) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 66 | elasticidad e(L,x) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 67 | esquema de mensaje 1.806 B | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 68 | campos suelo_heredado_de / verif_funcional | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 69 | TARIFA 1.073 EUR/acto a 1 g | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 70 | SLA POR CLASE DE RUTA, no global | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 71 | cascada de responsabilidad | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 72 | pipeline de 24 estados | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 73 | rollback antes de S13 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 74 | limite duro de 3 reintentos | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 75 | LA PUERTA NUNCA ES EL CASTIGO | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 76 | cordon umbilical + bateria S12-S16 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 77 | umbilical REDUNDANTE + bateria de reserva | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 78 | techo de la burbuja L <= 5,03 m | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 79 | E ~ L3: energia por persona PLANA | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 80 | el suelo de B admite hasta 7,8x el de A | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 81 | asimetria de ruta se paga en TIEMPO | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 82 | potestades A/B (A construye, B juzga) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 83 | APTITUD MEDICA (lista de vetos) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 84 | edad minima 12 anos (criterio del cuello) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 85 | ayuno + antiemetico + succion | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 86 | rampa <= 1,0 psi/min (oido medio) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 87 | cero objetos sueltos en cabina | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 88 | boton del ocupante hasta S13 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 89 | rotacion 40 min -> 8,2 actos/dia | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 90 | formula 28 valida solo < 1.421 km (9 g) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 91 | 1 g vs 9 g: E lineal en a | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 92 | retorno en vacio: +44 % de energia | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 93 | dosis de radiacion /74 frente a Hohmann | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 94 | CALENTAMIENTO AERODINAMICO | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 95 | estampido sonico y efectos en tierra | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 96 | salida de la sala (pozo / techo) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 97 | colision: trafico aereo, LEO, basura | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 98 | meteorologia de estacion | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 99 | dos actos que se cruzan | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 100 | propiedad de la cabina | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 101 | T_max <= 450 C (fluencia), no 35 um | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 102 | techo de q por altura (max-Q) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 103 | TODO acto es EXO-ATMOSFERICO | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 104 | retirada 50.000 ciclos / inspec. 5.000 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 105 | prima >= 3/n x VSL: INASEGURABLE hoy | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 106 | orden de banco 25->80->534->620 EUR | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 107 | ARQUITECTURA DECLARADA: 1 g | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 108 | independencia de los FIRMANTES, no de las empresas | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |
| 109 | los primeros actos se venden SIN SLA | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · |

**Las 109 afirmaciones llevan `8` en blanco sin excepción.** Ésa es la lectura honesta del
anexo: el marco está enunciado, dimensionado, fechado, falsado, costeado, acotado y
atacado — y **nadie lo ha medido todavía, empezando por nosotros**.
