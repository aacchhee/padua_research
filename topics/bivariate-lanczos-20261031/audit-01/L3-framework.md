# Independent Codex audit: L3 framework

Auditor: Codex, assigned `gpt-6-astra`, effort `xhigh`; runtime effort metadata is not independently exposed. Date: 2026-11-01 UTC. Rules/head supplied by the coordinating auditor: `3a9063b84d14ca0a5998378371e27643fde50a29`; candidate: `5ccfac223f466a9105450365d8c6c3781ff7d922`; branch: `claude/bivariate-lanczos-20261031`. This subaudit performed no Git operations and changed no developer source. Source hashes and comparison with the candidate handoff are recorded in [L3-framework/manifest.json](L3-framework/manifest.json).

**Scoped verdict: changes required.** The normalized residual formulation of T302(b) is false as written (LF-M1, exact counterexample). T304 retains a substantive unproved isomorphism claim inside an overall-PROVED file without the required split (LF-M2). The independently reconstructed Favard correspondence, full-space cone criterion, rate theorem, square-case commutator bound, compression distinction, and computed-data consistency theorem survive this audit. The Padua degree-2 and equispaced degree-1-through-7 computer-assisted positive results pass fresh exact checks. These conclusions do not settle the frozen Greenbaum question G.

## Scope and independence

Own mathematical scope: T300–T310, T314–T315, N302 and N304–N308. T311–T313 and N301/N303 are assigned to the companion [L3-certificates audit](L3-certificates.md); dependencies and claim boundaries were coordinated, without treating that agent's output as this agent's own execution.

Read the complete `AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`, `state/IDEAS.md`, and `literature/INDEX.md`; the audit handoff, report, plan; all own-scope theory and negative-result files; L3 candidates, SUMMARY, R01–R06 and both reconstruction responses; both prior L3 reconstruction reviews and the L3 prior-art review. Mechanisms compared include localized positive cubature, moment-cone inradius, double-zero jets/Hessian alternatives, Favard consistency, exact sections versus arbitrary compression, and weight-only linearized fits. Supporting source/checker code was inspected as identified below. This audit does not establish priority or exhaustive novelty: original literature full texts and literature source locators were not independently verified. Parent audit owns registry and literature consolidation.

Fresh executions are separated below into (i) independently written checks importing no developer/reviewer modules, (ii) fresh runs of prior independent reviewer checkers, and (iii) fresh runs of developer programs. Existing developer/reviewer logs are evidence reviewed, not counted as fresh runs. The degree-2 certificate numbers are imported as data only and verified independently.

## Findings requiring correction

### LF-M1 — T302(b) uses the full-cone inradius for a different, normalized residual problem

Priority: medium (P2). Source: `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-302-backward-reduction-moment-cone.md`, lines 14, 22, 26 and 54. Line 14 permits every functional perturbation `||E|| <= epsilon` and asserts the exact residual threshold `(1-theta)epsilon`; line 22 first normalizes `Phi^{-1}(Hhat)` to the original mass. Line 26 does not impose `E(1)=0`. The proof at line 54 establishes distance from **L_mu+E**, whereas the definition measures distance from its **mass-normalized representative**. Normalization changes the distance and defeats the exact threshold, even for a strictly positive truncated moment matrix.

An exact counterexample is implemented in [exact_framework_checks.py](L3-framework/exact_framework_checks.py), output [exact_framework_checks.log](L3-framework/exact_framework_checks.log):

- Set `n=1`, `V=Pi_3`, with the ten nodes `(a,b)` where `a,b` are nonnegative integers and `a+b <= 3`. The evaluation Vandermonde determinant is 576, so the evaluation functionals form a basis. Use the allowed norm `||sum c_i ev_zi|| = ||c||_2`.
- Give `(1,1)` weight `alpha=1/1000` and every other node weight `(1-alpha)/9`. Then `L_mu(1)=1`, `C(K_0)` is the nonnegative orthant in these coordinates, and `r(0)=alpha`.
- Take `epsilon=2 alpha-alpha^2=1999/1000000`, `theta=1/2`, and `E=-epsilon ev_(1,1)`. The leading principal minors of `M_1(L_mu+E)` are exactly `998001/1000000`, `110778111/100000000`, and `36889110963/40000000000`, all positive. Thus `Hhat=Phi(L_mu+E)` is admissible.
- The proposed threshold holds strictly: `r(0)=1/1000 > (1-theta)epsilon=1999/2000000`. But the mass-normalized inverse is `(L_mu+E)/(1-epsilon)`, and its distance to `C(K_0)` is exactly `1/999 > 1999/2000000 = theta epsilon`. Even an unconstrained-mass approximant cannot achieve the claimed normalized residual.

This is not an endpoint-only objection to the strict `delta > delta*` wording. The strict distance gap persists for sufficiently small positive delta. For example, the coordinate-extracting polynomial for the negative node, shifted by `O(delta)` times the constant polynomial, is nonnegative on all delta-balls and preserves a strict separating margin. Meanwhile `r(delta) >= r(0) > (1-theta)epsilon`, so the asserted residual threshold has `delta*=0` and fails at such positive delta.

The unnormalized distance is `999/1000000`, which does satisfy the full-cone theorem. Thus the correction should preserve that proved theorem. Options: formulate residuals consistently against the unnormalized `L_mu+E`; or restrict to `E(1)=0` and derive the mass-slice criterion with its restricted dual seminorm (and, if required, fixed-mass approximant set); or include the normalization factors and state only the corresponding asymptotic rate. An exact constant cannot be carried through normalization unchanged. This finding does **not** invalidate exact conic membership, the rate exponents in T303, or sign-separation certificates N301/N303, all of which are invariant under positive scaling.

### LF-M2 — T304's first-order isomorphism must be split from its proved bounds

Priority: medium (P2), status/proof-scope correction. Source: `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-304-square-case-commutator-bounds.md`, lines 6, 14, 26, 33 and 51. The file has `Split into: none`, overall `PROVED`, and an affirmative statement that kappa is the first-order `S_1*` component. Its own status table says the induced map `V*/T -> Skew_(n+1)` being an isomorphism is only MEASURED for Padua n=2,3 and is not proved. The proof establishes vanishing on T and a dimension count; equal dimensions do not prove injectivity or surjectivity.

Retain (a), (b), and the derivative factorization as PROVED. Move the general isomorphism target to an OPEN claim and the finite numerical rank observation to a MEASURED claim, with the required split mappings and preserved wording history. Alternatively supply a complete general proof before claiming the isomorphism. `agents/WORKFLOW.md:61–67` and `agents/codex/CODEX.md:13` explicitly require splitting substantive claims of differing statuses; the explanatory History sentence at line 64 does not implement that rule. This does not downgrade the proved quadratic commutator bound.

## Proof reconstruction and scope assessment

| Claim | Independent assessment |
|---|---|
| T300 target and L0/L/E/G distinction | E is a useful exact-section companion interpretation. Its negative Padua results do not answer G. Keeping G and the frozen target OPEN is correct. |
| T301(a–c), truncated Favard correspondence | The word-swapping proof works through degree `2n+1`: at every adjacent swap one side has degree below n, annihilating the commutator supported on the final block. Positive pivots give the triangular polynomial map and cyclicity. Normalized moment uniqueness and the local analytic embedding follow. No normalization defect was found in T301 itself. |
| T301(d), computed entries | Counts are consistent with its explicitly stated half-next-step convention; these are not automatically the L1 count convention. Fresh exact checks reproduce excess counts 1,6,17,36 for n=1,2,3,4. |
| T302(a), full-space portion of (b) | Compact evaluations have constant coordinate 1, making the conic hull closed; bipolar separation and conic Caratheodory prove the equivalences and atom bound. Full-space inradius and unnormalized residual criteria are valid. LF-M1 concerns the subsequent normalized definition. |
| T303, rate theorem | Independently reconstructed the compactness/Taylor arguments: `S0=0` gives positive limiting inradius; `S1=0 != S0` gives linear radius; `S1!=0` gives an `O(delta^2)` upper bound; condition H gives the quadratic lower bound. A nonzero double-zero polynomial with positive-definite node Hessians yields a local sign obstruction. The PSD-singular degenerate case is not decided by these alternatives and remains OPEN. Constants depend on the fixed nodes, weights, degree and norm. |
| T304(a,b) | Barycenters cancel the first-order cluster displacement; normalized moments and Lagrange-square tests make each cluster mass positive, producing `||kappa|| <= C delta^2`. For commuting data, cyclicity gives simple joint spectrum and positive weights; normal-matrix eigenvalue inclusion gives the linear support bound. LF-M2 only concerns the additional isomorphism. |
| T305 and N302 | The triangle edge-product is the nonzero cubic double-zero polynomial; its nonzero node Hessians are indefinite. This proves H and the square-root worst-case radius. N302 rules out a uniform linear worst-case bound, not a square-root lower bound for every perturbation. |
| T306 | Exact Padua n=2 jet-kernel reconstruction and an independent rational certificate check pass; details below. |
| T307 | Numerical observations remain MEASURED. Historical runs/reviewer discussion were read, but the entire LP/SDP survey was not independently rerun here. No extrapolation in n is justified by that survey. |
| T308 and N304 | The full operator-valued measure/compression cone interior argument is valid. Its local smallness condition depends on the fixed support radius. Arbitrary symmetric compression is weaker than exact sections generated by polynomial Gram–Schmidt; it cannot remove the exact-section obstruction. |
| T309 | Quadratic ideal-generator representation, leading Hankel-orthogonality constraint, and node-Hessian formulas check out under the stated unisolvence. Dimension counting alone is not a positivity certificate. |
| T310 and N306 | Fresh exact checkerboard checks certify H for n=1 through 7. In particular the n=3 contrast with the Padua obstruction supports N306: jet and Hessian dimensions alone do not decide H. The Padua half is audited by the companion agent. |
| T314 | Completion enforces low-column commutation algebraically, even for asymmetric input. Symmetry, the upper block band and positive pivots give the reverse implication to Favard consistency; the asymmetry lower bound follows from distance to symmetric matrices. Fresh arbitrary rational input checks n=1 through 4 are nonvacuous. |
| T315 and N307/N308 | Fresh runs reproduce large completed-pair asymmetry and the stated failure of the restricted, linearized weight-only fit. These are finite measured failures, not a proof that no nonlinear nearby positive measure or Greenbaum model exists. |

Two summary-level issues were passed to the coordinating auditor for consolidation rather than counted as additional local findings: `report.md:23` overstates E as ruling out a Greenbaum model; `report.md:27` replaces the S0/S1 hypotheses by “nonnegative annihilator” language. The latter is concretely contradicted by any nondegenerate n=1 triangle in T305: H holds and the worst-case rate is square-root although every nonzero double-zero cubic has an indefinite node Hessian and there is no locally nonnegative annihilator. Use T303's actual spaces and H hypothesis. Stale CONDITIONAL/MEASURED labels and “unresolved/no rerun” wording in T300/T307/T310/N306 should be reconciled with their current evidence; these are documentation corrections, not new mathematical refutations. The companion audit owns the distinct unsupported uniform-in-n radius inference.

## Fresh checks, commands and results

All commands ran from `/workspace/padua_research`, completed with exit code 0, and redirected stdout/stderr into the named local logs. Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, SymPy 1.14.0, mpmath 1.3.0; no new package installation. `cvxpy` was unavailable, so no new cvxpy-based survey is claimed. Developer versions differ, as disclosed in its handoff. Source and output SHA256 values are in the manifest. No network service or source PDF was used.

### Independently written exact checks

```
python3 -I topics/bivariate-lanczos-20261031/audit-01/L3-framework/exact_framework_checks.py > topics/bivariate-lanczos-20261031/audit-01/L3-framework/exact_framework_checks.log 2>&1
```

Trusted dependencies: Python integer arithmetic and SymPy exact rationals/matrix operations. No developer/reviewer module imported. For T306, reconstructs the value/gradient kernel in Pi_5 at the six rational Padua n=2 nodes; obtains jet rank 18, kernel dimension 3, Hessian-map rank 3, and Pi_2 evaluation determinant `-27/2`. Reads the six rational dual matrices from developer `directions/L3/logs/exact_certificates.log` **as data**, independently verifies symmetry and exact positive principal minors, and verifies zero pairing with all three reconstructed Hessian basis vectors. PD dual blocks plus injectivity exclude a nonzero PSD Hessian tuple, which is precisely H. The certificate-data SHA256 is `287e8dd0bdaa60d93d728045fcd47c5c75832813657f4849081fe4b1e0629e8b`.

The same script proves the LF-M1 counterexample exactly and tests T314 on independently generated rational asymmetric recurrence data (seed 314, n=1–4), finding all commutator columns below the final degree exactly zero. These finite tests supplement the separately reconstructed general proof.

### Fresh execution of a prior independent exact checker

```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -I tracks/bivariate-lanczos/code/review_L3b/equi_H_cert.py 1 7 40 > topics/bivariate-lanczos-20261031/audit-01/L3-framework/equi_H_cert_n1_7.log 2>&1
```

The mpmath barrier stage at 40 decimal digits proposes matrices; exact Fraction RREF, exact annihilation and exact 2-by-2 positive-definiteness tests accept or reject them. The proof is the finite exact acceptance stage, not the numerical optimizer. All n=1–7 pass. The following are rounded diagnostic displays from this fresh run; the checker uses exact rational values in its acceptance tests.

| n | Node count | Displayed proposed t_D | Displayed certified min(det/trace), normalized |
|---:|---:|---:|---:|
| 1 | 3 | 0.08574031842 | 4.2870e-2 |
| 2 | 6 | 0.02004888867 | 1.0024e-2 |
| 3 | 10 | 0.001828246589 | 9.1412e-4 |
| 4 | 15 | 0.0001326479725 | 6.6324e-5 |
| 5 | 21 | 4.846957176e-6 | 2.4235e-6 |
| 6 | 28 | 4.615113567e-8 | 2.3076e-8 |
| 7 | 36 | 6.783388890e-11 | 3.3917e-11 |

The exact setup also verifies the expected jet ranks and injective Hessian maps. This fresh run supplies T310 evidence and was shared with the companion T311 audit. n=8 was not rerun here; neither these seven degrees nor their falling margins prove an asymptotic rate in n.

### Fresh numerical reruns

```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 tracks/bivariate-lanczos/code/L3/favard_check.py 4 0 > topics/bivariate-lanczos-20261031/audit-01/L3-framework/favard_n1_4_seed0.log 2>&1
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 tracks/bivariate-lanczos/code/L3/r02_closed_form_C.py > topics/bivariate-lanczos-20261031/audit-01/L3-framework/closed_form_C1.log 2>&1
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 tracks/bivariate-lanczos/code/L3/r06_consistency.py random 40 > topics/bivariate-lanczos-20261031/audit-01/L3-framework/consistency_random_n40.log 2>&1
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -I tracks/bivariate-lanczos/code/review_L3b/consistency_recheck.py rot03 18 20 > topics/bivariate-lanczos-20261031/audit-01/L3-framework/consistency_rot03_n18_20.log 2>&1
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -I topics/bivariate-lanczos-20261031/audit-01/L3-framework/lstsq_sensitivity.py > topics/bivariate-lanczos-20261031/audit-01/L3-framework/lstsq_sensitivity.log 2>&1
```

- **Favard:** developer checker freshly executed, n=1–4 seed 0. Exact low-commutator support checks pass for measure-generated and functional-generated examples. Floating-point word-formula relative errors are `1.95e-16, 7.40e-16, 1.35e-15, 5.33e-15`.
- **N305:** developer C1 proposal freshly executed, n=2–12. All nodewise minimum eigenvalues are negative, from `-1.125` at n=2 to `-1.417e-5` at n=12; printed Hankel-perp residual is zero. This reproduces failure of that explicit proposal, not failure of the whole dual-certificate method.
- **N307:** developer random-square seed-0 case, M=1681, block-window CGS, n up to 40. At n=28: orthogonality loss `3.29e-13`, completed asymmetry/u `2.09e3`, commutator/u `7.39`. At n=40: loss `2.68e-9`, asymF `3.59e-13`, asymJ `1.88e-9`, asymmetry/u `1.69e7`, commutator/u `8.87`. This reproduces the distinction between enforced commutation and symmetry and preserves the caveat that raw F can remain much closer to symmetric.
- **N308:** prior independent reviewer implementation freshly executed at rotation .3, M=1681, seed 0, n=18–20. With its long-double reference C, loss is `1.38e-9, 7.63e-9, 4.55e-8`; residual ratio rho is `.652, .709, .740`; maximum relative fitted weight perturbation is `4.4e-6, 1.4e-4, 3.9e-3`. Thus the measured restricted linearized fit leaves a substantial fraction of the coefficient error while the weight correction remains in the tested local regime.
- **Fit sensitivity:** own instrumentation of that unchanged reviewer implementation records the singular ranks. At n=18 the long-double-reference default solve has rank **739**, the expected partial moment-tangent dimension `dim Pi_37 - 2`, with last retained singular value relative to the maximum `1.407888e-6` and numerical null modes far below. This supports interpreting the default result as a fit to the intended tangent space. Cutting the threshold to `1e-14,1e-15,1e-16,1e-17` admits ranks `741,761,802,1681`, with rho `.630,.159,.385,.398` and relative weights from 3562 to 49675: those extra directions are numerical nullspace artifacts and leave the linear regime. They do not refute the default tangent fit and do not demonstrate a positive-measure fit. The double-reference solve has spurious ranks 762/763, supporting the existing warning against using that less accurate reference for this test.

## Limits and integration instructions

This audit verifies fixed-degree hypotheses and the explicitly scoped finite measured failures. It does not prove uniform conditioning in n, generalize random-seed measurements, solve the degenerate PSD-singular case, optimize over nonlinear positive measures, or answer G. It does not use the independent finite checks as substitutes for the general proofs reconstructed above. Full T307 surveys and n=8 checkerboard certificates were not rerun. Literature priority is outside the verified conclusion.

No source correction was made: the coordinating auditor should consolidate LF-M1/LF-M2, the report-level scope corrections and the companion certificate findings, then request a developer response and targeted re-audit. Preserve the surviving self-contained PROVED results. The local evidence directory is small (every artifact well below 1 MB); its exact sizes and hashes are in the manifest. Parent owns repository-wide generated-output budget, staging, commits and final protocol records.
