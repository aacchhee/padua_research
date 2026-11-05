# PD-N?mz2d-frontier-codex-10 — the 1D sign-discard intermediary has no uniform mass floor

ID kind: PD-N.
Aliases: absolute-coefficient uniform-gap barrier; central Dirichlet
coefficient test; limitation of the PD-T014 intermediary.
Split from: IDEA?mz2d-frontier-codex-10, a proposed uniform-gap sharpening
of the 1D sign-discard argument. The original PD-T027 target is unchanged.
Split into: none.

## Statement

For every integer N>=2 let M_N,R_N be the continuous Lebesgue and
Clenshaw–Curtis mass matrices of T_0,...,T_(N−1), and set
`A_N=2M_N−R_N`. There is no real number delta>0 such that

\[
 |a|^T A_N |a|\ge\delta\,a^T M_Na
 \qquad(N\ge2,\ a\in\mathbb R^N).                       \tag{1}
\]

Here absolute values are taken coefficient by coefficient. More
explicitly, for N=2L+1, L>=1, set

\[
 a_{2j}=(-1)^j\quad(0\le j\le L),\qquad a_{2j+1}=0.
\]

Then

\[
0<\frac{|a|^TA_N|a|}{a^TM_Na}
 \le\frac{32\{2+\log(2N)\}}{L}\longrightarrow0.          \tag{2}
\]

Consequently the proof route which first replaces the original signs
in the *gap form* by
`a^T A_N a >= |a|^T A_N |a|` and then seeks the uniform lower bound (1)
cannot establish an N-independent endpoint gap. This says nothing
against a uniform bound for the actual ratio `a^T A_N a/a^T M_Na`.

## Definitions

The CC rule C_N has nodes cos(j*pi/N), weights given in PD-T013,
mass two and measure dx. For coefficient vector b,

\[
 b^TM_Nb=\int_{-1}^1\left(\sum_{i=0}^{N-1}b_iT_i\right)^2dx,
 \qquad
 b^TR_Nb=C_N\left[\left(\sum_{i=0}^{N-1}b_iT_i\right)^2\right].
\]

All coefficients in (2) belong to degree N−1, including the top mode.
There is no full-degree N polynomial in the construction.

## Assumptions

Real coefficients, integer N>=2, exact real arithmetic, unnormalized
Lebesgue measure. The countersequence uses odd N only, which is enough
to refute the all-N quantifier in (1).

## Status by part

Overall status: **PROVED** (analytic development; independent/Claude
audit pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Inequality (1) is impossible, with the explicit bound (2) | PROVED | Written norm comparison below |

Candidate / claim disposition: **REJECTED: failed**, restricted to the
uniform intermediary estimate (1).
Rejection reason: the explicit admissible coefficient sequence makes
its best possible mass-normalized constant tend to zero.

## Negative-result scope

Attempted mechanism: IDEA?mz2d-frontier-codex-10, retaining exactly the
absolute-coefficient lower-bound intermediary from IDEA-062/PD-T014
and improving only its comparison with the *original* continuous norm.
Parameter range: a subsequence of all odd N>=3; conclusion forbids one
positive constant for all N>=2.

The sign-discard inequality itself remains valid. The qualitative and
degree-dependent PD-T014/022 theorems are not refuted. PD-T027's uniform
upper gap and sharp limiting spectrum remain OPEN. No obstruction to
a different basis, retained signs, block cancellation, core-tail estimate
or distributed limiting operator follows.

## Depends on

PD-T013: positivity of CC weights. PD-T014: A_N positive definite on
degree N−1 (used only for the strict lower inequality in (2), not for
the failure of (1)). Elementary finite cosine identities and Lebesgue
integration. The second-kind norm identity is derived below; it also
appears in PD-T019.

## Checks

Rules/input `83cf6f1ee244f2e72057332a7ec04ee74db1f0de`.
The cheapest test was written in ideas-f12.md before this proof record.
No numerical or exact-arithmetic mathematical program was executed by
this worker. No independent check or rerun is claimed. This is an
analytic countersequence, so no computer-assisted proof obligation is
being substituted for the proof.

## Sources

Local full predecessors: IDEA-062/063/073 and PD-T013/014/015/022/027;
complete gate and search boundaries are in ../ideas-f12.md. No external
theorem or historical novelty claim.

## Proof or evidence

Put

\[
 q_L(x)=\sum_{j=0}^{L}T_{2j}(x),\qquad
 p_L(x)=\sum_{j=0}^{L}(-1)^jT_{2j}(x).
\]

The coefficient vectors of p_L and q_L are a and |a| respectively.
The finite cosine sum gives, with N=2L+1,

\[
 q_L(\cos t)=\frac12\left(1+\frac{\sin Nt}{\sin t}\right)
 =\frac12(1+U_{N-1}(\cos t)).                         \tag{3}
\]

The removable values at t=0,pi follow by continuity. The polynomial
identity

\[
 U_{N-1}^2=\sum_{k=0}^{N-1}U_{2k}
\]

follows, for example, by multiplying by sin²t and summing
`sin((2k+1)t)` as a geometric series. Also

\[
 \int_{-1}^1 U_{2k}(x)\,dx
 =\int_0^\pi\sin((2k+1)t)\,dt=\frac2{2k+1}.
\]

Since N is odd, integration of (3) therefore gives the exact formula

\[
 \|q_L\|_2^2
 =\frac12+\frac1N+\frac12\sum_{k=0}^{N-1}\frac1{2k+1}.
                                                               \tag{4}
\]

Monotonicity of the reciprocal function yields

\[
 \sum_{k=0}^{N-1}\frac1{2k+1}
 \le1+\frac12\log(2N-1).
\]

In particular `||q_L||_2² <= 2+log(2N)` for every N>=3.
Positive CC weights imply `C_N(q_L²)>=0`; hence

\[
 |a|^TA_N|a|=2\|q_L\|_2^2-C_N(q_L^2)
 \le4+2\log(2N).                                      \tag{5}
\]

To bound the original mass from below, write `t=pi/2+u`. Then

\[
 p_L(\cos t)=\sum_{j=0}^L\cos(2ju).
\]

On `|u|<=1/(4L)`, all `|2ju|<=1/2`; thus every cosine is at least
one half and `sin t=cos u>=1/2`. Integrating just this interval gives

\[
 a^TM_Na=\|p_L\|_2^2
 \ge\frac{(L+1)^2}{4}\frac12\frac1{2L}
 =\frac{(L+1)^2}{16L}\ge\frac L{16}.                  \tag{6}
\]

Combining (5) and (6) proves the upper inequality in (2). Its right
side tends to zero, because N=2L+1. Strict positivity on the left
follows from PD-T014 applied to the nonzero polynomial q_L. If (1)
held for some delta>0, (2) would give delta<=a quantity tending zero,
a contradiction. This proves the exact scoped failure. ∎

## Scope

Erasing the signs moves this explicit polynomial's concentration from
an interior angular layer to the endpoints and loses a factor of order
N/log N in the relevant mass comparison. This describes the selected
intermediary; it does not estimate the actual extremal eigenvectors or
exclude a uniform true spectral gap. No Padua spectral statement follows
from a one-dimensional obstruction to this proof route.

## Open items

Independent analytic reconstruction; required Claude audit. A successful
uniform-gap proof must bypass the specific intermediary (1). The full
1D PD-T027 and signed 2D PD-T110 targets remain unchanged and OPEN.

## History

2026-11-05, Codex F1/F2 developer, requested gpt-6.1-sol xhigh; runtime
model metadata unexposed. Rules/input SHA above. No Git operations;
scoped obstruction separated from the unresolved spectral target.
