"""Audit-06 budget recount with the audit-02/audit-05 generated-class convention (read-only git ls-tree)."""
import subprocess
SRC = ('.py', '.sh', '.c', '.cpp', '.h', '.tex', '.bib', '.diff')
def inv(ref):
    rows = {}
    for line in subprocess.check_output(['git', 'ls-tree', '-rl', ref], text=True).splitlines():
        meta, path = line.split('\t', 1); mode, typ, blob, size = meta.split()
        if typ != 'blob': continue
        base = path.rsplit('/', 1)[-1]
        if base == '.gitignore' or path.endswith(SRC): continue
        if path.endswith('.md') and base != 'COLD_STORAGE.md': continue
        rows[path] = (blob, int(size))
    return rows
def pos(a, b):
    t = 0; items = []
    for p, (blob, s) in b.items():
        o = a.get(p)
        if o is None: t += s; items.append((s, 'new', p))
        elif o[0] != blob and s > o[1]: t += s - o[1]; items.append((s - o[1], 'grow', p))
    return t, items
main, inp, head = 'b5388c25a2a5ccb8d0faf816ab87023cf347bcd3', '33b9eca8167980cad0b0a491da7de64280c9a158', '5b1a4942af498e60e9da4c8860c57cb4f67be4ef'
M, I, H = inv(main), inv(inp), inv(head)
tm, ti, th = (sum(s for _, s in X.values()) for X in (M, I, H))
print('main', tm, 'audit05-input', ti, 'head', th, 'topic share head-main', th - tm, 'input share', ti - tm)
d, items = pos(I, H)
print('positive deltas input->head', d, 'bound 11751309+d =', 11751309 + d, '| head+FREEZE.md 2087 =', th + 2087)
for r in sorted(items, reverse=True): print('  ', r)
outside = [p for p in set(M) | set(H) if not p.startswith('topics/padua-argmax-bridge-20261105/') and p != 'results/padua-argmax-bridge-20261105.md' and M.get(p) != H.get(p)]
print('generated-class paths outside topic differing from main:', outside)
