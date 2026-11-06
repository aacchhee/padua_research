import json, hashlib, sys
from fractions import Fraction as Q
import flint
sys.set_int_max_str_digits(10**6)
flint.ctx.prec = 300
# args: workdir endpoint_table
wd, table = sys.argv[1], sys.argv[2]
tab = json.load(open(table))
prov = {(p['backend'], p['rule']): p['scientific_rows_sha256'] for p in tab['case_provenance']}
rows = {}
for b in ('producer', 'checker'):
    for r in ('bj', 'mirror', 'alt', 'pivot'):
        try:
            vals = [json.loads(x) for x in open(f'{wd}/{b}-{r}.jsonl')]
        except FileNotFoundError:
            continue
        sci = [{k: v for k, v in row.items() if k != 'elapsed_seconds'} for row in vals]
        d = hashlib.sha256(json.dumps(sci, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
        print(b, r, len(vals), 'digest match' if prov.get((b, r)) == d else f'DIGEST MISMATCH {d} vs {prov.get((b,r))}')
        rows[b, r] = {row['degree']: row for row in vals}
# compare producer/checker
for r in ('bj', 'mirror', 'alt', 'pivot'):
    if ('producer', r) in rows and ('checker', r) in rows:
        for dg in rows['producer', r]:
            a = {k: v for k, v in rows['producer', r][dg].items() if k != 'elapsed_seconds'}
            c = {k: v for k, v in rows['checker', r][dg].items() if k != 'elapsed_seconds'}
            assert a == c, (r, dg)
        print('producer==checker', r)
# independent log enclosure with arb: log(q)/2 ; check table [lo,hi] contains it
scale = tab['scale']; bad = 0; n = 0
src = 'producer'
for deg, rule, lL, uL, lU, uU in tab['rows']:
    key = (src, rule) if (src, rule) in rows else ('checker', rule)
    if key not in rows or deg not in rows[key]:
        continue
    row = rows[key][deg]
    for field, lo, hi in (('Knode_squared', lL, uL), ('upper_squared', lU, uU)):
        q = Q(row[field]['exact'])
        v = (flint.arb(q.numerator).log() - flint.arb(q.denominator).log()) / 2
        a = flint.arb(lo) / scale; bb = flint.arb(hi) / scale
        ok = (a <= v) and (v <= bb)   # arb comparisons are certified
        # tightness: floor/ceil
        tight = (flint.arb(lo + 1) / scale > v) and (flint.arb(hi - 1) / scale < v)
        n += 1
        if not (ok and tight):
            bad += 1; print('ENCLOSURE PROBLEM', deg, rule, field, ok, tight)
print('enclosures checked', n, 'bad', bad)
