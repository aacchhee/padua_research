#!/usr/bin/env python3
"""Rebuild frozen independent checker; reconstruct every integer n=2..128."""
from pathlib import Path
from fractions import Fraction as Q
import ctypes
import datetime
import hashlib
import json
import platform
import resource
import subprocess
import time

ROOT = Path(__file__).resolve().parents[3]
TOPIC = Path(__file__).resolve().parents[1]
OUT = ROOT / 'local-output/argmax-bridge-20261105/check-corner-range'
SOURCE = TOPIC / 'code/check_corner_exact.cpp'
BINARY = OUT / 'check_corner_exact'
BULK = OUT / 'own-n2-128.jsonl'
INPUTS = list(range(2, 129))
PINS = {
    'code/check_corner_exact.cpp': '3646f4e8b6b16957b9e1114f95ad2f0a7c18eec4687b49d5e6f1947a25eea6e3',
    'theory/N3-corner-batch.md': '41e626ef792867f56b46d82df8bcd940a4645fe948fb99aa2a0c0fa64e04a471',
    'theory/N3-corner-radius-reduction.md': '8cf89c491a4d82df81a69bd1024139d1224bd1f43fd91b1d1fe58a1dd519aee4',
    'evidence/n3-corner-batch.json': '97e20cc877ad5afd0c9dfe96c1e399a42d820b38c18626e2b69bfa54f6acfc88',
    'evidence/independent-corner-replay.json': '573afc5d5ae229b0fa1d47df9b6bf334e47e0e437288a3543826838e5403cb4b',
    'independent-checks-corner.md': 'e540a6156ea1c18e508b34fff1eddecb4652cc450b9620f54d11dd4530fdd2c8',
}

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def ident(p):
    return dict(path=str(p.relative_to(ROOT)), sha256=sha(p), bytes=p.stat().st_size)

def check_pins():
    for p, expected in PINS.items():
        assert sha(TOPIC / p) == expected, (p, 'frozen input changed')

def child_cpu():
    r = resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime + r.ru_stime

def main():
    check_pins()
    OUT.mkdir(parents=True, exist_ok=True)
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    clock0, cpu0 = time.monotonic(), child_cpu()
    build = ['g++', '-O2', '-std=c++17', '-Wall', '-Wextra', '-Werror', str(SOURCE), '-lgmpxx', '-lgmp', '-o', str(BINARY)]
    subprocess.run(build, check=True, cwd=ROOT, timeout=1200)
    passed, completed, attempted = [], [], []
    nonzero = omitted = 0
    minimum = min_degree = None
    failure = None
    # Only own outputs are opened here: producer endpoints are not inputs.
    with BULK.open('w') as bulk:
        for n in INPUTS:
            try:
                assert child_cpu() - cpu0 < 1200, 'child CPU cap reached'
                remaining = 1200 - (time.monotonic() - clock0)
                assert remaining > 0, 'additional wall cap reached'
                attempted.append(n)
                proc = subprocess.run([str(BINARY), str(n)], check=True, capture_output=True, text=True, cwd=ROOT, timeout=remaining)
                a = json.loads(proc.stdout)
                completed.append(n)
                bulk.write(json.dumps(a, separators=(',', ':')) + '\n')
                bulk.flush()
                assert a['degree'] == n and a['precision_bits'] == 512
                ell, upper, lower_E, E, u = map(Q, (a['corner_lower'], a['corner_upper'], a['energy_lower'], a['energy_upper'], a['global_norm_upper']))
                assert 0 < ell <= upper and 0 <= lower_E <= E
                c = n.bit_length()
                assert 2**(c-1) < n+1 <= 2**c
                assert u == 110*(1+c)**2
                assert 8*E + 24*u*n**4 <= 16000*n**4*ell
                kappa = min(Q(1), 1/(8*(E/(n**4*ell)+3*u/ell)))
                assert kappa == Q(a['kappa']) and kappa > Q(1,12500)
                phase = Q(1,128**2)*(1+Q(n*n,(n+1)**2))/2
                assert phase == Q(a['scaled_phase_requirement']) and phase < Q(1,16000)
                assert a['nonzero_cardinals'] == (n+1)*(n+2)//2-n//2
                assert a['zero_cardinals_omitted'] == n//2
                if n == 2:
                    assert ell <= 3 <= upper and lower_E <= Q(331,18) <= E
                nonzero += a['nonzero_cardinals']
                omitted += a['zero_cardinals_omitted']
                if minimum is None or kappa < minimum:
                    minimum, min_degree = kappa, n
                passed.append(n)
            except Exception as exc:
                failure = dict(degree=n, type=type(exc).__name__, detail=str(exc), stderr=getattr(exc,'stderr',None))
                break
    check_pins()
    assert child_cpu() - cpu0 < 1200, 'child CPU cap exceeded'
    all_pass = passed == INPUTS and failure is None
    gmp = ctypes.CDLL('libgmp.so.10')
    result = dict(
        schema='independent-corner-range-v1', status='PASS' if all_pass else 'FAIL',
        reviewer='Distinct Codex /root/check_rows; coordinator-assigned gpt-6-astra high; serving metadata not independently exposed',
        rules_read_sha='3dda890275a7599caa707b0fb8c0b6e6f6a80643',
        input_degrees=INPUTS, common_kappa='1/16000', scaled_phase_square_radius='1/128',
        stronger_unchanged_native_threshold='kappa > 1/12500', precision_bits=512,
        exact_predicate='8*E + 24*u*n**4 <= 16000*n**4*ell',
        arithmetic='Independent GMP integer dyadic intervals; exact Machin/Taylor cosine; expanded physical gradient brackets; Python Fraction assembly; no MPFR or imported producer kernel/endpoints',
        counters=dict(requested=len(INPUTS), attempted=len(attempted), completed=len(completed), passed=len(passed), failed=1 if failure else 0, unrun=len(INPUTS)-len(attempted), nonzero_cardinals=nonzero, zero_cardinals_omitted=omitted),
        all_integer_inputs_ran_and_passed=all_pass, failure=failure,
        minimum_own_kappa=str(minimum), minimum_degree=min_degree, minimum_decimal_diagnostic=float(minimum) if minimum else None,
        exact_n2_control=dict(corner='3', energy='331/18', zero_cardinals=1, checked=2 in passed),
        source=ident(SOURCE), wrapper=ident(Path(__file__).resolve()), binary=ident(BINARY),
        frozen_reference_identities=[ident(TOPIC/p) for p in PINS if p != 'code/check_corner_exact.cpp'],
        build_command=build, execution_argv_template=[str(BINARY), '{n: every input_degrees entry in ascending order}'],
        command='python topics/padua-argmax-bridge-20261105/code/check_corner_range.py',
        execution_started_utc=started, execution_finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        total_child_cpu_cap_seconds=1200, child_cpu_seconds_diagnostic=child_cpu()-cpu0, wall_seconds_diagnostic=time.monotonic()-clock0,
        compiler=subprocess.check_output(['g++','--version'],text=True).splitlines()[0],
        gmp_runtime_version=ctypes.c_char_p.in_dll(gmp,'__gmp_version').value.decode(),
        linked_runtime=subprocess.check_output(['ldd',str(BINARY)],text=True), python=platform.python_version(), platform=platform.platform(),
        bulk_own_output=ident(BULK),
        storage='One aggregate receipt; all rational endpoint rows remain local and are regenerable from integer degrees and frozen checker source',
        scope='Finite local corner patches only. No global degree certificate, B2/B3 or all-degree claim; required Claude audit remains separate.')
    target = TOPIC / 'evidence/independent-corner-range.json'
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status=result['status'],counters=result['counters'],minimum_degree=min_degree,minimum_decimal_diagnostic=result['minimum_decimal_diagnostic'],receipt=ident(target)),indent=2))
    if not all_pass:
        raise SystemExit(1)

if __name__ == '__main__':
    main()
