"""Verify the staged independent-U0 artifact identities and compact summary."""
import hashlib,json
from pathlib import Path
here=Path(__file__).resolve().parent
manifest=json.loads((here/'evidence-manifest.json').read_text())
summary=json.loads((here/'check-summary.json').read_text())
for entry in manifest['cold_artifacts']+[summary['independent_checker'],summary['output']]:
    p=Path(entry['path']);data=p.read_bytes()
    assert len(data)==entry['bytes'] and hashlib.sha256(data).hexdigest()==entry['sha256'],str(p)
for entry in manifest['source_inputs']:
    for key in ['source','copy','committed_copy']:
        p=Path(entry[key]);assert hashlib.sha256(p.read_bytes()).hexdigest()==entry['sha256'],str(p)
assert len(manifest['source_child_statuses'])==6
assert all(r['exit_code']==0 for r in manifest['source_child_statuses'])
assert manifest['driver_status']['exit_code']==0
assert summary['determinant_cases']==112
assert [(r['dimension'],r['minimum_distance'],r['projective_messages']) for r in summary['code_results']]==[(3,7,57),(6,4,19608)]
assert len(summary['producer_checker_replay']['rows'])==10
print(json.dumps({'result':'PASS','cold_artifacts_verified':len(manifest['cold_artifacts']),'source_files_checked_at_three_paths':len(manifest['source_inputs']),'determinant_cases':112,'q7_projective_messages':[57,19608],'all_six_child_statuses':0}))
