#!/usr/bin/env python3
"""Read-only protocol/artifact check; writes only its requested JSON receipt."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[5]
TOPIC = 'topics/padua-lanczos-drift-20261101'
SOURCE = 'b09e1dbe0baafd666cf0d779a671a40f55de2d75'
HEAD = '7a6dd1f7f8f10d0f9c2568e89d693b7d04cd571b'
MAIN = '28aaa20861d08074b77efc74eaef75cdcb36234d'
ORIGINAL_BASE = '806cc7b4509fd93bae652f9545d32d95529f8281'

def sha(data):
    return hashlib.sha256(data).hexdigest()

def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])

def blob(revision, path):
    return git('show', revision + ':' + path)

def read_json(path):
    return json.loads((ROOT / path).read_text())

def content_id(path):
    data = Path(path).read_bytes()
    return {'bytes': len(data), 'sha256': sha(data)}

def references(value, pointer=''):
    """Yield explicitly manifested path/size/hash triples, retaining repeats."""
    if isinstance(value, dict):
        if isinstance(value.get('path'), str) and 'sha256' in value:
            yield pointer, value['path'], value.get('bytes'), value['sha256']
        if isinstance(value.get('output_path'), str) and 'output_sha256' in value:
            yield pointer, value['output_path'], value.get('output_bytes'), value['output_sha256']
        for key, child in value.items():
            if isinstance(child, dict) and '/' in key and 'sha256' in child:
                yield pointer + '/' + key, key, child.get('bytes'), child['sha256']
            yield from references(child, pointer + '/' + key)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from references(child, pointer + '/' + str(index))

def check_ref(manifest, pointer, path, size, digest):
    full = Path(path) if path.startswith('/') else ROOT / path
    row = {'manifest': manifest, 'pointer': pointer, 'path': path,
           'expected_bytes': size, 'expected_sha256': digest, 'exists': full.is_file()}
    if full.is_file():
        row.update(content_id(full))
        row['pass'] = row['sha256'] == digest and (size is None or row['bytes'] == size)
    else:
        row['pass'] = False
    return row

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    record = {'scope': 'Original workspace artifact integrity and bounded protocol checks; no Windows delivery or mathematical rerun is asserted.',
              'rules_and_audited_head': HEAD, 'scientific_snapshot': SOURCE,
              'current_main': MAIN, 'python': __import__('sys').version,
              'script': content_id(__file__)}
    receipt = read_json(TOPIC + '/evidence/archive-receipt.json')
    archive = Path(receipt['archive_path'])
    archive_check = {'path': str(archive), **content_id(archive)}
    archive_check['identity_matches'] = archive_check['bytes'] == receipt['archive_bytes'] and archive_check['sha256'] == receipt['archive_sha256']
    final_files = {entry['path']: entry for entry in read_json(TOPIC + '/final-validation.json')['files']}
    all_source_paths = git('ls-tree', '-r', '--name-only', SOURCE).decode().splitlines()
    expected = {path for path in all_source_paths if path.startswith(TOPIC + '/')
                or path.startswith('tracks/bivariate-lanczos/code/drift/')
                or path.startswith('tracks/bivariate-lanczos/theory/drift-codex-')}
    original_rows = []
    with zipfile.ZipFile(archive) as zf:
        archive_check['crc_first_bad_entry'] = zf.testzip()
        archive_check['entry_count'] = len(zf.infolist())
        archive_check['unique_entry_count'] = len(set(zf.namelist()))
        archive_check['entry_set_matches_81_plus_snapshot'] = set(zf.namelist()) == expected | {'SNAPSHOT.txt'}
        archive_check['snapshot_text'] = zf.read('SNAPSHOT.txt').decode()
        for path in sorted(expected):
            entry = final_files.get(path)
            data, source = zf.read(path), blob(SOURCE, path)
            original_rows.append({'path': path, 'bytes': len(data), 'sha256': sha(data),
                                  'git_blob': git('rev-parse', SOURCE + ':' + path).decode().strip(),
                                  'matches_pinned_git_bytes': data == source,
                                  'matches_final_validation': None if entry is None else len(data) == entry['bytes'] and sha(data) == entry['sha256']})
    archive_check['all_81_equal_pinned_git'] = all(row['matches_pinned_git_bytes'] for row in original_rows)
    archive_check['final_validation_matches'] = sum(row['matches_final_validation'] is True for row in original_rows)
    archive_check['final_validation_only_paths'] = sorted(set(final_files) - expected)
    archive_check['source_only_paths'] = sorted(expected - set(final_files))
    archive_check['final_validation_changed_paths'] = [row['path'] for row in original_rows if row['matches_final_validation'] is False]
    archive_check['entries'] = original_rows
    record['archive'] = archive_check

    # Every original content-ID reference to run files, not merely the two
    # selected manifests behind audit-01's historical "46" label.
    run_refs = []
    source_paths = git('ls-tree', '-r', '--name-only', SOURCE, TOPIC).decode().splitlines()
    for path in source_paths:
        if path.endswith('.json'):
            obj = json.loads(blob(SOURCE, path))
            for pointer, target, size, digest in references(obj):
                if target.startswith('/workspace/padua-drift-runs/'):
                    run_refs.append(check_ref(path, pointer, target, size, digest))
    record['all_original_run_references'] = {'row_count': len(run_refs),
        'unique_path_count': len({row['path'] for row in run_refs}),
        'pass_count': sum(row['pass'] for row in run_refs),
        'missing': [row['path'] for row in run_refs if not row['exists']],
        'mismatches': [row for row in run_refs if row['exists'] and not row['pass']], 'rows': run_refs}
    selected = [TOPIC + '/evidence/e1-scalar-manifest.json', TOPIC + '/evidence/independent-scalar-01.json']
    selected_stats = []
    for manifest in selected:
        refs = list(references(read_json(manifest)))
        off = [row for row in refs if row[1].startswith('/workspace/padua-drift-runs/')]
        repo_inputs = [row for row in refs if row[1].startswith(str(ROOT) + '/')]
        selected_stats.append({'manifest': manifest, 'all_manifest_rows': len(refs),
           'off_repo_rows': len(off), 'off_repo_unique_paths': len({row[1] for row in off}),
           'absolute_repository_input_rows': len(repo_inputs)})
    record['historical_46_count_reconciliation'] = selected_stats
    selected_46 = []
    for manifest in selected:
        obj = read_json(manifest)
        refs = list(references(obj['working_artifacts'])) if manifest.endswith('e1-scalar-manifest.json') else list(references(obj))
        for pointer, path, size, digest in refs:
            row = check_ref(manifest, pointer, path, size, digest)
            if path.startswith(str(ROOT) + '/'):
                relative = str(Path(path).relative_to(ROOT))
                candidates = [SOURCE] + git('rev-list', SOURCE, '--', relative).decode().splitlines()
                for revision in dict.fromkeys(candidates):
                    data = blob(revision, relative)
                    if sha(data) == digest and (size is None or len(data) == size):
                        row['historical_git_commit'] = revision
                        row['historical_git_blob'] = git('rev-parse', revision + ':' + relative).decode().strip()
                        break
                row['historical_id_available'] = 'historical_git_commit' in row
            selected_46.append(row)
    record['selected_46_manifest_rows'] = {'rows': selected_46,
        'total_rows': len(selected_46),
        'current_file_matches': sum(row['pass'] for row in selected_46),
        'all_content_ids_available': all(row['pass'] or row.get('historical_id_available', False) for row in selected_46)}
    raw = Path('/workspace/padua-drift-runs/e1/cgs2-multinode-rotated-n12-bj.json')
    record['large_raw_capacity'] = {'path': str(raw), **content_id(raw),
        'expected_identity_pass': raw.stat().st_size == 3626111 and sha(raw.read_bytes()) == 'ffd035eef09d39be2ab862a6c12abbe58c455cd9131615ee89b4eefba14d1d8e',
        'in_archive': str(raw) in expected, 'in_git': False}
    record['root_independent_e6'] = check_ref(TOPIC + '/evidence/independent-e6-root.json', '',
        '/workspace/padua-drift-runs/root-independent-e6.json', 25154,
        '3cc34860ead3b2bc4d07441e9e10a8adc7e0acc0be1c643c6a9287e2a18056c4')
    response = read_json(TOPIC + '/evidence/response-01-manifest.json')
    record['response_manifest'] = [check_ref(TOPIC + '/evidence/response-01-manifest.json', '', path, item['bytes'], item['sha256'])
                                   for path, item in response['files'].items()]

    new_paths = git('diff', '--diff-filter=A', '--name-only', MAIN, HEAD).decode().splitlines()
    own = [path for path in new_paths if path.startswith(TOPIC + '/') or path.startswith('tracks/bivariate-lanczos/code/drift/') or path.startswith('tracks/bivariate-lanczos/theory/drift-codex-') or path == 'results/padua-lanczos-drift-20261101.md']
    sizes = [{'path': path, 'bytes': len(blob(HEAD, path))} for path in own]
    json_sizes = [row for row in sizes if row['path'].endswith('.json')]
    record['pinned_campaign_size'] = {'scope': 'All new own files relative to current main; excludes imported MZ/current-main files and raw off-repository artifacts. The all-file total conservatively bounds generated outputs.',
        'files': len(sizes), 'all_file_bytes': sum(row['bytes'] for row in sizes),
        'json_bytes': sum(row['bytes'] for row in json_sizes),
        'max_file': max(sizes, key=lambda row: row['bytes']),
        'all_under_1000000': all(row['bytes'] <= 1000000 for row in sizes),
        'all_files_total_under_5000000': sum(row['bytes'] for row in sizes) < 5000000,
        'unclassified_additions': sorted(set(new_paths) - set(own))}
    old_theory = git('ls-tree', '-r', '--name-only', ORIGINAL_BASE, 'tracks/bivariate-lanczos/theory').decode().splitlines()
    record['old_theory'] = {'count': len(old_theory),
        'changes_since_original_base': [path for path in old_theory if blob(ORIGINAL_BASE,path) != blob(HEAD,path)],
        'differences_from_current_main': [path for path in old_theory if blob(MAIN,path) != blob(HEAD,path)]}
    protected = ['.github', 'state', 'PROOF_STATUS.md', 'literature', 'PAPER_MAP.md', 'RESULTS.md', 'AGENTS.md', 'agents']
    record['protected_changes_from_current_main'] = git('diff', '--name-only', MAIN, HEAD, '--', *protected).decode().splitlines()
    record['reservation_only_diffs'] = {path: git('diff', '--unified=2', MAIN, HEAD, '--', path).decode()
        for path in ['ID_CROSSWALK.md', 'topics/padua-batch-20261031/ALLOCATIONS.md']}
    record['windows_delivery'] = {'status': 'PENDING', 'performed_by_this_checker': False,
        'historical_claude_receipt': 'LOG audit-01 delivery/readback is attributed historical evidence; this checker cannot verify AC Windows bytes.'}
    Path(args.output).write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps({key: record[key] for key in ['historical_46_count_reconciliation','large_raw_capacity','root_independent_e6','pinned_campaign_size','old_theory','protected_changes_from_current_main']}, indent=2))
    print('ZIP:', archive_check['identity_matches'], archive_check['entry_count'], archive_check['all_81_equal_pinned_git'], 'manifest matches', archive_check['final_validation_matches'])
    print('Run refs:', len(run_refs), 'unique', len({row['path'] for row in run_refs}), 'pass', sum(row['pass'] for row in run_refs))
    print('Response manifest:', sum(row['pass'] for row in record['response_manifest']), '/', len(record['response_manifest']))

if __name__ == '__main__':
    main()
