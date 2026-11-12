#!/usr/bin/env python3
"""Complete a capped minimum-rank window; unchanged enumeration/rank core."""
import argparse,collections,json,pathlib,subprocess,sys
from r08_lattice import INPUT,identity,reduce_raw
def main():
    p=argparse.ArgumentParser()
    for k in ['binary','scratch','receipt','prefix_receipt']:p.add_argument('--'+k.replace('_','-'),required=True)
    p.add_argument('--n',type=int,required=True);p.add_argument('--seconds',type=float,default=120);a=p.parse_args()
    pp=pathlib.Path(a.prefix_receipt);pd=json.loads(pp.read_text());pr=next(r for r in pd['rows'] if r['n']==a.n)
    assert not pr['complete'];target=pr['target'];lo=pr['completed_det_interval'][1]+1;hi=8*(target-1)
    scratch=pathlib.Path(a.scratch);scratch.mkdir(parents=True,exist_ok=True);raw=scratch/f'minrank-n{a.n}-tail.jsonl'
    if raw.exists():raise RuntimeError(f'refuse existing {raw}')
    cmd=[a.binary,'complement',str(a.n),str(lo),str(hi),str(target-1),str(raw)]
    try:subprocess.run(cmd,check=True,timeout=a.seconds)
    except subprocess.TimeoutExpired:pass
    tail,small=reduce_raw(raw,a.n);hist=collections.Counter()
    for m,r,c in pr['fold_rank_hist']+tail['fold_rank_hist']:hist[m,r]+=c
    ranks=scratch/'tail-exact-ranks.json';ranks.write_text(json.dumps(small,separators=(',',':'))+'\n')
    full=[m for (m,r),c in hist.items() if r==pr['N']]
    out={'schema':'padua-r08-lattice-resume-rank-v1','input_sha':INPUT,'sources':[identity(__file__),identity(pathlib.Path(__file__).with_name('r08_lattice.py')),identity(pathlib.Path(__file__).with_name('r08_lattice_enum.cpp'))],
         'prefix_receipt':identity(pp),'prefix_n':a.n,'command':cmd,'tail':tail,'tail_rank_raw':identity(ranks),
         'combined_interval':[1,tail['completed_det_interval'][1]],'combined_complete':tail['complete'],
         'combined_fold_rank_hist':[[m,r,c] for (m,r),c in sorted(hist.items())],
         'attained_witness':pr['attained_witness'],
         'minimum_unisolvent_fold':min(full+[target]) if tail['complete'] else None}
    pathlib.Path(a.receipt).write_text(json.dumps(out,separators=(',',':'))+'\n');print(json.dumps(out),flush=True)
if __name__=='__main__':main()
