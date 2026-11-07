#!/usr/bin/env python3
"""Auditor: complete row-HNF search of all integer lattices of a given determinant q with
min nonzero l1 >= 2n. Vectorised over (b,c,e) for each diagonal (a,d,f) and each (u,v):
lattice vector = (a u, b u + d v, c u + e v + f w); its best w gives third |.| = dist(cu+ev, fZ).
Combined with the packing bound det >= 38 n^3/27 (Minkowski / Betke-Henk, LITERATURE), searching
q in [ceil(38n^3/27), seed-1] decides the global minimum determinant."""
import sys, json, math, time
import numpy as np
def triples(q):
    for a in range(1,q+1):
        if q%a: continue
        for d in range(1,q//a+1):
            if (q//a)%d: continue
            yield a,d,q//(a*d)
def admissible(n,q):
    R=2*n; found=[]; tested=0
    for a,d,f in triples(q):
        if f<R: continue_flag=True
        b=np.arange(d)[:,None,None]; c=np.arange(f)[None,:,None]; e=np.arange(f)[None,None,:]
        ok=np.ones((d,f,f),dtype=bool); tested+=d*f*f
        if f<R: continue          # (0,0,f) itself is too short
        umax=(R-1)//a
        for u in range(-umax,umax+1):
            ru=R-abs(a*u)
            vmax=(ru-1+(d-1)*abs(u))//d+1
            for v in range(-vmax,vmax+1):
                if u==0 and v<=0: continue   # symmetry k ~ -k; (0,0) handled
                s=np.abs(b*u+d*v)            # shape (d,1,1)
                r=ru-s                       # remaining budget for third coord
                if (r<=0).all(): continue
                t=(c*u+e*v)%f; dist=np.minimum(t,f-t)
                ok&=~((r>0)&(dist<r))
        idx=np.argwhere(ok)
        for bi,ci,ei in idx: found.append((a,int(bi),int(ci),d,int(ei),f))
    return found,tested
if __name__=='__main__':
    seeds={1:2,2:12,3:38,4:92,5:178,6:304,7:486,8:724,9:1026,10:1412,11:1878,12:2432,13:3098,14:3868,15:4750,16:5792}
    out=[]
    mode=sys.argv[2]
    for n in map(int,sys.argv[3:]):
        t=time.time()
        lo=math.ceil(38*n**3/27) if mode=='window' else 1
        res={'n':n,'packing_lower':lo,'seed_det':seeds[n],'per_q':[]}
        for q in range(lo,seeds[n]+1):
            good,tested=admissible(n,q)
            res['per_q'].append([q,tested,len(good)])
            if good:
                res['min_det']=q; res['minimizers']=len(good); res['example']=good[0]; break
        res['seconds']=round(time.time()-t,1); print(res,flush=True); out.append(res)
    json.dump(out,open(sys.argv[1],'w'))
