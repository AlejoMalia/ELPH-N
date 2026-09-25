"""Formulas de las fases III a VI del Pilar I, derivadas de registros ya medidos.

Ninguna de estas funciones simula nada: todas salen de datos que el programa ya
tiene guardados, o de constantes fisicas publicadas. Es la aplicacion del
principio del investigador -- no gastar computo para averiguar lo que los
registros ya contienen (D-115).

  III  identidad y criterio de exito   -> resolucion_identidad()
  IV   estado fuera del equilibrio     -> ventana_ensamblado()
  V    escala y composicion            -> extrapolacion_tasa()
  VI   cuerpo / bucle sensorimotor     -> canales_interfaz()
"""
import math

import numpy as np

__all__ = ['resolucion_identidad', 'id_operativa', 'BATERIA_ACEPTACION',
           'ventana_ensamblado', 'extrapolacion_tasa', 'canales_interfaz']


# ---------------------------------------------------------------------------
# FASE III - IDENTIDAD
# ---------------------------------------------------------------------------

def resolucion_identidad(senal_entre_individuos, ruido_metodologico,
                         margen_exigido=3.0):
    """¿Puede el instrumento distinguir dos individuos? (Fase III, P-3)

    Un criterio de exito del tipo «la copia vale si Δ < umbral» solo tiene
    sentido si el instrumento separa «otro individuo» de «mismo individuo,
    otro preprocesado». M-7 midio las dos cosas y la respuesta fue NO:

        senal entre individuos (♀ vs ♂, densidad igualada) : 0,0975
        ruido metodologico (mismo ♂, otro umbral)          : 0,2135
        SNR                                                : 0,46

    Con SNR < 1 el criterio es inaplicable, por mucho que se afine el umbral.

    Devuelve (snr, veredicto, reduccion_necesaria).
    """
    if ruido_metodologico <= 0:
        raise ValueError('el ruido debe ser positivo')
    snr = senal_entre_individuos / ruido_metodologico
    if snr >= margen_exigido:
        return snr, 'CRITERIO APLICABLE', 1.0
    if snr >= 1.0:
        return snr, f'INSUFICIENTE: hay senal pero sin margen {margen_exigido}:1', \
               margen_exigido / snr
    return snr, 'INAPLICABLE: el ruido supera a la senal', margen_exigido / snr


BATERIA_ACEPTACION = {
    'quimiosensorial_a_mando': ('anfidiales', 'mando'),
    'mecanosensorial_a_mando': ('tacto', 'mando'),
    'integracion_a_motor':     ('integradoras', 'motor_cabeza'),
    'visceral_autonoma':       ('faringeas_I', 'faringeas_M'),
}
"""Bateria de aceptacion (D-126). Instancia para *C. elegans* de la especificacion.

**Elegida por FUNCION, antes de mirar ningun Delta.** Cuatro papeles que un
sistema nervioso tiene que cumplir para que su replica se acepte:

  1. entrada quimiosensorial -> decision motora
  2. entrada mecanosensorial -> decision motora   (otra modalidad, misma salida)
  3. integracion -> salida motora                 (el otro extremo del arco)
  4. circuito visceral autonomo                   (no depende del arco anterior)

**NO es el menu exploratorio de E-2.** E-2 barre siete tareas para encontrar el
peor caso; esto son cuatro tareas de producto, fijas, con sustrato directo
verificado (15, 26, 16, 48 y 72 aristas respectivamente) por `validar_sustrato`
ANTES de medir nada.

**T0 queda FUERA a proposito**: tiene cero vias directas y se diseno asi para
investigar vias indirectas. Es una tarea de investigacion, no de aceptacion.
"""


def id_operativa(resultados, umbrales, bateria=None):
    """Identidad operativa: pasa / no pasa la bateria de aceptacion (D-126).

        ID_op = 1  si la instancia supera el umbral en TODAS las tareas de B
                0  si falla alguna

    No compara «almas»: compara **aceptacion de replica**. Es la unica magnitud
    de identidad que este programa autoriza, y solo porque no pretende medir
    identidad personal -- que queda [FUERA] por decision P3-C.

    `resultados` {tarea: Psi_obtenida}
    `umbrales`   {tarea: minimo exigido}, preinscritos bajo C-calibrado
    `bateria`    claves exigidas; por defecto BATERIA_ACEPTACION

    Devuelve (id_op, detalle) con el resultado por tarea, para que un fallo diga
    CUAL fallo y no solo que fallo.
    """
    b = list(bateria if bateria is not None else BATERIA_ACEPTACION)
    faltan = [t for t in b if t not in resultados]
    if faltan:
        raise ValueError(f'la bateria exige {b}; faltan resultados de {faltan}. '
                         f'Una bateria incompleta no da ID_op: da nada.')
    sin_umbral = [t for t in b if t not in umbrales]
    if sin_umbral:
        raise ValueError(f'sin umbral preinscrito para {sin_umbral}. Fijarlo '
                         f'despues de ver el resultado seria mover la porteria.')
    detalle = {t: (float(resultados[t]), float(umbrales[t]),
                   bool(resultados[t] >= umbrales[t])) for t in b}
    return int(all(v[2] for v in detalle.values())), detalle


# ---------------------------------------------------------------------------
# FASE IV - ESTADO FUERA DEL EQUILIBRIO
# ---------------------------------------------------------------------------

def ventana_ensamblado(Rm=1e9, Cm=1e-11, volumen=1e-15, conc_exceso=0.125,
                       Vm=70e-3):
    """Cuanto aguanta una neurona ensamblada antes de equilibrarse (Fase IV).

    D-105 establecio que un cuerpo ensamblado en equilibrio quimico es un
    cadaver, pero dejo sin responder cuanto dura el margen. Son DOS tiempos
    muy distintos, y confundirlos lleva a un requisito equivocado:

      VOLTAJE    tau = Rm x Cm ~ 10 ms. NO hay que transportarlo: se
                 restablece solo en cuanto exista gradiente.
      GRADIENTE  los iones de exceso se fugan a I/e por segundo. ~3 min.
                 ESTE es el que fija la ventana.

    Por defecto, una neurona pequena: 1 GΩ, 10 pF, 1 pL, 125 mM de exceso.

    Devuelve (tau_voltaje_s, tau_gradiente_s, razon).
    """
    e = 1.602e-19
    NA = 6.022e23
    tau_V = Rm * Cm
    n_iones = conc_exceso * 1000 * volumen * NA
    flujo = (Vm / Rm) / e
    tau_q = n_iones / flujo
    return tau_V, tau_q, tau_q / tau_V


# ---------------------------------------------------------------------------
# FASE V - ESCALA
# ---------------------------------------------------------------------------

def extrapolacion_tasa(nodos, tasas, n_objetivo):
    """¿Se puede extrapolar la tasa medida al tamano objetivo? (Fase V)

    Medido sobre los 30 circuitos [MEDIDO] del programa (excluyendo el humano,
    que esta en [PILOTO] y cuyo grafo H-4 declaro perisomatico):

        tamano  316-779 nodos   -> factor 2,5x
        tasa    1,50-4,00       -> factor 2,7x
        correlacion log(n) vs tasa: r = +0,005

    **La tasa no escala con el tamano EN EL RANGO MEDIDO.** Pero ese rango es
    2,5x y hasta el humano hay 10^8. Que no haya tendencia en dos ordenes y
    medio de nada NO autoriza a extrapolar ocho.

    Esta funcion devuelve explicitamente cuantos ordenes de magnitud se estan
    pidiendo de mas, para que la afirmacion vaya siempre con su alcance.

    Devuelve (r, ordenes_medidos, ordenes_pedidos, veredicto).
    """
    n = np.asarray(nodos, dtype=float)
    t = np.asarray(tasas, dtype=float)
    if n.size < 4:
        return float('nan'), 0.0, 0.0, 'INDETERMINADO: menos de 4 circuitos'
    r = float(np.corrcoef(np.log(n), t)[0, 1])
    med = math.log10(n.max() / n.min())
    ped = math.log10(n_objetivo / n.max())
    if abs(r) > 0.5:
        v = f'TENDENCIA (r={r:+.2f}): la tasa SI depende del tamano'
    elif ped > 2 * med:
        v = (f'NO SOPORTADA: sin tendencia en {med:.1f} ordenes, pero se piden '
             f'{ped:.1f}. Falta de contradiccion no es evidencia')
    else:
        v = f'RAZONABLE: {ped:.1f} ordenes pedidos sobre {med:.1f} medidos'
    return r, med, ped, v


# ---------------------------------------------------------------------------
# FASE VI - INTERFAZ CON EL CUERPO
# ---------------------------------------------------------------------------

INTERFAZ_MEDIDA = {          # D-134: primer CNS completo donde se MIDE
    'n_total': 211577,
    'sensoriales': 17873,    # 8,45 %  ·  vnc/ol/cb_sensory + sensory_ascending
    'motoras': 708,          # 0,33 %  ·  vnc_motor
    'interfaz_union': 18963, # 8,96 %  del sistema nervioso central
    'asimetria_in_out': 25,  # sensoriales por cada motora
    'pct_inh_sensorial': 0.2,
    'pct_inh_motor_aparente': 95.6,   # ARTEFACTO: son glutamatergicas
}
"""Interfaz cuerpo-sistema nervioso MEDIDA en MaleCNS v1.0 (D-134).

Es el unico CNS completo con anotacion de nervios de entrada y salida, asi que
es la primera vez que la fraccion de interfaz se mide en vez de estimarse.
La estimacion previa desde *C. elegans* daba 13,2 %; medido son **8,96 %**.
"""


def signo_de_salida_es_legible(nt_presinaptico, contexto):
    """¿Se puede deducir el signo de la sinapsis solo del neurotransmisor? (D-134)

    **NO en la salida al cuerpo.** El programa codifica el signo por el
    neurotransmisor presinaptico, con `INHIBITORIOS = (gaba, glutamate)`. Eso es
    correcto **dentro** del CNS de *Drosophila* —el glutamato inhibe via canales
    GluCl— y **falso en la union neuromuscular**, donde el mismo glutamato
    EXCITA via GluRIIA/B.

    Medido: **302 de 318 motoneuronas de MaleCNS son glutamatergicas.** Nuestra
    convencion las marcaria inhibitorias al 95,6 %. **Son excitadoras.**

    > **El signo no es propiedad del neurotransmisor: es del par
    > (neurotransmisor, receptor).** Dentro del CNS el receptor es lo bastante
    > consistente para que el atajo funcione. En la salida al cuerpo, no.

    **Ningun conectoma anota receptores postsinapticos.** Por eso la interfaz
    cuerpo-sistema nervioso **no es legible desde el conectoma solo**, y esa es
    la conclusion de la Fase VI.

    Devuelve (legible, motivo).
    """
    if contexto == 'intra_cns':
        return True, ('dentro del CNS el receptor es consistente: gaba y glutamate '
                      'inhiben (GluCl). La convencion vale')
    return False, ('en la union neuromuscular el glutamato EXCITA (GluRIIA/B). '
                   'El signo exige el receptor postsinaptico, que ningun '
                   'conectoma anota')


SENSIBILIDAD_SIGNO = 1.5713   # dDelta/d(error de signo), mediana de 20 circuitos
SENSIBILIDAD_DETECCION = 2.24 # dDelta/d(fraccion sinaptica capturada), D-137


def sensibilidad_escaner(degradacion_tolerada, fraccion_actual,
                         pendiente=SENSIBILIDAD_DETECCION):
    """Cuanta masa sinaptica mas debe capturar el escaner (D-137).

    **Descubrimiento incomodo sobre nuestros propios datos:** el umbral de peso
    >= 25 que usamos en toda la mosca conserva **el 0,50 % de las aristas** y
    **solo el 12,25 % de las sinapsis**. Todas nuestras medidas usan la octava
    parte de la masa sinaptica.

    | umbral | % aristas | % sinapsis |
    |---:|---:|---:|
    | 1 | 100 % | 100 % |
    | 5 | 5,02 % | 31,42 % |
    | 10 | 1,84 % | **21,78 %** |
    | **25** | **0,50 %** | **12,25 %** |
    | 100 | 0,04 % | 2,86 % |

    Y sabemos que **si importa**, porque lo medimos sin saberlo en D-114: pasar
    de umbral 25 a 10 —del 12,25 % al 21,78 % de la masa— movio el efecto del
    signo **0,2135**. De ahi sale la pendiente **2,24 por unidad de fraccion**.

    Traducido con D-136: esos 0,2135 equivalen a un **error de signo del 13,6 %**,
    cuando la tolerancia para degradar 0,05 es del **3,2 %**.

    > **La SENSIBILIDAD del escaner pesa tanto como su PRECISION en
    > neurotransmisor.** No es un parametro libre de preprocesado: es una
    > especificacion del instrumento de adquisicion.

    **Alcance:** dos puntos, valido localmente. NO se puede extrapolar al 100 %.
    """
    return float(fraccion_actual) + float(degradacion_tolerada) / pendiente


def precision_escaner(degradacion_tolerada, sensibilidad=SENSIBILIDAD_SIGNO):
    """Que precision de signo necesita el escaner (D-136). SIN simular.

    **Los controles de barajado ya median esto y nunca los habiamos usado asi.**
    `CTRL_shuffle_signo` permuta QUE neuronas son inhibitorias conservando la
    proporcion; si la fraccion inhibitoria es f, la tasa de error de signo bajo
    esa permutacion es **2f(1-f)**. Eso da **dos puntos** de la curva
    Delta(error):

        error = 0        ->  Delta(M2)
        error = 2f(1-f)  ->  Delta(CTRL_shuffle_signo)

    Sobre 20 circuitos validos, la pendiente mediana es **1,57**.

    | degradacion tolerada de Δ | error de signo maximo | precision exigida |
    |---:|---:|---:|
    | 0,01 | 0,6 % | **99,4 %** |
    | 0,05 | 3,2 % | **96,8 %** |
    | 0,10 | 6,4 % | 93,6 % |

    **Contraste con lo que se consigue hoy:**

    | dataset | acierto | error | degradacion |
    |---|---:|---:|---:|
    | MaleCNS | 97,3 % | 2,7 % | **0,042** |
    | H01 (humano) | 82,3 % | 17,7 % | **0,278** |

    > **El error de signo de H01 (0,278) es del tamaño del ruido metodologico
    > completo del programa (0,2135, D-114) y casi el de la horquilla entre
    > tareas (0,3717).** Un escaner con esa precision de signo introduce por si
    > solo tanto error como todas las decisiones de preprocesado juntas.

    **Supuesto declarado:** linealidad entre los dos puntos medidos. Con dos
    puntos no se puede testar. Si la curva fuera convexa —lo esperable— el error
    pequeño danaria menos, asi que **la cota es conservadora**, que es la
    direccion correcta para una especificacion.
    """
    return degradacion_tolerada / sensibilidad


TOLERANCIA_ENSAMBLADO = {    # D-138: fraccion de sinapsis omitidas -> perdida de Psi
    'omitidas':   (0.00, 0.20, 0.35, 0.50),
    'mediana':    (0.000, 0.049, 0.226, 0.441),
    'mejor':      (0.000, 0.000, 0.004, 0.016),   # e2e3_T6 (gusano)
    'peor':       (0.000, 0.475, 0.635, 0.759),   # m7_CXmachocrudo_dir
}


def tolerancia_ensamblado(perdida_tolerada, caso='mediana'):
    """Que fraccion de sinapsis puede fallar el ensamblador (D-138).

    **El eje de poda de la Curva A es un modelo de error de ensamblado** —
    sinapsis que existen y no se construyen— y llevabamos meses midiendolo sin
    llamarlo asi. 22 circuitos, cuatro niveles de poda cada uno.

    | sinapsis omitidas | perdida mediana | mejor | peor |
    |---:|---:|---:|---:|
    | 20 % | 4,9 % | 0,0 % | **47,5 %** |
    | 35 % | 22,6 % | 0,4 % | 63,5 % |
    | 50 % | 44,1 % | **1,6 %** | **75,9 %** |

    **Especificacion:** para no perder mas del 5 % de la funcion, el ensamblador
    debe colocar bien **>= 79,9 % de las sinapsis en el circuito mediano** y
    **>= 97,9 % en el peor**.

    > **El rango entre circuitos es de 47×** (1,6 % frente a 75,9 % de perdida al
    > omitir la mitad). **Ningun rasgo estructural lo predice:** la correlacion
    > con %I es r = +0,68 **global** pero **r = −0,16 dentro de la mosca**, y
    > `m3_MB` es contraejemplo directo (6,3 % de inhibicion, 61 % de fragilidad).
    > La correlacion global la sostiene la separacion gusano/mosca.

    **Conclusion: la tolerancia de ensamblado hay que MEDIRLA por circuito.**
    No se deduce del conectoma ni de sus resumenes.
    """
    import numpy as _np
    x = _np.asarray(TOLERANCIA_ENSAMBLADO[caso])
    p = _np.asarray(TOLERANCIA_ENSAMBLADO['omitidas'])
    return float(_np.interp(float(perdida_tolerada), x, p))


SENSIBILIDADES = {           # dDelta/d(error) medidas, una por fase
    'signo':      1.5713,    # D-136
    'deteccion':  2.24,      # D-137  (valida solo localmente)
    'colocacion': 0.882,     # D-138  (mediana de 22 circuitos)
}


def presupuesto_error(total_tolerado, etapas=None, sensibilidades=None):
    """Reparte un presupuesto de error entre las etapas del proceso (D-139).

    **El fallo que esto corrige:** cada tolerancia de las fases VI-VIII se
    derivo **suponiendo las demas perfectas**. Al componerlas:

    | etapa | error permitido | aporta a Δ |
    |---|---:|---:|
    | signo (D-136) | 3,2 % | 0,050 |
    | deteccion (D-137) | 7,3 % | 0,163 |
    | colocacion (D-138) | 20,1 % | 0,177 |
    | **SUMA** | | **0,391** |

    > **0,391 frente a un control barajado de ~0,45: el 87 % del camino hasta
    > ser indistinguible del azar.** Las especificaciones **no componen**.

    **Correccion:** con un presupuesto total B y n etapas, cada una recibe B/n:

    | presupuesto total | signo | deteccion | colocacion |
    |---:|---:|---:|---:|
    | 0,05 | **98,94 %** | **99,26 %** | **98,11 %** |
    | 0,10 | 97,88 % | 98,51 % | 96,22 % |

    **La especificacion conjunta es mucho mas dura que la suma de las
    individuales:** el signo pasa de 96,8 % a **98,9 %**, y la colocacion de
    79,9 % a **98,1 %**.

    Reparto aditivo, conservador. Si los errores fueran independientes se
    sumarian en cuadratura y cada etapa recibiria B/sqrt(n), mas holgado — pero
    no tenemos evidencia de independencia y **no se supone**.
    """
    sens = sensibilidades or SENSIBILIDADES
    et = list(etapas or sens)
    cuota = float(total_tolerado) / len(et)
    return {e: cuota / sens[e] for e in et}


VENTANA_RHO = (2.6, 6.0)     # P-24b, validada
RHO_OPERACION = 4.0          # punto de todos los experimentos del programa


def margen_bucle_cerrado(peso_emitido_por_salida, peso_total,
                         rho=RHO_OPERACION, ventana=VENTANA_RHO):
    """¿Sobrevive el regimen validado al cerrar el bucle sensorimotor? (D-135)

    Todos los experimentos del programa corren en **lazo abierto** con
    rho = 4,0, dentro de la ventana validada [2,6 · 6,0]. Cerrar el bucle anade
    ganancia:

        abierto : x(t+1) = W x(t) + u(t)
        cerrado : x(t+1) = W x(t) + B C x(t-d)

    En el peor caso (realimentacion en fase, retardo despreciable frente a la
    constante de tiempo), rho_efectivo <= rho + ||B C||. La condicion para no
    salir de la ventana es ||B C|| < ventana[1] - rho.

    **Medido en MaleCNS**, el unico CNS completo:

    | | |
    |---|---:|
    | motoras que reciben | **4,716 %** del peso total |
    | motoras que **emiten** intra-CNS | **0,020 %** |
    | grado de entrada de una motora | **17×** la mediana |

    > **El sistema nervioso es un EMBUDO:** convergencia masiva hacia la salida
    > y realimentacion interna despreciable. **La unica via de retorno es el
    > cuerpo.**

    Con esa cota, ||B C|| <= 0,0008 frente a un limite de 2,0: **margen 2.500×**.

    **PERO eso acota solo el lazo INTERNO.** El lazo externo pasa por el cuerpo,
    cuya funcion de transferencia **no esta en ningun conectoma**. La conclusion
    honesta es asimetrica:

    - **lado CNS:** medido, corto (2 saltos de mediana) y sin realimentacion
      propia. No desestabiliza.
    - **lado cuerpo:** no acotable desde estos datos.

    **Consecuencia para A3:** al poner un sistema nervioso en un cuerpo distinto,
    **la ganancia del bucle cambia** — y el CNS **no tiene realimentacion interna
    con la que compensar**. Es un riesgo de A3 que el conectoma no puede evaluar.

    Devuelve (cota_ganancia, limite, margen).
    """
    frac = float(peso_emitido_por_salida) / float(peso_total)
    cota = rho * frac
    limite = ventana[1] - rho
    return cota, limite, (limite / cota if cota > 0 else float('inf'))


def cota_decodificacion(n_entrada, n_salida):
    """Cota EXACTA de cuanto del estimulo se recupera desde la salida (D-154).

        R2_decod <= min(1, q/p)

    Es algebra lineal —el rango de la transferencia no supera min(p,q)— **no un
    ajuste**, y se calcula **sin simular**.

    | canal | p | q | cota | R² medido |
    |---|---:|---:|---:|---:|
    | arco sensorimotor real | 12.274 | 241 | **0,0196** | **−0,6345** |

    **El arco real no usa ni el 2 % que la cota permite: R² es NEGATIVO.** El
    sistema nervioso **destruye** el estimulo sensorial en el camino a la salida.

    > **No es un canal de transmision: es un canal de decision.**

    **Limitacion:** la cota y la medida son para decodificadores **lineales**.
    """
    return min(1.0, float(n_salida) / float(n_entrada))


def canales_interfaz(n_canales, bits_por_canal=None):
    """Coste informacional del mapa de interfaz cuerpo-sistema nervioso (Fase VI).

    Bajo A3 el sistema nervioso va a un cuerpo nuevo, y todo lo que sabe del
    mundo pasa por un numero finito de canales. Dos hallazgos:

    1. **La interfaz escala con el CUERPO, no con el cerebro.** En C. elegans
       la interfaz es el 13,2 % del sistema nervioso; aplicar esa fraccion al
       humano daria 1,1x10^10 canales. La anatomia real da ~10^7 (nervio optico
       2,4x10^6, auditivo 6x10^4, motores espinales ~2x10^5): **1.139x menos**.

    2. **En bits es despreciable.** Con 10^7 canales y log2(10^7)=23 bits para
       decir a que se conecta cada uno: **29 MB**, frente a 36,6 TB de
       conectoma. El 0,00008 %.

    > El problema de la Fase VI NO es informacional. Es que hay que ACERTAR la
    > correspondencia, y un error ahi no se corrige solo: un nervio conectado
    > al musculo equivocado no se arregla con mas bits.

    Devuelve (bits, megabytes).
    """
    if bits_por_canal is None:
        bits_por_canal = math.log2(n_canales)
    bits = n_canales * bits_por_canal
    return bits, bits / 8 / 1e6
