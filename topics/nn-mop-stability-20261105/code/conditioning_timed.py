#!/usr/bin/env python3
"""Run one derivative command, retaining wall/CPU/RSS when GNU time is absent."""
import json
from pathlib import Path
import resource
import runpy
import sys
import time

receipt, script, *arguments = sys.argv[1:]
start = time.monotonic()
before = resource.getrusage(resource.RUSAGE_SELF)
status = 0
try:
    sys.argv = [script]+arguments
    runpy.run_path(script,run_name='__main__')
except SystemExit as exc:
    status = exc.code or 0
    raise
except BaseException:
    status = 1
    raise
finally:
    after = resource.getrusage(resource.RUSAGE_SELF)
    Path(receipt).write_text(json.dumps(dict(wall_seconds=time.monotonic()-start,
                            user_seconds=after.ru_utime-before.ru_utime,
                            system_seconds=after.ru_stime-before.ru_stime,
                            max_rss_kib=after.ru_maxrss,exit=status),sort_keys=True)+'\n')
