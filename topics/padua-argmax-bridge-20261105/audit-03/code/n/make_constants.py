import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import loc
from pathlib import Path
T = Path('/home/user/padua_research/topics/padua-argmax-bridge-20261105')
P = {f: (T/'paper/sections'/(loc.short[f]+'.tex')).read_text().split('\n') for f in ['comparison','localization']}
# constant, regex for reuse in localization, definition (file,line,needle), eq, reminder lines (paper localization line numbers that cite the defining block)
C = [
 ('$T$', r'(?<![_\\a-zA-Z{])T(?![_a-zA-Z{(])', ('comparison',536,'T&='), 52),
 ('$D$', r'(?<![_\\a-zA-Z{])D(?![_a-zA-Z{(])', ('comparison',537,'D&='), 52),
 ('$\\mathcal M$', r'\\mathcal ?M(?![_a-zA-Z])', ('comparison',538,'\\mathcal M&='), 52),
 ('$\\bar e$', r'\\bar e', ('comparison',541,'\\bar e&='), 52),
 ('$K_D$', r'K_D', ('comparison',542,'K_D='), 52),
 ('$A_4$, $C_4$', r'[AC]_4', ('comparison',543,'C_4='), 52),
 ('$d_\\beta$', r'd_\\beta', ('comparison',544,'d_\\beta='), 52),
 ('$J_N$', r'J_N', ('comparison',545,'J_N&='), 52),
 ('$k_{Nx},k_{Ny},k_{Wx},k_{Wy}$', r'k_\{[NW]', ('comparison',547,'k_{Nx}&='), 52),
 ('$U_N$', r'U_N', ('comparison',551,'U_N&='), 52),
 ('$b_0$, $r_0$', r'[br]_0', ('comparison',536,'b_0=4'), 52),
 ('$\\epsilon$, $\\ell$ (as $\\varepsilon$, $\\ell$)', r'\\varepsilon|\\ell(?![_a-z])', ('comparison',558,'\\epsilon&=3'), 53),
 ('$W_n$', r'W_n', ('comparison',576,'W_n&='), 53),
 ('$\\overline C_E$', r'overline C_E', ('comparison',585,'\\overline C_E='), 54),
 ('$M(n)$', r'M\(n\)|M\(256\)', ('comparison',601,'M(n)='), 56),
 ('$M_\\infty$', r'M_\\infty', ('comparison',243,'M_\\infty(x,y,L)'), 38),
 ('$j$ (model constant)', r'(?<![_\\a-zA-Z{])j(?![_a-zA-Z\\])(?!\\geq)', ('comparison',309,'j=H_0'), None),
 ('$E_c$', r'E_c', ('comparison',325,'E_c='), 42),
 ('$I_4$', r'I_4', ('comparison',479,'I_4='), 50),
 ('$L$, $H$', r'(?<![_\\a-zA-Z{])[LH](?![_a-zA-Z{(])', ('comparison',4,'L=\\log n'), None),
 ('$u$, $x$, $y$, $a$, $p$, $q$, $P$', r'(?<![_\\a-zA-Z{])[uxy](?![_a-zA-Z{])', ('comparison',10,'u=1-a'), None),
]
ranges = [('4.3',68,243),('4.4',244,350),('4.5',351,465),('4.6',466,537)]
def unit(l):
    for u,a,b in ranges:
        if a <= l <= b: return u
cites = re.compile(r'\\eqref\{uc:(constants|phase-allowance|uniform-allowance|analytic-norm|model-loss|origin-lower|central-pair-bounds|relative-comparison|central-pair-general|Ec)\}|meanings in')
print('| Constant | Defined (paper / companion) | Eq. | Reused in 4.3–4.6 (paper line, page; companion page) | Reminder at the reuse |')
print('|---|---|---|---|---|')
for name, rx, (f, l, needle), eq in C:
    assert needle in P[f][l-1], (name, P[f][l-1])
    rxc = re.compile(rx)
    hits = [k for k in range(68, 538) if rxc.search(P['localization'][k-1])]
    # strip hits in comments-free? (sources have no comments in these ranges)
    cells, rem = [], []
    for k in hits:
        s = loc.P('localization', k)
        pp = s.split('(p.')[1].split(')')[0]; cp = s.split('(p.')[2].split(')')[0]
        cells.append(f'{k} (p.{pp}/{cp})')
        win = ' '.join(P['localization'][max(0,k-6):k+1])
        rem.append(bool(cites.search(win)))
    by = {}
    for k, c, r in zip(hits, cells, rem):
        by.setdefault(unit(k), []).append((c, r))
    reuse = '; '.join(f"{u}: " + ', '.join(c + ('' if r else '*') for c, r in v) for u, v in by.items())
    dl = loc.P(f, l).replace(' / ', '; C ')
    print(f'| {name} | P {dl} | {eq or "–"} | {reuse} | ' + ('none' if not any(rem) else ('partial' if not all(rem) else 'all')) + ' |')
