# E7 — regenerated-evidence delta review (audit-07 subagent)

Reviewer: Claude, dispatched as Opus 5.5 xhigh independent auditor (subagent "E7"); runtime effort metadata as dispatched, not independently exposed.
Repository: `/home/user/padua_research`, branch `codex/padua-argmax-bridge-20261105`, HEAD `d6dd6730e5413a238f5c55630d0d907fb5e41563` (verified with `git rev-parse HEAD`; working tree clean before and after).
T = `topics/padua-argmax-bridge-20261105`. Audit-06 candidate `f4e8d8d`; main base `99a9b1d161e41a80c4fd425b63022c681fbe8779`.
Mode: read-only on the repository (only `git log/show/diff/ls-tree/cat-file/rev-parse/status`); all scripts copied to and run from `.../scratchpad/audit7/e7` with `python3 -E -B`. No network. `local-output/` and `/workspace` are **absent** in this sandbox, so native histories, I25 outputs, ZIPs and PDFs could not be opened.

Evidence classes used below: **[measured]** = I executed it here; **[git]** = read directly from committed bytes/history; **[recorded]** = claim only in committed prose/receipts referring to off-Git data, *recorded, not re-examined*.

## Summary verdict

No BLOCKING or MAJOR finding. The regenerated-evidence delta is internally consistent: preregistrations and freezes precede the recorded executions in commit order; every pinned source hash in the I25 freeze/RESULTS equals the committed bytes at the freeze commit, at the RESULTS commit and at HEAD; the numerical core, hybrid-engine freeze, onset512 checker and compact_pack are byte-unchanged since `f4e8d8d`; all quoted numbers in `regeneration-20261114.md` agree with `RESULTS.json`/`execution-receipt.json`/`regeneration-delivery.json`, and the exact margins strictly exceed the stated bounds (exact Fraction check). The cf64/94ca reader distinction is real in Git (one-line diff) and honestly distinguished in the records. Budget figures reproduce exactly. Findings are MINOR wording/staleness items plus NOTES.

## Findings

**E7-01 (MINOR) — manuscript data statements describe a Zenodo package that no longer matches the Zenodo candidate.**
Location: `T/paper/main.tex:86-93`, `T/companion-paper/main.tex:93-100` (frozen at `e861c75`).
Evidence [git]: both say "The reproduction package for this version comprises a versioned source snapshot, the essential certificate inputs, new native and independent-checker outputs, runtime dependencies, and verification commands … The package will be deposited in Zenodo". The later public Zenodo candidate (`T/zenodo-public-package-20261114.md:21`, handoff 37 "Public artifact") deliberately contains no runtime/OS/compiler binaries and no raw native histories; those live only in the 296 MB preservation ZIP that is "not the suggested normal Zenodo download". The PDFs embedded in the public kit therefore describe a different package. Similarly `T/companion-paper/sections/certification-unified.tex:1864-1866` says the package includes the "rebuilt polynomial checker" (the public kit compiles it fresh).
Fix: AC decision on which artifact(s) are deposited; then reword both data statements, e.g. "a public verification kit (inputs, minimal checker sources, expected results) and a separately preserved full archive (native histories and runtime bytes)", or state that the full archive will be deposited. Wording-only; formal blocks unaffected.

**E7-02 (MINOR) — "Neither branch alone exceeds the cap" is inaccurate as worded.**
Locations: `T/pr-update-20261113.md:31`, `T/handoffs/37-claude-audit-public-reproduction.md:112-113`, `T/LOG.md:3355`, `3399`, `3499`.
Evidence [measured]: the topic branch tree at HEAD (which has merged main at `5f0e8e4`) counts 11,841,948 bytes under the size.py convention; already at `f4e8d8d` it counted 11,734,394. Only main's tree (9,787,481) and the topic's own classified share (2,054,467) are each below 10,000,000.
Fix: "Main alone (9,787,481) and the topic's own share (2,054,467) are each below the cap; the topic branch tree, which includes main, exceeds it."

**E7-03 (MINOR) — "all new tracked source/receipt files are individually under 16 KiB" is false for one source file.**
Locations: `T/handoffs/37-claude-audit-public-reproduction.md:114-115`; `T/LOG.md:3502-3503` ("all newly added source/receipt files respect the individual limit").
Evidence [measured, `git cat-file -s`]: `T/code/regeneration_delivery_20261114/delivery.py` is 19,169 B (> 16,384), added in `c2b5487`. All other topic files added since `f4e8d8d` that exceed 16 KiB are prose (`supplementary-regeneration-review-20261114.md`, 37,835 B); all new generated-class receipts are below 16 KiB (largest `regeneration_polynomial_20261114/frozen-inputs.json` 14,212 B; `RESULTS.json` 11,875; `COLD_STORAGE.md` 16,064; `MANIFEST.json.in` 16,043; `full_return.py` 16,235 < 16,384). WORKFLOW.md:115 applies the ~16 KiB norm to summaries/receipts/essential evidence and requires code to be committed, so this is a claim error, not a rule violation.
Fix: "all new tracked receipt/evidence files are under 16 KiB; one new source file (delivery.py, 19,169 B) is larger".

**E7-04 (MINOR) — stale "current" top matter in both manuscript READMEs.**
Locations: `T/paper/README.md:1-46`, `T/companion-paper/README.md:1-~50`.
Evidence [git]: the undated top block still says "builds the current **51-page** paper", default output `onset512-paper-20261108/main.pdf`, "off-Git I25 evidence dataset is 2,843,611 bytes", "canonical 81,602,992-byte new native provenance return", "19 formal statements, 85 numbered display environments and 116 labels", "not universal validation of historical native endpoints" (the current dependency is the new 382 + 560 records; "historical" no longer fits), while the dated tail (`T/paper/README.md:139-146`) says current is `e861c75`, 59/152 pages, 120 labels. The tail's "Earlier active-freeze descriptions above are historical" does not neutralize a heading/paragraph labelled "current".
Fix: retitle/mark the top block as the 2026-11-08 historical record and put a short current summary first (59/152, 19/86/120, regeneration record link, "not validation of every stored native endpoint").

**E7-05 (MINOR) — stale/incomplete statements in the native campaign README.**
Location: `T/code/regeneration_20261114/README.md:14` ("The full readback remains evidence verification pending independent I25 and audit"), `:16` (export stages into `regeneration-20261114-essentials/`; I25 actually consumed the separate `-direct-essentials/` staging), `:16` "Export is exclusive and is not a resume/retry path" (four export invocations occurred, 01–03 failed — documented in `native-execution.md:23-34` but not referenced here), and no mention that the committed reader (`94ca2a76…`) is not the executed export/readback reader (`cf64fbe8…`).
Fix: add a dated pointer to `native-execution.md` covering the four export attempts, direct staging and the cf64/94ca distinction; drop "pending independent I25".

**E7-06 (MINOR/EDITORIAL) — containment sentence uses the wrong relation and hides the remainder.**
Location: `T/regeneration-20261114.md:79-80` ("Independently substituted upper bounds are below 42,174 of the stored S uppers").
Evidence [git]: `T/code/independent_phase_checker/check.py:244` counts `hi <= stored[p]` (non-strict). The sentence also does not say that the other 942 of 43,116 stored S uppers are not validated by that test (RESULTS `native_S_uppers_total` 43,116).
Fix: "Independently substituted upper bounds are at most the stored upper for 42,174 of 43,116 S checks; the other 942 stored uppers are not validated by this test."

**E7-07 (NOTE) — RSS label inconsistency.**
`T/regeneration-20261114.md:35` and `T/LOG.md:3293-3294` call 112,708 KiB "max reported wrapper RSS"; `T/code/regeneration_20261114/execution-receipt.json` field is `max_pass_rss_kib` and `native-execution.md:11` says "maximum pass RSS". Which boundary was measured is recorded, not re-examined. Fix: use one label.

**E7-08 (NOTE) — post-commit edits to preregistration prose are not marked as amendments.**
`T/preregistration-regeneration-20261114.md` was edited in `4ed88e9` (00:14:25), five minutes after the `b918c1d` freeze (00:09:10) and therefore probably during the native run: developer-metadata line 5 and whitespace only (diff inspected). The frozen machine preregistration identity (`frozen-inputs.json`, `campaign.py`) is unchanged since `b918c1d` [git], so no scientific deviation. The I25 preregistration was edited in `4ed88e9` (census adds far-leaf/norm fields; matching `records.py` change) and `164a04c` (essentials path, appended "Concrete input freeze — before execution" section), both before the recorded launch and before/at the input freeze; the appended section is undated. Fix: add a one-line dated amendment note in each file.

**E7-09 (NOTE) — the direct-staging code that produced the I25 input directory is not in Git.**
`T/code/regeneration_20261114/native-execution.md:21`: an inline heredoc tool, retained off Git. Mitigation [recorded]: independent byte equality with native `essential-receipt.json` files (`supplementary-regeneration-review-20261114.md:96`) and with the exporter's essentials, same inventory digest `3d670da1…` (`:119`). WORKFLOW.md:115 asks that code needed to regenerate outputs be committed. Fix: commit the heredoc body (small) or name `full_return.py export` as the reproducible regeneration route for those bytes.

**E7-10 (NOTE) — "worker wait status" boundary.**
`T/code/regeneration_i25_20261114/launch.py:37-44` wait4s the `timeout` wrapper, which propagates the Python worker's exit code; the "four actual worker wait statuses" are those of the wrappers. `RESULTS.json` stores `worker_exits` only (no raw worker statuses). Semantically adequate; precise wording is optional.

**E7-11 (NOTE) — `independent_primary_fresh_pairs_equal` naming.**
Both passes of a degree run in one process with a shared exact cache (`worker.py:71`, RESULTS `cache`). Equality of the two result rows is therefore not two independent derivations (the earlier J3-01 point). `regeneration-20261114.md` says only "pairs agree", which is accurate; only the RESULTS/records.py field name says "independent". Optional rename or note.

**E7-12 (NOTE) — final reader never run as a full accepting readback.**
The full relocated readback ran `cf64fbe8…`; the committed `94ca2a76…` was exercised only by five in-memory corruption controls and the synthetic shadow fixture. This is stated honestly (`native-execution.md:34,38`; review `:123,125`; receipt `final_reader_guard.scope`). Because the documented `verify` command (`README.md:9`) runs the committed source, a reader running it would be the first full accepting run of 94ca. The guard is a single `need(...)` on name-overlapping entries with differing identity; with zero overlap [recorded] acceptance is not expected to change. Note: the guard rejects only *conflicting* overlap (identical-identity overlap passes); "zero genuine overlap" in `regeneration-20261114.md:52` is acceptable but "no overlapping names" (review `:123`) is the stronger, recorded fact.

**E7-13 (NOTE) — cross-check against historical counts.**
New RESULTS premise counts (43,116 / 21,558 / 1,290 / 645 / 42,174 / 942) equal the historical `independent_phase_checker/RESULTS.json` exactly, consistent with deterministic regeneration of the same 382 trees; the docs (correctly) do not inherit these counts. Historical J03 states the 942 unvalidated uppers are one per certificate; that pattern for the new run is recorded, not re-examined.

## Question-by-question results

**(1) Preregistration order and fidelity.** [git] Commit order: `b918c1d` 00:09:10 (native prereg + `campaign.py` + `frozen-inputs.json`) → `3b06035` 00:12:32 (I25 prereg + code) → `4ed88e9`, `c2b5487`, `82e75e5` → `ba643bb` 00:26:05 (polynomial prereg + `replay.py` + freeze) → `8e86fd6` → `164a04c` 00:31:08 (I25 `input-freeze.json`) → `c13ba8f` 00:32:47 → `1b9ebde` → `36498af` 00:40:55 → `53d611a` (native receipt) → `d9cd260` 00:48:46 (I25 RESULTS). Author date equals committer date throughout. Recorded durations fit this order (native ≈13+807 s wall after controls; staging 96 s; I25 768 s wall from ≥00:31; export 04 232 s after `c13ba8f`). Git can show only commit order, not when off-Git execution began; that is recorded, not re-examined.
Fidelity [git]: `campaign.py` (sha `d715d658…`) and `frozen-inputs.json` unchanged since `b918c1d`; runner `a198b651…` unchanged since 2026-11-13. I25: all ten pinned sources equal the input freeze at `164a04c`, at `d9cd260` and at HEAD; `input-freeze.json` sha = `0e3d9f28…` as cited. Launcher/worker caps match the preregistration (worker RLIMIT_CPU 2670/2671, AS 2 GiB, `timeout 7200s`, supervisor RLIMIT_CPU 80/10800, internal 7250 s and outer `timeout 7350s`, acceptance ≤10800 CPU s; recorded 2770.54 s). Polynomial: `replay.py` sha `01cbe322…` and freeze `6e42f2d1…` unchanged since `ba643bb` and equal to the review's cleared identities; caps in `replay.py:137` (n2 15/120, n17 60/300) match the preregistration. Deviations (three failed data-only exports, `-direct-essentials` path, prereg metadata edits) are disclosed except as in E7-05/E7-08.

**(2) Numbers.** [measured, exact Fraction on committed RESULTS.json] near_min ≈ 0.0057824 > 289/50000 (excess ≈ 2.43e-6, degree 42); far_min ≈ 0.165118 > 33/200 (degree 41); corner_gap ≈ 31.80312 > 159/5 (degree 41); floor_min = 1/512 (degrees 41–44); M min 13, M_max 30. 942 = 2·471; 471 = 511−41+1; 560 + 382 = 942 = 2·(279+1) + 2·191. S checks 43,116 = 2·21,558; lambda 1,290 = 2·645; 43,116 − 42,174 = 942; lower containment 942. All CPU/wall/RSS values in `regeneration-20261114.md` match `RESULTS.json`/`execution-receipt.json` to the quoted precision; replay CPU 1.385967 + 11.505129 + 15.274709 = 28.165805 [measured] matches the doc and companion `certification-unified.tex:1843`. Native archive bytes/files/blobs and the delivery ZIP figures match the receipts; `be41972` has exactly 8,137 tracked regular blobs (8,124 + 13 executable) [measured], as the delivery review states; `delivery.py` sha equals the receipt `builder_sha256` `e41d2ee8…`.

**(3) Endpoint claim consistency.** Consistent in `regeneration-20261114.md:78-82`, `RESULTS.json` (`scope`, `all_native_endpoints_validated: false`), `pr-update-20261113.md:23`, supplementary review `:137`, and both TeX trees (`paper/sections/certification-unified.tex:510-513`; `companion-paper/sections/certification-unified.tex:1627-1630`: "No stored native numerical endpoint is a premise of this recertification"). The code supports this: `check.py:237` uses stored lambda uppers only in a consistency `need`; the losses use independent `hi`. Exceptions: E7-04 ("historical native endpoints" in READMEs) and E7-06 (relation wording).

**(4) Unchanged core.** [git] `git diff f4e8d8d HEAD` over `code/independent_phase_checker`, `code/onset512_analytic`, `code/final_hybrid_engine`, `compact_pack`, `code/phase_checker`, `code/small_degree_unification`: only `independent_phase_checker/independent-phase-summary.md` (+13 lines, dated note), `onset512_analytic/README.md` (+14, how to run base_table) and the new read-only `onset512_analytic/base_table.py` (+160, `cc2f9ad`). `check.py`, `controls.py`, `runtime_probe.py`, `accept_controls.py`, `onset512_analytic/check.py` (sha `5ce8cc07…`), every hybrid-engine file and `FREEZE.json` (sha `0d9ce0a5…`, 4,153 B) are byte-unchanged; last engine/core change `074c7da` (2026-11-13), before audit-06. [measured] `base_table.py` copy run reproduces the root JSON byte-exactly: sha `c1df932e…` as in `response-06.md:68`, status PASS, 60/60 entries in each manuscript.

**(5) cf64 vs 94ca.** [git] `full_return.py` blob sha history: `4ed88e9` c1aee0a8 → `82e75e5` 8f4108f5 → `8e86fd6` 0da5495f → `c13ba8f` **cf64fbe8…** → `36498af` **94ca2a76…** = HEAD. `git diff c13ba8f 36498af` is exactly one added line: `need(all(files[name] == manifest[name] for name in set(files) & set(manifest)), 'no archive trusted-source shadowing')`. The docs distinguish executed versus final readers consistently (receipt `executed_export_reader`/`final_reader_guard`, `native-execution.md:34,38`, review `:123`, `regeneration-20261114.md:51-52`). See E7-12.

**(6) Budget.** Counting rule: `T/audit-02/code/t2/size.py` convention (excludes `.py .sh .c .cpp .h .tex .bib .diff`, `.gitignore`, and `.md` except `COLD_STORAGE.md`), against AC's temporary 10,000,000-byte cap (LOG:176-184); WORKFLOW.md:115 states the stricter "well below 5 MB" target. [measured via `git ls-tree -rl`] main `99a9b1d` = **9,787,481**; HEAD = 11,841,948; topic share (all under `T/`, no changed/removed main paths) = **2,054,467**; union **11,841,948**; +2,087 exception = **11,844,035**. The conservative 11,864,226 = 11,844,035 + 20,191, where 20,191 = the earlier inherited no-shrink allowance 19,660 (constant in LOG:3180, 3354, 3398; not re-derived here) + 531 B measured shrink of `COLD_STORAGE.md` (16,595 at `8b1a6b5` → 16,064). Positive generated-class growth `f4e8d8d`→HEAD is 107,554 B. 16 KiB check: see E7-03.

**(7) Stale or overclaimed text.** See E7-01, 02, 03, 04, 05, 06. Checked and acceptable: "no retry" is scoped to native passes and I25 (export failures are separately disclosed); "independently verified" for the delivery refers to the distinct Codex delivery review, not to this audit; waitstatus claims are scoped (raw for 382 engine passes; observed exits for 191 wrappers, review `:106`); "unchanged" claims for the core/engine hold in Git; `results/padua-argmax-bridge-20261105.md:277-290` and `pr-update-20261113.md:3-13` are consistent. All relative Markdown links in the nine reviewed records resolve [measured].

## Commands executed (all from the sandbox; exit status)

1. `git rev-parse HEAD; git status --short; git log --format=… f4e8d8d..HEAD; ls …` — 0
2. `wc -c` on the review targets, `ls -la` of code dirs, `git log` on `99a9b1d`/`5f0e8e4` — 0
3. `cat` of `regeneration-20261114.md`, `RESULTS.json`, `input-freeze.json`, receipts, READMEs, preregistrations, `launch.py`, `worker.py`, `records.py`, `freeze.py`, `runtime_identity.py`, `campaign.py` — 0
4. `python3 -E -B e7/margins.py …/RESULTS.json` (exact Fraction margins and count identities) — 0
5. `git show --stat` loop over the 20 commits since `ff92191`, with author/commit dates — 0
6. `sha256sum` of the pinned sources at HEAD plus `git show <c>:<path> | sha256sum` at `164a04c` and `d9cd260` — 0
7. `git diff --stat f4e8d8d HEAD -- <core paths>` and the full diffs of the two changed docs — 0
8. `git diff b918c1d HEAD` (native prereg/campaign/freeze); `git diff 3b06035 HEAD` and `git show 4ed88e9`/`164a04c` (I25 prereg/records) — 0
9. `full_return.py` blob hashes at five commits plus `git diff c13ba8f 36498af` — 0
10. `grep` passes over the TeX, READMEs, LOG, results, pr-update and J03 — 0 (a grep returning no match would be exit 1; none was relied on)
11. `python3 -E -B e7/size7.py`, `size8.py`, `size9.py` (copies of the size.py logic using `git -C … ls-tree -rl`) — 0, 0, 0
12. Loop of `git cat-file -s` over files changed since `f4e8d8d` (>16,384 B filter) — exit 1, caused only by the trailing `[ … ] && echo` on the last iteration; the output was complete. Re-listed by size for the topic — 0
13. `python3 -E -B e7/bt/base_table.py --paper … --companion …` (copied `base_table.py` + `check.py`) — 0; output sha `c1df932ee28cd4d89f0b4d378b2453d588c9072840b9f94339fe32b8212b32ef`
14. `python3 -E -B e7/cc/check_correspondence_e7.py` and `… --archival` (copy with only the `HERE` line changed to the absolute companion-paper path; it reads Git with `ls-tree`/`show`) — 0 (19/86/120 at `e861c75`), 0 (13/90/113 archival)
15. Relative-link existence check over the nine records — 0
16. `git ls-tree -r be41972 | awk … | uniq -c` — 0 (8,124 + 13)

## Limits

- `local-output/` is absent here: the native ZIP (164 MB), native histories, I25 per-worker outputs, reviewer observations, delivery and public ZIPs, and the PDFs could not be opened. Every waitstatus/CPU/wall/RSS value, the zero-workspace-read result, the five archive controls, the census over the 382 new trees, byte equality of staged inputs, and the PDF page/label checks are **recorded, not re-examined**. Exact minima are checked only for consistency with the stated bounds, not recomputed from certificates.
- No I25, native, polynomial or public-kit execution was repeated. The unchanged arithmetic core and analytic proofs were not reopened. Git timestamps show commit order only.
- The 19,660-byte inherited component of the conservative bound was taken from the LOG, not re-derived.
- Public-kit adapter internals (`code/zenodo_public_20261114/*`) were outside this E7 scope except where they bear on E7-01 and E7-03.
