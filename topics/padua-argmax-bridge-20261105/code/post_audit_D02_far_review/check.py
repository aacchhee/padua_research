"""Bounded independent scalar controls; all outputs are MEASURED."""
import hashlib
import json
import math
import platform
import resource
import sys
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU, (20, 20))
import mpmath as mp
import scipy
from scipy.special import digamma

ROOT = Path(__file__).resolve().parents[4]
TOPIC = ROOT / "topics/padua-argmax-bridge-20261105"
RAW = ROOT / "local-output/argmax-bridge-20261105/post-audit-D01/far/t1c.json"
OLD = TOPIC / "evidence/d01-far.json"
EXPECTED = {
    RAW: "08407e19b8a7a7600ae1c4b8aa00800242dbc2a3f1be6e06dec9a6e1b3ff2d5a",
    OLD: "10b8b2800b6ac910ce50eb43f50005b409388f664a3d8dc5ea2d62ab59323c1d",
}


def identity(path):
    b = path.read_bytes()
    return {"path": str(path.relative_to(ROOT)), "bytes": len(b),
            "sha256": hashlib.sha256(b).hexdigest()}


for path, digest in EXPECTED.items():
    assert identity(path)["sha256"] == digest
x = json.loads(RAW.read_text())[0]
v = x["model"]
assert x["phase"] == 2 and x["delta"] == 0.01
assert abs(v["a"] - math.cos(1.45)) < 1e-16
assert v["p"] == v["q"] == math.sin(1.45)
pi = math.pi
C = lambda t: -digamma(t) - digamma(1 - t)
Einf = v["a"] / 3 + v["a"] * C(.5) * C(.5 + 1.45 / pi) / pi**2
D0 = v["U"] / pi + v["B0"] * math.log(pi)
kap = math.log(.01 / pi)
ER = v["endpoint_rows"] + v["mesh_constant"] - v["B0"] * kap**2 - 2 * D0 * kap
bias = float(Einf - ER + x["strip_residual_partial_integral"])
eta = 1e-7
missing = 2 * eta / pi * (7 + (v["p"] + v["q"]) / pi * (5 + 2 * math.log(4*pi/eta)))
old = json.loads(OLD.read_text())
replay = {"E_infty": float(Einf), "E64": float(ER),
          "endpoint_tail": float(Einf-ER), "estimated_bias": bias,
          "omitted_strip_analytic_bound": missing,
          "old_floating_quadrature_estimate": x["strip_residual_partial_estimate"],
          "residuals": [{"n": r["n"], "old": r["S_minus_M"],
                         "bias_subtracted": r["S_minus_M"]-bias}
                        for r in old["results"] if r["phase"] == 2]}

mp.mp.dps = 60
pi = mp.pi
C = lambda t: -mp.digamma(t) - mp.digamma(1-t)
dec = lambda z: mp.nstr(z, 35)
eps = mp.mpf('.01') / (2*pi)
# Independent gamma expression and 12-term convergent odd-zeta expansion.
b_gamma = -(2/pi)*(mp.log(eps)+mp.loggamma(eps)-mp.loggamma(1-eps)
                       +2*eps*mp.log(pi))
b_series = 4/pi*((mp.euler-mp.log(pi))*eps + mp.fsum(
    mp.zeta(2*k+1)*eps**(2*k+1)/(2*k+1) for k in range(1, 13)))
assert abs(b_gamma-b_series) < mp.mpf('1e-55')
assert b_gamma < 0

telescoping = []
for R in (2, 64):
    for t in (mp.mpf('1e-10'), mp.mpf(1)/7, mp.mpf('.5')):
        p = mp.sin(pi*t)
        CR = p/pi * mp.fsum(1/(k+t)+1/(k+1-t) for k in range(R))
        ER = CR - p/pi*(mp.digamma(R+t)+mp.digamma(R+1-t))
        error = ER-p/pi*C(t)
        assert abs(error) < mp.mpf('1e-50')
        telescoping.append({"R": R, "t": dec(t), "E_R_minus_E_infty": dec(error)})

controls = []
for n, t in ((2, mp.mpf(1)/7), (3, mp.mpf('.5')),
             (16, mp.mpf('1e-8')), (17, mp.mpf(1)/3)):
    N = n*(n+1)
    p = mp.sin(pi*t)
    # PD-T365 scalar boundary formula, not an evaluation of the odd board.
    S = p/(2*N)*mp.fsum(abs(mp.cot(pi*(q+t)/(2*N))) for q in range(2*N))
    Cinf = p/pi*(C(t)+2*mp.log(2/pi))
    M = 4*p/pi*mp.log(n)+Cinf-p*b_gamma
    error = S-M-p*(b_gamma+2/pi*mp.log1p(mp.mpf(1)/n))
    bound = mp.mpf(7)/(12*N*N)
    assert abs(error) <= bound
    controls.append({"n": n, "t": dec(t), "residual_after_exact_correction": dec(error),
                     "claimed_bound": dec(bound), "absolute_ratio": dec(abs(error)/bound)})

r = resource.getrusage(resource.RUSAGE_SELF)
result = {
    "status": "MEASURED; no numerical result is a proof premise",
    "scope": "One scalar replay, six boundary cutoff controls, two scalar bias formulas, four 1D boundary controls; no native/full board/interior quadrature",
    "rules_input": "084a64f6465956f9c75b5538f83752c30318f151",
    "inputs": [identity(p) for p in EXPECTED],
    "script": identity(Path(__file__).resolve()),
    "environment": {"python": sys.version.split()[0], "platform": platform.platform(),
                    "scipy": scipy.__version__, "mpmath": mp.__version__, "mpmath_dps": mp.mp.dps},
    "scalar_replay": replay,
    "midpoint_bias": {"gamma": dec(b_gamma), "12_term_series": dec(b_series),
                      "difference": dec(b_gamma-b_series)},
    "boundary_endpoint_constants": telescoping,
    "boundary_finite_n_controls": controls,
    "cpu_seconds_including_imports": r.ru_utime+r.ru_stime,
    "cpu_limit_seconds": 20,
    "limitations": "Floating, non-interval arithmetic; controls are not exhaustive. Raw D01 input is local working output; its cold-storage retrieval remains as recorded by D01. No interior quadrature rerun, rate or uniform constant certified."
}
output = TOPIC / "evidence/d02-far-review.json"
payload = json.dumps(result, indent=2, sort_keys=True) + '\n'
assert len(payload.encode()) < 16384
output.write_text(payload)
print(json.dumps({"receipt": identity(output), "cpu_seconds": result["cpu_seconds_including_imports"],
                  "estimated_bias": bias, "max_boundary_ratio": max(float(r["absolute_ratio"]) for r in controls)}, indent=2))
