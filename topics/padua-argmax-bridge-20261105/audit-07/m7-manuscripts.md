# Audit-07 M7: manuscript delta and paper-to-evidence wording

Auditor: Claude Opus 5.5, xhigh (independent auditor; Codex developed). I chose this model because the scope includes reconstructing changed proof steps.
Rules/candidate head: `d6dd6730e5413a238f5c55630d0d907fb5e41563`, branch `codex/padua-argmax-bridge-20261105`. Topic T = `topics/padua-argmax-bridge-20261105`.
Delta audited: `f4e8d8d..HEAD` for `T/paper` and `T/companion-paper`. The TeX/Bib at HEAD is byte-identical to freeze `e861c752` (empty `git diff e861c75 HEAD` on `*.tex`/`*.bib`).
Repository access was read-only. All work used a local `git clone` and `git archive` copies under `.../audit7/m7`. There was no network access, and the publisher class/BST came from an earlier scratch copy, hash-verified by `build.sh` itself.

## Verdict

- No BLOCKING or MAJOR findings.
- **No theorem statement, hypothesis, constant, range, threshold or numbered display changed in substance.** Exactly two numbered blocks differ from f4e8d8d, matching response-06:
  - `cert:finite-verification` drops the word "recorded": "both recorded certificate records" became "both certificate records".
  - `ul:charts` changes its final "." to ",".
- Against 36ac772 the formal blocks are identical, with zero renames.
- Three unnumbered proof-step sentences changed. All are expansions of existing steps (M6-01, M6-08 and the Cauchy–Schwarz step). I reconstructed each and found it correct (see below).
- All ranges are unchanged: 2..40 Bernstein, 41..511 phase, ≥512 analytic.
- Findings: 4 MINOR, 4 EDITORIAL, 2 NOTE.

## Commands run (all in copies; statuses observed)

| # | Command (abridged) | Status / result |
|---|---|---|
| 1 | `git diff f4e8d8d HEAD -- T/paper T/companion-paper` (and `--stat`); `git diff e861c75 HEAD -- *.tex *.bib` | read in full; TeX delta = 18 files, TeX/Bib HEAD == e861c75 |
| 2 | `git archive HEAD T/paper T/companion-paper T/code/onset512_analytic` → m7/src; `git clone /home/user/padua_research m7/clone; checkout d6dd673` | ok |
| 3 | `PADUA_PAPER_OUTPUT_DIR=m7/out/paper bash m7/src/T/paper/build.sh` | exit 0; latexmk 5 pdflatex runs; **59 pages** |
| 4 | `PADUA_COMPANION_OUTPUT_DIR=m7/out/companion bash m7/src/T/companion-paper/build.sh` | exit 0; **152 pages** |
| 5 | log scan (Overfull / undefined / multiply / `^!` / Underfull; blg warnings) | 0/0/0/0 in both; bibtex 0 warnings. Underfull: paper 59 `\vbox (badness 10000) while \output is active` + 4 hbox (badness 2221, 7415, 1097, 1629); companion 152 vbox-output + 7 hbox (2221, 3735, 2772, 1264, 1701, 1097, 1629). No badness-10000 hbox. Approximate file attribution: preliminaries / comparison-unified / certification, none in changed hunks |
| 6 | `pdftotext -layout` rebuild vs shipped `zip-ro/.../papers/{paper,companion}.pdf`, `diff` | **0 differing lines** for both; shipped 59/152 pages. Shipped SHA256 `b0abf068…` / `3c7a114a…` equal the BUILD.md root-build records; my rebuild bytes differ (metadata only, expected) |
| 7 | `python3 -E -B check_correspondence.py` (clone) | PASS: baseline e861c75; 19 statements, 86 numbered displays, 120 labels, bib |
| 8 | `python3 -E -B check_correspondence.py --archival` | PASS (historical c6e195f/ac94504: 13/90/113) |
| 9 | `python3 -E -B check_baseline_controls.py` | PASS: 7 controls |
| 10 | `check_correspondence.py --artifacts …` (with and without original PDFs) | rc 2 (requires retired original PDFs) / rc 1 ("must not reuse original PDF paths"); see M7-03 |
| 11 | own `labels.py` (imports the committed module; compares built `main.aux` numbers) | 120 labels, 0 mismatches; no paper-only/companion-only aux labels |
| 12 | `audit-03/code/n/notation_scan.py --baseline-rev 36ac772 --rename-map notation-renames-response06.json` | rc 0; PASS 19/86; numbered blocks equal after 0 renames |
| 13 | same scanner, `--baseline-rev f4e8d8d` | rc 1 (expected): only `cert:finite-verification` (both texts) and `ul:charts` (both texts) differ |
| 14 | `python3 -E -B code/onset512_analytic/base_table.py --format text` | rc 0; paper PASS 60, companion PASS 60 |
| 15 | `python3 -E -B code/onset512_analytic/check.py` | rc 0 (Python 3.13.18 here) |
| 16 | own `indep_base.py`: all 15 quantities × 4 degrees recomputed from the **paper's formulas** (`uc:constants`, `uc:uniform-allowance`, `uc:analytic-norm`, `uc:relative-gate`; m=n+1, L=log n, L̄=1+L) in 80-digit `decimal`, Machin π, independent of check.py | **60/60 entries enclose my value and have width 10⁻⁶**, in both TeX tables. mpmath is not installed, so I used decimal. This is a high-precision float check, not a rigorous interval check |
| 17 | Fraction checks of scalar step: δ²+δj−t0² at (249/625, 23/250, 221/500); 9/4−4629/2500; 7/25+39/250−43/125; 2log2/π | 71/6250000; 249/625; 23/250; 0.44127 < 0.442 — all as printed |
| 18 | `RESULTS.json` (regeneration_i25) read + Fraction comparison of exact minima vs 289/50000, 33/200, 159/5 | all strict; floor_min 1/512; 942/471; pairs equal 471; census 191×(51 nodes, 26 leaves, 3 far, GRID); `all_native_endpoints_validated: false` |
| 19 | `python3 -I -B` over the public package's 942 `phase/inputs` | 471 produce/verify pairs have identical tree and key columns. For 320..510 the preorder string is 25 internal nodes ('a', 'b') and 26 leaves (23 '.' + 3 'f') = 51 nodes; norm GRID. Node range over 41..511 is 51..101 (matches Table 4) |
| 20 | `pdftoppm -r 70` paper pp. 42, 43, 56, 57; companion p. 109; images inspected | see the B6/M6 checks |

## Disposition spot-checks (response-06)

- **M6-01: confirmed.**
  - Paper comparison-unified.tex:1014–1015 has `8|w_r cot v_r|` and `|T_0| ≤ 4|w_r|/|sin v_r| = a/sin²(v_r/2) ≤ 2a`.
  - Companion :2274–2279 uses `|w_r|`.
  - Check: with w_r = a·cot(v_r/2)/2, 4|w_r|/|sin v_r| = a/sin²(v_r/2) holds identically.
- **M6-02: confirmed.**
  - Both data statements give the full companion title and path.
  - Paper certification-unified.tex:414–417 says "Section 5 of the expanded companion". The companion's `sec:certificates` is Section 5 (aux), and the paragraph "An elementary derivation of the arithmetic bounds" exists there.
- **M6-03: accurate as a historical disposition.** The current text has no sentence depending on unavailable outputs. grep for unavailable/historical/632/archive/custody/I25/onset-512 return finds nothing relevant in the paired TeX.
- **M6-05: confirmed.** The comma is present in both `ul:charts`, as the scanner confirms.
- **M6-06: confirmed.** Companion corner-unified.tex:1205–1206 cites `cu:quadrature`.
- **M6-07: confirmed.**
  - Paper comparison-unified.tex:1010 reads "Its normalized reference satisfies".
  - "recorded" is removed in the proposition in both texts.
- **B6-01: confirmed in my rebuild.** Table 2 renders alone on p. 43 after the p. 42 pointer paragraph, and §4.4 starts after the `\clearpage`.
- **B6-02: confirmed.** The companion p. 109 output/meaning/reference array has quad column spacing and is readable.

## Independent reconstruction of changed mathematical sentences

1. **Scalar maximum (paper comparison-unified.tex:588–591; same in the companion).**
   - Inputs: `C_∞−C_* ≤ −j·u + t0·p` (uc:model-loss), `p = sin x`, and `u = 1−a ≥ (1−cos x)/2` (because a = (cos x+cos y)/2 ≤ (1+cos x)/2).
   - Since j > 23/250 > 0, this gives C_∞ ≤ C_* − j/2 + (j/2)cos x + t0 sin x.
   - Cauchy–Schwarz gives (j/2)cos x + t0 sin x ≤ √(j²/4+t0²).
   - δ = 9/4 − C_* > 249/625 follows from C_* < 4629/2500.
   - δ² + δj − t0² is monotone in the bracketed constants, and the bound evaluates to 71/6250000 > 0.
   - Squaring is valid because both sides are positive. **Correct.** It is the same argument as before, with the hidden step now explicit.
2. **Kernel cancellation (paper :759–762; companion :1658–1661).**
   - From eq:kernel-evaluation, the numerator of (−1)^δ·(P_n(cos u) − P_n(cos v_r)) is cos x(1+cos u) − p sin u + cos y(1+cos v_r) + q sin v_r.
   - Substituting 1+cos u = (1+cos v_r) + (cos u − cos v_r) gives 2a(1+cos v_r) + cos x(cos u − cos v_r) − p sin u + q sin v_r.
   - After division by 2(cos u − cos v_r), the constant cos x/2 appears, i.e. (−1)^δ·cos x/2 in G_n/2.
   - Since cos(nu) = (−1)^δ cos x, the term −cos(nu)/2 cancels it, leaving the displayed fraction. **Correct.** Strictly, the constant sits in the divided-difference part of G_n/2. The wording is acceptable.
3. **Row half-amplitude (M6-01).** Verified above. Separately, |w_r| ≤ a·m/(πν) follows from cot(v/2)/2 ≤ 1/v. The change is notational: it adds scope and an absolute value.
4. **Base-value table.** All 60 values in both texts were reproduced independently (commands 14 and 16). The new sentence "composed from the exact interval routines" with "not part of its executed receipt.json" is accurate: base_table.py does not read receipt.json.

## Paper-to-evidence consistency (manuscripts vs RESULTS.json / regeneration-20261114.md)

These statements match the evidence:

- 942 records / 471 degrees.
- 560 authenticated (41..319, 511) + 382 new (320..510), generated in "new primary and fresh native pass".
- 39 polynomial degrees.
- 51 nodes / 26 leaves / 3 far leaves / grid norm for 320..510.
- Table 4 node range 51–101.
- Fresh rechecks at 41, 458, 511 "with all scientific result fields agreeing".
- Companion CPU/wall 2770.544476 / 768.464785 / 28.165805 equal RESULTS values rounded.
- "rebuild checked on degrees 2 and 17 … no new full 39-degree replay is claimed".
- Endpoint honesty: "No stored native numerical endpoint is a premise or is asserted valid" (paper cert:390–392) matches `all_native_endpoints_validated: false`.
- The companion trust-table footnote states that finite probes do not prove universal IEEE conformance.

The margins 289/50000, 33/200, 159/5 are not stated in either text, and nothing contradicts them. The floor 1/512 appears in the companion (cert:1268) and matches `floor_min`. No DOI is invented ("DOI pending; no permanent deposit has yet been assigned"). No sentence describes new data as recovered historical data.

All cited paths exist at HEAD:
- `regeneration-20261114.md`
- `code/regeneration_i25_20261114/input-freeze.json` (SHA `0e3d9f28…`, matches the record)
- `code/regeneration_20261114/frozen-inputs.json`
- `code/onset512_analytic/receipt.json`
- `companion-paper/main.tex`

## Findings

**M7-01 — MINOR (deposit-gating wording; AC decides which package): the data statement says the package contains things the planned public package does not have.**
- Location: `T/paper/main.tex:86-89` and `T/companion-paper/main.tex:93-96`.
- Both statements say "The reproduction package for this version comprises a versioned source snapshot, the essential certificate inputs, new native and independent-checker outputs, runtime dependencies, and verification commands", and that "The package will be deposited in Zenodo".
- That list describes the 296 MB preservation ZIP. The Zenodo candidate described in `T/zenodo-public-package-20261114.md` and in the shipped public `README.md:9-11,26,49` is different:
  - it has no full source snapshot, only a "small topics/ source closure";
  - it has no native histories;
  - it says "No compiler, interpreter, shared library or OS is bundled".
- The shipped `papers/paper.pdf` and `companion.pdf` inside that public ZIP therefore misdescribe the package they ship in.
- Fix: describe the public package's actual contents, e.g. "the 942 phase and 39 polynomial certificate inputs, the independent checker sources and expected results, exact analytic checkers and verification commands; a separate preservation archive holds native histories and runtime payloads". Alternatively, state explicitly that both archives are deposited.

**M7-02 — MINOR: the companion's data statement cites the companion itself as a separate preprint.**
- Location: `T/companion-paper/main.tex:91-92`.
- Inside the companion, "The unpublished preprint *…: an expanded explanatory companion* is available … at companion-paper/main.tex" refers to the document the reader is holding. This is inherited by copying the paper's statement verbatim.
- Fix: in the companion, refer to the research article (title and path `paper/main.tex`), or say "This companion's source is at …".

**M7-03 — MINOR (tooling vs BUILD claims): the committed checker can no longer run the built-label check.**
- Location: `T/companion-paper/check_correspondence.py:128-136,158-159` and `T/companion-paper/BUILD.md:31`.
- The built-label/page comparison in the committed checker only runs in `--artifacts` mode. That mode requires the historical 48/162-page original PDFs (fixed hashes at :20-23), which AC has retired.
- So the "120 built labels match" claim in BUILD.md/README.md cannot be reproduced with the committed CLI: commands 10a/10b fail.
- BUILD.md:31 still instructs `check_correspondence.py --artifacts` without the original-PDF arguments, which now always errors.
- I reproduced the claim (120/120, command 11) by calling the module's own `aux_numbers` and `compare_pair`. BUILD.md:149-151 does disclose that current auxiliary comparisons were "executed separately", but that separate command is not committed.
- Fix: add a current-artifact mode (e.g. `--built-labels`) that checks aux-number equality, page counts and companion ≤ 5×paper without historical PDFs. Mark the historical preservation mode as retired, and update BUILD.md:29-31.

**M7-04 — MINOR (outside the TeX, but the deposit README in the repo is stale).**
- Location: `T/zenodo-deposit/README.md:6,35-55,176`.
- Its "Files to deposit" table still lists retired artifacts as deposit items: `onset512-return-20261108.zip`, `i25-evidence-20261108…zip`, historical 51/147-page PDFs, the a433c7d snapshot.
- It still describes the canonical return as missing, and it does not mention the 2026-11-14 public package or the regenerated evidence.
- It does not contradict the manuscripts (no DOI is claimed), but it competes with `zenodo-public-package-20261114.md` as the deposit plan.
- Fix: add a superseding header pointing to the public-package record, and mark the table historical.

**M7-05 — EDITORIAL: the convention for relative paths is stated only after the paths are first used.**
- Location: `T/paper/sections/comparison-unified.tex:129-130,1880` and `certification-unified.tex:401-402`. Companion: `comparison-unified.tex:336-337,4145`, `certification-unified.tex:1576-1578`.
- The convention ("Paths here are relative to topics/padua-argmax-bridge-20261105/") appears only at `certification-unified.tex:519-520` (paper) and `:1636-1637` (companion), at the end of Section 5. In Section 4, `code/onset512_analytic/receipt.json` is unanchored.
- Fix: state the convention once at first use, or in the data statement, and say "paths below".

**M7-06 — EDITORIAL: two sentences can be read as saying every phase certificate is new.**
- Location: `T/paper/sections/certification-unified.tex:526` and `T/companion-paper/sections/certification-unified.tex:1643`, both "These new outputs provide the phase evidence used in this version". Also companion `:1864-1866`, "The reproduction package includes the retained polynomial certificates, rebuilt polynomial checker, new phase certificates and independent verification outputs".
- Both can be read as saying all phase certificates are new; 560 are retained.
- Also, "the native campaign freeze" (`:524` / `:1641`) does not say which campaign.
- Fix: "The new independent-checker outputs, together with the 942 input records described above, provide …"; "… the 942 phase certificate inputs (560 retained, 382 new) …"; "the freeze of the 2026 native campaign for degrees 320–510".

**M7-07 — EDITORIAL: a deposit is not "assigned".**
- Location: `T/paper/main.tex:92-93` and `T/companion-paper/main.tex:99-100`.
- "no permanent deposit has yet been assigned" mixes a deposit with a DOI.
- Fix: "the package has not yet been deposited and no DOI has been assigned".

**M7-08 — EDITORIAL: two small wording issues in the companion.**
- `T/companion-paper/sections/comparison-unified.tex:3043`: "distinct from the test function of Section 4" is written inside Section 4, because comparison-unified is `\input` at `localization-unified.tex:353`. Fix: name the location of the test function χ (the measure-inequality paragraph) rather than the section.
- Companion `certification-unified.tex:1841-1843`: CPU and wall times to 10⁻⁶ s are false precision for a journal text. Fix: round, e.g. "about 2771 CPU s and 768 s wall".
- Optional: paper/companion :1880/:4145 could name `code/onset512_analytic/base_table.py`, which actually reproduces Table 2, alongside check.py.

**M7-09 — NOTE: the paired texts diverge slightly on runtime and replay wording.**
- The companion trust-table footnote was rewritten (`companion cert:1576-1581`: runtime identities checked against input-freeze.json; probes do not prove universal IEEE conformance; separate C++/GMP environment).
- The paper footnote is unchanged (`paper cert:463-465`: "recorded interpreter, libraries, operating system and hardware are trusted").
- The paper also does not mention that the full 39-degree polynomial replay is historical and only degrees 2 and 17 were rebuilt and rechecked (the companion does at :1866-1868).
- This is not a contradiction. Optionally carry one sentence into the paper.

**M7-10 — NOTE (reserved to AC; report only).**
- The date markers predate the 14 Nov changes: paper `main.tex:43` "Development draft, 8 November 2026"; companion `main.tex:46,50` "Expanded companion, 13 November 2026" / "Development draft".
- The AI declaration, ORCID, contributions and funding were not assessed.

## Script critique

- `check_correspondence.py` (default mode) does what it claims: an exact TeX/Bib freeze against e861c75, plus paired statement, display, label, heading, counter and bibliography equality. Its docstring correctly disclaims mathematical correctness.
- Its statement regex counts only theorem/lemma/proposition/corollary/definition/remark. The paper has exactly these 19 (9+4+3+2+1) and 86 = 75 equation + 11 align. Nothing is missed for the current environment set.
- `check_baseline_controls.py` tests freeze sensitivity only. That is correct as described.
- The notation scanner passes a declared fake rename, as response-06 acknowledges. A pass with an empty map is meaningful only because the map is empty.
- `base_table.py` fails closed on table-format deviations. It checks both containment and six-decimal tightness.
- See M7-03 for the gap between the built-label claim and the CLI.

## Limits

- I did not run the public `verify.py` (integrity or replay), any phase/polynomial numerical recertification, or the 13-scenario mutation harness.
- The numerical facts in RESULTS.json were read, not re-executed, apart from the structural census over the public inputs (command 19).
- The base-table cross-check uses 80-digit decimal floating point, not outward intervals. All values lie strictly inside their 10⁻⁶ brackets.
- I rendered and inspected only 5 pages. Text equality of the whole document with the shipped PDFs was established by pdftotext.
- My TeX environment: pdfTeX 1.40.26, latexmk 4.83 (BUILD records 4.86). The class/BST were taken from an earlier scratch copy and hash-verified by build.sh against dependencies.json.
- File attribution of underfull boxes is approximate.
- No novelty content is in scope, so the full IDEAS read was omitted.
