"""Exact symbolic checks of direction2 round1 formulas; no all-n proof by execution."""
import hashlib
import json
from pathlib import Path
import sympy as S


def main():
    a, b, n = S.symbols('a b n', real=True)
    m = n + 1
    d, C = b - a, 1 - b
    # Differentiate a quotient from its exact endpoint derivative data.
    def second(N0, N1D1, N2, D1square, D2):
        return S.factor(N2/d - 2*N1D1/d**2 - N0*D2/d**2 + 2*N0*D1square/d**3)
    fx = -n*n*C/(2*d) + n*(a*b-1)/d**2 - C*a/d**2 + 2*C*(1-a*a)/d**3
    fy = -m*m*C/(2*d) + n*(a*b-1)/d**2 + C*(1+2*b)/d**2 + 2*C*(1-b*b)/d**3
    dx = second(C, n*(1-a*a)/2, -n*n*C/2+n*a, 1-a*a, a)
    dy = second(C, (m/2-1)*(1-b*b), -m*m*C/2-n*b, 1-b*b, -b)
    checks = {
        'quotient_second_x': S.simplify(dx-fx) == 0,
        'quotient_second_y': S.simplify(dy-fy) == 0,
        'zero_gradient_x': S.simplify(fx.subs(b,1)+n/(1-a)) == 0,
        'zero_gradient_y': S.simplify(fy.subs(b,1)+n/(1-a)) == 0,
        'gradient_difference': S.simplify(fy-fx+(2*n+1)*C/(2*d)-C*(1-a)/d**2) == 0,
    }
    x, y = S.symbols('x y')
    # Independent rational cardinals from the existing degree-two exact proof.
    polynomials = [
        (x*x+2*x*y+x+2*y*y+y-1)/6,
        (2*x*x-2*x*y+2*x-2*y*y-y+1)/6,
        (-2*x*x-2*y*y+y+3)/3,
        (-x*x+2*y*y-y)/3,
        (x*x-2*x*y-x+2*y*y+y-1)/6,
        (2*x*x+2*x*y-2*x-2*y*y-y+1)/6,
    ]
    vals = [p.subs({x:-1,y:-1}) for p in polynomials]
    grads = [(S.diff(p,x).subs({x:-1,y:-1}),S.diff(p,y).subs({x:-1,y:-1})) for p in polynomials]
    axes = []
    for axis in range(2):
        axes.append(sum(S.sign(v)*g[axis] if v else abs(g[axis]) for v,g in zip(vals,grads)))
    checks['n2_axis_slopes'] = axes == [-S.Rational(7,3),-S.Rational(14,3)]
    checks['n2_single_zero'] = sum(v == 0 for v in vals) == 1
    checks['n2_zero_gradient_equal'] = all(g[0] == g[1] for v,g in zip(vals,grads) if v == 0)
    result = {
        'kind': 'exact symbolic verification evidence, not an all-n computer proof',
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'sympy_version': S.__version__,
        'checks': checks,
        'n2_cardinal_values': [str(v) for v in vals],
        'n2_cardinal_gradients': [[str(t) for t in g] for g in grads],
        'n2_axis_slopes': [str(t) for t in axes],
        'accepted': all(checks.values()),
    }
    print(json.dumps(result, indent=2))
    if not result['accepted']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
