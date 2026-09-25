# PREREG · **los dos experimentos más baratos**, ejecutados aquí

Dos encargos, y digo antes cuál puedo hacer y cuál no.

- **El de enfriamiento (10 y 20 L de crioprotector en bolsa) es FÍSICO y no lo puedo correr.** Pero TRIADA
  paso 2 obliga a comprobar antes si una **cota cerrada** lo contesta. **Creo que lo contesta, y si acierto,
  el experimento cambia de forma.**
- **El observable de arquitectura de tejido SÍ es ejecutable entero**, y el agente lo señaló como el más
  barato de los once: es cómputo sobre datos que ya están en disco.

## TRIADA

**(1) INVENTARIO.** `data/corazon/spatial/tissue_hires_image.png`: **histología de tejido cardíaco humano
real, 2000 × 2000 px**. Con `spot_diameter_fullres` = 89,43 px para un spot de 55 µm y el factor de escala
0,150015, sale **4,10 µm por píxel** y un campo de **8,2 mm**. **Es exactamente la escala que D-533 dijo que
hacía falta**, y es tejido, no una rejilla de medida.

**(2) MATEMÁTICA · escrita antes.**

*Enfriamiento.* En conducción, el tiempo característico de un cuerpo enfriado por su superficie es
`τ = L²/α` con `L` la **semi-espesor**, no el volumen. Entonces:

```
placa (enfria por las dos caras):  tasa = dT·alfa / L^2      -> depende SOLO del espesor
esfera o cubo compacto:            L ~ V^(1/3)               -> tasa ~ V^(-2/3)
conveccion dominante (Biot bajo):  tasa ~ superficie/volumen -> tasa ~ V^(-1/3)
```

**El exponente empírico ajustado sobre tres puntos fue 0,62.** Si eso está cerca de **2/3 = 0,667**, la ley es
de **conducción** y no un artefacto del ajuste — **y entonces la magnitud que manda es el ESPESOR**.

*Arquitectura.* Observable = la imagen menos su desenfoque a la escala del contrato (100 µm): eso **es** la
arquitectura de ≤ 100 µm. Acto = leer a resolución `q` (promedio en bloques, que es lo que da un escáner) y
reconstruir. Suelo = dos lecturas independientes con ruido de imagen. Impostor = **direcciones de bloque
permutadas**. `Ω = 1 − corr`, `A = √(Ω_imp/Ω_acto)`.

**(3) MATE.** `banco.om`, el mismo Ω de siempre. Cero cómputo pesado, cero nervioso.

## Predicciones con número

**Enfriamiento**

- **P-E1.** El exponente empírico **0,62** estará a **menos del 15 %** de 2/3 → la ley es de conducción y la
  extrapolación de D-537 **no** es un artefacto de tres puntos.
- **P-E2.** La magnitud que manda es el **espesor**: el semi-espesor crítico para 0,1 °C/min saldrá
  **~10 cm** (espesor ~20 cm).
- **P-E3 · la que cambia el plan.** Una **extremidad** (espesor < 20 cm) vitrificará **por grande que sea su
  volumen**, y el **torso** quedará justo en el filo. *Si acierto, «33,9 L» deja de ser la cota y el
  experimento a hacer ya no es de volumen: es de GEOMETRÍA.*

**Arquitectura**

- **P-O1.** El suelo (dos lecturas con ruido) será **< 0,05**.
- **P-O2.** El impostor (bloques permutados) será **> 0,90**.
- **P-O3.** Leyendo a **100 µm** —la escala de la propia arquitectura— **A < 1,5**: se reproduce el fallo de
  D-533, ahora sobre **tejido real** y no sobre una rejilla.
- **P-O4.** Leyendo a **5 µm**, `Ω ≤ 0,05` y **A > 3**.
- **P-O5.** El cruce de `Ω = 0,05` caerá entre **10 y 30 µm**, es decir un factor **3–10×** sobre la
  arquitectura — **más suave que el 20–30× que derivé sobre la rejilla**. *Si cae en 20–30×, la rejilla no
  engañaba y el requisito es duro.*
