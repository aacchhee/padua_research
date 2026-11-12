#!/usr/bin/env python3
"""Resume a completed determinant prefix without repeating or hiding a cap."""
import argparse,json,pathlib,subprocess,sys
from r08_lattice import INPUT,identity,reduce_raw
def main():
    p=argparse.ArgumentParser()
    for k in ['binary','scratch','receipt','prefix_receipt']:p.add_argument('--'+k.replace('_','-'),required=True)
    for k in ['n','hi','cap']:p.add_argument('--'+k,type=int,required=True)
    p.add_argument('--seconds',type=float,default=120);a=p.parse_args()
    prefixpath=pathlib.Path(a.prefix_receipt);prefixdata=json.loads(prefixpath.read_text());prefix=next(r for r in prefixdata['rows'] if r['n']==a.n)
    lo=prefix['completed_det_interval'][1]+1
    assert prefix['completed_det_interval'][0]==1 and lo<=a.hi
    if prefix['summary']:
        # If cap increases, a known minimum above the new cap proves no lost cases.
        assert a.cap<=prefix['summary']['fold_cap'] or prefix['summary']['min_fold']>a.cap
    else:
        prefixcmd=next(c for c in prefixdata['commands'] if int(c[2])==a.n)
        assert not prefix['fold_rank_hist'] and a.cap==int(prefixcmd[5])
    scratch=pathlib.Path(a.scratch);scratch.mkdir(parents=True,exist_ok=True);raw=scratch/f'tail-n{a.n}-{lo}-{a.hi}.jsonl'
    if raw.exists():raise RuntimeError(f'refuse existing {raw}')
    cmd=[a.binary,'complement',str(a.n),str(lo),str(a.hi),str(a.cap),str(raw)]
    try:subprocess.run(cmd,check=True,timeout=a.seconds)
    except subprocess.TimeoutExpired:pass
    rec,small=reduce_raw(raw,a.n);rankraw=scratch/'exact-ranks.json';rankraw.write_text(json.dumps(small,separators=(',',':'))+'\n')
    summary=rec['summary'];prefixmin=prefix['summary']['min_fold'] if prefix['summary'] else None
    combinedmin=min(prefixmin,summary['min_fold']) if prefixmin is not None and summary else None
    out={'schema':'padua-r08-lattice-tail-v1','input_sha':INPUT,'sources':[identity(__file__),identity(pathlib.Path(__file__).with_name('r08_lattice.py')),identity(pathlib.Path(__file__).with_name('r08_lattice_enum.cpp'))],
         'prefix_receipt':identity(prefixpath),'prefix_n':a.n,'prefix_interval':prefix['completed_det_interval'],
         'command':cmd,'tail':rec,'exact_rank_raw':identity(rankraw),
         'combined_complete':rec['complete'],'combined_interval':[1,rec['completed_det_interval'][1]],
         'combined_min_fold_if_recorded':combinedmin,'combined_no_fold_at_most_cap':not prefix['fold_rank_hist'] and not rec['fold_rank_hist']}
    pathlib.Path(a.receipt).write_text(json.dumps(out,separators=(',',':'))+'\n');print(json.dumps(out),flush=True)
if __name__=='__main__':main()
