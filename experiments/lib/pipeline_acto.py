"""D-711 · EL PIPELINE COMPLETO, de encender la cabina A a salir por la cabina B.

  TRIADA
  ------
  INVENTARIO  · estan los PASOS FISICOS (D-698 minuto a minuto, D-704 siete fases).
                NO esta el FLUJO DE CONTROL: que hace el software entre paso y paso.
  MATEMATICA  · preinscrita antes de correr:
                P1 · los huecos estaran en las RAMAS DE ABORTO, no en los pasos.
                P2 · toda rama anterior al sellado sera trivial (nadie dentro).
                P3 · el presupuesto de energia se dimensiono para el ACTO (3,4 min)
                     y el pipeline dura ~20x mas -> no cerrara.
  MATE        · se reutiliza D-698 (tiempos), D-704 (fases), D-706 (suelo heredado),
                D-707 (30 % de no retorno), D-709 (banca). Coste de computo: 0.

  RESULTADO   · P1 SI: 9 de 17 ramas sin destino, TODAS posteriores al sellado.
                P2 SI: 8 de 8 ramas previas al sellado vuelven a S0 y son triviales.
                P3 SI: 105 W x 77 min = 135 Wh > 124 Wh de bateria. **No cerraba.**
                       La salida no es mas bateria: es que la cabina va con CORDON
                       UMBILICAL en estacion y la bateria solo cubre S12->S16
                       (7,4 min, 13 Wh, 9,6x de margen). Eso obliga a un pasamuros
                       de POTENCIA desconectable en caliente que D-696 no conto.
"""
CONT_W = 105.0            # W con la cabina encendida (6 cargas)
T_PIPE_MIN = 77.0         # S1 (T-35) a S23 (T+42)
T_BAT_MIN  = 7.4          # S12 sellado de ventilacion -> S16 apertura en B
BAT_WH = 124.0            # D-688, quimica sin litio

# La regla que sale del ataque: LA PUERTA NUNCA ES EL CASTIGO.
# S13 (commit) parte el pipeline en dos regimenes de aborto:
#   antes  -> ROLLBACK      (el acto no existio; la persona sale por donde entro)
#   despues-> SIN ROLLBACK  (la entrega se cumple SIEMPRE; solo el certificado falla)
ROLLBACK_HASTA = "S13"
REINTENTOS_LECTURA = 3    # limite duro nuevo: sin el, bucle con persona dentro

if __name__ == "__main__":
    print(f"  pipeline encendido      {T_PIPE_MIN:.0f} min x {CONT_W:.0f} W = {CONT_W*T_PIPE_MIN/60:.0f} Wh")
    print(f"  bateria                 {BAT_WH:.0f} Wh  -> {BAT_WH/(CONT_W*T_PIPE_MIN/60):.2f}x  **NO CIERRA**")
    print(f"  con cordon umbilical    {T_BAT_MIN:.1f} min x {CONT_W:.0f} W = {CONT_W*T_BAT_MIN/60:.0f} Wh"
          f"  -> {BAT_WH/(CONT_W*T_BAT_MIN/60):.1f}x  CIERRA")
