"""Claude audit-01: independent symbolic/exact checks of C1/C3 hand-proved identities."""
import sympy as sp, itertools
from fractions import Fraction
from math import comb
out={}
def mons(n,vars_):
    # ordering by total degree; within degree order as stated per claim
    pass
# ---- C3 n1 mixed-axis identity, columns (1,z,y,x)
x0,x1,y0,y1,y2,z0,z1,z2=sp.symbols('x0 x1 y0 y1 y2 z0 z1 z2')
X=[x0,x1];Y=[y0,y1,y2];Z=[z0,z1,z2]
I=[(i,j,k) for i in range(2) for j in range(3) for k in range(3) if (2*i+j+k)%4==1]
assert I==[(0,0,1),(0,1,0),(1,1,2),(1,2,1)],I
M=sp.Matrix([[1,Z[k],Y[j],X[i]] for i,j,k in I])
D=sp.factor(M.det()); target=(x1-x0)*((y2-y0)*(z1-z0)-(z2-z0)*(y1-y0))
out['c3_n1']=sp.expand(M.det()-target)==0; print('c3 n1 det:',D, out['c3_n1'])
# ---- C3 n2 axis factorization, columns (1,z,y,x,z^2,yz,y^2,xz,xy,x^2)  [fraction-free Bareiss over ZZ[vars]]
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bareiss import bareiss
from sympy.polys.rings import ring
from sympy import ZZ
R12,*G=ring(','.join([f"x{i}" for i in range(3)]+[f"y{i}" for i in range(4)]+[f"z{i}" for i in range(5)]),ZZ)
xs=G[:3]; ys=G[3:7]; zs=G[7:]
I=sorted((i,j,k) for i in range(3) for j in range(4) for k in range(5) if (3*i+j+2*k)%6==0)
assert [f"{i}{j}{k}" for i,j,k in I]==['000','003','022','111','114','130','133','200','203','222'],I
def row(i,j,k):
    x,y,z=xs[i],ys[j],zs[k]; return [R12.one,z,y,x,z**2,y*z,y**2,x*z,x*y,x**2]
det=bareiss([row(*t) for t in I])
FX=(xs[1]-xs[0])*(xs[2]-xs[0])**3*(xs[2]-xs[1])
FY=(ys[2]-ys[0])**2*(ys[3]-ys[0])*(ys[3]-ys[1])*(ys[2]-ys[3]-ys[1]+ys[0])
FZ=(zs[3]-zs[0])**3*(zs[4]-zs[1])*(zs[3]-zs[4]-zs[1]+zs[0])
out['c3_n2']=(det+FX*FY*FZ)==0; print('c3 n2 det == -FX FY FZ (exact, ZZ[12 vars]):',out['c3_n2'], 'terms',len(det))
# ---- C1 quadratic identity, columns 1,x,x^2,y,xy,y^2
xq=sp.symbols('a0:3'); u=sp.symbols('u0:3'); v=sp.symbols('v0:3')
rows=[]
for r in range(3):
    for yy in (u[r],v[r]): rows.append([1,xq[r],xq[r]**2,yy,xq[r]*yy,yy**2])
M=sp.Matrix(rows); s=[u[r]+v[r] for r in range(3)]
dX=(xq[1]-xq[0])*(xq[2]-xq[0])*(xq[2]-xq[1])
R=sp.Matrix([[1,xq[r],s[r]] for r in range(3)]).det()
out['c1_quad']=sp.expand(M.det()+dX*sp.prod([v[r]-u[r] for r in range(3)])*R)==0; print('c1 quadratic identity:',out['c1_quad'])
# ---- C1 mixed obstruction n2 value matrix and n3 modular certificate
def sel(n,p): return [(i,j) for i in range(n+1) for j in range(n+2) if (i+j-p)%4 in (0,1)]
def mon2(n): return [(a,dg-a) for dg in range(n+1) for a in range(dg+1)]  # total degree then x exponent increasing? check below
def detQ(n,Xv,Yv,order):
    return sp.Matrix([[Xv[i]**a*Yv[j]**b for a,b in order] for i,j in sel(n,0)]).det()
n2order=[(0,0),(1,0),(2,0),(0,1),(1,1),(0,2)]
vals=[[detQ(2,XA,YA,n2order) for YA in ([0,1,2,3],[0,1,2,4])] for XA in ([0,1,2],[0,3,5])]
print('c1 n2 rectangle values',vals); out['c1_n2_rect']=vals==[[0,16],[-180,0]]
o3=[(a,dg-a) for dg in range(4) for a in range(dg+1)]
XL=[[692,619,116,299],[418,202,907,646]]; YL=[[683,167,402,988,776],[873,563,295,641,484]]
dets=[[int(detQ(3,Xv,Yv,o3)) for Yv in YL] for Xv in XL]
mod=[[d%1009 for d in r] for r in dets]; cross=dets[0][0]*dets[1][1]-dets[0][1]*dets[1][0]
print('c1 n3 residues',mod,'integer cross nonzero',cross!=0, 'cross mod',cross%1009)
out['c1_n3_cert']=(mod==[[469,520],[14,277]] and cross!=0)
# ---- Chebyshev n2 kernel polynomial
xc=[1,0,-1]; yc=[1,sp.Rational(1,2),-sp.Rational(1,2),-1]
out['c1_cheb_kernel']=all(3*xc[i]**2-3*xc[i]*yc[j]+2*yc[j]**2-2==0 for i,j in sel(2,0)); print('n2 kernel poly vanishes:',out['c1_cheb_kernel'])
# ---- C1 counts table brute force n=0..40 all phases
tab={0:[1,0,-1,0],1:[0,1,0,-1],2:[0]*4,3:[0]*4}
ok=all([len(sel(n,p))-comb(n+2,2) for p in range(4)]==tab[n%4] for n in range(41)); out['c1_counts']=ok; print('c1 counts table n<=40:',ok)
print(out); assert all(out.values())
