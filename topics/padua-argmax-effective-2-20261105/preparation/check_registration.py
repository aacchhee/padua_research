#!/usr/bin/env python3
"""Independent byte-preservation/registration check; no Git mutations.
Recreate baseline with git archive 5821c3f... into an empty directory first.
"""
import argparse, hashlib, json, re
from pathlib import Path
BASE_SHA = '5821c3f130ec0b1e33ad1d01620b67620e1f0be1'
SLUG = 'padua-argmax-effective-2-20261105'
TOPIC = 'topics/' + SLUG
MAPPING = {'phase-structure.md': 'PD-T364', 'profile-boundary-cotangent.md': 'PD-T365', 'defect-radius-extension.md': 'PD-T366', 'corner-weighted-energy.md': 'PD-T367', 'corner-global-norm-ratio.md': 'PD-T368', 'corner-n2-local-radius.md': 'PD-T369', 'phase2-measurements.md': 'PD-T370', 'profile-leading-only-obstruction.md': 'PD-N132'}
def digest(b): return hashlib.sha256(b).hexdigest()
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--baseline', type=Path, required=True)
    ap.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[3])
    ap.add_argument('--output', type=Path)
    args = ap.parse_args()
    root, base = args.root, args.baseline
    checks, errors, proofs = {}, [], {}
    def check(name, ok):
        checks[name] = bool(ok)
        if not ok: errors.append(name)
    def read(path, old=False): return ((base if old else root) / path).read_bytes()
    # Exact bodies are protected, including old identity/status prose; metadata is append-only.
    for filename, final_id in MAPPING.items():
        rel = TOPIC + '/theory/' + filename
        old, new = read(rel), read(rel).split(b'\n', 1)[1]
        body = read(rel, True).split(b'\n', 1)[1]
        check('theory_body_prefix:' + filename, new.startswith(body))
        check('theory_heading:' + filename, old.split(b'\n')[0].startswith(('# ' + final_id + ' ').encode()))
        tail = new[len(body):] if new.startswith(body) else b''
        check('registration_metadata:' + filename, bool(tail) and b'registration' in tail.lower())
        proofs[filename] = {'preserved_body_sha256': digest(body), 'registered_file_sha256': digest(old)}
    mutable = {'topics/README.md','PROOF_STATUS.md','state/IDEAS.md','state/CURRENT.md','PAPER_MAP.md','ID_CROSSWALK.md','RESULTS.md','topics/padua-batch-20261031/ALLOCATIONS.md','results/' + SLUG + '.md'}
    mutable |= {TOPIC + '/' + p for p in ('LOG.md','ALLOCATIONS.md','COLD_STORAGE.md','cold-storage.json','evidence-manifest.json','report.md','ideas/H1.md','ideas/H2-H3.md')}
    mutable |= {TOPIC + '/theory/' + f for f in MAPPING}
    for name in ('H1.md','H2-H3.md'):
        rel = TOPIC + '/ideas/' + name
        old, new = read(rel,True), read(rel)
        normalized = re.sub(rb'(?m)^(#{1,2}) IDEA-\d{3} \((IDEA\?argmax-effective-2-codex-\d{2})\)', rb'\1 \2', new)
        check('IDEA_body_prefix:' + name, normalized.startswith(old))
    before_index, after_index = read('topics/README.md',True), read('topics/README.md')
    old_index_lines = [s for s in before_index.splitlines() if SLUG.encode() not in s]
    new_index_lines = [s for s in after_index.splitlines() if SLUG.encode() not in s]
    check('unrelated_topic_index_lines', after_index.startswith(before_index))
    # Handoff transition is orchestrator-owned and separately checked at publication.
    immutable_count = 0
    for path in base.rglob('*'):
        if not path.is_file(): continue
        rel = path.relative_to(base).as_posix()
        if rel in mutable or rel.startswith(TOPIC + '/handoffs/'): continue
        check('immutable:' + rel, (root / rel).exists() and read(rel) == path.read_bytes())
        immutable_count += 1
    def rows(data, pattern):
        out = {}
        for line in data.decode().splitlines():
            match = re.match(pattern, line)
            if match:
                out.setdefault(match[1], []).append(line)
        return out
    pattern = r'^\|\s*(PD-[TN]\d{3})\b'
    oldrows, newrows = rows(read('PROOF_STATUS.md', True), pattern), rows(read('PROOF_STATUS.md'), pattern)
    check('exact_added_PD_ids', set(newrows) - set(oldrows) == set(MAPPING.values()))
    for rid, row in oldrows.items():
        if rid != 'PD-T099': check('preserved_row:' + rid, newrows.get(rid) == row)
        else:
            current = newrows.get(rid, [''])[0]
            oldcells, newcells = row[0].split('|'), current.split('|')
            changed = [i for i in range(min(len(oldcells),len(newcells))) if oldcells[i] != newcells[i]]
            check('PD-T099_evidence_append_only', len(oldcells)==len(newcells) and len(changed)==1 and newcells[changed[0]].strip().startswith(oldcells[changed[0]].strip()))
            check('PD-T099_OPEN_range', 'OPEN' in current and ('2–32' in current or '2–n=32' in current or '2–32' in current.replace('n=', '')))
    for rid in MAPPING.values():
        entries = newrows.get(rid, [])
        check('unique_new_id:' + rid, len(entries) == 1)
        row = entries[0] if entries else ''
        check('status:' + rid, bool(re.search(r'\|\s*' + ('MEASURED' if rid=='PD-T370' else 'PROVED') + r'\s*\|', row)))
    idea_pattern = r'^\|\s*(IDEA-\d{3})\b'
    oi, ni = rows(read('state/IDEAS.md', True), idea_pattern), rows(read('state/IDEAS.md'), idea_pattern)
    check('exact_added_IDEAs', set(ni)-set(oi)=={f'IDEA-{i}' for i in range(454,462)})
    check('unique_new_IDEAs', all(len(ni.get(f'IDEA-{i}', [])) == 1 for i in range(454,462)))
    check('all_old_IDEA_rows', all(ni.get(k)==v for k,v in oi.items()))
    check('IDEAS_append_only', read('state/IDEAS.md').startswith(read('state/IDEAS.md', True)))
    check('LIT_registry_unchanged', read('literature/INDEX.md')==read('literature/INDEX.md',True))
    check('T02_unchanged', read(TOPIC+'/theory/localization-diagnosis.md')==read(TOPIC+'/theory/localization-diagnosis.md',True))
    def sections(data):
        return {part.split('\n',1)[0]:part for part in re.split(r'(?m)(?=^## )',data.decode()) if part}
    os, ns = sections(read('RESULTS.md',True)), sections(read('RESULTS.md'))
    check('unrelated_RESULTS_sections', all(ns.get(k,'').rstrip()==v.rstrip() for k,v in os.items() if SLUG not in k))
    old_report, new_report = sections(read(TOPIC+'/report.md',True)), sections(read(TOPIC+'/report.md'))
    excluded_report = ('# ', '## Protocol and storage limits', '## 2026-11-05 response record and reproduction corrections')
    check('report_scientific_sections', all(new_report.get(k,'').rstrip()==v.rstrip() for k,v in old_report.items() if not k.startswith(excluded_report)))
    check('own_RESULTS_section_present', any(SLUG in k for k in ns))
    canonical = read('results/'+SLUG+'.md').decode().replace('../topics/', 'topics/').strip()
    own_sections = [v.strip() for k,v in ns.items() if SLUG in k]
    check('canonical_RESULTS_copy', own_sections == [canonical])
    for rel in ('ID_CROSSWALK.md','topics/padua-batch-20261031/ALLOCATIONS.md',TOPIC+'/ALLOCATIONS.md'):
        check('append_only:' + rel, read(rel).startswith(read(rel, True)))
    mapping = json.loads(read(TOPIC+'/preparation/final-id-map.json'))
    check('mapping_exact_records', {Path(r['path']).name:r['final'] for r in mapping['records']} == MAPPING)
    check('mapping_exact_IDEAs', {r['provisional']:r['final'] for r in mapping['ideas']} == {f'IDEA?argmax-effective-2-codex-{i:02}':f'IDEA-{453+i}' for i in range(1,9)})
    check('mapping_counts', mapping['counts'] == {'PD-T':7,'PD-N':1,'IDEA':8,'LIT':0})
    check('permanent_gaps', mapping['unused_permanent_gaps'] == {'PD-T':'PD-T371–PD-T375','PD-N':'PD-N133–PD-N137','IDEA':'IDEA-462–IDEA-465','LIT':'LIT-594–LIT-597'})
    crosswalk = read('ID_CROSSWALK.md').decode()
    check('crosswalk_complete_mapping', all(f"| {r['provisional']} | {r['final']} |" in crosswalk for r in mapping['records']+mapping['ideas']))
    receipt = {'baseline':BASE_SHA,'result':'FAIL' if errors else 'PASS','scope':'mechanical registration and baseline preservation; no scientific rerun or Claude approval','checks_count':len(checks),'immutable_files_checked':immutable_count,'failed_checks':errors,'proof_body_hashes':proofs,'checked_shared_sha256':{p:digest(read(p)) for p in sorted(mutable) if (root/p).is_file() and '/theory/' not in p and not p.endswith('evidence-manifest.json')}}
    target = args.output or root / TOPIC / 'preparation/registration-check.json'
    target.write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({'result':receipt['result'],'checks':len(checks),'failures':errors},indent=2))
    raise SystemExit(bool(errors))
if __name__ == '__main__': main()
