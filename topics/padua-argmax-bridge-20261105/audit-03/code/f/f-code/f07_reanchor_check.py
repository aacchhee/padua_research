#!/usr/bin/env python3
"""Independent audit check of F01-seam-reanchor / F07-far-prune scalar functions.

[E] Interval (mpmath.iv, 120-bit) evaluation of every literal F01/F07 scalar
function at the sole base n=256, compared with each rational bound written in
F07 sections 2-6; plus a float scan of the scalar directions on real n>=32 and
the first integer base N where K*(N)>0 and F*(N)>0 (informative only).
Formulas transcribed by the auditor from theory/F01-seam-reanchor.md (frozen
prefix 9af7eb0f...) and theory/F07-far-prune.md (frozen prefix f62a559c...).
Usage: PYTHONPATH=<pylib> python3 f07_reanchor_check.py
"""
from fractions import Fraction as Fr
import mpmath
from mpmath import iv, mp

iv.prec = 120
mp.prec = 120

def funcs(n, M):
    """M is iv or mp namespace. n integer or real."""
    pi = M.pi
    n = M.mpf(n)
    m = n + 1
    L = M.log(n); H = 1 + L
    a0 = M.mpf(13)/16; w0 = M.mpf(29)/16; p0 = M.mpf(3)/5; P0 = M.mpf(6)/5; eta = M.mpf(3)/2
    js = M.mpf(23)/250; ts = M.mpf(221)/500
    T = (4*L**2 - 3*L)/pi**2
    b = 4/pi**2; hr = M.log(M.mpf(5)/2) + M.mpf(1)/18
    Da = ((52/pi**2)*H + 7)/n + 20*H/(pi*n**2)
    D = Da + 10/n**2
    KD = ((6 + 16/(3*pi))*H + 2/pi)/n
    eps = 3*pi/(2*m); ell = -M.log(M.sin(eps))
    W = (3*M.log(m) + M.log(2) + 2*M.log(pi) + 2)/(pi*m)
    C = 1 + 8*a0*m/(3*pi)
    Gb = p0*(1 + M.log(1 + C/p0))
    gb = 1 + M.log(1 + C/p0) - C/(p0 + C)
    MAb = p0/pi + a0*b
    VBb = 23 + (3*Gb + (2*p0 + 6*P0)*ell + 26*a0 + 20)/pi
    CBb = 6 + (4 + 4*a0/M.exp(1))/pi
    Genv = 7*L*MAb/m + VBb/(2*m) + (4/m)*(7 + (P0/pi)*(5 + 2*M.log(2*m))) + 2*CBb/m
    Denv = a0*Da + 10/n**2
    R6 = (21 + 21*a0 + 2*L + ((1 + 48*p0)*H + 24*p0)/pi)/n + (317 + M.mpf(5)/12)/n**2
    Dm = 4*w0/pi + a0*b*M.log(pi); Zm = Dm + a0*b/n
    Menv = (a0*b*(2*L + 2*hr)/n + (Dm + a0*b*(L + 1/n))/(4*n**2 - 1)
            + a0*b/(2*n - 1)**2 + (Zm + a0*b*(M.log(n + M.mpf(1)/2) + 2))/(4*(n - M.mpf(1)/2)**2))
    Cb = Denv + Genv + R6 + Menv
    Cs = eta*(7*L/(pi*m) + (3*gb + 2*ell)/(2*pi*m) + (48*H + 24)/(pi*n)) \
        + 3*((M.log(2) + 4*M.log(pi))/(pi*m) + W)
    Cl = (9*ell + 12*(5 + 2*M.log(2*m)))/(pi*m)
    Mesh = (b*(2*L + 2*hr)/n + (4 + b*(L + 1/n))/(4*n**2 - 1) + b/(2*n - 1)**2
            + (5 + b*(M.log(n + M.mpf(1)/2) + 2))/(4*(n - M.mpf(1)/2)**2))
    Bout = pi*(L + 25*M.log(2*m) + M.mpf(193)/3)/(8*m**2) + 1/(8*n**2)
    rp_raw = 71/n**2 - 22/(45*m)
    return dict(T=T, D=D, Mesh=Mesh, Bout=Bout, rp_raw=rp_raw, KD=KD, ell=ell, Gb=Gb, gb=gb,
                MAb=MAb, CBb=CBb, VBb=VBb, Genv=Genv, Denv=Denv, R6=R6, Menv=Menv, Cb=Cb,
                Cs=Cs, Cl=Cl, W=W, js=js, ts=ts, L=L, H=H)

def derived(f, M):
    rp = f['rp_raw'] if (M is mp and f['rp_raw'] > 0) else 0
    if M is iv:
        lo = f['rp_raw'].a
        assert f['rp_raw'].b < 0, "R+ positive part not certified zero"
        rp = 0
    e0 = f['D'] + f['Mesh'] + f['Bout'] + rp
    G = M.mpf(3)/16*(f['T'] + f['js']) - M.mpf(3)/5*f['ts'] - f['Cb'] - M.mpf(6)/5*f['KD'] - e0
    K = f['T'] + f['js'] - f['Cl'] - 3*f['KD']
    A = M.mpf(3)/2*f['ts'] + f['Cs']
    F = G - A**2/(4*K)
    return e0, G, K, A, F

def main():
    f = funcs(256, iv)
    e0, G, K, A, F = derived(f, iv)
    f['e0'], f['G*'], f['K*'], f['A*'], f['F*'] = e0, G, K, A, F
    # (name, relation, rational bound) as written in F07
    claims = [
        ('T', '>', Fr(21, 2)), ('T', '>', Fr(132683, 12500)),
        ('D', '<', Fr(27143, 163840)), ('Mesh', '<', Fr(87, 4000)), ('Bout', '<', Fr(1, 500)),
        ('e0', '<', Fr(143, 750)), ('KD', '<', Fr(13, 64)), ('KD', '<', Fr(21, 100)),
        ('ell', '<', Fr(41, 10)), ('Gb', '<', Fr(21, 5)), ('gb', '<', Fr(7)),
        ('MAb', '<', Fr(21, 40)), ('CBb', '<', Fr(233, 30)), ('VBb', '<', Fr(52)),
        ('Genv', '<', Fr(118, 257)), ('Denv', '<', Fr(7, 50)), ('R6', '<', Fr(30526, 65536)),
        ('Menv', '<', Fr(71, 4000)), ('Cb', '<', Fr(11, 10)), ('Cs', '<', Fr(867, 1000)),
        ('W', '<', Fr(219, 7710)), ('Cl', '<', Fr(12405, 40349)), ('K*', '>', Fr(19, 2) + Fr(193, 1500)),
        ('G*', '>', Fr(211, 1250)), ('A*', '<', Fr(1563, 1000)), ('F*', '>', Fr(283, 2850)),
    ]
    allok = True
    print("n=256 interval values (120-bit) versus F07 written bounds")
    for name, rel, q in claims:
        x = f[name]
        qv = mpmath.mpf(q.numerator) / q.denominator
        ok = (x.b < qv) if rel == '<' else (x.a > qv)
        allok &= ok
        print(f"  {name:5s} in [{mpmath.nstr(x.a, 12)}, {mpmath.nstr(x.b, 12)}]  {rel} {str(q):>14s} ({mpmath.nstr(qv, 10)}): {'OK' if ok else 'FAIL'}")
    print("  R+ raw at 256:", mpmath.nstr(f['rp_raw'].b, 6), "(<0 => positive part zero)")
    print("ALL F07 n=256 BOUNDS:", "PASS" if allok else "FAIL")
    # slack actually available
    print("  actual F*(256) lower:", mpmath.nstr(F.a, 12), " vs claimed 283/2850 =", mpmath.nstr(mpmath.mpf(283)/2850, 12))
    # scalar directions on real n >= 32 (float scan, MEASURED only)
    mp.prec = 80
    import math
    xs = [32 * (1.0005 ** k) for k in range(0, 60000)]  # 32 .. ~3.4e14
    prev = None; bad = []
    firstK = firstF = None
    for x in xs:
        g = funcs(x, mp); e0, G, K, A, F = derived(g, mp)
        if prev is not None:
            pG, pK, pA, pF, pKpos = prev
            if G < pG: bad.append(('G', x))
            if K < pK: bad.append(('K', x))
            if A > pA: bad.append(('A', x))
            if pKpos and K > 0 and F < pF: bad.append(('F', x))
        prev = (G, K, A, F, K > 0)
    print("direction scan on", len(xs), "real points in [32, %.3g]: violations =" % xs[-1], bad[:5], len(bad))
    # first integer base where both K*>0 and F*>0 (informative, NOT a claim of any record)
    for N in range(32, 400):
        g = funcs(N, mp); e0, G, K, A, F = derived(g, mp)
        if K > 0 and F > 0:
            print("first integer N>=32 with K*(N)>0 and F*(N)>0 (float):", N, " F*=", mpmath.nstr(F, 8))
            break
    for N in (32, 64, 128, 192, 200, 220, 240, 256, 320):
        g = funcs(N, mp); e0, G, K, A, F = derived(g, mp)
        print(f"  N={N}: G*={mpmath.nstr(G,6)} K*={mpmath.nstr(K,6)} A*={mpmath.nstr(A,6)} F*={mpmath.nstr(F,6)} Cb={mpmath.nstr(g['Cb'],5)} e0={mpmath.nstr(e0,5)}")

if __name__ == '__main__':
    main()
