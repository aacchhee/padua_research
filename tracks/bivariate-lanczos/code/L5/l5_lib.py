"""L5 shared library: C Givens (givens_core.c) + imports of the unchanged input module by path.

Input module (unchanged, imported by path):  ../inputs/f6_givens_vs_hl_deficit.py   (alias F)
Build the C core first:  gcc -O2 -ffp-contract=off -shared -fPIC -o libgivens_core.so givens_core.c -lm
"""
import os, sys, ctypes, importlib.util
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
_INP = os.path.join(HERE, "..", "inputs", "f6_givens_vs_hl_deficit.py")
_spec = importlib.util.spec_from_file_location("f6_givens_vs_hl_deficit", _INP)
F = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(F)
LD = F.LD

_lib = ctypes.CDLL(os.path.join(HERE, "libgivens_core.so"))
_dp = np.ctypeslib.ndpointer(dtype=np.float64, flags="C_CONTIGUOUS")
_ip = np.ctypeslib.ndpointer(dtype=np.int32, flags="C_CONTIGUOUS")
_lib.givens_run.argtypes = [_dp, _dp, _dp, ctypes.c_long, _ip, _ip, _ip, _ip,
                            ctypes.c_int, ctypes.c_double, ctypes.c_double, _dp, _dp, _dp]
_lib.givens_run.restype = ctypes.c_int

_RULES = {"scheme": 0, "largest": 1, "smaller": 2}
_tab_cache = {}

def tables(M):
    """prim/alt parent tables for the first M monomials (graded lex, x-power decreasing, 'downside-up' y-parent first)."""
    if M not in _tab_cache:
        ms, prim, alt = F.parents(M)
        pi = np.zeros(M, np.int32); pv = np.zeros(M, np.int32); ai = -np.ones(M, np.int32); av = np.zeros(M, np.int32)
        for j in range(1, M):
            pi[j], pv[j] = prim[j]
            if alt[j] is not None: ai[j], av[j] = alt[j]
        _tab_cache[M] = (pi, pv, ai, av)
    return _tab_cache[M]

def givens_c(x, y, v, rule="scheme", tol=0.0):
    """returns (Hx, Hy, stats) full M x M, stats = (n_rot, n_skip, n_alt_pivot_taken)."""
    x = np.ascontiguousarray(x, float); y = np.ascontiguousarray(y, float); v = np.ascontiguousarray(v, float)
    M = len(x); pi, pv, ai, av = tables(M)
    Hx = np.empty((M, M)); Hy = np.empty((M, M)); st = np.zeros(3)
    scale = max(np.abs(x).max(), np.abs(y).max(), np.abs(v).max())
    _lib.givens_run(x, y, v, M, pi, pv, ai, av, _RULES[rule], tol, scale, Hx, Hy, st)
    return Hx, Hy, st

# R03 extension (givens_run2: pair-norm / kappa pivot rules); built as libgivens_core2.so from the same source
try:
    _lib2 = ctypes.CDLL(os.path.join(HERE, "libgivens_core2.so"))
    _lib2.givens_run2.argtypes = [_dp, _dp, _dp, ctypes.c_long, _ip, _ip, _ip, _ip, ctypes.c_int, ctypes.c_double, _dp, _dp, _dp]
    _lib2.givens_run2.restype = ctypes.c_int
    _lib2.givens_insert.argtypes = [_dp, _dp, _dp, ctypes.c_long, ctypes.c_long, ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                    _ip, _ip, _ip, _ip, ctypes.c_int, ctypes.c_double, _dp]
    _lib2.givens_insert.restype = ctypes.c_int
except OSError:
    _lib2 = None

def givens_insert(Hx, Hy, w, i, xi, yi, vi, M, rule=0, kappa=1.0):
    """in-place insertion of one point into slot i of the state arrays (M x M, M x M, M); returns the smallest |pivot| over monomials 0..i."""
    pi, pv, ai, av = tables(M); mp = np.zeros(1)
    _lib2.givens_insert(Hx, Hy, w, M, i, xi, yi, vi, pi, pv, ai, av, rule, kappa, mp)
    return float(mp[0])

def givens_c2(x, y, v, rule, kappa=1.0):
    """rule 3: alt pair if hypot(alt) > kappa*hypot(primary); rule 4: alt if |alt pivot| > kappa*|primary pivot| (kappa=1 is 'largest').
    returns Hx, Hy, stats = (n_rot, n_skip, n_alt, n_noise_rotations(r<1e-10))."""
    x = np.ascontiguousarray(x, float); y = np.ascontiguousarray(y, float); v = np.ascontiguousarray(v, float)
    M = len(x); pi, pv, ai, av = tables(M)
    Hx = np.empty((M, M)); Hy = np.empty((M, M)); st = np.zeros(4)
    _lib2.givens_run2(x, y, v, M, pi, pv, ai, av, rule, kappa, Hx, Hy, st)
    return Hx, Hy, st

# ---------------------------------------------------------------- node sets and weights
def padua_cubature(n):
    """Padua points (first family) and the cubature weights (sum 1, normalised Chebyshev measure) of padua_weights_check.py."""
    pts, w = [], []
    for j in range(n + 1):
        for k in range(n + 2):
            if (j + k) % 2 == 0:
                pts.append((np.cos(j * np.pi / n), np.cos(k * np.pi / (n + 1))))
                ej = 0.5 if j in (0, n) else 1.0; ek = 0.5 if k in (0, n + 1) else 1.0
                w.append(2 * ej * ek / (n * (n + 1)))
    return np.array(pts), np.array(w)

def rel_err_H(Hx, Hy, Hxr, Hyr, N):
    """relative Frobenius error of the leading N x N blocks of (Hx, Hy) (same formula as F.errs, H part)."""
    Hx = Hx[:N, :N]; Hy = Hy[:N, :N]
    nH = np.sqrt(np.sum(Hxr ** 2) + np.sum(Hyr ** 2))
    return float(np.sqrt(np.sum((Hx - Hxr) ** 2) + np.sum((Hy - Hyr) ** 2)) / nH)

def reference_H(x, y, v, N):
    """long-double 3-pass full-reorthogonalised reference (F.reference), sign-fixed (positive primary pivots); returns double Hxr, Hyr."""
    Qr = F.reference(x, y, v, N)
    Qr, Hxr, Hyr = F.fixsign(Qr, N, x=x.astype(LD), y=y.astype(LD))
    return Hxr.astype(float), Hyr.astype(float)

def method_H(name, x, y, v, N):
    """H error input: returns sign-fixed (Hx, Hy) leading N x N for a method name."""
    if name in ("givens-scheme", "givens-largest"):
        Hx, Hy, st = givens_c(x, y, v, rule=name.split("-")[1])
        Q = np.zeros((len(x), N)); Q[:N, :N] = np.eye(N)  # dummy Q; fixsign with H given only uses H
        _, Hx, Hy = F.fixsign(Q, N, Hx[:N, :N], Hy[:N, :N])
        return Hx, Hy
    if name == "hl":   Q = F.krylov(x, y, v, N, window=True, reorth=True, mgs=True)
    elif name == "bj": Q = F.krylov(x, y, v, N, window=True, reorth=False, mgs=False)
    elif name == "cgs2": Q = F.krylov(x, y, v, N, window=False, reorth=True, mgs=False)
    elif name == "hh": Q = F.householder(x, y, v, N)
    else: raise ValueError(name)
    _, Hx, Hy = F.fixsign(Q, N, x=x, y=y)
    return Hx, Hy
