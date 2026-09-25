#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BANCO · genera las imagenes sinteticas que veria la maquina y corre el ciclo entero."""
import numpy as np, os, math
from PIL import Image
import maquina as M

PX=1400; RNG=np.random.default_rng(7)

def render(centros_mm, radios_mm, k1=-0.085, k2=0.012, ruido=0.004):
    """retroiluminado: fondo 1.0, siluetas 0.0, con antialias por supersampling x3 y DISTORSION real"""
    S=3; im=np.ones((PX*S,PX*S))
    esc=PX*S/M.CAMPO_MM
    c=np.array([M.CAMPO_MM/2,M.CAMPO_MM/2])
    yy,xx=np.mgrid[0:PX*S,0:PX*S]
    for (x,y),r in zip(centros_mm,radios_mm):
        # aplicar distorsion de lente al centro proyectado
        u=(np.array([x,y])-c)/(M.CAMPO_MM/2); r2=(u**2).sum()
        p=c+u*(1+k1*r2+k2*r2*r2)*(M.CAMPO_MM/2)
        im[((xx-p[0]*esc)**2+(yy-p[1]*esc)**2)<(r*esc)**2]=0.0
    im=im.reshape(PX,S,PX,S).mean((1,3))
    return np.clip(im+RNG.normal(0,ruido,im.shape),0,1)

def guarda(im,p): Image.fromarray((im*255).astype(np.uint8)).save(p)

os.makedirs('../banco',exist_ok=True); os.chdir('../banco')

# ── 1 · placa de fiduciales: 9 discos pequeños en rejilla conocida ──
rej=np.linspace(15,185,3); FID=np.array([[x,y] for x in rej for y in rej])
guarda(render(FID,[2.0]*9),'fid.png')

# ── 2 · el objeto: 25 bolas de 25 DIAMETROS DISTINTOS (D-611) ──
N=25
R=np.linspace(4.0,12.7,N)                       # radios distintos: la unidad es identificable
C=np.column_stack([RNG.uniform(30,170,N),RNG.uniform(30,170,N)])
for i in range(N):                              # separacion minima
    for _ in range(300):
        if all(np.hypot(*(C[i]-C[j]))>R[i]+R[j]+4 for j in range(N) if j!=i): break
        C[i]=RNG.uniform(30,170,2)

# LEER RETIRANDO: imagen completa, luego se quita una unidad cada vez
orden=RNG.permutation(N)
for k in range(N+1):
    q=[j for j in orden[k:]]
    guarda(render(C[q],R[q]),f'o{k:02d}.png')

# ── 3 · el DESTINO: la otra estacion coloca segun ordenes, con su error real ──
sigma=0.141   # mm · colocador de la maquina (D-609)
Cd=C+RNG.normal(0,sigma,C.shape)
for k in range(3):                              # 3 lecturas del destino -> suelo
    guarda(render(Cd,R,k1=-0.085,k2=0.012),f'd{k}.png')

print(f"  banco listo · {N} unidades · radios {R.min():.1f}-{R.max():.1f} mm · sigma_coloca {sigma} mm")
