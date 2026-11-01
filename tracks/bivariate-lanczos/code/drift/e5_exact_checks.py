#!/usr/bin/env python3
"""Exact symbolic corroboration of the two E5 analytic proofs.

No finite check is used as the reason for the all-n theorem. SymPy checks the
printed identities; the written Taylor argument supplies the universal limit.
"""
import json
import platform
import sympy as s


def main():
    n, m, t, alpha, beta = s.symbols("n m t alpha beta", real=True)
    f = (-s.cos((n-m)*t-alpha)*s.cos(m*t+beta)
         + s.cos(m*t+alpha)*s.cos((n+1-m)*t-beta))
    first = ((n+1)*s.cos(alpha)*s.sin(beta)
             - n*s.sin(alpha)*s.cos(beta))
    first_sines = (s.sin(alpha+beta)-(2*n+1)*s.sin(alpha-beta))/2
    second = (-(2*n+1-2*m)*s.cos(alpha)*s.cos(beta)
              - 2*m*s.sin(alpha)*s.sin(beta))
    assert s.simplify(s.diff(f, t).subs(t, 0)-first) == 0
    assert s.simplify(s.expand_trig(first-first_sines)) == 0
    assert s.simplify(s.diff(f, t, 2).subs(t, 0)-second) == 0
    cubic = -(2*n+1)*m**3*s.pi**3/(3*n**2*(n+1)**2)
    assert s.limit(n**3*cubic, n, s.oo) == -s.Rational(2, 3)*m**3*s.pi**3
    r = s.symbols("r")
    q = 9*((r+1)**2-r*(r+8)/2)+(r+8)**2-(r+1)*(r+27)
    assert s.expand(q) == s.Rational(9, 2)*r*r-30*r+46
    assert q.subs(r, s.Rational(10, 3)) == -4
    a = 20*s.pi**3/9
    b = s.Rational(2, 3)*a*s.pi**3
    assert s.simplify(-4*b*b + 6400*s.pi**12/729) == 0

    # Scoped failed-path identities (PD-N?drift-codex-32).
    angle, delta, amplitude = s.symbols("angle delta amplitude", real=True)
    sine_sequence = [amplitude*s.sin(angle-j*delta) for j in range(4)]
    edge_p = (9*(sine_sequence[1]**2-sine_sequence[0]*sine_sequence[2]/2)
              + sine_sequence[2]**2-sine_sequence[1]*sine_sequence[3])
    edge_expected = amplitude**2*(s.Rational(9, 2)*s.sin(angle-delta)**2
                                  + s.Rational(11, 2)*s.sin(delta)**2)
    sc, cc, sd, cd = s.symbols("sc cc sd cd")
    edge_difference = s.expand(s.expand_trig((edge_p-edge_expected)/amplitude**2))
    edge_polynomial = edge_difference.subs(
        {s.sin(angle): sc, s.cos(angle): cc,
         s.sin(delta): sd, s.cos(delta): cd}, simultaneous=True)
    circle_relations = s.groebner(
        [sc**2+cc**2-1, sd**2+cd**2-1], sc, cc, sd, cd, domain=s.QQ)
    assert circle_relations.reduce(edge_polynomial)[1] == 0
    equal_phase_p = (9*s.sin(delta)**2+s.sin(2*delta)**2
                     - s.sin(delta)*s.sin(3*delta))
    assert s.trigsimp(s.expand_trig(equal_phase_p-10*s.sin(delta)**2)) == 0
    coarse_a = s.symbols("coarse_a", real=True)
    coarse_g = [-coarse_a**2]*4
    coarse_p = (9*(coarse_g[1]**2-coarse_g[0]*coarse_g[2]/2)
                + coarse_g[2]**2-coarse_g[1]*coarse_g[3])
    assert s.simplify(coarse_p-s.Rational(9, 2)*coarse_a**4) == 0

    e = s.symbols("e", positive=True)
    one_third = s.Rational(1, 3)
    gram = s.Matrix([[1, one_third, one_third],
                     [one_third, one_third+e, e],
                     [one_third, e, one_third+e]])
    xgram = s.Matrix([[one_third, one_third+e, e],
                      [one_third+e, one_third, 0], [e, 0, 0]])
    ygram = s.Matrix([[one_third, e, one_third+e],
                      [e, 0, 0], [one_third+e, 0, one_third]])
    assert s.simplify(gram.det()-(1+18*e)/27) == 0
    ax, ay = gram.inv()*xgram, gram.inv()*ygram
    comm01 = s.factor((ax*ay-ay*ax)[0, 1])
    assert s.simplify(comm01-3*e*(12*e-1)/(1+18*e)**2) == 0

    # Separate exact moment calculation at formal split displacement t.
    moments = {}
    for total in range(4):
        for i in range(total+1):
            j = total-i
            split = (t**total+(-t)**total)/6
            original_origin = one_third if total == 0 else 0
            difference = s.expand(split-original_origin)
            expected = t*t/3 if total == 2 else 0
            assert difference == expected
            moments[f"x^{i}y^{j}"] = str(difference)

    result = {
        "result": "PASS",
        "scope": "exact symbolic identities; analytic universal proof in theory files",
        "python": platform.python_version(),
        "sympy": s.__version__,
        "corner_first_derivative": "PASS",
        "corner_sine_addition_identity": "PASS",
        "corner_second_derivative": "PASS",
        "corner_cubic_leading_limit": "PASS",
        "corner_quadratic_value": "-4",
        "corner_limit": "-6400*pi^12/729",
        "failed_equal_phase_identity": "PASS",
        "failed_square_edge_identity": "PASS",
        "failed_coarse_fixed_a_quadratic": "9*A^4/2",
        "square_gram_determinant": str(s.factor(gram.det())),
        "square_commutator_01": str(comm01),
        "square_moment_differences": moments,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
