"""Claude audit-01 auditor B: MEASURED float64/quadrature check that zero/small-phase projected defects
Qv, Qh (gated-01 formula (B) and its horizontal analogue) approach g_v(phi), g_h(theta) (codex-04/05 integrals),
independent of the unused coordinate; g_v(pi/2) vs PD-T188 enclosure; lower bounds c_delta; gated-05 d_delta.
Own numpy kernel (U-product with removable limits) and own scipy quadrature."""
import numpy as np, json
from scipy import integrate
def U(k, z):
    s = np.sin(z); c = np.cos(z)
    with np.errstate(divide='ignore', invalid='ignore'):
        val = np.sin(k*z)/s
    lim = k*np.cos(k*z)/c
    return np.where(np.abs(s) < 1e-13, lim, val)
def D(n, u, v):
    S, T = (u+v)/2, (v-u)/2
    return U(n+1, S)*U(n+1, T) + U(n, S)*U(n, T)
def G(n, u, v):
    return D(n, u, v) - np.cos(n*u)
def Qv(n, J, K, al, be):
    m = n+1; phi = K*np.pi/m + be/m
    k = np.arange(m+1); f = np.where((k == 0) | (k == m), .5, 1.)
    j = np.arange(2*n)
    jj, kk = np.meshgrid(j, k, indexing='ij')
    mask = ((jj + kk) % 2) == (J % 2)
    u = jj*np.pi/n + al/n; b = kk*np.pi/m
    sg = (-1.0)**jj
    Hp = sg*G(n, u, phi + b)/2; Hm = sg*G(n, u, phi - b)/2
    d = np.abs(Hp) + np.abs(Hm) - np.abs(Hp + Hm)
    return float((d*mask*f[None, :]).sum()/(n*m))
def Qh(n, J, K, al, be):
    m = n+1; th = J*np.pi/n + al/n
    j = np.arange(n+1); e = np.where((j == 0) | (j == n), .5, 1.)
    r = np.arange(2*m)
    jj, rr = np.meshgrid(j, r, indexing='ij')
    mask = ((jj + rr) % 2) == (K % 2)
    v = rr*np.pi/m + be/m; a = jj*np.pi/n
    # common sign (-1)^(shifted first index) is common to both halves: (J+j) and (J-j) have same parity
    Hp = G(n, th + a, v)/2; Hm = G(n, th - a, v)/2
    d = np.abs(Hp) + np.abs(Hm) - np.abs(Hp + Hm)
    return float((d*mask*e[:, None]).sum()/(n*m))
def gv(beta):
    def inner(b):
        lo = abs(beta - b); hi = beta + b
        if hi > np.pi: hi = 2*np.pi - hi
        if hi <= lo: return 0.
        zp, zm = np.cos(beta + b), np.cos(beta - b)
        fun = lambda u: min((1 + zp)/(np.cos(u) - zp), (1 + zm)/(zm - np.cos(u)))
        return integrate.quad(fun, lo, hi, limit=200, points=[(lo+hi)/2])[0]
    return 2/np.pi**2*integrate.quad(inner, 0, np.pi, limit=400, points=[beta, np.pi - beta])[0]
def gh(alpha):
    def inner(a):
        lo = abs(alpha - a); hi = alpha + a
        if hi > np.pi: hi = 2*np.pi - hi
        if hi <= lo: return 0.
        zp, zm = np.cos(alpha + a), np.cos(alpha - a)
        fun = lambda b: (1 + np.cos(b))*min(1/(np.cos(b) - zp), 1/(zm - np.cos(b)))
        return integrate.quad(fun, lo, hi, limit=200, points=[(lo+hi)/2])[0]
    return 2/np.pi**2*integrate.quad(inner, 0, np.pi, limit=400, points=[alpha, np.pi - alpha])[0]
out = {}
betas = [np.pi/8, np.pi/4, np.pi/3, np.pi/2, 2*np.pi/3, 3*np.pi/4]
out['gv'] = {f'{b:.6f}': gv(b) for b in betas}
out['gh'] = {f'{b:.6f}': gh(b) for b in betas}
out['gv_pi2_vs_PD-T188_enclosure'] = [out['gv'][f'{np.pi/2:.6f}'], 0.548504986190, 0.548525055355]
conv = []
for n in (63, 64, 255, 256, 1023, 1024):
    m = n+1
    for b in (np.pi/4, np.pi/2, 3*np.pi/4):
        K = int(round(m*b/np.pi))
        vals = []
        for J in (K % 2 == 0 and [1, n//2 | 1, n - 1 if (n-1) % 2 else n] or [0, 2*(n//4), n if n % 2 == 0 else n-1]):
            if (J + K) % 2 == 0: J += 1
            for (al, be) in ((0., 0.), (1/np.log(n)**2, -0.5/np.log(n)**2)):
                vals.append(Qv(n, J, K, al, be))
        conv.append({'n': n, 'phi': K*np.pi/m, 'Qv_values_over_theta_and_phase': vals, 'gv(phi)': gv(K*np.pi/m)})
        J = int(round(n*b/np.pi)); valsh = []
        for K2 in (1, m//2, m - 1):
            if (J + K2) % 2 == 0: K2 += 1
            for (al, be) in ((0., 0.), (1/np.log(n)**2, -0.5/np.log(n)**2)):
                valsh.append(Qh(n, J, K2, al, be))
        conv.append({'n': n, 'theta': J*np.pi/n, 'Qh_values_over_phi_and_phase': valsh, 'gh(theta)': gh(J*np.pi/n)})
out['convergence'] = conv
# c_delta and gated-05 d_delta vs actual Q at radius rho_delta, n>=N_delta
fin = []
for delta in (np.pi/8, np.pi/4, 1.2):
    kap = 1 - np.cos(delta/2); rho = kap/4; Nd = int(np.ceil(16*np.pi/delta)); dd = delta**2*kap/(256*np.pi**2)
    cd = delta**2*kap/(16*np.pi**2)
    grid = np.linspace(delta, np.pi - delta, 9)
    mg = min(gv(b) for b in grid); mgh = min(gh(b) for b in grid)
    worst = np.inf
    for n in (Nd, Nd + 1, 2*Nd + 1):
        m = n+1
        for b in grid:
            K = int(np.clip(round(m*b/np.pi), 0, m))
            phi = K*np.pi/m
            if not (delta <= phi <= np.pi - delta): continue
            J = 0 if K % 2 else 1
            for (al, be) in ((rho, 0.), (-rho/2, rho/2), (0., -rho)):
                worst = min(worst, Qv(n, J, K, al, be))
            Jh = int(np.clip(round(n*b/np.pi), 0, n)); th = Jh*np.pi/n
            if not (delta <= th <= np.pi - delta): continue
            Kh = 0 if Jh % 2 else 1
            for (al, be) in ((rho, 0.), (-rho/2, rho/2), (0., -rho)):
                worst = min(worst, Qh(n, Jh, Kh, al, be))
    fin.append({'delta': delta, 'c_delta': cd, 'min_grid_gv': mg, 'min_grid_gh': mgh, 'N_delta': Nd,
                'd_delta': dd, 'min_sampled_Q_at_radius': worst})
out['finite_block'] = fin
print(json.dumps(out, indent=1))
