# PREREG-TINTA · el techo real de densidad celular en tinta

**Fecha:** 2026-09-18 · Sólo cuerpo humano completo. Cero nervioso.

## INVENTARIO

Ancla actual **5×10⁷ células/mL**, estado `[L]` (D-549), **sin justificación física**. Densidad nativa de
hígado **1,35×10⁸ /mL** (`[L]`). Diámetro de hepatocito **20–30 µm** (`[L]`). Nada medido por nosotros.

## MATEMÁTICA — escrita antes de calcular

**No hace falta buscar un paper: lo contesta el empaquetamiento.** Una suspensión de esferas tiene
**empaquetamiento aleatorio compacto** en `φ_RCP` ≈ 0,64 y **atasca** (deja de fluir) en `φ_j` ≈ 0,58. Con
`V_cel` = `π/6·d³`:

```
rho_max(phi) = phi / (pi/6 * d^3)
```

Y hay una **triangulación gratis**: las dos cifras de literatura —densidad del hígado y diámetro del
hepatocito— **se restringen mutuamente**, porque `φ` no puede pasar de 1. Si a 25 µm sale `φ` > 1, una de las
dos está mal.

## Predicciones

- **P-T1** · techo de empaquetamiento para célula de 20 µm: **1,4–1,6×10⁸ /mL**.
- **P-T2** · el hígado nativo (1,35×10⁸) cae en `φ` = **0,55–0,60**, es decir **JUSTO en el atasco**:
  *el tejido hepático nativo es una pasta atascada, no una suspensión*.
- **P-T3** · nuestro ancla de 5×10⁷ corresponde a `φ` ≈ **0,20**, que es el límite de lo que fluye.
  **El ancla no era arbitraria: era el límite de suspensión fluida.**
- **P-T4** · contra el techo de atasco, `N_hígado` = **0,85–0,95: pasa** — pero sólo por extrusión de **pasta**,
  no de tinta líquida, y eso cambia el régimen de cizalla.
- **P-T5** · la triangulación **excluye** el hepatocito de 25 µm: daría `φ` > 1, imposible.
