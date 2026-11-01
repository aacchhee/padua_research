"""Independent bounded exact checks, Codex mathematical audit 2026-11-01.

No developer or previous reviewer module is imported. SymPy exact arithmetic is
trusted. These checks supplement the proofs and do not establish generality.
Run from the repository root with python3 -I <this path>.
"""
import json
import platform
import sympy as s
import numpy as np

R = s.Rational
results = {}


def zero(a):
    assert all(s.simplify(v) == 0 for v in a), a


def indices(n):
    return [(t, j) for t in range(n + 1) for j in range(t + 1)]


def graded(xs, ys, n):
    vs = []
    for t, j in indices(n):
        v = s.Matrix([x ** (t - j) * y ** j for x, y in zip(xs, ys)])
        for q in vs:
            v -= q * ((q.T * v)[0] / (q.T * q)[0])
        assert (v.T * v)[0] > 0
        vs.append(v)
    return vs


# Sheared tensor grid: distinct rational nodes, uniform positive weights, U(3).
grid = [R(-3, 3), R(-1, 3), R(1, 3), R(3, 3)]
xs = [x for x in grid for y in grid]
ys = [y + x / 2 for x in grid for y in grid]
V = graded(xs, ys, 3)
idx = indices(3)
pos = {ij: k for k, ij in enumerate(idx)}
X, Y = s.diag(*xs), s.diag(*ys)
outside = 0
for k, (t, j) in enumerate(idx):
    if t > 2:
        continue
    for op, shift in ((X, 0), (Y, 1)):
        for l, (d, i) in enumerate(idx):
            allowed = (d == t - 1 and i >= j - shift) or d == t or (d == t + 1 and i <= j + shift)
            if not allowed:
                zero(V[l].T * op * V[k])
                outside += 1
results['101_exact_structural_zeros'] = outside

# L4 affine codimension and the claimed staggered sum with orthogonalized starts.
for n in (1, 2):
    S = s.Matrix.hstack(*V[:len(indices(n))])
    A = X + R(2, 3) * Y + s.eye(len(xs)) / 7
    AS = A * S
    codim = s.Matrix.hstack(S, AS).rank() - AS.rank()
    assert codim == n + 1
    starts = [V[pos[(a, 0)]] for a in range(n + 1)]
    K = s.Matrix.hstack(*[Y**b * starts[a] for a in range(n + 1) for b in range(n - a + 1)])
    assert K.rank() == S.rank() == s.Matrix.hstack(S, K).rank()
    results[f'401_n{n}_affine_codimension'] = codim
    results[f'401_n{n}_orthogonalized_staggered_starts_rank'] = K.rank()

# 108: pencil and normalization, with exact orthonormal polynomial values.
Q = s.Matrix.hstack(*[v / s.sqrt((v.T*v)[0]) for v in V])
n = 2
N, P = len(indices(n)), len(indices(n - 1))
QQ = Q[:, :N]
HX, HY = QQ.T * X * Q[:, :P], QQ.T * Y * Q[:, :P]
x, y = R(2, 7), R(-3, 8)
embed = s.eye(N)[:, :P]
pencil = (x * embed - HX).T.col_join((y * embed - HY).T)
normrow = s.zeros(1, N)
normrow[0, 0] = 1
assert pencil.rank() == N - 1
assert normrow.col_join(pencil).rank() == N
L = s.zeros(N)
L[0, 0] = 1
for k, (t, j) in enumerate(indices(n)[1:], 1):
    parent = pos[(t - 1, 0)] if j == 0 else pos[(t - 1, j - 1)]
    row = parent if j == 0 else P + parent
    for l in range(N):
        L[k, l] = -pencil[row, l]
    assert L[k, k] > 0
    zero(L[k, k + 1:])
solution = L.inv()[:, 0]
zero(pencil * solution)
results['108_pencil_shape_rank'] = [*pencil.shape, pencil.rank()]
results['108_normalized_pencil_shape_rank'] = [pencil.rows+1, N, normrow.col_join(pencil).rank()]

# Parent of degree one less is insufficient: selecting X*q_(1,1) for
# target (2,0) has a later (2,1) nonzero. Valid selection must match the
# target monomial (or satisfy triangular support and nonzero pivot).
wrong = -pencil[pos[(1, 1)], :]
assert wrong[pos[(2, 1)]] != 0
results['108_degree_only_parent_counterexample_later_coefficient'] = str(s.simplify(wrong[pos[(2, 1)]]))

# Actual exchange of coordinates changes the ordered basis, unlike changing
# admissible parents while keeping the same monomial order.
W = graded(ys, xs, 1)
corr = s.simplify((V[1].T*W[1])[0] / s.sqrt((V[1].T*V[1])[0]*(W[1].T*W[1])[0]))
assert corr**2 == R(1, 5)
results['108_variable_swap_first_degree_overlap'] = str(corr)

# 103: exact complex symmetric instance, including dense skew part K.
M, m, q, r, b = 6, 4, 2, 2, 1
Qh = s.Matrix(M, m, lambda i, j: R(((i+2)*(j+3)) % 11 - 5, 7))
Qp = s.Matrix(M, q, lambda i, j: R(((i+1)*(j+4)) % 7 - 3, 5))
A = s.diag(*[R(i-2, 3)+s.I*R(i % 3, 5) for i in range(M)])
S = s.Matrix(m, m, lambda i,j: R(i+j+1, 9)*(1+s.I) if abs(i-j) <= b else 0)
K = s.Matrix(m, m, lambda i,j: R(i-j, 13)*(1-2*s.I))
T = S+K
B = s.Matrix(q, m, lambda i,j: R(i+j+1, 11) if j >= m-r else 0)
E = A*Qh-Qh*T-Qp*B
C, c = Qh.T*Qh, Qh.T*Qp
G = C-s.eye(m)
D = s.diag(*[G[i,i] for i in range(m)])
U = s.Matrix(m,m,lambda i,j: C[i,j] if j>i else 0)
Ul = s.Matrix(m,m,lambda i,j: U[i,j] if 0<j-i<=b else 0)
part = lambda Z, pred: s.Matrix(m,m,lambda i,j: Z[i,j] if pred(i,j) else 0)
up = lambda Z: part(Z,lambda i,j:j>i)
lo = lambda Z: part(Z,lambda i,j:i>j)
dg = lambda Z: part(Z,lambda i,j:i==j)
ld = lambda Z: part(Z,lambda i,j:i>=j)
Z = Ul*S-S*Ul
Phi = E.T*Qh-Qh.T*E-2*K-G*K-K*G
Omega = lo(Z)+lo(Z).T+dg(Z)-up(D*S-S*D)+up(B.T*c.T)+ld(c*B)+up(Phi)
zero(U*S-S*U-Omega+c*B)
results['103_matrix_identity_complex_dense_skew'] = 'exact zero'

# 104/106: arbitrary rational recurrence with nonorthogonal computed columns
# and nonzero local errors. No polynomial or unisolvence assumption is used.
n = 3
idx = indices(n)
pos = {ij:k for k,ij in enumerate(idx)}
N, P, M = len(idx), len(indices(n-1)), 5
X = s.diag(*[R(i-2, 5) for i in range(M)])
Y = s.diag(*[R(i*i-4, 9) for i in range(M)])
Q = s.zeros(M,N)
Q[:,0] = s.ones(M,1)/3
records = {}
TF, EF = s.zeros(N,P), s.zeros(M,P)
for k,(t,j) in enumerate(idx[1:],1):
    parent = pos[(t-1,0)] if j==0 else pos[(t-1,j-1)]
    op = X if j==0 else Y
    window = [l for l in range(k) if idx[l][0] >= t-2]
    h = {l:R((k+2*l)%5-2,37) for l in window}
    beta = R(k+3,k+2)
    f = s.Matrix([R((i+k)%5-2,100003) for i in range(M)])
    Q[:,k] = (op*Q[:,parent]-sum((Q[:,l]*v for l,v in h.items()),s.zeros(M,1))-f)/beta
    records[k] = parent,op,h,beta,f
    if j:
        for l,v in h.items():
            TF[l,parent]=v
        TF[k,parent]=beta
        EF[:,parent]=f
HJ = s.zeros(N,P)
for k,(t,j) in enumerate(idx[:P]):
    if j==0:
        child = pos[(t+1,0)]
        _,_,h,beta,_ = records[child]
        for l,v in h.items():
            HJ[l,k]=v
        HJ[child,k]=beta
    else:
        parent,_,h,beta,_ = records[k]
        HJ[:,k]=(TF*HJ[:P,parent]-sum((HJ[:,l]*v for l,v in h.items()),s.zeros(N,1)))/beta
CR = X*Q[:,:P]-Q*HJ
zero(Y*Q[:,:P]-Q*TF-EF)
for k,(t,j) in enumerate(idx[:P]):
    if j==0:
        zero(CR[:,k]-records[pos[(t+1,0)]][4])
    else:
        parent,_,h,beta,f=records[k]
        zero(beta*CR[:,k]-Y*CR[:,parent]+sum((CR[:,l]*v for l,v in h.items()),s.zeros(M,1))-EF*HJ[:P,parent]+X*f)
count=0
Gram=Q.T*Q
for k,(t,j) in enumerate(idx[1:],1):
    parent,_,h,beta,f=records[k]
    T,E=(TF,EF) if j else (HJ,CR)
    for l in range(min(k,P)):
        rhs=(T[:,l].T*Gram[:,parent])[0]+(E[:,l].T*Q[:,parent])[0]-sum(v*Gram[l,ll] for ll,v in h.items())-(Q[:,l].T*f)[0]
        assert s.simplify(beta*Gram[l,k]-rhs)==0
        count+=1
    for i in range(M):
        aa=X[i,i] if j==0 else Y[i,i]
        assert beta*Q[i,k]+sum(v*Q[i,l] for l,v in h.items())-aa*Q[i,parent]==-f[i]
results['104_residual_and_node_identities']='exact zero'
results['106_exact_omega_pairs']=count

# 102: independent double recurrence, residuals recomputed in long double.
# This is measured corroboration of first-order constants, not an exact proof.
for shape in ('shear', 'triangle'):
    if shape == 'shear':
        pts = np.array([(a/7, c/7+a/14) for a in range(-7,8) for c in range(-7,8)])
    else:
        pts = np.array([(a/8-1,c/8-1) for a in range(17) for c in range(17-a)])
    for method in ('cgs', 'orth'):
        ij = indices(8)
        at = {v:k for k,v in enumerate(ij)}
        QQ = np.zeros((len(pts),len(ij)))
        QQ[:,0]=1/np.sqrt(len(pts))
        ratios=[]
        for k,(t,j) in enumerate(ij[1:],1):
            p=at[(t-1,0)] if j==0 else at[(t-1,j-1)]
            av=pts[:,0] if j==0 else pts[:,1]
            # Exact window: lower degrees plus earlier same-degree columns.
            W=[l for l in range(k) if ij[l][0]>=t-2 and (ij[l][0]!=t-2 or ij[l][1]>=max(j-2,0))]
            QW=QQ[:,W]
            rr=av*QQ[:,p]
            if method=='cgs':
                hh=QW.T@rr
                rr-=QW@hh
            else:
                hh=np.zeros(len(W))
                old=np.linalg.norm(rr)
                for sweep in range(2):
                    for ll,l in enumerate(W):
                        cc=QQ[:,l]@rr
                        rr-=cc*QQ[:,l]
                        hh[ll]+=cc
                    new=np.linalg.norm(rr)
                    if new>0.707*old:
                        break
                    old=new
            beta=np.sqrt(np.sum(rr*rr))
            QQ[:,k]=rr/beta
            Ld=np.longdouble
            ff=av.astype(Ld)*QQ[:,p].astype(Ld)-QW.astype(Ld)@hh.astype(Ld)-Ld(beta)*QQ[:,k].astype(Ld)
            fn=float(np.sqrt(np.sum(ff*ff)))
            mu=np.max(np.linalg.norm(QQ[:,:k+1],axis=0))
            kap=np.linalg.norm(QW,2)
            w=len(W)
            constant=(w+2)*(1+kap*np.sqrt(w)*mu)+1 if method=='cgs' else (6*w+4)*kap**2
            bound=constant*2.0**-53*np.max(np.abs(av))*mu
            ratios.append(fn/bound)
        worst=max(ratios)
        assert worst<1
        results[f'102_{shape}_{method}_max_residual_over_first_order_bound']=worst

print(json.dumps({'python':platform.python_version(),'sympy':s.__version__,'numpy':np.__version__,'seed':'none; deterministic inputs','results':results},indent=2))
