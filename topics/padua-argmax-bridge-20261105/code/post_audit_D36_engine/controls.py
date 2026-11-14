"""Fixed pure schema/domain controls; no phase/native value evaluation."""
from fractions import Fraction as F
import checker as C

def reject(fn):
 try:fn()
 except (ValueError,RuntimeError,TypeError,KeyError,ZeroDivisionError):return
 raise AssertionError('invalid synthetic input admitted')

def run():
 cases=[]
 for n in (True,40,4096,F(41),41.0):reject(lambda n=n:C.degree(n))
 for n in (41,63,64,159,160,511,512,1023,1024,4095):assert C.degree(n)==n
 assert len(C.grid())==13 and C.canonical(F(3,4),F(1,4))==(F(1,4),F(3,4))
 assert C.canonical(F(1,4),F(1,2))==(F(1,4),F(1,2))
 assert C.coarse_norm({k:F(1) for k in C.grid()})==2
 reject(lambda:C.coarse_norm({}));reject(lambda:C.canonical(.25,F(0)))
 cases.append('strict integer domain, canonical13grid and valid coarse norm')
 assert C.actual_keys(1023)==((F(1,4092),F(0)),(F(0),F(3,16384)),(F(1,4092),F(3,16384)))
 reject(lambda:C.actual_keys(1024))
 assert C.corner_identity(1024)['kind']=='ANALYTIC_D27' and 'computer-assisted PD-T271' in C.corner_identity(1024)['dependencies']
 assert C.corner(1024,F(1),[],F(1))==C.corner_identity(1024)
 reject(lambda:C.corner(1024,F(1),[F(0)]*3,F(1)))
 cases.append('actual physical scaling and analytic1024 source-domain split')
 box=(F(0),F(1),F(0),F(1))
 for n in (41,63,64,159,160,511,512,1023,1024,4095):
  r,d=C.radius_floor(n,box);assert r==F(1,2) and d>0
  if n>=512:assert d==F(1,20)
 assert C.floor_identity(63)!=C.floor_identity(64) and C.floor_identity(159)!=C.floor_identity(160) and C.floor_identity(511)!=C.floor_identity(512)
 cases.append('piecewise accepted floors and actual-near radius guard')
 good={'format':'D36-midpoint-v1','n':1023,'preorder':'.'}
 for bad in (dict(good,n=True),dict(good,n=1024),dict(good,preorder='a.'),dict(good,preorder='..'),dict(good,preorder='?'),dict(good,preorder='a'*19+'.'*20)):
  reject(lambda bad=bad:C.decode(1023,bad))
 assert C.decode(1023,dict(good,preorder='a..'))
 rejects=C.decode(1023,good);uppers={k:F(1) for k in C.tree_keys(rejects)}
 assert C.tree_norm(1023,rejects,uppers)==(None,None)
 assert C.select_norm(1023,rejects,uppers,F(2))[0]=='GRID'
 cases.append('complete degree-bound closed tree; invalid theta rejects tree norm')
 n=1023;u,v=F(1,32),F(9,512);t=F(22,7)**4/192
 assert C.corner(n,F(100),[F(0)]*3,F(1))['gap']
 reject(lambda:C.corner(n,F(100),[F(100)-t*u,F(100)-t*v,F(100)-t*(u+v)],F(1)))
 tiny=(F(0),F(1,8),F(0),F(1,8));_,d=C.radius_floor(n,tiny)
 assert C.leaf(n,tiny,F(1),F(1)+C.theta(n,tiny)-d,F(1))[0] is None
 reject(lambda:C.parse_essential({'format':'D34-kept-proof-v1'},'x'))
 cases.append('pi-fourth corner equality; strict leaf comparison; version rejection')
 return {'result':'PASS fixed synthetic controls','cases':cases,'native_calls':0,'scope':'schema/domain arithmetic only; no scientific certificate'}
