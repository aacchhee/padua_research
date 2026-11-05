"""Validate PR21's mechanical registration and preservation boundaries."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote

ap = argparse.ArgumentParser()
ap.add_argument('--repo', type=Path, default=Path('.'))
ap.add_argument('--base', default='65b24972954a6e13e950a489ef9ecb0397601328')
ap.add_argument('--receipt', type=Path)
a = ap.parse_args()
root = a.repo.resolve()
topic = 'topics/padua-literature-20261103'
prep = root/topic/'preparation'
def git(*args):
    return subprocess.check_output(['git','-C',str(root),*args],stderr=subprocess.PIPE)
def old(path):
    return git('show',a.base+':'+path).decode()
def read(path):
    return (root/path).read_text()
def sha(s):
    return hashlib.sha256(s.encode()).hexdigest()
def canonical(s):
    rows = {}
    for line in s.splitlines():
        m = re.match(r'^\| (LIT-\d{3})(?!\d)(?: |\()',line)
        if m:
            rows.setdefault(m[1],[]).append(line)
    return rows

m = json.loads((prep/'final-id-map.json').read_text())
mapping = m['mapping']
aliases = set(re.findall(r'LIT\?padua-literature-claude-\d{2}(?!\d)',read(topic+'/proposed-record-changes.md')))
assert set(mapping)==aliases and len(mapping)==58
new = {f'LIT-{n}' for n in range(482,513)}
base_index = canonical(old('literature/INDEX.md'))
index = canonical(read('literature/INDEX.md'))
assert len(new)==31 and new.isdisjoint(base_index)
assert all(len(index.get(k,[]))==1 for k in new)
assert all(len(re.split(r'(?<!\\)\|',index[k][0]))==9 for k in new),'New INDEX table must render seven columns'
assert all(k in base_index for k in set(mapping.values())-new)
assert not any(f'LIT-{n}' in index for n in range(513,562))
assert all(len(v)<=max(1,len(base_index.get(k,[]))) for k,v in index.items())

# Only explicitly audited existing INDEX rows may change.
proposal = read(topic+'/proposed-record-changes.md')
allowed = set()
for match in re.finditer(r'(?m)^Old[^\n]*\n(?:\s*\n)*```[^\n]*\n(.*?)\n```',proposal,re.S):
    row = re.match(r'\| (LIT-\d{3})(?!\d)',match[1])
    if row:
        allowed.add(row[1])
for k,v in base_index.items():
    assert k in index,('lost accepted ID',k)
    if k not in allowed:
        assert index[k]==v,('foreign INDEX row changed',k)

def corpus_keys(s):
    return Counter(x[1] for x in re.finditer(r'^\| ([a-z][a-z0-9-]+) \|',s,re.M))
before = corpus_keys(old('literature/CORPUS.md'))
after = corpus_keys(read('literature/CORPUS.md'))
assert all(after[k]==v for k,v in before.items()),'Existing corpus key removed/duplicated'
assert all(v==1 for k,v in after.items() if k not in before)

for path in ['PROOF_STATUS.md','state/IDEAS.md','AGENTS.md','agents/WORKFLOW.md','agents/codex/CODEX.md']:
    assert read(path)==old(path),('protected scientific/rule file changed',path)
for path in git('ls-tree','-r','--name-only',a.base,topic).decode().splitlines():
    if '/audit-' in path or '/audit-support/' in path:
        assert read(path)==old(path),('immutable audit changed',path)

app = json.loads((prep/'application-receipt.json').read_text())
applied = {x['path']:x for x in app['changed']}
def without_registration(s):
    s = re.sub(r'\n\nRegistration \(2026-11-05 PR21 final registration\):[^\n]*\n','\n',s)
    return re.sub(r'(?m)^(#{2,4}) LIT-\d{3} \((LIT\?padua-literature-claude-\d{2})\)',r'\1 \2',s)
checked_bodies = 0
for f in (root/'literature/records').glob('*.md'):
    if '2026-11-05 PR21 final registration' not in f.read_text():
        continue
    path = f.relative_to(root).as_posix()
    expected = applied[path]['after_sha256'] if path in applied else sha(old(path))
    assert sha(without_registration(f.read_text()))==expected,('body changed beyond ID labels',path)
    checked_bodies += 1

for path,marker in [
    ('ID_CROSSWALK.md','## Padua literature campaign — PR21 final source-statement mapping'),
    ('topics/padua-batch-20261031/ALLOCATIONS.md','## PR21 audited literature registration'),
    ('state/CURRENT.md','## Literature footing — PR21 audited registration'),
    ('PAPER_MAP.md','## Audited literature footing — PR21'),
    ('topics/README.md','## Padua literature campaign — audited PR21 registration')]:
    assert read(path).split(marker,1)[0].rstrip()==old(path).rstrip(),('foreign prefix changed',path)
cross = read('ID_CROSSWALK.md').split('## Padua literature campaign — PR21 final source-statement mapping',1)[1]
assert all(cross.count('| '+k+' | '+v+' |')==1 for k,v in mapping.items())

marker = '## padua-literature-20261103\n'
head,section = read('RESULTS.md').split(marker,1)
assert head.rstrip()==old('RESULTS.md').rstrip(),'foreign RESULTS sections changed'
expected = read('results/padua-literature-20261103.md').split('\n',1)[1].lstrip().replace('(../topics/','(topics/')
assert section.strip()==expected.strip(),'own RESULTS content differs beyond link rebasing'

# Inspect newly added links only; unrelated inherited broken links are outside scope.
changed = set(git('diff','--name-only',a.base).decode().splitlines())
changed.update(git('ls-files','--others','--exclude-standard').decode().splitlines())
broken = []
links = 0
for path in sorted(changed):
    f = root/path
    if not f.is_file() or f.suffix!='.md':
        continue
    try:
        prior = old(path)
    except subprocess.CalledProcessError:
        prior = ''
    prior_links = set(re.findall(r'\[[^\]]*\]\(([^)]+)\)',prior))
    for target in set(re.findall(r'\[[^\]]*\]\(([^)]+)\)',f.read_text()))-prior_links:
        if re.match(r'\w+://|mailto:|#',target):
            continue
        target = unquote(target.split('#',1)[0].strip('<>'))
        if not target:
            continue
        links += 1
        if not (f.parent/target).exists():
            broken.append([path,target])
assert not broken,('new broken local links',broken)

json_sizes = {str(f.relative_to(root)):f.stat().st_size for f in (root/topic).rglob('*.json')}
assert all(n<16384 for n in json_sizes.values()),'Oversized topic JSON evidence'
suffixes = {'.json','.out','.txt','.csv','.log','.npy','.npz','.pdf','.png','.dat','.bin','.cert'}
files = git('ls-files','--cached','--others','--exclude-standard').decode().splitlines()
inventory = {x:(root/x).stat().st_size for x in files if (root/x).is_file() and Path(x).suffix.lower() in suffixes}
assert sum(inventory.values())<5000000,'Conservative generated-output budget exceeded'
subprocess.run(['git','-C',str(root),'diff','--check'],check=True)
receipt = {'result':'PASS','base':a.base,'aliases':len(mapping),'new_ids':sorted(new),
           'reused_aliases':sum(v not in new for v in mapping.values()),'normalized_record_bodies':checked_bodies,
           'new_local_links_checked':links,'broken_links':broken,'canonical_ID_collisions':False,
           'foreign_content_preserved':True,'PD_statuses_and_rules_unchanged':True,
           'conservative_generated_bytes':sum(inventory.values()),'generated_limit':5000000,
           'max_topic_json_bytes':max(json_sizes.values()),
           'limits':'Mechanical registration only; no new source/numerical verification or readiness declaration.'}
if a.receipt:
    a.receipt.write_text(json.dumps(receipt,separators=(',',':'))+'\n')
print(json.dumps(receipt,indent=2))
