import json, sys
from pathlib import Path
R = Path(sys.argv[1]); reg = json.loads((R/'PREREGISTRATION.json').read_text())
fields = ['S_upper_columns','S_upper_rows','analytic_far','corner','floor','lambda_upper_columns','lambda_upper_rows','n','norm','origin_lower_hex','pi_bracket','tree','verification','format','status','scope']
runs = {}
for f in sorted(R.glob('results-shard*.jsonl')):
    for line in f.read_text().splitlines():
        r = json.loads(line); runs[r['n']] = r
rows = []; bad = []
for c in reg['calls']:
    n = c['n']; r = runs.get(n)
    if r is None: rows.append({'n': n, 'ran': False}); bad.append((n, 'not run')); continue
    row = {'n': n, 'ran': True, 'exit': r['observed_exit'], 'timeout': r['timed_out'], 'cpu': round(r['child_cpu'], 3), 'echild': r['ECHILD_after']}
    why = []
    if r['observed_exit'] != 0 or r['timed_out'] or not r['ECHILD_after']: why.append('exit/timeout/echild')
    out = Path(c['output'])
    try:
        fa = json.loads((out/'final-accounting.json').read_text())
        row['result'] = fa.get('result'); row['first_failure'] = fa.get('first_failure'); row['complete'] = fa.get('complete')
        if fa.get('result') != 'FRESH_RETAINED_PROOF_VERIFY_ACCEPTED_PENDING_RESULT_REVIEW' or fa.get('first_failure') is not None or fa.get('complete') is not True:
            why.append('accounting')
        fresh = json.loads((out/'essential-receipt.json').read_text()); prim = json.loads(Path(c['certificate']).read_text())
        diff = [k for k in fields if fresh.get(k) != prim.get(k)]
        row['field_diffs'] = diff
        if diff: why.append('fields')
    except Exception as e:
        why.append('read:' + repr(e)); row['error'] = repr(e)
    row['ok'] = not why; row['why'] = why
    if why: bad.append((n, why))
    rows.append(row)
ok = sum(1 for r in rows if r.get('ok'))
cpu = sum(r.get('cpu', 0) for r in rows)
summary = {'calls': len(rows), 'ran': sum(1 for r in rows if r['ran']), 'ok': ok, 'bad': bad, 'child_cpu_total': round(cpu, 3)}
(R/'comparison.json').write_text(json.dumps({'summary': summary, 'rows': rows}, indent=1))
print(json.dumps(summary))
