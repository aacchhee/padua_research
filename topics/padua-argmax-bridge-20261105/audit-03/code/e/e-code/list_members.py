"""List tar members of the untrusted return WITHOUT extraction; safety summary."""
import collections, json, sys, tarfile
from pathlib import PurePosixPath
path = sys.argv[1]
rows = []; kinds = collections.Counter(); bad = []; total = 0; maxsize = 0
with tarfile.open(path, 'r|gz') as tar:
    for m in tar:
        p = PurePosixPath(m.name)
        kind = ('file' if m.isfile() else 'hardlink' if m.islnk() else 'symlink' if m.issym() else
                'dir' if m.isdir() else 'other')
        kinds[kind] += 1
        if p.is_absolute() or '..' in p.parts or str(p) != m.name: bad.append(('unsafe name', m.name))
        if kind in ('symlink', 'dir', 'other'): bad.append((kind, m.name))
        if kind == 'hardlink':
            lp = PurePosixPath(m.linkname)
            if lp.is_absolute() or '..' in lp.parts: bad.append(('unsafe link', m.name, m.linkname))
        if m.isfile(): total += m.size; maxsize = max(maxsize, m.size)
        rows.append({'name': m.name, 'kind': kind, 'size': m.size, 'link': m.linkname or None, 'mode': oct(m.mode)})
json.dump(rows, open(sys.argv[2], 'w'), indent=0)
print(json.dumps({'members': len(rows), 'kinds': kinds, 'unsafe': bad[:20], 'n_unsafe': len(bad),
                  'regular_bytes': total, 'max_member': maxsize,
                  'top': collections.Counter(r['name'].split('/')[0] for r in rows).most_common(20)}, indent=1))
