#!/usr/bin/env python3
"""Run/reduce exact round08 HNF searches; exact rank via rational characters.

No imports from frozen audit code. Source for the algorithms: audit03 T10
window_search.py, minfold_search.py, exact_confirm.py and T9 complement probe.
Raw JSONL is regenerate-only. Receipts never pin prose.
"""
import argparse, collections, fractions, hashlib, itertools, json, math
import os, pathlib, platform, subprocess, sys, time

ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCE = pathlib.Path(__file__).with_name('r08_lattice_enum.cpp')
SEEDS = {1:2,2:12,3:38,4:92,5:178,6:304,7:486,8:724,9:1026,
         10:1412,11:1878,12:2432,13:3098,14:3868,15:4750,16:5792}
INPUT = '9042e1c42964150f30fdbe8563c12ba6c6a8692a'
def identity(path):
    b=pathlib.Path(path).read_bytes()
    return {'path':str(path),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def exps(n):
    return [(i,j,k) for i in range(n+1) for j in range(n-i+1) for k in range(n-i-j+1)]
def characters(v, alpha):
    a,b,c,d,e,f=v; q=a*d*f; out=collections.Counter()
    for x,y,z in itertools.product(*[(-s,s) if s else (0,) for s in alpha]):
        out[(x*d*f%q,(-x*b*f+y*a*f)%q,(x*(b*e-c*d)-y*a*e+z*a*d)%q)]+=1
    return out
def exact_rank(v,n):
    piv={}
    for alpha in exps(n):
        row={k:fractions.Fraction(z) for k,z in characters(v,alpha).items()}
        while row:
            k=min(row)
            if k not in piv:
                t=row[k];piv[k]={j:z/t for j,z in row.items()};break
            t=row[k]
            for j,z in piv[k].items():
                w=row.get(j,0)-t*z
                if w:row[j]=w
                else:row.pop(j,None)
    return len(piv)
def dual(v):
    a,b,c,d,e,f=v;q=a*d*f;out=[]
    for j3 in range(f):
        for j2 in range(d):
            t=-e*j3+j2*f
            for j1 in range(a):
                out.append(((-b*t-c*j3*d+j1*d*f)%q,a*t%q,j3*a*d%q))
    assert len(set(out))==q
    assert all((a*x+b*y+c*z)%q==0 and (d*y+e*z)%q==0 and f*z%q==0 for x,y,z in out)
    return q,out
def folded(v):
    q,H=dual(v)
    return q,collections.Counter(tuple(min(h,q-h) for h in row) for row in H)
def shortest(v):
    a,b,c,d,e,f=v;best=f
    # Every improving vector has |au|<best; sign permits u>=0.
    for u in range((f-1)//a+1):
        rx=best-1-a*u
        for w in range((-rx-b*u+d-1)//d,(rx-b*u)//d+1):
            if u==w==0:continue
            t=(c*u+e*w)%f
            best=min(best,a*u+abs(b*u+d*w)+min(t,f-t))
    return best
def reduce_raw(path,n):
    qs=[];small=[];mins=[];summary=None
    with open(path) as stream:
        for line in stream:
            r=json.loads(line)
            if r['type']=='q':qs.append(r)
            elif r['type']=='small':small.append(r)
            elif r['type']=='minimizer':mins.append(r)
            elif r['type']=='summary':summary=r
    assert qs and all(qs[i]['q']==qs[0]['q']+i for i in range(len(qs)))
    # A timeout may leave small-case lines for an unfinished determinant.
    # Preserve them in raw bytes, but exclude them from completed-prefix results.
    small=[r for r in small if r['q']<=qs[-1]['q']]
    hist=collections.Counter();full=[]
    N=math.comb(n+3,3)
    for r in small:
        rank=exact_rank(r['hnf'],n);r['rank']=rank
        hist[(r['fold'],rank)]+=1
        if rank==N:full.append(r)
    rec={'n':n,'N':N,'completed_det_interval':[qs[0]['q'],qs[-1]['q']],
         'complete':summary is not None,'summary':summary,'raw':identity(path),
         'fold_rank_hist':[[m,r,c] for (m,r),c in sorted(hist.items())],
         'full_rank_small_count':len(full),'full_rank_small_examples':full[:3],
         'minimizer_count':len(mins),
         'minimizer_fold_hist':sorted([[m,c] for m,c in collections.Counter(r['fold'] for r in mins).items()]),
         'minimizer_example':mins[0] if mins else None,'exact_rank_cases':len(small)}
    if not summary:
        rec['completed_prefix_totals']={k:sum(r[k] for r in qs) for k in ('hnf_total','after_axis_pair_prune','admissible','small')}
        rec['elapsed_seconds_at_last_q']=qs[-1]['elapsed_seconds']
    return rec,small
def main():
    p=argparse.ArgumentParser();s=p.add_subparsers(dest='op',required=True)
    b=s.add_parser('build');b.add_argument('binary')
    r=s.add_parser('run');r.add_argument('kind',choices=['min','complement','n3below24']);r.add_argument('--degrees',nargs='+',type=int,required=True);r.add_argument('--binary',required=True);r.add_argument('--scratch',required=True);r.add_argument('--receipt',required=True);r.add_argument('--seconds',type=float,default=0)
    a=p.parse_args()
    if a.op=='build':
        subprocess.run(['g++','-O3','-std=c++17','-Wall','-Wextra',str(SOURCE),'-o',a.binary],check=True);return
    scratch=pathlib.Path(a.scratch);scratch.mkdir(parents=True,exist_ok=True)
    rows=[];commands=[];raw_small=[]
    for n in a.degrees:
        N=math.comb(n+3,3)
        mode='min' if a.kind=='min' else 'complement'
        lo=(1 if n<=3 else (38*n**3+26)//27) if mode=='min' else 1
        hi=SEEDS[n] if mode=='min' else (184 if a.kind=='n3below24' else 8*N)
        cap=23 if a.kind=='n3below24' else N
        raw=scratch/f'{a.kind}-n{n}.jsonl'
        if raw.exists():raise RuntimeError(f'refuse existing raw {raw}')
        cmd=[a.binary,mode,str(n),str(lo),str(hi),str(cap),str(raw)];commands.append(cmd)
        try:subprocess.run(cmd,check=True,timeout=a.seconds or None)
        except subprocess.TimeoutExpired:pass
        rec,small=reduce_raw(raw,n);rows.append(rec);raw_small.extend({'n':n,**r} for r in small)
        out={'schema':'padua-r08-lattice-v1','input_sha':INPUT,'kind':a.kind,
             'python':platform.python_version(),'sources':[identity(__file__),identity(SOURCE)],
             'commands':commands,'rows':rows}
        pathlib.Path(a.receipt).write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps({'n':n,'complete':rec['complete'],'interval':rec['completed_det_interval'],
                          'summary':rec['summary'],'fold_rank_hist':rec['fold_rank_hist']}),flush=True)
        if not rec['complete']:break
    extra=scratch/f'{a.kind}-exact-ranks.json'
    extra.write_text(json.dumps(raw_small,sort_keys=True,separators=(',',':'))+'\n')
    out['exact_rank_raw']=identity(extra)
    pathlib.Path(a.receipt).write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
