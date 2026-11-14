#!/usr/bin/env python3
"""Paper line + needle -> paper page, companion line/page (audit-04 N4). stdlib only."""
import sys, importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location('ns', Path(sys.argv[1])/'notation_scan.py'); ns = importlib.util.module_from_spec(spec); spec.loader.exec_module(ns)
P, C, PS, CS, items = Path(sys.argv[2]).resolve(), Path(sys.argv[3]).resolve(), sys.argv[4], sys.argv[5], sys.argv[6]
pp, cp = ns.synctex_pages(PS, P), ns.synctex_pages(CS, C)
for raw in Path(items).read_text().splitlines():
    if not raw.strip(): continue
    tag, f, needle = raw.split('|', 2)
    rel = 'main.tex' if f == 'main' else (f'sections/{f}.tex' if f in ('introduction','preliminaries') else f'sections/{f}-unified.tex')
    pl = [i for i, l in enumerate((P/rel).read_text().split('\n'), 1) if needle in l]
    cl = [i for i, l in enumerate((C/rel).read_text().split('\n'), 1) if needle in l]
    ps = ','.join(f'{i}(p{ns.page_lookup(pp, rel, i)})' for i in pl[:3]) or 'NOTFOUND'
    cs = ','.join(f'{i}(p{ns.page_lookup(cp, rel, i)})' for i in cl[:3]) or 'NOTFOUND'
    print(f'{tag:6s} {f[:13]:13s} P {ps:30s} C {cs}')
