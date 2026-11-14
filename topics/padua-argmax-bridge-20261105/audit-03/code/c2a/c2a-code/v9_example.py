import math
src = open('v4_model_grid.py').read().split("print('H0 =',")[0]
ns = {}; exec(src, ns)
for k in ['phase','f','H','bfull','Einf','Cinf','Ec','Bbeta','H0','Cstar','j','t0','v0','bc','J']: globals()[k] = ns[k]
pi = math.pi
for (x, y) in [(0.0, 0.0), (0.4, 0.3), (0.0, 0.4), (0.4, 0.0)]:
    rho, ce, cd, a, u, z, p, q = phase(x, y)
    Ci, _ = Cinf(x, y); ec = Ec(x, y); bb = Bbeta(x, y); bb = bb[0] if isinstance(bb, tuple) else bb
    U0 = ce*f(x-y)+cd*f(x+y)
    print('(x,y)=(%.1f,%.1f): a=%.5f u=%.5f z=%.2e p=%.4f q=%.4f U0=%.5f b_full=%.5f (b_c=%.5f, b_c+3u/pi^2=%.5f) E_inf=%.5f C_inf=%.5f E_c=%.2e B_beta=%.2e  C_inf-C*=%.5f bound(-ju+t0p-(H0+v0)z)=%.5f' % (x, y, a, u, z, p, q, U0, bfull(x, y), bc, bc+3*u/pi**2, Einf(x, y), Ci, ec, bb, Ci-Cstar, -j*u+t0*p-(ns['H0']+v0)*z))
for n in [160, 320]:
    L = math.log(n)
    for (x, y) in [(0.0, 0.0), (0.4, 0.3)]:
        rho, ce, cd, a, u, z, p, q = phase(x, y); Ci, _ = Cinf(x, y)
        print('n=%d (%.1f,%.1f): M_inf = %.4f' % (n, x, y, 4*a/pi**2*L**2+bfull(x, y)*L+Ci))
# Lemma 4.1 worked values
print('J(1,0.5,e) entropy value (any e) =', J(1.0, 0.5, 0.3), ' 2{0.25log0.25+0.75log0.75}=', 2*(0.25*math.log(0.25)+0.75*math.log(0.75)))
print('J(0.5,2,0.1) root regime =', J(0.5, 2.0, 0.1), ' 2s log sin e =', 4*math.log(math.sin(0.1)), '; J(0.5,2,1.2) beyond threshold =', J(0.5, 2.0, 1.2), ' = 4 log sin 1.2 =', 4*math.log(math.sin(1.2)))
