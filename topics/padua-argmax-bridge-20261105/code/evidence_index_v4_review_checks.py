#!/usr/bin/env python3
"""Independent bounded V4 audit; temporary writes only, --helper for adoption."""
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

ROOT = Path(__file__).resolve().parent.parent
ENC = {'schema', 'columns', 'path_prefixes', 'files'}

def packed(d):
    return (json.dumps(d, ensure_ascii=False, separators=(',', ':'), allow_nan=False)+'\n').encode()

def decode(d):
    if d['schema'].endswith('-v2'):
        return sorted(copy.deepcopy(d['files']))
    return sorted([[d['path_prefixes'][i]+s,n,base64.b64decode(b,validate=True).hex()]
                   for i,s,n,b in d['files']])

def main():
    resource.setrlimit(resource.RLIMIT_CPU, (2,2))
    start=time.process_time()
    parser=argparse.ArgumentParser()
    parser.add_argument('--helper',type=Path,default=Path(__file__).with_name('evidence_index_v4_candidate.py'))
    args=parser.parse_args()
    spec=importlib.util.spec_from_file_location('reviewed',args.helper)
    h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
    index=ROOT/'evidence-manifest.json';raw=index.read_bytes()
    oldhelper=Path(__file__).with_name('evidence_index.py');oldbytes=oldhelper.read_bytes()
    original=json.loads(raw);rows=decode(original)
    for p,n,d in rows:
        target=(ROOT/p).resolve()
        assert target.is_relative_to(ROOT.resolve()) and target!=index.resolve()
        b=target.read_bytes();assert len(b)==n and hashlib.sha256(b).hexdigest()==d
    v2={k:copy.deepcopy(v) for k,v in original.items() if k not in ENC}
    v2.update(schema=h.V2,columns=h.V2_COLUMNS,files=rows)
    v4=h.compact_v4(original)
    for source in (v2,original,v4):
        snapshot=copy.deepcopy(source)
        for fn in (h.compact,h.compact_v4):
            out=fn(source)
            assert decode(out)==rows==h.normalize(out)
            assert {k:v for k,v in out.items() if k not in ENC}=={k:v for k,v in source.items() if k not in ENC}
        assert source==snapshot
    assert len(rows)==176 and len(packed(v4))==14554 and len(v4['path_prefixes'])==18
    assert h.compact_v4(v4)==v4
    # Brute serialized-byte oracle; independently reconstruct LCPs and choices.
    paths=sorted([f'folder/{i:02}-λ\"\t-long-stem-{j}' for i in range(13) for j in ('a','b','c')]
             +['a/first','a/second','a/.first','a/.second','x','xyz'])
    fixture={'schema':h.V2,'columns':h.V2_COLUMNS,'files':[[p,0,'01'*32] for p in paths],
             'total_bytes':0,'opaque':{'unicode':'😀','nested':[False,None,1]}}
    actual=h.compact_v4(fixture)
    candidates=set()
    for a,b in zip(paths,paths[1:]):
        k=0
        while k<min(len(a),len(b)) and a[k]==b[k]:k+=1
        p=a[:k];q=p[:-1] if p.endswith('/') else p
        if q and all(part not in ('','.','..') for part in q.split('/')):candidates.add(p)
    prefixes=[''];assign=[0]*len(paths)
    def representation(ps,ids):
        return {'path_prefixes':ps,'files':[[i,p[len(ps[i]):],0,base64.b64encode(bytes.fromhex('01'*32)).decode()]
                                         for p,i in zip(paths,ids)]}
    while True:
        before=len(packed(representation(prefixes,assign)))
        choices=[]
        for p in sorted(candidates):
            ids=[len(prefixes) if path.startswith(p) and len(path)>len(p)>len(prefixes[i]) else i
                 for path,i in zip(paths,assign)]
            if ids.count(len(prefixes))<2:continue
            gain=before-len(packed(representation(prefixes+[p],ids)))
            if gain>0:choices.append((-gain,p,ids))
        if not choices:break
        _,p,assign=min(choices);prefixes.append(p);candidates.remove(p)
    assert len(prefixes)>10 and actual['path_prefixes']==prefixes
    assert actual['files']==representation(prefixes,assign)['files']
    assert decode(actual)==fixture['files'] and actual['opaque']==fixture['opaque']
    failures=0
    def rejected(d):
        nonlocal failures
        try:h.normalize(d)
        except ValueError:failures+=1
        else:raise AssertionError(d)
    digest=base64.b64encode(bytes(32)).decode()
    small={'schema':h.V4,'columns':h.V4_COLUMNS,'path_prefixes':['','a'],
           'files':[[1,'/x',0,digest]],'total_bytes':0}
    assert h.normalize(small)==[['a/x',0,'00'*32]]
    for prefix in ('.','..','a//','a/../','/a','a\\b','a\0b'):
        d=copy.deepcopy(small);d['path_prefixes'].append(prefix);rejected(d)
    for row in ([True,'/x',0,digest],[-1,'/x',0,digest],[2,'/x',0,digest],
                [1,'/x',False,digest],[1,'/x',16384,digest],[1,'/x',-1,digest],
                [1,'/../x',0,digest],[1,'//x',0,digest],[1,'/x',0,digest[:-2]+'B='],
                [1,'/x',0,base64.b64encode(bytes(31)).decode()], [1,'/x',0,digest+'\n']):
        d=copy.deepcopy(small);d['files']=[row];rejected(d)
    d=copy.deepcopy(small);d['files'].append([0,'a/x',0,digest]);rejected(d)
    with tempfile.TemporaryDirectory() as temp:
        root=Path(temp);(root/'item').write_bytes(b'payload')
        target=root/'evidence-manifest.json'
        doc={'schema':h.V2,'columns':h.V2_COLUMNS,'total_bytes':7,
             'files':[['item',7,hashlib.sha256(b'payload').hexdigest()]]}
        padded=json.dumps(doc,indent=12).encode();target.write_bytes(padded)
        def cli(*options):
            run=subprocess.run([sys.executable,str(args.helper.resolve()),*options,'--root',str(root)],
                               capture_output=True,text=True)
            assert run.returncode==0,run.stderr
        cli('--compact-v4');cli('--check')
        assert decode(json.loads(target.read_bytes()))==doc['files']
        # Inject replacement failure after a temporary is fully written.
        target.write_bytes(padded);oldreplace=Path.replace;argv=sys.argv
        def fail_replace(self,dst):raise OSError('injected replace failure')
        try:
            Path.replace=fail_replace;sys.argv=[str(args.helper),'--compact-v4','--root',str(root)]
            try:h.main()
            except OSError as exc:assert str(exc)=='injected replace failure'
            else:raise AssertionError('replacement failure not propagated')
        finally:Path.replace=oldreplace;sys.argv=argv
        assert target.read_bytes()==padded and not list(root.glob('*.tmp-*'))
        for bad in ('evidence-manifest.json','../outside'):
            try:h.verify_files([[bad,0,'00'*32]],root,target)
            except ValueError:failures+=1
            else:raise AssertionError('self/outside accepted')
        (root/'escape').symlink_to(Path(temp).parent)
        try:h.verify_files([['escape/outside',0,'00'*32]],root,target)
        except ValueError:failures+=1
        else:raise AssertionError('symlink outside accepted')
    assert raw==index.read_bytes() and oldbytes==oldhelper.read_bytes()
    child=resource.getrusage(resource.RUSAGE_CHILDREN)
    cpu=time.process_time()-start+child.ru_utime+child.ru_stime
    assert cpu<2,cpu
    print(json.dumps({'status':'PASS','rows_rehashed':len(rows),'old_bytes':len(raw),
        'v4_bytes':len(packed(v4)),'saved_bytes':len(raw)-len(packed(v4)),
        'prefixes':len(v4['path_prefixes']),'oracle_prefixes':len(prefixes),
        'rejections':failures,'cpu_seconds':round(cpu,6),
        'helper_sha256':hashlib.sha256(args.helper.read_bytes()).hexdigest(),
        'original_index_sha256':hashlib.sha256(raw).hexdigest(),
        'v4_index_sha256':hashlib.sha256(packed(v4)).hexdigest(),
        'review_checks_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}))

if __name__=='__main__':main()
