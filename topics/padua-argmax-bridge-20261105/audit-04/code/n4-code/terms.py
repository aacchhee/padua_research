#!/usr/bin/env python3
"""Terms-of-art first-use locator (audit-04 N4); stdlib only.
Usage: terms.py SCANNERDIR PAPERDIR COMPDIR PSYNCTEX CSYNCTEX"""
import re, sys, importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location('ns', Path(sys.argv[1])/'notation_scan.py'); ns = importlib.util.module_from_spec(spec); spec.loader.exec_module(ns)
TERMS = ['unisolvent','cardinal','Gram matrix','checkerboard','Cauchy sum','collision','chart','center','eligible','defect','floor',
 'certificate','witness','leaf','tree','board','phase triangle','phase radius','signed sum','envelope','majorant','allowance','gate','guard',
 'seam','tie','proxy','near part','far part','wide domain','cusp','atom','finite part','counterterm','entropy','telescope','matched',
 'linked','cyclic vector','residue','reflection loss','pair defect','projection','layer cake','layer-cake','Peano','Bernstein basis',
 'de Casteljau','Horner','binary64','unit roundoff','outward','GRID','TREE','physical','periodic mesh','effective angle',
 'inward','descent','punctured','analytic far leaf','numerical','retained','pole norm','pole numerator','half-line','row profile',
 'completed model','reciprocal pair','diamond','exponential type','bandwidth','unimodal','bounded variation','real-phase',
 'reproducing kernel','sine chord','norm witness','phase cover','frequenc','Lebesgue function','nonnode']
DEFM = re.compile(r'\\emph\{|\\textit\{|is called|we call|means|here means|refers to|is defined|denote|is the|are the|:=|we write|stands for|Put|Let|Define|define', re.I)
def first(name, root, stx):
    root = Path(root).resolve(); pages = ns.synctex_pages(stx, root)
    lines = ns.load_document(root); text, starts = ns.flatten(lines); loc = ns.Locator(starts)
    out = {}
    low = text.lower()
    for t in TERMS:
        i = low.find(t.lower())
        if i < 0: out[t] = None; continue
        f, l = loc(i); s0 = max(text.rfind('. ', 0, i), text.rfind('\n\n', 0, i)); s1 = text.find('. ', i)
        sent = text[s0+1:s1 if s1 > 0 else i+200]
        emph = bool(re.search(r'\\emph\{[^}]*' + re.escape(t[:6]), text[max(0,i-8):i+len(t)+2], re.I))
        out[t] = (f.split('/')[-1].replace('-unified.tex','').replace('.tex',''), l, ns.page_lookup(pages, f, l), 'emph' if emph else ('defmark' if DEFM.search(sent) else '-'), re.sub(r'\s+',' ',sent)[:90])
    return out
P = first('paper', sys.argv[2], sys.argv[4]); C = first('comp', sys.argv[3], sys.argv[5])
for t in TERMS:
    p, c = P[t], C[t]
    fp = f'{p[0]}:{p[1]} p{p[2]} {p[3]}' if p else 'absent'
    fc = f'{c[0]}:{c[1]} p{c[2]} {c[3]}' if c else 'absent'
    print(f'{t:20s} | P {fp:36s} | C {fc:36s} | {(c or p or ("","","","",""))[4][:80]}')
