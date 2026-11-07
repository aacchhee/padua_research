#!/usr/bin/env python3
"""Summarize an actually completed independent replay; performs no arithmetic."""
import collections
import hashlib
import json
from pathlib import Path
from n3_native_receipt import identity

ROOT=Path(__file__).resolve().parents[3]
TOPIC=Path(__file__).resolve().parents[1]
WORK=ROOT/'local-output/argmax-bridge-20261105/N3/outward-full-n17-r3'
REPORT=ROOT/'local-output/argmax-bridge-20261105/phase-checker/n17-full-r3-replay.json'

def main():
    raw=REPORT.read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='021ded297f360245fb30a884efe7a3670321e4a736c22873abaa6079cc0257d7'
    report=json.loads(raw)
    candidate=WORK/'n17-phase-compact.json'
    assert identity(candidate)['sha256']==report['candidate_sha256']=='64f7befd86658c8d9f29b05c1cb5a0162e611b726b161e737610547bed218c4b'
    assert report['complete'] is True and report['accepted'] is False
    assert report['checked_leaves']==report['total_leaves']==1288 and report['pending']==0
    failures=collections.Counter(x['kind'] for x in report['failed_leaves'])
    assert dict(failures)=={'far':184,'corner-orbit-plus-defect':180}
    result={
        'status':'MEASURED independent replay enclosure gap; phase proof OPEN',
        'rules_input':'c000899f3fb10d6ba0f1725341a045fe11ec943a',
        'collector_source':identity(Path(__file__).resolve()),
        'identity_helper':identity(TOPIC/'code/n3_native_receipt.py'),
        'collector_command':'python topics/padua-argmax-bridge-20261105/code/n3_full_result.py',
        'independent_checker_command':'python topics/padua-argmax-bridge-20261105/code/phase_checker/check.py local-output/argmax-bridge-20261105/N3/outward-full-n17-r3/n17-phase-compact.json --output local-output/argmax-bridge-20261105/phase-checker/n17-full-r3-replay.json',
        'independent_report':identity(REPORT),
        'candidate':identity(candidate),
        'essential_gzip_local':identity(WORK/'n17-phase-compact.json.gz'),
        'producer_summary':identity(TOPIC/'evidence/n3-full-n17-producer.json'),
        'build_manifest':identity(TOPIC/'evidence/n3-full-n17-build.json'),
        'independent_checker_binary':report['build_provenance']['checker_binary'],
        'independent_checker_python_sources':report['checker_python_sources'],
        'complete':True,'accepted':False,'checked_leaves':1288,'pending':0,
        'passing_leaves':924,'failed_leaves':364,'failure_counts':dict(failures),
        'independent_cpu_seconds':report['cpu_seconds'],
        'first_failure':report['failed_leaves'][0],
        'interpretation':'The distinct finite-cosine interval kernel did not establish sufficient inequalities on 364 broad leaves. This is not a witnessed function counterexample or a proof that the producer arithmetic is unsound. All 28 inherited-local and 32 outside leaves passed. No mathematical proof promotion or finite-range extension follows.',
        'next_unexecuted':'After stage publication and authorization, strengthen the independent quotient kernel or refine geometry and independently replay a newly frozen candidate. No refinement was run at this boundary.',
        'retention':'Large original trace and independent full report remain local; cold-storage archival pending. Essential compact gzip fits the evidence limit and its decompressed exact bytes are pinned above.'}
    encoded=(json.dumps(result,indent=2)+'\n').encode()
    assert len(encoded)<16384
    (TOPIC/'evidence/n3-full-n17-result.json').write_bytes(encoded)
    print(json.dumps({'bytes':len(encoded),'failed_leaves':364,'accepted':False}))

if __name__=='__main__':main()
