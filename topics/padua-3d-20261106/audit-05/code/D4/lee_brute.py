# Independent brute-force check of |DS(n-1)| and its l1 diameter, n=1..12.
import itertools, sys
def ball(r):
    return {v for v in itertools.product(range(-r,r+1),repeat=3) if abs(v[0])+abs(v[1])+abs(v[2])<=r}
ok=True
for n in range(1,13):
    r=n-1; B=ball(r); DS=B|{(x+1,y,z) for (x,y,z) in B}
    card=len(DS); formula=2*n*(2*n*n+1)
    assert formula%3==0; formula//=3
    alt=2*(r+1)+sum(8*s*(r+1-s) for s in range(1,r+1))
    L=list(DS)
    diam=max(abs(a[0]-b[0])+abs(a[1]-b[1])+abs(a[2]-b[2]) for a in L for b in L)
    print(n,card,formula,alt,diam,2*n-1)
    ok&= card==formula==alt and diam==2*n-1
print('ALL_OK' if ok else 'FAIL')
