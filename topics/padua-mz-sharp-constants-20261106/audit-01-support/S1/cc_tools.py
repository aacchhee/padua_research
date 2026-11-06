"""Independent CC tools for the S1 audit (Claude). Lebesgue CC, N+1 nodes cos(k pi/N)."""
import numpy as np
from scipy.fft import dct


def mu(k):
    k = np.asarray(k)
    out = np.zeros(k.shape)
    e = (k % 2) == 0
    out[e] = 2.0 / (1.0 - k[e].astype(float) ** 2)
    return out


def cheb_coeffs(v):
    """Chebyshev coefficients b_0..b_M of the degree-M interpolant of values v at cos(k pi/M)."""
    M = len(v) - 1
    b = dct(v, type=1) / M
    b[0] /= 2
    b[-1] /= 2
    return b


def cc_weights(N):
    # w_k = int ell_k = sum_j mu_j * d b_j/d v_k ; cheb_coeffs is linear: b = H C v /N.
    # Equivalent: w = (1/N) * e_k-halved DCT-I of (H mu). Verified against Vandermonde below.
    # b = A v with A_jk = (2 e_j e_k / N) cos(jk pi/N), e_0=e_N=1/2 => w_k = (e_k/N) dct1(mu)_k
    m = mu(np.arange(N + 1))
    w = dct(m, type=1) / N
    w[0] /= 2
    w[-1] /= 2
    return w


def eval_on_grid(b, M):
    """Values of sum b_i T_i at cos(j pi/M), j=0..M, M>=deg."""
    c = np.zeros(M + 1)
    c[: len(b)] = b
    # sum_i c_i cos(i j pi/M) = (dct1(c)_j + c_0 + (-1)^j c_M)/2
    y = dct(c, type=1)
    sgn = (-1.0) ** np.arange(M + 1)
    return (y + c[0] + sgn * c[M]) / 2


def l2_norm_sq(b):
    """Exact (up to rounding) int_{-1}^1 p^2 dx for p = sum b_i T_i."""
    n = len(b) - 1
    M = 2 * n + 2
    vals = eval_on_grid(b, M)
    cb = cheb_coeffs(vals ** 2)
    return float(cb @ mu(np.arange(M + 1)))


def l2_norm_sq_TH(b):
    """Alternative: b^T M b with M_ij=(mu_|i-j|+mu_{i+j})/2 via FFT correlations."""
    from scipy.signal import fftconvolve
    n = len(b) - 1
    conv = fftconvolve(b, b)            # index s=i+j, 0..2n
    corr = fftconvolve(b, b[::-1])      # index n+(i-j)
    s = np.arange(2 * n + 1)
    hank = conv @ mu(s)
    d = np.abs(np.arange(-n, n + 1))
    toep = corr @ mu(d)
    return float((hank + toep) / 2)


def selftest():
    from numpy.polynomial import chebyshev as C
    for N in [6, 7, 20, 33]:
        x = np.cos(np.arange(N + 1) * np.pi / N)
        w = cc_weights(N)
        # exactness on T_j, j<=N
        for j in range(N + 1):
            Tj = np.cos(j * np.arange(N + 1) * np.pi / N)
            assert abs(w @ Tj - mu(np.array([j]))[0]) < 1e-12, (N, j)
        rng = np.random.default_rng(1)
        v = rng.standard_normal(N + 1)
        b = cheb_coeffs(v)
        assert np.allclose(C.chebval(x, b), v)
        # exact L2 via numpy integration
        p2 = C.chebmul(b, b)
        P = C.chebint(p2)
        exact = C.chebval(1, P) - C.chebval(-1, P)
        assert abs(l2_norm_sq(b) - exact) < 1e-10 * max(1, exact)
        assert abs(l2_norm_sq_TH(b) - exact) < 1e-10 * max(1, exact)
    print("selftest ok")


if __name__ == "__main__":
    selftest()
