"""Independent audit-05 checks. Uses Git read-only and writes only disposable copies.

Usage from repository root: python3 -I .../check_integration_independent.py CANDIDATE
Semantic expectations below were reviewed against all 77 theory records; this
script does not import the developer's checker or allocator implementation.
"""
import collections
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import sys
import tarfile
import tempfile

BASE = '183d33760e8d6c3ecdeb588576bd65ba312f65fe'
TOP = 'topics/bivariate-lanczos-20261031'
PREP = TOP + '/pr-prep'
candidate = sys.argv[1]

def git(*args):
    return subprocess.check_output(['git', *args])

def content(rev, path):
    return git('show', rev + ':' + path).decode()

def inventory(rev):
    out = {}
    for entry in git('ls-tree', '-rz', rev).split(b'\0'):
        if entry:
            meta, path = entry.split(b'\t', 1)
            out[path.decode()] = meta.split()[2].decode()
    return out

def sha(data):
    return hashlib.sha256(data).hexdigest()

def aggregate(mapping):
    return sha(json.dumps(mapping, sort_keys=True, separators=(',', ':')).encode())

def protected(path):
    return (path.startswith('tracks/bivariate-lanczos/theory/')
            or path.startswith('tracks/bivariate-lanczos/code/')
            or any(path.startswith(TOP + '/' + p) for p in
                   ['directions/', 'reviews/', 'repro/', 'sources/', 'lit/'])
            or bool(re.match(re.escape(TOP) + r'/audit-0[1-4](?:/|\.md$)', path))
            or path in [TOP + '/' + p for p in
                        ['plan.md', 'baseline-candidates.md', 'audit-handoff.md']])

old, new = inventory(BASE), inventory(candidate)
selected = {p: h for p, h in old.items() if protected(p)}
changes = [p for p, h in selected.items() if new.get(p) != h]
assert not changes, changes
assert all(old[p] == new[p] for p in
           ['AGENTS.md', 'agents/WORKFLOW.md', 'agents/codex/CODEX.md'])
lower_bound = json.loads(content(BASE, TOP + '/audit-04/aggregate-output-lower-bound.json'))
assert len(lower_bound['artifacts']) == 348
assert sum(a['bytes'] for a in lower_bound['artifacts']) == 5078141
assert all(new[a['path']] == a['git_blob'] for a in lower_bound['artifacts'])
blob_sizes = subprocess.check_output(
    ['git', 'cat-file', '--batch-check=%(objectsize)'],
    input=''.join(a['git_blob'] + '\n' for a in lower_bound['artifacts']).encode())
assert list(map(int, blob_sizes.splitlines())) == [a['bytes'] for a in lower_bound['artifacts']]
mapping_path = PREP + '/id-map.json'
mapping = json.loads(content(candidate, mapping_path))
assert mapping == json.loads(content(BASE, mapping_path))
assert len(mapping['map']) == len(set(mapping['map'].values())) == 404
theories = mapping['theory_files']
assert len(theories) == 77
status_counts = collections.Counter()
for provisional, path in theories.items():
    text = content(candidate, path)
    assert text == content(BASE, path), path
    headers = re.findall(r'^Final ID: \*\*([^*]+)\*\*', text, re.M)
    assert headers == [mapping['map'][provisional]], (path, headers)
    status_counts[re.search(r'Overall status:\s*\**([A-Z]+)', text)[1]] += 1
assert status_counts == {'PROVED': 38, 'MEASURED': 34, 'OPEN': 4, 'CONDITIONAL': 1}

# Independent expectations, manually reconstructed from dependency assertions,
# their exclusions, filename references, and definitions in records lacking a
# dependency heading. T078 explicitly says "No registry dependency".
expected_text = '''
T029:
T030:T029
T031:T030,T032
T032:T029,T030
T033:T029,T032
T034:T030,T032
T035:T031,T032,T034
T036:T029,T032
T037:T032,T033,T035,T036
T038:T032,T033
T039:T033,T029
T040:T032,T038,T039
T041:T029,T032
T042:T029,T033,T039
T043:T039,T040,T042,T045
T044:T033,T032
T045:T042,T039,T040
T046:T029
T047:T029,T032,T034,T046
T048:T034,T032,T029
T049:T046,T047
T050:T047,T029,T032
T051:T053,T047
T052:T046,T047,T050,T053,T048
T053:
T054:T050
T055:T047,T053,N013
T056:T057,T058,T059,T060,T061,T062,T063,T064,T066,T067,T068,T069,T070,T071,T072,T073,T074,T075,N020,N021,N022,N028
T057:
T058:T057
T059:T058
T060:T057
T061:T059
T062:T059
T063:T059
T064:
T065:T059
T066:T059
T067:T066
T068:T065
T069:T065,T068
T070:T057,T032,T030
T071:T070
T072:T060,T074,T065
T073:T074
T074:T057,T060,T065
T075:T058,T059,T069,N020,N022
T076:T029
T077:
T078:
T079:T080
T080:
N007:T029
N008:T029
N009:T032,T035,T037,T040
N010:T042,T045,T043
N011:T029,T036,T037
N012:T035
N013:T046,T047,T053,T029,T032
N014:T047,T048
N015:T053,T051
N016:T043,T053
N017:T048
N018:T046,T049
N019:T048,T052
N020:T057,T058,T059
N021:T058,T059,T060
N022:T057,T058,T059,T065,T068,T069
N023:T064,N020
N024:T065,T062
N025:T066,N020
N026:T070
N027:T057,T059,T071
N028:T057,T058
N029:T080,T079
N030:N029
N031:T079
'''
expected = {}
for line in expected_text.strip().splitlines():
    fid, deps = line.split(':')
    expected['PD-' + fid] = {'PD-' + d for d in deps.split(',') if d}

def cells(line):
    return [x.strip() for x in re.split(r'(?<!\\)\|', line.strip())[1:-1]]

def rows(text, pattern):
    return {cells(line)[0]: cells(line) for line in text.splitlines()
            if re.match(pattern, line)}

ps = rows(content(candidate, 'PROOF_STATUS.md'), r'^\| PD-[TN]\d{3} \|')
assert len(expected) == 77
for fid, deps in expected.items():
    actual = set(re.findall(r'PD-[TN]\d{3}', ps[fid][5].split('. ', 1)[0]))
    assert actual == deps, (fid, actual, deps)

own_ideas = {v for k, v in mapping['map'].items() if k.startswith('IDEA?')}
idea_rows = rows(content(candidate, 'state/IDEAS.md'), r'^\| IDEA-\d{3} \|')
assert len(own_ideas) == 100 and own_ideas <= idea_rows.keys()
for fid in own_ideas:
    row = idea_rows[fid]
    assert len(row) == 5, (fid, len(row))
    assert row[3] and row[3] not in ['pending.', 'see record'], fid
    assert not re.search(r'(?:PD-[TN]|LIT|IDEA)\?', row[2] + row[3]), fid
    assert not re.search(r'(?:PD-[TN]\d{3}|LIT-\d{3})(?:\([^)]*\))?\s*[,/]\s*-?\d{3}\b', row[2] + row[3]), fid
for generated, shared, count in [
        ('proof_status', 'PROOF_STATUS.md', 77),
        ('ideas', 'state/IDEAS.md', 100),
        ('crosswalk', 'ID_CROSSWALK.md', 404),
        ('negative', 'tracks/bivariate-lanczos/NEGATIVE_RESULTS.md', 25)]:
    package = content(candidate, PREP + '/' + generated + '.rows.md').splitlines()
    published = content(candidate, shared).splitlines()
    assert len(package) == count
    assert all(line in published for line in package), generated
    if generated == 'negative':
        for line in package:
            row = cells(line)
            assert not re.search(r'(?:PD-[TN]|LIT|IDEA)\?', row[1] + row[2]), row[0]
            assert not re.search(r'(?:PD-[TN]\d{3}|IDEA-\d{3}|LIT-\d{3})(?:\([^)]*\))?\s*[,/]\s*-?\d{3}\b', row[1] + row[2]), row[0]
for shared, marker in [('PROOF_STATUS.md', '## Bivariate Lanczos track'),
                       ('state/IDEAS.md', '## Bivariate Lanczos campaign'),
                       ('ID_CROSSWALK.md', '## Bivariate Lanczos campaign')]:
    before, after = content(BASE, shared), content(candidate, shared)
    assert marker in before and marker in after, shared
    assert before.split(marker)[0] == after.split(marker)[0], shared

# Compare every numbered literature statement, stopping at the next heading.
def statement_blocks(rev, inv):
    blocks = {}
    for path in inv:
        if path.startswith('literature/records/') and path.endswith('.md'):
            text = content(rev, path)
            for match in re.finditer(r'^#{2,4} (LIT-\d{3})\b[^\n]*\n', text, re.M):
                stop = re.search(r'^#{1,6} ', text[match.end():], re.M)
                end = match.end() + stop.start() if stop else len(text)
                key = match[1]
                assert key not in blocks, key
                blocks[key] = text[match.start():end].rstrip()
    return blocks
lit_old, lit_new = statement_blocks(BASE, old), statement_blocks(candidate, new)
assert len(lit_old) == len(lit_new) == 292
assert lit_old == lit_new
canonical = 'literature/records/mourrain-telen-vanbarel.md'
assert content(candidate, canonical).startswith(content(BASE, canonical))
alias = content(candidate, 'literature/records/telen-mourrain-vanbarel-2018.md')
assert '(mourrain-telen-vanbarel.md)' in alias and not re.search(r'^#{2,4} LIT-', alias, re.M)
corpus = content(candidate, 'literature/CORPUS.md')
assert len(re.findall(r'^\| mourrain-telen-vanbarel \|', corpus, re.M)) == 1
assert not re.search(r'^\| telen-mourrain-vanbarel-2018 \|', corpus, re.M)
assert 'schmudgen-ten-lectures-2020' in corpus
idx = content(candidate, 'literature/INDEX.md')
topic_lit_rows = [cells(line) for line in idx.splitlines()
                  if line.startswith('| ') and 'LIT?bivariate-lanczos-claude-' in cells(line)[0]]
assert len(topic_lit_rows) == 227
for row in topic_lit_rows:
    provisional = re.search(r'LIT\?bivariate-lanczos-claude-\d{3}', row[0])[0]
    fid = re.match(r'LIT-\d{3}', row[0])[0]
    assert mapping['map'][provisional] == fid
    record = re.search(r'(records/[a-z0-9-]+\.md)', row[5])[1]
    assert re.search(r'^#{2,4} ' + fid + r'\b', content(candidate, 'literature/' + record), re.M)
    assert Path(record).stem == row[3]
tnf = next(row for row in topic_lit_rows if row[0].startswith('LIT-259 '))
assert tnf[3] == 'mourrain-telen-vanbarel'

# Execute the submitted allocator only in disposable archives of the exact head.
execution_records = []
integration_result = None
with tempfile.TemporaryDirectory(prefix='padua-audit05-') as temporary:
    directory = Path(temporary)
    archive = git('archive', '--format=tar', candidate)
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
        tar.extractall(directory, filter='data')
    integration = subprocess.run([sys.executable, '-I', PREP + '/check_integration.py'],
                                 cwd=directory, capture_output=True, text=True)
    assert integration.returncode == 0, integration.stdout + integration.stderr
    integration_result = json.loads(integration.stdout)
    def fingerprint():
        return {str(p.relative_to(directory)): sha(p.read_bytes())
                for p in directory.rglob('*') if p.is_file()}
    def run(mode, expect=0):
        command = [sys.executable, '-I', PREP + '/allocate.py', *mode]
        result = subprocess.run(command, cwd=directory, capture_output=True, text=True)
        execution_records.append({'args': mode, 'expected_exit': expect,
                                  'exit': result.returncode,
                                  'stdout': result.stdout.strip(), 'stderr': result.stderr.strip()})
        assert (result.returncode == 0) == (expect == 0), execution_records[-1]
    original = fingerprint()
    for mode in [[], [], ['--check'], ['--apply'], ['--apply']]:
        run(mode)
        assert fingerprint() == original, ('repeat mutated final tree', mode)

    # Recreate genuinely unfinalized headers and literature forms, while keeping
    # the frozen allocation and scientific source bodies. --apply must restore
    # the exact candidate tree, and default invocation must not touch inputs.
    for path in theories.values():
        p = directory / path
        p.write_text(re.sub(r'\n\nFinal ID:[^\n]*\n', '\n', p.read_text(), count=1))
    for p in [directory / 'literature/INDEX.md', *(directory / 'literature/records').glob('*.md')]:
        text = p.read_text()
        text = re.sub(r'^(#{2,4} |\| )LIT-\d{3} \((LIT\?bivariate-lanczos-claude-\d{3})\)',
                      r'\1\2', text, flags=re.M)
        p.write_text(text)
    provisional = fingerprint()
    run([])
    assert fingerprint() == provisional, 'default modified provisional inputs'
    run(['--apply'])
    assert fingerprint() == original, '--apply did not exactly restore final tree'
    run(['--apply'])
    assert fingerprint() == original

    # Malformed existing headers must fail before changing any file.
    p = directory / next(iter(theories.values()))
    text = p.read_text()
    p.write_text(text + '\nFinal ID: **PD-T999**\n')
    malformed = fingerprint()
    run(['--apply'], expect=1)
    assert fingerprint() == malformed, 'invalid-header failure mutated files'
    p.write_text(text)
    frozen_map = directory / mapping_path
    altered = json.loads(frozen_map.read_text())
    keys = list(altered['theory_files'])[:2]
    altered['map'][keys[0]], altered['map'][keys[1]] = altered['map'][keys[1]], altered['map'][keys[0]]
    frozen_map.write_text(json.dumps(altered))
    changed_map = fingerprint()
    run(['--apply'], expect=1)
    assert fingerprint() == changed_map, 'changed-map failure mutated files'

print(json.dumps({
    'baseline': BASE, 'candidate': candidate,
    'protected_files_unchanged': len(selected),
    'protected_path_blob_inventory_sha256': aggregate(selected),
    'theory_files_exactly_unchanged': len(theories),
    'status_counts': status_counts,
    'allocations_stable': 404, 'dependency_rows_independently_matched': len(expected),
    'preserved_repository_output_lower_bound': {'files': 348, 'bytes': 5078141,
       'limit': 5000000, 'scope': 'Selected historical outputs only; excludes audit-04/05 additions. Gate not discharged.'},
    'idea_rows_checked': len(own_ideas), 'literature_statement_blocks_preserved': len(lit_old),
    'topic_literature_paths_validated': len(topic_lit_rows),
    'developer_integration_checker_rerun': integration_result,
    'python_version': sys.version,
    'disposable_allocator_executions': execution_records,
    'scope': 'Technical preservation, registry integrity, literature relocation and allocator execution; semantic source review is documented in audit-05.md. No mathematical producer reruns.'
}, indent=2))
