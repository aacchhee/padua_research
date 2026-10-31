# M3 fixed-ratio development and retained candidates

Rules/base: `d36722823441dc40c6e19d69a174459348dd309c`; date 2026-10-31. Developer: Codex, assigned gpt-6.1-sol xhigh. M3 activated only after M1's frozen first target was proved in development and its files/checks were handed to the independent auditor. The other active direction is M2; no third mathematical direction was opened. This worker owns only directions/M3, theory/m3-*.md, and code/m3_*.py for this stage.

## Novelty gate and frozen question

The complete current `state/IDEAS.md` was reread after the orchestrator populated seeds01–08. Its full obstruction and disposition tables were read. Shortlist read in full: M1 seed02, M2 seed03, fixed-ratio seed04 and the manuscript seed08. `literature/INDEX.md` and the current records `mz-classical-mz-screen.md`, `mz-an-wu-2022.md` were read. Actual `rg` search terms included Fejer/Fejér, Vallée, kernel, oversampling, fixed-ratio, hyperinterpolation, theta and 1−theta across tracks, topics, state and literature. M1 and M2 local proofs were inspected as dependencies; the supplied original code was not imported.

Frozen question remains: for **each fixed 0<=theta<1**, give an explicit eta(theta)<1 valid uniformly for all N>=2 and degrees n<=theta N, using the actual Lebesgue CC weights. An operator-stability result alone would not close this question. General historical MZ inequalities are a serious prior-art threat; exact fulltexts/weight translation are still unresolved. No novelty or acceptance claim follows from this local proof.

## IDEA?mz-constants-codex-31 — degree-sensitive sign comparison

Aliases: rho Z-matrix; ratio-dependent upper MZ constant.

- Question/scope: upper ratio <=1+(max(2n/N−1,0))²<2 for n<N.
- Mechanism/hypotheses: set Aρ=(1+ρ)M−R=ρM+D/2; exploit r−d>=2(N−n), r<=N at each active same-parity entry.
- Closest entries read: seed02, IDEA?…-13 sign replacement, and the complete M1 proof. This is a degree-sensitive refinement, proposed by the orchestrator and reconstructed here.
- Separation criterion: the smaller coefficient ρ=(2n/N−1)² must still dominate (d²−1)/(r²−1) on active off-diagonal entries. An allowed pair violating this scalar ratio kills the proposed constant, though not the factor-two theorem.
- Literature limits: historical CC sharp constants unresolved; standard Z-matrix comparisons supply no novelty by themselves.
- Obstruction escaped: the full-degree T_N obstruction disappears only because n<N; rho tends one as n/N tends one, so no uniform endpoint gap is claimed.
- Novelty verdict: variant with a specified quantitative difference from M1; external duplicate status pending.
- First kill test and prewritten criterion: check the extremal max(i,j)=n pair and exact ratio inequality; reject this constant if d/r>2n/N−1. Algebra gives d/r<=1−2(N−n)/r<=2n/N−1, so the test survives. Exact finite enumeration follows.
- Actual evidence: checker passes every pair 2<=N<=25, 0<=n<N, and every same-parity off-diagonal entry. Universal proof is analytic.
- Disposition: development complete; PROVED, acceptance pending.
- Canonical theory: PD-T?mz-constants-codex-31, `m3-upper-ratio.md`.

## IDEA?mz-constants-codex-32 — filtered circle reconstruction removes the log N loss

Aliases: oversampled Fejér kernel; de la Vallée Poussin difference; inverse weighted Schur.

- Exact question/scope: lower ratio >=(1−n/N)²/C* for every 0<=n<N, with absolute explicit C*.
- Mechanism/hypotheses: the difference K=(NF_N−nF_n)/(N−n) has a Fourier plateau through n and degree N−1. Discrete convolution on the 2N-circle grid reproduces q(t)=p(cos t). Its inverse-square kernel decay remains summable after multiplying by sqrt[(|sin t|+1/N)/(|sin tj|+1/N)]. A weighted Schur bound then controls continuous Lebesgue norm by the positive CC samples.
- Closest entries read: seed03 ordinary cardinal lower spectrum and seed04 fixed ratio; M2's cardinal kernel only decays as inverse distance, producing log² N. M2's weight floor is a proved-development dependency, not an inherited private theorem.
- Separation criterion: exact reproduction for every degree <=n with degree cutoff <N must coexist with inverse-square spatial decay. Failure of the plateau at k=n, or an alias l−k=±2N, kills this exact reconstruction; ordinary cardinal interpolation has no such fixed-ratio decay claim.
- Literature baseline/limits: classical filtered reconstruction is established technique and may already yield this norm result; fulltext historical match unresolved. No priority claim.
- Applicable obstruction escaped: oversampling by N−n>0 permits tapering; at n=N the kernel is undefined, and at n=N−1 its bound degenerates, so no false uniform endpoint lower bound follows.
- Novelty verdict: quantitative variant of classical reconstruction applied to the exact CC norm; external duplicate verdict pending.
- Cheapest decisive test/kill criterion written before estimates: inspect Fourier coefficients at |k|=n and |k|=N and the maximal alias difference. The coefficient at n is exactly one, degree is N−1, and |l−k|<=n+N−1<2N. The n=0 convention nF_n=0 is checked explicitly.
- Verification plan/outcome: exact Fourier tests passed all 324 pairs N2..25; analytic row/column Schur constants give C*=12(1+pi)^4(1+2/pi). Independent adversarial auditor separately reconstructed the plateau, shell counts, circle factors and constant before pinned audit and found no gap. Pinned rerun/reconstruction remains pending.
- Disposition: development complete; PROVED, acceptance pending.
- Canonical theory: PD-T?mz-constants-codex-32, `m3-lower-ratio.md`.

## IDEA?mz-constants-codex-33 — hyperinterpolation uses the upper Gram bound directly

Aliases: adjoint evaluation bound; positive-rule hyperinterpolation stability.

- Question/scope: does the quadrature hyperinterpolant L_n f=Σ Q(fP_i)P_i have L∞→L² norm <=sqrt(V lambda_max), and the corresponding error <=sqrt(V)(1+sqrt(lambda_max))E_k under reproduction?
- Mechanism/hypotheses: positive weights, total weight V, orthonormal continuous basis; weighted Cauchy–Schwarz and finite-dimensional duality. No inverse Gram matrix enters this defined operator.
- Closest entries read: seed04; selected An–Wu source statement in the literature record. The source theorem is conditional; this is a direct independent inequality rather than a claimed refutation.
- Separation criterion: the operator must be the direct quadrature-coefficient operator. If its definition inverts a Gram matrix, the adjoint argument would not describe it. Written coefficient duality is the cheapest decisive check.
- Literature limits: published source fulltext and historical operator estimates remain incompletely screened. The independent auditor reports primary ASV arXiv2601.04708v1 equation(7) already has the factor1+sqrt(1+eta) with aliasing term, and equation(8) separates inverse-Gram least squares. Thus the generic upper-Gram mechanism is known context, and only the proved CC-bound application is developed here. The source record will carry the auditor's exact reading coverage. No erratum or novelty claim.
- Applicable obstructions escaped: small minimum Gram eigenvalue can affect inverse fitting but does not enter this adjoint norm. Signed quadrature weights are outside the assumptions.
- Novelty verdict: equivalent reconstruction of a known generic mechanism; the exact CC application is separate and its prior-art screen remains pending.
- First kill test/criterion: compute sup over unit coefficient vector of |Q(fp)|. If weighted Cauchy–Schwarz required a lower Gram factor, the proposed upper-only estimate would fail. It instead gives sqrt(Q(f²)Q(p²))<=sqrt(VB)||f||∞ immediately. The exactness condition must integrate each product rP_i; n+k suffices.
- Actual result: complete analytic proof; no implementation-mirroring numerical test needed. For CC n<N, B<2 gives a uniform constant below(1+sqrt2)sqrt2 in the error estimate whenever k<=min(n,N−n).
- Disposition: PROVED development, independent review pending; does not replace fixed-ratio eta target.
- Canonical theory: PD-T?mz-constants-codex-34, `m3-hyperinterpolation.md`.

## IDEA?mz-constants-codex-34 — explicit two-sided assembly

Aliases: strong eta(theta); fixed-ratio spectrum interval.

- Question/scope: the original frozen M3 target, explicit eta(theta)<1.
- Mechanism: combine IDEA?…-31 and -32 without another analytic mechanism.
- Closest entries read: seed04 and both full component proofs. This is their exact synthesis, not a separately novel candidate.
- Separation criterion: no separation claimed from the two components; both endpoints must hold uniformly for every n<=theta N. A constant depending on N kills the claimed uniform conclusion.
- Literature limits: strong classical-MZ prior-art risk remains.
- Applicable obstruction: theta=1 is excluded; 1−eta approaches zero as theta approaches one.
- Novelty verdict: equivalent synthesis, no new mechanism or priority claim.
- Cheapest decisive test/criterion: substitute 1−n/N>=1−theta and verify rho(n/N)<=rho(theta), then check Atheta>0 and rho(theta)<1. These scalar inequalities hold.
- Actual result: eta(theta)=max{1−(1−theta)²/C*,max(2theta−1,0)²}<1. Spectrum lies in[(1−theta)²/C*,1+max(2theta−1,0)²].
- Disposition: target PROVED development, acceptance pending. No PD-N is created for a successful/equivalent synthesis.
- Canonical theory: PD-T?mz-constants-codex-33, `m3-uniform-eta.md`.

## Round ledger and endpoint caveat

| Round | Distinct mechanism / decisive obligation | Outcome |
|---|---|---|
| 1 | Degree-sensitive Z-matrix comparison | Explicit uniform upper gap at fixed ratio proved |
| 2 | Filtered discrete reconstruction plus weighted Schur | Explicit uniform positive lower bound proved |
| 3 | Direct hyperinterpolation adjoint norm | Separate upper-Gram application proved |

All first M3 target obligations are resolved in development, leaving prior-art and independent acceptance. No failed mechanism was generated in this bounded M3 cycle; no PD-N allocation is warranted. At n=N−1, the available upper gaps are only order1/N and cannot be combined with endpoint lambda_min~log^-2 N to conclude 1−eta~log^-2 N or eventual active minimum endpoint. The sharp limiting upper constant stays OPEN. No manuscript was written by this worker.

## Provisional split map

| ID | File | Development status |
|---|---|---|
| PD-T?mz-constants-codex-31 | tracks/mz-constants/theory/m3-upper-ratio.md | PROVED |
| PD-T?mz-constants-codex-32 | tracks/mz-constants/theory/m3-lower-ratio.md | PROVED |
| PD-T?mz-constants-codex-33 | tracks/mz-constants/theory/m3-uniform-eta.md | PROVED |
| PD-T?mz-constants-codex-34 | tracks/mz-constants/theory/m3-hyperinterpolation.md | PROVED |

The orchestrator owns global final-ID/crosswalk integration and every Git mutation.
