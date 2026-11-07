"""MEASURED binary64: E_n(0) proxy = S_n(0) - M_far(0,log n) vs the one-sided allowance ebar (E08)."""
import ctypes, importlib.util, math, json
from e14_formulas import scalars
lib = ctypes.CDLL('./probe.so'); lib.phase_s.restype = ctypes.c_double
lib.phase_s.argtypes = [ctypes.c_int, ctypes.c_double, ctypes.c_double]
spec = importlib.util.spec_from_file_location('m', '/home/user/padua_research/topics/padua-argmax-bridge-20261105/code/post_audit_D01_far/model.py')
model = importlib.util.module_from_spec(spec); spec.loader.exec_module(model)
p = model.profile(0.0, 0.0, 0.0)
out = []
for n in [64, 96, 128, 160, 200, 256, 320, 512]:
    L = math.log(n); S0 = lib.phase_s(n, 0.0, 0.0); M0 = p['B0']*L*L + p['b']*L + p['constant']
    s = scalars(n)
    out.append(dict(n=n, S0=S0, M0=M0, E0=S0-M0, ebar=float(s['eorig'])))
    print(f"n={n:4d} Lambda_c={S0:.6f} M_far(0)={M0:.6f} E_n(0)~{S0-M0:+.5f}  one-sided allowance e0={float(s['eorig']):.4f}")
json.dump(out, open('origin_probe_out.json','w'), indent=1)
