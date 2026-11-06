#!/usr/bin/env python3
"""Inventory code/JSON/SVG identities and run inexpensive integration checks.

No numerical producer is imported or executed. Prose is never hash-pinned.
Paths in the manifest are relative to the topic directory.
"""
import argparse
import ast
from fnmatch import fnmatchcase
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

TOPIC = Path(__file__).resolve().parents[1]
ROOT = TOPIC.parents[1]
TARGET = TOPIC / 'evidence-manifest.json'
LIMIT = 16 * 1024
SOURCE_HEAD = '2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861'


def inventory(excluded, provisional):
    candidates = set((TOPIC / 'code').rglob('*.py'))
    candidates.update(TOPIC.rglob('*.json'))
    candidates.update((TOPIC / 'figures').glob('*.svg'))
    candidates.discard(TARGET)
    rows = []
    for path in sorted(candidates):
        name = path.relative_to(TOPIC).as_posix()
        if name in excluded or '__pycache__' in path.parts or any(fnmatchcase(part, 'audit-*-support') for part in path.parts):
            continue
        payload = path.read_bytes()
        if path.suffix in {'.json', '.svg'} and len(payload) >= LIMIT:
            raise ValueError(f'generated evidence must be below 16 KiB: {name}')
        rows.append([name, len(payload), hashlib.sha256(payload).hexdigest()])
    return {
        'format': 'padua-sharp-code-json-inventory-v1',
        'source_head': SOURCE_HEAD,
        'path_base': TOPIC.relative_to(ROOT).as_posix(),
        'status': 'PROVISIONAL' if provisional else 'FINAL snapshot',
        'columns': ['path_relative_to_base', 'bytes', 'sha256'],
        'files': rows,
        'dynamic_excluded_paths': sorted(excluded),
        'scope': 'All topic code/**/*.py, topic/**/*.json and figures/*.svg, except this manifest, '
                 '__pycache__, audit-*-support/ path components, and explicit dynamic exclusions. Prose is not pinned. '
                 'External source files, large raw artifacts and cold-storage payloads '
                 'are outside this inventory; JSON inventories record their provenance.',
    }


def markdown_without_code_or_math(source):
    lines = []
    fence = None
    for line in source.splitlines():
        match = re.match(r'^\s*(`{3,}|~{3,})', line)
        if match:
            marker = match.group(1)
            if fence is None:
                fence = marker[0]
            elif marker[0] == fence:
                fence = None
            lines.append('')
        elif fence is None and not re.match(r'^(?: {4}|\t)', line):
            lines.append(line)
        else:
            lines.append('')
    clean = '\n'.join(lines)
    clean = re.sub(r'\$\$.*?\$\$|\\\[.*?\\\]', '', clean, flags=re.S)
    clean = re.sub(r'(?<!\\)\$[^\n$]*?(?<!\\)\$|\\\(.*?\\\)', '', clean, flags=re.S)
    clean = re.sub(r'(`+).*?\1', '', clean)
    return clean


def check_links():
    documents = sorted(TOPIC.rglob('*.md'))
    documents.append(ROOT / 'results' / (TOPIC.name + '.md'))
    missing = []
    checked = 0
    for document in documents:
        if not document.is_file():
            missing.append(f'{document.relative_to(ROOT)}: document missing')
            continue
        clean = markdown_without_code_or_math(document.read_text())
        # Inline Markdown destinations, including angle-bracket destinations and
        # optional titles; plus reference-link definitions. This checks files,
        # not section anchors, remote URLs, or plain code-formatted path mentions.
        destinations = re.findall(r'!?\[[^\]\n]*\]\(\s*(<[^>\n]*>|[^\s)]+)(?:\s+[^)]*)?\)', clean)
        destinations += re.findall(r'^\s{0,3}\[[^\]\n]+\]:\s*(<[^>\n]*>|\S+)', clean, re.M)
        for raw in destinations:
            target = raw.strip('<>')
            if not target or target.startswith('#') or urlsplit(target).scheme:
                continue
            local = unquote(target.split('#', 1)[0].split('?', 1)[0])
            if not local:
                continue
            checked += 1
            path = document.parent / local
            if not path.exists():
                missing.append(f'{document.relative_to(ROOT)} -> {target}')
    print(f'Markdown: {len(documents)} documents, {checked} local file links, {len(missing)} missing targets')
    for issue in missing:
        print('MISSING ' + issue)
    return not missing


def integration_checks():
    failures = []
    scripts = sorted((TOPIC / 'code').rglob('*.py'))
    for script in scripts:
        try:
            ast.parse(script.read_text(), filename=str(script))
        except (SyntaxError, UnicodeError) as error:
            failures.append(f'{script.relative_to(TOPIC)}: {error}')
    receipts = sorted(TOPIC.rglob('*.json'))
    for receipt in receipts:
        try:
            json.loads(receipt.read_text())
        except (ValueError, UnicodeError) as error:
            failures.append(f'{receipt.relative_to(TOPIC)}: {error}')
        if receipt.stat().st_size >= LIMIT:
            failures.append(f'{receipt.relative_to(TOPIC)}: at least 16 KiB')
    total_json_bytes = sum(path.stat().st_size for path in receipts)
    largest = max(receipts, key=lambda path: path.stat().st_size)
    print(f'Python AST: {len(scripts)} files; JSON parse/size: {len(receipts)} files')
    print(f'Topic JSON total: {total_json_bytes} bytes including manifest; largest: '
          f'{largest.relative_to(TOPIC)} ({largest.stat().st_size} bytes)')
    for issue in failures:
        print('INVALID ' + issue)
    links_ok = check_links()
    return not failures and links_ok


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true', help='regenerate manifest before verification')
    parser.add_argument('--provisional', action='store_true', help='label generated snapshot provisional')
    parser.add_argument('--exclude', action='append', default=[], help='explicit mutable topic-relative path')
    parser.add_argument('--checks', action='store_true', help='run AST, JSON and local Markdown link checks')
    args = parser.parse_args()
    if (args.exclude or args.provisional) and not args.write:
        parser.error('--exclude and --provisional require --write')
    for name in args.exclude:
        path = Path(name)
        if path.is_absolute() or '..' in path.parts:
            parser.error('exclusions must stay within the topic')
    if args.write:
        payload = json.dumps(inventory(set(args.exclude), args.provisional),
                             separators=(',', ':'), ensure_ascii=True) + '\n'
        if len(payload.encode()) >= LIMIT:
            raise ValueError('manifest would exceed the 16 KiB limit; do not split it')
        TARGET.write_text(payload)
    recorded = json.loads(TARGET.read_text())
    current = inventory(set(recorded['dynamic_excluded_paths']),
                        recorded['status'] == 'PROVISIONAL')
    if recorded != current:
        raise ValueError('manifest mismatch: file content, scope or membership changed; regenerate intentionally')
    print(f"Manifest verified: {len(recorded['files'])} file identities, "
          f"{TARGET.stat().st_size} bytes, status={recorded['status']}")
    if args.checks and not integration_checks():
        raise SystemExit(1)


if __name__ == '__main__':
    main()
