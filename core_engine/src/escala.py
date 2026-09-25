"""
ESCALA EVIDENCIAL DEL MARCO  ·  D-662 (regla multiplicativa) + D-663 (15 apoyos nuevos)

  duda(condicion) = PROD (1 - w_i)  sobre LINEAS INDEPENDIENTES,  tope 0,99
  COBERTURA(capa) = media de sus condiciones    <- cuanta literatura la toca
  CAPA (regla 4)  = MINIMO de sus condiciones   <- lo que de verdad vale
  MARCO           = MINIMO sobre capas

pesos:  MED_AJ .95  MED_PRO .85  DER .70  LIT .60  DECL .30  NADA 0
La corroboracion matematica NO es independiente: factor 0,8 sobre el residuo.
"""
MED_AJ, MED_PRO, DER, LIT, DECL = .95, .85, .70, .60, .30

def cred(lineas, mate=False):
    duda = 1.0
    for w in lineas: duda *= (1 - w)
    c = min(1 - duda, 0.99)
    if mate: c = min(c + (0.99 - c) * 0.2, 0.99)   # la mate corrobora, no independiza
    return c

# ---- cada condicion: (nombre, [lineas independientes], corroboracion_matematica) ----
CAPAS = {
"1 · marco teorico": [
  ("algebra del contrato A=sqrt(Om_imp/Om_acto)", [MED_PRO, MED_PRO, MED_PRO], True),
  ("ley A = K_d sqrt(a/sigma)",                   [DER, MED_PRO, MED_PRO, MED_PRO, MED_AJ], True),
  ("psi = g K^4 / A^4 (instantaneo XOR certificado)", [DER, MED_PRO], True),
  ("g = 3 + (3 - dim grupo simetria)",            [DER, MED_AJ, MED_AJ], True),   # +BOP/MSSD simetria
  ("n_min = d n - d(d+1)/2",                      [DER, MED_PRO, MED_AJ], True),  # +Maxwell 1864
  ("identidad != transmision (capacidad ID)",     [MED_AJ, MED_AJ, DER, MED_AJ], True), # +Ahlswede-Dueck, +Daugman
  ("phi: clase 1 phi=0 / clases 2-3 phi=1",       [DER, MED_PRO, LIT], False),
],
"2 · instrumento": [
  ("los 5 criterios + identidad",                 [MED_PRO, MED_PRO, MED_AJ], False),
  ("suelo por RE-COLOCACION (regla 413)",         [MED_PRO, MED_PRO], False),
  ("delta medido, ~1/sqrt(n) (regla 414)",        [MED_PRO, DER], True),
  ("nunca magnitudes inconmensurables (415)",     [MED_PRO, MED_AJ], False),
  ("puntos de ruptura: mediana 50%, p98 2%, id 1/n", [DER, MED_AJ], True),
  ("ciego de verdad (compromiso SHA-256, 8/8)",   [MED_PRO, MED_AJ, MED_AJ], False), # +PT ciego vs declarado
  ("riesgo del consumidor declarado",             [DER, MED_AJ], True),
  ("tasa de falsa aceptacion con su n (3e6 obs)", [MED_PRO, MED_AJ, DER], True),  # D-666
],
"3 · maquina": [
  ("software 4 modos ejecutable",                 [MED_PRO], False),
  ("montaje + plano cerrados",                    [MED_PRO, LIT], False),
  ("lector optico: incertidumbre alcanzable",     [MED_AJ, MED_AJ, MED_PRO], False), # +EURAMET ball plate 25 bolas
  ("emparejado fiducial por asignacion, no orden",[MED_PRO, DER], True),
  ("GATE-0 alpha: umbral conjunto (alpha,C)",     [MED_PRO, MED_AJ, MED_AJ], True),
  ("alpha anclado al nucleo GP del gremio",        [DER, MED_AJ], True),            # D-668
  ("M3' PUEDE separar el 4t (placa de anillos)",  [MED_PRO, MED_AJ, MED_AJ], True), # D-664/667
  ("los fiduciales ENCIERRAN el campo",           [MED_PRO, DER], True),            # D-667
  ("error comun: tres planos de Whitworth",       [MED_AJ, MED_AJ], False),        # +BIPM -35ug modo comun real
  ("paralaje por altura de asiento CORREGIDO",    [DER, MED_PRO], True),           # D-663
  ("GATE-0 en NUESTRO banco (25 EUR)",            [], False),                      # <- solo banco
],
"4 · custodia": [
  ("transporte: 109 g sujeto vs 3 cm suelto",     [MED_PRO, MED_AJ], False),
  ("perturbacion de preparacion (25 nm, 27 ug)",  [MED_PRO, MED_AJ], False),
  ("choque = (pico, duracion), no pico solo",     [MED_AJ, MED_AJ, DER], True),    # +ISTA: 10 ms a 600 ms medidos
  ("estanqueidad: O2 por el elastomero",          [MED_AJ, DER], True),            # tabla + margen calculado: 15-246 anos
  ("sello frente a atacante experto",             [MED_AJ], False),                # Johnston: 100% batidos
  ("la custodia NO la da el sello, la da remedir",[DER, MED_PRO, MED_AJ, MED_AJ], True), # +Johnston: "deben ser inspeccionados"
  ("inspeccion de MAQUINA, sin la variable humana",[MED_AJ, MED_PRO], False),      # D-666
  ("B1-B4 en nuestro banco (80 EUR)",             [], False),
],
"5 · acto": [
  ("precedente historico de acto certificado",    [MED_AJ, MED_AJ, MED_AJ], False),# Abu Simbel+contenedor+BIPM
  ("re-verificacion POST-transporte, cifra",      [MED_AJ, MED_AJ], False),        # BIPM No.70: 5 ug/kg
  ("acuerdo inter-estacion eps <= sigma sqrt(2d)",[DER, MED_AJ], True),
  ("contrato: A>1 Y FAR<=1e-6 afirmable",         [MED_PRO, MED_AJ], True),        # D-666
  ("tolerancia de montaje real (MAA +-0,1 mm)",   [MED_AJ, LIT], False),           # +wing-box (cifras sin verificar)
  ("controles negativos fallan 48/48",            [MED_PRO, MED_PRO], False),
  ("multiplicidad efectiva de la asignacion",     [DER], False),                   # D-668: abierto, x2500 = FAR 2,5e-3
  ("LO HEMOS EJECUTADO NOSOTROS (534 EUR)",       [], False),
],
"6 · humano": [
  ("humano en volumen sellado, dias",             [MED_AJ, MED_AJ, MED_AJ], False),# hiperbarico+ABCS+Mars500
  ("envolvente fisiologica P y T, medida",        [MED_AJ, MED_AJ, MED_AJ], False),# +OCHMO 13,5 psi/min, 34,5-103 kPa
  ("monitorizacion continua: resolucion real",    [MED_AJ, MED_AJ], False),        # OCHMO [V2 6020] + submarinos
  # D-670 · el humano NO se lee: es CARGA dentro de un volumen cerrado, no unidad medida.
  # La cabecera del programa lo decia desde el principio: "custodia continua de
  # volumenes cerrados". Leer tejido a 100 um NO es condicion de nuestra via.
  ("identidad del OCUPANTE a la llegada",         [MED_AJ, MED_AJ], False),        # Daugman: FMR < 5e-12
  ("el ocupante es CARGA, no unidad medida",      [DER, MED_PRO], True),
  ("la carga VIVA flexa la cascara: presupuestado",[DER, MED_PRO], True),          # 29 um con pared 5 mm
  ("clase 3 -> phi=1 obliga a mover la masa",     [DER, MED_PRO], True),
],
}

if __name__ == "__main__":
    res = {}
    for capa, conds in CAPAS.items():
        vals = [cred(l, m) for _, l, m in conds]
        res[capa] = sum(vals)/len(vals)
        print(f"\n{capa}   ->  {res[capa]*100:5.1f} %")
        for (n,_,_), v in zip(conds, vals):
            print(f"    {v*100:5.1f} %  {n}")
    print("\n" + "="*70)
    print(f"  {'capa':<22}{'cobertura':>11}{'REGLA 4':>10}")
    for capa, conds in CAPAS.items():
        v = [cred(l,m) for _,l,m in conds]
        print(f"  {capa:<22}{sum(v)/len(v)*100:10.1f}%{min(v)*100:9.1f}%")
    m = min(min(cred(l,m) for _,l,m in c) for c in CAPAS.values())
    print(f"\n  MARCO (regla 4 hasta el fondo) = {m*100:.1f} %")
