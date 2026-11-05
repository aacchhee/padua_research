"""Replay every frozen open-edge/corner predicate; no interior/total claim."""
if not __debug__:
    raise RuntimeError('T1 boundary replay refuses optimized Python')
import argparse,ast,hashlib,json,sys,time
from pathlib import Path
FROZEN=Path(__file__).resolve().parents[2]/'padua-proof-attempts-2-20261101'/'code'
sys.path.insert(0,str(FROZEN))
import a5_checker_n8_staged_cached as cached
check=cached.check
ORIGINAL_VERIFIER=check.Verifier
ORIGINAL_BOUNDARY=check.Verifier.boundaries

def sha(raw):return hashlib.sha256(raw).hexdigest()

def frozen_boundary_ast():
    module=ast.parse(Path(check.__file__).read_bytes())
    cls=next(n for n in module.body if isinstance(n,ast.ClassDef)and n.name=='Verifier')
    method=next(n for n in cls.body if isinstance(n,ast.FunctionDef)and n.name=='boundaries')
    names={n.attr for n in ast.walk(method)if isinstance(n,ast.Attribute)and isinstance(n.value,ast.Name)and n.value.id=='self'}
    check.require(names=={'cardinals','edge_flat_values','exact_pattern'},'boundary state dependencies changed')
    return sha(ast.dump(method,include_attributes=False).encode())

def replay(args):
    started=time.monotonic();own=sha(Path(__file__).read_bytes())
    field_raw=Path(args.field_certificate).read_bytes();raw=Path(args.boundary).read_bytes()
    check.require(sha(field_raw)==args.field_certificate_sha256 and sha(raw)==args.boundary_sha256,'wrong raw input hash')
    original=cached.staged.load_json(field_raw);boundary=cached.staged.load_json(raw)
    check.require(boundary.get('unresolved')==[],'boundary has unresolved records')
    check.require(check.Verifier is ORIGINAL_VERIFIER and check.Verifier.boundaries is ORIGINAL_BOUNDARY,'boundary runtime changed before replay')
    cached.install();cached.guard_entry();method=ORIGINAL_BOUNDARY;method_ast=frozen_boundary_ast()
    verifier=check.Verifier(original['field_embedding'])
    check.require(verifier.edge_flat_values==[],'nonempty initial edge-only state')
    result=verifier.boundaries(boundary['edges'],boundary['corners'])
    # These are the exact boundary-summary conjuncts in original Verifier.run.
    summary=boundary['summary']
    check.require(summary.get('complete')is True and summary.get('unresolved')==0 and
                  summary.get('edge')==result['verified_edge_maxima_enclosures'] and
                  summary.get('corner')==result['verified_corner_maxima'] and
                  summary.get('counts')==result['edge_dispositions'],'boundary summary mismatch')
    cached.guard_entry()
    check.require(check.Verifier.boundaries is method and frozen_boundary_ast()==method_ast,'boundary method changed')
    check.require(own==sha(Path(__file__).read_bytes()),'entry source changed')
    check.require(sha(Path(args.field_certificate).read_bytes())==sha(field_raw)and sha(Path(args.boundary).read_bytes())==sha(raw),'input changed during replay')
    receipt=dict(format='t1-frozen-boundary-replay-v1',boundary_verified=True,all_boundary_predicates_replayed=True,
        interior_verified=False,count_certified=False,complete_closed_count=False,
        scope='all four open edges and all four corners through unchanged frozen Verifier.boundaries; no interior or total count execution',
        boundary_result=result,field_embedding_result=verifier.embedding_result,
        boundary_input_sha256=sha(raw),boundary_input_bytes=len(raw),boundary_input_sha256_after=sha(raw),
        field_certificate_sha256=sha(field_raw),field_certificate_bytes=len(field_raw),field_certificate_sha256_after=sha(field_raw),
        input_unchanged=True,execution_entry_sha256=own,execution_entry_source_unchanged=True,
        checker_sha256=check.SOURCE_SHA_AT_IMPORT,checker_sha256_after=sha(Path(check.__file__).read_bytes()),
        checker_source_unchanged=True,boundary_method_ast_sha256=method_ast,
        cached_evaluator_entry_sha256=cached.ENTRY_SHA_AT_IMPORT,cached_evaluator_controls_sha256=cached.CONTROL_SHA_AT_IMPORT,
        runtime_evaluate_backend='frozen bit-identical cached monomials and per-term rounding',
        runtime_evaluate_cache=cached.monomials.cache_info()._asdict(),
        python=check.platform.python_version(),sympy=check.sp.__version__,python_flint=check.flint.__version__,FLINT=check.flint.__FLINT_VERSION__,
        python_optimize_flag=sys.flags.optimize,seconds=time.monotonic()-started)
    cached.ORIGINAL_ATOMIC(args.output,receipt)
    print(json.dumps(receipt,sort_keys=True),flush=True)
    return receipt

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--field-certificate',required=True);ap.add_argument('--field-certificate-sha256',required=True)
    ap.add_argument('--boundary',required=True);ap.add_argument('--boundary-sha256',required=True);ap.add_argument('--output',required=True)
    replay(ap.parse_args())
if __name__=='__main__':main()
