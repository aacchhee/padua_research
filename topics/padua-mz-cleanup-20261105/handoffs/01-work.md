# Handoff 01 — padua-mz-cleanup-20261105 — MZ cleanup: certified finite witness, odd m, growth constants, manuscript integration

- Status: done in 10898ad99882248e5e6f9d76641624146af97454
- Previous handoff: none (new topic; the parent campaign is `topics/padua-mz-2d-frontier-20261105/`, merged as PR #23)

- Next agent / model / effort: Codex. Mathematics: gpt-6.1-sol xhigh. Code, witness certification, scans and manuscript LaTeX: gpt-6.1-sol medium. Supplementary independent checks: gpt-6-astra high.
- Role: orchestrator and developer
- Branch: codex/padua-mz-cleanup-20261105
- Input head SHA: `21dbfc90257b952d8923f6d01739d12aa8d6e0a1` (main, PR #23 merged; this branch adds only this handoff, LOG and the results stub)
- Main / base: `21dbfc9`
- Stage: WORK
- Written by / date: Claude, claude-opus-5-5 · 2026-11-05

## Context

PR #23 settled the signed Padua MZ questions in the negative, while proving a positive uniform norm:

- **PD-T295:** fixed-node weight asymptotics along even m, m⁴ w_jk / log m → −16 e_j e_k (−1)^j.
- **PD-N105:** a negative polynomial carrier with Q(p²)/log m → −16ab/9 (a, b > 0, a + b < 1/2), so λ_min(m, m−1) → −∞ along even m.
- **PD-N106:** a positive carrier with Q(p²)/log m → 8ab/9 (2a + b < 1/2), so λ_max → +∞ along even m.
- **PD-N107:** half-exactness is the sharp threshold. At every fixed ratio 1/2 < θ < 1 the extrema diverge.
- **PD-T297:** 2 ≤ ‖H_{m,n}‖_{C→L²} ≤ 28.3763… for all m ≥ 2 and 0 ≤ n < m.
- **PD-T296:** a positive-reference smooth diamond theorem.
- **PD-T298/299:** certified strict brackets at m = 60 and 80.
- **PD-T300:** finite MEASURED observations.

PD-T028/110/116 keep AC's registry status OPEN with binding REJECTED: refuted dispositions.

The report left these items as separate open tasks:
- constructive finite thresholds;
- exact certification of the m = 1600 float hit;
- sharp growth constants;
- odd-m behaviour;
- the 1-D PD-T027;
- adoption of the new results by the MZ manuscript (`tracks/mz-constants/paper/manuscript.tex`). Its section 6 still says only "an exact Padua compression", and PAPER_MAP still lists "no 2D upper theorem".

This topic is the cleanup: bounded, concrete tasks that turn the PR #23 results into finished, citable statements and a manuscript section.

**One fact that steers C1 and C3.** These are Claude's arithmetic on the merged PD-T300 minimum-only screen (even m, n = m−1); this is a post-hoc 4-point fit, MEASURED only, and steers effort without being a premise.
- The values are λ_min = 0.0400, 0.0197, 0.0030 and −0.0234 at m = 800, 1000, 1200 and 1600.
- They fit λ_min ≈ 0.6519 − 0.09153·log m with residuals below 4e-5.
- That predicts the first even crossing near m ≈ 1240.
- The slope −0.0915 is close to the carrier supremum: sup 16ab/9 over a + b < 1/2 is 1/9 ≈ 0.111.
- So the m = 1600 hit is plausibly the same logarithmic branch as PD-N105, with a modest constant term. That contradicts the report's reading that the carriers only "take hold" around log m ≈ 55: that figure concerns particular carriers, not the true minimizer.

## Targets (priority order)

### C1 — certified finite failure of positive definiteness. Box: about 6 h.

1. **Certify λ_min(1600, 1599) < 0.**
   - Regenerate the saved minimizing vector from committed code. The tmp file is gone, but `evidence/g1-minimum-only.json` and PD-T300 record the command and SHA-256.
   - Round it to a vector p with rational or dyadic coefficients in the Legendre (or Chebyshev) basis.
   - Prove Q_m(p²) < 0 rigorously, with ∫p² > 0 computed exactly. Enclose Q_m(p²) = Σ w_z p(z)² with outward-rounded ball arithmetic (Arb/FLINT, or MPFR with directed rounding). Use the exact weight formula of PD-T106/definitions, evaluated in balls, and rigorous enclosures of p at the 1,282,401 nodes, through Clenshaw in balls or a DCT with an a-posteriori error bound.
   - A single strictly negative enclosure is the certificate. No eigen-solver output is a premise.
   - An independent subagent checks it on its own arithmetic path: a different evaluation scheme, or exact rational weights with interval nodes.
2. **Locate the first even crossing.**
   - Float-scan λ_min(m, m−1) for even m from 1100 to 1400 (matrix-free solver of PR #23), coarse first and then every even m near the crossing.
   - Certify a negative witness, as in step 1, at the smallest even m found negative. Record the largest scanned m with a positive float minimum.
   - Certified positivity at m ≈ 1240 is out of reach (dimension about 7.7×10⁵). Say so: "smallest even m with a certified negative witness" is PROVED, while "first crossing" is MEASURED.
3. **Odd m in the same window.** Scan odd m from 1101 to 1601 (float). The result is a MEASURED statement about whether the branch exists for odd m.

- **Done:** a PROVED finite theorem "the signed Padua Gram form on Π_{m−1} is indefinite at m = m₁ (and at 1600)", with an independent check, plus MEASURED scan records.
- **Kill:** if the rounded witness's enclosure straddles 0 after two precision doublings, record the obstruction. The enclosure width should be far below |λ_min| ≈ 0.023 relative to ∫p², so a straddle would be a scaling or convention bug; check against PD-T298 at m = 60 first.

### C2 — odd m. Box: about 6 h.

- **Goal:** extend PD-T295 to odd m, giving the fixed-node weight asymptotics m⁴ w_jk / log m along odd m with their sign pattern. The node grid and checkerboard parity change with m mod 2; recheck PD-T111's corner weights in both parities.
- Then decide whether odd-m analogues of the PD-N105/106 carriers exist, so that λ_min → −∞ and/or λ_max → +∞ along odd m.
- **Done:** PROVED odd-m weight theorem and carriers (or a proof that the odd-m signs prevent one of the divergences), giving a complete classification of both extrema for all m → ∞. Alternatively, a precise PARTIAL.
- Cross-check against C1 step 3.

### C3 — sharp growth constants. Box: about 8 h; stretch.

- **Goal:** determine lim λ_min(m, m−1)/log m and lim λ_max(m, m−1)/log m along even m (and odd m after C2), or the best proved bounds.
  - Carrier lower bounds: λ_min/log m ≤ −1/9 + o(1) and λ_max/log m ≥ 1/36 + o(1). The latter is sup 8ab/9 over 2a + b < 1/2 at a = 1/8, b = 1/4. **Verify these optima.**
  - Matching upper bounds need control of the negative (respectively positive) nodal mass near the corners: PD-T295's majorant plus a sharp localization estimate.
- First run the cheap test: does the measured slope −0.0915 move toward −1/9 when the C1 scan is extended to m = 2000–3000 (float, minimum only)? Pre-register the comparison in `gates.md` before running it.
- **Done:** PROVED limits; or PROVED two-sided bounds with explicit constants; or the carrier bounds as the only proved side, with the measured slope recorded.

### C4 — manuscript integration. Box: about 6 h; starts after C1 and C2, or in parallel on the already accepted results.

Revise `tracks/mz-constants/paper/manuscript.tex` and `refs.bib` on this branch:

- **Replace section 6** ("An exact Padua compression") by a section on signed Padua rules beyond half-exactness. Keep PD-T021's compression theorem, and add:
  - the weight asymptotics (PD-T295);
  - the two carrier countersequences and the sharp half-degree threshold (PD-N105–107);
  - the uniform C→L² norm (PD-T297);
  - the C1 certified witness and C2/C3 results at their final status;
  - finite PD-T298/299 as illustrations.
- **Then update the rest:**
  - abstract, introduction and section 7 ("Finite observations and unresolved sharpenings"), with PD-T020, PD-T027 and the remaining 2-D items as open problems;
  - the positive-reference PD-T296, only if it fits the paper's line, as a remark.
- **Constraints:**
  - Use only final IDs in comments.
  - Make no claim beyond each record's accepted scope.
  - Make no historical priority claim beyond what `literature/INDEX.md` on main supports. The PR #21 literature comparison (unmerged) may be read; its new LIT entries can be cited only after it merges. Otherwise mark the sentence `% LIT pending PR21` for a later pass.
- Build the PDF in the sandbox to check compilation. Do not commit the PDF; record the build command and page count. Keep the existing preserved v1 and response-01 PDFs untouched.
- Update `tracks/mz-constants/paper/README.md` (scope table) and the `topics/mz-constants/directions/M7/manuscript-record.md` history entry.

### C5 — housekeeping. Box: about 2 h.

- **Cold storage:** list the pending cold-storage deliveries for PR #14 and PR #23 (`COLD_STORAGE.md` in both topics). Stage what is regenerable under `Downloads\padua\cold_storage\padua-mz-cleanup-20261105\`, including the C1 witness vector and its enclosure receipt, and hand the list to AC with sizes and SHA-256 values. Do not claim delivery.
- **Literal old→new blocks in `proposed-record-changes.md`** for:
  - the PAPER_MAP MZ manuscript row: drop "no 2D upper theorem" and state the new 2-D content;
  - the state/CURRENT.md MZ section;
  - track README pointers.

  Apply them at PR preparation as the shared-file rule requires.

## Optional

### C6 — PD-T027, the 1-D sharp endpoint upper limit. Box: about 4 h; only after C1–C4.

- One bounded round on the sharp Clenshaw–Curtis upper limit and uniform gap. PR #23's PD-N104 and the harmonic boundary escape PD-T294 show which intermediaries fail.
- Record the obstacle if the round does not close.

## Gates (kill criteria written here, before any run)

If a criterion proves ill-posed, record why and add a new criterion as a separate dated entry; never edit the original.

- **K0, replay.** Reproduce the PD-T300 minimum at m = 800 and the PD-T298 m = 60 bracket from committed code. **Kill:** mismatch beyond 1e-10 (float) or outside the bracket.
- **K1, witness feasibility.** At m = 400, certify the sign of Q(p²) for the rounded float minimizer (positive there) and report the enclosure width relative to |Q(p²)|. **Pass:** width ≤ 1e-6 of |Q(p²)| at under 10 min. Otherwise redesign the evaluation before m = 1600.
- **K2, C3 pre-registration.** Before any m > 1600 run, write the scan grid, the fit rule (least squares in log m over a declared window) and the decision rule "the slope moves toward −1/9 when the window rises" in `gates.md`.

## Read first

- AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md at the branch head.
- `topics/padua-mz-2d-frontier-20261105/`:
  - report.md;
  - theory/ (all files, above all f12-local-weight-asymptotic.md, f12-eventual-negative-carrier.md, f12-eventual-upper-carrier.md, f3-fixed-ratio-threshold.md, f4-uniform-density-bound.md, frontier-measurements.md);
  - numerical-results.md and certifier-results.md;
  - audit-01.md (incl. A2 and audit-01-support/) and response-01.md;
  - code/ (g1_minimum.py, g1_spectral.py, cert_*);
  - COLD_STORAGE.md.
- `topics/padua-mz-2d-20261101/definitions.md`: fixed conventions; do not change them.
- `tracks/mz-constants/paper/`: README.md, manuscript.tex, refs.bib. Also `topics/mz-constants/directions/M7/manuscript-record.md`.
- PROOF_STATUS rows PD-T013–T028, PD-T106–T117, PD-T294–T300, PD-N044–N053 and PD-N104–N107. IDEAS entries IDEA-210–227 and 384–397. PAPER_MAP (MZ rows) and state/CURRENT.md (signed Padua section).
- literature/INDEX.md. The PR #21 P2 comparison is readable with `git show origin/claude/padua-literature-20261103:topics/padua-literature-20261103/p2-comparison.md` (unmerged).

## Scope limits

- **Where to write.**
  - Inside `topics/padua-mz-cleanup-20261105/` and `results/padua-mz-cleanup-20261105.md`.
  - For C4 only: also `tracks/mz-constants/paper/manuscript.tex`, `refs.bib` and `README.md`, and `topics/mz-constants/directions/M7/manuscript-record.md` (append only).
  - Do not edit any other merged topic, theory, code or registry file. Import or copy frozen code instead. Put shared-record changes as literal old→new blocks in `proposed-record-changes.md`.
  - Do not write to any other open branch: PRs #21, #22 and #24, `codex/padua-argmax-effective-2-20261105`, and any later ones.
- **Novelty gate** (relaxed scan, WORKFLOW) before each new mechanism in C2/C3/C6. Record the closest entries (IDEA-210–227 and 384–397, and the obstruction rows behind PD-N044–053 and PD-N104), the verdict and the cheapest test.
- **Provisional IDs:** `PD-T?mz-cleanup-codex-NN`, and likewise for PD-N, IDEA and LIT. When the draft PR opens, reserve final ranges by the fresh-range procedure, with headroom: main, every open PR (#21, #22, #24 at writing), the argmax phase-2 branch, retired reservations and the batch ledger.
- **Statuses** follow AGENTS.md.
  - Float scans and fits are MEASURED.
  - The C1 witness is PROVED only with a written reduction (Q_m(p²) < 0 and ∫p² > 0 imply indefiniteness on Π_{m−1}), outward-rounded committed producer and checker code, small evidence, and an independent check by a different subagent on its own arithmetic path.
  - Never infer a constant from a fit.
- **Storage** (WORKFLOW, PR #18): commit code and small evidence, normally under 16 KiB per file. Vectors, node values and scans go to cold storage via `tools/cold_storage.py`, with `cold-storage.json` and `COLD_STORAGE.md`.
- **Compute.**
  - In the sandbox only: up to 4 h wall per run, and about 24 h of cumulative CPU. AC may change these.
  - Do not use AC's NTNU servers (syvert0/1/2) or any other machine without asking AC in the chat. If more is needed, stop at a checkpoint and ask, giving commands and projected times.
- **Literature.**
  - You may open any public page holding relevant literature. Cite only after a fulltext read, and record LIT entries.
  - List unreachable fulltexts for AC with clickable DOI and journal links.
  - Never commit third-party PDFs or extracts (the repo is public). Do not bypass captchas or bot checks.
- **Commits** are authored as Andrey Chesnokov <aacchhee@gmail.com>, with trailers `Agent: Codex` and `Model: <exact model and effort>`. Never commit to main, merge, force-push, create tags or touch .github/. Only AC merges.

## Acceptance and outputs

- `LOG.md` with an entry per gate and target boundary.
- `plan.md`, written before the first run, with time boxes.
- `gates.md` with K0–K2 verdicts.
- `attempts/C1…C6.md`.
- `theory/` records in THEORY-template form, one per result, including the finite indefiniteness theorem and the odd-m results.
- `independent-checks*.md` and `evidence-manifest.json`.
- The C4 manuscript diff, with a short `manuscript-changes.md` listing every changed section and the record each new sentence rests on.
- `results/padua-mz-cleanup-20261105.md` (kept current) and `report.md` at the end.
- Push at every gate and target boundary, and at least every ~10 minutes while something has changed.
- Open a draft PR to main early, with WORK / AUDIT (PENDING) / PR sections and the ID reservation.
- The report contains:
  - K0–K2 verdicts;
  - C1–C6 status with record links;
  - the certified witness degrees and the measured crossing window;
  - the odd-m classification;
  - the growth-constant status;
  - the manuscript status (page count, what it now claims, what is marked pending PR #21);
  - the cold-storage list for AC.
- When done, commit the outputs. Then, in a following commit, set this status to `done in <sha>` and open handoff 02 for the audit by Claude, Opus 5.5 xhigh. That audit reads the complete state/IDEAS.md if C2/C3/C6 produced new mechanisms. Otherwise it records "novelty: not applicable" with the reason. Reply to AC only with `Claude (Opus 5.5 xhigh): Continue codex/padua-mz-cleanup-20261105.`
