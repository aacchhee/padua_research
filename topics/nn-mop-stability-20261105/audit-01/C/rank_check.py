#!/usr/bin/env python3
"""Auditor C: exact forward-mode (dual over Fraction) Jacobian of the full NN map
in raw 3N coordinates (nodes, w1, w2) at the frozen inputs. Checks:
 - rank of full Jacobian = 3N-2, kernel = two mass-scaling directions;
 - rank of the marginal-axis rows alone = 3N-2 (infinitesimal left inverse);
 - structural-zero rows are identically zero.
"""
import sys, json
from fractions import Fraction as Q
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import native_exact_ref as ner


class D:
    __slots__ = ('v', 'g')
    def __init__(s, v, g=None):
        s.v = Q(v); s.g = g
    @staticmethod
    def lift(o):
        return o if isinstance(o, D) else D(o)
    def _gg(s, n):
        return s.g if s.g is not None else [Q(0)] * n
    def __add__(s, o):
        o = D.lift(o); n = len(s.g or o.g or [])
        return D(s.v + o.v, None if (s.g is None and o.g is None) else [a + b for a, b in zip(s._gg(n), o._gg(n))])
    __radd__ = __add__
    def __neg__(s):
        return D(-s.v, None if s.g is None else [-a for a in s.g])
    def __sub__(s, o):
        return s + (-D.lift(o))
    def __rsub__(s, o):
        return D.lift(o) - s
    def __mul__(s, o):
        o = D.lift(o); n = len(s.g or o.g or [])
        if s.g is None and o.g is None:
            return D(s.v * o.v)
        return D(s.v * o.v, [s.v * b + o.v * a for a, b in zip(s._gg(n), o._gg(n))])
    __rmul__ = __mul__
    def __truediv__(s, o):
        o = D.lift(o); n = len(s.g or o.g or [])
        if s.g is None and o.g is None:
            return D(s.v / o.v)
        q = s.v / o.v
        return D(q, [(a - q * b) / o.v for a, b in zip(s._gg(n), o._gg(n))])
    def __rtruediv__(s, o):
        return D.lift(o) / s
    def __pow__(s, k):
        r = D(1)
        for _ in range(k):
            r = r * s
        return r
    def __eq__(s, o):
        return s.v == (o.v if isinstance(o, D) else o)
    def __ne__(s, o):
        return not s.__eq__(o)
    def __abs__(s):
        return s if s.v >= 0 else -s
    __hash__ = None


def rank(rows):
    A = [r[:] for r in rows if any(r)]
    rk, ncol = 0, len(rows[0])
    for c in range(ncol):
        p = next((i for i in range(rk, len(A)) if A[i][c] != 0), None)
        if p is None:
            continue
        A[rk], A[p] = A[p], A[rk]
        for i in range(len(A)):
            if i != rk and A[i][c] != 0:
                f = A[i][c] / A[rk][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[rk])]
        rk += 1
    return rk


def main():
    res = []
    for fam in ('krawtchouk', 'hahn'):
        for N in (4, 6):
            x, W = ner.my_inputs(N, fam)
            n3 = 3 * N
            def seed(v, k):
                g = [Q(0)] * n3; g[k] = Q(1); return D(v, g)
            xd = [seed(v, k) for k, v in enumerate(x)]
            Wd = [[seed(v, (s + 1) * N + k) for k, v in enumerate(r)] for s, r in enumerate(W)]
            # assertion in exact_nn compares P to F built from Fractions; D.__eq__ handles values
            out, _ = ner.exact_nn(xd, Wd)
            rows, axis_rows, zero_rows_ok = [], [], True
            for nu, r in out.items():
                for f in ('a1', 'a2', 'b1', 'b2'):
                    g = r[f]._gg(n3) if isinstance(r[f], D) else [Q(0)] * n3
                    rows.append(g)
                    n, m = nu
                    if (m == 0 and f in ('a1', 'b1')) or (n == 0 and f in ('a2', 'b2')):
                        axis_rows.append(g)
                    if (f == 'a1' and n == 0) or (f == 'a2' and m == 0):
                        zero_rows_ok &= not any(g)
            # mass scaling directions: d w_s = w_s
            ker_ok = True
            for s in range(2):
                v = [Q(0)] * n3
                for k in range(N):
                    v[(s + 1) * N + k] = W[s][k]
                ker_ok &= all(sum(a * b for a, b in zip(g, v)) == 0 for g in rows)
            res.append(dict(family=fam, N=N, full_rank=rank(rows), axis_rank=rank(axis_rows),
                            expected=3 * N - 2, mass_directions_in_kernel=ker_ok, structural_zero_rows_zero=zero_rows_ok))
            print(json.dumps(res[-1]), flush=True)


if __name__ == '__main__':
    main()
