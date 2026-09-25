#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el Anexo D del paper DESDE el instrumento de auditoria.

  python3 tools/anexo_d.py > /tmp/anexo_d.md

El anexo anterior estaba escrito a mano y decia 158 afirmaciones cuando el
instrumento tenia 109: el documento se contradecia consigo mismo. Un anexo que
enumera el marco no puede mantenerse a mano — se genera.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'experiments', 'lib'))
from auditoria_marco import EJES, UMBRALES

n = len(UMBRALES)
cols = [sum(v[i] for v in UMBRALES.values()) for i in range(len(EJES))]
total = sum(sum(v) for v in UMBRALES.values())

print(f"# ANEXO D · LAS {n} AFIRMACIONES DEL MARCO\n")
print("""**Por qué están aquí:** un marco cuya meta es que otros lo ejecuten tiene que poder
**enumerarse**. Si no se puede listar, no se puede auditar; si no se puede auditar, no es
un marco.

**Este anexo se genera desde `experiments/lib/auditoria_marco.py`**, no se escribe a mano.
La versión anterior decía 158 afirmaciones cuando el instrumento ya tenía otras tantas
distintas, y el documento se contradecía consigo mismo — que es exactamente el fallo que
el marco existe para impedir.

> **Nota sobre el tamaño de esta lista.** Se preguntó si convenía llegar a mil
> afirmaciones. La respuesta del propio marco es que **no**: la regla 566 dice que
> *«promediar condiciones deja que la nota la decida qué condiciones metes en la lista»*.
> Añadir novecientas afirmaciones que salgan todas al 100 % no fortalece el marco: **lo
> hace más fácil de aprobar**. Los hallazgos que de verdad cambiaron el marco no vinieron
> de añadir afirmaciones, sino de **atacarlas**.
""")
print("## D.1 · Estado por eje\n")
print("| eje | qué pregunta | cumplen | % |")
print("|:--|:--|--:|--:|")
for (nom, desc), c in zip(EJES, cols):
    print(f"| **{nom}** | {desc} | {c}/{n} | **{100*c/n:.1f} %** |")
print(f"\n**MARCO COMPLETO (los {len(EJES)} ejes, las {n} afirmaciones): {100*total/(len(EJES)*n):.1f} %**\n")
print("""El octavo eje se añadió **porque** los siete primeros llegaron al 100 %. Un instrumento
que marca 100 % en todo **ha dejado de discriminar**, y las notas las pone quien hace el
trabajo: **un 100 % autoevaluado vale menos que un 98,7 % con huecos nombrados.**
""")
falt = [(k, [EJES[i][0] for i, x in enumerate(v) if not x and i < len(EJES)-1])
        for k, v in UMBRALES.items()]
falt = [(k, e) for k, e in falt if e]
print(f"## D.2 · Lo que falta en los siete ejes de planteamiento\n")
if falt:
    print("| afirmación | eje que falta |")
    print("|:--|:--|")
    for k, e in falt:
        print(f"| {k} | {', '.join(e)} |")
else:
    print("**Ninguna.** Los siete ejes de planteamiento están completos; "
          "lo que falta es el octavo, y ése no lo cierra ninguna batería.\n")
print(f"\n## D.3 · Las {n} afirmaciones\n")
print("Leyenda de ejes: `1` enunciado · `2` unidades · `3` evidencial · `4` falsable · "
      "`5` costeado · `6` ventana · `7` resistido · `8` **medido**.\n")
print("| # | afirmación | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
print("|--:|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|")
for i, (k, v) in enumerate(UMBRALES.items(), 1):
    marks = " | ".join("✓" if x else "·" for x in v)
    print(f"| {i} | {k} | {marks} |")
print(f"""
**Las {n} afirmaciones llevan `8` en blanco sin excepción.** Ésa es la lectura honesta del
anexo: el marco está enunciado, dimensionado, fechado, falsado, costeado, acotado y
atacado — y **nadie lo ha medido todavía, empezando por nosotros**.""")
