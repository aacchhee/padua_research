#!/usr/bin/env python3
"""Independent C01 source/receipt check and ONE uninstrumented n32 box.

No certificate acceptance or new degree. Raw build closure stays local.
"""
import ctypes
import hashlib
import json
import pathlib
import resource
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[4]
TOPIC = ROOT / 'topics/padua-argmax-bridge-20261105'
LOCAL = ROOT / 'local-output/argmax-bridge-20261105/c01-review-profile'
sys.path.insert(0, str(TOPIC / 'code/phase_checker'))
import build_snapshot_r9 as build
import check_r8


def identity(path):
    return build.identity(path)


def checked(item):
    assert identity(item['path']) == item, item['path']


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    start = time.process_time()
    wall = time.monotonic()
    child = resource.getrusage(resource.RUSAGE_CHILDREN)
    output = TOPIC / 'evidence/c01-review-profile.json'
    assert not output.exists(), 'one-shot receipt already exists'
    receipt = TOPIC / 'evidence/c01-fast-profile.json'
    assert identity(receipt)['sha256'] == '146abbe78426ab81bdd5f73a4e46e1677da732fc1210dd87084609edf144688b'
    saved = json.loads(receipt.read_bytes())
    rawpath = ROOT / saved['raw_receipt']['path']
    assert identity(rawpath)['sha256'] == saved['raw_receipt']['sha256']
    assert identity(rawpath)['bytes'] == saved['raw_receipt']['bytes']
    raw = json.loads(rawpath.read_bytes())
    for key in ('source', 'instrumentation', 'generated_source', 'builder'):
        checked(raw[key])
        assert raw[key] == saved[key]
    assert raw['results'] == saved['results']
    for item in raw['inputs']:
        checked(item)
    groups = ('toolchain', 'toolchain_dependency_closure', 'headers',
              'dependency_inputs', 'linked_dependency_closure', 'loaded_dependency_closure')
    for key in groups:
        for item in raw['build'][key]:
            checked(item)
        assert len(raw['build'][key]) == saved['closure_entry_counts'][key]
    for key in ('source_snapshot', 'preprocessed_translation_unit', 'checker_binary'):
        checked(raw['build'][key])
    original = pathlib.Path(raw['source']['path']).read_text()
    instrumented = pathlib.Path(raw['generated_source']['path']).read_text()
    # Undo independently enumerated insertions, demanding one occurrence each.
    additions = [
        '\n#include <ctime>\nstatic double cp(){timespec t;clock_gettime(CLOCK_PROCESS_CPUTIME_ID,&t);return t.tv_sec+1e-9*t.tv_nsec;}\nstatic double stats[12]={};\nstruct Scope{int i;double t;Scope(int j):i(j),t(cp()){}~Scope(){stats[i]+=cp()-t;}};\nextern "C" void c01_stats(double*out){for(int i=0;i<12;i++){out[i]=stats[i];stats[i]=0;}}\n\n',
        ' Scope timer(0);stats[4]++;stats[5]+=n;\n',
        ' Scope timer(1);stats[6]++;\n',
        ' stats[7]++;\n',
        ' Scope timer(2);stats[8]++;stats[9]+=2*n*(n+1);\n',
        '\n Scope timer(3);stats[10]++;stats[11]+=2*n*(n+1)*(2*n+3);',
    ]
    for addition in additions:
        assert instrumented.count(addition) == 1
        instrumented = instrumented.replace(addition, '')
    assert instrumented == original, 'arithmetic source changed'
    formula_checks = []
    for case in saved['results']:
        n, s = case['n'], case['stats']
        assert s[4] == 12*n*(n+1)
        assert s[5] == 12*n*n*(n+1)
        assert s[6] == 24*n*(n+1)
        assert 0 <= s[7] <= s[6]
        assert s[8] == 3 and s[9] == 6*n*(n+1) and s[10] == 2
        assert s[11] == 4*n*(n+1)*(2*n+3)
        actual_trig = s[5] + s[9] + s[6] + s[7]
        assert 6*n*(n+1)*(2*n+5) <= actual_trig <= 6*n*(n+1)*(2*n+9)
        assert case['status'] == 0
        formula_checks.append({'n': n, 'inferred_trig_calls': int(actual_trig)})
    # This fresh build is the frozen uninstrumented implementation, independently
    # loaded; the author's instrumented binary is never called in this review.
    LOCAL.mkdir(parents=True, exist_ok=True)
    build.LOCAL = LOCAL
    binary, manifest = build.build('round9')
    lib = ctypes.CDLL(str(binary))
    manifest['loaded_dependency_closure'] = build.loaded_closure(manifest)
    candidate = json.loads(pathlib.Path(raw['inputs'][2]['path']).read_bytes())
    leaf = next(item for item in candidate['leaves'] if item['kind'] != 'outside')
    box = check_r8.box_for(candidate['roots'], leaf['root'], leaf['path'])
    expected = next(item for item in saved['results'] if item['n'] == 32)
    assert box == expected['box']
    fn = lib.phase_bounds
    fn.argtypes = [ctypes.c_int] + [ctypes.c_double]*4 + [ctypes.POINTER(ctypes.c_double)]
    fn.restype = ctypes.c_int
    bounds = (ctypes.c_double*7)()
    before, before_wall = time.process_time(), time.monotonic()
    status = fn(32, *box, bounds)
    elapsed, elapsed_wall = time.process_time()-before, time.monotonic()-before_wall
    assert status == 0 and list(bounds) == expected['bounds']
    for key in groups:
        for item in manifest[key]:
            checked(item)
    for key in ('source_snapshot', 'preprocessed_translation_unit', 'checker_binary'):
        checked(manifest[key])
    checked(raw['source'])
    checked(raw['instrumentation'])
    rawout = LOCAL / 'build-manifest.json'
    rawout.write_text(json.dumps(manifest, indent=2)+'\n')
    now_child = resource.getrusage(resource.RUSAGE_CHILDREN)
    report = dict(
        format='C01-independent-profile-review-v1', status='MEASURED',
        rules_head='4b728b04216a5490910780bc609a82b853058426',
        reviewer='Codex; supplementary independent review; serving metadata unexposed',
        code=identity(pathlib.Path(__file__)), frozen_profile=identity(receipt),
        source=raw['source'], input=raw['inputs'][2],
        source_instrumentation_only=True, saved_closure_entries_checked=sum(len(raw['build'][key]) for key in groups),
        formula_checks=formula_checks,
        replay=dict(n=32, box=box, status=status, bounds=list(bounds),
                    identical_to_frozen_profile=True, cpu=elapsed, wall=elapsed_wall),
        build_manifest=identity(rawout), compiler_version=manifest['compiler_version'],
        binary=manifest['checker_binary'],
        own_cpu=time.process_time()-start,
        child_cpu=now_child.ru_utime+now_child.ru_stime-child.ru_utime-child.ru_stime,
        wall=time.monotonic()-wall,
        limitations=['One uninstrumented saved box; no full replay or certification.',
                     'Source equality and one output comparison do not measure timer overhead generally.'])
    output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
