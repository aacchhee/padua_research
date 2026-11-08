#!/usr/bin/env python3
"""Numbered blocks/statements touched by proposed renames (audit-04 N4). stdlib only.
Usage: blocks.py SCANNER PAPERDIR AUX"""
import re, sys, importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location('ns', Path(sys.argv[1])/'notation_scan.py'); ns = importlib.util.module_from_spec(spec); spec.loader.exec_module(ns)
d = ns.Doc('paper', Path(sys.argv[2]).resolve())
aux = Path(sys.argv[3]).read_text()
num = dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]*)\}', aux))
spans = []
for kind, pat in (('S', ns.CLAIMS), ('D', ns.DISPLAYS)):
    for m in re.finditer(r'\\begin\{(' + pat + r')\}.*?\\end\{\1\}', d.text, re.S):
        labs = re.findall(r'\\label\{([^}]+)\}', m.group())
        spans.append((m.start(), m.end(), kind, [f'{l}({num.get(l,"?")})' for l in labs] or [m.group(1)]))
R = [  # name, token regex (full token), file, line range
 ('P_n gate -> \\mathfrak p_n', r'P_\{n\}|P_\{512\}', 'comparison', 1506, 1641),
 ('P_n gate (Sec.4 preamble/Thm 4.12)', r'P_\{n\}', 'localization', 92, 117),
 ('P_n gate (proof of Thm)', r'P_\{n\}', 'localization', 404, 430),
 ('Theta (gate) -> \\vartheta_n', r'\\Theta', 'comparison', 1506, 1641),
 ('G(n,rho1) -> \\mathcal G', r'G', 'comparison', 1506, 1641),
 ('G (Cor 5.4 proof)', r'G', 'certification', 282, 296),
 ('U (Cor 4.7) -> U_*', r'U', 'comparison', 1572, 1641),
 ('j_* -> \\mathfrak j_*', r'j_\{\*\}', 'comparison', 1506, 1641),
 ('t_* -> \\mathfrak t_*', r't_\{\*\}', 'comparison', 1506, 1641),
 ('A_* const (4.4 tail) -> A_\\sharp', r'A_\{\*\}', 'localization', 280, 310),
 ('C=A(0) synonym (4.4)', r'C', 'localization', 260, 305),
 ('delta=x-y (4.1 envelope) -> \\delta_\\pm?', r'\\delta', 'comparison', 296, 335),
 ('J=48 -> J_{\\log}', r'J', 'comparison', 494, 527),
 ('A_N(q) -> \\mathcal A_N', r'A_\{N\}|A_\{40\}|A_\{39\}', 'comparison', 494, 527),
 ('Z_s -> \\zeta_{10}(s)', r'Z_\{s\}', 'comparison', 494, 527),
 ('xi,zeta phase shifts (4.4)', r'\\zeta|\\xi', 'localization', 185, 220),
 ('e_j,f_k -> eps_j,eta_k (Sec.4 pre)', r'e_\{j\}|f_\{k\}', 'localization', 1, 118),
 ('rho before def (table)', r'\\rho', 'localization', 70, 117),
]
for name, rx, f, a, b in R:
    r = re.compile(rx); hits = set(); lines = set()
    for key, full, pos in d.occ:
        if not r.fullmatch(full): continue
        ff, line = d.loc(pos)
        if not ff.endswith(f + ('-unified' if f not in ('introduction','preliminaries') else '') + '.tex') or not (a <= line <= b): continue
        lines.add(line)
        for s, e, k, labs in spans:
            if s <= pos < e: hits.add(k + ':' + ','.join(labs))
    print(f'{name:40s} lines={len(lines):3d}  blocks: {"; ".join(sorted(hits)) or "none"}')
