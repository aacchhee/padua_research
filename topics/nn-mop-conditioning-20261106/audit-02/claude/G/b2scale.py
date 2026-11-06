import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from gauge_exact import Num, inputs, nn_triangle
R = Num('fr')
ind = {(r['family'], r['N']): r for r in json.load(open(sys.argv[1]))['rows']}
mine = {}
for f in sys.argv[2:]:
    for line in open(f):
        r = json.loads(line)
        for c in r['cases']:
            mine[(r['family'], r['N'], c['model'], c['fixed_mass'])] = c
for fam, Ns in (('hahn', range(2, 15)), ('krawtchouk', (2, 4, 6))):
    for N in Ns:
        z, w = inputs(fam, N - 1)
        P, fields, _ = nn_triangle(z, w, R)
        sb2 = max(abs(v) for k, (v, g) in fields.items() if k[0] == 'b' and k[1] == 2)
        row = ind[(fam, N)]
        ok_scale = str(sb2) == row['b2_scale']
        worst = 0.0
        for model, mass, lower, r1, r2 in row['payload']:
            c = mine[(fam, N, model, mass)]
            assert float(Fr(lower)) <= float(c['kappa_b2']) * (1 + 1e-10), (fam, N, model, mass)
            assert abs(float(Fr(r1)) - float(c['r'][0])) <= 1e-9 * float(Fr(r1)) and abs(float(Fr(r2)) - float(c['r'][1])) <= 1e-9 * float(Fr(r2))
            worst = max(worst, float(Fr(lower)) / float(c['kappa_b2']))
        print(fam, N, 'my ||b2||=', sb2, 'matches codex b2_scale:', ok_scale, 'max(row lower/kappa_b2)=%.6f' % worst)
