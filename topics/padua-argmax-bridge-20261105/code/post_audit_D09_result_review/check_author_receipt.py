"""Pure post-publication receipt consistency; no numerical/native execution."""
import hashlib,json,pathlib,resource,time
resource.setrlimit(resource.RLIMIT_CPU,(1,1))
HERE=pathlib.Path(__file__).resolve().parent;ROOT=HERE.parents[3]
RAW=ROOT/'local-output/argmax-bridge-20261105/post-audit-D09/result-review'
AUTHOR=RAW.parent/'threepoint'
def identity(p):
    p=pathlib.Path(p).resolve();b=p.read_bytes()
    return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def verify(row):assert identity(row['path'])==row,row['path']
receipt_path=ROOT/'topics/padua-argmax-bridge-20261105/evidence/d09-threepoint.json'
r=json.loads(receipt_path.read_text());baseline=json.loads((AUTHOR/'checkpoint.json').read_text())
ours=json.loads((RAW/'worker-result.json').read_text())
for key in ('freeze','sources','controller','postprocessor','binary'):verify(r[key])
for row in r['raw_files']:verify(row)
assert r['corner']==baseline['corner']==ours['completed'][1]['result']
assert r['control']==baseline['control']==ours['completed'][0]['result']
assert r['rectangles']==baseline['rectangles']
assert r['rectangles']['primary']['criterion']==ours['criterion']
assert r['completed_calls']==[dict(label=c['label'],CPU_seconds=c['cpu_seconds'],meta=c['meta']) for c in baseline['completed_calls']]
account=json.loads((AUTHOR/'final-accounting.json').read_text())
assert r['CPU']['primary_through_supervisor_serialization']==account['total_cpu_seconds_through_supervisor_serialization']
post=json.loads((AUTHOR/'postprocess-accounting.json').read_text());verify(post['receipt'])
assert post['receipt']==identity(receipt_path) and post['postprocessing_CPU_through_receipt_serialization']<1
out=dict(status='PASS',author_receipt=identity(receipt_path),postprocessor=identity(r['postprocessor']['path']),
    code=identity(__file__),verified_identity_records=5+len(r['raw_files'])+1,
    matched='all receipt call values/counts/criterion/costs and complete author accounting; exact replay unchanged',
    CPU_before_final_output=time.process_time(),scope='metadata only; proof/report hashes read as passive provenance, not runtime pins')
with (RAW/'author-receipt-check.json').open('x') as f:json.dump(out,f,indent=2)
print(json.dumps(out))
