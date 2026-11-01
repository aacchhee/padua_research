"""Mechanically join complete ordinary interior/boundary proposals.

No mathematical predicate is trusted here.  The unchanged independent checker
must replay every component of the resulting ordinary certificate.
"""
import argparse,copy,gzip,hashlib,json,lzma,os,tempfile,ast
from collections import Counter
from pathlib import Path

BOUNDARY_SHA='6088db34cce2952332bd22e560c8b02e90446236f994dc2bac79b33717e769cb'
INTERIOR_SOURCES={'84e3ca91689f671cb05f008d87cd4c1ce835392b715505070e5f45e60e166def':'a5_n8_reflect.py',
 'a98e9eaccf64a736619e68781e3037aa90d9014c04e8b532ec85a20cf43978b5':'a5_n8_reflect_v5.py',
 'f77056651bb1bbf8eb3b154190eadad47ce33cbb3b793b4f32ae31f0834497e5':'a5_n8_reflect_axis.py'}
BASE_JOIN_SHA='a004f80c96ba75d78e6fff012c125e306c0d10bf9e625c859a177f17bd92e03e'
def require(condition,message):
 if not condition:raise ValueError(message)
def canonical(value):return json.dumps(value,separators=(',',':'),sort_keys=True).encode()
def sha(raw):return hashlib.sha256(raw).hexdigest()
def decode(raw):
 payload=gzip.decompress(raw)if raw.startswith(b'\x1f\x8b')else lzma.decompress(raw)if raw.startswith(b'\xfd7zXZ\x00')else raw
 def unique(pairs):
  result={}
  for key,value in pairs:
   require(key not in result,'duplicate JSON key');result[key]=value
  return result
 return json.loads(payload,object_pairs_hook=unique)
def integer(value):return type(value)is int and value>=0
def prefix_partition(paths):
 trie={}
 for path in paths:
  require(type(path)is str and len(path)<=44 and set(path)<=set('01'),'invalid path')
  node=trie
  for bit in path:
   require('_'not in node,'overlapping terminal prefix');node=node.setdefault(bit,{})
  require(not node,'duplicate/overlapping path');node['_']=True
 def full(node):return set(node)=={'_'}if'_'in node else set(node)=={'0','1'}and full(node['0'])and full(node['1'])
 require(full(trie),'interior prefix partition incomplete')
def components(boundary):return {k:boundary[k]for k in('edges','corners','summary')}
def validate_interior(data):
 require(data.get('format')=='a5-n8-spatial-v1'and type(data.get('n'))is int and data['n']==8 and data.get('precision')==160,'unsupported interior schema')
 require(data.get('pattern_order')=='compatible-mask','wrong implicit-mask ordering')
 source=data.get('metadata',{}).get('source_sha256');require(source in INTERIOR_SOURCES,'unsupported interior proposal source')
 require(not any(k in data for k in('edges','corners','boundary_summary')),'interior already has boundary fields')
 summary=data['summary'];require(summary.get('interior_complete')is True and summary.get('complete')is False,'interior is not a complete unjoined proposal')
 require(data.get('pending_paths')==[]and data.get('unresolved')==[],'interior still has pending/unresolved cases')
 leaves=data['leaves'];prefix_partition([r['path']for r in leaves]);counts=Counter()
 for leaf in leaves:
  require(set(leaf)in({'path','node_cone'},{'path','all_gradient'},{'path','patterns'}),'unsupported leaf encoding')
  if'node_cone'in leaf:counts['node_cone']+=1
  elif'all_gradient'in leaf:counts['all_gradient']+=1
  else:counts.update(row['code']for row in leaf['patterns'])
 require(summary.get('leaf_counts')==dict(counts),'interior leaf accounting mismatch')
 require(summary.get('node_leaves')==counts['node_cone']and summary.get('all_gradient_leaves')==counts['all_gradient'],'direct leaf accounting mismatch')
 require(summary.get('leaf_pattern_records')==sum(v for k,v in counts.items()if k not in('node_cone','all_gradient')),'ordinary record accounting mismatch')
 roots=data['interior_roots'];require([r['id']for r in roots]==list(range(len(roots)))and all(type(r['id'])is int for r in roots),'interior root ids are not consecutive integers')
 require(integer(summary.get('interior'))and summary['interior']==len(roots),'interior count mismatch')
 require(len(data['node_cones'])==45 and all(type(r.get('index'))is int and r['index']==i for i,r in enumerate(data['node_cones'])),'missing/index-mismatched node records')
 return source,len(roots)
def validate_boundary(data):
 require(data.get('unresolved')==[],'boundary has unresolved cases')
 summary=data['summary'];require(summary.get('complete')is True and summary.get('unresolved')==0,'boundary is incomplete')
 edges=data['edges'];require(type(edges)is list and len(edges)==4,'four edges required')
 require(all(type(e.get('axis'))is int and type(e.get('side'))is int for e in edges),'edge coordinates must be integers')
 require([(e['axis'],e['side'])for e in edges]==[(0,-1),(0,1),(1,-1),(1,1)],'physical edge list/order mismatch')
 counts=Counter();ids=[]
 for edge in edges:
  for row in edge['patterns']:
   if row['kind']=='flat':counts['flat']+=1;continue
   require(row['kind']=='roots','unsupported edge pattern')
   for point in row['points']:
    code=point['code'];require(code in('outside','derivative','minimum','sign','root','normal'),'unresolved/unsupported edge disposition');counts[code]+=1
    if code=='root':ids.append(point['id'])
 require(all(type(i)is int for i in ids)and ids==list(range(len(ids))),'edge root ids mismatch')
 corners=data['corners'];require([tuple(c['point'])for c in corners]==[(-1,-1),(-1,1),(1,-1),(1,1)],'physical corner list/order mismatch')
 require(all(c['kind']in('node','max')for c in corners),'unsupported corner disposition')
 corner_ids=[c['id']for c in corners if c['kind']=='max']
 require(all(type(i)is int for i in corner_ids)and corner_ids==list(range(len(corner_ids))),'corner ids mismatch')
 require(integer(summary.get('edge'))and summary['edge']==len(ids)and integer(summary.get('corner'))and summary['corner']==len(corner_ids),'boundary count mismatch')
 require(summary.get('counts')==dict(counts),'boundary disposition accounting mismatch')
 return len(ids),len(corner_ids)
def join_data(interior,boundary,identity):
 source,ninterior=validate_interior(interior);nedge,ncorner=validate_boundary(boundary)
 out=copy.deepcopy(interior);out['edges']=copy.deepcopy(boundary['edges']);out['corners']=copy.deepcopy(boundary['corners']);out['boundary_summary']=copy.deepcopy(boundary['summary'])
 out['summary'].update(edge=nedge,corner=ncorner,total=ninterior+nedge+ncorner,complete=True)
 out['metadata']['source_sha256']=sha(Path(__file__).read_bytes())
 out['metadata']['mechanical_join']=dict(identity,interior_source_sha256=source,boundary_source_sha256=BOUNDARY_SHA,scope='literal ordinary components; complete flag is structural, independent mathematical replay required')
 copied={'edges':out['edges'],'corners':out['corners'],'summary':out['boundary_summary']}
 require(canonical(copied)==canonical(components(boundary)),'copied boundary payload changed')
 return out,{'schema_complete':True,'count_certified':False,'independent_checker_required':True,'boundary_components_sha256':sha(canonical(copied))}
def write_atomic(path,payload):
 path=Path(path)
 if path.exists():require(path.read_bytes()==payload,'refusing to overwrite different output');return
 temporary=None
 try:
  with tempfile.NamedTemporaryFile(mode='wb',dir=path.resolve().parent,prefix=path.name+'.',suffix='.tmp',delete=False)as stream:
   temporary=stream.name;stream.write(payload);stream.flush();os.fsync(stream.fileno())
  os.replace(temporary,path);temporary=None
 finally:
  if temporary is not None:os.unlink(temporary)
def guards(source):
 folder=Path(__file__).resolve().parent
 require(sha((folder/'a5_n8_join.py').read_bytes())==BASE_JOIN_SHA,'frozen base joiner changed')
 def functions(path):return{n.name:n for n in ast.walk(ast.parse(path.read_text()))if isinstance(n,ast.FunctionDef)}
 original,current=functions(folder/'a5_n8_join.py'),functions(Path(__file__))
 for name in('canonical','decode','integer','prefix_partition','components','validate_interior','validate_boundary','join_data','write_atomic'):
  require(ast.dump(original[name],include_attributes=False)==ast.dump(current[name],include_attributes=False),'literal join behavior changed: '+name)
 require(sha((folder/'a5_n8_boundary.py').read_bytes())==BOUNDARY_SHA,'frozen boundary source changed')
 require(source in INTERIOR_SOURCES and sha((folder/INTERIOR_SOURCES[source]).read_bytes())==source,'frozen interior source changed')
def run(interior_path,boundary_path,interior_sha,boundary_sha,output):
 iraw=Path(interior_path).read_bytes();braw=Path(boundary_path).read_bytes()
 require(sha(iraw)==interior_sha and sha(braw)==boundary_sha,'raw input SHA mismatch')
 interior,boundary=decode(iraw),decode(braw);guards(interior.get('metadata',{}).get('source_sha256'))
 identity={'base_joiner_sha256':BASE_JOIN_SHA,'interior_input_sha256':interior_sha,'interior_input_bytes':len(iraw),'boundary_input_sha256':boundary_sha,'boundary_input_bytes':len(braw)}
 out,receipt=join_data(interior,boundary,identity);payload=gzip.compress(canonical(out),mtime=0);write_atomic(output,payload)
 decoded=decode(Path(output).read_bytes());require(decoded==out,'joined serialization changed data')
 require(canonical({'edges':decoded['edges'],'corners':decoded['corners'],'summary':decoded['boundary_summary']})==canonical(components(boundary)),'copied payload changed after serialization')
 return dict(receipt,**identity,output_path=str(output),output_bytes=len(payload),output_sha256=sha(payload),joiner_sha256=sha(Path(__file__).read_bytes()))
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('interior');parser.add_argument('boundary');parser.add_argument('--interior-sha256',required=True);parser.add_argument('--boundary-sha256',required=True);parser.add_argument('--output',required=True);parser.add_argument('--receipt',required=True);args=parser.parse_args()
 receipt=run(args.interior,args.boundary,args.interior_sha256,args.boundary_sha256,args.output);write_atomic(args.receipt,json.dumps(receipt,indent=2,sort_keys=True).encode()+b'\n');print(json.dumps(receipt,sort_keys=True),flush=True)
