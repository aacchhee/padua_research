#!/usr/bin/env python3
"""Independent read-only allocation audit; never imports or applies allocator.

Run from repository root with python3 -I <this path>. Reads pinned Git objects,
executes the inspected allocator with NO arguments in disposable snapshots,
and emits evidence as JSON to stdout. No Git mutations or developer-file writes.
"""
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

SOURCE = '37820a528c863e5cfe2dc2f1f8879b4fd40cf210'
MAIN = '21e620ba8b5f0e0706f3a8c6613517df04d9d469'
BASELINE = 'f4e213390f66a8c9f0c6bd65131b97b78db873c8'
ALLOC = '6954664fc0906b7e5c8ff0f1804b077bd3b5861f'
PR11 = '97968d2c2d039cb0910e0ea50747fb2d9e01a262'
ROOT = Path(__file__).resolve().parents[3]
TOPIC = 'topics/programme-ideas-20261031/'
REGISTRIES = ['PROOF_STATUS.md', 'state/IDEAS.md', 'literature/INDEX.md', 'ID_CROSSWALK.md']
ID = r'(?:PD-[TN]\d{3}|IDEA-\d{3}|LIT-\d{3})'
manifest = {}
checks = []


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def read(path, rev=SOURCE):
    data = git('show', rev + ':' + path)
    manifest[rev + ':' + path] = hashlib.sha256(data).hexdigest()
    return data.decode()


def check(name, success, detail=None):
    checks.append({'name': name, 'pass': bool(success), 'detail': detail})


def rows(text):
    return [[x.strip() for x in line.split('|')[1:-1]]
            for line in text.splitlines() if line.startswith('| ')]


def fmt(ns, number):
    return ns + ('' if ns.startswith('PD') else '-') + f'{number:03d}'


allocation = json.loads(read(TOPIC + 'pr-prep/id-map.json'))
mapping = allocation['map']
merged = allocation['merged_without_new_id']
lat = json.loads(read('topics/lattice-unisolvence-20261031/provisional-id-map.json'))['rows']
pi_lit = [r[0] for r in rows(read(TOPIC + 'lit/baseline.md')) if r[0].startswith('LIT?')]
pi_theory_files = git('ls-tree', '-r', '--name-only', SOURCE, TOPIC + 'theory').decode().splitlines()
pi_theory = {read(p).splitlines()[0].split()[1]: p for p in pi_theory_files}
inventory = {r['id'] for r in lat} | set(pi_lit) | set(pi_theory) | {
    f'IDEA?programme-ideas-claude-{i:02d}' for i in range(1, 21)}
check('complete_inventory_208_provisionals', inventory == set(mapping) | set(merged), len(inventory))
check('192_unique_new_final_ids', len(mapping) == len(set(mapping.values())) == 192)
check('16_merged_rows_no_new_id', len(merged) == 16 and not set(merged) & set(mapping))
expected_ranges = {
    'lattice-unisolvence': {'PD-T': (81,94), 'PD-N': (32,38), 'IDEA': (177,189), 'LIT': (300,331)},
    'programme-ideas': {'PD-T': (95,100), 'PD-N': (39,43), 'IDEA': (190,209), 'LIT': (332,426)}}
for camp, namespaces in expected_ranges.items():
    tag = '?lattice-' if camp.startswith('lattice') else '?programme-ideas-'
    for ns, (lo, hi) in namespaces.items():
        got = {v for k,v in mapping.items() if k.startswith(ns + tag)}
        expected = {fmt(ns,n) for n in range(lo, hi + 1)}
        check(camp + '_' + ns + '_range', got == expected and allocation['blocks'][camp][ns] == [fmt(ns,lo),fmt(ns,hi),hi-lo+1])
check('next_unreserved', allocation['next_unreserved'] == {'PD-T':'PD-T101','PD-N':'PD-N044','IDEA':'IDEA-210','LIT':'LIT-427'})
independent_map = {}
for camp, namespaces in expected_ranges.items():
    for ns, (lo, hi) in namespaces.items():
        if camp == 'lattice-unisolvence':
            names = [r['id'] for r in lat if r['id'].startswith(ns+'?')]
            names.sort(key=lambda value: tuple(int(n) for n in re.findall(r'\d+', value)))
        elif ns == 'LIT':
            names = [pid for pid in pi_lit if pid not in merged]
        elif ns == 'IDEA':
            names = [f'IDEA?programme-ideas-claude-{i:02d}' for i in range(1,21)]
        else:
            names = sorted(pid for pid in pi_theory if pid.startswith(ns+'?'))
        independent_map.update({pid:fmt(ns,lo+i) for i,pid in enumerate(names)})
check('independently_reconstructed_exact_mapping', independent_map == mapping)
expected_merges = {}
for p, relation, target in [('integration-map.json','relation','existing_ids'), ('integration-map-pr10.json','relation_vs_pr10','pr10_ids')]:
    for entry in json.loads(read(TOPIC + 'lit/' + p)):
        if entry[relation] == 'same':
            expected_merges[entry['id']] = entry[target][0]
check('merged_map_matches_source_relation_maps', expected_merges == merged)
main_ids = set()
for path in REGISTRIES:
    main_ids.update(re.findall(ID, read(path, MAIN)))
check('no_collision_with_main', not set(mapping.values()) & main_ids)
reserved = {f'LIT-{i}' for i in range(293,300)}
check('no_collision_with_PR11_reserved_293_299', not reserved & set(mapping.values()))
pr11_ledger = read('topics/padua-batch-20261031/ALLOCATIONS.md',PR11)
check('exact_PR11_head_confirms_reserved_range', '**LIT-293–LIT-299**' in pr11_ledger and 'No PD-T, PD-N or IDEA is reserved here.' in pr11_ledger)
pr11_ids = {r[0].split()[0] for r in rows(read('literature/INDEX.md',PR11)) if re.match(r'LIT-\d{3}',r[0])}
check('exact_PR11_primary_rows_include_all_seven_reservations', reserved <= pr11_ids)
check('no_collision_with_exact_PR11_primary_rows', not pr11_ids & set(mapping.values()))
main_lit = {r[0].split()[0] for r in rows(read('literature/INDEX.md', MAIN)) if re.match(r'LIT-\d{3}',r[0])}
check('all_16_merge_targets_exist_on_main', set(merged.values()) <= main_lit)

registry_rows = {p: rows(read(p)) for p in REGISTRIES}
for path, prefixes in [('PROOF_STATUS.md',('PD-T','PD-N')),('state/IDEAS.md',('IDEA',)),('literature/INDEX.md',('LIT',))]:
    counts = Counter(re.match(ID,r[0]).group() for r in registry_rows[path] if re.match(ID,r[0]))
    wanted = {v for k,v in mapping.items() if k.startswith(prefixes)}
    check(path + '_one_primary_row_per_new_id', all(counts[v] == 1 for v in wanted), len(wanted))
    provenance = {k: [r for r in registry_rows[path] if re.match(re.escape(v) + r'\b',r[0]) and k in r[0]] for k,v in mapping.items() if k.startswith(prefixes)}
    check(path + '_provisional_alias_retained', all(len(r) == 1 for r in provenance.values()))
crosswalk = {r[0]:r for r in registry_rows['ID_CROSSWALK.md'] if r[0] in inventory}
check('crosswalk_all_208_rows', len(crosswalk) == 208)
check('crosswalk_no_duplicate_provisional_rows', len([r for r in registry_rows['ID_CROSSWALK.md'] if r[0] in inventory]) == 208)
check('crosswalk_correct_final_column', all(v in crosswalk[k][1] for k,v in {**mapping,**merged}.items()))
pd_paths = {r['id']:r['path'] for r in lat if r['id'].startswith('PD')} | pi_theory
idea_paths = {r['id']:r['path'] for r in lat if r['id'].startswith('IDEA')} | {f'IDEA?programme-ideas-claude-{i:02d}': TOPIC+'ideas/candidates.md' for i in range(1,21)}
for category, paths in [('PD',pd_paths),('IDEA',idea_paths)]:
    invalid = []
    for provisional, path in paths.items():
        content = read(path)
        heading = re.search(r'^#+ ' + re.escape(provisional) + r' [^\n]*\n\nFinal ID: \*\*' + re.escape(mapping[provisional]) + r'\*\*', content, re.M)
        if not heading or content.count('Final ID: **'+mapping[provisional]+'**') != 1:
            invalid.append(provisional)
    check(category+'_canonical_Final_ID_lines', not invalid, {'count':len(paths),'invalid':invalid})

# Verify allocation itself preserves complete canonical files after deleting only
# its explicitly inserted Final ID paragraph; this is stronger than status-only.
def strip_final(text):
    return re.sub(r'\nFinal ID: \*\*[^\n]+\n', '', text)

canonical = set(pd_paths.values()) | set(idea_paths.values())
changed = [p for p in sorted(canonical) if strip_final(read(p)) != read(p, ALLOC+'^')]
check('canonical_content_unchanged_by_allocation', not changed, {'files':len(canonical),'changed':changed})
baseline_changes = [p for p in sorted(pd_paths.values()) if strip_final(read(p)) != read(p,BASELINE)]
# This known prior audit-03 T3 proof clarification predates allocation and is
# reported, not silently treated as byte-preserved accepted mathematics.
check('baseline_difference_limited_to_preallocation_T01', baseline_changes == [TOPIC+'theory/programme-ideas-claude-01-finite-favard-pattern-pairs.md'], baseline_changes)
proof_before = {r[0]:r for r in rows(read('PROOF_STATUS.md', ALLOC+'^')) if r[0] in pd_paths}
proof_after = {k: next(r for r in registry_rows['PROOF_STATUS.md'] if r[0].startswith(v+' ')) for k,v in mapping.items() if k in pd_paths}
check('32_PD_epistemic_status_cells_unchanged', len(proof_before)==32 and all(proof_before[k][2] == proof_after[k][2] for k in pd_paths))
check('32_PD_part_status_tokens_unchanged', all(re.findall(r'\b(?:PROVED|PARTIAL|CONDITIONAL|MEASURED|OPEN|REJECTED)\b',proof_before[k][3]) == re.findall(r'\b(?:PROVED|PARTIAL|CONDITIONAL|MEASURED|OPEN|REJECTED)\b',proof_after[k][3]) for k in pd_paths))
baseline_rows = {r[0]:r for r in rows(read('PROOF_STATUS.md', BASELINE)) if r[0] in pd_paths}
check('32_PD_status_cells_unchanged_from_accepted_baseline', len(baseline_rows)==32 and all(baseline_rows[k][2] == proof_after[k][2] for k in pd_paths))
references = {**mapping,**merged,**json.loads(read('topics/bivariate-lanczos-20261031/pr-prep/id-map.json'))['map']}
reference_pattern = re.compile('|'.join(re.escape(old)+r'\b' for old in sorted(references,key=len,reverse=True)))
def normalize_references(text):
    text = reference_pattern.sub(lambda match: references[match.group()],text)
    text = text.replace('PD-T?…-301', references['PD-T?bivariate-lanczos-claude-301'])
    text = text.replace('PD-T?…-304', references['PD-T?bivariate-lanczos-claude-304'])
    return text.replace('PD-N?…-02',mapping['PD-N?programme-ideas-claude-02'])
for path,prefixes in [('PROOF_STATUS.md',('PD-T','PD-N')),('state/IDEAS.md',('IDEA',)),('literature/INDEX.md',('LIT',))]:
    oldrows = rows(read(path,ALLOC+'^'))
    mismatches = []
    for pid,final in mapping.items():
        if not pid.startswith(prefixes):
            continue
        before = next(r for r in oldrows if r[0].split(';')[0].strip()==pid)
        after = next(r for r in registry_rows[path] if re.match(re.escape(final)+r'\b',r[0]))
        if [normalize_references(cell) for cell in before[1:]] != after[1:]:
            mismatches.append(pid)
    check(path+'_all_non_ID_cells_preserved_modulo_final_references',not mismatches,mismatches)

ledger = read('topics/padua-batch-20261031/ALLOCATIONS.md')
for camp, namespaces in expected_ranges.items():
    for ns,(lo,hi) in namespaces.items():
        check('ledger_'+camp+'_'+ns, f'{fmt(ns,lo)}–{fmt(ns,hi)} ({hi-lo+1})' in ledger)
check('ledger_authorization_owner_exception_and_reservation', all(s in ledger for s in ['allocate this block now','are the lattice ids allocated now? if not, do that as well','owner change applies to these two members only','LIT-293–299 reservation is unchanged']))

# Actual default-only reruns in snapshots: no --apply, imports, source rewriting,
# optimized assertions, or monkey-patching. Snapshot preparation is audit data.
script_path = TOPIC+'pr-prep/allocate.py'
script = read(script_path)
input_paths = REGISTRIES + ['topics/lattice-unisolvence-20261031/provisional-id-map.json','topics/bivariate-lanczos-20261031/pr-prep/id-map.json',TOPIC+'lit/integration-map.json',TOPIC+'lit/integration-map-pr10.json',TOPIC+'lit/baseline.md'] + pi_theory_files
reruns = []
for revision in [SOURCE, ALLOC+'^']:
    with tempfile.TemporaryDirectory(prefix='allocation-audit-') as directory:
        tmp = Path(directory)
        for path in input_paths + [script_path]:
            dest = tmp/path
            dest.parent.mkdir(parents=True,exist_ok=True)
            dest.write_text(script if path == script_path else read(path,revision))
        before = {str(p.relative_to(tmp)):hashlib.sha256(p.read_bytes()).hexdigest() for p in tmp.rglob('*') if p.is_file()}
        result = subprocess.run([sys.executable,'-I',script_path],cwd=tmp,capture_output=True,text=True)
        after = {str(p.relative_to(tmp)):hashlib.sha256(p.read_bytes()).hexdigest() for p in tmp.rglob('*') if p.is_file()}
        reruns.append({'input_revision':revision,'script_revision':SOURCE,'argv':['python3','-I',script_path], 'returncode':result.returncode,'stdout':result.stdout,'stderr':result.stderr,'snapshot_bytes_unchanged':before==after})
        check('default_dryrun_no_writes_'+revision, before==after)
check('source_dryrun_expected_self_collision', reruns[0]['returncode']==1 and 'AssertionError:' in reruns[0]['stderr'] and all(v in reruns[0]['stderr'] for v in mapping.values()))
check('preallocation_dryrun_succeeds_and_matches_committed_ranges',reruns[1]['returncode']==0 and json.loads(reruns[1]['stdout']) == {'blocks':allocation['blocks'],'next':allocation['next_unreserved']})

print(json.dumps({'source':SOURCE,'main':MAIN,'accepted_scientific_baseline':BASELINE,'allocation_commit':ALLOC,'PR11':PR11,'python':sys.version,'checks':checks,'reruns':reruns,'source_sha256':manifest,'all_checks_pass':all(c['pass'] for c in checks)},indent=2,ensure_ascii=False))
sys.exit(0 if all(c['pass'] for c in checks) else 1)
