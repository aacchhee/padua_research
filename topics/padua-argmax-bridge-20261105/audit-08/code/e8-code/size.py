import subprocess, sys
SRC = ('.py', '.sh', '.c', '.cpp', '.h', '.tex', '.bib', '.diff')
def inv(ref):
    out = subprocess.check_output(['git', 'ls-tree', '-rl', ref], text=True)
    rows = {}
    for line in out.splitlines():
        meta, path = line.split('\t', 1)
        mode, typ, blob, size = meta.split()
        if typ != 'blob': continue
        base = path.rsplit('/', 1)[-1]
        if base == '.gitignore' or path.endswith(SRC): continue
        if path.endswith('.md') and base != 'COLD_STORAGE.md': continue
        rows[path] = (blob, int(size))
    return rows
a, b = inv(sys.argv[1]), inv(sys.argv[2])
ta, tb = sum(s for _, s in a.values()), sum(s for _, s in b.values())
pos = 0; items = []
for p, (blob, s) in b.items():
    old = a.get(p)
    if old is None: pos += s; items.append((s, p, 'new'))
    elif old[0] != blob and s > old[1]: pos += s - old[1]; items.append((s - old[1], p, 'grow'))
print('base_total', ta, 'head_total', tb, 'net', tb - ta, 'positive_deltas', pos, 'counted_paths', len(b))
for s, p, k in sorted(items, reverse=True)[:200]: print(s, k, p)
