#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GATE-0 · la unica pregunta de la que cuelga la arquitectura (D-622).

  ¿El desacuerdo entre dos bandejas del mismo lote CRECE con la separacion?

      D(r) = | (p_i - p_j)_A  -  (p_i - p_j)_B |  =  C * r^alpha

      alpha ~ 1    campo SUAVE       -> la afin local lo mata como (r/L)^2.  PASA
      alpha ~ 0,5  paseo aleatorio   -> solo da raiz(r/L).                   INTERMEDIO
      alpha ~ 0    independiente     -> la jerarquia NO sirve.               FALLA

  PREDICCION PREINSCRITA:  alpha = 1,0 +- 0,2

  uso:  python3 gate0.py bandejaA.png bandejaB.png       (con calib.json)
        python3 gate0.py --autotest                      (valida el instrumento)
"""
import sys, json, math, os
import numpy as np

def alpha(PA, PB):
    """ajusta D(r) = C*r^alpha sobre TODOS los pares. Devuelve alpha, C, R2, n_pares."""
    assert PA.shape == PB.shape and len(PA) >= 4, 'hacen falta >= 4 fiduciales emparejados'
    # se quita la traslacion comun: no es un desacuerdo, es donde esta la bandeja (regla 440)
    A = PA - PA.mean(0); B = PB - PB.mean(0)
    i, j = np.triu_indices(len(A), 1)
    r = np.linalg.norm(A[i] - A[j], axis=1)
    D = np.linalg.norm((A[i] - A[j]) - (B[i] - B[j]), axis=1)
    # D-693 · ATAQUE POR EXTREMO OPUESTO. Con un campo PERFECTO todos los D valen 0,
    # el filtro los quita, quedan 0 pares y alpha salia **nan** -> veredicto "SIN DATO".
    # **El instrumento fallaba en el caso MEJOR POSIBLE**, que es el peor sitio para fallar.
    # Un campo por debajo del suelo del lector no es ausencia de dato: es un campo
    # perfectamente suave, y eso es alpha = 1 por construccion.
    # El suelo NO puede ser una constante absoluta: esta funcion se llama en mm (main)
    # y en metros (autotest). **Poner 0,52e-3 rompio el autotest al instante** — la misma
    # clase de error dimensional de la regla 601. Se usa un suelo RELATIVO a la escala
    # de la propia configuracion, que es adimensional y vale en cualquier unidad.
    SUELO_REL = 1e-9                  # D/r por debajo de esto = campo perfecto
    ok = (r > 0) & (D > SUELO_REL * r)
    if (r > 0).sum() >= 3 and ok.sum() < 3:
        return 1.0, float(np.median(D[r > 0])), 1.0, int((r > 0).sum())
    if ok.sum() < 3: return float('nan'), float('nan'), 0.0, int(ok.sum())
    x, y = np.log(r[ok]), np.log(D[ok])
    # D-674 · REGRESION ROBUSTA. np.polyfit es OLS y su punto de ruptura es 1/n:
    # UN solo fiducial contaminado (una mota de 50 um sobre 25) arrastraba alpha de
    # 0,974 a 0,765 y convertia PASA en INTERMEDIO. Theil-Sen aguanta el 29,3 %.
    # alpha y D(r0) eran los DOS UNICOS criterios del marco sin estimador robusto,
    # y son los del GATE-0, que es el veto del que cuelga todo lo demas.
    from scipy.stats import theilslopes
    a, b = theilslopes(y, x)[:2]
    R2 = 1 - ((y - (a*x+b))**2).sum() / max(((y - y.mean())**2).sum(), 1e-30)
    return float(a), float(math.exp(b)), float(R2), int(ok.sum())

R0_MM   = 176.0    # separacion de REFERENCIA: el diametro del campo util (D-667)
D0_MAX  = 35.0     # um · el residuo que D-608 exige en el borde

def D_ref(C, al, r0=R0_MM):
    """el desacuerdo en la separacion de referencia, en MICRAS."""
    return C * 1e3 * r0**al

def veredicto(al, C=None):
    """D-649 · la regla es CONJUNTA: GATE-0 es un VETO fiable (98,7 %) y un visto
    bueno malo (46 %), asi que PASA exige suavidad Y amplitud.

    D-669 · pero la amplitud NO se juzga sobre C. En D(r)=C*r^alpha las unidades
    de C son um*mm^(-alpha) y **alpha es un parametro ajustado**: un umbral fijo
    sobre C no es ni dimensionalmente valido (regla 415 dentro de nuestra propia
    regla de decision). Se juzga D(r0) en una separacion de referencia, en micras.
    Medido: el viejo "C <= 12 um" no mordia NUNCA (0 de 1800 campos)."""
    if not np.isfinite(al): return 'SIN DATO'
    if al < 0.35: return 'VETO · error independiente por sitio: cae D-616 y D-621 (fiable 98,7 %)'
    d0 = None if C is None else D_ref(C, al)
    if al >= 0.95 and (d0 is None or d0 <= D0_MAX):
        return 'PASA · campo suave Y amplitud dentro del presupuesto'
    if al >= 0.95:
        return f'INTERMEDIO · alpha vale pero D({R0_MM:.0f} mm) = {d0:.1f} um > {D0_MAX:.0f}'
    return 'INTERMEDIO · NO basta para lanzar el acto'

# ── validacion del instrumento sobre campos de alpha CONOCIDO ──
def autotest(n=9, L=0.2, T=200, semilla=0):
    rng = np.random.default_rng(semilla)
    q = int(math.sqrt(n)); g = np.linspace(0.075*L, 0.925*L, q)
    P = np.array([[x, y] for x in g for y in g])
    print(f"  validando el instrumento sobre {T} realizaciones, {n} fiduciales\n")
    print(f"  {'campo simulado':<34}{'alpha esperado':>15}{'alpha medido':>15}")
    out = {}
    for nom, esp, gen in (
        ('escala termica (gradiente lineal)', 1.0,
         lambda: P*(1+rng.normal(0,2e-4)) + rng.normal(0,1e-9,P.shape)),
        ('paseo aleatorio espacial', 0.5, None),
        ('ruido independiente por sitio', 0.0,
         lambda: P + rng.normal(0, 3e-6, P.shape)),
    ):
        vals = []
        for _ in range(T):
            if gen is None:                      # campo browniano: covarianza ~ -|r|
                d = np.linalg.norm(P[:,None]-P[None,:], axis=2)
                C = (d.max()-d)*1e-8 + 1e-12*np.eye(len(P))
                Lc = np.linalg.cholesky(C)
                B = P + np.column_stack([Lc@rng.normal(size=len(P)) for _ in range(2)])
            else:
                B = gen()
            a,_,_,_ = alpha(P, B)
            if np.isfinite(a): vals.append(a)
        m, s = float(np.mean(vals)), float(np.std(vals))
        out[nom] = m
        print(f"  {nom:<34}{esp:>15.2f}{m:>11.2f} ± {s:.2f}")
    return out

def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--autotest':
        autotest(); return
    if len(sys.argv) < 3: print(__doc__); return
    sys.path.insert(0, os.path.dirname(__file__))
    import maquina as M
    from PIL import Image
    calib_path = 'calib.json'
    if not os.path.exists(calib_path):
        candidate = os.path.join(os.path.dirname(sys.argv[1]), 'calib.json')
        if os.path.exists(candidate):
            calib_path = candidate
        else:
            candidate2 = os.path.join(os.path.dirname(__file__), '../test_bench/calib.json')
            if os.path.exists(candidate2):
                calib_path = candidate2
    c = json.load(open(calib_path))
    # D-669 · la placa del GATE-0 es de ANILLOS, no la rejilla de la maquina (D-664/667)
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../experiments/lib'))
    from placa_anillos import placa
    fid = placa()
    def leer(p):
        im = np.asarray(Image.open(p).convert('L'), dtype=float)/255.
        P,_ = M.lee_imagen(im, c, fid)
        from scipy.optimize import linear_sum_assignment
        D = np.linalg.norm(fid[:,None,:]-P[None,:,:], axis=2)
        _, col = linear_sum_assignment(D)
        return P[col]
    A, B = leer(sys.argv[1]), leer(sys.argv[2])
    al, C, R2, npar = alpha(A, B)
    print(f"\n  pares usados       **{npar}**")
    print(f"  ajuste D(r)=C*r^a  C = {C:.3e}   R2 = **{R2:.3f}**")
    print(f"  D({R0_MM:.0f} mm)         **{D_ref(C, al):.1f} um**   (presupuesto {D0_MAX:.0f} um)")
    print(f"  **alpha = {al:.2f}**   (preinscrito: 1,0 ± 0,2 · PASA exige >= 0,95)")
    print(f"  VEREDICTO · {veredicto(al, C)}\n")
    json.dump(dict(alpha=al, C=C, R2=R2, D_ref_um=D_ref(C, al), n_pares=npar, veredicto=veredicto(al, C)),
              open('gate0.json','w'), indent=1)

if __name__ == '__main__': main()
