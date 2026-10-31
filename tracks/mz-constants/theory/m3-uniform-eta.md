# PD-T024 — explicit strong MZ constants at every fixed ratio

Review update, 2026-10-31: final ID allocation and scoped independent Astra review are complete; see topics/mz-constants/independent-astra-01.md and ID_CROSSWALK.md. The original development-stage pending-review wording below is historical. Required Claude audit and unresolved literature/novelty coverage remain PENDING. This administrative update changes no mathematical claim or proof.

ID kind: PD-T. Aliases: fixed-ratio eta below one; strong CC MZ inequality.
Split from: frozen M3 question “explicit eta(theta)<1 uniform in n<=theta N for every fixed theta<1”.
Split into: substantive upper and lower results PD-T022 and PD-T023.

## Statement, definitions and assumptions

Let \(Q_N\) be the Lebesgue CC rule on \(N+1\) Lobatto nodes, \(N\ge2\). For every real \(0\le\theta<1\), define
\[
C_*=12(1+\pi)^4(1+2/\pi),\quad
A_\theta=(1-\theta)^2/C_*,\quad
\rho_\theta=\max\{2\theta-1,0\}^2,
\quad \eta_\theta=\max\{1-A_\theta,\rho_\theta\}<1.
\]
Then for every integer \(0\le n\le\theta N\) and every real \(p\in\Pi_n\),
\[
(1-\eta_\theta)\int_{-1}^1p^2
\le Q_N(p^2)\le(1+\eta_\theta)\int_{-1}^1p^2.\tag{1}
\]
More precisely the interval \([A_\theta,1+\rho_\theta]\) contains the full Gram spectrum.

## Status and dependencies

Overall status: **PROVED** in development; separate pinned independent review and prior-art acceptance pending. This proves the original fixed-ratio target with explicit, nonsharp constants. It does not replace that target by the hyperinterpolation corollary.

Depends on PD-T022 (upper interval) and PD-T023 (lower interval); the latter uses the explicit CC-weight bounds in PD-T017. These are local analytic development proofs with their own audit boundaries; no external MZ theorem is assumed.

## Proof

Since \(n/N\le\theta\), the lower theorem gives \(Q_N(p^2)/\int p^2\ge(1-n/N)^2/C_*\ge A_\theta\) for \(p\ne0\). The upper theorem gives the ratio at most \(1+\rho_\theta\). Since \(C_*>1\), \(0<A_\theta<1\), while \(0\le\rho_\theta<1\); hence \(\eta_\theta<1\). By its definition, \(1-\eta_\theta\le A_\theta\) and \(1+\eta_\theta\ge1+\rho_\theta\). This proves (1); the zero polynomial is immediate.

## Checks, sources, limits and open items

The exact finite checks and floating illustrative spectra in `topics/mz-constants/directions/M3/RUNS.md` supplement the analytic component proofs. Candidate coverage and first kill tests are preserved in the adjacent `IDEAS.md`. Literature novelty is unresolved; explicit classical theorem/weight translations remain required before a new-result claim. No manuscript gate is changed by this development status.

The constants tend to eta=1 as theta approaches one. This theorem does not give one constant eta<1 uniformly on n=N−1 as N grows. Even when combined with endpoint lambda_min of logarithmic order and the current upper bound <2−c/N, it does not prove that 1−eta at that endpoint has logarithmic order: that conclusion also requires a sufficiently strong endpoint upper gap. The sharp constant and eventual active endpoint remain OPEN.

## History

2026-10-31, Codex gpt-6.1-sol xhigh, rules `d36722823441dc40c6e19d69a174459348dd309c`: original M3 target resolved in development by combining split substantive bounds, subject to independent review and prior-art screen.
