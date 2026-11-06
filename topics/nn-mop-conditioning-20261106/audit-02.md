# Audit 02 — focused Claude re-audit of response 01

- **Auditor:** Claude, Opus 5.5 xhigh, acting as orchestrator and independent auditor (handoff [04](handoffs/04-reaudit.md)).
- **Workers:** four Claude audit workers, none of which changed Git or repository files:
  - G: new gauge theorem, Opus 5.5 xhigh (new mechanism);
  - R: classification, negative records, attribution and audit-01 MINOR diff, Opus 5.5 high;
  - K: code and evidence, Sonnet 5.5 high (ordinary technical audit);
  - N: full IDEAS read for the new mechanism, Opus 5.5 high.

  I also reconstructed the central steps of the new theorem myself.
- **Audited response input:** `b3350adf2e7f9270f0bca8558b1ac668c7826291`. Head `7c0c067` adds only handoffs 03 and 04. The diff was reviewed from `3d5b29d` (the audit-01 handoff head). Main is still `76ba4214b100c86a44941f5e9a662ce9ce48efb8`.
- **Rules:** read at `7c0c067`. AGENTS.md, agents/, templates/, state/ and literature/ are unchanged since `64a45b3`.
- **Scope:** the material response to audit-01 MAJOR-1/2/3, the new NOTE-1 theorem, the code and evidence changes, and diff confirmation of audit-01 MINOR-1…11. Accepted audit-01 science was not reopened.
- **Verdict:** no BLOCKING or MAJOR findings, and every material change is accepted. The MINOR findings below are not fixed in place, because this is the second round. They go to PR preparation, and the readiness check confirms them by diff. **Stage: PR** ([handoff 05](handoffs/05-pr-prep.md)).

## Coverage

- **Rules and the response:**
  - AGENTS.md, WORKFLOW.md and CLAUDE_ROLES.md;
  - audit-01.md, handoffs 03 and 04, response-01.md;
  - `git diff 3d5b29d b3350ad` for every topic file and the results file.
- **Classification and literature records:** classification-proposal.md, response-literature.md and response-code-checks.md.
- **Candidate records:** candidate-result-map.md and candidates-response-C2.md.
- **New gauge records:** response-gauge-candidate.md, novelty-gate-response-gauge.md and theory/response-gauge-infimum.md (all in full).
- **New negative records:** theory/response-c2-positivity-failure.md and response-c2-node-transfer-failure.md.
- **Edited theory files:** all of them.
- **Predecessor files:** PD-T448 (conditioning-growth-target.md), PD-T432 and PD-T437.
- **state/IDEAS.md:** read completely by worker N, lines 1–1112 in ten sequential chunks, with greps for gauge, diagonal, similarity, balanc, normaliz, orthonormal, monic, taper, b-field, condition and kappa.
- **literature/INDEX.md:** rows LIT-112, 113, 348, 365, 502, 503, 507 and 508, plus greps for scaling, balanc, diagonal, gauge, equilibrat, normaliz, sensitiv and conditioning.
- **Blocked:**
  - **Octave and the source archive** are still absent, so external values and the M2/M4 gates rest on the receipts.
  - **`code/response_code_checks.py`** has hard-coded developer `/tmp` inputs that are absent here: `/tmp/c4-comparison-bits-raw.json`, the C3 raw, the external bit grid and `c1-matrix-all.json`. It failed with FileNotFoundError before writing anything. Its full healthy-payload, table-byte and C1-diagnostic parts are therefore receipt review only.
  - **Codex's primary-source web reads** were not reproduced.

## Reconstruction and executed checks

All of the following was executed in this session. The scripts are in [audit-02/claude](audit-02/claude/README.md).

### New theorem: response-gauge-infimum.md — accepted as PROVED

- **Reconstruction.** I and worker G each reconstructed the theorem.
  - **Finite-t identity (2).** Under the gauge s_ν = t^(|ν|−1), the degree-one backward ratio is 1, so A_(e_i,i) = a_(e_i,i) = Var_i. Every backward ratio at higher degree is t. So the A_i field sup is max(v_i, tL_i) and its largest derivative support is max(d_i, tH_i), by homogeneity of the support norm.
  - **Other fields.** The u entries are constants, including the terminal 1/t scales, so they have zero derivative; B = b exactly. Since sup and max commute, (2) holds.
  - **Attainment under (3).** t from (6) is strictly positive and satisfies (5), so κ(t) = K at a **finite** positive t. The t → 0 limit is not used. The lower bound K ≤ K_dep ≤ K_fix follows from B_j ≡ b_j under every C1 section.
  - **Variance bound (8)–(9).** It holds: node part ≤ 2√v and weight part ≤ 2v. Smaller boxes, fixed mass and log weights only reduce the support.
  - **Krawtchouk.** v ≥ 24/(25M) gives r_i ≤ (9/2)M. PD-T437(1) gives K ≥ 5^M/M ≥ 5M, and that witness is weight-only, mass-zero and in all six models. Spacing 2/M > 1 only at M=1, which goes to the exact check.
  - **Hahn.** The beta-binomial variance formula specializes to (M+4)/(5M) and (160/891)(1+9/(2M)), so r_i < 7.
    - A_M ≥ 2^M(M−1), the fixed-mass loss is ≤ 2, the ratio identity holds with difference 2M³+M²+2M+5, and f₁₄/2 ≈ 9.09 > 7. So the onset M=14 is correct, and the exact obligations are exactly Hahn M=1..13 and Krawtchouk M=1 spacing.
  - **Finite reduction (12)–(14).** The adjoint formula, τ_succ = −Σx_l and the weighted-median support were re-derived.
- **Developer checker and supplementary checker.**
  - `code/response_gauge_infimum.py` exits 0 with 96 checks. With the Python version string normalized, its output is byte-identical to the committed receipt (eddfe64a…).
  - `code/response_independent.py` matches its pinned output (f00457e0…) and all 16 payload digests. The global minimum ratio is 42/13 (Krawtchouk N2).
- **Auditor's own checks** (no topic imports):
  - `G/gauge_exact.py` uses exact Fractions over the full NN triangle and all six gauged fields. In 138 model-cases (Krawtchouk N2–12, Hahn N2–14) it finds κ_s(t*) = K exactly, and formula (2) holds exactly at six t values.
  - Black-box finite differences at 70 dps agree to ≤ 7e-13.
  - Dominance at 100 dps for Hahn N15–24 and Krawtchouk N16/20 holds with margin ≥ 2e12.
  - On random generic inputs dominance fails in 4 of 12 cases, and there t* does not attain K. So hypothesis (3) has real content, and the stated exclusions are needed.
- **Novelty.** This is a variant of c1-gauge-invariants.md:168–173 and audit-01 NOTE-1, and the verdict "variant with difference, historical novelty unclaimed" is accurate. No IDEAS entry or obstruction pre-empts or contradicts it. The only other "gauge" entries are IDEA-255 and IDEA-262, which are unrelated.

### MAJOR-1 resolution (PARTIAL proposal for PD-T448) — accepted

- classification-proposal.md quotes PD-T448's statement verbatim.
- It decomposes the statement into the target's own cases (the Krawtchouk and Hahn families) and conjuncts (the limit/rate, the subexponential factors and constants, the radius/digit loss).
- The single PROVED part is exactly lim κ_N^(1/N) = 5+2√6 for the exact Krawtchouk pair in the PD-T432 metric. That follows from c2-sharp-upper.md together with PD-T437.
- Every other part is OPEN, with no MEASURED or CONDITIONAL part among them. Supporting lemmas (the Hahn ρ_H lower bound, normality, the base-2 lower bound, the parameter lower bound, measurements, gauge and matrix metrics) are correctly excluded from the aggregation.
- PARTIAL is legitimately applicable under WORKFLOW. The historical OPEN rationale is preserved, and the shared registries are untouched until preparation.
- "Split from: PD-T448" now remains only on c2-sharp-upper.md, and the supporting files say "none", with History entries.

### MAJOR-2 resolution (attribution) — accepted

- report.md:5, note-material.md:6, the C1 gate addendum and response-literature.md all separate LIT-502/348 (an algorithm's residual under norm-balancing basis scaling) from forward conditioning in the fieldwise metric.
- The Fischer attribution (LIT-113/112/365, IDEA-087/088) is bounded: these are secondary or UNVERIFIED rows, no O(N²) claim is imported, and the INDEX rows are not upgraded.
- The AT-system normality lead is qualified as unverified (note-material.md:11).

### MAJOR-3 resolution (C2 subroute records) — accepted

- The r4/r5/r6 subform records carry every IDEA template field, with retrospective kill criteria labelled honestly.
- The two new PD-N homes carry every THEORY field. Each negative statement is PROVED, and each disposition is REJECTED: failed at subroute scope only. Neither refutes the full Hahn upper.
- The extraction is faithful to the accepted text. `R/negs.py` confirms, exactly:
  - U(0) = 24 and U(1) = 18, so ΔU(0) = −6 at M=3, t=1;
  - formula (5) at every entry for M=2..18;
  - |D_(0,⌊M/2⌋)| = C(M,j)/j ≥ 2^M/[M(M+1)].
- `code/c2_hahn_upper_search.py --max-m 6` reproduces its payload. c2-hahn-upper-search.md is now labelled as an attempt record.

### Code and evidence (MINOR-2/4/5/10 of audit-01) — accepted

- **`native_result` (c4_compare.py:50–70)** matches the actual C3 producer shape.
- **Real breakdown on this platform.** On the audit-01 rerun native raw, which contains a real Krawtchouk N32 A-LU breakdown, `c4_compare.py` with a 58-input synthetic external file now exits 0. The breakdown row reads `32,shared_normalized,breakdown,,,,,,,`. Before the change this crashed with KeyError.
- **Healthy tables are unchanged.** Old (3d5b29d) and new code give identical raw `cases` and 14 byte-identical CSVs.
- **Malformed native inputs.** 19 variants (`K/mal.py`) give explicit statuses with blank metrics. Three non-producer shapes still crash (MINOR-6).
- **C2-hard check.** `code/c2_hard_check.py` is byte-identical to the block embedded at cc1edd2 (452d72d7…) and passes with counts 50/735/1050/330.
- **C1 diagnostic receipt.** c1-error-comparison.json changes only its receipt pin, which now equals sha256(c4-comparison-receipt.json) = 92ace13e…. The c1-matrix-all.json raw pin (29090 bytes, b4e53167…) has been added.
- **Verification and sizes.** `verify_evidence.py` passes with 86 identities. No committed generated evidence exceeds 16 KiB, and no third-party content is committed.
- **M2 documentation** now matches c4_external.m and c4_fidelity.py: pre-grid single-configuration gate, then full grid, then fidelity on the full bit grid.

### Audit-01 MINOR-1…11 — confirmed by diff

All are fixed except the two residual items in MINOR-1 and MINOR-2 below. No fix introduces a stronger rate or claim beyond the new theorem audited above. The explicit terminal-rate bounds added under NOTE-4 were checked by hand and hold: 10/13 < w < 17/22, 2w²−1 > 31/169, 1−2w³ > 822/10648, and the reciprocal branch has r > 3/2 > R.

## Findings

### BLOCKING

None.

### MAJOR

None.

### MINOR

These are for PR preparation; readiness confirms them by diff.

1. **Stale pending text not fixed (audit-01 MINOR-7 residual).** attempts/C2-hard.md:24–25 still says "independent checks and Claude audit pending". Pending-process wording also remains at response-gauge-infimum.md:113–114 and :333–334, and response-gauge-candidate.md:40–41 says the rerun is still the coordinator's responsibility. Move process state to LOG or the handoff.
2. **Wording after PARTIAL.** c2-sharp-upper.md:7 ("The other families and metrics in PD-T448 remain OPEN") and report.md:23 ("other unresolved cases and metrics") are imprecise: PD-T448 has one metric, and the Krawtchouk prefactor, constants and radius conjuncts also remain OPEN. Point to classification-proposal.md instead.
3. **Predecessor "optimizer OPEN" statements carry no dated addendum.** These still read as current status:
   - c1-gauge-invariants.md:98–100 and :170–173;
   - c1-hahn-gauge-lower.md:105–106;
   - novelty-gate-C1.md:81–82.

   Add one dated line to each, scoped to the b-dominant benchmark cases, which are now PROVED for all N in all six models. The generic non-dominant case stays OPEN.
4. **Gate literature search missed LIT-507/508.** literature/INDEX.md rows 579–580 (Laudadio–Mastronardi–Van Assche–Van Dooren) treat diagonal balancing and symmetrizing similarity of the MOP recurrence matrix for forward eigenvalue conditioning.
   - Neither pre-empts the result. They concern the forward problem H → (nodes, weights), not fieldwise inverse conditioning or b-invariant attainment.
   - But they are the closest indexed sources on choosing a diagonal gauge for MOP recurrences, and note-material.md:14 states the gauge result for external use. novelty-gate-response-gauge.md:87–91 searched exact phrases only.
   - Add a shortlist row and one distinguishing sentence. LIT-508's exact power-of-2 scaling also bears on the representability caveat at response-gauge-infimum.md:348–349.
5. **Hahn input wording.** response-gauge-infimum.md:102–103 calls the normalized Hahn weights "exactly the PD-T290 inputs", but PD-T290 uses unnormalized weights. There is no mathematical effect, since κ, K and r are invariant under per-measure scaling. Say "after per-measure mass normalization (C2-02)".
6. **c4_compare.py hardening.**
   - The `except` at :67 omits AttributeError, so a list-valued coefficient crashes. A string measurement entry (:53) and an int method source (:58) crash too.
   - A NaN coefficient is silently reported `ok`, because `max()` depends on the NaN's position.

   None of these shapes can come from c3_grid.py (allow_nan=False, fixed schema).

   MINOR-6 and MINOR-7 are **optional**. Either record the limitation in external-code.md, or change the code. A change to result-bearing code is a material change: the healthy payload and table bytes must be shown unchanged, and readiness then includes a focused check of that change.
7. **response_code_checks.py reproducibility.**
   - It has no CLI, and its inputs and work directory are hard-coded under `/tmp`.
   - A successful run overwrites the tracked files c1-error-comparison.json and response-code-checks.json, with platform strings.
   - `source_commit` is hard-coded to 3d5b29d.

   Write regenerated outputs to an output argument and document the regeneration of the raw dependencies.
8. **M2 receipt numeric difference unexplained.** In external-code.md, the pre-grid receipt (reference 8.66e-17, CORE 7.4834e-15) and the bit-transport receipt (7.18e-17, CORE 7.4724e-15) differ, and the text does not say why. Decimal versus bit transport is the likely reason; state it, or record it as unexplained. external-code.md also calls c4-m2-receipt.json "exploratory overbroad" in one paragraph and "authoritative pre-grid gate" in another; reconcile the two.
9. **Provisional ID format.** `IDEA?nn-mop-cond-response-gauge` and `PD-T?nn-mop-cond-response-gauge` omit the agent component, contrary to WORKFLOW (`<namespace>?<topic-slug>-<agent>-<n>`; the topic prefix is `nn-mop-cond-codex`). Rename them, or record the alias in candidate-result-map.md before final allocation.

### NOTE

1. **Registry application of PARTIAL needs these edits:**
   - PROOF_STATUS.md:531 and :541 (text "not a PARTIAL decomposition");
   - ID_CROSSWALK.md:1605 and :1617;
   - the predecessor conditioning-growth-target.md:
     - Split-into line (:5–7);
     - finite-scope Hahn-normality assumption (:22–26), which should now cite c2-hahn-normality;
     - OPEN rationale (:28–33), to be kept as History.

   Also state whether the D1 mechanism questions in PD-T448 History (:64–69) are outside the registered statement or are listed as OPEN parts. Either way they are OPEN, so PARTIAL is unaffected.
2. **Wording and scope sentences:**
   - note-material.md:8 says "Scalar differentiation follows Fischer1998"; "has the Fischer 1998 predecessor" is safer.
   - Optionally add that LIT-348/502 concern the step-line path.
   - The new theorem covers the NN six-field map only, and does not close PD-T432's open item on alternate step-line diagonal scaling (conditioning-local.md:155–158). One sentence would prevent misreading.
3. **Kill criterion.** response-gauge-candidate.md:28–30 is a rule about what may be claimed, not a falsifier. Suggest "no finite t attains K under (3)" or "some benchmark N violates (3)", with a retrospective qualifier like the C2 records use. The candidate's "strengthening the limiting observation" undersells NOTE-1, which already proposed the equality. The new content is the explicit t and the all-N benchmarks.
4. **Minor code and record observations:**
   - The subleading guard at response_gauge_infimum.py:131–132 is vacuous for Krawtchouk, but the theory claims it only for Hahn.
   - The benchmark t* lies in about [0.04, 1] for N ≤ 14.
   - The status-table text "Written M>=2 argument" actually covers M ≥ 1 in the non-spacing models.
   - c4-exploratory-receipt.json gained a `gate_labels_scope` key; the manifest was updated, and a companion note would have kept the historical bytes.
   - results/nn-mop-conditioning-20261106.md:15's next-step line must be dropped when the section enters RESULTS.md.
5. **Possible further citations.** IDEA-058 (finite reduction plus checker discipline) and IDEA-554 (deferred scaled evaluation conditioning) are uncited neighbours, not contradicted. Classical optimal-scaling and balancing literature (van der Sluis, Osborne, Parlett–Reinsch) is not indexed. Any such statement about invariant diagonal entries would be routine, and no novelty is claimed.

## Remaining uncertainty

- The M ≥ 14 Hahn tail relies on C2-04's all-M lower bound, which audit-01 accepted; high-precision checks to N24 are consistent with it.
- Exact checks cover Hahn to N14 and Krawtchouk to N12; mpmath checks are measurements, not enclosures.
- The log-weight equivalence was checked by argument only.
- Receipt-only review covers response_code_checks' healthy-payload part, external values, M2/M4, and the Codex web reads.
- The NOTE-1 theorem's external usefulness, such as the size of t and representability, is outside the claim.

## Required next step

Stage PR. Codex performs PR preparation under [handoff 05](handoffs/05-pr-prep.md):
- fix MINOR-1…9 above;
- run the fresh reservation check and allocation;
- apply the PARTIAL decomposition and every result/disposition mapping to the shared registries by reviewed diff;
- write the RESULTS.md section;
- request the readiness check.

The readiness check, by Claude, reviews the registry diff and refreshes the reservation; it is not a new audit round unless the application makes a material change. Only AC merges.
