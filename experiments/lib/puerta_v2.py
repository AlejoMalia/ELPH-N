"""Puerta v2 (D-103, cerrada en D-120): comprobaciones ESTATICAS anadidas al nivel 0.

Se construye SOLO con lo que los registros sostienen. Dos reglas propuestas, una
aceptada y una **rechazada por los datos**.

RECHAZADA — saturacion de la lectura
    Se propuso `si saturacion > theta -> RECHAZAR`. Medido sobre 54 circuitos:
    **r = -0,042** entre saturacion y sigma. El circuito de MAYOR saturacion
    (h2_INF, 0,383) tiene una de las sigmas mas BAJAS (0,0016) y es valido. De
    los 5 circuitos con saturacion > 0,10, solo 2 se invalidaron.
    **Una puerta asi rechazaria h2_INF y m3_MB, que son validos. NO se anade.**

ACEPTADA — inhibitorias en la via
    Si ninguna neurona de la via es inhibitoria, M2 (topologia + signo) construye
    **exactamente la misma matriz** que M1: el signo solo invierte los pesos de
    fuentes inhibitorias. No es una correlacion, es **identidad**, y por eso no
    necesita apoyo estadistico.
    Consecuencia: el efecto del signo **no es medible** en ese circuito, y un
    Delta(M1) == Delta(M2) NO es un hallazgo, es una tautologia.
    Se emite **ADVERTENCIA**, no rechazo: el circuito sigue sirviendo para todo
    lo demas.
"""
__all__ = ['revisar_v2', 'validar_sustrato', 'sigma_de_medicion',
           'registrar_saturacion', 'AvisoPuerta']

UMBRAL_I_BAJO = 0.02        # 2 % de inhibitorias en la via: signo casi mudo


class AvisoPuerta(UserWarning):
    pass


def validar_sustrato(pre, post, inyeccion, lectura, minimo=1, etiqueta='via',
                     indirecta_declarada=False):
    """RECHAZA una tarea sin camino anatomico de la inyeccion a la lectura (D-122).

    El nivel 0 comprobaba que inyeccion y lectura no estuvieran vacias ni se
    solaparan, **pero no que existiera camino entre ellas**. D-121 lo destapo:
    la tarea EPG->ER dentro de UN hemisferio del complejo central tiene **0
    aristas** (la proyeccion es contralateral). El experimento corrio 16 minutos
    y devolvio Psi = 0,0000 +- 0,0000 -- que no es un hallazgo, es la ausencia
    de sustrato.

    Ya existia el precedente: MB y escape tienen cero aristas de vuelta, y ahi
    se decidio a mano no invertirlas. **A mano no basta: se codifica.**

    Cuenta aristas DIRECTAS inyeccion -> lectura. Un camino indirecto puede
    existir y el aviso seguir siendo pertinente, por eso el minimo es
    configurable y el mensaje dice cuantas hay.
    """
    iny, lec = set(inyeccion), set(lectura)
    n = sum(1 for a, b in zip(pre, post) if a in iny and b in lec)
    if indirecta_declarada:
        # D-126: hay tareas donde la AUSENCIA de via directa es el diseno, no un
        # fallo -- T0 del gusano se eligio asi a proposito para medir vias
        # indirectas. La puerta no las prohibe: obliga a DECLARARLO, para que
        # nadie se encuentre un Psi = 0 sin saber por que.
        print(f'[NIVEL 0] {etiqueta}: {n} aristas directas, via INDIRECTA declarada')
        return n
    if n < minimo:
        raise ValueError(
            f'{etiqueta}: solo {n} aristas directas de inyeccion ({len(iny)} nodos) '
            f'a lectura ({len(lec)} nodos). La tarea NO tiene sustrato anatomico: '
            f'Psi sera 0 y no significara nada. Minimo exigido: {minimo}.')
    return n


def sigma_de_medicion(resultados, aleatorizadas, etiqueta='sigma'):
    """sigma de las condiciones de MEDIDA, centralizada (cierra D-092).

    D-092 fue el quinto fallo de instrumento y causo **dos invalidaciones
    falsas**: cuatro scripts clasificaban las condiciones por prefijo de nombre
    (`not k.startswith('CTRL_')`), y M0 esta aleatorizado pero no se llama CTRL.
    El arreglo se copio a mano en cada fichero como `ALEATORIZADAS = {...}`,
    asi que un experimento nuevo puede olvidarlo y repetir el fallo.

    Aqui se exige la lista **explicita**: si no se declara, no se calcula.

    `resultados`    {condicion: {'delta_std':..., 'psi_b_std':...}}
    `aleatorizadas` conjunto de condiciones que NO cuentan para C2, porque su
                    dispersion es intrinseca al diseno (M0, CTRL_*, shuffles).
    """
    if aleatorizadas is None:
        raise ValueError(
            f'{etiqueta}: hay que declarar EXPLICITAMENTE que condiciones estan '
            f'aleatorizadas. Clasificarlas por el nombre fue D-092 y costo dos '
            f'invalidaciones falsas.')
    al = set(aleatorizadas)
    sospechosas = {k for k in resultados
                   if ('shuffle' in k.lower() or 'ctrl' in k.lower()
                       or 'sin_topologia' in k.lower()) and k not in al}
    if sospechosas:
        raise ValueError(
            f'{etiqueta}: {sorted(sospechosas)} parecen aleatorizadas y NO se '
            f'han declarado. Declararlas o justificar por que cuentan para C2.')
    medicion = [k for k in resultados if k not in al]
    if not medicion:
        raise ValueError(f'{etiqueta}: no queda ninguna condicion de medida')
    return max(max(resultados[k].get('delta_std', 0.0),
                   resultados[k].get('psi_b_std', 0.0)) for k in medicion)


def registrar_saturacion(saturacion, etiqueta='circuito'):
    """La saturacion se REGISTRA como metadato. NUNCA veta.

    Hipotesis refutada (D-120): `saturacion > theta -> RECHAZAR`. Sobre 54
    circuitos, r = -0,042 entre saturacion y sigma; el de mayor saturacion
    (h2_INF, 0,383) tiene una de las sigmas mas bajas (0,0016) y es valido.
    Se guarda para analisis posterior, por si algun dia otra variable la
    convierte en util combinada -- pero como veto esta cerrada.
    """
    return {'saturacion': float(saturacion),
            'uso': 'metadato; refutada como criterio de rechazo (D-120)'}


def revisar_v2(nt_por_nodo, via, inhibitorios=('gaba', 'glutamate'),
               etiqueta='circuito', exige_signo=True):
    """Comprobaciones estaticas de la puerta v2. Devuelve lista de avisos.

    `nt_por_nodo`  {id: neurotransmisor}
    `via`          ids de las neuronas que participan en la via medida
                   (inyeccion + lectura + intermedias declaradas)

    NO rechaza nada: el nivel 0 ya rechaza por cobertura, canales y bateria.
    Esto anade lo que faltaba -- decir cuando una PREGUNTA no es contestable
    con ese circuito, aunque el circuito este sano.
    """
    avisos = []
    if not exige_signo:
        # matiz del investigador: si la prediccion bajo prueba no necesita el
        # signo, que la via no tenga inhibitorias no afecta a nada.
        return avisos
    via = [v for v in via if v in nt_por_nodo]
    if not via:
        return [f'{etiqueta}: la via no tiene ningun nodo con NT anotado']
    inh = sum(1 for v in via if str(nt_por_nodo[v]).lower() in inhibitorios)
    frac = inh / len(via)
    if inh == 0:
        avisos.append(
            f'{etiqueta}: CERO inhibitorias en la via ({len(via)} nodos). '
            f'M2 es IDENTICA a M1 por construccion: el efecto del signo NO es '
            f'medible aqui, y Delta(M1)==Delta(M2) seria una tautologia.')
    elif frac < UMBRAL_I_BAJO:
        avisos.append(
            f'{etiqueta}: solo {inh}/{len(via)} inhibitorias en la via '
            f'({100*frac:.1f} %). El efecto del signo sera casi mudo; '
            f'interpretar un Delta pequeno con cautela.')
    return avisos
