"""Operational child ownership only. Never infer an exit from ECHILD."""
import json
import sys
import os
import signal
import subprocess
import time


def normalize_startup():
    inherited = signal.getsignal(signal.SIGCHLD)
    signal.signal(signal.SIGCHLD, signal.SIG_DFL)
    if inherited != signal.SIG_DFL:
        sys.stderr.write(json.dumps({'event': 'SIGCHLD_STARTUP_REFUSED', 'inherited': repr(inherited), 'normalized': 'SIG_DFL', 'pid': os.getpid()}) + '\n')
        sys.stderr.flush()
        raise RuntimeError('refuse inherited nondefault SIGCHLD: ' + repr(inherited))
    return 'SIG_DFL'


class Popen(subprocess.Popen):
    def __init__(self, *args, **kwargs):
        normalize_startup()  # Immediately before EVERY operational child.
        super().__init__(*args, **kwargs)

    def poll(self):
        with self._waitpid_lock:
            if self.returncode is not None:
                return self.returncode
            # ChildProcessError/ECHILD deliberately propagates, including cleanup.
            pid, status = os.waitpid(self.pid, os.WNOHANG)
            if pid:
                if pid != self.pid:
                    raise RuntimeError('waitpid returned wrong child')
                self.returncode = os.waitstatus_to_exitcode(status)
            return self.returncode

    def _internal_poll(self, _deadstate=None):
        return self.poll()

    def wait(self, timeout=None):
        deadline = None if timeout is None else time.monotonic() + timeout
        while True:
            result = self.poll()
            if result is not None:
                return result
            if deadline is not None and time.monotonic() >= deadline:
                raise subprocess.TimeoutExpired(self.args, timeout)
            time.sleep(0.01)


def run(*args, **kwargs):
    """The preflight's small captured loader command, with strict direct wait."""
    capture = kwargs.pop('capture_output', False)
    timeout = kwargs.pop('timeout', None)
    if capture:
        kwargs.update(stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    with Popen(*args, **kwargs) as child:
        try:
            stdout, stderr = child.communicate(timeout=timeout)
        except BaseException:
            child.kill()
            child.wait()
            raise
        return subprocess.CompletedProcess(child.args, child.wait(), stdout, stderr)
