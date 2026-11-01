"""Rehearse the PR12 squash tree in a newly created disposable local branch.

No main mutation, commit, push or tag. --index rehearses final staged bytes;
--no-write checks without replacing the recorded earlier rehearsal receipt.
"""
import argparse,json,subprocess,tempfile,uuid
from pathlib import Path
R=Path(__file__).resolve().parents[3]
P=Path(__file__).resolve().parent
BASE='67bd07c0867d8d49eb104942237d7f51a7d9f77d'
def run(args,cwd=R,stdin=None):return subprocess.check_output(['git',*args],cwd=cwd,input=stdin,stderr=subprocess.STDOUT)
ap=argparse.ArgumentParser();ap.add_argument('--candidate',default='HEAD');ap.add_argument('--index',action='store_true');ap.add_argument('--no-write',action='store_true');a=ap.parse_args()
head=run(['rev-parse','HEAD']).decode().strip();branch=run(['symbolic-ref','--short','HEAD']).decode().strip()
main_before=run(['for-each-ref','--format=%(objectname)','refs/heads/main'])
candidate=run(['rev-parse',a.candidate]).decode().strip()
expected=run(['write-tree'] if a.index else ['rev-parse',candidate+'^{tree}']).decode().strip()
taskbranch='codex/pr12-rehearsal-'+uuid.uuid4().hex[:10]
folder=Path(tempfile.mkdtemp(prefix='padua-pr12-rehearsal-'))/'worktree'
created=False
try:
    run(['worktree','add','-b',taskbranch,str(folder),BASE]);created=True
    if a.index:
        patch=run(['diff','--cached','--binary',BASE]);run(['apply','--index','--binary','-'],cwd=folder,stdin=patch)
    else:run(['merge','--squash','--no-commit',candidate],cwd=folder)
    actual=run(['write-tree'],cwd=folder).decode().strip()
    assert actual==expected,(actual,expected)
    assert run(['rev-parse','HEAD'],cwd=folder).decode().strip()==BASE
finally:
    if created:
        run(['worktree','remove','--force',str(folder)])
        run(['branch','-D',taskbranch])
assert run(['rev-parse','HEAD']).decode().strip()==head
assert run(['symbolic-ref','--short','HEAD']).decode().strip()==branch
assert run(['for-each-ref','--format=%(objectname)','refs/heads/main'])==main_before
result={'purpose':'mechanical squash rehearsal; no mathematical execution','base':BASE,'candidate':candidate,'staged_index':a.index,'expected_tree':expected,'actual_tree':actual,'main_unchanged':True,'root_branch_unchanged':True,'disposable_worktree_and_branch_removed':True,'passed':True}
if not a.no_write:(P/'rehearsal.json').write_text(json.dumps(result,indent=1)+'\n')
print(json.dumps(result))
