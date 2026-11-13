# Claude audit-06: focused audit of response-05 (handoff 34)

Review reports and auditor scripts: [audit-06/](audit-06/). Audit round 6, after [audit-05](audit-05.md) and
[response-05](response-05.md). Scope: the material response-05 changes only (the onset-reader allowlist and receipt schema, the
analytic optimization guard and runtime probes, the changed analytic explanations, the custody wording, source/layout);
unchanged components were not re-audited. This is **not** a readiness decision, waives nothing, and PR 27 stays a draft.
Only AC merges. Novelty exception: this is a delta audit of repairs to existing code and text with no new mechanism, theorem
or threshold, so the IDEAS read was omitted.

## Decision

**Accepted, with no BLOCKING and no MAJOR finding.** The three repairs and the changed explanations hold at the scopes the
records state:
- **E5-01** (reader allowlist) is accepted as *synthetic storage compatibility* evidence; **E5-02** (analytic optimization guard) and
  **E5-04** (runtime probe, finite and per process) are accepted at their stated scopes.
- **Mathematics** of every changed clause reconstructs (corrected rho >= pi − v at the omitted collisions, the restored reasons, the
  section 3.3 steps, the new numbered kernel form, all 60 base-value table entries).
- **Source/layout:** builds, correspondence, freeze and baseline separation, mutation controls, rename-scan alignment, bibliography,
  and all twelve equation-tag placements pass.
- **Disposition accuracy:** supported, except two rows that are only partly done (M5A-05, M5B-E6; see M6-01, M6-02).

**Still OPEN and not closed by this audit** (files absent, no claim made): the canonical `onset512-return-20261108.zip` run of the
repaired reader, the selected 320/384/458/510 I25 data checks and cross-archive comparisons, historical PDF bytes, the 632 MiB native
histories and their custody, the post-repair snapshot and DOI, and AC's decision on the global budget. A focused audit completion does
not close them.

Stage: no MAJOR remains. The remaining MINOR/EDITORIAL items include TeX edits (a new paired freeze) and an evidence-status wording
change (M6-03), so they return to development as one batch; the topic is **not** ready, because the open evidence, budget and
publication decisions above remain with AC.

| Verdict | Result |
|---|---|
| Mathematics (changed text) | **Accepted**; no error found |
| Evidence readers (E5-01, E5-02, E5-04) | **Accepted** at stated scope (synthetic storage compatibility; finite per-process probe) |
| Source, correspondence, baselines, layout | **Accepted** (58/152 pages, 19 statements, 86 numbered environments, 120 labels) |
| Dispositions of response-05 | **Supported** except M5A-05 and M5B-E6 partly |
| 320..510 evidence, I25 data checks, custody | **OPEN** (inputs absent) |

## Identity, rules and disclosures

- **Models.** Orchestrator `claude-sonnet-5-5` (the session model was switched with `/model`; the prompt named Opus 5.5 xhigh); all
  audit work by **three Claude Opus 5.5 subagents instructed at xhigh** (effective effort not exposed): E6, M6, B6; distinct from the
  Codex developers and reviewers. The supplementary Astra reviews were read as evidence, not as the required audit.
- **Rules** read at be9a831; AGENTS.md, agents/, templates/ byte-identical at the audited head.
- **Candidate.** `codex/padua-argmax-bridge-20261105` at `5b1a4942af498e60e9da4c8860c57cb4f67be4ef` (handoff input head
  `26ab08d3d64eb29420752d4318fdb34a8ccdbbd0`); code checkpoint `074c7da` (executable code at HEAD byte-identical to it; only the
  campaign README changed after); final paired TeX/Bib freeze `8937d3b723c09c004f49d3e565d0b02976713a37`, pointer update `26ab08d`
  (separate commit; no `.tex` or `.bib` changed after the freeze); previous freeze `ad908acb`. Main `b5388c25a2a5ccb8d0faf816ab87023cf347bcd3`.
- **Data used:** the original return (36,045,486 B, sha256 `b00fd57f…`) and authenticated `padua30.zip` (25,111,335 B, `aac08e5f…`) from
  audit-05; both data-only. The canonical onset-512 ZIP, I25 bundle, derivative/inventory/review ZIPs, historical PDFs and native histories
  were unavailable; AC does not know the I25 location and it was not asked again. No Syvert, no native campaign, no regeneration.

## Executed checks

Every consequential run was preregistered, ran once and was observed (`wait4`); outputs in fresh scratch paths.

| Review | What ran | Result |
|---|---|---|
| E6 | handoff-34 commands: `check_reader_repairs.py` (exit 0, PASS, **60 controls**, all 40 audit-05 controls still present, stdout identical to the supplementary reviewer's), `onset512_analytic/check.py` (exit 0; 10 of 11 fields equal the receipt, only the `python` version differs), `runtime_probe.py` (exit 0, 31 controls, 4 probes true); own 53 reader controls (16 carried over with the two producer-file cases now ACCEPT, 8 lock rejections, 20 receipt rejections, 6 diagnostics); a **real** `deduplicate` → `completed` → `export` → reader round-trip with no adapter on those functions (exported ZIP 11,502 members = 191 x 60 + 42; every unsampled case exactly 60 members; the repaired reader accepts 191 pairs / 382 proofs; the previous reader `5e25c8a4` rejects the same archive with `unregistered campaign member: out/.preserve.lock`); 9 falsified-copy optimization tests; an MXCSR challenge with a gcc helper; budget accounting | 23 observed runs, all as preregistered, 30.4 s CPU |
| M6 | exact/interval and numerical reconstruction of every changed clause; 60 base-value entries; kernel identities; `check.py` byte copy `-E -B` and `-O` | all reconstruct; about 15 s |
| B6 | fresh builds; correspondence helper (default, `--archival`), `check_baseline_controls.py`, own aux parser, nine mutation types, rename scans, tag crops and a geometry scan of all 87 tags, evidence index, budget recount | all pass; about 2 min |

## Findings: evidence and records

- **E6-01 (MINOR; fixed in place).** `zenodo-deposit/README.md` lines 366–372 still say the active freeze is ad908acb with 57/150-page PDFs (and
  line 385 calls ad908acb final); `MANIFEST.json.in`, both BUILD.md files and the LOG give 8937d3b and 58/152. A dated addendum is committed with this audit.
- **M6-04 (MINOR; fixed in place).** `manuscript-duplicate-dispositions-20261113.md` still claims rows C1 (line 9), C10 (line 18) and B5 (line 37) were
  retained; only the supplementary review got the dated correction audit-05 asked for. A dated note is committed with this audit.
- **E6-02 (NOTE).** The runtime probe does not detect DAZ alone (a subnormal operand times 2 gives 0x0 under DAZ, 0x2 normally); it detects FTZ,
  FTZ|DAZ, RD, RU, RZ, FTZ|DAZ|RZ and DAZ|RU. The probe is per process (a child started while the parent had FTZ|DAZ set reads the default `0x1fa0`),
  and the nextafter probe tests the library, not the floating-point mode. The J03/response-05/LOG/README wording matches this scope. Optional: add a
  subnormal-operand probe `[2^-1074]*[2]` or state it in J03.
- **E6-03 (NOTE).** Storage receipts are only internally consistent: their counts are not checked against the pass's `S-build.json`; a false but consistent
  receipt is accepted. The records claim only "consistent counts" and the receipt is not part of the proof.
- **E6-04 (NOTE).** The committed regression has no misplaced lock/receipt controls and does not exercise the deps branch of `deduplicate`; the campaign README's
  adapter list omits the root/release/script relocation; any file name is accepted inside sampled `check-*` directories (class of E5-06).
- **E6-05 (NOTE).** The audit-05 dated E5-08 addendum in the campaign README was replaced rather than superseded; no information needed for verification is lost.
- **E6-06 / B6-03 (EDITORIAL; not fixed in place, risk of corrupting SHAs).** New record text drops the space between words and numbers or SHAs
  ("Code checkpoint074c7da", "at58/152pages", "is3f903e62", "alone9,733,758bytes") in `pr-update-20261113.md`, `response-05.md`, the results file, BUILD/README
  sections, handoff 34, the deposit README and the LOG. Content is correct; a careful manual pass is better than an automated one.
- **B6-04..B6-09 (NOTE).** The one-entry incremental map is not committed (it is the last entry of the 33-entry map); the white box behind "p_n on rho <= 1"
  in Figure 2 hides a short segment of the line x + y = pi (no text crossed; B5-01 resolved); the repository URL in the data statements is not pinned and GitHub
  `main` does not yet contain this topic (the open snapshot/DOI item); the artifact mode's PASS message hard-codes "historical 48/162-page PDFs preserved"
  though it was not run; both texts say the receipt is "in"/"retained by" the reproducibility package, which is not deposited yet; the AI declaration still omits
  Claude Sonnet 5.5 and the draft marker reads 8 November (AC's).
- Carry-over: E5-05, E5-06, E5-07, E5-09 unchanged.

## Findings: manuscripts

All of these are TeX edits (new paired freeze) or evidence-status wording; none changes a claim, constant or threshold.

- **M6-01 (MINOR, both texts).** Bare `w` still denotes the row half-amplitude w_r, contradicting the companion's section 4.2 symbol table (line 1468, which assigns
  w = r·pi + b): companion comparison 2270–2274 (p. 84), paper 1006–1009 (p. 32). Write w_r. M5A-05 is therefore only partly done and the supplementary review missed this.
- **M6-02 (MINOR).** The paper points to "the expanded companion" (certification 413–416, p. 54) but never identifies or cites it; `\ref{sec:certificates}` resolves to the paper's own
  Section 5 and is right only because both documents share the section structure. Identify the companion in the data statement or bibliography and refer to it in plain text (M5B-E6 partly done).
- **M6-03 (MINOR, both texts; evidence-status wording, so material for review).** The new custody sentences use undefined project terms ("canonical onset-512 return archive",
  "evidence bundle", "data-only checks"; paper certification 505–517, companion 1624–1635); "the four witnesses at degrees 320, 384, 458 and 510" is ambiguous (the text counts two witnesses per
  degree) and degree 458 appears both as re-executed and as open; the text does not say plainly that Proposition 5.3 at 320..510 rests on recorded runs whose outputs cannot currently be re-examined.
- **B6-01 (EDITORIAL).** The new provenance sentence "Table 2 was computed with the exact interval routines of `code/onset512_analytic/check.py`" sets a stretched line (underfull badness 10000)
  at paper `comparison-unified.tex` 1873 (p. 42) and companion 4138 (p. 107); reword, use a breakable path, or move it to a table note. In the paper Table 2 floats to the top of p. 43 after the section 4.4 heading.
  **B6-02** the companion-only "Returning to the comparison outputs" array (`localization-unified.tex` 357–366, p. 107) has touching columns (`l@{\quad}l@{\quad}l`).
- **M6-05..M6-07 (EDITORIAL).** The `ul:charts` display ends with "." before "where" (paper localization 35; companion 97), use a comma; companion corner 1203 "Apply the cell bound just proved" should cite
  the midpoint bound of Lemma cu:quadrature (line 944); paper comparison 1004–1006 "Its normalized |Xi_j| <= ..." has no verb; Prop 5.3 "both recorded certificate records" is redundant.
- **M6-08..M6-11 (NOTE).** The cosine-cancellation clause is correct but terse; rename-map entries 2 and 9 also match the kernel polynomial P_n(cos .), including one occurrence inside numbered (25), and the sources
  correctly leave those alone; remaining local reuses (tau as Q_tau subscript, chi, bare eta, vartheta_m vs vartheta) and the paper still lacks the amplitude-phase reason at 588; no committed command reproduces the
  60 table values (`check.py` returns 8 of the 15 quantities; the rest are composed ad hoc).

## What was reconstructed (summary)

- **Collision clause.** n(u ∓ v_r)/(2pi) ≡ 1/2 + (x ∓ y ± v_r)/(2pi); on left rows a collision needs x − y = pi − v, on right rows y − x = pi − v, or x + y = pi − v in the eta_+ channel, so in every case
  rho >= pi − v and a <= (P/2) tan(v/2) <= Pv/2. On non-retained rows (r = 2m − 3, 2m − 7) |x − y| is 2.07, 2.29, 2.32 against pi − v of 2.87, 3.09, 3.12 at n = 32, 192, 512: the old clause is false there, the corrected one
  holds; a randomized test found 2,940 actual collisions with 0 violations and 600 rows with rho < pi − v had none.
- **Restored reasons** (prefactor 2a tau(v/2)/(pi^2 nu) = a cot(v/2)/(pi m), wrap cost 8P/(3 pi m (j−1)) summing to 16 P H_n/(3 pi n), primitive 4a log sin(t/2), amplitude-phase minimum 3.2323 > 3, |N_s| <= 2 <= 8, pole
  decomposition 6 + pi²/24 + 1/pi = 6.7295 < 7), section 3.3 (trapezoid 1/(8z²), psi(y/2) = psi(1 + y/2) − 2/y giving A_1(0) = pi − a d_0, |psi'(r + 1/2) − 1/r| <= 1/(3 r³)), the corner-lemma and Cor 4.6 clauses; all
  60 base-value entries contain the true value and are the tightest 6-decimal outward enclosures (paper and companion tables identical); the new equation (25) is the former inline divided-difference form and equals the
  angular-kernel definition (7) and the sine-ratio product form including collisions (error <= 3e-29 for n = 1..9); Lemma 5.1 is byte-identical to ad908acb; Prop 5.3 changes only "retained" to "recorded"; the nine changed
  numbered or statement blocks are identical in both texts; the 33-entry rename map preserves meaning (the `h_m` to `vartheta_m` rename is not permissive: every `h_m` at ad908acb was the cell width pi/m).

## Disposition accuracy (response-05)

Rows M5A-01..04, 06..10, M5B-01..05, 07, M5B-E1..E5, B5-03, B5-04, B5-10 and the response-04 corrections section are supported. M5A-05 and M5B-E6 are only partly supported (M6-01, M6-02). The B5-02 tags (twelve
placements: equations (11), (20), (26), (40), (51), (55) at paper pages 9/14/16/23/26/28 and companion 24/39/47/64/71/74) were inspected in the rendered PDFs, not inferred from overfull-box logs.

## Budget and custody (for AC)

Reproduced exactly: main alone 9,733,758 B; this topic's classified share 2,000,636 B; union 11,734,394 B; with the 2,087 B `FREEZE.md` exception 11,736,481 B; conservative no-shrink bound 11,756,141 B (+4,832 B since audit-05: the
new `notation-renames-audit05.json` 3,749 B and `MANIFEST.json.in` +1,083 B, no shrink). The 10 MB cap is not met by the union; neither branch alone exceeded it. Outside the topic directory only `results/padua-argmax-bridge-20261105.md` differs from main;
`COLD_STORAGE.md` and `cold-storage.json` are unchanged and no destination, URL or DOI was invented. The cap, storage and share disposition remains AC's.

## Auditor in-place MINOR fixes (third-and-later round rule)

Dated addenda only, committed separately from this report: (1) `zenodo-deposit/README.md` (end): E6-01, active freeze is 8937d3b (58/152 pages), ad908acb historical; (2) `manuscript-duplicate-dispositions-20261113.md`
(end): M6-04, rows C1, C10 and B5 were not retained by the old freeze. Not fixed in place: every TeX edit, M6-03 (evidence status), E6-02..E6-04 (code/recipe scope), the word-number spacing in the records (E6-06).

## Limits

Absent files: canonical onset-512 ZIP (`da63280a…`), I25 bundle (`d1d03156…`), derivative/inventory/review ZIPs, historical PDFs, native histories. Every positive result for the onset reader uses adapters; there is no real-checker positive for 320..510 and the member-count
and identity-rule conclusions rest on derivation and analogy (only the canonical run can rule out an unknown extra top-level file). The MXCSR controls cover one thread on this machine (Python 3.13.18, NumPy 2.5.3). The compact verifier was not rerun (with `--package`
it imports `checker.py` from inside `padua30.zip`, which is archive code); `git diff 33b9eca..HEAD` is empty for `compact_pack`, the engine, the audit-03 suite and the I25 checker, so audit-05's results stand. Crossref and mathnet are blocked from this session
(the Pimenova Math-Net ID remains unchecked).

## Next step

Codex: one paired wording batch (new freeze, `FINAL_BASELINE` update in a separate commit, rebuild, correspondence and mutation controls, focused re-check) covering M6-01, M6-02, M6-03, M6-05..07, B6-01, B6-02 and the editorial items, plus the optional E6-02 probe and E6-04 regression additions. AC: the open decisions listed
above (canonical ZIP and I25 bundle or confirmation they are lost, native-history custody, the post-repair snapshot and DOI, the global budget, the AI declaration and draft marker). No readiness while these remain.

2026-11-13 · orchestrator `claude-sonnet-5-5`; audit work by three Claude Opus 5.5 subagents (instructed xhigh) · rules read at be9a831, unchanged at 5b1a494.
