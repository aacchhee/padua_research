# PD-T?proof-attempts-codex-01 — Exact Padua corner formula

Final ID: **PD-T101** (2026-11-01; provisional heading retained as alias; reservation published at `020dcddd36fa1e3254cbf288701d5ab02d27c580`).

ID kind: PD-T.
Aliases: T-A1; corner rhombus kernel; product-U formula; O(N) corner sum.
Split from: `PD-T?programme-ideas-claude-04`, the row “exact finite-sum form of Λ_c(n)”; precise target A1 in `topics/programme-ideas-20261031/OPEN_TARGETS.md` at `cadb35066160e466cb1704b9791ad6f374446422`.
Split into: none. Source and crosswalk integration applied during authorized PR finalization; see `../finalization/id-map.json`.

## Statement

For every integer n ≥ 1, let

\[
 B_{jk}=(\cos\theta_j,\cos\phi_k),\quad
 \theta_j=j\pi/n,\quad\phi_k=k\pi/(n+1),\quad
 0\leq j\leq n,\quad0\leq k\leq n+1,\quad j+k\equiv0\pmod2.
\]

Put ε_j=1/2 at j=0,n and 1 elsewhere, and η_k=1/2 at k=0,n+1 and 1 elsewhere. The positive weights are w_jk=2ε_jη_k/[n(n+1)]. For each corner c=(cos θ_c,cos φ_c), θ_c,φ_c∈{0,π}, the Lebesgue function of total-degree interpolation at these nodes satisfies

\[
 \lambda_n(c)=\sum_{j+k\;\mathrm{even}}w_{jk}
 \left|D_n(\theta_c+\theta_j,\phi_c+\phi_k)
       -T_n(\cos\theta_c)(-1)^j\right|,
\]

where, with S=(u+v)/2 and T=(v−u)/2,

\[
 D_n(u,v)=U_{n+1}(S)U_{n+1}(T)+U_n(S)U_n(T),\qquad
 U_m(t)=\frac{\sin(mt)}{\sin t}.
\]

Every U_m is interpreted by its continuous extension at t∈πℤ. Thus the statement includes all singular-looking summands, node corners and n=1.

## Definitions

Π_n is the space of real polynomials in two variables of total degree at most n. T_a(cos t)=cos(at). L_B is its cardinal polynomial at node B, and λ_n(z)=Σ_B|L_B(z)|. Here U_m denotes a trigonometric quotient indexed as in the target, rather than the usual polynomial U_m(cos t) notation.

## Assumptions

Exact real arithmetic; precisely the even checkerboard and the weights above. No corner-argmax or asymptotic assumption is used.

## Status by part

Overall status: **PROVED** (written all-n proof below; Claude audit-01 ACCEPTED).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Every n≥1, all four corner identities, with continuous singular limits | PROVED | Elementary discrete-cosine and Fourier proof below |
| Exact regression n=1,…,6 | Verification evidence | SymPy cyclotomic-field Vandermonde inversion plus Laurent coefficients; `../code/a1_exact_check.py`, `../outputs/a1_exact_check.json` |

The normalization and rhombus calculations below are routine steps of this one identity, not independently proposed research claims. The source expansion target remains OPEN.

## Depends on

Finite geometric sums, cosine product identities and elementary matrix algebra. No source theorem is inherited as a local proof. The published cardinal formula was checked separately as LITERATURE, as required by the target.

## Checks

Developer executed from the repository root:

```text
python topics/padua-proof-attempts-20261101/code/a1_exact_check.py > topics/padua-proof-attempts-20261101/outputs/a1_exact_check.json
```

Python 3.12.14; SymPy 1.14.0. Deterministic, no seeds or tolerances. The script independently inverts the unscaled product-Chebyshev Vandermonde over QQ(ζ), ζ a primitive [2n(n+1)]th root. It checks the inverse identity and every cardinal value at every corner against the corrected kernel, then checks the product-U identity as a Laurent-polynomial coefficient equality. For n=1,…,6 the respective corner checks are 12,24,40,60,84,112 (332 total); all passed. Cardinal equality term by term implies the equality of the absolute sums; no unverified numerical sign decision is needed.

Script SHA-256: `e7ea17bc56e44214fdf4206c654fb1710e7a8d3ca194dcdc15390a066a7920b0`.
Developer receipt SHA-256: `f8cd6cfd027989bf4bb59ebaebd9040824b0763ef660db51b5046078f33e8f94` (1,875 bytes).
The all-n proof does not depend on this finite regression. Independent execution is recorded by the orchestrator in the topic's independent-check evidence; Claude remains the required auditor.

## Sources

**LITERATURE, primary statement/normalization checked 2026-11-01:** Caliari–De Marchi–Vianello, *Bivariate Lagrange interpolation at the Padua points: Computational aspects*, JCAM 221 (2008), 284–292, [author preprint dated 5 November 2007](https://www.math.unipd.it/~marcov/pdf/PDcomp.pdf), §2: eq. (1), printed p.3, gives weights 1/(2n(n+1)), 1/(n(n+1)), 2/(n(n+1)) at vertices, edges and interior nodes; eq. (3), printed p.3, defines the kernel with normalized product-Chebyshev modes; eqs. (6a),(6b),(6c), printed p.4, give exactly this even checkerboard and the x-mode-corrected interpolation formula. The paper calls it its **third family**; this differs from the target's informal “first family” label, but agrees exactly with the target's authoritative coordinates and parity. No node definition is changed here. Coverage: the displayed definitions and interpolation formulas, not a full-paper proof review.

**LITERATURE, primary theorem checked:** Bos–Caliari–De Marchi–Vianello–Xu, *Bivariate Lagrange interpolation at the Padua points: the generating curve approach*, JAT 143 (2006), 15–25, [author preprint](https://www.math.unipd.it/~marcov/pdf/PaduaCurve3.pdf), Theorem 2, eqs. (6)–(9), printed pp.8–9. That orientation has its exceptional mode in y. Swapping the coordinates gives the present x correction. Its Lemma 2, printed p.9, uses a kernel named D_n with a different factor: that D_n is one quarter of the rhombus sum used here. Coverage: theorem statement, displayed formula and normalization; full source proof not inherited. No third-party PDF or fulltext extract is committed.

## Proof or evidence

### 1. Independently derive the cardinal normalization

For an integer M≥1, set t_j=jπ/M, ε_j=1/2 at the endpoints and 1 otherwise, and

\[
 Q_M(f)=\frac1M\sum_{j=0}^M\varepsilon_jf(t_j).
\]

A finite geometric sum gives Q_M(cos(rt))=0 for 1≤r≤2M−1, while Q_M(1)=Q_M(cos(2Mt))=1. One direct verification is to take the real part of Σ' exp(irjπ/M): for odd r the endpoint-reflection terms cancel, and for even r not divisible by 2M the complete Mth-root sum is zero. Therefore, by 2cos(at)cos(ct)=cos((a−c)t)+cos((a+c)t), for 0≤a,c≤M,

\[
 Q_M(\cos(at)\cos(ct))=\delta_{ac}h_a^{(M)},\qquad
 h_a^{(M)}=\begin{cases}1&a=0\text{ or }M,\\1/2&0<a<M.\end{cases}
\]

Also (−1)^j cos(at_j)=cos((M−a)t_j). Consequently

\[
 Q_M((-1)^j\cos(at_j)\cos(ct_j))=0\quad\text{unless }a+c=M.
\]

Take q_ab(x,y)=T_a(x)T_b(y), a+b≤n. Since 2·1_{j+k even}=1+(−1)^{j+k}, the checkerboard inner product of q_ab and q_cd equals the full tensor quadrature plus its alternating tensor quadrature. The latter vanishes: to be nonzero would require a+c=n and b+d=n+1, contradicting (a+b)+(c+d)≤2n. The former is diagonal, with entries h_a^(n)h_b^(n+1). All these are positive.

There are N=(n+1)(n+2)/2 nodes: among the two consecutive axis lengths n+1,n+2, the even-length axis has half its indices in each parity. There are also N modes q_ab. Thus the N×N evaluation matrix V has positive definite Gram matrix VᵀWV=H and is invertible. This independently proves unisolvence and the normalization needed here.

The discrete reproducing kernel is q(z)ᵀH⁻¹q(B). Its coefficients are the usual continuous product-Chebyshev coefficients c_ac_b, c_0=1 and c_a=2 for a>0, except at (a,b)=(n,0), where the coefficient is 1 rather than 2. Hence

\[
 \widetilde K_n(z,B)=K_n(z,B)-T_n(z_1)T_n(B_1),
\]

\[
 K_n(z,B)=\sum_{a+b\leq n}c_ac_bT_a(z_1)T_a(B_1)T_b(z_2)T_b(B_2).
\]

Since V is square, VH⁻¹Vᵀ=W⁻¹. Thus w_B\widetilde K_n(A,B)=δ_AB at every pair of nodes. Its degree is at most n, so uniqueness gives

\[
 L_B(z)=w_B\bigl(K_n(z,B)-T_n(z_1)T_n(B_1)\bigr).
\]

This derives the published formula locally rather than assigning PROVED to a citation.

### 2. Sum the rhombus exactly

Define the finite Fourier sum

\[
 R_n(u,v)=\sum_{|p|+|q|\leq n}e^{i(pu+qv)}.
\]

Grouping sign-reflected pairs gives

\[
 R_n(u,v)=\sum_{a+b\leq n}c_ac_b\cos(au)\cos(bv).
\]

For S=(u+v)/2, T=(v−u)/2, write r=p+q and s=q−p. This is a bijection from integer pairs in the rhombus to pairs with |r|,|s|≤n and r≡s (mod 2), because |p|+|q|=max(|r|,|s|). Also pu+qv=rS+sT. The r,s values of parity n run independently through −n,−n+2,…,n; those of the other parity run through −n+1,−n+3,…,n−1. Therefore

\[
 R_n(u,v)=\left(\sum_{r=-n,-n+2,\ldots,n}e^{irS}\right)
           \left(\sum_{s=-n,-n+2,\ldots,n}e^{isT}\right)
 +\left(\sum_{r=-n+1,-n+3,\ldots,n-1}e^{irS}\right)
  \left(\sum_{s=-n+1,-n+3,\ldots,n-1}e^{isT}\right).
\]

The geometric sum Σ_{r=−m+1,−m+3,…,m−1}e^{irt} equals sin(mt)/sin t when sin t≠0 and is continuous everywhere. At t=ℓπ its value is m(−1)^((m−1)ℓ). Consequently R_n=D_n with exactly the target's indexing, including every removable singularity.

### 3. Specialize to a corner

For θ_c∈{0,π}, sin(aθ_c)=0, so

\[
 T_a(c_1)T_a(\cos\theta_j)=\cos(a(\theta_c+\theta_j)).
\]

The same holds in the other coordinate. Substitution into the product-Chebyshev kernel and step 2 gives K_n(c,B_jk)=D_n(θ_c+θ_j,φ_c+φ_k). Finally T_n(cos θ_j)=cos(jπ)=(−1)^j. Insert these two equalities into the cardinal formula, take absolute values and sum. Because every w_B is positive it can be moved outside the absolute value. This is the asserted identity. ∎

## Scope

This closes A1 for the stated Padua nodes, every degree and corner. It supplies an exact finite identity; it does not prove a corner argmax, an asymptotic coefficient, a large-n rounding bound or any maxima count. This is a reconstruction using classical kernel ingredients, with no historical novelty claim.

## Open items

Claude audit-01 ACCEPTED; independent exact-check receipt recorded separately. The source's A2/A3 expansion and A4 argmax remain OPEN. Source edits remain proposed until the PR #6 audit is complete.

## History

2026-11-01, Codex development subagent `/root/a1_develop`, requested gpt-6.1-sol xhigh; resolved runtime metadata not independently exposed. Rules/base read at `cadb35066160e466cb1704b9791ad6f374446422`. The old A1 statement is preserved verbatim above in mathematical form; only its singular-limit convention is made explicit. Initial checker plumbing used a nonexistent DomainMatrix property; corrected before the successful receipt, with no mathematical mismatch. No existing source file was edited.
