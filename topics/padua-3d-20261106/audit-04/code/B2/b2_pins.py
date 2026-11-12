"""Auditor B2: compare every repo-relative sha256 pin found in U2 receipts with candidate-tree bytes."""
import json, hashlib, sys, os, re
root = sys.argv[1]; files = sys.argv[2:]
H = re.compile(r'^[0-9a-f]{64}$')
def norm(p):
    p = str(p)
    for pre in ('/workspace/padua_research/',):
        if p.startswith(pre): p = p[len(pre):]
    return p
res = {'match': 0, 'mismatch': [], 'absent_tmp': 0, 'absent_other': []}
def check(path, sha):
    p = norm(path)
    if p.startswith('/tmp') or p.startswith('/'):
        res['absent_tmp'] += 1; return
    f = os.path.join(root, p)
    if not os.path.exists(f):
        res['absent_other'].append(p); return
    h = hashlib.sha256(open(f, 'rb').read()).hexdigest()
    if h == sha: res['match'] += 1
    else: res['mismatch'].append((p, sha[:12], h[:12]))
def walk(x):
    if isinstance(x, dict):
        if 'path' in x and 'sha256' in x and isinstance(x['sha256'], str):
            check(x['path'], x['sha256'])
        for k, v in x.items():
            if isinstance(v, str) and H.match(v) and ('/' in k or k.endswith('.py') or k.endswith('.json')):
                check(k, v)
            walk(v)
    elif isinstance(x, list):
        for v in x: walk(v)
for fn in files:
    before = (res['match'], len(res['mismatch']))
    walk(json.load(open(fn)))
    print(os.path.basename(fn), 'match+', res['match'] - before[0], 'mismatch+', len(res['mismatch']) - before[1])
print(json.dumps(res, indent=0)[:3000])
