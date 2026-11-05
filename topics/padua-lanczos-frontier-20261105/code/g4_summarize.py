"""Compact G4 evidence without rerunning successful computations."""
import argparse,hashlib,json,pathlib

def main():
 p=argparse.ArgumentParser();p.add_argument('--input-dir',type=pathlib.Path,required=True);p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args();d=a.input_dir
 def file(p):return {'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
 r=json.loads((d/'summary.json').read_text());ans={k:v for k,v in r.items() if k!='cases'};ans['status']='G4_DEVELOPER_REPLAY_DIFFERENCES_L7_STOP_REVIEW_PENDING';ans['cases']=[]
 for c in r['cases']:
  z={k:v for k,v in c.items() if k!='scalar_differences'};z['all_scalar_differences_retained_externally']=True;ans['cases'].append(z)
 ans['artifacts']=[file(p) for p in sorted(d.iterdir()) if p.is_file()];ans['limitations']=['Historical Q/H and exact BLAS dispatch unavailable.','Numeric screens are unchanged saved diagnostics, not explanation or blanket acceptance.','Both executions are developer replay; distinct review and root acceptance required before suite.','No natural-target suite executed.'];a.output.write_text(json.dumps(ans,indent=2)+'\n');assert a.output.stat().st_size<16384
if __name__=='__main__':main()
