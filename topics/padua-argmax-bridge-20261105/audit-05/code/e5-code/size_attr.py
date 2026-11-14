"""R13: full per-path generated-class accounting with the SAME classification as audit-02/code/t2/size.py
(read-only `git ls-tree -rl`). Usage (cwd = repository): python3 -I -B size_attr.py REPORT"""
import collections, json, subprocess, sys

SRC = ('.py', '.sh', '.c', '.cpp', '.h', '.tex', '.bib', '.diff')
TOPIC = 'topics/padua-argmax-bridge-20261105/'


def inv(ref, all_files=False):
    out = subprocess.check_output(['git', 'ls-tree', '-rl', ref], text=True)
    rows = {}
    for line in out.splitlines():
        meta, path = line.split('\t', 1)
        mode, typ, blob, size = meta.split()
        if typ != 'blob': continue
        if not all_files:
            base = path.rsplit('/', 1)[-1]
            if base == '.gitignore' or path.endswith(SRC): continue
            if path.endswith('.md') and base != 'COLD_STORAGE.md': continue
        rows[path] = (blob, int(size))
    return rows


def group(path):
    if path.startswith('topics/'): return '/'.join(path.split('/')[:2])
    return path.split('/')[0] if '/' in path else '(root)'


def delta(a, b):
    pos = collections.Counter(); items = []
    for p, (blob, s) in b.items():
        old = a.get(p)
        if old is None: pos[group(p)] += s; items.append((p, 'new', s))
        elif old[0] != blob and s > old[1]: pos[group(p)] += s - old[1]; items.append((p, 'grow', s - old[1]))
    return pos, items


refs = {'old_topic_head': '8a94ce610594e9f52a23ca6b74b5751719f0d89e', 'main': 'b5388c25a2a5ccb8d0faf816ab87023cf347bcd3',
        'merge': '941aa335e60ca7058c8a0113faa76e31217f4753', 'head': '33b9eca8167980cad0b0a491da7de64280c9a158'}
I = {k: inv(v) for k, v in refs.items()}
tot = {k: sum(s for _, s in v.values()) for k, v in I.items()}
by_group = {k: dict(collections.Counter({g: 0 for g in []})) for k in I}
for k, v in I.items():
    c = collections.Counter()
    for p, (_, s) in v.items(): c[group(p)] += s
    by_group[k] = dict(c.most_common())
merge_pos, merge_items = delta(I['old_topic_head'], I['merge'])
post_pos, post_items = delta(I['merge'], I['head'])
all_pos, all_items = delta(I['old_topic_head'], I['head'])
# Non-topic integrity: every file (all classes) outside this topic identical at head vs main?
A = inv(refs['main'], True); H = inv(refs['head'], True)
outside = lambda p: not p.startswith(TOPIC) and p != 'results/padua-argmax-bridge-20261105.md'
changed = sorted(p for p in A if outside(p) and (p not in H or H[p][0] != A[p][0]))
added = sorted(p for p in H if outside(p) and p not in A)
freeze_md = I['head'].get(TOPIC + 'code/post_audit_D09_threepoint/FREEZE.md')
out = {'refs': refs, 'generated_class_totals': tot,
       'topic_share_at_head': by_group['head'].get('topics/padua-argmax-bridge-20261105'),
       'padua3d_share_at_head': by_group['head'].get('topics/padua-3d-20261106'),
       'head_by_group_top12': dict(list(by_group['head'].items())[:12]),
       'merge_positive_by_group': dict(merge_pos), 'merge_positive_total': sum(merge_pos.values()),
       'merge_positive_paths': len(merge_items),
       'post_merge_positive_by_group': dict(post_pos), 'post_merge_items': post_items,
       'old_head_to_head_positive_total': sum(all_pos.values()), 'old_head_to_head_by_group': dict(all_pos),
       'bound_9917613_plus_positive': 9917613 + sum(all_pos.values()),
       'actual_plus_inherited_FREEZE_md_2087': tot['head'] + 2087,
       'FREEZE_md_counted_by_script': freeze_md is not None and False,
       'outside_topic_changed_or_removed_vs_main': changed, 'outside_topic_added_vs_main': added,
       'largest_merge_paths': sorted(merge_items, key=lambda r: -r[2])[:8]}
open(sys.argv[1], 'w').write(json.dumps(out, indent=1) + '\n')
print(json.dumps({k: out[k] for k in out if k not in ('post_merge_items', 'largest_merge_paths')}, indent=1)[:4000])
print(out['largest_merge_paths'])
