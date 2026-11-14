#!/usr/bin/env python3
"""Arb enclosures (python-flint) of the constants of theory/X1-07 and of the elementary numerical inequalities used there.
  c1 = (2/pi)(gamma + log(8/pi)),  b = (4/pi) c1 = (8/pi^2)(gamma + log(8/pi)),  c = c1^2.
Asserted (certified by interval arithmetic): c1 + pi/288 < 1;  pi c1/36 + pi^2/5184 < 1.55/18;  pi/72 > 7/(240 pi);
(2/pi) log 2 < c1.  Also checks the X1-07 bounds numerically for n = 1..nmax in arb (enclosures strictly ordered):
  0 < L_n^2 - A_n^2 < (log n + 1.55)/(18 n^2),  -7 A_n/(120 pi n^4) < L_n^2 - A_n^2 - pi A_n/(36 n^2) < pi^2/(5184 n^4),
  L_n <= (2/pi) log n + 1 (strict for n >= 2).
Usage: python3 code/xu/research/x1_constants.py [--nmax 300] [--prec 256] [--out /tmp/x1r2/constants.json]
"""
import os, json, argparse
from flint import arb, ctx


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nmax", type=int, default=300); ap.add_argument("--prec", type=int, default=256)
    ap.add_argument("--out", default="/tmp/x1r2/constants.json")
    a = ap.parse_args()
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    ctx.prec = a.prec
    pi = arb.pi(); g = arb.const_euler()
    c1 = 2 / pi * (g + (8 / pi).log()); b = 4 / pi * c1; c = c1 * c1
    assert c1 + pi / 288 < 1
    assert pi * c1 / 36 + pi * pi / 5184 < arb("1.55") / 18
    assert pi / 72 > 7 / (240 * pi)
    assert 2 / pi * arb(2).log() < c1
    print("c1 =", c1.str(35)); print("b  =", b.str(35)); print("c  =", c.str(35))
    for n in range(1, a.nmax + 1):
        L = arb(0)
        for k in range(1, n + 1):
            x = pi * (2 * k - 1) / (4 * n)
            L += x.cos() / x.sin()
        L /= n
        A = 2 / pi * arb(n).log() + c1
        R = L * L - A * A
        nn = arb(n)
        assert R > 0 and R < (nn.log() + arb("1.55")) / (18 * nn ** 2), n
        E = R - pi * A / (36 * nn ** 2)
        assert E > -7 * A / (120 * pi * nn ** 4) and E < pi * pi / (5184 * nn ** 4), n
        if n >= 2:
            assert L < 2 / pi * nn.log() + 1, n
        else:
            assert (L - 1).contains(0)
    print("bounds of X1-07 verified in arb for n = 1..%d" % a.nmax)
    json.dump(dict(c1=c1.str(35), b=b.str(35), c=c.str(35), nmax=a.nmax, ok=True), open(a.out, "w"), indent=0)


if __name__ == "__main__":
    main()
