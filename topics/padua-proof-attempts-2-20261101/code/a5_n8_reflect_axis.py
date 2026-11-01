"""Propose ordinary N8 proof records with exact axis-root ID reuse under63.

This adds no verifier predicate.  Every emitted record must be replayed by the
unchanged independent checker.  Full mode requires complete left-half coverage.
Fixture mode is explicitly incomplete and performs no search.
"""
import argparse,copy,gzip,hashlib,json,ast
from pathlib import Path
from collections import Counter
from a5_n8_field import *
from a5_n8_boxes import write_artifact,krawczyk,inject,hull
from a5_n8_continue import FROZEN_SOURCES,prefix_partition,pathbox,restore_roots,require

CONTINUATION_SHA='96ce015c9d3d161030be8d8d0de7e2c20f8e21d31b718948734703f3667476ad'
PRODUCER_V5_SHA='e1ad5f540ee67f785b79ba333d2bbf221f0f4f8956c93ce6ad9ad5d3b4140993'
ORIGINAL_REFLECT_SHA='84e3ca91689f671cb05f008d87cd4c1ce835392b715505070e5f45e60e166def'
def guards():
 import a5_n8_reflect_v5 as previous_static
 require(hashlib.sha256(Path(previous_static.__file__).read_bytes()).hexdigest()=='a98e9eaccf64a736619e68781e3037aa90d9014c04e8b532ec85a20cf43978b5','frozen static version changed')
 previous_static.guards()
 original=ast.parse(Path(previous_static.__file__).read_text());current=ast.parse(Path(__file__).read_text())
 def functions(tree):return{n.name:n for n in ast.walk(tree)if isinstance(n,ast.FunctionDef)}
 first,second=functions(original),functions(current)
 for name in('reflected_path','reflected_box','reflected_C','maskmap','counts_for','validate_new_provenance','masks'):
  require(ast.dump(first[name],include_attributes=False)==ast.dump(second[name],include_attributes=False),'unchanged static helper modified: '+name)
def validate_new_provenance(data):
 if data.get('metadata',{}).get('source_sha256')!=PRODUCER_V5_SHA:return
 lineage=data['metadata'].get('continuation',{});focus=data['metadata'].get('left_focus',{})
 require(lineage.get('prior_source_sha256')==CONTINUATION_SHA and lineage.get('source96_sha256')==CONTINUATION_SHA,'wrong source96 ancestry in new artifact')
 require(lineage.get('frozen_sources')==FROZEN_SOURCES,'wrong original frozen ancestry in new artifact')
 original=lineage.get('original_v3_sha256');parent=lineage.get('input_sha256')
 require(all(type(v)is str and len(v)==64 and set(v)<=set('0123456789abcdef')for v in(original,parent)),'missing exact original/parent digest')
 require(type(lineage.get('original_v3_bytes'))is int and lineage['original_v3_bytes']>0,'missing original byte identity')
 require(focus.get('all_parked_paths_restored')is True,'parked right frontier not restored')
 parked=focus.get('parked_right_paths')
 require(type(parked)is list and all(type(p)is str and p.startswith('1')for p in parked),'invalid parked right frontier')
 require(data.get('pending_paths',[])[:len(parked)]==parked,'parked right words absent from full artifact')

def reflected_path(path):
 return ''.join(('1'if bit=='0'else'0')if i%2==0 else bit for i,bit in enumerate(path))
def reflected_box(box):
 return [[str(-F(box[0][1])),str(-F(box[0][0]))],list(box[1])]
def reflected_C(C):
 return [[str(F(C[0][0])),str(-F(C[0][1]))],[str(-F(C[1][0])),str(F(C[1][1]))]]
def maskmap(mask,permutation):
 return sum(1<<permutation[i]for i in range(45)if mask>>i&1)
def counts_for(leaves):
 counts=Counter()
 for leaf in leaves:
  if 'node_cone'in leaf:counts['node_cone']+=1
  elif 'all_gradient'in leaf:counts['all_gradient']+=1
  else:counts.update(row['code']for row in leaf['patterns'])
 return counts
def propose(data,fixture=False):
 require(data.get('format')=='a5-n8-spatial-v1'and data.get('n')==8 and data.get('precision')==PREC,'wrong format/degree/precision')
 require(data.get('field_embedding')==embedding_record(),'wrong exact field embedding')
 require(data.get('metadata',{}).get('source_sha256')in(FROZEN_SOURCES['a5_n8_boxes.py'],CONTINUATION_SHA,PRODUCER_V5_SHA),'unsupported input producer')
 validate_new_provenance(data)
 require(not data.get('unresolved'),'unresolved input is outside this proposal protocol')
 nodes,L=construct();lookup={(j,k):i for i,(u,v,j,k)in enumerate(nodes)}
 permutation=[lookup[8-j,k]for u,v,j,k in nodes]
 require(all(permutation[permutation[i]]==i for i in range(45)),'node permutation is not involutive')
 for i,p in enumerate(L):
  reflected=s.Poly.from_dict({(a,b):((-1)**a)*c for(a,b),c in p.rep.to_dict().items()},(x,y),domain=K)
  require(reflected==L[permutation[i]],'cardinal equivariance identity failed')
 LT=list(map(terms,L));LX=[terms(p.diff(x))for p in L];LY=[terms(p.diff(y))for p in L]
 def masks(path):
  Q=pathbox(path);sg=[sign(centered(LT[i],LX[i],LY[i],*Q))for i in range(45)]
  ambiguous=[i for i,v in enumerate(sg)if not v];fixed=sum(1<<i for i,v in enumerate(sg)if v>0)
  return [fixed+sum(1<<i for j,i in enumerate(ambiguous)if bits>>j&1)for bits in range(1<<len(ambiguous))]
 left=[copy.deepcopy(row)for row in data['leaves']if row['path'].startswith('0')]
 require(left,'no supplied left-half leaves')
 left_pending=[p for p in data.get('pending_paths',[])if p.startswith('0')]
 if not fixture:
  require(not left_pending,'left half still has pending paths')
  prefix_partition([row['path'][1:]for row in left])

 def box(encoded):
  require(len(encoded)==2 and all(len(row)==2 for row in encoded),'box dimension')
  result=[]
  for row in encoded:
   values=[F(z)*S for z in row];require(all(v.denominator==1 for v in values),'box endpoints must be exact precision160 dyadics');result.append(tuple(v.numerator for v in values))
  return result
 def Cvalue(encoded):return [[F(z)for z in row]for row in encoded]
 from functools import lru_cache
 @lru_cache(None)
 def pdata(mask):
  p=sum(((1 if mask>>i&1 else -1)*L[i]for i in range(45)),s.Poly(0,x,y,domain=K))
  return terms(p.diff(x)),terms(p.diff(y)),terms(p.diff((x,2))),terms(p.diff(x).diff(y)),terms(p.diff((y,2)))
 def rootcheck(root):
  mask=root['mask'];R=box(root['R']);C=Cvalue(root['C']);A,B,Hxx,Hxy,Hyy=pdata(mask)
  require(all(-S<a<b<S for a,b in R),'root not strictly inside physical square')
  require(krawczyk(A,B,Hxx,Hxy,Hyy,C,R),'root Krawczyk/contraction predicate failed')
  xx,xy,yy=[evaluate(p,*R)for p in(Hxx,Hxy,Hyy)]
  require(xx[1]<0 and add(mul(xx,yy),neg(power(xy,2)))[0]>0,'root Hessian predicate failed')
  require(all(scale(evaluate(LT[i],*R),1 if mask>>i&1 else -1)[0]>0 for i in range(45)),'root strict-cardinal predicate failed')
  return R,C
 def reference(mask,record,Q,root):
  require(root['mask']==mask,'root-reference mask mismatch')
  U=box(record['U']);R=box(root['R']);C=Cvalue(root['C'])
  require(all(U[i][0]<=min(Q[i][0],R[i][0])and U[i][1]>=max(Q[i][1],R[i][1])for i in range(2)),'reference hull does not contain leaf/root')
  _,_,Hxx,Hxy,Hyy=pdata(mask);require(inject(Hxx,Hxy,Hyy,C,U)[0],'original whole-reference injectivity failed')
  return U
 restore_roots(data['interior_roots'])
 selected=[];old_to_new={};kinds={};axis_checks=[]
 for root in data['interior_roots']:
  R,C=rootcheck(root);lo,hi=R[0]
  if lo>0:continue
  if hi<0:kind='left'
  else:
   kind='axis';require(maskmap(root['mask'],permutation)==root['mask'],'axis-box mask is not exactly invariant')
   reflected=dict(root,mask=maskmap(root['mask'],permutation),R=reflected_box(root['R']),C=reflected_C(root['C']))
   TR,_=rootcheck(reflected);U=hull(R,TR);_,_,Hxx,Hxy,Hyy=pdata(root['mask']);ok,E=inject(Hxx,Hxy,Hyy,C,U)
   require(ok,'same-mask hull(R,TR) is not injective')
   norm=max(sum(max(abs(v)for v in E[i][j])for j in range(2))for i in range(2))
   axis_checks.append({'original_id':root['id'],'same_mask':True,'full_stored_and_reflected_root_predicates':True,'hull':encbox(U),'contraction_upper':str(F(norm,S))})
  copied=copy.deepcopy(root);copied['id']=len(selected);old_to_new[root['id']]=copied['id'];kinds[copied['id']]=kind;selected.append(copied)
 for leaf in left:
  for record in leaf.get('patterns',[]):
   if record['code']=='root':
    require(record['id']in old_to_new,'left leaf references an unsupported right root');record['id']=old_to_new[record['id']]
 roots=list(selected);mirror_ids={}
 for root in selected:
  if kinds[root['id']]=='axis':mirror_ids[root['id']]=root['id'];continue
  mirrored_root={'id':len(roots),'mask':maskmap(root['mask'],permutation),'R':reflected_box(root['R']),'C':reflected_C(root['C'])}
  rootcheck(mirrored_root);mirror_ids[root['id']]=mirrored_root['id'];roots.append(mirrored_root)
 for i,root in enumerate(roots):
  R=box(root['R'])
  for other in roots[:i]:
   T=box(other['R']);require(not all(max(R[a][0],T[a][0])<=min(R[a][1],T[a][1])for a in range(2)),'proposed distinct root boxes overlap')
 reference_checks=0;enlarged=0
 node_records=data['node_cones'];require(len(node_records)==45,'all45node records required')
 mirrored=[];ordinary_records=0
 for leaf in left:
  target={'path':reflected_path(leaf['path'])}
  require(pathbox(target['path'])==[(-pathbox(leaf['path'])[0][1],-pathbox(leaf['path'])[0][0]),pathbox(leaf['path'])[1]],'path reflection mismatch')
  if 'all_gradient'in leaf:target['all_gradient']=leaf['all_gradient']
  elif 'node_cone'in leaf:
   index=permutation[leaf['node_cone']];B=[[int(F(z)*S)for z in interval]for interval in node_records[index]['B']];Q=pathbox(target['path'])
   require(all(B[i][0]<Q[i][0]<=Q[i][1]<B[i][1]for i in range(2)),'mirrored leaf is not strictly inside actual node cube')
   target['node_cone']=index
  else:
   original_masks=masks(leaf['path']);require(len(original_masks)==len(leaf['patterns']),'original implicit mask count mismatch')
   rows=[]
   for mask,record in zip(original_masks,leaf['patterns']):
    transformed=copy.deepcopy(record)
    if record['code']=='root':
     reference(mask,record,pathbox(leaf['path']),roots[record['id']])
     target_id=mirror_ids[record['id']];target_root=roots[target_id];target_mask=maskmap(mask,permutation)
     candidate=box(reflected_box(record['U']));U=hull(candidate,box(target_root['R']))
     enlarged+=U!=candidate;transformed.update(id=target_id,U=encbox(U))
     reference(target_mask,transformed,pathbox(target['path']),target_root);reference_checks+=1
    elif record['code']=='regular_point':
     transformed['point']=[list(map(lambda q:str(-F(q)),record['point'][0])),list(record['point'][1])]
     transformed['C']=reflected_C(record['C']);transformed['U']=reflected_box(record['U'])
    rows.append((maskmap(mask,permutation),transformed))
   rows.sort(key=lambda pair:pair[0]);require([pair[0]for pair in rows]==masks(target['path']),'reflected implicit masks differ')
   target['patterns']=[pair[1]for pair in rows];ordinary_records+=len(rows)
  mirrored.append(target)
 leaves=left+mirrored;pending=left_pending+[reflected_path(p)for p in left_pending]
 if not fixture:prefix_partition([row['path']for row in leaves])
 counts=counts_for(leaves);interior_complete=not fixture and not pending
 summary={'complete':False,'interior_complete':interior_complete,'interior':len(roots),
  'unresolved':0,'pending':len(pending),'depth':max(map(lambda row:len(row['path']),leaves)),
  'node_leaves':counts['node_cone'],'all_gradient_leaves':counts['all_gradient'],
  'leaf_counts':dict(counts),'leaf_pattern_records':sum(v for k,v in counts.items()if k not in('node_cone','all_gradient')),
  'maximum_ambiguity':45,'seconds':0,'stats':{'visited':2*len(leaves)+len(pending)-1,'discard':len(leaves),'node_cone':counts['node_cone'],'all_gradient':counts['all_gradient']}}
 out={'format':'a5-n8-spatial-v1','n':8,'precision':PREC,'field_embedding':embedding_record(),'pattern_order':'compatible-mask',
  'node_cones':copy.deepcopy(node_records),'interior_roots':roots,'leaves':leaves,'pending_paths':pending,'unresolved':[],
  'summary':summary,'metadata':{'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'seed':None,
   'scope':'candidate witness reflection; every record requires unchanged independent replay','fixture_only':fixture,
   'input_source_sha256':data['metadata']['source_sha256'],'node_permutation':permutation,'axis_reuse':axis_checks,'reference_rechecks':reference_checks,'enlarged_reference_hulls':enlarged}}
 return out,{'exact_cardinal_identities':45,'source_left_leaves':len(left),'mirrored_leaves':len(mirrored),
  'mirrored_ordinary_records':ordinary_records,'retained_left_roots':sum(v=='left'for v in kinds.values()),'retained_axis_roots':sum(v=='axis'for v in kinds.values()),'proposed_roots':len(roots),'reference_rechecks':reference_checks,'enlarged_reference_hulls':enlarged,
  'left_complete':not left_pending,'fixture_only':fixture,'acceptance_predicate_added':False}

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('certificate');parser.add_argument('--input-sha256',required=True);parser.add_argument('--output',required=True);parser.add_argument('--fixture-only',action='store_true');parser.add_argument('--boundary',action='store_true');args=parser.parse_args()
 guards();raw=Path(args.certificate).read_bytes();require(hashlib.sha256(raw).hexdigest()==args.input_sha256,'actual input raw SHA mismatch');data=json.loads(gzip.decompress(raw)if raw.startswith(b'\x1f\x8b')else raw)
 out,receipt=propose(data,args.fixture_only);out['metadata']['input_sha256']=hashlib.sha256(raw).hexdigest();write_artifact(out,args.output)
 if args.boundary:
  require(out['summary']['interior_complete'],'boundary requires complete proposed interior')
  from a5_n8_boundary import boundaries
  e,c,bs,bu=boundaries();out['edges']=e;out['corners']=c;out['boundary_summary']=bs;out['unresolved'].extend(bu)
  out['summary'].update(edge=bs['edge'],corner=bs['corner'],total=len(out['interior_roots'])+bs['edge']+bs['corner'],complete=not bu)
  write_artifact(out,args.output)
 print(json.dumps(receipt,sort_keys=True),flush=True)
