# PREREG · ¿son las dos leyes del veredicto del PROGRAMA o sólo de H01?

## TRIADA paso 1 · INVENTARIO — y una parte está bloqueada

Se necesita un segundo espacio con **posiciones Y conectividad**. Comprobado:

| dataset | posiciones | aristas | ¿sirve? |
|:--|:--|:--|:--|
| `humano/H01` | sí (16.087) | sí (116.611) | el actual |
| `malecns` / `cns.npz` | **no** | **sí (25,5 M)** | **sólo para Ω_D** |
| `mosca` | **sí (118.104 somas)** | no | no |
| **`corazon` (Visium)** | **sí (4.992 spots)** | **sí (rejilla hexagonal)** | **sirve para Ω_E** |

*(Comprobado que `cns.npz` y `mosca` NO son unibles: solape de ids = **0**.)*

Y el corazón es **tejido humano NO nervioso**, que es lo que `CLAUDE.md` prefiere como espacio.

## TRIADA paso 2 · la unificación que predigo, escrita ANTES

Las dos leyes tienen exponentes muy distintos (0,6388 y 1,6525). **Pero si se expresan contra la
FRACCIÓN de adyacencias corrompidas, deberían coincidir:**

- en D la fracción corrompida **es** `Π` → exponente 0,6388
- en E la fracción reasignada `f*` crece como σ\*³ (volumen de la esfera de desplazamiento
  frente al espaciado). Medido hoy: f\* pasa de 0,0082 a 0,5193 cuando σ\* va de 0,218 a 1,0 →
  **exponente 2,72 ≈ 3**. Luego `Ω_E ~ f*^(1,6525/2,72) = f*^0,607`.

```
**0,6388  (canal D)   frente a   0,607  (canal E)   ->  difieren un 5,3 %**
```

- **P-P1 · contra la fracción corrompida, los dos canales dan el MISMO exponente ≈ 0,62 ± 15 %**,
  y coincide con el cúmulo de 0,637 de los seis caminos independientes (D-484). *Si acierta, no
  hay dos leyes: hay una.*
- **P-P2 · `b_D` en `malecns` será 0,6388 ± 15 %.**
- **P-P3 · `b_E` en el CORAZÓN será 1,6525 ± 25 %**, con σ\* expresado en unidades del espaciado
  entre lugares (no en µm absolutos — el spot de Visium está a ~100 µm y la célula de H01 a
  1,55 µm).
- **P-P4 · el suelo del corazón caerá en [0,003 , 0,02]** (gusano 0,0044 · H01 0,00483).
- **P-P5 · el veredicto (0,27 % y 16,4×) cambiará más de 3× entre espacios**, porque el suelo y
  N difieren. *Si cambia menos de 3×, el veredicto es del programa. Si cambia más, era de H01.*
