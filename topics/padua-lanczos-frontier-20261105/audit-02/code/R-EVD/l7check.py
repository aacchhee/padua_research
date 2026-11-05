import json,re,sys,ast
D=sys.argv[1]
L=json.load(open(D+'/evidence/l7-full-loss-list.json'))
S=json.load(open(D+'/evidence/l7-suite-summary.json'))
rows=L['losses']; print('rows',len(rows),L['loss_count'])
keys=[(r['domain'],r['seed'],r['degree'],r['target'],r['method'],r['distribution']) for r in rows]
print('unique',len(set(keys)))
# summary truncated rows: exact equality prefix
sl=S['accepted_reference_resolved_losses']; print('summary rows',len(sl), all(sl[i]==rows[i] for i in range(len(sl))) if len(sl)<=len(rows) else 'longer')
# by method/distribution
from collections import Counter
c=Counter(f"{r['method']} / {r['distribution']}" for r in rows); print('bymd match', dict(c)==S['resolved_losses_by_method_distribution'])
# audit compare
txt=open(D+'/audit-01/code/L7G1/compare-l7run_haswell.txt').read()
aud=[]
for m in re.finditer(r"^  (\('triangle'.*?\)) err (\S+) ref (\S+) diff (\S+)$",txt,re.M):
    aud.append((ast.literal_eval(m.group(1)),float(m.group(2)),float(m.group(3)),float(m.group(4))))
print('audit rows',len(aud))
ok=True
for (k,e,rf,df),r,kk in zip(aud,rows,keys):
    if k!=kk: ok=False;print('keymismatch',k,kk)
    for a,b in ((e,r['error']),(rf,r['reference_error']),(df,r['prediction_difference'])):
        if float(f"{b:.4e}")!=a: ok=False;print('val',k,a,b)
print('audit order+4sig match',ok, set(k for k,*_ in aud)==set(keys))
# loss rule sanity: resolved loss rule? print min diff/ref ratio
for r in rows[:0]: pass
