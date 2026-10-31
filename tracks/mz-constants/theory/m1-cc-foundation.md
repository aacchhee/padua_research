# PD-T?mz-constants-codex-11 — exact CC weights, aliasing and defect

ID kind: PD-T. Aliases: DCT-I CC weights; Lebesgue Lobatto aliasing; Hankel defect.
Split from: none. Split into: none.

## Statement and definitions

For every integer (N\ge2), let \(x_j=\cos(j\pi/N)\), \(0\le j\le N\), and let \(\ell_j\in\Pi_N\) be their cardinal polynomials. Define the **Lebesgue Clenshaw–Curtis rule** by
\[
 w_j=\int_{-1}^1\ell_j(x)\,dx,\qquad Q_N(f)=\sum_{j=0}^Nw_j f(x_j).
\]
All \(w_j>0\). Write \(c_0=c_N=1/2\), \(c_j=1\) otherwise, and \(\theta_j=j\pi/N\). Then
\[
w_j=\frac{2c_j}{N}\left[1-\sum_{k=1}^{\lfloor(N-1)/2\rfloor}\frac{2\cos(2k\theta_j)}{4k^2-1}
-\mathbf1_{2\mid N}\frac{\cos(N\theta_j)}{N^2-1}\right].\tag{1}
\]
In particular \(w_0=w_N=N^{-2}\) for odd \(N\), and \((N^2-1)^{-1}\) for even \(N\).

Let \(T_k(\cos\theta)=\cos(k\theta)\) and
\[
\mu_k=\int_{-1}^1 T_k(x)\,dx=
\begin{cases}0&k\text{ odd},\\2/(1-k^2)&k\text{ even}.\end{cases}
\]
For \(0\le k\le2N\), \(Q_N(T_k)=\mu_k\) if \(k\le N\), and \(\mu_{2N-k}\) otherwise. For \(0\le i,j\le n\le N\), the continuous and discrete Chebyshev mass matrices are
\[
M_{ij}=(\mu_{|i-j|}+\mu_{i+j})/2,\qquad
R_{ij}=(\mu_{|i-j|}+Q_N(T_{i+j}))/2.
\]
Consequently \(M-R=D/2\), where
\[
D_{ij}=\mu_{i+j}-Q_N(T_{i+j}).\tag{2}
\]
For \(n\le N-1\), \(D\) is entrywise nonnegative; its entries are strictly positive exactly when \(i+j>N\) is even. For any continuous-Lebesgue-orthonormal polynomial basis, let \(C\) map its coefficient vectors to Chebyshev coefficient vectors, and let \(G\) be its discrete Gram matrix. Then
\[
I-G=\tfrac12 C^TDC.\tag{3}
\]

## Assumptions and status

Only the definitions above; no inherited theorem on CC weight positivity is assumed. Overall status: **PROVED** in development, independent pinned review pending. These exact identities and positive weights are substantive supporting results for M1/M2. No positive-semidefinite assertion about \(D\) is made; that assertion is false for \(N\ge5\) on \(\Pi_{N-1}\), as recorded in PD-N?mz-constants-codex-11.

## Proof

The finite geometric-series identity gives
\(\sum_{j=0}^N c_j\cos(k\theta_j)\cos(l\theta_j)=N\delta_{kl}/(2c_k)\), for \(0\le k,l\le N\). To check it, use the cosine product formula and \(\sum_{j=0}^N c_j\cos(mj\pi/N)=0\) for \(1\le m\le2N-1\), while the sums for \(m=0,2N\) are \(N\). Therefore
\[
\ell_j(\cos\theta)=\frac{2c_j}{N}\sum_{k=0}^N c_k\cos(k\theta_j)\cos(k\theta).
\]
Integration gives (1). The moment formula follows from \(x=\cos\theta\) and \(\sin\theta\cos(k\theta)=[\sin((k+1)\theta)-\sin((k-1)\theta)]/2\), with \(k=0,1\) checked directly.

Put \(m=\lfloor(N-1)/2\rfloor\). The elementary telescoping identity
\[
\sum_{k=1}^m\frac{2}{4k^2-1}=1-\frac1{2m+1}
\]
shows that the bracket in (1) is at least \(1/N\) for odd \(N\), and at least \(1/(N-1)-1/(N^2-1)=N/(N^2-1)\) for even \(N\). It is strictly positive. At the endpoints every cosine in (1) is one, proving the endpoint formulas. In particular \(Q_N(p^2)>0\) for every nonzero real \(p\in\Pi_N\), since a polynomial of degree at most \(N\) cannot vanish at all \(N+1\) distinct nodes.

By its cardinal definition the rule is exact on \(\Pi_N\). On every node, \(T_k=T_{2N-k}\); this proves the alias formula up to \(2N\). The product identity \(T_iT_j=(T_{i+j}+T_{|i-j|})/2\) now proves the mass and defect formulas. If \(s=i+j>N\), \(s\) is even and \(n\le N-1\), put \(r=2N-s\). Then \(2\le r<s\), so
\(D_{ij}=2/(r^2-1)-2/(s^2-1)>0\). Odd indices have zero moments. Finally \(C^TMC=I\) and \(G=C^TRC\), proving (3).

## Checks and provenance

Rules/source commit: `d36722823441dc40c6e19d69a174459348dd309c`. Developer: Codex, assigned gpt-6.1-sol xhigh. The supplied `code/hankel_check.py` and `cc_mz_large.py` motivated only the identity; this proof and the checker independently reconstruct it. Supplied notes are unaudited source reports, not dependencies.

Actual finite checks and file hashes are in `topics/mz-constants/directions/M1/RUNS.md`; checker: `tracks/mz-constants/code/m1_exact_check.py`. The all-N proof is analytic and does not depend on a finite computation. Independent reconstruction/pinned rerun and historical literature screen remain pending.

## Sources, scope and open items

Local source reports: `literature/records/mz-input-reports.md`; literature baseline: `topics/mz-constants/literature-search.md`. No external theorem is used or priority claimed. This result establishes definitions, positive weights, and exact low-degree aliasing; it does not estimate the nontrivial spectrum. The bracket lower bound is deliberately elementary and is not a sharp nodewise CC-weight estimate.

## History

2026-10-31: self-contained reconstruction in assigned M1 scope. Scientific status PROVED in development; candidate acceptance awaits prior-art and independent review.
