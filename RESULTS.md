# Padua research — results (merged view)

One section per topic. Each topic replaces only its own section, from its own `results/<topic-slug>.md`, at PR preparation and in its own PR (rule: `agents/WORKFLOW.md`). Earlier topics kept their results files on AC's computer; they are added here when their files are migrated.

## padua-mz-2d-20261101 — signed Padua MZ in two dimensions (PR #14, merged `e0d9e3d`, 2026-11-01)

- **Audit:** Claude audit-01 (Opus 5.5 xhigh) accepted the mathematics: 17 PROVED, 2 MEASURED, 3 OPEN. Response-01 fixed six record findings.
- **PROVED:**
  - Exact all-degree signed Padua aliases; the degree of exactness is precisely m (PD-T106).
  - A masked-tensor defect architecture of at most 160 terms (PD-T109).
  - Certified extreme-eigenvalue brackets at m=10/20/30/40 (PD-T107).
  - An m30 witness with η > 3/4 (PD-N044).
  - Corner weights negative for every m≥3, of size −(4 log m + O(1))/m⁴ (PD-T111).
  - Diamond-filter reconstruction (PD-T115).
  - Signed hyperinterpolation norm and reproduction degree (PD-T112/113); the endpoint operator reproduces only Π₁ (PD-N051).
  - Tensor-CC control with endpoint order log⁻² (PD-T117).
- **OPEN:**
  - λ_max < 2 for all m (PD-T110).
  - Positivity, endpoint order and η convergence for all m (PD-T028).
  - η(θ) < 1 at a fixed degree ratio (PD-T116).
  - A uniform operator norm (PD-T114).
- **Details:** [results/padua-mz-2d-20261101.md](results/padua-mz-2d-20261101.md)

## results-in-repo-20261101 — repository-only results tracking (PR #16, draft)

- **Rule (Codex audit-01 accepted it):**
  - Each topic keeps `results/<topic-slug>.md` in the repository.
  - This `RESULTS.md` is the merged view, updated in each topic's own PR.
  - All agent work must run from the cloud; AC's machine is only for unfetchable papers and cold storage.
- **Response:** response-01 corrected the migrated PR14 summary (audit F1–F3).
- **Details:** [results/results-in-repo-20261101.md](results/results-in-repo-20261101.md)

## padua-lanczos-drift-20261101 — finite-precision span drift in bivariate Lanczos (PR #15, draft)

- **Audits:** Claude audit-01 and Codex audits 02–04. Audit-04 accepted the final response; no PROVED or MEASURED claim was refuted.
- **PROVED:**
  - PD-T144: for the named Padua certificate, ρ_n = O(n⁻⁵), limsup n⁵ρ_n ≤ 20√2π⁴/9 (sharper ≈ 219.5). This splits PD-T075(U1); PD-T075 is now PARTIAL.
  - PD-T145: an explicit square-case √ε family (reading (E)).
  - PD-T136/137: the normal-quotient span derivative and rational certificates.
  - PD-T138: the formal scalar-CGS2 normal map.
  - PD-T139: the finite aggregate separation, κ ratio > 1126 on T24 and > 11.72 on rotated Q24.
  - PD-T141: the finite formal scalar separation, > 800 on T24 and > 7 on rotQ24 (thresholds post hoc).
  - PD-T142/143: a computed-polynomial span certificate and a fixed-degree selection criterion.
  - PD-N062: a fixed-degree closure lemma; projection-only rules cannot remove the drift.
  - PD-N063: three failed Padua witness paths.
- **MEASURED:**
  - PD-T140: the scalar experiment. Its factor-ten target is PARTIAL (T24 proved, rotQ24 OPEN).
  - PD-T146: public polyrat V+A span gaps of 0.0041 and 0.0102 at near-machine orthogonality.
- **OPEN:** all-degree drift, general staircase safety, PD-T055, PD-T075(U2) and PD-T056(G). Formal-model results imply no IEEE claim.
- **IDs:** PD-T136–146, PD-N062–063, IDEA-246–267.
- **Details:** [results/padua-lanczos-drift-20261101.md](results/padua-lanczos-drift-20261101.md)
