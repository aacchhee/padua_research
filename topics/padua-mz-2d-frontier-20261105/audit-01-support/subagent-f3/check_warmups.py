import numpy as np, math
PI = math.pi
def cc_weights(N):
    # Clenshaw-Curtis weights on cos(j pi/N), j=0..N, exact for degree<=N, dx on [-1,1]
    j = np.arange(N+1); th = j*PI/N
    w = np.zeros(N+1)
    for i in range(N+1):
        s = 0.0
        for k in range(0, N+1, 2):
            ck = 1.0 if k in (0, N) else 2.0
            s += ck*math.cos(k*th[i])*(2.0/(1-k*k))
        w[i] = s/N*(0.5 if i in (0, N) else 1.0)
    return np.cos(th), w
xg, wg = np.polynomial.legendre.leggauss(600)
def cheb(c, x): return np.polynomial.chebyshev.chebval(x, c)
print("1D sign-discard: N, ratio |a|A|a|/aMa, bound 32(2+log2N)/L, ||q||^2 exact formula vs quad, ||p||^2 >= L/16")
for L in [1, 2, 5, 10, 30, 100, 250]:
    N = 2*L+1
    a = np.zeros(N); a[0::2] = (-1.0)**np.arange(L+1)
    x, w = cc_weights(N)
    q = np.abs(a);
    Mq = np.sum(wg*cheb(q, xg)**2); Ma = np.sum(wg*cheb(a, xg)**2)
    Rq = np.sum(w*cheb(q, x)**2); Ra = np.sum(w*cheb(a, x)**2)
    assert abs(np.sum(w)-2) < 1e-12 and w.min() > 0
    num = 2*Mq-Rq
    exact_q = 0.5+1/N+0.5*sum(1/(2*k+1) for k in range(N))
    print(N, round(num/Ma, 6), round(32*(2+math.log(2*N))/L, 3), round(Mq-exact_q, 12), Ma >= L/16, num > 0, "actual signed ratio", round((2*Ma-Ra)/Ma, 4))
print("harmonic escape: N, max|p_N(cos t)|/(pi N) on (0,pi/2], endpoint mass/(pi^2K^2) for K=1,5, ||p_N||^2, C_N(p^2)/||p||^2")
for N in [3, 4, 9, 20, 61, 200, 401]:
    Mh = (N-1)//2
    def pN(t):
        out = np.zeros_like(t)
        for j in range(1, Mh+1):
            out += (np.sin((N-2*j)*t)-(1-2*j/N)*np.sin(N*t))/j
        return out/np.sin(t)
    t = np.linspace(1e-6, PI/2, 20000)
    r5 = np.max(np.abs(pN(t)))/(PI*N)
    xg2, wg2 = np.polynomial.legendre.leggauss(400)
    ems = []
    for K in [1, 5]:
        if K/N > PI/2: ems.append(None); continue
        tt = (xg2+1)*(K/N)/2; ww = wg2*(K/N)/2
        ems.append(round(2*np.sum(ww*pN(tt)**2*np.sin(tt))/(PI**2*K**2), 4))
    tq = (xg+1)*PI/2; wq = wg*PI/2
    nrm = np.sum(wq*np.sin(tq)*pN(tq)**2)
    x, w = cc_weights(N)
    tn = np.arccos(np.clip(x, -1, 1)); vals = np.where(np.abs(np.sin(tn)) < 1e-12, 0.0, 0.0)
    inner = (np.abs(np.sin(tn)) > 1e-12)
    vals[inner] = pN(tn[inner])
    print(N, round(r5, 4), ems, round(nrm, 4), round(np.sum(w*vals**2)/nrm, 5))
