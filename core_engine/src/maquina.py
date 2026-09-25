#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MAQUINA · software completo del acto de teletransporte de objetos.
Cuatro modos: calibrar · enviar · recibir · verificar.

  python3 maquina.py calibrar  img_fiduciales.png          -> calib.json
  python3 maquina.py enviar    img_*.png                   -> paquete.json  (lo que se transmite)
  python3 maquina.py recibir   paquete.json                -> ordenes.csv   (donde colocar)
  python3 maquina.py verificar paquete.json 's*.png' 'd*.png'  -> veredicto

SUELO y ACTO se separan por DONDE se coloca, no por cuantas veces se fotografia:
  suelo  s*.png : leer en A -> colocar en A -> leer en A   (lectura + colocacion)
  acto   d*.png : leer en A -> colocar en B -> leer en B   (+ el acuerdo entre estaciones)
Fotografiar dos veces la misma colocacion mide la camara, NO la maquina (regla 413).

Sin dependencias mas alla de numpy/scipy/PIL. Cero nervioso.
"""
import sys, json, math, glob
import numpy as np
from scipy.optimize import least_squares
from scipy import ndimage

# ── PARAMETROS DE LA MAQUINA (se ajustan una vez, en calib.json) ──
CAMPO_MM   = 200.0     # lado del campo de vision
R_BOLA_MM  = 12.70     # radio nominal de la unidad
L_CAM_MM   = 1500.0    # distancia camara-plano  (>= 1500, D-613)
N_FID      = 9         # fiduciales en la placa
N_IMP      = 100_000   # impostores. La cota afirmable es 3/N_IMP: con 32 era 1 entre 11
N_SUELO_MIN= 10        # re-colocaciones minimas para estimar delta (D-614)
K_DELTA    = 3.0       # delta = K * dispersion relativa del suelo * raiz(2). PREINSCRITO.
# D-676 · el percentil del inventario SE LIGA A n. Con n unidades, el percentil p
# tolera (100-p)/100*n atipicos: p98 con n=50 tolera EXACTAMENTE 1, luego NO puede
# detectar una unidad desplazada. Medido: p98 -> 10 % de deteccion, p99 -> 100 %.
#    p >= 100 (1 - 1/(2n))     para n=50 -> p >= 99,0
def pct_inv(n):  return 100.0 * (1.0 - 1.0/(2.0*n))
PCT_INV    = 99.0      # se recalcula por acto con pct_inv(n). D-611 fijaba 98: era el borde

# ═════════════════════════════════════════════════════════════════
#  1 · VISION: de imagen a coordenadas
# ═════════════════════════════════════════════════════════════════
def blobs(im, umbral=0.5, area_min=200):
    """siluetas oscuras sobre fondo retroiluminado -> centros por centroide de intensidad"""
    m = im < umbral
    lab, n = ndimage.label(m)
    out = []
    for i in range(1, n + 1):
        sel = lab == i
        a = int(sel.sum())
        if a < area_min:
            continue
        w = (1.0 - im) * sel                       # peso = oscuridad
        yy, xx = np.mgrid[0:im.shape[0], 0:im.shape[1]]
        s = w.sum()
        out.append((float((w * xx).sum() / s), float((w * yy).sum() / s), a))
    return out

def diametros(b, forma):
    """el area de la silueta da el diametro: es la IDENTIDAD de la unidad (D-611).
    Con 25 diametros distintos, la estacion B sabe QUE unidad tiene en la mano sin
    ninguna etiqueta. Es lo que hace posible phi = 1."""
    k = CAMPO_MM / max(forma)
    return 2.0 * np.sqrt(np.asarray(b)[:, 2] / math.pi) * k

def px_a_mm(p, forma):
    """px -> mm con el origen en el centro del campo"""
    k = CAMPO_MM / max(forma)
    return np.column_stack([p[:, 0] * k, p[:, 1] * k])

# ═════════════════════════════════════════════════════════════════
#  2 · CALIBRACION: modelo RADIAL de 4 parametros (D-613)
# ═════════════════════════════════════════════════════════════════
def distorsiona(P, k1, k2, cx, cy):
    c = np.array([cx, cy]); u = (P - c) / (CAMPO_MM / 2)
    r2 = (u ** 2).sum(1, keepdims=True)
    return c + (u * (1 + k1 * r2 + k2 * r2 * r2)) * (CAMPO_MM / 2)

def calibra(F_nom, F_med):
    """ajusta k1,k2,cx,cy. 4 parametros, 2*N_FID ecuaciones -> sobra con 9 fiduciales"""
    sol = least_squares(lambda p: (distorsiona(F_nom, *p) - F_med).ravel(),
                        [0.0, 0.0, CAMPO_MM / 2, CAMPO_MM / 2])
    return dict(k1=float(sol.x[0]), k2=float(sol.x[1]),
                cx=float(sol.x[2]), cy=float(sol.x[3]),
                rms_um=float(1000 * np.sqrt((sol.fun ** 2).mean())))

def desdistorsiona(Pd, c):
    """invierte el modelo: del punto medido al punto real"""
    f = lambda q: (distorsiona(q.reshape(-1, 2), c['k1'], c['k2'], c['cx'], c['cy']) - Pd).ravel()
    return least_squares(f, Pd.ravel()).x.reshape(-1, 2)

def corrige_silueta(P):
    """una esfera fuera de eje no proyecta su centro. Factor exacto 1/(1-R^2/D^2) (D-613)"""
    c = np.array([CAMPO_MM / 2, CAMPO_MM / 2])
    u = P - c
    D = np.sqrt((u ** 2).sum(1) + L_CAM_MM ** 2)
    return c + u * (1 - R_BOLA_MM ** 2 / D ** 2)[:, None]


def corrige_altura(P, diam_mm, r_asiento_mm=1.5):
    """
    Las unidades de distinto diametro se asientan a distinta ALTURA, y con una
    lente no telecentrica eso da un error radial proporcional: r_ap = r*L/(L-h).
    Hasta **400 um** en el borde del campo con diametros de 6 a 18 mm (D-663).
    Es DETERMINISTA y lo conocemos, porque el diametro ES el criterio de identidad.
    """
    R = np.asarray(diam_mm) / 2.0
    h = np.sqrt(np.maximum(R**2 - r_asiento_mm**2, 0.0))   # altura del centro sobre el circulo de apoyo
    c = np.array([CAMPO_MM/2, CAMPO_MM/2])
    L = L_CAM_MM
    return c + (P - c) * ((L - h) / L)[:, None]

def lee_imagen(im, calib, fid_nom):
    """imagen -> coordenadas corregidas de las unidades, en mm"""
    b = np.array(blobs(im))
    if len(b) == 0: return np.zeros((0, 2)), np.zeros(0)
    # NO se filtra por area: con 25 radios distintos (D-611) la bola menor tiene el 23 %
    # del area mediana y un filtro de tamaño la borraria. Los fiduciales viven en la PLACA
    # y se fotografian en el paso de calibracion, que es una imagen aparte.
    P = px_a_mm(b[:, :2], im.shape)
    d = diametros(b, im.shape)
    P = corrige_silueta(desdistorsiona(P, calib))
    P = corrige_altura(P, d)          # <- D-663: paralaje por altura de asiento
    return P, d

# ═════════════════════════════════════════════════════════════════
#  3 · CONTRATO
# ═════════════════════════════════════════════════════════════════
def omega(A, B, pct=50):
    from scipy.spatial import cKDTree
    if len(A) == 0 or len(B) == 0: return 1.0
    dA, _ = cKDTree(B).query(A); dB, _ = cKDTree(A).query(B)
    esc = max((A.max(0) - A.min(0)).max(), (B.max(0) - B.min(0)).max(), 1e-9)
    return float(0.5 * (np.percentile(dA, pct) + np.percentile(dB, pct)) / esc)

def veredicto(origen, destino, suelos, impostores, suelos_inv=None):
    """los tres numeros y el fallo.
    suelos: Om(origen, RE-COLOCACION en la misma estacion). NO relecturas (regla 413)."""
    # delta NO se elige: sale de la dispersion del propio suelo (D-614). Un delta fijo
    # sin fijar n no significa nada — Om es la mediana de n distancias y su ruido va como
    # 1/raiz(n): con n=25 hace falta delta=0,61 y con n=200 basta 0,18.
    if len(suelos) < N_SUELO_MIN:
        raise SystemExit(f'  ABORTA: {len(suelos)} re-colocaciones de suelo, '
                         f'hacen falta {N_SUELO_MIN} para estimar delta (D-614)')
    su = float(np.median(suelos))
    disp_rel = float(np.std(suelos) / np.mean(suelos))
    DELTA = K_DELTA * disp_rel * math.sqrt(2)
    umb = (1 + DELTA) * su
    disp = omega(origen, destino)                        # disposicion
    inv  = omega(origen, destino, PCT_INV)               # inventario (D-611)
    # el inventario se juzga contra el SUELO DEL p98, no contra el de la mediana: el p98 de
    # una Rayleigh vale ~2,8 veces su mediana y mezclarlos es comparar inconmensurables (D-363)
    su_i = float(np.median(suelos_inv)) if suelos_inv else su
    di_i = float(np.std(suelos_inv) / np.mean(suelos_inv)) if suelos_inv else disp_rel
    umb_i = (1 + K_DELTA * di_i * math.sqrt(2)) * su_i
    imp  = float(np.median(impostores)) if impostores else float('nan')
    A = math.sqrt(imp / max(disp, 1e-12)) if impostores else float('nan')
    # ---- D-666 · el contrato se declara como TASA, no como cociente ----------------
    # A = sqrt(Om_imp_MEDIANA/Om_acto) es una RAZON DE SEPARACION: contesta "estoy mas
    # cerca que un impostor TIPICO?". La pregunta del contrato es por el MAS CERCANO, y
    # el minimo no es una cota porque baja con k (D-665). La cifra del gremio es la tasa:
    #     FAR = P(Om_imp <= Om_acto)
    # y con CERO impostores por debajo del acto, lo maximo afirmable es la regla de tres
    # (Hanley & Lippman-Hand 1983):  FAR <= 3/k  al 95 %. SIN SU k, UN FAR NO DICE NADA.
    k    = len(impostores)
    bajo = int(np.sum(np.asarray(impostores) <= disp)) if k else 0
    far_obs  = bajo / k if k else float('nan')
    far_cota = 3.0 / k if (k and bajo == 0) else float('nan')   # cota 95 % con 0 eventos
    mu, sd   = (float(np.mean(impostores)), float(np.std(impostores))) if k > 1 else (float('nan'),)*2
    d_prime  = (mu - disp) / sd if k > 1 and sd > 0 else float('nan')   # Daugman 2006
    # ---- D-675 · ZONA MUERTA de A. "A > 1" no tenia banda de incertidumbre ----
    # A = sqrt(Om_imp/Om_acto), luego  dA/A = 0,5*sqrt(u_imp^2 + u_acto^2).
    # Con u = 10 % en cada Omega, A en [0,934 , 1,071] es un EMPATE, no un contrato.
    # Las dos u son medibles: la del acto sale del suelo, la del impostor de su propia
    # dispersion. Un acto con A = 1,05 NO esta certificado.
    u_acto = disp_rel
    u_imp  = (sd / mu) if (k > 1 and mu > 0) else 0.0
    dA_rel = 0.5 * math.sqrt(u_acto**2 + u_imp**2)
    A_min  = 1.0 + dA_rel
    return dict(suelo=su, umbral=umb, delta=DELTA, dispersion_suelo=disp_rel,
                suelo_inv=su_i, umbral_inv=umb_i, omega_disposicion=disp, omega_inventario=inv,
                impostor=imp, A=A,
                n_impostores=k, far_observado=far_obs, far_cota95=far_cota,
                A_min=A_min, zona_muerta=(1/(1+dA_rel), A_min),
                d_prime=d_prime, impostor_min=float(np.min(impostores)) if k else float('nan'),
                pasa_disposicion=bool(disp <= umb),
                pasa_inventario=bool(inv <= umb_i),
                # el contrato exige DOS cosas: separacion (A>1) y una tasa afirmable
                # D-675: fuera de la zona muerta, no sólo > 1
                pasa_contrato=bool(A > A_min and bajo == 0) if impostores else None,
                n_origen=len(origen), n_destino=len(destino),
                pasa_recuento=bool(len(origen) == len(destino)))

# ═════════════════════════════════════════════════════════════════
#  4 · CLI
# ═════════════════════════════════════════════════════════════════
def carga(p):
    from PIL import Image
    return np.asarray(Image.open(p).convert('L'), dtype=float) / 255.

def main():
    if len(sys.argv) < 2: print(__doc__); return
    modo = sys.argv[1]
    # D-667 · esta placa NO se cambia a anillos, y la razon esta medida:
    # estos 9 fiduciales ajustan k1,k2,cx,cy -> DISTORSION RADIAL, y aqui no se rota
    # nada, luego el argumento de armonicos de D-664 no aplica. Lo que decide el error
    # en el borde no es la topologia sino si los puntos ALCANZAN el borde (r=124):
    #   rejilla 3x3 (r_max=120,2) ....... 0,36 um       <- se queda
    #   3 anillos 40/70/100 (r_max=100) . 1,79 um  (5x peor: extrapola r^4)
    #   3 anillos 40/82/124 (r_max=124) . 0,35 um  (empate, no compensa el cambio)
    rejilla = np.linspace(15, 185, int(math.sqrt(N_FID)))
    fid_nom = np.array([[x, y] for x in rejilla for y in rejilla])

    if modo == 'calibrar':
        im = carga(sys.argv[2]); b = np.array(blobs(im))
        F = px_a_mm(b[:, :2], im.shape)
        # la correspondencia NO puede hacerse ordenando: la distorsion que se va a medir
        # desordena las coordenadas con que se ordenaria. Se empareja por proximidad a la
        # rejilla nominal, inequivoca porque el paso (85 mm) >> la distorsion (~12 mm).
        from scipy.optimize import linear_sum_assignment
        D = np.linalg.norm(fid_nom[:, None, :] - F[None, :, :], axis=2)
        _, col = linear_sum_assignment(D)
        c = calibra(fid_nom, F[col])
        json.dump(c, open('calib.json', 'w'), indent=1)
        print(f"  calibrado · k1={c['k1']:+.5f} k2={c['k2']:+.5f} "
              f"centro=({c['cx']:.2f},{c['cy']:.2f}) · RMS **{c['rms_um']:.2f} um**")

    elif modo == 'enviar':
        c = json.load(open('calib.json'))
        ims = sorted(sum([glob.glob(a) for a in sys.argv[2:]], []))
        # LEER RETIRANDO: n+1 imagenes, la coordenada sale de la DIFERENCIA (D-606)
        L = [lee_imagen(carga(p), c, fid_nom) for p in ims]
        coords, ident = [], []
        from scipy.spatial import cKDTree
        for i in range(len(L) - 1):
            P, D = L[i]; Q, _ = L[i + 1]
            d, _ = cKDTree(Q).query(P) if len(Q) else (np.full(len(P), 9e9), None)
            j = int(np.argmax(d))
            coords.append(P[j].tolist()); ident.append(float(D[j]))  # pose + QUIEN es
        paq = dict(unidades=coords, identidad_mm=ident, n=len(coords),
                   campo_mm=CAMPO_MM, pct_inventario=PCT_INV,
                   phi=1, nota='la MATERIA viaja: en destino no hay repuestos')
        json.dump(paq, open('paquete.json', 'w'), indent=1)
        print(f"  enviado · **{len(coords)} unidades** · "
              f"**{len(json.dumps(paq))/1024:.1f} kB** · origen destruido")

    elif modo == 'recibir':
        p = json.load(open(sys.argv[2]))
        with open('ordenes.csv', 'w') as f:
            f.write('n,x_mm,y_mm,diametro_mm\n')
            for i, ((x, y), d) in enumerate(zip(p['unidades'], p['identidad_mm']), 1):
                f.write(f'{i},{x:.4f},{y:.4f},{d:.4f}\n')
        print(f"  recibido · **{p['n']} ordenes** en ordenes.csv · el receptor NO ve el original")

    elif modo == 'verificar':
        c = json.load(open('calib.json')); p = json.load(open(sys.argv[2]))
        O = np.array(p['unidades'])
        I = np.array(p['identidad_mm'])
        S = [lee_imagen(carga(q), c, fid_nom)[0] for q in sorted(glob.glob(sys.argv[3]))]
        DD= [lee_imagen(carga(q), c, fid_nom)    for q in sorted(glob.glob(sys.argv[4]))]
        D = [d[0] for d in DD]
        # el suelo es RE-COLOCAR en la misma estacion, no re-fotografiar (regla 413)
        suelos     = [omega(O, s) for s in S]
        suelos_inv = [omega(O, s, PCT_INV) for s in S]
        # IMPOSTOR = direcciones de destino EQUIVOCADAS. Permutar etiquetas NO vale:
        # un conjunto de puntos permutado es el MISMO conjunto y Om sale 0 (falso positivo).
        # El impostor es el mismo inventario colocado en OTRA disposicion del mismo campo.
        imps = [omega(O, np.random.default_rng(i).uniform(O.min(0), O.max(0), O.shape))
                for i in range(N_IMP)]   # D-666: FAR <= 3/N_IMP, no negociable
        v = veredicto(O, D[0], suelos, imps, suelos_inv)
        v['n_suelo'] = len(S)
        # IDENTIDAD · el criterio que SOLO existe con phi = 1. Con repuestos cualquier
        # unidad vale para cualquier sitio y esta prueba no se puede ni plantear.
        from scipy.spatial import cKDTree
        Dp, Di = DD[0]
        if len(Dp):
            _, j = cKDTree(Dp).query(O)          # que unidad llego a cada direccion
            err = np.abs(Di[j] - I)
            tol = 0.5 * np.min(np.diff(np.sort(I)))   # media separacion entre diametros
            v['identidad_err_max_mm'] = float(err.max()); v['identidad_tol_mm'] = float(tol)
            v['n_mal_colocadas'] = int((err > tol).sum())
            v['pasa_identidad'] = bool(err.max() <= tol)
        print(f"\n  SUELO      **{v['suelo']:.5f}**   (de {len(suelos)} pares de lecturas)")
        print(f"  UMBRAL     **{v['umbral']:.5f}**   (delta = {v['delta']:.2f}, MEDIDO del suelo)")
        print(f"  ACTO       disposicion **{v['omega_disposicion']:.5f}**  "
              f"{'pasa' if v['pasa_disposicion'] else '**FALLA**'}")
        print(f"             inventario  **{v['omega_inventario']:.5f}**  (umbral {v['umbral_inv']:.5f})  "
              f"{'pasa' if v['pasa_inventario'] else '**FALLA**'}")
        print(f"  RECUENTO   {v['n_origen']} -> {v['n_destino']}  "
              f"{'pasa' if v['pasa_recuento'] else '**FALLA**'}")
        print(f"  IDENTIDAD  error max **{v['identidad_err_max_mm']:.4f} mm** "
              f"(tol {v['identidad_tol_mm']:.4f})  " +
              ("pasa" if v['pasa_identidad'] else
               f"**FALLA: {v['n_mal_colocadas']} unidades en direccion ajena**"))
        print(f"  IMPOSTOR   **{v['impostor']:.5f}**  mediana de {v['n_impostores']} direcciones"
              f" equivocadas · minimo {v['impostor_min']:.5f}")
        print(f"  FAR        {v['bajo'] if 'bajo' in v else int(v['far_observado']*v['n_impostores'])}"
              f"/{v['n_impostores']} por debajo del acto  ->  **FAR <= {v['far_cota95']:.1e}** (regla de 3, 95 %)")
        print(f"  d'         {v['d_prime']:.1f}   (indice de decidibilidad, Daugman 2006)")
        print(f"  ZONA MUERTA A in [{v['zona_muerta'][0]:.3f}, {v['zona_muerta'][1]:.3f}] "
              f"-> el contrato exige **A > {v['A_min']:.3f}**, no A > 1")
        print(f"  CONTRATO   A = **{v['A']:.2f}**   "
              f"{'existe' if v['pasa_contrato'] else '**NO EXISTE**'}\n")
        json.dump(v, open('veredicto.json', 'w'), indent=1)
    else:
        print(__doc__)

if __name__ == '__main__':
    main()
