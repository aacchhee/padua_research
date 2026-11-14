import numpy as np
exec(open('c4c_scalar.py').read().split("# F_0 on the origin")[0].split("# scalar profile facts")[0])
for eps in (1e-2, 3e-3, 1e-3):
    w = np.linspace(-np.pi+eps, np.pi-eps, 400001)
    fpw = fp(w)
    V = np.sum(np.abs(np.diff(fpw)))
    jump = abs(fp(np.array([-np.pi+eps]))[0] - fp(np.array([np.pi-eps]))[0])
    print(f"eps={eps}: Var on interior {V:.4f}, endpoint jump {jump:.4f}, total {V+jump:.4f} (<4 claimed); sup|f'|={np.max(np.abs(fpw)):.4f} (<6/pi={6/np.pi:.4f})")
print("J0 = 2(log pi - gamma)/pi =", 2*(np.log(np.pi)-np.euler_gamma)/np.pi)
