import json,collections,sys,math
S='./out/'
def load(fn):
    qs={};small=[];mins=[];summ=None
    for l in open(fn):
        r=json.loads(l)
        if r['type']=='q':qs[r['q']]=r
        elif r['type']=='small':small.append(r)
        elif r['type']=='minimizer':mins.append(r)
        elif r['type']=='summary':summ=r
    return qs,small,mins,summ
def sub(fn,qmax,cap):
    qs,small,mins,summ=load(fn)
    sel=[r for r in small if r['q']<=qmax and r['fold']<=cap]
    return dict(hnf=sum(qs[q]['hnf_total'] for q in qs if q<=qmax),adm=sum(qs[q]['admissible'] for q in qs if q<=qmax),
                foldhist=sorted(collections.Counter(r['fold'] for r in sel).items()),
                minfold=min((r['fold'] for r in sel),default=None),
                minfold_q=sorted(set(r['q'] for r in sel if r['fold']==min(x['fold'] for x in sel))) if sel else None,
                first_adm_q=min((q for q in qs if qs[q]['admissible']>0),default=None), complete=summ is not None)
if __name__=='__main__':
    for n,qa,ca,scopes in [(1,32,4,[(32,4)]),(2,80,10,[(80,10)]),(3,184,23,[(160,20),(184,23)]),(4,352,44,[(280,35),(352,44)])]:
        fn=S+f'mine-fold/fold-n{n}-q{qa}-c{ca}.jsonl'
        for qm,c in scopes: print(n,qm,c,sub(fn,qm,c))
