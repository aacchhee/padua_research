# A4: evaluate T4-03 majorants (1) for M/A/L and (2) for L; compare with recorded sampled values (must be >=)
import json, math, mpmath as mp
mp.mp.dps=50
ev='topics/padua-3d-20261106/evidence/'
B=lambda m: mp.mpf(1) if m==0 else mp.sqrt(2*m*(m+1))
for fam in 'MAL':
    rec=json.load(open(ev+f't4-mesh-{fam}.json'))
    for row in rec['rows']:
        n=row['n']; order=row['height_indices']
        z=[mp.cos(mp.pi*j/n) for j in order]
        om=lambda k,x: mp.fprod(x-z[j] for j in range(k))
        b=[]
        for k in range(n+1):
            b.append(B(n-k)/abs(om(k,z[k]))*(1+mp.fsum(abs(om(i,z[k]))*b[i] for i in range(k))))
        U1=mp.fsum(2**k*b[k] for k in range(n+1))
        # sharper: use actual sup of |omega_k| on [-1,1] instead of 2^k (still rigorous variant, for info)
        line="%s n=%d sampled=%.4f  bound(1)=%.4g"%(fam,n,row['sampled_lebesgue'],float(U1))
        if fam=='L':
            U2=mp.sqrt(2*n)*(mp.fprod(1+B(m) for m in range(n+1))-1)
            line+="  bound(2)=%.4g"%float(U2)
        lowM=math.exp(max(0,row['log_determinant_lower_diagnostic']))
        line+="  detlower=%.4f ok=%s"%(lowM, lowM<=row['sampled_lebesgue']<=float(U1))
        print(line)
