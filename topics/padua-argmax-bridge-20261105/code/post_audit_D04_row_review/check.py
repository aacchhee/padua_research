"""Tiny independent D04 formula controls; floating, not interval proof."""
import hashlib
import json
import resource
import sys
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU, (20, 20))
import mpmath as mp

mp.mp.dps = 60
pi = mp.pi
dec = lambda x: mp.nstr(x, 35)
halfline = []
for h, v, t in ((mp.mpf('.4'), mp.mpf('.1'), mp.mpf(0)),
                (mp.mpf('.7'), mp.mpf('.3'), mp.mpf(1)),
                (pi/17, pi/2-mp.mpf('1e-9'), mp.mpf('.3'))):
    ys = []
    k = 0
    while v+h*(k+t) < pi/2:
        ys.append(v+h*(k+t))
        k += 1
    Q = mp.fsum(mp.cot(y) for y in ys) + mp.log(mp.sin(v))/h
    expected = (mp.log(v/h)-mp.digamma(v/h+t))/h
    error = Q-expected
    assert abs(error) <= 4/pi
    halfline.append({"h": dec(h), "v": dec(v), "t": dec(t), "sample_count": k,
                     "error": dec(error), "bound": dec(4/pi)})

rows = []
cases = [(16, mp.mpf('.95'), mp.mpf('.02'), 2),
         (16, mp.mpf('.95'), mp.mpf('.02'), 31),
         (17, mp.mpf(1)/5, mp.mpf(1)/7, 3),
         (17, mp.mpf(1)/5, mp.mpf(1)/7, 32)]
for n, x, t, r in cases:
    m = n+1
    alpha, beta = pi*x, pi*t
    a = (mp.cos(alpha)+mp.cos(beta))/2
    P = mp.sin(alpha)+mp.sin(beta)
    v = (r*pi+beta)/m
    original_w = a*mp.cot(v/2)/2
    samples = []
    for k in range(n):
        u = (((1-r) % 2)*pi+alpha+2*k*pi)/n
        X = (u-v)/2
        assert abs(mp.sin(X)) > mp.mpf('1e-40')
        assert abs(mp.sin(X+v)) > mp.mpf('1e-40')
        left, right = -original_w*mp.cot(X), original_w*mp.cot(X+v)
        samples.append(abs(left+right)-abs(left)-abs(right))
    if v < pi/2:
        j, s, z = r, t, v
    else:
        j, s, z = 2*m-r, -t, 2*pi-v
    assert 0 < z < pi/2
    nu = j+s
    displacement = nu/(2*m)
    theta = [(1-s+x)/2+displacement, (1-s-x)/2+displacement]
    wraps = [int(mp.floor(q)) for q in theta]
    qs = [(1+s+x)/2, (1+s-x)/2]
    ys = [j+q-displacement for q in qs]
    assert all(0 < q-mp.floor(q) < 1 for q in theta)
    assert all(abs(n*z/pi+mp.frac(th)-(y-w)) < mp.mpf('1e-50')
               for th, y, w in zip(theta, ys, wraps))
    folded_w = a*mp.cot(z/2)/2
    integral = 4*folded_w*mp.log(mp.sin(z))
    T0 = mp.fsum(samples)-n*integral/pi
    Theta = (a*n/pi)*mp.cot(z/2)*(mp.fsum(mp.digamma(y-w) for y,w in zip(ys,wraps))
                                            -2*mp.log(n*z/pi))
    bound = 16*folded_w/pi
    assert abs(T0-Theta) <= bound
    Xi = 2*a/pi**2*(mp.fsum(mp.digamma(j+q) for q in qs)-2*mp.log(nu))/nu
    matching_error = Theta/(n*m)-Xi
    matching_bound = 10*a/(pi**2*n*nu)+a/m**2+8*P/(3*pi*m*(j-1))
    assert abs(matching_error) <= matching_bound
    rows.append({"n": n, "alpha_over_pi": dec(x), "beta_over_pi": dec(t), "r": r,
                 "j": j, "s": dec(s), "wraps": wraps,
                 "T0_minus_Theta": dec(T0-Theta), "half_line_bound": dec(bound),
                 "half_line_ratio": dec(abs(T0-Theta)/bound),
                 "Theta_normalized_minus_Xi": dec(matching_error),
                 "matching_bound": dec(matching_bound),
                 "matching_ratio": dec(abs(matching_error)/matching_bound)})

script = Path(__file__).resolve()
root = script.parents[4]
r = resource.getrusage(resource.RUSAGE_SELF)
result = {"status": "MEASURED; no proof premise", "rules_read": "084a64f6465956f9c75b5538f83752c30318f151",
          "observed_review_head": "a6d7a788b3ce457a4631bbb507624303240c570c",
          "script": {"path": str(script.relative_to(root)), "bytes": script.stat().st_size,
                     "sha256": hashlib.sha256(script.read_bytes()).hexdigest()},
          "python": sys.version.split()[0], "mpmath": mp.__version__, "decimal_digits": mp.mp.dps,
          "half_line_controls": halfline, "reference_row_controls": rows,
          "reference_sample_count": sum(q[0] for q in cases),
          "cpu_seconds_including_imports": r.ru_utime+r.ru_stime, "cpu_limit_seconds": 20,
          "limitations": "Four isolated bounded reference rows, not actual polynomial board evaluation. No quadrature, sweep, interval enclosure, all-row reference test or practical-rate claim."}
output = root / 'topics/padua-argmax-bridge-20261105/evidence/d04-row-review.json'
payload = json.dumps(result, indent=2, sort_keys=True)+'\n'
assert len(payload.encode()) < 16384
output.write_text(payload)
print(json.dumps({"path": str(output.relative_to(root)), "bytes": output.stat().st_size,
                  "sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
                  "cpu_seconds": result['cpu_seconds_including_imports'],
                  "max_half_line_row_ratio": max(float(q['half_line_ratio']) for q in rows),
                  "max_matching_ratio": max(float(q['matching_ratio']) for q in rows)}, indent=2))
