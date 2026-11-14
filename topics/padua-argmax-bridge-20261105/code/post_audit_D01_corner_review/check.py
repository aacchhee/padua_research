"""Independent bounded D01 corner review; no production runner invocation.

Fresh output directory, existing degrees only, 20 aggregate CPU-second cap.
Floating checks are measurements. The Fraction checks support the written proof.
"""
import hashlib
import json
import math
import pathlib
import resource
import shutil
import subprocess
import sys
from fractions import Fraction as F

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
TOPIC = HERE.parents[1]
SOURCE = HERE.parent / 'post_audit_D01_corner'
OUT = ROOT / 'local-output/argmax-bridge-20261105/post-audit-D01/corner-review'
OUT.mkdir(parents=True, exist_ok=False)

def cpu():
    return sum(resource.getrusage(k).ru_utime + resource.getrusage(k).ru_stime
               for k in (resource.RUSAGE_SELF, resource.RUSAGE_CHILDREN))

def identity(path):
    p = pathlib.Path(path).resolve()
    return dict(path=str(p), bytes=p.stat().st_size,
                sha256=hashlib.sha256(p.read_bytes()).hexdigest())

commands = []
def run(args, label):
    remaining = math.floor(19 - cpu())
    assert remaining >= 1, 'review CPU reserve exhausted'
    def limit():
        resource.setrlimit(resource.RLIMIT_CPU, (remaining, remaining))
    before = cpu()
    p = subprocess.run(list(map(str, args)), capture_output=True,
                       preexec_fn=limit, timeout=30)
    stdout, stderr = OUT / (label + '.stdout'), OUT / (label + '.stderr')
    stdout.write_bytes(p.stdout)
    stderr.write_bytes(p.stderr)
    commands.append(dict(args=list(map(str, args)), exit=p.returncode,
                         cpu_seconds=cpu()-before,
                         stdout=identity(stdout), stderr=identity(stderr)))
    assert p.returncode == 0
    return p.stdout

def independent_board(n, exact=False):
    """Enumerate by physical rows, with rational common-denominator g.

    Do not use production term(), diagonal ranges, B20/C20 grouping or run.py.
    Rowwise fsum limits floating summation error in the nonexact controls.
    """
    total = [[] for _ in range(6)]
    count = 0
    for j in range(n+1):
        rows = [[] for _ in range(6)]
        for r in range((j+1) % 2, n+2, 2):
            if r-j == 1 and j >= (n+1)//2:
                continue
            s = F(6*(j+r)-1, 6) if exact else j+r-1/6
            g_num = 6*abs((n+1)*j-n*r)-n
            g = F(g_num, 6*n) if exact else g_num/(6*n)
            d = F(6*(2*n+1-j-r)-1, 6) if exact else 2*n+1-j-r-1/6
            assert s > 0 and g > 0 and d > 0
            values = (1/(s*g**3), 1/(s**3*g), 1/(s*s*g*g),
                      1/(g*g), 1/(s*s), 1/(d*d))
            for dest, v in zip(rows, values):
                dest.append(v)
            count += 1
        for dest, row in zip(total, rows):
            dest.append(sum(row, F(0)) if exact else math.fsum(row))
    return [sum(x, F(0)) if exact else math.fsum(x) for x in total], count

def budget(row, upper):
    n = row['n']; m = n+1
    xs = [v + (t if upper else 0) for v,t in zip(row['sums_low'], row['tail_upper'])]
    a1,a2,a3,g2 = xs
    regular = (m/n)**3*(16*a1/math.pi**4 + 4*(a2+a3)/math.pi**2)
    h = 1+math.log(2*m)
    rem = 30*m*m/(math.pi**2*n**3) + 18*m*h/(25*n**3) + 3456*m*h/(25*math.pi**2*n**3) + 8/(n*m)
    sine = m/n**2*(50*g2/(9*math.pi**2)+(row['B20']+row['C20'])/2)
    strip = 28*(n//2+0.25)/(5*m)
    return regular+rem+sine+strip-math.log(m)/3

compiler = pathlib.Path(shutil.which('g++')).resolve()
version = run([compiler, '--version'], 'compiler-version').decode().splitlines()[0]
binary = OUT / 'measure-fresh'
run([compiler, '-O2', '-std=c++17', '-fno-fast-math', SOURCE/'measure.cpp', '-o', binary], 'build')
rows = {}
for n,mode in [(17,1),(1000,1),(1001,1),(1000,0),(1001,0),(10000,0),(10001,0),(20000,0),(20001,0)]:
    rows[(n,mode)] = json.loads(run([binary,n,127,mode], f'n{n}-mode{mode}'))

controls = []
for n in (17,1000,1001):
    values, count = independent_board(n, exact=n==17)
    ref = rows[(n,1)]
    native = ref['sums_low']+[ref['B20'],ref['C20']]
    relative = [abs(float(a)-b)/max(1,abs(float(a))) for a,b in zip(values,native)]
    assert count == ref['board'] and max(relative) < 2e-14
    controls.append(dict(n=n, exact=n==17, board=count,
                         max_relative_difference=max(relative)))
    if n > 17:
        tr = rows[(n,0)]
        assert tr['board'] == count
        assert all(a-1e-12 <= v <= a+t+1e-12 for v,a,t in zip(values,tr['sums_low'],tr['tail_upper']))
        assert all(abs(float(v)-b) < 1e-11 for v,b in zip(values[4:],(tr['B20'],tr['C20'])))

old = json.loads((TOPIC/'evidence/d01-corner.json').read_text())
oldrows = {x['n']:x for x in old['rows']}
summary = []
for (n,mode),row in rows.items():
    if mode:
        continue
    low, high = budget(row,False), budget(row,True)
    assert abs(low-oldrows[n]['envelope']['low']['K']) < 1e-12
    assert abs(high-oldrows[n]['envelope']['upper']['K']) < 1e-12
    summary.append(dict(n=n, K_low=low, K_upper=high, board=row['board']))
assert budget(rows[(1000,0)],False)>4
assert budget(rows[(10000,0)],False)>7.8
kill = math.log(20001)**2/10-math.log(20001)/3
assert budget(rows[(20000,0)],False)>kill

# Exact proof arithmetic; it is independent of the measured envelope.
exp7 = sum((F(7)**k/math.factorial(k) for k in range(12)),F(0))
strip = F(28,5)*F(2001,4)/1001
bound = F(96,25)+F(279,100)-F(7,3)
assert F(25,21)**4 > 2 and exp7 > 1001
assert strip > F(279,100) and bound == F(1289,300) and bound>4
assert F(5,6)+F(1,1000) < F(21,25)

# Verify retained original provenance identities, not merely names.
verified = set()
def verify_records(obj):
    if isinstance(obj,dict):
        if {'path','bytes','sha256'} <= obj.keys():
            actual = identity(obj['path'])
            assert actual['bytes']==obj['bytes'] and actual['sha256']==obj['sha256'], obj['path']
            verified.add(str(actual['path']))
        for v in obj.values():
            verify_records(v)
    elif isinstance(obj,list):
        for v in obj:
            verify_records(v)
verify_records(old)
original_manifest = json.loads(pathlib.Path(old['manifest']['path']).read_text())
verify_records(original_manifest)
closure = json.loads(pathlib.Path(old['postrun_build_closure']['path']).read_text())
verify_records(closure)

receipt = dict(status='PASS', scope='Supplementary measured review; exact analytic obstruction reconstructed separately',
    rules_head='e6549177fe48c7fea8436cece8a04b411dc544e1',
    requested_model='gpt-6-astra high', serving_metadata='unexposed',
    sources=[identity(__file__),identity(SOURCE/'measure.cpp'),identity(SOURCE/'run.py')],
    compiler=identity(compiler), compiler_version=version, binary=identity(binary),
    original_receipt=identity(TOPIC/'evidence/d01-corner.json'),
    controls=controls, measurements=summary, kill_threshold_n20000=kill,
    exact_scalar_checks=dict(exp7_partial_sum=str(exp7),strip=str(strip),lower_bound=str(bound)),
    original_provenance_files_verified=len(verified),
    original_build_dependencies=len(closure['header_dependencies']),
    cpu_seconds_through_checks=cpu(), cpu_cap=20,
    limitations=['No directed rounding; no actual-Hessian or optimal-constant assertion',
                 'Original 100000/100001 rows inspected, not rerun',
                 'Shell-observed original 2.644 CPU seconds is recorded history, not reproduced'],
    commands=commands)
assert cpu()<20
target = TOPIC/'evidence/d01-review-corner.json'
target.write_text(json.dumps(receipt,indent=2)+'\n')
assert target.stat().st_size<16384
print(json.dumps({'status':'PASS','cpu_seconds_through_checks':cpu(),
                  'receipt':identity(target),'controls':controls,'measurements':summary}))
