#!/usr/bin/env python3
"""Independent focused premise/guard checks; no numerical kernel build/replay."""
import ast
import copy
import hashlib
import importlib.util
import json
import math
import pathlib
import platform
import time
from fractions import Fraction as F

ROOT=pathlib.Path(__file__).resolve().parents[3]
TOPIC=ROOT/'topics/padua-argmax-bridge-20261105'
SOURCE=TOPIC/'code/phase_checker'
PINS={
 'check_r6.py':'437378a5d0fe21d4d0ef30b1c9843274d2cb98fc9f408e9bad5683ec9f1e73dc',
 'check.py':'88dde644a77a286e547679b0547c4d35814a4dda7373575208246882d9a26820',
 'hybrid_kernel_v2.cpp':'17fea91d4fa02e4183823e5d70b44705e96da7acfd26b04a0f3ed1cac443d9a2',
 'build_snapshot.py':'19a5a7c2296768853b94672b9b5dc4cf16c9ae87c37abbcde073ffaf89246bfb'}


def ident(path):
 raw=path.read_bytes()
 return {'path':str(path),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}


def main():
 started=time.process_time();sources=[ident(SOURCE/p) for p in PINS]
 assert all(row['sha256']==PINS[pathlib.Path(row['path']).name] for row in sources)
 spec=importlib.util.spec_from_file_location('independent_r6',SOURCE/'check_r6.py')
 r6=importlib.util.module_from_spec(spec);spec.loader.exec_module(r6)
 receipt_path=ROOT/r6.RANGE_RECEIPT_PATH;raw=receipt_path.read_bytes();receipt=r6.strict_json(raw)
 reads=[]
 def read(path):
  assert path in r6.CODE_DATA_PINS and not path.endswith('.md')
  reads.append(path);return (ROOT/path).read_bytes()
 verified=r6._validate_range_snapshot(raw,read)
 assert len(verified)==4 and set(reads)==set(r6.CODE_DATA_PINS)
 production=r6.published_corner_premise()
 assert production['degrees']==list(range(2,129)) and production['kappa']=='1/16000'
 rejected=[]
 def reject(name,fn):
  try:fn()
  except r6.Invalid as e:rejected.append({'case':name,'reason':str(e)})
  else:raise AssertionError('unexpected acceptance: '+name)
 reject('different receipt bytes',lambda:r6._validate_range_snapshot(raw+b' ',read))
 changed=copy.deepcopy(receipt);changed['input_degrees'].remove(24)
 reject('missing integer degree24',lambda:r6._validate_range_contents(changed,read))
 changed=copy.deepcopy(receipt);changed['counters']['failed']=False
 reject('boolean zero counter alias',lambda:r6._validate_range_contents(changed,read))
 def bad_code(path):
  value=read(path)
  return value+b' ' if path.endswith('check_corner_range.py') else value
 reject('changed wrapper bytes',lambda:r6._validate_range_snapshot(raw,bad_code))
 def bad_data(path):
  value=read(path)
  return value+b' ' if path.endswith('n3-corner-batch.json') else value
 reject('changed evidence data bytes',lambda:r6._validate_range_snapshot(raw,bad_data))
 changed=copy.deepcopy(receipt);changed['wrapper']=copy.deepcopy(changed['source'])
 reject('duplicate required source identity',lambda:r6._validate_range_contents(changed,read))
 # Degree rejection happens before any arithmetic input is requested.
 class NoKernel:
  def bounds(self,*args):raise AssertionError('arithmetic should not run')
 square=[-1/128,1/128,-1/128,1/128]
 invalid_degrees=[1,129,True,False,24.0]
 for n in invalid_degrees:
  assert not r6.local_range(n,square)
  reject('candidate degree '+repr(n),lambda n=n:r6.check({'format':'n3-phase-candidate-v1','n':n},NoKernel()))
 geometry=[]
 for n in (2,24,32,128):
  bound=(F(1,128)**2+F(n*n,(n+1)**2)*F(1,128)**2)/2
  assert bound<F(1,16384)<F(1,16000) and r6.local_range(n,square)
  for axis in (0,2):
   enlarged=square.copy();enlarged[axis+1]=math.nextafter(1/128,math.inf)
   assert not r6.local_range(n,enlarged)
  geometry.append({'n':n,'bound':str(bound),'square_boundary_accepted':True,'one_ulp_enlargement_rejected':True})
 names=['rational','Kernel','tree_partition','box_for','minabs','maxabs','local_inherited','strict_json']
 def definitions(path):
  return {node.name:ast.dump(node,include_attributes=False) for node in ast.parse(path.read_bytes()).body
          if isinstance(node,(ast.FunctionDef,ast.ClassDef))}
 old,new=definitions(SOURCE/'check.py'),definitions(SOURCE/'check_r6.py')
 assert all(old[name]==new[name] for name in names)
 assert sources==[ident(SOURCE/p) for p in PINS]
 result={'scope':'Independent focused fixed-premise guard review; no arithmetic or full-cover replay',
         'rules_input':'fc8c2885f47b08cecc7f65328db0e740cbc205ea',
         'command':'python topics/padua-argmax-bridge-20261105/code/review_phase_r6_premise.py',
         'script':ident(pathlib.Path(__file__).resolve()),'sources':sources,
         'premise_receipt':ident(receipt_path),'verified_code_data_pins':verified,
         'rejection_controls':rejected,'geometry_controls':geometry,'unchanged_AST_definitions':names,
         'no_prose_reads_in_guard':True,'published_premise_resolved':True,
         'python':platform.python_version(),'cpu_seconds':time.process_time()-started,
         'passed':True,'full_phase_runs':0,'corner_range_reruns':0,'numerical_kernel_builds':0}
 target=TOPIC/'evidence/phase-r6-premise-review.json';target.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'passed':True,'rejection_controls':len(rejected),'boundary_degrees':len(geometry),
                   'cpu_seconds':result['cpu_seconds'],'full_phase_runs':0}))


if __name__=='__main__':main()
