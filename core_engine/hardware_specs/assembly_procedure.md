# MONTAJE · paso a paso

**Dos estaciones idénticas.** Todo lo que sigue se hace **dos veces**, salvo el paso 2, que se
hace **una sola vez para las dos** y es la razón de que la máquina funcione.

Plano: [`PLANO.md`](PLANO.md) · Software: [`../code/maquina.py`](../code/maquina.py)

---

## 0 · Antes de comprar nada

> **Corre el GATE-0 primero.** Cuesta 10–25 € y una tarde. Si falla, **nada de lo que sigue sirve**
> y te ahorras los 1.000 €. Mide si las dos estaciones se corrigen contra los fiduciales por debajo
> de 35 µm. D-610 ya avisó de lo que puede salir mal: **la pose del sensor respecto a la bandeja
> tiene que ser MECÁNICA, no procedimental** — si no, ninguna calibración la salva.

---

## 1 · Bandeja

1.1 · Encarga **las dos bandejas juntas**: mismo fichero CNC, mismo material, **mismo lote de
barra**. Dilo explícitamente en el pedido. *Si el taller las hace en semanas distintas o de coladas
distintas, se pierde la cancelación en modo común y el acuerdo se va de 7,9 µm a ~40 µm.*

1.2 · Graba los **9 fiduciales** (⌀ 4 mm, rejilla de paso 85 mm) en la misma sujeción que los
asientos. *En la misma sujeción: si se reposiciona la pieza, fiduciales y asientos dejan de estar
en el mismo sistema de referencia y la calibración corrige lo que no es.*

1.3 · Taladra los **75 alojamientos** (25 asientos × 3), ⌀ 2,4 mm, a 120°, círculo de ⌀ 9 mm.

## 2 · Asientos · **se hace una vez, en pareja**

2.1 · Pega las esferas de 3 mm con adhesivo anaeróbico. **Una esfera por alojamiento, sin holgura.**

2.2 · Deja curar **24 h en horizontal**. *Curar en vertical deja la esfera descendida unas micras y
el asiento pierde la simetría de 120°, que es de donde sale la determinación del centro.*

2.3 · **Comprobación:** deja caer una bola en un asiento 10 veces y mira la silueta. Si el centro se
mueve más de **1 px**, el asiento está mal. Repite.

## 3 · Columna y cámara

3.1 · Atornilla la columna a la bandeja. **La columna y la bandeja son una sola pieza rígida.**

3.2 · Monta la cámara a **L = 1.500 mm** del plano, mirando abajo. *No es un número redondo
arbitrario: el sesgo de silueta cae como 1/L². A 300 mm son 65 µm, a 1.500 mm son 0,03 µm.*

3.3 · Nivela: la diferencia de foco entre las cuatro esquinas de la bandeja, por debajo de la
profundidad de campo. **Enclava con tornillo prisionero, no con la fricción de la brida.**

3.4 · Enfoca a los fiduciales y **bloquea el anillo con laca**. *Cualquier reenfoque posterior
invalida la calibración.*

## 4 · Retroiluminación y báscula

4.1 · Panel LED + difusor bajo la bandeja. Sube la corriente **hasta justo antes de saturar**:
la silueta tiene que ser negra sobre fondo blanco uniforme.

4.2 · Báscula bajo el conjunto, con la bandeja apoyada **sólo** en el plato. Tara.

4.3 · **Comprobación:** quita una bola y mira. El escalón tiene que ser ≥ 100× el ruido de la
báscula. *Es el enclavamiento de masa: una coordenada sólo se escribe cuando la báscula registra
el escalón de una unidad — el fichero es un subproducto de la destrucción (D-608).*

---

## 5 · Calibración · en cada estación

```bash
python3 maquina.py calibrar fid.png
```

**Criterio de aceptación:** RMS por debajo de **30 µm** en el banco de 7 px/mm; por debajo de
**5 µm** con la cámara de la lista. Si sale más, revisa 3.3 antes de tocar nada del software.

## 6 · El suelo · **12 re-colocaciones, no 12 fotos**

```bash
# 12 veces: retirar las 25 bolas, volver a colocarlas segun ordenes.csv, fotografiar
python3 maquina.py verificar paquete.json 's*.png' 'd*.png'
```

> **Esto es lo más fácil de hacer mal, y lo hicimos mal.** Fotografiar 12 veces la misma colocación
> mide la repetibilidad de **la cámara**, no la de **la máquina**: deja fuera los 141 µm del
> colocador y el suelo sale cero. Con un suelo cero, **todo acto falla**. Hay que **retirar y volver
> a colocar** cada vez (**regla 413**).

**Hacen falta 12 y no 3** porque δ no se elige, **se mide** de la dispersión del propio suelo. Con
menos de 10 la dispersión no se estima y el software **aborta a propósito**.

## 6bis · Transporte

6bis.1 · Las unidades se retiran **en orden sorteado** (el software lo exige) y cada una va a un
alvéolo de la revista. *Si se retiran de izquierda a derecha, el número de alvéolo filtra 84 bits de
disposición por fuera del canal.*

6bis.2 · La revista se cierra con su tapa **apoyando sobre las bolas**, no sobre la placa: la unidad
queda precargada contra sus tres puntos y **no puede despegar**.

6bis.3 · **Criterio:** el transporte no debe superar **109 g** de choque. Es holgado —una caída libre
de la revista entera sobre hormigón no llega—, pero una unidad **suelta** fluye ya a 3 cm de caída.
*La diferencia entre las dos cifras es sólo la tapa.*

## 7 · El acto

```bash
# ESTACION A
python3 maquina.py calibrar fid.png
python3 maquina.py enviar 'o*.png'        # leer retirando: 26 fotos para 25 unidades

# --- cruza paquete.json, 1,1 kB. NADA MAS. ---

# ESTACION B
python3 maquina.py recibir paquete.json   # -> ordenes.csv
python3 maquina.py verificar paquete.json 's*.png' 'd*.png'
```

**Leer retirando:** se fotografía, se retira **una** unidad, se vuelve a fotografiar. La coordenada
sale de la **diferencia**. El kerf es cero **porque la unidad ES el vóxel**, y la destrucción del
original no es un paso añadido: **es el propio acto de leer**.

## 8 · Criterios de aceptación

| | criterio | medido en el banco |
|:--|:--|--:|
| **disposición** | `Ω_acto` ≤ (1+δ)·suelo, δ **medido** | 0,00112 ≤ 0,00184 **pasa** |
| **inventario** | p98 contra el **suelo del p98** | 0,00247 ≤ 0,00408 **pasa** |
| **recuento** | n_origen = n_destino | 25 → 25 **pasa** |
| **contrato** | `A` = √(Ω_imp/Ω_acto) > 1 | **A = 9,03** |
| **control negativo** | tiene que **FALLAR** | A = 0,94 **falla como debe** |

## 9 · Lo que esta máquina NO puede ver

**Medido, no supuesto:** una sola unidad mal colocada se detecta el **95 %** de las veces a
**1,0 mm**, el 55 % a 0,7 mm, y **por debajo de 0,4 mm la máquina es ciega**.

Y la disposición **es ciega al inventario**: en el control con una bola de menos, `Ω` de disposición
**pasó tranquilamente**. Quien lo cazó fue el p98 y la báscula, por dos vías independientes. **Por
eso la báscula no es redundante: es carga estructural.**
