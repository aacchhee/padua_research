"""New paper-supporting campaign; unchanged original runner and frozen engine.

prepare is data-only. Native actions require the orchestrator's freeze commit.
All writes are exclusive; no retry, rescue, pruning, or resume is implemented.
"""
import argparse
import os
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parents[1]
sys.path.insert(0, str(TOPIC / 'code/local_onset512_campaign'))
import runner as R

OUTPUT = R.ROOT / 'local-output/argmax-bridge-20261105/regeneration-20261114'
CONTROL = OUTPUT.parent / 'regeneration-20261114-controls'
SNAPSHOT = HERE / 'frozen-inputs.json'
INPUT_HEAD = 'cc2f9ad'  # Expanded full SHA supplied by prepare; no Git operation here.
RUNNER_SHA = 'a198b65182590be13cb91110ff976d90e7e885c778180e59699fbe9b067ccdad'
HELPERS = ('common.py', 'evidence.py', 'ownership.py', 'plans.py', 'process_guard.py', 'storage.py')


def prepare(head):
    R.require(len(head) == 40 and head.startswith(INPUT_HEAD), 'assigned full input SHA')
    R.require(R.identity(R.__file__)['sha256'] == RUNNER_SHA, 'unchanged campaign runner')
    release_zip = Path('/workspace/attachments/328eca48-8208-4df2-b3de-bb3be96e7698/padua30.zip')
    release_identity = R.identity(release_zip)
    R.require(release_identity['bytes'] == 25111335 and release_identity['sha256'] == 'aac08e5f25bd27b2710de22039efd229b4ee67d8c1e3ffef9456af200e1f74d2', 'authenticated original release ZIP')
    pin = R.pins()
    helper_rows = [R.identity(TOPIC / 'compact_pack' / name) for name in HELPERS]
    reg = {
        'format': 'paper-regeneration-20261114-v1',
        'campaign_id': 'padua-argmax-paper-regeneration-20261114',
        'input_head': head, 'rules_head': head,
        'created_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        'degrees': list(range(320, 511)), 'passes': ['produce', 'verify'],
        'workers': 4, 'pilot': 320, 'remaining': list(range(321, 511)),
        'pins': pin, 'runner': R.identity(R.__file__),
        'campaign_wrapper': R.identity(__file__), 'helper_sources': helper_rows,
        'compact_evidence': R.identity(TOPIC / 'compact_pack/evidence.py'),
        'authenticated_release_archive': release_identity,
        'trusted_manifest': R.identity(R.RELEASE / 'runtime_manifest.json'),
        'python': R.identity(sys.executable), 'output': str(OUTPUT),
        'controls_output': str(CONTROL),
        'caps': {'pass_cpu': 120, 'pass_wall': 1050, 'case_cpu': 260, 'case_AS': 2*1024**3},
        'policy': 'exactly once, primary then fresh per n; actual n320 pilot, then321..510; stop admitting on first failure; active cases finish; no retry/rescue/resume',
        'validation': 'unchanged full compact validate_pass before byte-preserving immutable hardlink dedup; exact primary/fresh fields; observed wait4 exits and ECHILD',
        'retention': 'Preserve every raw history, receipt, stdout/stderr, native source/TU/binary/dependency and summary. No pruning. Full delivery archive and inventory follow completion.',
        'scope': 'Regenerated paper-supporting finite evidence; pending independent I25 and audit. Historical archive identity is not a target.',
        'environment': {'affinity': sorted(os.sched_getaffinity(0)),
            'selected_cores': sorted(os.sched_getaffinity(0))[:4],
            'cpu_max': Path('/sys/fs/cgroup/cpu.max').read_text(),
            'memory_max': Path('/sys/fs/cgroup/memory.max').read_text(),
            'platform': list(os.uname()), 'python': sys.version},
    }
    OUTPUT.mkdir(exist_ok=False); (OUTPUT / 'jobs').mkdir()
    R.save(OUTPUT / 'preregistration.json', reg)
    R.save(SNAPSHOT, {'format': 'paper-regeneration-freeze-v1',
        'preregistration': R.identity(OUTPUT / 'preregistration.json'),
        'runner': reg['runner'], 'campaign_wrapper': reg['campaign_wrapper'],
        'input_head': head, 'rules_head': head})
    print(R.identity(SNAPSHOT))


def checked():
    frozen = R.read(SNAPSHOT)
    R.require(R.identity(OUTPUT / 'preregistration.json') == frozen['preregistration'], 'committed machine preregistration identity')
    reg = R.read(OUTPUT / 'preregistration.json')
    R.require(reg['runner'] == frozen['runner'] and reg['campaign_wrapper'] == frozen['campaign_wrapper'], 'freeze code identities')
    for key, path in [('runner', R.__file__), ('campaign_wrapper', __file__), ('python', sys.executable),
                      ('trusted_manifest', R.RELEASE / 'runtime_manifest.json')]:
        R.require(R.identity(path) == reg[key], 'preregistered ' + key)
    for row in reg['helper_sources']:
        R.require(R.identity(row['path']) == row, 'preregistered helper ' + row['path'])
    R.require(R.pins() == reg['pins'], 'preregistered engine/arithmetic')
    R.require(sorted(os.sched_getaffinity(0))[:4] == reg['environment']['selected_cores'], 'preregistered worker cores')
    return reg


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('action', choices=['prepare', 'controls', 'pilot', 'remaining'])
    ap.add_argument('--input-head')
    args = ap.parse_args()
    if args.action == 'prepare': prepare(args.input_head)
    else:
        checked()
        if args.action == 'controls': R.controls(CONTROL)
        else:
            R.require(R.read(CONTROL / 'controls.json')['ignored_SIGCHLD_refused'] is True, 'operational controls completed')
            R.run(OUTPUT, args.action)
