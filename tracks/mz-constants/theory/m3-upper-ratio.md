# PD-T022 — a fixed-ratio CC upper constant below two

Review update, 2026-10-31: final ID allocation and scoped independent Astra review are complete; see topics/mz-constants/independent-astra-01.md and ID_CROSSWALK.md. The original development-stage pending-review wording below is historical. Required Claude audit and unresolved literature/novelty coverage remain PENDING. This administrative update changes no mathematical claim or proof.

ID kind: PD-T. Aliases: degree-sensitive Z-matrix bound; oversampled upper MZ constant.
Split from: M3 fixed-ratio two-sided target. Split into: none.

## Statement

For integers \(N\ge2\) and \(0\le n<N\), define
\(\rho_{N,n}=\max\{2n/N-1,0\}^2\). For every real \(p\in\Pi_n\),
\[
Q_N(p^2)\le (1+\rho_{N,n})\int_{-1}^1p^2.\tag{1}
\]
If \(2n\le N\), equality holds for every \(p\). If \(2n>N\), inequality (1) is strict for every nonzero \(p\). In particular, for \(n\le\theta N\) with any fixed \(0\le\theta<1\), the upper constant is at most
\(1+\max\{2\theta-1,0\}^2<2\).

### Endpoint corollary (PD-T022)

For every integer \(N\ge2\),
\[
\lambda_+(N,N-1)\le1+(1-2/N)^2
=2-\frac4N+\frac4{N^2}<2.\tag{2}
\]
At \(N=2\), \(\rho_{2,1}=0\) and exactness gives \(\lambda_+(2,1)=1\), so the first inequality in (2) is equality. For \(N\ge3\), \(\rho_{N,N-1}>0\) and that inequality is strict. Here \(\lambda_+(N,n)\) is the largest discrete Gram eigenvalue on \(\Pi_n\) in a continuous-Lebesgue-orthonormal basis.

This corollary quantitatively supersedes the historical bound \(2-2/(\pi N)\) in PD-T014 for every \(N\ge2\), since \(4-4/N\ge2>2/\pi\). PD-T014 retains its independent short proof of the qualitative threshold and its weaker quantitative alternative using PD-T015.

## Definitions, assumptions and status

\(Q_N\) is the Lebesgue CC rule on \(N+1\) Lobatto nodes. \(M,R,D=2(M-R)\) denote its continuous/discrete Chebyshev mass matrices and exact Hankel defect on indices \(0,\ldots,n\), as in PD-T013.

Overall status: **PROVED** in development; prior-art screen and pinned independent acceptance pending. This is a degree-sensitive refinement of PD-T014, including the explicit endpoint corollary (2), but not a uniform upper gap at \(n=N-1\). The added corollary awaits focused independent re-audit in response to audit-01 M1.

Depends on: locally proved moment/alias/defect signs, PD-T013. The sign-replacement argument of M1 is repeated explicitly. No external theorem is used.

## Proof

If \(2n\le N\), polynomial exactness gives \(R=M\). Otherwise set \(t=2n/N-1>0\), \(\rho=t^2\), and \(A_\rho=(1+\rho)M-R=\rho M+D/2\).

We claim \((A_\rho)_{ij}\le0\) for \(i\ne j\). Opposite parities vanish; unaliased same-parity entries equal \(\rho M_{ij}<0\). For an aliased same-parity pair, put \(s=i+j>N\), \(d=|i-j|\ge2\), \(r=2N-s\), and \(\delta=N-n>0\). Then \(r<N\), \(r>d\), and
\[
d\le r-2\delta,\qquad \frac dr\le1-\frac{2\delta}{N}=t,
\qquad \frac{d^2-1}{r^2-1}\le\frac{d^2}{r^2}\le\rho.
\]
The first inequality is \(r-d=2(N-\max(i,j))\ge2\delta\). The ratio inequality follows since \(r\le N\); the comparison of squares follows by cross multiplication because \(r\ge d>1\). The exact entry is
\[
(A_\rho)_{ij}=-\frac\rho{d^2-1}-\frac{1+\rho}{s^2-1}+\frac1{r^2-1}<0.
\]
For any coefficient vector \(a\) and \(v=|a|\), therefore,
\[
a^TA_\rho a\ge v^TA_\rho v
=\rho v^TMv+\tfrac12v^TDv>0
\]
when \(a\ne0\), because \(D\) is entrywise nonnegative and \(M\) positive definite. This is precisely (1), with strictness in the nonexact case. Monotonicity of \(\max(2x-1,0)^2\) gives the fixed-\(\theta\) assertion.

For (2), substitute \(n=N-1\) into (1): \(\max\{2(N-1)/N-1,0\}=1-2/N\) for every \(N\ge2\). Expansion gives the stated expression. The exact case \(N=2\) has \(2n=N\); for \(N\ge3\), \(2n>N\) and the already proved strictness applies. Finally \(4/N-4/N^2>2/(\pi N)\) proves quantitative dominance over PD-T014's historical constant. Since \(\rho_{N,n}\) is nondecreasing in \(n\), the same dominance holds for \(1+\rho_{N,n}\) at every \(0\le n<N\).

## Checks, sources and limits

Exact finite checks cover the filter-independent sign inequalities for every pair \(2\le N\le25\), \(0\le n<N\); see `tracks/mz-constants/code/m3_exact_check.py` and `topics/mz-constants/directions/M3/RUNS.md` for the actual executed scope and hashes. The all-N proof is analytic. Source attribution: the orchestrator suggested the degree-sensitive refinement after the M1 proof; the present developer reconstructed and wrote it. Historical weighted-MZ/CC literature remains under documented screen; no novelty claim is made.

At \(n=N-1\) this upper gap is of order \(N^{-1}\). Neither this result nor the M1 gap alone proves that \(1-\eta\) is of order \(\log^{-2}N\) at the endpoint. The measured sharp constant near 1.004437 remains outside the theorem.

## History

2026-10-31, Codex gpt-6.1-sol xhigh, rules `d36722823441dc40c6e19d69a174459348dd309c`: M3 activated after M1 frozen first target completed, leaving only M2 and M3 active. Provisional ID allocated within assigned range31–39.

2026-10-31, audit-01 response, Codex gpt-6.1-sol xhigh (explicit orchestrator assignment), rules `6d10a82cf6fd6f7ef6fbe76e68133ccbcbe51994`: added the endpoint specialization (2) without changing (1), its proof or status. Its quantitative dominance over PD-T014 was previously unreported; the corollary now has an explicit all-N statement, the N=2 equality case, and a focused re-audit obligation. No new global ID or novelty claim is introduced.
