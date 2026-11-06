# Proposed manuscript statements

These are proposed sentences for a later writing step; the manuscript is untouched. Local theory is developed and supplementarily checked as recorded below; audit-02 accepted the P1–P4 mathematics at their stated scopes. The new B2 supporting derivation alone awaits a focused Claude recheck. Exact constants are distinguished from measured decimal proxies.

## CC lower endpoint

“For the Lebesgue Clenshaw–Curtis rule with N+1 Lobatto nodes, on polynomials of degree at most N−1, one has
\[
\limsup_{N\to\infty}(\log N)^2\lambda_{\min}(G_{N,N-1})\leq\frac{\pi^4}{8}.
\]
The bound holds on both parity subsequences. Together with the reverse bound, this yields the exact limit lim (log N)^2 lambda_min = pi^4/8, through all integers N. The same limit holds on degree at most N.”

Dependencies: [reverse bound and full limit](theory/P3-reverse-bound.md), [one-sided theorem](theory/S1-sharp-one-sided.md), [model norm](theory/S1-volterra-model.md), PD-T013/017; [supplementary check](independent-checks-S1-S3.md). This theorem does not turn a continuum norm into an equality for the finite spectra. K2's finite-window rejection of the equality model does not refute this inequality.

## Uniform CC upper bound and norm defect

“For every integer N≥2 and every real polynomial p of degree at most N−1,
\[
0<Q_N(p^2)\leq\frac53\int_{-1}^1p^2\,dx\qquad(p\neq0).
\]
Consequently, with \(\eta_N=\|I-G_{N,N-1}\|_2\), one has \(\eta_N\to1\) and
\[
1-\eta_N\asymp(1+\log N)^{-2}.
\]”

The explicit retained bounds are \(\min(K_N^{-1},1/3)\leq1-\eta_N\leq\min(1,128000/(\log N)^2)\), where K_N is PD-T017's stated harmonic-number constant. Dependencies: [uniform proof](theory/S2-uniform-upper.md), [deficit corollary](theory/S2-eta-deficit.md), PD-T017/018; [check](independent-checks-S2.md). No sharp defect coefficient or effective asymptotic onset is asserted.

## CC upper spectral limit

“Let \(\mathcal V_0\) be the finite span of \(2[\cos(\pi j s)-(-1)^j]\), j≥1, on [0,1]. For \(g\in\mathcal V_0\), put \(F_g(t)=\int_0^1g(s)\cos(st)\,ds\), \(\omega_j=2[(-1)^j+\pi j\operatorname{Si}(\pi j)]\), and
\[
\Lambda_{\rm edge}=\sup_{0\neq g\in\mathcal V_0}
\frac{|F_g(0)|^2+\sum_{j\geq1}\omega_j|F_g(\pi j)|^2}
{\int_0^\infty t|F_g(t)|^2\,dt}.
\]
Then \(\lambda_{\max}(G_{N,N-1})\to\Lambda_{\rm edge}\) through all integers N, with \(1\leq\Lambda_{\rm edge}\leq3/2\).”

Dependencies: [exact model](theory/S2-endpoint-model.md), [fixed-trial bound](theory/S2-fixed-trial-limit.md), [qualitative convergence](theory/S2-qualitative-limit.md), [check](independent-checks-S2-limit.md). The finite J512 value 1.0044369188646673 is a measured proxy, not a certified decimal evaluation of this exact supremum. The separately proved [finite certificates](theory/S2-finite-certificate.md) give explicit finite matrix quantities L_N,U_N bracketing both the finite upper eigenvalue and Lambda_edge, with |lambda_max−Lambda_edge|<=U_N−L_N->0. [Independent certificate check](independent-checks-S2-certificate.md) accepts the exact construction. No such finite certificate was numerically solved, and no elementary or practical convergence rate is asserted.

## Signed Padua logarithmic limits

“Let \(D=\{(a,b):a,b\geq0,\ a+b\leq1\}\), \(\mathcal H=L^2(D,ab\,da\,db)\), \(e_0=1/2\), \(e_j=1\) for j≥1, and \(\psi_{jk}(a,b)=J_0(\pi ja)J_0(\pi kb)\). Define
\[
B_K=-16\sum_{\substack{(1+j)(1+k)\leq K\\j+k\ {\rm even}}}
 e_je_k(-1)^j\,|\psi_{jk}\rangle\langle\psi_{jk}|.
\]
These operators converge in norm to a compact selfadjoint operator B, with \(\|B-B_K\|\leq120/K\). For the signed Lebesgue Padua rule on total degree at most m−1,
\[
\frac{\lambda_-(m,m-1)}{\log m}\longrightarrow\inf\sigma(B)<0,
\qquad
\frac{\lambda_+(m,m-1)}{\log m}\longrightarrow\sup\sigma(B)>0.
\]
The constants agree on the even- and odd-m subsequences.”

Dependencies: [full signed reduction](theory/S3-full-form-log-model.md), [elementary kernel theorem](theory/S3-corner-kernel-hard.md), [compact operator theorem](theory/S3-corner-operator-limit.md), PD-T379 and [strict carrier improvement](theory/S3-normalized-carrier-improvement.md). Supplementary checks: [full form](independent-checks-S3-model.md), [kernel](independent-checks-S3-kernel.md), [operator](independent-checks-S3-operator.md). Explicit finite-m comparison is stated in the operator theorem; it is coarse and certifies no practical fit window.

The displayed operator extrema define exact constants. The inherited negative carrier family has the independently proved coefficient ceiling 1/[9(4log2)(16log2−9log3)]<1/24; this ceiling applies to that fixed-parameter family only. See [family theorem](theory/S3-carrier-family-ceiling.md) and [check](independent-checks-S3-family.md). Finite-model orientation values approximately −0.1336 and +0.0456 are not certified decimal values. No closed scalar formula, optimal packet parameters or effective sign-change degree follows. The manuscript should not identify the earlier four-point measured slope −0.0915 with the true limiting minimum coefficient.


## 2026-11-06 audit-01 K2 interpretation addendum

The K1 final-window intercept 13.0611 exceeds the PROVED bound
limsup (log N)² lambda_min <= pi⁴/8 = 12.1761. It therefore cannot identify
the true limit under S1-02. K2 KILL_MODEL remains the registered operational
outcome and carries no evidential weight against equality; the equality
route stopped on a misspecified numerical test. The candidate is **deferred**,
with resume condition: a proof of the reverse bound liminf >= pi⁴/8, or a
new prospectively registered numerical protocol. No PD-N is created.

## 2026-11-06 audit-01 K4 interpretation addendum

S3-03 (3)/(4) predict limits, and make no prediction about finite-window
slopes. K4 compared those limits with finite-window slopes and retains its
unchanged KILL_HEURISTIC_PROXY outcome. The audit diagnostic
[big.json](audit-01-support/S3/big.json) and
[mid.json](audit-01-support/S3/mid.json) is MEASURED floating evidence:
at m=400,800,801 the Q-minimiser has about 94–96% weight on the second
L_m mode, while L_m's bottom mode already lies near the B proxy −0.1336.
Mode-dependent O(1) corrections explain the registered slopes near −0.092
without contradicting the theorem. This is a finite-scope interpretation,
not a certified crossing law or a PD-N.

Literature context is only search/abstract-screened in literature-screen.md; no priority claim is supported.
