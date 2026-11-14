import math
C=8821/3000; fixed=7/50+2/63
def Lstar(u,fix,dlim=16/25):
    # u(4L^2-3L)/10 + 0.9 + dlim - 0.001 - C - fix = 0
    rhs=(C+fix+0.001-0.9-dlim)*10/u
    return (3+math.sqrt(9+16*rhs))/8
for rho0 in [0.5,0.75,1.0,1.5]:
    u=1-math.cos(rho0/2)
    for fix in [fixed,0.0]:
        L=Lstar(u,fix); print(f"rho0={rho0} u={u:.4f} fixed={fix:.4f} L*={L:.3f} n*~{math.exp(L):.3g}")
print('--- with extra noncorner defect 1/16 credited (fixed errors kept)')
for rho0 in [0.5,1.0]:
    u=1-math.cos(rho0/2); L=Lstar(u,fixed-1/16); print(rho0, round(L,3), f"{math.exp(L):.3g}")
