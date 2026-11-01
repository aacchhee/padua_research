"""Outward integer Bernstein bounds for global-max-only finite certificates.

The n=8 exact cardinal/real-embedding module from merged part 2 is read-only.
All mathematical comparisons are integer comparisons at its fixed precision.
Tensor coefficient intervals are stored cardinal-major, then row-major.
"""
from fractions import Fraction as F
from functools import lru_cache
import hashlib
from math import comb
from pathlib import Path
import sys

TOPIC = Path(__file__).resolve().parents[2]
REPO = TOPIC.parents[1]
PART2 = REPO / "topics/padua-proof-attempts-2-20261101/code"
PINNED_HEAD = "328be35e55143013047ec03a70e9906e82b95353"


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ceil(q):
    return -((-q.numerator)//q.denominator)


def linearly_combine(values, weights):
    lo = F(0)
    hi = F(0)
    for (a, b), w in zip(values, weights):
        if w >= 0:
            lo += a*w
            hi += b*w
        else:
            lo += b*w
            hi += a*w
    return lo.numerator//lo.denominator, ceil(hi)


@lru_cache(None)
def monomial_to_bernstein(n, i, k):
    # x=2u-1; power-to-Bernstein identity proved in correctness record.
    return sum((F(comb(i, a)*(-1)**(i-a)*2**a*comb(k, a), comb(n, a))
                for a in range(min(i, k)+1)), F(0))


def initial_coefficients(cardinals, n, interval):
    out = []
    for p in cardinals:
        terms = list(p.rep.to_dict().items())
        values = [interval(c) for (i, j), c in terms]
        rows = []
        for k in range(n+1):
            for l in range(n+1):
                weights = [monomial_to_bernstein(n, i, k)*monomial_to_bernstein(n, j, l)
                           for (i, j), c in terms]
                rows.append(linearly_combine(values, weights))
        out.append(rows)
    return out


def split_line(line):
    """Both halves from outward-rounded de Casteljau at exact t=1/2."""
    left = [line[0]]
    right = [line[-1]]
    while len(line) > 1:
        line = [((a[0]+b[0])//2, -((-(a[1]+b[1]))//2))
                for a, b in zip(line, line[1:])]
        left.append(line[0])
        right.append(line[-1])
    return left, right[::-1]


def subdivide(coeffs, n, axis):
    m = n+1
    left, right = [], []
    for table in coeffs:
        a, b = [None]*(m*m), [None]*(m*m)
        for fixed in range(m):
            indices = ([moving*m+fixed for moving in range(m)] if axis == 0
                       else [fixed*m+moving for moving in range(m)])
            l, r = split_line([table[k] for k in indices])
            for k, lv, rv in zip(indices, l, r):
                a[k], b[k] = lv, rv
        left.append(a)
        right.append(b)
    return left, right


def coefficient_bounds(coeffs):
    return [sum(max(abs(table[k][0]), abs(table[k][1])) for table in coeffs)
            for k in range(len(coeffs[0]))]


def verdict(coeffs, n, box, threshold, corners):
    bounds = coefficient_bounds(coeffs)
    if max(bounds) < threshold:
        return {"kind": "bound", "upper": max(bounds)}
    m = n+1
    for corner in corners:
        if all(box[a][0] == corner[a] or box[a][1] == corner[a] for a in range(2)):
            # Containment in the square and nonzero widths are checked by the
            # root/recursive partition; a square corner can only be a vertex.
            i = 0 if box[0][0] == corner[0] else n
            j = 0 if box[1][0] == corner[1] else n
            index = i*m+j
            other = max(v for k, v in enumerate(bounds) if k != index)
            if other < threshold:
                return {"kind": "corner", "corner": list(corner), "upper_away_from_vertex": other}
    return None


def split_box(box, axis):
    mid = sum(box[axis])/2
    left, right = list(box), list(box)
    left[axis] = (box[axis][0], mid)
    right[axis] = (mid, box[axis][1])
    return tuple(left), tuple(right)


def setup_n8():
    sys.path.insert(0, str(PART2))
    import a5_n8_field as field
    nodes, polynomials = field.construct(check=True)
    n = 8
    corners = ((-1, -1), (1, -1))
    values = []
    for x, y in corners:
        cardinal_values = [sum((c*field.K(x)**i*field.K(y)**j
                               for (i, j), c in p.rep.to_dict().items()), field.K.zero)
                           for p in polynomials]
        values.append(sum((z if field.ksign(z) >= 0 else -z for z in cardinal_values), field.K.zero))
    assert values[0] == values[1]
    corner = values[0]
    assert field.ksign(corner-field.K.one) > 0
    bound = field.kfield(corner)
    assert bound[0] > field.S
    coeffs = initial_coefficients(polynomials, n, field.kfield)
    source = PART2 / "a5_n8_field.py"
    # Pin this exact merged-file version; a changed source fails before search.
    expected_source = "764a7d7e50718c04f076ab3bbc86270adad1c47bc902d0b8d4eecf32ebbd2ec2"
    assert digest(source) == expected_source, "part-2 field source hash mismatch"
    return coeffs, {"n": n, "precision": field.PREC, "scale": field.S,
                    "threshold_interval": list(bound),
                    "corner_field_vector": [str(q) for q in field.kparts(corner)],
                    "corners": [list(z) for z in corners],
                    "exact_interpolation_checked": True,
                    "part2_field_sha256": digest(source)}


def self_test():
    # Negative endpoints exercise floor/ceiling in every average.
    left, right = split_line([(-5, -4), (0, 1), (8, 9)])
    assert left == [(-5, -4), (-3, -1), (0, 2)]
    assert right == [(0, 2), (4, 5), (8, 9)]
    assert linearly_combine([(-2, 3)], [F(-1, 3)]) == (-1, 1)
    # Constant and affine polynomials have the expected tensor coefficients.
    assert [monomial_to_bernstein(2, 0, k) for k in range(3)] == [1, 1, 1]
    assert [monomial_to_bernstein(2, 1, k) for k in range(3)] == [-1, 0, 1]
    assert [monomial_to_bernstein(2, 2, k) for k in range(3)] == [1, -1, 1]
    assert verdict([[(3, 3), (2, 2), (2, 2), (2, 2)]], 1,
                   ((F(-1), F(0)), (F(-1), F(0))), 3, ((-1, -1),))["kind"] == "corner"
    assert verdict([[(3, 3)]*4], 1,
                   ((F(-1), F(0)), (F(-1), F(0))), 3, ((-1, -1),)) is None
    return True


if __name__ == "__main__":
    assert self_test()
    print("exact Bernstein arithmetic controls passed; no mathematical search run")
