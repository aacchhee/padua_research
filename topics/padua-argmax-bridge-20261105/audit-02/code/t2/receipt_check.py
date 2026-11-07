import hashlib, importlib.util, json, sys, time, resource
from pathlib import Path
root = Path(sys.argv[1]); T = 'topics/padua-argmax-bridge-20261105/'
spec = importlib.util.spec_from_file_location('chk', root / T / 'code/final_hybrid_engine/checker.py')
C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
fz = (root / T / 'code/final_hybrid_engine/FREEZE.json').read_bytes()
fid = {'bytes': len(fz), 'sha256': hashlib.sha256(fz).hexdigest()}
def strict(b):
    def pairs(rows):
        out = {}
        for k, v in rows:
            assert k not in out; out[k] = v
        return out
    return json.loads(b, object_pairs_hook=pairs)
out = {}
for name in ['primary-41', 'fresh-41', 'primary-511', 'fresh-511']:
    b = (root / T / 'evidence/final-hybrid-validation' / (name + '.json')).read_bytes(); d = strict(b)
    t = time.process_time()
    v = C.verify_essential(d, d['freeze'])
    out[name] = {'bytes': len(b), 'lt16384': len(b) < 16384, 'freeze_match': d['freeze']['sha256'] == fid['sha256'] and d['freeze']['bytes'] == fid['bytes'],
                 'reconstructs': v == d['verification'], 'nodes': v['nodes'], 'S': v['S_premises'], 'method': v['norm_method'],
                 'leaf_counts': v['leaf_counts'], 'actual_rows': len(d['lambda_upper_rows']), 'cpu': round(time.process_time() - t, 4)}
p41 = strict((root / T / 'evidence/final-hybrid-validation/primary-41.json').read_bytes()); f41 = strict((root / T / 'evidence/final-hybrid-validation/fresh-41.json').read_bytes())
out['fresh41_same_tree_as_primary'] = p41['tree'] == f41['tree']
print(json.dumps(out, indent=1))
