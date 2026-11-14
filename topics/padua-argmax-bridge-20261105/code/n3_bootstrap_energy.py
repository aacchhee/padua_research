#!/usr/bin/env python3
"""Fixed N3 bootstrap energy helper; old-data countertest then one fresh sweep.

The MPFR C arithmetic is unchanged. Exact Fraction comparisons test the new
4E<=3*n^4*ell threshold. Producer success remains CONDITIONAL until a
distinct fresh GMP reconstruction; old kappa acceptance is not reused.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path
import platform
import resource
import shutil
import subprocess
import sys
import time

BASE = Path('topics/padua-argmax-bridge-20261105')
INPUT_SHA = '88e702321cd5d9c3395a551fc8a55a2f7cb8bc10'
FIRST, LAST, BITS, CPU_CAP = 2, 128, 256, 1200
FROZEN = {
    BASE / 'code/n3_corner_bounds.c': 'a0497ca1219850e28f2bf51e72cb4fc8f78cde238b81fd678262d646511402bd',
    BASE / 'code/check_corner_exact.cpp': '3646f4e8b6b16957b9e1114f95ad2f0a7c18eec4687b49d5e6f1947a25eea6e3',
    BASE / 'evidence/n3-corner-batch.json': '97e20cc877ad5afd0c9dfe96c1e399a42d820b38c18626e2b69bfa54f6acfc88',
    BASE / 'evidence/independent-corner-range.json': 'e685674c028bc99e42d547e8b84a2ce5a7e7e67c3cc69f6c29a55ecbcffd23c0',
    Path('local-output/argmax-bridge-20261105/N3-corner-batch/r01/corner-bounds-n2-128.jsonl'): '58d3586adae81360b296740c984e122affab08514e1e3e0481803b26a5404d2f',
    Path('local-output/argmax-bridge-20261105/check-corner-range/own-n2-128.jsonl'): '47f3d233b5fd7bc46dca8c45a0de2ecc09be4d36988ab83b16f87c44a843bd20',
}


def sha_bytes(data):
    return hashlib.sha256(data).hexdigest()


def identity(path):
    path = Path(path)
    return dict(path=str(path), bytes=path.stat().st_size,
                sha256=sha_bytes(path.read_bytes()))


def child_cpu():
    usage = resource.getrusage(resource.RUSAGE_CHILDREN)
    return usage.ru_utime + usage.ru_stime


def limits(seconds):
    def apply():
        # Reserve a full CPU second against integer RLIMIT rounding.
        bound = max(1, math.floor(seconds) - 1)
        resource.setrlimit(resource.RLIMIT_CPU, (bound, bound))
    return apply


def endpoints(cert, n, producer):
    if cert['degree'] != n or cert['precision_bits'] != (256 if producer else 512):
        raise ValueError('degree/precision mismatch')
    if producer and cert['schema'] != 'n3-corner-energy-v1':
        raise ValueError('producer schema mismatch')
    ell, high, low_energy, energy = (Q(cert[k]) for k in
        ('corner_lower', 'corner_upper', 'energy_lower', 'energy_upper'))
    if not (0 < ell <= high and 0 <= low_energy <= energy):
        raise ValueError('invalid endpoint order')
    if cert['zero_cardinals_omitted'] != n // 2:
        raise ValueError('zero mask count mismatch')
    if cert['nonzero_cardinals'] + n // 2 != (n + 1) * (n + 2) // 2:
        raise ValueError('cardinal count mismatch')
    b = energy / (n ** 4 * ell)
    if Q(cert['normalized_energy_upper']) != b:
        raise ValueError('normalized energy assembly mismatch')
    if n == 2 and not (ell <= 3 <= high and low_energy <= Q(331, 18) <= energy):
        raise ValueError('exact n2 mass/energy control failed')
    return b, 3 * n ** 4 * ell - 4 * energy


def old_countertest(path, producer):
    rows = [json.loads(line) for line in path.read_text().splitlines()]
    if [r['degree'] for r in rows] != list(range(FIRST, LAST + 1)):
        raise ValueError(f'old input coverage mismatch: {path}')
    maximum, worst_n = None, None
    for row in rows:
        n = row['degree']
        cert = row['certificate'] if producer else row
        b, margin = endpoints(cert, n, producer)
        if margin < 0:
            raise ValueError(f'old endpoint countertest failed at n{n}: 3*n^4*ell-4E={margin}')
        if maximum is None or b > maximum:
            maximum, worst_n = b, n
    return dict(status='EXACT_ENDPOINT_COUNTERTEST_PASS', count=len(rows),
                maximum_normalized_energy_upper=str(maximum), maximum_degree=worst_n,
                gap_below_three_quarters=str(Q(3, 4) - maximum),
                scope='Old identified endpoints only; not fresh independent acceptance of the new threshold')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--mpfr-include', type=Path, required=True)
    parser.add_argument('--receipt', type=Path, required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=False)
    started, initial_cpu = time.monotonic(), child_cpu()
    start_utc = datetime.now(timezone.utc).isoformat()
    counters = dict(requested=127, attempted=0, completed=0, passed_new_threshold=0,
                    failed_new_threshold=0, arithmetic_or_process_errors=0, unrun=127,
                    nonzero_cardinals=0, zero_cardinals_omitted=0)
    frozen, countertests, helpers, runtime, failure = [], [], [], [], None
    maximum, maximum_n, native_cpu, versions = None, None, 0.0, None
    source = BASE / 'code/n3_corner_bounds.c'
    source_snapshot = args.output_dir / 'n3_corner_bounds.c'
    binary = args.output_dir / 'n3_corner_bounds'
    rawpath = args.output_dir / 'bootstrap-energy-n2-128.jsonl'
    header = args.mpfr_include / 'mpfr.h'
    wrapper_before = identity(__file__)

    def run(command):
        remaining = CPU_CAP - (child_cpu() - initial_cpu)
        if remaining < 2:
            raise RuntimeError('total child CPU cap before subprocess')
        before = child_cpu()
        proc = subprocess.run(command, capture_output=True, text=True,
                              preexec_fn=limits(remaining))
        used = child_cpu() - before
        if child_cpu() - initial_cpu > CPU_CAP:
            raise RuntimeError('total child CPU cap after subprocess')
        return proc, used

    try:
        for path, expected in FROZEN.items():
            item = identity(path)
            if item['sha256'] != expected:
                raise ValueError(f'frozen source/data identity mismatch: {path}')
            frozen.append(item)
        if identity(header)['sha256'] != '588c2bd606cba060afb49cd024f9119e996089a341a99d1dc7e0367622335a13':
            raise ValueError('official MPFR header identity mismatch')
        old_paths = list(FROZEN)[-2:]
        for path, producer in zip(old_paths, [True, False]):
            outcome = dict(input=identity(path), **old_countertest(path, producer))
            countertests.append(outcome)
            print(json.dumps(dict(countertest=outcome)), flush=True)

        source_snapshot.write_bytes(source.read_bytes())
        build = ['cc', '-O2', '-std=c11', '-Wall', '-Wextra', '-Werror', '-I',
                 str(args.mpfr_include), str(source_snapshot), '-Wl,-l:libmpfr.so.6',
                 '-lgmp', '-o', str(binary)]
        for command in [build, ['cc', '--version'], ['ldd', str(binary)]]:
            proc, used = run(command)
            record = dict(command=command, returncode=proc.returncode, child_cpu_seconds=used,
                          stdout=proc.stdout, stderr=proc.stderr)
            helpers.append(record)
            if proc.returncode:
                raise RuntimeError(f'helper process failed: {command}')
        for line in helpers[-1]['stdout'].splitlines():
            part = line.split('=>', 1)[-1].strip().split()[0]
            if part.startswith('/'):
                resolved = Path(part).resolve()
                if resolved.is_file():
                    runtime.append(identity(resolved))
        with rawpath.open('x') as raw:
            for n in range(FIRST, LAST + 1):
                counters['attempted'] += 1
                command = [str(binary), str(n), str(BITS)]
                proc, used = run(command)
                row = dict(degree=n, command=command, returncode=proc.returncode,
                           child_cpu_seconds=used, stdout=proc.stdout, stderr=proc.stderr,
                           stdout_bytes=len(proc.stdout.encode()), stdout_sha256=sha_bytes(proc.stdout.encode()))
                try:
                    if proc.returncode:
                        raise RuntimeError(f'producer exited {proc.returncode}')
                    cert = json.loads(proc.stdout)
                    b, margin = endpoints(cert, n, True)
                    current_versions = {k: cert[k] for k in ('gmp_version', 'mpfr_version')}
                    versions = versions or current_versions
                    if current_versions != versions:
                        raise ValueError('runtime version changed')
                    counters['completed'] += 1
                    counters['unrun'] -= 1
                    counters['nonzero_cardinals'] += cert['nonzero_cardinals']
                    counters['zero_cardinals_omitted'] += cert['zero_cardinals_omitted']
                    native_cpu += cert['cpu_seconds_diagnostic']
                    row.update(normalized_energy_upper=str(b), exact_threshold_margin=str(margin))
                    if maximum is None or b > maximum:
                        maximum, maximum_n = b, n
                    if margin < 0:
                        counters['failed_new_threshold'] += 1
                        raise ValueError(f'new threshold failed: margin={margin}')
                    counters['passed_new_threshold'] += 1
                    row['outcome'] = 'PASS_NEW_THRESHOLD'
                except (ValueError, RuntimeError, KeyError) as exc:
                    row['outcome'] = 'STOPPED'
                    row['error'] = str(exc)
                    raw.write(json.dumps(row, sort_keys=True, separators=(',', ':')) + '\n')
                    raw.flush()
                    raise
                raw.write(json.dumps(row, sort_keys=True, separators=(',', ':')) + '\n')
                raw.flush()
        for item in frozen:
            if identity(item['path']) != item:
                raise ValueError(f'frozen input changed during run: {item["path"]}')
        if identity(__file__) != wrapper_before or identity(source_snapshot)['sha256'] != FROZEN[source]:
            raise ValueError('wrapper/compiled-source changed during run')
    except (ValueError, RuntimeError, KeyError, OSError) as exc:
        counters['arithmetic_or_process_errors'] += 1
        failure = dict(detail=str(exc), first_uncompleted_degree=FIRST + counters['completed'])

    complete = failure is None and counters['passed_new_threshold'] == 127
    helper_path = args.output_dir / 'build-runtime.json'
    helper_path.write_text(json.dumps(helpers, indent=2) + '\n')
    receipt = dict(schema='n3-bootstrap-energy-v1', rules_input_sha=INPUT_SHA,
        status='COMPLETE_PRODUCER' if complete else 'STOPPED',
        claim_status='CONDITIONAL pending distinct fresh GMP reconstruction for the new threshold',
        target='For each integer2<=n<=128: 4E<=3*n^4*ell, hence W_n<=(3/4)*n^4*Lambda_c',
        command=['python', str(Path(__file__)), '--output-dir', str(args.output_dir),
                 '--mpfr-include', str(args.mpfr_include), '--receipt', str(args.receipt)],
        range=dict(first=FIRST, last=LAST, step=1, count=127), precision_bits=BITS,
        total_child_cpu_cap_seconds=CPU_CAP, counters=counters, all_ran_and_passed=complete,
        failure=failure, old_endpoint_countertests=countertests,
        maximum_producer_normalized_energy_upper=str(maximum) if maximum is not None else None,
        maximum_degree=maximum_n,
        gap_below_three_quarters=str(Q(3, 4) - maximum) if maximum is not None else None,
        maximum_decimal_diagnostic=float(maximum) if maximum is not None else None,
        exact_n2_controls=dict(corner='3', energy='331/18'),
        total_child_cpu_seconds=child_cpu() - initial_cpu,
        summed_native_cpu_seconds_diagnostic=native_cpu,
        wall_seconds=time.monotonic() - started, start_utc=start_utc,
        stop_utc=datetime.now(timezone.utc).isoformat(),
        wrapper=wrapper_before, frozen_inputs=frozen, official_mpfr_header=identity(header),
        compiled_source=identity(source_snapshot) if source_snapshot.exists() else None,
        binary=identity(binary) if binary.exists() else None,
        compiler_binary=identity(Path(shutil.which('cc')).resolve()),
        build_command=helpers[0]['command'] if helpers else None,
        producer_argv_template=[str(binary), '{n=2..128}', str(BITS)],
        runtime_versions=versions, linked_runtime_libraries=runtime,
        build_runtime_output=identity(helper_path),
        bulk_raw_output=identity(rawpath) if rawpath.exists() else None,
        python=platform.python_version(), platform=platform.platform(),
        independent_new_threshold_reconstruction='PENDING; old kappa replay does not discharge it',
        scope='Finite energy helper only; no all-n energy, pointwise patch predicate, global degree, phase rerun or cost-law claim',
        storage='Original per-degree stdout/CPU/hash/count/margin retained in local JSONL; only this aggregate receipt essential',
        model='Codex developer, parent allocation inherited; serving model/effort metadata unexposed')
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_text(json.dumps(receipt, indent=2) + '\n')
    if args.receipt.stat().st_size >= 16384:
        raise RuntimeError('aggregate receipt exceeds predeclared16KiB limit')
    print(json.dumps(dict(receipt=identity(args.receipt), all_ran_and_passed=complete,
        counters=counters, maximum_degree=maximum_n,
        maximum_normalized_energy_upper=receipt['maximum_producer_normalized_energy_upper'],
        total_child_cpu_seconds=receipt['total_child_cpu_seconds'], failure=failure)), flush=True)
    return 0 if complete else 1


if __name__ == '__main__':
    sys.exit(main())
