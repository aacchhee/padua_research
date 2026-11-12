import json, sys
from pathlib import Path
A = Path(sys.argv[1]); B = Path(sys.argv[2])
omit = {'seconds', 'search_seconds', 'raw_path', 'versions'}
def clean(v):
    if isinstance(v, dict): return {k: clean(x) for k, x in v.items() if k not in omit}
    if isinstance(v, list): return [clean(x) for x in v]
    return v
for name in sys.argv[3:]:
    a = json.loads((A / name).read_text()); b = json.loads((B / name).read_text())
    eq = clean(a) == clean(b)
    diff = [k for k in set(a) | set(b) if clean(a.get(k)) != clean(b.get(k))]
    print(name, 'scientific+hash fields equal' if eq else f'DIFF {diff}')
