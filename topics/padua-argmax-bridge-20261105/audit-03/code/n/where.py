"""where.py DOC REGEX [FILEFILTER] -- grep a source with unit and printed page."""
import sys, re, pickle, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from notation_scan import Doc, synctex_pages, unit_of, page_lookup
from pathlib import Path
repo = Path('/home/user/padua_research'); T='topics/padua-argmax-bridge-20261105'
here = Path(os.path.dirname(os.path.abspath(__file__)))
doc = sys.argv[1]; pat = re.compile(sys.argv[2]); ff = sys.argv[3] if len(sys.argv) > 3 else ''
cache = here / f'cache-{doc}.pkl'
if cache.exists():
    d = pickle.load(open(cache, 'rb'))
else:
    sub = 'paper' if doc == 'paper' else 'companion-paper'
    pages = synctex_pages(here / f'synctex/{doc}/main.synctex.gz', repo / T / sub)
    d = Doc(doc, repo / T / sub, pages)
    pickle.dump(d, open(cache, 'wb'))
pos = 0
for f, no, t in d.lines:
    if ff in f and pat.search(t):
        # position of this line
        import bisect
        i = [k for k, s in enumerate(d.loc.starts) if s[1] == f and s[2] == no][0]
        p = d.loc.starts[i][0]
        u = unit_of(d.units, p)
        eq = d.eq_numbers(p + len(t) // 2)
        print(f"{f.split('/')[-1].replace('-unified','').replace('.tex','')}:{no} p{page_lookup(d.pages, f, no)} [{u}]{' eq'+','.join(map(str,eq)) if eq else ''}: {t.strip()[:150]}")
