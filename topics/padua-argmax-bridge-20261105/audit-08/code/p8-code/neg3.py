import sys, re, json
from pathlib import Path
sys.argv = [sys.argv[0], sys.argv[1], sys.argv[2]]
src = open(sys.argv[0].replace('neg3.py', 'negatives.py')).read()
exec(src.split('# ---- previous')[0])
for t in ('paper', 'companion'):
    d = fresh('M20' + t); p = d / f'analytic/tables/{t}.tex'; s = p.read_text()
    i = s.index(r'\label{uc:base-values}'); j = s.index(r'\begin{tabular}', i)
    m = re.compile(r'\$\[(-?\d+\.\d{6}),').search(s, j); old = m.group(1); new = old[:-1] + str((int(old[-1]) + 9) % 10)
    p.write_text(s[:m.start(1)] + new + s[m.end(1):]); refresh(d)
    run(f'M20 {t} labeled base-values lower endpoint {old}->{new}, refreshed, integrity', d, [], 'accept')
    run(f'M20b {t} same, --analytic', d, ['--analytic'], 'reject')
for j in jobs:
    r = execute(j); results.append(r); print(json.dumps(r))
json.dump(results, open(work / 'neg3.json', 'w'), indent=1)
