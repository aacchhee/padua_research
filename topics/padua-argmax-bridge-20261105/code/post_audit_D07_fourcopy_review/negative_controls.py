"""Independent D07 controller-only negative checks; no native library load.

Preregistered scope: frozen AST-selected functions, stubbed platform/syscall
failures and incomplete reaping, actual nested call ledger control flow.
No compiler, subprocess, native point/root/reference or numerical call.
Aggregate CPU cap 10 seconds. Print a small receipt to stdout.
"""
import ast
import copy
import hashlib
import json
import pathlib
import resource
import textwrap
from types import SimpleNamespace as NS

resource.setrlimit(resource.RLIMIT_CPU, (9, 10))
source_path = pathlib.Path(__file__).resolve().parents[1] / 'post_audit_D07_fourcopy_point/controller.py'
raw = source_path.read_bytes()
expected = 'af8d357badba85786fec088c735cc988f0950587d112e2e63a8d5b39cc14a9a5'
assert hashlib.sha256(raw).hexdigest() == expected
source = raw.decode()
tree = ast.parse(source)
chosen = ['enable_subreaper', 'reap_descendants', 'commit_call']
nodes = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in chosen]
worker = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == 'worker')
nodes.append(next(node for node in worker.body if isinstance(node, ast.FunctionDef) and node.name == 'call'))
program = '\n\n'.join(textwrap.dedent(ast.get_source_segment(source, node)) for node in nodes)
checks = []
ns = dict(sys=NS(platform='non-linux'), ctypes=None)
exec(compile(program, '<frozen-controller-AST>', 'exec'), ns)

try:
    ns['enable_subreaper']()
    raise AssertionError('unsupported platform accepted')
except RuntimeError:
    checks.append('unsupported platform rejected before loading libc')

class Prctl:
    def __init__(self, set_status):
        self.set_status = set_status
    def __call__(self, option, *args):
        return self.set_status if option == 36 else 0

for set_status, kind in [(-1, OSError), (0, RuntimeError)]:
    ns['sys'] = NS(platform='linux')
    ns['ctypes'] = NS(CDLL=lambda *a, **k: NS(prctl=Prctl(set_status)),
                      c_int=lambda: NS(value=0), c_ulong=int,
                      get_errno=lambda: 1, addressof=lambda flag: 123)
    try:
        ns['enable_subreaper']()
        raise AssertionError('subreaper failure accepted')
    except kind:
        checks.append('subreaper set failure rejected' if set_status else 'subreaper verification failure rejected')

ns['signal'] = NS(SIGKILL=9)
for events, times, complete, expected_count in [
    (['nochild'], [0], True, 0),
    ([(73, 9, NS(ru_utime=.2, ru_stime=.03)), 'nochild'], [0], True, 1),
    ([(0, 0, None)], [0, 6], False, 0),
]:
    queue = iter(events)
    clock = iter(times)
    kills = []
    def wait4(*args):
        value = next(queue)
        if value == 'nochild':
            raise ChildProcessError
        return value
    ns['os'] = NS(killpg=lambda *a: kills.append(a), wait4=wait4, WNOHANG=1)
    ns['time'] = NS(monotonic=lambda: next(clock), sleep=lambda delay: None)
    result = ns['reap_descendants'](71)
    assert result['complete'] is complete and len(result['reaped']) == expected_count
    assert kills == [(71, 9)]
    if not complete:
        assert 'lower bound' in result['reason']
    checks.append('reap scenario complete=' + str(complete) + ' count=' + str(expected_count))

case = dict(n=32, reference=True)
later = dict(n=512, reference=False)
def fresh():
    return dict(completed_calls=[], point_results=[], pending=[case, later], active_call=None)

state = fresh()
before = copy.deepcopy(state)
try:
    ns['commit_call'](state, dict(label='bad'), later)
    raise AssertionError('out-of-order case committed')
except RuntimeError:
    assert state == before
    checks.append('case ledger mismatch rejected without mutation')

class CostStop(Exception):
    pass
ns.update(CostStop=CostStop, SINGLE_SOFT=20)
state = fresh()
snapshots = []
clock = iter([1., 2., 24.])
ns.update(state=state, cpu=lambda: next(clock), checkpoint=lambda: snapshots.append(copy.deepcopy(state)))
try:
    ns['call']('slow-reference', lambda: dict(enclosure=[1., 2.], reference_enclosure=[1.2, 1.3]), case=case)
    raise AssertionError('slow completed call did not stop')
except CostStop:
    assert state['pending'] == [later] and state['active_call'] is None
    assert state['status'] == 'SINGLE_CALL_COST_STOP'
    assert len(state['completed_calls']) == len(state['point_results']) == 1
    assert state['point_results'][0]['point_output_complete']
    assert state['point_results'][0]['reference_output_complete']
    assert snapshots[1]['pending'] == [later] and 'status' not in snapshots[1]
    assert snapshots[0]['active_call']['stage'] == 'combined point+reference; no intermediate point output exposed'
    checks.append('actual call branch durably commits both outputs before completed-cost stop')

state = fresh()
clock = iter([1., 2., 3.])
ns.update(state=state, cpu=lambda: next(clock), checkpoint=lambda: None)
def fail():
    raise ValueError('simulated native/reference failure')
try:
    ns['call']('failed-reference', fail, case=case)
    raise AssertionError('failed call accepted')
except ValueError:
    assert not state['completed_calls'] and not state['point_results']
    assert state['pending'] == [case, later] and state['active_call'] is not None
    assert 'simulated native/reference failure' in state['first_exception']['error']
    checks.append('failed combined call remains uncomputed with first exception')

assert hashlib.sha256(source_path.read_bytes()).hexdigest() == expected
cpu = sum(resource.getrusage(kind).ru_utime + resource.getrusage(kind).ru_stime
          for kind in (resource.RUSAGE_SELF, resource.RUSAGE_CHILDREN))
assert cpu < 10
print(json.dumps(dict(status='PASS', controller_sha256=expected,
    helper_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
    checks=checks, total_self_and_children_CPU_seconds=cpu,
    scope='Pure Python negative/controller-flow checks; stubs only, no native/library/build/subprocess/numerical execution'), indent=2))
