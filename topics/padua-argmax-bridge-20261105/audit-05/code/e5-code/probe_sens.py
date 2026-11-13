"""A2: runtime_probe.py sensitivity to MXCSR FTZ/DAZ/rounding. Usage: python3 -E -B probe_sens.py TREE LIB REPORT"""
import contextlib, ctypes, io, json, sys
from pathlib import Path
tree, lib, report = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3])
sys.path.insert(0, str(tree / 'topics/padua-argmax-bridge-20261105/code/independent_phase_checker'))
import numpy as np
import runtime_probe as RP  # trusted copy; imports frozen controls.py
L = ctypes.CDLL(lib); L.get_csr.restype = ctypes.c_uint; L.set_csr.argtypes = [ctypes.c_uint]
default = L.get_csr()
FTZ, DAZ, RZ = 1 << 15, 1 << 6, 3 << 13
rows = []
for label, csr in [('default', default), ('FTZ|DAZ', default | FTZ | DAZ), ('round-toward-zero', default | RZ),
                   ('FTZ only', default | FTZ), ('DAZ only', default | DAZ)]:
    L.set_csr(csr)
    try:
        bits = float.hex(float((np.array([2.0**-1022]) / 2)[0]))
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):
                RP.main()
            outcome = json.loads(buf.getvalue())['runtime_probes']; status = 'PASS'
        except SystemExit as e:
            outcome = str(e)[:300]; status = 'SystemExit'
        except Exception as e:
            outcome = type(e).__name__ + ': ' + str(e)[:300]; status = 'Exception'
    finally:
        L.set_csr(default)
    rows.append({'mode': label, 'mxcsr': hex(csr), 'half_tiny_bits': bits, 'status': status, 'probes': outcome})
    print(label, hex(csr), bits, status, outcome if status != 'PASS' else outcome, flush=True)
report.write_text(json.dumps({'default_mxcsr': hex(default), 'rows': rows, 'numpy': np.__version__}, indent=1) + '\n')
