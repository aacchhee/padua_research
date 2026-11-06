"""Preregistered synthetic-only negative controls, separate <=1 CPU author or auditor share of reserved2.
Never imports producer, constructs Native, compiles, loads a .so or evaluates S.
"""
import json,math,pathlib,resource,tempfile
from fractions import Fraction as F
import checker as C
import runtime as R
OUT=R.ROOT/'local-output/argmax-bridge-20261105/post-audit-D11/point-cover-pure-controls'


def rejected(fn):
 try:fn()
 except (ValueError,RuntimeError,TypeError,KeyError,ZeroDivisionError):return
 raise AssertionError('malformed input admitted')


def main():
 import argparse
 p=argparse.ArgumentParser();p.add_argument('--run-once',action='store_true');a=p.parse_args()
 if not a.run_once:raise RuntimeError('reviewed explicit --run-once required')
 resource.setrlimit(resource.RLIMIT_CPU,(1,1))
 OUT.mkdir(parents=True,exist_ok=False)
 R.check_freeze()
 with (OUT/'preregistration.json').open('x') as f:json.dump({'source':R.identity(__file__),'freeze':R.identity(R.HERE/'FREEZE.json'),'hard_CPU':1,'aggregate_author_and_auditor_reserved':2,'scope':'synthetic pure Python only'},f)
 cases=[]
 def check(name,fn):fn();cases.append(name)
 for s in ('1/0','01','1/2/3','1.0','nan','1/'+'9'*300):
  check('rational '+s[:12],lambda s=s:rejected(lambda:C.rational(s)))
 for text in ('{"x":1,"x":2}','{"x":NaN}','{"x":Infinity}','{"x":1e999}'):
  p=OUT/'malformed.json';p.write_text(text)
  check('strict JSON '+text,lambda:rejected(lambda:R.strict_json(p)))
 p.unlink()
 good={'format':'D11-midpoint-v1','n':512,'preorder':'.'}
 for key,value in (('n',True),('n',511),('preorder','a.'),('preorder','..'),('preorder','x'),('preorder','a'*66+'.'*67)):
  check('preorder '+key+str(value)[:12],lambda key=key,value=value:rejected(lambda:C.decode_certificate(dict(good,**{key:value}))))
 assert C.canonical(F(1),F(0))==C.canonical(F(0),F(1))
 assert C.canonical(F(3,4),F(3,4))==C.canonical(F(1,4),F(1,4))
 cases.append('closed-edge and outside-fold equivalence')
 # A tangent singleton belongs to T and must request/verify vertex values.
 calls=[]
 tree={'format':'D11-tree-v1','n':512,'tree':{'axis':0,'at':'1/2','left':{'leaf':True},'right':{'leaf':True}}}
 C.verify_tree_skeleton(tree,F(100),lambda key:(calls.append(key) or F(0)))
 assert calls;cases.append('full child union exact traversal')
 singleton=(F(1,2),F(1),F(1,2),F(1))
 rejected(lambda:C.leaf_predicate(singleton,[F(100)]*4,F(1)))
 assert C.leaf_predicate((F(3,4),F(1),F(3,4),F(1)),[],F(1))=='OUTSIDE'
 cases.append('tangent retained; strictly outside omitted')
 rejected(lambda:C.verify_certificate(good,F(1),lambda key:math.nan))
 rejected(lambda:C.verify_certificate(good,F(1),lambda key:F(-1)))
 rejected(lambda:C.verify_certificate(good,F(1),lambda key:F(100)))
 node={'leaf':True};alias={'format':'D11-tree-v1','n':512,'tree':{'axis':0,'at':'1/2','left':node,'right':node}}
 rejected(lambda:C.verify_tree_skeleton(alias,F(100),lambda key:F(0)))
 for axis,at in ((True,'1/2'),(2,'1/2'),(0,'0'),(0,'1')):
  bad={'format':'D11-tree-v1','n':512,'tree':{'axis':axis,'at':at,'left':{'leaf':True},'right':{'leaf':True}}}
  rejected(lambda:C.verify_tree_skeleton(bad,F(100),lambda key:F(0)))
 cases.append('false oracle, strict margin, aliases, invalid axis/progress')
 R.check_freeze()
 R.save(OUT/'summary.json',{'result':'PASS synthetic controls only','cases':cases,'CPU_before_summary':R.cpu(),'cap':1,'native_calls':0,'limitations':'does not establish a point enclosure or mathematical cover'})
if __name__=='__main__':main()
