"""D-687 · CENSO DE LA MAQUINA · todos los elementos reales de la burbuja/objeto.
   DET = el marco lo determina (con qué) · PAR = parcial · HUECO = nada lo determina."""
E = [
("ESTRUCTURA",[
 ("cáscara monolítica, una sola operación","DET","f.17 · υ ≥ L · y elimina el fallo por soldadura"),
 ("espesor de pared","DET","f.20 · robusto a todo k ≤ 0,5 · acero ≥4,0 / Al ≥6,5 / comp ≥7,5 mm"),
 ("sobreespesor de corrosión","DET","+1,5 mm sobre la pared de cálculo (D-682)"),
 ("material sin transición dúctil-frágil","DET","austenítico 316L o aluminio (D-682)"),
 ("geometría esférica","DET","g = 3 + (3−dim); la esfera minimiza g, luego minimiza ψ"),
 ("anclajes de sujeción","DET","464 kN a 9 g · Eiband: la sujeción es la variable primaria"),
 ("pasamuros y refuerzos locales","PAR","WRC 107 da la tensión; **no está declarado CUÁNTOS ni para qué**"),
 ("protección contra pandeo externo","DET","P_cr con knockdown 0,2 → margen ×4"),
]),
("METROLOGÍA",[
 ("placa de fiduciales 5 anillos × 5 a 72°","DET","D-664/667 · separa el 4θ"),
 ("campo útil redondo r ≤ 88 mm","DET","un reparto circular no alcanza esquinas cuadradas"),
 ("asiento cinemático de 3 puntos","DET","repetibilidad submicrométrica"),
 ("lector óptico a L ≥ 1.500 mm","DET","D-613 · σ = 0,52 µm, al nivel EURAMET"),
 ("corrección de paralaje por altura","DET","f.19 · 400 µm → 0,03 µm"),
 ("ILUMINACIÓN del lector","HUECO","**nada la determina, y el iris exige condiciones declaradas**"),
 ("referencia térmica del campo","HUECO","**ΔT dilata la cáscara 15-21 µm y no hay sensor de campo**"),
 ("giro motorizado de la placa (M3′)","PAR","el protocolo exige 5 posiciones; el mecanismo no está"),
]),
("CUSTODIA",[
 ("sello elastomérico","DET","EPDM/FKM · permeación presupuestada · **NO es la custodia**"),
 ("báscula / enclavamiento de masa","DET","criterio 3 + B2"),
 ("testigo de micro-vulneración","DET","B4 · taladro de 0,5 mm"),
 ("registrador de choque ≥2.000 muestras/s","DET","ISTA · 0,5-500 Hz · pre-disparo 20 %"),
 ("registrador térmico de dos caras","PAR","ΔT ≤ 50 °C declarado; **el sensor no está especificado**"),
 ("compromiso criptográfico del registro","DET","ciego.py · SHA-256"),
]),
("SOPORTE VITAL",[
 ("depurador de CO₂","DET","OBLIGATORIO por encima de 16 min (f.29)"),
 ("suministro de O₂","DET","banda 145-155 mmHg"),
 ("control de T y humedad","DET","OCHMO [V2 6012]"),
 ("ventilación y circulación","DET","OCHMO [V2 6107] · evitar bolsas de CO₂ y térmicas"),
 ("sensores continuos P/HR/T/ppO₂/ppCO₂","DET","OCHMO [V2 6020] por compartimento aislable"),
 ("ENERGÍA para todo lo anterior","HUECO","**nada la determina. Sin ella no funciona ningún elemento de esta lista**"),
 ("gestión de residuos y fluidos","HUECO","**a partir de 1 h de acto es inevitable y no está**"),
]),
("FUEGO",[
 ("sensor de O₂ con alarma a 23,5 %","DET","NFPA 99 · instantáneo, sin ventana"),
 ("diluvio activo en ≤ 3 s","DET","NFPA 99 Class A"),
 ("materiales no sintéticos, lubricantes O₂-compatibles","DET","NFPA 99 / NFPA 53"),
 ("detección de precombustión","DET","OCHMO [V2 6024] tiempo real"),
 ("BIBS · respiración independiente en humo","PAR","IMCA lo exige; **no está en nuestras 42 afirmaciones**"),
]),
("OCUPANTE",[
 ("sujeción tipo Eiband, 25-50 lb de tensión","DET","la variable primaria"),
 ("asiento reclinado","DET","exigido por ≥ 9 g"),
 ("traje anti-g","DET","exigido por ≥ 9 g"),
 ("captura biométrica de iris","DET","condiciones declaradas + FRR con su n"),
 ("apertura desde dentro, sin herramienta, ≤ 60 s","DET","IMCA / FAA"),
 ("COMUNICACIÓN con el exterior","HUECO","**nada la determina. Y OCHMO exige alertar 'local y remotamente'**"),
 ("instrumentación visible para el ocupante","HUECO","**OCHMO [V2 6021] exige mostrar en tiempo real. No hay pantalla**"),
]),
("INTERFAZ CON EL EXTERIOR",[
 ("interfaz de propulsión","HUECO","**el marco nunca dice cómo se empuja la cabina**"),
 ("control de actitud","HUECO","**una cabina que gira en tránsito cambia el vector g sobre el ocupante**"),
 ("DISIPACIÓN TÉRMICA EN TRÁNSITO","HUECO","**44× el Apolo en Londres-Sídney. Rompe un caso ya 'resuelto'**"),
 ("interfaz de datos con la estación","PAR","el contrato viaja como descripción; el canal no está"),
 ("suministro de energía en estación","HUECO","**ver ENERGÍA**"),
]),
]
if __name__=="__main__":
    from collections import Counter
    tot=Counter(); print("\n  "+"="*104)
    for blo,it in E:
        c=Counter(e[1] for e in it); tot.update(c)
        print(f"\n  {blo}   ({c['DET']} determinados · {c['PAR']} parciales · {c['HUECO']} HUECOS)")
        print("  "+"-"*104)
        for n,s,por in it:
            m={"DET":"·","PAR":"~","HUECO":"**X**"}[s]
            print(f"  {m:>5} {n:<48}{por}")
    N=sum(tot.values())
    print("\n  "+"="*104)
    print(f"  TOTAL {N} elementos:  **{tot['DET']} determinados ({100*tot['DET']/N:.0f} %)** · "
          f"{tot['PAR']} parciales ({100*tot['PAR']/N:.0f} %) · **{tot['HUECO']} HUECOS ({100*tot['HUECO']/N:.0f} %)**")
    hue=[(b,n) for b,it in E for n,s,_ in it if s=="HUECO"]
    from collections import defaultdict
    d=defaultdict(list); [d[b].append(n) for b,n in hue]
    print(f"\n  LOS {len(hue)} HUECOS, POR BLOQUE:")
    for b,ns in d.items(): print(f"    {b:<26}{len(ns)}   {' · '.join(ns)}")
