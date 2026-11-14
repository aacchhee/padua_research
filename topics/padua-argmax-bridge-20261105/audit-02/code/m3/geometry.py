"""Measurement-only sampling of the E13 joint geometry (1) on the CLOSED outer
diamond x,y>=0, 1<=x+y<=pi, and the E15/E09 caps on pi/2<=x+y<=pi.
Not a proof: dense grid plus all four boundary lines, float64 with a
reported minimum slack.  Auditor m3 (Claude Opus 5.5 xhigh).
"""
import math
u1 = 47/384; a0 = 337/384; w0 = 721/384; p0 = 12/25; P0 = 24/25; eta = 1.5
def pts(rlo, N=1400):
    out = []
    for i in range(N + 1):
        rho = rlo + (math.pi - rlo) * i / N
        for j in range(N + 1):
            x = rho * j / N; out.append((x, rho - x))
    # extra density at rho=rlo and near the x in [1/2,1] branch
    for j in range(200001):
        x = rlo * j / 200000; out.append((x, rlo - x))
    for j in range(20001):
        x = math.pi * j / 20000; out.append((x, math.pi - x))
    return out
worst = {}
def upd(k, s, pt):
    if k not in worst or s < worst[k][0]: worst[k] = (s, pt)
for (x, y) in pts(1.0):
    ce = math.cos((x + y) / 2); cd = math.cos((x - y) / 2); a = (math.cos(x) + math.cos(y)) / 2
    u = 1 - a; v = u - u1; p = math.sin(x); q = math.sin(y); P = p + q
    upd('v>=0', v, (x, y)); upd('a<=a0', a0 - a, (x, y)); upd('ce+cd<=w0', w0 - ce - cd, (x, y))
    sv = math.sqrt(max(v, 0))
    upd('p<=p0+eta sqrt v', p0 + eta * sv - p, (x, y)); upd('q<=p0+eta sqrt v', p0 + eta * sv - q, (x, y))
    upd('|p-q|<=2sqrt(2v)', 2 * math.sqrt(2 * max(v, 0)) - abs(p - q), (x, y))
    upd('P<=2sqrt(2u-u^2)', 2 * math.sqrt(2 * u - u * u) - P, (x, y))
    upd('2sqrt(2u-u^2)<=P0+4v', P0 + 4 * v - 2 * math.sqrt(2 * u - u * u), (x, y))
    upd('ce,cd>=0', min(ce, cd), (x, y))
for k, (s, pt) in worst.items():
    print('E13 %-26s min slack %.3e at (x,y)=(%.6f,%.6f)' % (k, s, pt[0], pt[1]))
worst = {}
for (x, y) in pts(math.pi / 2, 1000):
    ce = math.cos((x + y) / 2); cd = math.cos((x - y) / 2); a = (math.cos(x) + math.cos(y)) / 2
    u = 1 - a; p = math.sin(x); q = math.sin(y); P = p + q; d = max(q - p, 0)
    Fv = 2 * math.sqrt(u * (1 - u)) if u <= 0.5 else 1.0; Q = min(2.0, math.sqrt(8 * u))
    upd('u>7/24', u - 7/24, (x, y)); upd('max(p,q)<=F', Fv - max(p, q), (x, y)); upd('d<=F', Fv - d, (x, y))
    upd('P<=Q', Q - P, (x, y)); upd('ce+cd<=2-u', 2 - u - ce - cd, (x, y))
for k, (s, pt) in worst.items():
    print('E15 %-26s min slack %.3e at (x,y)=(%.6f,%.6f)' % (k, s, pt[0], pt[1]))
bad = [k for k, (s, _) in worst.items() if s < -1e-12]
print('E15 violations:', bad)
