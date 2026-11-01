"""Structural controls for staged scheduling; no N8 mathematical acceptance."""
import argparse
from collections import Counter
import copy
from datetime import datetime, timezone, timedelta
import hashlib
import json
from pathlib import Path
import tempfile
import time

HERE = Path(__file__).resolve()
BEFORE = hashlib.sha256(HERE.read_bytes()).hexdigest()
DRIVER_PATH = HERE.with_name('a5_checker_n8_staged.py')
DRIVER_BEFORE = hashlib.sha256(DRIVER_PATH.read_bytes()).hexdigest()
import a5_checker_n8_staged as d

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    start = time.monotonic()
    d.guard_sources()
    controls = []
    def reject(name, action):
        try:
            action()
        except (d.check.Rejected, ValueError, OSError) as error:
            controls.append({'name': name, 'rejected': True, 'reason': str(error)})
        else:
            raise RuntimeError('invalid staged structure accepted: ' + name)
    original = {'format':'a5-n8-spatial-v1','n':8,'precision':160,
                'field_embedding':{'fixture':'not mathematical data'},'pattern_order':'compatible-mask',
                'interior_roots':[{'id':0,'mask':1,'R':[['-1/2','-1/3'],['0','1/8']]}],
                'leaves':[{'path':'','patterns':[{'code':'gradient'}]}],
                'node_cones':[{'fixture':True}], 'unresolved':[], 'pending_paths':[],
                'metadata':{'source_sha256':'0'*64,'scope':'structural fixture'},
                'summary':{'complete':False,'interior_complete':True,'interior':1,'node_leaves':0,
                           'all_gradient_leaves':0,'leaf_pattern_records':0,'leaf_counts':{},'seconds':0}}
    interior_raw=d.canonical(original);interior_sha=d.sha(interior_raw)
    final=copy.deepcopy(original)
    final.update(edges=[],corners=[],boundary_summary={'complete':True,'unresolved':0,'edge':0,'corner':0,'counts':{}})
    final['summary'].update(complete=True,edge=0,corner=0,total=1)
    final['metadata']['source_sha256']='1'*64
    final['metadata']['mechanical_join']={'interior_input_sha256':interior_sha,'interior_input_bytes':len(interior_raw),
        'boundary_input_sha256':'2'*64,'boundary_input_bytes':10,'interior_source_sha256':'0'*64,
        'boundary_source_sha256':'3'*64,'scope':'structural join'}
    d.validate_interior_input(original)
    d.validate_final_interior(original,final,interior_sha,len(interior_raw))
    controls.append({'name':'unchanged_typed_interior_with_only_allowed_join_changes','accepted':True})
    def final_case(name, change):
        altered=copy.deepcopy(final);change(altered)
        reject(name,lambda:d.validate_final_interior(original,altered,interior_sha,len(interior_raw)))
    for key in ('field_embedding','interior_roots','leaves','node_cones','pending_paths','unresolved','format','pattern_order','precision'):
        final_case('changed_interior_'+key,lambda x,k=key:x.__setitem__(k,{'changed':True}))
    final_case('integer_to_equal_float_is_not_identity',lambda x:x.__setitem__('n',8.0))
    final_case('root_ID_integer_to_boolean_is_not_identity',lambda x:x['interior_roots'][0].__setitem__('id',False))
    final_case('unknown_final_top_field',lambda x:x.__setitem__('unchecked',1))
    final_case('missing_final_boundary_field',lambda x:x.pop('corners'))
    for key in ('interior','seconds','leaf_counts','interior_complete'):
        final_case('changed_forbidden_summary_'+key,lambda x,k=key:x['summary'].__setitem__(k,'changed'))
    final_case('final_complete_flag_still_false',lambda x:x['summary'].__setitem__('complete',False))
    final_case('changed_original_metadata',lambda x:x['metadata'].__setitem__('scope','changed'))
    final_case('unknown_metadata_key',lambda x:x['metadata'].__setitem__('extra',1))
    final_case('wrong_join_interior_binding',lambda x:x['metadata']['mechanical_join'].__setitem__('interior_input_sha256','4'*64))
    final_case('unknown_join_provenance_key',lambda x:x['metadata']['mechanical_join'].__setitem__('unchecked',1))
    altered=copy.deepcopy(original);altered['pending_paths']=['0']
    reject('pending_original_interior',lambda:d.validate_interior_input(altered))
    altered2=copy.deepcopy(original);altered2['edges']=[]
    reject('stage1_already_contains_boundary',lambda:d.validate_interior_input(altered2))
    reject('expired_deadline',lambda:d.check_deadline(datetime.now(timezone.utc)-timedelta(seconds=1)))
    tail=d.extracted_tail()
    controls.append({'name':'exact_frozen_source_and_original_tail_AST_extracted','accepted':True,'tail_ast_sha256':d.TAIL_AST_SHA})
    reject('modified_frozen_tail_source_bytes',lambda:d.extracted_tail(d.MAIN_PATH.read_bytes()+b'\n'))
    class StructuralStub:
        # This stub tests only scheduling/guards of the copied AST, never math.
        def __init__(self):
            self.roots={0:{'value':['1','2']}};self.patterns=0;self.node_leaves=0
            self.dispositions=Counter();self.all_gradient_leaves=0;self.all_gradient_masks=0
            self.all_gradient_axes=Counter();self.all_gradient_methods=Counter();self.calls=0
        def boundaries(self,edges,corners):
            self.calls+=1
            return {'verified_edge_maxima_enclosures':0,'verified_corner_maxima':0,
                    'edge_dispositions':{},'edge_roots':[],'corner_roots':[]}
    stub=StructuralStub()
    result=tail(stub,final,False,{},final['leaves'],True)
    d.require(result['count_certified']is True and stub.calls==1,'structural tail callback/control failed')
    controls.append({'name':'unchanged_tail_guard_flow_on_nonmathematical_stub','accepted':True,'scope':'structural only; no N8 count'})
    for name,change in (('pending_tail_final',lambda x:x['pending_paths'].append('0')),
                        ('false_tail_complete',lambda x:x['summary'].__setitem__('complete',False)),
                        ('wrong_tail_count',lambda x:x['summary'].__setitem__('total',2)),
                        ('wrong_tail_boundary_summary',lambda x:x['boundary_summary'].__setitem__('edge',1))):
        altered=copy.deepcopy(final);change(altered)
        reject(name,lambda a=altered:tail(StructuralStub(),a,False,{},a['leaves'],True))
    with tempfile.TemporaryDirectory(prefix='a5-checker-n8-staged-controls-')as directory:
        folder=Path(directory);cp=folder/'count.json';gp=folder/'global.json';rp=folder/'ready.json'
        cr=d.canonical(final);gr=d.canonical({'fixture':'structural global binding only'})
        cp.write_bytes(cr);gp.write_bytes(gr)
        ready={'format':'a5-n8-staged-ready-v1','interior_sha256':interior_sha,
               'certificate_path':str(cp),'certificate_sha256':d.sha(cr),
               'global_path':str(gp),'global_sha256':d.sha(gr)}
        rp.write_bytes(d.canonical(ready));loaded=d.load_ready(rp,interior_sha)
        d.require(loaded[2]==cr and loaded[3]==gr,'READY positive binding failed')
        controls.append({'name':'READY_binds_exact_raw_pair_and_original_interior','accepted':True})
        reject('missing_READY',lambda:d.load_ready(folder/'missing.json',interior_sha))
        for key,value in (('format','wrong'),('interior_sha256','5'*64),
                          ('certificate_sha256','6'*64),('global_sha256','7'*64)):
            bad=dict(ready);bad[key]=value;rp.write_bytes(d.canonical(bad))
            reject('wrong_READY_'+key,lambda:d.load_ready(rp,interior_sha))
        rp.write_bytes(b'{"format":"x","format":"y"}')
        reject('duplicate_READY_JSON_key',lambda:d.load_ready(rp,interior_sha))
        rp.write_bytes(d.canonical(ready));gp.write_bytes(gr+b' ')
        reject('global_file_changed_after_READY',lambda:d.load_ready(rp,interior_sha))
        gp.write_bytes(gr);cp.write_bytes(cr+b' ')
        reject('count_file_changed_after_READY',lambda:d.load_ready(rp,interior_sha))
        output=folder/'atomic.json';d.atomic_json(output,{'same':1});d.atomic_json(output,{'same':1})
        reject('different_atomic_receipt_cannot_overwrite_history',lambda:d.atomic_json(output,{'same':2}))
    d.guard_sources()
    after=hashlib.sha256(HERE.read_bytes()).hexdigest();driver_after=hashlib.sha256(DRIVER_PATH.read_bytes()).hexdigest()
    unchanged=BEFORE==after and DRIVER_BEFORE==driver_after==d.DRIVER_SHA_AT_IMPORT
    d.require(unchanged,'staged source changed during controls')
    result={'format':'a5-n8-staged-structural-controls-v1','all_controls_passed':True,
            'scope':'structural scheduling/identity/AST/READY controls only; no mathematical N8 acceptance',
            'controls':controls,'controls_sha256':BEFORE,'controls_sha256_after':after,
            'driver_sha256':DRIVER_BEFORE,'driver_sha256_after':driver_after,
            'sources_unchanged':unchanged,'checker_sha256':d.MAIN_SHA,'frozen_controls_sha256':d.CONTROLS_SHA,
            'seconds':time.monotonic()-start,'count_certified':False}
    d.atomic_json(args.output,result);print(json.dumps(result,sort_keys=True),flush=True)

if __name__=='__main__':
    main()
