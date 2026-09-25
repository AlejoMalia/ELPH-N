"""
NIVEL 0 - PUERTA UNICA DE ARRANQUE.

Ningun experimento calcula nada hasta pasar por aqui. Coste: microsegundos.

Los fallos mas caros del programa NO fueron "N demasiado grande": fueron
arranques invalidos que consumieron minutos u horas y produjeron numeros que
parecian resultados.

  D-029  poda por umbral que conservaba empates      -> 5 experimentos invalidados
  D-037  cuantizador que no representaba el cero     -> 5 experimentos invalidados
  D-050  lista GABA con DD1 en vez de DD01           -> 15 de 26 inhibitorias perdidas
  M-2    lectura por fallback ordenada por root_id   -> 40 min a 2064 nodos, inutiles

Los cuatro se cazan SIN EJECUTAR NADA. Ese es el punto.

REGLA: aqui solo entran invariantes que ya han roto en silencio. Nada de
ciencia nueva; nada que dependa de los datos del experimento en curso.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

__all__ = ['PuertaCerrada', 'abrir', 'validar_metadata', 'validar_canales']


class PuertaCerrada(RuntimeError):
    """El experimento no arranca. No se calcula nada."""


# ----------------------------------------------------------------------------

def validar_metadata(meta, claves, etiqueta='metadata'):
    """Las claves que el codigo espera tienen que estar.

    Caza el `KeyError: 'fuente'` de M-2 -- que era inofensivo porque reventaba
    ruidosamente, pero al final de una ejecucion de 40 minutos.
    """
    faltan = [k for k in claves if k not in meta]
    if faltan:
        raise PuertaCerrada(f'{etiqueta}: faltan claves {faltan}')
    return True


def validar_canales(inyeccion, lectura, biologica, etiqueta='canales'):
    """Entrada y salida: no vacias, sin solape, y declaradas biologicas.

    Caza el fallback de M-2: `lec = [descendentes] or [primeros 40 por root_id]`.
    En MBON la "salida" acabaron siendo celulas de Kenyon, que son la ENTRADA
    del cuerpo fungiforme. El sintoma fue que barajar el signo daba MEJOR
    reconstruccion que el signo correcto.
    """
    if not inyeccion:
        raise PuertaCerrada(f'{etiqueta}: inyeccion vacia')
    if not lectura:
        raise PuertaCerrada(f'{etiqueta}: lectura vacia')
    if set(map(str, inyeccion)) & set(map(str, lectura)):
        raise PuertaCerrada(f'{etiqueta}: inyeccion y lectura se solapan')
    if not biologica:
        raise PuertaCerrada(
            f'{etiqueta}: la lectura no esta declarada biologica. '
            'Un canal elegido por grado o por identificador de segmentacion '
            'no es una lectura: es un artefacto de ordenacion.')
    return True


def validar_listas_nominales(listas, presentes):
    """Toda lista nominal al 100 % contra el dataset.

    Caza D-050: DD1..DD6 frente a DD01..DD06. Un nombre que no coincide NO es
    "una neurona ausente": es un error de formato que corrompe la red en
    silencio.
    """
    from biologia import validar_cobertura, CoberturaIncompleta
    for etiqueta, nombres in listas.items():
        try:
            validar_cobertura(nombres, presentes, etiqueta)
        except CoberturaIncompleta as e:
            raise PuertaCerrada(str(e))
    return True


def _bateria():
    """T1-T9 sobre el instrumento. Caza D-029 y D-037."""
    import subprocess
    r = subprocess.run([sys.executable,
                        str(Path(__file__).resolve().parent / 'test_instrumento.py')],
                       capture_output=True, text=True)
    if r.returncode != 0:
        cola = '\n'.join(r.stdout.strip().splitlines()[-8:])
        raise PuertaCerrada(f'bateria del instrumento en ROJO:\n{cola}')
    return True


def abrir(meta=None, claves=(), inyeccion=None, lectura=None,
          biologica=None, listas=None, presentes=None, bateria=True,
          etiqueta='experimento', pre=None, post=None, nt_por_nodo=None,
          exige_signo=True, indirecta_declarada=False):
    """La puerta. Si algo falla, lanza PuertaCerrada y NO se calcula nada.

    D-125: las comprobaciones de la puerta v2 se ejecutan AQUI, no en un modulo
    aparte que haya que acordarse de llamar. `puerta_v2.py` se escribio ayer y
    NADIE lo importaba: el arreglo de D-122 -- rechazar una tarea sin camino
    anatomico -- habria quedado inerte y el proximo experimento lo repetiria.
    Es el mismo fallo que D-074, donde `puerta.py` existia y nadie la cruzaba.

    Pasando `pre`/`post` (las aristas) se activa `validar_sustrato`, que RECHAZA
    una tarea sin camino de la inyeccion a la lectura. Pasando `nt_por_nodo` se
    activa el aviso de %I de via.

    Uso tipico al principio de main():

        from puerta import abrir
        abrir(meta=meta, claves=('rol','nodos','inyeccion','lectura'),
              inyeccion=meta['inyeccion'], lectura=meta['lectura'],
              biologica=meta.get('lectura_biologica'),
              listas={'GABA': sorted(GABA)}, presentes=set(neurons))
    """
    hechas = []
    if bateria:
        _bateria(); hechas.append('bateria T1-T9')
    if meta is not None and claves:
        validar_metadata(meta, claves, etiqueta); hechas.append(f'{len(claves)} claves')
    if inyeccion is not None or lectura is not None:
        validar_canales(inyeccion or [], lectura or [], biologica, etiqueta)
        hechas.append('canales')
    if listas and presentes is not None:
        validar_listas_nominales(listas, presentes)
        hechas.append(f'{len(listas)} listas nominales')
    if pre is not None and post is not None and inyeccion and lectura:
        from puerta_v2 import validar_sustrato
        n = validar_sustrato(pre, post, inyeccion, lectura, etiqueta=etiqueta,
                             indirecta_declarada=indirecta_declarada)
        hechas.append(f'sustrato ({n} aristas directas)')
    if nt_por_nodo is not None and inyeccion and lectura:
        from puerta_v2 import revisar_v2
        for av in revisar_v2(nt_por_nodo, list(inyeccion) + list(lectura),
                             etiqueta=etiqueta, exige_signo=exige_signo):
            print(f'[NIVEL 0 · AVISO] {av}')
    print(f'[NIVEL 0] puerta abierta para {etiqueta}: ' + ' · '.join(hechas))
    return True


if __name__ == '__main__':
    # autoprueba: la puerta debe CERRARSE en los cuatro casos historicos
    casos = [
        ('D-050 lista GABA con un digito',
         lambda: validar_listas_nominales({'GABA': ['DD1', 'DD2']},
                                          {'DD01', 'DD02'})),
        ('M-2 clave de metadata ausente',
         lambda: validar_metadata({'a': 1}, ('a', 'fuente'))),
        ('M-2 lectura no biologica',
         lambda: validar_canales([1, 2], [3, 4], biologica=False)),
        ('canales solapados',
         lambda: validar_canales([1, 2], [2, 3], biologica=True)),
        ('lectura vacia',
         lambda: validar_canales([1, 2], [], biologica=True)),
    ]
    fallos = 0
    print('AUTOPRUEBA DE LA PUERTA - debe cerrarse en los 5 casos\n')
    for nom, fn in casos:
        try:
            fn()
            print(f'  [FALLA] {nom}: la puerta NO se cerro')
            fallos += 1
        except PuertaCerrada as e:
            print(f'  [PASA ] {nom}: cerrada -> {str(e)[:60]}')
    print('\n' + ('PUERTA EN VERDE' if not fallos else f'{fallos} caso(s) sin cazar'))
    sys.exit(1 if fallos else 0)
