#!/usr/bin/env python3
"""Complete global minimum-unisolvent-fold windows against an attained target."""
import argparse, json, pathlib, subprocess, sys
from r08_lattice import INPUT, identity, reduce_raw, exact_rank, folded, shortest
def main():
    p=argparse.ArgumentParser();p.add_argument('--binary',required=True);p.add_argument('--scratch',required=True);p.add_argument('--receipt',required=True);p.add_argument('--degrees',type=int,nargs='+',required=True);p.add_argument('--seconds',type=float,default=120);a=p.parse_args()
    scratch=pathlib.Path(a.scratch);scratch.mkdir(parents=True,exist_ok=True);rows=[];commands=[]
    targets={4:45,5:75,6:112};source=pathlib.Path(__file__).with_name('r08_lattice_enum.cpp')
    for n in a.degrees:
        target=targets[n];raw=scratch/f'minrank-n{n}.jsonl'
        if raw.exists():raise RuntimeError(f'refuse existing {raw}')
        cmd=[a.binary,'complement',str(n),'1',str(8*(target-1)),str(target-1),str(raw)];commands.append(cmd)
        try:subprocess.run(cmd,check=True,timeout=a.seconds)
        except subprocess.TimeoutExpired:pass
        rec,small=reduce_raw(raw,n)
        # Attained anisotropic parity lattice: (n,n+1,n+1).
        v=(n,0,n+1,n+1,n+1,2*(n+1))
        q,F=folded(v);assert len(F)==target and exact_rank(v,n)==rec['N'] and shortest(v)>=2*n
        full=[r for r in small if r['rank']==rec['N']]
        rec['target']=target;rec['attained_witness']={'hnf':v,'det':q,'fold':len(F),'rank':rec['N']}
        rec['minimum_unisolvent_fold']=(min([r['fold'] for r in full]+[target]) if rec['complete'] else None)
        rankraw=scratch/f'minrank-n{n}-exact-ranks.json';rankraw.write_text(json.dumps(small,separators=(',',':'))+'\n');rec['exact_rank_raw']=identity(rankraw)
        rows.append(rec);out={'schema':'padua-r08-lattice-minrank-v1','input_sha':INPUT,'sources':[identity(__file__),identity(pathlib.Path(__file__).with_name('r08_lattice.py')),identity(source)],'commands':commands,'rows':rows}
        pathlib.Path(a.receipt).write_text(json.dumps(out,separators=(',',':'))+'\n');print(json.dumps({'n':n,'complete':rec['complete'],'minimum_unisolvent_fold':rec['minimum_unisolvent_fold'],'hist':rec['fold_rank_hist']}),flush=True)
        if not rec['complete']:break
if __name__=='__main__':main()
