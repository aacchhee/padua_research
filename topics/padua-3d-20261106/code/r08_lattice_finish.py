#!/usr/bin/env python3
"""Finish a disjoint exact prefix and compare every determinant to a full replay."""
import argparse,hashlib,json,pathlib,subprocess,sys
from r08_lattice import INPUT,identity,reduce_raw
def main():
    p=argparse.ArgumentParser()
    for k in ['binary','scratch','receipt','reference']:p.add_argument('--'+k,required=True)
    for k in ['n','lo','hi','cap']:p.add_argument('--'+k,type=int,required=True)
    p.add_argument('--prefix-receipts',nargs='+',required=True);p.add_argument('--seconds',type=float,default=120);a=p.parse_args()
    rawpaths=[];prefixids=[]
    for pp in a.prefix_receipts:
        d=json.loads(pathlib.Path(pp).read_text());prefixids.append(identity(pp))
        r=next(r for r in d['rows'] if r['n']==a.n) if 'rows' in d else d['tail']
        rawpaths.append(r['raw']['path'])
    scratch=pathlib.Path(a.scratch);scratch.mkdir(parents=True,exist_ok=True);raw=scratch/f'last-n{a.n}-{a.lo}-{a.hi}.jsonl'
    if raw.exists():raise RuntimeError(f'refuse existing {raw}')
    cmd=[a.binary,'complement',str(a.n),str(a.lo),str(a.hi),str(a.cap),str(raw)]
    try:subprocess.run(cmd,check=True,timeout=a.seconds)
    except subprocess.TimeoutExpired:pass
    rec,small=reduce_raw(raw,a.n);rawpaths.append(str(raw))
    refpath=pathlib.Path(a.reference);ref=json.loads(refpath.read_text());refr=next(r for r in ref['rows'] if r['n']==a.n)
    keys=['q','hnf_total','after_axis_pair_prune','admissible','small']
    def qrows(path):
        return [{k:r[k] for k in keys} for r in map(json.loads,pathlib.Path(path).read_text().splitlines()) if r['type']=='q']
    own=[]
    for rp in rawpaths:own.extend(qrows(rp))
    reference=qrows(refr['raw']['path'])
    assert all(r['q']==i+1 for i,r in enumerate(own)), 'noncontiguous or overlapping completed prefixes'
    assert own==reference[:len(own)],'per-determinant replay disagreement'
    scientific=json.dumps(own,separators=(',',':')).encode()
    complete=len(own)==a.hi
    out={'schema':'padua-r08-lattice-finish-v1','input_sha':INPUT,'n':a.n,
         'sources':[identity(__file__),identity(pathlib.Path(__file__).with_name('r08_lattice.py')),identity(pathlib.Path(__file__).with_name('r08_lattice_enum.cpp'))],
         'prefix_receipts':prefixids,'command':cmd,'last_segment':rec,'own_raw_segments':[identity(rp) for rp in rawpaths],
         'reference_receipt':identity(refpath),'reference_raw':refr['raw'],
         'combined_complete':complete,'combined_interval':[1,len(own)],'per_q_all_scientific_fields_equal':True,
         'scientific_per_q_sha256':hashlib.sha256(scientific).hexdigest(),
         'combined_totals':{k:sum(r[k] for r in own) for k in keys if k!='q'},
         'no_fold_at_most_cap':all(r['small']==0 for r in own),
         'command_argv':sys.argv}
    pathlib.Path(a.receipt).write_text(json.dumps(out,separators=(',',':'))+'\n');print(json.dumps(out),flush=True)
if __name__=='__main__':main()
