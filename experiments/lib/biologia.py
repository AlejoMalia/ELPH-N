"""
LISTAS NOMINALES DE CLASES CELULARES - definicion unica del programa.

Ningun experimento vuelve a escribir su propia lista de neuronas. Ese fue el
cuarto bug de instrumento de la serie (D-050): la lista GABAergica usaba
DD1..DD6 y VD1..VD13, mientras el dataset nombra DD01..DD06 y VD01..VD13.
Quince de veintiseis neuronas inhibitorias no coincidian, en silencio, y las
cuatro que si acertaban (VD10..VD13) lo hacian por casualidad de formato.

Efecto: 3.0 % de aristas inhibitorias en vez de 5.8 %. La asignacion de signo
-- la pieza central medida en P-25 y P-27 -- se midio con menos de la mitad de
las inhibitorias reales.

REGLA: toda lista nominal se valida contra el dataset ANTES de usarse. Una
cobertura menor del 100 % es un fallo de instrumento, no un dato que falta.
Verificado por test_instrumento.T7.
"""
import numpy as np

__all__ = ['GABA', 'SENSORIALES_ANFIDIALES', 'MOTORAS_EXCITATORIAS',
           'validar_cobertura', 'CoberturaIncompleta']


class CoberturaIncompleta(RuntimeError):
    """Una lista nominal no se corresponde con los nombres del dataset."""


# --- GABAergicas de C. elegans (las inhibitorias bien establecidas) ---
#
# PROCEDENCIA (D-280 · nivel EXTERNO, no verificado contra la fuente desde aqui):
#   McIntire, Jorgensen, Kaplan & Horvitz (1993), "The GABAergic nervous system of
#   Caenorhabditis elegans", Nature 364:337-341. Identifica 26 neuronas GABAergicas.
# La composicion de esta lista coincide exactamente con ese recuento:
#   6 DD + 13 VD + 4 RME + AVL + DVB + RIS = 26.
#
# LO QUE SI ESTA VERIFICADO AQUI, y es lo unico:
#   cobertura 100 % contra los nombres de herm_full_edgelist.csv (26/26).
#   El dataset NO trae columna de neurotransmisor: no hay nada interno contra lo que
#   contrastar la asignacion en si. Por eso la lista se queda en EXTERNO y no sube.
#
# REVISION POSTERIOR NO INCORPORADA, y se declara:
#   Gendrel, Atlas & Hobert (2016), eLife 5:e17686, amplia el conjunto GABA-positivo
#   con clases adicionales. Incorporarlo subiria el % de aristas inhibitorias. Por
#   D-255 eso es COSMETICO: mueve cifras, no mueve ningun veredicto del registro.
#
# Formato de dos digitos, que es el que usa herm_full_edgelist.
GABA = frozenset(
    {f'DD{i:02d}' for i in range(1, 7)}          # motoneuronas dorsales D
    | {f'VD{i:02d}' for i in range(1, 14)}       # motoneuronas ventrales D
    | {'AVL', 'DVB', 'RIS', 'RMED', 'RMEV', 'RMEL', 'RMER'}
)

# --- Sensoriales quimiosensoriales anfidiales ---
SENSORIALES_ANFIDIALES = tuple(
    ['ASEL', 'ASER', 'AWCL', 'AWCR', 'AWAL', 'AWAR', 'ASHL', 'ASHR',
     'ADFL', 'ADFR', 'ASIL', 'ASIR', 'ASJL', 'ASJR', 'ASKL', 'ASKR',
     'AWBL', 'AWBR', 'ADLL', 'ADLR'])

# --- Motoneuronas colinergicas del cordon ventral (excitatorias) ---
MOTORAS_EXCITATORIAS = tuple(
    [f'VA{i:02d}' for i in range(1, 13)]
    + [f'VB{i:02d}' for i in range(1, 12)]
    + [f'DA{i:02d}' for i in range(1, 10)]
    + [f'DB{i:02d}' for i in range(1, 8)])


def validar_cobertura(nombres, presentes, etiqueta, minimo=1.0):
    """Falla ruidosamente si una lista nominal no aparece en el dataset.

    Un nombre que no coincide NO es 'una neurona que no esta en los datos':
    es, casi siempre, un error de formato que corrompe en silencio la
    construccion de la red. Por eso el default exige cobertura total.
    """
    nombres = list(nombres)
    faltan = [n for n in nombres if n not in presentes]
    cob = 1.0 - len(faltan) / max(len(nombres), 1)
    if cob < minimo:
        raise CoberturaIncompleta(
            f'{etiqueta}: cobertura {cob:.1%} ({len(nombres) - len(faltan)}'
            f'/{len(nombres)}). Ausentes: {sorted(faltan)[:20]}'
            + (' ...' if len(faltan) > 20 else ''))
    return cob


def resumen_cobertura(presentes):
    """Devuelve la cobertura de cada lista nominal contra un conjunto de
    nombres del dataset. Para el informe, no para decidir."""
    out = {}
    for etiqueta, lst in (('GABA', sorted(GABA)),
                          ('sensoriales_anfidiales', SENSORIALES_ANFIDIALES),
                          ('motoras_excitatorias', MOTORAS_EXCITATORIAS)):
        faltan = [n for n in lst if n not in presentes]
        out[etiqueta] = {'total': len(lst), 'presentes': len(lst) - len(faltan),
                         'cobertura': 1.0 - len(faltan) / len(lst),
                         'ausentes': sorted(faltan)}
    return out
