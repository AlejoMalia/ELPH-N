# PREREG · el canal que faltaba: DISTORSIÓN del gel de ExM

## TRIADA paso 1 · INVENTARIO de la lista del investigador

Cinco fuentes públicas de ExM. **Ninguna tiene verdad de campo de CONECTIVIDAD** (HeLa con
mitocondrias, cardiomiocitos, riñón con nefrina, protocolos). Para `e_conn` de ExM **no sirven**,
y la afirmación «necesita laboratorio» se mantiene **para esa cifra**.

**Pero destapan un fallo de mi modelo:** ExM apaga el canal de **corte** y **enciende uno nuevo
que yo nunca puse: la distorsión del gel.** `Π = e1 × 0,1516` (D-486) **omite ese canal**, luego
`Π` está **subestimado**.

## TRIADA paso 2 · la tolerancia de distorsión, derivada ANTES de buscar datos

Se aplica un campo de distorsión suave de amplitud δ (en vóxeles de 16 nm) al volumen de
etiquetas y se mide `e_conn(δ)`. Luego se invierte: qué δ mantiene la contribución bajo el
presupuesto.

- **P-D1 · `e_conn` crecerá con δ como una potencia, y a δ = 1 vóxel (16 nm) ya será ≥ 0,05.**
  Razón: las membranas ocupan ~2 vóxeles; un desplazamiento de 1 vóxel ya cruza interfaces.
- **P-D2 · la δ tolerable para que la distorsión no domine `Π` será < 1 vóxel, es decir
  < 16 nm en el tejido original.**
- **P-D3 · la literatura de ExM reporta 1–4 % de distorsión sobre ~10 µm, es decir 100–400 nm.
  Predigo que eso es 6–25× MAYOR que la tolerancia derivada**, y que por tanto **la distorsión
  es el canal dominante de ExM, no el alineamiento.**
  *Si la tolerancia sale > 100 nm, la distorsión no importa y tus datasets tampoco hacen falta.*

**Y sólo si P-D3 acierta merece la pena bajar los datasets**: entonces la pregunta pasa a ser
«¿cuánta distorsión tiene un gel real?», y S-BIAD2200 (pan-ExM con MIC60/TOM20, estructuras de
referencia conocidas) es el candidato.
