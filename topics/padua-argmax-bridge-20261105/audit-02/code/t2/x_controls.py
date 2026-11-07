"""Auditor-owned synthetic controls (NO_SCIENCE). Uses copied pack + fake worker only."""
import importlib, json, os, resource, shutil, signal, sys, time
from pathlib import Path
TREE = Path(sys.argv[1]).resolve(); OUT = Path(sys.argv[2]).resolve(); WHICH = sys.argv[3]
T = 'topics/padua-argmax-bridge-20261105'
HARNESS = TREE / T / 'code/final_pack_ops_review'; SOURCE = TREE / T / 'syvert2_pack'
sys.path.insert(0, str(HARNESS))
rc3 = importlib.import_module('review_controls_03')
resource.setrlimit(resource.RLIMIT_CPU, (60, 60)); signal.alarm(120)
OUT.mkdir(parents=True, exist_ok=False)
def j(p): return json.loads(Path(p).read_bytes())
def setup(name, degrees):
    path = OUT / name; m = rc3.package(path, SOURCE)
    server, evidence, verify, common = rc3.load_ops(path)
    p = dict(server.plan('all'), degrees=degrees); server.plan = lambda group: p
    rc3.put(path / 'plan.json', {'all': p})
    return path, m, server, evidence, verify, common, p
res = {}
if WHICH in ('sigchld_dfl', 'sigchld_ign'):
    path, m, server, *_ = setup(WHICH, [41, 42])
    os.environ['FIXTURE_MODE'] = 'failure'   # fake n=41 exits 7 after 0.15 s; n=42 exits 0 after 5 s
    server.PROFILE = dict(server.PROFILE, case_wall_seconds=10)
    if WHICH == 'sigchld_ign': signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    try: server.run('all', 2, False); res['run'] = 'returned normally'
    except BaseException as e: res['run'] = 'raised ' + repr(e)
    for n in (41, 42):
        res['wrapper-exit-%d' % n] = j(path / 'outputs/all/jobs' / str(n) / 'wrapper-exit.json')
    s = j(path / 'outputs/all/summary.json')
    res['summary'] = {k: s.get(k) for k in ('first_failure', 'quiescent', 'ECHILD', 'never_started', 'cleanup_killed')}
elif WHICH == 'reboot':
    path, m, server, evidence, verify, common, p = setup(WHICH, [41])
    server.run('all', 1, False)   # fake success worker writes synthetic attempt
    s = j(path / 'outputs/all/summary.json'); res['summary_quiescent'] = [s['quiescent'], s['ECHILD'], s['first_failure']]
    server.PROFILE = dict(server.PROFILE, archive_free_floor_bytes=0)
    own = importlib.import_module('ownership')
    real = own.boot_id
    own.boot_id = lambda: '11111111-2222-3333-4444-555555555555'   # simulate a host reboot
    try: server.collect(OUT / 'reboot-collect'); res['collect_after_reboot'] = 'ACCEPTED'
    except BaseException as e: res['collect_after_reboot'] = 'refused ' + repr(e)
    own.boot_id = real
    res['collect_same_boot'] = str(server.collect(OUT / 'sameboot-collect').name)
elif WHICH == 'delete_resume':
    path, m, server, evidence, verify, common, p = setup(WHICH, [41, 42, 43])
    os.environ['FIXTURE_MODE'] = 'failure'
    server.PROFILE = dict(server.PROFILE, case_wall_seconds=10)
    try: server.run('all', 2, False)
    except BaseException as e: res['first_run'] = repr(e)
    res['first_summary_first_failure'] = j(path / 'outputs/all/summary.json')['first_failure']
    res['first_jobs'] = sorted(x.name for x in (path / 'outputs/all/jobs').iterdir())
    try: server.run('all', 2, True); res['resume_with_failed_dirs'] = 'ACCEPTED'
    except BaseException as e: res['resume_with_failed_dirs'] = 'refused ' + repr(e)[:120]
    for d in (path / 'outputs/all/jobs').iterdir(): shutil.rmtree(d)   # out-of-protocol external deletion
    os.environ.pop('FIXTURE_MODE')
    try: server.run('all', 2, True); res['resume_after_deletion'] = 'ACCEPTED'
    except BaseException as e: res['resume_after_deletion'] = 'refused ' + repr(e)[:160]
    s = j(path / 'outputs/all/summary.json')
    res['final_summary'] = {k: s.get(k) for k in ('first_failure', 'quiescent', 'ECHILD', 'never_started')}
    res['outputs_all_files'] = sorted(x.name for x in (path / 'outputs/all').iterdir())
    access = evidence.Access(path, str(path)); run = j(path / 'outputs/all/run.json')
    res['validate_attempts'] = [evidence.validate_attempt(access, 'all', n, run) for n in (41, 42, 43)]
elif WHICH == 'sighup':
    path, m, server, *_ = setup(WHICH, [41])
    own = importlib.import_module('ownership'); own.subreaper()
    os.environ['FIXTURE_MODE'] = 'writer'
    pid = os.fork()
    if pid == 0:
        try: server.run('all', 1, False)
        except BaseException: os._exit(9)
        os._exit(0)
    deadline = time.monotonic() + 5
    while not (path / 'outputs/all/jobs/41/live-marker').exists():
        assert time.monotonic() < deadline; time.sleep(.02)
    os.kill(pid, signal.SIGHUP); _, status = os.waitpid(pid, 0)
    res['supervisor_status'] = {'signaled': os.WIFSIGNALED(status), 'sig': os.WTERMSIG(status) if os.WIFSIGNALED(status) else None}
    s = j(path / 'outputs/all/summary.json'); res['summary_after_sighup'] = [s.get('quiescent'), s.get('ECHILD'), s.get('phase')]
    res['orphan_worker_alive'] = bool(own.descendants())
    res['cleanup_killed'] = own.cleanup()
print(json.dumps(res, indent=1, default=str))
(OUT / 'result.json').write_text(json.dumps(res, indent=1, default=str))
