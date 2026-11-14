#!/usr/bin/env python3
"""Capacity-only metadata checks, preregistered at <=2 CPU seconds.

No scientific code imported. Temporary index files use the actual topic root
only to resolve existing evidence; actual evidence and manifest remain untouched.
"""
import argparse
import base64
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import subprocess
import sys
import tempfile
import time
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent.parent

def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    result=importlib.util.module_from_spec(spec);spec.loader.exec_module(result)
    return result

def dump(document):
    return (json.dumps(document,separators=(',',':'),ensure_ascii=False)+'\n').encode()

def main():
    resource.setrlimit(resource.RLIMIT_CPU,(2,2));started=time.process_time()
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--helper',type=Path,default=Path(__file__).with_name('evidence_index_capacity_candidate.py'))
    args=parser.parse_args();helper=args.helper.resolve()
    h=module(helper,'candidate');baseline_path=Path(__file__).with_name('evidence_index.py')
    baseline=module(baseline_path,'baseline')
    baseline_raw=baseline_path.read_bytes();candidate_raw=helper.read_bytes()
    # Reviewable exact patch, allowing the checker to run after adoption too.
    expected=baseline_raw.replace(b'LIMIT=16384\n',b'LIMIT=16384\nINDEX_LIMIT=32768\n')
    expected=expected.replace(b"len(original)<LIMIT,'index reaches/exceeds16KiB'",b"len(original)<INDEX_LIMIT,'index reaches/exceeds32KiB'")
    expected=expected.replace(b"len(candidate)<LIMIT,'compact index reaches/exceeds16KiB'",b"len(candidate)<INDEX_LIMIT,'compact index reaches/exceeds32KiB'")
    if not hasattr(baseline,'INDEX_LIMIT'):assert candidate_raw==expected
    assert h.LIMIT==16384 and h.INDEX_LIMIT==32768
    index=ROOT/'evidence-manifest.json';original=index.read_bytes();document=json.loads(original)
    independent=[]
    for row in document['files']:
        if document['schema']==h.V2:path,n,digest=row
        else:
            prefix,suffix,n,encoded=row
            path=document['path_prefixes'][prefix]+suffix
            digest=base64.b64decode(encoded,validate=True).hex()
        raw=(ROOT/path).read_bytes()
        assert len(raw)==n and hashlib.sha256(raw).hexdigest()==digest
        independent.append([path,n,digest])
    independent.sort();assert h.normalize(document)==baseline.normalize(document)==independent
    before=copy.deepcopy(document)
    for transform in ('compact','compact_v4'):
        new=getattr(h,transform)(document);old=getattr(baseline,transform)(document)
        assert new==old and h.normalize(new)==independent
        assert {k:v for k,v in new.items() if k not in {'schema','columns','path_prefixes','files'}}=={
            k:v for k,v in document.items() if k not in {'schema','columns','path_prefixes','files'}}
    assert document==before
    v2={k:v for k,v in document.items() if k not in {'schema','columns','path_prefixes','files'}}
    v2.update(schema=h.V2,columns=h.V2_COLUMNS,files=independent)
    for version in (v2,baseline.compact(v2),document):
        assert h.normalize(version)==baseline.normalize(version)==independent
    commands=0
    def cli(target,action='--check',ok=True):
        nonlocal commands
        run=subprocess.run([sys.executable,str(helper),action,'--root',str(ROOT),str(target)],capture_output=True,text=True)
        assert (run.returncode==0)==ok,(run.stdout,run.stderr)
        commands+=1;return run
    with tempfile.TemporaryDirectory(prefix='index-capacity-check-',dir=ROOT) as folder:
        target=Path(folder)/'index.json'
        def sized(size):
            padded=copy.deepcopy(document);padded['capacity_test_padding']=''
            padded['capacity_test_padding']='x'*(size-len(dump(padded)))
            raw=dump(padded);assert len(raw)==size;return raw
        target.write_bytes(sized(16385));cli(target)
        target.write_bytes(sized(32767));cli(target)
        for size in (32768,32769):
            target.write_bytes(sized(size));run=cli(target,ok=False)
            assert '32KiB' in run.stderr
        # Both compact action guards: serialized output can exceed the old cap,
        # and must still be strictly below the new cap.
        for action,transform in (('--compact',h.compact),('--compact-v4',h.compact_v4)):
            source=copy.deepcopy(v2);source['capacity_test_padding']=''
            source['capacity_test_padding']='x'*max(0,22000-len(dump(transform(source))))
            compacted=dump(transform(source));assert 16384<len(compacted)<32768
            target.write_bytes(json.dumps(source,indent=4).encode())
            cli(target,action);assert target.read_bytes()==compacted
            source['capacity_test_padding']='x'*33000
            padded=json.dumps(source,indent=4).encode();target.write_bytes(padded)
            run=cli(target,action,ok=False)
            assert '32KiB' in run.stderr and target.read_bytes()==padded
        # Evidence remains strictly below 16KiB at both independent guards.
        evidence=Path(folder)/'oversize.bin';raw=b'x'*16384;evidence.write_bytes(raw)
        relative=evidence.relative_to(ROOT).as_posix();digest=hashlib.sha256(raw).hexdigest()
        oversized={'schema':h.V2,'files':[[relative,16384,digest]],'total_bytes':16384}
        try:h.normalize(oversized)
        except ValueError as exc:assert 'oversize' in str(exc)
        else:raise AssertionError('16KiB declared evidence accepted')
        try:h.verify_files([[relative,16384,digest]],ROOT,target)
        except ValueError as exc:assert 'byte mismatch' in str(exc)
        else:raise AssertionError('16KiB physical evidence accepted')
        evidence.write_bytes(raw[:-1]);digest=hashlib.sha256(raw[:-1]).hexdigest()
        h.verify_files([[relative,16383,digest]],ROOT,target)
    assert index.read_bytes()==original
    cpu=time.process_time()-started+resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime+resource.getrusage(resource.RUSAGE_CHILDREN).ru_stime
    assert cpu<2,cpu
    print(json.dumps({'status':'PASS','entries':len(independent),'rehashed_files':len(independent),
        'index_bytes':len(original),'cli_checks':commands,'cpu_seconds':round(cpu,4),
        'baseline_sha256':hashlib.sha256(baseline_raw).hexdigest(),
        'candidate_sha256':hashlib.sha256(candidate_raw).hexdigest(),
        'checks_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}))

if __name__=='__main__':main()
