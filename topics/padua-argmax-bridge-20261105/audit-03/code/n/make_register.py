"""Generate the symbol register table; every cited line is checked by a needle."""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import loc, q
from pathlib import Path
T = Path('/home/user/padua_research/topics/padua-argmax-bridge-20261105')
FILES = {}
def text(doc, f):
    key = (doc, f)
    if key not in FILES:
        sub = 'paper' if doc == 'P' else 'companion-paper'
        FILES[key] = (T / sub / 'sections' / (loc.short[f] + '.tex')).read_text().split('\n')
    return FILES[key]
ERR = []
def site(doc, f, line, needle):
    t = text(doc, f)
    if needle not in t[line - 1]:
        ERR.append(f'{doc} {f}:{line} lacks {needle!r}: {t[line-1][:80]}')
    if doc == 'P':
        s = loc.P(f, line)
        # also check the companion counterpart line has the needle
        c = s.split(' / ')[1].split(' ')[0].lstrip('~')
        ct = text('C', f)
        if c != '?' and needle not in ct[int(c) - 1]:
            c0 = int(c)
            hits = [k for k in range(max(1, c0 - 80), min(len(ct), c0 + 80) + 1) if needle in ct[k - 1]]
            if not hits:
                ERR.append(f'C counterpart {f}:{c} lacks {needle!r}')
            else:
                k = min(hits, key=lambda k: abs(k - c0))
                s = s.split(' / ')[0] + ' / ' + loc.C(f, k).split(':', 1)[1]
        a, b = s.split(' / ')
        return 'P ' + a + '; C ' + b.lstrip('~')
    return 'C only ' + loc.C(f, line)
def E(tok, *ranges):
    rs = [(ranges[i], ranges[i+1], ranges[i+2]) for i in range(0, len(ranges), 3)]
    rx = re.compile(tok) if ('\\{' in tok or '.*' in tok) else None
    return sorted(set(q.eqs(rx if rx else tok, rs)))
def EL(*parts):
    """EL(('label', tok, ranges...), ...) -> 'label: 1, 2; label2: 3'."""
    out = []
    for part in parts:
        label, tok, rs = part[0], part[1], part[2:]
        e = E(tok, *rs)
        if e:
            out.append(f'{label}: ' + ', '.join(map(str, e)))
    return '; '.join(out)

R = []   # rows: (symbol, rank, meaning, sites, live, eqs, status)
def S(symbol, rank, rows):
    for k, (meaning, sites, live, eqs, status) in enumerate(rows):
        R.append((symbol if k == 0 else '', rank if k == 0 else '', meaning,
                  '<br>'.join(site(*s) for s in sites), live,
                  ', '.join(map(str, sorted(set(eqs)))) if isinstance(eqs, list) else eqs, status))
CO, LO, CE, CN, IN, PR = 'comparison', 'localization', 'certification', 'corner', 'intro', 'prelim'
ALL = (IN,1,200, PR,1,100, CN,1,460, CO,1,1400, LO,1,560, CE,1,270)

# ------------------------------------------------------------------ data
S('$\\varepsilon,\\epsilon$', 1, [
 ('endpoint weights $\\epsilon_j$ (Sec. 2) $=\\varepsilon_j$ (Sec. 3): same object, two glyphs',
  [('P',PR,17,'\\epsilon_j'),('P',CN,11,'\\varepsilon_j')], '§2–§3', E('\\varepsilon_{j}',CN,1,460)+E('\\epsilon_{j}',PR,1,100), 'glyph'),
 ('cutoff in the finite parts $H(w)$, $C_\\infty$', [('P',CO,106,'\\epsilon')], '4.1', E('\\epsilon',CO,100,260), 'A (4.1)'),
 ('coefficient displacement bound', [('P',CO,266,'\\varepsilon'),('P',CO,828,'\\varepsilon')], '4.1 (proof of (39)); 4.2', E('\\varepsilon',CO,260,290,CO,815,850), 'A (4.1, 4.2)'),
 ('$\\epsilon=\\min(t,\\pi-t)$ (separation)', [('P',CO,378,'\\epsilon=\\min')], '4.1 (proof of L. 4.3)', [], 'A (4.1)'),
 ('$\\epsilon=3\\pi/(2m)$ cutoff of $\\ell$; written $\\varepsilon$ in 4.5', [('P',CO,558,'\\epsilon&=3\\pi'),('P',LO,373,'\\varepsilon=3\\pi')], '4.2, 4.5', E('\\epsilon',CO,555,580), 'A (4.2), D, glyph'),
 ('$\\epsilon_n=\\log(m/n)$; $\\epsilon=h/2$ with a second $\\ell=-\\log\\sin\\epsilon$', [('P',CO,656,'\\epsilon_n'),('P',CO,1330,'\\epsilon=h/2')], '4.2', [], 'A (4.2: two $\\ell$)'),
 ('sign vectors $\\varepsilon_\\ell$, $\\varepsilon_{rs}$, $f_\\varepsilon$', [('P',CE,9,'\\varepsilon_\\ell'),('P',CE,116,'f_\\varepsilon')], '§5', [], 'B'),
])
S('$T$', 2, [
 ('Chebyshev polynomial $T_r$', [('P',PR,14,'T_r(\\cos t)')], 'global (§2, §5)', E('T_{.*}',PR,1,100,CE,1,270), 'D'),
 ('angle $T=(v-u)/2$ (with $S$); $T_t=2a\\cot(t/2)$', [('P',CN,28,'T=(v-u)/2'),('P',CO,289,'T_t=2a')], '3.1; 4.1', [], 'B'),
 ('row sum $T_{n,r}$', [('P',CN,64,'T_{n,r}')], '3.1', E('T_{n,r}',CN,1,460), 'D'),
 ('quadratic-log model loss $T=(4L^2-3L)/\\pi^2$', [('P',CO,536,'T&=(4L^2')], '4.2–4.6', E('T',CO,530,1400,LO,1,560), 'A (4.2), D'),
 ('half-line defect $T_0$, $T_{0,r}$', [('P',CO,730,'defect $T_0$'),('P',CO,738,'T_{0,r}')], '4.2', E('T_{0}',CO,1,1400)+E('T_{0,r}',CO,1,1400), 'A (4.2), D'),
 ('outer increment $T_{\\rm out}$', [('P',CO,1274,'T_{\\rm out}')], '4.2', E('T_{out}',CO,1,1400), 'A (4.2), D'),
 ('$\\mathcal T_c=4-2c+4\\log c$; triangle $\\mathcal T$', [('P',LO,200,'\\mathcal T_c=4'),('P',CE,112,'\\mathcal T=')], '4.3; §5', E('\\mathcal{T}_{c}',LO,1,560), 'B, D'),
 ('companion: $T(t)=\\sin(\\pi t)/(\\pi t)$; $T_R$; $T=2\\tan(e/2)$; trig. polynomial $T$', [('C',CO,453,'T(t)='),('C',CO,2109,'T_R='),('C',CO,2975,'T=2\\tan'),('C',CE,743,'$T$')], '4.1; 4.2; 4.2; 5.2', '–', 'C (A in 4.2)'),
])
S('$H,\\mathcal H$', 3, [
 ('harmonic numbers $H_k$, $H_{m-1}$, $H_n$; shifted $H_j(q)=\\psi(j+q)-\\psi(q)$', [('P',CN,140,'H_k='),('P',CO,5,'H_n='),('P',CO,766,'H_j(q)=')], '3.2–3.3; 4.1–4.2', E('H_{.*}',CN,1,460), 'B'),
 ('$\\mathcal H_m$ harmonic row aggregate', [('P',CN,76,'\\mathcal H_m')], '3.1–3.3', E('\\mathcal{H}_{m}',CN,1,460), 'D'),
 ('$H=1+L=1+\\log n$', [('P',CO,4,'H=1+L')], '4.1–4.6', E('H',CO,530,1400,LO,1,560), 'A (4.1), D'),
 ('finite part $H(w)$, $H_0=H(0)$', [('P',CO,106,'H(w)='),('P',CO,110,'H_0:=H(0)')], '4.1, 4.4', E('H',CO,90,230)+E('H_{0}',CO,1,1400), 'A (4.1), D'),
 ('$\\mathcal H(L,v)=A(v)L+\\mathcal B(v)$', [('P',CO,238,'\\mathcal H(L,v)')], '4.1–4.2', [], 'A (4.2 with $\\mathcal H_j$)'),
 ('$\\mathcal H_j=h_j(t)+h_j(1-t)$, $\\mathcal H_2,\\mathcal H_n$', [('P',CO,654,'\\mathcal H_j=')], '4.2', [], 'A (4.2)'),
 ('periodic primitive values $H_{rs}$', [('P',LO,37,'H_{rs}')], '§4 pre., 4.3, 5.2', E('H_{rs}',LO,1,560), 'D'),
 ('$H_h=(1+\\cos v)/(2K)$', [('P',CO,944,'H_h=')], '4.2', [], 'A (4.2)'),
 ('companion: $H_n^*$; $H(g)=A_g(1-d/g)$ with $d=\\pi/L$', [('C',CO,1902,'H_n^*'),('C',LO,676,'H(g)=')], '4.2; 4.3', '–', 'C'),
])
S('$C,\\mathcal C$', 4, [
 ('generic finite constant (Thm 1.2, L. 3.1, (20)); $C=-1+C_H+C_B$ then $C=\\kappa$', [('P',IN,131,'constant $C$'),('P',CN,439,'C=-1+C_H')], '§1, §3', E('C',IN,1,200,CN,1,460), 'B'),
 ('named constants $C_H,C_B,C_K,C_M$', [('P',CN,275,'C_H,C_B'),('P',CN,372,'C_K')], '3.3', E('C_{H}',CN,1,460)+E('C_{B}',CN,1,460), 'D'),
 ('real coefficients $C,D$ in $I(C,D,e)$, $g(C,D;t)$', [('P',CO,16,'real $C,D$')], '4.1–4.2', E('C',CO,1,30), 'A (4.1), D'),
 ('row coefficient $C(v)$', [('P',CO,231,'C(v)&=')], '4.1–4.2', E('C',CO,225,240), 'A (4.1), D'),
 ('$\\mathcal C(t)$ reciprocal pair, $C_0=\\mathcal C(1/2)$', [('P',CO,80,'\\mathcal C(t)')], '4.1–4.2', E('\\mathcal{C}',CO,1,1400), 'D'),
 ('model constants $C_\\infty,C_*$; $C_2$; $C_4$; $C_{E,\\phi},\\overline C_E,C_{6,\\phi},C_B^\\phi$', [('P',CO,249,'C_\\infty='),('P',CO,543,'C_4=')], '4.1–4.6', EL(('$C_\\infty,C_*$',r'C_\{(\\infty|\*)\}',CO,1,1400,LO,1,560),('$C_4$','C_{4}',CO,1,1400,LO,1,560),('$C_{E,\\phi},C_{6,\\phi},C_B^\\phi,\\overline C_E$',r'(\\overline\{C\}_\{E\}|C_\{(E,\\phi|6,\\phi)\}|C_\{B\}\^\{\\phi\})',CO,1,1400,LO,1,560)), 'D'),
 ('$\\mathcal C_s=I_s(\\phi,z)-aI_s(0,z)-\\dots$', [('P',CO,1271,'\\mathcal C_s=')], '4.2', [], 'A (4.2 with $\\mathcal C(t)$)'),
 ('local $C$: $C=a_r-r/2$; $C=1+8a_0m/(3\\pi)$ (with $C_b,C_s,C_l,C_{B,b}$); $C=\\Lambda_c(n)$', [('P',LO,211,'$C=a_r-r/2$'),('P',LO,374,'C=1+8a_0m'),('P',CE,64,'Write $C=\\Lambda_c(n)$')], '4.3; 4.5; 5.1', [], 'B'),
])
S('$D$', 5, [
 ('Dirichlet-type diamond kernel $D_n(u,v)$', [('P',CN,26,'D_n(u,v)')], '3.1', [], 'B'),
 ('digamma row $D_{m,r}$', [('P',CN,75,'D_{m,r}')], '3.1–3.3', E('D_{m,r}',CN,1,460), 'D'),
 ('coefficient $D$ in $I(C,D,e)$; row coefficient $D(v)$; $D_0$', [('P',CO,16,'real $C,D$'),('P',CO,231,'D(v)=('),('P',CO,240,'D_0=')], '4.1–4.2', E('D',CO,1,30)+E('D',CO,225,240), 'A (4.1), D'),
 ('$D=\\mathcal C(\\cdot)+\\mathcal C(\\cdot)-2C_0$ (proof of L. 4.3); $D_h=\\mu^2w^2-z^2$, $D\'$', [('P',CO,361,'If $D='),('P',CO,942,'D_h=')], '4.1; 4.2', [], 'A (4.1, 4.2)'),
 ('allowance $D$; $D_a$, $D_\\phi$, $\\overline D_\\phi$ ($D_a$ restated as $D-10/n^2$ in 4.5)', [('P',CO,537,'D&='),('P',CO,556,'D_a&='),('P',LO,374,'D_a=D-10')], '4.2–4.6', E('D',CO,530,1400,LO,1,560)+E('D_{a}',CO,1,1400), 'A (4.2), D'),
 ('$D_b=\\sin\\gamma\\sin b$ vs $D_b=4w_0/\\pi+a_0b_0\\log\\pi$', [('P',LO,192,'D_b=\\sin'),('P',LO,384,'D_b&=')], '4.3 vs 4.5', [], 'B (same token)'),
 ('$D_R$ largest coefficient sum', [('P',CE,65,'D_R')], '5.1', [], 'B'),
 ('companion: $D=\\operatorname{diag}(\\dots)$; $D_*=(v^2-s^2\\sin^2e)_+^{1/2}$', [('C',PR,365,'D='),('C',CO,219,'D_*=')], '§2; 4.1', '–', 'C'),
])
S('$k$, $K$', 6, [
 ('node index $k$ and generic summation index', [('P',PR,15,'\\phi_k'),('P',CN,70,'k=0')], 'global', E('k',IN,1,200,PR,1,100,CN,1,460,CO,1,1400), 'D'),
 ('$k=2\\gamma-2\\log\\pi$; $k_0=C_0-2\\log\\pi$', [('P',CO,122,'k=2\\gamma'),('P',CO,128,'k_0=C_0')], '4.1', E('k_{0}',CO,1,1400), 'A (4.1: index $k$ in (32))'),
 ('allowance slopes $k_{Nx},k_{Ny},k_{Wx},k_{Wy}$', [('P',CO,547,'k_{Nx}')], '4.2–4.6', E('k_{.*[xy]}',CO,1,1400,LO,1,560), 'D'),
 ('mesh ratio $k=n/m$ ($=\\mu$ of 4.2)', [('P',LO,473,'k=n/m'),('P',CE,113,'k=n/(n+1)')], '4.6, §5', E('k',LO,465,560,CE,1,270), 'B, D, synonym of $\\mu$'),
 ('local: $k_s$; $k_\\pm\\in\\{0,1\\}$; $k=r\\pm j$; argument of $K(k)$', [('P',CO,898,'k_s='),('P',CO,798,'k_\\pm'),('P',CO,1190,'k=r\\pm j'),('P',CO,507,'K(k)')], '4.1–4.2', [], 'A (4.2)'),
 ('kernel $K_n(z,B)$', [('P',PR,25,'K_n(z,B)')], '§2', [], 'B'),
 ('chart index $K$ (with $J$), $\\Delta_{JK}$, $Q_v(K)$', [('P',LO,28,'K\\pi+\\beta')], '§4, 5.2', E('K',LO,1,70), 'D'),
 ('truncation $K$ in (48); $K(k)$; $K_D$; $K=\\operatorname{sinc}\\cdot\\operatorname{sinc}$; $K=L+25\\log(2m)+193/3$; $K_t(w)$', [('P',CO,428,'\\sum_{k=0}^K'),('P',CO,542,'K_D='),('P',CO,943,'K=\\operatorname'),('P',CO,1089,'for $K='),('P',CO,1163,'K_t(w)')], '4.1–4.2', E('K',CO,1,1400)+E('K_{D}',CO,1,1400), 'A (4.2), D'),
 ('outer-gate slope $K$', [('P',LO,407,'K=T+j_*')], '4.5', E('K',LO,400,430), 'B (chart $K$), D'),
 ('companion: curvature bound $K$; $K_M$; trapezoid kernel $K$', [('C',CE,42,'K$ on an'),('C',CN,780,'K_M'),('C',CN,896,'K(t)=')], '§5 pre.; 3.2; 3.3', '–', 'C'),
])
S('$j$, $J$', 7, [
 ('node/summation index $j$ (also $j$ in (74))', [('P',PR,15,'\\theta_j'),('P',LO,249,'j\\geq0')], 'global', E('j',IN,1,200,PR,1,100,CN,1,460,LO,245,252), 'D'),
 ('model constant $j=H_0+d_0-g_0$; $j_*=23/250$', [('P',CO,309,'j=H_0'),('P',LO,401,'j_*=')], '4.1–4.6', E('j',CO,300,560)+E('j',LO,253,560)+E('j_{*}',LO,1,560), 'A (4.2, 4.4), D'),
 ('reference label $j$ in $\\ell_r$, $h_j,g_j,B_j,\\Xi_j,e_j$', [('P',CO,637,'h_j(t)'),('P',CO,1113,'j=2,\\ldots')], '4.2', E('j',CO,630,1400), 'A (4.2), D'),
 ('$J(x)=\\log(1-x)-\\psi((1-x)/2)$', [('P',CN,357,'J(x)=')], '3.3', [], 'B'),
 ('cancellation $J(v,s,e)$; $J_0$', [('P',CO,20,'J(v,s,e)'),('P',CO,101,'J_0=')], '4.1–4.2', E('J',CO,1,560)+E('J_{0}',CO,1,560), 'A (4.1–4.2), D'),
 ('chart index $J$, $\\Delta_{JK}$, $Q_h(J)$', [('P',LO,28,'(J\\pi+\\alpha)/n')], '§4, 5.2', E('J',LO,1,70), 'D'),
 ('allowances $J_N,J_W$; retained rows $J_6,J_{\\rm end},J_{\\rm cen}$', [('P',CO,545,'J_N&='),('P',CO,634,'J_6=')], '4.2–4.4', E('J_{.*}',CO,530,1400), 'D'),
])
S('$a$, $\\mathfrak a$', 8, [
 ('$a=2/\\pi$ (Thm 1.2)', [('P',IN,112,'a=\\frac2\\pi')], '§1, §3', E('a',IN,1,200,CN,1,460), 'B, D'),
 ('$a=c_ec_d=(\\cos x+\\cos y)/2$', [('P',CO,10,'a=c_ec_d')], '4.1–4.6 (also in $A(u,v)$, 4.3)', E('a',CO,1,1400,LO,1,560), 'A (4.3 with $a_r,a_0$), D'),
 ('$a_j=j\\pi/n$ (with $b_k$)', [('P',LO,14,'a_j=j\\pi/n')], '§4 pre.', E('a_{j}',LO,1,70), 'D'),
 ('radius profile $a_r=1-r^2/4$, $a_\\rho$', [('P',LO,77,'a_r=1-r^2/4')], '4.3–4.4', E('a_{r}',LO,1,560), 'A (4.3)'),
 ('band endpoint $a_0$ ($\\pi/20$, $\\pi/100$)', [('P',LO,193,'[a_0,b_0]'),('P',LO,230,'a_0=\\pi/100')], '4.3', E('a_{0}',LO,180,243), 'A (4.3), D'),
 ('$a_0=337/384$', [('P',LO,354,'a_0=337/384')], '4.5', E('a_{0}',LO,350,430), 'B (same token)'),
 ('phase coordinate $a$, rectangle $[a_0,a_1]$', [('P',CE,19,'[a_0,a_1]'),('P',CE,113,'\\pi a')], '§5', E('a',CE,1,270)+E('a_{0}',CE,1,270), 'B, D'),
 ('$\\mathfrak a_p$ series coefficients', [('P',CO,413,'\\mathfrak a_0')], '4.1', E('\\mathfrak{a}_{p}',CO,1,1400), 'D'),
 ('companion: $a,b$ real parts; Fourier coefficients $a_p$', [('C',PR,223,'$a,b$'),('C',CE,745,'a_p')], '§2; 5.2', '–', 'C'),
])
S('$A$', 9, [
 ('node $A\\in\\mathcal P_n$', [('P',PR,3,'L_B(A)')], '§2', [], 'B'),
 ('$A(z)=a(\\log z+d)$', [('P',CN,15,'A(z)=a')], '§3', E('A',CN,1,460), 'B, D'),
 ('$A(v)=2(|C|+|D|)/\\pi$', [('P',CO,234,'A(v)&=')], '4.1', E('A',CO,225,240), 'D'),
 ('$A=398/(11\\pi^2)$ (with $B=48/\\pi$)', [('P',CO,1004,'A=398')], '4.2', [], 'A (4.2: $A_4,A_6$)'),
 ('$A_4$ allowance; $A_6$ row set', [('P',CO,543,'A_4&='),('P',CO,633,'A_6=')], '4.2–4.4', E('A_{4}',CO,1,1400,LO,1,560), 'D'),
 ('pair numerators $A(u,v)$, $A_*$, $A_g$, $A(b)$, $A_0$, $A_r$; $A_h,A_w$', [('P',LO,127,'A(u,v)='),('P',LO,192,'A(b)='),('P',LO,99,'A_r&='),('P',LO,281,'A_h&=')], '4.3–4.4', [], 'A (4.3)'),
 ('outer-gate coefficient $A$; $A_u=1-u$', [('P',LO,407,'A=\\eta t_*'),('P',LO,434,'A_u=1-u')], '4.5', E('A',LO,400,430), 'D'),
 ('inward corner phases $A,B$', [('P',LO,471,'s=A^2/2'),('P',CE,214,'\\cos(A/n)')], '4.6, 5.2', E('A',LO,465,560), 'B, D'),
 ('companion: integer indices $A=p+q$, $B=q-p$; $A=c_e/(2c)$; $A_N$', [('C',CN,105,'$A=p+q$'),('C',CO,3526,'A='),('C',CE,510,'A_N')], '3.1; 4.2; 5.1', '–', 'C'),
])
S('$B,\\mathcal B$', 10, [
 ('node $B$, coordinates $B_1,B_2$', [('P',PR,31,'B=(\\cos')], '§1–§2', E('B_{.*}',PR,1,100), 'D'),
 ('$B(x)$ two-pole-removed cotangent; $I_B,C_B,\\beta_B,F_B,G_B$', [('P',CN,58,'B(x)=')], '§3', E('B',CN,1,460)+E('C_{B}',CN,1,460), 'D'),
 ('$\\mathcal B(v)$; $B_0=4a/\\pi^2$; $B=C_0^2/\\pi^2$; $B_\\beta$', [('P',CO,235,'\\mathcal B(v)'),('P',CO,239,'B_0=4a'),('P',CO,306,'B=C_0^2'),('P',CO,473,'B_\\beta=')], '4.1–4.2', EL(('$\\mathcal B$','\\mathcal{B}',CO,1,1400),('$B_0$','B_{0}',CO,1,1400),('$B$','B',CO,300,470),('$B_\\beta$','B_{\\beta}',CO,1,1400)), 'A (4.1), D'),
 ('pole norm $B_n(t)$', [('P',CO,685,'B_n(t)=')], '4.2', E('B_{n}',CO,1,1400), 'D (same token as below)'),
 ('floor $B_n(r)$', [('P',LO,81,'B_n(r)=')], '4.3', E('B_{n}',LO,1,560), 'B, D'),
 ('$B_j(s)$; $B=48/\\pi$; $B_{\\rm out}$; $B_h,B_w$', [('P',CO,746,'B_j(s)='),('P',CO,1004,'B=48'),('P',CO,1084,'B_{\\rm out}='),('P',LO,282,'B_h&=')], '4.2, 4.4', [], 'A (4.2)'),
 ('Bernstein basis $B_i^n$; inward phase $B$', [('P',CE,31,'B_i^n(s)'),('P',LO,471,'t=B^2/2')], '§5; 4.6', E('B_{i}^{n}',CE,1,270), 'B, D'),
 ('companion: $B=c_d/(2c)$; $B_t$; $B_{\\rm ord}$', [('C',CO,3526,'B='),('C',CO,3254,'B_t(s)='),('C',CO,1770,'B_{\\rm ord}')], '4.2', '–', 'C'),
])
S('$g$', 11, [
 ('function in $Q_M(g)$; quadrature function in L. 3.1', [('P',PR,41,'Q_M(g)'),('P',CN,212,'Suppose $g$')], '§2; 3.3', [], 'B'),
 ('second derivative $g=f\'\'$ of the scalar profile', [('P',CO,94,'second derivative $g$')], '4.1 (L. 4.2)', E('g',CO,90,230), 'A (4.1), D'),
 ('cancellation integrand $g(C,D;t)$', [('P',CO,22,'g(C,D;t)'),('P',CO,817,'g(C,D;t)')], '4.1–4.2', E('g',CO,1,30)+E('g',CO,735,850), 'A (4.1–4.2), D'),
 ('$g_0$; $g_j(t)$; $g_n$; $g_L,g_R$', [('P',CO,308,'g_0='),('P',CO,639,'g_j(t)'),('P',CO,582,'g_n='),('P',CO,1270,'\\pi g_L')], '4.1–4.2', E('g_{.*}',CO,1,1400), 'A (4.2), D'),
 ('$g_{\\sigma\\eta}$ reflected values', [('P',LO,44,'g_{\\sigma\\eta}=')], '§4 pre.', E('g_{\\sigma\\eta}',LO,1,70), 'D'),
 ('constant $g$ of the radial quadratic', [('P',LO,304,'g=\\frac')], '4.4', E('g',LO,295,330), 'B, D'),
 ('angle $g$ in $A_g$; descent margin $g=q-M\\pi^4\\max/6$', [('P',LO,177,'A_g='),('P',CE,216,'g=q-')], '4.3; 5.2', [], 'B'),
])
S('$f$, $F$', 12, [
 ('interpolated function $f$', [('P',IN,8,'\\|f-I_nf')], '§1–§2', E('f',IN,1,200), 'D'),
 ('corner summand $f(u,v)$', [('P',CN,19,'f(u,v)=')], '§3', E('f',CN,1,460), 'D'),
 ('scalar profile $f(w)=\\Phi(1/2+w/(2\\pi))$', [('P',CO,86,'f(w)=')], '4.1–4.2', E('f',CO,1,560), 'A (4.2), D'),
 ('weights $f_k$ (with $e_j$)', [('P',LO,14,'f_k')], '§4 pre., 4.3', E('f_{k}',LO,1,560), 'D'),
 ('$f=g(-w+c,w+d)-g(-w,w)$', [('P',CO,828,'For $f=g')], '4.2', E('f',CO,826,835), 'A (4.2), D'),
 ('sinc row $f_j$ (with $F_j$)', [('P',CO,926,'f_j=')], '4.2', E('f_{j}',CO,1,1400), 'A (4.2), D'),
 ('$f_b(z)$; decreasing $f$; quadratic coefficient $f$; even $f$', [('P',LO,195,'f_b(z)='),('P',LO,303,'f=\\frac'),('P',LO,474,'even smooth $f$')], '4.3, 4.4, 4.6', E('f',LO,295,330), 'B, D'),
 ('$f_\\sigma$, $F=\\max f_\\sigma$; $f_\\varepsilon$', [('P',CE,18,'F(z)=\\max')], '§5', E('F',CE,1,270), 'B, D'),
 ('$F_r(u)$; $F(x)$; $F_B$; $F_s(L,z)$; $F_0$; $F(v,a)$; $F_{\\rm near},F_{\\rm small},F_h,F_w$; $F_u$', [('P',CN,87,'F_r(u)'),('P',CN,322,'F(x)='),('P',CO,659,'F_s(L,z)'),('P',CO,502,'F(v,a)'),('P',LO,435,'F_u=')], '§3–4.5', [], 'B'),
])
S('$r$, $s$ (indices vs parameters)', 13, [
 ('row index $r$; Chebyshev degree $r$; $r=j+k$', [('P',CN,61,'1\\leq r<m'),('P',CN,122,'r=j+k')], '§2–§3, 4.2', E('r',CN,1,460), 'D'),
 ('radius bound $r$ of Lemma 4.6 ($\\rho\\leq r$); $a_r,U_r,\\dots$', [('P',LO,77,'\\rho\\leq r')], '4.3–4.4', E('r',LO,68,243), 'A (4.3 proof), D'),
 ('periodic indices $(r,s)$ in $\\Gamma^-$, $H_{rs}$', [('P',LO,35,'(r,s)'),('P',LO,120,'r+k\\equiv J')], '§4 pre., 4.3, 5.2', E('r',LO,1,70)+E('s',LO,1,70), 'A (4.3 proof), D'),
 ('endpoint index distance $s$ ($1\\leq s\\leq4$)', [('P',LO,145,'distance is $1\\leq s')], '4.3 (proof)', [], 'A (4.3)'),
 ('$s=m-r$; $s=j-k$; $J(v,s,e)$ argument; $c_s$; $s=b/\\pi$, $\\pm y/\\pi$; side label $v_s,N_s,P_s$', [('P',CN,62,'s=m-r'),('P',CN,122,'s=j-k'),('P',CO,20,'J(v,s,e)'),('P',CO,1115,'s=\\pm y')], '§3, 4.1–4.2', EL(('§3','s',CN,1,460),('§4.1–4.2','s',CO,1,1400)), 'A (4.2), D'),
 ('$r_0$; $r(w)$ residual; $r=c_e+c_d-2a$; $r_U$; $r_R$; Abel $r$', [('P',CO,536,'r_0='),('P',CO,1147,'r(w)='),('P',CO,1297,'r=c_e'),('P',LO,513,'r_U='),('P',CE,188,'r_R=')], '4.1–§5', E('r_{0}',CO,1,1400), 'A (4.2), D'),
 ('squared inward variables $s=A^2/2$, $t=B^2/2$; Bernstein $(s,t)$', [('P',LO,471,'s=A^2/2'),('P',CE,32,'(s,t)\\in')], '4.6, §5', E('s',CE,1,270), 'B, D'),
])
S('$L$', 14, [
 ('cardinal polynomials $L_B$, $L_{jk}$, $L_\\ell$', [('P',IN,74,'L_B'),('P',LO,17,'L_{jk}')], '§1–§2, §4 pre., §5', E('L_{.*}',PR,1,100,LO,1,70,CE,1,270), 'D'),
 ('square reference $L_n$', [('P',CN,113,'L_n=')], '3.2–3.3', E('L_{n}',CN,1,460), 'D'),
 ('$L=\\log n$', [('P',CO,4,'L=\\log n')], '4.1–4.6', E('L',CO,1,1400,LO,244,560), 'B (4.3/4.4), D'),
 ('periodic mesh size $L$ in $(M,L)$', [('P',LO,135,'(M,L)=(m,n)')], '4.3 (proof)', E('L',LO,115,243), 'B, D'),
 ('floor $L_h(\\rho)$; cyclic vector $L_{n,k}$; lower endpoint $L_c$', [('P',LO,275,'L_h(\\rho)'),('P',CO,1215,'L_{n,k}'),('P',CE,60,'L_c')], '4.4; 4.2; §5', E('L_{h}',LO,1,560), 'B, D'),
 ('companion: $L=\\log m$; $L(y)$ analytic factor', [('C',CN,1519,'$L=\\log m$'),('C',CN,1427,'L')], '3.3', '–', 'C'),
])
S('$M,\\mathcal M$', 15, [
 ('grid size $M$ in $Q_M$, $h_p^{(M)}$; offset cutoff $M$ ($\\ell>M$); $M_m$; $C_M$', [('P',PR,39,'For $M\\geq1$'),('P',CN,194,'\\ell>M'),('P',CN,347,'M_m=')], '§2; 3.2; 3.3', E('M_{m}',CN,1,460), 'B, D'),
 ('$M_\\infty$ completed model; $\\mathcal M$, $\\mathcal M_\\phi$; $M_A^\\phi,M_A$', [('P',CO,243,'M_\\infty'),('P',CO,538,'\\mathcal M&=')], '4.1–4.6', EL(('$M_\\infty$','M_{\\infty}',CO,1,1400,LO,1,560),('$\\mathcal M,\\mathcal M_\\phi$',r'\\mathcal\{M\}(_\{\\phi\})?',CO,1,1400),('$M_A^\\phi,M_A$',r'M_\{A\}(\^\{\\phi\})?',CO,1,1400)), 'D'),
 ('analytic norm $M(n)$ (also bare $M$ in 4.6, §5)', [('P',CO,601,'M(n)='),('P',LO,471,'If $M$ bounds')], '4.2–§5', EL(('$M(n)$','M',CO,590,610),('4.6','M',LO,465,560),('L. 5.1 (generic)','M',CE,15,55),('5.2','M',CE,100,270)), 'D'),
 ('coefficient height $M$ in $M\\tan(e/2)$', [('P',CO,824,'M\\tan(e/2)')], '4.2', [], 'A (4.2: $M(n)$, $\\mathcal M$)'),
 ('physical mesh size $M$ in $(M,L)$', [('P',LO,135,'(M,L)')], '4.3', E('M',LO,115,243), 'B, D'),
 ('$M_b$, $\\mathcal M_b$; $M_*$ true norm', [('P',LO,378,'M_b&='),('P',CE,142,'M_*')], '4.5; 5.2', E('M_{*}',CE,1,270), 'B, D'),
 ('companion: $M_*:=2\\varepsilon\\cot e$; $M=\\sup|F_0\'|$; $N=2M+1$', [('C',CO,2305,'M_*'),('C',CO,3957,'M='),('C',CO,977,'N=2M+1')], '4.2; 4.1', '–', 'C ($M_*$ clashes with §5)'),
])
S('$Q,\\mathcal Q$', 16, [
 ('quadrature $Q_M(g)$; $Q_\\tau[F]$', [('P',PR,41,'Q_M(g)'),('P',CO,661,'Q_\\tau[F]')], '§2; 4.2', E('Q_{\\tau}',CO,1,1400)+E('Q_{t}',CO,1,1400), 'D'),
 ('$Q_i=|u-v_i|/2$; remainder $Q_{m,r}$', [('P',CN,155,'Q_i='),('P',CN,325,'Q_{m,r}')], '3.2; 3.3', E('Q_{m,r}',CN,1,460), 'D'),
 ('square $Q=[-1,1]^2$; series $Q(t)=2\\sum\\zeta(2j+1)t^{2j}$', [('P',PR,2,'Q=[-1,1]^2'),('P',CO,116,'Q(t)=')], '§2; 4.1', [], 'B (vs $Q_t$ in 4.2)'),
 ('$\\mathcal Q_j$; $Q_0(z)$; $Q_u$', [('P',CO,654,'\\mathcal Q_j='),('P',CO,1047,'Q_0(z)='),('P',LO,436,'Q_u=')], '4.2; 4.5', [], 'A (4.2: $Q_0$ vs $Q_\\tau$)'),
 ('projections $Q_v(K),Q_h(J)$ and bare $Q$ for a projection value', [('P',LO,53,'Q_v(K)'),('P',LO,160,'Q>')], '§4 pre., 4.3', E('Q',LO,115,243)+E('Q_{v}',LO,1,560), 'D'),
 ('companion: $Q$ = magnitude of negative sum; $Q_*$; $Q_H$', [('C',CN,353,'$Q$'),('C',CO,1031,'Q_*'),('C',CO,3344,'Q_H')], '3.1; 4.1; 4.2', '–', 'C'),
])
S('$R$', 17, [
 ('remainder $R(v,s,e)$, derivatives $R_s,R_e$', [('P',CO,30,'R(v,s,e)'),('P',CO,36,'R_e&=')], '4.1–4.2', E('R',CO,1,1400)+E('R_{e}',CO,1,1400), 'D'),
 ('$R(x)$ singularity-subtracted; cutoff $R$', [('P',CN,356,'R(x)='),('P',CN,312,'r=1}^R')], '3.3', [], 'B'),
 ('row sums $R_r$; $R_{\\rm mesh}$, $R_{\\log}$', [('P',CO,622,'R_r='),('P',CO,665,'R_{\\rm mesh}')], '4.2', E('R_{mesh}',CO,1,1400), 'A (4.2: $R(v,s,e)$), D'),
 ('band remainder $R$; $R_h,R_w$; $R_b$', [('P',LO,213,'R=C\\log'),('P',LO,100,'R_h&='),('P',LO,382,'R_b&=')], '4.3; 4.5', E('R',LO,1,560), 'B, D'),
 ('rectangle $R$, $I_R,q_R,V_R,\\theta_R,\\delta_R,r_R$', [('P',CE,19,'R=[a_0,a_1]')], '§5', E('R',CE,1,270), 'B, D'),
 ('companion: $R_n$ remainder (intro) and $R_n(z,B)$ kernel (§2); $R_t$', [('C',IN,369,'R_n'),('C',PR,180,'R_n(z,B)'),('C',CO,578,'R_t')], '§1; §2; 4.1', '–', 'C (same token)'),
])
S('$\\gamma$, $\\kappa$, $\\zeta$, $\\psi$', 18, [
 ('Euler\'s constant $\\gamma$', [('P',IN,115,'$\\gamma$ is Euler')], 'global ((3), (10), (32), (40))', E('\\gamma',*ALL), 'D'),
 ('center angle\'s distance $\\gamma$ to the nearest endpoint; $\\gamma_b$', [('P',LO,136,'let $\\gamma$ be'),('P',LO,377,'\\gamma_b&=')], '4.3 (proof); 4.5', [], 'B (Euler $\\gamma$ live in 4.1)'),
 ('main constant $\\kappa$ (4)', [('P',IN,117,'\\kappa=')], 'global', E('\\kappa',*ALL), 'D'),
 ('companion: $\\kappa=8a_0/(3\\pi)$', [('C',LO,1421,'\\kappa=8a_0')], '4.5', '–', 'C (severe)'),
 ('Riemann $\\zeta$ vs companion root of unity $\\zeta=e^{2\\pi\\mathrm i/N}$', [('P',CO,116,'\\zeta(2j+1)'),('C',CO,965,'\\zeta=e')], '4.1', '–', 'C (A in 4.1)'),
 ('digamma $\\psi$ vs companion hat function $\\psi_B$', [('P',CN,70,'\\psi(z)='),('C',PR,55,'\\psi_B')], '§3–4.2; §2', '–', 'C'),
])
S('$e$, $\\bar e$', 19, [
 ('Euler\'s number: $\\mathrm e$ in (53), but italic $e^{i(pu+qv)}$ in 3.1', [('P',CN,26,'e^{i(pu+qv)}'),('P',CO,562,'\\mathrm e')], '3.1; 4.2, 4.5', E('\\mathrm{e}',CO,1,1400), 'glyph'),
 ('separation $e$ in $I(C,D,e)$, $J,E,Z,R$', [('P',CO,16,'0<e<\\pi')], '4.1–4.2', E('e',CO,1,560), 'A (4.2), D'),
 ('weights $e_j$; $e_r=\\psi(r+1/2)-\\log r$, $S_e$', [('P',LO,14,'e_j,f_k'),('P',CN,304,'e_r=')], '§4 pre.; 3.3', E('e_{j}',LO,1,70), 'B, D'),
 ('$e_j$ endpoint comparison; $e=\\rho$; $e=\\pi-z$', [('P',CO,1120,'e_j=\\frac2'),('P',CO,1260,'e=\\rho'),('P',CO,894,'e=\\pi-z')], '4.2', [], 'A (4.2)'),
 ('radial-quadratic coefficient $e$', [('P',LO,302,'e=\\frac')], '4.4', E('e',LO,295,330), 'B, D'),
 ('allowance $\\bar e=D+\\mathcal M+1/n$', [('P',CO,541,'\\bar e&=')], '4.2–4.6', E('\\bar{e}',CO,1,1400,LO,1,560), 'D'),
 ('companion: odd-$n$ indicator $e$; $e_{pq}$; $e_B$; $e_r:=R_r/(nm)-\\ell_r$', [('C',CN,468,'Let $e$'),('C',PR,287,'e_{pq}'),('C',IN,74,'e_B'),('C',CO,3332,'e_r')], '3.2; §2; §1; 4.2', '–', 'C ($e_r$ same token as 3.3)'),
])
S('$b$', 20, [
 ('$b=2ac_1$ (3); $b_{\\rm full}$, $b_c$, $b_*$', [('P',IN,113,'b=2ac_1'),('P',CO,244,'b_{\\rm full}')], '§1; 4.1', E('b',IN,1,200)+E('b_{full}',CO,1,1400), 'D'),
 ('$b_k=k\\pi/m$', [('P',LO,14,'b_k=k\\pi/m')], '§4 pre.', E('b_{k}',LO,1,70), 'D'),
 ('$b=(v+s)/2$ in proof of L. 4.1; $b=2\\arctan(q/(2a))$', [('P',CO,53,'b=(v+s)/2'),('P',CO,472,'b=2\\arctan')], '4.1', [], 'A (4.1)'),
 ('$b_0=4/\\pi^2$', [('P',CO,536,'b_0=4/\\pi^2')], '4.2, 4.5', E('b_{0}',CO,1,1400), 'D'),
 ('residual $b$; $b(z)$; $b=\\xi+|s|$; $b_s,b_L,b_R$; second argument of $\\ell_r(x,b)$', [('P',CO,691,'residual $b$'),('P',CO,1045,'b(z)='),('P',CO,1131,'b=\\xi'),('P',CO,1324,'b_L=')], '4.2', E('b',CO,640,1400), 'A (4.2), D'),
 ('physical row $b=l\\pi/M$; band $[a_0,b_0]$', [('P',LO,137,'b=l\\pi/M'),('P',LO,216,'[a_0,b_0]')], '4.3', [], 'B ($b_0$ token)'),
 ('phase coordinate $b$, $[b_0,b_1]$', [('P',CE,19,'[b_0,b_1]')], '§5', E('b',CE,1,270), 'B, D'),
])
S('$c$', 21, [
 ('$c=c_1^2+\\kappa$, $c_1=ad$', [('P',IN,113,'c=c_1^2')], 'global', E('c',IN,1,200), 'D'),
 ('$c_r=\\csc(r\\pi/(2n))$', [('P',CN,123,'c_r=')], '3.2', [], 'B'),
 ('$c=(v-s)/2$ in proof of L. 4.1; $c_s$, $c=\\cos(\\pi s/2)$', [('P',CO,53,'c=(v-s)/2'),('P',CO,128,'c_s='),('P',CO,342,'c=\\cos(\\pi s/2)')], '4.1', [], 'A (4.1)'),
 ('$c_e,c_d$ (phase cosines); $c_k$ (48)', [('P',CO,9,'c_e='),('P',CO,418,'c_k&=')], '4.1–4.6', E('c_{k}',CO,1,1400)+E('c_{e}',CO,1,1400), 'D'),
 ('shift $c$ in $g(-w+c,\\dots)$; $n\\pm c$; $c$ in $2\\cos$ denominators; $c_P$', [('P',CO,828,'w+c'),('P',CO,980,'n\\pm c'),('P',CO,1235,'c>99/100'),('P',CO,1365,'c_P=')], '4.2', [], 'A (4.2)'),
 ('band parameter $c$ ($5/4$, $2$); $c=\\cos(1/2)$; descent $c$', [('P',LO,196,'1<c\\leq2'),('P',LO,361,'c=\\cos(1/2)'),('P',LO,527,'c=32\\delta')], '4.3; 4.5; 4.6', E('c',LO,1,560), 'B, D'),
 ('Bernstein coefficients $c_{\\ell,ij}$; $c=q/\\pi^2$', [('P',CE,28,'c_{\\ell,ij}'),('P',CE,210,'c=q/\\pi^2')], '§5', E('c_{\\ell,ij}',CE,1,270), 'B, D'),
 ('companion: $c=\\cos u$, $c_i=\\cos v_i$; $c_v$; $c_j$', [('C',CN,571,'c=\\cos u'),('C',CN,1519,'c_v'),('C',CE,750,'c_j')], '3.2; 3.3; 5.2', '–', 'C'),
])
S('$d,\\mathfrak d$', 22, [
 ('$d=\\gamma+\\log(8/\\pi)$', [('P',IN,112,'d=\\gamma')], 'global', E('d',IN,1,200,CN,1,460), 'D'),
 ('weights $d_r$', [('P',CN,114,'d_r=')], '3.2', [], 'B'),
 ('$d_0=\\gamma+2\\log2$', [('P',CN,321,'d_0=\\gamma')], '3.3', E('d_{0}',CN,1,460), 'B (same token)'),
 ('$d_0=C_0b_*/\\pi^2$', [('P',CO,306,'d_0=C_0b_*')], '4.1', E('d_{0}',CO,1,1400), 'B (same token), D'),
 ('$d_+=(q-p)_+$; $d_\\beta$', [('P',CO,13,'d_+='),('P',CO,544,'d_\\beta=')], '4.1–4.6', E('d_{\\beta}',CO,1,1400), 'D'),
 ('$d=v/h_*$; shift $d$; $d(z)$; $d_1,d_2$', [('P',CO,718,'d=v/h_*'),('P',CO,828,'w+d'),('P',CO,1045,'d(z)='),('P',LO,296,'d_1,d_2')], '4.2; 4.4', [], 'A (4.2)'),
 ('pair defect $\\mathfrak d(z,w)$', [('P',LO,51,'\\mathfrak d(z,w)')], '§4 pre., 4.3', E('\\mathfrak{d}',LO,1,560), 'D'),
 ('companion: $d=\\pi/L$; degree $d$; $d_i^{(r)}$', [('C',LO,676,'d=\\pi/L'),('C',CE,745,'d'),('C',CE,418,'d_i^{(r)}')], '4.3; 5.1–5.2', '–', 'C'),
])
S('$h$', 23, [
 ('$h=n-j$; $h_{\\sigma,\\ell}$; cell width $h$; shift $h$', [('P',CN,167,'put $h=n-j$'),('P',CN,185,'h_{\\sigma,\\ell}'),('P',CN,227,'[u,u+h]'),('P',CN,296,'shift $h$')], '3.2; 3.2; 3.3; 3.3', [], 'A (3.3)'),
 ('mesh steps $h=\\pi/m$, $h=\\pi/n$, $h_*=\\pi/n$', [('P',CO,635,'h=\\pi/m'),('P',CO,697,'h=\\pi/n'),('P',CO,718,'h_*=\\pi/n')], '4.2', [], 'A (4.2)'),
 ('series $h_j(t)$; $H_h$, $D_h$', [('P',CO,637,'h_j(t)')], '4.2', E('h_{j}',CO,1,1400), 'A (4.2), D'),
 ('label h(orizontal) in $Q_h$, $I_h,R_h,F_h,A_h,B_h$', [('P',LO,55,'Q_h(J)'),('P',LO,100,'I_h&=')], '§4 pre.–4.4', E('Q_{h}',LO,1,560)+E('F_{h}',LO,1,560), 'D'),
 ('$h_p^{(M)}$; $h=x-1/2$; $h=\\pi/4$; vector $(h_\\ell)$', [('P',PR,47,'h_p^{(M)}'),('P',LO,362,'h=x-1/2'),('P',LO,490,'h=\\pi/4'),('P',CE,7,'(h_\\ell)')], '§2; 4.5; 4.6; §5', [], 'B'),
])
S('$u,v,w,z$ (variables)', 24, [
 ('kernel arguments $u,v$ in $G_n(u,v)$, $f(u,v)$, $A(u,v)$; $v=r\\pi/m$; $v_0,v_1$', [('P',PR,70,'G_n(u,v)'),('P',CN,85,'v=r\\pi/m'),('P',CN,153,'v_0=\\theta_k')], '§2–§4', E('v',CN,1,460), 'D'),
 ('$u_r$; $v(x)=w(x)-a/x$', [('P',CN,304,'u_r='),('P',CN,336,'v(x)=')], '3.3', [], 'A (3.3: $v$ angle and $v(x)$)'),
 ('$u=1-a$, $z=(1-c_e)(1-c_d)$', [('P',CO,10,'u=1-a')], '4.1–4.6', E('u',CO,1,1400)+E('z',CO,1,560), 'A (4.2: $u$ angle), D'),
 ('$J(v,s,e)$ coefficient $v$ ($v=p/2$); row variable $v$ in $C(v)$', [('P',CO,20,'J(v,s,e)'),('P',CO,229,'0<v<2\\pi'),('P',CO,492,'v=p/2')], '4.1–4.2', E('v',CO,1,560), 'A (4.1), D'),
 ('$v_0=7b_*/(2\\pi^2)$ vs $v_0=\\pi j/m$ vs $v_0=\\theta_k$', [('P',CO,307,'v_0=7b_*'),('P',CO,1170,'v_0=\\pi j/m')], '4.1; 4.2', E('v_{0}',CO,1,1400), 'B (same token), D'),
 ('$v=w/m$, $u_j=z/n$, $w=r\\pi+b$, $z=j\\pi+x$', [('P',CO,917,'v=w/m')], '4.2', E('w',CO,915,930)+E('z',CO,915,930), 'A (4.2), D'),
 ('$w(x)=\\cot(\\pi x/2)$; $w_{jk}$ weights', [('P',CN,57,'w(x)='),('P',PR,20,'w_{jk}=')], '§3; §2, §4', E('w',CN,1,460)+E('w_{jk}',PR,1,100,LO,1,70), 'D'),
 ('$w$ in $f(w)$, $H(w)$; $w=a\\cot(t/2)/2$; $w_r$; effective angle $w$; $w_0=721/384$; $w_*$', [('P',CO,86,'f(w)'),('P',CO,265,'w=a\\cot'),('P',LO,147,'effective angle $w$'),('P',LO,354,'w_0=')], '4.1–5.1', E('w',CO,1,560)+E('w_{0}',LO,1,560), 'A (4.1–4.2), D'),
 ('$v=u-u_1$ (outer variable); $u_1$, $u_0$; $u\',v\'$', [('P',LO,353,'v=u-u_1'),('P',CE,201,"u'=U")], '4.5; 5.2', E('v',LO,350,465), 'B, D'),
])
S('$p,P$ and $q$', 25, [
 ('mode indices $p,q$', [('P',PR,25,'p+q\\leq n')], '§2–§3', E('p',PR,1,100), 'D'),
 ('$p=\\sin x$, $q=\\sin y$, $P=p+q$', [('P',CO,13,'p=\\sin x')], '4.1–4.6', EL(('$p$','p',CO,1,1400,LO,350,430),('$q$','q',CO,1,409,CO,432,1400,LO,350,430),('$P$','P',CO,1,1400,LO,350,430)), 'D'),
 ('$q_0=\\pi^2/4-1$ vs $q_0=7/48$', [('P',CN,321,'q_0=\\pi'),('P',LO,490,'q_0=7/48')], '3.3; 4.6', [], 'B (same token)'),
 ('$q_\\pm$; offsets $q$; corner-witness ratio $q$; $q_R$', [('P',CO,744,'q_\\pm='),('P',LO,145,'offsets'),('P',CE,203,'q=\\min'),('P',CE,124,'q_R')], '4.2; 4.3; 5.2', E('q_{R}',CE,1,270), 'A (4.3: $q$ offset vs $q=\\sin y$), D'),
 ('$P_r$; nodes $\\mathcal P_n$; $P_n=T_{n+1}+T_n$', [('P',CN,96,'P_r=w'),('P',LO,21,'P_n=T_{n+1}')], '3.1; §4 pre.', E('\\mathcal{P}_{n}',IN,1,200,PR,1,100), 'D'),
 ('$P_0(z)$ function vs $P_0=24/25$', [('P',CO,1046,'P_0(z)='),('P',LO,354,'P_0=24/25')], '4.2; 4.5', E('P_{0}',LO,1,560), 'B (same token), D'),
 ('$P_s$, $P_s^0$; polynomial $P(\\rho)$; $p_\\pi,p_0,p_\\pm$', [('P',CO,1266,'P_s='),('P',LO,328,'P(\\rho)='),('P',LO,94,'p_\\pi=22/7'),('P',CE,176,'p_-\\leq\\pi')], '4.2; 4.4; 4.3–§5', E('P',LO,320,350), 'A (4.4/4.5: $P(\\rho)$ vs $P$), D'),
])
S('$\\delta,\\Delta$', 26, [
 ('Kronecker $\\delta_{AB}$; Dirac $\\delta_\\pi$', [('P',PR,3,'\\delta_{AB}'),('P',CO,100,'\\delta_\\pi')], '§2; 4.1', E('\\delta_{\\pi}',CO,1,1400), 'D'),
 ('$\\delta=v_0-v_1$; Riemann width $\\delta$', [('P',CN,154,'\\delta=v_0'),('P',CN,190,'[\\delta,1-\\delta]')], '3.2', [], 'A (3.2)'),
 ('$\\delta=9/4-C_*$; $\\delta=q/2$', [('P',CO,464,'\\delta=9/4'),('P',CO,492,'\\delta=q/2')], '4.1', [], 'A (4.1)'),
 ('$\\delta_r$ parity; operator $\\delta_aX$; $\\delta\\mathcal H_j$; $\\delta=x-y$', [('P',CO,620,'\\delta_r='),('P',CO,682,'\\delta_aX'),('P',CO,1251,'\\delta\\mathcal H_j'),('P',CO,1260,'\\delta=x-y')], '4.2', E('\\delta_{a}',CO,1,1400), 'A (4.2), D'),
 ('floors $\\delta_n(r)$; gates $\\delta_A,\\delta_D,\\delta$; $\\delta_R$', [('P',LO,87,'\\delta_n(r)='),('P',LO,494,'\\delta_A&='),('P',CE,174,'\\delta_R')], '4.3; 4.6; §5', E('\\delta_{n}',LO,1,560), 'D'),
 ('$\\Delta_n$; $\\Delta_{JK}$; $\\Delta_2$', [('P',CN,173,'\\Delta_n'),('P',LO,47,'\\Delta_{JK}'),('P',CO,656,'\\Delta_2=')], '3.2; §4; 4.2', E('\\Delta_{JK}',LO,1,560)+E('\\Delta_{2}',CO,1,1400), 'D'),
])
S('$\\eta,\\sigma,\\tau$', 27, [
 ('weights $\\eta_k$ vs signs $\\eta=\\pm1$ (24), (27)', [('P',PR,19,'\\eta_k'),('P',LO,18,'\\sigma,\\eta=\\pm1')], '§2–§3; §4 pre.', E('\\eta',LO,1,70), 'B, D'),
 ('profile offsets $\\eta_\\pm(v)$; $\\eta j$; $\\eta_r$; $\\eta=3/2$', [('P',CO,232,'\\eta_-(v)'),('P',CO,771,'\\eta j'),('P',LO,96,'\\eta_r&='),('P',LO,355,'\\eta=3/2')], '4.1; 4.2; 4.3; 4.5', EL(('$\\eta_\\pm$',r'\\eta_\{[+-]\}',CO,1,1400),('$\\eta=3/2$','\\eta',LO,350,430)), 'B, D'),
 ('$\\sigma=\\pm1$; $\\sigma_\\pm$; label $\\sigma=N,W$; sign index of $f_\\sigma$', [('P',CN,180,'\\sigma=\\pm1'),('P',CO,919,'\\sigma_-='),('P',CO,1379,'\\sigma=N,W'),('P',CE,18,'f_\\sigma')], '3.2; 4.2; 4.2; §5', E('\\sigma',LO,1,70), 'A (4.2), D'),
 ('$\\tau=v/a$; $\\tau(w)=w\\cot w$; offset $\\tau$ in $Q_\\tau$; $\\tau_j$', [('P',CO,503,'\\tau=v/a'),('P',CO,802,'\\tau(w)='),('P',CO,661,'Q_\\tau'),('P',CO,1122,'\\tau_j=')], '4.1; 4.2', E('\\tau',CO,1,1400), 'A (4.2), D'),
])
S('$\\ell$, $l$', 28, [
 ('odd index $\\ell$ in $\\kappa$, (35), (48); $\\ell=|j-k|$; row index in $T_{n,r}$', [('P',IN,118,'\\ell\\geq1'),('P',CN,147,'\\ell=|j-k|')], '§1, §3, 4.1', E('\\ell',IN,1,200,CN,1,460)+E('\\ell',CO,1,530), 'D'),
 ('$\\ell=-\\log\\sin\\epsilon$ (two values of $\\epsilon$ in 4.2)', [('P',CO,558,'\\ell=-\\log'),('P',CO,1330,'\\ell=-\\log'),('P',LO,373,'\\ell=-\\log')], '4.2, 4.5', E('\\ell',CO,555,580), 'A (4.2), D'),
 ('endpoint references $\\ell_r(x,b)$, $\\ell_1,\\ell_2$ in $C_2$', [('P',CO,648,'\\ell_r(x,b)')], '4.2', [], 'A (4.2)'),
 ('linear coefficients $\\ell_1,\\ell_2$', [('P',LO,296,'(\\ell_1,\\ell_2')], '4.4', E('\\ell_{1}',LO,1,560), 'B (same token as $\\ell_1(x,y)$), D'),
 ('arc length $\\ell$; row index $l$', [('P',LO,140,'length $\\ell$'),('P',LO,137,'index $l$')], '4.3', [], 'A (4.3)'),
 ('cardinal index $\\ell$: $h_\\ell,L_\\ell,c_{\\ell,ij}$', [('P',CE,28,'c_{\\ell,ij}')], '§5', E('L_{\\ell}',CE,1,270), 'B, D'),
])
S('$I$', 29, [
 ('operator $I_n$; bilinear $I_R,I_a,I_b$', [('P',IN,5,'I_n'),('P',CE,27,'I_R')], '§1–§2; §5', E('I_{n}',IN,1,200)+E('I_{R}',CE,1,270), 'D'),
 ('integrals $I_1,I_2,I_B$; $I(t)$', [('P',CN,270,'I_1='),('P',CN,399,'I(t)=')], '3.3', E('I_{1}',CN,1,460), 'D'),
 ('cancellation $I(C,D,e)$; $I_4$; $I_s$', [('P',CO,18,'I(C,D,e)'),('P',CO,479,'I_4='),('P',CO,1271,'I_s(')], '4.1–4.6', E('I',CO,1,1400)+E('I_{4}',CO,1,1400), 'D'),
 ('band integral $I$; $I_h,I_w$', [('P',LO,212,'I=C(b_0'),('P',LO,100,'I_h&=')], '4.3', E('I',LO,1,560), 'B, D'),
 ('companion: intervals $I_1,I_2$', [('C',CO,2299,'I_1')], '4.2', '–', 'C (same tokens as 3.3)'),
])
S('$E,\\mathcal E$', 30, [
 ('$E(v,s,e)$; $E_\\infty$; $E_c$', [('P',CO,42,'E(v,s,e)'),('P',CO,246,'E_\\infty='),('P',CO,325,'E_c=')], '4.1–4.6', EL(('$E$','E',CO,1,100),('$E_\\infty$','E_{\\infty}',CO,1,1400),('$E_c$','E_{c}',CO,1,1400,LO,1,560)), 'D'),
 ('error $E_n=S_n-M_\\infty$; $E_2,E_{\\rm row},E_{\\rm out},E_{\\rm ret}$; $\\mathcal E$', [('P',CO,603,'E_n=S_n'),('P',CO,1150,'\\mathcal E(h_*')], '4.2', E('E_{n}',CO,1,1400), 'D'),
 ('lower bound $E_n=245931/6050000-\\dots$', [('P',LO,224,'$E_n=')], '4.3', [], 'B (same token)'),
 ('quarter grid $E$, $V_E$', [('P',CE,155,'E=\\{')], '5.2', E('V_{E}',CE,1,270), 'B, D'),
 ('companion: $E_j$ trapezoid error; $E_{n,M,\\delta}$', [('C',CN,1487,'E_j'),('C',CN,789,'E_{n,M,\\delta}')], '3.3; 3.2', '–', 'C'),
])
S('$S$, $N$, $U,V,W$, $G$, $Z$, $\\Gamma$', 31, [
 ('$S,T$ angles; $S_i$; $S_e,S_u$ vs majorant $S_n(\\alpha,\\beta)$', [('P',CN,28,'S=(u+v)/2'),('P',CN,309,'S_e='),('P',LO,38,'S_n(\\alpha,\\beta)')], '§3; §4–§5', EL(('$S_n$','S_{n}',LO,1,560,CO,1,1400,CE,1,270)), 'B, D'),
 ('$N=n+1/2$ vs $\\mathsf N=nm$ vs $N_s,N_L,N_R$ vs labels $U_N,J_N,k_{Nx}$', [('P',IN,125,'N=n+'),('P',LO,11,'\\mathsf N=nm'),('P',CO,278,'N_s'),('P',CO,1263,'N_L=')], '§1, §3; §4–§5; 4.1–4.2', EL(('$N$','N',IN,1,200,CN,1,460),('$\\mathsf N$','\\mathsf{N}',LO,1,560,CE,1,270)), 'B, D'),
 ('$U_0$; $U_N,U_W$; $U_j$; $U_r$; vertex value $U$; Chebyshev $U_{n-1}$', [('P',CO,239,'U_0='),('P',CO,551,'U_N&='),('P',CO,1123,'U_j='),('P',LO,79,'U_r='),('P',LO,490,'U=V='),('P',CO,1218,'U_{n-1}')], '4.1–§5', EL(('$U_N,U_W$',r'U_\{[NW]\}',CO,1,1400,LO,1,560),('vertex $U$','U',LO,465,560)), 'A (4.2: $U_N$, $U_j$, $U_{n-1}$), D'),
 ('$V_n$; $V$; $V_A^\\phi,V_B^\\phi$; variation $V$ (67); $V_s,V_0$; $V_\\pm$; $V_r$; $V_b$; $V$; $V_R$', [('P',CN,65,'V_n='),('P',CN,154,'V=(v_0'),('P',CO,1053,'=:V'),('P',CO,1265,'V_s='),('P',LO,79,'V_r='),('P',CE,128,'V_R=')], '§3–§5', EL(('$V_n$','V_{n}',CN,1,460),('$V_A^\\phi,V_B^\\phi$',r'V_\{[AB]\}\^\{\\phi\}',CO,1,1400),('$V$ (67)','V',CO,1040,1060),('vertex $V$','V',LO,465,560),('$V_R,V_E$',r'V_\{[RE]\}',CE,1,270)), 'A (4.2: $V$, $V_s$, $V_A^\\phi$), D'),
 ('$W(t)=tw(t)$ vs $W(t)=\\int\\log\\cot$ ; span $W$; $W_r$; $W_n$; $W_z$', [('P',CN,401,'W(t)=tw'),('P',CO,209,'W(t)=\\int'),('P',LO,132,'span is $W$'),('P',CO,576,'W_n&='),('P',CE,22,'W_z')], '3.3; 4.1; 4.3; 4.2–4.5; §5', EL(('$W_n$','W_{n}',CO,1,1400,LO,1,560),('$W$ (§5)','W',CE,1,270)), 'B (same token $W(t)$), D'),
 ('$G_n$ kernel; $G_B$; $G_\\phi,G_g$; $G_b$; gate $G$', [('P',PR,70,'G_n(u,v)'),('P',CN,403,'G_B(t)'),('P',LO,406,'G=u_1')], '§2–4.5', EL(('$G_n$','G_{n}',PR,1,100,LO,1,560),('$G_\\phi,G_g$',r'G_\{(\\phi|g)\}',CO,1,1400),('gate $G$','G',LO,400,430)), 'B, D'),
 ('$Z(v,s,e)$; $Z_n$; $Z=2a\\cot(z/2)$; $Z_b$; $\\overline Z_\\phi$', [('P',CO,43,'Z(v,s,e)'),('P',CO,657,'Z_n=D_0'),('P',CO,1269,'Z=2a')], '4.1–4.5', EL(('$Z$','Z',CO,1,1400),('$\\overline Z_\\phi$','\\overline{Z}_{\\phi}',CO,1,1400)), 'A (4.2), D'),
 ('$\\Gamma^-$ periodic lattice; entropy $\\Gamma_\\phi$, $\\Gamma_b$, $\\Gamma(p,a)$', [('P',LO,35,'\\Gamma^-='),('P',CO,560,'\\Gamma_\\phi=')], '§4 pre., 4.3; 4.2, 4.5', EL(('$\\Gamma^-$','\\Gamma^{-}',LO,1,560,CE,1,270),('$\\Gamma_\\phi$','\\Gamma_{\\phi}',CO,1,1400)), 'D'),
])
S('$\\alpha,\\beta,\\theta,\\phi,\\nu,x,y,t$', 32, [
 ('$\\alpha=(1-x)/2$ (11) vs phase $\\alpha$ (25)', [('P',CN,62,'\\alpha=(1-x)/2'),('P',LO,28,'J\\pi+\\alpha')], '§3; §4–§5', EL(('§3','\\alpha',CN,1,460),('phase','\\alpha',LO,1,560,CE,1,270)), 'B, D'),
 ('$\\beta_H,\\beta_B$ vs phase $\\beta$; $B_\\beta$, $d_\\beta$ (label)', [('P',CN,278,'\\beta_H'),('P',LO,28,'K\\pi+\\beta')], '3.3; §4', EL(('$\\beta_H,\\beta_B$',r'\\beta_\{[HB]\}',CN,1,460),('phase','\\beta',LO,1,560,CE,1,270)), 'B, D'),
 ('$\\theta_j$ mesh angles vs physical $\\theta,\\phi$; $\\theta$ in (44); $\\theta_\\pm$; $\\theta_R$', [('P',PR,15,'\\theta_j'),('P',LO,17,'L_{jk}(\\cos\\theta'),('P',CO,338,'\\cos(\\theta/2)'),('P',CO,1168,'\\theta_\\pm='),('P',CE,129,'\\theta_R=')], '§2–§5', EL(('physical','\\theta',LO,1,70),('(44)','\\theta',CO,330,340),('$\\theta_R$','\\theta_{R}',CE,1,270)), 'B, D'),
 ('$\\phi_k$ vs physical angle $\\phi$ vs phase point/label $\\phi$ ($D_\\phi$, $E_n(\\phi)$)', [('P',PR,15,'\\phi_k'),('P',CO,557,'D_\\phi='),('P',CO,1378,'E_n(\\phi)')], '§2–§4', EL(('physical $\\phi$','\\phi',LO,1,70),('label','D_{\\phi}',CO,1,1400)), 'B, D'),
 ('$\\nu_r$ multiplicities vs $\\nu=j+s$', [('P',PR,22,'\\nu_0=1'),('P',CO,744,'\\nu=j+s')], '§2; 4.2', [], 'B'),
 ('$x=r/m$, $y_r$, $y=1-x$ (§3) vs phases $x=|\\alpha|,y=|\\beta|$ (§4); $X,Y$', [('P',CN,62,'x=r/m'),('P',CO,8,'x=|\\alpha|'),('P',CO,289,'X=\\max')], '§3; §4', EL(('§3','x',CN,280,460),('phase','x',CO,1,1400,LO,1,560)), 'B, D'),
 ('offset $t=y/\\pi$ (4.2) vs dummy $t$; $t=j/n$; $t=r/m$; $t_0,t_1,t_\\pm,t_d,t_e,t_*$', [('P',CO,635,'t=y/\\pi'),('P',CN,181,'t=j/n'),('P',CO,309,'t_0=2')], '§3–4.6', E('t',CO,630,1400), 'A (4.2), D'),
])
def cell(x):
    x = str(x).replace('\\|', '\\Vert ').replace('|', '\\vert ')
    return x
open(os.path.join(os.path.dirname(__file__), 'out', 'register-table.md'), 'w').write(
    '| # | Symbol | Meaning | Defined at (paper / companion, printed page) | Live range | Paper numbered formulas | Status |\n'
    '|---|---|---|---|---|---|---|\n' +
    '\n'.join('| ' + ' | '.join(cell(x) for x in (r, s, m, d, l, e, st)) + ' |' for s, r, m, d, l, e, st in R) + '\n')
print('rows', len(R), 'symbols', len({r[1] for r in R if r[1]}))
print('\n'.join(ERR) if ERR else 'all needles found')
