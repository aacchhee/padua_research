"""Predeclared small correctness check for the exact beta=0 row identities."""
import hashlib
import json
import math
from pathlib import Path
import platform


def uk(k, z):
    return sum(math.cos(l*z) for l in range(1-k, k, 2))


def finite_f(n, j, r, alpha):
    m = n+1
    u = (j*math.pi+alpha)/n
    v = r*math.pi/m
    p, t = (u+v)/2, (v-u)/2
    d = uk(m, p)*uk(m, t)+uk(n, p)*uk(n, t)
    return ((-1)**j)*(d-math.cos(n*u))/2


def run():
    out = []
    for n in (2, 3, 4, 8, 16):
        m = n+1
        for alpha in (0., .17, -.17, .4, -.4):
            # Absolute rows are even in alpha; use its reflected positive row.
            sigma = abs(alpha)
            a = (1+math.cos(sigma))/2
            errors = {"cot_terms": 0., "signed_rows": 0., "absolute_rows": 0.}
            for r in range(2*m):
                delta = (1-r) % 2
                js = list(range(delta, 2*n, 2))
                ref = [finite_f(n, j, r, alpha) for j in js]
                signed = -n*(m-a) if r == 0 else n*a
                errors["signed_rows"] = max(errors["signed_rows"], abs(sum(ref)-signed))
                if r == 0:
                    row_abs = n*(m-a)
                elif r == m:
                    if sigma == 0:
                        row_abs = float(n)
                    else:
                        row_abs = abs(math.sin(sigma))/2 * sum(
                            abs(1/math.tan((sigma/2+k*math.pi)/n)) for k in range(n))
                else:
                    v = min(r, 2*m-r)*math.pi/m
                    av = (math.sin(sigma)-2*a/math.tan(v/2))/4
                    bv = (math.sin(sigma)+2*a/math.tan(v/2))/4
                    cot_values = []
                    neg_sum = 0.
                    q = math.inf if sigma == 0 else (1+math.cos(v))/math.tan(sigma/2)
                    eta = None if q >= 1 else math.asin(max(0., q))
                    for j in js:
                        u = (j*math.pi+sigma)/n
                        if abs(math.cos(u)-math.cos(v)) < 1e-13:
                            f = (n+math.cos(v))/2
                        else:
                            f = av/math.tan((u-v)/2)+bv/math.tan((u+v)/2)
                        cot_values.append(f)
                        dneg = v < u < 2*math.pi-v
                        nneg = eta is not None and eta < u < math.pi-eta
                        if dneg != nneg:
                            neg_sum -= f
                    row_abs = n*a+2*neg_sum
                    reflected_ref = [finite_f(n, j, r, sigma) for j in js]
                    errors["cot_terms"] = max(errors["cot_terms"], *(abs(x-y) for x,y in zip(cot_values, reflected_ref)))
                errors["absolute_rows"] = max(errors["absolute_rows"], abs(row_abs-sum(abs(x) for x in ref)))
            out.append({"n": n, "alpha": alpha, "rows": 2*m, "max_abs_errors": errors})
    return {"status": "MEASURED correctness only; no uniform or exact-arithmetic proof role",
            "python": platform.python_version(), "arithmetic": "Python binary64 math",
            "seed": None, "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "registered_degrees": [2,3,4,8,16], "registered_phases": [0.,.17,-.17,.4,-.4],
            "checks": out,
            "max_errors": {key: max(row["max_abs_errors"][key] for row in out)
                           for key in ("cot_terms", "signed_rows", "absolute_rows")}}


if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
