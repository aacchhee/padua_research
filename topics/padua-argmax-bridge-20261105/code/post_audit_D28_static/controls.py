"""Fixed pure controls consumed only by the preregistered controller stage.
Synthetic Fractions only: no native oracle or degree output is evaluated here.
"""
from fractions import Fraction as F
import checker as C

def rejects(fn):
 try:fn()
 except (ValueError,RuntimeError,TypeError,KeyError,ZeroDivisionError):return
 raise AssertionError('synthetic malformed input accepted')

def run():
 cases=[]
 assert C.canonical(F(3,4),F(3,4))==(F(1,4),F(1,4))
 assert C.canonical(F(3,4),F(1,4))==(F(1,4),F(3,4))
 assert C.canonical(F(1,4),F(1,2))==(F(1,4),F(1,2))
 rejects(lambda:C.canonical(F(-1),F(0)))
 rejects(lambda:C.canonical(.25,F(0)))
 cases.append('exact even-lattice fold; reversal only on hypotenuse')
 bad={'format':'D19-midpoint-v1','n':2048,'preorder':'.'*61}
 rejects(lambda:C.decode(bad))
 rejects(lambda:C.decode(dict(bad,n=True)))
 rejects(lambda:C.decode(dict(bad,preorder='a'*61)))
 cases.append('fixed schema; complete siblings and no trailing tokens')
 box=(F(0),F(1,8),F(0),F(1,8));leaves=[(0,box)]
 values={key:F(1) for key in C.keys(leaves)}
 M,norm=C.adaptive_norm(leaves,values);R=F(norm['R'])
 assert M-1<R<=M
 rejects(lambda:C.adaptive_norm(leaves,{}))
 rejects(lambda:C.adaptive_norm(leaves,{key:1.0 for key in values}))
 rejects(lambda:C.adaptive_norm([(0,(F(0),F(1),F(0),F(1)))],{key:F(1) for key in C.keys([(0,(F(0),F(1),F(0),F(1)))] )}))
 cases.append('complete rational oracle keys; exact absorption/ceiling; theta guard')
 assert C.leaf((F(3,4),F(1),F(3,4),F(1)),[],F(1),F(1))[0]=='OUTSIDE'
 tangent=(F(1,2),F(1),F(1,2),F(1))
 rejects(lambda:C.leaf(tangent,[F(100)]*4,F(1),F(1)))
 # Equality never satisfies the strict FAR or actual-NEAR gap.
 bound=C.theta(box)
 rejects(lambda:C.leaf(box,[F(0)]*4,bound-F(1,16),F(1)))
 assert C.leaf(box,[F(0)]*4,F(100),F(1))[0]=='FAR'
 cases.append('closed seam/tangent; strict margin equality rejected')
 import baseline as B
 key=(F(0),F(0));old={'lower':F(0),'upper':F(1,16384),'radius':F(0),'counts':[0]*6}
 raw={'api':'S','n':6912,'key':['0','0'],'native':{'returncode':0,'raw_hex':['0x0.0p+0','0x1.0000000000000p-16','0x0.0p+0'],'counts':[0]*6}}
 assert B.compare(key,raw,old)[0]==F(1,65536)
 bad={**raw,'native':{**raw['native'],'counts':[1]*6}};rejects(lambda:B.compare(key,bad,old))
 bad={**raw,'native':{**raw['native'],'raw_hex':['0x0.0p+0','0x1.0000000000000p-15','0x0.0p+0']}};rejects(lambda:B.compare(key,bad,old))
 bad={**raw,'n':2048};rejects(lambda:B.compare(key,bad,old))
 rejects(lambda:B.compare(key,raw,{**old,'lower':F(1),'upper':F(2)}))
 cases.append('synthetic exact comparison: overlap, key/degree, counter identity and endpoint width')
 return {'result':'PASS synthetic controls only','cases':cases,'native_calls':0,'scope':'fixed preexecution protocol controls, no scientific instance'}
