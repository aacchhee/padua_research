"""Audit-06 budget accounting (own implementation of the audit-02 size.py classification; read-only git ls-tree).
Usage: python3 -I -B size6.py REPO REPORT
Counted: every blob except suffixes .py .sh .c .cpp .h .tex .bib .diff, basename .gitignore, and .md other than COLD_STORAGE.md.
Topic convention adds topics/padua-argmax-bridge-20261105/code/post_audit_D09_threepoint/FREEZE.md (2,087 B)."""
import json, subprocess, sys
from collections import Counter

repo, report = sys.argv[1], sys.argv[2]
SRC = ('.py', '.sh', '.c', '.cpp', '.h', '.tex', '.bib', '.diff')
TOPIC = 'topics/padua-argmax-bridge-20261105/'
EXC = TOPIC + 'code/post_audit_D09_threepoint/FREEZE.md'
REFS = {'main': 'b5388c25a2a5ccb8d0faf816ab87023cf347bcd3', 'head': '5b1a4942af498e60e9da4c8860c57cb4f67be4ef',
        'audit05_input': '33b9eca8167980cad0b0a491da7de64280c9a158', 'pre_merge_topic': '8a94ce6',
        'response05_input': '520b3645a4b8a584cb17eddc64defb97747cb253'}


def tree(ref):
    out = subprocess.run(['git', '-C', repo, 'ls-tree', '-r', '-l', '--full-tree', ref], check=True, capture_output=True, text=True).stdout
    rows = {}
    for line in out.splitlines():
        meta, path = line.split('\t', 1)
        mode, typ, blob, size = meta.split()
        if typ == 'blob': rows[path] = (blob, int(size))
    return rows


def counted(path):
    base = path.rsplit('/', 1)[-1]
    if base == '.gitignore' or path.endswith(SRC): return False
    if path.endswith('.md') and base != 'COLD_STORAGE.md': return False
    return True


T = {k: tree(v) for k, v in REFS.items()}
C = {k: {p: r for p, r in t.items() if counted(p)} for k, t in T.items()}
tot = {k: sum(s for _, s in c.values()) for k, c in C.items()}
head, main = C['head'], C['main']
topic_share = sum(s for p, (_, s) in head.items() if p.startswith(TOPIC))
non_topic_head = {p: r for p, r in T['head'].items() if not p.startswith(TOPIC)}
non_topic_main = {p: r for p, r in T['main'].items() if not p.startswith(TOPIC)}
diff_outside = sorted(p for p in set(non_topic_head) | set(non_topic_main) if non_topic_head.get(p) != non_topic_main.get(p))
topic_in_main = sorted(p for p in T['main'] if p.startswith(TOPIC))


def positive(a, b):
    pos = 0; items = []
    for p, (blob, s) in C[b].items():
        old = C[a].get(p)
        if old is None: pos += s; items.append((s, 'new', p))
        elif old[0] != blob and s > old[1]: pos += s - old[1]; items.append((s - old[1], 'grow', p))
    shrink = [(C[a][p][1] - s, p) for p, (blob, s) in C[b].items() if p in C[a] and C[a][p][0] != blob and s < C[a][p][1]]
    removed = [(C[a][p][1], p) for p in C[a] if p not in C[b]]
    return pos, sorted(items, reverse=True), shrink, removed


pos_pre, _, _, _ = positive('pre_merge_topic', 'head')
pos_pre_a5, _, _, _ = positive('pre_merge_topic', 'audit05_input')
pos_a5, items_a5, shrink_a5, removed_a5 = positive('audit05_input', 'head')
pos_r5, items_r5, shrink_r5, removed_r5 = positive('response05_input', 'head')
exc = T['head'].get(EXC)
big = sorted(((s, p) for p, (_, s) in head.items() if p.startswith(TOPIC) and s > 16384), reverse=True)
out = {
    'totals': tot, 'head_minus_main': tot['head'] - tot['main'], 'topic_counted_share_at_head': topic_share,
    'FREEZE_md_exception': exc[1] if exc else None, 'head_plus_exception': tot['head'] + (exc[1] if exc else 0),
    'positive_deltas_8a94ce6_to_head': pos_pre, 'positive_deltas_8a94ce6_to_33b9eca': pos_pre_a5, 'no_shrink_bound_9917613_plus': 9917613 + pos_pre,
    'audit05_input_to_head': {'net': tot['head'] - tot['audit05_input'], 'positive': pos_a5, 'items': items_a5,
                              'shrinks': shrink_a5, 'removed': removed_a5},
    'response05_input_to_head': {'net': tot['head'] - tot['response05_input'], 'positive': pos_r5, 'items': items_r5,
                                 'shrinks': shrink_r5, 'removed': removed_r5},
    'paths_outside_topic_differing_head_vs_main': diff_outside, 'topic_paths_in_main': len(topic_in_main),
    'counted_paths': {k: len(c) for k, c in C.items()},
    'topic_counted_files_over_16KiB_at_head': {'count': len(big), 'top': big[:8]},
    'classes_head_topic': dict(Counter(p.rsplit('.', 1)[-1] if '.' in p.rsplit('/', 1)[-1] else '(none)'
                                       for p in head if p.startswith(TOPIC)).most_common(10)),
}
open(report, 'x').write(json.dumps(out, indent=1) + '\n')
for k in ('totals', 'head_minus_main', 'topic_counted_share_at_head', 'FREEZE_md_exception', 'head_plus_exception',
          'positive_deltas_8a94ce6_to_head', 'positive_deltas_8a94ce6_to_33b9eca', 'no_shrink_bound_9917613_plus', 'paths_outside_topic_differing_head_vs_main',
          'topic_paths_in_main', 'counted_paths', 'topic_counted_files_over_16KiB_at_head'):
    print(k, out[k])
print('audit05_input->head', {k: out['audit05_input_to_head'][k] for k in ('net', 'positive', 'items', 'shrinks', 'removed')})
print('response05_input->head', {k: out['response05_input_to_head'][k] for k in ('net', 'positive', 'shrinks', 'removed')})
