# PREREG · recomputar el canal de ALINEAMIENTO (canal 4, gratis)

## TRIADA paso 1 · INVENTARIO

15 datasets en disco. **Ninguno tiene imagen ExM con verdad de campo densa**, así que la eficacia
de ExM sigue siendo laboratorio o literatura — *pero mi afirmación anterior fue sin inventariar,
y el inventario sí cambió otras cosas:* hay **córtex humano H01** (16.087 células con posiciones
3D, 116.611 aristas) y **1,0 GB de CNS macho**, que el marco no ha usado para esto.

Para recomputar alineamiento hacen falta **vóxeles**, y sólo CREMI los tiene. Se hace ahí.

## El riesgo de circularidad, escrito antes

**Si corrompo con desplazamientos rígidos y recupero con registro rígido, recupero el 100 % por
construcción.** Eso no mediría nada. Diseño para evitarlo:

- **corromper** con afín por sección: traslación **+ rotación pequeña** (realista entre cortes)
- **recuperar** con **sólo traslación** por correlación cruzada sobre la imagen EM cruda
- el modelo de recuperación es **deliberadamente más pobre** que el de corrupción

## TRIADA paso 2 · predicciones

- **P-A1 · el registro por traslación recuperará entre el 60 % y el 90 % del canal de
  alineamiento, central 75 %.**
- **P-A2 · el residuo estará dominado por la componente de ROTACIÓN**, que el modelo no puede
  describir. Verificable: corromper sólo con traslación debe recuperar > 95 %.
- **P-A3 · `Π` tras recomputar el alineamiento caerá en [0,006 , 0,020].**
  *Si baja de 0,01386 = `Π_max`, la cadena cierra con dos intervenciones gratis.*

## TRIADA paso 3 · MATE

Correlación cruzada por FFT (`np.fft`), una pasada por sección · se reutiliza `adya()` de D-476 ·
se cronometra una sección antes de estimar (regla 127).
