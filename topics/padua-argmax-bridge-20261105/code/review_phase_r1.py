#!/usr/bin/env python3
"""Independent focused R1 evidence/predicate review; no arithmetic rerun."""
import hashlib
import importlib.util
import json
import math
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[3]
TOPIC = ROOT / 'topics/padua-argmax-bridge-20261105'
OUT = ROOT / 'local-output/argmax-bridge-20261105/phase-math-review'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(identity):
    path = pathlib.Path(identity['path'])
    if not path.is_absolute():
        path = ROOT / path
    raw = path.read_bytes()
    assert len(raw) == identity['bytes'] and hashlib.sha256(raw).hexdigest() == identity['sha256'], path


def main():
    names = ['check.py', 'build_snapshot.py', 'arb_kernel.cpp', 'provenance_controls.py']
    pins = dict(zip(names, [
        '8713026a1b5a872f0e8dd33c311eafef2cf310f42ae2eebb4055ad224b8acfae',
        'a8a805ba27e880a3a5cf1db7d0707dab4a982d7a988b493c822015518ee2e2c2',
        '236116452dc7aae66e39cbf8800fe847cffe931ac0ce8a9682397313de7c43a6',
        '983a63abddbcb2f83f22116070be9af956d89a9fc4b8df445787da57293ca810']))
    source = TOPIC / 'code/phase_checker'
    for name, pin in pins.items():
        assert sha(source / name) == pin
    spec = importlib.util.spec_from_file_location('review_r1_checker', source / 'check.py')
    ck = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ck)
    rejections = []
    for raw in [b'{"n":17,"n":33}', b'{"x":{"a":0,"a":1}}',
                b'{"x":NaN}', b'{"x":Infinity}', b'{"x":1e400}']:
        try:
            ck.strict_json(raw)
        except ck.Invalid:
            rejections.append(raw.decode())
        else:
            raise AssertionError(raw)
    premise = ck.published_corner_premise()
    assert premise['receipt_sha256'] == '573afc5d5ae229b0fa1d47df9b6bf334e47e0e437288a3543826838e5403cb4b'
    guards = {}
    for n in (17,24,32,33,64,128,129):
        guards[str(n)] = ck.local_fixed_instance(n, [-1/128,1/128,-1/128,1/128])
        assert guards[str(n)] == (n in (33,64,128))
    for n in (33,64,128):
        assert not ck.local_fixed_instance(n, [0.,math.nextafter(1/128,math.inf),0.,0.])
    receipt_path = TOPIC / 'evidence/phase-checker-provenance.json'
    receipt = json.loads(receipt_path.read_bytes())
    all_count, rows, workdirs = 0, [], []
    for row in receipt['fresh_replays']:
        verify(row)
        replay = json.loads((ROOT / row['path']).read_bytes())
        assert not replay['accepted'] and not replay['complete'] and not replay['failed_leaves']
        assert replay['checked_leaves'] == 1 and replay['pending'] > 0
        manifest = replay['build_provenance']
        workdirs.append(manifest['workdir'])
        fields = ['source_snapshot','preprocessed_translation_unit','checker_binary']
        identities = [manifest[field] for field in fields]
        for field in ['toolchain','toolchain_dependency_closure','headers','dependency_inputs',
                      'linked_dependency_closure','loaded_dependency_closure']:
            identities.extend(manifest[field])
        identities.extend(replay['checker_python_sources'])
        for identity in identities:
            verify(identity)
        assert manifest['source_snapshot']['sha256'] == pins['arb_kernel.cpp']
        assert replay['candidate_sha256'] == sha(ROOT / 'local-output/argmax-bridge-20261105/N3/outward-calibration-v1/n17-sample-far.json')
        all_count += len(identities)
        rows.append({'path':row['path'],'sha256':row['sha256'],'verified_identity_entries':len(identities)})
    assert len(set(workdirs)) == 2
    report = {'scope':'Independent R1 source/evidence inspection plus focused parser/premise controls; no new full replay',
              'reviewer':'distinct Codex Astra high assignment; serving metadata not independently exposed',
              'command':'python topics/padua-argmax-bridge-20261105/code/review_phase_r1.py',
              'source_pins':pins,'script_sha256':sha(pathlib.Path(__file__).resolve()),
              'provenance_receipt_sha256':sha(receipt_path),'parser_controls_rejected':len(rejections),
              'fixed_corner_guards':guards,'outside_phase_guard_rejected':True,
              'corner_premise':premise,'manifest_rows':rows,'verified_identity_entries':all_count,
              'R1_disposition':'CLOSED at listed hashes; normal trusted compiler/runtime assumptions remain',
              'full_n17_replay':'Performed separately by phase_checker; not claimed as this reviewer execution'}
    OUT.mkdir(parents=True, exist_ok=True)
    target = TOPIC / 'evidence/phase-math-review-r1.json'
    target.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'R1':report['R1_disposition'],'verified_identity_entries':all_count,
                      'parser_controls':len(rejections),'receipt':str(target.relative_to(ROOT))}))


if __name__ == '__main__':
    main()
