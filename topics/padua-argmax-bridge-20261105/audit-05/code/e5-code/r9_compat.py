"""R9 data-only compatibility probe: repaired reader's strict() and check_members allowlist vs authentic
engine/compact records of the OLD return (same frozen engine). Usage: python3 -I -B r9_compat.py TREE RETURN REPORT"""
import collections, json, sys, tarfile
from pathlib import Path

tree, ret, report = Path(sys.argv[1]), sys.argv[2], sys.argv[3]
sys.path.insert(0, str(tree / 'topics/padua-argmax-bridge-20261105/code/local_onset512_campaign'))
import return_bundle as B  # trusted repository copy

payload = {}
with tarfile.open(ret, 'r|gz') as t:
    for m in t:
        if m.isfile() and m.name.endswith('.json'):
            payload[m.name] = t.extractfile(m).read()
rejected = collections.defaultdict(list); parsed = 0
for name, data in sorted(payload.items()):
    try:
        B.strict(data); parsed += 1
    except Exception as e:  # record, never raise
        rejected[type(e).__name__ + ': ' + str(e)].append(name)
# Which keys of interest occur with which value types (all JSON members)?
types = collections.defaultdict(collections.Counter)
KEYS = {'bytes', 'n', 'observed_returncode', 'hard_aggregate_cap', 'ECHILD', 'quiescent', 'complete', 'terminal',
        'no_live_children', 'input_head_equal', 'timeout', 'failed', 'total_CPU_through_summary', 'waited_child_CPU',
        'absolute_self_CPU_hard'}
def walk(v):
    if isinstance(v, dict):
        for k, c in v.items():
            if k in KEYS: types[k][type(c).__name__] += 1
            walk(c)
    elif isinstance(v, list):
        for c in v: walk(c)
for data in payload.values():
    walk(json.loads(data))
out = {'json_members': len(payload), 'strict_accepted': parsed,
       'strict_rejections': {k: {'count': len(v), 'examples': v[:4]} for k, v in rejected.items()},
       'key_value_types': {k: dict(v) for k, v in types.items()}}
Path(report).write_text(json.dumps(out, indent=1) + '\n')
print(json.dumps(out)[:3000])
