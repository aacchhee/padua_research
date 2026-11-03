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

## padua-proof-attempts-2-20261101


Stage PR (prepared for AC review); Claude Opus 5.5 xhigh audit-01 accepted for the stated scope, with minor findings answered in response-01. [PR12](https://github.com/aacchhee/padua_research/pull/12) is prepared after merged PR15; only AC merges.

- A2 PROVED: requested corner b coefficient, explicit absolute remainder ≤ 68; local results 01–04.
- A5 certification item PARTIAL by degree: closed counts 15, 27, 25, 41, 50 for n = 3–7 and separate corner-only globals. Degree 8 has at least 44 strict interior maxima; exact counts/global remain OPEN. PD-T100's measured-search status stays MEASURED.
- A4(a) PROVED at its central-envelope scope: R_cen = Λ_c − g + o(1), both parities, 0.548504986190 < g < 0.548525055355; exact all-four-edge formula. Full-square A4 and global runner-up identification remain OPEN.
- PD-N072 PROVED; specified S(α) REJECTED: refuted on positive n = 1, p = 1/10, M = 4 sections. Count 1/2 differs from valid reference count 1 at the required square-root gap. Other counts/reference existence are not refuted.
- B1 PROVED for generic exterior parallel real diagonal poles, every fixed admissible sample/finite T; literal even-count Ldiag taper except finitely many parameters. Other classes, fixed parameters and stability remain OPEN.

[Full report, proofs and evidence](topics/padua-proof-attempts-2-20261101/report.md).
Next: Codex (gpt-6.1-sol medium): Continue codex/padua-proof-attempts-2-20261101. Only AC merges.

Final registration: PD-T156–197; PD-N072–073; IDEA-286–311. [Exact ID map](topics/padua-proof-attempts-2-20261101/COLD_STORAGE.md). Reservation gaps PD-T198–205, PD-N074–077, IDEA-312–315 remain permanent.

## cold-storage-20261102


Branch: `claude/cold-storage-20261102`. Finalized 2026-11-03; Stage PR, ready for AC's merge decision. Claude developed the cleanup/response; Codex (AC-requested/configured gpt-6-astra high) independently accepted [audit-02](topics/cold-storage-20261102/audit-02.md). Backend model/effort metadata is not separately exposed.

- **Cleanup.** 176 files, **15,846,089 bytes**, archived from nine topic/track directories. Git-measured batches: 163 / 15,418,937 bytes and 13 / 427,152 bytes. Every artifact retains its exact source commit/path/blob, size and SHA-256; all 176 identities verify. No mathematical claim, status or ID changes.
- **Retrieval.** Complete command/reader metadata and superseding human correction sections remain committed. The POSIX tool preflights collisions, protects tracked/local files, uses no-follow traversal, reads exported payloads back before issuing v2 receipts and verifies transferred archives without Git using `verify-archive DIR --manifest M`.
- **Validation.** 23 storage tests and 8 independently written fault controls pass; all nine manifests verify. Charter and track-MZ export/verify/clean cycles pass with 11 direct source-byte comparisons. Audit-01's three scientific outputs and historical patch remain byte-identically reproduced; audit-02 changes no science.
- **Integration.** PR #18 first. A disposable squash rehearsal against PR #17 reference head `cdb12257af24ea2542de707b9730f8278d69a168` finds two later conflicts, both shared tool files; keeping PR #18's audited versions resolves them and passes all 23 storage tests. PR #17's branch was not changed or declared ready here.
- **Separate archival work.** AC delivery is unconfirmed, native Windows is unsupported, WSL/drvfs is untested, and no history purge was performed. Current retrieval uses Git objects. A purge needs independently verified physical archives, preserved code/metadata and migrated locators; an export receipt alone is insufficient.

All assigned repository work is complete under AC's instruction to finalize without more Claude rounds. No further agent continuation is requested. [PR #18](https://github.com/aacchhee/padua_research/pull/18) is for AC alone to merge. [Log](topics/cold-storage-20261102/LOG.md) · [audit evidence](topics/cold-storage-20261102/audit-02/receipt.json).
