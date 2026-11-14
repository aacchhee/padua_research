#!/usr/bin/env python3
"""Bounded encoding checks; no scientific code. --helper supports final rename.

Preregistered scope: independent row decode/rehash and metadata equality on the
actual index, malformed input rejection, backward compatibility, temporary CLI
checks and compaction. Changed-source CPU budget is 4.5 seconds including child processes.
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

ROOT=Path(__file__).resolve().parent.parent
ENCODING={'schema','columns','path_prefixes','files'}

def imported(path):
    spec=importlib.util.spec_from_file_location('tested_index',path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module

def serialized(document):
    return (json.dumps(document,separators=(',',':'),ensure_ascii=False,allow_nan=False)+'\n').encode()

def independent(document):
    result=[]
    for row in document['files']:
        if document['schema'].endswith('-v2'):
            path,n,digest=row
        else:
            i,suffix,n,encoded=row
            path=document['path_prefixes'][i]+suffix
            digest=base64.b64decode(encoded,validate=True).hex()
        result.append([path,n,digest])
    return sorted(result)

def main():
    resource.setrlimit(resource.RLIMIT_CPU,(4,4))
    started=time.process_time()
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--helper',type=Path,default=Path(__file__).with_name('evidence_index_v4_candidate.py'))
    args=parser.parse_args();helper=args.helper.resolve();h=imported(helper)
    index=ROOT/'evidence-manifest.json';original=index.read_bytes()
    document=json.loads(original);expected=independent(document)
    failures_checked=0
    def reject(doc):
        nonlocal failures_checked
        try:h.normalize(doc)
        except ValueError:failures_checked+=1
        else:raise AssertionError('accepted malformed document: '+repr(doc)[:250])
    v2={k:copy.deepcopy(v) for k,v in document.items() if k not in ENCODING}
    v2.update(schema=h.V2,columns=list(h.V2_COLUMNS),files=copy.deepcopy(expected))
    # Extra opaque metadata must survive exactly, including nested values.
    tagged=copy.deepcopy(v2);tagged['test_metadata']={'text':'λ', 'nested':[None,False,{'x':1}]}
    converted=h.compact_v4(document);newraw=serialized(converted)
    assert len(newraw)<len(original)<h.LIMIT
    for source in (v2,document,converted,tagged):
        before=independent(source);snapshot=copy.deepcopy(source)
        for transform in (h.compact,h.compact_v4):
            result=transform(source)
            assert independent(result)==before==h.normalize(result)
            assert {k:v for k,v in result.items() if k not in ENCODING}=={
                k:v for k,v in source.items() if k not in ENCODING}
            assert source==snapshot
    assert h.compact(document)['path_prefixes']==['','evidence/','code/']
    assert h.compact_v4(converted)==converted
    assert h.normalize(document)==expected
    # Independent all-file rehash: no helper verifier or scientific import.
    for path,n,digest in expected:
        raw=(ROOT/path).read_bytes()
        assert len(raw)==n and hashlib.sha256(raw).hexdigest()==digest,path
    h.verify_files(expected,ROOT,index)
    def changed(field,value,base=converted):
        doc=copy.deepcopy(base);doc[field]=value;reject(doc)
    for schema in ('unknown',None,4,True):changed('schema',schema)
    for value in (None,{},True):changed('files',value)
    for value in (True,-1,0,document['total_bytes']+1):changed('total_bytes',value)
    changed('columns',h.V2_COLUMNS)
    for prefixes in ([],['x/'],['',''],['',True],['','../'],['','a//'],['','a/./'],
                     ['','/a/'],['','a\\b/'],['','a\x00/'],['','//'],['','a/../b/']):
        changed('path_prefixes',prefixes)
    changed('path_prefixes',['','different/'],h.compact(v2))
    badv2=copy.deepcopy(v2);badv2['path_prefixes']=[''];reject(badv2)
    # Minimal synthetic rows isolate validation, including full path collisions.
    digest=base64.b64encode(bytes(32)).decode()
    small={'schema':h.V4,'columns':h.V3_COLUMNS,'path_prefixes':['','a/'],
           'files':[[1,'x',0,digest]],'total_bytes':0}
    assert h.normalize(small)==[['a/x',0,'00'*32]]
    for prefix,suffix,path in (('evidence/n3-','certificate.json','evidence/n3-certificate.json'),
                               ('evidence/post_audit_','D18.json','evidence/post_audit_D18.json'),
                               ('a','/x','a/x')):
        valid=copy.deepcopy(small);valid['path_prefixes']=['',prefix]
        valid['files']=[[1,suffix,0,digest]]
        assert h.normalize(valid)==[[path,0,'00'*32]]
    stems=copy.deepcopy(v2);stems['files']=[['evidence/n3-long-common-'+tail,0,'00'*32]
        for tail in ('alpha.json','beta.json','gamma.json')];stems['total_bytes']=0
    stemmed=h.compact_v4(stems)
    assert 'evidence/n3-long-common-' in stemmed['path_prefixes']
    assert independent(stemmed)==independent(stems)
    dotfiles=copy.deepcopy(stems)
    dotfiles['files']=[['a/.'+tail,0,'00'*32] for tail in ('first','second')]
    assert independent(h.compact_v4(dotfiles))==independent(dotfiles)
    # Unused unsafe prefixes are rejected before rows, including partial forms.
    for prefix in ('.','..','../bad','a/../bad','/absolute','a//bad','a/./bad','a\\bad','a\x00bad'):
        invalid=copy.deepcopy(small);invalid['path_prefixes'].append(prefix);reject(invalid)
    for row in ([],[1,'x',0], [True,'x',0,digest],[-1,'x',0,digest],[2,'x',0,digest],
                [1,'x',True,digest],[1,'x',-1,digest],[1,'x',h.LIMIT,digest],
                [1,'x',0,True]):
        changed('files',[row],small)
    for suffix in ('','/x','../x','x/../y','./x','x//y','x/','x\\y','x\x00'):
        changed('files',[[1,suffix,0,digest]],small)
    for encoded in ('',digest[:-1],digest+'=',digest.replace('=','=='),
                    base64.b64encode(bytes(31)).decode(),base64.b64encode(bytes(33)).decode(),
                    digest[:-2]+'B=', '-'+digest[1:],digest+'\n'):
        changed('files',[[1,'x',0,encoded]],small)
    changed('files',[[1,'x',0,digest],[0,'a/x',0,digest]],small)
    for path in ('/absolute','../escape','x//y','x/./y','x/../y'):
        doc=copy.deepcopy(v2);doc['files'][0][0]=path;reject(doc)
    for value in ('f'*63,'F'*64,'0'*65,None):
        doc=copy.deepcopy(v2);doc['files'][0][2]=value;reject(doc)
    for raw in ('{"a":1,"a":2}','{"x":NaN}','[]'):
        try:h.load(raw)
        except ValueError:failures_checked+=1
        else:raise AssertionError('accepted malformed JSON')
    # Actual helper CLI --check is read-only. Every mutation targets temp data.
    def cli(*arguments,ok=True):
        run=subprocess.run([sys.executable,str(helper),*map(str,arguments)],capture_output=True,text=True)
        assert (run.returncode==0)==ok,(arguments,run.stdout,run.stderr)
        return run
    cli('--check','--root',ROOT)
    with tempfile.TemporaryDirectory() as directory:
        root=Path(directory);(root/'a').mkdir();payload=b'check\n';(root/'a'/'file').write_bytes(payload)
        fixture={'schema':h.V2,'columns':h.V2_COLUMNS,'files':[
            ['a/file',len(payload),hashlib.sha256(payload).hexdigest()]],'total_bytes':len(payload),
            'metadata':{'opaque':[1,True,None]}}
        target=root/'evidence-manifest.json'
        # Deliberate whitespace allows each CLI action a strict improvement.
        padded=json.dumps(fixture,indent=8).encode();target.write_bytes(padded)
        cli('--compact-v4','--root',root)
        assert h.load(target.read_bytes())['schema']==h.V4
        assert independent(h.load(target.read_bytes()))==independent(fixture)
        stable=target.read_bytes();cli('--compact-v4','--root',root,ok=False)
        assert target.read_bytes()==stable
        # Simulate a concurrent index change at each pre-replace comparison.
        for changed_read in (2,3):
            target.write_bytes(padded);reads=0
            real_read=Path.read_bytes;old_argv=sys.argv
            def racing_read(path):
                nonlocal reads
                raw=real_read(path)
                if path==target:
                    reads+=1
                    if reads==changed_read:return raw+b' '
                return raw
            try:
                Path.read_bytes=racing_read
                sys.argv=[str(helper),'--compact-v4','--root',str(root)]
                try:h.main()
                except ValueError as exc:assert 'index changed' in str(exc)
                else:raise AssertionError('concurrent change accepted')
            finally:
                Path.read_bytes=real_read;sys.argv=old_argv
            assert target.read_bytes()==padded
            assert not list(root.glob('evidence-manifest.json.tmp-*'))
        target.write_bytes(padded);cli('--compact','--root',root)
        assert h.load(target.read_bytes())['schema']==h.V3
        stable=target.read_bytes();cli('--check','--compact-v4','--root',root,ok=False)
        assert target.read_bytes()==stable
        (root/'a'/'file').write_bytes(b'wrong')
        cli('--compact-v4','--root',root,ok=False);assert target.read_bytes()==stable
    assert index.read_bytes()==original,'actual index changed'
    cpu=time.process_time()-started+resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime+resource.getrusage(resource.RUSAGE_CHILDREN).ru_stime
    assert cpu<4.5, cpu
    print(json.dumps({'status':'PASS','entries':len(expected),'rehashed_files':len(expected),
        'rejections':failures_checked,'old_bytes':len(original),'v4_bytes':len(newraw),
        'prefixes':converted['path_prefixes'],'cpu_seconds':round(cpu,4),
        'helper_sha256':hashlib.sha256(helper.read_bytes()).hexdigest(),
        'checks_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}))

if __name__=='__main__':main()
