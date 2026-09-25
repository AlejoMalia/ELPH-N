# PREREG · MATRIZ DE CAPAS v2 · proyectar los datos NUEVOS (D-513 a D-517) sobre las otras capas

Escrito antes de calcular. D-512 cruzó los 21 pares **antes** de SynEM, α = 1, origami,
cinética, FIB/SEM y el acto real. **Esos datos no se han propagado a las demás capas.**

## TRIADA

**(1) INVENTARIO de datos nuevos no propagados**

| dato | capa de origen | ¿propagado? |
|:--|:--|:--|
| `N_sinapsis` 5,525e14 → **2,407e14** | C (D-517) | **NO** — D-516/517 calcularon E con `lugares` = 5,825e14 |
| acto real: `cD` por espacio, `Ω` 0,213 / 0,399 | F (D-517) | **NO** — nunca se invirtió hacia D |
| `σ*` origami 13,8 nm | E (D-516) | a F sí; a G **no** |
| `portador_TB` = 962,8 TB | C | **la pierna ENVIAR de F nunca se ha costeado** |

**(2) MATEMÁTICA, pares con cota cerrada**

- **C → E.** `lugares` baja 2,15× → la densidad por lámina baja 2,15× y las obleas también; las
  **láminas no cambian** (las fija la geometría). *Predigo: margen de densidad 1,98e4 → 4,27e4 y
  obleas 56 → 26; el tiempo de montaje NO se mueve.*
- **F → D, el par que nadie ha hecho.** Invertir la ley de F: ¿qué `Π` exige `Ω` p95 ≤ 0,05?
  *Predigo que sale MÁS exigente que el `Π_max` = 0,01386 de D, porque ése se derivó de un modelo de
  margen de lectura (D-484), no del acto dinámico.* **Riesgo de inconmensurabilidad declarado:** el
  arnés de F modela el error de lectura como **inversión de signo** y D lo define como **Jaccard**
  (arista perdida). Una inversión mueve el peso 2w y una pérdida w. **Se MIDE la conversión**
  corriendo el arnés con modelo de **borrado**, en vez de suponerla. Predigo razón de daño
  borrado/inversión en `Ω − suelo` ∈ [0,3 , 0,6].
- **C → F (ENVIAR).** 962,8 TB a velocidad de enlace publicada y con BER post-FEC publicado.
  *Predigo: < 24 h y error de canal > 10 órdenes por debajo de `Π`.*
- **F → D → F (VERIFICAR).** Verificar el destino es LEERLO con la misma modalidad: el `Ω` mínimo
  certificable es `Ω_D(Π)`. *Predigo: con `Π` de literatura, la fidelidad es NO CERTIFICABLE aunque la
  fabricación fuera perfecta, en ≥ 5 de 6 celdas.*
- **E → G y D → G.** La G del acto real (PREREG-G-CAOS).

**(3) MATE.** `f_real_*.json` (los `cD` por celda), `predice.py`, `jacobiano.py`, `de_lit.py`.
