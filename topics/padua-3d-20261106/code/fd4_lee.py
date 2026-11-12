#!/usr/bin/env python3
"""D4 anticode restart and independent existing-auditor implementation replay."""
import argparse,hashlib,itertools,json,platform,subprocess,sys,time
from pathlib import Path
TOP=Path(__file__).resolve().parents[1]
def ident(p):
 p=Path(p);return {'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def main():
 p=argparse.ArgumentParser();p.add_argument('--scratch',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();a.scratch.mkdir(parents=True,exist_ok=False)
 out={'schema':'fd4-lee-restart-v1','command':sys.argv,'source':ident(__file__),'seed':None,'python':platform.python_version(),'rows':[]}
 for label,source in [('producer',TOP/'code/r08_lattice_enum.cpp'),('auditor',TOP/'audit-04/code/A1/aud_enum.cpp')]:
  binary=a.scratch/label;cmd=['g++','-std=c++17','-O3',str(source),'-o',str(binary)];t=time.monotonic();subprocess.run(cmd,check=True,capture_output=True,timeout=60)
  for n,hi in [(4,92),(5,178),(6,304),(7,486)]:
   lo=2*n*(2*n*n+1)//3;r=n-1
   ball={v for v in itertools.product(range(-r,r+1),repeat=3) if sum(map(abs,v))<=r};ds=ball|{(v[0]+1,v[1],v[2]) for v in ball}
   assert len(ds)==lo and max(sum(abs(x-y) for x,y in zip(v,w)) for v in ds for w in ds)==2*n-1
   raw=a.scratch/f'{label}-n{n}.jsonl';cmd=[str(binary),'min',str(n),str(lo),str(hi),'0',str(raw)]
   started=time.monotonic();run=subprocess.run(cmd,capture_output=True,text=True,timeout=120);elapsed=time.monotonic()-started;assert run.returncode==0,run.stderr
   rows=[json.loads(s) for s in raw.read_text().splitlines()];qs=[d for d in rows if d['type']=='q'];mins=[d for d in rows if d['type']=='minimizer'];assert qs[-1]['q']==hi and qs[-1]['admissible']==len(mins)
   assert all(d['admissible']==0 for d in qs[:-1]) and [d['q'] for d in qs]==list(range(lo,hi+1))
   out['rows'].append({'implementation':label,'code':ident(source),'binary':ident(binary),'command':cmd,'seconds':elapsed,'n':n,'double_sphere_count':lo,'diameter_checked':2*n-1,'min_det':hi,'minimizers':len(mins),'per_q':[[d['q'],d['hnf_total'],d['admissible']] for d in qs],'hnfs':sorted(d['hnf'] for d in mins),'fold_histogram':{str(k):sum(d['fold']==k for d in mins) for k in sorted({d['fold'] for d in mins})},'raw':ident(raw)})
 for n in (4,5,6,7):
  pair=[r for r in out['rows'] if r['n']==n];assert pair[0]['hnfs']==pair[1]['hnfs'] and pair[0]['per_q']==pair[1]['per_q']
 out['status']='EXACT_TWO_IMPLEMENTATION_MATCH; developer ran both, formal independent audit remains required'
 payload=json.dumps(out,separators=(',',':'))+'\n';assert len(payload.encode())<=32768;a.output.write_text(payload);print(json.dumps({'status':out['status'],'rows':[(r['implementation'],r['n'],r['min_det'],r['seconds']) for r in out['rows']]}))
if __name__=='__main__':main()
