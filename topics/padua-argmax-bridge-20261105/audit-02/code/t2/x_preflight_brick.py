"""NO_SCIENCE: a recoverable preflight precondition failure, then retry via supported paths."""
import importlib, json, os, sys
from pathlib import Path
TREE = Path(sys.argv[1]).resolve(); OUT = Path(sys.argv[2]).resolve(); T = 'topics/padua-argmax-bridge-20261105'
sys.path.insert(0, str(TREE / T / 'code/final_pack_ops_review')); rc3 = importlib.import_module('review_controls_03')
OUT.mkdir(parents=True, exist_ok=False); path = OUT / 'pkg'; m = rc3.package(path, TREE / T / 'syvert2_pack')
server, evidence, verify, common = rc3.load_ops(path)
p = dict(server.plan('all'), degrees=[41]); server.plan = lambda group: p; rc3.put(path / 'plan.json', {'all': p})
def disk_floor(*a): raise ValueError('prospective scratch+collection free-space floor not met')
server.inspect = disk_floor
res = {}
for label, resume in [('first', False), ('fresh_again', False), ('resume', True)]:
    try: server.run('all', 1, resume); res[label] = 'ran'
    except BaseException as e: res[label] = 'refused ' + repr(e)[:110]
server.inspect = rc3.fake_inspect   # precondition now satisfied
for label, resume in [('fresh_after_fix', False), ('resume_after_fix', True)]:
    try: server.run('all', 1, resume); res[label] = 'ran'
    except BaseException as e: res[label] = 'refused ' + repr(e)[:110]
s = json.loads((path / 'outputs/all/summary.json').read_bytes()); res['summary'] = [s['quiescent'], s['ECHILD'], s['first_failure']]
res['run_json_provenance'] = json.loads((path / 'outputs/all/run.json').read_bytes())['provenance']
print(json.dumps(res, indent=1))
