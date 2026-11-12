import json,sys
D,S=sys.argv[1],sys.argv[2]
rec=json.load(open(S+'/evidence/fd4-lee.json'))
def formula(q): return sum(d*(q//a//d)**2 for a in range(1,q+1) if q%a==0 for d in range(1,q//a+1) if (q//a)%d==0)
ok=True
for n,lo,hi in [(4,88,92),(5,170,178),(6,292,304),(7,462,486)]:
    Q=[];H=[];folds=set()
    for line in open(f'{D}/lee_n{n}.txt'):
        t=line.split()
        if t[0]=='Q': Q.append([int(t[1]),int(t[2]),int(t[3])])
        elif t[0]=='H': H.append([int(x) for x in t[2:8]]); folds.add(t[9])
    assert [q[0] for q in Q]==list(range(lo,hi+1))
    assert all(q[1]==formula(q[0]) for q in Q)
    for r in rec['rows']:
        if r['n']!=n: continue
        same = r['per_q']==Q and sorted(r['hnfs'])==sorted(H) and r['min_det']==hi and r['minimizers']==len(H)
        print(n,r['implementation'],'per_q/hnfs match:',same,'fold',folds,r['fold_histogram'],'total',sum(q[1] for q in Q))
        ok&=same
    ok&= all(q[2]==0 for q in Q[:-1]) and Q[-1][2]>0
print('ALL_MATCH' if ok else 'MISMATCH')
