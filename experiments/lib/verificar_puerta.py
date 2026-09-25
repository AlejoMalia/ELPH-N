"""
VERIFICACION DE LA UNIFICACION DE LA PUERTA (nivel 0).

Los experimentos M-1, M-3 y H-1 traian cada uno su propio bloque de chequeos
previos -- o ninguno, en el caso de M-1. Ahora los tres llaman a
`puerta.abrir()`. Este script demuestra que la unificacion NO cambia ningun
veredicto ya publicado:

  (a) la puerta unica ABRE sobre el metadata congelado de los cuatro circuitos
      ya medidos (escape, MB, CX, H01), que es lo que hacian los bloques
      artesanales;
  (b) la puerta unica CIERRA sobre los cinco fallos historicos.

Coste: segundos. No simula nada, no toca ningun resultado.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from puerta import (abrir, PuertaCerrada, validar_metadata, validar_canales,
                    validar_listas_nominales)

EXP = HERE.parent

CLAVES_FLY = ('rol', 'n_nodos', 'pct_inhib', 's0', 'nodos', 'inyeccion',
              'lectura', 'nt_por_nodo', 'lectura_biologica')
CLAVES_M1 = ('fuente', 'n_nodos', 'n_aristas', 'nodos', 'inyeccion', 'lectura',
             'nt_por_nodo', 'sha256_connections', 'sha256_annotations')

# circuitos ya medidos: (etiqueta, fichero, clave, claves exigidas, biologica)
MEDIDOS = [
    ('M-1 escape', 'M1-mosca-escape/results/subgrafo_meta.json', None,
     CLAVES_M1, True),   # declarada en codigo: descendentes por tipo
    ('M-3 escape', 'M3-roles-biologicos/results/circuitos_meta.json', 'escape',
     CLAVES_FLY, None),
    ('M-3 MB', 'M3-roles-biologicos/results/circuitos_meta.json', 'MB',
     CLAVES_FLY, None),
    ('M-3 CX', 'M3-roles-biologicos/results/circuitos_meta.json', 'CX',
     CLAVES_FLY, None),
    ('H-1 H01', 'H1-humano-piloto/results/circuitos_meta.json', 'H01',
     CLAVES_FLY, None),
]

FALLOS = [
    ('D-050 lista GABA con un digito',
     lambda: validar_listas_nominales({'GABA': ['DD1', 'DD2']}, {'DD01', 'DD02'})),
    ('M-2 clave de metadata ausente',
     lambda: validar_metadata({'a': 1}, ('a', 'fuente'))),
    ('M-2 lectura no declarada biologica',
     lambda: validar_canales([1, 2], [3, 4], biologica=False)),
    ('canales solapados',
     lambda: validar_canales([1, 2], [2, 3], biologica=True)),
    ('lectura vacia',
     lambda: validar_canales([1, 2], [], biologica=True)),
]


def main():
    fallos = 0
    print('(a) LA PUERTA UNICA ABRE SOBRE LO YA MEDIDO\n')
    for etiq, ruta, clave, claves, bio in MEDIDOS:
        d = json.loads((EXP / ruta).read_text())
        meta = d if clave is None else d[clave]
        biologica = bio if bio is not None else meta.get('lectura_biologica')
        try:
            abrir(meta=meta, claves=claves,
                  inyeccion=meta.get('inyeccion'), lectura=meta.get('lectura'),
                  biologica=biologica, bateria=False, etiqueta=etiq)
        except PuertaCerrada as e:
            print(f'  [FALLA] {etiq}: la puerta se cerro -> {e}')
            fallos += 1

    print('\n(b) LA PUERTA UNICA CIERRA SOBRE LOS FALLOS HISTORICOS\n')
    for nom, fn in FALLOS:
        try:
            fn()
            print(f'  [FALLA] {nom}: la puerta NO se cerro')
            fallos += 1
        except PuertaCerrada as e:
            print(f'  [PASA ] {nom}: cerrada -> {str(e)[:58]}')

    print('\n(c) BATERIA DEL INSTRUMENTO T1-T9\n')
    try:
        abrir(bateria=True, etiqueta='instrumento')
    except PuertaCerrada as e:
        print(f'  [FALLA] {e}')
        fallos += 1

    print('\n' + ('UNIFICACION VERIFICADA' if not fallos
                  else f'{fallos} fallo(s)'))
    return 1 if fallos else 0


if __name__ == '__main__':
    sys.exit(main())
