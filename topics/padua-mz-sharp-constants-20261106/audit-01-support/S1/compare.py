"""S1 audit: trial quotient vs measured lambda_min at every registered N."""
import json, sys
t = json.load(open(sys.argv[1])); m = {r[0]: r[1] for r in json.load(open(sys.argv[2]))['rows']}
for run in t['runs']:
    ratios = [(r['N'], r['quotient'] / m[r['N']]) for r in run['rows'] if r['N'] in m]
    print(run['f'], 'n=', len(ratios), 'min trial/lambda_min =', min(ratios, key=lambda x: x[1]), 'all >=1:', all(x[1] >= 1 for x in ratios))
