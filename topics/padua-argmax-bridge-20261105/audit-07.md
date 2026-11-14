# Claude audit-07: regenerated evidence and the public verification kit (handoff 37)

**Decision: accepted for the mathematics, the regenerated evidence and the public package's data and replays. One MAJOR finding (P7-01, a publication-coherence defect, no mathematical content) and three AC decisions keep the topic out of readiness.** No BLOCKING finding. No theorem statement, hypothesis, constant, range or threshold changed. The MAJOR finding is returned to Codex as one paired batch (handoff 38). The MINOR stale-record items below are fixed in place in a separate commit, as WORKFLOW requires from the third audit round.

## Identity and candidate

- Role: independent auditor of Codex development. Orchestrator: `claude-sonnet-5-5` (no scientific judgment delegated away: I made the classification and wrote this record). Review work: three independent Claude Opus 5.5 subagents, instructed at xhigh effort (the runtime does not expose the effort it applied): **E7** (regenerated evidence), **P7** (public ZIP), **M7** (manuscripts). Opus was chosen because the scope includes reconstruction of changed proof sentences and adversarial checks of a verifier; Sonnet orchestrated.
- Rules: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md` read at head `d6dd6730e5413a238f5c55630d0d907fb5e41563`; byte-identical to the versions read at `5b1a494` (no diff of `AGENTS.md` or `agents/` since).
- Candidate: branch head `d6dd6730e5413a238f5c55630d0d907fb5e41563` (outputs `d340d2e7…`, handoff-only commit `d6dd673`); TeX/Bib byte-identical to freeze `e861c752218fc0a6648d4a4a67fea616ba5cbdd1` (pointer `3e2805e`); public adapter source `77e4f1e73f59098ee280d9ed681a33d823e5e7aa`; scientific base `656c15b…`.
- Artifact: the **public ZIP supplied by AC in this session** (it is not in Git): 5,138,944 bytes, SHA256 `15885d34498b7f20c20f4b97453babfa85a09d46490dbcb14c051b429e2ee036`, recomputed by me and by P7; 1,019 files / 10,213,669 expanded bytes; `testzip` clean. It is the exact artifact the handoff names.
- Not reachable in this container (recorded, not re-examined): the 164,004,073-byte native-history archive, the 296 MB preservation archive, the I25 per-worker observation files, the 382 original regenerated inputs outside the ZIP, and `local-output/`. AC retired the historical-only artifacts; they are not requirements.
- Environment of my reruns: Python 3.13.18, NumPy 2.5.3, g++ 13.3.0, GMP 6.3.0, 4 cores. The reference environment was Python 3.12.14, NumPy 2.3.5, g++ 14.2, GMP 6.3. Every numerical result agreed; no environment effect was seen. This is a point in favour, not a conformance proof.

## What I did myself

Recomputed the ZIP hash and `testzip`, extracted it read-only for the reviewers, set the briefs and strict read-only rules (all work in scratch copies; the repository was unchanged by every reviewer), checked each load-bearing finding against the source (M7-01/E7-01/P7-01 in `paper/main.tex:84-93`, `companion-paper/main.tex:91-100`; M7-03 in `companion-paper/BUILD.md:28-34`), and classified.

## Executed checks (reviewer reports, full command lists with wait statuses in the linked files)

| Area | Result |
|---|---|
| ZIP census, P7's own checker (not `verify.py`) | PASS: 1,018 SHA256SUMS lines and 1,017 manifest hashes; 942 phase inputs n0041..n0511 × {produce, verify} (560 retained, 382 regenerated); 39 polynomial inputs byte-identical to Git HEAD; 942 expected rows; summaries equal recomputed counts/minima and the tracked RESULTS.json; 30 mapped sources and the checkers byte-identical to Git (32 with the PDFs); README.txt = README.md = Git source |
| Public `verify.py` as a new user | integrity PASS (0.24 CPU s); `python -O` refused before any PASS; README quick command verbatim PASS (34.1 CPU s); **degrees 100,192,256,295,320,384,500, both records each: 14/14 PASS** (56.7 CPU s); polynomial n=9 PASS and **n=33 PASS** (486 CPU s, peak 1.72 GB); `--controls` 27 corruptions rejected, 3 substitutions accepted; `--analytic` assertions and both 60-entry tables PASS. All wait statuses 0 except the deliberate `-O` refusal |
| Negative controls (31 on disposable copies) | rejected as intended: changed byte, missing/extra input, duplicate input, swapped inputs with only checksums refreshed, duplicate JSON key and NaN in inputs, traversal/duplicate checksum lines, symlinks, bad selections; **endpoints lowered in both records and a tampered expected row pass integrity but are rejected by the numerical replay of that degree**. Accepted (all stated or by design, see P7-03/P7-08/P7-09): a consistently refreshed SHA256SUMS+extra file; a produce/verify swap with refreshed checksums and manifest |
| Regenerated evidence (E7, Git-only) | prereg order b918c1d → 3b06035 → ba643bb → 164a04c → d9cd260; engine, runner, frozen-inputs and I25 code pins unchanged since their freeze commits; numbers in `regeneration-20261114.md` agree with RESULTS.json and receipts; exact Fraction margins reproduced (near 0.0057824 > 289/50000 at 42; far 0.165118 > 33/200 at 41; corner 31.80312 > 159/5 at 41; floor 1/512); 43,116 = 2·21,558 and 1,290 = 2·645; core `check.py`, `controls.py`, `runtime_probe.py`, `onset512_analytic/check.py`, engine freeze `0d9ce0a5` and `compact_pack` byte-unchanged since f4e8d8d (only docs and the new read-only `base_table.py` differ); reader cf64fbe8 vs 94ca2a76 is exactly one added `need(...)` line, honestly distinguished; the endpoint non-validation statement is consistent everywhere |
| Budget, reproduced | main 9,787,481; topic share 2,054,467; union 11,841,948; with the 2,087 B exception 11,844,035; bound 11,864,226 (= +19,660 inherited, +531 measured) against 10,000,000 |
| Manuscripts (M7) | only two numbered blocks differ from f4e8d8d (one word, one punctuation mark), none from 36ac772; ranges unchanged; three expanded unnumbered proof sentences reconstructed (Cauchy–Schwarz step with exact δ²+δj−t0² = 71/6250000; kernel cancellation; row amplitude 4\|w_r\|/\|sin v_r\| = a/sin²(v_r/2)); fresh builds 59/152 pages, exit 0, no errors/overfull/undefined/multiply-defined, `pdftotext` of rebuild equals both shipped PDFs (0 differing lines); `check_correspondence.py` PASS 19/86/120 default and `--archival` 13/90/113; `check_baseline_controls.py` 7/7; all 60 base values recomputed independently at 80 digits inside their printed brackets; audit-06 dispositions M6-01/02/03/05/06/07, B6-01, B6-02 confirmed on the TeX and on rendered pages 43 and 109 |

## Findings

IDs are the reviewers' own (unique, with the E7-, M7- and P7- prefixes). The same defect carries three IDs; I treat it as one.

### MAJOR (publication coherence; returned to Codex; AC chooses the wording, not the science)

- **P7-01 (= E7-01 = M7-01; also E7-01 for `certification-unified.tex:1864-1866`).** Both data statements (`paper/main.tex:84-93`, `companion-paper/main.tex:91-100`) say the reproduction package "comprises a versioned source snapshot, the essential certificate inputs, new native and independent-checker outputs, runtime dependencies, and verification commands" and point to repository paths. The deposit candidate that carries those very PDFs has none of the native outputs, runtime dependencies or snapshot (its README says nothing of the kind is bundled); those live only in the separate 296 MB preservation archive. The deposited manuscripts would misdescribe their own deposit. The companion's certification section also lists the "rebuilt polynomial checker" as shipped (the kit compiles it fresh). I classify this MAJOR because it is a false description inside a publication-bound document and cannot be fixed within the auditor's in-place limits (it edits frozen TeX, changes the PDFs inside the public ZIP and its hash). One sentence per text, formal blocks unaffected.

### MINOR returned to Codex (in the same batch, none gating)

- **P7-03** the README does not say that `SHA256SUMS` and `MANIFEST.json` are inside the package: `PASS integrity` shows internal consistency, authenticity needs the externally published ZIP checksum; replays of degrees not run rest on checksums. **P7-06** no memory statement: n=33 needed about 1.7 GB. **P7-04** `expected-results.jsonl` is read with plain `json.loads` (verify.py line 64), unlike the inputs (duplicate keys accepted, N12). **P7-05** polynomial replay compares three acceptance booleans, not the stored receipt's certificate hash/counts. **P7-07/P7-11** README: "Python 3.12" is ambiguous (3.13 works here), README.md is plain text, one overlong line, "the repository supplies no license" mentions a repository the user does not have, no single analytic PASS line, `corner_gap` is the string "None" for n≥256. **M7-02** the companion's data statement cites the companion itself as a separate "unpublished preprint". **M7-05..M7-09** TeX editorial items (path rule stated only at the end of section 5; "These new outputs provide the phase evidence" and "new phase certificates" read as all 942 new while 560 are retained, "the native campaign freeze" unnamed; "no permanent deposit has yet been assigned" should say no DOI; a stray "Section 4" inside Section 4; false precision in CPU times; paper trust-table footnote not updated in step with the companion). **E7-06** `regeneration-20261114.md:79-80`: "below 42,174" should be "at most … for 42,174 of 43,116 S checks; the other 942 stored uppers are not validated by this test". **E7-07..E7-13** NOTEs (RSS label; preregistration prose edited after commit without a marked amendment; the I25 staging heredoc is not in Git; "worker wait statuses" are those of the `timeout` wrappers; `independent_primary_fresh_pairs_equal` shares a per-degree cache; the committed 94ca reader has never done a full accepting readback, as the records say; the 942 unvalidated uppers are not re-examined). **P7-08..P7-10** NOTEs by design or cosmetic (replay does not authenticate every byte; the file population is checked against SHA256SUMS only; members are mode 0600).
- **M7-03** `check_correspondence.py` checks built labels only in `--artifacts` mode, which needs the retired historical PDFs; the "120 built labels" claim is therefore reproducible only with M7's own script (labels.py in the code directory). Returned to Codex as a tooling item (add a label-comparison mode over the current aux files).

### Needs AC (P7-02, and the others below)

- **P7-02 (MINOR; AC acknowledgement before any upload).** The 560 retained phase inputs contain the absolute path `/home/ahomel/a/andreyac/num_tests/padua30/...`; many files contain `/workspace/padua_research/...`; receipts for degrees 37..40 contain `/opt/codex/runtimes/...`; the required provenance file `proof-attempts-codex-01-padua-corner.md` contains internal process text ("Claude audit-01 ACCEPTED", model names, "PR #6 audit"). They cannot be redacted without changing hashes that the manifest and expected results pin. This is a personal-data and internal-process disclosure decision for AC, not a defect of the check. Options for AC: accept as is; or Codex prepares a documented, transformation-recorded sanitised derivative (as was done for the compact polynomial summaries) and the replay is re-run.

### MINOR fixed in place (separate commit)

Stale or inaccurate process text, each as a dated addendum or note with the evidence, no claim, proof, status or result changed. Locations in the fix commit's diff:

| # | Finding | Location | Fix |
|---|---|---|---|
| F1 | E7-02 "neither branch alone exceeds the cap" is wrong as worded (the topic branch tree includes main); E7-03 "all new tracked source/receipt files under 16 KiB" is false for `regeneration_delivery_20261114/delivery.py` (19,169 B; all receipts are under 16 KiB) | `pr-update-20261113.md` (dated correction at the end of the file) | addendum |
| F2 | M7-04 deposit README lists retired artifacts as files to deposit and does not point to the public package | `zenodo-deposit/README.md` (dated addendum at the end) | addendum |
| F3 | E7-04 top block still says "current 51-page paper … 85/116 … historical native endpoints" | `paper/README.md`, `companion-paper/README.md` (dated note under the title) | note pointing to the current state |
| F4 | M7-03 `BUILD.md` tells readers to run `check_correspondence.py --artifacts`, which cannot run without the retired PDFs | `companion-paper/BUILD.md` (dated note after the command block) | note |
| F5 | E7-05 campaign README: "pending independent I25", export staging directory, "not a resume/retry path", cf64 versus 94ca | `code/regeneration_20261114/README.md` (dated note at the end) | note |
| F6 | E7-06 comparison in `regeneration-20261114.md` | dated addendum at the end of the file | addendum |

Not fixed in place and returned instead: everything that edits frozen TeX or the public ZIP (they change hashes), the `verify.py` items, and the privacy decision.

## Limits

- Not re-examined: native histories (164 MB), the preservation archive, the I25 observation files, the original locations of the 382 regenerated inputs; only the ZIP's copies, their byte-identity to Git where Git has them, and the recorded RESULTS were checked. The regenerated records inside the ZIP were replayed here only for degrees 320, 384 and 500 among the new range; their production is recorded, not re-executed.
- Replays: 10 of the 471 phase degrees (41, 511 and 458 by the developer and Codex's reviewer; 100, 192, 256, 295, 320, 384, 500 by P7, both records each) and polynomial degrees 2, 9, 16, 17, 33 of 39 (2 and 17 by the developer); no full 942-record or 39-degree replay was repeated (not requested). A numerical match does not prove a universal claim; the finite-to-universal reduction remains the accepted analytic argument with J03's explicit IEEE/libm/SIMD assumptions, which finite probes do not prove.
- Python 3.13 and NumPy 2.5.3 are newer than the reference. The mathematical premises remain those stated in the papers.
- TeX Live and latexmk versions differ slightly from BUILD.md; text equality was shown, not byte equality.
- The effort level of each subagent is not observable to me; it was instructed at xhigh. The three independent reviews supplement but do not replace the Codex-side supplementary reviews.

## Remaining decisions for AC

1. **The one MAJOR (P7-01) wording**: which package(s) the data statements name. Recommended: name both ("a public verification kit … and a separately preserved full archive") and replace repository paths by what the kit contains.
2. **P7-02** disclosure (home-directory name, workspace and runtime paths, internal process prose in a required provenance file): accept or sanitise.
3. The global generated-output budget (bound 11,864,226 B against 10,000,000 B; main 9,787,481 B alone; topic share 2,054,467 B): exception, cold-storage destination or share reduction. The earlier statement that neither branch exceeds the cap is corrected (F1).
4. The DOI, the AI declaration (still omits Sonnet 5.5, which orchestrated audits 02–07), ORCID, contributions, funding and the draft marker; whether and where to upload.

## Next step

One paired batch for Codex (WORK, handoff 38): the P7-01 data statements and companion certification sentence (new TeX freeze, separate pointer commit, rebuild, correspondence, baseline controls and the 13-scenario mutation harness); the README/verify.py items; a rebuilt public ZIP with a new hash, a new frozen adapter commit and a new bounded smoke; one regression/reader-facing check by a distinct agent; then audit by a focused diff review (data statements and ZIP delta only; no repeat of this audit). Topic readiness is not offered until AC's decisions above are made.

2026-11-14 · orchestrator `claude-sonnet-5-5`; three Claude Opus 5.5 reviewers (instructed xhigh) · rules read at d6dd673 (unchanged from 5b1a494).
