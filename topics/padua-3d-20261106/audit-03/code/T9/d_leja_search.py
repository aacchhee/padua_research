# Is the (3.5) sequence the no-repeat real projection of SOME Leja sequence on U initiated at 1?
# Leja sequences initiated at 1: E_{2^{n+1}} = E_{2^n} ^ rho_n E_{2^n}, rho_n any 2^n-th root of -1 (source Thm 2.2 characterization).
import numpy as np, math, cmath
def rleja35(K):
    r=[1.0,-1.0,0.0]; j=2
    while len(r)<K:
        a=math.sqrt((r[j]+1)/2); r+=[a,-a]; j+=1
    return np.array(r[:K])
def proj(E):
    out=[]
    for z in E:
        if all(abs(z.real-y)>1e-11 for y in out): out.append(z.real)
    return np.array(out)
LEV=10; target=rleja35(2**LEV+1)
cands=[[1+0j]]  # keep all partial E consistent with target
for n in range(LEV):
    new=[]
    for E in cands:
        for m in range(2**n):
            rho=cmath.exp(1j*math.pi*(2*m+1)/2**n)
            E2=E+[rho*z for z in E]
            p=proj(E2)
            if len(p)==2**(n+1)//2+1 or True:
                L=len(p)
                if np.allclose(p,target[:L],atol=1e-10): new.append(E2)
    # keep at most a few to bound cost
    cands=new[:4]
    print("level",n+1,"len E",2**(n+1),"consistent choices kept",len(new), "proj length",len(proj(cands[0])) if cands else None)
    if not cands: break
F=[1+0j]
for n in range(LEV):
    F=F+[cmath.exp(1j*math.pi/2**n)*z for z in F]
pF=proj(F); first=np.where(~np.isclose(pF,target[:len(pF)],atol=1e-10))[0]
print("source F projection first mismatch index vs (3.5):",first[:4], "values",pF[first[:2]],target[first[:2]])
Fc=[1+0j]
for n in range(LEV):
    Fc=Fc+[cmath.exp(-1j*math.pi/2**n)*z for z in Fc]
print("conjugate-rho F' projection equals (3.5):",np.allclose(proj(Fc),target[:len(proj(Fc))],atol=1e-10))
