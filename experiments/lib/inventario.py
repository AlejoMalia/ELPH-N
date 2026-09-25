"""Inventario mecanico del dataset. Primera pata de la TRIADA obligatoria.

La triada, exigida por el investigador antes de proponer o lanzar nada:

    1. INVENTARIO   ¿esta la respuesta ya en los registros?
    2. MATEMATICA   ¿hay una formula que la de sin simular?
    3. MATE         ¿que parte del computo esta ya demostrada?

**Si la triada basta, se ejecuta directamente y se informa del resultado.**
**Si no basta, se dice que hace falta computo real y por que.**

Esta pata se automatiza porque escribir la regla no bastaba: se incumplio en
D-125 (herramienta sin importar), D-146 (magnitud recalculada sin leer su
definicion) y D-152 (plan propuesto sin inventariar). **Lo que no es mecanico
se olvida.**
"""
import json
import collections
from pathlib import Path

__all__ = ['campos_disponibles', 'buscar', 'resumen']

RAIZ = Path(__file__).resolve().parent.parent


def _jsons(patron='*/results/*.json'):
    for f in sorted(RAIZ.glob(patron)):
        try:
            d = json.loads(f.read_text())
        except Exception:
            continue
        if isinstance(d, dict):
            yield f, d


def campos_disponibles(profundidad=2):
    """Todos los campos del dataset y en cuantos ficheros aparecen."""
    c = collections.Counter()
    def rec(o, pre, d):
        if d > profundidad or not isinstance(o, dict):
            return
        for k, v in o.items():
            c[f'{pre}{k}'] += 1
            if isinstance(v, dict) and d < profundidad:
                rec(v, f'{pre}{k}.', d + 1)
    for _, d in _jsons():
        rec(d, '', 0)
    return c


def buscar(*terminos, minimo=2):
    """Campos cuyo nombre contiene alguno de los terminos. Punto de partida
    del inventario: dice QUE hay antes de decidir que se mide."""
    t = [x.lower() for x in terminos]
    return {k: n for k, n in campos_disponibles().items()
            if n >= minimo and any(x in k.lower() for x in t)}


def resumen(*terminos):
    """Informe legible para pegar en una decision."""
    tot = sum(1 for _ in _jsons())
    print(f'  INVENTARIO · {tot} ficheros de resultados')
    if terminos:
        r = buscar(*terminos)
        print(f'  campos que casan con {list(terminos)}: {len(r)}\n')
        for k, n in sorted(r.items(), key=lambda kv: -kv[1])[:25]:
            print(f'    {k:44s} {n:4d} ficheros')
        if not r:
            print('    NINGUNO -> la respuesta no esta en los registros')
    else:
        c = campos_disponibles()
        print(f'  campos distintos: {len(c)}\n')
        for k, n in c.most_common(25):
            print(f'    {k:44s} {n:4d} ficheros')
    return None
