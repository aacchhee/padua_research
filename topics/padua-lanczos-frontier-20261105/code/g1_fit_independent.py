#!/usr/bin/env python3
"""Independent prospective G1 fit certificate arithmetic and report verifier.
Actual G1 execution is authorized only after complete152-row scope/root START.
"""
import argparse
import copy
import hashlib
import json
import pathlib
import sys
import tempfile
from fractions import Fraction as F

sys.set_int_max_str_digits(1000000)
FROZEN = '19ce7b774e5a6fa56108eebca3b2ef81f5237328e518d95225adf9f8835e060f'
FIELDS = ('Knode_squared', 'KHS_squared', 'Urow_squared', 'upper_squared')


def need(ok, message):
    if not ok:
        raise ValueError(message)


def identity(path):
    path = pathlib.Path(path)
    content = path.read_bytes()
    return dict(path=str(path.resolve()), sha256=hashlib.sha256(content).hexdigest(), bytes=len(content))


def artifact(record):
    actual = identity(record['path'])
    need(actual['sha256'] == record['sha256'] and actual['bytes'] == record['bytes'], 'artifact hash/size mismatch')
    return pathlib.Path(record['path']).read_text()


def endpoint_rows(text):
    try:
        parsed = json.loads(text)
        return parsed['runs']
    except json.JSONDecodeError:
        return [json.loads(line) for line in text.splitlines() if line.strip()]


def validate_row(row, grid, rule):
    degree = row['degree']
    need(type(degree) is int and 2 <= degree <= 20, 'invalid degree')
    count = (degree+1)*(degree+2)//2
    nodes = 325 if grid == 'triangle' else 625
    need(row['set'] == grid and row['rule'] == rule and row['sources'] == 'all'
         and row['source_count'] == count-1 and row['basis_count'] == count
         and row['point_count'] == nodes, 'row scope/source/node/basis mismatch')
    need(F(row['normal_trace_exact']) == nodes-count, 'incorrect normal trace')
    choices = row['pivot_choices']
    need(len(choices) == count-1 and set(choices) <= {'X', 'Y'}, 'invalid choices')
    for t in range(1, degree+1):
        for j in range(t+1):
            choice = choices[t*(t+1)//2+j-1]
            if j == 0:
                need(choice == 'X', 'invalid boundary choice')
            elif j == t:
                need(choice == 'Y', 'invalid boundary choice')
            elif rule != 'pivot':
                axis_x = ((rule == 'bj' and j == 0) or (rule == 'mirror' and j != t)
                          or (rule == 'alt' and 2*j < t))
                need(choice == ('X' if axis_x else 'Y'), 'incorrect frozen rule choice')
    ties = row['pivot_ties']
    need(ties == sorted(ties) and len({tuple(t) for t in ties}) == len(ties), 'invalid tie list')
    need(rule == 'pivot' or not ties, 'nonpivot tie list')
    for t, j in ties:
        need(type(t) is int and type(j) is int and 1 <= t <= degree and 0 < j < t
             and choices[t*(t+1)//2+j-1] == 'X', 'invalid X tie choice')
    if rule == 'pivot':
        need([t for t in ties if t[0] <= 12] == ([[2, 1]] if grid == 'rotated' else []),
             'incorrect frozen overlap ties')
    values = [F(row[name]['exact']) for name in FIELDS]
    need(all(v > 0 for v in values) and values[0] <= values[3]
         and values[3] == min(values[1:3]), 'endpoint positivity/order/minimum failure')
    if 'exact_gram_pairs_checked' in row:
        need(row['exact_gram_pairs_checked'] >= count*(count-1)//2, 'incomplete Gram declaration')


def load_manifest(manifest):
    """Complete entry guard. Does not call any log, OLS or fit operation."""
    need(manifest['schema'] == 'g1-fit-input-v1'
         and manifest['source_metric'] == 'PD-T137 aggregate all-source spectral normal output'
         and manifest['tie_convention'] == 'X wins exact ties'
         and manifest['frozen_source_sha256'] == FROZEN, 'wrong frozen manifest identity')
    cases = manifest['cases']
    keys = [(case['grid'], case['rule']) for case in cases]
    expected = {(g, r) for g in ('triangle', 'rotated') for r in ('bj', 'mirror', 'alt', 'pivot')}
    need(len(keys) == 8 and set(keys) == expected, 'missing/duplicate case')
    accepted = {}
    for case in cases:
        grid, rule = case['grid'], case['rule']
        p_rows = endpoint_rows(artifact(case['endpoints']))
        n_rows = endpoint_rows(artifact(case['independent_endpoints']))
        receipt = json.loads(artifact(case['acceptance_receipt']))
        need(receipt['status'].startswith('PASS'), 'independent acceptance not PASS')
        receipt_text = json.dumps(receipt)
        need(case['endpoints']['sha256'] in receipt_text
             and case['independent_endpoints']['sha256'] in receipt_text,
             'acceptance lacks endpoint identities')
        for rows in (p_rows, n_rows):
            need([r['degree'] for r in rows] == list(range(2, 21)), 'missing/duplicate degree')
            for row in rows:
                validate_row(row, grid, rule)
        for p, n in zip(p_rows, n_rows):
            for name in ('set', 'rule', 'degree', 'sources', 'source_count', 'basis_count',
                         'point_count', 'pivot_choices', 'pivot_ties'):
                need(p[name] == n[name], 'independent metadata mismatch')
            need(all(F(p[name]['exact']) == F(n[name]['exact']) for name in FIELDS),
                 'independent endpoint mismatch')
        accepted[grid, rule] = p_rows
    need(sum(map(len, accepted.values())) == 152, 'incomplete full scope')
    return accepted


def down(x, p):
    x = F(x)
    return F((x.numerator << p)//x.denominator, 1 << p)


def up(x, p):
    return -down(-F(x), p)


class I:
    """Closed rational interval rounded outward to p fractional binary bits."""
    def __init__(self, lo, hi=None, p=128):
        hi = lo if hi is None else hi
        need(F(lo) <= F(hi), 'reversed interval')
        self.p = p
        self.lo, self.hi = down(lo, p), up(hi, p)

    def lift(self, x):
        if isinstance(x, I):
            need(x.p == self.p, 'mixed precision')
            return x
        return I(x, p=self.p)

    def __add__(self, other):
        o = self.lift(other)
        return I(self.lo+o.lo, self.hi+o.hi, self.p)
    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo, self.p)

    def __sub__(self, other):
        return self+-self.lift(other)

    def __rsub__(self, other):
        return self.lift(other)+-self

    def __mul__(self, other):
        o = self.lift(other)
        v = [a*b for a in (self.lo, self.hi) for b in (o.lo, o.hi)]
        return I(min(v), max(v), self.p)
    __rmul__ = __mul__

    def __truediv__(self, other):
        o = self.lift(other)
        need(not o.lo <= 0 <= o.hi, 'denominator interval contains zero')
        return self*I(1/o.hi, 1/o.lo, self.p)

    def square(self):
        lo = 0 if self.lo <= 0 <= self.hi else min(self.lo**2, self.hi**2)
        return I(lo, max(self.lo**2, self.hi**2), self.p)

    def abs_upper(self):
        return max(abs(self.lo), abs(self.hi))

    def contains(self, x):
        return self.lo <= x <= self.hi

    def encode(self):
        return [str(self.lo), str(self.hi)]


def power2(k):
    return F(2**k) if k >= 0 else F(1, 2**(-k))


def atanh_log(v, terms):
    """Exact rational enclosure for log(v), 1<=v<=2."""
    need(1 <= v <= 2 and terms >= 1, 'invalid reduced logarithm')
    z = (v-1)/(v+1)
    total, term = F(0), z
    for j in range(terms):
        total += 2*term/(2*j+1)
        term *= z*z
    tail = 2*term/((2*terms+1)*(1-z*z))
    return total, total+tail


def logq(q, p=128):
    q = F(q)
    need(q > 0, 'nonpositive logarithm input')
    if q == 1:
        return I(0, p=p)
    k = q.numerator.bit_length()-q.denominator.bit_length()
    if q < power2(k):
        k -= 1
    t = q/power2(k)
    need(1 <= t < 2, 'incorrect range reduction')
    extra = abs(k).bit_length()+12
    bits = p+extra
    while True:
        lo, hi = down(t, bits), up(t, bits)
        terms = (bits+2)//3+4
        a, _ = atanh_log(lo, terms)
        _, b = atanh_log(hi, terms)
        l2, u2 = atanh_log(F(2), terms)
        left = a+k*(l2 if k >= 0 else u2)
        right = b+k*(u2 if k >= 0 else l2)
        if right-left <= power2(-p-2):
            return I(left, right, p)
        bits += 16


def predictors(kind, p):
    need(kind in ('E', 'P'), 'unknown predictor')
    return {s: I(s, p=p) if kind == 'E' else logq(F(s+1), p) for s in range(2, 21)}


def ols(y, x, degrees):
    degrees = list(degrees)
    need(len(degrees) >= 2, 'insufficient OLS degrees')
    meanx = sum((x[s] for s in degrees), I(0, p=x[degrees[0]].p))/len(degrees)
    meany = sum((y[s] for s in degrees), I(0, p=x[degrees[0]].p))/len(degrees)
    denom = sum(((x[s]-meanx).square() for s in degrees), I(0, p=meanx.p))
    need(denom.lo > 0, 'OLS denominator not certified positive')
    slope = sum(((x[s]-meanx)*y[s] for s in degrees), I(0, p=meanx.p))/denom
    return meany-slope*meanx, slope


def prediction_weights(kind, p):
    x = predictors(kind, p)
    mean = sum((x[s] for s in range(2, 15)), I(0, p=p))/13
    denominator = sum(((x[s]-mean).square() for s in range(2, 15)), I(0, p=p))
    need(denominator.lo > 0, 'prediction denominator not positive')
    return {h: {s: I(F(1, 13), p=p)+(x[h]-mean)*(x[s]-mean)/denominator
                for s in range(2, 15)} for h in range(15, 21)}


def quadratic(p):
    result = [[I(0, p=p) for _ in range(19)] for _ in range(19)]
    for kind, multiplier in [('P', 2), ('E', -1)]:
        weights = prediction_weights(kind, p)
        for h in range(15, 21):
            residual = [-weights[h][s] if s <= 14 else I(int(s == h), p=p)
                        for s in range(2, 21)]
            for i in range(19):
                for j in range(i, 19):
                    result[i][j] += multiplier*residual[i]*residual[j]
    for i in range(19):
        for j in range(i):
            result[i][j] = result[j][i]
    return result


def quadratic_value(Q, y):
    total = I(0, p=Q[0][0].p)
    for i in range(19):
        total += Q[i][i]*y[i].square()
        for j in range(i+1, 19):
            total += 2*Q[i][j]*y[i]*y[j]
    return total


def box_upper(Q, box):
    p = Q[0][0].p
    middle = [I((z.lo+z.hi)/2, p=p) for z in box]
    # The rational center is exact dyadic, but may require p+1 bits. Include
    # that final outward rounding in radius instead of shrinking the box.
    radius = [max(m.hi-z.lo, z.hi-m.lo) for z, m in zip(box, middle)]
    value = quadratic_value(Q, middle).hi
    for i in range(19):
        qm = sum((Q[i][j]*middle[j] for j in range(19)), I(0, p=p))
        value += 2*qm.abs_upper()*radius[i]
        value += max(F(0), Q[i][i].hi)*radius[i]**2
        for j in range(i+1, 19):
            value += 2*Q[i][j].abs_upper()*radius[i]*radius[j]
    return min(value, quadratic_value(Q, box).hi)


def slope_weights(kind):
    if kind == 'early':
        return [F(s-6, 60) if s <= 10 else F(0) for s in range(2, 21)]
    need(kind == 'late-half-early', 'unknown slope clause')
    return [-F(s-6, 120) if s <= 10 else F(2*s-31, 165) for s in range(2, 21)]


def slope_corner(kind):
    c = slope_weights(kind)
    # 0 selects lower ordinate endpoint; 1 selects upper; half for zero weight.
    if kind == 'early':
        return [F(0) if v > 0 else F(1) if v < 0 else F(1, 2) for v in c]
    return [F(1) if v > 0 else F(0) if v < 0 else F(1, 2) for v in c]


def slope_product(kind, lower, upper):
    weights, tau = slope_weights(kind), slope_corner(kind)
    scale = 60 if kind == 'early' else 1320
    product = F(1)
    for c, t, a, b in zip(weights, tau, lower, upper):
        exponent = c*scale
        need(exponent.denominator == 1, 'nonintegral exact product exponent')
        if exponent:
            product *= (a if t == 0 else b)**int(exponent)
    return (product > 1)-(product < 1)


def ratios(rows, grid):
    lower, upper, recipes = [], [], []
    for index, degree in enumerate(range(2, 21)):
        comparators = {r: rows[grid, r][index] for r in ('mirror', 'alt', 'pivot')}
        minimum_upper = min(F(row['upper_squared']['exact']) for row in comparators.values())
        minimum_lower = min(F(row['Knode_squared']['exact']) for row in comparators.values())
        bj = rows[grid, 'bj'][index]
        a = F(bj['Knode_squared']['exact'])/minimum_upper
        b = F(bj['upper_squared']['exact'])/minimum_lower
        need(0 < a <= b, 'incorrect ratio bracket')
        lower.append(a)
        upper.append(b)
        recipes.append(dict(degree=degree, lower_q=str(a), upper_q=str(b),
                            lower_min_rules=[r for r, row in comparators.items()
                                             if F(row['upper_squared']['exact']) == minimum_upper],
                            upper_min_rules=[r for r, row in comparators.items()
                                             if F(row['Knode_squared']['exact']) == minimum_lower]))
    return lower, upper, recipes


def log_endpoints(lower, upper, p):
    return [logq(q, p)/2 for q in lower], [logq(q, p)/2 for q in upper]


def slope_sign(kind, lower, upper, p):
    a, b = log_endpoints(lower, upper, p)
    values = tau_vector(slope_corner(kind), a, b)
    bound = sum((c*y for c, y in zip(slope_weights(kind), values)), I(0, p=p))
    if bound.lo > 0:
        return 1
    if bound.hi < 0:
        return -1
    return slope_product(kind, lower, upper)


def tau_vector(tau, a, b):
    need(len(tau) == 19 and all(0 <= t <= 1 for t in tau), 'inadmissible witness tau')
    return [(1-t)*lo+t*hi for t, lo, hi in zip(tau, a, b)]


def certify_witness(clause, tau, lower, upper, p):
    tau = list(map(F, tau))
    need(len(tau) == 19 and all(0 <= t <= 1 for t in tau), 'inadmissible witness tau')
    if clause in ('early', 'late-half-early'):
        need(tau == slope_corner(clause), 'slope witness is not frozen extremizing corner')
        comparison = slope_sign(clause, lower, upper, p)
        need(comparison <= 0 if clause == 'early' else comparison > 0,
             'claimed exact slope violation is false')
        return dict(clause=clause, exact_product_compare_to_one=comparison)
    need(clause == 'SSE', 'unknown violated clause')
    a, b = log_endpoints(lower, upper, p)
    margin = quadratic_value(quadratic(p), tau_vector(tau, a, b))
    need(margin.lo > 0, 'strict SSE counterchoice not independently certified')
    return dict(clause=clause, strict_margin=margin.encode())


def certify_tree(events, lower, upper, p, log_endpoint_enclosures=None):
    """Verify a complete final-restart midpoint partition, never just leaves."""
    need(p in (128, 256, 512) and 1 <= len(events) <= 4096, 'tree precision/budget failure')
    lookup = {event['id']: event for event in events}
    need(len(lookup) == len(events), 'duplicate tree id')
    roots = [e for e in events if e['parent'] is None]
    need(len(roots) == 1, 'tree must have exactly one root')
    a, b = log_endpoints(lower, upper, p)
    Q = quadratic(p)
    policy_widths = [bi.hi-ai.lo for ai, bi in zip(a, b)]
    if log_endpoint_enclosures is not None:
        supplied_a, supplied_b = log_endpoint_enclosures['lower'], log_endpoint_enclosures['upper']
        need(len(supplied_a) == len(supplied_b) == 19, 'incomplete split-policy log bounds')
        for q, pair in zip(lower+upper, supplied_a+supplied_b):
            lo, hi = map(F, pair)
            need(lo <= hi, 'reversed supplied log bound')
            verified = False
            for extra in (32, 64, 128):
                independent = logq(q, p+extra)/2
                if lo <= independent.lo <= independent.hi <= hi:
                    verified = True
                    break
            need(verified, 'supplied split-policy log enclosure not independently verified')
        policy_widths = [F(bi[1])-F(ai[0]) for ai, bi in zip(supplied_a, supplied_b)]
        need(all(width >= 0 for width in policy_widths), 'negative split-policy width')
    visited = set()
    # A legal4096-node unbalanced binary cover can exceed Python's default
    # recursion depth. The node-count guard still bounds this traversal.
    if sys.getrecursionlimit() < 10000:
        sys.setrecursionlimit(10000)
    def visit(key, parent, expected):
        need(key in lookup and key not in visited, 'missing/repeated tree child')
        visited.add(key)
        event = lookup[key]
        box = [[F(v) for v in pair] for pair in event['tau_box']]
        need(event['parent'] == parent and event['precision'] == p and box == expected,
             'tree parent/precision/partition mismatch')
        need(len(box) == 19 and all(0 <= lo <= hi <= 1 for lo, hi in box), 'invalid tau box')
        if event['action'] == 'certified':
            image = []
            for (lo, hi), ai, bi in zip(box, a, b):
                left, right = (1-lo)*ai+lo*bi, (1-hi)*ai+hi*bi
                image.append(I(left.lo, right.hi, p))
            need(box_upper(Q, image) <= 0, 'leaf upper bound not independently certified')
            return
        need(event['action'] == 'split', 'unaccepted leaf in universal certificate')
        axis = event['axis']
        need(type(axis) is int and 0 <= axis < 19, 'invalid split axis')
        scores = [width*(hi-lo) for (lo, hi), width in zip(box, policy_widths)]
        expected_axis = max(range(19), key=lambda i: (scores[i], -i))
        need(axis == expected_axis, 'split does not follow frozen width/tie rule')
        lo, hi = box[axis]
        need(lo < hi and len(event['children']) == 2, 'degenerate split')
        mid = (lo+hi)/2
        left, right = [pair[:] for pair in box], [pair[:] for pair in box]
        left[axis][1], right[axis][0] = mid, mid
        visit(event['children'][0], key, left)
        visit(event['children'][1], key, right)
    visit(roots[0]['id'], None, [[F(0), F(1)] for _ in range(19)])
    need(len(visited) == len(events), 'unreachable extra tree nodes')
    need(slope_sign('early', lower, upper, p) > 0
         and slope_sign('late-half-early', lower, upper, p) <= 0,
         'universal slope extrema do not pass')
    return dict(status='PASS independent universal certificate', visited_nodes=len(visited), precision=p)


def verify_report(manifest, report):
    """Future report interface; never invoked on actual G1 data before START."""
    rows = load_manifest(manifest)
    need(json.loads(artifact(report['input_manifest'])) == manifest, 'report manifest identity mismatch')
    artifact(report['producer'])
    artifact(report['specification'])
    need(report['schema'] == 'g1-fit-output-v1' and report['accepted_rows'] == 152
         and set(report['grids']) == {'triangle', 'rotated'}, 'incomplete output scope')
    verified = {}
    def enclosure(claim, value):
        lo, hi = map(F, claim)
        need(lo <= value.lo <= value.hi <= hi, 'reported descriptive interval not independently enclosed')
    for grid in ('triangle', 'rotated'):
        item = report['grids'][grid]
        universal = item['universal']
        p = universal['precision']
        need(p in (128, 256, 512), 'unregistered precision')
        qlo, qhi, recipes = ratios(rows, grid)
        need(item['ratio_recipes'] == recipes, 'ratio recipe/minimum mismatch')
        work = p+32
        a, b = log_endpoints(qlo, qhi, work)
        x = {kind: predictors(kind, work) for kind in ('E', 'P')}
        weights = {kind: prediction_weights(kind, work) for kind in ('E', 'P')}
        for rule in ('bj', 'mirror', 'alt', 'pivot'):
            rowset = rows[grid, rule]
            low = [logq(F(r['Knode_squared']['exact']), work)/2 for r in rowset]
            high = [logq(F(r['upper_squared']['exact']), work)/2 for r in rowset]
            for name, curve in [('lower', low), ('upper', high),
                                ('midpoint', [(lo+hi)/2 for lo, hi in zip(low, high)])]:
                y = dict(zip(range(2, 21), curve))
                for kind in ('E', 'P'):
                    intercept, slope = ols(y, x[kind], range(2, 21))
                    claim = item['rule_descriptive_fits'][rule][name][kind]
                    enclosure(claim['intercept'], intercept)
                    enclosure(claim['slope'], slope)
        for name, curve in [('lower', a), ('upper', b),
                            ('midpoint', [(lo+hi)/2 for lo, hi in zip(a, b)])]:
            y = dict(zip(range(2, 21), curve))
            claim = item['ratio_descriptive_diagnostics'][name]
            for kind in ('E', 'P'):
                intercept, slope = ols(y, x[kind], range(2, 21))
                train_intercept, train_slope = ols(y, x[kind], range(2, 15))
                sse = sum(((y[h]-sum((weights[kind][h][s]*y[s] for s in range(2, 15)),
                                     I(0, p=work))).square() for h in range(15, 21)), I(0, p=work))
                for key, value in [('all_degree_intercept', intercept), ('all_degree_slope', slope),
                                   ('training_2_14_intercept', train_intercept), ('training_2_14_slope', train_slope),
                                   ('holdout_15_20_SSE', sse)]:
                    enclosure(claim[kind][key], value)
            early = slope_weights('early')
            late = [g+e/2 for g, e in zip(slope_weights('late-half-early'), early)]
            for key, coefficients in [('early_slope', early), ('late_slope', late)]:
                enclosure(claim[key], sum((c*y for c, y in zip(coefficients, curve)), I(0, p=work)))
        status = universal['status']
        if status == 'INCONCLUSIVE, certified counterchoice':
            clause = {'early_positive': 'early', 'late_minus_half_early': 'late-half-early',
                      'SSE': 'SSE'}[universal['violated_clause']]
            result = certify_witness(clause, universal['witness_tau'], qlo, qhi, p)
        elif status == 'KILL, certified universal':
            events = [json.loads(line) for line in artifact(universal['tree_artifact']).splitlines() if line.strip()]
            result = certify_tree(events, qlo, qhi, p, item['log_endpoint_enclosures'])
        else:
            need(status == 'INCONCLUSIVE, not certified within budget', 'unknown universal status')
            result = dict(status='UNACCEPTED mathematical decision; reported budget/guard inconclusive')
        verified[grid] = dict(reported_status=status, independent=result,
                              descriptive_intervals='PASS independent outward enclosures')
    return verified


def exponential_bounds(x, terms=80):
    """Separate rational exponential-series enclosure for synthetic log checks."""
    if x < 0:
        lo, hi = exponential_bounds(-x, terms)
        return 1/hi, 1/lo
    need(x < 2, 'synthetic exponential control range')
    total, term = F(1), F(1)
    for k in range(1, terms+1):
        term *= x/k
        total += term
    following = term*x/(terms+1)
    return total, total+following/(1-x/(terms+2))


def self_test():
    controls = []
    for q in [F(1), F(2), F(3, 2), F(1, 2)]:
        interval = logq(q)
        if q != 1:
            need(exponential_bounds(interval.lo)[1] <= q
                 and exponential_bounds(interval.hi)[0] >= q,
                 'independent exp-series log enclosure check failed')
        else:
            need(interval.lo == interval.hi == 0, 'log1 not exact')
    controls.append('log bounds checked by separate exact exponential series')
    need(logq(power2(-137)).hi < 0 and logq(power2(137)).lo > 0,
         'signed range reduction')
    need(I(-1, 2).square().lo == 0 and I(-3, -2).square().lo == 4,
         'interval-square zero crossing')
    need(down(F(-1, 3), 8) <= F(-1, 3) <= up(F(-1, 3), 8), 'negative outward rounding')
    controls.append('negative log powers, negative rounding and crossing-zero squares')
    for kind in ('E', 'P'):
        x = predictors(kind, 128)
        y = {s: 2+3*x[s] for s in range(2, 21)}
        intercept, slope = ols(y, x, range(2, 21))
        need(intercept.contains(2) and slope.contains(3), 'known affine predictor regression')
    controls.append('known exact affine exponential and log predictor coefficients')
    equal = [F(1)]*19
    need(slope_product('early', equal, equal) == 0
         and slope_product('late-half-early', equal, equal) == 0, 'exact product equality')
    need(slope_product('early', [power2(s) for s in range(2, 21)],
                       [power2(s) for s in range(2, 21)]) > 0, 'exact positive early slope')
    controls.append('strict early equality fails; nonstrict late equality passes; positive early product')
    exponential = [power2(2*s) for s in range(2, 21)]
    certify_witness('SSE', [F(1, 2)]*19, exponential, exponential, 128)
    controls.append('strict SSE witness for exact synthetic exponential singleton ordinates')
    polynomial = [F((s+1)**2) for s in range(2, 21)]
    event = dict(id=0, parent=None, precision=128, tau_box=[['0', '1'] for _ in range(19)],
                 action='certified', upper_bound='0')
    certify_tree([event], polynomial, polynomial, 128)
    controls.append('universal root cover for exact synthetic logarithmic singleton ordinates')
    def rejects(label, action):
        try:
            action()
        except (ValueError, KeyError):
            controls.append('rejected '+label)
            return
        raise ValueError('malformed synthetic control accepted: '+label)
    with tempfile.TemporaryDirectory(prefix='padua-g1-independent-fit-synthetic-') as directory:
        root = pathlib.Path(directory)
        manifest = dict(schema='g1-fit-input-v1', frozen_source_sha256=FROZEN,
                        source_metric='PD-T137 aggregate all-source spectral normal output',
                        tie_convention='X wins exact ties', cases=[])
        for grid in ('triangle', 'rotated'):
            for rule in ('bj', 'mirror', 'alt', 'pivot'):
                rows = []
                choices = []
                for t in range(1, 21):
                    for j in range(t+1):
                        x = j == 0 or (j != t and ((rule == 'mirror')
                            or (rule == 'alt' and 2*j < t) or rule == 'pivot'))
                        choices.append('X' if x else 'Y')
                    if t < 2:
                        continue
                    n = (t+1)*(t+2)//2
                    rows.append(dict(set=grid, rule=rule, degree=t, sources='all',
                                     source_count=n-1, basis_count=n,
                                     point_count=325 if grid == 'triangle' else 625,
                                     pivot_choices=choices[:],
                                     pivot_ties=[[2, 1]] if rule == 'pivot' and grid == 'rotated' else [],
                                     normal_trace_exact=str((325 if grid == 'triangle' else 625)-n),
                                     **{field: {'exact': '1'} for field in FIELDS}))
                case = dict(grid=grid, rule=rule)
                for name in ('endpoints', 'independent_endpoints'):
                    path = root/f'{grid}-{rule}-{name}.json'
                    path.write_text(json.dumps({'runs': rows}))
                    case[name] = identity(path)
                path = root/f'{grid}-{rule}-acceptance.json'
                path.write_text(json.dumps(dict(status='PASS explicitly synthetic fixture',
                                                 hashes=[case['endpoints']['sha256'],
                                                         case['independent_endpoints']['sha256']])))
                case['acceptance_receipt'] = identity(path)
                manifest['cases'].append(case)
        guarded = load_manifest(manifest)
        need(sum(map(len, guarded.values())) == 152, 'synthetic full-scope guard')
        controls.append('accepted full explicitly synthetic152-row manifest without logarithms')
        bad = copy.deepcopy(manifest);bad['cases'].pop()
        rejects('missing case before logs', lambda: load_manifest(bad))
        bad = copy.deepcopy(manifest);bad['frozen_source_sha256'] = '0'*64
        rejects('wrong frozen source before logs', lambda: load_manifest(bad))
        bad = copy.deepcopy(manifest);bad['cases'][0]['endpoints']['sha256'] = '0'*64
        rejects('incorrect artifact hash before logs', lambda: load_manifest(bad))
        base = guarded['rotated', 'pivot'][0]
        for label, change in [
            ('omitted source', lambda r: r.update(source_count=4)),
            ('wrong node family cardinality', lambda r: r.update(point_count=624)),
            ('wrong exact upper minimum', lambda r: r['upper_squared'].update(exact='2')),
            ('Y tie choice', lambda r: r['pivot_choices'].__setitem__(3, 'Y')),
            ('missing frozen tie', lambda r: r.update(pivot_ties=[]))]:
            bad = copy.deepcopy(base);change(bad)
            rejects(label, lambda bad=bad: validate_row(bad, 'rotated', 'pivot'))
    return dict(status='PASS synthetic independent fit arithmetic controls', controls=controls,
                actual_G1_inputs_used=False,
                code_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest())


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--self-test', action='store_true')
    ap.add_argument('--manifest')
    ap.add_argument('--report')
    ap.add_argument('--receipt')
    args = ap.parse_args()
    if args.self_test:
        need(not any((args.manifest, args.report, args.receipt)), 'mixed synthetic/actual invocation')
        print(json.dumps(self_test(), indent=2))
    else:
        need(all((args.manifest, args.report, args.receipt)), 'manifest/report/receipt all required')
        manifest = json.loads(pathlib.Path(args.manifest).read_text())
        report = json.loads(pathlib.Path(args.report).read_text())
        result = verify_report(manifest, report)
        receipt = dict(status='PASS independent SYNTHETIC report verification; REAL G1 NOT RUN'
                       if manifest.get('synthetic_only') else
                       'PASS independent complete G1 descriptive report/certificate verification',
                       synthetic_only=bool(manifest.get('synthetic_only')),
                       checker=identity(__file__), manifest=identity(args.manifest), report=identity(args.report),
                       grids=result, command=[sys.executable, '-B', str(pathlib.Path(__file__).resolve()), *sys.argv[1:]],
                       scope='Finite descriptive fits and unchanged operational certificates only; no asymptotic claim.')
        output = pathlib.Path(args.receipt)
        need(not output.exists(), 'refusing to overwrite receipt')
        output.write_text(json.dumps(receipt, indent=2)+'\n')
        print(json.dumps(receipt, indent=2))
