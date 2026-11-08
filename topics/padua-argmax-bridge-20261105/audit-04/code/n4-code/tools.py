#!/usr/bin/env python3
"""Named-tool locator (audit-04 N4). stdlib only. Usage: tools.py PAPERDIR COMPANIONDIR"""
import re, sys
from pathlib import Path
TOOLS = [
 ('Euler-Maclaurin', r'Euler.{0,3}Maclaurin'), ('Peano kernel', r'Peano'),
 ('Bernstein inequality', r'Bernstein(\'s)? inequality'), ('Riesz', r'Riesz'),
 ('digamma', r'digamma'), ('dominated convergence', r'dominated.convergence'),
 ('Tonelli', r'Tonelli'), ('Fubini', r'Fubini'), ('Abel', r'Abel'),
 ('Taylor', r'Taylor'), ('partial fraction', r'partial.fraction'),
 ('trapezoid', r'trapezoid'), ('midpoint rule/error', r'midpoint (rule|error|quadrature|comparison)'),
 ('BV / bounded variation', r'\bBV\b|bounded variation'), ('Lipschitz', r'Lipschitz'),
 ('mean value', r'mean.value'), ('interval arithmetic', r'interval (arithmetic|operation|endpoint)'),
 ('Arb', r'\bArb\b'), ('IEEE / binary64', r'IEEE|binary64'), ('pairwise summation', r'pairwise (addition|sum)'),
 ('layer cake', r'[Ll]ayer.cake'), ('Machin', r'Machin'), ('de Casteljau', r'Casteljau'),
 ('Horner', r'Horner'), ('alternating series', r'alternating (arctangent|cosine|sine|series)'),
 ('finite sine product', r'sine product'), ('Riemann sum', r'Riemann sum'),
 ('product-to-sum', r'[Pp]roduct.to.sum'), ('geometric sums', r'geometric sum'),
 ('termwise differentiation', r'termwise'), ('cosine/Fourier series', r'cosine series|Fourier'),
 ('dilogarithm Li_2', r'operatorname\{Li\}'), ('atanh series', r'atanh'),
 ('convexity', r'convexity|convex'), ('integration by parts', r'integrations? by parts'),
 ('reproducing kernel', r'reproducing'), ('Gram matrix', r'Gram'), ('unisolvent', r'unisolv'),
 ('triangle inequality', r'triangle inequality'), ('compactness', r'[Cc]ompactness'),
 ('Jordan sin bound', r'sin z\\geq2z/\\pi|Jordan'), ('Stirling', r'Stirling'),
 ('Cauchy (sum/seq)', r'Cauchy'), ('measure (Stieltjes)', r'measure'), ('rearrangement / translate', r'translat'),
 ('square completion', r'completing the square|square completion|Completing the square'),
 ('Chebyshev recurrence', r'Chebyshev recurrence|T_\{r\+1\}'), ('Chebyshev 2nd kind U', r'U_\{n-1\}'),
 ('reflection formula psi', r'\\psi\(1-t\)-\\psi\(t\)'), ('Leibniz / alternating bound', r'Leibniz'),
 ('outward rounding', r'outward'), ('unit roundoff', r'roundoff'), ('nextafter', r'nextafter'),
 ('GMP', r'\bGMP\b'), ('FLINT', r'FLINT'), ('MPFR', r'MPFR'), ('NumPy', r'NumPy'), ('Python', r'Python'),
 ('sinc', r'operatorname\{sinc\}'), ('zeta', r'\\zeta\('), ('Bernstein basis/positivity', r'Bernstein (basis|positivity|coefficient|form)'),
 ('harmonic estimate', r'harmonic estimate'), ('monotone sequence', r'monotone sequence'),
 ('Wallis/Gamma', r'\\Gamma\(|Gamma function'), ('Var_per definition', r'Var\}_\{\\rm per\}'),
]
def scan(d):
    files = [Path(d)/'main.tex'] + sorted((Path(d)/'sections').glob('*.tex'))
    res = {}
    for f in files:
        for no, line in enumerate(f.read_text().split('\n'), 1):
            for name, pat in TOOLS:
                if re.search(pat, line):
                    res.setdefault(name, []).append(f'{f.stem.replace("-unified","")}:{no}')
    return res
P, C = scan(sys.argv[1]), scan(sys.argv[2])
for name, _ in TOOLS:
    p, c = P.get(name, []), C.get(name, [])
    print(f'{name:28s} P[{len(p):2d}] {" ".join(p[:4]):60s} C[{len(c):2d}] {" ".join(c[:4])}')
