# Auditor check: Betke-Henk octahedron basis normalization, det, l1 minimum, threshold arithmetic.
from fractions import Fraction as F
import itertools, sympy as sp
cols=[(F(1,3),F(1,2),F(1,6)),(F(-1,6),F(-1,3),F(1,2)),(F(-1,2),F(1,6),F(-1,3))]
B=sp.Matrix([[2*c[i] for c in cols] for i in range(3)])  # columns = 2*vectors
print("B=",B.tolist()); print("det B=",B.det())
Bc=sp.Rational(1,3)*sp.Matrix([[2,-1,-3],[3,-2,1],[1,3,-2]])
print("repo Bcrit equals 2*cols:", B==Bc)
# l1 minimum over a box of integer coefficient vectors (box large enough: the lattice is well-conditioned)
best=None; R=6
for z in itertools.product(range(-R,R+1),repeat=3):
    if z==(0,0,0): continue
    v=B*sp.Matrix(z); n=sum(abs(x) for x in v)
    if best is None or n<best[0]: best=(n,z)
print("min l1 over |z|<=6:",best)
# rigorous: l1 >= ||v||_2 >= sigma_min*|z|_2 ; check sigma_min to justify box
import numpy as np
s=np.linalg.svd(np.array(B.tolist(),dtype=float),compute_uv=False); print("sigma_min",s.min(),"=> any |z|_inf>6 has l1>=",s.min()*6)
vol=F(4,3); d=abs(F(str(B.det()))); print("density vol/det=",vol/d)
# count of min vectors
cnt=sum(1 for z in itertools.product(range(-R,R+1),repeat=3) if z!=(0,0,0) and sum(abs(x) for x in B*sp.Matrix(z))==2)
print("number of l1=2 vectors:",cnt)
f=lambda n:n**3-108*n**2-198*n-108
print("f(109),f(110)=",f(109),f(110), "first n with 19n^3>18(n+1)(n+2)(n+3):",next(n for n in range(1,1000) if 19*n**3>18*(n+1)*(n+2)*(n+3)))
print("all n>=110 up to 10^5 positive:",all(f(n)>0 for n in range(110,100000)))
n=sp.symbols('n'); print("648*diff =",sp.expand(648*(sp.Rational(19,108)*n**3-(n+1)*(n+2)*(n+3)/6)),"; 108*diff=",sp.expand(108*(sp.Rational(19,108)*n**3-(n+1)*(n+2)*(n+3)/6)))
print("f(n+1)-f(n)=",sp.expand(f(n+1)-f(n)))
