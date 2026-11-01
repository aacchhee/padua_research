# Bartels-Jezioranski ordering (n variables): row r ranges; parent j' = mu(j)/x_{k_j}, k_j = first var with exp>0.
# Window of possibly nonzero alpha_{j,l}: l from j'' to j-1 (Thm 1), minus Cor.4 zeros (k_j<k_j': l in row of j'' from j'' to end of that row).
import itertools
def table(nv, deg):
    rows=[[tuple([0]*nv)]]
    for r in range(1,deg+1):
        row=[]
        for k in range(nv):
            prev=[m for m in rows[-1] if all(e==0 for e in m[:k])] if r>1 else []
            if r==1: row.append(tuple(1 if t==k else 0 for t in range(nv))); continue
            for m in prev:
                mm=list(m); mm[k]+=1; row.append(tuple(mm))
        rows.append(row)
    flat=[m for row in rows for m in row]; return rows, flat
for nv in (2,3):
    rows, flat = table(nv, 12); pos={m:i for i,m in enumerate(flat)}; rowof={m:r for r,row in enumerate(rows) for m in row}
    out=[]
    for r in range(2,13):
        lens=[]
        for m in rows[r]:
            j=pos[m]; k=next(t for t in range(nv) if m[t]>0); mp=list(m); mp[k]-=1; jp=pos[tuple(mp)]
            mpp=tuple(mp); kp=next(t for t in range(nv) if mpp[t]>0); mq=list(mpp); mq[kp]-=1; jpp=pos[tuple(mq)]
            L=set(range(jpp,j))
            if k<kp: L-= {pos[q] for q in rows[rowof[tuple(mq)]] if pos[q]>=jpp}
            lens.append(len(L))
        out.append((r,max(lens)))
    print(nv,"vars: (degree, max #nonzero alpha) =",out)
