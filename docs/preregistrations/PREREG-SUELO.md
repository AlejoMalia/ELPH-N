# PREREG-SUELO · ¿es honesto nuestro suelo por mitades aleatorias?

**Fecha:** 2026-09-19 · Cero nervioso. **Escrito antes de correr.**

## Por qué importa

En **D-599** no había dos medidas de la misma hoja, así que el **suelo** se aproximó partiendo cada nube en
**dos mitades aleatorias** (regla 371). De ese suelo cuelga todo: `A` = √(`Ω_imp`/`Ω_suelo`), y publicamos
**`A_max` = 8,01**.

> **Si el proxy subestima el suelo real, nuestra `A` está inflada.** Hay que comprobarlo.

## El dato

**Open3D · DemoICPPointClouds**, descargado sin cuenta: **tres escaneos del mismo escenario físico desde
puntos de vista distintos**, con las **matrices de alineación conocidas** en `init.log`. 198.835 puntos el
primero, `.pcd` binario.

## MATEMÁTICA — antes de correr

Dos mitades de la **misma** nube comparten **todo el error sistemático** —posición del sensor, calibración,
sesgo de la superficie— y sólo difieren en el ruido de muestreo. **Dos escaneos distintos no comparten el
sistemático.** Luego:

```
suelo_proxy (mitades)  <  suelo_real (dos escaneos)
```

## Predicciones

- **P-S1** · el suelo por **mitades aleatorias** sale **menor** que el suelo por **dos escaneos**, en un
  factor de **2 a 10×**.
- **P-S2** · por tanto **`A_max` = 8,01 de D-599 está inflada**, y el valor honesto es
  `8,01`/√(factor) = **entre 2,5 y 5,7**.
- **P-S3** · restringir al **solapamiento** baja el suelo real respecto a comparar las nubes enteras, porque
  quita la diferencia de cobertura, que no es error de medida.

## Si P-S1 falla

Si el suelo por mitades sale **igual o mayor** que el real, **el proxy era conservador** y la `A` de D-599
se sostiene o mejora. *Las dos salidas son informativas; por eso se escribe antes.*
