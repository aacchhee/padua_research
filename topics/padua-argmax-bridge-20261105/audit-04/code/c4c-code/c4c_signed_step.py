import numpy as np
exec(open('c4c_rows.py').read().split("Pos = {")[0])
rng=np.random.default_rng(3); worst=0
for n in (32,33,160):
    for _ in range(200):
        x=rng.uniform(0,1); y=rng.uniform(0,1-x); S=setup(n,x,y); m=S['m']
        for (r,sb) in ((1,1),(1,-1),(2,-1),(0,1)):
            b=sb*y; w=r*np.pi+b; v=w/m
            idx = r if sb>0 else 2*m-r
            val,_,_=row_vals(S,idx)
            a,p=S['a'],S['p']; sb_=np.sin(b)
            Cm=(p-sb_-2*a/np.tan(v/2))/4; Cp=(p+sb_+2*a/np.tan(v/2))/4
            step=-(Cm*np.tan((x-b+v)/2)+Cp*np.tan((x+b-v)/2))/m
            worst=max(worst,abs(val.sum()/(n*m)-step))
print("max |signed - (-(1/m)[C- tan((x-b+v)/2)+C+ tan((x+b-v)/2)])| =",worst)
