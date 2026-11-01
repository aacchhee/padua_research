"""Focused, read-only audit of source 0ef90ed; output JSON on stdout."""
from pathlib import Path
import hashlib
import json
import platform
import re
import subprocess
import sys
import sympy as s

ROOT = Path(__file__).resolve().parents[3]
SOURCE = '0ef90edc5b4d5639474cca7fa8d6d688e684e505'
PREVIOUS = '39c5ae616111e47798c06229eca6d366bbcd9583'
MAIN = '9739a0c56b7a3976422ce60a8441bfbbfd6554df'
TOPIC = 'topics/programme-ideas-20261031'

def git(*args):
    return subprocess.check_output(['git','-C',str(ROOT),*args])

def blob(p, sha=SOURCE):
    return git('show',sha+':'+p)

changed = git('diff','--name-only',PREVIOUS,SOURCE).decode().splitlines()
assert len(changed)==13
assert git('merge-base',SOURCE,MAIN).decode().strip()==MAIN
protected = ['AGENTS.md','agents/WORKFLOW.md','agents/codex/CODEX.md',
             'agents/claude/CLAUDE_ROLES.md','ID_CROSSWALK.md',
             TOPIC+'/audit-01.md',TOPIC+'/audit-02.md']
for p in protected:
    assert blob(p)==blob(p,PREVIOUS),p
old = git('ls-tree','-r','--name-only',PREVIOUS,TOPIC+'/checks/code',
          TOPIC+'/audit-support',TOPIC+'/audit-02-support').decode().splitlines()
for p in old:
    assert blob(p)==blob(p,PREVIOUS),p

# Fresh execution of the new developer checker, without replacing its output.
checker_path=TOPIC+'/checks/code/response-02/ritz_saturated_centre.py'
run=subprocess.run([sys.executable,'-I',str(ROOT/checker_path)],capture_output=True,text=True,check=True)
observed=json.loads(run.stdout)
assert observed==json.loads(blob(checker_path.replace('.py','.out')))
assert observed=={'rank_V':6,'s_2(0)':'1','residual_x_zero':True,'residual_y_zero':True}

# Independent nodal argument: the degree-two cardinal polynomial is zero on
# every off-centre node; xK and yK therefore vanish on the whole support.
x,y=s.symbols('x y')
nodes=[(0,0),(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)]
cardinal=1-x*x-y*y+x*y
values=[cardinal.subs({x:a,y:b}) for a,b in nodes]
assert values==[1,0,0,0,0,0,0]
V=s.Matrix([[1,a,b,a*a,a*b,b*b] for a,b in nodes])
assert V.rank()==6
assert all(a*v==0 and b*v==0 for (a,b),v in zip(nodes,values))

# Algebraic verification of the similarity/weighted-symmetry reduction in
# the proposed B5 route. This is not a genericity theorem or witness.
a,b,c,u,v,w=s.symbols('a b c u v w',real=True)
D=s.diag(2,3); H=s.Matrix([[a,b],[b,c]]); E=s.Matrix([[u,v],[v,w]])
Hhat=D*H*D.inv(); F=D*E*D.inv()
assert s.simplify(F-D**2*F.T*D**-2)==s.zeros(2)
assert s.simplify(Hhat*F-F*Hhat-D*(H*E-E*H)*D.inv())==s.zeros(2)

proof=blob('PROOF_STATUS.md').decode()
prior_proof=blob('PROOF_STATUS.md',PREVIOUS).decode()
def statuses(text):
    return {q[1].strip():q[3].strip() for line in text.splitlines()
            if line.startswith('| PD-') and (q:=line.split('|'))
            and '?programme-ideas-claude-' in q[1]}
assert statuses(proof)==statuses(prior_proof) and len(statuses(proof))==11

ids=[]
for p in sorted(set(changed+protected)):
    data=blob(p)
    ids.append({'path':p,'git_blob_sha':git('rev-parse',SOURCE+':'+p).decode().strip(),
                'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
print(json.dumps({'candidate':SOURCE,'main':MAIN,'previous_audit_delivery':PREVIOUS,
    'python':platform.python_version(),'sympy':s.__version__,
    'changed_paths':changed,'previous_code_and_audit_support_files_unchanged':len(old),
    'protected_files_unchanged':protected,'developer_checker':{'command':[sys.executable,'-I',checker_path],
      'result':observed,'matches_committed_output':True},
    'independent_cardinal':str(cardinal),'independent_nodal_values':list(map(str,values)),
    'independent_rank':6,'weighted_symmetry_similarity_check':True,
    'statuses_unchanged':statuses(proof),'source_identities':ids,
    'result':'PASS; open formulations are reviewed as targets, not proved results'},indent=2))
