"""M6: apply the cumulative 33-entry rename map to 24a98db sources; report
per-entry occurrence counts (base, after-map, residual in new) and residual
old tokens in the 8937d3b sources. Read-only on trees extracted by git archive."""
import json, sys, re, os
R = sys.argv[1]  # trees root
T = 'topics/padua-argmax-bridge-20261105'
mp = json.load(open(sys.argv[2]))
for prod in ('paper', 'companion-paper'):
    print('=====', prod)
    texts = {}
    for e in mp:
        for f in e['files']:
            texts.setdefault(f, open(f'{R}/base24/{T}/{prod}/sections/{f}').read())
    base = dict(texts)
    for i, e in enumerate(mp):
        for f in e['files']:
            c = texts[f].count(e['from'])
            texts[f] = texts[f].replace(e['from'], e['to'])
            new = open(f'{R}/new/{T}/{prod}/sections/{f}').read()
            print(f"{i:2d} {f[:14]:14s} {e['from']!r:42s} -> {e['to']!r:36s} base24={base[f].count(e['from']):3d} applied={c:3d} new_has_to={new.count(e['to']):3d} new_has_from={new.count(e['from']):3d}")
    # contexts for kernel P_n in comparison
    b = base['comparison-unified.tex']
    for m in re.finditer(r'P_n', b):
        ctx = b[m.start()-20:m.start()+25].replace('\n', ' ')
        if 'cos' in ctx:
            print('  kernel P_n context in base24 comparison:', ctx)
