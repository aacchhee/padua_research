"""Explicit COMPACTLY SUPPORTED Delsarte witness for int(2O) (record -05 target; audit-01 A1).

Let phi be the record -07 function, phi(xi) = f(alpha xi/2)/f(0), f = P e^{-pi|x|^2}, with
gamma_1 = (3/4) int phi - 1 certified by gamma_certificate.py (and its independent rerun).
Cutoff: beta(t) = (3/2) M4(t), M4 = 1_[-1/2,1/2]^{*4} the centred cubic B-spline, so beta(0)=1,
0 <= beta <= 1, supp beta = [-2,2], beta-hat = (3/2) sinc^4 >= 0, and 1 - beta(t) <= (3/2) t^2.
g(eta) = prod_i beta(eta_i); psi_R(xi) = phi(xi) g(xi/R).
Then psi_R is continuous, supported in [-2R,2R]^3, psi_R(0)=1, psi_R <= 0 where phi <= 0, and
psi_R-hat = phi-hat * (R^3 g-hat(R .)) >= 0; i.e. psi_R satisfies record -02 (b). Moreover
1 - g <= sum_i (1 - beta(eta_i)) <= (3/2)|eta|^2, hence
  (3/4) int psi_R - 1 >= gamma_1 - (3/4)(3/(2R^2)) int |phi(xi)| |xi|^2 dxi,
  int |phi| |xi|^2 = (2/alpha)^5 / P(0) * int |P(x)| |x|^2 e^{-pi|x|^2} dx
                  <= (2/alpha)^5 / P(0) * sum_a |p_a| sum_i m(a + e_i),
with P = sum_a p_a x^(2a) and m(b) = prod_i (2b_i - 1)!! / (2 pi)^(b_i) = int x^(2b) e^{-pi|x|^2}.
This script evaluates the bound in Arb (exact rationals and pi), for the chosen R, and checks
that the lower bound exceeds 1/36. gamma_1 is taken as the certified lower end from the
certificate receipt passed with --gamma-receipt.
Usage: python3 -B gamma_compact.py --anc PATH/octa_double.func.cpp --gamma-receipt evidence/gamma-certificate.json --R 100000 --out out.json
"""
import argparse, hashlib, json, os, sys
from fractions import Fraction
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gamma_certificate as gc
from flint import arb, ctx, fmpq

ap = argparse.ArgumentParser()
ap.add_argument("--anc", required=True); ap.add_argument("--gamma-receipt", required=True)
ap.add_argument("--R", default="100000"); ap.add_argument("--alpha", default="1001/1000")
ap.add_argument("--out", required=True)
a = ap.parse_args()
ctx.prec = 256
C, sha = gc.read_coeffs(a.anc)
assert sha == gc.ANC_SHA
P = gc.P_in_y(C)
pi = arb.pi()
def dfact(n):           # (2b-1)!! for n = b
    r = 1
    for k in range(1, 2 * n, 2):
        r *= k
    return r
def m(b):
    return arb(dfact(b[0]) * dfact(b[1]) * dfact(b[2])) / (2 * pi) ** (b[0] + b[1] + b[2])
S = arb(0)
for k, v in P.items():
    av = arb(fmpq(abs(v.numerator), v.denominator))
    for i in range(3):
        b = list(k); b[i] += 1
        S += av * m(b)
alpha = Fraction(a.alpha); R = Fraction(a.R)
al = arb(fmpq(alpha.numerator, alpha.denominator)); Rb = arb(fmpq(R.numerator, R.denominator))
P0 = arb(fmpq(P[(0, 0, 0)].numerator, P[(0, 0, 0)].denominator))
second_moment_bound = (2 / al) ** 5 / P0 * S
loss = arb(3) / 4 * arb(3) / (2 * Rb ** 2) * second_moment_bound
rec = json.load(open(a.gamma_receipt))
assert rec["verdict"] == "PASS"
g1 = arb(rec["gamma1_lower"].split("+/-")[0].strip(" [")) - arb("1e-40")   # conservative
lower = g1 - loss
ok = bool(lower > arb(fmpq(1, 36)))
res = {"anc_sha256": sha, "R": str(R), "alpha": str(alpha), "support": f"[-{2*R},{2*R}]^3",
       "sum_abs_moment_bound": str(S), "int_abs_phi_xi2_bound": str(second_moment_bound),
       "loss_upper": str(loss.upper()), "gamma1_used": str(g1), "gamma_compact_lower": str(lower.lower()),
       "gt_1_36": ok, "gamma_receipt_sha256": hashlib.sha256(open(a.gamma_receipt, "rb").read()).hexdigest(),
       "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
       "python": sys.version.split()[0], "verdict": "PASS" if ok else "FAIL"}
json.dump(res, open(a.out, "w"), indent=1)
print(json.dumps({k: res[k] for k in ("int_abs_phi_xi2_bound", "loss_upper", "gamma_compact_lower", "verdict")}))
