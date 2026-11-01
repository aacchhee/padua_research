from fractions import Fraction as F
import sys
sys.path.insert(0,'/home/claude/audit-scripts')
from claude_mz2d_audit_extra import hint, fold, q
ok=True; cnt=0
for m in range(3,13):
    n=m-1
    B=[(a,d-a) for d in range(n+1) for a in range(d,-1,-1)]
    pres=0 if m%2==0 else 1; sec=1-pres
    for (i,j) in B:
        for (k,l) in B:
            ab=(i,j); cd=(k,l)
            if ab[pres]%2!=cd[pres]%2: continue
            if ab[sec]%2==cd[sec]%2: continue
            H=sum(hint(u)*hint(v) for u in (i+k,abs(i-k)) for v in (j+l,abs(j-l)))/4
            R=sum(q(m,u,v) for u in (i+k,abs(i-k)) for v in (j+l,abs(j-l)))/4
            C3=-sum((hint(m-fold(u,m))*hint(m+1-fold(v,m+1)) if fold(u,m)+fold(v,m+1)>m else F(0)) for u in (i+k,abs(i-k)) for v in (j+l,abs(j-l)))/4
            ok &= (H==0) and (2*H-R==C3); cnt+=1
print('PD-T110 eq(2)-(3) mixed block check m=3..12:',ok,cnt,'pairs')
