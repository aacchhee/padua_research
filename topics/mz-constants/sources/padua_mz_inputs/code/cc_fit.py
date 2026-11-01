import numpy as np
N=np.array([40,80,160,320,640,1280,2560,5120,10240,20480.])
lm=np.array([0.259849,0.216153,0.182490,0.156015,0.134833,0.117635,0.103490,0.091721,0.081831,0.073442])
L=np.log(N); y=1/lm
print("2nd differences of 1/lmin per doubling:", np.round(np.diff(y,2),4))
for name,cols in [("a+bL+cL^2",[L**0,L,L**2]),("a+bL",[L**0,L]),("a+bL+cL^2 (N>=320)",None)]:
    if cols is None:
        s=N>=320; A=np.column_stack([L[s]**0,L[s],L[s]**2]); c=np.linalg.lstsq(A,y[s],rcond=None)[0]; r=A@c-y[s]
    else:
        A=np.column_stack(cols); c=np.linalg.lstsq(A,y,rcond=None)[0]; r=A@c-y
    print(name, np.round(c,5), "max resid", f"{np.abs(r).max():.2e}")
print("candidates: 1/(4pi)=%.5f 8/pi^4=%.5f 1/pi^2*0.8=%.5f 2/(pi^2*2.5)=%.5f"%(1/(4*np.pi),8/np.pi**4,0.8/np.pi**2,2/(np.pi**2*2.5)))
