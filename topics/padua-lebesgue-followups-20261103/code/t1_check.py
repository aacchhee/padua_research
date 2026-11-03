"""Count-only execution of frozen Verifier.run with its frozen exact cache.

No verifier predicate or run method changes. Successful receipt is published
atomically only after frozen and wrapper source/input after-hashes pass.
"""
if not __debug__:
    raise RuntimeError('T1 refuses optimized Python: t1_check.py')
import hashlib,json,os,sys,tempfile
from pathlib import Path
FROZEN=Path(__file__).resolve().parents[2]/'padua-proof-attempts-2-20261101'/'code'
sys.path.insert(0,str(FROZEN))
import a5_checker_n8_staged_cached as cached

def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    own=digest(__file__);arguments=sys.argv[:]
    input_path=Path(sys.argv[1]);input_before=digest(input_path)
    output_index=sys.argv.index('--output')+1;output=Path(sys.argv[output_index])
    with tempfile.NamedTemporaryFile(dir=output.resolve().parent,prefix=output.name+'.',suffix='.unpublished',delete=False)as f:
        temporary=Path(f.name)
    try:
        sys.argv[output_index]=str(temporary)
        cached.install();cached.guard_entry()
        result=cached.check.main()
        cached.guard_entry()
        assert digest(__file__)==own,'wrapper source changed'
        assert digest(input_path)==input_before,'input changed during replay'
        data=json.loads(temporary.read_text())
        assert data['certificate_sha256']==input_before,'frozen receipt input binding mismatch'
        data.update(execution_entry_sha256=own,execution_entry_source_unchanged=True,
                    cached_evaluator_entry_sha256=cached.ENTRY_SHA_AT_IMPORT,
                    cached_evaluator_controls_sha256=cached.CONTROL_SHA_AT_IMPORT,
                    runtime_evaluate_backend='frozen bit-identical cached monomials and per-term rounding',
                    runtime_evaluate_cache=cached.monomials.cache_info()._asdict(),
                    input_sha256_after=input_before,input_unchanged=True,count_only_scope=True)
        with temporary.open('w')as f:
            f.write(json.dumps(data,indent=2,sort_keys=True)+'\n');f.flush();os.fsync(f.fileno())
        os.replace(temporary,output)
        return result
    finally:
        sys.argv[:]=arguments
        if temporary.exists():temporary.unlink()
if __name__=='__main__':raise SystemExit(main())
