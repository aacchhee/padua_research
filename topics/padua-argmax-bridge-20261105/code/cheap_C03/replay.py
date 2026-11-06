#!/usr/bin/env python3
"""One explicitly released C03 mode0 replay of frozen known-n32 bytes; no retry.

Preparation is not execution authorization. The coordinator must publish and
release before invoking --run-once --source-commit FULL_SHA. No leaf cap exists.
"""
import argparse
import collections
import ctypes
from fractions import Fraction
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import resource
import secrets
import signal
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[4]
TOPIC = ROOT/'topics/padua-argmax-bridge-20261105'
OLD = TOPIC/'code/phase_checker'
WORK = ROOT/'local-output/argmax-bridge-20261105/cheap-C03/n32'
REPORT = WORK/'checker-report.json'
RECEIPT = TOPIC/'evidence/c03-cheap-n32.json'
CANDIDATE_REL = 'evidence/n3-phase-n32-bootstrap-r8.json.gz'
CANDIDATE_SHA = '97c339181652d37e7e3c34522959f1b7157b8ea26d3f0ab83c0ebc1c3901528e'
BASELINE_REL = 'evidence/phase-r9-n32.json'
PRIOR_FAILED_REL = 'evidence/c02-cheap-n32.json'
PINS = {
    'code/cheap_C03/prototype.cpp': '9e357b25efde553211563bb69147644c67b7752bc703bf05ac502141c82e0861',
    'code/phase_checker/check_r8.py': '3c71ada8e49829cb897ee1c064fcdc70d08c846afcb1fb067c6c84673e205bb9',
    'code/phase_checker/check_r6.py': '437378a5d0fe21d4d0ef30b1c9843274d2cb98fc9f408e9bad5683ec9f1e73dc',
    'code/phase_checker/build_snapshot.py': '19a5a7c2296768853b94672b9b5dc4cf16c9ae87c37abbcde073ffaf89246bfb',
    'code/phase_checker/build_snapshot_r9.py': '6e29f5990515d50829aa7978ebeeb97dcb49e8f62716d62d37fc8ddc69e82bfa',
    'code/check_corner_exact.cpp': '3646f4e8b6b16957b9e1114f95ad2f0a7c18eec4687b49d5e6f1947a25eea6e3',
    'code/check_corner_range.py': '66fc2d9583260572125bd6c70a943577f94f1dd1ce2755a2c47ad96fffa9a982',
    'code/check_bootstrap_energy.py': '915c6c7c40e8c9e0c748cf50c2fe278f6760d79a9e725939aed1553269030972',
    'evidence/independent-bootstrap-energy.json': 'f0c48ea7f55e3a926b36537ebe46724b4305cacb9f1254c6417b2abd9676425b',
    'evidence/independent-corner-range.json': 'e685674c028bc99e42d547e8b84a2ce5a7e7e67c3cc69f6c29a55ecbcffd23c0',
    'evidence/n3-corner-batch.json': '97e20cc877ad5afd0c9dfe96c1e399a42d820b38c18626e2b69bfa54f6acfc88',
    'evidence/independent-corner-replay.json': '573afc5d5ae229b0fa1d47df9b6bf334e47e0e437288a3543826838e5403cb4b',
    CANDIDATE_REL: 'a01bc14b968676161afa0690e5ed41005da8cb3f87fb8c6393594bc37ed3986a',
    BASELINE_REL: '5bdab76556a37552121afabe172d641e57a60026d1b07b36c4f6e5e5069977ae',
    PRIOR_FAILED_REL: '924e8ebbe15ff8fd9a46e1d6c6887ae77e47fa4533af548df864fcea19bf3f41',
}
ARTIFACTS = ('source_snapshot', 'preprocessed_translation_unit', 'checker_binary')
GROUPS = ('toolchain', 'toolchain_dependency_closure', 'headers',
          'dependency_inputs', 'linked_dependency_closure', 'loaded_dependency_closure')


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def identity(path):
    path = Path(path).resolve()
    raw = path.read_bytes()
    return dict(path=str(path), bytes=len(raw), sha256=digest(raw))


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def write_new(path, data):
    with Path(path).open('x') as stream:
        json.dump(data, stream, indent=2, allow_nan=False)
        stream.write('\n')


def child_cpu():
    usage = resource.getrusage(resource.RUSAGE_CHILDREN)
    return usage.ru_utime+usage.ru_stime


def group_cpu(group):
    # Live own times plus waited-for descendant times: exited/reaped build
    # helpers transfer their time to the waiting ancestor, rather than vanish.
    ticks = 0
    for path in Path('/proc').iterdir():
        if not path.name.isdecimal():
            continue
        try:
            fields = (path/'stat').read_text().rsplit(')', 1)[1].split()
            if int(fields[2]) == group:
                ticks += sum(int(fields[i]) for i in (11, 12, 13, 14))
        except (FileNotFoundError, ProcessLookupError):
            pass
    return ticks/os.sysconf('SC_CLK_TCK')


def inputs():
    entries = []
    for relative, sha in PINS.items():
        item = identity(TOPIC/relative)
        require(item['sha256'] == sha, 'frozen input mismatch: '+relative)
        entries.append(item)
    raw = gzip.decompress((TOPIC/CANDIDATE_REL).read_bytes())
    require(len(raw) == 21338 and digest(raw) == CANDIDATE_SHA, 'candidate plain bytes mismatch')
    return entries, raw


def verify(entries):
    for item in entries:
        require(identity(item['path']) == item, 'identity changed: '+item['path'])


def verify_publication(commit, entries):
    # Read-only Git operation; verifies content at the supplied publication
    # SHA. Remote publication and run release remain the coordinator's gate.
    for item in entries:
        relative = str(Path(item['path']).relative_to(ROOT))
        result = subprocess.run(['git', 'cat-file', 'blob', commit+':'+relative],
                                cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        require(result.returncode == 0 and len(result.stdout) == item['bytes'] and
                digest(result.stdout) == item['sha256'],
                'publication commit content mismatch: '+relative)


def full_closure(manifest):
    entries = [manifest[key] for key in ARTIFACTS]
    for key in GROUPS:
        require(bool(manifest[key]), 'missing build/runtime closure: '+key)
        entries.extend(manifest[key])
    return entries


def project_modules():
    paths = {Path(__file__).resolve()}
    for module in tuple(sys.modules.values()):
        filename = getattr(module, '__file__', None)
        if filename:
            path = Path(filename).resolve()
            if path.is_relative_to(ROOT):
                paths.add(path)
    allowed = {Path(__file__).resolve(), *(TOPIC/p for p in PINS if p.endswith('.py'))}
    require(paths <= allowed, 'unrecorded project Python import: '+str(paths-allowed))
    return [identity(path) for path in sorted(paths)]


def fresh_build(builder):
    # Same frozen builder, adapting only source/output paths. No acceptance
    # function, interval function, numerical guard or imported module is patched.
    text = Path(builder.__file__).read_text()
    substitutions = {
        "LOCAL=ROOT/'local-output/argmax-bridge-20261105/phase-r9'":
        "LOCAL=ROOT/'local-output/argmax-bridge-20261105/cheap-C03/n32/build'",
        'source_path=pathlib.Path(__file__).with_name(KERNEL_SOURCES[kernel_variant])':
        "source_path=ROOT/'topics/padua-argmax-bridge-20261105/code/cheap_C03/prototype.cpp'",
    }
    for old, new in substitutions.items():
        require(text.count(old) == 1, 'builder adaptation target changed')
        text = text.replace(old, new)
    snapshot = WORK/'builder_snapshot.py'
    with snapshot.open('x') as stream:
        stream.write(text)
    namespace = {'__file__': str(OLD/'build_snapshot_r9.py')}
    exec(compile(text, str(snapshot), 'exec'), namespace)
    binary, manifest = namespace['build']()
    manifest['executed_builder_snapshot'] = identity(snapshot)
    manifest['adaptation'] = 'only source_origin and fresh output directory; frozen builder arithmetic unchanged'
    require(manifest['source_snapshot']['sha256'] == PINS['code/cheap_C03/prototype.cpp'],
            'built source is not reviewed C03 prototype')
    return binary, manifest, namespace['loaded_closure']


class Kernel:
    def __init__(self, builder):
        binary, self.provenance, self.loaded = fresh_build(builder)
        self.lib = ctypes.CDLL(str(binary))
        self.provenance['loaded_dependency_closure'] = self.loaded(self.provenance)
        verify(full_closure(self.provenance))
        self.fn = self.lib.phase_bounds
        self.fn.argtypes = [ctypes.c_int]+[ctypes.c_double]*4+[ctypes.POINTER(ctypes.c_double)]
        self.fn.restype = ctypes.c_int
        self.mode = self.lib.c03_variant
        self.mode.argtypes = [ctypes.c_int]
        self.mode.restype = ctypes.c_int
        require(self.mode(0) == 0, 'failed to select the sole released mode0')
        self.provenance['selected_variant'] = 0
        self.counter = self.lib.c03_counts
        self.counter.argtypes = [ctypes.POINTER(ctypes.c_double)]
        self.counter.restype = None
        self.calls = 0
        self.cpu = 0.
        self.counts = [0.]*12
        self.trace = (WORK/'native-calls.jsonl').open('x')
        write_new(WORK/'build-before.json', self.provenance)

    def bounds(self, n, box):
        require(type(n) is int and n == 32, 'only known degree32 is released')
        started = time.process_time()
        out = (ctypes.c_double*7)()
        code = self.fn(n, *box, out)
        counters = (ctypes.c_double*12)()
        self.counter(counters)
        duration = time.process_time()-started
        self.calls += 1
        self.cpu += duration
        self.counts = [a+b for a, b in zip(self.counts, counters)]
        record = dict(call=self.calls, n=n, box=box, status=code,
                      bounds=[x if math.isfinite(x) else repr(x) for x in out],
                      counters=list(counters), cpu_seconds=duration)
        self.trace.write(json.dumps(record, allow_nan=False)+'\n')
        self.trace.flush()
        require(code == 0 and all(math.isfinite(x) for x in out), 'native bounds failed')
        require(counters[10] == 0 and counters[11] == 0,
                'unreleased centered or ODE refinement observed')
        require(out[3] <= out[4] and out[5] <= out[6], 'inconsistent constants')
        return list(out)

    def verify_after(self):
        self.trace.close()
        verify(full_closure(self.provenance))
        verify([self.provenance['executed_builder_snapshot']])
        require(self.loaded(self.provenance) == self.provenance['loaded_dependency_closure'],
                'actual loaded mappings changed during replay')


def worker(token):
    resource.setrlimit(resource.RLIMIT_CPU, (178, 179))
    launch = json.loads((WORK/'launch.json').read_bytes())
    require(token == launch['worker_token'] and os.getppid() == launch['supervisor_pid'] and
            os.getpgrp() == os.getpid(), 'worker must be launched once by its supervisor')
    started, before = time.process_time(), child_cpu()
    kernel, report, code = None, {}, 1
    try:
        entries, raw = inputs()
        require(entries == launch['inputs'] and identity(__file__) == launch['supervisor'],
                'launch snapshot changed before worker')
        require((WORK/'candidate.json').read_bytes() == raw, 'worker candidate snapshot mismatch')
        sys.path.insert(0, str(OLD))
        import check_r8 as acceptance
        import build_snapshot_r9 as builder
        imports = project_modules()
        verify(imports)
        python_runtime = identity(sys.executable)
        data = acceptance.strict_json(raw)
        require(data.get('n') == 32 and data.get('complete') is True and
                len(data.get('leaves', [])) == 364 and data.get('pending') == [],
                'wrong candidate scope')
        kernel = Kernel(builder)
        # Exact unmodified acceptance function, explicit new arithmetic object,
        # no cap, no predicate interception and no tree/leaf mutation.
        report = acceptance.check(data, kernel)
        kernel.verify_after()
        verify(entries+[launch['supervisor'], python_runtime]+imports)
        require(project_modules() == imports, 'project imports changed during replay')
        require((WORK/'candidate.json').read_bytes() == raw, 'candidate snapshot changed')
        require(inputs() == (entries, raw), 'source/input closure changed after replay')
        report['source_input_runtime_unchanged_after'] = True
        report['project_python_sources'] = imports
        report['python_runtime'] = python_runtime
        report['python_version'] = sys.version
        code = 0 if report.get('accepted') is True else 1
    except Exception as error:
        report['mathematical_acceptance_before_error'] = report.get('accepted')
        report.update(accepted=False, error=repr(error))
    finally:
        if kernel is not None:
            if not kernel.trace.closed:
                kernel.trace.close()
            report['build_provenance'] = kernel.provenance
            report['native_calls'] = kernel.calls
            report['native_cpu_seconds'] = kernel.cpu
            report['native_counts'] = kernel.counts
        report.update(candidate_sha256=CANDIDATE_SHA, candidate_bytes=21338,
                      source_commit=launch['source_commit'], no_max_leaves=True, selected_variant=0)
        write_new(REPORT, report)
        write_new(WORK/'worker-accounting.json', dict(exit_status=code,
                  worker_cpu_seconds=time.process_time()-started,
                  compiler_helper_cpu_seconds=child_cpu()-before,
                  process_rlimit_cpu=[178, 179]))
    return code


def comparison(report, baseline, raw_before):
    result = dict(old_accepted=baseline['accepted'], old_checked_leaves=baseline['checked_leaves'],
                  old_total_cpu_seconds=baseline['total_subprocess_cpu_seconds'],
                  scope='same frozen candidate; changed kernel; no new degree',
                  raw_comparison_available=raw_before is not None)
    if raw_before is None:
        result['limitation'] = 'Old raw report absent; only committed acceptance/CPU comparison available.'
        return result
    verify([raw_before])
    old = json.loads(Path(raw_before['path']).read_bytes())
    previous, current = old.get('replay', []), report.get('replay', [])
    if len(previous) != len(current):
        result['same_complete_leaf_order'] = False
        return result
    result['same_complete_leaf_order'] = all(
        (a['root'], a['path'], a['kind']) == (b['root'], b['path'], b['kind'])
        for a, b in zip(previous, current))
    weakened = collections.Counter()
    for a, b in zip(previous, current):
        if a.get('bounds') is None or b.get('bounds') is None:
            continue
        for i in range(7):
            x, y = Fraction(a['bounds'][i]), Fraction(b['bounds'][i])
            if (y < x if i in (2, 3, 5) else y > x):
                weakened[str(i)] += 1
    result['weakened_bound_counts_by_output_index'] = dict(weakened)
    result['old_valid_now_failed'] = sum(a.get('valid') is True and b.get('valid') is False
                                         for a, b in zip(previous, current))
    return result


def supervisor(commit):
    start, own_start, before = time.monotonic(), time.process_time(), child_cpu()
    require(len(commit) == 40 and not set(commit)-set('0123456789abcdef'), 'full lowercase source commit SHA required')
    require(not WORK.exists() and not RECEIPT.exists(), 'refuse replay/output reuse')
    entries, raw = inputs()
    wrapper = identity(__file__)
    verify_publication(commit, entries+[wrapper])
    baseline = json.loads((TOPIC/BASELINE_REL).read_bytes())
    prior_failed = json.loads((TOPIC/PRIOR_FAILED_REL).read_bytes())
    require(prior_failed.get('accepted') is False and prior_failed.get('checked_leaves') == 364 and
            prior_failed.get('failed_leaves_count') == 76 and
            prior_failed['candidate']['sha256'] == CANDIDATE_SHA,
            'wrong preserved C02 failed outcome')
    require(baseline.get('accepted') is True and baseline.get('checked_leaves') == 364 and
            baseline['candidate']['sha256'] == CANDIDATE_SHA, 'wrong accepted old baseline')
    oldraw = baseline['checker_report']
    oldpath = ROOT/oldraw['path']
    raw_before = identity(oldpath) if oldpath.exists() else None
    if raw_before:
        require((raw_before['bytes'],raw_before['sha256']) == (oldraw['bytes'],oldraw['sha256']),
                'old raw report identity mismatch')
    WORK.mkdir(parents=True, exist_ok=False)
    token = secrets.token_hex(16)
    launch = dict(source_commit=commit, supervisor_pid=os.getpid(), worker_token=token,
                  inputs=entries, supervisor=wrapper, old_raw_report=raw_before)
    write_new(WORK/'launch.json', launch)
    with (WORK/'candidate.json').open('xb') as stream:
        stream.write(raw)
    stdout, stderr = WORK/'stdout.txt', WORK/'stderr.txt'
    command = [sys.executable, str(Path(__file__).resolve()), '--worker-token', token]
    peak, stopped = 0., False
    preworker_cpu = child_cpu()-before
    with stdout.open('x') as out, stderr.open('x') as err:
        process = subprocess.Popen(command, stdout=out, stderr=err, start_new_session=True)
        try:
            while process.poll() is None:
                observed = group_cpu(process.pid)+preworker_cpu+time.process_time()-own_start
                peak = max(peak, observed)
                if observed >= 176:
                    os.killpg(process.pid, signal.SIGKILL)
                    stopped = True
                    break
                time.sleep(.1)
            code = process.wait()
        except BaseException:
            # An interrupted or failed supervisor must not leave the compiler
            # or checker running outside its one-shot budget.
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            process.wait()
            raise
    report = json.loads(REPORT.read_bytes()) if REPORT.exists() else {}
    errors = []
    closure_entries = []
    try:
        verify(entries+[wrapper])
        require(inputs() == (entries, raw), 'source/input changes after worker')
        require((WORK/'candidate.json').read_bytes() == raw, 'candidate changed after worker')
        closure_entries = full_closure(report['build_provenance'])
        verify(closure_entries+[report['build_provenance']['executed_builder_snapshot']])
        require(report.get('source_input_runtime_unchanged_after') is True, 'worker did not finish runtime checks')
        require(report.get('selected_variant') == 0 and
                report['build_provenance'].get('selected_variant') == 0 and
                len(report.get('native_counts', [])) == 12 and
                report['native_counts'][10:] == [0, 0],
                'mode0 execution identity or counters changed')
        compared = comparison(report, baseline, raw_before)
    except Exception as error:
        errors.append(repr(error))
        compared = dict(old_accepted=True, old_total_cpu_seconds=baseline['total_subprocess_cpu_seconds'])
    subprocess_cpu = child_cpu()-before
    supervisor_cpu = time.process_time()-own_start
    total_cpu = subprocess_cpu+supervisor_cpu
    failed = report.get('failed_leaves', [])
    passed = (code == 0 and not stopped and not errors and total_cpu <= 180 and
              report.get('accepted') is True and report.get('complete') is True and
              report.get('n') == 32 and report.get('checked_leaves') == 364 and
              report.get('total_leaves') == 364 and report.get('pending') == 0 and failed == [] and
              report.get('candidate_sha256') == CANDIDATE_SHA and report.get('candidate_bytes') == 21338)
    receipt = dict(format='C03-cheap-known-n32-v1', status='PASS' if passed else 'FAIL',
                   accepted=passed, source_commit=commit, supervisor=wrapper,
                   prototype=identity(TOPIC/'code/cheap_C03/prototype.cpp'),
                   candidate=dict(sha256=CANDIDATE_SHA, bytes=21338),
                   supervisor_argv=[sys.executable, str(Path(__file__).resolve()), '--run-once', '--source-commit', commit],
                   process_exit_status=code, watchdog_stopped=stopped, errors=errors,
                   total_cpu_seconds=total_cpu, total_subprocess_cpu_seconds=subprocess_cpu,
                   supervisor_cpu_seconds=supervisor_cpu, wall_seconds=time.monotonic()-start,
                   total_cpu_limit_seconds=180, watchdog_trigger_seconds=176,
                   observed_group_plus_supervisor_peak_seconds=peak, worker_rlimit_cpu=[178,179],
                   checked_leaves=report.get('checked_leaves'), total_leaves=report.get('total_leaves'),
                   pending=report.get('pending'), complete=report.get('complete'),
                   failed_leaves_count=len(failed), first_failed_leaf=failed[0] if failed else None,
                   native_calls=report.get('native_calls'), native_cpu_seconds=report.get('native_cpu_seconds'),
                   native_counts=report.get('native_counts'),
                   counter_order=['base_ratio','sin_cos','base_pole','base_fallback','lazy_S','analytic_floor',
                                  'profiles','boards','outer_ratio','endpoint_refinements','centered_refinements','ODE_caps'],
                   source_runtime_checks_complete=not errors, closure_entries_rehashed_after=len(closure_entries),
                   baseline_comparison=compared,
                   prior_failed_C02=dict(receipt=identity(TOPIC/PRIOR_FAILED_REL), accepted=False,
                       checked_leaves=364, failed_leaves_count=76,
                       total_cpu_seconds=prior_failed['total_cpu_seconds']),
                   selected_variant=0, mode_switches=0, no_max_leaves=True, retries=0,
                   producer_run=False, tree_refinement=False, new_candidate=False, new_degree_certified=False,
                   full_record=identity(REPORT) if REPORT.exists() else None,
                   launch_record=identity(WORK/'launch.json'), stdout=identity(stdout), stderr=identity(stderr),
                   worker_accounting=identity(WORK/'worker-accounting.json') if (WORK/'worker-accounting.json').exists() else None,
                   native_trace=identity(WORK/'native-calls.jsonl') if (WORK/'native-calls.jsonl').exists() else None,
                   scope='one mode0 replay of original known n32 candidate; failed predicates retained; no rescue or mode switch',
                   actual_loaded_closure_location='full_record.build_provenance.loaded_dependency_closure')
    require(len(json.dumps(receipt).encode()) < 12000, 'essential receipt exceeds prospective size cap')
    write_new(RECEIPT, receipt)
    print(json.dumps(dict(status=receipt['status'], accepted=passed, checked=receipt['checked_leaves'],
                          failed=receipt['failed_leaves_count'], total_cpu_seconds=total_cpu)))
    return 0 if passed else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run-once', action='store_true')
    parser.add_argument('--source-commit')
    parser.add_argument('--worker-token', help=argparse.SUPPRESS)
    args = parser.parse_args()
    os.chdir(ROOT)
    if args.worker_token:
        require(not args.run_once and args.source_commit is None, 'invalid internal worker arguments')
        return worker(args.worker_token)
    require(args.run_once and args.source_commit is not None, 'explicit run-once and publication SHA required')
    return supervisor(args.source_commit)


if __name__ == '__main__':
    raise SystemExit(main())
