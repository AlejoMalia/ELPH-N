# Reglas de ejecución

**Cada experimento debe dejar el siguiente más barato.** No es una aspiración: es un
requisito de cierre. Un experimento que solo produce datos y no reduce el coste del
siguiente está a medio terminar.

## Antes de lanzar — `preflight.chequeo()`, en orden de coste creciente

| | comprobación | cuesta | si falla |
|---|---|---|---|
| 1 | **MATE** (`mate.py`, D-108) — ¿hay trabajo ya demostrado? | nada | quitarlo con `compartir.py` |
| 2 | **PARALELISMO** — ¿cuántos obreros caben? | nada | cola de trabajo, no reparto fijo |
| 3 | **SECUENCIAL** (`secuencial.py`, D-107) — ¿parada temprana? | **paga α** | solo si 1 y 2 no bastan |
| 4 | **POTENCIA** (D-111) — ¿basta K para las condiciones NUEVAS? | 1 piloto | `regla_K` con `diagnostico_sigma` |

**Nunca se salta el 1 y el 2.** Son gratis y no tocan el protocolo. Pagar α (paso 3) o
gastar cómputo (paso 4) antes de haber quitado la grasa es tirar recursos.

## Antes de calcular — mirar los registros

`diagnostico_sigma()`, `regla_K()`, `coste_experimento()`, `extrapolacion_tasa()` y las de
`fases.py` **responden sin simular**. El programa tiene 292 medidas de σ, 30 tasas y 19
efectos del signo guardados. **Antes de lanzar un proceso para averiguar algo, comprobar
si ya está medido.**

> Caso real (D-115): se lanzó un piloto de **4 horas** para preguntar si subir K arreglaría
> una σ. La respuesta estaba en los registros. El piloto se canceló.

## Al cerrar — qué deja el experimento para el siguiente

Un experimento no está cerrado hasta responder a esto por escrito:

- [ ] ¿Qué **constante** deja medida? (coste, σ, tasa, cota de ruido…)
- [ ] ¿Qué **etapa** suya era redundante, y está ya en `compartir.py`?
- [ ] ¿Qué **fallo de instrumento** destapó, y está en la puerta o en `preflight`?
- [ ] ¿Qué **afirmación anterior** invalida o acota?

## Reglas de operación aprendidas a golpes

- **No se añaden obreros en caliente.** Cerrojo por PID; para cambiar, parar y relanzar
  en frío (D-112).
- **No se toca un diseño en vuelo con datos ya a la vista** (D-109).
- **`K` no se fija a ojo** cuando el experimento introduce una condición nueva (D-111).
- **Antes de afirmar que dos circuitos difieren**, comprobar si el grafo es el mismo:
  grafos distintos exigen superar la cota de ruido metodológico (D-117).
- **Parchear código sin probarlo cuesta más que probarlo.** Prueba de humo con K mínima
  antes de comprometer horas.

## Medido antes de optimizar

`csr(M.toarray() * g)` densifica una matriz 448×448 para multiplicarla por un escalar.
`M * g` hace lo mismo escalando `.data`: **103× más rápido**. Pero son **11 s de 50 min
por punto — el 0,4 %**. No es el cuello y **no se toca**.

> Medir antes de optimizar ahorró un cambio inútil en código que ya dio dos fallos.

## Tras cada parche, reimportar

Un parche por **rango de texto** (`s[s.index(a):s.index(b)]`) puede llevarse por delante
código añadido antes dentro de ese rango. Ocurrió: `diagnostico_sigma()` se añadió y se
borró dos comandos después, y una decisión llegó a afirmar que la herramienta existía
cuando ya no estaba.

> **Después de cada parche a una librería: `python3 -c "from X import Y"`.** La sintaxis
> correcta no prueba que la función siga ahí.

## Una herramienta que nadie importa es código muerto

Auditoría obligatoria tras añadir cualquier módulo a `lib/`:

```bash
grep -rl -e "import X" -e "from X import" --include='*.py' experiments/ | grep -v "lib/X.py"
```

> Ha fallado **dos veces**: `puerta.py` en D-074, `puerta_v2.py` en D-125. En ambos casos la
> herramienta existía, la decisión la anunciaba, y **ningún experimento la cruzaba**.

**Las comprobaciones de runtime se cablean en el punto de paso** (`abrir()`,
`conectoma_real()`), nunca en un módulo que haya que acordarse de llamar.

## Antes de diseñar un experimento, inventariar la base de datos

**Un campo guardado en 58 ficheros y usado en un solo punto es una pregunta ya pagada y sin
cobrar.**

```bash
# qué campos existen y en cuántos ficheros
python3 -c "import json,glob,collections; c=collections.Counter()
[c.update(json.load(open(f)).keys()) for f in glob.glob('*/results/*.json')]
print(c.most_common())"
```

> Ocurrió con `curva_a`: **58 ficheros × 20 celdas medidas**, y solo se usaba `b*`. De ahí
> salió D-131 — una ley universal, cero simulaciones nuevas, y sustituye 19 celdas por un
> número.

**Y la pregunta que sigue: ¿qué fórmula nueva convierte ese dato en respuesta?** No basta
con mirar el dato: hay que **crear la matemática** que lo explota. Una fórmula validada
ahorra un experimento entero.

## Rechazar por el motivo correcto

Una idea puede tener un envoltorio malo y un núcleo contrastable. **Rechazarla por el
envoltorio la deja sin testar.**

> Ocurrió con el «Mapeo Tensorial por Ondículas» (D-105 → D-144): se descartó por un
> isomorfismo forzado, cuando el núcleo —asignar bits por banda en vez de uniformemente—
> era una hipótesis concreta que se comprueba en minutos. Salió **negativa (7 % de ahorro)**,
> y eso **reforzó** un resultado propio al cerrarle una vía de escape.

**Al rechazar: separar el envoltorio del núcleo, y decir cuál de los dos se rechaza.**

## Antes de recalcular una magnitud del repositorio, leer su definición

**Un nombre igual no garantiza la misma fórmula.**

> Ocurrió con `F` (D-145 → D-146): la recalculé como `corr(W, W')` cuando
> `instrumento.weight_fidelity()` la define como **distancia de Frobenius normalizada**
> `1 − ‖W−W'‖_F / ‖W‖_F`. Sobre esa magnitud falsa construí una decisión entera y dos
> análisis más. La definición estaba a un `grep` de distancia.

**Y al comparar simulaciones: verificar que corren con el MISMO protocolo.** Sin ruido y con
otra K, Ψ sale inflada y no es comparable con lo guardado.

## El inventario también se aplica al PLAN

No basta con inventariar antes de lanzar: hay que hacerlo **antes de proponer**.

> Ocurrió con E-1 (D-149): propuse cinco experimentos y el investigador preguntó si les
> había aplicado el método. **El primero ya estaba respondido en el dataset** — el cruce
> perturbativo aparecía en 20 pares guardados.

**Un plan sin inventario es una lista de cosas que quizá ya sabemos.**

## `preflight` responde lo que le preguntas

`chequeo()` no valida que las etiquetas de dependencia sean coherentes con el parámetro
barrido. Si nombras el parámetro `'canal'` pero etiquetas las etapas como
`('grafo','tarea')`, dirá **75 % de redundancia** — y será falso.

> Ocurrió en P3-2 (D-152). El valor real era ~0 %: cada canal es un grafo distinto.

**Comprobar que el parámetro barrido aparece en al menos una tupla de dependencia.**

- **Un diseño se mide contra el SUELO, no contra cero.** Con lectura perfecta el destino
  sigue sin ser el origen (el payload no es la red entera). Comparar Ω contra 0 hace
  parecer fracaso lo que es el límite del payload — y esconde que el escáner ya llegó
  (D-220: 1,24× el suelo en los tres circuitos, y aun así uno «falla»).
- **En un escáner la especificación que manda es la precisión, y no vale 0,999.** Una
  sinapsis inventada de 2.895 sube Ω un 48 %; quitar diez no se nota (D-220). Antes de
  gastar dosis en ver más, comprobar que no se está inventando nada.
- **Un parámetro congelado sin declararlo es una decisión escondida.** D-188/189 fijaron
  la dosis total y la regla de voto; el techo que parecía físico era de esa elección.
  Al inventariar un mecanismo propio, listar qué se congeló y por qué.
- **Submuestrear un conjunto y ampliarlo no son la misma operación.** Un exponente
  ajustado quitando elementos no predice lo que pasa al añadir otros nuevos: en D-223
  falló por un 64 %, siempre en el mismo sentido.
- **Un coeficiente de un modelo con R² bajo no sirve para descontar nada.** Si el ajuste
  no describe los datos (D-223: R²=0,24 entre circuitos), sus exponentes no pueden usarse
  para separar causas de otro experimento.
- **Una hoja de especificaciones con los ejes aislados no es una hoja.** En D-225 cada
  eje cumplía en su límite; los cuatro juntos daban 0/3 y hubo que doblar el margen en
  todos (D-226). Medir siempre el presupuesto conjunto antes de publicar un límite.
- **Antes de reinterpretar una columna como magnitud física nueva, mirar su RANGO.** En
  D-227 tomé `vol` (vóxeles) por `syn_count` y simulé 31.552 contactos por conexión. El
  disparate estaba en la tabla de la parte 0; me paró el control, no la lectura.
- **El ruido dinámico no se promedia con la ventana.** En un sistema recurrente, un
  sorteo por paso cambia la trayectoria: mirar más tiempo la ve alejarse, no volver.
  Sólo el ruido de MEDIDA baja como 1/√T.
- **`rho_pot` está OBSOLETA: usar `banco.rho()`.** La iteración de potencia arrancaba de
  un vector con semilla fija en orden de nodo: no era invariante al reetiquetado y salía
  sesgada. Movía Ω 3,4× su propio ruido (D-228).
- **Un patrón oro sobre una cantidad con ruido compara DISTRIBUCIONES, no valores.**
  Fallé dos veces seguidas en D-229: primero exigiendo igualdad bit a bit de una variable
  aleatoria, después comparando una distribución contra una constante de varianza cero.
- **Añadir a un conjunto y sustituir dentro de él no son la misma operación** (segunda vez
  que me pasa, tras D-223). Un resultado sobre «añadir» no autoriza nada sobre «cambiar».
- **Un solapamiento entre dos redes es una propiedad del EMPAREJAMIENTO, no del tejido.**
  Antes de leer un ρ como una diferencia biológica, acotar el techo optimizando la
  correspondencia: en D-232 subió de 0,27 a 0,73 sin tocar los datos.
- **Cuidado con optimizar usando información que el aparato real no tendría.** La búsqueda
  local de D-232 usa los DOS conectomas; un sistema real sólo tiene tipos celulares. El
  número resultante es una cota, no una especificación.
- **Valores idénticos al último decimal entre dos condiciones distintas = artefacto,
  no hallazgo.** Segunda vez (D-227, D-233). Antes de leer una fila, contar cuántos
  elementos ha tocado de verdad la manipulacion y **imprimirlo**.
- **Antes de exigir igualdad, probar con distancia.** La misma información que da 2 % de
  aciertos como huella exacta da 92 % como coste de emparejamiento (D-233 -> D-234).
- **Un dato que no sirvio para una pregunta puede ser el unico que sirve para otra.** Los
  99 pares L/R del gusano dieron celda NULA en H3-cruce y son la unica verdad de
  referencia del programa para puntuar un emparejador (D-234).
- **Si dos circuitos comparten grafo, sus cifras identicas son UNA medida, no dos.** INF y
  FB (D-218) han aparecido como «2 de 3» en varias tablas: son una selección repetida.
- **Apagar un mecanismo puede DEGENERAR el sistema en vez de aislarlo.** Quitar el signo o
  la saturación deja una red donde todo correlaciona con todo: lo que se mide entonces no
  es la ausencia del mecanismo (D-238). Preferir manipulaciones GRADUADAS.
- **Mas informacion no es mejor: medir la PREVALENCIA de un rasgo antes de darselo a un
  emparejador por distancia.** Uno casi constante ocupa una dimension y solo diluye (D-237).
- **Un umbral que separa dos veredictos hay que justificarlo ANTES, o no se firma.** En
  D-241 fije 0,35 sin razon, midio 0,41, y el script imprimio una etiqueta que no se
  sostiene. Lo que se firma es la descripcion, no la etiqueta.
- **Cuando afinar deja de comprar, preguntar si la informacion DISCRIMINA**, en vez de
  seguir refinando. En D-241 la pareja verdadera y la impostora estaban a la misma
  distancia: mas busqueda no podia ayudar (D-241).
- **Antes de dar por «no disponible» un nivel del manifiesto, mirar dataset por dataset.**
  M3 (uniones gap) figuraba como nunca disponible porque mosca y raton no las dan; el
  gusano las traia en el MISMO fichero, y valian 84x -> 6x (D-242).
- **Si dos causas salen fuertes y opuestas, eso NO es «ninguna domina»: es la respuesta.**
  En D-248 escribi la condicion esperando que una ganara, y el script imprimio que el
  confundido no se resolvia cuando en realidad daba la descomposicion (n/densidad)^2.
- **Un umbral de la hoja puede depender del criterio de PUERTOS, no solo del dispositivo.**
  Con puertos por grado el suelo baja 3x y los umbrales estaticos dejan de morder (D-249).
- **Antes de catalogar tecnologia, usar la checklist para reducir el espacio.** En D-250
  los ejes estaticos de la hoja no discriminaban: el catalogo abierto se redujo a tres
  preguntas cuantitativas. Sin ese paso habria sido el catalogo de papers ajenos que el
  propio investigador critico.
- **Lo externo se etiqueta [EXTERNO] y no se usa para afirmar, solo para acotar.**
- **Un AUC alto sobre una tasa base baja NO es capacidad de reconstruccion.** AUC 0,814
  con base 3,5 % dio 14 % de precision en el top-N, y la red sintetizada salio PEOR que
  ninguna (D-251). Antes de celebrar un AUC, construir la cosa y puntuarla.
- **Un modelo con mejor R2 que predice lo imposible NO se publica.** En D-252 el ajuste
  lineal ganaba en R2 y daba tolerancia NEGATIVA donde habia tolerancia medida positiva.
  Entre modelos, primero se descartan los que contradicen un punto medido.
- **Si una regla no encuentra su vocabulario en un dataset, devolver NO APLICA, nunca 0.**
  En D-255 el 0 % silencioso fabrico un cambio de veredicto que no existia.
- **Una regla de independencia puede quitarte el punto que necesitas.** Excluir FB por
  compartir grafo con INF es correcto para replicar; en D-256 me dejo sin el unico
  circuito de holgura baja y sin curva. Antes de excluir, comprobar que no era el que
  daba el CONTRASTE.
- **Si TODO control degenera, la pregunta se contesta con la condicion real sola.** En
  D-258 quitar o barajar el cableado daba Omega=1 siempre; la conjetura se refuto
  comparando la curva real contra su propia recta, sin control externo.
- **Al comparar variantes, cada una lleva SU PROPIA referencia.** Comparar todas contra la
  referencia de la variante original hace que todas empeoren por construccion: mide
  «cambiar algo cambia la dinamica», que es obvio (D-260).
- **Un cociente cuyo denominador tiende a cero no es un estadistico.** La «caida»
  bits(1)/bits(4) se disparo a 135x y 320x porque bits(4) bajaba a 0,009 (D-261). Elegir
  una medida que no divida por lo que se apaga.
- **Antes de leer una celda de un barrido, comprobar que no esta SATURADA.** Pedir densidad
  90 donde solo hay para 45 devuelve el mismo circuito: dos filas identicas que no son dos
  medidas (D-261).
- **Segunda confirmacion: rankear no es reconstruir.** AUC 0,828 y precision 38,7 % (casi
  3x la de D-251) siguen dando una red indistinguible del azar (D-266). El AUC no es la
  metrica; la reconstruccion puntuada si.
- **Antes de declarar una incognita «bloqueada por datos», comprobar que no esta bloqueada
  por una dependencia.** La morfologia llevaba semanas en via A y solo faltaba
  `pip install cloud-volume` (D-266).
- **Tercera vez: dos operaciones que se parecen no son la misma.** Anadir vs sustituir
  (D-223/D-229), excluir vs contrastar (D-256), y ahora **apuntar mal vs inventar**
  (D-267). Antes de extender un resultado, nombrar la operacion exacta que medía.
- **Preinscribir el umbral sirve sobre todo para CONTENERSE.** En D-268 dos factores
  quedaron a 0,666 y 0,665 de un umbral de 0,70 escrito antes: con 0,65 elegido despues
  habria «encontrado» la causa. El umbral previo es lo que separa el hallazgo del ajuste.
- **Una incognita se puede CERRAR en negativo si el criterio esta escrito antes.** Sin eso,
  cada intento fallido deja la puerta abierta y se gasta computo indefinidamente (D-268).

- **Un muestreador con parámetro escalar devuelve un escalar.** `r.binomial(N, p)` con N
  entero da UN número; con un array de longitud nnz da uno por arista. La primera versión
  hacía fluctuar toda la red al unísono —ruido global de ganancia— y salía 32× más
  optimista. **Lo delató el control de reproducir una celda ya medida**, no la lectura del
  código. Si un barrido nuevo se solapa con uno viejo, incluir el solape SIEMPRE. (D-274)
- **Un mínimo hallado en rejilla gruesa es un techo, no un valor.** D-227 barrió
  2·8·32·128 y publicó «128»; el mínimo real caía en el hueco 32–128. Antes de construir
  sobre un número de rejilla, refinar la rejilla alrededor de él. (D-274)
- **Una cuenta puede acertar la pendiente y fallar la ordenada.** N ∝ (1−p)/p falló como
  predicción absoluta y acertó entera al reanclarla en un punto medido del propio banco.
  Publicar la forma como ley y la constante como calibración. (D-274)
- **Antes de nombrar «la clausula mas cara», comprobar cual es la restriccion ACTIVA.**
  Si el coste es max(A,B), medir sólo A y declararlo caro es un error de bulto: en el
  punto de operación A y B empataban y ahorrar en A no ahorraba nada. (D-274 → D-275)
- **Dos rejillas gruesas seguidas dieron el mismo sesgo**: D-227 (2·8·32·128) y D-256
  (1·8·128) publicaron 128 cuando el mínimo era 64. Una potencia de dos de más se paga
  en el doble de dispositivos. (D-275)
- **Elegir el estadistico que la metrica mira.** Me alarmé por el error RELATIVO por
  arista, que en dispositivos reales llega al 293 %; Ω mira el error ABSOLUTO, y ese error
  relativo enorme cae sobre pesos casi nulos. La alarma era del estadístico equivocado, y
  **el control de mediana fue lo que lo demostró**, no el razonamiento. (D-277)
- **Cuando varios casos que cumplen comparten un numero, ese numero es la especificacion.**
  Cuatro distribuciones de error distintas convergieron en σ/√N ≈ 1 % por arista: eso deja
  de ser una coincidencia y pasa a ser el criterio de un solo elemento. (D-277)
- **Un suelo de 0,0000 exige el control de discriminacion antes de publicarse.** Si la red
  colapsa a un punto fijo, la lectura no ve la entrada y Ω ≈ 0 sale gratis. Criterio:
  Ω(entrada A, entrada B) > 0,5. Aquí el control PASÓ y el resultado era real — pero sin
  él no habría sido publicable. (D-279)
- **«Cuantos» y «cuales» no son la misma exigencia.** El 54-62 % de inyeccion que el
  programa arrastraba era el coste de NO poder elegir; eligiendo por grado basta el 5 %.
  Antes de dar una fraccion como requisito, decir si el diseño podia elegir. (D-279)
- **Que dos ejes compongan como max() no se extiende a cuatro.** D-276 lo midió para
  deriva y liberación; al añadir cuantización y ventana el presupuesto conjunto se agota
  y N deja de arreglarlo. (D-278)
- **Una frontera medida a 3 semillas esta a un ruido de invertirse.** El barrido de H*
  salio no monotono con 3 semillas y monotono con 8: cerca del contrato, 3 semillas no
  distinguen 0,0478 de 0,0501. Fronteras y umbrales: 8 semillas mínimo. (D-282)
- **Antes de aceptar un dominio restringido, comprobar que la restriccion no es del
  montaje.** «FB no certifica» parecia una propiedad del tejido; era de los puertos con
  los que lo mediamos, y el mismo grafo con otros puertos certifica. (D-282)
- **Que una eleccion gane no significa que aporte.** La seleccion por grado gana siempre,
  pero su residuo sobre el ajuste en H es 0,0000: importa SOLO porque sube H. La
  especificacion entonces no pide un criterio, pide un numero. (D-282)
- **Una constante ajustada que no transfiere hay que intentar derivarla antes de replicarla.**
  H* = 0,482 era un ajuste sin mecanismo; el algebra da H* = c/contrato en dos lineas y
  explica ademas por que la recta no viajaba entre tejidos. (D-286)
- **Dos formulas simetricas alrededor del punto medido cuadran las dos.** `c/0,05` y
  `1 - c/0,05` dan 0,511 y 0,489 cuando c ~ 0,025: comprobar el algebra contra un caso
  ALEJADO del punto de ajuste, no contra el punto de ajuste. (D-286)
- **Una regla cuyo predictor se mide en la misma celda que predice puede ser una identidad.**
  `H >= c/0,05` se reduce a `hoja <= 0,05`, la definicion de PASS: acertaba 5/5 sin probar
  nada. Antes de celebrar un acierto, sustituir y ver si la regla es tautologica. (D-287)
- **Un coste que sale negativo en parte de las celdas no soporta un ajuste.** c dio valores
  negativos en 4 de 18: el ruido era del orden de la magnitud. Afirmar la comparacion
  gruesa, no las pendientes. (D-287)
- **Distinguir lo que es POR ARISTA de lo que es CALENDARIO GLOBAL.** La ventana de
  escritura no se puede enmascarar por arista: al hacerlo, un tercio del grafo corria a 1/8
  de fuerza y el «subconjunto» salia 3x peor que el total. Antes de ablacionar un eje,
  preguntarse si es una propiedad del elemento o del proceso. (D-288)
- **«Coste por unidad» sobre una magnitud que satura solo informa del tamaño del conjunto.**
  En 9 de 9 celdas el subconjunto menor salio mas caro por arista. La razon se reconstruia
  exactamente desde los tamaños. Comparar a fraccion igualada, o regresar contra la
  fraccion y mirar el residuo. (D-288)
- **Una prohibicion nueva obliga a revisar lo publicado ANTES de escribirla.** La
  prohibicion de promediar holguras (D-282) invalidaba una ablacion de D-278 que ya habia
  llegado a la hoja y al encargo: el «eje dominante» era la respuesta del circuito de poca
  holgura arrastrando la media. Al escribir una regla, buscar que resultados previos la
  violan. (D-290)
- **Declarar H junto al veredicto, nunca suelta.** El suelo depende del camino de medida:
  FF dio 0,0152 (D-221) y 0,0193 con 8 semillas y la tuberia unica, o sea H 0,696 frente a
  0,614. Citar una H sin su medicion es citar un numero de otro experimento. (D-290)
- **Estimar un margen sin correr el INVENTARIO es saltarse el primer paso de la TRIADA.**
  Declare tres huecos «bloqueados por dato» y los tres estaban en disco: un grafo 20x mas
  denso (raton), dos individuos emparejados (CXmacho/CXhembra), un cuarto modelo de
  dispositivo con deriva temporal (SONOS), y un circuito humano en la banda de holgura que
  decia que faltaba (H2-SUP). **Segunda vez en el programa.** Antes de decir «falta dato»,
  listar lo construido. (D-294, D-295)
- **Usar SIEMPRE todos los circuitos construidos, no los tres de costumbre.** El programa
  llevaba decenas de decisiones sobre H4/FF-INF-FB sin tocar los cuatro de H2, que son mas
  densos, traen NT por nodo y contienen el unico caso humano de margen estrecho. (D-295)
- **Un compresor generico no es una cota de compresibilidad estructural.** lzma perdio
  contra la cuenta cerrada en 7 de 9 conectomas: no sabe que los nodos son intercambiables.
  Para «cuanta informacion hay aqui», usar cotas de teoria de la informacion, no benchmarks
  de compresion. (D-298)
- **Cuando el optimo cae en el ultimo punto de la rejilla, la rejilla es el resultado.**
  El barrido de bloques daba k=32 siempre; extendido a 256, el optimo real es k=64 y el
  ahorro sube del 18 % al 26 %. Misma leccion que D-275, tercera vez. (D-298)
- **Un veredicto impreso por el script no es un resultado: mirar dentro de los grupos.** El
  script concluyo «f* sigue a la holgura» por un r=+0,684 y un rango coincidente; dentro de
  cada metodo de puertos f* era CONSTANTE mientras H barria 0,305. La correlacion la
  producian dos puntos de otro grupo. (D-304)
- **Antes de creer un mecanismo propio, probarlo directamente.** El «solape» entre puertos y
  neuronas enteras explicaba los datos y era falso: excluir los puertos del envio no abarata,
  rompe. Una explicacion que encaja no esta medida hasta que se manipula. (D-304)
- **Una razon de 1,0x es un EMPATE, no un ganador.** El script concluyo «lo fija la lectura,
  1,0x mas efecto» cuando los dos efectos principales valian 0,15 exactamente. Segunda linea
  automatica enganosa en dos experimentos: **leer la tabla, no el veredicto impreso**. (D-305)
- **«Plano frente al numero» no implica «plano frente a la identidad».** D-221 midio que el
  suelo no depende de CUANTOS canales de lectura hay, y de ahi supuse que la lectura no
  importaba. Su identidad mueve f* tanto como la inyeccion. (D-305)
- **No dejar conclusiones escritas a mano en la salida de un script que sigue corriendo.**
  Imprimi «la caida se acelera: -0,018 y -0,162 por decada» calculado sobre seis puntos, y
  el septimo lo revirtio: el texto quedo junto a la tabla que lo contradice. Los numeros de
  una conclusion se calculan de los datos, siempre. (D-306)
- **Una serie con una reversion al final no autoriza a extrapolar.** r = -0,645 sobre siete
  puntos cuyo ultimo se aparta 1,5 sigma en sentido contrario: la pendiente no existe.
  Comprobar monotonia antes de proyectar. (D-306)
- **Un contenido de informacion NEGATIVO es imposible: es la senal de que la formula esta
  fuera de su rango.** log2 N < 0 dice «no existe ningun grafo con esas restricciones»
  cuando el grafo real las cumple. Cazo un ahorro falso del 85 %. (D-307)
- **Toda cuenta de compresion necesita un CASO LIMITE como control.** El DC-SBM a k=1 debe
  reducirse al modelo de configuracion: coincidio a 0,001 bits/arista y eso valido la
  implementacion en un segundo. Sin ese control, el artefacto habria pasado. (D-307)
- **Un modelo mas expresivo puede comprimir PEOR: su cabecera cuenta.** El DC-SBM pierde
  contra el SBM llano en 6 de 7 porque transmitir la secuencia de grados cuesta mas que la
  estructura que explica. Comparar longitudes de descripcion COMPLETAS, cabecera incluida.
  (D-307)

83. **Un ajuste publicado de ruido de dispositivo no es un dato crudo.** Casi todo sigma_G(G)
    publicado es la distribucion DESPUES de programar-y-verificar. Si lo comparas con un
    barrido de un solo disparo estas comparando dos cosas distintas: declaralo o el N que
    salga es mentira (D-324).
84. **Antes de creerte una prevalencia sacada de un clasificador, mira su tasa base.** Un
    clasificador 82 % exacto sobre un conjunto curado BALANCEADO puede tener 67 % de falsos
    positivos a la prevalencia real. Aqui se propago un 4x al signo del demostrador de
    referencia y sobrevivio 300 decisiones sin que nadie lo mirara (D-325).
85. **Cuando falte un segundo dataset, busca la segunda etiqueta dentro del primero.** H01
    traia dos etiquetados E/I independientes; la peticion de un segundo conectoma humano se
    cerro sin salir del volumen que ya estaba en disco (D-325).

86. **Un estimador liso puede «certificar» ganandole al ruido del blanco.** Si el suelo esta
    por encima del contrato, la media global correlaciona mejor con la mitad 2 que la mitad 1,
    y eso NO es evidencia de que la especificacion baste (D-326).
87. **El control de discriminacion no es solo para acto_lib.** En cualquier regimen: si un
    perfil falso —otra region, ruido con los mismos momentos— certifica, el veredicto se
    retira. Dos resultados publicados cayeron por no aplicarlo fuera del nervioso (D-326).

88. **Comprueba la ley de escala ANTES de redactar la peticion que se apoya en ella.** Iba a
    pedir «datos corporales mas profundos»; medir suelo frente a cuentas (exponente -0,04,
    r=-0,09) mostro que la peticion era falsa (D-327).
89. **Un pomo que eliges tu no es un parametro: es un eje.** Barrelo y busca donde el control
    cambia de veredicto, en vez de fijarlo donde el resultado sale bonito (D-327).
90. **Antes de culpar al dato, descarta el observable; antes de culpar al observable, descarta
    la dinamica.** El suelo puede ser propiedad de la clase de dinamica y entonces ni el dato
    ni el observable lo mueven (D-327).

91. **Reconstruir una muestra y compararla contra ESA muestra mide compresion, no identidad.**
    La prueba de teletransporte es CRUZADA: el portador sale de una instancia fisica y tiene
    que senalar al sujeto en OTRA. La version circular daba 100 % por encima de un techo del
    40 % (D-329).
92. **Si un predictor baja el techo, el predictor sobra.** Una ridge de A a B hundio el techo
    de 36-42 % a 9-14 %: destruia senal. El emparejamiento directo no necesita modelo (D-329).
93. **Una firma de arquitectura puede redefinir la meta sin que nadie lo note.** A3 cerro tres
    bloques por alcance y dejo el nervioso como unico contenido; durante cinco sesiones
    «trabajar en el marco» significo «trabajar en el nervioso». Al firmar un alcance, decir en
    voz alta que meta deja de estar en el programa (D-329).

91. **La ceguera aparente de un contrato puede ser un observable debil, no una propiedad del
    contrato.** En COMPOSICION/v1 el modulo excitable parecia ciego a la interfaz (0,0049 con
    el 100 % degradado) porque se medio su actividad media por correlacion; con sus invariantes
    estadisticos la caza a z=52,8 con el 10 %. Antes de concluir «este contrato no ve X»,
    prueba el observable propio de ese contrato (D-339).

92. **Al probar aditividad, excluye las celdas donde un factor es cero.** Son aditivas por
    construccion (predicho = base + coste + 0 = medido) e inflan la mediana. En D-340 daban
    0,3 % de error frente al 2,3 % real de las celdas cruzadas.
93. **Si dos observables no son del mismo orden, no se pueden poner en la misma unidad sin
    convertir.** Omega es cuadratico en la amplitud del error y z es lineal: la unidad comun se
    fija en la AMPLITUD, con raiz para los cuadraticos (D-340).

94. **No podes nunca un experimento por lo que predigas.** La tasa de acierto de las
    predicciones pre-escritas del programa es del 56 % (10 de 18): sirven como disciplina, no
    para priorizar. Solo se poda por una COTA del paso 2 de la TRIADA (D-345).
95. **El suelo se mide una vez, con muchas semillas, y se guarda con su incertidumbre.** Con 8
    semillas el suelo tiene 8 % de error, que son 4 % en ⱎ: todo veredicto a menos de esa
    distancia del umbral es indistinguible de su contrario. En D-336, 12 de 20 celdas (D-345).
96. **Conocer la banda de ruido dice DONDE gastar semillas.** No se recorre toda la rejilla con
    mas semillas: solo la frontera. Y las celdas que pedirian centenares de semillas se
    declaran indecidibles en vez de fingir un veredicto (D-345).
97. **Antes de construir un contrato para un tejido, mide A.** Dos corridas frente a la docena
    de experimentos y las tres retractaciones que costo descubrirlo por las malas (D-344/345).

98. **Un veredicto agregado no se publica sin excluir antes las celdas triviales**, aquellas
    donde el resultado es cierto por construccion (K=N sin agregar, un factor a cero, el suelo
    evaluado dentro de muestra). Ha entrado tres veces por la misma puerta: D-340 (aditividad),
    D-345 (rejilla del acto) y D-352 (nivel critico). Las reglas 92 y 96 no bastaron porque
    dependian de que yo me acordara: **el codigo tiene que marcarlas y excluirlas solo**.

**99.** Un **sustituto sintético no vale hasta que reproduce el SUELO del original**. Si el
suelo del sustituto se aleja del real (D-369: 0,1175 frente a 0,0046, 25×), el sustituto no
modela lo que dice modelar y todo lo ajustado sobre él es ruido. Y **ninguna fila con
suelo > contrato entra en un ajuste**: ahí el contrato no existe y la tolerancia no está
definida. Comprobar ambas cosas **antes** de ajustar ningún exponente.

**100.** Si un barrido da **la misma cifra a cuatro decimales en todas las filas**, la variable
barrida **no está entrando en el cómputo**. Una pendiente de 10⁻¹⁹ no es un resultado nulo: es
la firma de una variable desconectada (D-371: el destino no participaba, se escribía el
manifiesto sobre la topología del origen). Comprobar la conexión **antes** de interpretar un
resultado plano.

**101.** Comparar dos espacios exige un **esquema de direccionamiento explícito**: qué nodo de
destino hace de qué nodo de origen. Los índices locales de dos muestreos son **arbitrarios**, y
compararlos mide renumeraciones, no biología (D-372: gestos idénticos para Corazón→Corazón y
Corazón→Cerebro). Emparejar antes de comparar, y **publicar la calidad del pareo** como
observable — mide si el destino puede siquiera aportar quien haga de cada ciudad del origen.

**102.** Toda banda `A` lleva su **tipo**: `A_técnica` (suelo = réplica del mismo dato con otra
semilla, dispersión ~1,2-1,5×) o `A_biológica` (suelo = tejido vivo distinto, dispersión ~20×).
Nunca `A` a secas. **Las decisiones de aparato sólo pueden apoyarse en `A_biológica`** (D-379).

**103.** Toda banda se publica también por **colas**, en la dirección conservadora:
`A_crit = ⱎ_impostor(p05) / ⱎ_suelo(p95)` — el impostor que **más** se te parece contra la
réplica que **menos** se parece a sí misma. `imp_p95/suelo_p05` es la cota optimista y no
sirve para garantizar un aparato (D-378).

**104.** **Escribir la cabecera TRIADA no es aplicarla.** Antes de lanzar un barrido, comprobar
que el cómputo pesado **depende de verdad de la variable barrida**. En D-386 el número de
canales sólo cambiaba qué columnas se leían al final, y la simulación completa se repetía en
cada fila: 1.008 corridas donde bastaban 168, 45 minutos donde bastaban 4.

## Regla 105 (D-407)
Un metodo estadistico mejor nunca sube la consolidacion de un marco; solo reparte mejor la
incertidumbre que ya tiene. **La consolidacion la compra la medida, no el metodo.**
Comprobado: copula gaussiana + proyeccion PSD de Higham, correctamente implementada sobre las
anclas, deja la consolidacion en 30 % -> 30 %. Con las anclas a +-1 %, el MISMO metodo da 100 %.

## Regla 106 (D-408)
Antes de creerse una banda estrecha, contar cuantas muestras entraron en el estimador. Una
banda que se estrecha porque se descartaron las muestras que no cruzaban no se ha estrechado:
**se ha truncado.** Comprobado: TOL_conn dio +-13,8 % usando 18 de 48 semillas y +-28,2 %
usando las 48.

## Regla 108 (D-412)
El valor marginal de un ancla se mide a la precision ALCANZABLE para esa magnitud, no a +-1 %
universal. Un +10 que exige +-3 % sobre una magnitud fractal no es un +10: es un imposible con
etiqueta de tarea. Comprobado: L_neurita_mm figuraba como +10 puntos y no puede comprarlos.

## Regla 109 (D-415)
Cuando una banda declarada se ENSANCHA al comprobar su procedencia, la consolidacion publicada
es una COTA SUPERIOR, no una medida. Comprobado: 4 de 10 anclas revisadas se ensancharon
(FFN_fus 24->50 %, pend_barrios 9,6->31 %, L_neurita 50->66 %, N_sinapsis 33->67 %). Las no
revisadas hay que suponerlas optimistas hasta prueba en contrario.

## Regla 110 (D-416)
Cuando una magnitud no tiene valor unico —fractal, dependiente de calibre o de tiempo— no se
abandona ni se le pone un cero: **se acota y se prueba el marco en la PEOR ESQUINA.** Precision
y robustez son criterios distintos; para una magnitud sin unidad fijada el que aplica es la
robustez. Comprobado: L_neurita no tiene valor unico y el marco aguanta [2,75 , 61,67] mm con
791,8x de margen. La pregunta «cuanto vale» no tenia respuesta y no hacia falta que la tuviera.

## Regla 111 (D-418)
Una tolerancia medida como MEDIANA no es una tolerancia: es el punto donde el proceso falla la
mitad de las veces. En un contrato que se aplica a una persona, toda tolerancia se publica al
CUANTIL de fiabilidad exigido, y el cuantil se declara junto al numero. Comprobado: TOL_conn
mediana 5,294e-3 -> cuantil 95 **1,024e-3**, 5,17x mas apretado.

## Regla 112 (D-419)
Condicionar en «el sistema sobrevive» no aporta informacion cuando el sistema sobrevive SIEMPRE.
La contraccion bayesiana exige que algo falle. **Robustez del 100 % y ganancia de precision por
filtrado son mutuamente excluyentes.** Comprobado: 20.000/20.000 muestras sobreviven y la
contraccion es 1,00x en las once anclas, a cuatro decimales.

## Regla 113 (D-420)
Antes de presupuestar la medida de un ancla, comprobar si es una DECISION SIN TOMAR.
mu_bioink era la eleccion de tinta; L_neurita era el calibre de trazado. Las dos parecian
incognitas caras de laboratorio y las dos se cierran DECLARANDO, no midiendo. Una decision
explicita elimina una falsa «imprecision de medida».

## Regla 114 (D-423)
Una triangulacion contra una ley de conservacion solo estrecha si TODAS las variables del
balance estan mejor acotadas que el objetivo. Una sola variable mal conocida en el denominador
destruye la ventaja. Comprobado: N_sinapsis por ATP da +-98 % (peor que el +-66,7 % de partida)
porque la tasa de disparo aporta 50x de los 114x de span, y las otras cinco juntas 2,1x.

## Regla 116 (D-429) · ETIQUETA DE REGIMEN, obligatoria
Toda certificacion lleva etiqueta: **{denso | disperso} x {con colocacion | sin colocacion}**.
Una certificacion sin etiqueta se considera **denso, sin colocacion** — el regimen facil.
Comprobado: el mismo acto da 100 % en {denso, sin} y **47,5 % en {disperso, con}** (D-424).

## Regla 117 (D-429) · PROHIBIDO exportar tolerancias entre regimenes
Un PASS en regimen denso **no respalda** una tolerancia del cuerpo. TOL_95 del gusano (grado
177) da 93,0 % en un espacio de grado 3,27: no llega al 95 %. Las tolerancias **se recalibran
en el espacio donde se aplican** (regla 115); solo se pueden ESCALAR si se ha demostrado que la
cola del suelo escala asi, y esa demostracion no existe.

## Regla 118 (D-429) · el aprendizaje activo ignora la validez fisica
Un criterio de adquisicion que maximiza reduccion de varianza colocara puntos donde mas
estrechan la banda, **aunque sean fisicamente invalidos**. Comprobado: el maximo brazo de
palanca eligio B=100.000 y 50.000 sobre N=500.000 — **5 y 10 barrios**, pleno efecto de borde;
la banda bajo de 22,9 % a 12,6 % mientras la estimacion se movia un 20 %. **Precision mejorada,
exactitud degradada.** Todo conjunto de candidatos lleva restriccion de validez declarada.

## Regla 119 (D-430)
Un efecto grande entre dos condiciones **no implica una ley continua entre ellas.** Antes de
ajustar una potencia, comprobar que la variable explicativa es monotona en el rango.
Comprobado: el suelo cambia x33 entre grado 177,6 y 3,27, pero `log s = a0 + a1 log <k>` da
R2 = 0,018 — porque el suelo sigue a **rho(M)**, no a <k>, y rho no es monotono bajo dilucion.

## Regla 120 (D-435)
**El modelo de error importa tanto como su magnitud.** Antes de declarar una tolerancia
imposible, comprobar si el error real es independiente o correlacionado. Comprobado: sigma*
pasa de 1,0 um (ruido blanco por celula) a 20,1 um (deriva correlacionada a lam=32d) — **20x**,
y la ganancia es LINEAL en lam/d. Ninguna maquina de fabricacion coloca cada elemento de forma
independiente, luego el ruido blanco por elemento describe un proceso que no existe.

## Regla 121 (D-435)
**Dos resultados incompatibles a la vez son la firma de un artefacto, no una paradoja.**
Comprobado: f*=0 exacto y sigma*=2,26 um simultaneamente delataron una rejilla de 7 celdas
muestreada por celda mas proxima. Cuarta aparicion de la degeneracion por discretizacion
(D-377, D-392, D-413, D-435). **Ante cualquier campo espacial: forma cerrada antes que rejilla.**

## Regla 122 (D-437)
Una tolerancia imposible puede volverse posible **cambiando el ESPECTRO del error en vez de su
magnitud.** Comprobado: sigma* pasa de 1,0 um a 20 um bajando el ancho de banda de deriva de la
maquina de 63 Hz a 1,9 Hz. La especificacion util no es «mas preciso» sino «que derive mas
despacio» — se pide una maquina peor en ancho de banda, no mejor.

## Regla 123 (D-439)
Un suelo tiene que ser **estocastico por construccion**. Si el «suelo» de un observable sale
EXACTAMENTE cero, no es un suelo: es la identidad, y toda razon calculada contra el carece de
sentido. Comprobado: d_B(origen, replica) = 0,0000 porque la replica sin ruido ES el mismo
grafo; la razon acto/suelo de 1,8e7 era dividir por cero.

## Regla 124 (D-440)
**Un criterio de verificacion no vale mas que el instrumento que lo alimenta.** Antes de
celebrar una discriminacion, comparar la perturbacion del ACTO con la del INSTRUMENTO: si el
instrumento perturba mas, la discriminacion medida es del modelo, no del mundo. Comprobado: el
suelo instrumental (e_conn=3e-3) da d_B = 161,9 en H0 y el impostor 248,3 — razon 1,5x, no los
13.775x que parecia D-439, porque el instrumento perturba 10-22x mas que el acto.

## Regla 125 (D-441)
Un contrato al **cuantil 95** exige potencia para distinguir 95 % de su alternativa relevante.
Con n=80 el intervalo binomial es +-6,8 puntos: **cualquier veredicto PASS/FAIL a ese n es
decorativo.** Hacen falta n >= 640 por brazo para separar 95 % de 91 % con potencia 80 %.

## Regla 126 (D-443)
Antes de usar cualquier observable espectral, **contar las componentes conexas**. En un grafo
desconectado lambda_2 = 0 POR CONSTRUCCION y todo cociente que lo contenga es una division por
cero disfrazada. Comprobado: el espacio disperso a grado 3,27 esta desconectado, lambda_2 =
-1,28e-16, y tres de los cinco observables de la DI-Signature salieron invalidos por eso.
**Tercer cero-division del mismo dia: el diagnostico hay que EJECUTARLO, no recordarlo.**

## Regla 127 (D-444)
**Aplicar TRIADA a la TAREA antes que al experimento.** Cronometrar una unidad de trabajo antes
de estimar el total, y comprobar si el inventario ya cubre parte. Comprobado: tres estimaciones
seguidas infladas 10-160x (40 min -> segundos, 2-3 h -> 20 min, «largo» -> 27 min) venian de no
hacerlo.

## Regla 128 (D-445)
**Un valor redondo no es evidencia de nada.** eta = 0,3332 se celebro como «1/3 exacto» y salio
de datos contaminados por el tramo de bajo N; con la rejilla limpia eta = +0,0053, compatible
con cero. Antes de leer significado en un numero bonito, comprobar que el rango de ajuste esta
libre de efectos de borde.

## Regla 129 (D-447)
**La redundancia estructural de un grafo escala con sus TRIANGULOS, no con sus aristas.**
A grado medio 3,27 hay 0,135 triangulos por nodo y la AUC de discriminacion entre arista real y
falso positivo vale **0,506 — azar puro**. Ningun decodificador puede corregir errores de
lectura ahi: la correccion de errores exige densidad, y el cuerpo no la tiene. La redundancia
tiene que venir de FUERA (lecturas repetidas o modalidades ortogonales).

## Regla 130 (D-449)
**Una comprobacion de paridad exige que el sindrome sea EXACTO.** Con 0,02 errores por nodo, un
ruido de +-1 en la medida de paridad genera 50x mas falsas alarmas que errores reales, y el
decodificador destruye mas de lo que arregla. Comprobado: paridad de grado con grado exacto da
factor 39x (AUC 0,989); con grado +-1 da 0,0x. **La redundancia multimodal no degrada
suavemente: tiene umbral.**

## Regla 131 (D-450) — **RETRACTADA en D-460: la dependencia es LINEAL (0,91-0,98), no cuadratica**
Cuando una capa depende de otra, medir el **EXPONENTE** de la dependencia, no solo su
existencia. Comprobado: D -> G es **cuadratica** (mejorar e_conn 39x mejora la razon del
verificador 1.478x = 39^1,99). El esfuerzo en lectura se amplifica al cuadrado en verificacion.

## Regla 132 · PROTOCOLO DE POTENCIA, congelado por contrato
Ninguna capa se declara CERRADA sin calculo previo de potencia. Parametros del contrato:
**alpha = 0,01 · beta = 0,90**. Para un PASS/FAIL al 95 % frente a la alternativa relevante:

    separar 95 % de 91 %  ->  **n >= 1.049**
    separar 95 % de 93 %  ->  **n >= 4.196**

Con alpha=0,05 y beta=0,80 los numeros bajan a 554 y 2.214, pero **ese no es el contrato**.
Todo resultado publicado declara su n y con que parametros cumple.

## Regla 133 (D-454)
Al degradar un observable para medir su sensibilidad, **comprobar que fraccion de entradas queda
corrompida.** Ruido uniforme en {-1,0,+1} corrompe el **67 %**, no el «+-1» que sugiere el
nombre. Comprobado: la regla 130 («la redundancia multimodal tiene umbral») se apoyaba en ese
contraste y queda EN SUSPENSO. Un acantilado medido asi puede ser del diseno del test, no del
sistema.

## Regla 134 (D-455)
**Una ganancia que aparece al salir del regimen declarado no es una ganancia: es una fuga.**
Comprobar siempre que el parametro que define el regimen sigue en su valor antes de aceptar un
resultado favorable. Comprobado: la decimacion aleatoria a m=8 da R=98,8 % — pero deja el grafo
en grado medio **24,8** cuando el regimen H se define por **3,268**. No comprime el mapa:
cambia de regimen, y en el denso ya sabiamos que todo pasa.

## Regla 135 (D-456)
**Un decodificador que solo puede ELIMINAR candidatos no reduce el error de OMISION.** Antes de
acreditar una ganancia a una magnitud, comprobar que el mecanismo puede actuar sobre TODOS sus
sumandos. Comprobado: la paridad de grado limpia el 97,9 % de los falsos positivos y es **ciega
a los falsos negativos**, que en una lectura son la mitad del error -> factor real **0,937x**,
no los 39x publicados en D-449.

## Regla 136 (D-459)
**Antes de dividir por la desviacion de un brazo de control, contar cuantos SUCESOS lo
generaron.** Con menos de un suceso por replica la desviacion es cero la mayoria de las veces y
la razon mide el tamano de la muestra, no el del efecto. Comprobado: a e_conn=7,68e-5 hay 0,299
sucesos/replica y los ceros suben al 74-99 %; las razones de 753x-4.127x son ruido de conteo.
Pone bajo sospecha el 14.071x de D-450.

## Regla 137 (D-460)
Cuando el suelo de un brazo de control es CERO en la mayoria de replicas, **la RAZON no vale y
hay que cambiar de metrica**. AUC y margen entre las dos poblaciones que importan —acto e
impostor— no tocan el suelo instrumental y sobreviven al ruido de conteo. Comprobado: las
razones de 753x-41.643x eran ruido (99,6 % de ceros), mientras AUC y margen daban un veredicto
limpio y estable con n=1.049.

## Regla 138 (D-464)
Cuando un prior falla, **comprobar si esta mirando la dimension equivocada** antes de buscar un
regularizador mejor. Comprobado: sobre el MISMO dato, el prior topologico da AUC 0,506 (azar) y
el geometrico —contacto fisico en el volumen 3D— da **0,9995 con recall 100 %**. No faltaba
estadistica: faltaba usar la geometria que ya estaba medida.

## Regla 139 (D-465)
**Una AUC alta no basta cuando la tasa base es baja.** Con 0,84 % de positivos, una AUC de
0,9599 deja la precision en **7 %** al recall del 95 %. Antes de celebrar un clasificador,
calcular la PRECISION al recall que el contrato exige, no la AUC.

**Regla 140:** *un término del presupuesto que ya es despreciable no puede comprar nada. Antes
de proponer compensar por otra vía, medir cuánto pesa esa vía HOY, no cuando se escribió.*

**Regla 141:** *una reducción se compara contra la pata que reduce, no contra el hueco
declarado. «3,95× frente a 2,35×» era un 3,95× sobre 92.000×.*

**Regla 142:** *declarar una constante no consolida: compra el derecho a una medida más barata.
La consolidación la paga siempre el laboratorio.*

**Regla 143:** *una cota estructural se verifica sobre el grafo real, no sobre el grado nominal.*

**Regla 144:** *al bajar resolución el error dominante es OMISIÓN, no fusión. Y la omisión es la
clase que ningún prior que recorte candidatos puede corregir (regla 135). Resolución y dosis no
son intercambiables.*

**Regla 145:** *una métrica de consolidación sólo consolida lo que mide. Antes de celebrar un
porcentaje, comprobar que el bloqueo declarado del programa es una de las cifras contadas.*

**Regla 146:** *una restricción heredada se revisa cuando cambia el supuesto que la generaba.*

**Regla 147:** *si un criterio suspende a un instrumento perfecto, el criterio está mal
calibrado. Comprobar qué puntúa el caso ideal bajo el ruido intrínseco del sistema.*

**Regla 148:** *la anchura de banda mide una cifra que se propaga; la probabilidad de superar el
umbral mide una cifra que sólo tiene que despejarlo. Usar el criterio equivocado hace que una
cadena resuelta puntúe 0 y que una cadena ciega puntúe 100.*

**Regla 149:** *una tolerancia y una medida de la misma magnitud no son la misma cifra. Antes de
usar un número como «lo alcanzable», comprobar si su procedencia dice «lo que el contrato
admite».*

**Regla 150:** *antes de lanzar un experimento que una decisión dejó pendiente, comprobar si ya
se corrió. El registro es lo único que convierte un fichero en un hallazgo.*

**Regla 151:** *antes de contar con promediar N lecturas, enumerar qué canales de error se
re-aleatorizan entre ellas. Un bloque se corta y se tiñe UNA vez.*

**Regla 152:** *cuando la tolerancia exige apagar el 99,7 % de un error, descomponerlo en canales
no ayuda: lo condena. La descomposición sólo salva si UN canal concentra casi todo.*

**Regla 153:** *cuando los errores de varios canales se solapan, apagar un canal recupera mucho
menos que su magnitud aislada, y menos cuantos más canales queden encendidos.*

**Regla 154:** *cuando un umbral absoluto suspende al caso ideal, traducirlo a la unidad relativa
del marco no es relajarlo: es corregirlo. Pero la holgura resultante es función del ruido
intrínseco supuesto, y hay que declararla con él.*

**Regla 155:** *un resultado obtenido poniendo cada factor blando en su extremo favorable es una
esquina, no una estimación. Antes de publicar un «estamos a N×», propagar los rangos.*

**Regla 156:** *cuando se corrige un ancla, recorrer las identidades que la usan. Aquí N_sin se
corrigió y el grado derivado de ella siguió con el valor viejo 66 decisiones.*

**Regla 157:** *no todo se compone igual. Medir la interacción antes de suponerla: los canales
físicos eran sub-aditivos al 0,615 y los parámetros que los gobiernan salieron separables.*

**Regla 158:** *una envolvente derivada no deriva el punto de trabajo. Si la curva de compromiso
es una recta, no hay óptimo que encontrar: la elección sigue siendo una decisión, pero con
procedencia y con techo.*

**Regla 159:** *antes de leer un índice de sensibilidad bajo como «esta entrada no importa»,
comprobar si el modelo tenía acoplamientos quitados por construcción.*

**Regla 160:** *un índice de interacción que sale exactamente cero delata la forma del modelo, no
una propiedad del mundo. Un modelo multiplicativo es aditivo en log y no puede mostrar
interacción.*

**Regla 161:** *confrontar los parámetros dominantes con datos ajenos al modelo puede anclarlos,
y anclarlos suele BAJAR la probabilidad: la incertidumbre siempre contiene esperanza.*

**Regla 162:** *un «principio» descubierto post hoc en un solo espacio, con una sola
coincidencia, no es un principio. Y si aplicarlo afloja el contrato en la dirección que conviene,
la carga de la prueba se multiplica.*

**Regla 163:** *un extremo de un rango de incertidumbre nunca puede ser el requisito. Si lo es,
la «esquina favorable» pasa por 1,0× por construcción y no informa de nada.*

**Regla 164:** *un instrumento que apaga un canal de error puede encender otro. Antes de contar
la ganancia de una modalidad nueva, enumerar los canales que INTRODUCE.*

**Regla 165:** *cuando una predicción descansa en un parámetro citado de memoria, el margen
declarado es parte de la predicción: «dos órdenes» y «3,2×» llevan a decisiones distintas.*

**Regla 166:** *una media corporal no es el lugar peor. Si el criterio es el máximo sobre lugares,
la tolerancia la fija el tejido MÁS DENSO, no el promedio del cuerpo.*

**Regla 167:** *un símbolo que aparece en dos cadenas distintas puede necesitar dos valores
distintos. `d` sirve para contar (media) y para tolerar (mínimo).*

**Regla 168:** *la capa que parece el bloqueo puede no ser la que decide. Proyectar todas las
capas sobre el veredicto común antes de dedicar el esfuerzo a una.*

**Regla 169:** *el alcance topológico de una magnitud en la red de dependencias no predice su
influencia en el veredicto.*

**Regla 170:** *antes de costear la incertidumbre de una máquina, comprobar que esa máquina
alcanza la tolerancia.*

**Regla 171:** *la anchura de banda no detecta un error de central. Una cifra puede tener la
banda más estrecha del marco y estar 536× equivocada: bien medida y mal planteada.*

**Regla 172:** *un índice de sensibilidad mide cuánto VARÍA el veredicto con una magnitud, no
cuánto MARGEN consume. Una magnitud puede tener Sobol cero y comerse el 87,9 % del presupuesto.*

**Regla 173:** *un presupuesto de error hacia atrás puede pedir a una capa más de lo que su
propia condición de existencia permite. Comprobar el reclamo contra los axiomas, no sólo contra
los rangos.*

**Regla 174:** *un criterio que se puede aprobar empeorando el instrumento no es un criterio.
Probar todo umbral contra la degradación deliberada del aparato antes de firmarlo.*

**Regla 175:** *distinguibilidad y fidelidad son criterios distintos. `A > 1` dice que llegaste
al sitio correcto; `Ω ≤ Ω_max` dice que llegaste bien.*

**Regla 176:** *un ratio sólo es adimensional si se demostró que lo es. Antes de mover el
denominador de una cadena, comprobar a qué valor del denominador se ancló el numerador.*

**Regla 177:** *un ancla con incertidumbre declarada que no mueve ninguna derivada es una columna
nula: medirla no puede cambiar nada.*

**Regla 178:** *la prohibición de exportar entre regímenes aplica a las LEYES igual que a las
tolerancias. Una ley de escala medida en un solo espacio es una ley de ese espacio.*

**Regla 179:** *antes de publicar un veredicto, remedirlo en un segundo espacio. Un veredicto
medido en un espacio es propiedad de ese espacio hasta que se demuestre lo contrario.*

**Regla 180:** *antes de atribuir una diferencia a los espacios, medir la variación DENTRO de un
espacio con el mismo protocolo y varias semillas. La varianza de submuestreo puede ser del mismo
orden que la diferencia entre tejidos.*

**Regla 181:** *no se rellena un hueco con el valor de un cúmulo global sin comprobar que la
magnitud pertenece al cúmulo.*

**Regla 182:** *una cota de potencia dimensiona el n para distinguir dos hipótesis vecinas. Si la
realidad está lejos de la frontera, el n exigido cae un orden.*

**Regla 183:** *no se mide la portabilidad de una magnitud con una función escalón de ella. R es
un indicador de paso: junto al umbral amplifica un 10 % en Ω hasta 65 puntos en R.*

**Regla 184:** *una razón entre/dentro que cae por debajo de 2 porque subió el denominador no
demuestra portabilidad: demuestra que el estimador perdió resolución.*

**Regla 185:** *un criterio que falla y otro que pasa sobre el mismo acto no son un conflicto:
son dos criterios. Comprobar si el criterio de cierre mezcla distinguibilidad con fidelidad.*

**Regla 186:** *antes de inferir una magnitud, comprobar si el dataset ya la contiene.*

**Regla 187:** *un grupo adimensional sólo es válido entre las dos magnitudes con las que se
midió. Cambiar una de ellas cambia el π y lo invalida.*

**Regla 188:** *un umbral que no se deriva por dentro puede corroborarse por fuera, y la
corroboración vale si la magnitud y el observable son los mismos.*

**Regla 189:** *un umbral de tasa de éxito debe compararse con el que alcanza el sistema real
consigo mismo.*

**Regla 190:** *un ajuste log-log que incluye puntos donde la dependiente se acerca a un suelo
ruidoso pivota su pendiente. Ajustar sólo donde la señal supera al suelo.*

**Regla 191:** *dimensionar `n` por el error binomial sólo vale si el error de muestreo domina.*

**Regla 192:** *una ley ajustada sólo vale si predice fuera de muestra. Una constante de
composición sólo es física si su uso MEJORA la predicción.*

**Regla 193:** *el orden de ataque por capas debe recalcularse cuando una capa cierra antes de lo
previsto.*

**Regla 194:** *compartir trayectoria bajo entrada no implica compartir atractor en reposo: la
dinámica libre puede amplificar la diferencia en vez de contraerla.*

**Regla 195:** *el mejor de N casos no es el resultado: es el máximo de una muestra. Dar la media
y la dispersión de todas las celdas antes de publicar.*

**Regla 196:** *«bloqueado por laboratorio» y «no publicado» no son lo mismo. Buscar si la cifra
existe medida con su incertidumbre antes de declararla inalcanzable.*

## 197 · toda tabla de fabricación lleva DOS columnas: precisión y paralelismo
Una tabla de modalidades que compara sólo precisión aprueba tecnologías **serie** que no pueden
hacer el trabajo. En D-492 el haz de electrones figuraba como «cumple» con 12,46× de margen
siendo inútil para 5,8e14 elementos, y la modalidad que sí sirve —colocación de origami de
ADN, 13,8 nm y una incubación por chip entero— **no estaba en la tabla**. · D-516

## 198 · un «pomo barrido» puede estar publicado como PORCENTAJE de la escala
Antes de declarar libre un exponente de escala, comprobar si la literatura da la magnitud como
fracción de la distancia medida: un «RMS del 1–3 % de la distancia» **es α = 1 medido**, no un
rango. Aquí estrechó la banda de la capa D **7,8×** (de 22,7× a 2,9×). · D-516

## 199 · un cuello con número vale más que una vía abierta sin él
E pasó de «colocar 10¹⁵ elementos a σ\*, sin demostrador concebible» a **2.745× en tiempo de
incubación**, con la ruta nombrada (concentración ~0,30 µM) y su modo de fallo nombrado
(agregación). El porcentaje de capa mide **consolidación del conocimiento**, no éxito: una rama
cerrada en negativo con cifra sube la capa igual que una que pasa. · D-516

## 200 · antes de declarar «conflicto de literatura», comprobar si un método está superado
En D-515 declaré conflicto entre la estereología de sección fina (11,05e8 sin/mm³) y la
envolvente de Drachman, y publiqué la cifra equivocada. La EM de volumen (FIB/SEM, 3D) ya había
corregido ese método: 4,814e8/mm³, que **cae dentro** de la envolvente. No había conflicto:
había un método viejo. · D-517

## 201 · predecir un punto inventado sólo demuestra que la ley interpola
Lo que convierte una capa de integración en un veredicto es predecir el punto que la
**tecnología real** impone. Aquí cambió qué capa manda: con `σ*/esp` = 0,0156 (origami) la
colocación aporta el 0,5 % del error donde D-491 le había medido el 53 %. · D-517

## 202 · la CV entre regiones no es el ε del total
La variación biológica entre regiones se **promedia** en un total corporal; la incertidumbre del
total es el error del promedio (SD/√n), no la CV. Aquí la diferencia era 29,9 % frente a 11,3 %,
y decidía si `portador_TB` pasaba la banda de 2× (ε crítico 21,0 %). · D-517

## 203 · «misma cuenca» sólo vale si la red tiene UNA cuenca consigo misma
Arrancar la misma red dos veces desde condiciones iniciales independientes. Si Ω consigo misma ≈
Ω del impostor, el criterio no está fallado: está mal planteado. En D-518 salió 0,99–1,02 en
15/15 por **multiestabilidad** (λ ≤ 0), no por el caos que predije. · D-518

## 204 · dos derivaciones del mismo contrato se cruzan antes de publicar un hueco
`Π_max` (modelo de margen, D-484) y el `Π` que exige el acto medido (F) difieren 4,9×, y D-516
publicó su hueco contra el más laxo. · D-519

## 205 · medir la conversión entre modelos de error antes de invertir una ley entre capas
Inversión de signo y borrado no son el mismo error: razón de daño medida 0,464 (9/9), que cambia
el umbral 4,38×. · D-519

## 206 · el impostor sólo se delata en la componente que depende de la dirección
En tejido vivo con ráfagas de red, quitar el modo común antes de medir Ω_imp: en `hdmea` pasó de 0,55 ± 0,34 a
0,9974 ± 0,0090. · D-520

## 207 · una tasa de fusión sobre esqueletos dispersos es cota inferior
Sólo cuenta fusiones entre esqueletos anotados. El ancla de Januszewski 2018 (0,041/mm) era 109× la evaluación
densa (RoboEM 3,3–6,1/mm; MICrONS 19,2 ediciones/mm). · D-520

## 208 · en redes multiestables la identidad lleva los bits de qué atractor
La sincronización generalizada es todo o nada por entrada (Ω_aux ≈ 1e-10 donde sincroniza). Alargar la
integración no quita el suelo: 600 → 4.000 pasos no lo movió. · D-520

## 209 · el tipo de contrato de un módulo lo decide su renovación medida
Si el cuerpo reescribe un módulo en semanas, su dirección celular no es identidad. El 83 % de las células son
glóbulos rojos y se renuevan en ~100 días: el 99,4 % de las células sale del contrato posicional. · D-521

## 210 · una ley de escala sólo fija el exponente dentro de su rango medido
«RMS del 1–3 % de la distancia» se midió en 0–40 µm; extrapolarlo a 320 nm contradijo D-488 (α ≈ 0,5 bajo la
malla del gel). · D-521

## 211 · comprobar que el peldaño existe antes de publicar un factor de distancia
«4,7e4× para funcionar tras vitrificar» parecía escala; lo real es que **ningún mamífero ha recuperado
circulación espontánea desde vitrificado, a ninguna escala**. Distancia de escala y peldaño ausente no se
escriben igual. · D-522

## 212 · una ventana biológica se estira con Q10, y eso es una cota cerrada
Multiplicar por 8.760 la tolerancia exige bajar 83–131 °C, fuera del agua líquida. Cuando la cota cae fuera del
régimen físico disponible, la tecnología deja de ser opción y pasa a requisito (aquí: vitrificar). · D-522

## 213 · si falta un peldaño, buscar el peldaño VECINO ya publicado
La resucitación de hámsteres enteros con 40–50 % de agua congelada (1954) convierte el experimento de
vitrificación en uno con **control positivo validable**. · D-523

## 214 · una cascada de regresiones independientes no conserva la masa
Hay que cerrarla con una constante biológica (hidratación de la magra 0,73). Pasó de 19,1 % de casos imposibles
a 0 %, y la confrontación de las dos rutas dio el error real del prior: 7,1 % en agua corporal. · D-524

## 215 · un prior vale lo que compra menos lo que cuesta, en bits
Sexo, edad, altura y peso cuestan 29 bits y compran 93: **3,2× netos**. Toda prelectura se mide así. · D-524

## 216 · tres cadenas independientes en el mismo número marcan la unidad del contrato
Difusión de oxígeno (Krogh), resolución de lectura del cuerpo (D-355) y distancia al capilar (D-356) coinciden en
**100 µm**. El módulo geométrico se construye a esa escala. · D-526

## 217 · antes de predecir distancia, separar cantidad de estructura
Los 35,8 kg de músculo y grasa los produce una planta de carne cultivada en un día; predije 20× de distancia.
Lo que falta no son kilos: es arquitectura vascular. · D-526

## 218 · profundidad de la jerarquía ≠ longitud de su contenido
×6.400 en volumen añade 12,7 niveles al árbol vascular (logarítmico) y 6.400× a la longitud impresa (lineal).
Publicar «6.400× de distancia» sin separarlas exagera el problema. · D-527

## 219 · la distancia se mide sobre lo que hay que FABRICAR, no sobre el total
La microvasculatura se autoensambla: se imprimen 70 km de los 11.000 km de capilar del cuerpo — el 0,64 %. · D-527

## 220 · evaluar una objeción física con la concentración real del sistema
El exotermo de polimerización hierve una resina acrílica (105 °C) y no mueve un hidrogel de colágeno al 1–2 %
(0,13 °C): factor 800 entre el caso temido y el real. · D-530

## 221 · entre rutas que discrepan, manda la que explica el experimento demostrado
El brote desde fuera (5 µm/h) no explica una construcción de 4 mm viva; el autoensamblaje in situ sí, y fija
`s` en 1–2 mm. · D-530

## 222 · si un hueco «de tiempo» tiene margen holgado y no cierra, es un hueco de TECHO · **CORREGIDA en D-538**
La maduración cabe 4–13× en el presupuesto y sigue sin llegar: falta fenotipo adulto, no semanas. · D-530

## 223 · antes de medir, contar cuántas cifras son identidades
En el motor del cuerpo, 12 de 22 lo eran, y tres anclas escritas por separado (difusión de O2, resolución de
lectura, distancia al capilar) eran **la misma**: `d_irrig`. El jacobiano no acelera el cálculo: dice qué ancla
comprar. · D-531

## 224 · una cifra en escala de intervalo no admite banda como razón
`T_vitrif` (una temperatura) daba un cociente absurdo al cruzar el cero. Se reporta el rango y se excluye del
recuento de bandas. · D-531

## 225 · comprobar si la magnitud es intensiva, extensiva o de SUPERFICIE antes de anclarla
La dosis de curado es J/cm² (fluencia), no J/cm³. Eso invierte el escalado: la energía por volumen cae como 1/D
y un módulo grande cuesta **menos** por litro. · D-532

## 226 · estrechar una cifra y añadir cifras mueven el porcentaje en sentidos distintos
Reportar siempre las dos cosas: el recuento de bandas < 2× y la banda de la cifra que se atacó (aquí 24,6× →
4,7× sin que el porcentaje se moviera). · D-532

## 227 · un contrato sobre estructura exige leer mucho más fino que la estructura
A la misma resolución (100 µm sobre arquitectura de 100 µm) el suelo sube a 0,74 y el contrato se queda en
A = 1,05. Suministro y muestreo no son el mismo número: `q_lectura = d_irrig / k`, k ≈ 20–30. · D-533

## 228 · un agente externo trae hipótesis, no medidas
De doce contradicciones se adoptaron cero y se verificaron dos. Sólo cuando dos caminos independientes dan lo
mismo, la hipótesis pasa a dato. · D-535

## 229 · clasificar antes de gastar un experimento: comprable / declarable / desconocida
En el cuerpo salieron 14 de 16 anclas y 12 de 21 celdas que **no eran preguntas**, y yo había estado midiendo
varias de ellas. Sólo la tercera clase justifica un experimento. · D-536

## 230 · comprobar que las incógnitas duras están DENTRO del instrumento
El motor del cuerpo propaga 26 cifras con rigor y **no contiene 3 de las 5 incógnitas reales**. Un instrumento
puede ser riguroso y estar mirando a otro lado. · D-536

## 231 · una cifra récord se lee con sus condiciones
«4,1e7 células/mL imprimibles» eran células FIJADAS en un vial de 5 mm; con vivas y a 12,6 cm la ley ρ·D = cte
da 4-8e5 y la distancia pasa de 1,05× a 54–108×. Un récord sin sus condiciones no es un dato. · D-537

## 232 · costear también la operación INVERSA
El marco costeó recalentar durante cuatro decisiones y nunca costeó enfriar. El muro estaba ahí: un cuerpo
entero no vitrifica de una pieza (falla 1,57×), mientras el recalentamiento sobra por 220×. · D-537

## 233 · comprobar si el muro es del PROBLEMA o de la TECNOLOGÍA elegida
La opacidad a 19 caminos libres de transporte era de la impresión tomográfica. SWIFT parte de densidad de
órgano y escribe con boquilla: el muro desaparece, a cambio de días en vez de minutos. · D-538

## 234 · un «techo» sin intervención probada no es un techo (corrige la 222)
El fenotipo fetal se levanta a adulto en 4 semanas con acondicionamiento electromecánico progresivo — pero
**sólo donde hay carga mecánica que aplicar**. En un hematíe no la hay, y allí el techo sigue. · D-538

## 235 · una cota en volumen puede ser una cota de longitud disfrazada
En conducción manda el ESPESOR: un brazo de 3,5 L y un cubo de 3,5 L tienen la misma masa y distinto destino.
El cuerpo humano vitrifica **tendido** (1,15×) y no **de pie** (0,51×). · D-539

## 236 · forma cerrada y ajuste empírico que coinciden al 2 % dejan de ser una apuesta
Y hay que usar el autovalor bueno antes de comparar: `τ = L²/α` daba 8,5 L y `τ = 4L²/π²α` da 33,1 L frente a
los 33,9 L medidos. · D-539

## 237 · un récord de UNA variable no mueve una celda
Densidad, volumen y resolución tienen que estar en la MISMA construcción publicada. Si están en tres papers,
la celda sigue desconocida. Tres veces seguidas cayó lo contrario: células fijadas en vial de 5 mm, bloque de
0,257 cm³, canal de 400 µm–1 mm. · D-540 (la propone el agente)

## 238 · mover una celda «con una condición pendiente» es moverla mal
Si la condición es la que decide, no se mueve. En D-538 moví la celda de fabricación con el volumen sin
verificar, y el volumen era 7.782×. · D-540

## 239 · leer los MÉTODOS del paper antes de proponer el experimento
El espesor de las criobolsas (5,5 / 6,5 / 10,5 cm) estaba publicado y decidía si el torso vitrifica. Propuse
medio día de congelador para obtener un número que llevaba años impreso. · D-541

## 240 · una condición de contorno idealizada da una cota optimista, y hay que declararla
«Superficie a temperatura fija» dio 32 cm de espesor crítico; con convección real (h = 100 W/m²K) son 9,0 cm
—3,6×— y el torso pasa de «vitrifica» a «falla». · D-541

## 241 · al adoptar una arquitectura, contar su coste de INTERFAZ el mismo día
Laminar el cuerpo en 9 losas parecía un detalle de montaje: crea **1,44 m² de herida interna** (76 % de la
piel) con 3×10⁸ capilares seccionados que no se suturan. · D-542

## 242 · pasar el contrato medido por el punto donde el demostrador propone operar
El primero del programa fallaría su propia verificación por leer a 8–25 µm cuando exige ≤ 5 µm. El arreglo es
una línea de la especificación. · D-542

## 243 · un dato negativo bien acotado es un hallazgo
«Nadie ha publicado un constructo con canales separados más de 200 µm» a la sexta búsqueda no es fallo de
búsqueda: dice que el marco apostó **25×** sobre una inferencia sin experimento, y que la razón de que no
exista es que nadie fabrica litros. · D-543

## 244 · si un problema de arquitectura parece nuevo, comprobar si la biología ya lo resuelve
El 1,44 m² de herida interna de la laminación lo cierra un mecanismo descrito en 1975 —la inosculación— en
48 h y con 2× de margen sobre la isquemia. · D-543

## 245 · antes de buscar una constante por sexta vez, comprobar si es una constante
`s` no cerraba porque no existe: es `2√(2DC₀/q)` y vale 0,10 mm en corazón y 0,95 mm en grasa. Las dos
observaciones del campo que se contradecían eran las dos correctas, cada una para su tejido. · D-544

## 246 · un marco físico es un conjunto de condiciones adimensionales, no una lista de cifras
Hasta ensamblarlas no se ve lo que importa: al hacerlo aparecieron **dos condiciones operando en `N` = 1,00
exacto** porque el diseño se había puesto en su propio criterio, y 24 decisiones anteriores no lo notaron. · D-545

## 247 · un factor CONSTANTE entre dos estimaciones no es error de ley: son dos anclas
El 4,81 ± 2,4 % entre `s` impresa y `s` capilar medida **es el autoensamblaje**, y coincide con el «5× más allá
de la difusión pura» que D-531 había medido por otra vía. · D-546

## 248 · declarar si una longitud es centro a centro o borde a borde antes de usarla
`L = V/s²` exige paso de rejilla. Con canales gruesos la confusión vale 3,6×, y de la definición correcta sale
gratis la condición de imprimibilidad `d_canal ≤ s/2` (50 µm para corazón y riñón). · D-546

## 249 · no se puede medir una ley de composición con un término en saturación
Con colocación de 20 µm sobre arquitectura de 100 µm, `Ω` salió 0,73 y el ajuste dio `r` > 1 — imposible para
una unión. Comprobar que todos los términos están lejos del techo antes de ajustar. · D-547

## 250 · «lo más fino que probé y pasaba» es una cota, no el umbral
Interpolando, la lectura del cuerpo exige arquitectura/**12** y no arquitectura/20: 4,2× menos datos y una
condición que dejaba de estar al filo. · D-547

## 251 · si un muro reaparece en la ruta elegida para esquivarlo, es del problema
El oxígeno mató la impresión tomográfica y vuelve a matar el baño de soporte a 2 L: en las dos el tejido está
vivo y sin perfundir durante horas. `N_O2` = 15–98×. · D-548

## 252 · antes de decir «exige una máquina que no existe», mirar el mayor objeto que ya ha hecho
Un corazón humano a tamaño real (~300 cm³) estaba impreso: la brecha no era de máquina (6,7×) sino de baño
celularizado (7.782×). · D-548

## 253 · comprobar en qué régimen trabaja ya el aparato antes de proponerle uno nuevo
Calculé que imprimir en frío compraría ventana de anoxia, y el baño de soporte **ya es frío por diseño**: el
marco se cobraba un coste que la máquina no paga. · D-549

## 254 · no usar una dimensión de la pieza como proxy de la precisión de la máquina
Tomé canal/2 (50 µm) como precisión de colocación; la platina real da 1,0 µm y la condición pasa. El error era
de 30× y era mío. · D-549

## 255 · un `N` = 1,00 exacto repetido en varios casos suele ser tautología del criterio
`s`/2 = L_Krogh **por definición**, así que «cubre exactamente» no aportaba nada. Lo informativo era el margen
en frío (0,22). · D-550

## 256 · antes de comprar un simulador, comprobar si el problema cabe en un script
La única condición que aún falla se atacó con 60 líneas de numpy: cambió el diseño (perfundir durante la
impresión) y validó el modelo agregado que ya se usaba. · D-550

## 257 · validar el simulador contra dato publicado antes de aplicarlo, y arrastrar su sesgo
El nuestro reproduce las tres criobolsas dentro de 1,20–1,30× con sesgo constante: 20–30 % optimista. Eso deja
el muslo y los hombros **indecididos**, no fallados. · D-551

## 258 · comprobar qué pregunta contesta la geometría montada
Monté una sección 2D creyendo que evaluaba losas y evaluaba **piezas intactas enfriadas por la piel** — una
pregunta que el marco no tenía, y su respuesta cambia la arquitectura. · D-551

## 264 · `V/A` gobierna el enfriamiento sólo con Biot ≪ 1
Limitado por conducción manda el **semiespesor**, y la anchura no interviene. Comprobar el Biot antes de elegir
la longitud característica. · D-558

## 265 · no meter una constante en un script sin traerla de su decisión
Puse una CCR inventada (2,8 en vez de 0,1 °C/min) y la delató un crítico menor que el de partida. · D-558

## 266 · una condición «al filo» puede ser artefacto de convenio, no defecto de diseño
Comprobar en qué convenio se derivó el crítico antes de declarar que el marco opera en `N` = 1. · D-558

## 267 · la exactitud de la máquina no es la del material depositado
Entre una y otra: hinchamiento de boquilla, relajación del baño, gravedad. En baño de esfuerzo umbral manda el
hinchamiento (`Y` = 153, la gravedad no existe). · D-559

## 268 · al apretar una condición, comprobar qué otra se afloja
400 → 33 µm de boquilla arregla la precisión y multiplica el tiempo de fabricación por 147. · D-559

## 269 · una interfaz sin vascularizar es un problema de Krogh, no de cirugía
El hueco de aposición tolerable es `s/2` del tejido más exigente: 50 µm en corazón. · D-559

## 270 · una brecha en volumen esconde su exponente
Si el mecanismo fija una longitud, la brecha real es la raíz cúbica: 7.782× eran **19,8×**. · D-560

## 271 · comprobar si una condición fija una longitud que otra acota
Baño celularizado fija grano de 15–25 µm; la precisión exige 3,3 µm. Se excluyen. · D-560

## 272 · dos magnitudes con las mismas unidades no son la misma magnitud
`τ_y` del baño (15 Pa) y `τ` de lisis en boquilla (5 kPa) difieren en 333×. · D-560

## 273 · un sesgo sistemático no es un error de colocación
Se calibra. Separar sesgo de dispersión antes de escribir un `σ`. · D-560

## 274 · ¿la condición mide el contrato o la ruta elegida?
Un cociente de volúmenes de aparato es **ruta**; una densidad en sitio es **contrato**. · D-561

## 275 · si dos anclas distintas son el mismo número, sospechar
`N` = 1,00 exacto en corazón era densidad cardíaca y densidad de tinta, ambas 5×10⁷. · D-561

## 276 · elegir el modelo animal por lo que el experimento DEJA de probar
El ratón se elige porque 80× de margen térmico impide echar un fallo a la física. · D-562

## 277 · preinscribir las predicciones antes de pedir el experimento a otro laboratorio
Es lo único que hace el marco refutable por terceros. · D-562

## 278 · ¿el techo de una capacidad lo fija un catálogo o la física?
El de densidad celular lo fijan empaquetamiento y lisis; nuestro ancla resultó ser `φ` = 0,21. · D-563

## 279 · dos cifras de literatura sobre el mismo tejido se restringen si comparten fracción volumétrica
Densidad del hígado y diámetro del hepatocito se eligen mutuamente (25 µm da `φ` > 1). · D-563

## 280 · al acercarse al atasco, comprobar qué diverge antes
Krieger–Dougherty lleva el esfuerzo de pared a 17× la lisis antes de que la pasta deje de fluir. · D-563

## 281 · una regla de tres es un proyector con exponente 1 sin declarar
Clasificar la magnitud (intensiva / extensiva / metabólica / frecuencia) y ajustar `b` antes de proyectar. · D-564

## 282 · validar el proyector sobre pares conocidos y publicar su error mediano
El nuestro: **1,20×** sobre ocho pares. Sin ese número, una proyección no es una medida. · D-564

## 283 · tres mecanismos independientes que apuntan a la misma decisión la hacen más fuerte que cualquiera
Térmica, reloj de fabricación y toxicidad convergen en la modularidad. · D-564

## 284 · coherencia y evidencia son ejes distintos y no se suman
La convergencia de mecanismos independientes fortalece lo primero y deja lo segundo en 0 %. · D-565

## 285 · ordenar la validación por coste, no por ambición
El primer peldaño cuesta 500 € y lo podemos hacer nosotros. · D-565

## 286 · un experimento sobre materia vale por la predicción que puede REFUTAR
Si la razón 22/8 sale 2,8 en vez de 7,5, la arquitectura de losas se cae entera. · D-565

## 287 · un parámetro de población no es un parámetro de medio
`Δρ` tiene suelo irreducible de 16 kg/m³: la densidad flotante celular es un histograma. · D-566

## 288 · comprobar qué paso impone cada límite antes de encadenarlos
Confundí el límite del baño (imprimir) con el de la bobina (recalentar): 14 m² que no existen. · D-566

## 289 · cuando un requisito parece importado de fuera, buscar qué lo fuerza antes de quitarlo
El frío profundo lo impone la ventana de fabricación de 5,1 días, no una preferencia. · D-567

## 290 · un requisito de identidad no es un requisito de física
«Sin copia» no cambia ninguna ecuación: cambia qué cuenta como éxito. · D-567

## 291 · lo que no tiene dirección en el contrato no se envía ni se mide: se declara
El agua son 42 kg y 2,5× de canal transportados sin necesidad. · D-568

## 292 · antes de dar un mecanismo por imposible, comprobar si la naturaleza ya lo hace
Supresión metabólica sin frío: anhidrobiosis, demostrada en célula humana. · D-568

## 293 · comparar peldaños por lo que YA se ha hecho, no por lo lejos que parece la meta
V3 nunca se intentó; la anhidrobiosis ya está en célula humana a 5 días. · D-568

## 294 · una exclusión de alcance no es un resultado físico
MIN-RESTORE excluyó encoger materia porque sólo existía Pym. Con mecanismo real se revisa. · D-569

## 295 · procesar POR la vasculatura convierte la distancia del cuerpo en la de Krogh
Valió para el oxígeno (D-550) y vale para el agua: 20,9 días → 20 segundos. · D-569

## 296 · el contrato mide el estado RESTAURADO, no el intermedio
Una deformación intermedia sólo cuenta si es plástica. · D-569

## 297 · cuando una condición se resiste, mirar si algún organismo la tiene resuelta
Tardígrado (valida la cota), pulpo (nombra al culpable), osteoclasto (da el método). · D-570

## 298 · la parte RÍGIDA fija el límite de compresión de un cuerpo blando
El pulpo pasa entero por donde pasa su pico. En el cuerpo humano, el hueso. · D-570

## 299 · transformar mientras el material está en su estado permisivo
Perfundir mientras se imprime, secar por la vasculatura, ablandar mientras se seca. · D-570

## 300 · antes de medir una tolerancia, preguntar si el contrato se mide directamente
El límite elástico era un intermediario innecesario entre el desajuste y `Ω`. · D-571

## 301 · si el resultado no distingue dos cosas que deben distinguirse, el error está en el montaje
Suave y aleatorio dando el mismo `Ω`: faltaba restar el movimiento común. · D-571

## 302 · un umbral medido en un sustrato no es universal
El 1 % de B2 da `A` = 7,00 en tejido cardíaco humano. · D-571

## 303 · una condición de protocolo no se cumple o falla: se diseña
El choque osmótico no es un muro, es un número de pasos (7). · D-572

## 304 · un marco teórico se completa especificando qué contaría como éxito, no consiguiéndolo
La condición discreta tiene criterio (V1–V5) aunque nadie la haya intentado. · D-572

## 305 · si una condición «hereda» un fallo, comprobar que hereda el mecanismo y no el nombre
La trehalosa heredaba Krogh, y lo que fallaba era la partición. · D-573

## 306 · un problema de partición se resuelve con el orden de operaciones
Delipidar antes de cargar trehalosa. El orden ya estaba en el marco por otra razón. · D-573

## 307 · el experimento que hay que hacer es el que puede refutar lo último que se dio por bueno
Aquí: que el campo sea suave, que es lo que la simulación había supuesto. · D-574

## 308 · antes de comprar un experimento, comprobar si otra disciplina ya lo hizo
La ciencia de alimentos tenía media E1-bis medida sin saber que servía. · D-575

## 309 · dos rutas al mismo estado final pueden diferir en todo lo demás
Secar y liofilizar dejan el mismo residuo; una colapsa la arquitectura y la otra no. · D-575

## 310 · «recuperación dimensional» y `Ω` no son la misma magnitud
El 78 % dice que vuelve la forma, no que vuelva la vecindad. · D-575

## 311 · una apuesta no es evidencia por muchos sujetos que tenga
260 criopreservados y 0 revividos aportan cero números: la fuente se descarta. · D-576

## 312 · distinguir «vitrificado físicamente» de «recuperado con función»
3 L contra 1 mL: un factor de 3.000 bajo la misma palabra. · D-576

## 313 · buscar el peldaño más alto que ya existe, aunque esté en otra técnica
EPR-CAT: un humano entero parado y devuelto, a 10–15 °C. · D-576

## 314 · comprobar qué magnitud cambia de verdad entre dos estados
Entre 15 °C y el vidrio no cambia la temperatura: cambia la química. · D-577

## 315 · la mejor búsqueda es la que puede fallarte
Escribir las predicciones antes convirtió una lectura de papers en una medida. · D-577

## 316 · comprobar si una magnitud escala con el tamaño antes de meterla en una brecha de escala
La toxicidad del CPA no escala: la fija `s/2` de Krogh, que es constante. · D-578

## 317 · descomponer una brecha en factores con mecanismo y factor residual
Lo que queda sin mecanismo no es un muro: es un experimento que nadie ha hecho. · D-578

## 318 · un dato tras muro de pago no se redondea a favor
«Protege fuertemente» no es un número: la predicción queda SIN RESOLVER. · D-578

## 319 · buscar quién lo ha intentado antes de contar un factor como «nadie lo ha hecho»
El 33× estaba intentado a 1,35 L; baja a 27×. · D-579

## 320 · anotar cuando un resultado externo confirma una deducción nuestra por otro camino
La carga de CPA no escala con el volumen: Krogh lo deduce, la práctica lo afirma. · D-579

## 321 · fallar por defecto es fallar
Predije 1,5–5× y salió 6–18×: se anota como fallo aunque el resultado favorezca. · D-580

## 322 · una relación dosis-respuesta vale más que un efecto binario del mismo tamaño
Es mucho más difícil de explicar por artefacto. · D-580

## 323 · distinguir DESCONOCIDA por no medida de DESCONOCIDA por PROTEGIDA
La segunda se cierra con una licencia o una réplica, no con un experimento nuestro. · D-580

## 324 · una magnitud que no escala con el tamaño se resuelve UNA vez
Toxicidad del CPA resuelta en riñón de conejo = resuelta para el cuerpo. · D-580

## 325 · una tabla de condiciones no sustituye un experimento: lo convierte en dosis-respuesta
Mismo dinero, resultado mucho más difícil de falsear. · D-581

## 326 · todo experimento de contrato necesita un CONTROL NEGATIVO conocido
Sin un caso que deba fallar, un buen resultado puede ser insensibilidad del instrumento. · D-581

## 327 · una raíz cúbica sobre volúmenes es un supuesto de isotropía disfrazado de aritmética
Comprobarlo antes de construir encima. · D-582

## 328 · lo que importa de un campo de deformación es su ESCALA, no su amplitud
37 % suave sale gratis; 125 % a escala de arquitectura rompe el contrato. · D-582

## 329 · una fuente radiante a distancia mete un gradiente espacial que se confunde con el medido
Para medir un contrato, condiciones uniformes. · D-582

## 330 · clasificar cada condición por si escala con el tamaño antes de diseñar la escalera
En nuestro marco 10 de 13 no escalan: el tamaño sólo es el problema en una. · D-583

## 331 · un experimento GATE se ordena por lo que mata si falla, no por su coste
E1-bis cuesta 100 € y puede matar la ruta entera. · D-583

## 332 · el momento fija cuánto impulso hace falta, no dónde está la masa que lo entrega
Tres localizaciones —cuerpo, vía, extremos— y sólo una es un vehículo. · D-584

## 333 · antes de buscar un argumento exótico, comprobar si uno ordinario basta
La identidad material la rompe el metabolismo (10⁶ recambios), no la cuántica. · D-584

## 334 · «no es medible» y «no se puede garantizar» son cosas distintas
Sin copia lo certifica una cadena de custodia, no un instrumento. · D-584

## 335 · al cambiar de objeto de estudio, recorrer las condiciones una por una
No suponer que el caso más simple es más fácil: aquí mueren seis y nacen dos. · D-585

## 336 · un objeto definido por su diseño no se teletransporta: se fabrica
El problema sólo existe donde la estructura no se deriva del plano. · D-585

## 337 · el suelo del contrato lo pone el objeto, no el aparato
Un objeto que no se reproduce a sí mismo acota su propia `A`. Medirlo antes del acto. · D-586

## 338 · al cambiar de dominio, separar lo que transfiere en DATO y en INSTRUMENTO
Aquí el dato no sirve casi nada; el instrumento sirve entero. · D-586

## 339 · una `A` alta con impostor débil no es un contrato bueno
Comprobar `Ω_imp` antes de leer `A`. · D-587

## 340 · un muro que se quita no desaparece: se muda
Quitar Howells trasladó el suelo de leer a reconstruir. · D-588

## 341 · el kerf es la distancia de Krogh del objeto
Fija una arquitectura mínima (165 µm) independiente del tamaño. · D-588

## 342 · lo que separa teletransporte de fabricación es el origen del fichero
Plano o medida. Por eso la herramienta de fabricación es reutilizable. · D-588

## 343 · precio de acceso y precio de compra difieren en un orden
Declarar cuál se usa: 3,2 k€ frente a 37 k€ en el mismo experimento. · D-589

## 344 · el plazo no es dinero
El camino crítico puede ser un trámite, y entonces no se acorta pagando. · D-589

## 345 · ~~la tolerancia de la unidad entra en `σ` junto a la de la máquina~~ · **ENMENDADA por la 348**
~~El grano de catálogo tiene ±2,5 µm: sube el suelo un 12 %.~~ El ±2,5 µm es **media de lote**: sistemático, se
calibra, y **no suma en cuadratura**. `arq*` vuelve a 307 µm. · D-589, enmendada en D-590

## 346 · un muestreo por tropiezo subestima la población
Si las instancias conocidas se encontraron sin buscarlas, su número no estima el total. · D-590

## 347 · una capa que no pertenece a ningún eje de la clasificación es invisible para ella
Organizar por verbos ocultó el 48 % del marco y el 100 % de lo que no se cierra con dinero. · D-590

## 348 · una tolerancia de lote es sesgo sistemático, no dispersión
Se calibra y no suma en cuadratura. Comprobar si es media de lote o desviación por unidad. · D-590

## 349 · al eliminar la peor condición de un acto, recalcular todas
La que queda arriba suele ser de otra naturaleza, y de una capa que la clasificación no veía. · D-591

## 350 · un porcentaje cuyo denominador no ha saturado no se publica
Si apenas se mueve cuando el denominador crece 70 %, no mide lo que dice. · D-592

## 351 · el número de condiciones es propiedad de la taxonomía, no del problema
`condiciones ≈ 0,19 × pares × dimensiones`. Declarar la taxonomía antes de contar. · D-592

## 352 · toda tasa por unidad se multiplica por el número de unidades, y `ⱎ` = max no perdona ni una
2,42×10⁹ piezas exigen `p` ≤ 4×10⁻¹⁰, dos veces. · D-592

## 353 · la `N` cruda y la `N` tras cierre son magnitudes distintas
Etiquetar cuál se publica. Nos equivocamos los dos en la misma pasada. · D-592

## 354 · la profundidad no es un eje del contrato
Un interior es tan direccional como su superficie: declararlo cuesta la `A` entera. · D-593

## 355 · comprobar que una analogía se aplica al mismo eje
«Lo que no lleva dirección se declara» vale para fases, no para profundidad. Falla por 8×. · D-593

## 356 · dos vías con exigencias opuestas no se cierran a la vez
Derivar exige que la estructura cruce; declarar exige que no cruce. · D-593

## 357 · un marco de más de diez condiciones se mantiene con un motor de anclas, no con una tabla
La tabla se desincroniza sola; el motor no puede. · D-594

## 358 · dos taxonomías del mismo proceso suelen ser la misma a distinta granularidad
Mapearlas cierra la ambigüedad del denominador sin gastar un experimento. · D-594

## 359 · escribir el análisis del veredicto antes de que exista el dato
Y validarlo sobre materia sintética. Aquí cazó un fallo de diseño antes de gastar 3.600 €. · D-595

## 360 · una segunda verificación debe fallar por otra razón Y medir la misma magnitud
La conductividad medía composición mientras el contrato medía disposición. · D-595

## 361 · el techo de lo demostrable lo pone el instrumento de lectura, no el objeto
El error de clasificación del µCT fija `A_max`. · D-595

## 362 · antes de diseñar un experimento, comprobar si alguien ya lo hizo para otra cosa
El acto completo se hace en forense y en museos; falta medirle el contrato. · D-596

## 363 · una desviación en milímetros no es un contrato
Sin suelo y sin impostor no hay `A`, y sin `A` no se sabe si la réplica se distingue de otro objeto. · D-596

## 364 · comprobar si un ancla es función de otra antes de meterla en el jacobiano
Tres de quince lo eran y repartían una influencia que era de una sola. · D-597

## 365 · verificar la atribución de una norma, no sólo su número
El 4:1 era de MIL-STD-45662A, no de ISO 14253. · D-597

## 366 · `(L/arq)³` es el cubo circunscrito, no el objeto
Declarar `f_ocup` o se sobrecuenta 70× en cualquier cosa que no sea un cubo. · D-597

## 367 · comprobar la clase del objeto antes de descargar el dato
Un dataset que compara contra un CAD no puede demostrar teletransporte: su fichero viene de un plano. · D-598

## 368 · verificar todo DOI antes de construir encima
Tres de tres no contenían lo que su descripción decía. · D-598

## 369 · correlación inversa entre apertura de datos y utilidad para el contrato
Quien mide contra un diseño publica; quien mide contra un objeto real, no. · D-598

## 370 · si falta la reconstrucción de un dataset, hacerla nosotros y declararlo
Medida ajena + acto propio siguen dando las tres cifras del contrato. · D-599

## 371 · dos mitades aleatorias de una nube de puntos son un SUELO legítimo
Dos medidas independientes del mismo objeto, y gratis. · D-599

## 372 · `k_muestreo` es propiedad del sustrato, no del contrato
12 histología · 25 granular · 40 hoja. Llevarlo como ancla por sustrato. · D-599

## 373 · un descriptor de ocupación mide forma Y cobertura
Para superficies, usar distancia al vecino más próximo. · D-600

## 374 · si una validación da un factor absurdo, sospechar del instrumento antes que del dato
110× no era ruido de medida: era mi descriptor. · D-600

## 375 · el suelo por mitades aleatorias subestima el real en 2,0×
Medido contra dos escaneos físicos. Proxy utilizable si se declara y se corrige. · D-600

## 376 · al corregir un observable, recalcular TODO lo medido con él
No sólo lo que saltó. Dejé el acto un día sin rehacer. · D-601

## 377 · «no existe» y «no lo he construido» no son lo mismo
Tres de los cinco criterios que di por inalcanzables eran una tarde de código. · D-602

## 378 · el exponente de la curva tasa–distorsión mide la dimensión efectiva del objeto
Superficie → bits ∝ `k²`. Por eso la cáscara es barata. · D-602

## 379 · una resolución que se cuantiza a un entero de píxeles no mide por debajo de dos píxeles
Comprobar el tamaño de bloque efectivo antes de leer un cruce. · D-603

## 380 · si una medida no se resuelve hoy con el mismo dato, nunca estuvo medida
El 12 de D-547 estaba en el escalón donde la medida se agota. · D-603

## 381 · si una medida se agota por cuantización, cambiar el operador antes de comprar dato
Una gaussiana de `σ` continuo mide donde un bloque entero de píxeles no llega. · D-604

## 382 · una meseta puede ser cuantización o suelo de ruido, y sólo una invalida la medida
Comprobar cuál antes de descartar. · D-604

## 383 · `A` = 0,56√(`a`/`s`) no contiene el número de piezas
Añadir unidades no compra contrato: compra factura. · D-605

## 384 · quien elige el espaciado de lectura elige la `A` que publica
Preinscribir `s`, o `A` es una elección disfrazada de resultado. · D-605

## 385 · leer más fino de lo que el colocador alcanza MATA el acto
El suelo lo pone el lector. Degradar la resolución a propósito: `σ` ≤ `s`/10. · D-605

## 386 · el exponente de los bits es la dimensión MÁS 1/ln k
Para leer una dimensión, contar celdas, no bits. · D-605

## 387 · `Ω_d` depende de la densidad de muestreo
Suelo y acto a la MISMA densidad, o el margen es ficticio. · D-605

## 388 · un objeto discreto se lee RETIRANDO: el kerf es cero porque la unidad es el vóxel
Sólo los objetos continuos pagan kerf. · D-606

## 389 · una lectura sin kerf lo cambia por recuento de lecturas
`(fracción perdida) × (resolución en z)` = kerf. No se esquiva. · D-606

## 390 · si la `A` sube y el impostor no se mueve, la ganancia es densidad, no cobertura
Y por la regla 385 encarece el acto. · D-606

## 391 · un impostor SATURADO en 1,000 tampoco mide · extiende la 339
Comprobar `Ω_imp` por los dos extremos antes de leer `A`. · D-606

## 392 · dos fuentes con instrumentos distintos pueden acertar las dos y medir pasos distintos
Leer los métodos antes de retirar un nombre. · D-607

## 393 · un dataset publicado contiene más pasos del acto de los que anuncia su resumen
Mirar qué midieron con qué, paso por paso. · D-607

## 394 · un criterio que el propio suelo no puede cumplir está mal escrito
`Ω_acto` ≥ `Ω_suelo` idénticamente: el umbral es (1+δ)·mediana con δ preinscrito. · D-608

## 395 · con unidades idénticas, barajar etiquetas es la identidad
Un control negativo por permutación es un falso positivo perfecto. · D-608

## 396 · lo que se pueda hacer aritmético no se deja en evidencial
Si el fichero sólo se escribe cuando la balanza confirma la retirada, la custodia deja de prometerse. · D-608

## 397 · la ceguera se compra con ANCHO DE BANDA, no con protocolo
Un periférico que no puede mostrar el dato no puede filtrarlo. · D-608

## 398 · ~~`Ω` mide disposición, no inventario~~ · **RETIRADA en D-611**
~~Un subconjunto está entero sobre la superficie original.~~ **Falso: modelé la pérdida como decimación
uniforme. Una unidad perdida es un trozo CONTIGUO, y el p99 la detecta a 7,4× del umbral.**

## 399 · todo contrato de disposición necesita un acompañante que CUENTE · **enmendada en D-611**
No porque `Ω` no vea la pérdida —sí la ve— sino porque la báscula la ve **por vía independiente** y además
dice **cuál** unidad falta. · D-609, enmendada

## 400 · probar el criterio contra los modos de fallo de la MATERIA antes de comprar
Aquí reveló que dos de cuatro son invisibles, y eso cambia la lista de la compra. · D-609

## 401 · ninguna corrección global quita un residuo de pose
Si dos medidas ven superficies distintas, hay que fijar la geometría en hierro. · D-610

## 402 · una prueba que no decide la pregunta vale si descarta un modo de fallo
Declarar antes qué acota y qué no. · D-610

## 403 · perder una unidad es quitar un trozo CONTIGUO, no decimar · sustituye a la 398
Un modelo que tira puntos sueltos da una ceguera que no existe. · D-611

## 404 · una regla incumplida dos veces en cuatro decisiones hay que meterla en el CÓDIGO
La 387 (suelo y acto a igual densidad) no puede vivir en una lista. · D-611

## 405 · un cono no es un asiento cinemático
Apoya en una circunferencia y lo fija el rozamiento. Tres puntos repiten a decenas de nm. · D-612

## 406 · un error entre dos estaciones no hay que hacerlo pequeño: hay que hacerlo COMÚN
Mismo programa, mismo material, mismo lote — y se cancela en `Ω`. · D-612

## 407 · si el objeto es discreto por construcción, leer pasa de metrología a clasificación
El instrumento baja tres órdenes de magnitud. · D-612

## 408 · todo mecanismo que garantiza una condición por construcción la retira de lo demostrado
`N` mejora y la evidencia empeora. Declararlo antes de montarlo. · D-612

## 409 · si las unidades tienen forma conocida, leer no es metrología: es ajuste de parámetros
Baja tres órdenes de magnitud de precio. · D-613

## 410 · ajustar el MODELO físico, no una superficie genérica
Cuatro parámetros con sentido baten a diez libres por 28×, con menos datos. · D-613

## 411 · un sesgo determinista no se mide: se calcula y se resta
El de la silueta de una esfera vale exactamente `1/(1 − R²/D²)`. · D-613

## 412 · antes de comprar precisión, mirar si la geometría la regala
Alejar la cámara 3× baja el sesgo de silueta 9× y cuesta un trípode. · D-613

**413** · El suelo de una máquina se mide **volviendo a colocar**, no volviendo a fotografiar.
Repetir la medida deja fuera el error del actuador, el suelo sale cero y **todo acto falla**.
El suelo tiene que recorrer el mismo camino físico que el acto, menos lo que se quiere aislar.

**414** · Un δ preinscrito **sin preinscribir n no significa nada**. Ω es la mediana de n
distancias y su ruido va como 1/√n: con n = 25 hace falta δ = 0,61 y con n = 200 basta 0,18.
δ no se elige: **se mide de la dispersión del propio suelo**.

**415** · Cada estadístico se juzga **contra su propio suelo**. Comparar el p98 del acto con la
mediana del suelo es comparar inconmensurables (D-363): el p98 de una Rayleigh vale 2,8 veces su
mediana, así que ese test **no puede pasar nunca**.

**416** · Emparejar por orden **falla cuando lo que se ordena es lo que se va a medir**. Los
fiduciales no se pueden ordenar por coordenada para calibrar la distorsión, porque la distorsión
los desordena. Se emparejan por **proximidad** al patrón nominal.

**417** · `A` **no depende de n**, sólo de `a/σ`. Y la constante no había que ajustarla:
`A = K_d·√(a/σ)` con `K_d = √((ln2/V_d)^(1/d) / c_d)` da **K₃ = 0,597** contra el **0,56 que D-605
midió**. Llevábamos desde D-605 usando como empírica una ley que era deducible.

**418** · **El tamaño de la unidad está en el NUMERADOR.** Ir más fino **empeora** el contrato:
con σ = 25 µm, la unidad de 100 µm da A = 1,19 y la unidad celular de 10 µm da **A = 0,38 — el
contrato deja de existir**. La intuición de que más resolución es mejor está invertida.

**419** · `n` no entra en `A`, pero entra en **δ**, y por ahí **fija el acuerdo entre estaciones**:
`ε ≤ σ√(2δ)` con `δ ∝ 1/√n`. Con n astronómico el acto tiene que igualar al suelo casi
exactamente. Es un requisito que no aparece por ninguna otra vía.

**420** · Cuando dos leyes tienen **exponentes de signo opuesto** sobre la misma variable, hay
**óptimo**, y hay que calcularlo antes de fijar la escala. El contrato va como `√a` y la ruta del
agua como `a²`: el óptimo está en 408 µm y no lo había buscado nadie.

**421** · Una DESCONOCIDA que «exige materia» puede cerrarse por **literatura** si alguien la midió
para otra cosa — pero **sólo después de traducirla a magnitud adimensional**. El rTRE de registro
histológico está normalizado por la diagonal de la imagen y nuestra Ω por la escala del objeto:
compararlos crudos es la trampa de D-363. La traducción correcta es `σ_residual = strain_local × a`.

**422** · **Cerrar un hueco puede destapar que no era el cuello.** La liofilización llevaba desde
D-575 marcada como la DESCONOCIDA decisiva; medida contra su presupuesto aporta 4–9 µm de 17, y el
que manda es la colocación. Un hueco abierto mucho tiempo **acumula importancia que no ha ganado**.

**423** · Cuando un ancla es DECLARADA y existe literatura que la mide, la literatura **gana**.
σ = 25 µm era un ancla del motor; hay ±14 µm **medidos** sobre esferoides de 200–250 µm, que es
nuestro régimen de unidad. El ancla sube de DECLARADA a LITERATURA y `A` sube con ella.

**424** · **`φ` no se exige al objeto, se exige a cada unidad según su CLASE.** La identidad
material fue rechazada como criterio global (el metabolismo la rompe), pero dejarla libre convierte
teletransporte en fabricación. La clase decide: clase 1 admite `φ` = 0, clase 2–3 exigen `φ` = 1.

**425** · **LEER no es ENVIAR.** Son dos canales distintos y la razón entre ellos la fija `φ`: con la
materia viajando, la unidad **es** su propia descripción y sólo se envía su pose. Comparar un dato de
lectura con uno de envío es otra inconmensurabilidad.

**426** · **Clase 2 fuerza `φ` = 1 por ancho de banda, no por filosofía.** Sin catálogo del que sacar
la forma, describirla cuesta 629.000× más que llevarla. La exigencia de «sin copia» y la de «clase 2»
son la misma, y ninguna es ideológica.

**427** · **La precisión de un asiento cinemático exige una unidad DISEÑADA, y una unidad diseñada es
clase 1, donde el acto no prueba nada.** Precisión y valor probatorio tiran en sentidos opuestos, y
se reconcilian metiendo la unidad de clase 2 **dentro de un portador de clase 1**.

**428** · Con `g` = 6 el asiento de 3 puntos **no basta**: 3 restricciones para 6 grados. Hace falta
un acoplamiento de **Maxwell** — 3 bolas en 3 ranuras en V, 6 contactos, exactamente determinado.

**429** · **Un destino con repuestos es un fax.** Si en B hay unidades intercambiables, «la unidad
correcta en la dirección correcta» no se puede ni plantear, y el contrato certifica igual un acto en
el que **todas** las unidades están en el sitio equivocado. Medido: la disposición pasó el control
permutado (0,00128, bajo umbral) con **25 de 25** unidades en dirección ajena.

**430** · Con `φ` = 1 aparece un criterio que con `φ` = 0 **no existe**: la **IDENTIDAD**. No es
disposición (dónde hay algo) ni inventario (cuántos hay), sino **quién está dónde**. Es el único de
los cinco que distingue teletransporte de fabricación, y sólo es comprobable si las unidades son
distinguibles.

**431** · **Ni fax ni envío.** La materia viaja **sin orden** y el orden viaja **sin materia**, por
caminos separados, y se recombinan en destino. Si sólo se empaquetara el objeto no habría nada que
certificar; si sólo viajaran los bits, haría falta repuesto.

**432** · **Proteger la carga y destruir el orden son exigencias opuestas.** Si las unidades viajan
sujetas en una bandeja que conserva sus posiciones, la disposición viaja con la materia y el acto
vuelve a ser un envío. Se reconcilian con **alvéolo genérico + orden de retirada sorteado**.

**433** · **La misma pieza que da la precisión da la protección.** Sujeta en su asiento cinemático la
unidad fluye a 109 g; suelta en una caja fluye a 3 cm de caída. **La diferencia es la tapa.**

**434** · Un canal lateral hay que **contarlo en bits y cerrarlo**. El orden de la revista son
`log2(n!)` bits —84 con 25 unidades, el 0,7 % del acto— viajando por fuera del canal declarado.

**435** · **Un dato de entrada supuesto hay que triangularlo antes de concluir con él.** Puse el
coeficiente de Archard en 10⁻⁴ y la literatura lo lleva hasta **10⁻¹** para acero seco: mil veces
más. La conclusión aguantó, pero la aguanté por suerte, no por método.

**436** · **`ψ` = fracción de la información estructural que cruzó por el canal** = `g·(σ/a)²`, y
está acoplada al contrato por `ψ = g·K⁴/A⁴`. **Mejorar `A` hace el acto más trivial a la cuarta
potencia.** `A` sola no basta para juzgar un acto: llevada al límite certifica una caja cerrada.

**437** · **`A` > 1 con unidades de clase 2–3 ⟹ `φ` > 0: la materia viaja.** El contrato existiendo
**obliga** al transporte físico; no es una elección de diseño. *(Segunda derivación independiente de
la regla 426, que salió del ancho de banda.)*

**438** · **`n` = 1 no tiene disposición.** `Ω` entre dos lecturas de un sólido rígido es cero por
construcción: no hay acto que certificar. Una cabina no es un teletransporte, es una caja.

**439** · **Lo único que puede ir a `c` es la información.** Certificar cuesta velocidad: en la
frontera `A` = 1 más de la mitad del objeto va por carretera, y con margen defendible el 99,8 %.

**440** · **Una traslación rígida de TODO el objeto no es un fallo de teletransporte.** `Ω` tiene que
cocientar el movimiento rígido antes de juzgar. La nuestra centra pero no quita rotación ni escala —
y la distorsión de lote común es dominantemente **escala**. Gastábamos presupuesto en lo que no
contaba.

**441** · **Aflojar un test bajando `n` por test NO es una ganancia: es bajar la potencia.** Si un
esquema «mejora» porque el estadístico se vuelve más ruidoso, es trampa al solitario. La ganancia
legítima viene de quitar lo que no era un fallo, no de dejar de verlo.

**442** · **Alineación afín LOCAL: el residuo de un campo suave cae como `(r/L)²`, no como `r/L`.**
Quitar constante + lineal dentro de cada trozo deja sólo el cuadrático.

**443** · **`ψ` no es un eje.** `ψ = g·K⁴/A⁴`: depende sólo de `a/σ`, igual que `A`. **El eje
independiente que separa un acto de una caja cerrada es `n`** — la cabina tiene la misma `A` y la
misma `ψ` que la máquina, y `n` = 1.

**444** · **Un gate envejece con la arquitectura.** El GATE-0 de D-610 medía dos escáneres contra
tres fiduciales; desde D-612 no hay escáneres. **Antes de correr un experimento preinscrito hace
tiempo, comprobar que sigue preguntando lo que hoy decide algo.**

**445** · **Validar el instrumento sobre casos de respuesta CONOCIDA antes de aplicarlo al caso
desconocido.** El estimador de `α` se probó sobre gradiente, paseo aleatorio y ruido independiente,
y recuperó 1,00 / 0,49 / 0,01. Sin eso, un `α` medido no significa nada.

**446** · **Más muestras no siempre bajan el error.** `σ_α` se satura en 0,15 porque los pares de
puntos **no son independientes**: salen todos de `n` puntos, así que el tamaño efectivo es `n`, no
`n²`. Bajar de ahí exige repeticiones independientes, no más fiduciales.

**447** · **La física externa no certifica un interior.** Masa, centro de masas, tensor de inercia y
espectro vibracional son ~31 ligaduras contra 10⁸ grados de libertad: razón 4×10⁻⁸. Lo que no se
lee **sólo lo avala la custodia**, y la custodia se mide en bits, no en confianza.

**448** · **Un sello intacto prueba que está intacto AHORA, no que no se abrió y se rehízo.** La
custodia de extremos y la custodia continua **no son la misma garantía**.

**449** · **Antes de comprar un experimento, preguntar qué MÁS mide el mismo montaje.** GATE-0 pedía
un solo número y los mismos ficheros dan tres: el exponente, **la amplitud** (que es el acuerdo
absoluto) y **la repetibilidad del lector**. Dos de las tres eran gratis y no estaban pedidas.

**450** · **Que un modelo de pocos parámetros ajuste muchos puntos ES una medida de suavidad.** El
error volumétrico se describe con **21 parámetros sobre 200–400 puntos medidos**: eso fija una
longitud de correlación de `L`/2,76 = 616 mm, y nuestros padres de 100 mm caben 6× dentro. **`α` = 1
no es una esperanza: es lo que predice el modelo que la industria usa a diario y que funciona.**

**451** · **El `n` mínimo no es filosofía: son ligaduras.** Tras quitar el movimiento rígido quedan
`d·n − d(d+1)/2`, y cada una aporta `log2(a/σ)` bits. Con `n` = 1 o 2 el número es ≤ 0: **el acto es
vacío**. Baremo no arbitrario —igualar los 1.024 bits del sello— da **`n` ≥ 49 en 3D, 73 en monocapa**.

**452** · **Para el tamaño de unidad no hay óptimo, hay TECHO.** `A` crece como `√a` y la evidencia
cae como `a⁻³`: no se cruzan en un pico, se cruzan en un límite. **La burbuja más grande que aún
certifica.**

**453** · **La custodia se mide en bits × COBERTURA TEMPORAL.** Un sello de 1.024 bits que sólo habla
del instante de llegada cubre medida nula del intervalo; un testigo irreversible de **1 bit** cubre
`[0,T]` entero. Y un testigo sirve sólo si es **irreversible** y vive **dentro** del volumen sellado:
un sello se rehace, una reacción química no.

**454** · **Antes de declarar un problema abierto, comprobar si es el problema que tenemos.** Traté
la custodia continua como criptografía —demostrar que nadie abrió y rehízo— cuando en este marco el
impostor **no es un saboteador**, es una dirección equivocada. Reencuadrada como física, se resuelve
con 2 €.

**455** · **«No se puede calcular más» es la versión perezosa de «no existe».** Cuatro condiciones que
declaré techo eran magnitudes que la industria mide a diario: acoplamientos cinemáticos (Slocum),
centroide subpíxel (fotogrametría), repetibilidad ISO 230-2 y choque en transporte. **Todas cerradas
por literatura en una ronda.** La regla 377 otra vez, y esta vez me la recordó el investigador.

**456** · **El error de PERPENDICULARIDAD es lineal en la posición POR DEFINICIÓN.** Un desescuadre
de `ε` radianes desplaza `ε·r`. Para ese término `α` = 1 **exacto**, no aproximado: no es un supuesto
sobre el campo, es lo que el término significa.

**457** · **Un criterio ya construido puede estar dando gratis lo que se iba a comprar aparte.** Los
bits de custodia no necesitan un PUF dedicado: **el criterio de IDENTIDAD ya es uno** — 50 diámetros
únicos medidos a 0,5 µm dan **728 bits** con el hardware que ya está.

**458** · **Un porcentaje único supone que si falla, falla para siempre.** Hay que partir las
condiciones en **SISTEMÁTICAS** (propiedad del mundo · no las mueve nada), **HARDWARE** (las mueve el
dinero) y **ESTOCÁSTICAS** (las mueve repetir). Sin esa partición, el número miente en los tres
sentidos a la vez.

**459** · **La repetición SATURA.** Lo estocástico se agota en **3 intentos**; a partir de ahí repetir
es tiempo tirado. Saber cuándo parar de repetir vale tanto como saber empezar.

**460** · **Un techo calculado con `n` continuo no es un techo con `n` entero.** El «techo» de 33,8 cm
daba 1.024 bits con `n` real y **988 con `n` = 25**: no llegaba. Redondear a la baja puede cruzar el
umbral que el cálculo decía tocar.

**461** · **La misma evidencia se alcanza por rutas opuestas:** muchas ligaduras pobres (objeto: 144 ×
9,5 bits) o pocas ricas (burbuja: 72 × 14,3). **Eligen distinto en masa, tiempo y ancho de banda**, y
el porcentaje solo lo escondía.

**462** · **Una condición copiada de un marco a otro hay que re-justificarla, no heredarla.** `α`
entró en D-621 para salvar el acuerdo del HUMANO y yo la dejé copiada en las condiciones del OBJETO,
que **pasa con 19× sin jerarquía ninguna**. El objeto nunca necesitó `α`.

**463** · **`D(r)` de cualquier campo acotado SATURA.** Crece por debajo de la longitud de
correlación y se aplana por encima: `α` = 1 sólo vale **dentro** de `L_c`. Medido sobre dos escaneos
reales: `α` ≈ 0,3–0,7 por debajo de 1 m y **α ≤ 0 por encima**. Mi «`α` = 1 siempre» era un modelo
sin longitud de correlación.

**464** · **El TIEMPO DE EJECUCIÓN es una condición, y no estaba en ninguna lista.** Con `n` = 10⁹
unidades a 1 kHz —más rápido que cualquier pick-and-place real— el acto humano tarda **12 días**, y
exige **p < 6,7×10⁻¹⁰ de fallo por operación** para tener un 50 % de terminar. La industria está en
10⁻⁵–10⁻⁶: **faltan 3–4 órdenes**. `n` no sólo fija δ y el acuerdo: **fija el reloj y la fiabilidad.**

**465** · **Una tabla de materiales puede ser UNA SOLA condición disfrazada.** Las siete filas de
escala cumplían `N × arq` = 303 constante: no eran siete materiales, eran **la precisión de
colocación evaluada en siete sitios**, con el σ del demostrador viejo. Antes de tratar una tabla como
datos independientes, **comprobar si el producto de sus columnas es constante**.

**466** · **Las condiciones transversales escalan con `n`, y por eso no son transversales.** Acuerdo,
tiempo y fiabilidad **pasan holgadas con `n` = 50 y fallan las tres con `n` = 10⁹**. No son un fallo
del método: **son un fallo de `n`.**

**467** · **Antes de correr un experimento, mirar en qué verbo cae cada medida.** Las seis medidas
del PREREG-E1BIS caen **enteras** en COMPRIMIR y RESTAURAR — los dos verbos que objeto y burbuja no
usan. **Validan el marco humano y no aportan ni un dato a las cuatro arquitecturas.**

**468** · **El trozo más grande que se puede mover no lo fija la biología: lo fija `n_min`.** Todo
empuja a trozos grandes —`A` sube, las interfaces cortadas bajan como 1/a, y acuerdo, tiempo y
fiabilidad mejoran con `n` bajo—. Lo único que empuja a trozos pequeños es **la evidencia**, y de ahí
sale el tamaño: `a = (V/n_min)^(1/3)`.

**469** · **Cuando un muro físico cae, suele dejar en su sitio un muro LOGÍSTICO.** El arranque de
3.610× desaparece a escala de órgano, y lo que queda no es física sino **cuántos quirófanos hay a la
vez**: 490 h de microcirugía contra 24 h de perfusión = **21 equipos en paralelo**.

**470** · **Trocear a la escala del contrato y trocear a la escala de la función son cosas distintas,
y la buena es la segunda.** A 408 µm el cuerpo son 10⁹ trozos y las tres transversales fallan; a
11 cm son 49 y **las tres pasan**. La escala no se hereda del observable: **se elige**.

**471** · **Si todas las revisiones mueven el número en el mismo sentido, el sesgo está en el
revisor.** En esta sesión las cinco correcciones que tocaron las cuatro arquitecturas subieron, y las
tres que bajaron cayeron **todas** en el marco humano. Ninguna justificación individual explica ese
patrón: hay que auditarlo aparte.

**472** · **Lo verificado en un banco propio, con un verificador propio y un modelo propio, lleva
DESCUENTO POR CIRCULARIDAD.** Un fallo del modelo no aparece en ninguno de los tres. Y no es
hipotético: D-626 demostró que nuestro banco produce **falsos fallos** — luego puede producir falsos
aciertos.

**473** · **Una etiqueta no puede cambiar de definición a mitad de análisis.** «Iterando» pasó de
«+0,15 por condición» a «3 intentos + 274 €» sin avisar, y el mismo nombre significó dos cosas. Se
fija la definición **una vez** y se mantiene.

**474** · **Justificar el marco no es justificar la pieza.** El reencuadre de la custodia continua
—el impostor es una dirección equivocada, no un saboteador— está bien fundado; el indicador de
oxígeno que lo implementa **no lo ha probado nadie aquí**. Las dos cosas se puntúan por separado.

**475** · **Un porcentaje se da como INTERVALO, y el ancho es lo que compra el experimento.** El
punto único esconde de qué depende.

**476** · **Un fallo RUIDOSO no cierra una vía: encarece una tirada.** Si al fallar la condición el
contrato lo dice —el suelo sube, `Ω` sube, el acto falla— te enteras, lo arreglas y repites. **Sólo
los fallos SILENCIOSOS**, los que pueden dar un falso aprobado, **matan la arquitectura.** Puntuar
los ruidosos como si cerraran la vía infravalora el conjunto: aquí eran **5 de 8**.

**477** · **La evidencia acumulada del programa hay que POOLEARLA, no reusar la última.** La ley
`A = K√(a/σ)` no se apoya en una cosa: forma cerrada derivada · coincidencia con el 0,56 medido sin
ajustar · simulación a 3 cifras en dos dimensiones · **tres sustratos reales ajenos** · y D-370, que
certifica igual en corazón humano que en nervioso. **Cinco vías independientes puntuadas como una.**

**478** · **Contar los DETECTORES, no las condiciones.** El inventario tiene tres vías independientes
(p98, recuento, báscula), la identidad dos (diámetro óptico, masa) y la custodia cuatro. Una
condición con tres detectores independientes **no es un punto único de fallo**.

**479** · **Los dos límites de un intervalo contestan preguntas DISTINTAS**, y hay que decir cuál.
Pesimista: *¿funciona este montaje a la primera, descontando lo verificado en casa?* Optimista:
*¿es sólida la arquitectura, arreglando lo que falle ruidosamente?* Un argumento que mueve uno **no
tiene por qué mover el otro** — y aquí no lo movió.

**480** · **Un programa con predicciones preinscritas y puntuadas PUEDE CALIBRARSE CON SU PROPIO
HISTORIAL.** El nuestro: **147 predicciones, 100 aciertos, 68 %**. Eso fija el prior de que una
derivación mía sea errónea (**32 %**), y con él la posterior de una ley que ha sobrevivido a `k`
contrastes independientes. **Deja de haber probabilidades puestas a ojo.**

**481** · **Una tasa de acierto del 68 % corta en los dos sentidos y hay que decir los dos.** En
contra: ninguna derivación no contrastada vale más de 0,68. A favor, y es más fuerte: **un método que
encuentra 47 predicciones fallidas de 147 está probando de verdad**, y lo que sobrevive a ese régimen
vale mucho más que lo que nunca se sometió a él.

**482** · **«Sintético» no es lo mismo que «propio».** Descontaba los 5 criterios por sintéticos
cuando el veredicto a ciegas **8/8, p = 2,5×10⁻⁵, fue sobre dato de TERCEROS** descargado de
Sketchfab. Lo sintético son el lector y el colocador; **el contrato ya se probó sobre materia ajena.**

**483** · **Nunca heredar un valor numérico entre turnos: recalcular la tabla entera.** En D-633
dejé hardcodeado un pesimista viejo y «a la primera» saltó de 20 % a 60 % sin ninguna justificación.
Un número que no se recalcula **deriva en la dirección que le conviene al que escribe**.

**484** · **LEER el interior y DIVIDIR el interior son exigencias distintas, y sólo la segunda es
obligatoria.** Nuestra máquina lee posición y diámetro de 50 bolas y **no mira dentro de ninguna**:
el interior viaja sin describirse. **Leer nunca fue un requisito del acto. Dividir sí.**

**485** · **`n` = 1 no da un acto débil: no da acto.** Las ligaduras certificables son `3n − 6`, y con
`n` = 1 valen **−3**. Un sólido rígido tiene 6 grados y los 6 se van en la alineación: **cero
ligaduras, nada que certificar.** No lo arregla ninguna tecnología, porque no es un límite de
instrumento: **es contar grados de libertad.**

**486** · **Un contrato sólo vale lo que vale su impostor.** Los nuestros han sido fáciles —
direcciones al azar, unidades permutadas, otro ejemplar—. **El homólogo contralateral es el impostor
más duro que existe en la naturaleza**: mismo organismo, mismo tipo, misma vecindad, **generado por
el mismo programa de desarrollo en espejo**. Una banda `A` medida sólo contra impostores cómodos
**está inflada y no se sabe cuánto.**

**487** · **La posición de un soma NO es una dirección.** Medido sobre FlyWire: la dirección vecina
**equivocada** está **7,8× más cerca** que el homólogo correcto. Miles de tipos celulares comparten
sitio; la identidad está en la arborización, no en el soma. **Un espacio sólo tiene direcciones si
`a/σ` > 1 medido contra el VECINO EQUIVOCADO MÁS PRÓXIMO**, no contra un barajado.

**488** · **Una ley que también predice bien cuando dice que NO se puede es una ley.** `A = K√(a/σ)`
predijo **0,359** sobre FlyWire y se midió **0,359** — tercera cifra, dato ajeno, impostor duro, y en
un régimen donde el contrato **no existe**. Es la confirmación más exigente que ha tenido.

**489** · **La cancelación en modo común exige HISTORIA común, no sólo lote común.** Dos bandejas del
mismo programa CNC dejan de estar correlacionadas cuando una pasa ocho meses a −60 °C y 0,38 g: la
dilatación sola da **368 µm** contra un presupuesto de 7,9. **En destino lejano, el modo común se
repone con control térmico (≤ 0,5 K) o no existe.**

**490** · **Un testigo de custodia sellado en atmósfera inerte es INCOMPATIBLE con un ocupante vivo.**
El indicador de O₂ se dispara solo si dentro hay alguien respirando. Se arregla con **dos cáscaras** y
el testigo en el hueco — pero es un **rediseño**, no un detalle. *Toda pieza de custodia hay que
contrastarla contra lo que la burbuja lleva dentro.*

**491** · **INSTANTÁNEO y CERTIFICADO son mutuamente excluyentes.** Instantáneo exige `φ` = 0, que
exige describirlo todo (`ψ` = 1), que da `A` = `K·g^(1/4)` < 1: **no hay contrato.** No es una
limitación de esta época ni de esta máquina — es la identidad de D-620 escrita en el eje del tiempo.

**492** · **El teletransporte instantáneo existe, es trivial, y sólo vale para CLASE 1.** Si la forma
está en un catálogo, describirla cuesta un número de referencia: se manda el código, llega a `c`, y
en destino lo sacan del almacén. **Se llama pedir la pieza.** Lo que no puede ir a `c` es clase 2–3
— y un humano es clase 3.

**493** · **El valor del acto nunca fue el reloj: era poder DESMONTAR.** Un envío ordinario exige que
el objeto llegue montado. El acto permite secarlo, trocearlo o perfundirlo, destruir el original con
acta y reconstruir en destino **con banda medida**. Esas tres cosas un camión no las da.

**494** · **El tiempo del ACTO no depende del interior: sólo de `n`.** Leer, colocar y verificar
escalan con el número de unidades. Lo único que el interior toca es el **transporte**, y sólo por la
**masa** — que es un observable exterior que la báscula ya mide. *En trayectoria de Hohmann ni eso:
el reloj es mecánica orbital y no sabe lo que lleva la nave.*

**495** · **Lo que el tiempo necesita saber del interior se DECLARA, no se lee** *(regla 291)*.
Cuánto aguanta de choque y cuánto aguanta de tiempo son **declaraciones del que carga**, como el
contenido de un contenedor. **El sistema no lo comprueba abriendo: lo comprueba VIGILANDO** — el
acelerómetro y el testigo son observables exteriores.

**496** · **Un ocupante vivo introduce un BUCLE que la carga inerte no tiene:** más tiempo pide más
provisiones, que piden más masa, que dan menos delta-v, que dan más tiempo. Se cierra con **un solo
número declarado**: los kg/día del ocupante.
