# Auditor B: compare auditor rerun JSONs with the committed 61-row D1 table and exact small-N values
import json, re, sys
from fractions import Fraction as Fr
import mpmath as mp
mp.mp.dps=320
import os
B = os.environ.get('AUDIT_OUT', os.path.dirname(os.path.abspath(__file__)))  # auditor output directory
prec=sys.argv[1] if len(sys.argv)>1 else '260'
d1=open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../../')+'topics/nn-mop-stability-20261105/attempts/D1.md').read()
tab={}
for m in re.finditer(r'^\| (\d+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$',d1,re.M):
    if m.group(1).isdigit(): tab[int(m.group(1))]=[m.group(i).strip() for i in range(2,6)]
assert sorted(tab)==list(range(4,65)), sorted(tab)
runs={f:json.load(open(f'{B}/runs/conditioning-full-{f}{prec}.json')) for f in ('krawtchouk','hahn')}
for f,d in runs.items():
    assert [r['N'] for r in d['cases']]==list(range(4,65))
    print(f, 'python',d['python'],'mpmath',d['mpmath'],'code',d['code_sha256'][:12],'baseline',d['baseline_sha256'][:12])
mism=0; worst=0
for i,N in enumerate(range(4,65)):
    k,h=runs['krawtchouk']['cases'][i],runs['hahn']['cases'][i]
    mine=[k['NN']['mixed']['kappa'],h['NN']['mixed']['kappa'],k['step_line']['mixed']['kappa'],h['step_line']['mixed']['kappa']]
    for a,b in zip(mine,tab[N]):
        s=mp.nstr(mp.mpf(a),7)
        rel=abs(mp.mpf(a)/mp.mpf(b)-1); worst=max(worst,rel)
        if s!=b and mp.mpf(s)!=mp.mpf(b):
            mism+=1; print('MISMATCH',N,s,b)
print(prec,'dps: 7-digit string mismatches vs committed table:',mism,'of',4*61,'; max rel dev of full value from 7-digit cell:',mp.nstr(worst,4))
ex={ (r['family'],r['N']):r for r in json.load(open(B+'/exact3to8.json'))}
w=0
for i,N in enumerate(range(4,9)):
    for f in ('krawtchouk','hahn'):
        r=runs[f]['cases'][i]
        for tgt,key in (('NN','NN'),('SL','step_line')):
            for model in ('mixed','componentwise','blocknorm'):
                e=Fr(ex[(f,N)][tgt][model]['kappa']); e=mp.mpf(e.numerator)/e.denominator
                w=max(w,abs(mp.mpf(r[key][model]['kappa'])-e)/e)
print(prec,'dps vs auditor exact Fraction kappa (N4-8, 2 fam, 2 targets, 3 models = 60 values): max rel diff',mp.nstr(w,5))
mc=[(f,runs[f]['cases'][0].get('moment_check')) for f in runs]; print('N4 moment_check',mc)
