"""Bounded exact controls for revised gamma conversion/enclosure; no DGOV replay."""
import ast
import hashlib
import importlib.util
import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path
import numpy as np
import flint
from flint import arb, ctx, fmpq

SOURCE = Path(__file__).resolve().parents[1] / 'code/gamma_certificate.py'
spec = importlib.util.spec_from_file_location('gamma', SOURCE)
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)
# Execute the actual conversion block of main(), with synthetic exact coefficients.
tree = ast.parse(SOURCE.read_text())
main = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'main')
start = next(j for j,n in enumerate(main.body) if isinstance(n, ast.ImportFrom) and n.module == 'flint')
stop = next(j for j in range(start + 1, len(main.body)) if isinstance(main.body[j], ast.For) and ast.unparse(main.body[j].target) == '(k, v)')
# The first (k,v) loop is P conversion. Include both conversion loops, stopping before top-degree identity.
stop = next(j for j in range(stop + 1, len(main.body)) if isinstance(main.body[j], ast.For) and ast.unparse(main.body[j].target) == '(k, v)')
block = ast.Module(body=main.body[start:stop], type_ignores=[])
P={(0,0,0):F(1,10),(1,0,0):F(7,13),(0,1,0):F(1,10**310)}
G={(0,0,0):{0:F(-33102),-1:F(103993)},(1,0,0):{-13:F(23,37)},(0,1,0):{0:F(1,10**310)}}
env={'P':P,'G':G,'Fraction':F}
exec(compile(block,str(SOURCE),'exec'),env)
for k,v in P.items():
    assert abs(v-F(env['Pf'][k])) <= F(env['Pe'][k])
ctx.prec=512
for k,dd in G.items():
    b=sum(arb(fmpq(q.numerator,q.denominator))*arb.pi()**e for e,q in dd.items())
    f=F(env['Gf'][k]); err=(b-arb(fmpq(f.numerator,f.denominator))).abs_upper()
    assert err <= arb(env['Ge'][k])

# Exact rational Taylor bounds of (sum y - 3)^13/97, with cancellation.
checks=[]
for dim in (2,3):
    coef={}
    for a in itertools.product(range(14),repeat=dim):
        s=sum(a)
        if s<=13:
            multinomial=math.factorial(13)//math.factorial(13-s)
            for e in a: multinomial//=math.factorial(e)
            coef[a]=F(multinomial*(-3)**(13-s),97)
    C=np.zeros((14,)*dim); E=np.zeros_like(C)
    for a,c in coef.items():
        C[a]=float(c)
        E[a]=float(abs(c-F(C[a])))*(1+2**-50)+1e-300
    boxes=[([F(1,2)]*dim,[F(1,16)]*dim),([F(1)]*dim,[F(1,2**14)]*dim),([F(8)]*dim,[F(1,4)]*dim)]
    for M,R in boxes:
        exact={}
        for a,c in coef.items():
            for b in itertools.product(*(range(e+1) for e in a)):
                v=c
                for j in range(dim): v*=math.comb(a[j],b[j])*M[j]**(a[j]-b[j])
                exact[b]=exact.get(b,F(0))+v
        zero=(0,)*dim
        radius=sum(abs(c)*math.prod(R[j]**b[j] for j in range(dim)) for b,c in exact.items() if b!=zero)
        lb=exact[zero]-radius; ub=exact[zero]+radius
        low,high=g.taylor_enclose(C,np.abs(C),np.array([[float(x) for x in M]]),np.array([[float(x) for x in R]]),Eten=E)
        assert F(low[0])<=lb and F(high[0])>=ub,(dim,M,R,float(low[0]-float(lb)),float(high[0]-float(ub)))
        checks.append({'dim':dim,'M':list(map(str,M)),'R':list(map(str,R)),'pass':True})
# Error-only tensor: coefficient uncertainty must survive even when nominal coefficients vanish.
C=np.zeros((14,14,14));E=np.zeros_like(C);E[4,4,5]=0.125
M=np.array([[0.5,0.5,0.5]]);R=np.array([[0.25,0.25,0.25]])
lo,hi=g.taylor_enclose(C,C,M,R,Eten=E)
exact=F(1,8)*F(3,4)**13
assert F(lo[0])<=-exact and F(hi[0])>=exact
# Default-radius tail: all homogeneous degrees have strictly negative coefficients.
C=np.zeros((14,14,14)); E=np.zeros_like(C)
for k in range(14): C[0,0,k]=-1.0; E[0,0,k]=2**-40
assert g.tail(C,+1,4,Eten=E)['ok']
E[0,0,13]=2.0
assert not g.tail(C,+1,4,Eten=E,max_boxes=1)['ok']
report={'verdict':'PASS','scope':'synthetic controls only; not DGOV certificate replay','conversion_P':len(P),'conversion_G':len(G),'exact_Taylor_boxes':checks,'error_only_tensor':True,'tail_radius_propagation':True,'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'control_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'numpy':np.__version__,'flint':flint.__version__}
print(json.dumps(report,indent=2))
