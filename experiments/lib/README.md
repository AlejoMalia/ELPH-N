# Instrumento y métodos — paquete exportable

Diez módulos, sin dependencias del resto del repositorio salvo `numpy`, `scipy` y
`pandas`. Todo lo que hay aquí **se validó contra datos medidos**, no contra ejemplos
inventados, y varias funciones existen porque un fallo real las hizo necesarias.

```python
import sys; sys.path.insert(0, 'ruta/a/lib')
```

## Antes de medir — la puerta

| módulo | qué hace | por qué existe |
|---|---|---|
| **`puerta.py`** | nivel 0: metadata, canales, listas nominales, batería T1–T9 | ha detenido **cuatro experimentos** a coste cero |
| **`puerta_v2.py`** | σ de medición centralizada · aviso de %I de vía · saturación como metadato | D-092 estaba copiado a mano en cada fichero |

`validar_canales` **rechaza** una lectura que no esté declarada biológica: elegir canales
por grado o por identificador de segmentación produjo un resultado insignia que hubo que
retirar.

`sigma_de_medicion` **exige la lista explícita** de condiciones aleatorizadas. Clasificarlas
por prefijo de nombre causó **dos invalidaciones falsas**.

## Antes de lanzar — el chequeo previo

**`preflight.chequeo()`** en orden de coste creciente. Los dos primeros son gratis y no se
saltan nunca:

| | comprobación | cuesta |
|---|---|---|
| 1 | **`mate.py`** — ¿hay trabajo cuyo resultado ya está demostrado? | nada |
| 2 | paralelismo — cola de trabajo, no reparto fijo | nada |
| 3 | **`secuencial.py`** — parada temprana con frontera O'Brien-Fleming | **paga α** |
| 4 | potencia — ¿basta K para las condiciones **nuevas**? | 1 piloto |

> Espiar 25 veces con α = 0,05 convierte el 5 % prometido en **26 %**. La frontera calibrada
> lo mantiene en 4,9 % y resuelve con el 29 % del coste cuando el efecto es grande.

**`compartir.py`** quita la redundancia que `mate.py` detecta: el primer obrero calcula, los
demás leen. La clave es el hash de **todo** de lo que depende el objeto, **incluido el código
fuente** — si el cálculo cambia, la caché falla en frío.

## Sin simular — responder desde los registros

| función | responde |
|---|---|
| `metodos.diagnostico_sigma` | ¿subir K arreglará esta σ? **Exige σ a dos K distintas** |
| `metodos.regla_K` | cuántos estímulos, por régimen (muestreo · suelo · fallo) |
| `metodos.coste_experimento` | horas de reloj, ±25 %, calibrado con reloj |
| `metodos.envolvente`, `b_estrella_adaptativo` | presupuesto y punto operativo |
| `horquilla.horquilla` | rango entre tareas **con barras de error** |
| `horquilla.descomposicion` | varianza entre tareas vs entre manifiestos |
| `fases.resolucion_identidad` | ¿distingue el instrumento dos individuos? |
| `fases.ventana_ensamblado` | cuánto aguanta un gradiente iónico sin bomba |
| `fases.extrapolacion_tasa` | ¿cuántos órdenes se están pidiendo de más? |
| `fases.canales_interfaz` | coste informacional del mapa cuerpo↔sistema nervioso |

## La regla que gobierna todo esto

> **Cada experimento debe dejar el siguiente más barato.** Ver `REGLAS.md`.

Y su contraria, aprendida a golpes: **medir antes de optimizar**. Una conversión encontrada
aquí era 103× más lenta de lo necesario — y suponía el **0,4 %** del tiempo. No se tocó.
