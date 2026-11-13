"""Audit-06 P1: runtime_probe.py sensitivity to MXCSR FTZ/DAZ/rounding, with uint64 readouts.
Usage: python3 -E -B probe6.py TREE LIB REPORT
Imports NumPy and the TREE copy of runtime_probe (and its frozen controls) BEFORE changing MXCSR; per mode sets MXCSR in
this thread, reads bit patterns without float comparison, calls the real runtime_probe.main(), restores MXCSR in finally."""
import contextlib, ctypes, io, json, subprocess, sys
from pathlib import Path

tree, lib, report = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3])
sys.path.insert(0, str(tree / 'topics/padua-argmax-bridge-20261105/code/independent_phase_checker'))
import numpy as np
import runtime_probe as RP

L = ctypes.CDLL(lib); L.get_csr.restype = ctypes.c_uint; L.set_csr.argtypes = [ctypes.c_uint]
default = L.get_csr()
FTZ, DAZ = 1 << 15, 1 << 6
RC = {'RN': 0, 'RD': 1 << 13, 'RU': 2 << 13, 'RZ': 3 << 13}
modes = [('default', default), ('FTZ', default | FTZ), ('DAZ', default | DAZ), ('FTZ|DAZ', default | FTZ | DAZ),
         ('RD', default | RC['RD']), ('RU', default | RC['RU']), ('RZ', default | RC['RZ']),
         ('FTZ|DAZ|RZ', default | FTZ | DAZ | RC['RZ']), ('DAZ|RU', default | DAZ | RC['RU'])]


def bits(x):
    return hex(int(np.asarray(x).view(np.uint64).reshape(-1)[0]))


rows = []
for label, csr in modes:
    L.set_csr(csr)
    try:
        observed = L.get_csr()
        readout = {
            'tiny_div_2': bits(np.array([2.0**-1022]) / np.array([2.0])),
            'subnormal_operand_times_2': bits(np.array([2.0**-1074]) * np.array([2.0])),
            'nextafter_0_1': bits(np.nextafter(np.float64(0), np.float64(1))),
            'tie_down': bits(np.array([1.0]) + np.array([2.0**-53])),
            'tie_up': bits((np.array([1.0]) + np.array([2.0**-52])) + np.array([2.0**-53])),
        }
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):
                RP.main()
            verdict = 'PASS'; detail = json.loads(buf.getvalue())['runtime_probes']
        except SystemExit as e:
            verdict = 'REJECT'; detail = str(e)[:300]
        except Exception as e:  # e.g. a frozen arithmetic control failing under the mode
            verdict = 'EXCEPTION'; detail = type(e).__name__ + ': ' + str(e)[:300]
    finally:
        L.set_csr(default)
    rows.append({'mode': label, 'mxcsr_set': hex(csr), 'mxcsr_read': hex(observed), 'readout': readout,
                 'probe_verdict': verdict, 'detail': detail})
    print(label, hex(csr), readout, verdict, detail, flush=True)

# Per-process scope: set FTZ|DAZ in this thread, then start a fresh interpreter that reads its own MXCSR.
L.set_csr(default | FTZ | DAZ)
try:
    child = subprocess.run([sys.executable, '-E', '-B', '-c',
                            'import ctypes,sys; L=ctypes.CDLL(sys.argv[1]); L.get_csr.restype=ctypes.c_uint; print(hex(L.get_csr()))',
                            lib], capture_output=True, text=True)
finally:
    L.set_csr(default)
child_row = {'parent_mxcsr_while_spawning': hex(default | FTZ | DAZ), 'child_exit': child.returncode,
             'child_mxcsr': child.stdout.strip(), 'child_stderr': child.stderr[-200:]}
print('child', child_row, flush=True)
report.write_text(json.dumps({'default_mxcsr': hex(default), 'numpy': np.__version__, 'python': sys.version,
                              'rows': rows, 'fresh_child_after_FTZ_DAZ_parent': child_row}, indent=1) + '\n')
