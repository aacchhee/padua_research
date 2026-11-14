#!/usr/bin/env python3
"""Independent single-process capacity-only review; temporary writes only."""
import base64, contextlib, copy, hashlib, importlib.util, io, json
from pathlib import Path
import resource, sys, tempfile, time
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent.parent

def main():
    resource.setrlimit(resource.RLIMIT_CPU,(2,2));started=time.process_time()
    base=ROOT/'code/evidence_index.py';candidate=ROOT/'code/evidence_index_capacity_candidate.py'
    prior=base.read_bytes();new=candidate.read_bytes()
    assert hashlib.sha256(new).hexdigest()=='d9d4590d59f44cbfc1627a4a0cab0b6bda398f327c0e755eb0c19c48aa063e2f'
    assert hashlib.sha256((ROOT/'code/evidence_index_capacity_checks.py').read_bytes()).hexdigest()=='30a80befd96e47275436f1be78425e8efe1177e96429713d53505348ed6fdbcd'
    expected=prior.replace(b'LIMIT=16384\n',b'LIMIT=16384\nINDEX_LIMIT=32768\n')
    for name in ('original','candidate'):
        expected=expected.replace(('len('+name+")<LIMIT,'" ).encode(),('len('+name+")<INDEX_LIMIT,'").encode())
    expected=expected.replace(b'index reaches/exceeds16KiB',b'index reaches/exceeds32KiB')
    assert expected==new
    def load(path,name):
        spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
    old=load(base,'old');h=load(candidate,'new');assert h.LIMIT==16384 and h.INDEX_LIMIT==32768
    index=ROOT/'evidence-manifest.json';raw=index.read_bytes();doc=json.loads(raw)
    rows=sorted([[doc['path_prefixes'][i]+s,n,base64.b64decode(d,validate=True).hex()] for i,s,n,d in doc['files']])
    assert len(rows)==194
    for p,n,d in rows:
        b=(ROOT/p).read_bytes();assert len(b)==n and hashlib.sha256(b).hexdigest()==d
    assert h.normalize(doc)==old.normalize(doc)==rows
    ignored={'schema','columns','files','path_prefixes'}
    for fn in ('compact','compact_v4'):
        result=getattr(h,fn)(doc);assert result==getattr(old,fn)(doc)
        assert {k:v for k,v in result.items() if k not in ignored}=={k:v for k,v in doc.items() if k not in ignored}
    count=0
    with tempfile.TemporaryDirectory() as directory:
        root=Path(directory);target=root/'evidence-manifest.json'
        def invoke(action,ok):
            nonlocal count
            argv=sys.argv
            try:
                sys.argv=['helper',action,'--root',str(root)]
                try:
                    with contextlib.redirect_stdout(io.StringIO()):h.main()
                except ValueError as exc:
                    assert not ok and '32KiB' in str(exc),str(exc)
                else:assert ok
            finally:sys.argv=argv
            count+=1
        empty={'schema':h.V2,'files':[],'total_bytes':0,'opaque':''}
        def packed(d):return (json.dumps(d,separators=(',',':'),ensure_ascii=False)+'\n').encode()
        for size,ok in ((16385,True),(32767,True),(32768,False)):
            source=copy.deepcopy(empty);source['opaque']='x'*(size-len(packed(source)))
            b=packed(source);assert len(b)==size;target.write_bytes(b);invoke('--check',ok);assert target.read_bytes()==b
        for action,fn in (('--compact',h.compact),('--compact-v4',h.compact_v4)):
            for size,ok in ((32767,True),(32768,False)):
                source=copy.deepcopy(empty);source['opaque']='x'*(size-len(packed(fn(source))))
                out=packed(fn(source));assert len(out)==size
                before=json.dumps(source,indent=32).encode();assert len(before)>size
                target.write_bytes(before);invoke(action,ok)
                assert target.read_bytes()==(out if ok else before)
        file=root/'payload'
        for size in (16383,16384):
            b=b'x'*size;file.write_bytes(b);row=['payload',size,hashlib.sha256(b).hexdigest()]
            d={'schema':h.V2,'files':[row],'total_bytes':size}
            for check in (lambda:h.normalize(d),lambda:h.verify_files([row],root,target)):
                try:check()
                except ValueError:assert size==16384
                else:assert size==16383
    assert base.read_bytes()==prior and index.read_bytes()==raw
    cpu=time.process_time()-started;assert cpu<2
    print(json.dumps({'status':'PASS','rows_rehashed':len(rows),'index_bytes':len(raw),'cli_main_cases':count,
        'cpu_seconds':round(cpu,6),'candidate_sha256':hashlib.sha256(new).hexdigest(),
        'index_sha256':hashlib.sha256(raw).hexdigest(),'review_checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}))
if __name__=='__main__':main()
