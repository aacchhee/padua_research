"""loc.py: map paper lines to companion lines (difflib) and print locations with pages.
usage: loc.py P file line [...]   or   loc.py C file line   (file short: intro, prelim, corner, comparison, localization, certification)"""
import sys, os, pickle, difflib, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from notation_scan import synctex_pages, page_lookup
from pathlib import Path
repo = Path('/home/user/padua_research'); T = repo/'topics/padua-argmax-bridge-20261105'
here = Path(os.path.dirname(os.path.abspath(__file__)))
short = {'intro':'introduction','prelim':'preliminaries','corner':'corner-unified','comparison':'comparison-unified','localization':'localization-unified','certification':'certification-unified','main':None}
cache = here/'loc-cache.pkl'
if cache.exists():
    M, PP, CP = pickle.load(open(cache,'rb'))
else:
    PP = synctex_pages(here/'synctex/paper/main.synctex.gz', T/'paper')
    CP = synctex_pages(here/'synctex/companion/main.synctex.gz', T/'companion-paper')
    M = {}
    for s, f in short.items():
        if not f: continue
        a = (T/'paper/sections'/(f+'.tex')).read_text().split('\n')
        b = (T/'companion-paper/sections'/(f+'.tex')).read_text().split('\n')
        sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
        m = {}
        for i, j, n in sm.get_matching_blocks():
            for k in range(n): m[i+k+1] = j+k+1
        M[f] = m
    pickle.dump((M, PP, CP), open(cache,'wb'))
def P(f, line):
    f = short.get(f, f)
    c = M[f].get(line)
    if c is None:
        # nearest previous mapped line
        prev = max([k for k in M[f] if k <= line], default=None)
        c = f'~{M[f][prev] + (line-prev)}' if prev else '?'
    pp = page_lookup(PP, f'sections/{f}.tex', line)
    cp = page_lookup(CP, f'sections/{f}.tex', int(str(c).lstrip('~'))) if c != '?' else ''
    return f'{f.replace("-unified","")}:{line} (p.{pp}) / {c} (p.{cp})'
def C(f, line):
    f = short.get(f, f)
    return f'{f.replace("-unified","")}:{line} (p.{page_lookup(CP, f"sections/{f}.tex", line)})'
if __name__ == '__main__':
    args = sys.argv[1:]
    while args:
        kind, f, l = args[0], args[1], int(args[2]); args = args[3:]
        print(P(f, l) if kind == 'P' else 'C ' + C(f, l))
