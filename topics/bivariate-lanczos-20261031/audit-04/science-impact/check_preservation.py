"""Independent audit-04 identity/integration check; runs no mathematical producer.

Run from the repository root with python3 -B -I. Git operations are read-only.
"""
from pathlib import Path
import hashlib
import json
import platform
import re
import subprocess
import sys

ACCEPTED = 'cf01449fc96233c9074ce25efcb056535414aa1d'
HEAD = 'a2dd845b8a231e1b00733e1361e2a9ad3bad222f'
MAIN = '9739a0c56b7a3976422ce60a8441bfbbfd6554df'
TOPIC = 'topics/bivariate-lanczos-20261031/'
TRACK = 'tracks/bivariate-lanczos/'


def git(*args):
    return subprocess.check_output(['git', *args])


def sha(b):
    return hashlib.sha256(b).hexdigest()


def content(commit, path):
    return git('show', f'{commit}:{path}')


def tree(commit):
    out = {}
    for entry in git('ls-tree', '-r', '-z', commit).split(b'\0'):
        if not entry:
            continue
        meta, path = entry.split(b'\t', 1)
        mode, kind, blob = meta.decode().split()
        out[path.decode()] = dict(mode=mode, kind=kind, blob=blob)
    return out


base, head, main = tree(ACCEPTED), tree(HEAD), tree(MAIN)
mapping = json.loads(content(HEAD, TOPIC+'pr-prep/id-map.json'))['map']
theory = sorted(p for p in base if p.startswith(TRACK+'theory/') and p.endswith('.md'))
assert len(theory) == 77
assert set(theory) == {p for p in head if p.startswith(TRACK+'theory/') and p.endswith('.md')}
theory_results = []
final_pattern = rb'Final ID: \*\*(PD-[TN][0-9]{3})\*\* \(allocated at PR preparation, 2026-11-01; the provisional ID above and in the text is retained as provenance \xe2\x80\x94 see ID_CROSSWALK\.md\)\.\n\n'
for p in theory:
    before, after = content(ACCEPTED, p), content(HEAD, p)
    provisional = re.search(rb'^# (PD-[TN]\?bivariate-lanczos-claude-\d+)', before).group(1).decode()
    finals = re.findall(final_pattern, after)
    stripped, count = re.subn(final_pattern, b'', after)
    status = re.search(rb'^Overall status:.*$', before, re.M)
    assert count == 1 and stripped == before, p
    assert finals[0].decode() == mapping[provisional], p
    assert Path(p).read_bytes() == after, p
    theory_results.append(dict(path=p, provisional=provisional, final_id=finals[0].decode(),
        status_line=status.group().decode() if status else None,
        accepted_sha256=sha(before), head_sha256=sha(after),
        accepted_git_blob=base[p]['blob'], head_git_blob=head[p]['blob'],
        only_final_id_line_and_blank_added=True))

# All pre-existing topic and track files are frozen except these explicit administrative changes
# and the theory-ID headers checked above. This includes scripts, raw data, outputs,
# checker implementations, manifests, reviews, handoffs and accepted audit records.
admin = {TOPIC+'LOG.md', TOPIC+'progress.md', TOPIC+'lit/search-log.md',
         TRACK+'AUDIT_LOG.md', TRACK+'NEGATIVE_RESULTS.md'}
protected = sorted(p for p in base if p.startswith((TOPIC, TRACK)) and p not in admin and p not in theory)
frozen = []
for p in protected:
    assert p in head and base[p] == head[p], p
    data = content(HEAD, p)
    assert Path(p).read_bytes() == data, p
    frozen.append(dict(path=p, git_blob=head[p]['blob'], sha256=sha(data), bytes=len(data)))
added = sorted(p for p in head if p.startswith((TOPIC, TRACK)) and p not in base)
assert all(p.startswith(TOPIC+'pr-prep/') for p in added), added

summaries = ['state/CURRENT.md', 'PAPER_MAP.md', TRACK+'README.md', TRACK+'AUDIT_LOG.md', TOPIC+'report.md']
summary_records = []
id_to_theory = {r['final_id']:r for r in theory_results}
for p in summaries:
    data = content(HEAD, p)
    assert Path(p).read_bytes() == data, p
    ids = sorted(set(re.findall(r'PD-[TN]\d{3}', data.decode())))
    topic_ids = [i for i in ids if i in id_to_theory]
    links = []
    for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)', data.decode()):
        if '://' in target or target.startswith('#'):
            continue
        target = target.split('#')[0]
        resolved = (Path(p).parent/target).resolve()
        links.append(dict(target=target, exists=resolved.exists()))
    assert all(x['exists'] for x in links), p
    summary_records.append(dict(path=p, sha256=sha(data), git_blob=head[p]['blob'],
        same_as_accepted=(p in base and head[p] == base[p]),
        same_as_main=(p in main and head[p] == main[p]),
        referenced_topic_ids={i:dict(path=id_to_theory[i]['path'], status=id_to_theory[i]['status_line'])
                              for i in topic_ids}, markdown_links=links))

rule_paths = ['AGENTS.md', 'agents/WORKFLOW.md', 'agents/codex/CODEX.md']
rules = [dict(path=p, sha256=sha(content(HEAD,p)), git_blob=head[p]['blob'],
              same_as_accepted=head[p] == base[p], same_as_main=head[p] == main[p]) for p in rule_paths]
counts = {
    'theory_header_only':len(theory), 'frozen_preexisting_topic_and_track_files':len(frozen),
    'frozen_code_files':sum(p.startswith(TRACK+'code/') for p in protected),
    'frozen_direction_files':sum(p.startswith(TOPIC+'directions/') for p in protected),
    'frozen_review_files':sum(p.startswith(TOPIC+'reviews/') for p in protected),
    'frozen_audit_files':sum(p.startswith(TOPIC+'audit-') for p in protected),
    'new_pr_prep_administrative_files':len(added),
}
result = dict(scope='Scientific identity, final-ID header consistency and summary link targets; no proof/experiment or novelty re-audit.',
    accepted=ACCEPTED, reviewed_head=HEAD, main=MAIN, actual_head=git('rev-parse','HEAD').decode().strip(),
    environment=dict(python=sys.version, platform=platform.platform()),
    counts=counts, result='PASS for identity and links; prose/status correctness is independently reviewed in science-impact.md',
    rules=rules, theory=theory_results, frozen_files=frozen,
    administrative_changed_paths=sorted(admin), added_paths=added, summaries=summary_records)
print(json.dumps(result, indent=2, sort_keys=True))
