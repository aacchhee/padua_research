import ctypes, random, sys, time
from fractions import Fraction as Fr
lib=ctypes.CDLL(sys.argv[1]); random.seed(int(sys.argv[2])); NB=int(sys.argv[3])
D=ctypes.POINTER(ctypes.c_double); L=ctypes.POINTER(ctypes.c_long); cs=ctypes.c_char_p
lib.c12_box.argtypes=[ctypes.c_long,cs,cs,cs,cs,D,L]
lib.c15_global.argtypes=[ctypes.c_long,cs,cs,cs,cs,D,L]
lib.c15_fault_probe.argtypes=[ctypes.c_long,cs,cs,cs,cs,ctypes.c_long,ctypes.c_long,D,L]
lib.c12_reference.argtypes=[ctypes.c_long,cs,cs,D]
def s(q): return str(q).encode()
def ref(n,a,b):
    o=(ctypes.c_double*2)(); assert lib.c12_reference(n,s(a),s(b),o)==0; return o[0],o[1]
bad=0; stats=dict(boxes=0,c12fail=0,c15fail=0,pts=0,fb12=0,fb15=0,probe=0,probebad=0)
ratios=[]
t0=time.process_time()
for it in range(NB):
    n=random.choice([2,3,4,5,7,8,11,12,16,17,20,24,31,32])
    kind=random.random(); den=random.choice([64,256,1024,4096,2**20])
    w=Fr(random.choice([0,1,1,2,4,16]), den*random.choice([1,4,16]))
    wb=Fr(random.choice([0,1,1,2,4,16]), den*random.choice([1,4,16]))
    if kind<0.15: al=Fr(0); bl=Fr(random.randint(0,den),den)
    elif kind<0.3: bl=Fr(0); al=Fr(random.randint(0,den),den)
    elif kind<0.45:
        al=Fr(random.randint(0,den),den); bl=1-al-wb-w
    else:
        al=Fr(random.randint(0,den),den); bl=Fr(random.randint(0,den),den)*(1-al)
    if bl<0: bl=Fr(0)
    ah=al+w; bh=bl+wb
    if ah+bh>1:
        continue
    stats['boxes']+=1
    o12=(ctypes.c_double*4)(); c12=(ctypes.c_long*10)()
    o15=(ctypes.c_double*5)(); c15=(ctypes.c_long*12)()
    e12=lib.c12_box(n,s(al),s(ah),s(bl),s(bh),o12,c12)
    e15=lib.c15_global(n,s(al),s(ah),s(bl),s(bh),o15,c15)
    if e12: stats['c12fail']+=1
    if e15: stats['c15fail']+=1
    if not e12: stats['fb12']+=c12[4]
    if not e15: stats['fb15']+=c15[4]
    pts=[(al,bl),(al,bh),(ah,bl),(ah,bh),((al+ah)/2,(bl+bh)/2)]
    for _ in range(6): pts.append((al+(ah-al)*Fr(random.randint(0,1000),1000), bl+(bh-bl)*Fr(random.randint(0,1000),1000)))
    mx=0
    for a,b in pts:
        lo,hi=ref(n,a,b); stats['pts']+=1; mx=max(mx,hi)
        if not e12 and not lo<=o12[0]: bad+=1; print('C12 VIOLATION',n,al,ah,bl,bh,a,b,lo,o12[0])
        if not e15 and not lo<=o15[0]: bad+=1; print('C15 VIOLATION',n,al,ah,bl,bh,a,b,lo,o15[0])
    if not e12 and not e15: ratios.append((o12[0]-mx, o15[0]-mx, n, float(w+wb)))
    # rollback probe on a random ordinary row/vertex
    if not e15 and random.random()<0.3 and n>=3:
        m=n+1; row=random.choice([r for r in range(2*m) if r not in (0,2*m-1,m-1,m)]); vtx=random.randrange(c15[10])
        op=(ctypes.c_double*5)(); cp=(ctypes.c_long*12)()
        ep=lib.c15_fault_probe(n,s(al),s(ah),s(bl),s(bh),row,vtx,op,cp); stats['probe']+=1
        # forced failure must charge a full row cap n*N (normalized: n) and drop nothing else
        if ep or cp[0]<1 or op[0] < o15[0] or op[0] < mx or op[0] < n*0.999:  # rowcap/N = n
            stats['probebad']+=1; print('PROBE',ep,cp[0],op[0],o15[0],n)
print(stats,'bad',bad,'cpu',time.process_time()-t0)
import statistics
if ratios:
    print('C12 excess over sampled max: median %.3g max %.3g; C15 median %.3g max %.3g'%(statistics.median(r[0] for r in ratios),max(r[0] for r in ratios),statistics.median(r[1] for r in ratios),max(r[1] for r in ratios)))
    print('C15<=C12 fraction', sum(r[1]<=r[0] for r in ratios)/len(ratios))
