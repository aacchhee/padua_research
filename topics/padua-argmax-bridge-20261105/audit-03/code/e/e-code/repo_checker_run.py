"""Run the repository's frozen checker (from the copy tree) on committed receipts.
Expected source identity is computed from the copy tree's FREEZE.json, NOT taken
from the receipt itself (verify_compact passes the receipt's own freeze field)."""
import hashlib, importlib.util, json, sys
from pathlib import Path

tree = Path(sys.argv[1]).resolve()
T = tree / 'topics/padua-argmax-bridge-20261105'
eng = T / 'code/final_hybrid_engine'
spec = importlib.util.spec_from_file_location('repo_checker', eng / 'checker.py')
C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
fz = (eng / 'FREEZE.json').read_bytes()
fsha = hashlib.sha256(fz).hexdigest()
assert fsha == '0d9ce0a5dbb7fb37cf1a05f07040b72d046b61b8d36b6a5a8bf137eb7d9914eb', fsha
expected = {'sha256': fsha, 'bytes': len(fz)}

files = sys.argv[2:]
out = []
for f in files:
    p = T / f
    data = p.read_bytes(); doc = json.loads(data)
    row = {'file': f, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(), 'n': doc['n']}
    try:
        v = C.verify_essential(doc, expected)
        row['reconstructs_recorded_verification'] = (v == doc['verification'])
        row['nodes'] = v['nodes']; row['leaves'] = v['leaves']; row['S'] = v['S_premises']
        row['method'] = v['norm_method']; row['M'] = v['M']; row['counts'] = v['leaf_counts']
        row['freeze_in_receipt_matches_tree'] = doc['freeze']['sha256'] == fsha and doc['freeze']['bytes'] == len(fz)
    except Exception as e:
        row['error'] = repr(e)
    out.append(row)
print(json.dumps(out, indent=1))
