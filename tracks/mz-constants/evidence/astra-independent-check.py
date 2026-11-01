#!/usr/bin/env python3
"""Independent exact CC audit; floating Padua and cardinal checks are measurements.

No developer or supplied computation is imported. CC quadrature is reconstructed
as integration of polynomial remainder modulo (x*x-1)U_(N-1), which has exactly
the CC nodes. Only Python Fraction is trusted for the rational checks.
"""
from fractions import Fraction as F
import hashlib
import json
import platform
from pathlib import Path
import numpy as np


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b, scale=F(1)):
    c = list(a) + [F(0)] * max(0, len(b)-len(a))
    for j, v in enumerate(b):
        c[j] += scale*v
    return trim(c)


def mul(a, b):
    c = [F(0)]*(len(a)+len(b)-1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            c[i+j] += u*v
    return trim(c)


def rem(a, b):
    a = trim(a)
    while len(a) >= len(b):
        offset = len(a)-len(b)
        a = add(a, [F(0)]*offset + b, -a[-1]/b[-1])
    return a


def integ(a):
    return sum((F(2)*v/F(j+1) for j, v in enumerate(a) if j % 2 == 0), F(0))


def cheb(max_degree, second=False):
    out = [[F(1)], [F(0), F(2 if second else 1)]]
    for j in range(2, max_degree+1):
        out.append(add([F(0)] + [2*v for v in out[-1]], out[-2], F(-1)))
    return out[:max_degree+1]


def moment(k):
    return F(0) if k % 2 else F(2, 1-k*k)


def positive_pivots(a):
    a = [row[:] for row in a]
    for k in range(len(a)):
        pivot = a[k][k]
        assert pivot > 0, (k, pivot)
        for i in range(k+1, len(a)):
            for j in range(i, len(a)):
                a[i][j] -= a[i][k]*a[j][k]/pivot
                a[j][i] = a[i][j]


def exact_cc(N):
    ts, us = cheb(N), cheb(N-1, second=True)
    nodal = mul([F(-1), F(0), F(1)], us[N-1])
    T, Q = [], []
    for i in range(N):
        tr, qr = [], []
        for j in range(N):
            p = mul(ts[i], ts[j])
            tr.append(integ(p))
            qr.append(integ(rem(p, nodal)))
            s = i+j
            alias = s if s <= N else 2*N-s
            assert qr[-1] == (moment(abs(i-j))+moment(alias))/2
        T.append(tr)
        Q.append(qr)
    D = [[2*(T[i][j]-Q[i][j]) for j in range(N)] for i in range(N)]
    A = [[2*T[i][j]-Q[i][j] for j in range(N)] for i in range(N)]
    assert all(v >= 0 for row in D for v in row)
    assert all(A[i][j] <= 0 for i in range(N) for j in range(N) if i != j)
    positive_pivots(A)
    neg_minor = None
    if N >= 5:
        i, j = N//2, N//2+2
        neg_minor = D[i][i]*D[j][j]-D[i][j]*D[j][i]
        assert neg_minor < 0
    u2 = mul(us[N-1], us[N-1])
    unorm = 2*sum((F(1, 2*k-1) for k in range(1, N+1)), F(0))
    uq = F(2) if N % 2 else F(2*N*N, N*N-1)
    assert integ(u2) == unorm
    assert integ(rem(u2, nodal)) == uq
    tn2 = mul(ts[N], ts[N])
    assert integ(rem(tn2, nodal)) == 2
    tnratio = F(2)/integ(tn2)
    assert tnratio == F(2*(4*N*N-1), 4*N*N-2) > 2
    return dict(N=N, exact_checks_pass=True, negative_D_minor=str(neg_minor),
                U_norm_squared=str(unorm), U_Q=str(uq), T_N_ratio=str(tnratio))


def padua_measurement(m):
    pts = [(np.cos(j*np.pi/m), np.cos(k*np.pi/(m+1)))
           for j in range(m+1) for k in range(m+2) if (j+k) % 2 == 0]
    pts = np.array(pts)
    idx = [(i, d-i) for d in range(m+1) for i in range(d+1)]
    vx = np.polynomial.chebyshev.chebvander(pts[:, 0], m)
    vy = np.polynomial.chebyshev.chebvander(pts[:, 1], m)
    V = np.column_stack([vx[:, i]*vy[:, j] for i, j in idx])
    mu = np.array([float(moment(i)*moment(j)) for i, j in idx])
    weights = np.linalg.solve(V.T, mu)
    xs = np.cos(np.arange(m+1)*np.pi/m)
    C = np.polynomial.chebyshev.chebvander(xs, m)
    wc = np.linalg.solve(C.T, np.array([float(moment(i)) for i in range(m+1)]))
    margin = np.array([weights[np.abs(pts[:, 0]-x) < 1e-12].sum() for x in xs])
    residual = float(np.max(np.abs(margin-2*wc)))
    assert residual < 2e-12
    return dict(m=m, marginal_max_residual=residual, min_weight=float(weights.min()))


def cardinal_measurement(N):
    j = np.arange(N+1)
    th = np.pi*j/N
    c = np.ones(N+1); c[[0, -1]] = 2
    coefficients = (2/N)*np.cos(np.outer(j, th))/np.outer(c, c)
    T = np.array([[float((moment(abs(a-b))+moment(a+b))/2)
                   for b in j] for a in j])
    w = np.array([float(moment(k)) for k in j]) @ coefficients
    B = coefficients.T @ T @ coefficients / np.sqrt(np.outer(w, w))
    constraint = (-1.)**j/(c*np.sqrt(w))
    m = np.maximum(np.minimum(j, N-j), 1)
    v = (-1.)**j/np.sqrt(m)
    qfull = float(v @ B @ v/(v @ v))
    q, _ = np.linalg.qr(constraint[:, None], mode='complete')
    restricted = q[:, 1:].T @ B @ q[:, 1:]
    return dict(N=N, full_inverse_lambda_min=float(np.linalg.eigvalsh(B)[-1]),
                degree_N_minus_1_inverse_lambda_min=float(np.linalg.eigvalsh(restricted)[-1]),
                imported_style_vector_inverse_quotient=qfull,
                relative_constraint_violation=float(abs(constraint @ v)/(np.linalg.norm(constraint)*np.linalg.norm(v))))


if __name__ == '__main__':
    report = dict(
        audit='Independent CC exact rational reconstruction and floating Padua/cardinal checks',
        date='2026-10-31', model='gpt-6-astra', effort='xhigh',
        rules_sha='d36722823441dc40c6e19d69a174459348dd309c',
        python=platform.python_version(), numpy=np.__version__, seed=None,
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        exact_CC=[exact_cc(N) for N in range(2, 21)],
        measured_Padua=[padua_measurement(m) for m in range(2, 11)],
        measured_cardinal=[cardinal_measurement(N) for N in (16, 32, 64, 128)],
        scope='Exact CC finite checks are supplementary; analytic proof is required for all N. Padua/cardinal results are floating measurements only.'
    )
    print(json.dumps(report, indent=2))
