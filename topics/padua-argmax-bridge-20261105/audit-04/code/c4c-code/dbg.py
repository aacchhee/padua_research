import numpy as np, sys
sys.argv=['x']
exec(open('c4c_rows.py').read().split("Pos = {")[0])
S=setup(32,0.3,0.2); n,m=S['n'],S['m']
for (r,sb) in ((1,1),(1,-1),(2,-1)):
    b=sb*S['y']; idx=actual_row_index(S,r,sb)
    val,_,v=row_vals(S,idx); js,z,F=sinc_row(S,r,b)
    print(r,sb,idx,len(js),len(val))
    print(' top actual', np.sort(val/(n*m))[-3:], ' bottom', np.sort(val/(n*m))[:2])
    print(' top sinc  ', np.sort(F)[-3:], ' bottom', np.sort(F)[:2])
    print(' pos js', js[F>0], ' sum F', F.sum(), ' sum act', val.sum()/(n*m))
