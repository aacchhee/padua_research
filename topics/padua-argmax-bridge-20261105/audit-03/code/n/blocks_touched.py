import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from q import doc, short
d = doc('paper')
claims = []
for m in re.finditer(r'\\begin\{(theorem|lemma|proposition|corollary|definition|remark)\}(.*?)\\end\{\1\}', d.text, re.S):
    lab = re.search(r'\\label\{([^}]+)\}', m.group(2))
    claims.append((m.start(), m.end(), lab.group(1) if lab else m.group(1)))
NAMES = {'thm:main-location':'Thm 1.1','thm:main-expansion':'Thm 1.2','lem:cardinal-kernel':'L 2.1','cu:quadrature':'L 3.1','cu:aggregate':'P 3.2',
 'uc:cancellation-lemma':'L 4.1','uc:scalar-maximum':'L 4.2','uc:master':'L 4.3','uc:central-pair':'L 4.4','uc:finite-bounds':'P 4.5','ul:selected-pairs':'L 4.6','cert:positive':'L 5.1','remark':'Rem 2'}
def touched(tok, ranges):
    rx = re.compile(tok[3:]) if tok.startswith('re:') else (re.compile(tok) if ('\\{' in tok or '.*' in tok) else None)
    eqs, sts, lines = set(), set(), set()
    for k, fu, pos in d.occ:
        if (rx.fullmatch(fu) if rx else fu == tok):
            f, line = d.loc(pos)
            for fs, a, b in ranges:
                if f.endswith(short.get(fs, fs) + '.tex') and a <= line <= b:
                    eqs.update(d.eq_numbers(pos)); lines.add((fs, line))
                    for s, e, lab in claims:
                        if s <= pos < e: sts.add(NAMES.get(lab, lab))
    return sorted(eqs), sorted(sts), len(lines)
R = [
 (r'model loss $T\to\mathfrak T$ (4.2–4.6)', r'Chebyshev $T_r$, $T_{n,r}$, $T_0$, $T_{\rm out}$', 'T', [('comparison',530,1400),('localization',244,537)]),
 (r'$j\to\mathfrak j$ (4.1–4.6)', r'index $j$ in (59), (63), (74)', 'j', [('comparison',300,610),('localization',253,537)]),
 (r'$j_*\to\mathfrak j_*$ (4.5)', r'as above', 'j_{*}', [('localization',1,560)]),
 (r'$k\to\mathfrak k$ (4.1)', r'index $k$ in (32)', 'k', [('comparison',120,160)]),
 (r'$k_0\to\mathfrak k_0$ (4.1)', r'as above', 'k_{0}', [('comparison',1,1400)]),
 (r'$k=n/m\to\mu$ (4.6, §5)', r'synonym of $\mu$ in (66); index $k$', 'k', [('localization',465,537),('certification',1,270)]),
 (r'$H=1+L\to\bar L$ (4.1–4.6)', r'$H(w)$, $H_0$, $H_n$ in 4.1', 'H', [('comparison',1,5),('comparison',530,1400),('localization',244,537)]),
 (r'$C(v),D(v)\to C_-(v),C_+(v)$ (4.1–4.2)', r'coefficients $C,D$ of (29); allowance $D$', 're:(C|D)', [('comparison',229,240),('comparison',700,716),('comparison',970,976)]),
 (r'$\mathcal H(L,v)\to\mathcal V(L,v)$ (4.1–4.2)', r'$\mathcal H_j$ (4.2), $\mathcal H_m$ (§3)', '\\mathcal{H}', [('comparison',236,240),('comparison',655,670)]),
 (r'$W(t)$ of 4.1 $\to\mathcal W(t)$', r'$W(t)=tw(t)$ of 3.3', 'W', [('comparison',205,227)]),
 (r'pole norm $B_n(t)\to\mathcal N_n(t)$ (4.2)', r'floor $B_n(r)$ of Lemma 4.6', 'B_{n}', [('comparison',680,716)]),
 (r'$(\ell_1,\ell_2,d_1,d_2)\to(\ell_x,\ell_y,d_x,d_y)$ (4.4)', r'$\ell_1(x,y)$ of 4.2; $d$ family', 're:(\\\\ell|d)_\\{[12]\\}', [('localization',290,330)]),
 (r'radial $(e,f,g)\to(\mathfrak e,\mathfrak f,\mathfrak g)$ (4.4)', r'$e$, $f$, $g$ elsewhere in §4', 're:[efg]', [('localization',299,330)]),
 (r'$P(\rho)\to\mathfrak p(\rho)$ (4.4)', r'$P=p+q$', 'P', [('localization',326,333)]),
 (r'$d_0,v_0$ of Lemma 4.3 $\to d_*,v_*$', r'$d_0$ of 3.3; $v_0$ thrice', '(d|v)_\\{0\\}', [('comparison',300,470)]),
 (r'4.5 bounds $a_0,w_0,p_0,P_0\to\bar a,\bar w,\bar p,\bar P$', r'$a_0$ of 4.3, $P_0(z)$ of 4.2', '(a|w|p|P)_\\{0\\}', [('localization',351,465)]),
 (r'band $[a_0,b_0]\to[b_-,b_+]$ (4.3)', r'$b_0=4/\pi^2$; §5 $a_0,b_0$', '(a|b)_\\{0\\}', [('localization',191,236)]),
 (r'$C=a_r-r/2\to A(0)$, $A_0\to A(b_-)$ (4.3) [D: $A(0)=C$, $A(a_0)=A_0$]', r'$C$ family', 're:(C|A_\\{0\\})', [('localization',205,236)]),
 (r'4.3 lower bound $E_n\to B_n^\sharp$', r'$E_n=S_n-M_\infty$ of (57)', 'E_{n}', [('localization',220,230)]),
 (r'$D_b=\sin\gamma\sin b\to w_b$ (4.3)', r'$D_b$ of 4.5', 'D_{b}', [('localization',190,215)]),
 (r'meshes $(M,L)\to(\bar m,\bar n)$ (4.3 proof)', r'$L=\log n$; $M(n)$', 're:(M|L)', [('localization',135,243)]),
 (r'angle $\gamma\to\theta_c$ (4.3); $\gamma_b\to\lambda_b$ (4.5)', r'Euler $\gamma$', '\\gamma', [('localization',130,243)]),
 (r'radius $r\to\bar\rho$ in Lemma 4.6 ($a_{\bar\rho}$, $U_{\bar\rho}$, …)', r'periodic $(r,s)$ in the same proof', 'r', [('localization',68,243)]),
 (r'endpoint distance $s\to i$ (4.3 proof)', r'periodic $s$ in the same proof', 's', [('localization',144,170)]),
 (r'gate $G,K,A\to\mathcal G,\mathcal K,\mathcal A$ (4.5)', r'chart $K$, $K_D$; $A$ family', 're:(G|K|A)', [('localization',400,430)]),
 (r'$C=1+8a_0m/(3\pi)\to C_\Gamma$ (4.5)', r'$C$ family; companion $\kappa$', 'C', [('localization',370,400)]),
 (r'$q_0=7/48\to q_h$ (4.6)', r'$q_0$ of 3.3', 'q_{0}', [('localization',466,537)]),
 (r'$\epsilon,\ell$ of (53) and 4.5 $\to\hat\varepsilon,\hat\ell$', r'second $\ell$ at comparison:1330', 're:(\\\\epsilon|\\\\varepsilon|\\\\ell)', [('comparison',555,580),('localization',370,430),('comparison',1005,1012)]),
 (r'$\epsilon,\ell$ at comparison:1330 $\to\varepsilon_h,\ell_h$', r'as above', 're:(\\\\epsilon|\\\\ell)', [('comparison',1329,1340)]),
 (r'displacement $\varepsilon\to\varepsilon_d$ (comparison:266–275, 828–843)', r'limit $\epsilon$ in (34), (38)', '\\varepsilon', [('comparison',260,290),('comparison',815,850)]),
 (r'$\epsilon=\min(t,\pi-t)\to e_t$ (comparison:378)', r'it is the separation $e$', '\\epsilon', [('comparison',376,379)]),
 (r'$f$ of (64) $\to\tilde g$', r'scalar profile $f$', 'f', [('comparison',826,842)]),
 (r"$g=f''$ of Lemma 4.2 $\to f''$", r'integrand $g(C,D;t)$', 'g', [('comparison',90,230)]),
 (r'variation $V$ of (67) $\to V_F$', r'$V$ family', 'V', [('comparison',1050,1075)]),
 (r'§3: $D_n\to\mathcal D_n$, $(S,T)\to(u_+,u_-)$', r'$D_{m,r}$; $T_r$, $T_{n,r}$, $S_n$', 're:(D_\\{n\\}|S|T)', [('corner',24,50)]),
 (r'§2–§3: $\epsilon_j\to\varepsilon_j$; $e^{i\cdot}\to\mathrm e^{\mathrm i\cdot}$', r'glyph', 're:(\\\\epsilon_\\{j\\}|e|i)', [('prelim',15,22),('corner',26,26)]),
 (r'optional: §3 $\alpha\to\alpha_r$', r'phase $\alpha$', '\\alpha', [('corner',1,460)]),
]
print('| Old → new (scope) | Clashes with | Numbered displays | Statements | Paper lines |')
print('|---|---|---|---|---|')
for name, why, tok, rs in R:
    e, st, n = touched(tok, rs)
    print(f"| {name} | {why} | {', '.join(map(str,e)) or 'none'} | {', '.join(st) or 'none'} | {n} |")
