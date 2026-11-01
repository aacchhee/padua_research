"""Independent replay of preregistered unshifted fit family on stored data.
No asymptotic error certificate is implied by fitting finite observations.
"""
import pathlib,re,json
import mpmath as mp
root=pathlib.Path(__file__).resolve().parents[1]
vals={}
for fn in ('t2_onepage.out','t2_odd.out'):
    for line in (root/'checks/code/decisive/gen4-2'/fn).read_text().splitlines():
        m=re.match(r'n=(\d+) corner \((-?1), (-?1)\) Lambda_c = ([0-9.]+)',line)
        if m: vals[int(m[1])]=m[4]
mp.mp.dps=70
a=4/mp.pi**2; b=8/mp.pi**2*(mp.euler+mp.log(8/mp.pi))
rows=[]
for K in (3,4,5):
    for nmin in (64,128,256,512):
        ns=[n for n in sorted(vals) if n%2==0 and n>=nmin]
        for fix in (False,True):
            count=(1 if fix else 2)+sum(k+1 for k in range(1,K+1))
            if len(ns)<count+2: continue
            A=[];y=[]
            for n in ns:
                n=mp.mpf(n); L=mp.log(n)
                A.append(([] if fix else [L])+[mp.mpf(1)]+[L**j/n**k for k in range(1,K+1) for j in range(k+1)])
                y.append(mp.mpf(vals[int(n)])-a*L**2-(b*L if fix else 0))
            mat=mp.matrix(A); rhs=mp.matrix(y)
            coef,_=mp.qr_solve(mat,rhs)
            c=coef[0 if fix else 1]
            res=max(abs(x) for x in mat*coef-rhs)
            rows.append(dict(K=K,nmin=nmin,b_fixed=fix,npoints=len(ns),c=str(c),residual=str(res)))
cs=[mp.mpf(r['c']) for r in rows]
summary=dict(fit_count=len(rows),c_min=str(min(cs)),c_max=str(max(cs)),half_spread=str((max(cs)-min(cs))/2),rows=rows)
(root/'audit-support/proposal-fit.json').write_text(json.dumps(summary,indent=2))
print({k:v for k,v in summary.items() if k!='rows'})
