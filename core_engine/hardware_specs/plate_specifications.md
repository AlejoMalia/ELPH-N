# PLANO · máquina universal de teletransporte de objetos

**Una sola máquina.** Las dos estaciones son **idénticas**: la que recibe puede enviar. No hay
"emisor" ni "receptor", hay **estaciones** y un sentido de marcha que se elige en el software.

---

## 1 · Alzado de una estación

```
                    ^ z
                    |
   ┌────────────────────────────────┐
   │      CAMARA  (sensor 1")       │   <- mira hacia ABAJO, eje vertical
   └────────────────┬───────────────┘
                    │
                    │   L = 1.500 mm   <- NO es arbitrario: el sesgo de silueta
                    │                     cae como 1/L2 (65 um a 300 mm,
                    │                     0,03 um a 1.500)
        columna     │
        de perfil   │
        40x40 mm    │
                    │
   ════════════════ │ ═══════════════   <- PLANO DE TRABAJO  z = 0
   ┌────────────────┴───────────────┐
   │  BANDEJA   200 x 200 mm        │      placa CNC, 10 mm, aluminio
   │  · 9 fiduciales grabados       │      mismo programa, material y lote
   │  · 25 asientos de 3 puntos     │      que la otra estacion  <- CLAVE
   └────────────────────────────────┘
   ┌────────────────────────────────┐
   │  DIFUSOR  +  PANEL LED         │   <- RETROILUMINACION. El objeto se ve
   └────────────────────────────────┘      como SILUETA NEGRA sobre blanco:
                                            SNR alto gratis, y mata el brillo
   ┌────────────────────────────────┐      especular del cromado
   │  BASCULA  0,001 g              │   <- enclavamiento de masa (D-608)
   └────────────────────────────────┘
```

## 2 · Planta de la bandeja

```
   +--------------------------------------------------+  200 mm
   | (F)              (F)              (F)            |   F = fiducial grabado
   |                                                  |       diam 4 mm, paso 85 mm
   |      o    o    o    o    o                       |
   |                                                  |   o = asiento de 3 puntos
   |      o    o    o    o    o                        |      paso 2 mm en rejilla
   | (F)              (F)              (F)            |       -> leer es CLASIFICAR,
   |      o    o    o    o    o                       |          no medir (D-612)
   |                                                  |
   |      o    o    o    o    o                       |
   |                                                  |
   | (F)  o    o    o    o    o       (F)        (F)  |
   +--------------------------------------------------+
        \_______________ 25 sitios _______________/
```

## 3 · El asiento de 3 puntos · la pieza que sustituye al nido de conos

```
   vista en planta          seccion

      .  120º  .             bola
     .         .            (  )
    (P)-------(P)          __||__
      \       /           P      P      tres esferas de 3 mm a 120º
       \     /            ^      ^      la bola apoya en TRES PUNTOS:
        \   /             |      |      el centro queda determinado
         (P)              acero templado
```

**Por qué no un cono:** una bola en un cono apoya en una **circunferencia** — está
sobredeterminada, y quien decide dónde para es el rozamiento. Tres puntos fijan el centro
**exactamente**. Por Hertz repite a **8–14 nm**, margen 71×. Coste **79 €** contra 1.500–5.000 €
del nido de conos de catálogo.

## 4 · Qué cruza entre las dos estaciones, y qué NO

```
   ESTACION A                                    ESTACION B
   ==========                                    ==========

   objeto original                               25 bolas de repuesto
        |                                        (mismos 25 diametros)
        v                                              |
   leer retirando  --> paquete.json  ===========>  colocar
        |                1,1 kB                        |
        v              SOLO ESTO                       v
   original destruido   CRUZA                      verificar a ciegas
   con acta

   NO cruza: ninguna imagen · ninguna nube de puntos · ningun objeto.
   Si cruzara materia seria transporte. Si cruzara una imagen del original,
   el veredicto dejaria de ser ciego.
```

## 4bis · La revista de transporte · **es la propia bandeja**

```
   A ---- leer retirando ----> REVISTA ---- transporte ----> B ---- colocar ---->
          cada unidad pasa    (= una bandeja        la unidad NUNCA sale de un
          de su sitio en el    identica, con sus    asiento cinematico entre que
          objeto a un ALVEOLO  25 alveolos)         se lee en A y se coloca en B
          GENERICO
```

| | suelta en una caja | **sujeta en su asiento** |
|:--|--:|--:|
| fluencia plástica | **0,77 m/s = caída de 3 cm** | **109 g de choque** |

**La misma pieza que da la precisión da la protección.** Hertz sobre el contacto
bola(12,5 mm)/asiento(1,5 mm): a 50 g de choque `p₀` = 2,47 GPa contra 3,2 de fluencia. Ningún
transporte normal alcanza 109 g. **Coste: cero piezas nuevas** — la revista es una bandeja más,
mismo programa CNC.

> **EL ORDEN DE RETIRADA SE SORTEA.** El alvéolo es genérico, pero si las unidades se retiran en
> orden espacial (izquierda→derecha), **el número de alvéolo filtra la disposición**: son
> `log2(25!)` = **84 bits**, el 0,7 % del acto, viajando por fuera del canal declarado. El receptor
> identifica por **diámetro**, nunca por número de alvéolo.

## 5 · Lista de materiales · una estación

| pieza | qué | € |
|:--|:--|--:|
| bandeja CNC aluminio 200×200×10 | **mismo programa/material/lote que la otra** | 45 |
| 75 esferas acero 3 mm (25 asientos) | asiento cinemático | 79 |
| cámara industrial 1" + objetivo 50 mm | lector | 96–183 |
| columna perfil 40×40 + brida | fija L = 1.500 mm | 38 |
| panel LED + difusor 200×200 | retroiluminación | 24 |
| báscula 0,001 g | enclavamiento de masa | 60 |
| 25 bolas cromadas, **25 diámetros distintos** | el objeto · **sólo en A, no hay repuestos en B** | 35 |
| tornillería, cableado, PC | | 40 |
| | **total por estación** | **417–504** |
| | **las dos estaciones** | **834–1.008** |

**Los 25 diámetros distintos tampoco son un detalle.** Se decidieron en D-611 por otra razón —la
precisión de la unidad es enemiga de la identidad— y resultan ser **lo que hace posible φ = 1**: sin
etiquetas, la estación B mide el diámetro de cada unidad que llega y sabe **cuál es**. Con 25 bolas
iguales, «la unidad correcta en la dirección correcta» no se podría ni plantear.

**El lote común no es un detalle de compra, es la pieza de contrato.** Dos bandejas del mismo
programa CNC, el mismo material y el mismo lote tienen distorsión **correlacionada**, y lo
correlacionado **se cancela en Ω**. Por eso el acuerdo entre estaciones sale a 7,9 µm **sin Invar
y sin artefacto certificado**: no se hace el error pequeño, se hace **común**.
