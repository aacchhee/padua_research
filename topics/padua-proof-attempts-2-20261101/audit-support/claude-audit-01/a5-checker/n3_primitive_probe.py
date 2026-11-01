#!/usr/bin/env python3
"""Claude audit-01: unit probes of the frozen n=3 checker primitives (no certificate)."""
import json, random, sys, time
from fractions import Fraction as F
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "code"))
import a5_checker as c  # noqa: E402
import sympy as s  # noqa: E402

out = []


def reject(name, fn):
    try:
        fn()
    except c.Invalid as e:
        out.append({"name": name, "rejected": True, "reason": str(e)[:100]}); return
    raise SystemExit("ACCEPTED " + name)


def accept(name, fn):
    fn(); out.append({"name": name, "accepted": True})


t0 = time.monotonic()
t = s.Symbol("t")
p = s.Poly((t**2 - 2)*(3*t - 1), t, domain=s.QQ)
accept("touching_nonroot_endpoint_allowed", lambda: c.check_roots(p, [["-2", "0"], ["0", "1"], ["1", "2"]]))
reject("touching_at_root_rejected", lambda: c.check_roots(p, [["-2", "-1"], ["0", "1/3"], ["1/3", "1/3"], ["1", "2"]]))
reject("overlap_rejected", lambda: c.check_roots(p, [["-2", "0"], ["-1/2", "1"], ["1", "2"]]))
reject("omitted_root_rejected", lambda: c.check_roots(p, [["-2", "0"], ["0", "1"]]))
reject("double_root_interval_rejected", lambda: c.check_roots(p, [["-2", "0"], ["0", "2"]]))
q = s.Poly(t**2 + 1, t, domain=s.QQ)
accept("no_real_roots_empty_partition", lambda: c.check_roots(q, []))
reject("no_real_roots_fake_interval", lambda: c.check_roots(q, [["-1", "1"]]))
# qsign on a+b*sqrt2 against high-precision reference
import mpmath as mp
mp.mp.dps = 60
rng = random.Random(3)
for _ in range(3000):
    a = F(rng.randint(-10**8, 10**8), rng.randint(1, 10**4)); b = F(rng.randint(-10**8, 10**8), rng.randint(1, 10**4))
    e = s.Rational(a.numerator, a.denominator) + s.Rational(b.numerator, b.denominator)*s.sqrt(2)
    ref = mp.mpf(a.numerator)/a.denominator + mp.mpf(b.numerator)/b.denominator*mp.sqrt(2)
    assert c.qsign(e) == (1 if ref > 0 else -1 if ref < 0 else 0)
out.append({"name": "qsign_random_vs_mpmath", "accepted": True, "cases": 3000})
# interval power/product containment
for _ in range(3000):
    lo, hi = sorted(F(rng.randint(-999, 999), rng.randint(1, 99)) for _ in range(2))
    k = rng.randint(0, 6); X = c.I(lo, hi)
    for u in (lo, hi, (lo+hi)/2):
        assert X.__pow__(k).lo <= u**k <= X.__pow__(k).hi
out.append({"name": "interval_power_containment", "accepted": True, "cases": 3000})
print(json.dumps({"all_probes_passed": True, "probes": out, "seconds": round(time.monotonic()-t0, 2)}, indent=1))
