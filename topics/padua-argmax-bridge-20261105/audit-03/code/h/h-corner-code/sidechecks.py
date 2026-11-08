# MEASURED side checks of exact identities used/stated in H, PD-T159 (paper cu:square,
# cu:deform), H03 (1)-(3), and H04 (9) derivative bounds. Exact identities are tested at
# 40 digits for small n; this is a finite-n consistency check, not a proof.
import mpmath as mp
import brute
mp.mp.dps = 40
pi = mp.pi

def f(u, v):
    return (1 + mp.cos(v))/abs(mp.cos(u) - mp.cos(v))

def square_check(n):
    th = lambda j: j*pi/n
    eps = lambda j: mp.mpf(1)/2 if j in (0, n) else 1
    S = mp.fsum(eps(j)*eps(k)*f(th(j), th(k)) for j in range(n+1) for k in range(n+1) if (j+k) % 2)
    L = (mp.mpf(2)/n)*mp.fsum((mp.mpf(1)/2 if r == n else 1)/mp.sin(r*pi/(2*n)) for r in range(1, n+1, 2))
    return 4*S/n**2 - L**2

def deform_check(n):
    m = n+1; worst = mp.mpf(0)
    for j in range(n+1):
        for k in range(n+1):
            if (j+k) % 2 == 0: continue
            l = abs(j-k)
            diff = abs(f(j*pi/n, k*pi/m) - f(j*pi/n, k*pi/n))
            worst = max(worst, diff/(pi**2*n/(2*l**2)))
    return worst  # must be <= 1

def h03_check(n):
    m = n+1; Q = n*m; a = 2*n+1
    x = lambda j: mp.cos(j*pi/n); y = lambda k: mp.cos(k*pi/m)
    eps = lambda j: mp.mpf(1)/2 if j in (0, n) else 1
    eta = lambda k: mp.mpf(1)/2 if k in (0, m) else 1
    s1 = mp.fsum(eps(j)*eta(k)*(2+x(j)+y(k))/abs(x(j)-y(k))
                 for j in range(n+1) for k in range(m+1) if (j+k) % 2 and (j, k) != (n, m))
    L1 = 2*s1/Q + mp.mpf(1)/(2*Q)
    qd = lambda dd: pi*dd/(2*Q)
    K = lambda dd: (1 - mp.cos(a*qd(dd))*mp.cos(qd(dd)))/(abs(mp.sin(a*qd(dd)))*mp.sin(qd(dd)))
    Kt = lambda dd: (1 - mp.cos(a*qd(dd))*mp.cos(qd(dd)))/(mp.sin(a*qd(dd))*mp.sin(qd(dd)))
    L2 = (1 + mp.fsum(K(dd) for dd in range(1, 2*Q)))/(2*Q)
    st = mp.fsum(Kt(dd) for dd in range(1, 2*Q))
    return L1, L2, st - (4*n**2 + 2*n - 1)

if __name__ == "__main__":
    for n in list(range(2, 16)) + [24, 31]:
        Lb = brute.rowformula(n)
        L1, L2, st = h03_check(n)
        print(n, "square:", mp.nstr(square_check(n), 3), " deform max ratio:", mp.nstr(deform_check(n), 6),
              " H03(1)-row:", mp.nstr(L1-Lb, 3), " H03(2)-row:", mp.nstr(L2-Lb, 3), " H03(3) signed-sum resid:", mp.nstr(st, 3))
    # H04 (9): sup |W''| on [0,1], W(t)=t cot(pi t/2)
    W = lambda t: t*mp.cot(pi*t/2) if t != 0 else 2/pi
    mx = max(abs(mp.diff(W, mp.mpf(i)/200, 2)) for i in range(1, 201))
    mx1 = max(abs(mp.diff(W, mp.mpf(i)/200, 1)) for i in range(1, 201))
    print("H04: sup|W'| ~", mp.nstr(mx1, 6), " sup|W''| ~", mp.nstr(mx, 6), "(claimed <3, <5)")
    Bf = lambda x: mp.cot(pi*x) - 1/(pi*x) + 1/(pi*(1-x))
    pts = [mp.mpf(-1)/4 + mp.mpf(i)*(mp.mpf(3)/2)/400 for i in range(401)]
    pts = [p for p in pts if p not in (0, 1)]
    print("H04: sup|B'| on [-1/4,5/4] ~", mp.nstr(max(abs(mp.diff(Bf, p, 1)) for p in pts), 6),
          " sup|B''| ~", mp.nstr(max(abs(mp.diff(Bf, p, 2)) for p in pts), 6), "(claimed <=3, <=5)")
