"""
VALIDACION DE lib/metodos.py CONTRA LOS DATOS MEDIDOS DEL REPOSITORIO.

La autoprueba de metodos.py comprueba que el codigo hace lo que dice. Esto
comprueba algo distinto y mas exigente: que **reproduce lo que ya se midio**.

Ninguna comprobacion usa datos sinteticos. Todas leen JSON de experimentos
ejecutados y exigen coincidencia exacta o dentro de tolerancia declarada.

  V1  b* adaptativo == b* del barrido exhaustivo, en los 15 experimentos con
      candidatas guardadas, y cuanto ahorra
  V2  el supuesto que hace valida la biseccion se cumple en esos 15
  V3  la envolvente reproduce E-1 celda a celda
  V4  diagnosticar_regimen clasifica bien los experimentos reales, incluido el
      par M-4 / M-4b que motivo la regla
  V5  rasgos_estructurales reproduce la tabla de PROY
  V6  delta_peor_caso sobre pares de tarea REALES (mosca CX/CXinv, raton
      INF/FB)

Uso:  python3 lib/validar_metodos.py
"""
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
EXP = HERE.parent
sys.path.insert(0, str(HERE))
from metodos import (b_estrella_adaptativo, fidelidad_decrece_con_poda,
                     envolvente, diagnosticar_regimen, regla_K,
                     rasgos_estructurales, delta_peor_caso,
                     REGIMEN_ESTABLE, REGIMEN_INESTABLE)

ok_global = True


def chk(cond, msg):
    global ok_global
    print(f'   [{"PASA " if cond else "FALLA"}] {msg}')
    ok_global &= bool(cond)
    return bool(cond)


def con_candidatas():
    out = []
    for f in sorted(EXP.glob('*/results/*.json')):
        try:
            d = json.loads(f.read_text())
        except Exception:
            continue
        po = d.get('punto_operativo')
        if isinstance(po, dict) and 'candidatas' in po and po.get('b_estrella'):
            out.append((f, d, po))
    return out


# --- V1 y V2 -----------------------------------------------------------------
def v1_v2():
    print('\nV1 · b* ADAPTATIVO frente al barrido exhaustivo, en datos reales\n')
    casos = con_candidatas()
    print(f'   {"experimento":42s}{"b* real":>12s}{"b* adapt":>12s}{"ev":>5s}{"rejilla":>9s}')
    tot_ev = tot_rej = 0
    iguales = 0
    supuesto_ok = 0
    for f, d, po in casos:
        cand = {(c['bits'], round(c['poda'], 4)): c for c in po['candidatas']}
        bits = sorted({k[0] for k in cand})
        podas = sorted({k[1] for k in cand})
        fid = lambda b, p: cand.get((b, round(p, 4)), {}).get('fidelidad_pesos', -1.0)
        tas = lambda b, p: cand.get((b, round(p, 4)), {}).get('tasa', float('inf'))
        deg = [tuple(x) for x in (po.get('degeneradas') or [])]
        b_ad, ev = b_estrella_adaptativo(fid, tas, bits, podas,
                                         po.get('umbral_fidelidad', 0.70), deg)
        b_real = tuple(po['b_estrella'])
        b_ad_n = (b_ad[0], round(b_ad[1], 4)) if b_ad else None
        b_real_n = (b_real[0], round(b_real[1], 4))
        igual = b_ad_n == b_real_n
        iguales += igual
        rej = len(cand) - len(deg)
        tot_ev += ev; tot_rej += rej
        nom = f'{f.parent.parent.name}/{f.stem}'
        print(f'   {nom[:42]:42s}{str(b_real_n):>12s}{str(b_ad_n):>12s}'
              f'{ev:5d}{rej:9d}{"" if igual else "   <-- DIFIERE"}')
        okk, _ = fidelidad_decrece_con_poda(fid, bits, podas)
        supuesto_ok += okk
    print()
    chk(iguales == len(casos),
        f'b* adaptativo coincide con el exhaustivo en {iguales}/{len(casos)} experimentos')
    chk(tot_ev < tot_rej,
        f'evaluaciones: {tot_ev} frente a {tot_rej} de rejilla completa '
        f'({100*(1-tot_ev/tot_rej):.0f} % menos)')
    print('\nV2 · el supuesto que hace valida la biseccion\n')
    chk(supuesto_ok == len(casos),
        f'la fidelidad decrece con la poda en {supuesto_ok}/{len(casos)} '
        f'-- si fallara en alguno, ahi NO se puede bisecar')


# --- V3 ----------------------------------------------------------------------
def v3():
    print('\nV3 · la ENVOLVENTE reproduce E-1\n')
    p = EXP / 'E1-envolvente' / 'results' / 'e1_result.json'
    if not p.exists():
        chk(False, 'falta e1_result.json'); return
    e1 = json.loads(p.read_text())
    tasa = e1['tasa_por_celda']
    g = json.loads((EXP / 'G1bis-orden-margen' / 'results' /
                    'g1bis_result.json').read_text())['celdas']
    for M in ('M2_signo', 'M3_gaps'):
        pts = [(tasa[k], g[k][M]['delta']) for k in g]
        mio = envolvente(pts, menor_es_mejor=True)
        suyo = e1['envolvente'][M]
        orden = sorted(g, key=lambda k: tasa[k])
        difs = [abs(mio[i][1] - suyo[k]) for i, k in enumerate(orden)]
        chk(max(difs) < 1e-12,
            f'{M}: coincide con E-1 en las {len(orden)} celdas '
            f'(max dif {max(difs):.2e})')
    # y la conclusion cualitativa
    pts2 = envolvente([(tasa[k], g[k]['M2_signo']['delta']) for k in g])
    pts3 = envolvente([(tasa[k], g[k]['M3_gaps']['delta']) for k in g])
    cruces = sum(1 for i in range(1, len(pts2))
                 if (pts3[i][1] < pts2[i][1]) != (pts3[i-1][1] < pts2[i-1][1]))
    chk(cruces == e1['n_cruces'],
        f'reproduce el numero de cruces de E-1: {cruces} (D-100)')


# --- V4 ----------------------------------------------------------------------
def v4():
    print('\nV4 · diagnosticar_regimen sobre experimentos REALES\n')
    CASOS = [
        ('M-4 mosca CXinv K=500', 'M4-tarea-invertida/results/m4_CXinv_EJECUCION1_INVALIDADA.json', REGIMEN_INESTABLE),
        ('M-4b mosca CXinv K=2000', 'M4-tarea-invertida/results/m4_CXinv.json', REGIMEN_ESTABLE),
        ('M-6 raton FF', 'M6-raton-microns/results/m6_FF.json', REGIMEN_ESTABLE),
        ('M-3 mosca CX', 'M3-roles-biologicos/results/m3_CX.json', REGIMEN_ESTABLE),
        ('H-2 humano FF', 'H2-capas-humanas/results/h2_FF.json', REGIMEN_ESTABLE),
    ]
    for nom, f, esperado in CASOS:
        p = EXP / f
        if not p.exists():
            chk(False, f'{nom}: falta el fichero'); continue
        b = json.loads(p.read_text())['equipo_b']
        sig = {k: v['delta_std'] for k, v in b.items()
               if not v.get('aleatorizada') and not k.startswith('CTRL')}
        r, malas = diagnosticar_regimen(sig)
        chk(r == esperado, f'{nom:26s} -> {r}'
            + (f' (culpable {malas})' if malas else ''))
    # la regla de K, con las cifras reales del par M-4 / M-4b
    K, conf = regla_K(500, 0.0956, 0.03, REGIMEN_INESTABLE)
    chk(conf.startswith('baja') and K <= 2000,
        f'regla_K en inestable: K={K}, confianza {conf} '
        f'(K=2000 basto en la medida real)')


# --- V5 ----------------------------------------------------------------------
def v5():
    print('\nV5 · rasgos_estructurales reproduce la tabla de PROY\n')
    p = EXP / 'PROY-proyector' / 'results' / 'tabla_circuitos.csv'
    if not p.exists():
        chk(False, 'falta tabla_circuitos.csv'); return
    import csv
    filas = list(csv.DictReader(open(p)))
    import pandas as pd
    M3 = EXP / 'M3-roles-biologicos' / 'results'
    meta = json.loads((M3 / 'circuitos_meta.json').read_text())
    INH = ('gaba', 'glutamate')
    for c in ('MB', 'escape', 'CX'):
        sub = pd.read_csv(M3 / f'{c}.csv')
        m = meta[c]
        nodos = [int(x) for x in m['nodos']]
        nt = {int(k): v for k, v in m['nt_por_nodo'].items()}
        inh = {r for r in nodos if nt.get(r) in INH}
        r = rasgos_estructurales(list(sub.pre_root_id), list(sub.post_root_id),
                                 inh, nodos)
        ref = next(x for x in filas if x['circuito'] == f'mosca {c}')
        for campo, clave in (('pct_nodos_inhib', 'pct_inhib'),
                             ('reciprocidad', 'reciprocidad'),
                             ('concentracion_inhib', 'concentracion_inhib')):
            dif = abs(r[campo] - float(ref[clave]))
            chk(dif < 1e-6, f'mosca {c:7s} {campo:20s} {r[campo]:9.4f} '
                            f'== PROY {float(ref[clave]):9.4f}')


# --- V6 ----------------------------------------------------------------------
def v6():
    print('\nV6 · delta_peor_caso sobre pares de tarea REALES\n')
    PARES = [('mosca CX / CXinv',
              {'CX': 'M3-roles-biologicos/results/m3_CX.json',
               'CXinv': 'M4-tarea-invertida/results/m4_CXinv.json'}),
             ('raton INF / FB',
              {'INF': 'M6-raton-microns/results/m6_INF.json',
               'FB': 'M6-raton-microns/results/m6_FB.json'})]
    for nom, fs in PARES:
        d = {}
        for t, f in fs.items():
            p = EXP / f
            if not p.exists():
                break
            b = json.loads(p.read_text())['equipo_b']
            d[t] = {k: v['delta'] for k, v in b.items()
                    if not v.get('aleatorizada') and not k.startswith('CTRL')}
        if len(d) != len(fs):
            chk(False, f'{nom}: faltan ficheros'); continue
        w = delta_peor_caso(d)
        for M, v in sorted(w['delta_wc'].items()):
            reales = {t: d[t][M] for t in d}
            chk(abs(v - max(reales.values())) < 1e-12,
                f'{nom:18s} {M:14s} wc={v:.4f} (peor: {w["tarea_peor"][M]}) '
                f'· tareas {["%.4f" % x for x in reales.values()]}')


if __name__ == '__main__':
    print('VALIDACION DE METODOS CONTRA DATOS MEDIDOS — sin datos sinteticos')
    v1_v2(); v3(); v4(); v5(); v6()
    print('\n' + ('=' * 62))
    print('METODOS VALIDADOS CONTRA DATOS REALES' if ok_global
          else 'HAY FALLOS: alguna formula NO reproduce lo medido')
    sys.exit(0 if ok_global else 1)
