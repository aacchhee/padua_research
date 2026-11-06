# Handoff 01 — padua-mz-sharp-constants-20261106 — sharp MZ constants via limiting operators (PD-T020, PD-T027, PD-T381)

- Status: done in 5110954b07fd834982167780daa8cd22bef13ce1
- Previous handoff: none (new topic)

- Next agent / model / effort: Codex. This follows the allocation AC set on 2026-11-05 and adopted for this topic on 2026-11-06 ("yes, open sharp-constants codex topic under the suggested rules"):
  - coordinator: gpt-6-astra high;
  - numerics, structured eigensolvers, extrapolation, replays and bookkeeping: gpt-6.1-sol medium;
  - routine mathematics: gpt-6.1-sol xhigh;
  - gpt-6-astra ultra only for a decisive hard step: a limit theorem, an identification of a model operator's spectrum, or an error bound linking the model to finite N or m. Record a one-line justification for each in LOG;
  - supplementary independent checks: a distinct gpt-6-astra high instance.
- Role: orchestrator and developer
- Branch: codex/padua-mz-sharp-constants-20261106
- Input head SHA: `76ba421` (main, PR #28 merged; this branch adds only this handoff, LOG and the results stub)
- Main / base: `76ba421`. The rules are PR #29's "Proportionate audit and records".
- Stage: WORK
- Written by / date: Claude, claude-opus-5-5 · 2026-11-06

## Why

The MZ manuscript (`tracks/mz-constants/paper/`) is the paper closest to submission. Its endpoint and growth statements are orders or one-sided constants, not values. Three OPEN targets share one missing tool: an asymptotic limiting-operator model with a quantified error. Each theory file names exactly this as the way to resume.

| Target | Statement (see its record) | Known |
|---|---|---|
| **PD-T020** (`m2-sharp-constant-open.md`) | Does lim (log N)² λ_min(CC, N−1) = c_* ∈ (0, ∞) exist? If so, find c_*. | Order log⁻² two-sided (PD-T017/018); PD-T294: low-Rayleigh harmonic witnesses escape every fixed microscopic edge layer |
| **PD-T027** (`open-upper-limit.md`) | Does λ_max(G_{N,N−1}) converge, and to what? Is there a uniform B < 2? | PD-T022: λ_max < 2 for each N; measured lead about 1.004437 (PD-T026); PD-N104: the sign-discard intermediary has no uniform floor |
| **PD-T381** (`topics/padua-mz-cleanup-20261105/theory/sharp-growth-open.md`) | Do the even- and odd-m limits of λ±(m, m−1)/log m for the signed Padua rule exist, what are they, and do the parities agree? | PD-T379: limsup λ₋/log m ≤ −c₋ and liminf λ₊/log m ≥ c₊ with exact carrier constants, c₋ ≈ 0.02962 and c₊ ≈ 0.01278 (not claimed sharp); PD-T376–378, PD-T380 (MEASURED scans) |

**A steering fact, MEASURED only.** This is Claude's post-hoc 4-point fit to the PD-T300 even-m minima at m = 800–1600: λ_min ≈ 0.652 − 0.0915 log m. The fitted slope is about 3 times the proved one-sided constant c₋ ≈ 0.0296.
- **Correction of Claude's earlier chat remark:** the value 1/9 (the supremum of 16ab/9) belongs to the unnormalized Q(p²)/log m. It is not the normalized Rayleigh quotient, so it is not the comparison for λ_min.
- The carriers of PD-N105 are therefore far from optimal, or the scan has not reached the asymptotic regime. Deciding which is part of S3.

## The idea: scale-invariant (Mellin) and edge (Wiener–Hopf) limit operators

These methods come from neighbouring fields. Read each source's fulltext before citing it, record LIT entries, and give AC clickable DOI or journal links for any paywalled source.

- **The log⁻² law is a classical signature of Mellin-convolution operators.**
  - The norm of the N×N Hilbert matrix, a section of the Carleman operator, is π − π⁵/(2 log² N) + O(log log N / log³ N). Sources:
    - de Bruijn–Wilf, Bull. AMS 1962;
    - Widom–Wilf, "Small eigenvalues of large Hankel matrices", Proc. AMS 1966;
    - Wilf, *Finite Sections of Some Classical Inequalities*, Springer 1970.

    Verify each against its fulltext.
  - The mechanism: in the logarithmic variable t = log(scale), the operator becomes a convolution on a window of length about log N. The spectral gap is then the ground state of the second-order expansion of its Mellin symbol at the extremum, which gives π²/log² N times a symbol coefficient.
  - PD-T294 places the low-Rayleigh CC witnesses at intermediate scales between 1/N and 1, exactly where such a model governs.
- **Microscopic endpoint limits are Wiener–Hopf or Toeplitz-plus-Hankel operators.** A largest eigenvalue that converges to a constant near 1.004 is the kind of value one expects from the norm of a fixed endpoint limit operator at angle scale 1/N. Its norm can be computed from the symbol: Böttcher–Silbermann; Basor–Ehrhardt on Toeplitz-plus-Hankel; Kac–Murdock–Szegő and Widom on extreme eigenvalues.
- **In two dimensions,** the PD-T295/T377 corner weights behave like log m/m⁴, which is scale-invariant at a corner. Polar coordinates around the corner give a radial Mellin variable times an angular operator. The log m growth of λ± should be a Mellin resonance there, with the sharp constant the extremum of an angular eigenvalue problem. The carriers of PD-N105/106 and PD-T378 are particular trial functions for it.

## Directions (all in parallel from the start, after K0)

### S1 — PD-T020, the sharp lower constant

1. Derive the mesoscopic limit of the CC Gram defect, written as G − I or as the cardinal form from PD-T017. Use the exact moments and aliasing of PD-T013 at angle scales 1/N ≪ θ ≪ 1, in the logarithmic variable.
2. Identify its Mellin symbol and the symbol's second-order behaviour at the critical point.
3. Write the predicted c_*^model in a theory file, with a timestamped commit, **before** K1's final extrapolation is read.
4. Then prove:
   - (a) the variational upper bound (log N)² λ_min ≤ c_* + o(1), with an explicit trial family from the model ground state;
   - (b) the matching lower bound, by localization (IMS-type partition between microscopic, mesoscopic and macroscopic scales) plus the model's spectral bound with quantified error.

- Done: a PROVED limit with explicit c_*, or a PROVED one-sided sharp bound plus a precise PARTIAL.
- Mind parity: PD-T018 is parity-exact. State whether c_* depends on N mod 2.

### S2 — PD-T027, the sharp upper limit and a uniform gap

1. Derive the microscopic endpoint limit operator at angle scale 1/N, a Wiener–Hopf or Toeplitz-plus-Hankel operator with an explicit symbol, and compute its norm, giving a predicted λ_max limit.
2. Prove convergence λ_max → that norm, with an explicit error bound ε(N).
3. Then prove a uniform B < 2 for all N:
   - large N from (norm + ε(N));
   - finite N below the crossover from the exact certified CC spectra (existing `tracks/mz-constants/code/`, or a fresh exact or outward port).
- PD-N104's failed intermediary must not be reused.

### S3 — PD-T381, the 2-D sharp growth constants

1. Build the corner model: the PD-T295/T377 weight asymptotics in corner polar coordinates (radial log variable and angle), for even and odd m separately.
2. Derive the predicted slopes for λ₋/log m and λ₊/log m as extrema of an angular eigenproblem.
   - Explain the gap between the carrier constants (c₋ ≈ 0.0296, c₊ ≈ 0.0128) and the measured slope near −0.0915.
   - Decide whether the scan is pre-asymptotic.
3. Prove the limits, or matching two-sided bounds, and settle whether the two parities agree.
- Done: PROVED limits per parity (and their agreement or disagreement), or PROVED improved one-sided constants plus a precise PARTIAL.

### S4 — high-precision numerics (feeds the K gates)

- **1-D:** λ_min and λ_max of the CC Gram problem for N on a geometric grid 10² to 10⁵, plus both parities at each grid point. The problem is Toeplitz-plus-Hankel, so use structured or matrix-free extremal solvers. Use float64 with selective high-precision confirmation, and validate against PD-T026 and the merged spectra.
- **2-D:** the matrix-free signed Padua extremal solver from PR #23/#26, for even and odd m up to about 3000 where affordable.
- Results are MEASURED. Pre-register every fit in `gates.md` before running it.

## Gates (kill criteria written here, before any run)

If a criterion proves ill-posed, record why and add a new criterion as a separate dated entry; never edit the original.

- **K0, replay.** Reproduce:
  - the PD-T026 extreme eigenvalues at its recorded N;
  - the PD-T300 minima at m = 800 and 1000;
  - one PD-T379 carrier norm limit, numerically at large m.

  **Kill:** any mismatch beyond 1e-10 relative (float) until it is explained.
- **K1, 1-D extrapolation (MEASURED).** Fit (log N)² λ_min ≈ c + a·(log log N)/log N + b/log N on two disjoint N windows, with parities separate. Use the Widom–Wilf form, which is the pre-registered model.
  - **Pass:** the two windows' c agree within 2 %.
  - Otherwise: INCONCLUSIVE. Extend N once, then proceed with proof work without a numerical target.
- **K2, S1 model test.** Compare c_*^model, registered before K1's final numbers, with K1's extrapolated c. **Kill (that model):** a mismatch above 5 % when K1 passed. Revise the model once, recording why, then stop S1's model route if it fails again.
- **K3, S2 model test.** Compare the predicted λ_max limit with the extrapolated limit from S4. **Kill (that model):** a mismatch above 1e-3.
- **K4, S3 model test.** Compare the predicted 2-D slopes (even and odd) with the S4 fits over the largest affordable m windows. **Kill (that model):** a mismatch above 10 % on a window that S4 shows is asymptotic, meaning stable slope estimates across two windows.
- **K5, parity.** Before any agreement claim, pre-register whether the even-m and odd-m models predict equal constants.

## Round budget and parallelism

- Up to **15 rounds per direction** (S1–S4), all running in parallel from the start after K0. Each direction has its own subagent and disjoint files; only the coordinator writes LOG, `rounds.md`, `gates.md`, results and the report.
- A round is one development step ending in a pushed LOG entry with its outcome.
- A direction continues only after recorded progress: a new proved lemma, a sharper bound, a model that passes its K gate, or a gate verdict that narrows the route.
- Two consecutive rounds without progress end it, with the obstacle recorded. Kills at K2–K4 end that model route regardless of the budget.

## Read first

- AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md at the branch head.
- `tracks/mz-constants/`:
  - README.md;
  - theory m1-*, m2-* and m3-* (above all m1-cc-foundation, m2-cardinal-lower, m2-parity-upper, m2-sharp-constant-open, m3-upper-ratio, open-upper-limit, reproduced-spectra);
  - code/;
  - paper/ (README.md, manuscript.tex).
- `topics/padua-mz-2d-frontier-20261105/`:
  - report.md;
  - theory f12-local-weight-asymptotic, f12-eventual-negative-carrier, f12-eventual-upper-carrier, f12-harmonic-boundary-escape (PD-T294), f12-1d-sign-discard-obstruction (PD-N104);
  - code/.
- `topics/padua-mz-cleanup-20261105/`: report.md; theory/ (growth-carrier-bounds, odd-weight-asymptotic, odd-carriers, sharp-growth-open, finite-measurements); code/.
- PROOF_STATUS rows PD-T013–T028, PD-T294–T300, PD-T376–T381 and PD-N104–N107. IDEAS entries IDEA-210–227, 384–397 and the cleanup entries.
- `literature/INDEX.md` and the merged PR #21 P2 comparison (`topics/padua-literature-20261103/p2-comparison.md`) for priority wording.

## Scope limits

- **Where to write.** Only inside `topics/padua-mz-sharp-constants-20261106/` and `results/padua-mz-sharp-constants-20261106.md`.
  - Do not edit the manuscript on this branch. Draft manuscript-ready statements in `manuscript-insert.md` for a later writing step.
  - At PR preparation, edit the shared registries directly; the readiness check reviews them by diff.
  - Do not write to any other open branch, PR #27 included.
- **IDs.** Provisional IDs `PD-T?mz-sharp-codex-NN`, and likewise for PD-N, IDEA and LIT. Reserve final ranges when first needed (normally at PR preparation), and recheck at readiness.
- **Novelty gate** before each model or mechanism. Nearest entries: IDEA-210–227 and 384–397, the cleanup entries, and the obstruction rows behind PD-N104.
- **Statuses follow AGENTS.md.**
  - Extrapolations and fits are MEASURED and never prove a constant.
  - A limit theorem needs a written proof with quantified errors. A computer-assisted finite range needs a proved reduction, exact or outward arithmetic, committed producer and checker code, and an independent rerun.
- **Storage:** commit code and small evidence, normally under 16 KiB per file. Large spectra and arrays go to cold storage via `tools/cold_storage.py`, with `cold-storage.json` and `COLD_STORAGE.md`.
- **Compute.**
  - Sandbox: up to 6 h wall per run and about 48 h of cumulative CPU, as AC approved for the parallel campaigns.
  - Ask AC before using Syvert. If you do, build packs in the "Syvert run pack" structure of the bridge handoff. Until PR #27 merges, read it with `git show origin/codex/padua-argmax-bridge-20261105:topics/padua-argmax-bridge-20261105/handoffs/01-work.md`.
- **Literature.**
  - You may open any public page holding relevant literature. Cite only after a fulltext read, and record LIT entries.
  - List unreachable fulltexts for AC with clickable DOI and journal links.
  - Never commit third-party PDFs or extracts (the repo is public). Do not bypass captchas or bot checks.
- **Commits** are authored as Andrey Chesnokov <aacchhee@gmail.com>, with trailers `Agent: Codex` and `Model: <exact model and effort>`. Never commit to main, merge, force-push, create tags or touch .github/. Only AC merges.

## Acceptance and outputs

- **Files.**
  - `LOG.md`, `plan.md` (written before the first run) and `rounds.md`.
  - `gates.md`, with K0–K5 verdicts and all pre-registrations.
  - `attempts/S1…S4.md` and `novelty-gate-*.md`.
  - `theory/` records in THEORY-template form: each model operator, each symbol computation, each limit or bound, each PD-N.
  - `independent-checks*.md`, `evidence-manifest.json` and `manuscript-insert.md`.
  - `results/padua-mz-sharp-constants-20261106.md`, kept current, and `report.md` at the end.
- **Pushes and PR.** Push at every gate and round boundary, and at least every ~10 minutes while something has changed. Open a draft PR early; no reservation is needed for a draft.
- **The report contains:**
  - K0–K5 verdicts;
  - for each target, the model, the predicted constant, the measured extrapolation and the proved statement;
  - the parity answers;
  - what remains OPEN;
  - the exact sentences proposed for the MZ manuscript, with their dependencies.
- **Closing.** When done, commit the outputs. Then, in a following commit, set this status to `done in <sha>` and open handoff 02 for the single substantive audit by Claude, Opus 5.5 xhigh, which reads the complete state/IDEAS.md because this branch carries mechanism and novelty content. Reply to AC only with `Claude (Opus 5.5 xhigh): Continue codex/padua-mz-sharp-constants-20261106.`
