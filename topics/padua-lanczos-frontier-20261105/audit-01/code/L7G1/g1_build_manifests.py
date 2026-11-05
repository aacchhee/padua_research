# Builds (1) a T24-only manifest from regenerated real rows (entry guard must refuse: 4 cases),
# (2) a HYBRID code-path test manifest: real T24 rows (producer rows reused as the 'independent' file; acceptance
# receipts are auditor-made TEST stubs) + synthetic rotated rows. Not evidence of independent row matching.
import sys, json, pathlib, hashlib, shutil
G1OUT=pathlib.Path(sys.argv[1]); W=pathlib.Path(sys.argv[2]); syn=pathlib.Path(sys.argv[3])
def ident(p): p=pathlib.Path(p); b=p.read_bytes(); return {'path':str(p.resolve()),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}
base={'schema':'g1-fit-input-v1','source_metric':'PD-T137 aggregate all-source spectral normal output','tie_convention':'X wins exact ties','frozen_source_sha256':'19ce7b774e5a6fa56108eebca3b2ef81f5237328e518d95225adf9f8835e060f'}
tri=[]
for r in ['bj','mirror','alt','pivot']:
    pp=G1OUT/f'full-{r}'/'endpoints.json'
    rows=json.loads(pp.read_text())['runs']; ip=W/f'triangle-{r}-indep-copy.jsonl'; ip.write_text('\n'.join(json.dumps(x) for x in rows)+'\n')
    rp=W/f'triangle-{r}-TEST-acceptance.json'; rp.write_text(json.dumps({'status':'PASS AUDITOR CODE-PATH TEST STUB ONLY','producer_endpoints':ident(pp),'native_endpoints':ident(ip)}))
    tri.append({'grid':'triangle','rule':r,'endpoints':ident(pp),'independent_endpoints':ident(ip),'acceptance_receipt':ident(rp)})
(W/'manifest-t24-only.json').write_text(json.dumps({**base,'cases':tri}))
sm=json.loads((syn/'manifest.json').read_text()); rot=[c for c in sm['cases'] if c['grid']=='rotated']
(W/'manifest-hybrid-TEST.json').write_text(json.dumps({**base,'cases':tri+rot,'auditor_test_only':True}))
print('ok', len(tri), len(rot))
