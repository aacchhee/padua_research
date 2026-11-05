# Claude audit-01 — independent scientific and protocol audit of the frontier batch

2026-11-05. **Stage verdict: FINDINGS REQUIRE WORK. Return to WORK for a Codex response.**

- **Mathematics:** every PROVED theorem in the batch was independently reconstructed and **accepted**. No BLOCKING finding exists, and no proof needs correcting.
- **What requires work:** two MAJOR findings on status and scope labels, one MINOR protocol finding (the novelty-gate timing deviation), and a set of MINOR record-hygiene fixes before PR preparation.
- This audit approves nothing for merge. Only AC merges.

## Identity, inputs and rules

- **Auditor.** Claude, cross-family independent auditor for handoff06. The orchestrator ran Claude Opus 5.5 (`claude-opus-5-5`) at xhigh effort, as AC requested ("Claude (Opus5.5 xhigh): Continue …") and handoff06 assigns. Eight family subagents ran the same model and effort; they had no Git authority and returned reports to this orchestrator. The developer is Codex (gpt-6.1-sol, with gpt-6-astra supplementary checks). No developer conclusion was inherited.
- **Audited candidate.** `95251656352bc49b19191c46419f6256c23374da`, handoff06's input head. Files were read at publication head `3a179f68ecbed20dc7e15862da842ed6116aa375`; the only difference from the candidate is the handoff05 status line plus handoff06. Per-file SHA-256 values are in the family reports and in [code/PROT/sha256.txt](audit-01/code/PROT/sha256.txt).
- **Rules.** AGENTS.md, agents/WORKFLOW.md and agents/claude/CLAUDE_ROLES.md, read at `3a179f6`. They are byte-identical to current main `330fab8`.
- **Base.**
  - The branch base is main `aff30e8`.
  - Current main is `330fab8`, which adds PR26 (MZ indefiniteness/parity/manuscript) and does not touch Lanczos sources.
  - This audit did not merge main.
- **Commits during the audit.** Checkpoints `6f10e90` and `763bb9e` added only `audit-01/**`.
- **Read coverage.**
  - Full `state/IDEAS.md` (974 lines) and every obstruction/disposition table: PROT report §1.
  - The literature/INDEX rows used for priority wording, and the pinned PR21 P3 memo (blob `4741c389`, unchanged at PR21 head `67b3e01`).
  - All 20 theory records, the methods, attempts and ideas files, independent checks, gates, LOG, handoffs 01–06, report, results, proposals, allocations and storage indices.
  - Each family report lists exactly what was and was not read.

## Family reports (preserved as written)

| Family | Records | Verdict | Report |
|---|---|---|---|
| L1 | SH_n aggregate separation | ACCEPT WITH MINOR FINDINGS | [L1.md](audit-01/L1.md) |
| L2 | smooth-rule closure reduction; G2 certificates; positive-weight embedding; SH_n W/R growth | ACCEPT WITH MINOR FINDINGS | [L2.md](audit-01/L2.md) |
| L3 | explicit finite-error selection theorem | Proof accepted; FINDINGS REQUIRE WORK (status label) | [L3.md](audit-01/L3.md) |
| L4 | rotQ24 full formal scalar-CGS2 factor ten; fixed-lower envelope obstruction | ACCEPT WITH MINOR FINDINGS | [L4.md](audit-01/L4.md) |
| L5 | finite radius-certificate reduction; n3 bracket; n4/n5 lower bounds | ACCEPT WITH MINOR FINDINGS | [L5.md](audit-01/L5.md) |
| L6 | complete-square residual bound; scoped obstruction; frozen n1 run; raw-data nonrealizability | ACCEPT WITH MINOR FINDINGS | [L6.md](audit-01/L6.md) |
| L7, G1 | natural suite; finite growth fits | L7 FINDINGS REQUIRE WORK; G1 ACCEPT WITH MINOR FINDINGS | [L7G1.md](audit-01/L7G1.md) |
| PROT | novelty gate, timing deviation, G0/G4, statuses/IDs, reservations, resources, storage, LOG/handoffs | FINDINGS REQUIRE WORK (records/protocol) | [PROT.md](audit-01/PROT.md) |

Auditor-written checkers, scripts and small receipts are in [audit-01/code/](audit-01/code/). Every file there is under 16 KiB, and the folder totals about 0.7 MB. Bulk arrays and pickles stayed in local scratch and are not claimed retained.

## Claim-by-claim disposition

| Claim (provisional) | Claimed status | Audit disposition |
|---|---|---|
| L1a SH_n BJ lower √(2(4^(n+1)−1)/3) and mirror upper 2√6(n+1)²(N_n−1), all n≥2 | PROVED analytic | **Accepted.** The ratio bound exceeds 1 only for n≥18 (L1-1). |
| L2-01 smooth exact-base rule invariance and actual X-closure derivative | PROVED analytic | **Accepted** |
| L2-02 G2 degree-12 W/R lower certificates, both grids | PROVED finite computer-assisted | **Accepted.** Byte-identical reruns; own exact recomputation. |
| L2-03 positive-weight embedding | PROVED analytic | **Accepted** |
| L2-04 C_n ≥ √((4^n−1)/6)/cos(π/(n+3)) ≥ 2^(n−4) | PROVED analytic | **Accepted** |
| L2-05 E_n ≥ (4^n−1)/(6n(n+2)cos²) ≥ 2^(n−8) | PROVED analytic | **Accepted** |
| L3-01 explicit radius, quadratic remainder, tolerance acceptance, adaptive completion | PROVED analytic | **Accepted.** The broader-target label must be OPEN (A-M1). |
| L4a rotQ24 K_BJ² ≥ 2041704913997 > 100·13462956266 ≥ 100K_alt² | PROVED finite computer-assisted | **Accepted.** Fresh producer and fixed-certificate rerun, plus a FLINT-free CPython reconstruction. |
| PD-N L4-01 fixed-old-lower envelope obstruction | PROVED, scoped negative | **Accepted** |
| PD-T140 target part → PROVED via PD-T141(c) and L4a | proposed (unapplied) | **Accepted** as the correct target status. The experiment stays MEASURED/INCONCLUSIVE. |
| L5a finite certificate reduction | PROVED analytic | **Accepted** |
| L5b 1/512 ≤ δ_obs(3) ≤ 1/2 | PROVED finite computer-assisted | **Accepted.** Two SymPy backends plus an own kernel-free checker. |
| L5c δ_obs(4) ≥ 1/2048; L5d δ_obs(5) ≥ 1/16384 | PROVED finite computer-assisted | **Accepted.** Wording fix in L5-1; context in L5-5. |
| L6-01 commutator ≥ e/6; residual sum ≥ eσ_min(Q)/12 | PROVED analytic | **Accepted.** The exact minimum ratio is ≈4.57e. |
| PD-N L6-01 scoped e/u obstruction | PROVED, scoped negative | **Accepted** |
| L6-03 frozen n1 binary64 run | MEASURED | **Accepted.** Reproduced three ways. |
| PD-N L6-02 raw 14-slot nonrealizability (2^-55) | PROVED, scoped negative | **Accepted** |
| L7 natural fixed-target suite | MEASURED | **Accepted only after the scope fix in A-M2.** The headline counts depend on an unrecorded BLAS kernel. |
| G1 finite growth fits, both grids INCONCLUSIVE | MEASURED | **Accepted.** T24 counterchoice rigorously recomputed; rotQ24 checked from receipts and code only (L7G1-8). |
| Unchanged OPEN targets: PD-T055, F, PD-T056(G), U2/G3 n4–8 (handoff01 asked n3–10), degree-uniform selection, scalar/IEEE activation | OPEN | **Confirmed not upgraded** |

## Findings requiring disposition

Each finding is detailed, with exact file:line locations, in the family report it cites.

### MAJOR (fix before PR readiness)

**A-M1 — broader L3 target labelled PARTIAL** (L3-1 = PROT-3).
- *Location:* attempts/L3.md:3 and ideas-l3-continuation.md:123–124.
- *Problem:*
  - WORKFLOW reserves PARTIAL for an explicit decomposition of the target's own statement, with conjuncts proved under split IDs.
  - Handoff01's L3 shapes are alternatives, and L3-01 proves a reformulated shape under a stronger per-column budget than PD-T143's Hres.
  - A version uniform under Hres alone is impossible.
- *Remedy:* label the broader target OPEN, with L3-01 a PROVED supporting result. Or, if Codex prefers, write an explicit split and its History and refer the classification to AC. Make all files agree.
- *Note:* handoff01's own L3 "Done" line used "PARTIAL with the exact remaining obligation" loosely, so the developer followed the handoff wording. WORKFLOW's definition still governs registered and reported statuses.

**A-M2 — L7 headline counts depend on an unrecorded OpenBLAS kernel** (L7G1-1).
- *Evidence:*
  - The auditor reran with the same code, pinned NumPy 2.3.5, SciPy 1.17.0 and polyrat, and byte-identical inputs.
  - On the default AVX-512 kernel the triangle-24 suite gives 18 loss cells, with different cells, and 9 same-group paired directions.
  - Only `OPENBLAS_CORETYPE=Haswell` reproduces the committed 20 cells and 6 directions exactly.
- *Remedy:*
  - Add a dated scope addendum recording the platform/kernel and pinning it in the recipe.
  - Disclose the cross-kernel result.
  - State which features are robust: the accepted/rejected references, triangle-24-only losses, no entire-function loss, pairs only at triangle24/tanh/boundary, and exact own/L2 agreement.
  - Keep MEASURED.

### MINOR — protocol

**A-P1 — prospective novelty-gate timing deviation** (PROT-2; family slices L1-8, L2 §protocol, L3-9, L4-9, L5 §5, L6-9).

*Facts confirmed:*
- Three workers drafted candidate families and formulas before completing the mandatory shortlisted reading. All the drafts first entered Git together in `0574c47`.
- Essentially every claimed result descends from such a draft, and L3-01's constants survived unchanged.
- In each direction, further development followed a completed and recorded gate.
- The full IDEAS.md read finds no duplicate pursued as new and no changed novelty verdict. No novelty or priority claim is made.

*Disposition:*
- This is a real WORKFLOW deviation. It is **not waived and not cured** by later reading.
- It has **no effect on mathematical validity**, because every proof was reconstructed independently by this audit.
- Once remediated it does not block readiness by itself. **Accepting the deviation is AC's decision**; this auditor recommends acceptance with permanent disclosure.

*Required remediation before readiness:*
- **R1.** One dated table: each pre-gate candidate, its first commit, the reads missing at drafting, the gate-completion SHA, the post-gate verdict and the resulting claim.
- **R2.** A timing qualifier in each affected IDEA registration and in each descended PD-T/PD-N History.
- **R3.** Fix the closest-entry omissions: IDEA-130/134 for SH_n; IDEA-148/PD-N013 and IDEA-151/PD-N015 for W/R.
- **R4 (process).** Commit gate checkpoints before drafting any candidate.

### MINOR — records, wording and evidence (fix before or at PR preparation)

- **A-m1 — small-n qualifier for L1** (L1-1). Add: "both bounds hold for all n≥2; the ratio bound exceeds 1 only for n≥18; no small-n ordering is claimed". Also add "affine image of a product grid" in the one-line summaries (L1-4).
- **A-m2 — provisional-ID hygiene** (L1-2, L3-6, L4-4, PROT-5).
  - Inconsistencies: L1a/L1-01 and L3a/L3-01; G1-fit, L7 and IDEA?frontier-l7 lack the agent component; letter local numbers.
  - L4: crisp dispositions are needed. IDEA L4a is `REJECTED: failed` for its 100U<G_R criterion only; L4b is retained/successful. Align Split from/into.
  - Remedy: one canonical ID per record, with aliases.
- **A-m3 — stale records** (L2-1, L2-3, L4-5, L5-2, L5-3, L6-1, L7G1-3, PROT-6, PROT-8).
  - Use additive dated updates.
  - Where a checker pins a file's hash (l2-smooth-rule-closure-reduction.md, l6-02 contract), keep the pinned bytes frozen or re-pin as a recorded packaging change and rerun once.
  - Refresh the LOG header and Runs needed, with exact commands where possible.
- **A-m4 — wording precision.**
  - L3: the strengthened-model reformulation, the per-column vs Hres comparison and the proved universal radius ceiling r_R ≤ 5^{−(N−3)/2}/(4√2λ_1) (L3-2, L3-3, L3-4, L3-5 template sections).
  - L4: "distinct re-execution of the pinned producer" (L4-1); the results line names the conjunct (L4-3); runtime rounding (L4-6).
  - L5: the checker source-vs-input hash label, and "largest passing saved dyadic radius" (L5-1); cite the stronger PD-T075 reviewer bounds b₄, b₅ (L5-5).
  - L6: corrected-branch wording consistent with the pre-frozen l6-02 rules (L6-4); disposition objects (L6-3).
  - L7: grouping of paired comparisons labelled post-registration, with cross-group counts (L7G1-2).
  - G1: "undecided" SSE wording (L7G1-7).
  - L2: model qualifier in results (L2-4); committed L1 hash `f27a22c4…` instead of the uncommitted `9f59217…` (L2-2).
- **A-m5 — proposals incomplete** (L4-2, L5-4, PROT-7).
  - Write literal old→new blocks for every affected registry row: PD-T055/056/075/140/141/143/146, the IDEA-248/250/251/255/262/263–267 updates, about 22 new IDEA rows, CURRENT.md:103, the ID_CROSSWALK original-to-split mapping, and this topic's RESULTS section.
  - Register L6-02 as IDEA-262's contract and L4b as a variant of IDEA-250, never as new mechanisms.
- **A-m6 — per-statement priority wording for the paper paragraph** (PROT-9): P3 row 14/group C for the PD-T136–141 extensions; row 15 (Barrio–Peña–Sauer Remark 9) for L3-01; "PR21 (unmerged)", blob `4741c389`.
- **A-m7 — retrievability and receipts** (L6-2, L7G1-4, L7G1-8, PROT-10).
  - Document a non-overwriting, repository-only rerun recipe for the n1 checker.
  - Commit the full 20-row L7 loss list and pin the aggregator hash.
  - Commit compact per-degree outward-rounded G1 endpoint tables, so rotQ24's verdict can be rechecked without about 1.5 h of regeneration, or deliver the rows to cold storage.
  - State the local-only retrievability limit, and record BLAS dispatch and CPU ISA in numerical receipts.
- **A-m8 — manifest after audit** (PROT-13). `code/check_manifest.py` now fails at HEAD because audit-01/ was added. Exclude audit outputs or regenerate the manifest with provenance. Do not edit the audit files.

### NOTEs (no action required unless stated)

**G0/G4 accepted and strengthened** (PROT-1). Both dispositions discharge the unchanged "explained" criterion with no tolerance waiver and no bit-identity demand.
- An AVX-512 host running the frozen `8359bf7` code under the default (SkylakeX) OpenBLAS kernel reproduces **all 12 historical own-method G0/G4 gaps bit-for-bit**, with matching input hashes. The historical alt row is reconstructed from 0.85u local residuals with amplification 4.03e3.
- The orchestrator reran this separately; its receipts are byte-identical to the subagent's.
- Haswell agrees with the developer's recorded current own-method gaps only to about 8e-8 / 7e-5 relative, not bit-for-bit (see PROT §3(a′)). upstream_xy was not rerun.
- Remedy: a dated additive note to both dispositions; record BLAS dispatch in future receipts.

**Robustness and strengthening opportunities** (optional, each needing impact review):
- L4's lower bound beats 100× the inherited PD-T141(a) upper (L/U_R = 150.87).
- L1's proof applies to every degree s ≤ m−2 on a fixed grid.
- L5's n4/n5 dyadic lower bounds are weaker than known reviewer bounds; a cutting-plane upper proposer is suggested.
- L6's e/6 constant is about 27× loose.

**Verified positives:**
- **Chronology and freezes.**
  - G2 preceded the all-degree L2 attempts (`b81c374` 14:34Z before `dfa3244` 14:50Z).
  - The L6 contract was frozen at the recorded execution head before the run.
  - The L7 preregistration predates the suite.
  - The G1 spec, fitter and fit are in order.
- **Gates, IDs and storage.**
  - The 60 s/1800 s/900 s scheduling successors were documented prospectively and changed no scientific acceptance.
  - No final IDs are assigned, and the shared-registry diff against main is empty.
  - No reservation overlaps PR25 (T364–375…), PR26 (T376–391/IDEA466–489) or PR21 (LIT482–561).
  - Committed evidence files are ≤15,773 B, and there are no third-party files.
- **Process.** Handoff and commit-trailer protocol is correct.

**Process.** Guard looseness in G1 receipts (L7G1-9); model-metadata mismatch in independent-checks-g1-fit.md (L7G1-10); handoff03's missing Role/Written-by fields (PROT-14); repository JSON ≈4.28 MB after integration, near the 5 MB guidance (PROT-15).

## Independent executions actually performed

All runs took place in this cloud session (Linux 6.18.44, Intel Xeon with AVX-512F, Python 3.13.18), on `git archive` copies outside the repository and single-threaded. They used the scratch dependency set (numpy 2.5.4, scipy 1.18.1, python-flint 0.9.0, mpmath 1.3.0, sympy 1.14.0), with families installing pinned versions where needed (python-flint 0.9.0/numpy 2.3.5 for L4; numpy 2.3.5/scipy 1.17.0/polyrat `6903d7a` for L7).

Summary by family:
- **L1:** rerun of the committed SH checker (PASS, identical); own exact latent-monomial checker n=2..6; fixed-grid variant; 50-digit physical-node run; float capacity measurements n=2..7 (MEASURED).
- **L2:** committed G2 checker and producer on both grids (byte-identical); own exact dual-number recomputation (all 325 T24 nodes; rotQ24 floors plus witness node); SH_n numeric checks; exact inequality sweep.
- **L3:** own 60-digit adversarial, edge-case, adaptive-tie and outside-hypothesis tests (MEASURED supplements).
- **L4:** COLD_STORAGE recipe end to end (`l4_envelope.py` 221 s, `l4_full_witness.py` 164 s, `l4_recheck_fixed.py` PASS with 7/7 controls); own FLINT-free exact reconstruction (0 mismatches over 170,000 entries); degree-12 decimal operation replay with a dropped-channel control.
- **L5:** three committed checkers under two SymPy backends; recorded malformed controls; own FLINT/arb kernel-free checker; predecessor-radius checks.
- **L6:** committed checker on the committed trace; producer rerun (byte-identical); own replay with independent exact rounding; sympy constant analysis; hash reconstructions of the reviewed versions.
- **L7/G1:**
  - Triangle suite under three kernel settings; disk seed 1; own reference check.
  - The four T24 G1 rules regenerated (endpoints byte-identical), with own Arb/exact counterchoice recomputation.
  - The committed fitter on real T24 rows (triangle section byte-identical).
  - Guard refusal test, and fused-engine reproduction.
- **PROT:** the manifest check and reconstruction; G0/G4 legacy rows under four kernels; residual recheck; arithmetic on committed receipts. The orchestrator separately reran the legacy rows under two kernels.

Failed or aborted attempts are recorded in the family reports:
- `/usr/bin/time` absent (exit 127);
- Python's integer-digit limit (L4);
- harness-tolerance defects (L3);
- `-I` dropping `PYTHONPATH` (orchestrator);
- a raw `/tmp` input path (L5);
- the polyrat source fetch refused (PROT).

**Not rerun:**
- the full 152-row G1 scan and rotQ24 rows;
- the capped L5 upper searches;
- the native C++/GMP ports;
- the rotQ24 all-node G2 first-principles dual;
- polyrat upstream_xy G0/G4 rows;
- IEEE/finite-u questions, which are not claimed.

## Trusted dependencies and remaining uncertainty

**Trusted dependencies:**
- CPython integer and Fraction arithmetic;
- FLINT 3.x/python-flint 0.9.0 (fmpq, fmpq_mat, arb);
- SymPy 1.14.0, with both ground-type backends;
- mpmath, NumPy and SciPy/OpenBLAS, for non-proof checks only, plus L7's MEASURED results, which depend on the kernel;
- polyrat `6903d7a`;
- inherited PD-T136–PD-T145 statements where they are cited as dependencies. PD-T138 was re-derived and corroborated at degree 12; PD-T142 was checked against its hypotheses.

**Remaining uncertainty:**
- The developers' self-reported pre-gate drafting order. Git places all drafts in one commit.
- rotQ24 G1 verified from receipts and code only.
- Uncommitted reviewed drafts (L1 `9f59…`, L3 `cdcf…`) whose acceptance carries over by digest or prose. The audited final bytes were checked directly.
- Historical Q bytes unavailable, though 12 matching 17-digit values make the reproduction compelling.

Readiness concerns the stated scope only.

## Stage and next step

- Stage returns to **WORK**. Codex answers each finding in `response-01.md`, by fix, evidence-based rejection or explicit unresolved item, without editing this report or the family reports.
- After that, the changed statuses, scopes and records come back for a focused Claude re-audit before PR preparation. That covers A-M1, A-M2, the A-P1 remediation and A-m1–A-m8. Unchanged accepted mathematics need not be reopened.
- AC must still decide on A-P1. Final IDs, registry application, reservation refresh, main merge and readiness all remain later steps.
