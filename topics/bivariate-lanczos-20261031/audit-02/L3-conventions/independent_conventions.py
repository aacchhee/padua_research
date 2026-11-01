"""Independent exact audit checks for T302 and N309; no project imports.

Uses SymPy rational/symbolic arithmetic. Unlike the developer checker, the
positive-radius proof uses sqrt(10) < 16/5; simplex projection is certified by
explicit primal feasibility and normal-cone inequalities, not a sorting routine.
"""
import sympy as s

R = s.Rational
x, y = s.symbols('x y')
nodes = [(a, k-a) for k in range(4) for a in range(k+1)]
mon = [x**a * y**(k-a) for k in range(4) for a in range(k+1)]
at = lambda f, z: f.subs({x:z[0], y:z[1]})
V = s.Matrix([[at(p,z) for p in mon] for z in nodes])
t = nodes.index((1,1))
alpha = R(1,1000)
w = s.Matrix([(1-alpha)/9 if i != t else alpha for i in range(10)])
e = s.eye(10)[:,t]
ones = s.ones(10,1)
eps = 2*alpha-alpha**2
theta = R(1,2)
c = w-eps*e
mass = sum(c)
G = sum((ci*s.Matrix([1,*z])*s.Matrix([1,*z]).T for z,ci in zip(nodes,c)),s.zeros(3))
mins = [G[:k,:k].det() for k in range(1,4)]
assert V.det()==576 and all(v>0 for v in mins)
assert mass == (1-alpha)**2
distance = -c[t]/mass
assert distance == R(1,999) and distance>theta*eps
print('N309 point counterexample: det V =',V.det(),'; leading minors =',mins)

q = x*y*(3-x-y)
assert [at(q,z) for z in nodes] == list(e)
derivative_l1 = sum(sum(abs(coef)*4**sum(powers) for powers,coef in s.Poly(s.diff(q,v),x,y).terms()) for v in [x,y])
assert derivative_l1 == 120
d = R(1,10**8)
sqrt10_upper = R(16,5)
assert sqrt10_upper**2>10
lower = (distance-derivative_l1*d)/(1+sqrt10_upper*derivative_l1*d)
gap = s.factor(lower-theta*eps)
assert lower>theta*eps and gap>0
print('N309 positive-radius proof: q =',q,'; gradient bound =',derivative_l1)
print('delta =',d,'; exact rational lower bound =',lower,'; gap over theta epsilon =',gap)

# Explicit KKT/normal-cone certificate for the simplex projection.
# z is the point on the opposite face attained by the outward normal ray.
P = s.eye(10)-ones*ones.T/10
boundary_E = -(10*alpha/9)*P*e
z = w+boundary_E
r_slice_sq = (boundary_E.T*boundary_E)[0]
assert sum(boundary_E)==0 and z[t]==0 and all(a>=0 for a in z)
assert r_slice_sq == 10*alpha**2/9
def certify_projection(k):
    v = w+k*boundary_E
    normal = v-z
    assert all(normal[i]==normal[j] for i in range(10) for j in range(10) if i!=t and j!=t)
    # For every a>=0, sum(a)=1, normal.(a-z)=(normal[t]-normal[j])*a[t]<=0.
    j = 0 if t != 0 else 1
    assert normal[t] <= normal[j]
    return s.factor((normal.T*normal)[0])

for th in [R(0), R(1,2), R(9,10)]:
    k = 1/(1-th)
    d2 = certify_projection(k)
    assert d2 == th**2*k**2*r_slice_sq
    k_above = k*R(1001,1000)
    d2_above = certify_projection(k_above)
    assert d2_above > th**2*k_above**2*r_slice_sq
    # Full cone: analogous outward coordinate ray, projected by zeroing t.
    assert ((k-1)*alpha)**2 == th**2*(k*alpha)**2
    assert ((k_above-1)*alpha)**2 > th**2*(k_above*alpha)**2
    print('threshold equality and strict-failure checks PASS: theta =',th,'; k =',k)

# The same mass-zero perturbation can fail R2 and pass unrestricted-mass R1.
k = R(202,100)
v = w+k*boundary_E
fixed2 = certify_projection(k)
free2 = v[t]**2
budget2 = theta**2*k**2*r_slice_sq
assert free2 <= budget2 < fixed2
print('R2 requires fixed mass: free dist^2 =',free2,'<= budget^2 =',budget2,'< fixed dist^2 =',fixed2)

# Compare r=alpha and r_0=sqrt(10)*alpha/3 with the stated A and B.
r_slice = s.sqrt(10)*alpha/3
A = 1+s.sqrt(10)
B = s.sqrt(10)/alpha
assert s.simplify(alpha-r_slice/(A+B*r_slice))>0
assert r_slice>alpha
print('r/r_0 comparison PASS: r =',alpha,'; r_0 =',r_slice,'; A =',A,'; B =',B)

# Homogeneous cone projection directly checks the R3 scaling identity.
scale = 1/mass
unnorm_dist = eps-alpha
assert scale*unnorm_dist==distance
assert 1-eps*s.sqrt(10)>0
assert s.simplify(theta*eps/(1-eps*s.sqrt(10))-distance)>0
print('R3 identity and upper bound PASS: scale =',scale,'; normalized distance =',distance)
print('ALL INDEPENDENT CHECKS PASS')
