# MZ prior-art and fulltext closure (CC / Padua MZ manuscript)

- Branch: `claude/mz-prior-art-20261101` · Base: main `9739a0c56b7a3976422ce60a8441bfbbfd6554df` · Developer: Claude (orchestrator) · Auditor: Codex `gpt-6-astra`, high (audit-01: CHANGES REQUIRED)
- Stage: AUDIT (narrow re-audit of response-02) · Next: `Codex gpt-6-astra, high: narrow re-audit of response-02 on claude/mz-prior-art-20261101 (PR #11)`.
- Claims: none new. Literature topic only; no PD-T/PD-N status changes (literature verdicts never change a PD status).
- For the PR: record updates for LIT-045–065; new LIT-293–299 (after the bivariate-Lanczos block LIT-066–292) reserved in the shared ledger; manuscript §1/§4/Prop. 5.1 wording and refs.bib; literature INDEX/CORPUS; topics/mz-constants/literature-search.md.
- Open for AC: missing fulltexts (see local working track `Downloads\padua\results\mz-prior-art-20261101.md`).

## 2026-11-01 — Claude, Opus 5.5 (orchestrator)

- Rules read at `9739a0c56b7a3976422ce60a8441bfbbfd6554df` (AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md). Role: orchestrator and literature developer.
- Task prompt: AC's "New topic: MZ prior-art and fulltext closure" (first copy truncated in Step 3; AC supplied the complete copy at 09:38).
- Read first: topics/mz-constants/POST_MERGE.md, report.md, literature-search.md, literature-response-01.md; all literature/records/mz-*.md; manuscript §1 related-work paragraph and refs.bib; PROOF_STATUS rows PD-T013–PD-T028, PD-N004; batch ledger.
- ID reconciliation: open PR #6 (programme-ideas, draft) and branches codex/padua-proof-attempts-20261101 (967131d), claude/programme-ideas-20261031 (0ef90ed), claude/bivariate-lanczos-20261031 (cf01449), claude/results-track-rule-20261101 (6eeec5b) mention only the next-free IDs PD-T029, PD-N007, LIT-066, IDEA-077; none reserves beyond them. No allocation made yet.
- Novelty gate: not applicable to new mechanisms — this topic generates no candidate, mechanism or theorem. It makes priority/attribution statements, so the audit must read the complete state/IDEAS.md.

### Step 1 — local inventory (orchestrator, directly)

- `Downloads\padua\papers`: 16 PDFs, each identified by first-page text (staged to the session workspace only): EGK 1991 SIMAX; Barrio–Peña–Sauer JAT 2010; Meurant et al. JCAM 2019 (disk points); Bartels–Jezioranski TOMS; Huhtanen–Larsen BIT 2002; Sommariva–Vianello NFAO 2015; Harris–Simanek PAMS 2021; Xu SIMA 1994; two SIMAX 2002 Lanczos/normal-matrix papers; Cools–Poppe BIT 2011; Sauer NA 2007; Van Barel–Chesnokov NA 2010; Marco–Martínez–Viaña NA 2019; Humet thesis; Mach–Van Barel–Vandebril TW629. **None is on the MZ target list.**
- `Downloads\bttb\papers` (access granted by AC's prompt; listed by filename only): ~250 Toeplitz/algebra PDFs. No filename matches any target DOI (BF01398509, BF01403676, BF01889904, S0002-9947-1984-0732113-4, 0518041, s003659900123, s003659910002, S000497270001025X, S0002-9947-1966-0187099-X, S0002-9939-1966-0189237-7, 0731079, jath.1993.1019, 0021-9045(90)90065-X). Not opened.

### Step 2 — target verification (done)

- Three Sonnet 5.5 high literature-verification workers (metadata + legal access only, no repo writes): group A (Nevai III/addendum, Askey 1972, Lubinsky 147, Erdős–Feldheim preceding note, LMN 1987, Mastroianni–Totik 2000, Lubinsky survey); group B (Sloan–Smith 1978/1980 and companions, Smith 1986, Mastroianni–Milovanović, Mastroianni–Russo, Xu I/II, Widom, Widom–Wilf, Don–Gottlieb); group C (ASV published, An–Wu published/corrections, An–Sommariva–Xue, forward citations 2010–2026).

- Worker results (scratchpad reports; not committed, since they contain only metadata and queries). Group A: Nevai III free AMS PDF has a text layer; the preceding Erdős–Feldheim note is Feldheim alone, C. R. 203, 650–652; Nevai 1990's Crossref title has no "Addendum". Group B: verified DOIs for Xu II (10.1006/jath.1994.1006), Mastroianni–Russo 1999 (10.1007/s003659900107), Sloan–Smith 1982 (10.1137/0719027) and Smith–Sloan 1980 (10.1137/0717001); found the Don–Gottlieb ICASE report on NTRS. Group C: ASV published DOI 10.1016/j.matcom.2026.10.001 (not OA); An–Sommariva–Xue not public; no An–Wu correction found; forward-citation screen via Semantic Scholar (An–Wu 24, Sloan–Smith 67, partial Nevai III 244, ASV 0). Each worker issued 20–30 literal queries; the lists are in the worker reports. Incident: one group-C OpenAlex request included AC's email as a `mailto=` parameter; it failed, was not repeated, and was reported to AC.
- Access correction to the worker classifications: the workers marked Askey, Mastroianni–Totik and the Lubinsky survey "not reachable", but all three were read through AC's NTNU access in AC's built-in browser.

### Step 3 — deliverable to AC (done ~10:00)

Missing-fulltexts table sent by message and written to `Downloads\padua\results\mz-prior-art-20261101.md` (new file, no prior bytes).

### Step 4 — reading and comparison (done for the reachable set)

- Access: Springer/Cambridge PDFs fetched in AC's built-in browser with AC's NTNU access (AC authorized all literature downloads, 09:40 and 09:49). Text was extracted in-page with pdf.js (cdnjs 4.0.379) and read in the session only. AMS/arXiv/NTRS/MDPI texts were read through WebFetch extraction, which is paraphrase-level and flagged in the records. ScienceDirect, SIAM and the AMS HTML pages loop on bot checks in the automated browser; no attempt was made to solve them.
- Wrote translation.md (T1–T5), comparison.md, report.md. Records updated: mz-sloan-smith, mz-mean-convergence-screen, mz-classical-mz-screen, mz-mastroianni-milovanovic, mz-an-wu, mz-widom, mz-don-gottlieb, mz-an-sommariva-vianello, mz-passi-cv; new record mz-prior-art-2026-additions (LIT-293–295).

### Step 5 — integration

- Manuscript: status line, abstract last sentence, §1 related-work paragraph, opening of §4, remark after Proposition 5.1; refs.bib notes, plus LIT-058 and LIT-293–295 entries. Compiled cleanly (16 pp.). No PD status changed.
- Ledger: bivariate-Lanczos branch `a2dd845` already holds an AC-authorized block LIT-066–292 (plus PD-T029–080, PD-N007–031, IDEA-077–176) in its ledger copy. This branch therefore reserves LIT-293–295, with the reconciliation recorded in ALLOCATIONS.md. The provisional numbers LIT-066–068 used earlier on this branch were renumbered before any push of those files.
- No contact with ASV or other authors.

### Step 4b — AC-supplied fulltexts (10:00–10:20)

- Papers folder re-listed at the step boundary: AC added 0518041 (LMN 1987), 0717001 (Smith–Sloan 1980), 0719027 (Sloan–Smith 1982), 1-s2.0-002190459090065X (Nevai 1990), 1-s2.0-S0021904583710191 / -S0021904584710069 (Xu I / II, image-only scans), and 1-s2.0-S0378475426004416 (published ASV). Each was identified by its first page. They were staged to the session only and read with pdftotext; Xu I/II were OCR'd with tesseract at 300 dpi.
- Records updated; LIT-296–298 reserved (ledger: next LIT-299). Comparison, report, manuscript (§1 list: LMN forward bound, Xu borderline, later Sloan–Smith, published-ASV assessment) and refs.bib updated. Build: 17 pp., no warnings.
- Verdicts unchanged: no source gives the two-sided endpoint order, an all-N upper constant <2, or explicit fixed-ratio constants. LMN adds a classical *unspecified* uniform upper bound.

## Runs needed

None (literature topic; no computation planned).

## 2026-11-01 — Codex audit-01

Audited candidate/rules `4f937137f9baac5e51814964e6a83aeb2df38815`; main/base `9739a0c56b7a3976422ce60a8441bfbbfd6554df`. Allocation: Codex gpt-6-astra high; runtime-resolved model/effort is not independently exposed. Complete state/IDEAS.md read, including all obstruction/disposition tables. Three bounded independent source checks supplement the root audit.

**CHANGES REQUIRED; stage WORK.** [Audit-01](audit-01.md) records F1–F4 (T4 smoothing normalization, Sloan–Smith coverage overstatement, König–Nielsen parameter restriction, and scoped classical-attribution inference) plus N1–N4. No PD status or developer proof changed. Every comparison row has a coverage disposition; inaccessible primary bodies are not counted as independently verified.

Independent manuscript build: pdflatex/bibtex/pdflatex/pdflatex, 17 A4 pages, no final-pass warnings. LIT-293–298 is disjoint from PR #10's LIT-066–292 at `a2dd845b8a231e1b00733e1361e2a9ad3bad222f`; next LIT-299 after both reservations. Three shared-file text merges against base pass; this is not a full squash rehearsal. [Input manifest](audit-support/input-manifest.json) and three source checks preserve commands, identities, coverage and limits. No external author contact or merge.

Developer must answer all findings in response-01.md and submit material corrections for focused re-audit. AC's desktop working-results file was unavailable in this environment; delivery there remains pending, with this audit/log as the durable handoff. No shared local RESULTS.md write was attempted.

## 2026-11-01 — Claude, Opus 5.5 high: response-01

- Rules re-read at branch head `64c3c79` (identical to `9739a0c`). Audit-01 (Codex, CHANGES REQUIRED) is answered in [response-01.md](response-01.md); all of F1–F4 and N1–N4 are accepted.
- Material changes:
  - translation.md T2/T4/T5 corrected and **T6** added.
  - Mastroianni–Totik verdict downgraded to RELATED: its window lies inside half-exactness.
  - Sloan–Smith 1980 screened in full.
  - König–Nielsen exponent uses max(α,β).
  - F4 rescoped: the Gauss-node and same-weight sources are analogues only.
  - The audit lead Mastroianni–Milovanović–Notarangelo 2012 was read (LIT-299). Its Cor. 2.2 necessity part gives inf_N λ_−(N,N)=0 at the CC nodes on Π_N (qualitative, conditional).
  - Manuscript abstract/§1/§4/Prop. 5.1 remark revised; INDEX/CORPUS/refs/ledger updated (next LIT-300).
- No PD status change. Build: 17 pp., clean. Build products are outside Git.
- Sources read in this step: Sloan–Smith 1980 (AC's NTNU access, built-in browser) and the MMN 2012 author PDF (text layer plus p. 164 page image).
- Focused Codex re-audit requested (response-01, last section). Audit-01's note on AC's local results file: this developer session writes it via the device link (updated after this commit).

## 2026-11-01 — Codex audit-02, focused response-01 re-audit

Candidate/rules `41bbc231be4b5ccc7c3f92e5818a53b950ccc25f`; prior audit delivery `64c3c79b8fe2fac27645b181aab79e3206886d16`. Requested allocation Codex gpt-6-astra high; resolved runtime model/effort not independently exposed. Complete candidate state/IDEAS.md reread, including every obstruction/disposition table. Two bounded independent checks supplement the root audit.

**CHANGES REQUIRED; stage WORK.** [Audit-02](audit-02.md) accepts the T2/T4/T5 fixes, source-specific coverage wording, corrected König–Nielsen exponent, and the conditional T6 deduction. One new P2, R1: translation.md T6's scope and response-01 F4 item 3 incorrectly attribute the squared-log order to the single U witness. That witness gives an O(1/log N) upper bound and every-N vanishing; the harmonic witness and PD-T017/018 give the squared-log order. Minor precision notes remain. The manuscript's harmonic proof and all PD statuses are untouched.

Independent rebuild: 17 A4 pages, no final-pass warnings, and both source hashes match response-01. Selected source statements rechecked; source necessity proof and inaccessible historical pages remain explicitly unaudited. Support checks, input identities, commands and limits are in audit-support/response-01-*.

**Reservation confirmation requested by AC:** LIT-293–299 is reserved to this topic; next unreserved LIT-300, with PD-T081, PD-N032 and IDEA-177 unchanged. Main `21e620ba8b5f0e0706f3a8c6613517df04d9d469` has merged PR #10 and holds exactly LIT-001–292. No numbered collision with active PR #6 `3e0100f` or PR #12 `95ca473`; their old LIT-293 planning advice must be superseded before later allocation. No extra ID is allocated by this confirmation. Reconcile the merged main and preserve both ledger blocks before merge readiness; no main merge or full integration rehearsal was performed by this focused audit.

Next: Claude responds in response-02 and requests a narrow re-audit. AC's desktop local-results file remains unavailable here; audit delivery there is not claimed. No external contact or merge.

## 2026-11-01 — Claude, Opus 5.5 high: response-02

- Rules re-read at `97968d2` (unchanged). Audit-02 (R1 P2; E1, E2 P3) is answered in [response-02.md](response-02.md); all items accepted.
- R1: the single-U upper bound O(1/log N) and the every-N limit are separated from the squared-log order (PD-T018 upper bound, PD-T017 lower bound) in translation T6, response-01 (marked in place), comparison, report and manuscript §1.
- E1: the Christoffel scale is interior-only. E2: the INDEX LIT-063 cell is fixed.
- Merged main `a7e1234` (PRs #10 and #6) without conflicts. INDEX has 426 distinct LIT IDs, LIT-293–299 are intact, and the ledger pointers are refreshed (next PD-T101, PD-N044, IDEA-210, LIT-427).
- Manuscript rebuilt: 17 pp., clean. No PD status change.
- Narrow Codex re-audit requested.
