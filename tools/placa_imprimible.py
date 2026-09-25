#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera la placa de anillos del GATE-0 lista para imprimir en A4, a escala 1:1.

  python3 tools/placa_imprimible.py salida.pdf

IMPRESION · sin escalado. En el dialogo de impresion, "Tamano real" / "100 %" /
"Escala: ninguna". La barra de comprobacion debe medir 100,0 mm con una regla.
Si no mide 100,0, la foto seguira valiendo para alpha (que es adimensional) pero
D(176 mm) en micras saldra escalado.
"""
import sys, math
sys.path.insert(0, 'experiments/lib')
from placa_anillos import placa, L as CAMPO, R_BORDE
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

D_FID = 6.0          # mm, diametro del disco fiducial
def build(dst):
    c = canvas.Canvas(dst, pagesize=A4)
    W, H = A4
    ox, oy = (W - CAMPO*mm)/2, (H - CAMPO*mm)/2 + 6*mm     # centrado, hueco abajo
    c.setLineWidth(0.3); c.setStrokeColorRGB(.6,.6,.6)
    c.rect(ox, oy, CAMPO*mm, CAMPO*mm)                      # marco del campo
    # campo util redondo
    c.setDash(2,3)
    c.circle(ox + CAMPO/2*mm, oy + CAMPO/2*mm, R_BORDE*mm)
    c.setDash()
    # los 25 fiduciales
    c.setFillColorRGB(0,0,0); c.setStrokeColorRGB(0,0,0)
    P = placa()
    for x, y in P:
        c.circle(ox + x*mm, oy + y*mm, D_FID/2*mm, stroke=0, fill=1)
    # tres marcas de registro en esquinas: fijan orientacion y detectan volteo
    c.setLineWidth(0.8)
    for dx, dy in ((8,8),(CAMPO-8,8),(8,CAMPO-8)):
        c.line(ox+(dx-4)*mm, oy+dy*mm, ox+(dx+4)*mm, oy+dy*mm)
        c.line(ox+dx*mm, oy+(dy-4)*mm, ox+dx*mm, oy+(dy+4)*mm)
    # barra de comprobacion de escala
    by = oy - 13*mm
    c.setLineWidth(1.0)
    c.line(ox, by, ox + 100*mm, by)
    for t in (0, 50, 100):
        c.line(ox + t*mm, by - 2*mm, ox + t*mm, by + 2*mm)
    c.setFont('Helvetica', 7.5); c.setFillColorRGB(0,0,0)
    c.drawString(ox, by - 9*mm, 'COMPROBACION DE ESCALA: esta barra debe medir 100,0 mm. '
                                'Imprimir al 100 %, sin ajustar a pagina.')
    c.setFont('Helvetica-Bold', 8.5)
    c.drawString(ox, oy + CAMPO*mm + 7*mm,
                 'ELPH-N · GATE-0 · placa de 5 anillos × 5 fiduciales (25)')
    c.setFont('Helvetica', 7.5)
    c.drawString(ox, oy + CAMPO*mm + 2.5*mm,
                 f'campo {CAMPO:.0f} × {CAMPO:.0f} mm · campo util r ≤ {R_BORDE:.0f} mm · '
                 f'fiducial ⌀ {D_FID:.0f} mm · giro válido n = 5 (72°)')
    # pie: identificacion de la pieza, a rellenar a mano
    c.setFont('Helvetica', 7.5)
    c.drawString(ox, by - 19*mm, 'PIEZA  ......................   PROCESO  ......................   '
                                 'FECHA  ..............   HORA  ..........   T (°C)  ..........')
    c.showPage(); c.save()
    return dst

if __name__ == '__main__':
    print('escrito:', build(sys.argv[1] if len(sys.argv) > 1 else 'gate0_placa_A4.pdf'))
