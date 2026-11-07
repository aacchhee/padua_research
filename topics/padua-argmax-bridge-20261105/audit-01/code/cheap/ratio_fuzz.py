import sys, ctypes, random, math
sys.path.insert(0,'pylib'); import mpmath as mp
mp.mp.dps=80
lib=ctypes.CDLL(sys.argv[1]); seed=int(sys.argv[2]); random.seed(seed)
P=ctypes.POINTER(ctypes.c_double)
f=lib.phase_ratio; f.argtypes=[ctypes.c_int,ctypes.c_int,ctypes.c_double,ctypes.c_double,P,ctypes.POINTER(ctypes.c_int)]; f.restype=ctypes.c_int
lib.c03_variant.argtypes=[ctypes.c_int]
def truth(k,turn,off):
    z=mp.pi*turn+mp.mpf(off)
    if off==0:
        e=-1 if (turn%2 and k%2==0) else 1
        return mp.mpf(e*k), mp.mpf(0)
    s,c=mp.sin(z),mp.cos(z); sk,ck=mp.sin(k*z),mp.cos(k*z)
    return sk/s, (k*ck*s-sk*c)/s**2
bad=0; n=0; widths=[0,0,0]
for it in range(int(sys.argv[3])):
    k=random.choice([2,3,4,5,31,32,33,64,127,255,256,512,513,random.randint(2,513)])
    turn=random.randint(-4,4)
    mode=random.random()
    if mode<0.3:   # around pole
        a=random.uniform(-1,1)*random.choice([1e-9,1e-4,0.01,0.1,4/k,1.5]); b=a+random.uniform(0,1)*random.choice([1e-9,1e-4,0.01,0.1,4/k,1.0])
    elif mode<0.5: # near guard edges r=4/k or 1.5
        e=random.choice([4/k,1.5,math.pi/k,3/k]); a=e*(1+random.uniform(-1e-3,1e-3))*random.choice([1,-1]); b=a+abs(random.gauss(0,1e-3))
    elif mode<0.6:
        a=0.0;b=random.choice([1e-12,4/k,1.5])
    else:
        a=random.uniform(-2,2); b=a+random.expovariate(1)*random.choice([1e-6,1e-2,0.3,2])
    lo,hi=min(a,b),max(a,b)
    for v in (0,1,2):
        assert lib.c03_variant(v)==0
        o=(ctypes.c_double*8)(); fl=ctypes.c_int()
        rc=f(k,turn,lo,hi,o,ctypes.byref(fl))
        if rc: print('rc',rc,k,turn,lo,hi,v); bad+=1; continue
        pts=[lo,hi]+[lo+(hi-lo)*random.random() for _ in range(12)]+([0.0] if lo<=0<=hi else [])
        for off in pts:
            if not lo<=off<=hi: continue
            V,D=truth(k,turn,off); n+=1
            if not (mp.mpf(o[0])<=V<=mp.mpf(o[1]) and mp.mpf(o[2])<=D<=mp.mpf(o[3])):
                bad+=1; print('VIOLATION v%d k=%d turn=%d [%r,%r] off=%r V=%s D=%s out=%s'%(v,k,turn,lo,hi,off,mp.nstr(V,17),mp.nstr(D,17),list(o)[:4]))
        widths[v]+=o[1]-o[0]
print('seed',seed,'samples',n,'bad',bad,'sum value widths by variant',widths)
