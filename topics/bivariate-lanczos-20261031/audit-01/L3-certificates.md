# L3 certificate and obstruction audit

Date: 2026-11-01. Auditor: Codex independent subagent `/root/audit_l3_certificates`. Launch parameters recorded by the orchestrator: `gpt-6-astra`, `xhigh`, `fork_turns:none`; this subagent has no independent runtime confirmation of model/effort. Developer: Claude. This audit makes no developer-file edits or Git changes.

Rules were read at **`3a9063b84d14ca0a5998378371e27643fde50a29`**. The scientific candidate is **`5ccfac223f466a9105450365d8c6c3781ff7d922`** on `claude/bivariate-lanczos-20261031`. Subsequent orchestrator audit checkpoints do not change the scientific inputs. All nine theory hashes in [the manifest](L3-certificates/manifest.json) match the handoff, including T311/T312/T313/N301/N303. The manifest records full SHA-256 identities, sizes, environment, actual commands and outputs for seven completed executions.

## Verdict

**Core certificate mathematics confirmed; one medium scope overclaim and one low status-maintenance finding remain.** N301 is supported by an independently implemented exact certificate check and a fresh execution of the prior independent checker. T312 and T313 have a complete all-n analytic proof, with independently reconstructed algebra and fresh exact checks. N303 follows under its explicit Padua-unisolvence assumption. No counterexample or missing edge/corner case was found in those core statements. The claim that there is *no uniform obstruction radius in n* is not established by the supplied evidence and should be withdrawn or proved. This is not a failure of the per-degree obstruction theorem.

T311 remains a finite **MEASURED** claim. Its recorded values and ratios agree with the source logs; no asymptotic law or bound for the constant in T303(d) is certified by them. A fresh full equispaced rerun belongs to the companion [L3 framework audit](L3-framework.md); that execution was still in progress when this report was finalized and is not counted as a completed execution here.

## Coverage

Read in full: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`; all of `state/IDEAS.md`, including its obstruction and disposition tables; all of `literature/INDEX.md`; topic `audit-handoff.md`, `plan.md`, `report.md`; L3 `candidates.md`, R01/R04/R05 and both developer responses; both L3 reconstruction reports. Read the L3 prior-art report for its mechanism comparisons and explicit source-reading limitations. No new external source was fetched or inherited as a proof.

Theory read in full for this scope: T311, T312, T313, N301, N303 and dependencies T302, T303, T309. T301's uniqueness and consistency claims were checked at the application boundary and independently audited by `/root/audit_l3_framework`; its full audit belongs to that report. That agent reported that the normalized uniqueness/words argument holds. Its separate findings about T302's normalization and residual threshold do not affect the certificate separation argument below.

Code inspected: developer `exact_certificates.py`; reviewer `indep_exact_check.py`, `turan_symbolic.py`, `padua_turan_check.py`, `padua_delta0.py`, and `rigorous.py`; and the small family-failure script whose output is retained. The new [independent checker](L3-certificates/independent_certificate_check.py) imports no campaign code. It reads only the developer's polynomial coefficients as data and implements a separate exact n=3 evaluation/Taylor check, plus a different symbolic interior reconstruction.

Novelty scope: no new mechanism or novelty claim is proposed. The existing candidates and negative scopes were checked against the full registry. The prior-art report explicitly uses summarizing fetches and leaves significant literature unread; this audit does not upgrade those literature comparisons or claim an exhaustive search. The distinction between reading (E), exact representation of arbitrary consistent perturbations, and the still-OPEN Greenbaum reading (G) is essential and is preserved here.

## Findings

### LC-M1 — A decreasing certified lower bound does not establish absence of a uniform obstruction radius

Locations: T313 `bivariate-lanczos-claude-313-padua-turan-certificate-all-n.md:64`; N303 `bivariate-lanczos-claude-N303-padua-all-n-exact-backward-obstruction.md:10`; propagated to T300 `bivariate-lanczos-claude-300-l3q1-backward-interpretation-target.md:33`. The immediate source is reconstruction 02 finding L7, accepted in `directions/L3/response-recon-02.md`.

T313 concludes from finite lower bounds and sampled negative radii that “δ_0(n) → 0 ... with no radius uniform in n.” The first part needs careful interpretation: an existentially chosen valid radius can always be replaced by `min(radius,1/n)`, so the existence of a shrinking choice is unobjectionable but says nothing about the optimal radius. The unsupported substantive inference is the exclusion of a positive radius uniform in n.

The rigorous outputs are **lower bounds** for a sufficient positivity radius of this particular polynomial P_n, only for n=4,...,12. This audit reran and confirmed those bounds. Decreasing lower bounds cannot bound the maximal radius from above. The sampled negative points are floating evidence for loss of positivity of this particular P_n at finitely many n; they neither prove an all-n limit nor exclude a different certificate or obstruction on larger neighborhoods.

Requested correction: retain the valid per-degree theorem and write, for example, “The certified lower bounds decrease over n=4,...,12. No uniform-in-n obstruction radius is established here; asymptotics remain open.” Distinguish a chosen sufficient radius, the maximal positivity radius of P_n, and a maximal radius for any obstruction if further claims are intended. Do not edit the old auditor's report; record the disposition of its L7 recommendation in the developer response/history.

Severity: **medium**, because the unsupported nonuniformity claim is part of the current mathematical statement/summary. The core certificate and exact-section obstruction survive unchanged.

### LC-L1 — Current status pointers still describe discharged obligations

Locations: N303 `:24` still labels the P_n certificate **CONDITIONAL** on symbolic expansion, although T313 and the N303 overall status are PROVED; `directions/L3/candidates.md:139,145,159` retain pending-rerun/unresolved language inconsistent with the current claims; T311 `:23` says seven values after its statement was updated to eight, and `:27` says “No independent rerun yet” while citing the same prior independently rerun evidence as T310. T300's split list also retains obsolete CONDITIONAL labels; that file is owned by the companion audit.

Requested correction: synchronize the *current* status table and candidate/obstruction pointers with the accepted evidence, while preserving explicitly dated historical round statements. T311 should distinguish prior independent computations, this audit's log review, and the companion audit's actual new execution. No numerical or theorem status upgrade follows from this maintenance change.

Severity: **low**. The certificate obligation is genuinely discharged, so this is a misleading current record rather than a missing proof.

## Independent mathematical reconstruction

### N301: rational septic and its certified neighborhood

The committed certificate data has SHA-256 `287e8dd0bdaa60d93d728045fcd47c5c75832813657f4849081fe4b1e0629e8b`. The new checker parses exactly 20 nonzero rational coefficients, checks total degree 7 and evenness in y, and builds the ten nodes directly from x in `{1,1/2,-1/2,-1}` and y in `{1,sqrt(2)/2,0,-sqrt(2)/2,-1}` with even index parity.

Independent arithmetic represents `a+b sqrt(2)` as a pair of Python Fractions. It verifies exact zero value and both derivatives at every node; the leading Hessian entry and determinant are strictly positive using rational enclosures whose squared endpoints straddle 2. It does not use the developer's basis, nullspace, SDP, field class or sign routine. The negative polynomial fails the PD test, and adding a constant fails the zero-value condition.

For each node, the checker expands the polynomial exactly through degree 7. If `lambda=det(H)/tr(H)` and `B_k` bounds the sum of absolute coefficients of the homogeneous Taylor part of degree k, then for `r=|h|_2`:

`p*(z+h) >= r^2 [lambda/2 - sum_(k=3)^7 B_k r^(k-2)]`.

At the published radius `30117029139000/77370908310949543`, the bracket has a strictly positive rational lower bound at every node; its smallest bound is approximately **0.04615155**. Thus the original radius is verified independently without the developer's third-derivative estimate.

Fresh execution of the previous reviewer checker also confirms rank J=30, dim S1=6, rank Hess|S1=6, minimum eigenvalue lower bound about 0.112782, and the stronger **0.04** punctured-square positivity certificate. The latter implies positivity on the Euclidean discs and is an actual new rerun, not merely a reading of the old log. It is supplementary; the new independent checker already validates the stated N301 radius.

### T312: interior criterion, including nondegeneracy

At an interior node put theta=j*pi/n, phi=k*pi/(n+1), S=sin²(theta), T=sin²(phi). The elementary node identities give the printed generator gradients. For direction u, writing the sine sequence in coordinates A,B gives

`Q = sin²(theta+phi) A² + 2(S-T)(1-8cST) AB + sin²(theta-phi) B²`.

The change of direction coordinates is invertible because both sines sin(theta), sin(phi) are nonzero. Neither sin(theta+phi) nor sin(theta-phi) vanishes: equality of the angles, or their sum being pi, would force n to divide j by gcd(n,n+1)=1, contradicting 0<j<n. Hence S-T is also nonzero.

The determinant is `16cST(S-T)²(1-4cST)`, so, with its positive first diagonal entry, Q is PD exactly when `0<cST<1/4`. The checker independently reconstructs the same determinant in the alternative a,b coordinates using only Chebyshev recurrences and polynomial reduction by `sx²=1-x²`, `sy²=1-y²`; the factor is divided by four as required by the coordinate change. This tests an identity in symbolic variables rather than a sample of angles.

Degree cancellation and double zeros follow from the top forms and products of vanishing generators. For n>=3 the four generators used have the asserted normalization, including m=3 at n=3. The lemma's stated n range is valid. In particular c=1/10 makes every interior Hessian PD.

### T313: all edges and corners

Starting from `T_k'(1)=k²` and `T_k'(-1)=(-1)^(k+1)k²`, I re-derived E1/E3 and the parity reductions to E2/E4. The possible corners are (1,1), (1,-1) for odd n and (-1,1) for even n. The fourth corner has index sum 2n+1 and is never a node. Every product in the quadratic form has even generator-index sum, so the parity factors cancel and reflection of one direction coordinate preserves PD.

For `Q=A u1²+X u1*u2+B u2²`, the recomputed normalized discriminants, with s=1-t², are

* E1: `32s²/5 + n(121n-1040)s/100 + 99n²/100`, with B=(n+1)².
* E3: `32s²/5 + (n+1)(121n-919)s/100 + 99(n+1)²/100`, with A=n².
* Corner: `4AB-X²=99n²(n+1)²/25`, with `A=n²(9n²-36n+80)/20>0`.

The first two expressions are `(4AB-X²)/(n²(n+1)²)`. Dropping the positive quadratic term leaves a linear function whose endpoint values are positive for E1 when n>=5, and E3 when n>=4. At n=4 the E1/E2 nodes have k=2 or 4, giving exactly `(247 +/- 89 sqrt(5))/50>0`; the strict inequality follows from 247²>5*89². This covers the otherwise missing n=4 boundary case. The corner diagonal is positive because its inner quadratic has negative discriminant and positive leading coefficient.

This is an all-n proof: the dependence on n has been reduced to the displayed fixed polynomial identities and elementary inequalities. The interval check n=4,...,16 corroborates it but is not the reason for the universal quantifier. The proof uses only vanishing and the generator gradients, not the unproved general assertion that every S1 polynomial is in the quadratic-generator family.

### N301/N303: functional perturbations and exact sections

For any positive weights, `L_mu(p)=0` for the relevant certificate. Positive definite node Hessians and double zeros imply `p>=0` on some common closed neighborhood by Taylor's theorem. The moment matrix `M_n(L_mu)` is positive definite when the nodes are Pi_n-unisolvent, and positive definiteness is open, so sufficiently small perturbations E yield well-defined sections with the exact structural and interior-commutativity conditions. Analytic dependence of Gram-Schmidt/Cholesky gives an O(epsilon) section change; the square-case unperturbed pair commutes, so the last-block defect is O(epsilon).

If `E(p)<0`, every positive measure nu supported in that neighborhood satisfies `L_nu(p)>=0`, whereas `c(L_mu+E)(p)<0` for every c>0. Equality of normalized exact sections determines the functional up to such a positive scalar by T301, so equality of sections is impossible. Also

`||L_nu-L_mu-E|| >= |E(p)|/||p||_*`.

This argument works for the full positive cone and is unaffected by whether a separate residual theorem is formulated on a fixed-mass slice. It does not require interpreting all functional norms as identical section norms. The normalized negative evaluation example has the stated norm, and smallness is correctly restricted to the regime preserving `M_n>0`.

For N303, all-n Padua unisolvence remains an explicitly assumed literature fact; this audit has not replaced that assumption by a new all-n unisolvence proof. T313's polynomial assertion itself needs no such assumption. For N301, a fresh exact Vandermonde-rank rerun verifies unisolvence at n=3 (also n=1,2,4), so no unverified unisolvence assumption remains in this finite case. The obstruction does not characterize real floating-point errors or settle reading (G), and it does not rule out residuals of the same order as the perturbation.

### T311: what the margins establish

The developer logs report exact-certificate margins approximately `4.287e-2, 1.002e-2, 9.141e-4, 6.632e-5, 2.423e-6, 2.308e-8, 3.396e-11`. These agree at the stated precision with T311. The prior reviewer log reports high-precision proposal values `0.08574031842, 0.02004888867, 0.001828246589, 0.0001326479725, 4.846957176e-6, 4.615113567e-8, 6.78338889e-11`, and the separate n=8 log gives `4.124591777e-15`. Their ratios agree with 4.28, 10.97, 13.78, 27.4, 105, 680, and about 16400. The low-precision n=8 solve failed exact acceptance; that failure is not a negative theorem.

These are finite numerical proposal values and exact feasibility margins, not an exact proof of an optimum or a super-geometric asymptotic. T311 explicitly labels the pattern MEASURED and leaves asymptotics and the quantitative link to T303(d)'s constant open. That status is appropriate. This subagent did not rerun the equispaced optimizer; fresh execution and exact feasibility evidence belong to the companion audit.

## Executed checks and evidence

All commands below ran from `/workspace/padua_research`, with stdout redirected to `topics/bivariate-lanczos-20261031/audit-01/L3-certificates/<log>`. They completed with exit code 0; outputs were inspected, including expected failure controls. Exact full commands, input/output hashes and byte sizes are in [manifest.json](L3-certificates/manifest.json).

| Command | Log | Observed result |
|---|---|---|
| `python3 -I -B topics/bivariate-lanczos-20261031/audit-01/L3-certificates/independent_certificate_check.py topics/bivariate-lanczos-20261031/directions/L3/logs/exact_certificates.log` | `independent_certificate_check.log` | independent n3 certificate/radius and symbolic interior/boundary/corner identities PASS |
| `python3 -I -B tracks/bivariate-lanczos/code/review_L3/indep_exact_check.py topics/bivariate-lanczos-20261031/directions/L3/logs/exact_certificates.log` | `rerun_n3_exact.log` | exact n3 zeros/PD/radius PASS; rigorous radius .04 PASS; auxiliary n1/n2 checks also PASS |
| `python3 -I -B tracks/bivariate-lanczos/code/review_L3b/padua_turan_check.py 3 16` | `rerun_turan.log` | expected n3 FAIL (-225); n4..16 degree/double-zero/boundary-gradient/interval-PD PASS; all tested interior equivalences agree |
| `python3 -I -B tracks/bivariate-lanczos/code/review_L3b/padua_delta0.py 4 12` | `rerun_delta0.log` | all nine rigorous lower bounds reproduced, 5.6302e-4 through 6.5495e-8; sampled negative radii retained as MEASURED |
| `python3 -I -B tracks/bivariate-lanczos/code/review_L3b/turan_symbolic.py` | `rerun_symbolic.log` | all symbolic interior/boundary identities and exceptional n4 values PASS |
| `python3 -I -B tracks/bivariate-lanczos/code/review_L3b/kappa_family_n3.py` | `rerun_family_n3.log` | n3 edge requires c>3/5, inconsistent with the interior condition c<1/3 at (j,k)=(1,2) |
| `python3 -I -B tracks/bivariate-lanczos/code/review_L3/unisolvence_check.py` | `rerun_unisolvence.log` | exact Vandermonde ranks 3,6,10,15 for n=1,2,3,4; all unisolvent |

The seven small output logs total under **17 KB** (exact sizes in the manifest). The manifest and the two small audit scripts are necessary evidence/provenance, staged for orchestrator integration. No external archive or storage destination was invented; preservation and retrieval are via these repository paths and hashes. Generate the manifest with `python3 -I -B topics/bivariate-lanczos-20261031/audit-01/L3-certificates/record_evidence.py`.

## Computer-proof obligations and limits

* **Finite reduction:** N301 reduces to the explicit polynomial's finite exact jets and a rigorous Taylor bound; T313 reduces analytically to a finite number of symbolic identities and all-n inequalities. The obstruction reduction is proved above and in T303(e).
* **Exact arithmetic:** the new n3 checker uses Python integers/Fraction and verified rational sqrt(2) bounds. Symbolic checks use SymPy 1.14.0. Prior-reviewer reruns use SymPy algebraic arithmetic or integer/Fraction polynomial and interval arithmetic. The interval multiplication rounds outward; node proposals are accepted only after exact sign changes and disjoint ordered intervals certify all roots of U. The Taylor radius checker uses exact coefficient bounds and strict rational inequalities.
* **Code and evidence:** the original checkers and coefficient data are present in the candidate. This audit adds its separate checker and actual rerun logs with full content identities; they require the orchestrator's normal commit/integration, which this subagent does not perform.
* **Independent execution:** all seven executions listed here actually ran in this session. Inspection of the historical equispaced logs is identified separately and is not counted as a rerun.

Environment: Python **3.12.14**, SymPy **1.14.0**, NumPy **2.3.5**, mpmath **1.3.0**, Linux x86_64 (full platform in the manifest). Developer proposal code was inspected but its cvxpy optimization was not rerun here; fixed certificate acceptance is independent of cvxpy/CLARABEL. The previous reviewer uses mpmath only to propose node brackets; exact sign checks certify them. NumPy and floating eigenvalue/radius displays are not trusted for positivity. Shared SymPy use is disclosed; the core n3 acceptance has a separate Fraction-only implementation.

No finding here supplies an all-n unisolvence proof, an asymptotic radius bound, a uniform-in-n obstruction theorem, or a theorem about actual floating-point error directions. No developer proof was silently fixed and then self-approved. Resolve LC-M1 and LC-L1 in a developer response; the verified per-degree certificate results can be retained at their stated status, with N303's explicit unisolvence assumption.
