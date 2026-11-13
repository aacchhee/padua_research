import importlib.util, math, sys
from fractions import Fraction as F
import numpy as np
base='/workspace/padua_research/topics/padua-effective-cubature-20261112/code/'
def mod(name):
    s=importlib.util.spec_from_file_location(name,base+name+'.py')
    m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
d=mod('gamma_certificate'); i=mod('gamma_certificate_indep')
T=d.T_tables(13)
for a in range(14):
    for j in range(a+1):
        q,e=i.gamma_coef(a,j)
        assert T[a][j] == {-e:q/F(4)**e},(a,j)
print('Exact independent FT formula agrees for all 105 coefficients m<=13')
count=0
for dim in [2,3]:
    terms={(0,)*dim:F(1,3),(2,)+(0,)*(dim-1):F(-7,11),(1,)*dim:F(13,17),(0,)*(dim-1)+(4,):F(-19,23)}
    coef=np.zeros((5,)*dim); rad=coef.copy()
    for k,v in terms.items(): coef[k],rad[k]=i.fr_to_float_rad(v)
    bern=i.Bern(coef,rad,[list(range(5))]*dim)
    for lo,hi in [(np.zeros(dim),np.full(dim,.25)),(np.full(dim,.5),np.full(dim,.625)),(np.full(dim,2),np.full(dim,2.5))]:
        low,up=bern.bounds(lo[None],hi[None]); exact=[]
        for b in np.ndindex(*((27,)*dim)):
            value=F(0)
            for ex,c in terms.items():
                f=c
                for k,m in enumerate(ex):
                    l=F(float(lo[k])); w=F(float(hi[k]))-l
                    f*=sum(F(math.comb(b[k],r)*math.comb(m,r),math.comb(26,r))*l**(m-r)*w**r for r in range(min(b[k],m)+1))
                value+=f
            exact.append(value)
        assert F(float(low[0])) <= min(exact) and F(float(up[0])) >= max(exact)
        count+=1
print('Independent Bernstein enclosures contain exact rational extrema of coefficients for',count,'synthetic boxes')
print('versions',sys.version.split()[0],np.__version__,i.flint.__version__)
