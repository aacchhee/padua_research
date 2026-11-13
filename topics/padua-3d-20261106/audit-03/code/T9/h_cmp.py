# Compare scientific content of reruns vs committed receipts, ignoring volatile keys.
import json,sys
VOL={'command','versions','cpu_seconds','seconds','scratch','cpu','timings','code_sha256','argv','elapsed','wall_seconds','threads','cpu_seconds_group','cpu_seconds_rank','probe_cpu','group_cpu_seconds','rank_cpu_seconds'}
def strip(x):
    if isinstance(x,dict): return {k:strip(v) for k,v in x.items() if k not in VOL and 'cpu' not in k and 'second' not in k and 'time' not in k}
    if isinstance(x,list): return [strip(v) for v in x]
    if isinstance(x,float): return round(x,9)
    return x
def diff(a,b,path=''):
    out=[]
    if type(a)!=type(b): return [(path,str(a)[:80],str(b)[:80])]
    if isinstance(a,dict):
        for k in set(a)|set(b):
            if k not in a or k not in b: out.append((path+'/'+k,'missing' if k not in a else 'present','missing' if k not in b else 'present'))
            else: out+=diff(a[k],b[k],path+'/'+k)
    elif isinstance(a,list):
        if len(a)!=len(b): return [(path,'len',len(a),len(b))]
        for i,(u,v) in enumerate(zip(a,b)): out+=diff(u,v,f'{path}[{i}]')
    elif a!=b: out.append((path,str(a)[:80],str(b)[:80]))
    return out
for mine,theirs in zip(sys.argv[1::2],sys.argv[2::2]):
    d=diff(strip(json.load(open(mine))),strip(json.load(open(theirs))))
    print(theirs.split('/')[-1],'differences:',len(d)); [print('   ',x) for x in d[:8]]
