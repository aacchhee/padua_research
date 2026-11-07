# Test: F_{2^{n+1}} = F_{2^n} ^ e^{i pi/2^n} * conj(F_{2^n}) (a Leja sequence by source Thm 2.1, since conj of a Leja section from 1 is one)
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
LEV=14
F=[1+0j]
for n in range(LEV):
    F=F+[cmath.exp(1j*math.pi/2**n)*z.conjugate() for z in F]
# Leja property direct check on first 2^9 points: e_k maximizes prod|z-e_j| over circle (compare with value 2^{sigma1(k)} from Thm 2.2)
ok=True
for k in range(1,513):
    val=np.prod([abs(F[k]-F[j]) for j in range(k)])
    ok &= abs(val-2**bin(k).count('1'))<1e-6*val
print("conj-F satisfies |w_{E_k}(e_k)|=2^sigma1(k) for k<=512:",ok)
p=proj(F); t=rleja35(len(p))
print("projection length",len(p),"equals (3.5):",np.allclose(p,t,atol=1e-10))
