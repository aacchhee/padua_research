# Supplementary manuscript response-05 review — 2026-11-13

## Identity and scope

Rules read at `520b3645a4b8a584cb17eddc64defb97747cb253`: `AGENTS.md`,
`agents/WORKFLOW.md`, `agents/codex/CODEX.md`. This is the distinct Codex
supplementary reviewer, dispatched as **gpt-6-astra, high**; serving model and
effective effort metadata are runtime-unexposed. It supplements, and does not
replace, the required focused Claude handoff.

Inputs: handoff 33; audit-05 and audit-05-manuscripts; the detailed M5A, M5B and
B5 reports; the blocked-input instructions; the response working tree against
`520b364`. Only this report is reviewer-owned. No source edits, Git mutations,
native runs, new scientific campaign, or novelty claim were made. The novelty
gate does not apply: the task is a bounded review of requested repairs to
existing arguments, notation, exposition and evidence-status wording.

The review reads both actual texts, including each changed analytic clause,
rather than inheriting the response-04 dispositions. Source owners supplied
stable-file notices; final source hashes are recorded below. Source agreement
is a syntactic control, not a mathematical proof or an evidence-custody check.

## Analytic reconstruction

1. **Collision consequence.** In the endpoint range, the unwrapped actual
   offset `(1-s±xi)/2+nu/(2m)` is positive and less than two. An integral value
   therefore forces one of `x-y`, `y-x`, `x+y` to equal `pi-v`, hence
   `rho >= pi-v`. The old implication for `|x-y|` is false. Since
   `a=(P/2)cot(rho/2)` and `0<v<pi/2`, the corrected consequence gives
   `a <= (P/2)tan(v/2) <= Pv/2`; the charge is unchanged. Independently running
   `s8_collision.py` reproduced all six old-clause counterexamples at
   `n=32,192,512`, `j=2,3`. For example, `n=512,j=2` gives
   `|x-y|=2.3301 < pi-v=rho=3.1301`, with cosine collision to displayed
   floating-point precision. This execution corroborates the counterexample;
   the offset algebra supplies the reason for the repair.
2. **Three formerly lost clauses.** The companion now defines
   `tau(w)=w cot(w)`, including its continuous value, before the reference
   ledger. Substituting `v=pi*nu/m` verifies the normalized prefactor
   `2a*tau(v/2)/(pi^2*nu)`. The wrap recurrence, the lower denominator
   `3(j-1)/4`, and at most two wraps give `8P/(3*pi*m*(j-1))` per row;
   summing both endpoint sides gives the displayed harmonic charge.
   Differentiating `4a log sin(t/2)` gives `T_t=2a cot(t/2)`.
   Cauchy–Schwarz gives `A cos x+B sin x <= sqrt(A^2+B^2)`, and the
   positive coefficients allow the stated attained minimum. These are now
   present in the actual companion, not merely claimed retained in a ledger.
3. **Endpoint envelope and domination.** The new decomposition is an exact
   subtraction of `U_0/t`. The earlier scalar lemma gives `1/2<f<=1`, so
   `|N_s|<=c_e+c_d<=2<=8`. The Lipschitz bound gives the stated `12t/pi`;
   `12/pi<6`. The chord and Taylor remainder give
   `0 <= 1/(2sin(t/2))-1/t <= pi*t/48`. Thus the deliberately loose
   `6+pi*t/6` and then `6+pi^2/24+1/pi<7` follow. The coefficient displacement
   has exactly the displayed `P/pi` envelope. The two max-subtraction
   differences are bounded by one, and the remaining cotangent subtraction
   is uniformly bounded, so the stated phase-independent domination follows.
   The companion now states the cosine chord's concavity reason, the
   alternating first-omitted-term rule, and the scalar amplitude step.
4. **Restored corner reasons.** The unit-cell trapezoid kernel has maximum
   `1/8`; integrating `2(z+t)^(-3)` gives `1/(8z^2)`, uniformly in the cutoff.
   The recurrence `psi(y/2)=psi(1+y/2)-2/y` yields the stated endpoint
   `A_1(0)=pi-a*d_0`. The midpoint-cell bound sums to `1/(3r^3)` for real
   `r>=1`, so the restored half-integer derivative estimate has the stated
   uniform scope. The temporary limit is now `kappa_infty`; the orientation
   pairing identifies it with the defined kappa before `cu:kappa` is asserted.
   The later uniqueness-of-limit argument explicitly cites that result.
5. **Other changed analytic clauses.** The row kernel now cites the actual
   divided-difference display; `cos(nu)=(-1)^delta_r cos x` explains its
   constant cancellation. The corner-axis use of `q_h` has its nonnegative
   multiplier and positive lower bound stated; the diagonal chain cites its
   three premises. The Peano dummy-variable changes leave the nonnegative
   double integral and its `1/3` mass intact. The parity/sign clause, monotone
   tangent step, and origin-sum wording reconstruct without changing constants.

## Finding-by-finding dispositions

Here **FIXED** concerns the reviewed text or stated check only. It does not
mean absent evidence has been recovered or publication requirements completed.

| Finding | Reviewed disposition and limits |
| --- | --- |
| M5A-01 | **FIXED, material clause reviewed.** Both texts use `rho>=pi-v` with the three possible equalities; the comma splice is gone. Reconstruction and counterexample execution above. |
| M5A-02 | **FIXED.** Companion prefactor/tau, explicit per-row wrap charge, logarithmic primitive and amplitude inequality all restored. The dated correction in the earlier supplementary review withdraws its B5/C1/C10 retention claims for ad908acb. |
| M5A-03 | **FIXED.** Chord, first-use numerator bound, pole decomposition/sum to seven, alternating remainder, max-subtraction, amplitude and concavity reasons checked in the actual text. |
| M5A-04 | **FIXED.** Both files consistently use `vartheta_m` for the outer width and preserve `h_j(t)` for the series. Searched all occurrences and reviewed products, powers, interval endpoints and `uc:signed-outer`; no `h_m` residue remains. |
| M5A-05 | **FIXED within the listed scopes.** Paper uses `e_rho`, `Delta_x`, `e_c`, `r_hl`, `r_c`, lambda; the half-amplitude is explicitly `w_r`; companion table lists its separate role. Companion logarithms use `eta_log,+/-`, the half-angle differentiation uses chi, and central differentials use `de_c`. The paper's factor-four looseness note is present. This is not a claim that every locally reused symbol in the manuscripts has been globally renamed. |
| M5A-06 | **FIXED.** Before the companion ledger, the four absolute allowances point to `uc:phase-allowance`, and `B_out` points to the actual-origin estimate. These are explicit forward pointers, not earlier definitions. |
| M5A-07 | **FIXED in source; rendering recorded below.** The row figure and worked table are beside the decomposition, labeled/cited in both texts, with direct floating-point provenance and no proof-input claim. Arrows run pole-to-right-sample; the sample label is anchored to a dot. |
| M5A-08 | **FIXED.** Merge artifact and dangling sentence removed; positivity supplies the first equivalence, parity the second. |
| M5A-09 | **FIXED.** Shared `eq:kernel-evaluation` added and cited, cancellation reason supplied in both comparisons. This intentionally adds one numbered environment and shifts later equation numbers. |
| M5A-10 | **NOTE retained.** The unnumbered bounds `317+5/12` and `318` remain different and valid; both use the same final allowance. No unnecessary equalization or threshold change. |
| M5B-01 | **FIXED wording; evidence remains OPEN.** Both certification sections explicitly say the onset return and independent evidence bundle are unavailable, four data-only witness checks remain open, and 632 MiB history custody is unverified. Inventories describe past computation, not custody. Remaining “retained” occurrences concern mathematical terms, vertices, leaves or arithmetic representation, not availability. |
| M5B-02 | **FIXED.** Companion explicitly proves Theorem 1.1 by the analytic theorem and finite proposition; physical corners and both abstract qualifiers are present. |
| M5B-03 | **FIXED.** The trust row says the error bound is derived under the **assumed IEEE model**; binary64 semantics remain implementation trust. No model-proof claim is inherited. |
| M5B-04 | **FIXED.** All six detailed subitems reviewed: trapezoid bound, recurrence, half-integer derivative statement, kappa citation, temporary limit name/identification order, and correct order of the psi derivations. |
| M5B-05 | **FIXED, with table-coverage correction below.** Both tables follow Corollary 4.7, label/reference their definitions, explain exact-API provenance and exclusion from the old receipt. Independently checked all 60 actual entries in each text. The exact checker now explicitly asserts `log(PI).lo>11/10` and ran successfully. |
| M5B-06 / B5-01 | **Source FIXED; rendered assessment below.** Paper Figure 2 now has the companion's white-filled label/arrow placements. |
| M5B-07 | **FIXED wording.** Paper unit roundoff and node weight precede use; both ratio formulas use xi and `u_+/-`; unexplained I25 replaced with “independent phase checker.” Snapshot limitation is B5-04 below. |
| B5-02 | Six paired display splits reviewed algebraically; final rendered check below is required. Absence of overfull warnings alone does not establish this fix. |
| B5-03 | **FIXED.** Companion explicitly defines the alternating arctangent partial sums and displays the correct Machin bracket, reversing the bounds for the subtracted term. |
| B5-04 | **HONEST PLACEHOLDER, not publication-complete.** Both data statements say the permanent post-repair snapshot is being prepared and DOI is pending; a433c7d is no longer presented as the current snapshot. The snapshot/DOI and archive retrieval remain open. |
| B5-05 / B4-09 | **Source FIXED; rendered assessment below.** Both roles arrays have explicit quad intercolumn spacing. |
| B5-06 / B5-07 | **Integration controls, outside this mathematical verdict.** Root owns the new freeze, baseline, rename map/scanner and mutation-control record. This review does not substitute paired agreement for preservation against a baseline. |
| B5-08 | **Historical correction retained.** The auditor's dated report addendum distinguishes 942 records from 471 trees; no blanket new custody claim is made. |
| B5-09 | Source repair included with M5A-07; rendered assessment below. |
| B5-10 | **FIXED.** Companion explicitly says “last two rows of Table~ref{cert:coverage}”; the count is 942 records of 471 distinct trees. |
| B5-11 | **NOTE retained.** Bibliographies are byte-identical and unchanged, 26 entries; different trust-table grouping remains consistent. No new bibliographic web verification or Pimenova-ID verification is claimed. |
| B5-12 | **AC-reserved, unchanged.** AI declaration, draft marker, ORCID, contributions and funding were not edited or approved by this review. |
| M5B-E1–E6 | **FIXED within requested wording.** Tree-norm splice, duplicate inward-phase sentence, corner reasons/citations/dummies, duplicate derivative claim, companion `d_r` weights, and explicit companion arithmetic-derivation pointer all checked. M5B-E7 is a permitted table-structure difference. |

### Finding returned during this review

The first response draft followed M5B-05's recommendation by citing the base
table directly after `F_h(295)>50064/10^6`. The table contains no `F_h` or
`floor295` entry, and its coefficient values do not establish that rational
floor computation. I returned this misleading pointer to the noncomparison
source owner. The owner removed it in **both** localization files; I reread
both corrected passages. Gate and corner-256 references remain. This is a
scoped correction of the earlier audit recommendation, not a lost table fix.

## Executed checks

Environment: Python **3.12.14**, NumPy **2.3.5**, mpmath **1.3.0**. Read-only
Git commands were `rev-parse`, `diff`, and file inspection against input HEAD.

- `python3 -E -B audit-05/code/m5a-code/s8_collision.py`: six counterexamples
  reproduced, with the corrected rho bound and amplitude inequality satisfied.
- `python3 -E -B code/onset512_analytic/check.py`: exit 0, exact-Fraction
  receipt reports PASS; this includes the new explicit logarithm assertion.
  No claim is made here about independent implementation of its interval API.
- `python3 -E -B audit-05/code/m5b-code/base_table.py`: reran the existing
  audit implementation. Separately imported its `consts`/`contains` functions,
  parsed the **current TeX** table rows, and checked each of 60 printed
  intervals in each text using its 80-digit mpmath interval implementation.
  **120/120 containments passed.** The separate implementation is the prior
  audit's, independently executed here, not newly authored by this reviewer.
- Imported the current correspondence helper and directly invoked
  `compare_pair(current_sources(paper), current_sources(companion-paper))`:
  **19 statements, 86 numbered environments, 120 labels PASS**, including
  equal headings, setup/counters, section file sets and bibliography.
  This deliberately checks the unfrozen response working tree without
  pretending its old `FINAL_BASELINE` already matches.
- Full response TeX diffs read; scoped searches checked first definitions,
  custody language, obsolete local names, all changed products and subscripts.

The first attempt to locate the correspondence helper under `paper/` failed
with file-not-found; its actual location is `companion-paper/`. This had no
effect on the successful import and check above.

## Rendered checks

The orchestrator built the final sources; I independently opened these actual
PDFs with PyMuPDF 1.26.6, obtained tag locations from their final aux files,
rendered crops and full pages, and inspected the images. I did not perform the
root build itself. Scratch images are in
`/tmp/padua-response05-manuscript-review/` (not committed or an archival deposit).

| PDF under `local-output/padua-argmax-bridge-20261105/` | Pages | Bytes | SHA256 |
| --- | --- | --- | --- |
| `audit05-paper-20261113/main.pdf` | 58 | 798493 | `1dc50b84b6ac6a7d92300370dde5e95b867b4e428708883c291d2b4cd089c657` |
| `audit05-companion-20261113/main.pdf` | 152 | 1215607 | `9bd922db9599a46577fe5af5a19499e96f338946ad7b5a7c55f79210e5809a1c` |

**B5-02 FIXED in the rendered pair.** All twelve inspected numbers sit beside
the corresponding multiline blocks. None is an own-line fallback below its
formula. The increased numbering follows the new kernel-evaluation equation.

| Label | Old number | New number | Paper page | Companion page |
| --- | --- | --- | --- | --- |
| `cu:D` | 11 | 11 | 9 | 24 |
| `cu:row-expand` | 20 | 20 | 14 | 39 |
| `ul:charts` | 25 | 26 | 16 | 47 |
| `uc:completed-model` | 39 | 40 | 23 | 64 |
| `uc:scalar-constants` | 50 | 51 | 26 | 71 |
| `uc:uniform-allowance` | 54 | 55 | 28 | 74 |

Also visually inspected:

- **B5-01 / M5B-06:** phase figures, paper p18 and companion p51; the
  hypotenuse does not cross either revised label.
- **B5-05:** roles arrays, paper p17 and companion p51 (also context p50);
  columns have visible spacing and their degree conditions are readable.
- **B5-09 / M5A-07:** row figure/worked table, paper p29–30 and companion p77;
  both arrows are visible, eta-minus is attached, and `u_rk` labels a dot.
  The figure/table are next to the row decomposition, with explicit captions
  and proof-input limits, not sixteen pages later.
- **M5B-05:** base table and preceding provenance, paper p42–43 and companion
  p107–108; the table is legible, after the relative-gate definitions/proof,
  and the API-versus-receipt qualification is rendered. It is Table 2 in both
  texts after the new worked-values Table 1.

These are the enumerated renders, not an exhaustive inspection of 210 pages.
No layout DECISION accepting the old six fallbacks is needed.

## Source identity and remaining limits

**Supplementary verdict: the requested changed analytic clauses and the
listed rendered repairs are accepted within this scope.** The sole new
minor pointer finding was returned to its owner, fixed, and reread in both
texts. Final paired-source control was repeated after that correction and
again passed 19/86/120. The honest snapshot/DOI placeholder and evidence
retrieval limitations remain as stated above. Root's freeze, baseline,
scanner and mutation record must accompany this report.

Analytic/source reconstruction above found no unresolved mathematical finding
in the changed clauses. It does not rerun
the unavailable witness bundles, establish history custody, prove the IEEE
model, certify unchanged manuscript arguments afresh, or confer PR readiness.


### SHA256 of reviewed final TeX/Bib sources

Paths are relative to this topic. These identify the working-tree inputs
reviewed here; root records their eventual freeze commit separately.

| Source | SHA256 |
| --- | --- |
| `paper/main.tex` | `060786ff62873361600a543eba7acdac2c183c340943a9831c525e8309fe4923` |
| `paper/references.bib` | `138871f1d0d1c70a5c753cae8ae2004ba094511c8f3afe031fd2c51210ee39fc` |
| `paper/sections/certification-unified.tex` | `b3f0099dd340e12bbddd8238c7789b42d699333eac25b4b99d16d0b30a492ad4` |
| `paper/sections/comparison-unified.tex` | `8c57a0a97b814556b221df6bd4ab68390af930902aa20211a1ad8da85ea9674e` |
| `paper/sections/corner-unified.tex` | `355ca7fc806551fa9aedd96d6bf513c72d317e09978c0d0835811afddacc076c` |
| `paper/sections/introduction.tex` | `898086d2be870ea56b5619ffa32dedcd1bd6987e2e4df3796aed415fbf5e9916` |
| `paper/sections/localization-unified.tex` | `bed0dcbd3d64415e09d8c20f2099ebbeabe6ffe8815f447d9b93077f2128ea76` |
| `paper/sections/preliminaries.tex` | `54682f1589aac78021899b94a95b0e8cece81dce5d257eea5b1b1bc0a50c5c29` |
| `companion-paper/main.tex` | `40cea7c559d04b434d7840a472523b036b7ee83dc6d06fb0d0109c085f775f03` |
| `companion-paper/references.bib` | `138871f1d0d1c70a5c753cae8ae2004ba094511c8f3afe031fd2c51210ee39fc` |
| `companion-paper/sections/certification-unified.tex` | `4dcdb37ddaf7ada7a856d9ae0812a7730974e5987ee81ffa756b04aaf3b2e440` |
| `companion-paper/sections/comparison-unified.tex` | `c31e6a714563ad126eff9f3554d879ed8aca701fc21385ed1699dfc683059812` |
| `companion-paper/sections/corner-unified.tex` | `d5370dfbdc55adc83c5fd6bdea2d5c7fda7894b2aadbc16f31c1ea6d0caea919` |
| `companion-paper/sections/introduction.tex` | `32d30750c826ad1758c4d9610471b39a61def8c6369d089d273af69b027b82cd` |
| `companion-paper/sections/localization-unified.tex` | `bc187e0b1f22486ca858a23d3913a4a0c3aa672efa11cf2788589763331b3dac` |
| `companion-paper/sections/preliminaries.tex` | `8e536da1be0c2992443b7dcb4b4b4c680fde6de67d45de79b0ee29a6e39f11b1` |
| `code/onset512_analytic/check.py` | `5ce8cc0701ed105fa619674993583f749046709cb02d233570e2dedc59ca1d2d` |


## Final freeze and baseline follow-up — 2026-11-13

The final reviewed TeX/Bib sources are now committed at
`8937d3b723c09c004f49d3e565d0b02976713a37`. I independently inspected the
subsequent helper diff: its only change is `FINAL_BASELINE` from ad908acb to
that source commit. A read-only `git show` confirms that the helper **inside
8937d3b still points to ad908acb**. Thus the source commit precedes the separate
pointer update; the latter was still uncommitted when inspected. No TeX was
changed in this follow-up.

Independently executed from repository root (all exit 0):

```sh
python3 -E -B topics/padua-argmax-bridge-20261105/companion-paper/check_correspondence.py
python3 -E -B topics/padua-argmax-bridge-20261105/companion-paper/check_correspondence.py --archival
python3 -E -B topics/padua-argmax-bridge-20261105/companion-paper/check_baseline_controls.py
```

- Default: source freeze **8937d3b**, paired headings, **19 statements / 86
  numbered environments / 120 labels**, bibliography PASS.
- Archival: historical source pair c6e195f/ac94504, **13 / 90 / 113**, PASS.
  This is archival source verification, not verification of absent original
  PDF bytes.
- Baseline controls: **7/7 PASS**, including paired theorem quantifier,
  numbered formula, unnumbered formula, bibliography, extra TeX file, main
  preamble text, and a companion-only statement mismatch.
- Current correspondence helper SHA256:
  `a3cff22b4151b606ebebfe2dd5dda0e98c61e24402c71eab65cbed6a0c2fafbd`.
- Unchanged baseline-controls helper SHA256:
  `ef474bb594d65abf5219e1574fabc2e2acdf3bd53ec344d555afa9ece408e309`.
- Recomputed final PDF hashes still equal the two hashes in the rendered
  checks above.

The root's cumulative rename-map/scanner and content-alignment results were
reported to this reviewer; they were **not independently rerun in this
follow-up**. Their structural/material differences must remain visible in
root's integration record, rather than be hidden by permissive renames.
These successful preservation controls do not broaden the analytic review
or resolve the snapshot, DOI, witness retrieval, historical-PDF or custody
limitations recorded above.
