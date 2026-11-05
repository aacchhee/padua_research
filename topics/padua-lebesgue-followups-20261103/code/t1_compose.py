"""Typed proof-input identity and literal frozen accounting, not a full replay.

Actual original interior and boundary executions are external proved dependencies.
This program never creates a fake Verifier or claims to execute Verifier.run.
"""
if not __debug__:
    raise RuntimeError('T1 composition refuses optimized Python')
import argparse,ast,copy,hashlib,json,sys
from collections import namedtuple
from pathlib import Path
from t1_payload import canonical,proof_payload
FROZEN=Path(__file__).resolve().parents[2]/'padua-proof-attempts-2-20261101'/'code'
sys.path.insert(0,str(FROZEN))
import a5_checker_n8_staged as staged
check=staged.check
require=check.require


def sha(raw):return hashlib.sha256(raw).hexdigest()

def load(path,expected):
    require(staged.valid_sha(expected),'invalid expected SHA256')
    raw=Path(path).read_bytes();require(sha(raw)==expected,'wrong raw hash: '+str(path))
    return raw,staged.load_json(raw)

def exact_integer(value):return type(value)is int and value>=0


def summary_predicates():
    """Original summary block, with only its self variable renamed to facts."""
    raw=Path(check.__file__).read_bytes();require(sha(raw)==staged.MAIN_SHA,'wrong frozen checker')
    module=ast.parse(raw);cls=next(n for n in module.body if isinstance(n,ast.ClassDef)and n.name=='Verifier')
    run=next(n for n in cls.body if isinstance(n,ast.FunctionDef)and n.name=='run')
    start=next(i for i,n in enumerate(run.body)if isinstance(n,ast.Assign)and any(isinstance(t,ast.Name)and t.id=='summary'for t in n.targets))
    stop=next(i for i,n in enumerate(run.body[start:],start)if isinstance(n,ast.Expr)and isinstance(n.value,ast.Call)and isinstance(n.value.func,ast.Name)and n.value.func.id=='require'and n.value.args and ast.dump(n.value.args[0],include_attributes=False)==ast.dump(ast.parse('allow_partial or complete',mode='eval').body,include_attributes=False))
    body=copy.deepcopy(run.body[start:stop+1]);original_dump=ast.dump(ast.Module(body=body,type_ignores=[]),include_attributes=False)
    reads={n.attr for n in ast.walk(ast.Module(body=body,type_ignores=[]))if isinstance(n,ast.Attribute)and isinstance(n.value,ast.Name)and n.value.id=='self'}
    require(reads=={'node_leaves','all_gradient_leaves','patterns','roots','dispositions'},'summary dependencies changed')
    require(not any(isinstance(n,ast.Attribute)and isinstance(n.value,ast.Name)and n.value.id=='self'and not isinstance(n.ctx,ast.Load)for n in ast.walk(ast.Module(body=body,type_ignores=[]))),'summary mutates accounting facts')
    class Rename(ast.NodeTransformer):
        def visit_Name(self,node):
            if node.id=='self':node.id='facts'
            return node
    body=Rename().visit(ast.Module(body=body,type_ignores=[])).body
    # Confirm this is solely a bound-variable rename, not a predicate change.
    inverse=copy.deepcopy(ast.Module(body=body,type_ignores=[]))
    for n in ast.walk(inverse):
        if isinstance(n,ast.Name)and n.id=='facts':n.id='self'
    require(ast.dump(inverse,include_attributes=False)==original_dump,'summary AST changed beyond rename')
    function=ast.parse('def verify(certificate,facts,boundary_result,complete):\n allow_partial=False\n').body[0]
    function.body+=body+ast.parse('return expected_summary').body
    namespace=dict(vars(check));exec(compile(ast.fix_missing_locations(ast.Module(body=[function],type_ignores=[])),'<literal-frozen-accounting>','exec'),namespace)
    return namespace['verify'],sha(original_dump.encode())


def interior_receipt(data,certificate,input_sha,driver_sha):
    for key in('interior_complete','complete_prefix_partition','verified_supplied_witnesses','checker_source_unchanged','execution_entry_source_unchanged','input_unchanged','count_only_scope'):
        require(data.get(key)is True,'missing positive interior obligation: '+key)
    for key in('accepted','count_certified','boundary_complete'):
        require(data.get(key)is False,'wrong interior-only flag: '+key)
    require(data.get('certificate_sha256')==data.get('input_sha256_after')==input_sha,'interior input binding')
    require(data.get('checker_sha256')==data.get('checker_sha256_after')==staged.MAIN_SHA,'interior checker identity')
    require(data.get('execution_entry_sha256')==driver_sha,'interior execution entry identity')
    import a5_checker_n8_staged_cached as cache
    require(data.get('cached_evaluator_entry_sha256')==cache.ENTRY_SHA_AT_IMPORT and data.get('cached_evaluator_controls_sha256')==cache.CONTROL_SHA_AT_IMPORT,'interior frozen cache identity')
    summary=certificate['summary']
    pairs={'verified_leaves':len(certificate['leaves']),'verified_patterns':summary['leaf_pattern_records'],
           'verified_interior_maxima_enclosures':len(certificate['interior_roots']),'verified_node_leaves':summary['node_leaves'],
           'verified_node_records':len(certificate['node_cones'])}
    for key,value in pairs.items():require(exact_integer(data.get(key))and data[key]==value,'interior accounting mismatch: '+key)
    require(canonical(data['dispositions'])==canonical(summary['leaf_counts']),'interior leaf dispositions mismatch')
    require(exact_integer(data['all_gradient_summary']['leaves'])and data['all_gradient_summary']['leaves']==summary['all_gradient_leaves'],'interior universal count mismatch')
    require(summary['interior']==pairs['verified_interior_maxima_enclosures'],'interior root summary mismatch')
    return {key:data[key]for key in('verified_patterns','verified_node_leaves','verified_interior_maxima_enclosures','dispositions','all_gradient_summary','node_status_counts','verified_node_records','verified_direction_breakpoints','accepted_node_cones','root_values')}


def boundary_receipt(data,input_sha,field_sha,driver_sha):
    for key in('boundary_verified','all_boundary_predicates_replayed','input_unchanged','execution_entry_source_unchanged','checker_source_unchanged'):
        require(data.get(key)is True,'missing positive boundary obligation: '+key)
    for key in('interior_verified','count_certified','complete_closed_count'):
        require(data.get(key)is False,'wrong boundary-only flag: '+key)
    require(data.get('boundary_input_sha256')==data.get('boundary_input_sha256_after')==input_sha,'boundary input binding')
    require(data.get('field_certificate_sha256')==data.get('field_certificate_sha256_after')==field_sha,'boundary field binding')
    require(data.get('checker_sha256')==data.get('checker_sha256_after')==staged.MAIN_SHA and data.get('execution_entry_sha256')==driver_sha,'boundary source identity')
    from t1_check_boundary import frozen_boundary_ast
    require(data.get('boundary_method_ast_sha256')==frozen_boundary_ast(),'boundary method AST identity')
    import a5_checker_n8_staged_cached as cache
    require(data.get('cached_evaluator_entry_sha256')==cache.ENTRY_SHA_AT_IMPORT and data.get('cached_evaluator_controls_sha256')==cache.CONTROL_SHA_AT_IMPORT,'boundary frozen cache identity')
    result=data['boundary_result']
    for key in('verified_edge_maxima_enclosures','verified_corner_maxima','verified_edge_patterns','corner_active_patterns'):
        require(exact_integer(result.get(key)),'malformed boundary count: '+key)
    return result


def main():
    ap=argparse.ArgumentParser()
    for key in('archived-interior','fresh-interior','boundary','joined'):
        ap.add_argument('--'+key,required=True);ap.add_argument('--'+key+'-sha256',required=True)
    for key in('interior-receipt','boundary-receipt'):
        ap.add_argument('--'+key,action='append',required=True);ap.add_argument('--'+key+'-sha256',action='append',required=True)
    ap.add_argument('--interior-driver-source',default=str(Path(__file__).with_name('t1_check.py')))
    ap.add_argument('--boundary-driver-source',default=str(Path(__file__).with_name('t1_check_boundary.py')))
    ap.add_argument('--output',required=True);args=ap.parse_args();own=sha(Path(__file__).read_bytes())
    import a5_checker_n8_staged_cached as cache
    source_paths=[Path(__file__),Path(__file__).with_name('t1_payload.py'),Path(__file__).with_name('t1_check_boundary.py'),Path(args.interior_driver_source),Path(args.boundary_driver_source),Path(check.__file__),staged.HERE,cache.HERE,cache.CONTROL_PATH]
    source_before={str(p.resolve()):sha(p.read_bytes())for p in source_paths}
    require(cache.ENTRY_SHA_AT_IMPORT==sha(cache.HERE.read_bytes()),'cached entry changed before composition')
    staged.guard_sources();inputs={};identities={}
    for key in('archived_interior','fresh_interior','boundary','joined'):
        raw,data=load(getattr(args,key),getattr(args,key+'_sha256'));inputs[key]=data
        identities[key]=dict(path=getattr(args,key),sha256=sha(raw),bytes=len(raw))
    old,fresh,boundary,joined=(inputs[k]for k in('archived_interior','fresh_interior','boundary','joined'))
    staged.validate_interior_input(old);staged.validate_interior_input(fresh)
    old_proof,old_removed=proof_payload(old);fresh_proof,fresh_removed=proof_payload(fresh)
    require(canonical(old_proof)==canonical(fresh_proof),'fresh interior proof-input identity failed: full fresh replay required')
    staged.validate_final_interior(fresh,joined,args.fresh_interior_sha256,identities['fresh_interior']['bytes'])
    copied={'edges':joined['edges'],'corners':joined['corners'],'summary':joined['boundary_summary']}
    require(canonical(copied)==canonical({k:boundary[k]for k in('edges','corners','summary')}),'joined boundary differs from checked artifact')
    provenance=joined['metadata']['mechanical_join']
    require(provenance['boundary_input_sha256']==args.boundary_sha256 and provenance['boundary_input_bytes']==identities['boundary']['bytes']and provenance['boundary_source_sha256']==boundary['metadata']['source_sha256'],'join boundary raw/source provenance mismatch')
    require(boundary.get('unresolved')==[],'unresolved boundary')
    driver_hashes=dict(interior=sha(Path(args.interior_driver_source).read_bytes()),boundary=sha(Path(args.boundary_driver_source).read_bytes()))
    facts=[];boundary_results=[];receipt_ids=[]
    for kind,target in(('interior',facts),('boundary',boundary_results)):
        paths=getattr(args,kind+'_receipt');digests=getattr(args,kind+'_receipt_sha256')
        require(len(paths)==len(digests)==2 and len(set(digests))==2,'two distinct pinned '+kind+' receipts required')
        for path,digest in zip(paths,digests):
            raw,data=load(path,digest);receipt_ids.append(dict(kind=kind,path=path,sha256=digest,bytes=len(raw)))
            if kind=='interior':target.append(interior_receipt(data,old,args.archived_interior_sha256,driver_hashes[kind]))
            else:target.append(boundary_receipt(data,args.boundary_sha256,args.archived_interior_sha256,driver_hashes[kind]))
        require(canonical(target[0])==canonical(target[1]),'independent '+kind+' replay facts disagree')
    fact=facts[0];result=boundary_results[0]
    Facts=namedtuple('PreviouslyVerifiedAccountingFacts','node_leaves all_gradient_leaves patterns roots dispositions')
    # This is read-only accounting, NOT a Verifier or reconstructed replay state.
    accounting=Facts(fact['verified_node_leaves'],fact['all_gradient_summary']['leaves'],fact['verified_patterns'],tuple(range(fact['verified_interior_maxima_enclosures'])),fact['dispositions'])
    complete_partition=check.partition([leaf['path']for leaf in joined['leaves']])
    no_unresolved=not joined.get('unresolved')and not joined.get('pending_paths')
    interior_complete=complete_partition and no_unresolved
    boundary_complete='edges'in joined and 'corners'in joined
    complete=interior_complete and boundary_complete
    require(complete,'joined certificate is structurally incomplete')
    verify,summary_ast=summary_predicates();counts=verify(joined,accounting,result,complete)
    for key,identity in identities.items():require(sha(Path(identity['path']).read_bytes())==identity['sha256'],'input changed after identity checks')
    for identity in receipt_ids:require(sha(Path(identity['path']).read_bytes())==identity['sha256'],'receipt changed')
    require(driver_hashes['interior']==sha(Path(args.interior_driver_source).read_bytes())and driver_hashes['boundary']==sha(Path(args.boundary_driver_source).read_bytes()),'execution-source blob changed')
    require(all(sha(Path(p).read_bytes())==h for p,h in source_before.items()),'composition/helper source changed');staged.guard_sources()
    output=dict(format='t1-proof-identity-accounting-composition-v1',composition_accounting_passed=True,
        fresh_interior_mathematical_payload_identical=True,literal_join_components_identical=True,
        complete_prefix_partition=complete_partition,interior_structurally_complete=interior_complete,boundary_fields_present=boundary_complete,
        original_complete_run_executed=False,count_certified=False,
        scope='typed identity and original summary predicates compose separately executed complete interior and boundary proofs; not an executed full joined Verifier.run',
        requires_actual_distinct_agent_execution_record=True,counts_from_verified_strata=counts,
        inputs=identities,replay_receipts=receipt_ids,execution_driver_source_sha256=driver_hashes,
        mathematical_interior_payload_sha256=sha(canonical(old_proof)),excluded_old_fields=sorted(old_removed),excluded_fresh_fields=sorted(fresh_removed),
        excluded_old_fields_sha256=sha(canonical(old_removed)),excluded_fresh_fields_sha256=sha(canonical(fresh_removed)),
        original_summary_ast_sha256=summary_ast,checker_sha256=staged.MAIN_SHA,source_sha256=own,
        source_unchanged=True,all_inputs_unchanged=True,used_source_sha256=source_before)
    staged.atomic_json(args.output,output);print(json.dumps(output,sort_keys=True),flush=True)
if __name__=='__main__':main()
