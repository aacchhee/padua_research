# Audit 01 — MZ prior-art and fulltext closure

**Verdict: CHANGES REQUIRED; stage WORK.** No P1 finding or refutation of an existing PD theorem was established. This is not historical novelty clearance. Several primary pages could not be independently obtained, so this audit does not certify every literature verdict as verified.

- Candidate: `4f937137f9baac5e51814964e6a83aeb2df38815`, branch `claude/mz-prior-art-20261101`, PR #11.
- Base/current main checked: `9739a0c56b7a3976422ce60a8441bfbbfd6554df`.
- Auditor: Codex, requested allocation `gpt-6-astra`, high; three bounded independent source checks used the same explicit allocation. Resolved runtime model/effort metadata is not independently exposed. This Codex audit is distinct from Claude development.
- Rules read at candidate: AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md; unchanged rules were first read at base. Date: 2026-11-01, Europe/Oslo.
- Complete `state/IDEAS.md` read, lines 1–457, including every obstruction/disposition table. Full relevant M1/M2/M3 candidate records and the linked endpoint/weight theory were inspected. Literature INDEX was read before source inspection. No new mechanism, PD status change, or final-ID allocation was made by this audit.

## Findings requiring a developer response

### F1 — P2: T4 deletes a factor from its own smoothed-weight definition

Location: `topics/mz-prior-art-20261101/translation.md:38–42`; propagate to comparison row 7, line 28.

The displayed definition is `w_n(x)=Delta_n(x)^(-1) integral_(x-Delta_n)^(x+Delta_n) w`. For w=1 it equals **2** in the interior, rather than 1; truncating the interval to [-1,1] makes it lie between 1 and 2. The proof deletes this factor while retaining the same C that the proposition calls the Mastroianni–Totik source constant. With that meaning of C, the argument yields denominator `16 pi^2 M^2 C`, rather than `8 pi^2 M^2 C`.

Fix by defining a specialized constant `C_CC=2 C_source` before stating the consequence, or retaining the factor 2 throughout. Explicitly choose admissible M>=1 before the proposition; enlarging M preserves the source's upper-gap implication and the floor argument is then sound. The qualitative small-ratio implication survives. Source-theorem fidelity to the original pp.65–66 remains unverified in this audit because that fulltext was inaccessible; this normalization finding is independently visible in the submitted formulas.

### F2 — P2: manuscript excludes content in explicitly unread Sloan–Smith pages

Location: `tracks/mz-constants/paper/manuscript.tex:161–166`; related overstatement in `topics/mz-constants/literature-search.md:174` and report.md's “Threat removed” row.

The manuscript says full texts were inspected and jointly asserts that LIT-047 and LIT-048 contain no quadratic-form or nodal l2 estimate. The LIT-048 source record explicitly says only pp.387–388 were read, pp.389–401 unread, and keyword screening still pending; its bibliography note agrees. Neither the title nor publisher summary establishes an exclusion across those unread pages. Comparison line 37 correctly preserves the unread qualification, so the manuscript and summary must match it.

Either inspect the remaining pages or narrow the claim to the inspected portion and keep the remaining content unresolved. Use source-specific coverage rather than a collective fulltext claim. Also avoid grouping Lubinsky's survey solely under uniform norms/Sobolev inputs/matrix problems (manuscript:201–207): its recorded converse quadrature-sum theorem is a genuine nodal-norm result in a different node/weight setting.

### F3 — P2: König–Nielsen's recorded critical exponent omits a parameter restriction

Location: `literature/records/mz-prior-art-2026-additions.md:20`.

The record gives `M=4(alpha+1)/(2alpha+1)` for alpha>-1/2 without restricting beta. The primary arXiv Theorem 1, pp.3–4, defines the endpoint using both parameters; the alpha-only expression in its necessity proof, p.15, assumes alpha>=beta. For example alpha=0,beta=1 gives the recorded endpoint 4, but the correct endpoint is 8/3. Add the ordering assumption or use `a=max(alpha,beta)` and the appropriate infinite-endpoint convention when a<=-1/2. The table's same-weight versus mixed-weight distinction is still supported.

Primary: [König–Nielsen, arXiv math/9208201](https://arxiv.org/pdf/math/9208201), Theorem 1 and eqs.(18)–(19).

### F4 — P2: scope the classical-attribution inference to the setting actually established

Locations: `topics/mz-prior-art-20261101/comparison.md:54–60`, `tracks/mz-constants/paper/manuscript.tex:178–187,845–848`, and the report's endpoint-classical summary.

The comparison correctly says Mastroianni–Russo is a Gauss-node statement without endpoint terms, then broadens that evidence to qualitative failure at “Chebyshev/Lobatto-type” nodes. The manuscript's “Thus” sentence links that Gauss criterion to the specific CC full-sequence limit. This requires a transfer argument: adding endpoint observations changes the norm problem, and failure of a uniform bound alone gives an unbounded subsequence rather than automatically a limit along every N.

König–Nielsen also does not directly supply the precise Lebesgue-L2 U-polynomial attribution: its U specialization alpha=beta=1/2 is critical at p=3 with continuous weight sqrt(1-x^2), giving log^(1/3) norm growth; at p=2 the same-weight Gaussian quadratic form is exact. It supports an analogous classical Jacobi borderline mechanism. The claimed mixed-weight Mastroianni–Russo proof was not independently accessible here.

Separate these assertions explicitly. State the classical result with its Gauss/mixed-weight or same-weight hypotheses, then attribute the CC limit to the written exact CC evaluation of U_(N-1), which gives Q_N(U^2)=O(1) and integral U^2 asymp log N. If claiming the precise CC conclusion itself was previously established, cite and verify a source or write the missing transfer. This does not challenge the manuscript's independently proved CC limit or its squared-logarithm theorem.

## Smaller corrections

- **N1, P3 — angular orientation and constants:** translation.md:38 lists x_j increasing but xi_j=arccos x_j and positive gaps xi_(j+1)-xi_j. Use absolute gaps or reverse the angle difference; otherwise the upper-gap assumption is vacuous and lower-gap assumption impossible. The same error occurs in the LIT-051 source summary. At translation.md:22, norm/eigenvalue comparison constants are reciprocally squared, not literally the same constants.
- **N2, P3 — T5 endpoint hypothesis:** translation.md:50 should choose `c=N^-2` and check Lubinsky (1.31). c=0 fails at Lobatto endpoints; fixed c>0 does not justify the displayed near-endpoint equivalence. With c=N^-2, positive delta_j asymp sin(theta_j)/N at interior nodes, endpoint delta_j asymp N^-2, and endpoint derivative magnitude 2N, the stated coefficient inflation N^(2-4 sigma) is correct. Keep the conclusion limited to the direct fixed-sigma specialization; no tracked optimization as sigma approaches 1/2 is supplied.
- **N3, P3 — compressed source cells:** comparison.md:45 should call Don–Gottlieb H a pullback of the **discrete GLL energy**, not an exact continuous L2 mass identity on Pi_N. GLL exactness through degree 2N-1 does not integrate every p^2 in degree 2N. The different-setting verdict survives. Line 44's Widom–Wilf rate drops the boundary-case qualification already present in its record; omit the unnecessary rate or preserve its regime and unread-erratum qualification.
- **N4, P3 — current reading status:** INDEX LIT-063 and refs.bib still say the 1990 letter is unread although the final addendum reports it read. INDEX's new block says three additions but has six. Update current summaries while retaining historical dated records.

## Translation assessment

T1: accepted, exact inverse of evaluation/interpolation on V_n with positive CC weights. T2(a,b): accepted with the stated numerical square root; T2(c)'s containment and DCT hyperplane constraint are correct, and containment alone does not transfer a full-space growth witness to degree N-1. This audit has not proved a separate transfer theorem. T3: accepted from PD-T017's weight bounds, including both endpoints; both weight-transfer directions are correct. General weight comparability preserves orders but supplies no sharp threshold below 2.

T4: the floor choice, degree inclusion, gap size, and Delta comparison are valid after F1/N1. Because the proof chooses M>=1, its stated window lies within n/N<=1/pi<1/2, where elementary CC exactness already yields both extrema equal to 1. It is a conservative historical consequence, not evidence of a nontrivial beyond-half-exactness window.

T5: Lubinsky's author manuscript, PDF pp.1–7, independently supports the open exponent range and nodal coefficient; journal p.583/version identity was not separately verified. The nodal polynomial, interior derivative magnitude N, and exponent 4 sigma-2 are correct. N2 supplies the omitted endpoint specialization.

## Every comparison row: independent coverage

Row numbers count the 29 data rows, starting at comparison.md:22. “Selected” verifies the identified statement/setting, not all proofs or absence of all other results. “Limited” uses only an abstract, predecessor version, or partial text. “Unavailable” is not acceptance or rejection of the developer's reading report.

| Rows | Source / claims | Independent disposition |
|---|---|---|
| 1–2 | Nevai III, uniform-input theorems and property (g) | Original pages unavailable. A 2012 primary paper corroborates attribution of a forward inequality to p.675, but does not replace inspection of Nevai's hypotheses. |
| 3 | Mastroianni–Russo Thm2.7 | Original theorem/necessity pages unavailable; endpoint substitution checked conditional on the printed statement. F4 limits propagation. |
| 4 | König–Nielsen | Selected primary pp.2–4,15 support same-weight/Gauss distinction; F3/F4 apply. Journal version not compared. |
| 5–6 | Lubinsky 1999 | Selected author manuscript Thm1.7 supports open-range/norm-direction distinction, subject to N2. Published version unavailable. |
| 7–9 | Mastroianni–Totik | Original pp.65–66 unavailable; conditional local translation checked, F1/N1 apply. Small-ratio context corroborated by Lubinsky's introduction. |
| 10–11 | Lubinsky–Mate–Nevai 1987 | Publisher abstract supports forward quadrature-sum focus; exact Thm5 p.534 and absence of converse results not independently verified. For fixed l, C may depend on l; it is not uniform over all l. |
| 12 | Askey 1972 | 1969 primary report supports Gauss/continuous-input distinction; corrected journal theorem/range unavailable. |
| 13 | Smith 1986 | Selected primary pp.375–379 directly support uniform-input/Chebyshev-measure distinction. |
| 14 | Erdos–Feldheim | Original scan pp.913–915 supports even-power mean convergence in Chebyshev measure; preceding-note conventions unresolved. |
| 15–16 | Sloan–Smith 1978/1980 | Publisher summaries support functional/error-estimator settings; original auxiliary estimates not independently verified. F2 applies to LIT-048. |
| 17 | Lubinsky survey | PDF gave no inspectable text/images; body theorem and Xu pointer unverified. |
| 18 | Xu I/II | Original bodies unavailable. Algebraic substitution in stated (3.2c) gives (1-x^2)^-1, but original sufficient hypotheses unverified. |
| 19 | Nevai 1990 | Developer's final reading report reviewed; original letter unavailable, so theorem-preservation claim not independently verified. |
| 20 | Sloan–Smith 1982 / Smith–Sloan 1980 | Primary abstracts support functional/mean-convergence context; exact theorem equivalences not independently verified. |
| 21 | Mastroianni–Milovanovic book | Chapter4 abstract supports uniform-norm result; ch2/ch5 bodies and all-chapter exclusions unverified. |
| 22–23 | Widom / Widom–Wilf | Original bodies inaccessible; basis-dependent ordinary versus Gram eigenproblem distinction is mathematically sound. Rate/erratum not verified; N3 applies. |
| 24 | Don–Gottlieb | Selected NASA report pp.3–4,7–8 verified; N3 corrects its energy identity. Journal version unverified. |
| 25 | Niu et al. | Primary article mirror p.3 Lemma1 eqs.(2)–(3) verifies Sobolev-input distinction. |
| 26 | ASV numerical/Gaussian results | arXiv v1 and author PDF support numerical predecessor, Gaussian result, and its own open-question wording. Published p.738/version comparison unavailable. |
| 27 | ASV eq.(7) | Primary arXiv selected text verifies the upper-Gram factor with aliasing term. The unrestricted upper-only theorem is an elementary extension, not literally the source's full hypothesis set. |
| 28 | An–Wu | arXiv v3 Cor4.1 and count convention verified; m=513,n=511 is in range. Published version comparison/correction search not independently closed. |
| 29 | Forward-citation screen | Selected primary abstracts/sphere introduction support the recorded scope distinctions. Historical citing-list totals and exhaustive coverage not rerun; Wu AML body unread. |

Exact URLs, page coverage, access failures and independent calculations are retained in [translation check](audit-support/translation-source-check.md), [primary comparison check](audit-support/comparison-primary-check.md), and [other comparison check](audit-support/comparison-other-check.md). No third-party fulltext is included.

A further primary lead found during verification is Mastroianni–Milovanovic–Notarangelo (2012), *On an interpolation process of Lagrange–Hermite type*, DOI 10.2298/PIM1205163M, [author PDF](https://www.mi.sanu.ac.rs/~gvm/radovi/n105p163.pdf), Cor2.2 pp.166–167. It treats interior Jacobi nodes plus endpoint data and is closer to the qualitative Lobatto question. Endpoint-parameter hypotheses need page-image checking before importing the specialization; no quantitative critical rate or degree-N-1 implication is established by this audit. Record as a follow-up lead, not a subsumption finding or a newly allocated LIT ID.

## LIT reservation and integration check

Checked main above; PR #10 source `a2dd845b8a231e1b00733e1361e2a9ad3bad222f`; PR #6 source `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e` as returned by the current open-PR listing. PR #10's ledger records its AC-authorized block LIT-066–292, and its INDEX has all 227 distinct IDs. PR #11's six distinct IDs are exactly LIT-293–298; no overlap. The next free LIT is **299** after both reservations. The other next ranges remain PD-T081, PD-N032, IDEA-177. This confirms arithmetic and registry consistency; it does not impersonate the historical allocation owner's separate assent or recreate AC's original authorization message.

Only three changed paths overlap PR #10: literature/INDEX.md, literature/CORPUS.md, and the batch ALLOCATIONS.md. Independent `git merge-file -p` checks against base merge each without textual conflict. The INDEX union preserves both blocks. This was a three-file text check, **not** a full sequential squash-integration rehearsal. Semantic work remains: PR #10's historical “next LIT-293” and PR #6's current next-free advice must not drive a new allocation after this reservation. Preserve both ledger sections and use LIT-299 on subsequent allocation; obtain the named owner's confirmation if still required by the recorded delegation. No ID was assigned or renumbered by the auditor.

## Executions, provenance and residual risk

- Fetched all 21 PR-changed files plus candidate AGENTS.md, CODEX.md and IDEAS.md, and separately WORKFLOW.md, through connected GitHub tools at the exact candidate. Their returned Git blob identities were checked against local bytes; [input manifest](audit-support/input-manifest.json) records the full fetched list, hashes and additional base inputs. Base theory/candidate files were read from the existing clean checkout at main; they are unchanged by this PR. Network Git fetch failed because its proxy was unreachable; no alternate revision was silently substituted.
- Independently executed `pdflatex`, `bibtex`, `pdflatex`, `pdflatex` against candidate manuscript.tex and refs.bib. BibTeX was run from the output directory with absolute BIBINPUTS (initial absolute-output invocation was rejected by TeX's openout policy, then corrected). Final PDF: 17 A4 pages; final LaTeX/BibTeX logs contain no warnings, undefined references/citations or overfull/underfull boxes. Build artifacts stay local at `/workspace/pr11-audit/build`.
- Executed unique-ID/range checks and the three-file text merge above. Reviewed diffs: no PD theorem/proof/registry status change in this PR. No numerical suite was rerun: the changed claims are literature comparisons and translations; the existing numerical evidence is not re-certified here.
- Inspected sources independently where available; did not count developer summaries, publisher metadata, failed screenshots or AC's unavailable institutional PDFs as page verification. No claim that every comparison is independently closed. No public contact, submission, merge, force push or tag operation was performed.

Developer next step: answer F1–F4 and N1–N4 in response-01.md, correct the affected wording/formulas, preserve source-specific coverage limits, and return the material changes for a focused Codex audit. Existing accepted PD statuses remain untouched. AC alone decides merge.
