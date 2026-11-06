#!/usr/bin/env python3
"""Inventory committed topic code/receipts and their explicit external files.

Run after committing final inputs:
  python -B topics/<slug>/code/inventory_evidence.py --topic <slug>
Preview without changing topic manifests: add --output-dir /tmp/<slug>/inventory.
Only git ls-files entries also present at HEAD are read; working-tree edits and
uncommitted additions are ignored. Outputs describe local working artifacts,
never archival delivery. This program does not write COLD_STORAGE.md.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

LIMIT = 16 * 1024  # Every generated JSON file must be strictly smaller.
OMIT = {'elapsed_seconds', 'exact_gram_pairs_checked'}
PATH_KEYS = {'path', 'stdout', 'stderr', 'output', 'log', 'artifact',
             'raw_file', 'output_file', 'log_file', 'file_path'}
COMMAND_KEYS = {'command', 'argv', 'generating_command', 'compile_commands',
                'regeneration_command', 'checker_command'}
PROSE = {'.md', '.rst', '.adoc'}


def encoded(value):
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + '\n').encode()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args])


def pointer(base, key):
    return base + '/' + str(key).replace('~', '~0').replace('/', '~1')


def within(path, root):
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def receipt_paths(value, base='', command_ref=None, status=None):
    """Yield explicit path fields with nearest command/status JSON pointers."""
    if isinstance(value, dict):
        commands = [pointer(base, k) for k in value if k in COMMAND_KEYS]
        if commands:
            command_ref = commands
        if 'status' in value:
            status = value['status']
        for key, item in value.items():
            loc = pointer(base, key)
            if key in PATH_KEYS and isinstance(item, str) and item:
                declared = {k: value[k] for k in ('bytes', 'sha256') if k in value}
                yield item, loc, command_ref, status, declared
            elif isinstance(item, (dict, list)):
                yield from receipt_paths(item, loc, command_ref, status)
    elif isinstance(value, list):
        for n, item in enumerate(value):
            yield from receipt_paths(item, pointer(base, n), command_ref, status)


def inspect_raw(path, scientific):
    result = {'availability': 'unavailable'}
    try:
        if not path.is_file():
            result['reason'] = 'missing or not a regular file'
            return result
        before = path.stat()
        h = hashlib.sha256()
        with path.open('rb') as stream:
            for block in iter(lambda: stream.read(1024 * 1024), b''):
                h.update(block)
        result.update(availability='local-working', bytes=before.st_size,
                      sha256=h.hexdigest())
        if scientific and path.suffix == '.jsonl':
            digest = hashlib.sha256()
            count = 0
            try:
                with path.open('r', encoding='utf-8') as stream:
                    for line in stream:
                        if not line.strip():
                            continue
                        row = json.loads(line)
                        if not isinstance(row, dict) or not {'degree', 'Knode_squared', 'KHS_squared'} <= row.keys():
                            raise ValueError('row is not a native endpoint record')
                        for field in OMIT:
                            row.pop(field, None)
                        canonical = json.dumps(row, sort_keys=True, separators=(',', ':'), ensure_ascii=False)
                        digest.update((canonical + '\n').encode('utf-8'))
                        count += 1
                result['scientific_projection'] = {'method': 'native-jsonl-v1',
                    'sha256': digest.hexdigest(), 'rows': count}
            except (ValueError, UnicodeError) as exc:
                result['scientific_projection'] = {'status': 'unavailable', 'reason': str(exc)[:160]}
        after = path.stat()
        if (before.st_size, before.st_mtime_ns, before.st_ino) != (after.st_size, after.st_mtime_ns, after.st_ino):
            result['availability'] = 'unstable-during-read'
    except OSError as exc:
        result = {'availability': 'unavailable', 'reason': str(exc)}
    return result


def chunks(kind, items, out, head):
    """Separate records for bounded storage; never split a single record."""
    groups, current = [], []
    def compact(value):
        return (json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False) + '\n').encode()
    def envelope(entries):
        return {'schema': 'padua-inventory-chunk-v1', 'kind': kind,
                'source_head': head, 'entries': entries}
    for item in items:
        if len(compact(envelope(current + [item]))) >= LIMIT:
            if not current:
                raise ValueError(f'{kind}: single record exceeds 16KiB')
            groups.append(current)
            current = []
        if len(compact(envelope([item]))) >= LIMIT:
            raise ValueError(f'{kind}: single record exceeds 16KiB')
        current.append(item)
    if current:
        groups.append(current)
    indexes = []
    for n, group in enumerate(groups, 1):
        rel = f'inventory/{kind}-{n:03d}.json'
        data = compact(envelope(group))
        indexes.append({'path': rel, 'bytes': len(data), 'sha256': sha(data), 'records': len(group)})
        out[rel] = data
    return indexes


def build(repo, topic, external_roots, scientific):
    head = git(repo, 'rev-parse', 'HEAD').decode().strip()
    prefix = 'topics/' + topic + '/'
    listed = git(repo, 'ls-files', '-z', '--', prefix + 'code', prefix + 'evidence').decode().split('\0')
    code, receipts, raw, refs, review = [], [], {}, [], []
    for name in sorted(filter(None, listed)):
        is_code = name.startswith(prefix + 'code/')
        is_receipt = name.startswith(prefix + 'evidence/') and name.endswith('.json')
        if not (is_code or is_receipt):
            continue
        if Path(name).suffix.lower() in PROSE:
            review.append({'path': name, 'review_commit': head})
            continue
        # Newly staged/uncommitted files can occur in ls-files; require HEAD.
        found = subprocess.run(['git', '-C', str(repo), 'cat-file', '-e', head + ':' + name],
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if found.returncode:
            continue
        data = git(repo, 'show', head + ':' + name)
        blob = git(repo, 'rev-parse', head + ':' + name).decode().strip()
        ident = {'path': name, 'bytes': len(data), 'sha256': sha(data), 'git_blob': blob}
        if is_code:
            code.append(ident)
            continue
        try:
            doc = json.loads(data)
        except (ValueError, UnicodeError) as exc:
            ident['parse_error'] = str(exc)
            receipts.append(ident)
            continue
        ident['receipt_status'] = doc.get('status', 'not supplied') if isinstance(doc, dict) else 'not supplied'
        receipts.append(ident)
        for text, loc, commands, status, declared in receipt_paths(doc):
            candidate = Path(text)
            if not candidate.is_absolute():
                candidate = repo / candidate
            # Resolve explicit paths only; never recursively scan directories.
            candidate = candidate.resolve()
            if within(candidate, repo):
                continue
            if candidate.suffix.lower() in PROSE:
                review.append({'path': str(candidate), 'receipt': name,
                               'pointer': loc, 'review_commit': head})
                continue
            key = str(candidate)
            if key not in raw:
                if any(within(candidate, root) for root in external_roots):
                    info = inspect_raw(candidate, scientific)
                else:
                    info = {'availability': 'unavailable', 'reason': 'outside explicitly permitted external roots'}
                raw[key] = {'path': key, **info, 'references': []}
            info = raw[key]
            comparison = {}
            for field, expected in declared.items():
                if field in info:
                    comparison[field] = 'MATCH' if info[field] == expected else 'MISMATCH'
                else:
                    comparison[field] = 'unavailable'
            # Exact expected identities/commands remain in committed receipts.
            # Receipt basename resolves through the hashed receipt inventory.
            reference = {'receipt': Path(name).name, 'pointer': loc,
                         'receipt_status': status if status is not None else 'not supplied',
                         'command_pointers': commands or [],
                         'observed_vs_declared': comparison}
            raw[key]['references'].append(reference)
            refs.append(reference)
    out = {}
    code_index = chunks('code', code, out, head)
    receipt_index = chunks('receipts', receipts, out, head)
    raw_index = chunks('external-files', sorted(raw.values(), key=lambda r: r['path']), out, head)
    review_index = chunks('prose-review-paths', review, out, head)
    common = {'source_head': head, 'topic': topic, 'status': 'local-working; archival-pending',
              'input_policy': 'git ls-files intersect HEAD; bytes from committed HEAD, not working tree',
              'archive_delivery': 'not performed or asserted'}
    out['evidence-manifest.json'] = encoded({'schema': 'padua-evidence-manifest-v1', **common,
        'code': code_index, 'receipts': receipt_index, 'prose_review_only': review_index,
        'cold_storage_index': 'cold-storage.json',
        'receipt_identity_rule': 'External reference receipt basenames resolve under topics/<topic>/evidence/ to receipt inventory SHA256/git_blob at source_head. pointer identifies the path field; declared bytes/SHA256 are its dictionary siblings. command_pointers identify exact retained commands in that same committed receipt.',
        'counts': {'code': len(code), 'receipts': len(receipts)}})
    out['cold-storage.json'] = encoded({'schema': 'padua-local-artifact-inventory-v1', **common,
        'files': raw_index,
        'external_read_roots': [str(p) for p in external_roots],
        'scientific_projection_method': {'name': 'native-jsonl-v1', 'enabled': scientific,
            'description': 'Each nonblank native endpoint JSONL row parsed independently; omit only top-level elapsed_seconds and exact_gram_pairs_checked; sorted keys, compact separators, ensure_ascii=False, UTF-8 plus LF; SHA256 concatenation in original row order.',
            'does_not_establish': 'completion, correctness, equality of omitted guards, or archival delivery'},
        'regeneration': 'Resolve each file reference receipt through evidence-manifest.json receipt index; command_pointers retain exact generating commands. Empty command_pointers means no enclosing command supplied: consult the committed receipt. No command is executed by this inventory.',
        'retention_retrieval_notes': 'Coordinator supplies COLD_STORAGE.md; local paths are not an archive.',
        'counts': {'unique_external_paths': len(raw), 'references': len(refs),
            'unavailable_or_unstable': sum(r['availability'] != 'local-working' for r in raw.values())}})
    for name, data in out.items():
        if len(data) >= LIMIT:
            raise ValueError(f'{name} exceeds 16KiB; no outputs written')
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--topic', default='padua-lanczos-nonproduct-20261105', help='topic slug')
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument('--output-dir', type=Path, help='default: repository topic directory')
    parser.add_argument('--external-root', type=Path, action='append', help='permitted read root; repeat; default /tmp/<topic>')
    parser.add_argument('--no-scientific-digest', action='store_true')
    args = parser.parse_args()
    if not args.topic or '/' in args.topic or args.topic in {'.', '..'}:
        parser.error('--topic must be a single topic slug')
    repo = args.repo.resolve()
    roots = [p.resolve() for p in (args.external_root or [Path('/tmp') / args.topic])]
    # Do not accept roots which would allow broad environment/credential access.
    if any(p in {Path('/'), Path('/home'), Path('/root'), Path('/workspace'), Path('/tmp')} for p in roots):
        parser.error('--external-root must be a specific artifact directory')
    out = build(repo, args.topic, roots, not args.no_scientific_digest)
    destination = (args.output_dir or repo / 'topics' / args.topic).resolve()
    for name, data in out.items():
        target = destination / name
        target.parent.mkdir(parents=True, exist_ok=True)
        temporary = target.with_suffix(target.suffix + '.tmp')
        temporary.write_bytes(data)
        os.replace(temporary, target)
    print(json.dumps({'source_head': json.loads(out['evidence-manifest.json'])['source_head'],
                      'output_dir': str(destination), 'files_written': len(out),
                      'largest_json_bytes': max(map(len, out.values())),
                      'status': 'local-working; archival-pending'}))


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        sys.exit(str(exc))
