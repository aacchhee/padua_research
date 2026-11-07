"""MEASURED binary64: n-scaling of the true relative error proxy E_true(n,phi) (see looseness_probe)
at fixed binding phases, compared with the E14 per-unit-rho slope charge.  Planning only."""
import ctypes, importlib.util, math, json, time
from e14_formulas import scalars
lib = ctypes.CDLL('./probe.so'); lib.phase_s.restype = ctypes.c_double
lib.phase_s.argtypes = [ctypes.c_int, ctypes.c_double, ctypes.c_double]
spec = importlib.util.spec_from_file_location('m', '/home/user/padua_research/topics/padua-argmax-bridge-20261105/code/post_audit_D01_far/model.py')
model = importlib.util.module_from_spec(spec); spec.loader.exec_module(model)
t0 = time.process_time()
ph = [(0.0, 0.0), (0.15, 0.11), (0.25, 0.25), (0.5, 0.5), (0.4, 0.0)]
prof = {p: model.profile(p[0], p[1], 0.0) for p in ph}
out = []
for n in [64, 128, 256, 512, 1024, 2048]:
    L = math.log(n)
    M = {p: prof[p]['B0']*L*L + prof[p]['b']*L + prof[p]['constant'] for p in ph}
    S0 = lib.phase_s(n, 0.0, 0.0)
    for p in ph[1:]:
        S = lib.phase_s(n, p[0], p[1]); E = (S - S0) - (M[p] - M[ph[0]])
        r = p[0] + p[1]; s = scalars(n); k = float(s['kNx'] if r <= 0.5 else s['kWx'])
        out.append(dict(n=n, phi=p, E_true=E, nE_over_L=n*E/L, charge_slope_times_r=k*r))
        print(f"n={n:5d} phi={p} E_true={E:+.3e}  n*E/L={n*E/L:+.4f}  E14 slope*r={k*r:.4f}", flush=True)
print('CPU', round(time.process_time()-t0, 2))
json.dump(out, open('scaling_probe_out.json','w'), indent=1)
