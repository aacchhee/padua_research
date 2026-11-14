#!/usr/bin/env python3
"""Q0c: leverages, lifted atom count and cube-LP cap D/sum p^2 for the D3 rule.

Floating-point (mpmath, 50 digits) evaluation at the dyadic certificate centres of
topics/padua-3d-20261106/evidence/fd3-certificate.json. The true D3 rule lies within
2^-100 of these centres, so the reported values are MEASURED approximations of the
true rule's values (error far below the printed precision for the quantities used).
"""
import argparse, hashlib, itertools, json, sys
from pathlib import Path
import mpmath as mp

mp.mp.dps = 50

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--certificate', required=True)
    ap.add_argument('--output', required=True)
    a = ap.parse_args()
    c = json.loads(Path(a.certificate).read_text())
    den = mp.mpf(2) ** int(c['center_bits'])
    v = [mp.mpf(int(s)) / den for s in c['center_numerators']]
    X = [v[3*j:3*j+3] for j in range(20)]
    W = v[60:80]
    n = 3
    A = [al for al in itertools.product(range(n), repeat=3) if sum(al) <= n-1]
    D = len(A)
    def K(x):  # Christoffel-Darboux kernel of Pi_{n-1}, normalized Chebyshev product measure
        s = mp.mpf(0)
        for al in A:
            t = mp.mpf(1)
            for i in range(3):
                t *= (2 if al[i] > 0 else 1) * mp.chebyt(al[i], x[i])**2
            s += t
        return s
    p = [W[j]*K(X[j]) for j in range(20)]
    # sign-orbit sizes on the torus: 2^(number of coordinates not equal to +-1)
    orbit = [2**sum(1 for t in x if abs(abs(t)-1) > mp.mpf(10)**-20) for x in X]
    out = dict(
        schema='q0c-d3-leverage-v1',
        code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        certificate_sha256=hashlib.sha256(Path(a.certificate).read_bytes()).hexdigest(),
        command=' '.join(sys.argv), mpmath_dps=mp.mp.dps,
        n=n, D=D, N=20,
        sum_weights=mp.nstr(sum(W), 30),
        sum_leverage=mp.nstr(sum(p), 30),
        leverage_min=mp.nstr(min(p), 15), leverage_max=mp.nstr(max(p), 15),
        sum_leverage_sq=mp.nstr(sum(q*q for q in p), 20),
        cube_lp_cap_D_over_sum_p2=mp.nstr(D/sum(q*q for q in p), 20),
        lifted_atom_count_M=sum(orbit), orbit_sizes=sorted(orbit),
        m_n=sum(1 for k in itertools.product(range(-(n-1), n), repeat=3) if sum(map(abs, k)) <= n-1),
    )
    Path(a.output).write_text(json.dumps(out, indent=1) + '\n')
    print(json.dumps(out, indent=1))

if __name__ == '__main__':
    main()
