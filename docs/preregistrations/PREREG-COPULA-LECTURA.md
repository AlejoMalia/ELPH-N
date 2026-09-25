# PREREG · segunda cópula: la cadena de LECTURA

Escrito **antes** de correr. La cópula existente cubre 17 anclas → 10 cifras de **colocación y
fabricación**. D-468 probó que es **ciega a la lectura**. Ésta es la segunda.

## Las anclas de la cadena de lectura y su estado evidencial

| ancla | valor | ε | procedencia |
|:--|--:|--:|:--|
| `D_tol_10nm` | 1e8 Gy | **±100 %** | Howells 2009 — **LITERATURA, no medida aquí** |
| `alpha_tol` | 1,0 | ±30 % | exponente de `D_tol ∝ d^α` — literatura |
| `beta_req` | 4,0 | ±10 % | Rose, `D_req ∝ d^−β` — sólido |
| `e_por_voxel` | 2.000 | ±50 % | instrumento |
| `eV_por_e` | 300 | ±33 % | deposición media |
| `X_exp` | 4,0 | **±0 %** | **DECISIÓN del diseñador — GRATIS** |
| **`iota`** | **?** | **±100 %** | **fracción del error que es de DETECCIÓN y no de la muestra — NO MEDIDA** |
| `e1` | 3e-3 | ±33 % | una lectura destructiva, D-436 |
| `ADM` | 4,65e-4 | ±10 % | **MEDIDO hoy**, TOLERA/D-466 |
| `distor_ExM` | 2 % | ±50 % | literatura ExM (1–4 %) |

## TRIADA paso 2 · la cifra cerrada que decide la cadena

Si sólo una fracción `ι` del error es de detección y `(1−ι)` es ambigüedad irreducible de la
muestra, releer N veces **no toca la parte irreducible**:

```
e_final(N=3) = (1−ι)·e1 + 3·(ι·e1)²
```

Exigir `e_final ≤ ADM` define un **umbral de independencia `ι*`**.

- **P-C1 · `ι*` ∈ [0,80 , 0,90], central 0,85.** *Es la cifra más importante del programa: dice
  qué fracción del error de lectura tiene que ser del instrumento y no del tejido.*
- **P-C2 · la consolidación de la cópula de lectura será baja: 1 o 2 de 4 cifras** con banda
  < 2×, porque dos anclas no están medidas.
- **P-C3 · el ancla dominante será `iota`, no Howells.** `ι` multiplica directamente el residuo
  y es la única con soporte [0,1] entero.
- **P-C4 · P(la cadena cierra) bajo la incertidumbre de hoy ∈ [0,05 , 0,25], central 0,12.**
  *Si sale > 0,25, la cadena está mejor de lo que creo.*
- **P-C5 · declarar `X_exp` = 10 en vez de 4 NO subirá P(cierra) más de 5 puntos**, porque el
  cuello no es la dosis: es `ι`.
