# PD-T?mz-constants-codex-13 — a quantitative Chebyshev mass floor

ID kind: PD-T. Aliases: telescoping mass floor; weighted diagonal dominance.
Split from: M1 quantitative refinement of the strict upper-bound proof.
Split into: none.

## Statement and definitions

For every integer \(N\ge2\), put \(n=N-1\), and let \(M\) be the Lebesgue mass matrix for \(T_0,\ldots,T_n\). Set \(E=\operatorname{diag}(2,1,\ldots,1)\). Then, in quadratic-form order,
\[
\frac1N E\ \preceq\ M\ \preceq\ \frac\pi2 E.\tag{1}
\]

## Assumptions and status

Only real Chebyshev coefficients and the Lebesgue measure on \([-1,1]\). Overall status: **PROVED** in development, pinned independent review pending. This is a substantive supporting inequality for the quantitative M1 theorem; it is not itself the M1 spectral theorem.

Depends on: moment formula in PD-T?mz-constants-codex-11 (also directly reproved by elementary integration). No external theorem or scientific claim is assumed.

## Proof

For distinct indices \(i,j\), \(M_{ij}\le0\): opposite parity gives zero, and same parity gives \(\mu_{|i-j|},\mu_{i+j}<0\). Put \(b_0=1/2\), \(b_i=1\) for \(i\ge1\). Let \(m_i\) be the least integer at least \(N\) with the same parity as \(i\), and put \(k_i=m_i-1\in\{N-1,N\}\). Direct telescoping gives
\[
(Mb)_0=\frac1{k_0},\qquad
(Mb)_i=\frac12\left(\frac1{k_i-i}+\frac1{k_i+i}\right)
=\frac{k_i}{k_i^2-i^2},\quad i\ge1.\tag{2}
\]
Here is an explicit derivation avoiding an implicit limiting sum. The absolutely convergent even moment series has
\(\sum_{h\in2\mathbb Z}\mu_{|h|}=2-4\sum_{k\ge1}(4k^2-1)^{-1}=0\).
For each fixed \(i\), the infinite row weighted by \(b\) is half this sum, hence zero, including \(i=0\). Its tail starting at \(j=m_i\), in steps of two, is
\[
-\sum_{j=m_i,m_i+2,\ldots}\left[\frac1{(j-i)^2-1}+\frac1{(j+i)^2-1}\right].
\]
The identity \(1/(u^2-1)=[1/(u-1)-1/(u+1)]/2\) gives (2), including \(i=0\). Since \(k_i>i\) and \(k_i\le N\),
\[
\frac{(Mb)_0}{b_0}=\frac2{k_0}\ge\frac2N,
\qquad \frac{(Mb)_i}{b_i}\ge\frac1{k_i}\ge\frac1N\quad(i\ge1).
\]
For every real vector \(a\), expanding both sides proves the exact identity
\[
a^TMa=\sum_i\frac{(Mb)_i}{b_i}a_i^2
+\sum_{i<j}(-M_{ij})b_i b_j\left(\frac{a_i}{b_i}-\frac{a_j}{b_j}\right)^2.
\]
Every term in the second sum is nonnegative, proving the lower bound in (1).

For the upper bound, if \(q(\theta)=\sum_{i=0}^n a_i\cos(i\theta)\), then
\[
a^TMa=\int_0^\pi q(\theta)^2\sin\theta\,d\theta
\le\int_0^\pi q(\theta)^2\,d\theta
=\frac\pi2 a^TEa.
\]
This proves the result.

## Checks, sources, limitations and open items

Exact telescoping and floor checks are in `tracks/mz-constants/code/m1_exact_check.py`, with executed commands and hashes in `topics/mz-constants/directions/M1/RUNS.md`. The all-N argument is analytic. No inherited/private theorem or primary literature statement is used. The floor is not asserted sharp; it serves only to make the M1 strict gap explicit. Independent pinned audit and documented prior-art screen remain pending.

## History

2026-10-31, Codex gpt-6.1-sol xhigh, rules `d36722823441dc40c6e19d69a174459348dd309c`: developed after the strict Z-matrix argument, split as its own substantive supporting result.
