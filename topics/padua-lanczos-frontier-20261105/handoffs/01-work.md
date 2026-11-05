# Handoff 01 — padua-lanczos-frontier-20261105 — bivariate Lanczos / Vandermonde-with-Arnoldi, round 2

- Status: open
- Previous handoff: none

- Next agent / model / effort: Codex. Mathematics: gpt-6.1-sol xhigh. Ultra is allowed for proof steps on L1–L3, with a written justification in LOG. Code, exact certificates, benchmarks and replays: gpt-6.1-sol medium. Supplementary independent checks: gpt-6-astra high.
- Role: orchestrator and developer
- Branch: codex/padua-lanczos-frontier-20261105
- Input head SHA: `440d1079e42c3ef21c40d1cf8870f5b206410c6a` (main, PR #17 merged; this branch adds only this handoff, LOG and the results stub)
- Main / base: `440d107`
- Stage: WORK
- Written by / date: Claude, claude-opus-5-5 · 2026-11-05

## Context

The drift campaign (PR #15, merged; `topics/padua-lanczos-drift-20261101/`) produced the first span-sensitivity theory for bivariate Stieltjes/Lanczos recurrences and multivariate V+A:

- **PROVED.**
  - PD-T136: the first-order span derivative is the normal quotient of the frozen recurrence.
  - PD-T137: rational lower and upper certificates for aggregate span sensitivity.
  - PD-T138: the normal-quotient map of a formal scalar CGS2 graph.
  - PD-T139 and PD-T141: certified finite BJ/comparator separations on T24 and rotQ24 at degree 12.
  - PD-T142: an a-posteriori span certificate from a computed recurrence.
  - PD-T143: a first-order selection guarantee at fixed degree.
  - PD-T144: ρ_n = O(n⁻⁵) for the Padua certificate P_n, which proves PD-T075(U1).
  - PD-T145: an explicit n = 1 square family with √ε support spread.
- **PROVED negatives.**
  - PD-N062: at fixed degree, no prior-vector subtraction rule removes the drift or closure defect of a raw-product source.
  - PD-N063: three failed negative-witness mechanisms for P_n.
- **MEASURED.**
  - PD-T140: the formal scalar-CGS2 capacity experiment. Its factor-ten target is PARTIAL: T24 conjunct PROVED, rotQ24 conjunct OPEN; the certified rotQ24 squared ratio 62.09 is below 100.
  - PD-T146: polyrat 0.2.2 V+A span gaps of 0.0041 (rotated square, n = 24) and 0.0102 (triangle, n = 20) at near-machine orthogonality. Off-sample errors are about 1e-3 on centre-concentrated points and about 2e-2 on uniform interior points, for an adversarially chosen polynomial target. exp(x+y) is fitted to about 1e-13.
- **OPEN** (report, "Remaining obligations"):
  - **E2:** an all-degree drift theorem on an explicit non-product family. It needs an exponential BJ lower bound and a matching good-rule upper bound in a fully stated model.
  - an **unconditional selection theorem**: polynomial score bounds, accepted staircases for every degree, a usable finite-u radius, and efficient online selection;
  - **PD-T055** in its original scope. The pathwise reading is ill-posed (IDEA-253), so the target needs a well-posed formalization first.
  - **PD-T056 reading (G):** a Greenbaum-type backward model for actual 2-D runs;
  - **PD-T075(U2):** is inf_{n≥3} δ_obs(n) > 0?
  - the rotQ24 factor-ten conjunct of PD-T140;
  - the missing BNT (MATLAB) and Zhu–Nakatsukasa code runs;
  - optionally, PD-T072 (square-case first-order commutator isomorphism).
- **Literature** (PR #21, P3 comparison, unmerged). No matching published result was found for span drift (PD-T053, PD-T136–143), PD-T069, PD-T144 or PD-T145. Every finite-precision Lanczos theory read is for one operator, with a single vector or a block start. Zhu–Nakatsukasa Remark 5.1(5) bounds the orthogonality ‖Q*Q − I‖ for CGS2, not span accuracy. Hokanson remarks that many orderings fail the span property, in exact arithmetic.

This is round 2, and it is broader and more adventurous than round 1. The aim is to turn finite separations into theorems about all degrees, to fix PD-T055 into a provable or refutable statement, and to find out whether span drift matters on real fitting problems. Run directions in parallel subagents with disjoint file ownership, chase surprises, and stop each direction at its box. The honesty rules do not relax.

## Targets (priority order)

### L1 — the all-degree drift theorem E2. Box: about 10 h.

- **Goal.**
  - Fix an explicit non-product family before any proof attempt. Candidates: uniform triangle grids T_N; rational rotated product grids rotQ_N (cos 3/5, sin 4/5); Padua points; a one-parameter family with closed-form recurrence coefficients, if one exists.
  - Fix its parent rule, the number of samples against the space dimension (M > N_s), and the perturbation class (aggregate preprojection residuals as in PD-T136/137, or the formal scalar-CGS2 model of PD-T138).
  - Prove: (i) a lower bound on the span sensitivity of the BJ/dev selection that grows exponentially in degree, and (ii) an upper bound for at least one good selection (pivot-adaptive, alternating staircase or mirror) that grows at most polynomially, or exponentially at a provably smaller rate. Both must hold for all degrees in the family.
- **Keep two notions apart.** Worst-case aggregate-residual amplification is not drift for every scalar-rounding realization; E2's direction file says the latter cannot be inferred from an operator norm. State which one each result proves.
- **Routes.**
  - Structure of the normal-quotient map along the family: transfer-matrix or recursion form of the PD-T136 derivative.
  - A product-to-non-product perturbation argument from closed-form product-grid recurrences.
  - PD-T053, the reference-free drift lower bound, as the lower-bound engine.
  - Exact certificates from PD-T137/139 extended to higher degrees to fix the constants.
- **Done:**
  - a PROVED all-degree theorem with explicit constants on one family;
  - or PROVED for one direction (lower or upper) and OPEN for the other, as a precise PARTIAL;
  - or a scoped PD-N showing the separation is subexponential on the frozen family.

### L2 — PD-T055 well-posed and settled. Box: about 6 h; may share L1's subagent.

- **Step 1.** Write candidate well-posed formalizations of PD-T055(U) in `attempts/L2.md` before attempting any proof. For example:
  - (W) worst case over admissible error realizations, |err| ≤ u, for each rule in a stated class;
  - (R) expectation or high probability under a stated random-rounding model;
  - (F) a fixed IEEE implementation with a stated operation order.

  Each formalization must exclude the trivial exact-run counterexample behind IDEA-253, and keep the selection fixed to BJ, as the original requires.
- **Step 2.** Prove or refute one formalization on one family. L1's lower-bound engine, if it succeeds, is the natural input. PD-N062 supplies the fixed-degree O(u) step, so growth is what is needed.
- **Done:** a PROVED or refuted well-posed PD-T055 on an explicit family, with the formalization recorded as its own theory file; or a precise obstruction.

### L3 — the selection principle. Box: about 6 h.

- **Goal:** turn PD-T142/143 into an unconditional, computable selection rule with a guarantee, or prove that none of a stated kind exists. Possible shapes:
  - polynomial-in-degree score bounds for the filtered minimax staircase;
  - existence of an accepted staircase at every degree on a family;
  - a finite-u radius for the first-order guarantee, with an explicit O(u²) remainder;
  - an online O(n)-per-degree selection whose certificate is checked a posteriori by PD-T142.

  Note that PD-T143 excludes the pivot-adaptive rule. Decide whether pivot-adaptive admits its own guarantee.
- **Done:** a PROVED guarantee, a counterexample family (scoped PD-N), or PARTIAL with the exact remaining obligation.

### L4 — the factor-ten rotQ24 conjunct of PD-T140. Box: about 4 h.

- Tighten the certified full scalar-CGS2 comparison on rotQ24 at degree 12 until the squared ratio exceeds 100 (κ ratio > 10), or prove that the frozen model's achievable ratio is below 100 (a kill).
- Routes:
  - sharper comparator upper bounds, using the row bound beyond KHS as response-01 did for the aggregate case;
  - a better multinode BJ lower witness than greedy.
- Keep the frozen test separate: an improved certificate never replaces the original INCONCLUSIVE outcome, which stays recorded.

### L5 — PD-T075(U2), uniform Padua obstruction radius. Box: about 4 h.

- **Goal:** decide whether inf_{n≥3} δ_obs(n) > 0, as defined in `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-319-padua-obstruction-radius-uniformity.md`.
- PD-T144 bounds only the radius of the named certificate P_n, and ρ_n ≤ δ_obs(n) cannot bound δ_obs from above.
- Routes:
  - an upper bound on δ_obs(n) → 0, from any nonzero p ∈ Π_{2n+1} vanishing on 𝒫_n and nonnegative on K_δ(n), via a dimension or interlacing argument near the edges where Padua nodes cluster;
  - or a uniform positive lower bound from a family of certificates.

  Compute exact or certified δ_obs(n) bounds for n = 3–10 first, by a semidefinite or sum-of-squares search, with exact rational certificates for acceptance.
- **Done:** PROVED (U2) either way, or certified finite values (PROVED as finite statements) with the asymptotic question still OPEN.

### L6 — PD-T056 reading (G). Box: about 4 h; lower priority.

- **Goal:** a Greenbaum-type backward model realized by an actual floating-point recurrence. That means a computed 2-D run (fixed implementation, fixed u) whose computed section is the exact section of a nearby measure, with explicit radius.
- Start from the PD-T145 square n = 1 family: is there an actual recurrence with smaller local u realizing it? Then Padua n = 3, 4.
- Respect PD-T069/N303: on Padua, reading (E) has an exact obstruction for all n ≥ 3, so (G) there must allow the obstruction's scale.
- **Done:** PROVED construction, PROVED obstruction, or a precise reduction.

### L7 — measured V+A study on real fitting problems. Box: about 6 h; can run in parallel from the start (medium effort).

- **Pre-register in `gates.md` before any run** the problem suite, codes, selections, metrics and comparison rule.
- **Suite:**
  - smooth functions with nearby complex singularities (e.g. 1/(1 + 25(x² + y²)), tanh(10(x + y − 0.3)));
  - nonsmooth data (|x − y|);
  - scattered data on non-product domains: disk, L-shape, triangle, annulus sector;
  - a data-fitting task from the literature that is cited only after a fulltext read.
- **Codes:**
  - polyrat (pinned commit 6903d7a…; see `topics/padua-lanczos-drift-20261101/external-code.md`);
  - BNT's code under GNU Octave if it is installable in the sandbox;
  - a Zhu–Nakatsukasa implementation if one can be identified (record the search);
  - the repository's own BJ/dev, mirror, alternating and pivot-adaptive selections, with and without reorthogonalization.
- **Metrics:**
  - span gap against an exact or long-double reference;
  - off-sample error on uniform and boundary-concentrated test sets, both pre-registered;
  - ‖Q*Q − I‖;
  - coefficient norms.
- **Question:** does span drift translate into a fitting-error loss on natural (non-adversarial) targets, and does the selection rule matter? Results are MEASURED. Third-party source stays outside the repository; record URL, version and hashes only.

## Gates (kill criteria written here, before any run)

Run G0 first. Then the others may run in parallel. Record each verdict in `gates.md` with the command, the output receipt and the date. If a criterion proves ill-posed, record why and add a new criterion as a separate dated entry; never edit the original.

- **G0, replay.** In a clean subagent, rerun from `tracks/bivariate-lanczos/code/drift/`:
  - `e1_reproduce.py` (or its documented subset at degrees 2–6);
  - `e1_scalar_finite_check.py`;
  - `e5_exact_checks.py`;
  - `e6_benchmark.py` on one case.

  Compare with the committed evidence. **Kill:** any unexplained mismatch stops the campaign until it is explained.
- **G1, growth scan for L1.**
  - Compute exact or certified PD-T137 aggregate-sensitivity bounds for BJ/dev and for the best comparator, on T_N and rotQ_N, at degrees 2–20, with N large enough for M > N_s at every degree.
  - Use C/FLINT (or GMP/Arb) if Python exact arithmetic exceeds about 30 min per case. Validate against PD-T139 at degrees ≤ 12, and write an independent checker port.
  - Pre-register the fit: the slope of log K against degree, the range, and a model comparison of exponential against polynomial growth.
  - **Kill (exponential separation on that family):** the BJ/comparator log-ratio grows sublinearly in degree by the pre-registered rule. Then L1 pivots to a different family or to a scoped PD-N. MEASURED fits never prove a rate.
- **G2, L2 formalization check.** Each candidate formalization in `attempts/L2.md` must:
  - (a) exclude the exact-run counterexample;
  - (b) have a finite-degree instance computable exactly on T24 or rotQ24;
  - (c) have its truth value at degree 12 decided by a certified computation before any all-degree proof attempt.

  **Kill:** a formalization whose degree-12 instance is false is dropped, with a scoped record.
- **G3, L5 small-n values.** Certified δ_obs(n) brackets for n = 3–8 from exact rational sum-of-squares or LP certificates. **Pass:** a monotone trend clear enough to choose between "→ 0" and "bounded below" for the proof attempt. Otherwise, try both directions for one round each.
- **G4, L7 sanity.** Reproduce PD-T146's two table rows with polyrat before running new problems. **Kill:** a mismatch stops L7 until it is explained.

## Read first

- AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md at the branch head.
- `topics/padua-lanczos-drift-20261101/`:
  - report.md and plan.md;
  - directions/E1–E6.md;
  - ideas-e1.md, ideas-e3-e4.md, ideas-e5.md, ideas-e6.md;
  - audits 01–04 and responses 01–03;
  - external-code.md and independent-checks.md.
- `tracks/bivariate-lanczos/theory/`:
  - drift-codex-*.md (PD-T136–146, PD-N062–063);
  - bj-universal-reorthogonalization-obstruction-open.md (PD-T055);
  - bivariate-lanczos-claude-300/302/304/305/309/316/319 and N301/N302/N303/N308 (PD-T056–T075, PD-T069);
  - commutator-shadow-recursion-and-span-drift-bound.md (PD-T053);
  - condition-C-staircase-selections-acyclic-sections.md.
- `tracks/bivariate-lanczos/code/drift/` and the track README.
- PROOF_STATUS rows PD-T029–T080, PD-T136–T146, PD-N007–N031 and PD-N062–N063. IDEAS entries IDEA-246–267, the Lanczos rows of the Obstruction table, and the entries those rows point to.
- Literature: literature/INDEX.md. Also read the P3 comparison on PR #21's branch, read-only: `git show origin/claude/padua-literature-20261103:topics/padua-literature-20261103/p3-comparison.md`, with its addenda on Xu Trans. AMS 1994 and Dunkl–Xu. These are unmerged; cite them as "PR #21 (unmerged)".

## Scope limits

- Write only inside `topics/padua-lanczos-frontier-20261105/` and `results/padua-lanczos-frontier-20261105.md`.
  - Do not edit merged topic, theory, code or registry files; import or copy frozen code instead.
  - Put proposed shared-record changes as literal old→new blocks in `proposed-record-changes.md`.
  - Do not write to any other open branch: PR #19–#22, and `codex/padua-mz-2d-frontier-20261105`.
- Novelty gate (relaxed scan, WORKFLOW) before each new mechanism. Record the closest entries (at least IDEA-246–267, IDEA-253, and the entries behind PD-N062/063), the applicable obstructions and which hypotheses the idea breaks, the verdict and the cheapest test.
- Provisional IDs: `PD-T?lanczos-frontier-codex-NN`, and likewise for PD-N, IDEA and LIT.
  - When the draft PR opens, reserve final ranges by the fresh-range procedure: main, every open PR (#19–#22 at writing), retired reservations and the batch ledger, with headroom.
  - Coordinate through the ledger with the parallel MZ frontier branch, and do not overlap.
- Statuses follow AGENTS.md:
  - Floating-point experiments, fits and benchmark results are MEASURED.
  - A computer-assisted PROVED claim needs a written proved reduction, exact or outward-rounded arithmetic, committed producer and checker code, small evidence, and an independent rerun by a different subagent.
  - Results in a formal rounding model say so in their statement and never claim actual IEEE behaviour.
  - Finite separations never prove all-degree rates.
- Storage (WORKFLOW, PR #18): commit code and small evidence (normally under 16 KiB per file). Regenerable or large outputs go to cold storage via `tools/cold_storage.py`, with `cold-storage.json` and `COLD_STORAGE.md`, under `Downloads\padua\cold_storage\padua-lanczos-frontier-20261105\`. Hand them to AC.
- Third-party code is never committed. Record its URL, version, commit and file hashes in `external-code.md`.
- Literature:
  - You may open any public page holding relevant literature. Cite a source only after reading its fulltext, and record LIT entries.
  - List unreachable fulltexts for AC with clickable DOI and journal links.
  - Never commit third-party PDFs or fulltext extracts (the repo is public). Do not bypass captchas or bot checks.
- Compute only in your sandbox. Ask AC before using NTNU servers (syvert0/1/2) or any other machine.
- Commits are authored as Andrey Chesnokov <aacchhee@gmail.com>, with trailers `Agent: Codex` and `Model: <exact model and effort>`. Never commit to main, merge, force-push, create tags or touch .github/. Only AC merges.

## Acceptance and outputs

- `LOG.md` with an entry per gate and target boundary.
- `plan.md`, written before the first run, with time boxes.
- `gates.md` with G0–G4 verdicts against the criteria above, and L7's pre-registration.
- `attempts/L1…L7.md`.
- `theory/` records in THEORY-template form, one per result (PROVED, PARTIAL, MEASURED or PD-N).
- `independent-checks*.md`, `evidence-manifest.json`, `external-code.md`, `results/padua-lanczos-frontier-20261105.md` (kept current) and `report.md` at the end.
- Push at every gate and target boundary, and at least every ~10 minutes while something has changed.
- Open a draft PR to main early, with WORK / AUDIT (PENDING) / PR sections and the ID reservation.
- The report contains:
  - G0–G4 verdicts;
  - L1–L7 status with record links;
  - the frozen family and model for each theorem;
  - certified ranges and cost curves;
  - L7's measured verdict on whether drift costs accuracy on natural targets;
  - what remains OPEN, with the exact next obligation;
  - a short "for the paper" paragraph: which statements could enter the bivariate Lanczos / V+A note, with exact dependencies and the P3 priority wording they need.
- When done, commit the outputs. Then, in a following commit, set this status to `done in <sha>` and open handoff 02 for the audit by Claude, Opus 5.5 xhigh, which reads the complete state/IDEAS.md because this branch carries mechanism and novelty content. Reply to AC only with `Claude (Opus 5.5 xhigh): Continue codex/padua-lanczos-frontier-20261105.`
