# MEASURED: check C07 (6)/C05 (4) regular formula against the defining polynomial F at random regular points.
import math, random
random.seed(3)
def F(n,j,r,g,d):
    m=n+1; u=(j*math.pi+g)/n; v=(r*math.pi+d)/m
    D=(math.cos(m*u)+math.cos(n*u)-math.cos(m*v)-math.cos(n*v))/(math.cos(u)-math.cos(v))
    return (-1)**j*(D-math.cos(n*u))/2, u, v
worst=0
for n in (40,41,300,301):
    m=n+1
    for _ in range(3000):
        j=random.randrange(0,n+1); r=random.randrange(0,m+1)
        if (j+r)%2==0 or (r==j+1 and j>=n/2): continue
        g=random.uniform(-0.5,0.5); d=random.uniform(-(0.5-abs(g)),0.5-abs(g))
        Fv,u,v=F(n,j,r,g,d); den=math.cos(u)-math.cos(v)
        a=(math.cos(g)+math.cos(d))/2
        Rv=a*(1+math.cos(v))/den-(math.sin(g)/2)*math.sin(u)/den+(math.sin(d)/2)*math.sin(v)/den
        worst=max(worst,abs(Fv-Rv)/(1+abs(Fv)))
print("max rel diff regular formula:",worst)
