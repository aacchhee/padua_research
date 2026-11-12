"""Supplemental D3 audit: independent rational intervals and negative controls.

Run with normal CPython (no -O); production code supplies only untrusted
preconditioner proposals to this second implementation of the inequalities.
"""
import copy
import hashlib
import importlib.util
import itertools
import json
import math
import platform
import sys
import time
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent
CODE = HERE / "fd3_certify.py"
CERT = HERE.parent / "evidence/fd3-certificate.json"
OUT = HERE.parent / "evidence/fdc-d3-rational-audit.json"
CODE_HASH = "b8ca61f9c46610f20e81ea234ae6a583b3003095947317951d74cf72fbd780db"
CERT_HASH = "3677318c6dcf793f256750c0f270eb9be8eaa1143534428fcc096e497aa18a7d"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def plus(a, b):
    return a[0] + b[0], a[1] + b[1]


def times(a, b):
    endpoints = [x*y for x in a for y in b]
    return min(endpoints), max(endpoints)


def power(a, exponent):
    if exponent == 0:
        return Q(1), Q(1)
    endpoints = [a[0]**exponent, a[1]**exponent]
    if exponent % 2 == 0 and a[0] <= 0 <= a[1]:
        endpoints.append(Q(0))
    return min(endpoints), max(endpoints)


def monomial(node, alpha):
    answer = Q(1), Q(1)
    for coord, exponent in zip(node, alpha):
        answer = times(answer, power(coord, exponent))
    return answer


def indices(degree):
    # Independent product/filter construction; production uses nested bounds.
    return sorted(a for a in itertools.product(range(degree+1), repeat=3)
                  if sum(a) <= degree)


def expectation(alpha):
    # Even Chebyshev moments via the recurrence M_(k+2)/M_k=(k+1)/(k+2).
    answer = Q(1)
    for exponent in alpha:
        if exponent % 2:
            return Q(0)
        for j in range(0, exponent, 2):
            answer *= Q(j+1, j+2)
    return answer


def moment_system(box, alphas, active):
    residuals, jacobian = [], []
    for alpha in alphas:
        total = Q(0), Q(0)
        row = []
        for node_index in range(20):
            node = box[3*node_index:3*node_index+3]
            total = plus(total, times(box[60+node_index], monomial(node, alpha)))
        residuals.append(plus(total, (-expectation(alpha),)*2))
        for variable in active:
            if variable >= 60:
                node_index = variable-60
                row.append(monomial(box[3*node_index:3*node_index+3], alpha))
            else:
                node_index, axis = divmod(variable, 3)
                if not alpha[axis]:
                    row.append((Q(0), Q(0)))
                else:
                    beta = list(alpha)
                    beta[axis] -= 1
                    term = times(box[60+node_index],
                                 monomial(box[3*node_index:3*node_index+3], beta))
                    row.append(tuple(alpha[axis]*x for x in term))
        jacobian.append(row)
    return residuals, jacobian


def left_product(row, column):
    total = Q(0), Q(0)
    for coefficient, interval in zip(row, column):
        total = plus(total, times((coefficient, coefficient), interval))
    return total


def defect(preconditioner, matrix):
    columns = list(zip(*matrix))
    answer = Q(0)
    for i, row in enumerate(preconditioner):
        row_sum = Q(0)
        for j, column in enumerate(columns):
            a, b = left_product(row, column)
            row_sum += max(abs(Q(i == j)-a), abs(Q(i == j)-b))
        answer = max(answer, row_sum)
    return answer


def enclosing(outer, inner, scale):
    return Q(outer[0], scale) <= inner[0] <= inner[1] <= Q(outer[1], scale)


def modular_det(matrix, modulus):
    require(all(modulus % j for j in range(2, math.isqrt(modulus)+1)), "prime modulus")
    a = [[entry[0].numerator*pow(entry[0].denominator, -1, modulus) % modulus
          for entry in row] for row in matrix]
    answer = 1
    for k in range(len(a)):
        pivot = next((i for i in range(k, len(a)) if a[i][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            answer = -answer
        answer = answer*a[k][k] % modulus
        inverse = pow(a[k][k], -1, modulus)
        a[k] = [v*inverse % modulus for v in a[k]]
        for i in range(k+1, len(a)):
            multiplier = a[i][k]
            a[i] = [(x-multiplier*y) % modulus for x, y in zip(a[i], a[k])]
    return answer % modulus


def main():
    started = time.monotonic()
    require(sys.flags.optimize == 0 and __debug__, "normal CPython required")
    require(hashlib.sha256(CODE.read_bytes()).hexdigest() == CODE_HASH, "code pin")
    require(hashlib.sha256(CERT.read_bytes()).hexdigest() == CERT_HASH, "certificate pin")
    spec = importlib.util.spec_from_file_location("fd3_frozen", CODE)
    dev = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dev)
    cert = json.loads(CERT.read_text())
    centers = [Q(int(c), 2**180) for c in cert["center_numerators"]]
    active = cert["active"]
    radius = Q(1, 2**100)
    center = [(c, c) for c in centers]
    box = [(c-radius, c+radius) if i in active else (c, c)
           for i, c in enumerate(centers)]
    a5, a3 = indices(5), indices(3)
    require(len(a5) == 56 and len(a3) == 20, "monomial dimensions")
    require(a5 == dev.A5 and a3 == dev.A3, "monomial order")
    require(all(expectation(a) == dev.moment(a) for a in a5), "moments")
    require(len(active) == len(set(active)) == 56 and all(0 <= i < 80 for i in active),
            "active square restriction")
    require(all(-1 < lo <= hi < 1 for lo, hi in box[:60]), "interior nodes")
    require(all(0 < lo <= hi for lo, hi in box[60:]), "positive weights")
    require(all(any(box[3*i+d][1] < box[3*j+d][0] or
                    box[3*j+d][1] < box[3*i+d][0] for d in range(3))
                for i, j in itertools.combinations(range(20), 2)), "distinct nodes")
    fc, jc = moment_system(center, a5, active)
    _, jb = moment_system(box, a5, active)
    dc = [(int(c*dev.S),)*2 for c in centers]
    db = [(int(lo*dev.S), int(hi*dev.S)) for lo, hi in box]
    dfc, djc = dev.polys(dc, a5, True)
    _, djb = dev.polys(db, a5, True)
    djc = [[row[k] for k in active] for row in djc]
    djb = [[row[k] for k in active] for row in djb]
    require(all(enclosing(o, i, dev.S) for o, i in zip(dfc, fc)), "residual enclosure")
    require(all(enclosing(o, i, dev.S) for ro, ri in zip(djc, jc) for o, i in zip(ro, ri)),
            "center Jacobian enclosure")
    require(all(enclosing(o, i, dev.S) for ro, ri in zip(djb, jb) for o, i in zip(ro, ri)),
            "box Jacobian enclosure")
    r = [[Q(c, dev.S) for c in row] for row in dev.inverse_proposal(djc)]
    q = defect(r, jb)
    z = max(max(map(abs, left_product(row, fc))) for row in r)
    require(q < 1 and z + q*radius < radius, "rational self-map and contraction")
    vc = [[monomial(center[3*i:3*i+3], a) for a in a3] for i in range(20)]
    vb = [[monomial(box[3*i:3*i+3], a) for a in a3] for i in range(20)]
    dvc, dvb = dev.evaluations(dc), dev.evaluations(db)
    require(all(enclosing(o, i, dev.S) for ro, ri in zip(dvb, vb) for o, i in zip(ro, ri)),
            "Vandermonde enclosure")
    rv = [[Q(c, dev.S) for c in row] for row in dev.inverse_proposal(dvc)]
    qv = defect(rv, vb)
    require(qv < 1, "rational rank transfer")
    determinants = {str(p): modular_det(vc, p) for p in (65537, 1000003)}
    require(determinants["65537"] == 60293 and determinants["1000003"] != 0,
            "independent modular center rank")
    require(q < Q(3, 10**17) and z < Q(4, 10**55) and qv < Q(2, 10**17),
            "published readable bounds")
    a, b = centers[0], centers[3]
    dd = (1-a*a)*(1-b*b)
    require(0 not in active and 3 not in active, "fixed pair")
    require(dd > 0 and (math.isqrt(dd.numerator)**2 != dd.numerator or
                       math.isqrt(dd.denominator)**2 != dd.denominator), "quadratic degree")
    require((4*a*b).denominator != 1, "nonintegral trace")
    mutations = []
    for name in ("weight_mass_shift_2^-20", "zero_weight", "outside_cube", "duplicate_active"):
        mutated = copy.deepcopy(cert)
        if name == "weight_mass_shift_2^-20":
            mutated["center_numerators"][60] = str(int(mutated["center_numerators"][60])+2**160)
        elif name == "zero_weight":
            mutated["center_numerators"][60] = "0"
        elif name == "outside_cube":
            mutated["center_numerators"][0] = str(2**180)
        else:
            mutated["active"][1] = mutated["active"][0]
        try:
            dev.check(mutated)
        except AssertionError:
            mutations.append({"mutation": name, "result": "REJECTED_ASSERTION"})
        else:
            raise RuntimeError("accepted mutation: "+name)
    receipt = dict(verdict="PASS_INDEPENDENT_RATIONAL_RECONSTRUCTION", python=platform.python_version(),
                   implementation=platform.python_implementation(), optimize=sys.flags.optimize,
                   code_sha256=CODE_HASH, certificate_sha256=CERT_HASH,
                   audit_code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                   arithmetic="independent Fraction interval powers, derivatives, matrix defects",
                   preconditioner="untrusted proposal from frozen checker; no accuracy assumption",
                   independently_computed_center_determinants=determinants,
                   q=str(q), z=str(z), qv=str(qv), selfmap_margin=str(radius-z-q*radius),
                   normal_interpreter_mutations=mutations, elapsed_seconds=time.monotonic()-started)
    data = json.dumps(receipt, indent=2, sort_keys=True)+"\n"
    require(len(data.encode()) <= 32768, "receipt size")
    OUT.write_text(data)
    print(json.dumps(receipt))


if __name__ == "__main__":
    main()
