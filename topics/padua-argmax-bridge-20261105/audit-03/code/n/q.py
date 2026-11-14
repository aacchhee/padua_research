import sys, os, pickle, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from notation_scan import Doc
from pathlib import Path
here = Path(os.path.dirname(os.path.abspath(__file__)))
repo = Path('/home/user/padua_research'); T = repo/'topics/padua-argmax-bridge-20261105'
short = {'intro':'introduction','prelim':'preliminaries','corner':'corner-unified','comparison':'comparison-unified','localization':'localization-unified','certification':'certification-unified'}
_docs = {}
def doc(name):
    if name not in _docs:
        c = here/f'qcache-{name}.pkl'
        if c.exists(): _docs[name] = pickle.load(open(c,'rb'))
        else:
            _docs[name] = Doc(name, T/('paper' if name=='paper' else 'companion-paper'))
            pickle.dump(_docs[name], open(c,'wb'))
    return _docs[name]
def eqs(full, ranges, name='paper', key=False):
    d = doc(name); out = set()
    rx = re.compile(full) if isinstance(full, re.Pattern) else None
    for k, fu, pos in d.occ:
        tok = k if key else fu
        if (rx.fullmatch(tok) if rx else tok == full):
            f, line = d.loc(pos)
            for fs, a, b in ranges:
                if f.endswith(short.get(fs, fs)+'.tex') and a <= line <= b:
                    out.update(d.eq_numbers(pos))
    return sorted(out)
if __name__ == '__main__':
    full = sys.argv[1]; rs = []
    a = sys.argv[2:]
    while a:
        rs.append((a[0], int(a[1]), int(a[2]))); a = a[3:]
    print(full, eqs(full, rs))
