"""Independent rigorous Padua Lagrange cardinals (Claude audit, from first principles).

Does NOT import any repository code or the repository's cardinal formula.

Nodes (even checkerboard, as defined in PD-T101 / theory17 statement text):
    B=(a,b), 0<=a<=n, 0<=b<=n+1, a+b even, node point (cos(a pi/n), cos(b pi/(n+1))).
Space: total degree <= n, basis phi_(p,q)(x,y)=T_p(x)T_q(y), p+q<=n.
V[B][alpha]=phi_alpha(node B). The cardinal L_B has basis coefficients equal to
column B of V^{-1}.  V^{-1} is enclosed rigorously: R=approximate inverse (mpmath,
floating), rounded to dyadic integers at scale 2^P; E=I-R V computed EXACTLY in
integer interval arithmetic from outward cosine enclosures of V's entries;
beta=||E||_inf<1 gives |V^{-1}-R|_entry <= ||R||_inf beta/(1-beta).

Cosine enclosures: mpmath.iv (interval arithmetic, outward), converted to integer
intervals with outward floor/ceil.  Everything after that is exact integers/Fractions.
"""
from fractions import Fraction as Fr
from functools import lru_cache
import mpmath
from mpmath import mp, iv

P = 160
SC = 1 << P
iv.prec = P + 64
mp.dps = 70


def _raw_to_int(raw, shift, ceil):
    """Exact floor/ceil of raw mpf tuple (sign, man, exp, bc) times 2^shift."""
    sign, man, exp, bc = raw
    if man == 0:
        return 0
    v = -man if sign else man
    k = exp + shift
    if k >= 0:
        return v << k
    return -((-v) >> (-k)) if ceil else v >> (-k)


def iv_to_int(x):
    """Integer interval [lo,hi] at scale SC containing interval x (exact outward)."""
    lo_raw, hi_raw = x._mpi_
    return (_raw_to_int(lo_raw, P, False), _raw_to_int(hi_raw, P, True))


@lru_cache(None)
def cospi(num, den):
    """Enclosure (scale SC) of cos(num*pi/den)."""
    num %= 2 * den
    # exact values where trivially known
    if num == 0:
        return (SC, SC)
    if 2 * num == 2 * den:
        return (-SC, -SC)
    if 2 * num == den or 2 * num == 3 * den:
        return (0, 0)
    return iv_to_int(iv.cos(iv.pi * num / den))


@lru_cache(None)
def sinpi(num, den):
    num %= 2 * den
    if num == 0 or num == den:
        return (0, 0)
    if 2 * num == den:
        return (SC, SC)
    if 2 * num == 3 * den:
        return (-SC, -SC)
    return iv_to_int(iv.sin(iv.pi * num / den))


def imul(a, b):
    """Exact product of integer intervals (scale multiplies)."""
    p = (a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1])
    return (min(p), max(p))


def iadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def rescale_down(a, bits):
    """Outward divide integer interval by 2^bits."""
    return (a[0] >> bits, -((-a[1]) >> bits))


def nodes(n):
    return [(a, b) for a in range(n + 1) for b in range(n + 2) if (a + b) % 2 == 0]


def basis(n):
    return [(p, q) for p in range(n + 1) for q in range(n + 1 - p)]


@lru_cache(None)
def verified_inverse(n):
    m = n + 1
    N = nodes(n)
    A = basis(n)
    assert len(N) == len(A) == (n + 1) * (n + 2) // 2
    # V entries as integer intervals at scale SC
    V = [[rescale_down(imul(cospi(p * a, n), cospi(q * b, m)), P) for (p, q) in A] for (a, b) in N]
    # floating approximate inverse
    Vm = mp.matrix(len(N), len(A))
    for i in range(len(N)):
        for j in range(len(A)):
            lo, hi = V[i][j]
            Vm[i, j] = mpmath.mpf(lo + hi) / (2 * SC)
    Rm = Vm ** -1
    R = [[int(mpmath.nint(Rm[i, j] * SC)) for j in range(len(N))] for i in range(len(A))]
    # E = I - R V exactly, scale SC^2
    dim = len(A)
    beta_num = 0
    for i in range(dim):
        Ri = R[i]
        row_sum = 0
        for j in range(dim):
            lo = hi = 0
            for k in range(dim):
                r = Ri[k]
                if r == 0:
                    continue
                vlo, vhi = V[k][j]
                if r > 0:
                    lo += r * vlo
                    hi += r * vhi
                else:
                    lo += r * vhi
                    hi += r * vlo
            ident = SC * SC if i == j else 0
            elo, ehi = ident - hi, ident - lo
            row_sum += max(abs(elo), abs(ehi))
        beta_num = max(beta_num, row_sum)
    beta = Fr(beta_num, SC * SC)
    assert beta < 1, beta
    Rnorm = Fr(max(sum(abs(x) for x in row) for row in R), SC)
    delta = Rnorm * beta / (1 - beta)
    dint = -((-delta.numerator * SC) // delta.denominator)  # ceil(delta*SC)
    # coefficient enclosure: coef[B][alpha] = Vinv[alpha][B]
    coef = [[(R[al][Bi] - dint, R[al][Bi] + dint) for al in range(dim)] for Bi in range(dim)]
    return {'nodes': N, 'basis': A, 'coef': coef, 'beta': beta, 'delta': delta,
            'R_float': [[float(Fr(R[i][j], SC)) for j in range(dim)] for i in range(dim)]}


def edge_cos_coeffs(n, xsign):
    """d[B][q]: P_B(cos th)=sum_q d[B][q] cos(q th) on edge x=xsign (exact integer sums)."""
    inv = verified_inverse(n)
    out = []
    for Bi in range(len(inv['nodes'])):
        d = [(0, 0)] * (n + 1)
        for al, (p, q) in enumerate(inv['basis']):
            c = inv['coef'][Bi][al]
            if xsign == -1 and p % 2 == 1:
                c = (-c[1], -c[0])
            d[q] = iadd(d[q], c)
        out.append(d)
    return out


def lambda_point_edge(n, xsign, num, den):
    """Enclosure (Fractions) of lambda_n(xsign, cos(num*pi/den))."""
    d = edge_cos_coeffs(n, xsign)
    lo_sum = hi_sum = 0
    for dB in d:
        v = (0, 0)
        for q in range(n + 1):
            v = iadd(v, imul(dB[q], cospi(q * num, den)))
        lo, hi = v
        lo_sum += 0 if lo <= 0 <= hi else min(abs(lo), abs(hi))
        hi_sum += max(abs(lo), abs(hi))
    return Fr(lo_sum, SC * SC), Fr(hi_sum, SC * SC)


def lambda_point_general(n, xa, xden, yb, yden):
    """Enclosure of lambda_n(cos(xa pi/xden), cos(yb pi/yden)) at a general point."""
    inv = verified_inverse(n)
    lo_sum = hi_sum = 0
    for Bi in range(len(inv['nodes'])):
        v = (0, 0)
        for al, (p, q) in enumerate(inv['basis']):
            phi = rescale_down(imul(cospi(p * xa, xden), cospi(q * yb, yden)), P)
            v = iadd(v, imul(inv['coef'][Bi][al], phi))
        lo, hi = v
        lo_sum += 0 if lo <= 0 <= hi else min(abs(lo), abs(hi))
        hi_sum += max(abs(lo), abs(hi))
    return Fr(lo_sum, SC * SC), Fr(hi_sum, SC * SC)
