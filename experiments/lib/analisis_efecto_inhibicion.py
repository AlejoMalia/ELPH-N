"""
No-linealidad del efecto del signo frente a la fraccion inhibitoria.

Reproduce todos los numeros de docs/EFECTO-DEL-SIGNO-Y-INHIBICION.md a partir
de los JSON congelados de M-3. No simula nada: solo lee y compara.

La conclusion que sostiene: D-064 no falla por FORMA (una recta donde hacia
falta una curva) sino por ORDEN. El orden roto no lo arregla ninguna
reparametrizacion del eje %I.
"""
import json
import math
import sys
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
M3 = HERE.parent / 'M3-roles-biologicos' / 'results'

# C. elegans: valor publicado en P-30 / M-1 §3, sin sigma registrada
GUSANO = ('C. elegans', 5.8, 0.1195, None)
UMBRAL_MISMO_PI = 1.0     # puntos porcentuales para considerar "mismo %I"


def cargar():
    puntos = [GUSANO]
    topo = {}
    for c in ('MB', 'escape', 'CX'):
        v = json.loads((M3 / f'm3_{c}.json').read_text())
        e = v['efecto_signo']
        puntos.append((c, v['pct_inhib'], e['valor'], e['sigma']))
        topo[c] = (v['pct_inhib'], v['topologia_sola'])
    puntos.sort(key=lambda r: r[1])
    return puntos, topo


def main():
    puntos, topo = cargar()

    print('1. LOS CUATRO PUNTOS\n')
    for n, pi, e, s in puntos:
        sig = f' +- {s:.4f}' if s else '  (sin sigma)'
        print(f'   {n:12s} %I={pi:5.1f}   efecto={e:+.4f}{sig}')

    print('\n2. MONOTONIA -- se rompe, y con cuanta fuerza\n')
    rupturas = []
    for (n1, p1, e1, s1), (n2, p2, e2, s2) in zip(puntos, puntos[1:]):
        nsig = abs(e1 - e2) / math.hypot(s1 or 0, s2 or 0) if (s1 and s2) else None
        marca = 'sube' if e2 >= e1 else 'BAJA <-- RUPTURA'
        extra = f'  ({nsig:.1f} sigma)' if nsig else ''
        print(f'   {n1:11s} -> {n2:11s}  {e1:+.4f} -> {e2:+.4f}   {marca}{extra}')
        if e2 < e1:
            rupturas.append((n1, n2, nsig))

    print('\n3. PAR CRITICO -- mismo %I, efecto distinto\n')
    pares = []
    for a, b in combinations(puntos, 2):
        if abs(a[1] - b[1]) < UMBRAL_MISMO_PI:
            r = max(a[2], b[2]) / min(a[2], b[2])
            pares.append((a, b, r))
            print(f'   {a[0]} ({a[1]:.1f} %) vs {b[0]} ({b[1]:.1f} %): '
                  f'delta %I = {abs(a[1]-b[1]):.1f} pts -> razon {r:.2f}x')

    print('\n4. TOPOLOGIA SOLA (M0 - M1) -- esta SI ordena\n')
    for c, (pi, t) in sorted(topo.items(), key=lambda kv: kv[1][0]):
        print(f'   {c:8s} %I={pi:5.1f}   M0-M1 = {t["valor"]:+.4f} +- {t["sigma"]:.4f}'
              f'   {"ayuda" if t["valor"] > 0 else "ESTORBA"}')

    print('\n5. VEREDICTO\n')
    ok = True
    if not rupturas:
        print('   [FALLA] no hay ruptura de monotonia: el documento no se sostiene')
        ok = False
    else:
        for n1, n2, ns in rupturas:
            print(f'   monotonia rota en {n1} -> {n2}'
                  + (f' a {ns:.1f} sigma' if ns else ''))
        print('   => ninguna funcion monotona de %I ajusta los cuatro puntos.')
        print('      La refutacion NO depende de la forma elegida.')
    if not pares:
        print('   [FALLA] no hay par al mismo %I')
        ok = False
    else:
        for a, b, r in pares:
            print(f'   a %I igual (+-{UMBRAL_MISMO_PI} pt) el efecto varia {r:.2f}x'
                  f' => %I no determina el efecto.')
    print('\n   D-064: ARCHIVADA' if ok else '\n   revisar')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
