"""Probe for gen2-draft-4: for a unisolvent random set (N = dim Pi_n), build the
degree-(n+1) ideal generators as residuals of x*P_n, y*P_n off Pi_n (in the discrete
OP basis), find the linear syzygies (Hilbert-Burch pencil), and test whether the
syzygy coefficients are carried by the recurrence blocks: i.e. whether the pencil
L(x,y) = x*Lx + y*Ly + L0 acting on the residual vector [r_x; r_y] (2(n+1) polys)
has Lx, Ly of the simple form predicted by commutativity (A-blocks), up to the
n constant-coefficient relations among the residuals."""
import numpy as np, itertools
rng = np.random.default_rng(3)
n = 5; N = (n+1)*(n+2)//2
x = rng.uniform(-1,1,N); y = rng.uniform(-1,1,N); w = rng.uniform(0.5,1.5,N)
# monomial index sets by degree (graded lex), up to degree n+2
def mons(d): return [(i,d-i) for i in range(d,-1,-1)]
idx = {}; allm=[]
for d in range(n+3):
    for m in mons(d): idx[m]=len(allm); allm.append(m)
def ev(m): return x**m[0]*y**m[1]
Vn = np.sqrt(w)[:,None]*np.array([ev(m) for m in allm if sum(m)<=n]).T   # N x N
Qm, Rm = np.linalg.qr(Vn)   # Qm = sqrt(w)*Phi, OPs p_k = sum_j Rinv[j,k] mon_j
Rinv = np.linalg.inv(Rm)
# coefficient vectors (in monomials up to degree n+2) of all OPs up to degree n
Ncoef = len(allm)
P = np.zeros((Ncoef, N))
for k in range(N): P[:N,k] = Rinv[:,k]
degk = np.array([sum(m) for m in allm[:N]])
Pn = P[:, degk==n]            # columns: degree-n OPs (n+1 of them)
def mulx(c):  # multiply monomial-coefficient vector by x
    out=np.zeros(Ncoef)
    for j,m in enumerate(allm):
        if c[j]!=0 and sum(m)<n+2: out[idx[(m[0]+1,m[1])]]+=c[j]
    return out
def muly(c):
    out=np.zeros(Ncoef)
    for j,m in enumerate(allm):
        if c[j]!=0 and sum(m)<n+2: out[idx[(m[0],m[1]+1)]]+=c[j]
    return out
Hx = Qm.T@(x[:,None]*Qm); Hy = Qm.T@(y[:,None]*Qm)
# residuals r_x = x p_k - sum_j Hx[j,k] p_j  (k of degree n): degree n+1 polynomials vanishing on nodes
Rx = np.array([mulx(P[:,k]) - P@Hx[:,k] for k in np.where(degk==n)[0]]).T
Ry = np.array([muly(P[:,k]) - P@Hy[:,k] for k in np.where(degk==n)[0]]).T
Rall = np.hstack([Rx,Ry])  # Ncoef x 2(n+1)
# check vanishing on nodes
vals = np.array([np.prod(np.array([x,y])**np.array(m)[:,None],axis=0) for m in allm]).T  # N x Ncoef
print("max residual value on nodes:", np.abs(vals@Rall).max())
sv = np.linalg.svd(Rall, compute_uv=False); print("rank of residual span (expect n+2 =",n+2,"):", (sv>1e-10*sv[0]).sum())
# linear syzygies: find (alpha,beta,gamma) in R^{3*2(n+1)} with sum (alpha_k x+beta_k y+gamma_k) R_k = 0
cols=[]
for k in range(2*(n+1)):
    cols += [mulx(Rall[:,k]), muly(Rall[:,k]), Rall[:,k]]
S = np.array(cols).T   # Ncoef x 6(n+1)
u,s,vt = np.linalg.svd(S); null = vt[(s>1e-10*s[0]).sum():]
print("dim of linear syzygy space of the 2(n+1) residuals:", null.shape[0],
      " (expected: n constant relations*3 shifts... see below)")
# constant relations among residuals (gamma only)
u2,s2,vt2=np.linalg.svd(Rall); nc = Rall.shape[1]-(s2>1e-10*s2[0]).sum()
print("constant relations among residuals:", nc, "(expect 2(n+1)-(n+2) = n =",n,")")
# genuinely linear syzygies modulo constant ones: dim(null) - (3*nc) should be n+1 (Hilbert-Burch)
print("linear syzygies beyond constant-multiples:", null.shape[0]-3*nc, "(expect n+1 =",n+1,")")
# test the predicted syzygy: y*(Rx) - x*(Ry) = y(xPn - Pi) - x(yPn - Pi) = -(y*Pix - x*Piy), where Pix = sum Hx p_j.
# i.e. y*r_x_k - x*r_y_k + [terms] = 0 with the terms being x*(P Hy[:,k]) - y*(P Hx[:,k]), which re-expanded
# via the recurrence give combinations of residuals of degree n+1 and OPs of degree <= n+1... check it's in span.
for k in range(n+1):
    kk = np.where(degk==n)[0][k]
    lhs = muly(Rx[:,k]) - mulx(Ry[:,k])
    # express lhs as combination of x*R, y*R, R
    coef, res, *_ = np.linalg.lstsq(S, lhs, rcond=None)
    print(f"k={k}: y r_x - x r_y in span{{xR,yR,R}}? residual={np.linalg.norm(S@coef-lhs):.1e}")
