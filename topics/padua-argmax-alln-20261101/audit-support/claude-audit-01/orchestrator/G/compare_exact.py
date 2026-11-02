import json,sys,math
IGN={'seconds','runtime_seconds','elapsed','wall_seconds','cpu_seconds','python','numpy','scipy','platform','argv','time','timestamp','command','environment','started','finished','runtime'}
def leaves(x,p=''):
    if isinstance(x,dict):
        for k,v in x.items():
            if k in IGN: continue
            yield from leaves(v,p+'/'+k)
    elif isinstance(x,list):
        for i,v in enumerate(x): yield from leaves(v,p+f'[{i}]')
    else: yield p,x
def cmp(a,b):
    A=dict(leaves(a));B=dict(leaves(b))
    keys=set(A)|set(B); miss=[k for k in keys if (k in A)!=(k in B)]
    diff=[k for k in keys if k in A and k in B and A[k]!=B[k] and not (isinstance(A[k],float) and isinstance(B[k],float) and abs(A[k]-B[k])<=0)]
    return len(A),len(B),miss,diff
a=json.load(open(sys.argv[1]));b=json.load(open(sys.argv[2]))
na,nb,miss,diff=cmp(a,b)
print(sys.argv[1].split('/')[-1],'leaves',na,nb,'onlyone',len(miss),miss[:5],'diff',len(diff),diff[:5])
