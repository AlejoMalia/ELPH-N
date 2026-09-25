# PREREG · `d_min` de LUGARES, medido (no inferido)

## TRIADA paso 1 · el dato existe y no se había usado

`data/humano/h01_oficial/aristas.csv` tiene **115.530 sinapsis con coordenadas x,y,z**, y
`somas.csv` tiene **49.380 somas** con x,y,z, tipo celular y capa. **`metadata.npz`, que es lo
que veníamos usando, sólo trae 16.087 posiciones de células.**

D-497 dejó pendiente: `d_min` se midió sobre **células**, pero D-415 estableció que **la sinapsis
ES lugar**. El agente infirió geométricamente
`d_min(lugar) = 1,5718·(N_cel/lugares)^(1/3) = 0,7313 µm`, **suponiendo distribución uniforme**.

**Ahora se puede MEDIR en vez de inferir.**

## TRIADA paso 2 · predicciones

- **P-L1 · el `d_min` de lugares MEDIDO será MENOR que el inferido (0,7313 µm)**, porque las
  sinapsis **se agrupan sobre las neuritas** en vez de repartirse uniformemente. Predigo
  **[0,20 , 0,70] µm, central 0,40 µm**.
- **P-L2 · eso lleva σ\* = k·d_min a [28 , 98] nm, central 56 nm**, y **rompe el «la máquina
  existe»** de D-492 (2 fotones = 150 nm). *Si sale > 150/0,1407 = 1,066 µm, la máquina sigue
  valiendo.*
- **P-L3 · el `d_min` de CÉLULAS medido sobre las 49.380 somas de `somas.csv` diferirá del de
  las 16.087 de `metadata.npz`** (1,5718 µm) **en más de un 20 %**, porque son censos distintos.
- **P-L4 · en `mosca` (118.104 somas) el `d_min` celular será del mismo orden** que en H01 —
  predigo dentro de un factor 3.
