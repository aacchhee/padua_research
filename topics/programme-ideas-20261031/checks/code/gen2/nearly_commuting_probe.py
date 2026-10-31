import numpy as np
exec(open('sturm_pair_check.py').read().split('def count_box')[0])  # reuse setup (Hx,Hy,x,y,N,deg)
rng2 = np.random.default_rng(7)
pat = (np.abs(deg[:,None]-deg[None,:]) <= 1)
def inertia(Mat):
    S = 0.5*(Mat+Mat.T); return int((np.linalg.eigvalsh(S) > 0).sum())
def joint_count(Hx,Hy,a,a2,b,b2):
    I=np.eye(N); Mx=(Hx-a*I)@(a2*I-Hx); My=(Hy-b*I)@(b2*I-Hy)
    return (inertia(Mx@My)-N+inertia(Mx)+inertia(My))//2
# distance of box boundary to nearest node
boxes=[(-1,0,-1,0),(-0.5,0.5,-0.5,0.5),(-0.3,0.3,0.2,0.9)]
for delta in [1e-12,1e-8,1e-5,1e-3,1e-2]:
    Ex=rng2.standard_normal((N,N)); Ex=(Ex+Ex.T)/2*pat; Ey=rng2.standard_normal((N,N)); Ey=(Ey+Ey.T)/2*pat
    Hxp=Hx+delta*Ex/np.linalg.norm(Ex); Hyp=Hy+delta*Ey/np.linalg.norm(Ey)
    comm=np.linalg.norm(Hxp@Hyp-Hyp@Hxp)
    res=[]
    for (a,a2,b,b2) in boxes:
        true=int(((x>a)&(x<a2)&(y>b)&(y<b2)).sum())
        d=min(np.min(np.abs(np.r_[x-a,x-a2])),np.min(np.abs(np.r_[y-b,y-b2])))
        res.append((true,joint_count(Hxp,Hyp,a,a2,b,b2),f"{d:.2e}"))
    print(f"delta={delta:.0e} ||[.,.]||={comm:.1e}  (true,count,mindist): {res}")
