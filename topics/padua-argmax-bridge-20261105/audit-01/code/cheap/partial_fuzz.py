import ctypes, random, sys, time
lib=ctypes.CDLL(sys.argv[1]); random.seed(5)
D=ctypes.POINTER(ctypes.c_double)
lib.c06_compare.argtypes=[ctypes.c_long,ctypes.c_long,ctypes.c_char_p,D]
bad=fail=tot=0; t=time.process_time(); maxrad=0
for it in range(600):
    n=random.choice([2,3,17,32,33,100,512,1000,2048,4096]); q=random.randint(1,n)
    room=n-q+1  # need 0<y and y+q-1<n -> y in (0, room)
    mode=random.random()
    if mode<0.3: y=random.choice([1e-6,1e-3,0.01,0.3])*room
    elif mode<0.6: y=room*(1-random.choice([1e-6,1e-3,0.01,0.3]))
    else: y=random.uniform(0,room)
    rad=random.choice([0,0,1e-12,1e-6,1e-3])*min(y,room-y)
    s=('[%r +/- %r]'%(y,rad) if rad>0 else repr(y)).encode()
    o=(ctypes.c_double*3)(); e=lib.c06_compare(n,q,s,o); tot+=1
    if e: fail+=1; continue
    if o[1]!=1: bad+=1; print('NOT CONTAINED',n,q,s,list(o))
    maxrad=max(maxrad,o[2])
print('tot',tot,'native_fail',fail,'bad',bad,'cpu',time.process_time()-t)
