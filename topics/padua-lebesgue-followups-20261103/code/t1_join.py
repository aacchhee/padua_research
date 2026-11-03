"""Literal component join; full frozen mathematical replay remains mandatory."""
import argparse,copy,gzip,hashlib,json,sys
from pathlib import Path
FROZEN=Path(__file__).resolve().parents[2]/'padua-proof-attempts-2-20261101'/'code'
sys.path.insert(0,str(FROZEN))
import a5_n8_join_axis as base
BASE_SHA='bee99288a67fd7fd007bf587ea62cb5e4a91cbf000c60d2fe0eb81d465179581'
# Filled from physical sources at invocation; every input source must be one of
# these frozen implementations, never a guessed source label.
SOURCES=['a5_n8_boxes.py','a5_n8_continue.py','a5_n8_continue_v5.py','a5_n8_reflect_axis.py']

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser();ap.add_argument('interior');ap.add_argument('boundary');ap.add_argument('--interior-sha256',required=True);ap.add_argument('--boundary-sha256',required=True);ap.add_argument('--output',required=True);ap.add_argument('--receipt',required=True);a=ap.parse_args()
    own=sha(__file__);base_before=sha(base.__file__);assert base_before==BASE_SHA;boundary_source=Path(__file__).with_name('t1_boundary.py');boundary_before=sha(boundary_source)
    iraw=Path(a.interior).read_bytes();braw=Path(a.boundary).read_bytes()
    assert base.sha(iraw)==a.interior_sha256 and base.sha(braw)==a.boundary_sha256,'wrong raw input hash'
    interior=base.decode(iraw);boundary=base.decode(braw)
    allowed={sha(FROZEN/name):name for name in SOURCES};base.INTERIOR_SOURCES.update(allowed)
    source,ninterior=base.validate_interior(interior);nedge,ncorner=base.validate_boundary(boundary)
    assert boundary.get('metadata',{}).get('source_sha256')==boundary_before,'wrong boundary producer identity'
    assert boundary['metadata']['frozen_boundary_sha256']==sha(FROZEN/'a5_n8_boundary.py'),'wrong boundary frozen ancestry'
    out=copy.deepcopy(interior)
    out.update(edges=copy.deepcopy(boundary['edges']),corners=copy.deepcopy(boundary['corners']),boundary_summary=copy.deepcopy(boundary['summary']))
    out['summary'].update(edge=nedge,corner=ncorner,total=ninterior+nedge+ncorner,complete=True)
    out['metadata']['source_sha256']=own
    out['metadata']['mechanical_join']=dict(interior_input_sha256=a.interior_sha256,interior_input_bytes=len(iraw),boundary_input_sha256=a.boundary_sha256,boundary_input_bytes=len(braw),interior_source_sha256=source,boundary_source_sha256=boundary_before,base_joiner_sha256=base_before,scope='literal ordinary components; structural completeness only; every mathematical predicate requires frozen independent replay')
    for key in('field_embedding','pattern_order','interior_roots','format','n','precision','node_cones','unresolved','pending_paths','leaves'):
        assert base.canonical(out[key])==base.canonical(interior[key]),'interior component changed'
    assert base.canonical({'edges':out['edges'],'corners':out['corners'],'summary':out['boundary_summary']})==base.canonical(base.components(boundary)),'boundary component changed'
    assert own==sha(__file__)and base_before==sha(base.__file__)and boundary_before==sha(boundary_source)
    assert base.sha(Path(a.interior).read_bytes())==a.interior_sha256 and base.sha(Path(a.boundary).read_bytes())==a.boundary_sha256
    payload=gzip.compress(base.canonical(out),mtime=0);base.write_atomic(a.output,payload)
    assert base.decode(Path(a.output).read_bytes())==out
    receipt=dict(joiner_sha256=own,base_joiner_sha256=base_before,output_sha256=base.sha(payload),output_bytes=len(payload),interior_sha256=a.interior_sha256,boundary_sha256=a.boundary_sha256,interior=ninterior,edge=nedge,corner=ncorner,total=ninterior+nedge+ncorner,structural_complete=True,count_certified=False,scope='mechanical join only; all original finite predicates still require independent replay')
    base.write_atomic(a.receipt,json.dumps(receipt,indent=2,sort_keys=True).encode()+b'\n');print(json.dumps(receipt),flush=True)
if __name__=='__main__':main()
