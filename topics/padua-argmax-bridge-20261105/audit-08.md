# Claude audit-08: focused review of response-07 (handoff 39)

**Decision: accepted. Response-07 resolves audit-07's MAJOR (P7-01) in both manuscripts and in the rebuilt public kit. No BLOCKING or MAJOR finding. Mathematics, evidence and numerical core are unchanged.** Three MINOR items and some notes are returned or recorded (below); small stale-record items are fixed in place in a separate commit. The topic is **not offered for readiness**: PR preparation (registry application and the readiness reservation check) has not been done, the manuscripts and kit will need one more rebuild after AC's own edits, and AC's decisions are open.

## Identity and candidate

- Role: independent auditor of Codex development. Orchestrator `claude-sonnet-5-5`; review by three independent Claude Opus 5.5 subagents instructed at xhigh effort (effort actually applied is not observable): **M8** manuscripts, **E8** records and kit source, **P8** the delivered ZIP. Opus was chosen for source/PDF reconstruction and adversarial verifier controls; Sonnet orchestrated and classified.
- Rules: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md` at head `50070f520b3d5cfe9afbc75f10fdb1bc664b7b71`, unchanged since `d6dd673` (E8 diffed `agents/`; no change).
- Reviewed diff: `9d3f5e0f8b270d039d78d4ebc0df53269a7892ab..50070f5` (response-07): paired TeX/Bib freeze `5f435be21f29f6fbf48e6d8cba15346117d7e151`; current-label tooling and pointer `daa77deb6371a12f6a6e36ff7b894ebb71a7f232`; public adapter source `dce3260b88c11a964168a64c34b168ac37f2a11c`; records `687e9d4`; handoff `50070f5`. No code under `code/` changed after `dce3260`.
- Artifact, **supplied by AC in this session** and recomputed by me and P8: the new public ZIP, 5,149,206 bytes, SHA256 `b341e6a1c6875550b58576b2cb167766f5a3cf9a4e4fc620b1134d2c490adbaa`, 1,019 files, 10,229,741 expanded bytes, `testzip` clean. Compared with the audit-07 package (`15885d34…`): exactly nine members differ (MANIFEST.json, SHA256SUMS, README.md, README.txt, verify.py, `analytic/tables/{paper,companion}.tex`, `papers/{paper,companion}.pdf`); 1,010 members, including all 942 phase and 39 polynomial inputs, are byte-identical.
- Not examined (recorded, not re-examined): the native-history and preservation archives (not in this container; unchanged by the receipt), full 942-record or 39-degree replays (excluded by the handoff), polynomial degrees 35–40.

## Executed checks

| Area | Result |
|---|---|
| ZIP census, P8's own checker | PASS: 1,018 SHA256SUMS lines (all files but itself), 1,017 manifest payload rows, 942 + 39 inputs with exact names, 942 strictly parsed expected rows, summary recomputed, every stored polynomial certificate hash equals the manifest; all members 0644, no directory entries or ZIP comment; 30 mapped sources, README.txt/.md and verify.py equal Git HEAD (`verify.py` 92319b64…, `build.py` fabac559… as recorded); PDFs equal the receipt hashes (59 and 152 pp); table `.tex` files equal the HEAD comparison sections |
| New user, README verbatim (Python 3.13.18, NumPy 2.5.3, g++ 13.3, caps recorded in the P8 report) | integrity PASS; quick command PASS (33.0 CPU s); `--controls` 27 rejected / 3 substitutions accepted; `--analytic` PASS; **new degrees 77,150,222,333,410,487 (12/12 records) PASS**; polynomial n=5, 21, 28, **34** PASS (peak 1.93 GB); `-O`/`-OO` refused; working copies unchanged afterwards |
| 73 negative controls (P8) + E8's controls on the delivered package | 68 as predicted; the 5 deviations are all selection-argument parsing (P8-01/02). **Previously accepted by audit-07, now rejected:** an extra file with only SHA256SUMS refreshed (N04), a duplicate key in expected results (N12). New checks rejecting as intended: NaN/Infinity/1e999 in expected rows; missing payload, hash mismatch, wrong byte count, duplicate payload path against the manifest; swapped or re-gzipped polynomial inputs; stored polynomial receipt changed (acceptance, return code, rows at integrity; split/bound counts and a certificate with a leaf deleted at replay); lowered S/lambda endpoints at n100 and n410; a changed base-table entry. **Still accepted, by design and stated:** produce/verify swap with consistent refresh, substituted-field edits, a fully consistent refresh of checksums and manifest, an extra file added to both lists |
| Residual trust statement | the README now says SHA256SUMS and MANIFEST are inside the package, integrity proves internal consistency only, authenticity needs an externally published checksum (none exists yet), unreplayed degrees rest on that and the embedded identities |
| Disclosure of embedded paths and process text (P8 grep of the ZIP) | `/home/ahomel/a/andreyac/num_tests/padua30` 2,242 times in exactly the 560 retained inputs; `/workspace/padua_research/` 1,556 times in the 382 regenerated inputs, MANIFEST (two PDF source paths), `analytic/receipt.json` and receipts n37–40; `/opt/codex/runtimes/…` only in n37–40; internal process prose in the corner dependency text. The README's disclosure is accurate by category; no path in the 39 certificates; licence, DOI and upload are not invented (AC chose "retain with explicit disclosure"; resolved, not asked again) |
| Manuscripts (M8) | `git diff 5f435be HEAD` on `*.tex`/`*.bib` empty; every TeX hunk is wording or provenance; **no theorem, hypothesis, constant, range, threshold, numbered display or proof step changed** (the only numerical edit rounds recorded CPU/wall times); builds 59/152 pp, exit 0, no errors/overfull/undefined/multiply-defined; scanner with empty and response06 maps: 19/86, equal numbered blocks against 9d3f5e0 and e861c75; `check_correspondence.py` default 19/86/120, `--archival` 13/90/113, new `--built-labels` 120; baseline controls 7/7; `base_table.py` 60/60 each; negative cases on corrupted aux copies reject (changed number, deleted/duplicate label, same directory, symlink, relative path, missing aux, invalid mode combinations); rebuilt PDFs differ from the shipped ones in bytes only, `pdftotext` text byte-identical; the rendered data statements match the TeX |
| Records (E8) | every audit-07 disposition in `response-07.md` accurate (P7-01, 03..07, 09, 10, E7-02..13, M7-02, 05..09); J03 diff is wording only; E7-08 amendment commits and times consistent; **budget reproduced exactly**: main 9,787,481; HEAD 11,848,485; topic share 2,061,004; with the 2,087 B exception 11,850,572; conservative bound 11,870,763 (the 20,191 B allowance is inherited, not re-derived) against 10,000,000; no file added since 9d3f5e0 over 16 KiB (largest 14,298 B) |

### Audit-07 dispositions

P7-01 resolved (the shipped data statements now describe the public kit and, separately, the author-held preservation archive; quoted by P8 from the shipped PDFs). P7-03..P7-07, P7-09, P7-10 resolved. P7-02 retained with accurate disclosure by AC's decision. P7-08 unchanged by design and stated. P7-11 resolved except 9 README lines over 80 characters (cosmetic). M7-02, M7-05..M7-09 fixed (M8). E7-02, E7-03 corrected earlier by audit-07 F1.

## Findings

IDs are the reviewers' (unique prefixes M8-, E8-, P8-).

### MINOR (returned; none gating; none a mathematical issue)

- **M8-02** `paper/main.tex:90-91`, `companion-paper/main.tex:97-98`: the preservation archive is said to contain "the full native histories". It holds the full histories only for the 2026 regeneration of degrees 320–510; the histories behind the 560 retained records were retired. Say "the native histories of the regenerated records" (or equivalent). TeX edit.
- **M8-03** the paper's trust-table footnote (`paper cert:463-470`, now identical to the companion's) dropped "The recorded interpreter, libraries, operating system and hardware are trusted"; neither text now mentions the operating system or hardware. Restore the sentence in both. TeX edit.
- **M8-01** `--built-labels` (`companion-paper/check_correspondence.py:129-135, 183-184`) passes vacuously with the paper's aux copied into the companion directory (rc 0), does not check aux freshness, page counts or the 152 ≤ 5×59 ratio that BUILD.md cites, and a missing aux gives an uncaught traceback. Tooling; add a document-identity check and a clean error.
- **P8-01** `code/zenodo_public_20261114/verify.py:176,181`: `--degrees ''` or `--polynomial-degrees ''` skips replay and still prints "PASS requested verification" (empty string is falsy). Test `is not None` and reject empty selections. Needs a kit rebuild.
- **E8-01** `README.txt:139-142` says the certificate SHA256 and counts must equal "the stored accepted record and input manifest"; the manifest carries no counts, and the fresh certificate hash is the input file's hash, already checked by integrity. Say the hash matches the manifest and stored record, and the counts match the stored record. Needs a kit rebuild.

### NOTE and EDITORIAL (recorded; optional at the next rebuild)

P8-02 (abbreviated options such as `--degree` and padded values accepted; use `allow_abbrev=False`); P8-03/E8-08 (README lists PASS polynomial before PASS analytic; actual order has analytic first after about 300 lines of JSON; line 121 is 93 characters); E8-05 (README refers to "the audit", unidentifiable to a ZIP reader); P8-05 (memory guidance has no figure for degrees 35–40; n=34 peaked at 1.93 GB); P8-06 (`analytic/tables/*.tex` are whole section sources; `--analytic` checks only the labelled 60-entry table); P8-07/M8-05 (PDFs cite repository records that are not in the kit; the data statements do not say that `verify.py` is a new adapter); P8-04/E8-04 (the disclosure does not name `/root/a1_develop`, MANIFEST's own PDF source paths or the "codex" filename of the corner dependency; implicit under "process prose"); M8-04 (neither archive is identified by size or hash in the manuscripts: AC's choice); M8-06 (comparison "Repository paths below" precedes naming the repository); P8-08 (`cleanup: false` in the receipt means no forced kill, not "temporary files left"); E8-06 (the claim that the committed staging script is the exact historical body, 1,775 B, ef88f9f7…, cannot be checked from Git; no earlier hash record); E8-07 (for polynomial degrees 17..32 stored acceptance rests on membership in `accepted_rows` because that receipt format has no acceptance field).

### MINOR fixed in place (separate commit)

| # | Finding | Location | Fix |
|---|---|---|---|
| F1 | E8-02 the retained audit-07 correction now points at sentences that response-07 rewrote | `pr-update-20261113.md` (dated note at the end) | note: the correction applies to the text at `9d3f5e0`; current figures are those of audit-08 |
| F2 | E8-03 `zenodo-deposit/MANIFEST.json.in` still calls `e861c752` the current pair | `zenodo-deposit/README.md` (dated addendum; the manifest carries a hash pin and is not edited) | addendum naming `5f435be`/`daa77de` as current |
| F3 | M8-07 `zenodo-public-package-20261114.md:51-55` lists the earlier 5,138,944-byte ZIP with no pointer to the new one | same file (dated note at the end) | pointer to the response-07 ZIP |

Nothing else is fixed in place: the remaining items edit frozen TeX, `verify.py` or the kit README, which changes hashes, or are code.

## Readiness

Not offered. (1) **PR preparation is outstanding.** No shared-registry change exists on the branch (no diff of `PROOF_STATUS.md`, `ID_CROSSWALK.md`, `RESULTS.md` or `state/` against main); the reserved ranges (`ALLOCATIONS.md`) remain unassigned. The readiness check (reviewed registry `git diff` and the reservation refresh against current heads) can only run after Codex applies them and AC authorizes final-ID assignment. (2) **One more rebuild is coming regardless.** AC will edit the AI involvement, draft marker, DOI and possibly the data statement, which changes both PDFs and therefore the public ZIP. The MINOR items above are cheap to bundle into that single final freeze (M8-02, M8-03, M8-01, P8-01, E8-01, P8-02, P8-03, P8-05) rather than force a rebuild now; a rebuild for them alone is not warranted. A final-freeze diff review (data statements, this item list and the ZIP delta) then suffices. (3) AC's decisions below.

## Limits

- The supplementary Astra review and this audit's three reviews agree; none of them re-executed the native campaign or a full replay. The ZIP's regenerated records were replayed here for degrees 77, 150, 222, 333, 410 and 487 among others; 10 + 6 of 471 phase degrees in audits 07 and 08 and polynomial degrees 2, 5, 9, 16, 17, 21, 28, 33, 34 of 39.
- A numerical match does not prove a universal claim; the finite-to-universal reduction is the accepted analytic argument with J03's explicit IEEE/libm/SIMD assumptions, which finite probes do not prove.
- Python 3.13.18/NumPy 2.5.3/g++ 13.3 differ from the reference (3.12.14/2.3.5/14.2); no environment effect was seen.
- Effort level of the subagents is not observable to me.

## Remaining decisions for AC (not decided here)

1. Global generated-output budget: bound 11,870,763 B against 10,000,000 B (main alone 9,787,481; topic share 2,061,004; the topic tree including main 11,848,485): exception, cold-storage destination or share reduction.
2. Upload, DOI, licence, the author/AI declaration (still omits Sonnet 5.5, which orchestrated audits 02–08), ORCID, contributions, funding and the draft marker; the final TeX edits above are made together with these.
3. Authorization to apply the shared registries and assign final IDs from the reserved ranges (PR preparation), after which the readiness check runs.

2026-11-14 · orchestrator `claude-sonnet-5-5`; three Claude Opus 5.5 reviewers (instructed xhigh) · rules read at 50070f5 (unchanged from d6dd673).
