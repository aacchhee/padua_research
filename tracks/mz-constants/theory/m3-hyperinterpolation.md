# PD-T025 — hyperinterpolation stability from the upper Gram bound

Review update, 2026-10-31: final ID allocation and scoped independent Astra review are complete; see topics/mz-constants/independent-astra-01.md and ID_CROSSWALK.md. The original development-stage pending-review wording below is historical. Required Claude audit and unresolved literature/novelty coverage remain PENDING. This administrative update changes no mathematical claim or proof.

ID kind: PD-T. Aliases: positive-rule upper-Gram stability; corrected use of an MZ factor.
Split from: M3 applicability question. Split into: none; this supporting application does not replace the fixed-ratio MZ target.

## Statement and definitions

Let \(\mu\) be a finite positive measure of total mass \(V>0\) on a compact domain, and let \(\{P_1,\ldots,P_d\}\) be an orthonormal basis for a real polynomial space \(\Pi_n\) in \(L^2(\mu)\). Let a quadrature rule \(Q(f)=\sum_{j=1}^s w_j f(x_j)\) have \(w_j>0\), \(\sum_j w_j=V\), and suppose
\[
Q(p^2)\le B\|p\|_{L^2(\mu)}^2\qquad(p\in\Pi_n).
\]
Define the quadrature hyperinterpolant
\[
\mathcal L_nf=\sum_{i=1}^d Q(fP_i)P_i.
\]
Then
\[
\|\mathcal L_nf\|_{L^2(\mu)}\le\sqrt{VB}\,\|f\|_\infty.\tag{1}
\]
If, in addition, Q integrates every polynomial of degree at most n+k exactly, where 0<=k<=n, then
\[
\|f-\mathcal L_nf\|_{L^2(\mu)}
\le\sqrt V(1+\sqrt B)E_k(f),\tag{2}
\]
where \(E_k(f)=\inf_{r\in\Pi_k}\|f-r\|_\infty\). On a general polynomial domain, assume explicitly that products of a degree-k polynomial and degree-n basis member have degree at most n+k.

For Lebesgue CC on [-1,1], N>=2 and 0<=n<N, one can take
\[
B=\min\left\{2-\frac2{\pi N},\ 1+\max\{2n/N-1,0\}^2\right\}<2.
\]
For every 0<=k<=min(n,N−n), bound (2) consequently has constant at most \((1+\sqrt2)\sqrt2\), uniformly in N and n. If n=0, k=0 is permitted. The extra parity exactness of even-N CC can enlarge k, but is not required here.

## Status and dependencies

Overall status: **PROVED** in development; pinned independent review and historical source comparison pending. General bound (1) requires no lower Gram estimate and no eta<1 assumption. Its application does not assert that the true operator norm grows logarithmically when the inverse Gram eigenvalue does.

Depends on elementary finite-dimensional duality, proved below; the CC application uses positive weights/exactness from PD-T013, upper theorem PD-T014, and fixed-ratio upper theorem PD-T022. No external hyperinterpolation theorem is assumed.

## Proof

Let \(c_i=Q(fP_i)\) be the coefficient vector of \(\mathcal L_nf\). For any unit Euclidean vector a, the polynomial \(p_a=\sum_i a_iP_i\) has continuous norm one. Weighted Cauchy–Schwarz gives
\[
|a\cdot c|=|Q(fp_a)|\le Q(f^2)^{1/2}Q(p_a^2)^{1/2}
\le\sqrt{VB}\,\|f\|_\infty.
\]
Taking the supremum over unit a yields \(\|c\|_2\le\sqrt{VB}\|f\|_\infty\). Orthonormality identifies \(\|c\|_2=\|\mathcal L_nf\|_{L^2(\mu)}\), proving (1).

For every \(r\in\Pi_k\), the asserted exactness gives \(Q(rP_i)=\int rP_i\,d\mu\). Since r belongs to \(\Pi_n\), orthonormal expansion gives \(\mathcal L_nr=r\). Therefore
\[
\|f-\mathcal L_nf\|_2
\le\|f-r\|_2+\|\mathcal L_n(f-r)\|_2
\le\sqrt V(1+\sqrt B)\|f-r\|_\infty.
\]
Taking the infimum proves (2), without needing attainment. In the CC case V=2 and exactness through N suffices for every stated k. The explicit upper bound follows from the two cited local theorems.

## Checks, sources, limits and open items

The proof is analytic and finite-dimensional. No numerical test is necessary to establish the elementary dual norm calculation. The source comparison is scoped: `literature/records/mz-an-wu-2022.md` records a conditional 3sqrt(V) error bound with eta=3/4 in selected arXiv v3 primary text. The independent auditor's primary-text read additionally identifies ASV arXiv:2601.04708v1 equation(7) as already using the factor 1+sqrt(1+eta), with an aliasing term, and equation(8) as explicitly separating the inverse-Gram least-squares operator. The generic upper-Gram mechanism is therefore known context; this file independently reconstructs it and applies the new locally proved CC bound. No novelty is claimed for the generic mechanism. These auditor-reported locators are literature context, not proof dependencies, and the orchestrator will update the source record with the exact reading coverage.

The estimate here does not refute the conditional An–Wu theorem or establish a journal erratum. Published-text and historical coverage remain explicit literature gaps.

This is the ordinary quadrature hyperinterpolant, not least-squares fitting through inversion of the Gram matrix; its operator is exactly the one defined above. Any claimed transfer to another operator must recheck its definition. The result has no conclusion for signed quadrature weights.

## History

2026-10-31, Codex gpt-6.1-sol xhigh, rules `d36722823441dc40c6e19d69a174459348dd309c`: the orchestrator identified that an inverse-MZ factor need not be the true stability norm. This file reconstructs the corrected direct upper-Gram argument as a separate substantive application.
