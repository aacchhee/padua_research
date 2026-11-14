"""Postrun provenance only: no mathematical kernel run or source mutation."""
import hashlib,json,pathlib,resource,shutil,subprocess
HERE=pathlib.Path(__file__).resolve().parent;ROOT=HERE.parents[3]
OUT=ROOT/'local-output/argmax-bridge-20261105/post-audit-D01/corner'
def ident(p):
 p=pathlib.Path(p).resolve();return {'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def cpu():return sum(resource.getrusage(k).ru_utime+resource.getrusage(k).ru_stime for k in (resource.RUSAGE_SELF,resource.RUSAGE_CHILDREN))
target=OUT/'build-closure.json'
if target.exists():raise RuntimeError('refuse provenance overwrite')
compiler=shutil.which('g++');cmd=[compiler,'-std=c++17','-M',str(HERE/'measure.cpp')]
p=subprocess.run(cmd,capture_output=True,check=False)
(OUT/'build-headers.d').write_bytes(p.stdout);(OUT/'build-headers.stderr').write_bytes(p.stderr)
if p.returncode:raise RuntimeError('provenance preprocessor failed')
deps=p.stdout.decode().replace('\\\n',' ').split(': ',1)[1].split()
x={'scope':'postrun same-source build header provenance, no numerical rerun','command':cmd,'exit':p.returncode,'helper_source':ident(__file__),'compiler':ident(compiler),'header_dependencies':[ident(q) for q in sorted(set(deps))],'cpu_seconds':cpu()}
target.write_text(json.dumps(x,indent=2)+'\n')
receipt=HERE.parents[1]/'evidence/d01-corner.json';r=json.loads(receipt.read_text());r['postrun_build_closure']=ident(target);r['postrun_build_closure_cpu_seconds']=x['cpu_seconds'];receipt.write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({'build_closure':ident(target),'dependencies':len(x['header_dependencies']),'cpu_seconds':x['cpu_seconds']}))
