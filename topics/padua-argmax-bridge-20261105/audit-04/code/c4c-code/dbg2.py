import numpy as np, sys
exec(open('c4c_rows.py').read().split("Pos = {")[0])
rng=np.random.default_rng(1)
bad=0
for n in (32,33,47,64,160):
  for t in range(300):
    x=rng.uniform(0,np.pi); y=rng.uniform(0,np.pi-x)
    if t%3==0: x=rng.uniform(0,1); y=rng.uniform(0,1-x)
    S=setup(n,x,y); m=S['m']
    for (r,sb) in ((1,1),(1,-1),(2,-1)):
        b=sb*y; idx=actual_row_index(S,r,sb)
        val,_,v=row_vals(S,idx); js,z,F=sinc_row(S,r,b)
        if len(js)!=len(val) or np.max(np.abs(np.sort(F)-np.sort(val/(n*m))))>1e-9:
            bad+=1
            if bad<4: print('MISMATCH n',n,'x',x,'y',y,'chart',r,sb,'len',len(js),len(val))
        if x+y<=1:
            pos=sorted(js[F>0].tolist())
            exp={(1,1):[0],(1,-1):[0],(2,-1):[-1,1]}[(r,sb)]
            if pos!=exp:
                print('POSSET n',n,'x',x,'y',y,'chart',r,sb,'pos',pos, 'F near', [ (j,F[js==j][0]) for j in (-3,-1,0,1,2,3) if j in js])
print('bad',bad)
