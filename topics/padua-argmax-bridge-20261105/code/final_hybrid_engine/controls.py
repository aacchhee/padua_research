"""Prospective fixed pure schema/domain controls. Never run on import."""
from fractions import Fraction as F
from copy import deepcopy
import checker as C

def reject(fn):
 try:fn()
 except (ValueError,RuntimeError,TypeError,KeyError,ZeroDivisionError):return
 raise AssertionError('invalid synthetic input admitted')

def run():
 cases=[]
 for n in (True,40,4096,F(41),41.0):reject(lambda n=n:C.degree(n))
 for n in (41,63,64,159,160,191,192,255,256,511,512,4095):assert C.degree(n)==n
 assert len(C.grid())==13 and C.canonical(F(3,4),F(1,4))==(F(1,4),F(3,4))
 assert C.canonical(F(1,4),F(1,2))==(F(1,4),F(1,2))
 assert C.coarse_norm({k:F(1) for k in C.grid()})==2
 reject(lambda:C.coarse_norm({}));reject(lambda:C.canonical(.25,F(0)))
 cases.append('strict integer domain, canonical13grid and valid coarse norm')
 assert C.actual_keys(255)==((F(1,1020),F(0)),(F(0),F(3,4096)),(F(1,1020),F(3,4096)))
 reject(lambda:C.actual_keys(256));reject(lambda:C.corner(255,F(1),[],F(1)))
 assert C.corner_identity(255)['kind']=='ACTUAL_THREE'
 assert C.corner_identity(256)['kind']=='ANALYTIC_E12_256'
 assert C.corner(256,F(1),[],F(1))==C.corner_identity(256)
 reject(lambda:C.corner(256,F(1),[F(0)]*3,F(1)))
 cases.append('corner255 cannot use analytic theorem;256 closed square loss1/30')
 box=(F(0),F(1),F(0),F(1))
 for n in (41,63,64,159,160,511,512,4095):
  r,d=C.radius_floor(n,box);assert r==F(1,2) and d>0
  if n>=512:assert d==F(1,20)
 assert C.floor_identity(63)!=C.floor_identity(64) and C.floor_identity(159)!=C.floor_identity(160) and C.floor_identity(511)!=C.floor_identity(512)
 cases.append('unchanged accepted noncorner floors and actual-near radius guard')
 good={'format':'FINAL-HYBRID-midpoint-v1','n':256,'preorder':'a.f'}
 for bad in (dict(good,n=True),dict(good,n=255),dict(good,preorder='a.'),dict(good,preorder='..'),dict(good,preorder='?'),dict(good,preorder='a'*19+'.'*20),dict(good,preorder='af.'),dict(good,preorder='a.f.')):
  reject(lambda bad=bad:C.decode(256,bad))
 assert C.decode(256,good)
 reject(lambda:C.decode(191,dict(good,n=191)))
 assert C.decode(192,dict(good,n=192))
 whole=(F(1,2),F(1),F(0),F(1));below=(F(1,4),F(1,2),F(0),F(1))
 assert C.analytic_far(192,whole)
 reject(lambda:C.require_analytic_far(191,whole));reject(lambda:C.require_analytic_far(192,below))
 reject(lambda:C.require_analytic_far(192,(F(0),F(1),F(0),F(1))))
 reject(lambda:C.tree_norm(256,C.decode(256,good),{k:F(1) for k in C.grid()},good))
 assert C.select_norm(256,C.decode(256,good),{k:F(1) for k in C.grid()},F(2),good)==('GRID',F(2),None)
 numeric=dict(good,preorder='ab..b..')
 # Four closed half-width leaves cover the whole square: D19 applies.
 assert C.tree_norm(256,C.decode(256,numeric),{k:F(1) for k in C.grid()},numeric)[0] is not None
 cases.append('closed explicit analytic topology;191/belowhalf reject; GRID with f, valid complete numeric TREE')
 n=255;u,v=F(1,32),F(9,512);t=F(22,7)**4/192
 assert C.corner(n,F(100),[F(0)]*3,F(1))['gap']
 reject(lambda:C.corner(n,F(100),[F(100)-t*u,F(100)-t*v,F(100)-t*(u+v)],F(1)))
 tiny=(F(0),F(1,8),F(0),F(1,8));_,d=C.radius_floor(n,tiny)
 assert C.leaf(n,tiny,F(1),F(1)+C.theta(n,tiny)-d,F(1))[0] is None
 cases.append('unchanged exact pi-fourth equality rejection and strict numeric leaf')
 # Structurally valid diagnostic input, deliberately not a scientific proof.
 ident={'path':'synthetic/FREEZE.json','bytes':1,'sha256':'0'*64}
 verification={'n':256,'nodes':3,'leaves':2,'S_premises':13,'norm_method':'GRID','M':'2','R_tree':None,'L':'1','leaf_counts':{},'minimum_strict_margins':{},'minimum_used_floor':'1/32','corner':C.corner_identity(256),'floor':C.floor_identity(256),'analytic_far':C.far_identity(256)}
 doc={'format':'FINAL-HYBRID-kept-proof-v1','status':'PROVISIONAL_REQUIRES_FINAL_ACCOUNTING_AND_RETURN0','n':256,'tree':good,'pi_bracket':['157/50','22/7'],'S_upper_columns':['a_pi','b_pi','outward_upper_hex'],'S_upper_rows':[[str(a),str(b),'0x1.0000000000000p+0'] for a,b in C.grid()],'origin_lower_hex':'0x1.0000000000000p+0','lambda_upper_columns':['physical_xi_pi','physical_zeta_pi','outward_upper_hex'],'lambda_upper_rows':[],'norm':{'method':'GRID','M':'2'},'floor':C.floor_identity(256),'corner':C.corner_identity(256),'analytic_far':C.far_identity(256),'verification':verification,'freeze':ident,'whole_raw_evidence':ident,'execution_role':'synthetic','CPU_stages':[],'CPU_through_receipt_start':0,'scope':'synthetic parser control, not a proof'}
 parsed=C.parse_essential(doc,ident);assert parsed['tree']==good and parsed['method']=='GRID'
 for field,changes in (('freeze',{'sha256':'1'*64}),('freeze',{'sha256':'invalid'}),('norm',{'method':'TREE'}),('tree',{'preorder':'af.'}),('corner',{'kind':'ANALYTIC_D27'}),('analytic_far',{'primitive_gap':'1/2'})):
  bad=deepcopy(doc);bad[field].update(changes);reject(lambda bad=bad:C.parse_essential(bad,ident))
 bad=deepcopy(doc);bad['S_upper_rows'].pop();reject(lambda:C.parse_essential(bad,ident))
 reject(lambda:C.parse_essential({'format':'D36-kept-proof-v1'},ident))
 cases.append('strict new schema, hash identity, grid closure, theorem and geometry tamper rejection')
 return {'result':'PASS fixed synthetic controls','cases':cases,'native_calls':0,'scope':'schema/domain arithmetic only; no scientific certificate'}
