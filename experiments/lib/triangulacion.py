# -*- coding: utf-8 -*-
"""TRIANGULACION · el marco como sistema de propagacion de restricciones.

Idea del investigador: muchas metricas del programa se han tratado como PERILLAS cuando en
realidad son VARIABLES DERIVADAS, fijadas algebraicamente por los anclajes. Si se declaran los
anclajes y se deriva el resto, el espacio de parametros se colapsa y **el sistema avisa solo**
cuando alguien toca una cifra que ya estaba congelada.

TRES CAPAS ESTRICTAS
  ANCLA     medido o externo, no negociable
  DERIVADA  queda fijada por los anclajes; tocarla a mano es un ERROR
  LIBRE     eleccion de diseño, se puede mover

Uso:  python3 experiments/lib/triangulacion.py
      -> deriva todo, contrasta contra lo PUBLICADO y marca las discrepancias.
"""
import numpy as np
from scipy.stats import chi

# ══════════════ CAPA 1 · ANCLAJES ══════════════
A = dict(
    # biologia y geometria (EXTERNO / ARITMETICA sobre conteos)
    N_celulas      = (3.36e13, 'celulas del cuerpo · envolvente Bianconi 2013 / Sender 2016 / Hatton 2023 · D-409'),
    N_sinapsis     = (1.50e14, 'sinapsis encefalicas'),
    V_cuerpo_L     = (70.0,    'volumen del cuerpo'),
    L_neurita_mm   = (10.0,    'neurita por neurona cortical humana'),
    # medidos en el programa
    k_sigma_d      = (0.1407,  'razon sigma*/d · D-376, dos espacios al 4,9 %'),
    Omega_contrato = (0.05,    'contrato'),
    TOL_conn       = (5.294e-3,'error de conexion tolerado · AFINA v4 D-409, 1.500 semillas, +-4,4 %'),
    alpha_fus      = (2.2,     'amplificacion fusion->conexion · E1, D-374'),
    lam_sobre_d    = (27.378,    'longitud de correlacion del campo · D-377'),
    beta_escala    = (0.0725,  'exponente de f*(K) · D-402'),
    pend_barrios   = (0.3271,   'sigma* ~ B^p · D-384'),
    bits_arista    = (8.0,     'codo de cuantizacion en espacio corporal · D-392'),
    adyac_lugar    = (11.4,    'adyacencias por lugar · D-372'),
    rho_natural    = (4.99,    'radio espectral natural · D-388'),
    # externos de instrumentacion
    FFN_fus_mm     = (4/97.0,  'fusiones por mm · Januszewski 2018'),
    tau_lisis_Pa   = (5.0,     'cortante donde cae la viabilidad · literatura, POR MEDIR'),
    # **DOS FLUIDOS, y el marco no lo declaraba.** La triangulacion lo cazo en su primera
    # ejecucion: Q salia 100x distinto segun cual se usara, y 100 es la razon de viscosidades.
    mu_bioink      = (0.1,     'viscosidad del portador celular en la boquilla · D-390'),
    mu_acuoso      = (1e-3,    'viscosidad del medio en el chip de viabilidad · D-397'),
    tasa_sincro    = (6.4e10/30,'voxeles/s por linea de sincrotron'),
    E_gesto_pJ     = (23.23,   'energia por gesto · D-373 C3'),
)
V = {k:v[0] for k,v in A.items()}

# ══════════════ CAPA 2 · DERIVADAS ══════════════
D = {}
D['d_celula_um']   = (V['V_cuerpo_L']/1000/V['N_celulas'])**(1/3)*1e6
D['sigma_um']      = V['k_sigma_d']*D['d_celula_um']
D['f_estrella']    = float(chi.sf(D['d_celula_um']/(2*D['sigma_um']),3))
D['lugares']       = V['N_celulas']+V['N_sinapsis']
D['portador_TB']   = D['lugares']*V['adyac_lugar']*V['bits_arista']/8/1e12
D['gestos']        = D['lugares']*V['adyac_lugar']
D['energia_kJ']    = D['gestos']*V['E_gesto_pJ']*1e-12/1e3
D['lam_um']        = V['lam_sobre_d']*D['d_celula_um']
D['fiduciales']    = V['V_cuerpo_L']*1e-3/((D['lam_um']/2)*1e-6)**3
# tramo optimo de trazado: maximiza p_costura admisible
Ls = np.linspace(1,120,2000)/1000.0
p  = (V['TOL_conn']-V['FFN_fus_mm']*Ls)*Ls/V['L_neurita_mm']
i  = int(np.argmax(p))
D['L_tramo_um']    = Ls[i]*1000
D['p_costura_max'] = p[i]
D['costuras_neu']  = V['L_neurita_mm']*1000/D['L_tramo_um']
# caudal por boquilla, fijado por el cortante
R = 400e-6
D['Q_boquilla_uLs']= V['tau_lisis_Pa']*np.pi*R**3/(4*V['mu_bioink'])*1e9
D['Q_chip_uLs']    = 2.5   # el chip se opera al MISMO caudal que la boquilla, por diseño
D['w_chip_1Pa_mm'] = 6*V['mu_acuoso']*2.5e-9/(1.0*(12e-6)**2)*1e3
D['w_chip_25Pa_mm']= 6*V['mu_acuoso']*2.5e-9/(25.0*(12e-6)**2)*1e3
D['f_cuerpo']      = 1.734*(D['lugares']/125)**(-V['beta_escala'])/100
D['sigma_cuerpo_um']=D['d_celula_um']/(2*chi.ppf(1-D['f_cuerpo'],3))
for B in (1e3,1e4):
    D[f'sigma_barrio_{int(B):d}_um']=D['sigma_cuerpo_um']*B**V['pend_barrios']

# ══════════════ CAPA 3 · LIBRES ══════════════
LIBRE = ['numero de boquillas','numero de lineas de sincrotron','tamaño de barrio B',
         'reparto del presupuesto entre etapas','rho impuesto (4,0 frente a 4,99 natural)']

# ══════════════ CONTRASTE contra lo PUBLICADO ══════════════
PUB = dict(
    d_celula_um=(12.35,'D-376'), sigma_um=(1.74,'D-376'),
    portador_TB=(2134.,'D-392'), energia_kJ=(49.6,'D-373'),
    lam_um=(395.,'D-396'), fiduciales=(9.07e9,'D-396'),
    L_tramo_um=(36.,'D-396'), p_costura_max=(5.46e-6,'D-396'),
    Q_boquilla_uLs=(2.5,'D-390'), w_chip_1Pa_mm=(104.,'D-397'), w_chip_25Pa_mm=(4.2,'D-397'), sigma_cuerpo_um=(1.62,'D-402'),
    sigma_barrio_10000_um=(74.7,'D-402'),
)
if __name__=='__main__':
    print('\n  ═════ TRIANGULACION · el marco como sistema de restricciones ═════\n')
    print(f'  ANCLAJES declarados: {len(A)}   ·   DERIVADAS: {len(D)}   ·   LIBRES: {len(LIBRE)}\n')
    print(f"  {'derivada':>26}{'calculado':>15}{'publicado':>14}{'razon':>9}  fuente")
    mal=0
    for k,(pv,src) in PUB.items():
        cv=D[k]; r=cv/pv
        ok=0.95<=r<=1.05
        if not ok: mal+=1
        print(f'  {k:>26}{cv:15.4g}{pv:14.4g}{r:9.3f}  {src}'+('' if ok else '   <-- DISCREPA'))
    print(f'\n  discrepancias: **{mal} de {len(PUB)}**')
    print(f'\n  ── derivadas que NADIE puede tocar a mano ──')
    for k in ('sigma_um','f_estrella','L_tramo_um','p_costura_max','Q_boquilla_uLs',
              'fiduciales','sigma_cuerpo_um'):
        print(f'    {k:<22} = {D[k]:.6g}')
    print(f'\n  ── lo que SI es libre ──')
    for x in LIBRE: print(f'    · {x}')
    print(f'\n  ── propagacion: si un ancla cambia, esto se mueve solo ──')
    for nom,fac in (('tau_lisis_Pa',0.5),('k_sigma_d',1.2),('TOL_conn',0.5)):
        v0=V[nom]; V[nom]=v0*fac
        R2=400e-6
        q=V['tau_lisis_Pa']*np.pi*R2**3/(4*V['mu_bioink'])*1e9
        s=V['k_sigma_d']*D['d_celula_um']
        Ls2=np.linspace(1,120,2000)/1000.0
        p2=(V['TOL_conn']-V['FFN_fus_mm']*Ls2)*Ls2/V['L_neurita_mm']
        j=int(np.argmax(p2))
        print(f'    {nom} x{fac}  ->  Q={q:.2f} uL/s · sigma*={s:.2f} um · '
              f'L_tramo={Ls2[j]*1000:.0f} um · p_costura={p2[j]:.2e}')
        V[nom]=v0
