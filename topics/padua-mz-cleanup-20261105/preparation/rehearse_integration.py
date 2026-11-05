#!/usr/bin/env python3
"""Disposable sequential squash integration, never touching main or live branches."""
import argparse
import json
from pathlib import Path
import subprocess
import tempfile


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate',required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    root=Path(__file__).resolve().parents[3]
    base='aff30e8ad5542c94fab642ae024dc9aab4fa7ad7'
    heads={'26':args.candidate,
           '21':'3ed6c94246f21353350f82712b6628b39db6f65a',
           '24':'b81a1a1dcd6a633dcfd27429dc6ee22e74849d14',
           '25':'22e8540cf90278dad2eba3eb51f129ca10a9dd9e'}
    foreign={'21':['topics/padua-literature-20261103','results/padua-literature-20261103.md'],
             '24':['topics/padua-lanczos-frontier-20261105','results/padua-lanczos-frontier-20261105.md'],
             '25':['topics/padua-argmax-effective-2-20261105','results/padua-argmax-effective-2-20261105.md']}
    own=['PROOF_STATUS.md','state/IDEAS.md','state/CURRENT.md','ID_CROSSWALK.md',
         'RESULTS.md','PAPER_MAP.md','topics/padua-batch-20261031/ALLOCATIONS.md',
         'tracks/mz-constants/README.md','tracks/mz-constants/paper/manuscript.tex',
         'topics/padua-mz-cleanup-20261105/theory']
    orders=[['26']]+[[a,b] for x in ['21','24','25'] for a,b in [(x,'26'),('26',x)]]
    orders += [['21','24','25','26'],['26','25','24','21']]
    work=Path(tempfile.mkdtemp(prefix='padua-mz-squash-',dir='/tmp'))
    def run(*cmd,cwd=root,ok=True):
        p=subprocess.run(cmd,cwd=cwd,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        if ok and p.returncode:raise RuntimeError(p.stdout)
        return p
    run('git','worktree','add','--detach',str(work),base)
    rows=[]
    try:
        for order in orders:
            run('git','reset','--hard',base,cwd=work)
            run('git','clean','-fd',cwd=work)
            commits=[];conflicts=[]
            for label in order:
                merged=run('git','merge','--squash','--no-commit',heads[label],cwd=work,ok=False)
                if merged.returncode:
                    conflicts=run('git','diff','--name-only','--diff-filter=U',cwd=work).stdout.splitlines()
                    rows.append(dict(order=order,status='FAIL',conflicts=conflicts,diagnostic=merged.stdout[-1500:]))
                    raise RuntimeError('disposable integration failed')
                run('git','commit','-q','--author=Andrey Chesnokov <aacchhee@gmail.com>',
                    '-m','test: disposable PR'+label+' squash rehearsal',
                    '-m','Agent: Codex\nModel: gpt-6.1-sol xhigh',cwd=work)
                commits.append(run('git','rev-parse','HEAD',cwd=work).stdout.strip())
            own_diff=run('git','diff','--name-only',args.candidate,'HEAD','--',*own,cwd=work).stdout.splitlines()
            if own_diff:raise RuntimeError('owned integration bytes changed: '+repr(own_diff))
            checks={}
            for label in order:
                if label=='26':continue
                diff=run('git','diff','--name-only',heads[label],'HEAD','--',*foreign[label],cwd=work).stdout.splitlines()
                if diff:raise RuntimeError('foreign topic bytes changed: '+repr(diff))
                checks[label]='topic subtree and dedicated results byte-identical'
            rows.append(dict(order=order,status='PASS',conflicts=[],squash_commits=commits,
                             own_shared_and_theory='byte-identical to candidate',foreign=checks))
    finally:
        run('git','worktree','remove','--force',str(work),ok=False)
    report=dict(method='actual sequential git merge --squash plus detached commits in disposable /tmp worktree; no main/live ref touched',
                base=base,heads=heads,cases=rows,accepted=len(rows)==9 and all(r['status']=='PASS' for r in rows))
    args.output.write_text(json.dumps(report,separators=(',',':'))+'\n')
    print(f"{len(rows)} disposable integration sequences passed; no conflicts; own/foreign scientific bytes preserved")


if __name__=='__main__':main()
