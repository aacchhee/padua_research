"""Data-only archive reader and bounded, append-only independent runs."""
import argparse, hashlib, json, os, platform, re, resource, sys, tarfile, time
from pathlib import Path
import numpy as np
import check
from controls import arithmetic_controls, corruption_controls

ARCHIVE_SHA='b00fd57f85ce6d96a6c1fa01e2307abd815088bb8fcb28b1587657ef142b109a'
def digest(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(1048576),b''): h.update(b)
    return h.hexdigest()
def archive_inputs(path):
    check.need(digest(path)==ARCHIVE_SHA,'archive pin')
    items=[]
    with tarfile.open(path,'r:gz') as tf:
        seen=set()
        for m in tf:
            match=re.fullmatch(r'outputs/all/jobs/(\d+)/(produce|verify)/essential-receipt.json',m.name)
            if not match: continue
            check.need(m.isfile() and 0<m.size<100000,'unsafe data member')
            check.need(m.name not in seen,'duplicate archive member'); seen.add(m.name)
            b=tf.extractfile(m).read(); d=json.loads(b)
            check.need(d['n']==int(match[1]),'member degree mismatch')
            items.append((d['n'],match[2],m.name,b,d))
    check.need(len(items)==560,'archive certificate inventory')
    check.need({(n,p) for n,p,_,_,_ in items}=={(n,p) for n in [*range(41,320),511] for p in ['produce','verify']},'archive exact scope')
    return items
def main():
    p=argparse.ArgumentParser(); p.add_argument('--archive',required=True); p.add_argument('--output',required=True)
    p.add_argument('--degrees',default='41,199,238,511'); p.add_argument('--cpu-limit',type=int,default=3600)
    p.add_argument('--additional-dir'); p.add_argument('--controls',action='store_true'); args=p.parse_args()
    resource.setrlimit(resource.RLIMIT_CPU,(args.cpu_limit,args.cpu_limit+1))
    out=Path(args.output); out.mkdir(parents=True,exist_ok=False)
    started=time.process_time(); items=archive_inputs(args.archive)
    degrees=None if args.degrees=='all' else set(map(int,args.degrees.split(',')))
    if args.additional_dir:
        for path in sorted(Path(args.additional_dir).glob('*.json')):
            b=path.read_bytes(); d=json.loads(b)
            if d.get('format')=='FINAL-HYBRID-kept-proof-v1': items.append((d['n'],path.stem,str(path),b,d))
    items=sorted((x for x in items if degrees is None or x[0] in degrees),key=lambda x:(x[0],x[1]))
    sources={p.name:digest(p) for p in Path(__file__).parent.glob('*.py')}
    metadata={'source_hashes':sources,'archive_sha256':ARCHIVE_SHA,'CPU_limit':args.cpu_limit,
      'python':sys.version,'numpy':np.__version__,'platform':platform.platform(),'command':sys.argv,
      'cache_policy':'fresh process; reuse only exact (kind,n,Fraction a,Fraction b) within one degree; erase at degree change; no disk/pilot cache',
      'inputs':[{'n':n,'pass':pa,'path':name,'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)} for n,pa,name,b,d in items]}
    (out/'inputs.json').write_text(json.dumps(metadata,indent=2)+'\n')
    smoke=arithmetic_controls(); records=[]; cache={}; previous=None; mutations=None
    with (out/'observations.jsonl').open('x') as log:
        for n,pa,name,b,d in items:
            if n!=previous: cache={}; previous=n
            t=time.process_time()
            try:
                result=check.check(d,cache)
                record={'n':n,'pass':pa,'accepted':True,'CPU_seconds':time.process_time()-t,**result}
                if args.controls and n==199 and mutations is None: mutations=corruption_controls(d,cache)
            except Exception as e:
                record={'n':n,'pass':pa,'accepted':False,'CPU_seconds':time.process_time()-t,'error':repr(e)}
                log.write(json.dumps(record)+'\n'); log.flush(); raise
            records.append(record); log.write(json.dumps(record)+'\n'); log.flush()
            print(json.dumps({'n':n,'pass':pa,'accepted':True,'CPU_seconds':record['CPU_seconds']}),flush=True)
    if args.controls: check.need(mutations is not None and len(mutations)>=20,'controls not exercised')
    summary={'accepted':len(records),'requested':len(items),'CPU_seconds':time.process_time()-started,
             'arithmetic_controls':len(smoke),'corruption_controls':len(mutations or []),
             'maximum_S_keys':max(r['S_keys'] for r in records),'scope':'independent substituted-bound recertification',
             'all_native_endpoints_validated':False,'cache_policy':metadata['cache_policy']}
    (out/'controls.json').write_text(json.dumps({'arithmetic':smoke,'corruption':mutations},indent=2)+'\n')
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n'); print(json.dumps(summary),flush=True)
if __name__=='__main__': main()
