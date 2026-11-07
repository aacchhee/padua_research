# Auditor feasibility probe (MEASURED timing; exact integer enumeration): all row-HNF sublattices L of Z^3
# with det in [dlo,dhi] and min l1 >= 2n. HNF rows (a,b,c),(0,d,e),(0,0,f), 0<=b<d, 0<=c,e<f.
import sys, time, itertools, numpy as np
n=int(sys.argv[1]); dlo=int(sys.argv[2]); dhi=int(sys.argv[3]); R=2*n-1
t0=time.process_time(); tested=0; hits=[]
def short_exists(a,b,c,d,e,f):
    # any nonzero (x,y,z) in L with |x|+|y|+|z|<=R ?
    for i in range(-(R//a),R//a+1):
        x=i*a; rx=R-abs(x)
        # y=i*b+j*d, |y|<=rx
        jlo=-((rx+i*b)//d) if d else 0
        for j in range((-rx-i*b+d-1)//d if True else 0,(rx-i*b)//d+1):
            y=i*b+j*d; ry=rx-abs(y)
            if ry<0: continue
            base=i*c+j*e
            klo=-((ry+base)//f); khi=(ry-base)//f
            for k in range((-ry-base+f-1)//f,(ry-base)//f+1):
                z=base+k*f
                if abs(z)<=ry and (x or y or z): return True
    return False
for m in range(dlo,dhi+1):
    for a in [x for x in range(1,m+1) if m%x==0]:
        for d in [x for x in range(1,m//a+1) if (m//a)%x==0]:
            f=m//(a*d)
            if f<2*n: continue
            for b in range(d):
                for e in range(f):
                    # 2D sublattice check (0,d,e),(0,0,f) first
                    if short_exists(10**9,0,0,d,e,f): continue
                    for c in range(f):
                        tested+=1
                        if not short_exists(a,b,c,d,e,f): hits.append((m,(a,b,c,d,e,f)))
    if hits and m==hits[0][0]: pass
print({'n':n,'det_range':[dlo,dhi],'tested_full_3d':tested,'lattices_with_min>=2n':len(hits),'first':hits[:3],'min_det_found':min([h[0] for h in hits]) if hits else None,'cpu_seconds':round(time.process_time()-t0,2)})
