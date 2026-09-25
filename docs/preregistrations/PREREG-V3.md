# PREREG · V3 · **el primer mamífero que recupera circulación espontánea tras vitrificación**

**Lo que aquí se puede ejecutar y lo que no, dicho antes:** el experimento es de **laboratorio húmedo con
animales**. Aquí se ejecuta **todo lo demás**: el diseño, los umbrales, los controles, el tamaño de muestra, las
cotas físicas cerradas y la elección de especie por triangulación. **La parte húmeda no se puede correr en esta
sesión y no se simula: se especifica.**

## TRIADA

**(1) INVENTARIO.** D-522: V2 desde vitrificado demostrado (riñón de rata 1,5 mL, de conejo ~9 mL);
calentamiento uniforme físico a 2 L; V1–V5 en humano entero sólo con parada hipotérmica ≤ 50 min **sin**
vitrificar. **Y un peldaño que D-522 no tenía:** Smith, Lovelock y Parkes (1954/1956) resucitaron **hámsteres
enteros** con **40–50 % del agua corporal congelada**, recalentados por **dieléctrico (microondas)**.

**(2) MATEMÁTICA · cotas cerradas, escritas antes.**

- **Por qué hace falta calentamiento volumétrico incluso en un ratón.** Con difusividad térmica
  α ≈ 1,3e-7 m²/s, el tiempo característico de conducción es `τ = r²/α`, y la tasa media alcanzable en el
  centro es `ΔT/τ` con ΔT ≈ 150 °C. **Se compara con la tasa crítica de recalentamiento de M22 (10–80 °C/min
  según concentración).**
- **Carga de CPA:** M22 tiene tasa crítica de enfriamiento ≈ **0,1 °C/min**, que cualquier baño alcanza; el
  cuello es el **recalentamiento**, no el enfriamiento.
- **Tamaño de muestra:** para distinguir una tasa de éxito `p` de cero con potencia 0,8 basta
  `n ≥ ln(0,2)/ln(1−p)`; para estimar `p` con ±0,15 al 95 % hacen falta `n ≈ 4p(1−p)/0,15²`.

**(3) MATE.** `cuerpo.py`, `vivo.py` y la tabla de niveles V1–V5 de D-522. Cero cómputo nuevo pesado.

## El experimento, especificado

**Objetivo primario:** un mamífero **entero**, vitrificado (ice-free, bajo Tg) y recalentado, que alcance
**V3 = ROSC sostenido ≥ 20 min** (criterio Utstein).

**Especie, por triangulación de escala** (se elige la menor que sea un mamífero entero).

**Brazos:**

| brazo | qué | para qué |
|:--|:--|:--|
| **A · vitrificado** | M22 por perfusión vascular → < Tg → nanocalentamiento RF | el experimento |
| **B · control de CPA** | M22 y enfriamiento a 0 °C **sin** vitrificar, recalentado igual | separa toxicidad de CPA del daño por vitrificación |
| **C · control de parada** | parada circulatoria hipotérmica equivalente, sin CPA | da el suelo de isquemia |
| **D · control positivo histórico** | cristalización parcial 40–50 %, recalentamiento dieléctrico (1954) | comprueba que el banco reproduce un peldaño ya publicado |

**Medidas, en el orden de D-522:** V1 (viabilidad en biopsias), V2 (función de órgano), **V3 (ROSC ≥ 20 min,
primario)**, V4 (gasometría), V5 (EEG no isoeléctrico).

**Criterios de retirada, escritos antes:** si el brazo **D** no reproduce el resultado de 1954, el banco no está
validado y **nada de lo demás cuenta**. Si el brazo **B** falla, el problema es la toxicidad del CPA y no la
vitrificación, y eso cambia el programa entero.

## Predicciones con número

- **P-V3a.** La conducción sola **no** alcanza la tasa crítica de M22 ni en un ratón: predigo < 10 °C/min en el
  centro para r ≥ 1 cm → **el calentamiento volumétrico es obligatorio**. *Y explica por qué Lovelock usó
  microondas en 1954.*
- **P-V3b.** La especie mínima viable (mamífero entero) queda **entre 2 y 30 veces** el mayor órgano ya
  vitrificado con función (riñón de conejo, ~9 mL), y **muy por debajo** de los 2 L ya recalentados de forma
  uniforme.
- **P-V3c.** Con `p` = 0,2, **n ≥ 8** animales por brazo para excluir el cero con potencia 0,8; para estimar `p`
  al ±0,15, **n ≈ 28**.
- **P-V3d.** El experimento **no** está limitado por volumen ni por tasa de enfriamiento: el cuello es
  **toxicidad de CPA y perfusión completa**, no la física térmica.
