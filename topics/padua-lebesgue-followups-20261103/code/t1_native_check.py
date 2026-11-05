"""Full frozen Verifier.run with truthful optional native endpoint accumulation."""
if not __debug__:
    raise RuntimeError('T1 native checker refuses optimized Python')
import hashlib,json,os,sys,tempfile
from pathlib import Path
import _t1_native
import t1_native_check_backend as native
cached=native.cached;check=native.check

def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    arguments=sys.argv[:];original_evaluate=check.evaluate
    check.require('--native-build-receipt'in sys.argv,'native build receipt required')
    index=sys.argv.index('--native-build-receipt');check.require(index+1<len(sys.argv),'missing build receipt path')
    receipt=Path(sys.argv[index+1]);del sys.argv[index:index+2]
    input_path=Path(sys.argv[1]);input_before=digest(input_path)
    output_index=sys.argv.index('--output')+1;output=Path(sys.argv[output_index])
    own=Path(__file__).resolve();code=own.parent
    paths=[own,Path(native.__file__),code/'t1_native.c',code/'t1_native_build.py',Path(_t1_native.__file__),receipt,cached.HERE,cached.CONTROL_PATH]
    before={str(p.resolve()):digest(p)for p in paths}
    build=json.loads(receipt.read_text())
    check.require(build['source_sha256']==digest(code/'t1_native.c'),'native C/build source mismatch')
    check.require(build['binary_sha256']==digest(_t1_native.__file__)and Path(build['binary_path']).resolve()==Path(_t1_native.__file__).resolve(),'native binary/build mismatch')
    check.require(build['python']==sys.version and build['build_script_sha256']==digest(code/'t1_native_build.py'),'native build runtime/script mismatch')
    def guard():
        cached.ORIGINAL_GUARD()
        check.require(all(digest(p)==sha for p,sha in before.items()),'native checker source/binary/build changed')
        check.require(check.evaluate is native.evaluate,'native checker runtime evaluator changed')
    with tempfile.NamedTemporaryFile(dir=output.resolve().parent,prefix=output.name+'.',suffix='.unpublished',delete=False)as f:temporary=Path(f.name)
    try:
        sys.argv[output_index]=str(temporary);check.evaluate=native.evaluate;guard()
        result=check.main();guard()
        check.require(digest(input_path)==input_before,'input changed during replay')
        data=json.loads(temporary.read_text())
        check.require(data['certificate_sha256']==input_before,'frozen receipt input binding mismatch')
        data.update(execution_entry_sha256=before[str(own)],execution_entry_source_unchanged=True,
          native_sources_and_binary_sha256=before,native_build=build,
          runtime_evaluate_backend='frozen cached monomials, fresh coefficient snapshot, exact CPython PyLong ordered endpoint sums',
          runtime_evaluate_cache=cached.monomials.cache_info()._asdict(),native_table_view_cache=native.table_view.cache_info()._asdict(),
          input_sha256_after=input_before,input_unchanged=True,count_only_scope=True)
        with temporary.open('w')as f:f.write(json.dumps(data,indent=2,sort_keys=True)+'\n');f.flush();os.fsync(f.fileno())
        os.replace(temporary,output);return result
    finally:
        check.evaluate=original_evaluate;sys.argv[:]=arguments
        if temporary.exists():temporary.unlink()
if __name__=='__main__':raise SystemExit(main())
