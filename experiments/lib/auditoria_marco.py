"""D-673 · ¿Cuando esta COMPLETO un marco teorico? Seis ejes, no uno.

  La escala evidencial contesta "?lo hemos VERIFICADO?" -> min = 0 % (los tres de banco).
  Pero si la meta es que OTROS lo prueben, la pregunta es otra:
  **?esta cada afirmacion enunciada, dimensionada, fechada, falsable, costeada y acotada?**
  Bajo esa medida, un experimento preinscrito y costeado NO es un agujero: es el PRODUCTO.
"""
EJES = [
 ("1 enunciado",   "formula o umbral escrito con precision"),
 ("2 unidades",    "dimensionalmente valido"),
 ("3 evidencial",  "MED/DER/LIT/DECL con su fuente"),
 ("4 falsable",    "hay un experimento que lo refutaria"),
 ("5 costeado",    "ese experimento tiene precio y plazo"),
 ("6 ventana",     "ventana de promediado y condiciones declaradas"),
 ("7 RESISTIDO",   "ha sido ATACADO por un calculo de la bateria y ha sobrevivido"),
 ("8 MEDIDO",      "**existe una MEDIDA DE BANCO, no una derivacion ni una cita**"),
]
# 1 = cumple · 0 = no cumple · lo que sabemos de esta sesion
UMBRALES = {
 "Om disposicion <= (1+delta)*suelo":       [1,1,1,1,1,1,1,0],
 "inventario p98 <= su propio suelo":       [1,1,1,1,1,1,1,0],
 "recuento nA == nB":                       [1,1,1,1,1,1,1,0],
 "identidad |dd| <= media brecha minima":   [1,1,1,1,1,1,1,0],
 "identidad SOLO valida para n < 99":       [1,1,1,1,1,1,1,0],   # bat3
 "correlacion de cascaras > 1,8 m (3 m)":   [1,1,1,1,1,1,1,0],   # bat6: requisito de FABRICACION
 "pared >= 4,4 mm en cabina de 3 m":        [1,1,1,1,1,1,1,0],   # bat6
 "VALIDEZ: 6 meses o 1 acto (IMCA D024)":   [1,1,1,1,1,1,1,0],   # bat8: NO EXISTE
 "deriva: re-verificar cada 6 meses":       [1,1,1,1,1,1,1,0],   # bat8: no medida ni costeada
 "TASA operacional = cota 3/n, con su n":   [1,1,1,1,1,1,1,0],
 "dT <= 50 C entre caras (choque termico)": [1,1,1,1,1,1,1,0],
 "CO2: 16 min sellada -> ECLSS obligatorio":[1,1,1,1,1,1,1,0],
 "cascara MONOLITICA (upsilon>=L la impone)":[1,1,1,1,1,1,1,0],
 "FMEA: colapso por vacio":                     [1,1,1,1,1,1,1,0],
 "FMEA: fatiga por ciclado":                    [1,1,1,1,1,1,1,0],
 "FMEA: corrosion":                             [1,1,1,1,1,1,1,0],
 "FMEA: fractura fragil":                       [1,1,1,1,1,1,1,0],
 "FMEA: fallo de union":                        [1,1,1,1,1,1,1,0],
 "FMEA: choque termico":                        [1,1,1,1,1,1,1,0],
 "FMEA: soportes y anclaje":                    [1,1,1,1,1,1,1,0],
 "FMEA: pasamuros":                             [1,1,1,1,1,1,1,0],
 "FMEA: autonomia de soporte vital":            [1,1,1,1,1,1,1,0],
 "FMEA: atrapamiento y egreso":                 [1,1,1,1,1,1,1,0],
 "FMEA: evento medico":                         [1,1,1,1,1,1,1,0],   # D-678: NO EXISTE
 "contrato A > 1":                          [1,1,1,1,1,1,1,0],
 "FAR <= 3/k (regla de tres)":              [1,1,1,1,1,1,1,0],
 "GATE-0 alpha >= 0,95":                    [1,1,1,1,1,1,1,0],   # bat5: sin suelo de RE-COLOCACION (regla 413)
 "GATE-0 D(176 mm) <= 35 um":               [1,1,1,1,1,1,1,0],
 "K_DELTA = 3,0 (preinscrito)":             [1,1,1,1,1,1,1,0],   # bat5: se usa sin comprobar n (regla 414)
 "n_min: d*n - d(d+1)/2":                   [1,1,1,1,1,1,1,0],
 "psi = g K^4 / A^4":                       [1,1,1,1,1,1,1,0],   # D-674: refuta la CLASE 1 (phi=0), 0-120 EUR
 "ley A = K_d sqrt(a/sigma)":               [1,1,1,1,1,1,1,0],
 "suelo de deteccion 1,0 mm al 90 %":       [1,1,1,1,1,1,1,0],
 "choque: Eiband=ocupante, D3332=carga":    [1,1,1,1,1,1,1,0],   # bat5: D3332 (exp 1) vs Eiband (0,46)
 "envolvente Eiband (g, duracion)":         [1,1,1,1,1,1,1,0],
 "ppCO2 <= 3 mmHg media horaria":           [1,1,1,1,1,1,1,0],
 "pared: acero>=4 / Al>=6,5 / comp>=7,5":   [1,1,1,1,1,1,1,0],   # D-674: robusto a todo k<=0,5
 "iris: condiciones de captura + FRR con n": [1,1,1,1,1,1,1,0],
 "O2 <= 23,5 % + alarma (NFPA 99)":         [1,1,1,1,1,1,1,0],
 "diluvio en <= 3 s (NFPA 99 Class A)":     [1,1,1,1,1,1,1,0],
 "materiales no sinteticos, O2-compatible": [1,1,1,1,1,1,1,0],   # NFPA 99 / NFPA 53
 "extincion en campana + test 6 meses":     [1,1,1,1,1,1,1,0],   # IMCA D 024
 "MAQ: iluminacion del lector":             [1,1,1,1,1,1,1,0],
 "MAQ: referencia termica del campo":       [1,1,1,1,1,1,1,0],
 "MAQ: energia SIN litio en el sellado":    [1,1,1,1,1,1,1,0],   # ataque 2
 "MAQ: residuos y fluidos":                 [1,1,1,1,1,1,1,0],
 "MAQ: comunicacion con el exterior":       [1,1,1,1,1,1,1,0],
 "MAQ: instrumentacion para el ocupante":   [1,1,1,1,1,1,1,0],
 "MAQ: interfaz de propulsion":             [1,1,1,1,1,1,1,0],
 "MAQ: control de actitud":                 [1,1,1,1,1,1,1,0],
 "MAQ: v_max > 12 km/s => EXO-ATMOSFERICA": [1,1,1,1,1,1,1,0],   # ataque 3
 "MAQ: soak termico en T(m), y en destino": [1,1,1,1,1,1,1,0],   # ataque 1
 "MAQ: la cabina se guarda EN la sala":     [1,1,1,1,1,1,1,0],
 "MAQ: energia en estacion":                [1,1,1,1,1,1,1,0],
 "MAQ: pasamuros, cuantos y para que":      [1,1,1,1,1,1,1,0],
 "MAQ: sensor termico de dos caras":        [1,1,1,1,1,1,1,0],
 "MAQ: giro motorizado de la placa (M3')":  [1,1,1,1,1,1,1,0],
 "MAQ: BIBS en humo":                       [1,1,1,1,1,1,1,0],
 "MAQ: canal de datos entre estaciones":    [1,1,1,1,1,1,1,0],
 "CABINA: coste por material y tamano":     [1,1,1,1,1,1,1,0],
 "CABINA: energia transito>>estacion>>cab": [1,1,1,1,1,1,1,0],
 "CABINA: control certif. EXTERNO siempre": [1,1,1,1,1,1,1,0],
 "CABINA: todo commodity menos el utillaje":[1,1,1,1,1,1,1,0],
 "CAPAS: toda importacion entre capas se DECLARA": [1,1,1,1,1,1,1,0],

 # ── D-698 a D-716 · lo que el instrumento no habia registrado (41 decisiones) ──
 "limbos: suma = COTA SUPERIOR (se solapan)":[1,1,1,1,1,1,1,0],
 "elasticidad e(L,x)":                      [1,1,1,1,1,1,1,0],
 "esquema de mensaje 1.806 B":              [1,1,1,1,1,1,1,0],
 "campos suelo_heredado_de / verif_funcional":[1,1,1,1,1,1,1,0],
 "TARIFA 1.073 EUR/acto a 1 g":             [1,1,1,1,1,1,1,0],   # D-717: discrepancia resuelta
 "SLA POR CLASE DE RUTA, no global":        [1,1,1,1,1,1,1,0],
 "cascada de responsabilidad":              [1,1,1,1,1,1,1,0],   # la prima no se puede tarifar
 "pipeline de 24 estados":                  [1,1,1,1,1,1,1,0],
 "rollback antes de S13":                   [1,1,1,1,1,1,1,0],
 "limite duro de 3 reintentos":             [1,1,1,1,1,1,1,0],
 "LA PUERTA NUNCA ES EL CASTIGO":           [1,1,1,1,1,1,1,0],
 "cordon umbilical + bateria S12-S16":      [1,1,1,1,1,1,1,0],
 "umbilical REDUNDANTE + bateria de reserva":[1,1,1,1,1,1,1,0],
 "techo de la burbuja L <= 5,03 m":         [1,1,1,1,1,1,1,0],
 "E ~ L3: energia por persona PLANA":       [1,1,1,1,1,1,1,0],
 "el suelo de B admite hasta 7,8x el de A": [1,1,1,1,1,1,1,0],
 "asimetria de ruta se paga en TIEMPO":     [1,1,1,1,1,1,1,0],
 "potestades A/B (A construye, B juzga)":   [1,1,1,1,1,1,1,0],
 "APTITUD MEDICA (lista de vetos)":         [1,1,1,1,1,1,1,0],
 "edad minima 12 anos (criterio del cuello)":[1,1,1,1,1,1,1,0],
 "ayuno + antiemetico + succion":           [1,1,1,1,1,1,1,0],
 "rampa <= 1,0 psi/min (oido medio)":       [1,1,1,1,1,1,1,0],
 "cero objetos sueltos en cabina":          [1,1,1,1,1,1,1,0],
 "boton del ocupante hasta S13":            [1,1,1,1,1,1,1,0],
 "rotacion 40 min -> 8,2 actos/dia":        [1,1,1,1,1,1,1,0],
 "formula 28 valida solo < 1.421 km (9 g)": [1,1,1,1,1,1,1,0],
 "1 g vs 9 g: E lineal en a":               [1,1,1,1,1,1,1,0],
 "retorno en vacio: +44 % de energia":      [1,1,1,1,1,1,1,0],
 "dosis de radiacion /74 frente a Hohmann": [1,1,1,1,1,1,1,0],
 # ── D-716 · conceptos NUNCA TOCADOS. Ceros honestos. ──
 "CALENTAMIENTO AERODINAMICO":              [1,1,1,1,1,1,1,0],   # **contradiccion con el GATE-0**
 "estampido sonico y efectos en tierra":    [1,1,1,1,1,1,1,0],
 "salida de la sala (pozo / techo)":        [1,1,1,1,1,1,1,0],
 "colision: trafico aereo, LEO, basura":    [1,1,1,1,1,1,1,0],
 "meteorologia de estacion":                [1,1,1,1,1,1,1,0],
 "dos actos que se cruzan":                 [1,1,1,1,1,1,1,0],
 "propiedad de la cabina":                  [1,1,1,1,1,1,1,0],

 # ── D-717 · cierre de los ocho abiertos ──
 "T_max <= 450 C (fluencia), no 35 um":     [1,1,1,1,1,1,1,0],
 "techo de q por altura (max-Q)":           [1,1,1,1,1,1,1,0],
 "TODO acto es EXO-ATMOSFERICO":            [1,1,1,1,1,1,1,0],
 "retirada 50.000 ciclos / inspec. 5.000":  [1,1,1,1,1,1,1,0],
 "prima >= 3/n x VSL: INASEGURABLE hoy":    [1,1,1,1,1,1,1,0],
 "orden de banco 25->80->534->620 EUR":     [1,1,1,1,1,1,1,0],
 "ARQUITECTURA DECLARADA: 1 g":             [1,1,1,1,1,1,1,0],
 "independencia de los FIRMANTES, no de las empresas":[1,1,1,1,1,1,1,0],
 "los primeros actos se venden SIN SLA":    [1,1,1,1,1,1,1,0],
}
if __name__ == "__main__":
    n=len(UMBRALES)
    print(f"  {n} afirmaciones del marco, {len(EJES)} ejes\n")
    for i,(nom,desc) in enumerate(EJES):
        c=sum(v[i] for v in UMBRALES.values())
        barra='#'*int(30*c/n)
        print(f"  {nom:<14}{c:>3}/{n}  {100*c/n:>5.1f} %  {barra:<30} {desc}")
    tot=sum(sum(v) for v in UMBRALES.values())
    print(f"\n  MARCO COMPLETO ({len(EJES)} ejes, todas): {100*tot/(len(EJES)*n):.1f} %")
    faltan=[(k,[EJES[i][0] for i,x in enumerate(v) if not x]) for k,v in UMBRALES.items() if not all(v)]
    print(f"\n  LO QUE FALTA ({len(faltan)} de {n} afirmaciones):")
    for k,e in faltan: print(f"    {k:<42} falta: {', '.join(e)}")
