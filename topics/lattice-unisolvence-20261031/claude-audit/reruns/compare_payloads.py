import json,sys,math
VOL={'argv','command','elapsed','elapsed_seconds','timing','generated_at','timestamp','output','output_path','cwd','runtime_seconds','wall_seconds','python','platform','hostname','seconds','started','finished','environment','python_version'}
diffs=[]
def cmp(a,b,p):
    if isinstance(a,dict) and isinstance(b,dict):
        for k in set(a)|set(b):
            if k in VOL: continue
            if k not in a or k not in b: diffs.append((p+'/'+k,'missing')); continue
            cmp(a[k],b[k],p+'/'+k)
    elif isinstance(a,list) and isinstance(b,list):
        if len(a)!=len(b): diffs.append((p,'len %d vs %d'%(len(a),len(b)))); return
        for i,(x,y) in enumerate(zip(a,b)): cmp(x,y,p+'[%d]'%i)
    elif isinstance(a,float) or isinstance(b,float):
        try:
            if not (a==b or abs(a-b)<=1e-9*max(1,abs(a),abs(b))): diffs.append((p,a,b))
        except TypeError: diffs.append((p,a,b))
    else:
        if a!=b: diffs.append((p,str(a)[:80],str(b)[:80]))
D='topics/lattice-unisolvence-20261031/directions'
pairs=[('c0/catalogue.json',D+'/C0/catalogue.json'),('c0/count-result.json',D+'/C0/count-result.json'),('c0/count-trials.json',D+'/C0/count-trials.json'),
('ranks.json',D+'/C3/ranks.json'),('structure.json',D+'/C3/structure.json'),('obstructions.json',D+'/C3/obstructions.json'),('lowdegree.json',D+'/C3/lowdegree.json'),('lebesgue.json',D+'/C3/lebesgue.json'),
('mod4.json',D+'/C1/results.json'),('stability.json',D+'/C1/stability.json'),('symbolic.json',D+'/C1/symbolic.json'),('gram.json',D+'/C1/gram.json'),('extension.json',D+'/C1/extension.json')]
for mine,ref in pairs:
    diffs=[]
    cmp(json.load(open('/tmp/lattice-claude/'+mine)),json.load(open(ref)),'')
    print(f"{mine:22s} diffs={len(diffs)}", diffs[:6])
