#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Markdown -> PDF cientifico. Tinta negra, serif, cobertura Unicode real.

  uso: python3 tools/md2pdf.py entrada.md salida.pdf "Titulo" "Subtitulo" "Autor" ES|EN

Tipografia
----------
Ninguna fuente del sistema cubre los 73 caracteres no-ASCII que usa el marco, asi que
se combinan tres y se resuelve por caracter:
  · cuerpo      Times New Roman (serif, familia completa)
  · formulas    Menlo (mono con Griego, matematicas y super/subindices)
  · respaldo    Arial Unicode, solo para los glifos que falten en Times
Ademas los super/subindices Unicode se convierten en <super>/<sub> REALES, que es lo
correcto tipograficamente y no depende de que la fuente traiga el glifo precompuesto.
"""
import sys, re, html
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether, PageBreak,
                                CondPageBreak)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.ttfonts import TTFontFile

BLACK = colors.black
GREY  = colors.Color(.40,.40,.40)
RULE  = colors.Color(.70,.70,.70)
SHADE = colors.Color(.955,.955,.955)

# ── registro de fuentes ────────────────────────────────────────────────────────
SUP = '/System/Library/Fonts/Supplemental/'
def reg(name, path, idx=None):
    try:
        pdfmetrics.registerFont(TTFont(name, path, subfontIndex=idx) if idx is not None
                                else TTFont(name, path))
        return True
    except Exception:
        return False

SERIF, SERIF_B, SERIF_I, SERIF_BI = 'Times-Roman','Times-Bold','Times-Italic','Times-BoldItalic'
if (reg('Srf', SUP+'Times New Roman.ttf') and reg('Srf-B', SUP+'Times New Roman Bold.ttf')
        and reg('Srf-I', SUP+'Times New Roman Italic.ttf')
        and reg('Srf-BI', SUP+'Times New Roman Bold Italic.ttf')):
    SERIF, SERIF_B, SERIF_I, SERIF_BI = 'Srf','Srf-B','Srf-I','Srf-BI'
    pdfmetrics.registerFontFamily('Srf', normal='Srf', bold='Srf-B', italic='Srf-I',
                                  boldItalic='Srf-BI')
SANS, SANS_B = 'Helvetica','Helvetica-Bold'
if reg('Sns', SUP+'Arial Unicode.ttf') or reg('Sns', '/Library/Fonts/Arial Unicode.ttf'):
    pass
FALLBACK = 'Sns' if 'Sns' in pdfmetrics.getRegisteredFontNames() else SANS
MONO = 'Courier'
for p, i in (('/System/Library/Fonts/Menlo.ttc', 0), (SUP+'Courier New.ttf', None)):
    if reg('Mno', p, i): MONO = 'Mno'; break
MONO_B = MONO
if MONO == 'Mno' and reg('Mno-B', '/System/Library/Fonts/Menlo.ttc', 1): MONO_B = 'Mno-B'

def _cmap(fname):
    try:
        f = pdfmetrics.getFont(fname).face
        return set(f.charToGlyph.keys())
    except Exception:
        return None
SERIF_CM = _cmap(SERIF)

# ── normalizacion de caracteres que NINGUNA fuente del sistema trae ───────────
SUBST = {
    '\u2c4e':'\u0428',   # ⱎ  unidad Emilio -> Ш (glifo equivalente; se declara en el texto)
    '\u27f9':'\u21d2',   # ⟹ -> ⇒
    '\u27fa':'\u21d4',   # ⟺ -> ⇔
    '\u26a0':'!',        # ⚠ -> !
    '\u2714':'\u2713',   # ✔ -> ✓
}
SUPS = {'\u2070':'0','\u00b9':'1','\u00b2':'2','\u00b3':'3','\u2074':'4','\u2075':'5',
        '\u2076':'6','\u2077':'7','\u2078':'8','\u2079':'9','\u207b':'\u2212','\u207a':'+'}
SUBS = {'\u2080':'0','\u2081':'1','\u2082':'2','\u2083':'3','\u2084':'4','\u2085':'5',
        '\u2086':'6','\u2087':'7','\u2088':'8','\u2089':'9','\u1d62':'i','\u2090':'a'}
SUP_RE = re.compile('[' + ''.join(SUPS) + ']+')
SUB_RE = re.compile('[' + ''.join(SUBS) + ']+')

def normalize(t):
    for a, b in SUBST.items(): t = t.replace(a, b)
    return t

def typographic(t):
    """super/subindices Unicode -> etiquetas reales. Solo para cuerpo y tablas."""
    t = SUP_RE.sub(lambda m: '<super>%s</super>' % ''.join(SUPS[c] for c in m.group(0)), t)
    t = SUB_RE.sub(lambda m: '<sub>%s</sub>'   % ''.join(SUBS[c] for c in m.group(0)), t)
    return t

_TAG = re.compile(r'(<[^>]+>)')
def fallback(t):
    """envuelve en la fuente de respaldo los caracteres que la serif no tiene."""
    if not SERIF_CM: return t
    out = []
    for piece in _TAG.split(t):
        if piece.startswith('<'): out.append(piece); continue
        buf, miss = [], []
        def flush():
            if miss: buf.append('<font face="%s">%s</font>' % (FALLBACK, ''.join(miss))); miss.clear()
        for c in piece:
            if ord(c) < 128 or c in '\n' or ord(c) in SERIF_CM:
                flush(); buf.append(c)
            else:
                miss.append(c)
        flush(); out.append(''.join(buf))
    return ''.join(out)

# ── estilos ───────────────────────────────────────────────────────────────────
def S(**kw):
    kw.setdefault('textColor', BLACK); return ParagraphStyle(kw.pop('name'), **kw)

ST = {
 'h1':   S(name='h1', fontName=SERIF_B, fontSize=15, leading=19, spaceBefore=19,
           spaceAfter=7, keepWithNext=1),
 'h2':   S(name='h2', fontName=SERIF_B, fontSize=11.5, leading=15, spaceBefore=13,
           spaceAfter=4, keepWithNext=1),
 'h3':   S(name='h3', fontName=SERIF_BI, fontSize=10.3, leading=13.6, spaceBefore=10,
           spaceAfter=3, keepWithNext=1),
 'body': S(name='body', fontName=SERIF, fontSize=9.7, leading=13.8, spaceAfter=6,
           alignment=TA_JUSTIFY),
 'li':   S(name='li', fontName=SERIF, fontSize=9.7, leading=13.6, spaceAfter=2.5,
           leftIndent=12, bulletIndent=2, alignment=TA_JUSTIFY),
 'quote':S(name='quote', fontName=SERIF_I, fontSize=9.7, leading=13.8, spaceBefore=4,
           spaceAfter=5, leftIndent=12, rightIndent=6),
 'code': S(name='code', fontName=MONO, fontSize=8.2, leading=11.4, leftIndent=0),
 'th':   S(name='th', fontName=SERIF_B, fontSize=8.2, leading=10.4),
 'td':   S(name='td', fontName=SERIF, fontSize=8.3, leading=10.8),
}

def rebalance(t):
    """el markdown cruza spans; reportlab exige anidamiento estricto."""
    TAGS = re.compile(r'<(/?)(b|i|font|super|sub)(\s[^>]*)?>')
    out, stack, pos = [], [], 0
    for m in TAGS.finditer(t):
        out.append(t[pos:m.start()]); pos = m.end()
        closing, name, attrs = m.group(1), m.group(2), m.group(3) or ''
        if not closing:
            stack.append((name, attrs)); out.append(m.group(0))
        else:
            if name not in [n for n, _ in stack]: continue
            reopen = []
            while stack:
                n, a = stack.pop(); out.append('</%s>' % n)
                if n == name: break
                reopen.append((n, a))
            for n, a in reversed(reopen):
                stack.append((n, a)); out.append('<%s%s>' % (n, a))
    out.append(t[pos:])
    for n, _ in reversed(stack): out.append('</%s>' % n)
    return ''.join(out)

def inline(t):
    t = normalize(t)
    t = html.escape(t, quote=False)
    t = re.sub(r'`([^`]+)`', lambda m: '<font face="%s" size="8.6">%s</font>' % (MONO, m.group(1)), t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    t = re.sub(r'(?<![\w*])\*([^*\n]+?)\*(?![\w*])', r'<i>\1</i>', t)
    t = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
    t = t.replace('`', '')
    return fallback(typographic(rebalance(t)))

def P(txt, style, **kw):
    try:
        return Paragraph(inline(txt), style, **kw)
    except Exception:
        return Paragraph(html.escape(normalize(re.sub(r'[*`_]', '', txt)), quote=False), style, **kw)

def formula_block(lines, W):
    """bloque de formula: mono Unicode, filete arriba y abajo, fondo tenue."""
    body = '<br/>'.join(
        fallback(html.escape(normalize(l), quote=False).replace(' ', '&nbsp;')) or '&nbsp;'
        for l in lines)
    try:    inner = Paragraph(body, ST['code'])
    except Exception:
        inner = Paragraph(html.escape(normalize('\n'.join(lines)), quote=False), ST['code'])
    return Table([[inner]], colWidths=[W], style=TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),SHADE),
        ('LINEABOVE',(0,0),(-1,0),.7,RULE), ('LINEBELOW',(0,-1),(-1,-1),.7,RULE),
        ('LEFTPADDING',(0,0),(-1,-1),9), ('RIGHTPADDING',(0,0),(-1,-1),9),
        ('TOPPADDING',(0,0),(-1,-1),6), ('BOTTOMPADDING',(0,0),(-1,-1),6)]))


def colwidths(hdr, rows, n, W):
    """Anchos proporcionales al CONTENIDO, no a una heuristica de posicion.

    La version anterior daba el 42 % a la primera columna de una tabla de cinco,
    y en el pipeline esa columna es un indice de dos caracteres: el resto quedaba
    estrujado. Se mide el texto real con las metricas de la fuente, se mezcla el
    maximo con la media (para que una celda larga no se lo lleve todo) y se acota
    cada columna entre el 6 % y el 46 % del ancho util.
    """
    def w(txt):
        txt = re.sub(r'[*`\[\]]|\([^)]*\)', '', normalize(txt))
        try:    return pdfmetrics.stringWidth(txt, SERIF, 8.3)
        except Exception: return len(txt) * 4.2
    cols = []
    for j in range(n):
        vals = [w(hdr[j] if j < len(hdr) else '')]
        for r in rows:
            vals.append(w(r[j]) if j < len(r) else 0)
        mx, mean = max(vals), sum(vals)/len(vals)
        cols.append(max(0.6*mx + 0.4*mean, 14.0))
    tot = sum(cols)
    frac = [c/tot for c in cols]
    lo, hi = 0.06, 0.46
    for _ in range(6):                      # acotar y renormalizar
        frac = [min(hi, max(lo, f)) for f in frac]
        t = sum(frac); frac = [f/t for f in frac]
    return [W*f for f in frac]

def parse(md, W):
    out, i, L = [], 0, md.split('\n')
    while i < len(L):
        ln = L[i]
        if ln.startswith('```'):
            i += 1; buf = []
            while i < len(L) and not L[i].startswith('```'): buf.append(L[i]); i += 1
            i += 1
            if buf:
                blk = formula_block(buf, W)
                out.append(Spacer(1,3))
                out.append(KeepTogether(blk) if len(buf) <= 18 else blk)
                out.append(Spacer(1,7))
            continue
        if ln.startswith('|') and i+1 < len(L) and re.match(r'^\|[\s:\-\|]+\|$', L[i+1].strip()):
            def cells(r): return [c.strip() for c in r.strip().strip('|').split('|')]
            hdr = cells(ln)
            aligns = ['RIGHT' if a.strip().endswith(':') and not a.strip().startswith(':')
                      else ('CENTER' if a.strip().startswith(':') and a.strip().endswith(':')
                            else 'LEFT') for a in cells(L[i+1])]
            i += 2; rows = []
            while i < len(L) and L[i].startswith('|'):
                rows.append(cells(L[i])); i += 1
            n = len(hdr)
            data = [[P(c, ST['th']) for c in hdr]]
            for r in rows: data.append([P(c, ST['td']) for c in (r + ['']*n)[:n]])
            cw = colwidths(hdr, rows, n, W)
            st = [('LINEABOVE',(0,0),(-1,0),.9,BLACK), ('LINEBELOW',(0,0),(-1,0),.6,BLACK),
                  ('LINEBELOW',(0,-1),(-1,-1),.9,BLACK), ('VALIGN',(0,0),(-1,-1),'TOP'),
                  ('TOPPADDING',(0,0),(-1,-1),3.4), ('BOTTOMPADDING',(0,0),(-1,-1),3.4),
                  ('LEFTPADDING',(0,0),(-1,-1),5), ('RIGHTPADDING',(0,0),(-1,-1),5)]
            for c, a in enumerate(aligns[:n]): st.append(('ALIGN',(c,0),(c,-1),a))
            for r in range(1, len(data)):
                if r % 2 == 0: st.append(('BACKGROUND',(0,r),(-1,r),SHADE))
            tb = Table(data, colWidths=cw, style=TableStyle(st), repeatRows=1)
            out.append(Spacer(1,3))
            # una tabla corta NUNCA se parte; una larga repite cabecera en cada pagina
            out.append(KeepTogether(tb) if len(data) <= 14 else tb)
            out.append(Spacer(1,8)); continue
        s = ln.strip()
        if not s: out.append(Spacer(1,1.5)); i += 1; continue
        if re.match(r'^(-{3,}|\*{3,}|_{3,})$', s):
            out.append(Spacer(1,4))
            out.append(Table([['']], colWidths=[W], rowHeights=[.5],
                       style=TableStyle([('LINEBELOW',(0,0),(-1,-1),.5,RULE)])))
            out.append(Spacer(1,6)); i += 1; continue
        m = re.match(r'^(#{1,6})\s+(.*)$', s)
        if m:
            lvl = len(m.group(1)); k = 'h1' if lvl == 1 else ('h2' if lvl == 2 else 'h3')
            if k == 'h1': out.append(CondPageBreak(46*mm))
            elif k == 'h2': out.append(CondPageBreak(30*mm))
            else: out.append(CondPageBreak(22*mm))
            out.append(P(m.group(2), ST[k])); i += 1; continue
        if s.startswith('>'):
            buf = []
            while i < len(L) and L[i].strip().startswith('>'):
                buf.append(L[i].strip().lstrip('>').strip()); i += 1
            txt = ' '.join(x for x in buf if x)
            out.append(KeepTogether(Table([[P(txt, ST['quote'])]], colWidths=[W],
                style=TableStyle([('LINEBEFORE',(0,0),(0,-1),1.7,BLACK),
                                  ('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),2),
                                  ('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3)]))))
            continue
        m = re.match(r'^([-*]|\d+\.)\s+(.*)$', s)
        if m:
            b = '\u2022' if not m.group(1)[0].isdigit() else m.group(1)
            out.append(P(m.group(2), ST['li'], bulletText=b)); i += 1; continue
        buf = []
        while i < len(L) and L[i].strip() and not re.match(r'^(#|\||>|```|---|[-*]\s|\d+\.\s)', L[i].strip()):
            buf.append(L[i].strip()); i += 1
        if buf: out.append(P(' '.join(buf), ST['body']))
    return out

def build(src, dst, title, subtitle, author, lang='ES'):
    md = open(src, encoding='utf-8').read()
    md = re.sub(r'^\s*#\s+.*\n', '', md, count=1)
    md = re.sub(r'^\s*##\s+.*\n', '', md, count=1)
    ML, MR, MT, MB = 22*mm, 22*mm, 22*mm, 20*mm
    W = A4[0] - ML - MR
    doc = BaseDocTemplate(dst, pagesize=A4, leftMargin=ML, rightMargin=MR, topMargin=MT,
                          bottomMargin=MB, title=title, author=author, subject=subtitle)
    run = {'ES':'ELPH-N · El Elefante en una Neurona',
           'EN':'ELPH-N · The Elephant in a Neuron'}[lang]
    def deco(cv, d):
        cv.saveState()
        if d.page > 1:
            cv.setFillColor(GREY); cv.setFont(SANS, 6.8)
            cv.drawString(ML, A4[1]-MT+7*mm, run)
            cv.drawRightString(A4[0]-MR, A4[1]-MT+7*mm, author)
            cv.setStrokeColor(RULE); cv.setLineWidth(.4)
            cv.line(ML, A4[1]-MT+5.6*mm, A4[0]-MR, A4[1]-MT+5.6*mm)
            cv.setFillColor(BLACK); cv.setFont(SERIF, 8.6)
            cv.drawCentredString(A4[0]/2, MB-10*mm, str(d.page))
        cv.restoreState()
    doc.addPageTemplates([PageTemplate(id='p', frames=[Frame(ML, MB, W, A4[1]-MT-MB, id='f')],
                                       onPage=deco)])
    F = [Spacer(1, 44*mm),
         Paragraph(html.escape(title), S(name='T', fontName=SERIF_B, fontSize=22, leading=26,
                                         alignment=TA_CENTER, spaceAfter=10)),
         Table([['']], colWidths=[54*mm], rowHeights=[1], hAlign='CENTER',
               style=TableStyle([('LINEBELOW',(0,0),(-1,-1),1.1,BLACK)])),
         Spacer(1, 9),
         Paragraph(fallback(html.escape(normalize(subtitle))),
                   S(name='ST', fontName=SERIF_I, fontSize=12, leading=16.5,
                     alignment=TA_CENTER, spaceAfter=30)),
         Paragraph(html.escape(author), S(name='AU', fontName=SERIF, fontSize=12.5,
                   leading=16, alignment=TA_CENTER, spaceAfter=3)),
         Paragraph({'ES':'Investigador principal','EN':'Principal investigator'}[lang],
                   S(name='AF', fontName=SANS, fontSize=8, leading=11, alignment=TA_CENTER,
                     textColor=GREY, spaceAfter=24))]
    note = {'ES':('AVISO DE ESTADO EVIDENCIAL<br/><br/>'
        'Ninguna cifra de este documento procede de una medida de banco propia. Todo valor es '
        'derivación, simulación o literatura, y lleva declarado su estado (MED · DER · LIT · DEC). '
        'Sobre los ocho ejes de completitud del marco, los siete de planteamiento están al 100 % '
        'y el octavo —MEDIDO— está al <b>0 %</b>. El marco está al <b>87,5 %</b>.<br/><br/>'
        'Este documento es un <b>protocolo preinscrito para que terceros lo refuten</b>, no un '
        'informe de resultados.<br/><br/>'
        '<i>Nota tipográfica:</i> la unidad Emilio se compone aquí como Ш; ningún tipo de letra '
        'del sistema incluye su glifo propio (U+2C4E).'),
        'EN':('EVIDENTIARY STATUS NOTICE<br/><br/>'
        'No figure in this document comes from a bench measurement of our own. Every value is a '
        'derivation, a simulation or a citation, and carries its declared status '
        '(MEAS · DER · LIT · DEC). Across the framework\u2019s eight axes of completeness, the seven '
        'statement axes stand at 100 % and the eighth \u2014 MEASURED \u2014 stands at <b>0 %</b>. '
        'The framework is at <b>87.5 %</b>.<br/><br/>'
        'This document is a <b>pre-registered protocol for third parties to refute</b>, not a '
        'report of results.<br/><br/>'
        '<i>Typographic note:</i> the Emilio unit is set here as Ш; no system typeface carries its '
        'own glyph (U+2C4E).')}[lang]
    F.append(Table([[Paragraph(note, S(name='NB', fontName=SANS, fontSize=7.8, leading=11.2))]],
             colWidths=[W*.84], hAlign='CENTER', style=TableStyle([
                 ('BOX',(0,0),(-1,-1),.8,BLACK),
                 ('LEFTPADDING',(0,0),(-1,-1),12), ('RIGHTPADDING',(0,0),(-1,-1),12),
                 ('TOPPADDING',(0,0),(-1,-1),10), ('BOTTOMPADDING',(0,0),(-1,-1),10)])))
    F.append(PageBreak())
    F += parse(md, W)
    doc.build(F)
    return dst

if __name__ == '__main__':
    a = sys.argv[1:]
    print('escrito:', build(a[0], a[1], a[2], a[3], a[4], a[5] if len(a) > 5 else 'ES'))
