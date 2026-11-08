import math
from scipy import integrate
pi=math.pi
def I_quad(C,D,e):
    g=lambda t: abs(C/math.tan(t)+D/math.tan(t+e))-abs(C/math.tan(t))-abs(D/math.tan(t+e))
    pts=sorted([x%pi for x in [pi/2,pi-e,pi/2-e]])
    return integrate.quad(g,0,pi,points=pts,limit=500,epsabs=1e-13)[0]
J=lambda v,s,e: I_quad((v-s)/2,(v+s)/2,e)
for (v,s,e) in [(1,0.5,0.3),(1,0.5,1.2),(0.5,2,0.1),(0.5,2,1.2)]:
    val=J(v,s,e); print((v,s,e),'J=%.5f'%val,' 2(s-v)_+ log sin e=%.5f'%(2*max(s-v,0)*math.log(math.sin(e))), ' 2s log sin e=%.5f'%(2*s*math.log(math.sin(e))))
print('entropy value 2v{r log r+(1-r)log(1-r)}, v=1,s=.5:', 2*(0.25*math.log(0.25)+0.75*math.log(0.75)))
