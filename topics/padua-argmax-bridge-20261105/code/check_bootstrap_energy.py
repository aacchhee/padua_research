"""Fresh independent GMP bounds and exact bootstrap-energy predicate, n=2..128.

Build with --build, then run once with --run. No producer data/module imported.
"""
import argparse
import datetime
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform
import resource
import subprocess
import time

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / 'topics/padua-argmax-bridge-20261105'
LOCAL = ROOT / 'local-output/argmax-bridge-20261105/check-bootstrap'
SOURCE = TOPIC / 'code/check_corner_exact.cpp'
SOURCE_SHA = '3646f4e8b6b16957b9e1114f95ad2f0a7c18eec4687b49d5e6f1947a25eea6e3'
HEAD = '88e702321cd5d9c3395a551fc8a55a2f7cb8bc10'


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path, data):
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + '\n')


def pin():
    require(sha(SOURCE) == SOURCE_SHA, 'frozen independent arithmetic source changed')


def execute(argv, remaining=1200):
    def limit():
        seconds = max(1, int(remaining))
        resource.setrlimit(resource.RLIMIT_CPU, (seconds, seconds))
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    start = time.monotonic()
    p = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True, preexec_fn=limit)
    wall = time.monotonic() - start
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    user = after.ru_utime - before.ru_utime
    system = after.ru_stime - before.ru_stime
    return p, dict(argv=argv, exit_status=p.returncode, wall_seconds=wall,
                   user_seconds=user, system_seconds=system, cpu_seconds=user+system)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--build', action='store_true')
    group.add_argument('--run', action='store_true')
    args = parser.parse_args()
    LOCAL.mkdir(parents=True, exist_ok=True)
    binary = LOCAL / 'corner-exact'
    pin()
    if args.build:
        require(not binary.exists(), 'fresh binary destination required')
        historical = subprocess.check_output(['git', 'show', f'{HEAD}:{SOURCE.relative_to(ROOT)}'], cwd=ROOT)
        require(hashlib.sha256(historical).hexdigest() == SOURCE_SHA, 'source differs from published input')
        argv = ['g++', '-O3', '-std=c++17', str(SOURCE), '-lgmpxx', '-lgmp', '-o', str(binary)]
        p, result = execute(argv)
        (LOCAL/'compile.stdout').write_text(p.stdout)
        (LOCAL/'compile.stderr').write_text(p.stderr)
        require(p.returncode == 0, 'compilation failed')
        pin()
        result.update(binary_sha256=sha(binary), source_sha256=SOURCE_SHA,
                      python=platform.python_version(),
                      compiler=subprocess.check_output(['g++', '--version'], text=True).splitlines()[0],
                      gmp_package=subprocess.check_output(['dpkg-query','-W','-f=${Version}','libgmp-dev'], text=True))
        write(LOCAL/'build.json', result)
        print(json.dumps(result, sort_keys=True))
        return
    receipt = TOPIC/'evidence/independent-bootstrap-energy.json'
    require(not receipt.exists() and not (LOCAL/'n2.json').exists(), 'refuse duplicate sweep')
    build = json.loads((LOCAL/'build.json').read_text())
    require(sha(binary) == build['binary_sha256'], 'binary changed after fresh compile')
    started_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
    started = time.monotonic()
    cpu = build['cpu_seconds']
    rows = []
    worst = (F(0), None)
    n2 = None
    for n in range(2,129):
        pin()
        require(cpu < 1200, 'aggregate child CPU cap exhausted')
        p, execution = execute([str(binary), str(n)], 1200-cpu)
        cpu += execution['cpu_seconds']
        output = LOCAL/f'n{n}.json'
        output.write_text(p.stdout)
        (LOCAL/f'n{n}.stderr').write_text(p.stderr)
        write(LOCAL/f'n{n}-execution.json', execution)
        require(p.returncode == 0, f'n{n}: native process failure')
        require(cpu < 1200, 'aggregate child CPU cap exceeded')
        data = json.loads(p.stdout)
        require(type(data['degree']) is int and data['degree'] == n, 'degree mismatch')
        require(data['precision_bits'] == 512, 'precision mismatch')
        require(data['zero_cardinals_omitted'] == n//2, 'zero mask count')
        require(data['nonzero_cardinals'] + data['zero_cardinals_omitted'] == (n+1)*(n+2)//2,
                'full cardinal count')
        ell, upper = F(data['corner_lower']), F(data['corner_upper'])
        lower_energy, energy = F(data['energy_lower']), F(data['energy_upper'])
        require(0 < ell <= upper and 0 <= lower_energy <= energy, 'invalid bound ordering')
        # New exact predicate, independently evaluated from this fresh reconstruction.
        require(4*energy <= 3*n**4*ell, f'n{n}: bootstrap energy threshold failed')
        ratio = energy/(n**4*ell)
        if ratio > worst[0]:
            worst = ratio, n
        if n == 2:
            require(ell <= 3 <= upper and lower_energy <= F(331,18) <= energy,
                    'n2 exact control not enclosed')
            n2 = dict(corner_exact='3', energy_exact='331/18', both_enclosed=True,
                      zero_cardinals_omitted=data['zero_cardinals_omitted'],
                      nonzero_cardinals=data['nonzero_cardinals'])
        rows.append(dict(degree=n, execution=execution, raw_sha256=sha(output), raw_bytes=output.stat().st_size,
                         normalized_energy_upper=str(ratio), exact_predicate=True))
    pin()
    require(sha(binary) == build['binary_sha256'], 'binary changed during sweep')
    require([r['degree'] for r in rows] == list(range(2,129)), 'not every integer checked')
    raw = LOCAL/'executions.json'
    write(raw, rows)
    result = dict(format='padua-independent-bootstrap-energy-v1', accepted=True,
                  input_head=HEAD, started_utc=started_utc, cwd=str(ROOT),
                  independent_execution=True, producer_endpoints_imported=False,
                  predicate='4*energy_upper <= 3*n^4*corner_lower',
                  every_integer_degree_checked=True, degree_first=2, degree_last=128, degree_count=len(rows),
                  all_native_exit_statuses_zero=True, all_new_predicates_passed=True,
                  all_masks_cardinal_counts_and_positive_denominators_verified=True,
                  arithmetic='GMP exact integers/rationals; outward 512-bit fixed-point intervals; Python Fraction comparison',
                  n2_control=n2, worst_normalized_energy_degree=worst[1],
                  worst_normalized_energy_upper=str(worst[0]), normalized_threshold='3/4',
                  total_child_cpu_including_build_seconds=cpu, cpu_limit_seconds=1200,
                  sweep_child_cpu_seconds=sum(r['execution']['cpu_seconds'] for r in rows),
                  sweep_wall_seconds=time.monotonic()-started,
                  cpu_accounting='sum of RUSAGE_CHILDREN user+system deltas for each actual subprocess',
                  actual_argv_template=[str(binary), '{n}'], raw_execution_manifest=str(raw.relative_to(ROOT)),
                  raw_execution_manifest_sha256=sha(raw), raw_execution_manifest_bytes=raw.stat().st_size,
                  build=build, runner_sha256=sha(Path(__file__)), source_sha256=SOURCE_SHA,
                  trusted_dependencies=['PD-T101','PD-T227','frozen check_corner_exact.cpp','GMP','compiler','Python','hardware'],
                  scope='finite energy bound n=2..128 only; no all-degree energy or complement coverage')
    write(receipt, result)
    require(receipt.stat().st_size < 16384, 'receipt exceeds normal size limit')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
