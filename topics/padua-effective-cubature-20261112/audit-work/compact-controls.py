"""Audit-only arithmetic controls; NOT a replay of the DGOV coefficient certificate.

The full compact script is exercised with explicitly synthetic coefficients and
a synthetic gamma receipt to test its moment/loss arithmetic. These synthetic
inputs make no Delsarte-admissibility claim. The real receipt control separately
checks rounding and the reported compact bound, conditional on its moment sum.
"""
import contextlib
import io
import json
import runpy
import sys
import tempfile
from fractions import Fraction as F
from pathlib import Path

from flint import arb, ctx, fmpq
import sympy as sp

TOPIC = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOPIC / "code"))
import gamma_certificate as gc

ctx.prec = 256
t = sp.symbols("t", real=True)
beta_inner = 1 - sp.Rational(3, 2)*t**2 + sp.Rational(3, 4)*t**3
beta_outer = (2-t)**3/4
assert beta_inner.subs(t, 0) == 1
assert beta_inner.subs(t, 1) == beta_outer.subs(t, 1) == sp.Rational(1, 4)
assert beta_outer.subs(t, 2) == 0
assert sp.factor(sp.diff(beta_inner, t)) == 3*t*(3*t-4)/4
assert sp.factor(sp.diff(beta_outer, t)) == -3*(t-2)**2/4
assert sp.expand(sp.Rational(3, 2)*t*t-(1-beta_inner)) == sp.Rational(3, 4)*t**3
print("B-spline formulas/endpoints/derivatives and inner quadratic bound: checked")

real = json.loads((TOPIC / "evidence/gamma-certificate.json").read_text())
compact = json.loads((TOPIC / "evidence/gamma-compact.json").read_text())
mid, rad = real["gamma1_lower"].strip("[]").split("+/-")
assert F(rad) < F("1e-40")
gused = arb(mid.strip()) - arb("1e-40")
assert gused < arb(real["gamma1_lower"])
loss = arb(9)/8/arb(100000)**2*arb(compact["int_abs_phi_xi2_bound"])
lower = gused-loss
assert lower > arb("0.02781152574")
assert lower > arb(fmpq(1, 36))
assert arb(compact["gamma_compact_lower"]).overlaps(lower)
print("Pinned-receipt parsing and conditional compact arithmetic:", lower)
assert arb(real["gamma1"])-arb("3.0043e-5") < arb("0.0278115257")
print("Display-chain discrepancy reproduced: rounded loss implies only 0.027811525690776...")

# P=1-2|x|^2+3 sum_i x_i^4. Triangle-inequality moment integral:
# E[|x|^2]+2E[|x|^4]+3E[(sum_i x_i^4)|x|^2].
# Independent Gaussian/radial moment calculation gives the expression below.
synthetic_C = {(0, 0, 0): F(1), (1, 0, 0): F(-2), (0, 1, 0): F(3)}
pi = arb.pi()
expected_S = 3/(2*pi) + 15/(2*pi**2) + 189/(8*pi**3)
expected_moment = (arb(2000)/1001)**5*expected_S
saved_read = gc.read_coeffs
saved_argv = sys.argv
gc.read_coeffs = lambda _: (synthetic_C, gc.ANC_SHA)
try:
    with tempfile.TemporaryDirectory(prefix="compact-audit-controls-") as directory:
        scratch = Path(directory)
        receipt = scratch / "synthetic-receipt.json"
        receipt.write_text(json.dumps({"verdict": "PASS", "gamma1_lower": "[0.03 +/- 1e-70]"}))
        for radius, expected_verdict in ((100000, "PASS"), (1, "FAIL")):
            output = scratch / f"synthetic-{radius}.json"
            sys.argv = ["gamma_compact.py", "--anc", "SYNTHETIC-NOT-DGOV",
                        "--gamma-receipt", str(receipt), "--R", str(radius), "--out", str(output)]
            with contextlib.redirect_stdout(io.StringIO()):
                runpy.run_path(str(TOPIC / "code/gamma_compact.py"), run_name="__main__")
            result = json.loads(output.read_text())
            assert arb(result["sum_abs_moment_bound"]).overlaps(expected_S)
            assert arb(result["int_abs_phi_xi2_bound"]).overlaps(expected_moment)
            expected_lower = arb("0.03")-arb("1e-40")-arb(9)/(8*radius**2)*expected_moment
            # The script serializes an endpoint, not the full lower-value ball;
            # differing valid arithmetic orders can put endpoints just outside
            # the other order's tighter enclosure. Bound their discrepancy.
            assert abs(arb(result["gamma_compact_lower"])-expected_lower) < arb("1e-60")
            assert result["verdict"] == expected_verdict
        print("Actual compact-script arithmetic on synthetic inputs: R=100000 accepts, R=1 rejects; exact moment formulas match")
finally:
    gc.read_coeffs = saved_read
    sys.argv = saved_argv

print("All scoped controls passed. DGOV data-dependent replay was NOT performed.")
