# PREREG-CIEGO · cerrar los tres criterios que quedan, con matemática propia

**Fecha:** 2026-09-19 · Cero nervioso. **Predicciones antes de correr.**

## Lo que faltaba de D-595, y por qué NO era inalcanzable

| criterio | por qué dije que no | **la verdad** |
|:--|:--|:--|
| **2 · control negativo que falle** | «no existe para las hojas» | **se CONSTRUYE**: un caso que debe fallar |
| **4 · veredicto a ciegas** | «yo conocía el emparejamiento» | **se PROGRAMA**: que el algoritmo asigne sin saber |
| **5 · original destruido con acta** | «no hubo objeto físico» | **tiene forma informacional**: reconstruir **sólo** desde lo transmitido |

**El 5 se parte en dos**, y hay que decirlo: su función es descartar que el destino sea el original de
contrabando. **En versión informacional eso SÍ se comprueba** —la reconstrucción no puede tocar la nube
original, sólo los bits enviados—. **En versión material no**, porque no hay objeto que destruir.

## La matemática que falta y nadie nos va a dar

**La curva tasa–distorsión del contrato:** cuántos bits hay que enviar para que `Ω_acto` ≤ suelo.

```
bits(k) = n_ocupados(k) * log2(k^3 / n_ocupados(k))    (indices de celda ocupada)
```

y se busca el **`k*` donde `Ω_d(original, reconstruido desde los bits)` = suelo.**
**Ése es el coste en bits de un teletransporte certificado de este objeto.**

## Predicciones

- **P-C1** · el protocolo ciego acierta **8 de 8** emparejamientos.
- **P-C2** · el **control negativo** —estructura destruida conservando extensión y densidad— cae en zona de
  impostor: **`A` < 1,5**.
- **P-C3** · los bits para `Ω` ≤ suelo están entre **10 kB y 1 MB** por hoja.
- **P-C4** · los bits crecen **como `k³`** (exponente medido entre 2,5 y 3,2).
