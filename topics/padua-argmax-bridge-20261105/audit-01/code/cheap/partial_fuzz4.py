import ctypes, random, sys, time
lib=ctypes.CDLL(sys.argv[1]); random.seed(5)
D=ctypes.POINTER(ctypes.c_double)
lib.c06_partial.argtypes=[ctypes.c_long,ctypes.c_long,ctypes.c_char_p,D]
lib.c06_compare.argtypes=[ctypes.c_long,ctypes.c_long,ctypes.c_char_p,D]
bad=tot=0; ptbad=0
for it in range(600):
    n=random.choice([2,3,17,32,33,100,512,1000,2048,4096]); q=random.randint(1,n); room=n-q+1
    mode=random.random()
    if mode<0.3: y=random.choice([1e-6,1e-3,0.01,0.3])*room
    elif mode<0.6: y=room*(1-random.choice([1e-6,1e-3,0.01,0.3]))
    else: y=random.uniform(0,room)
    rad=random.choice([0,0,1e-12,1e-6,1e-3])*min(y,room-y)
    s=('[%r +/- %r]'%(y,rad) if rad>0 else repr(y)).encode()
    o=(ctypes.c_double*3)(); assert lib.c06_partial(n,q,s,o)==0; lo,hi=o[0],o[1]
    # point references at the ball ends and middle
    from fractions import Fraction as Fr
    for yy in [t for t in ([y-rad*0.49,y,y+rad*0.49] if rad>0 else [y]) if abs(Fr(t)-Fr(y))<=Fr(rad)/2 and (rad==0 or rad>1e-10*abs(y))]:
        r=(ctypes.c_double*3)(); assert lib.c06_compare(n,q,repr(yy).encode(),r)==0
        r2=(ctypes.c_double*3)(); lib.c06_partial(n,q,repr(yy).encode(),r2)
        tot+=1
        if r[1]!=1: ptbad+=1; print('POINT NOT CONTAINED',n,q,yy)
        # point partial must lie in ball partial
        if not (lo<=r2[0] and r2[1]<=hi): bad+=1; print('BALL MISSES POINT',n,q,s,yy,(lo,hi),(r2[0],r2[1]))
print('tot',tot,'pointbad',ptbad,'ballbad',bad)
