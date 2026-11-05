"""Summarize native artifacts, reference replay, and explicitly limited cost fits."""
import argparse
import gzip
import hashlib
import json
import math
from pathlib import Path

NONMATHEMATICAL={'setup_seconds','search_seconds','total_seconds','producer_provenance'}

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes())
def math_hash(data):
    return hashlib.sha256(json.dumps({k:v for k,v in data.items() if k not in NONMATHEMATICAL},sort_keys=True,separators=(',',':')).encode()).hexdigest()
def fit(rows, field):
    x=[math.log(r['n']) for r in rows];y=[math.log(r[field]) for r in rows]
    xm=sum(x)/len(x);ym=sum(y)/len(y)
    exponent=sum((a-xm)*(b-ym) for a,b in zip(x,y))/sum((a-xm)**2 for a in x)
    scale=math.exp(ym-exponent*xm)
    budgets={}
    for name,seconds in [('24h',86400),('7days',604800)]:
        cumulative=0;maximum=0
        for n in range(17,10001):
            cumulative+=scale*n**exponent
            if cumulative>seconds:break
            maximum=n
        budgets[name]=dict(single_degree_n=(seconds/scale)**(1/exponent),contiguous_from17_max_n=maximum)
    return dict(degrees=[r['n'] for r in rows],exponent=exponent,scale=scale,budgets=budgets)

def receipt(folder, original, independent):
    rows=[];python=[];provenance=[]
    for p in sorted(folder.glob('n*.json.gz'),key=lambda p:int(p.name.split('.')[0][1:])):
        d=read(p);n=d['n'];provenance.append(d['producer_provenance']);r=dict(n=n,complete=d['complete'],leaves=len(d['leaves']),setup_cpu=d['setup_seconds'],search_cpu=d['search_seconds'],total_wall=d['total_seconds'],certificate_sha256=digest(p),mathematical_sha256=math_hash(d))
        r['native_hotpath_cpu']=r['setup_cpu']+r['search_cpu']
        reference=original/f'n{n}-reference-check.json'
        if reference.exists():
            checked=read(reference);prior=original/f'n{n}.json.gz'
            r['reference_accepted']=checked['accepted'] and checked['certificate_sha256']==digest(prior) and math_hash(read(prior))==r['mathematical_sha256']
        q=independent/f'reference-n{n}.json'
        if q.exists():
            pd=read(q)
            if pd['complete']:python.append(dict(n=n,total_wall=pd['total_seconds']))
        rows.append(r)
    python_cpu=[]
    for p in sorted((original/'python-cpu').glob('n*-timing.json')):
        q=read(p);n=q['n'];native=next((r for r in rows if r['n']==n),None)
        if native:
            q['hotpath_vs_reference_cpu_ratio']=q['cpu_seconds']/native['native_hotpath_cpu']
            assert math_hash(read(original/'python-cpu'/f'n{n}.json.gz'))==native['mathematical_sha256']
            python_cpu.append(q)
    native_full=[]
    for p in sorted((original/'native-full-cpu').glob('n*-timing.json')):
        q=read(p);n=q['n'];native=next((r for r in rows if r['n']==n),None)
        if native:
            assert math_hash(read(original/'native-full-cpu'/f'n{n}.json.gz'))==native['mathematical_sha256']
            ref=next((r for r in python_cpu if r['n']==n),None)
            native_full.append(dict(n=n,full_driver_cpu_seconds=q['full_driver_cpu_seconds'],parent_cpu_seconds=q['parent_cpu_seconds'],child_cpu_seconds=q['child_cpu_seconds'],cold_compile_included=True,reference_cpu_over_full_native=(ref['cpu_seconds']/q['full_driver_cpu_seconds'] if ref else None)))
    pipeline=[]
    bench=original.parent/'checker'/'cpu-bench-corrected.json'
    if bench.exists():
        for q in read(bench)['rows']:
            native=next((r for r in native_full if r['n']==q['n']),None)
            if native:
                matching=next((r for r in rows if r['n']==q['n']),None)
                assert matching and q['receipt']['accepted'] and q['receipt']['certificate_sha256']==matching['certificate_sha256']
                pipeline.append(dict(n=q['n'],cpu_seconds=native['full_driver_cpu_seconds']+q['cpu_user_seconds']+q['cpu_system_seconds']))
    fits={}
    if len(pipeline)>1:fits['native_producer_plus_checker_cpu_two_point']=fit(pipeline,'cpu_seconds')
    if len(native_full)>1:fits['native_full_cpu17_24_two_point']=fit(native_full,'full_driver_cpu_seconds')
    if len(python_cpu)>1:fits['python_cpu17_24_two_point']=fit(python_cpu,'cpu_seconds')
    for label,subset,field in [('native_hotpath_cpu17_24',[r for r in rows if 17<=r['n']<=24],'native_hotpath_cpu'),('native_hotpath_cpu17plus',[r for r in rows if r['n']>=17 and r['complete']],'native_hotpath_cpu'),('python_wall17_24',[r for r in python if 17<=r['n']<=24],'total_wall')]:
        if len(subset)>1:fits[label]=fit(subset,field)
    return dict(status='MEASURED',scope='Producer implementation/performance and reference validation only; corrected checker summaries govern independent acceptance.',environment=dict(python='3.12.14',gcc='14.2.0',gmp='6.3.0'),checker_cpu_benchmark_sha256=(digest(bench) if bench.exists() else None),rows=rows,fits=fits,python_producer_wall=python,python_producer_cpu=python_cpu,native_full_driver_cpu=native_full,native_producer_plus_checker_cpu=pipeline,
                native_source_sha256=sorted({x['source_sha256'] for x in provenance}),
                driver_sha256=sorted({x['driver_sha256'] for x in provenance}),
                limits='Fits are heuristic. Native per-row CPU is hotpath only; native_full_driver_cpu includes cold gcc, Python setup and certificate output. Reference CPU covers constructor+search only, omitting final compression/write; the primary full-driver ratio therefore conservatively charges extra native work. Python wall fits reflect shared contention. All projections ignore memory, fixed192-bit enclosure growth, and n<=100 cap; they do not validate any projected degree. Python CPU/wall fits are producer-only, not certification-pipeline costs; native_producer_plus_checker is a separate provisional two-point pipeline fit.')

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--folder',type=Path,required=True);p.add_argument('--original',type=Path,required=True)
    p.add_argument('--independent',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();a.output.write_text(json.dumps(receipt(a.folder,a.original,a.independent),sort_keys=True,separators=(',',':'))+'\n')
