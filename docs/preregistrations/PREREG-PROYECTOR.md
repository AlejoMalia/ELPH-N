# PREREG-PROYECTOR · la regla de tres ratón → humano, ajustada y VALIDADA antes de usarla

**Fecha:** 2026-09-18 · **Autorizado explícitamente por el investigador** (levanta para esta tarea la norma
dura de `CLAUDE.md` §0, y **sólo** para usar datos nerviosos como **sustrato de calibración**, no como campaña).

## La idea, y su trampa

Proyectar el resultado del V3 en ratón a humano con una regla de tres. **La trampa: una regla de tres supone
exponente 1.** En biología casi nada escala así. El instrumento correcto es:

```
X_humano = X_raton * (M_humano/M_raton)^b       y todo depende de b
```

**Así que b no se supone: se ajusta sobre pares donde conocemos los DOS valores, y el instrumento se valida
antes de aplicarlo** — igual que validamos el simulador térmico contra las criobolsas antes de usarlo
(regla 257).

## INVENTARIO

Pares ratón/humano en estado `[L]`: masa corporal, masa encefálica, número de neuronas, densidad neuronal
cortical, **densidad sináptica**, tasa metabólica basal, frecuencia cardíaca, radio de Krogh, hematocrito.
Y pares **nuestros**, `[M]`: `L_C` y tasa de enfriamiento de D-541/D-562.

## MATEMÁTICA — antes de calcular

Las magnitudes caen en familias con exponente conocido (regla 225): **intensivas** `b` ≈ 0, **extensivas**
`b` ≈ 1, **metabólicas** `b` ≈ 0,75, **frecuencias** `b` ≈ −0,25, **superficie/volumen** `b` ≈ −1/3.
El proyector **primero clasifica, luego aplica**.

## Predicciones

- **P-P1** · clasificadas por familia, las proyecciones sobre los pares conocidos dan **error mediano < 2×**.
- **P-P2** · **el exponente térmico medido sobre NUESTROS datos NO es el isométrico −2/3**, sino más
  empinado, **entre −0,85 y −1,0**: el cuerpo humano no es un ratón escalado, es relativamente más grueso.
- **P-P3** · el tiempo de exposición a crioprotector proyecta **500–1.000×** de ratón a humano.
  *Ésta es la cifra que decide qué significa un V3 positivo en ratón.*
- **P-P4** · **la densidad sináptica es la magnitud más conservada** (|b| < 0,1) — y ése es el papel del
  dato nervioso aquí: **es el patrón invariante contra el que se calibra**, no una campaña de conectoma.

## Lo que esto NO es

**No modifica ningún dato.** No es una campaña nerviosa: las capas A–G siguen congeladas. Y un proyector
validado **no sustituye al experimento**: da la banda en la que se espera el resultado, y se deja refutar.
