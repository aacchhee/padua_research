"""Propose ordinary N8 proof records by exact x reflection.

This adds no verifier predicate.  Every emitted record must be replayed by the
unchanged independent checker.  Full mode requires complete left-half coverage.
Fixture mode is explicitly incomplete and performs no search.
"""
import argparse,copy,gzip,hashlib,json,ast
from pathlib import Path
from collections import Counter
from a5_n8_field import *
from a5_n8_boxes import write_artifact
from a5_n8_continue import FROZEN_SOURCES,prefix_partition,pathbox,restore_roots,require

CONTINUATION_SHA='96ce015c9d3d161030be8d8d0de7e2c20f8e21d31b718948734703f3667476ad'
PRODUCER_V5_SHA='e1ad5f540ee67f785b79ba333d2bbf221f0f4f8956c93ce6ad9ad5d3b4140993'
ORIGINAL_REFLECT_SHA='84e3ca91689f671cb05f008d87cd4c1ce835392b715505070e5f45e60e166def'
def guards():
 folder=Path(__file__).resolve().parent
 for name,digest in FROZEN_SOURCES.items():
  require(hashlib.sha256((folder/name).read_bytes()).hexdigest()==digest,'frozen source changed: '+name)
 require(hashlib.sha256((folder/'a5_n8_continue.py').read_bytes()).hexdigest()==CONTINUATION_SHA,'continuation source changed')
 require(hashlib.sha256((folder/'a5_n8_continue_v5.py').read_bytes()).hexdigest()==PRODUCER_V5_SHA,'new producer source changed')
 require(hashlib.sha256((folder/'a5_n8_reflect.py').read_bytes()).hexdigest()==ORIGINAL_REFLECT_SHA,'original static proposer changed')
 def functions(path):return{n.name:n for n in ast.walk(ast.parse(path.read_text()))if isinstance(n,ast.FunctionDef)}
 original,versioned=functions(folder/'a5_n8_reflect.py'),functions(Path(__file__))
 for name,node in original.items():
  if name not in('guards','propose'):require(ast.dump(node,include_attributes=False)==ast.dump(versioned[name],include_attributes=False),'changed reflection transformation helper: '+name)
 def normalized(node):
  node=copy.deepcopy(node);body=[]
  for statement in node.body:
   if isinstance(statement,ast.Expr)and isinstance(statement.value,ast.Call)and isinstance(statement.value.func,ast.Name):
    call=statement.value
    if call.func.id=='validate_new_provenance':continue
    if call.func.id=='require'and call.args and isinstance(call.args[-1],ast.Constant)and call.args[-1].value=='unsupported input producer':continue
   body.append(statement)
  node.body=body;return ast.dump(node,include_attributes=False)
 require(normalized(original['propose'])==normalized(versioned['propose']),'mathematical proposal body changed')
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
 selected=[];old_to_new={}
 for root in data['interior_roots']:
  lo,hi=map(F,root['R'][0])
  require(not(lo<=0<=hi),'axis-crossing root requires a separate exact reuse proof')
  if hi<0:
   copied=copy.deepcopy(root);copied['id']=len(selected);old_to_new[root['id']]=copied['id'];selected.append(copied)
 for row in left:
  if 'patterns'in row:
   for record in row['patterns']:
    if record['code']=='root':
     require(record['id']in old_to_new,'left leaf references a non-left root; exact reuse proof required')
     record['id']=old_to_new[record['id']]
 roots=list(selected);offset=len(selected)
 for root in selected:
  roots.append({'id':offset+root['id'],'mask':maskmap(root['mask'],permutation),'R':reflected_box(root['R']),'C':reflected_C(root['C'])})
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
    if record['code']=='root':transformed.update(id=offset+record['id'],U=reflected_box(record['U']))
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
   'input_source_sha256':data['metadata']['source_sha256'],'node_permutation':permutation}}
 return out,{'exact_cardinal_identities':45,'source_left_leaves':len(left),'mirrored_leaves':len(mirrored),
  'mirrored_ordinary_records':ordinary_records,'retained_left_roots':len(selected),'proposed_roots':len(roots),
  'left_complete':not left_pending,'fixture_only':fixture,'acceptance_predicate_added':False}

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('certificate');parser.add_argument('--output',required=True);parser.add_argument('--fixture-only',action='store_true');parser.add_argument('--boundary',action='store_true');args=parser.parse_args()
 guards();raw=Path(args.certificate).read_bytes();data=json.loads(gzip.decompress(raw)if raw.startswith(b'\x1f\x8b')else raw)
 out,receipt=propose(data,args.fixture_only);out['metadata']['input_sha256']=hashlib.sha256(raw).hexdigest();write_artifact(out,args.output)
 if args.boundary:
  require(out['summary']['interior_complete'],'boundary requires complete proposed interior')
  from a5_n8_boundary import boundaries
  e,c,bs,bu=boundaries();out['edges']=e;out['corners']=c;out['boundary_summary']=bs;out['unresolved'].extend(bu)
  out['summary'].update(edge=bs['edge'],corner=bs['corner'],total=len(out['interior_roots'])+bs['edge']+bs['corner'],complete=not bu)
  write_artifact(out,args.output)
 print(json.dumps(receipt,sort_keys=True),flush=True)
