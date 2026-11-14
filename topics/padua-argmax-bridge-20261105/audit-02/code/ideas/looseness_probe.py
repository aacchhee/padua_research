"""MEASURED (binary64, no enclosure) looseness probe of the E14 near/wide FINITE-ERROR charges.

E_true(phi) := [S_n(phi)-S_n(0)] - [M_far(phi,L)-M_far(0,L)]  (proxy for E_n(phi)-E_n(0);
M_far is the frozen fixed-cutoff C06 model, whose cutoff bias vs the completed M_infty is ~1e-3
at most and tiny near the origin), compared with the E14 relative error charge after exact
origin conversion,
  Charge(phi) = C4 + kx*x + ky*y - u*(A4 + r*J - ebar)     (kN,JN for r<=1/2; kW,JW for r>1/2).
S_n from the inherited floating kernel phase_probe.c (sha256 692d4afd...), M_far from the frozen
read-only evaluator code/post_audit_D01_far/model.py (sha256 6b97477f...).  Planning data only.
"""
import ctypes, importlib.util, json, math, sys, time
import mpmath as mp
from e14_formulas import scalars, KAPPA

lib = ctypes.CDLL('./probe.so')
lib.phase_s.restype = ctypes.c_double
lib.phase_s.argtypes = [ctypes.c_int, ctypes.c_double, ctypes.c_double]
MODEL = '/home/user/padua_research/topics/padua-argmax-bridge-20261105/code/post_audit_D01_far/model.py'
spec = importlib.util.spec_from_file_location('d01model', MODEL)
model = importlib.util.module_from_spec(spec); spec.loader.exec_module(model)

PHASES = [(0.15, 0.11), (0.26, 0.0), (0.0, 0.26), (0.13, 0.13), (0.3, 0.2), (0.25, 0.25), (0.5, 0.5), (0.8, 0.2)]
NS = [int(a) for a in sys.argv[1:]] or [128, 200, 256, 320]

t0 = time.process_time()
prof = {}
for ph in [(0.0, 0.0)] + PHASES:
    p = model.profile(ph[0], ph[1], 0.0)
    prof[ph] = p
rows = []
for n in NS:
    L = math.log(n)
    s = scalars(n)
    S0 = lib.phase_s(n, 0.0, 0.0)
    M0 = prof[(0.0, 0.0)]['B0'] * L * L + prof[(0.0, 0.0)]['b'] * L + prof[(0.0, 0.0)]['constant']
    for (x, y) in PHASES:
        r = x + y
        S = lib.phase_s(n, x, y)
        pr = prof[(x, y)]
        M = pr['B0'] * L * L + pr['b'] * L + pr['constant']
        Etrue = (S - S0) - (M - M0)
        a = (math.cos(x) + math.cos(y)) / 2; u = 1 - a
        if r <= 0.5:
            kx, ky, J = float(s['kNx']), float(s['kNy']), float(s['JN'])
        else:
            kx, ky, J = float(s['kWx']), float(s['kWy']), float(s['JW'])
        charge = float(s['C4']) + kx * x + ky * y - u * (float(s['A4']) + r * J - float(s['eorig']))
        Ec = float(KAPPA) * math.sin(x) ** 1.5 / math.sqrt(a)
        upper = Ec - u * (float(s['T']) + float(s['j'])) + charge
        rows.append(dict(n=n, x=x, y=y, S_minus_Lc=S - S0, dM=M - M0, E_true=Etrue, charge=charge,
                         ratio=charge / abs(Etrue) if Etrue != 0 else None, E14_upper_exact_u=upper))
        print(f"n={n:4d} phi=({x:.2f},{y:.2f}) S-Lc={S-S0:+.5f} dM={M-M0:+.5f} E_true={Etrue:+.2e} charge={charge:+.4f} "
              f"charge/|E|={charge/abs(Etrue):8.1f} E14upper={upper:+.4f}", flush=True)
print('process CPU s:', round(time.process_time() - t0, 2))
json.dump(rows, open('looseness_probe_out.json', 'w'), indent=1)
