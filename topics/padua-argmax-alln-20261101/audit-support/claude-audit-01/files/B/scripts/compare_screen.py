import gzip, json, hashlib, sys
dev_gz = sys.argv[1]; mine = sys.argv[2]
raw = gzip.open(dev_gz,'rb').read()
print('dev decompressed bytes', len(raw), 'sha256', hashlib.sha256(raw).hexdigest())
A = json.loads(raw); B = json.load(open(mine))
diffs = []; nnum = [0]; noth=[0]
def walk(a, b, path):
    if isinstance(a, dict):
        if not isinstance(b, dict): diffs.append((path,'type')); return
        for k in set(a)|set(b):
            if k not in a or k not in b: diffs.append((path+'/'+k,'missing')); continue
            walk(a[k], b[k], path+'/'+k)
    elif isinstance(a, list):
        if not isinstance(b, list) or len(a)!=len(b): diffs.append((path,'len')); return
        for i,(x,y) in enumerate(zip(a,b)): walk(x,y,path+f'[{i}]')
    else:
        if isinstance(a,(int,float)) and not isinstance(a,bool): nnum[0]+=1
        else: noth[0]+=1
        if a != b: diffs.append((path, a, b))
walk(A,B,'')
print('numeric leaves', nnum[0], 'other leaves', noth[0], 'differing leaves', len(diffs))
import collections
kinds = collections.Counter()
for d in diffs:
    p = d[0]
    key = p.split('/')[-1].split('[')[0]
    kinds[key]+=1
print(kinds)
for d in diffs:
    p=d[0]
    if not any(s in p for s in ('time','seconds','cpu','wall','argv','python','platform','numpy','scipy','version')):
        print('NONTIMING DIFF', d[:3] if len(str(d))<400 else str(d)[:400])
