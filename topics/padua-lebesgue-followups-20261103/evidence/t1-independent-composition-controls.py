"""Adversarial identity/accounting controls; receipts are synthetic, not proofs."""
if not __debug__:raise RuntimeError('independent composition controls refuse optimized Python')
import argparse,contextlib,copy,hashlib,importlib.util,io,json,subprocess,sys,tempfile
from pathlib import Path

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--driver',required=True)
    ap.add_argument('--output',required=True);args=ap.parse_args()
    path=Path(args.driver).resolve();sys.path.insert(0,str(path.parent))
    spec=importlib.util.spec_from_file_location('composition_driver',path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    import a5_checker_n8_staged_cached as cache
    from t1_check_boundary import frozen_boundary_ast
    digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    before=digest(path);original_sha=m.sha;original_summary=m.summary_predicates
    driver_i=digest(path.with_name('t1_check.py'));driver_b=digest(path.with_name('t1_check_boundary.py'))
    old={'format':'a5-n8-spatial-v1','n':8,'precision':160,'pattern_order':'compatible-mask',
         'field_embedding':{},'metadata':{'source_sha256':'1'*64},
         'node_cones':[{'index':i}for i in range(45)],'interior_roots':[],
         'leaves':[{'path':'','all_gradient':0}],'pending_paths':[],'unresolved':[],
         'summary':{'interior_complete':True,'complete':False,'interior':0,'node_leaves':0,
                    'all_gradient_leaves':1,'leaf_counts':{'all_gradient':1},'leaf_pattern_records':0,'seconds':1,'Pcache':0}}
    boundary={'edges':[{'axis':a,'side':s,'patterns':[]}for a,s in((0,-1),(0,1),(1,-1),(1,1))],
              'corners':[{'point':[u,v],'kind':'node'}for u,v in((-1,-1),(-1,1),(1,-1),(1,1))],
              'summary':{'complete':True,'unresolved':0,'edge':0,'corner':0,'counts':{},'seconds':0},'unresolved':[],
              'metadata':{'source_sha256':'4'*64}}
    cases=('metadata_and_timing_only_positive','fresh_root_edit','fresh_embedding_edit','fresh_leaf_edit',
           'fresh_integer_to_float','fresh_non_diagnostic_summary_edit','joined_leaf_edit','joined_total_edit',
           'joined_boundary_edit','joined_incomplete_flag','interior_missing_flag','interior_boolean_to_integer',
           'interior_wrong_input','interior_wrong_source','interior_false_count_flag','interior_wrong_dispositions',
           'boundary_missing_flag','boundary_true_total_flag','boundary_wrong_field','boundary_wrong_method_ast',
           'boundary_wrong_source','boundary_wrong_count','boundary_wrong_dispositions',
           'duplicate_receipts','raw_input_hash_fault','source_changed_after','input_changed_after','receipt_changed_after',
           'join_boundary_raw_provenance','join_boundary_byte_provenance','join_boundary_source_provenance')
    rows=[]
    with tempfile.TemporaryDirectory(prefix='t1-independent-composition-')as directory:
        root=Path(directory)
        for case in cases:
            folder=root/case;folder.mkdir();data={'archived-interior':copy.deepcopy(old),'boundary':copy.deepcopy(boundary)}
            data['fresh-interior']=copy.deepcopy(old)
            data['fresh-interior']['metadata']={'source_sha256':'2'*64,'fresh_provenance':True}
            data['fresh-interior']['summary'].update(seconds=987,Pcache=456)
            if case=='fresh_root_edit':data['fresh-interior']['interior_roots'].append({'id':0})
            if case=='fresh_embedding_edit':data['fresh-interior']['field_embedding']['changed']=True
            if case=='fresh_leaf_edit':data['fresh-interior']['leaves'][0]['all_gradient']=1
            if case=='fresh_integer_to_float':data['fresh-interior']['n']=8.0
            if case=='fresh_non_diagnostic_summary_edit':data['fresh-interior']['summary']['new_count']=1
            paths={k:folder/(k+'.json')for k in data}
            for key in data:paths[key].write_bytes(m.canonical(data[key]))
            hashes={k:digest(p)for k,p in paths.items()}
            joined=copy.deepcopy(data['fresh-interior'])
            joined.update(edges=data['boundary']['edges'],corners=data['boundary']['corners'],boundary_summary=data['boundary']['summary'])
            joined['summary'].update(complete=True,edge=0,corner=0,total=0)
            joined['metadata']['source_sha256']='3'*64
            joined['metadata']['mechanical_join']={'interior_input_sha256':hashes['fresh-interior'],
               'interior_input_bytes':paths['fresh-interior'].stat().st_size,'boundary_input_sha256':hashes['boundary'],
               'boundary_input_bytes':paths['boundary'].stat().st_size,'interior_source_sha256':'2'*64,
               'boundary_source_sha256':'4'*64,'scope':'synthetic structural control only'}
            if case=='joined_leaf_edit':joined['leaves'][0]['all_gradient']=1
            if case=='joined_total_edit':joined['summary']['total']=1
            if case=='joined_boundary_edit':joined['edges'][0]['patterns']=[{'changed':True}]
            if case=='joined_incomplete_flag':joined['summary']['complete']=False
            if case=='join_boundary_raw_provenance':joined['metadata']['mechanical_join']['boundary_input_sha256']='0'*64
            if case=='join_boundary_byte_provenance':joined['metadata']['mechanical_join']['boundary_input_bytes']+=1
            if case=='join_boundary_source_provenance':joined['metadata']['mechanical_join']['boundary_source_sha256']='0'*64
            data['joined']=joined;paths['joined']=folder/'joined.json';paths['joined'].write_bytes(m.canonical(joined));hashes['joined']=digest(paths['joined'])
            ir={'interior_complete':True,'complete_prefix_partition':True,'verified_supplied_witnesses':True,
                'checker_source_unchanged':True,'execution_entry_source_unchanged':True,'input_unchanged':True,'count_only_scope':True,
                'accepted':False,'count_certified':False,'boundary_complete':False,
                'certificate_sha256':hashes['archived-interior'],'input_sha256_after':hashes['archived-interior'],
                'checker_sha256':m.staged.MAIN_SHA,'checker_sha256_after':m.staged.MAIN_SHA,
                'execution_entry_sha256':driver_i,'cached_evaluator_entry_sha256':cache.ENTRY_SHA_AT_IMPORT,
                'cached_evaluator_controls_sha256':cache.CONTROL_SHA_AT_IMPORT,
                'verified_leaves':1,'verified_patterns':0,'verified_interior_maxima_enclosures':0,'verified_node_leaves':0,
                'verified_node_records':45,'dispositions':{'all_gradient':1},'all_gradient_summary':{'leaves':1},
                'node_status_counts':{'accepted':45},'verified_direction_breakpoints':0,'accepted_node_cones':45,'root_values':{}}
            br={'boundary_verified':True,'all_boundary_predicates_replayed':True,'input_unchanged':True,
                'execution_entry_source_unchanged':True,'checker_source_unchanged':True,'interior_verified':False,
                'count_certified':False,'complete_closed_count':False,
                'boundary_input_sha256':hashes['boundary'],'boundary_input_sha256_after':hashes['boundary'],
                'field_certificate_sha256':hashes['archived-interior'],'field_certificate_sha256_after':hashes['archived-interior'],
                'checker_sha256':m.staged.MAIN_SHA,'checker_sha256_after':m.staged.MAIN_SHA,
                'execution_entry_sha256':driver_b,'boundary_method_ast_sha256':frozen_boundary_ast(),
                'cached_evaluator_entry_sha256':cache.ENTRY_SHA_AT_IMPORT,'cached_evaluator_controls_sha256':cache.CONTROL_SHA_AT_IMPORT,
                'boundary_result':{'verified_edge_maxima_enclosures':0,'verified_corner_maxima':0,'verified_edge_patterns':0,
                                   'corner_active_patterns':0,'edge_dispositions':{},'edge_roots':[],'corner_roots':[]}}
            if case=='interior_missing_flag':ir.pop('verified_supplied_witnesses')
            if case=='interior_boolean_to_integer':ir['interior_complete']=1
            if case=='interior_wrong_input':ir['certificate_sha256']='0'*64
            if case=='interior_wrong_source':ir['execution_entry_sha256']='0'*64
            if case=='interior_false_count_flag':ir['count_certified']=True
            if case=='interior_wrong_dispositions':ir['dispositions']={'gradient':1}
            if case=='boundary_missing_flag':br.pop('all_boundary_predicates_replayed')
            if case=='boundary_true_total_flag':br['complete_closed_count']=True
            if case=='boundary_wrong_field':br['field_certificate_sha256']='0'*64
            if case=='boundary_wrong_method_ast':br['boundary_method_ast_sha256']='0'*64
            if case=='boundary_wrong_source':br['execution_entry_sha256']='0'*64
            if case=='boundary_wrong_count':br['boundary_result']['verified_edge_maxima_enclosures']=1
            if case=='boundary_wrong_dispositions':br['boundary_result']['edge_dispositions']={'root':1}
            output=folder/'result.json';argv=[str(path)]
            for key,p in paths.items():argv+=['--'+key,str(p),'--'+key+'-sha256',hashes[key]]
            if case=='raw_input_hash_fault':argv[argv.index('--fresh-interior-sha256')+1]='0'*64
            receipt_paths=[]
            for kind,receipt in(('interior',ir),('boundary',br)):
                for i in(1,2):
                    value=dict(receipt,synthetic_fixture_run=i if case!='duplicate_receipts'else 1)
                    p=folder/(kind+str(i)+'.json');p.write_bytes(m.canonical(value));receipt_paths.append(p)
                    argv+=['--'+kind+'-receipt',str(p),'--'+kind+'-receipt-sha256',digest(p)]
            argv+=['--output',str(output)];saved_argv=sys.argv[:];sys.argv[:]=argv
            def altered_summary():
                result=original_summary()
                if case=='source_changed_after':
                    entry=path.read_bytes();m.sha=lambda raw:'0'*64 if raw==entry else original_sha(raw)
                if case=='input_changed_after':paths['fresh-interior'].write_bytes(b'changed input')
                if case=='receipt_changed_after':receipt_paths[0].write_bytes(b'changed receipt')
                return result
            m.summary_predicates=altered_summary
            try:
                try:
                    with contextlib.redirect_stdout(io.StringIO()):m.main()
                except (m.check.Rejected,ValueError,KeyError,TypeError)as error:
                    assert case!='metadata_and_timing_only_positive',(case,str(error))
                    assert not output.exists();failure=str(error)
                else:
                    assert case=='metadata_and_timing_only_positive',case
                    out=json.loads(output.read_text());assert out['composition_accounting_passed']
                    assert not out['count_certified']and not out['original_complete_run_executed']
                    assert out['requires_actual_distinct_agent_execution_record'];failure=None
                rows.append({'case':case,'passed':True,'failure':failure})
            finally:sys.argv[:]=saved_argv;m.sha=original_sha;m.summary_predicates=original_summary
    verify,ast_sha=m.summary_predicates()
    refusals=[]
    for flag in('-O','-OO'):
        run=subprocess.run([sys.executable,flag,str(path)],capture_output=True,text=True)
        assert run.returncode and 'refuse'in run.stderr;refusals.append(flag)
    assert digest(path)==before
    result={'all_controls_passed':True,'count_certified':False,
            'scope':'synthetic identity/accounting receipts only; no actual mathematical replay claimed',
            'driver_sha256':before,'driver_sha256_after':before,'original_summary_ast_sha256':ast_sha,
            'control_sha256':digest(__file__),'optimized_refusals':refusals,'rows':rows}
    Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps(result))
if __name__=='__main__':main()
