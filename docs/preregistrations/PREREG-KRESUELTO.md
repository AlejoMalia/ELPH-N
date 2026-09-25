# PREREG-KRESUELTO · resolver `k_muestreo` sin histología más fina

**Fecha:** 2026-09-19 · Cero nervioso. **Predicciones antes de correr.**

## INVENTARIO

En disco: corazón humano a **4,10 µm/px** y mama humana a **3,76 µm/px**. **Ninguna llega a los 2,50 µm/px**
que D-603 dijo que hacían falta. *Comprar más fino es semanas y dinero.*

## MATEMÁTICA — y aquí puede caerse la necesidad de comprar nada

**El problema de D-603 no es la imagen: es el MÉTODO.** Promediar por bloques usa un tamaño **entero de
píxeles**, así que sólo puede representar `q` = 1, 2, 3… píxeles y **entre `b` = 2 y `b` = 1 no hay nada.**

> **Una convolución gaussiana de `σ` CONTINUO degrada igual y no se cuantiza.** Un bloque de ancho `q` y una
> gaussiana de `σ` = `q`/√12 tienen el mismo segundo momento — y la gaussiana es **más física**, porque la
> PSF de un instrumento real se parece más a una gaussiana que a un escalón.

```
si esto funciona, **no hace falta histologia mas fina: hacia falta otro operador de lectura**
```

## Predicciones

- **P-R1** · con gaussiana continua **la meseta desaparece** y `Ω` varía suavemente con `q`.
- **P-R2** · el cruce con el suelo cae entre **arq/10 y arq/25**.
- **P-R3** · **no saldrá exactamente 12**: el 12 de D-547 estaba dentro de la meseta `b` = 2, así que era un
  artefacto de cuantización, no una medida.
- **P-R4** · las dos histologías —corazón 4,10 y mama 3,76 µm/px— **darán el mismo `k` dentro de 1,5×**, porque
  `k` es propiedad del sustrato y no del píxel. *Si difieren mucho, `k` depende del instrumento y no del tejido,
  y eso rompería la regla 372.*
