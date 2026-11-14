# Supplementary focused review of response-06

Independent reviewer: Codex, dispatched as `gpt-6-astra`, high; runtime model and effective effort are not exposed. Rules read at `f4e8d8d313b1fec0cd4976de98524552fbdc94dd`: `AGENTS.md`, `agents/WORKFLOW.md`, and `agents/codex/CODEX.md`. Inputs: handoff 35, audit-06 and its analytic/build findings. This supplements the handoff; it is **not a Claude audit or a readiness decision**.

Scope: the paired response-06 wording and layout changes, their evidence-status clarification, and the new read-only `code/onset512_analytic/base_table.py`. No unchanged theorem, certificate, engine, reader, runtime-probe or scientific campaign was re-audited. No new scientific campaign, archive regeneration, custody verification, threshold, final ID, or novelty claim was introduced. The novelty gate is not applicable to this bounded repair review. Only this report was written in the repository; temporary review scripts and outputs are under `/tmp/response06-independent-review/`. No Git mutation or developer-source fix was performed by the reviewer.

## Source review

The reviewed diff is against the rules/input head above (the prior paired source freeze is `8937d3b723c09c004f49d3e565d0b02976713a37`). The wording changes are accepted at their stated scope:

- **M6-01:** both central-reference paragraphs now use the row half-amplitude `w_r` and the actual row angle `v_r`. The companion residual paragraph uses the same symbol. Remaining bare `w` occurrences are separately defined scalar arguments, substitutions, or the endpoint distance `r*pi+b`; no global search-and-replace was applied. One focused finding was returned to the developer: since the global row amplitude can be negative after reflection, the residual inference must state `|w_r| <= a*m/(pi*nu)`, not merely `w_r <= ...`. The developer supplied that modulus; rereading the corrected paragraph confirms the original constant and inference. Indeed `|cot(v_r/2)|=cot(v/2)` on the reflected endpoint side and `cot(v/2)<=2/v`, where `v=pi*nu/m`.
- **M6-02:** the paper points in plain text to Section 5 and the named arithmetic paragraph of the companion. The data statement gives its full title, matching the companion's title exactly, and its actual repository source path. It is described as an unpublished preprint; no DOI or published status is invented. The snapshot/DOI placeholders remain explicit.
- **M6-03:** the identical new paragraph in both manuscripts states plainly that Proposition 5.3 for `320 <= n <= 510` rests on recorded executions whose outputs cannot currently be re-examined. It defines the missing material as the certificate-run output archive and stored independent-checker outputs. The planned inspection concerns four sampled degrees and both records at each (eight records); it compares stored producer/checker outputs without rerunning the certificate search. The separate historical degree-458 execution is expressly distinguished from that pending inspection. This is an evidence-status clarification, not an execution or restoration of missing evidence.
- **M6-05..08, M6-10:** the chart comma, midpoint-lemma citation, reference-satisfies verb and certificate-record redundancy are corrected. Local offset/function, angle/mesh and displacement/pole-offset uses are scoped. The amplitude-phase explanation is the Cauchy–Schwarz estimate for `(j/2)*cos(x)+t0*sin(x)`, leaving all constants intact. The cosine paragraph follows by extracting `(-1)^delta*cos(x)/2` from the divided-difference term in `G_n/2`; it cancels `cos(nu)/2`. No kernel identity changes.
- **B6-01/B6-02/B6-08:** the table provenance uses a breakable path; the companion output array has explicit column gaps; the receipt is described as present in the repository. The paired page break keeps Table 2 before the next subsection. B6-05's optional Figure 2 box relocation is deferred; this review makes no new claim about that unchanged figure.

No mathematical constant or threshold is changed by the reviewed wording. Bibliography bytes and the reserved declarations remain unchanged. Open evidence, custody, budget and publication decisions remain outside this acceptance.

## Independent base-table verification

`base_table.py` has no displayed numerical answer literals: it imports the adjacent exact `Fraction` interval API, obtains its elementary constants, composes the manuscript formulas and rounds outwards to six decimal places. It neither reads nor writes historical `receipt.json`, modifies TeX, nor executes the gate-checker main routine. Inspection of the parser confirms that it requires the unique labeled table, the fixed degree set, recognized rows, six-decimal interval syntax and all 60 unique entries; duplicate/missing/unrecognized entries fail closed. Verification requires both containment and the tight six-decimal endpoints, so a merely widened enclosure fails. The optimization refusal comes from the unchanged imported checker.

The reviewer independently transcribed all 15 table quantities from the manuscript's constants, uniform allowance, norm and relative-gate definitions using only `I`, `PI`, `LOG2`, `log` and exact fractions from `check.py`. The reconstruction did **not** call `constants()`, `base_values()` or `decimal_enclosure()`. In particular it independently formed `D`, the mesh allowance, `G_g`, `W_n`, `C_E`, `A_4` and the eight additional table quantities before rational floor/ceiling formatting. The added formulas are `L=log(n)`, `d_beta=(17L+27)/n^2`, `M=(4L^2+(79/5)L)/pi^2+9/4+C_E+2K_D`, `U=T-ebar+A_4+23/250`, `d_x=11U/48-5/12`, `d_y=11U/48`, and `ell_x=k_Wx+5/48`, with `ell_y=k_Wy` (one imported constant, `A_4`, is not itself a table row).

Executed independently on Python 3.12.14:

```text
python3 -E -B /tmp/response06-independent-review/check_table_review.py
```

That script separately executed the new CLI with `python3 -E -B`, parsed its JSON, and compared all four degrees with the reconstruction. It also parsed both actual TeX tables independently. Results: **60/60 recomputed output values agree; 120/120 manuscript cells agree**. Eight separate temporary-source controls (malformed, widened, missing and reversed first cell, independently targeting `--paper` and `--companion`) each return exit 1 and `FAIL`; the widened-cell controls explicitly still contain the interval but fail tightness. Separate `-O` and `-OO` invocations both refuse before any verdict with `optimization is not permitted for the exact analytic checker`. No optimization-sensitive assertions occur in the new CLI.

The script's SHA-256 is `6fdfea3e21a9280ed9bbda85ff8b133c501d3f11fb68a850794d73ebf9bdbd90`; it and its JSON outputs are temporary verification material, not claimed deposited artifacts. The durable reproduction command for ordinary use is `python3 -E -B code/onset512_analytic/base_table.py` from the topic directory. `git diff --quiet f4e8d8d -- topics/padua-argmax-bridge-20261105/code/onset512_analytic/check.py` confirmed that the exact API is unchanged. The existing API's mathematical justification is inherited from its prior audit; this review checks the new composition and parsing, not a new proof of that API.

## Layout and final identity

Final coordinator build/control receipts and identities are recorded below. The reviewer first inspected the developer builds at `/tmp/padua-response06-tex-{paper,companion}/main.pdf`: paper pages 16, 32, 42–43, 54, 56–57 and companion pages 84, 107–109, 146 and 150. The provenance lines, table, widened array, custody explanation and companion identification are legible. Table 2 is on paper page 43 before Section 4.4 on page 44, and companion page 108 before the return-to-outputs array/Section 4.4 on page 109. These are visual checks, not an inference from box-warning counts.

### Reviewed source identities

SHA-256 values computed directly from the reviewed bytes:

| Path relative to the topic | SHA-256 |
|---|---|
| `code/onset512_analytic/base_table.py` | `7448c95b6055a34a55d175d3af3732714a5f11d15584baf8f6d2c4b800a92282` |
| `code/onset512_analytic/check.py` | `5ce8cc0701ed105fa619674993583f749046709cb02d233570e2dedc59ca1d2d` |
| `companion-paper/main.tex` | `02adae63f0ef64e4fae0ba394d91596aa8064a8dedd51412b25cbcd730037a7c` |
| `companion-paper/references.bib` | `138871f1d0d1c70a5c753cae8ae2004ba094511c8f3afe031fd2c51210ee39fc` |
| `companion-paper/sections/certification-unified.tex` | `abe7f0541ac18685b4581f7f68a2273cbb76ad21146496eb0627c03b6e2ca2ae` |
| `companion-paper/sections/comparison-unified.tex` | `5e5d9bea84f05ebcf3aa8c650df48365c1ed54b310ac1acd592ef2df7dbb199a` |
| `companion-paper/sections/corner-unified.tex` | `c66c935cd5339a98ea2ad9801c129e503bcddfccfaaf8eaac0b76044ce19e2be` |
| `companion-paper/sections/introduction.tex` | `32d30750c826ad1758c4d9610471b39a61def8c6369d089d273af69b027b82cd` |
| `companion-paper/sections/localization-unified.tex` | `e9f4d10a9c1e20f0ab9871cbdf24fef54a496997c66aa62668ee43bce12b9a37` |
| `companion-paper/sections/preliminaries.tex` | `8e536da1be0c2992443b7dcb4b4b4c680fde6de67d45de79b0ee29a6e39f11b1` |
| `paper/main.tex` | `a9385a32013a73f750018296a0e694119ee8f727938e9b7b2c23de1ae5d8df3a` |
| `paper/references.bib` | `138871f1d0d1c70a5c753cae8ae2004ba094511c8f3afe031fd2c51210ee39fc` |
| `paper/sections/certification-unified.tex` | `42ce059a8dc5983a52a7a553801d038abf49ca50d802d657af4d16b7462d1ff4` |
| `paper/sections/comparison-unified.tex` | `2c9a3fb22f56941df381414f0ac8f44db12bdbca0c172b63d2b76f1983ebd3a8` |
| `paper/sections/corner-unified.tex` | `355ca7fc806551fa9aedd96d6bf513c72d317e09978c0d0835811afddacc076c` |
| `paper/sections/introduction.tex` | `898086d2be870ea56b5619ffa32dedcd1bd6987e2e4df3796aed415fbf5e9916` |
| `paper/sections/localization-unified.tex` | `000d5181a14c63cd0bd8f870d8cb389c9e43b1775080882de6a9c3b3ff36dc2f` |
| `paper/sections/preliminaries.tex` | `54682f1589aac78021899b94a95b0e8cece81dce5d257eea5b1b1bc0a50c5c29` |

The independently captured CLI baseline JSON hashes to `c1df932ee28cd4d89f0b4d378b2453d588c9072840b9f94339fe32b8212b32ef`.

### Final paired freeze and rendered artifacts

The paired TeX/Bib freeze is `36ac77252fb490e58b807767a6bd52f6f3f3dff4`. The coordinator subsequently committed the separate `FINAL_BASELINE` update and base-table CLI in `cc2f9ad10c2b5baf29af1887e681b851e9e9dc60`. A read-only `git diff --exit-code 36ac77252fb490e58b807767a6bd52f6f3f3dff4 --` over both `main.tex`, `sections/` and `references.bib` trees was empty after the final builds. The source hash table above therefore identifies that freeze.

The coordinator executed both final builds; I inspected their logs (`/tmp/response06-final-paper-build.out` and `/tmp/response06-final-companion-build.out`) and final artifact bytes:

| Artifact relative to `/workspace/padua_research/` | Pages | SHA-256 |
|---|---:|---|
| `local-output/padua-argmax-bridge-20261105/audit06-paper-20261114/main.pdf` | 59 | `d978c5fe064421be6f38bb776c29190fbbbc62e3859d15945f29701d61a33ec4` |
| `local-output/padua-argmax-bridge-20261105/audit06-companion-20261114/main.pdf` | 152 | `54245f25277e01dfb4d8d76ea06305b794362fe302db0f6e7361f3193f6dba4b` |

Using PyMuPDF, I independently compared rendered pixel bytes of final paper pages 16, 32, 42, 43, 44, 54, 56, 57 and companion pages 47, 84, 107, 108, 109, 146, 150 to the corresponding developer builds: all match. I also directly viewed fresh final-artifact renders of paper page 42 and companion pages 84, 109 and 146, including the corrected modulus, separated array and explicit evidence limitation. The final logs contain no overfull boxes, undefined references/citations, or badness-10000 **horizontal** boxes; other underfull warnings, including vertical boxes, remain. This is a focused inspection of affected layout, not a renewed examination of all equation tags or unchanged figures.

### Baselines, mutation controls and scan review

I independently executed all three current baseline commands from the companion directory, after the separate baseline-pointer commit:

```text
python3 -E -B check_correspondence.py
python3 -E -B check_correspondence.py --archival
python3 -E -B check_baseline_controls.py
```

All exited 0. Current pairing/freezing gives **19 statements, 86 numbered display environments and 120 labels** against `36ac772`; archival mode separately gives 13/90/113 against its unchanged archival baselines. The seven committed controls pass: paired theorem quantifier, numbered formula, unnumbered formula, bibliography, extra TeX file, main preamble and companion-only statement mismatch. I also independently parsed the final `.aux` files: **120/120 label numbers match**.

I reviewed the coordinator's executed nine-type mutation harness and `/tmp/response06-mutations.jsonl`, rather than claiming a separate rerun of that harness. Its 13 scenarios comprise two passing controls (`S0` unchanged, `S7` README-only) and eleven actual source mutations, all rejected by the strict source baseline. A direct normalized comparison confirms that `/tmp/response06-mutation-harness.py` differs from the committed audit-06 harness only in `HEAD` and `BASELINE` assignments. Its SHA-256 is `895658d2c8dbeeb91007bf5aacb1c181268b4436a26255990bcde707f9e6c0c1`. The coordinator's command was the harness invocation on this repository and a fresh scratch output tree; the checked output identifies the current freeze in its passing baseline row.

The observed paired constant, quantifier, numbered-display and unnumbered-display edits pass pairwise equality but fail the independent source freeze, as required. The extra TeX, bibliography, main-numbering, one-sided statement and prose edits also fail. A real paired rename passes the rename-aware scanner only with its map; the false constant-as-rename control also passes that scanner with its fake map. This preserves the documented limitation: a rename map needs semantic review, and scan agreement is not mathematical certification. Strict source freezing rejects both variants.

The final scanner output `/tmp/response06-notation-final.stdout` passes against `36ac772` with the empty incremental map. Against the preceding `8937d3b` freeze, `/tmp/response06-notation.stdout` flags exactly `cert:finite-verification` (redundant wording removed) and `ul:charts` (period changed to comma), in each manuscript. I inspected those diffs. No numbered mathematical symbol was renamed; the `w_r`/`v_r` repairs are unnumbered prose/formula edits and were reviewed semantically above.

**Final disposition:** accepted within this bounded supplementary scope, with the one returned modulus clarification resolved and reread. No unresolved finding in the reviewed delta. No missing historical artifact, current witness output, native-history custody, global storage-budget decision or publication placeholder is closed by these checks; no readiness or Claude-audit completion is claimed.
