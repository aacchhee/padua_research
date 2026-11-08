"""Grid check of (ul:outer-geometry) and the far-guard majorants (auditor, float64)."""
import numpy as np
u1=47/384; a0=337/384; w0=721/384; p0=12/25; P0=24/25; eta=1.5
xs=np.linspace(0,np.pi,3001)
X,Y=np.meshgrid(xs,xs); R=X+Y
mask=(R>=1)&(R<=np.pi)
ce=np.cos(R/2); cd=np.cos((X-Y)/2); a=ce*cd; u=1-a; v=u-u1
p=np.sin(X); q=np.sin(Y); P=p+q; dp=np.maximum(q-p,0)
sv=np.sqrt(np.maximum(v,0))
def worst(lhs,rhs): d=(rhs-lhs)[mask]; return d.min()
print("min v:",v[mask].min())
print("a0-a min:",worst(a,a0)," w0-(ce+cd) min:",worst(ce+cd,w0))
print("p0+eta sqrt v - max(p,q) min:",worst(np.maximum(p,q),p0+eta*sv))
print("3 sqrt v - d+ min:",worst(dp,3*sv)," 2sqrt(2v)-|p-q| min:",worst(abs(p-q),2*np.sqrt(2*np.maximum(v,0))))
print("P0+4v-P min:",worst(P,P0+4*v)," 2sqrt(2u-u^2)-P min:",worst(P,2*np.sqrt(2*u-u*u)))
# the text's case 'x>=1 follows from u>=11/48': is u>=11/48 alone sufficient?
vmin=11/48-u1
print("u>=11/48 alone gives p0+eta*sqrt(v) >=",p0+eta*np.sqrt(vmin)," but sin x can reach 1 for x in [1,pi]")
# the needed x-dependent fact: for x>=1, u >= (1-cos x)/2 and sin x <= p0+eta*sqrt((1-cos x)/2-u1)
xx=np.linspace(1,np.pi,100001)
print("min over x in [1,pi] of p0+eta*sqrt((1-cos x)/2-u1)-sin x:",(p0+eta*np.sqrt((1-np.cos(xx))/2-u1)-np.sin(xx)).min())
# points with x>=1 and u closest to 11/48 while sin x near 1?
m2=mask&(X>=1)
print("over x>=1: min u =",u[m2].min(),"; at x=pi/2,y=0 u=",1-(0+1)/2)
# far-guard majorants for u<=1 on rho in [pi/2,pi] and in general
mask2=(R<=np.pi)
Fu=np.where(u<=0.5,2*np.sqrt(np.clip(u*(1-u),0,None)),1.0); Qu=np.minimum(2,np.sqrt(8*u))
for name,l,r in (("p<=F_u",p,Fu),("q<=F_u",q,Fu),("d+<=F_u",dp,Fu),("P<=Q_u",P,Qu),("ce+cd<=2-u",ce+cd,2-u)):
    print(name,"min slack",(r-l)[mask2].min())
print("far: min u on rho in [pi/2,pi]:",u[(R>=np.pi/2)&(R<=np.pi)].min()," vs 7/24=",7/24)
