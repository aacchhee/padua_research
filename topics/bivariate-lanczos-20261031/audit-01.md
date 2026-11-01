# Codex audit-01 — bivariate Lanczos campaign

Date: 2026-11-01 (Europe/Oslo). Scientific candidate: **`5ccfac223f466a9105450365d8c6c3781ff7d922`**. Session-start head/rules: `3a9063b84d14ca0a5998378371e27643fde50a29`. Fetched main: `07c5f5465d6de306aa81dbe8ca1f615295163864`. The candidate's **67 theory files** are byte-identical to the session-start head and working science; no developer proof, claim, experiment code or historical log is edited by this audit.

Auditor: independent Codex team, separate from the Claude developers and earlier Claude reconstructors. AC requested `gpt-6-astra xhigh`; each of the six workers was launched with explicit `model=gpt-6-astra`, `reasoning_effort=xhigh`, `fork_turns=none`. Runtime model/effort metadata is not independently exposed to the workers; the root's separate runtime identity is likewise unexposed. The workflow authorizes bounded agentic audit orchestration; only the root controls Git.

## Verdict

**CHANGES REQUIRED — return to WORK.** The central exact certificates and many foundational proofs survive independent reconstruction and actual reruns. The submission nevertheless contains false or overbroad statement variants, inconsistent normalization, unsupported evidence interpretation and required claim splits. This is not acceptance of the campaign as a whole. Retain valid exact results and their proved scopes; do not downgrade them merely because a separate application, corollary or measurement needs correction.

The clearest mathematical counterexample concerns **T302(b)'s normalized residual threshold**: its unnormalized cone-ball theorem is correct, but the claimed identical threshold after fixing functional mass is false. An exact rational example has `r(0)=1/1000 > (1-theta)*epsilon=1999/2000000`, while the normalized distance to the cone is `1/999 > theta*epsilon=1999/2000000`, with a positive-definite degree-one moment matrix. The root separately inspected and executed the independent auditor's checker. The rate exponents and the negative Padua certificates are not refuted by this normalization defect.

## Coverage and detailed reports

The full idea registry and obstruction/disposition tables were read for the mechanism/negative audit. Per-direction reports document full candidate scope, proofs reconstructed, source coverage, actual commands, source/output hashes, findings and limits. Existing literature digests are identified as such; no exhaustive novelty search or new primary-source verification is claimed.

| Audit scope | Report | Principal checked result / remaining issue |
|---|---|---|
| L1 foundations and L4 | [L1-foundations](audit-01/L1-foundations.md) | Exact supports, local identities, Paige/omega algebra and band-Krylov obstruction checked; row-selection statement needs admissibility and normalization qualifications |
| L1 later proofs and measurements | [L1-later](audit-01/L1-later.md) | Exact triangle/square certificate and coefficient/checkerboard calculations rerun; Ritz claim scope and mixed statuses require correction |
| L2 | [L2](audit-01/L2.md) | Exact theorem/recursions and independent span drift checked; corollary constants, reorthogonalization scope and semiorthogonality wording need repair |
| L3 moment framework | [L3-framework](audit-01/L3-framework.md) | Analytic framework reconstructed; exact normalization counterexample, false rate-summary paraphrase and status split |
| L3 obstruction certificates | [L3-certificates](audit-01/L3-certificates.md) | n=3 rational certificate and all-n symbolic/interior/edge/corner proof checked; no-uniform-radius inference unsupported |
| L5 | [L5](audit-01/L5.md) | Rotation/prefix proofs and scoped failures checked; Householder-ratio inference and numerical-certification terminology overstated |
| Protocol/provenance | [protocol](audit-01/protocol.md) | All theory/input/log identities match; count/source consolidation and E-versus-G scope obligations remain |

## Consolidated disposition checklist

Every finding in the linked reports, including low-severity corrections, needs a developer disposition in `response-01.md`. The following groups identify the material issues without replacing the detailed locations and evidence:

1. **Normalization and residual claim (L3-framework).** Repair T302(b) consistently: either retain unnormalized functionals throughout the residual theorem, formulate mass-preserving perturbations with the correct affine-slice norm/duality, or include normalization factors. Do not retain the exact `c=1` threshold while mixing those conventions. Check propagated report/application wording.
2. **Precise theorem hypotheses and consequences (L1-foundations, L2).** T108's degree-only parent condition is insufficient; require triangular support and a nonzero intended pivot, and include `pi0=1` in the left-inverse system. Preserve the actual pivot/amplification factors in T201's corollary unless a non-breakdown quantitative hypothesis bounds them. T202's exact residual identity does not prove that every reorthogonalization scheme fails.
3. **Measured scope and inference (L1-later, L2, L5).** Narrow N101's blanket Ritz claims to the probes and magnitudes actually measured; distinguish the defined `sqrt(u)` threshold from a relaxed kill threshold. Householder ratios leave paired slope differences unchanged and do not prove conditioning removal. Preserve the failed frozen criterion and distinguish descriptive estimates from significance/causality. Floating-point prefix estimates and SVD outputs are not exact/interval certificates; intermediate-state data need not grow monotonically.
4. **Padua radius and original question (L3-certificates, protocol).** Finite per-degree lower bounds and sampled negative values do not prove that every possible obstruction radius must tend to zero, or that no uniform radius exists. A valid chosen radius may of course be made decreasing. Restrict the backward obstruction to reading **(E)**: exact representation or a sufficiently smaller residual for specified perturbations given as data. Actual finite-precision Greenbaum reading **(G)** remains OPEN.
5. **Claim splitting and report accuracy (all relevant reports).** Keep substantive PROVED claims in their own files/IDs, moving distinct CONDITIONAL/MEASURED/OPEN claims into separate durable homes and preserving crosswalk/history. Examples include T105, T114, T202's substantive drift bound and T304's measured isomorphism; see the exact classifications in the direction reports. T113's Q40 conditional execution obligation was discharged by a fresh exact audit rerun: record that new evidence explicitly when updating its status. The rate summary must use the jet-space conditions `S0`, `S1`, `(H)` rather than substituting absence/existence of a nonnegative annihilator. Correct stale status pointers, the nonexistent L5 N503 reference, and the theory count of 64 to 67.
6. **PR-preparation obligations (protocol).** Consolidate the additional L2/L3 literature statements into canonical source records/index/corpus with honest reading limits. Merge charter/MZ-bearing main at the previously authorized preparation boundary; reconcile accepted registries and the single batch owner before final allocation. Rehearse the relevant integration and re-audit material changes. No final IDs or new reservations are allocated here.

## Executed evidence and limits

The linked reports distinguish newly implemented independent checks, reruns of earlier checkers, and reanalysis of existing data. All floating-point observations remain **MEASURED**; finite numerical agreement does not prove an arbitrary-degree statement. Symbolic/exact certificate checks supplement the written reductions and analytic proofs.

Representative actual observations include exact triangle/square propagator inequalities under two arithmetic constructions; independent rational reconstruction of the Padua n=2 Hessian dual and n=3 obstruction certificate; all-n symbolic boundary/interior identities; exact equispaced checks through n=7; new full-CGS2 span drift about `4.105e-3` (rotated square, n=24) and `1.016e-2` (triangle, n=20), falling to about `8e-6` in long double; and an independently reproduced n=50 GEPP Givens failure ratio about 7602 despite a numerically well-conditioned-prefix margin. Scope, seeds, arithmetic and references are in each report.

The [inventory checker](audit-01/check_inventory.py) and [result](audit-01/inventory.json) independently verify all 67 theory hashes, all 12 input-copy identities, and all 16 reproduction-log hashes. The frozen candidate's 216 recorded output files total 1,361,364 bytes and satisfy the size caps. The final audit artifact manifest records audit evidence identities separately. The Windows input archive/fulltexts were not retrieved in this session; historical delivery/re-verification is documented, and no fresh archival verification is claimed. Large syvert runs, unexecuted experiments and named literature gaps remain pending. No claim of a globally optimal nonlinear positive-measure fit follows from the linearized fit experiments.

## Handoff

No finding is silently fixed in the developer files. Claude should respond to every finding, preserve the frozen audit records, and return material corrections to AUDIT with exact hashes and a focused impact map. A later ready PR requires its own recorded preparation checks; this review does not authorize a GitHub merge.

Suggested next prompt: `Claude (Opus 5.5 xhigh): Continue claude/bivariate-lanczos-20261031; address audit-01.md and every linked finding in response-01.md, preserve the audited science/history, split substantive mixed-status claims, and return material changes to AUDIT for Codex re-review.`
