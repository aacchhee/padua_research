"""Bounded exact producer for three G6 spots; independent checker required."""
import argparse,hashlib,json,platform,sys,time
from pathlib import Path
SOURCE=Path(__file__).resolve().parents[3]/'padua-argmax-alln-20261101'/'code'/'gated'
sys.path.insert(0,str(SOURCE))
import d3_edge_common as c
from d3_edge_generate import certify_pair

def main():
    p=argparse.ArgumentParser();p.add_argument('--float-input',required=True);p.add_argument('--output',required=True);p.add_argument('--cpu-per-pair',type=float,default=120);a=p.parse_args()
    raw=Path(a.float_input).read_bytes();data=json.loads(raw);c.DEGREES=(13,17,24)
    result={'format':'padua-effective-g6-spots-v1','status':'exact producer output; checker pending','python':platform.python_version(),'invocation':sys.argv,'float_input_sha256':hashlib.sha256(raw).hexdigest(),'producer_sha256':c.digest(__file__),'inherited_source_sha256':c.source_hashes(),'precision':c.g.PRECISION,'scale':c.g.S,'rows':[]}
    assert c.arithmetic_controls()
    for n in c.DEGREES:
        row=next(r for r in data['rows'] if r['n']==n);r=min(row['E_C_comparisons'],key=lambda r:r['difference'])
        identity=(n,0 if r['edge']=='v+' else n,r['source'],r['target']);start=time.process_time();wall=time.monotonic()
        cert=certify_pair(identity,start+a.cpu_per_pair)
        result['rows'].append({'identity':identity,'cpu_seconds':time.process_time()-start,'wall_seconds':time.monotonic()-wall,'certificate':cert})
        Path(a.output).write_text(json.dumps(result,indent=2)+'\n');print(identity,len(cert['leaves']),len(cert['pending']),result['rows'][-1]['cpu_seconds'],flush=True)
if __name__=='__main__':main()
