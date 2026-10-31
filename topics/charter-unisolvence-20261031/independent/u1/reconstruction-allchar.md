# PD-T?charter-unisolvence-u1-independent-01 — Independent reconstruction of the normalized checkerboard criterion

ID kind: PD-T; provisional independent verification label, to be consolidated with the producer's corresponding result rather than registered as a second discovery.
Aliases: U1; alternation Hankel criterion; parity-restricted moments; complementary Hankel minors.
Split from: none; this is a changed functional and corrected statement following original U1, whose wording remains preserved in the negative record.
Split into: none. The original characteristic-two obstruction is separately recorded in `reconstruction-char2.md`.

Rules/base: d36722823441dc40c6e19d69a174459348dd309c. Independent Codex adversarial reconstruction, actual assigned model gpt-6-astra, effort xhigh, 2026-10-31. This is not the required final Claude audit. No producer U1 file was read before this proof and the independent checker were completed. The initial assignment disclosed the producer's parity-Gram route; a later message disclosed the proposed normalized cutoff while this reviewer was independently deriving complementary minors. Independence is reconstruction and separate execution, not a claim of zero exposure to the proposed mechanism.

## Statement

Let K be any field, m≥0, X=(h_0,...,h_m) and Y=(g_0,...,g_{m+1}) be lists distinct within each axis, and e∈{0,1}. Put N=(m+1)(m+2)/2 and S_e={(h_i,g_j):i+j≡e mod2}. For a labelled list H=(t_0,...,t_{L-1}), define

\[
\omega_H(z)=\prod_i(z-t_i),\quad w_i=1/\omega_H'(t_i),\quad
\eta_{H,s}=\sum_{i\ {even}}w_i t_i^s,\quad
B_{H,r}=\det(\eta_{H,a+b})_{0\le a,b<r},\quad B_{H,0}=1.
\]

The word “even” in this definition refers to the integer label i, including in characteristic two. Define k=⌊L/2⌋ and

\[
C_H=\begin{cases}
B_{H,k}\prod_{r=1}^{k-1}B_{H,r}^{,2},&L=2k,\\
\prod_{r=1}^{k}B_{H,r}^{,2},&L=2k+1.
\end{cases}
\]

An empty product is one. Let E_e be the evaluation matrix of any ordering of the total-degree monomials x^a y^b, a+b≤m, at any ordering of S_e. Then

\[
(-1)^{eN}\det(E_e)^2
\prod_{(i,j):\,i+j\equiv e\ (2)}\frac1{\omega_X'(h_i)\omega_Y'(g_j)}
=C_X C_Y.\tag{1}
\]

Consequently S_e is unisolvent for Π_m if and only if

\[
B_{H,r}\ne0\quad(H=X,Y;\quad1\le r\le\lfloor (|H|-2)/2\rfloor).\tag{2}
\]

A negative upper bound means an empty range. In particular the two checkerboards are simultaneously unisolvent or singular.

## Definitions and assumptions

Unisolvent means the square evaluation map Π_m→K^{S_e} is invertible. Distinctness is only required within each axis; the two axes may share values. There is no node ordering, positivity, perfectness or characteristic hypothesis. Each parity has N points because one axis length is even and each row or column along that axis splits equally.

## Status by part

Overall mathematical status: PROVED by the hand argument below, subject to independent campaign acceptance. This reviewer does not certify novelty or replace the Claude audit.

Candidate disposition: verification of the corrected U1 statement. The original all-field alternation iff is refuted separately. Numerical checks are verification evidence, not proof dependencies.

## Depends on

Elementary Lagrange interpolation, Vandermonde determinants, Jacobi's complementary-minor identity, and Gaussian elimination/Gram orthogonalization over a rational-function field. All specialized determinant steps needed here are reconstructed below. No uninspected literature theorem is a proof dependency.

## Proof

### 1. Barycentric duality and complementary alternation minors

Fix H of length L. Write β(f)=Σ_i w_i f(t_i) and A(f)=Σ_i(-1)^i w_i f(t_i). Lagrange interpolation implies β(z^s)=0 for 0≤s≤L−2 and β(z^{L−1})=1. These statements include the empty zero range when L=1.

On K[z]_{<L}, let M and T be the matrices of the form β(fg) and multiplication, modulo ω_H, by the unique polynomial s with s(t_i)=(-1)^i. Thus T²=I and the full alternation Gram matrix is A_L=MT. Let V be the square Vandermonde matrix V_{i,a}=t_i^a. Then

\[
\det A_L=\det(V)^2\prod_i\frac{(-1)^i}{\omega_H'(t_i)}=1.\tag{3}
\]

Indeed Σ_i i=L(L−1)/2, and the product of the derivatives is (-1)^{L(L−1)/2}det(V)^2. In particular A_L is invertible in every characteristic.

Define q_i(z) by

\[
\frac{\omega_H(z)-\omega_H(u)}{z-u}=\sum_{i=0}^{L-1}q_i(z)u^i.
\]

The polynomial q_i is monic of degree L−1−i. Applying β(z^j·) and Lagrange interpolation gives β(z^j q_i)=δ_{ij}, for 0≤i,j<L: at z=t_l the kernel equals ω_H(u)/(u-t_l), so its barycentric sum is precisely the interpolation formula for u^j. The coefficient matrix Q of the q_i is therefore M^{-1}. Since M is symmetric,

\[
Q^T A_LQ=M^{-1}(MT)M^{-1}=TM^{-1}=A_L^{-1}.
\]

Write Δ_{H,r} for the leading r×r minor of A_L, and Δ_{H,0}=1. The bottom-right (L−r)×(L−r) block of A_L^{-1} is the alternation Gram matrix on q_r,...,q_{L-1}. Reversing these polynomials gives a monic degree-ordered basis of K[z]_{<L−r}; its change-of-basis determinant is ±1, whose square is one. Its determinant is therefore Δ_{H,L−r}. Jacobi's principal complementary-minor identity, together with (3), yields

\[
\Delta_{H,r}=\Delta_{H,L-r}\qquad(0\le r\le L).\tag{4}
\]

For r≤⌊L/2⌋ all entries of the r×r moment matrix use exponents ≤2r−2≤L−2. On these exponents A=2η−β=2η, whence

\[
\Delta_{H,r}=2^r B_{H,r}.\tag{5}
\]

Combining (4) and (5), by grouping r with L−r, gives the identity

\[
\prod_{r=1}^{L-1}\Delta_{H,r}
=2^{\lfloor L^2/4\rfloor}C_H.\tag{6}
\]

The grouping treats L=1 by empty products.

### 2. The central normalized factor never vanishes

For L=2k, there are exactly k even labels. Their k×k moment determinant is

\[
B_{H,k}=\det(V_{\rm even})^2\prod_{i\ {even}}w_i\ne0.
\]

For L=2k+1, there are k odd labels. Since β(z^s)=0 through s=2k−2, the even moment matrix equals the negative odd moment matrix at order k. Hence

\[
B_{H,k}=(-1)^k\det(V_{\rm odd})^2\prod_{i\ {odd}}w_i\ne0.
\]

For k=0 this asserts B_{H,0}=1. Thus C_H is nonzero exactly when B_{H,r} is nonzero for 1≤r≤⌊(L−2)/2⌋.

### 3. A total-degree tensor moment determinant

For two arbitrary moment sequences μ_s,ν_s, let G_m be the matrix with rows and columns indexed by (a,b) with a+b≤m, whose ((a,b),(c,d)) entry is μ_{a+c}ν_{b+d}. Then

\[
\det G_m=\prod_{r=1}^{m+1}\det(\mu_{a+b})_{a,b<r}\;
\prod_{r=1}^{m+1}\det(\nu_{a+b})_{a,b<r}.\tag{7}
\]

To prove the identity without assuming nonvanishing on the desired specialization, first take all moments to be independent indeterminates over Q. Every leading Hankel determinant is a nonzero polynomial (its anti-diagonal specialization has determinant ±1). Gram orthogonalization therefore produces monic orthogonal polynomials p_a, q_b with norms Δ^μ_{a+1}/Δ^μ_a and Δ^ν_{b+1}/Δ^ν_b. The products p_aq_b for a+b≤m give a monic triangular change of basis, and their Gram matrix is diagonal. The norm for p_a occurs m−a+1 times. The resulting telescoping products give (7). Both sides are polynomials with integer coefficients in the moments, so equality in the characteristic-zero rational-function field proves an integer polynomial identity. It remains true for every field specialization, including zero principal minors.

### 4. The parity Gram relation

For f,g∈Π_m the ordinary product barycentric form (β_X⊗β_Y)(fg) is zero. Indeed every monomial x^a y^b of total degree≤2m has a≤m−1 or b≤m, so at least one of β_X(x^a), β_Y(y^b) vanishes. Let

\[
G_e=E_e^T\operatorname{diag}_{S_e}\left(\frac1{\omega_X'(h_i)\omega_Y'(g_j)}\right)E_e.
\]

Then G_0+G_1=0. The alternation product moment matrix is G_0−G_1=2(-1)^eG_e. Taking determinants, using (7) and Δ_{X,m+1}=1 from (3), yields

\[
2^N(-1)^{eN}\det(E_e)^2\prod_{S_e}\frac1{\omega_X'\omega_Y'}
=\left(\prod_{r=1}^{|X|-1}\Delta_{X,r}\right)
\left(\prod_{r=1}^{|Y|-1}\Delta_{Y,r}\right).\tag{8}
\]

Here no Gram nonsingularity was inferred from a general rectangular matrix: E_e is square and the diagonal node weights are all nonzero, so the determinant equality is exact even for indefinite or characteristic-two forms.

### 5. Integral cancellation and specialization

Perform (6) and (8) first in the localization

\[
R=\mathbb Z[h_0,...,h_m,g_0,...,g_{m+1},D^{-1}],
\quad D=\prod_{i<j}(h_i-h_j)\prod_{i<j}(g_i-g_j).
\]

It is an integral domain. All displayed moments and determinants belong to R. Because the axis lengths are consecutive,

\[
\lfloor (m+1)^2/4\rfloor+\lfloor (m+2)^2/4\rfloor=N.
\]

Substitution of (6) in (8) therefore has the common factor 2^N, which can be cancelled in R. This proves (1) in R, with no power of two in a denominator. Specializing the variables to any field with distinct nodes is valid because D remains nonzero. This order of operations is essential: one cannot cancel 2 inside a characteristic-two field. The nonzero weights, field property and central-factor result now prove (2).

## Checks

The separately written and executed `check_u1.py` tested the squared identity, complementary minors, full alternation determinant one, normalization, central nonvanishing, shortened iff, and original odd-characteristic iff on 9,336 labelled axis pairs / 18,672 checkerboards. See `check-output.txt` and `evidence.md` for exact source hash, command, environment, seed and finite scopes. These checks are MEASURED verification; the theorem is established by the preceding hand proof, not by extrapolation from these cases.

## Sources and novelty limits

The entire registry and its obstruction/disposition tables were read. The literature index was read before reconstruction. No original PDF was opened for this independent task. De Marchi–Usevich 2014 Proposition1 / §4 Corollary1 eq23 is reported and partly inspected by the separate literature agent as a prior axis-only factorization. This record makes no novelty claim for factorization, Hankel orthogonalization or complementary-minor algebra. Exact comparison of this normalized rewrite and field transfer with the published factors remains with the literature/producer work and final audit.

## Scope and open items

Both e, all m≥0 and every field are covered with the stated distinctness. The original signed-alternation criterion is recovered only when char K≠2; see the separate odd-characteristic corollary. No complexity, unsquared determinant sign, kernel formula or larger rectangular excess is asserted. Producer-file comparison and final Claude audit were pending when this independent reconstruction was frozen.

## History

2026-10-31: Codex gpt-6-astra xhigh independently derived the parity Gram identity, tensor determinant, complementary minors and normalized criterion, then executed its own exact checker before opening producer U1 files. The square-free ideal/union-of-two-rectangles route was considered first but not developed into a separate claim; it was unnecessary once the Gram and barycentric-dual arguments closed. Base supplied by orchestrator; this subagent performed no Git commands and edited only its assigned independent/u1 directory.
