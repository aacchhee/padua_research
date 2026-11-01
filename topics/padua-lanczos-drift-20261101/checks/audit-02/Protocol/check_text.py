#!/usr/bin/env python3
"""Check literal proposal anchors and bounded administrative invariants."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[5]
TOPIC = 'topics/padua-lanczos-drift-20261101'
HEAD = '7a6dd1f7f8f10d0f9c2568e89d693b7d04cd571b'
MAIN = '28aaa20861d08074b77efc74eaef75cdcb36234d'
RESPONSE = 'cef79d66321a93d93d53e53efcb7e6744c387481'
THEORY = 'tracks/bivariate-lanczos/theory/'

def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])

def contents(revision, path):
    return git('show', revision + ':' + path).decode()

def identity(path):
    data = (ROOT/path).read_bytes()
    return {'path':path, 'bytes':len(data), 'sha256':hashlib.sha256(data).hexdigest()}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    path=TOPIC+'/proposed-record-changes.md'
    text=contents(HEAD,path)
    matches=list(re.finditer(r'OLD\n```text\n(.*?)\n```\s*NEW\n```text\n(.*?)\n```',text,re.S))
    targets=[
        'bj-universal-reorthogonalization-obstruction-open.md',
        'condition-C-staircase-selections-acyclic-sections.md',
        'bivariate-lanczos-claude-300-l3q1-backward-interpretation-target.md',
        *['bivariate-lanczos-claude-319-padua-obstruction-radius-uniformity.md']*3,
        'reorthogonalization-does-not-restore-graded-spaces.md',
        'one-relation-selections-do-not-keep-spans-near-Sn.md',
        *['bivariate-lanczos-claude-319-padua-obstruction-radius-uniformity.md']*4,
        *['bivariate-lanczos-claude-313-padua-turan-certificate-all-n.md']*2,
        'bivariate-lanczos-claude-305-three-node-square-case-sqrt-rate.md']
    assert len(matches)==len(targets)==15
    anchors=[]
    dry={}
    for index,(match,target) in enumerate(zip(matches,targets),1):
        target=THEORY+target
        old,new=match.groups()
        dry.setdefault(target,contents(MAIN,target))
        anchors.append({'block':index,'proposal_line':text[:match.start()].count('\n')+1,
            'target':target,'old_sha256':hashlib.sha256(old.encode()).hexdigest(),
            'old_occurrences_at_main':contents(MAIN,target).count(old),
            'old_occurrences_at_head':contents(HEAD,target).count(old),
            'old_occurrences_after_previous_proposals':dry[target].count(old)})
        if dry[target].count(old)==1:dry[target]=dry[target].replace(old,new,1)
    history='2026-10-31, Claude Opus 5.5 (xhigh, requested), L3 developer, base 2d8c3ab: created in round R01.'
    target=THEORY+'bivariate-lanczos-claude-305-three-node-square-case-sqrt-rate.md'
    anchors.append({'block':'optional_history','target':target,
        'old_occurrences_at_main':contents(MAIN,target).count(history),
        'old_occurrences_at_head':contents(HEAD,target).count(history),
        'old_occurrences_after_previous_proposals':dry[target].count(history)})
    files=['AGENTS.md','agents/WORKFLOW.md','agents/codex/CODEX.md',
        TOPIC+'/handoffs/06-reaudit.md',TOPIC+'/audit-01.md',TOPIC+'/checks/audit-01/E6-novelty-protocol.md',
        TOPIC+'/response-01.md',TOPIC+'/LOG.md',TOPIC+'/COLD_STORAGE.md',TOPIC+'/proposed-record-changes.md',
        TOPIC+'/local-results-entry.md','results/padua-lanczos-drift-20261101.md',
        TOPIC+'/ideas-e1.md',TOPIC+'/ideas-e5.md',TOPIC+'/ideas-e6.md',
        TOPIC+'/evidence/archive-receipt.json',TOPIC+'/evidence/response-01-manifest.json',
        'tracks/bivariate-lanczos/code/drift/e1_reproduce.py']
    files += [str(p.relative_to(ROOT)) for p in sorted((ROOT/TOPIC/'checks/response-01').glob('*.md'))]
    result={'rules_and_audited_head':HEAD,'current_main':MAIN,'scientific_response_candidate':RESPONSE,
        'scope':'Literal OLD anchors, immutable original theory checks and administrative provenance; no new novelty or mathematical status judgment.',
        'anchors':anchors,'all_anchors_unique':all(all(x[k]==1 for k in ['old_occurrences_at_main','old_occurrences_at_head','old_occurrences_after_previous_proposals']) for x in anchors),
        'response_scientific_changes_since_candidate':git('diff','--name-only',RESPONSE,HEAD,'--','tracks/bivariate-lanczos/code/drift','tracks/bivariate-lanczos/theory/drift-codex-*',TOPIC+'/evidence/response-01-*').decode().splitlines(),
        'immutable_audit01_changes_since_candidate':git('diff','--name-only',RESPONSE,HEAD,'--',TOPIC+'/audit-01.md',TOPIC+'/checks/audit-01').decode().splitlines(),
        'files_read_identities':[identity(p) for p in files],
        'source_provenance_correction':{'basis':'Exact AC request quotations supplied by the current orchestrator audit brief; audit-01 did not have this prompt.',
            'quotes':['Campaign mode adventurous and less gated','Relaxed novelty gate at start and before each new mechanism'],
            'scope':'Corrects authority provenance only. Does not change the historically performed gate or justify inventing omitted gate checks.'},
        'historical_receipt_rule':'Audit-01 Windows delivery and readback are attributed to Claude LOG:90; this audit has no Windows bridge and does not re-verify that delivery.',
        'preparation_advisory':{'file':TOPIC+'/proposed-record-changes.md','line':143,
            'issue':'Active preparation prose still points to a local Windows results file and a modification-time guard for shared RESULTS.md.',
            'current_rule':'agents/WORKFLOW.md repository-only results; topic orchestrator updates own results/<slug>.md, and only own root RESULTS.md section at PR preparation. No further Windows results write.'}}
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['files_read_identities','anchors']},indent=2))

if __name__=='__main__': main()
