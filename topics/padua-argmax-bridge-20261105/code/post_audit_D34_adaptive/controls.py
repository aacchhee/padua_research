"""Fixed synthetic preexecution controls only; no native imports or S values."""
from fractions import Fraction as F
import checker as C

def reject(fn):
 try:fn()
 except (ValueError,RuntimeError,TypeError,KeyError,ZeroDivisionError):return
 raise AssertionError('invalid synthetic input admitted')

def run():
 cases=[]
 assert len(C.grid())==13 and C.canonical(F(3,4),F(1,4))==(F(1,4),F(3,4))
 assert C.canonical(F(1,4),F(1,2))==(F(1,4),F(1,2))
 reject(lambda:C.canonical(F(-1),F(0)));reject(lambda:C.canonical(.25,F(0)))
 M=C.coarse_norm({k:F(1) for k in C.grid()});assert M==2
 reject(lambda:C.coarse_norm({}));reject(lambda:C.coarse_norm({k:1.0 for k in C.grid()}))
 cases.append('13 distinct canonical grid keys; exact D14 norm and argument types')
 good={'format':'D34-midpoint-v1','n':41,'preorder':'.'}
 for bad in (dict(good,n=True),dict(good,n=42),dict(good,preorder='a.'),dict(good,preorder='..'),dict(good,preorder='?'),dict(good,preorder='a'*19+'.'*20)):reject(lambda bad=bad:C.decode(bad))
 assert C.decode(dict(good,preorder='a..'))
 cases.append('strict n41 schema, siblings, suffixes, depth and closed coverage')
 r,delta=C.radius_floor((F(0),F(1,64),F(0),F(1,64)))
 assert r==F(11,112) and F(1,512)<=delta<=F(1,32)
 r,delta=C.radius_floor((F(0),F(1),F(0),F(1)));assert r==F(1,2) and delta>=F(1,512)
 cases.append('actual-near capped radius and accepted D29 floor domain')
 assert C.corner(F(100),[F(0)]*3,F(1))['gap']
 u,v=F(1,32),F(9,512);t=F(22,7)**4/192
 reject(lambda:C.corner(F(100),[F(100)-t*u,F(100)-t*v,F(100)-t*(u+v)],F(1)))
 reject(lambda:C.corner(F(1),[F(1)]*3,F(1)))
 cases.append('exact pi-fourth actual corner criterion; equality rejects')
 box=(F(0),F(1,8),F(0),F(1,8));_,d=C.radius_floor(box)
 assert C.leaf((F(3,4),F(1),F(3,4),F(1)),None,F(1),F(1))[0]=='OUTSIDE'
 assert C.leaf(box,F(0),C.theta(box)-d,F(1))[0] is None
 assert C.leaf((F(1,2),F(1),F(1,2),F(1)),F(100),F(1),F(1))[0] is None
 cases.append('closed tangency and strict leaf equality rejection')
 leaves=C.decode(good);uppers={k:F(1) for k in C.tree_keys(leaves)}
 assert C.tree_norm(leaves,uppers)==(None,None)
 assert C.select_norm(leaves,uppers,F(2))[0]=='GRID'
 # A complete synthetic refined tree has valid small-theta norm; tie chooses TREE.
 finer=C.decode(dict(good,preorder='ab..b..'));vals={k:F(1) for k in C.tree_keys(finer)}
 mt,R=C.tree_norm(finer,vals);assert mt is not None and mt-1<R<=mt
 assert C.select_norm(finer,vals,mt)[0]=='TREE'
 cases.append('predeclared valid norm selection and TREE tie; no postfailure retry')
 return {'result':'PASS fixed synthetic controls','cases':cases,'native_calls':0}
