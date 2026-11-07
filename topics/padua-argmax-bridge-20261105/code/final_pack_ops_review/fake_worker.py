"""Bounded operational worker, never executes scientific code."""
import argparse
import os
from pathlib import Path
import resource
import signal
import sys
import time
sys.path.insert(0, str(Path(__file__).resolve().parent))
from fixture import make_attempt
import json
resource.setrlimit(resource.RLIMIT_AS, (128 * 1024**2, 128 * 1024**2))
resource.setrlimit(resource.RLIMIT_CPU, (10, 10))
ap = argparse.ArgumentParser(); ap.add_argument('--n', type=int); ap.add_argument('--directory'); ap.add_argument('--core', type=int)
a = ap.parse_args(); os.sched_setaffinity(0, {a.core})
mode = os.environ.get('FIXTURE_MODE', 'success')
if mode == 'failure':
    if a.n == 41: time.sleep(.15); sys.exit(7)
    time.sleep(5); sys.exit(0)
if mode == 'timeout':
    signal.signal(signal.SIGTERM, signal.SIG_IGN)
    if a.n == 41: time.sleep(25)
    else: time.sleep(.25)
    sys.exit(0)
if mode == 'writer':
    signal.signal(signal.SIGTERM, signal.SIG_IGN)
    Path(a.directory, 'live-marker').write_text(str(os.getpid()))
    time.sleep(25); sys.exit(0)
directory = Path(a.directory); group = directory.parent.parent.name
run = json.loads((directory.parent.parent / 'run.json').read_bytes())
make_attempt(Path(__file__).parent, group, a.n, run, started=False)
# Scheduler owns its direct wrapper EXIT0 record. This synthetic helper only
# produces the pass/attempt fixture and removes its helper-generated placeholder.
(directory / 'wrapper-exit.json').unlink()
