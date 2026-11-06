# Auditor check: single represented impulse gain via complex-step equals ell_hi=(1-P_ii)v_hi (no extra w_i)
import numpy as np, json, sys
sys.argv=[sys.argv[0]]
import finite_capacity_check as fc
res=[]
for kind,n in [("dev_triangle",2),("dev_triangle",3),("randT",3)]:
    for rule in ("BJ","mirror"):
        z,w=fc.family(kind,n); ms,B,alpha,sig2,choice=fc.setup(z,w,n,rule)
        M,Ns=B.shape; d=np.sum(B*B,axis=0); P=(B/np.sqrt(d))@(B/np.sqrt(d)).T; R=np.eye(M)-P
        g=fc.g_responses(z,alpha,choice); J=list(range(1,Ns)); T=fc.derivative_tensor(z,w,choice,J)
        err=0
        for h in J:
            for i in range(M):
                out=np.sqrt(sig2[h])*(R@T[(h,i)])/np.sqrt(d)
                gain2=np.linalg.norm(out,2)**2
                ell=(1-P[i,i])*sig2[h]*sum(g[k,h,i]**2/d[k] for k in range(h,Ns))
                err=max(err,abs(gain2-ell)/max(ell,1e-300))
                # with a spurious extra w_i the formula would be off by factor w_i
        res.append((kind,n,rule,M*len(J),err))
print(json.dumps(res))
