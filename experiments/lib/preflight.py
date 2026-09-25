"""Chequeo previo obligatorio antes de lanzar cualquier experimento caro.

Responde tres preguntas, EN ESTE ORDEN, porque cada una es mas barata que la
siguiente:

  1. MATE (D-108)        ¿hay trabajo cuyo resultado ya esta demostrado?
                         Gratis, no toca el protocolo. Se aplica siempre.
  2. PARALELISMO         ¿cuantos obreros caben? Los puntos son independientes
                         y cada uno es monohilo. Gratis, no toca el protocolo.
  0. INVENTARIO (D-155)  ¿esta la respuesta ya en los registros? OBLIGATORIO,
                         y va PRIMERO: un experimento que repite algo medido
                         es coste puro. Usa `inventario.resumen(...)`.
  3. SECUENCIAL (D-107)  ¿conviene parada temprana? NO es gratis: exige frontera
                         preinscrita. Solo si 1 y 2 no bastan.

El orden importa: no tiene sentido pagar alpha por una parada temprana cuando
el 75 % del coste era trabajo redundante que se quita sin pagar nada.

Uso:
    from preflight import chequeo
    chequeo(etapas={'curva_A': ('tarea',), 'M4': ('tarea','b')},
            parametro='b', n_valores=6,
            coste={'curva_A': 570, 'M4': 480})
"""
import os
import numpy as np

from mate import informe
from metodos import regla_K, REGIMEN_INESTABLE

__all__ = ['chequeo', 'obreros_recomendados']


def obreros_recomendados(margen=2):
    """Nucleos fisicos menos un margen para que el usuario siga trabajando.

    NO se descuenta la carga actual a proposito: un chequeo PREVIO suele
    ejecutarse mientras la tanda anterior sigue viva, y restar esa carga daria
    una recomendacion absurdamente baja para un experimento que arrancara
    cuando la maquina ya este libre.
    """
    return max(1, (os.cpu_count() or 4) - margen)


def chequeo(etapas, parametro, n_valores, coste=None, n_puntos=None,
            min_por_punto=20.0, condiciones_nuevas=(), K=None,
            sigma_max=0.03, piloto=None, inventariado=None):
    """Informe previo. Devuelve dict; imprime el resumen.

    `condiciones_nuevas`  condiciones de medida que NINGUN experimento anterior
                          ha corrido. Su sigma es desconocida: fijar K sin
                          medirla es exactamente lo que hundio F-1 (D-111).
    `piloto`              {condicion: sigma medida en un punto piloto}. Con eso
                          se aplica regla_K y se decide K con la herramienta.
    """
    r = informe(etapas, parametro, n_valores, coste)
    obr = obreros_recomendados()
    n_puntos = n_puntos or n_valores
    serie_h = n_puntos * min_por_punto / 60
    tras_mate_h = serie_h * (1 - r['redundancia'])
    final_h = tras_mate_h / obr

    print('CHEQUEO PREVIO\n')
    print('  0. INVENTARIO (D-155) — obligatorio, y va primero')
    if inventariado is None:
        print('     *** SIN DECLARAR. Ejecutar inventario.resumen(<terminos>) y')
        print('     *** pasar inventariado="<que se busco y que se encontro>".')
        print('     *** Un experimento que repite algo medido es coste puro.')
    else:
        print(f'     {inventariado}')
    if parametro not in {p for deps in etapas.values() for p in deps}:
        print(f"\n  *** AVISO: '{parametro}' no aparece en ninguna tupla de")
        print(f"  *** dependencia. MATE dira 100 % de redundancia y sera FALSO (D-152).")

    print(f'  1. MATE (gratis, sin tocar protocolo)')
    if r['etapas_fijas']:
        print(f'     etapas independientes de "{parametro}": '
              f'{", ".join(r["etapas_fijas"])}')
    else:
        print(f'     ninguna etapa es independiente de "{parametro}"')
    print(f'     redundancia: {100*r["redundancia"]:.1f} %'
          f'   ({r["coste_actual"]} -> {r["coste_minimo"]} unidades)')
    if r['redundancia'] < 0.05:
        print('     -> sin grasa. El coste es real; buscar el ahorro en 2 y 3.')

    print(f'\n  2. PARALELISMO (gratis, sin tocar protocolo)')
    print(f'     nucleos={os.cpu_count()}  obreros recomendados={obr}'
          f'   (cola de trabajo, no reparto fijo)')

    print(f'\n  3. SECUENCIAL (D-107: NO gratis, exige frontera preinscrita)')
    if final_h < 2:
        print(f'     no hace falta: con 1 y 2 el experimento baja a '
              f'~{final_h:.1f} h. No se paga alpha por nada.')
    else:
        print(f'     considerar: quedan ~{final_h:.1f} h. Calibrar la frontera '
              f'con secuencial.calibrar_obf() y ESCRIBIRLA en el preregistro')
        print(f'     ANTES de la primera ejecucion.')

    if condiciones_nuevas:
        print(f'\n  4. POTENCIA (D-111: la comprobacion que faltaba)')
        print(f'     condiciones NUEVAS, sin sigma conocida: '
              f'{", ".join(condiciones_nuevas)}')
        falta = [c for c in condiciones_nuevas if not (piloto or {}).get(c)]
        if falta:
            print(f'     *** BLOQUEADO: {", ".join(falta)} no tienen sigma medida.')
            print(f'     *** Correr UN punto piloto y aplicar regla_K ANTES de la')
            print(f'     *** rejilla. Fijar K a ojo es el fallo de F-1 (D-111).')
        else:
            for c in condiciones_nuevas:
                s0 = piloto[c]
                if s0 <= sigma_max:
                    print(f'     {c}: sigma piloto {s0:.4f} <= {sigma_max} -> K={K} basta')
                    continue
                Kn, conf = regla_K(K, s0, sigma_max, REGIMEN_INESTABLE)
                print(f'     {c}: sigma piloto {s0:.4f} > {sigma_max} -> '
                      f'K {K} debe subir a {Kn} (confianza {conf})')
                print(f'        coste x{Kn/K:.1f}')
    else:
        print(f'\n  4. POTENCIA (D-111)')
        print(f'     el experimento no anade condiciones nuevas: '
              f'K vale el de los experimentos previos comparables.')

    print(f'\n  proyeccion:  serie {serie_h:.1f} h  ->  tras MATE '
          f'{tras_mate_h:.1f} h  ->  con {obr} obreros {final_h:.1f} h')
    r.update(obreros=obr, horas_serie=serie_h, horas_final=final_h)
    return r
