# Handoff 01 — padua-mz-2d-frontier-20261105 — signed Padua Marcinkiewicz–Zygmund frontier (PD-T110, PD-T116, PD-T028, PD-T114)

- Status: done in dee638408505c9977f3febd98fdd42c9bc512c92
- Previous handoff: none

- Next agent / model / effort: Codex. Mathematics: gpt-6.1-sol xhigh. Ultra is allowed for proof steps on F1–F3, with a written justification in LOG. Code, certification ports and replays: gpt-6.1-sol medium. Supplementary independent checks: gpt-6-astra high.
- Role: orchestrator and developer
- Branch: codex/padua-mz-2d-frontier-20261105
- Input head SHA: `440d1079e42c3ef21c40d1cf8870f5b206410c6a` (main, PR #17 merged; this branch adds only this handoff, LOG and the results stub)
- Main / base: `440d107`
- Stage: WORK
- Written by / date: Claude, claude-opus-5-5 · 2026-11-05

## Context

The first 2-D campaign (PR #14, merged; `topics/padua-mz-2d-20261101/`) built the exact machinery for the signed interpolatory Padua rule Q_m on Π_n. It also left every universal spectral question about that rule OPEN. In summary:

- **What exists (PROVED).**
  - PD-T106: the exact alias formula and rational Gram pencil. Q_m(T_aT_b) = h_A h_B if A+B ≤ m, and h_{m−A} h_{m+1−B} otherwise, where A, B are folds modulo 2m and 2(m+1).
  - PD-T109: the finite masked-tensor defect architecture. It has at most 160 terms, each a 1-D signed-degree truncation with Fourier multiplier ≤ 1+log(8n+1). This controls the operator but gives no sharp spectral estimate.
  - PD-T107: certified strict brackets of width 1e-6 at m = 10, 20, 30, 40, from an exact inertia checker.
  - PD-N044: η > 3/4 at m = 30, n = 29.
  - PD-T111: exact corner weights, negative for every m ≥ 3, with w_c = −(4 log m + O(1))/m⁴.
  - PD-T112/113: signed hyperinterpolation, with norm from absolute weights and the correct reproduction degree.
  - PD-T115: exact diamond-filter reconstruction.
  - PD-T117: tensor-CC extrema on the total-degree space equal the coordinate CC extrema; the endpoint order is log⁻², and η → 1.
  - Negatives PD-N045–053: which transfer mechanisms fail, and exactly where.
- **What is measured (PD-T108).** For n = m−1:

  | m | 10 | 20 | 30 | 40 | 60 | 80 | 100 |
  |---|---|---|---|---|---|---|---|
  | λ₋ | 0.35619 | 0.27223 | 0.23671 | 0.21482 | 0.18859 | 0.17273 | 0.16175 |
  | λ₊ | 1.63486 | 1.72331 | 1.75793 | 1.77809 | 1.80201 | 1.81650 | 1.82658 |

  A sweep over every integer m = 2–40 found no nonpositive minimum and no maximum reaching 2. The fitted asymptotics were never claimed.
- **What is OPEN.**
  - PD-T110: λ₊(m, m−1) < 2 for all m ≥ 2, with an explicit bound.
  - PD-T028: λ₋ > 0 for all m, the endpoint order (log⁻² against log⁻⁴ or another law), and η → 1.
  - PD-T116: an explicit η(θ) < 1 at every fixed ratio θ < 1, or a disproof.
  - PD-T114: a uniform C → L²(dx dy) bound for the signed coefficient operator H_{m,m−1}.
  - The 1-D sibling, PD-T027: the sharp Clenshaw–Curtis endpoint upper limit and a uniform endpoint gap.
- **Literature.** The literature campaign (PR #21, P2 comparison, including Mastroianni–Russo 2000 read on 2026-11-05) found no published result matching PD-T110/114/116/028 in the documented search. The nearest published work uses positive weights and oversampled or full-interpolation spaces with unspecified constants: KLP Lemma 5.1, De Marchi–Kroó, Wu, An–Sommariva–Vianello. Mastroianni–Russo Thm 11 covers Clenshaw–Curtis only away from the p = 2, u ≡ 1 endpoint case, where its A₂ hypothesis fails, and gives no rates.

This campaign is deliberately broader and more adventurous than PR #14. Its working hypothesis is the two-part shape that worked for the argmax:

1. an **asymptotic part**: a limiting (scaled, corner- or edge-localized) operator whose spectrum controls λ_± for m ≥ m₀;
2. a **finite part**: certified spectra for m < m₀, from a fast exact or interval port.

That hypothesis may be wrong. Gates G1–G3 exist to find out cheaply. Run directions in parallel subagents with disjoint file ownership, chase surprises, and stop each direction at its box. The honesty rules do not relax.

## Targets (priority order)

### F1 — the upper threshold PD-T110 (and its 1-D sibling PD-T027). Box: about 10 h.

- **Goal:** for all m ≥ 2, λ₊(m, m−1) < 2 with an explicit quantitative gap, or a certified counterexample (scoped PD-N).
- Equivalent form (theory file): A := 2H − R is positive definite on Π_{m−1}, where H is the continuous mass matrix and R the signed Padua mass matrix in the product-Chebyshev basis.
- **Routes**, not prescriptions:
  - **R1, limiting operator.**
    - Locate the extremal eigenvectors: do they concentrate at the corners, at the edges, or spread out?
    - Derive the scaled limit of the defect R − H there (a quadrant or half-plane Hankel/Toeplitz model from PD-T106's fold formula).
    - Prove a spectral bound for the model, then a quantitative m → ∞ comparison.
    - Do the 1-D analogue first (PD-T027, CC endpoint upper limit) as the warm-up and the cheapest test of the method.
  - **R2, tensor comparison.**
    - Write R = T + (R − T), with T the tensor-CC Gram on the same total-degree space (PD-T117 gives λ_max(T) < 2).
    - Bound the signed remainder on the actual Padua sample subspace, keeping PD-T109's exact sign structure instead of absolute majorants.
    - Exclusions:
      - PD-N046: doubled tensor weights do not majorize.
      - mz2d-upper-tensor-obstruction and mz2d-upper-sign-obstruction: two exact mechanism failures.
      - Test any proposed scalar bound first on the boundary modes with a reflected zero index, where h₀ reverses the sign of the mixed kernel (theory file, Open items).
  - **R3, parity/Schur resumption.** Allowed only with a genuinely new mass-normalized estimate (theory file resumption criterion).
- **Done:**
  - a PROVED all-m theorem with an explicit gap, or PROVED for m ≥ m₀ together with certified finite m < m₀;
  - or a precise PARTIAL split, each part in its own theory file;
  - or a certified counterexample.

### F2 — positivity and endpoint order, PD-T028. Box: about 8 h; shares R1 machinery with F1.

- **Goal:** λ₋(m, m−1) > 0 for all m. Then the two-sided order of λ₋: is it ≍ (1+log m)⁻² like tensor CC (PD-T117), ≍ log⁻⁴, or something else? Then whether η → 1.
- Known: λ₋ ≤ C/(log m)² (PD-T018/021); liminf η ≥ 1.
- The measured λ₋ in the table decays more slowly than (1+log m)⁻² over m ≤ 100. The ratio λ₋·(1+log m)² rises from about 3.9 to about 5.1. So the asymptotic regime may not have been reached; G2 below decides what to measure next.
- **Done:**
  - PROVED positivity for all m (asymptotic plus certified finite range);
  - or a two-sided order, or one side;
  - or a certified nonpositive case.

### F3 — fixed ratio, PD-T116. Box: about 6 h.

- **Goal:** an explicit η(θ) < 1 for every θ < 1, uniformly over m and n ≤ θm, or a disproof at some θ < 1.
- For 2n ≤ m half-exactness gives η = 0, so the content is θ ∈ (1/2, 1).
- **Routes:**
  - the 1-D template PD-T024 (fixed-ratio η(θ) from PD-T022/023);
  - the fixed-ratio limit of R1's model operator;
  - the theory file's resumption obligation: a positive coercive sampled form S_{m,n} and r(θ) < 1 bounding the negative nodal contribution, together with a separate upper constant below 2.
- Exclusions: PD-N048 (crude continuous corner subtraction diverges, θ⁴ (log m)/6) and PD-N053 (rectangular Fejér aliasing). Use the diamond reconstruction PD-T115 with its diagonal localization checked.
- **Done:** PROVED η(θ) < 1 with explicit form; or PARTIAL for θ ≤ θ₀ < 1; or a counterexample.

### F4 — uniform hyperinterpolation norm, PD-T114. Box: about 4 h; lowest priority.

- **Goal:** sup_m ‖H_{m,m−1}‖_{C→L²} < ∞ with a useful value, or a proof of growth.
- PD-T112 gives the norm as √(τ β_abs). PD-N052 shows that uniform absolute-Gram and negative-leverage majorants diverge, so a proof must use the actual signed operator.
- If F1/F2 succeed, check whether their structure gives F4 directly.

## Gates (kill criteria written here, before any run)

Run G0 first. G1–G3 may then run in parallel. Record each verdict in `gates.md` with the command, the output receipt and the date. If a criterion proves ill-posed, record why and add a new criterion as a separate dated entry; never edit the original.

- **G0, replay.** In a clean subagent, rerun:
  - `tracks/mz-constants/code/mz2d_exact.py` and `mz2d_independent_check.py` at m = 10;
  - `mz2d_spectra.py` at m = 10, 20, 30, 40.

  Compare with PD-T107/108. **Kill:** any mismatch beyond the stated bracket or float tolerance stops the campaign until it is explained.
- **G1, fast spectra and certified extension.**
  - Build a matrix-free extremal eigensolver for the pencil (R, H) on Π_{m−1}. Matrix-vector products via the PD-T106 fold formula or fast cosine transforms; LOBPCG or Lanczos with a shift. Float64 (MEASURED) up to m = 1000 if feasible.
  - Port the PD-T107 exact inertia certifier to C with FLINT (fmpq_mat or fmpz with denominators), or GMP/MPFR/Arb with outward rounding. Python is acceptable only up to about m = 40.
  - Validate the port on m = 10–40 against PD-T107. Write an independent checker port, in a different language or with a different method, by a different subagent.
  - Push the certified range as far as cost allows. Report sizes, times and memory.
  - **Kill (port):** if the port cannot certify m = 60 within 2 h of wall time in the sandbox, record the cost curve and stop the extension at the last certified m. Ask AC before using any machine outside the sandbox (NTNU servers included).
- **G2, scaling pre-registration.** Before running m > 100, write in `gates.md` the candidate laws:
  - for 2 − λ₊(m): (a) → L > 0; (b) ≍ 1/log m; (c) ≍ 1/log² m; (d) other;
  - for λ₋(m): (a′) ≍ log⁻² m; (b′) ≍ log⁻⁴ m; (c′) other;

  together with the fit protocol (range, weights, model comparison rule). Then run G1's float solver at m up to 1000 and record which law fits. **Kill (R1 upper limit):** if (b) or (c) wins by the pre-registered rule, the R1 claim "λ₊ → L < 2" is killed. F1 then becomes a log-gap statement, and the explicit-bound target is adjusted in a dated entry. MEASURED fits never prove an order.
- **G3, localization.** For m = 100, 200, 400 (float), record where the extremal eigenvectors of (R, H) concentrate. Use the mass fraction within distance K/m of the corners and edges (in angle variables), for K = 2, 5, 10.
  - **Pass (R1 viable):** for both λ₊ and λ₋, at least 90 % of the mass lies in a K = 10 corner and edge neighbourhood, at all three m.
  - **Kill (R1 as stated):** if the mass spreads (under 50 % in that neighbourhood at m = 400). Then pivot to R2/R3 and record the profile.
- **G4, counterexample screen.** Combine G1's certified brackets for every m = 2–(max certified) at n = m−1 with a float scan at n = m−1 and n = m−2 for m up to 300, looking for λ₋ ≤ 0 or λ₊ ≥ 2. Any hit must be certified exactly before it becomes a PD-N. No hit is MEASURED, finite-range evidence only.
- **G5, F4 screen.** Certified lower bounds on ‖H_{m,m−1}‖_{C→L²}, from explicit continuous inputs (sign patterns of the cardinal functions), and float estimates of the norm, for m up to 200. Pre-register laws (bounded / ≍ log m / ≍ √log m). A finite growth witness does not refute uniformity; it only steers effort.

## Read first

- AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md at the branch head.
- `topics/padua-mz-2d-20261101/`: report.md, definitions.md (fixed conventions; do not change them), ideas-d1/d2/d4/d5.md, independent-math-d1/d2.md, audit-01.md, response-01.md, response-d4/d5.md, literature.md, LOG.md.
- `tracks/mz-constants/theory/`:
  - mz2d-upper-open.md (PD-T110), mz2d-fixed-ratio.md (PD-T116), mz2d-hyperinterpolation-uniform-open.md (PD-T114), open-padua-target.md (PD-T028), open-upper-limit.md (PD-T027);
  - every other mz2d-*.md;
  - the 1-D records for PD-T013–T024 (m1-*, m2-*, m3-*), above all m3-upper-ratio.md and m3-uniform-eta.md.
- `tracks/mz-constants/code/`: mz2d_exact.py, mz2d_independent_check.py, mz2d_spectra.py, m1–m3 checkers, reproduce.py.
- PROOF_STATUS rows PD-T013–T028, PD-T106–T117, PD-N044–N053. IDEAS entries IDEA-210–227 and the Obstruction table.
- Literature: literature/INDEX.md. Also read the P2 comparison and the Mastroianni–Russo record on PR #21's branch, read-only:
  - `git show origin/claude/padua-literature-20261103:topics/padua-literature-20261103/p2-comparison.md`
  - `git show origin/claude/padua-literature-20261103:literature/records/mastroianni-russo-2000.md`

  These are not merged. Cite them as "PR #21 (unmerged)", and re-cite by LIT number once merged.

## Scope limits

- Write only inside `topics/padua-mz-2d-frontier-20261105/` and `results/padua-mz-2d-frontier-20261105.md`.
  - Do not edit merged topic, theory, code or registry files; import or copy frozen code instead.
  - Put proposed shared-record changes as literal old→new blocks in `proposed-record-changes.md`.
  - Do not write to any other open branch: PR #19 effective argmax, #20 Lebesgue follow-ups, #21 literature, #22 nn-MOP IEP.
- Novelty gate (relaxed scan, WORKFLOW) before each new mechanism. Record the closest entries (at least IDEA-210–227 and the obstruction rows behind PD-N044–053), the applicable obstructions and which hypotheses the idea breaks, the verdict and the cheapest test.
- Provisional IDs: `PD-T?mz2d-frontier-codex-NN`, and likewise for PD-N, IDEA and LIT.
  - When the draft PR opens, reserve final ranges by the fresh-range procedure: main, every open PR (#19–#22 at writing), retired reservations and the batch ledger, with headroom.
  - The parallel Lanczos frontier branch `codex/padua-lanczos-frontier-20261105` reserves its own ranges; coordinate through the ledger and do not overlap.
- Statuses follow AGENTS.md:
  - Float spectra, fits and localization profiles are MEASURED.
  - A computer-assisted PROVED claim needs a written proved reduction, exact or outward-rounded arithmetic, committed producer and checker code, small evidence, and an independent rerun by a different subagent.
  - Do not combine a lower-only estimate with an unspecified upper norm to claim η < 1.
  - Finite certified ranges never prove an all-m quantifier without the asymptotic part.
- Storage (WORKFLOW, PR #18): commit code and small evidence (normally under 16 KiB per file). Regenerable or large outputs (eigenvectors, certificates, sweeps) go to cold storage via `tools/cold_storage.py`, with `cold-storage.json` and `COLD_STORAGE.md`, under `Downloads\padua\cold_storage\padua-mz-2d-frontier-20261105\`. Hand them to AC.
- Literature:
  - You may open any public page holding relevant literature. Cite a source only after reading its fulltext, and record LIT entries.
  - List unreachable fulltexts for AC with clickable DOI and journal links.
  - Never commit third-party PDFs or fulltext extracts (the repo is public). Do not bypass captchas or bot checks.
- Compute only in your sandbox. Ask AC before using NTNU servers (syvert0/1/2) or any other machine.
- Commits are authored as Andrey Chesnokov <aacchhee@gmail.com>, with trailers `Agent: Codex` and `Model: <exact model and effort>`. Never commit to main, merge, force-push, create tags or touch .github/. Only AC merges.

## Acceptance and outputs

- `LOG.md` with an entry per gate and target boundary.
- `plan.md`, written before the first run, with time boxes.
- `gates.md` with G0–G5 verdicts against the criteria above.
- `attempts/F1…F4.md`.
- `theory/` records in THEORY-template form, one per result (PROVED, PARTIAL, MEASURED or PD-N), with the 1-D PD-T027 work in its own records.
- `independent-checks*.md`, `evidence-manifest.json`, `results/padua-mz-2d-frontier-20261105.md` (kept current) and `report.md` at the end.
- Push at every gate and target boundary, and at least every ~10 minutes while something has changed.
- Open a draft PR to main early, with WORK / AUDIT (PENDING) / PR sections and the ID reservation.
- The report contains:
  - G0–G5 verdicts;
  - F1–F4 status with record links;
  - the certified finite range and its cost curve;
  - the measured scaling verdicts;
  - any counterexample;
  - for each target, what is now OPEN and the exact next obligation;
  - a short "for the paper" paragraph: which statements could enter a 2-D signed-Padua MZ note, with exact dependencies.
- When done, commit the outputs. Then, in a following commit, set this status to `done in <sha>` and open handoff 02 for the audit by Claude, Opus 5.5 xhigh, which reads the complete state/IDEAS.md because this branch carries mechanism and novelty content. Reply to AC only with `Claude (Opus 5.5 xhigh): Continue codex/padua-mz-2d-frontier-20261105.`
