# Supplemental Sol max review of the onset-512 manuscripts

Reviewer: distinct Codex supplementary manuscript auditor, assigned
`gpt-6.1-sol` at max effort at AC's explicit request. This is supplementary
review, not the substantive Claude audit or a PR-readiness decision. Root
alone controls Git. No manuscript, checker, evidence or shared record is
edited by this reviewer.

Rules read at `2d6be5f94880e53b240a11ed29ab55bd0d48af42`:
`AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`.

## Status and candidate

**Supplemental manuscript review: ACCEPT at final source freeze
`24a98db4c3c4c4d0eede2e3929532956df87911b`.** Whole-source review was
completed at baseline `dcb27db7d159ca0eac66e5fb48623589035a31ef`, followed
by complete focused review of the integrated source delta and refreshed
outputs. No BLOCKING, MAJOR or MINOR finding remains within this review's
scope. This acceptance is separate from the required substantive Claude
audit and is not a PR-readiness or submission-readiness decision.

**Correctness:** no mathematical defect found in either manuscript within
the declared scope. **Exposition:** the paired five-section architecture is
coherent; the constant construction, all-degree gates, corner arguments and
direct arithmetic route now have the needed explanations. Safe duplicate
cuts preserve the full elementary proofs at first use. Named tools are cited
or stated locally, and the first-use omissions found in this review are
resolved. Companion depth is appropriate to university analysis.

Final integrated outputs, independently checked with `pdfinfo`, SHA256,
auxiliary labels and log inspection (root built them; this reviewer did not):

| Manuscript | PDF under `local-output/padua-argmax-bridge-20261105/` | Pages | Bytes | SHA256 |
| --- | --- | ---: | ---: | --- |
| Journal | `onset512-paper-20261108/main.pdf` | 51 | 733598 | `1346fc2891e2cdd5deb6db4b1a5928a2a7bac05c1838999b1a1dee1fc0db1d2c` |
| Companion | `onset512-companion-20261108/main.pdf` | 147 | 1171187 | `83ca42c8052ccd760c3929ff0c30cd1667971476ae111736fe371b30e4581af2` |

The final ratio is 147/51, approximately 2.88, below the five-times limit.
Both final logs contain no errors, warnings, overfull boxes, undefined
references/citations or multiply defined labels. All 116 corresponding
built label numbers agree. The larger phase figures, repaired trigonometric
display and new arithmetic page are readable in the final PDFs.

Integrated baseline builds were supplied by root and independently identified
with `pdfinfo` and SHA256 (no build was performed by this reviewer):

| Manuscript | PDF under `local-output/padua-argmax-bridge-20261105/` | Pages | SHA256 |
| --- | --- | ---: | --- |
| Journal | `onset512-paper-20261108/baseline-dcb27db/main.pdf` | 50 | `8472d34cbc2fda6e2bdb809fe9d01752a60b21870ba48ba5c6707780ef9225ef` |
| Companion | `onset512-companion-20261108/baseline-dcb27db/main.pdf` | 147 | `53810a5a6e8aea0a54ada4dbd4401f9e4135b682fc8f9689c6b395c760b89049` |

The baseline ratio was 2.94, within AC's five-times limit. Both baseline
copies were rechecked at their retained paths and retain these hashes.
Forty-three pages was an
earlier projection, not a ceiling. AC subsequently clarified that conceptual
coherence, explicit constants and complete corner arguments take priority over
page savings; 50 pages with the necessary explanations is acceptable. AC
asked that the worked degree-two example remain. Source locations below refer
to the frozen baseline, even where root has since corrected the working copy.

## Preparation and scope

Read in full: handoff 29 and its dated AC decisions; `audit-03.md`;
`audit-03-manuscripts.md`; the S, P, C1, C2A, C2B and C3 audit-03 reports;
`notation-pass.md`; `theory/J01-onset512-gates.md`;
`theory/J02-elementary-constant-enclosure.md`; and the current
`independent-checks-onset512-response.md`. Read the LOG entries for the
2026-11-08 audit and response, including AC's funding confirmation.

The scope is correctness of newly inserted manuscript derivations,
conceptual clarity, useful compression and missing explanation throughout
the journal paper and its elementary-analysis companion. It also covers
their same five-section structure and matched formal statements, headings,
numbering and bibliography. The accepted older certified claims and frozen
engine are not reopened. There will be no native or certificate run, new
degree campaign, broad test campaign or remote computation.

This revision implements approved architecture B and an existing analytic
constant enclosure; it makes no new mechanism or priority claim. A complete
IDEAS read is therefore unnecessary for this scope. Any literature judgment
is confined to audit-03's recorded search scope and its inspectable records.

## Review criteria

1. **Main chain.** Explicit assumptions and interfaces for
   `lambda = S - Delta`, the radius-one relative polynomial, the uniform
   `1/20` noncorner floor, the absolute gate, corner descent and finite
   completion through degree 511. Closed charts, ties, collisions, equality
   cases and seams must remain covered.
2. **New derivations.** Compare the manuscript proof with J01/J02:
   positive curvatures; maximum/vertex identities; real-degree monotone
   transfer of the maximum and the half-radius value; tangent-condition
   persistence; every sign in the absolute gate; the elementary constant
   brackets and `C_infinity < 9/4`. Distinguish proof from finite arithmetic
   receipts, independent execution and measurement.
3. **Finite trust.** Preserve certificate-consumed floor tiers, the
   far-192 guard and gap, corner-256 square and loss, both norm witnesses,
   corner-witness rectangle and pi bracket. Report the actual current I25
   status without claiming universal validation of native endpoints.
4. **Whole-text exposition.** Review every section, with particular attention
   to shared row calculus, the corner formula and asymptotic coefficient
   ledger, the completed model's origin, row/residual identities and finite
   charge ledgers. A useful statement needs a clear consumer; a routine
   assertion needs the explanation appropriate to its audience.
5. **Companion depth.** Some university analysis is the assumed background.
   Identify undefined jargon, unstated tools, missing hypotheses,
   unexplained steps, forward dependencies and duplicated compressed/expanded
   arguments. Judge examples, diagrams and notation by their explanatory
   value. The companion must be at most five times the paper's length.
6. **Compression.** Propose cuts with locations, approximate size and
   tradeoffs. The earlier 43-page estimate is a projection, not a length
   requirement. Retain proof obligations and meaningful explanation; prefer
   removing repeated summaries, dead stronger bounds and secondary material.
7. **Presentation constraints.** Avoid defensive/process prose and keep
   novelty bounded. AI declaration, ORCID and contributions are reserved to
   AC; the no-specific-grant statement is confirmed accurate. A clearly
   marked DOI/deposit placeholder is allowed while AC reserves/publishes it.

## Baseline verdicts and scope of evidence

**Correctness:** no blocking mathematical defect found in the complete journal
or companion reading. In particular the new onset-512 reduction, elementary
constant enclosure and inserted row/kernel derivations are coherent with
their stated assumptions. This is a supplementary manuscript judgment, not
an independent re-proof of every inherited finite allowance, a fresh execution
of certificates, or readiness for merging/submission. The substantive Claude
audit remains outstanding.

**Baseline exposition:** the five-section architecture made the main chain
clear. The elementary companion had one substantial omission in the newly
adopted sine arithmetic explanation, several definite stale aliases, and
avoidable duplicate derivations. The targeted corrections below resolve
these findings. The new all-n gate proof should remain: its monotonic transfer and the
positive fixed-segment optimizer are useful proof obligations, not secondary
results to remove merely to shorten the paper.

Read both `main.tex` files, all twelve section files, and both bibliographies
in full. Mathematical source review used frozen Git bytes, not later mutable
TeX. Also read J03's arithmetic-soundness and complete-cover account to locate
the missing companion explanation. Render inspection covered journal pages
16, 23, 46 and 47 and companion pages 127 and 128, in addition to extracted PDF
text and auxiliary label/page information. Root reported successful integrated
builds with no undefined references/citations or multiply defined labels; this
review did not rerun those builds.

Executed read-only checks:

* Direct comparison of the two frozen sources: identical five numbered
  sections and subsection headings, 19 complete formal statement blocks,
  85 numbered display environments, 116 unique labels, counter controls,
  main numbering/input setup and bibliography.
* All 116 corresponding built label numbers match in the two supplied `.aux`
  files. This checks numbering and preservation, not mathematical truth.
* Exact `Fraction` calculations confirm the K=3 tail `1/480`, the
  `j > 23/250` arithmetic, the positive constant margin `71/6250000`, the
  corner-gate derivative margin `10451/30000`, and
  `F_h(295)=385242805909/7694959360000 > 50064/10^6 > 1/20`.

No native, interval-certificate, production-evaluator or degree-campaign job
was run. The full 942-witness result and the six separately executed replays
are accepted evidence from the distinct Astra review, not executions claimed
by this reviewer. The text accurately claims revalidation with the independent
checker's own bounds; it does not claim containment of every native endpoint.

## Whole-section coverage

| Section | Baseline pages, journal / companion | Review and assessment |
| --- | --- | --- |
| 1. Introduction | 1–4 / 2–9 | Main maximum and expansion statements, parity, computer-assisted finite range, analytic asymptotic tail, numerical coefficients, applications and literature qualifications read. The De Marchi fit and older two-variable work are described with bounded scope. No new priority conclusion is inferred. Companion norm/error examples are useful but the opening explanation repeats itself. |
| 2. Operator and normalization | 4–6 / 9–19 | Corrected highest-mode coefficient one, endpoint weights, discrete orthogonality, Gram/invertibility and cardinal formula checked. The companion supplies the linear-algebra steps rather than assuming special Padua identities. The injectivity argument can be given once. |
| 3. Exact corner and first correction | 6–15 / 19–47 | Finite diamond/product identity, collisions, periodic row sum/sign count, endpoint row, equal-mesh square, mesh-defect limit, digamma-series tools, uniform endpoint remainders and final coefficient ledger read. The added row derivation repairs the earlier unexplained transition. The endpoint cancellation and termwise-differentiation explanations are adequate. Several complete arguments are then repeated in compressed form. |
| 4. Global localization | 15–41 / 47–115 | Entire reflection geometry, closed odd-chart cover, endpoint multiplicity, projections, completed model, cusp/finite part, constant enclosure, full finite-row telescope and charges, both scalar gates, all three selected-pair classes, corner descent and final tail proof read. The lambda=S−Delta interface is clear; radius halves, one, pi/2 and pi have the correct distinct roles. Stale companion aliases and a hanging sentence require correction. |
| 5. Finite completion | 41–47 / 115–145 | Positive interpolation, exceptional Bernstein vertex, complete trees, whole-signed-family derivative norm, TREE/GRID absorption, closed proxies, floor radius, squared corner witness, analytic substitutions, verification proposition, trust/coverage tables and retained-record descriptions read. The new direct arithmetic route is honestly scoped. Its sine error budget is asserted rather than taught in the companion; see E1. The degree-two example provides concrete pedagogical grounding; AC has asked to retain it in both manuscripts. |

Declarations and reference lists were also read. AC-locked AI/ORCID/contribution
statements were not reopened. The confirmed no-specific-grant statement and
honest future-Zenodo wording do not create findings. Archival retrieval and
the final DOI remain AC's pending publication work.

## Mathematical reconstruction of the new parts

1. **Relative gate.** `u >= 11(x^2+y^2)/48` and
   `x^(3/2) <= x^2+x/4` give positive diagonal curvatures. Completing the
   square on `x+y=rho` gives the stated radial quadratic, its unrestricted
   maximum and its vertex. Increasing curvatures and decreasing positive
   linear terms transfer the maximum and vertex bounds to every real
   `n>=512`. For the half-radius value the proof additionally shows the
   maximizing coordinates stay positive, making it a maximum over one fixed
   compact segment. This extra argument is necessary and valid.
2. **Absolute gate.** In `h=rho/2`, `delta=(x-y)/2`, the subtracted phase
   expression is `A(h) cos(delta)+B(h) sin(delta)`. The tangent hypothesis
   makes both nonnegative amplitudes decrease. The estimate
   `sqrt(A^2+B^2) <= A+B^2/(2A)` produces the stated G with the correct
   adverse signs. All-n increase and persistence of the tangent condition
   follow from the explicitly decreasing allowances. The far-192 and
   outer-512 instances are distinct and correctly used.
3. **Elementary constants.** The endpoint-cancelled coefficient series has
   the stated geometric coefficient/tail bounds. The K=3 radius is 1/480;
   Machin/logarithm, convex zeta tails and harmonic gamma brackets supply
   finite rational inputs. The resulting coarse bounds suffice for H0, j
   and t0 and for `C_infinity<9/4`. Neither the obsolete PD271 premise nor
   the stronger unsupported `kappa<0.92` is needed.
4. **Joining the regions.** The uniform selected-pair floor from n=295 gives
   more than 1/20 on the half-radius near region; the radial maximum is less
   than 41/1000. Their difference is a strict gap greater than 9/1000.
   The half-to-one region has gap 1/7, the outer region gap 1/2, and the
   corner half-diamond lies in the pi/4 descent square. Closed ties, axes,
   collisions and exact equality points remain included. Degree ranges
   2..40, 41..511 and >=512 meet without a gap.

These are manuscript-level reconstructions. The broad hand reconstruction
and five small executed rational checks are not a new numerical certification.

## Findings and required dispositions

**No BLOCKING correctness finding.** The severity below concerns exposition
and notation; it must not be converted into a claim that accepted arithmetic
or inherited inequalities failed.

### E1 — MAJOR exposition: teach the new sine enclosure in the companion

Companion `certification-unified.tex:1666–1676` and `1764–1776` invoke a
Taylor polynomial with “proved truncation and roundoff bounds,” but give no
polynomial, numeric error budget or normal-operation hypotheses. Earlier
pages carefully derive the old cosine/arctangent construction. After the new
direct-sum substitution, the final proof-producing sine arithmetic needs the
same treatment. J03, Arithmetic soundness 1–5 already supplies it.

Fix: add unnumbered companion derivations for exact argument reduction and
collisions; guarded integer/normal ranges; degree-25 sine Horner evaluation;
coefficient conversion and evaluation error below `77 u t`, truncation below
`u t`, argument error below `6 u t`, hence total below `84 u t < 128 u t`;
and widened pairwise-sum induction. State a compact polynomial/error formula
in the journal and identify the deposited arithmetic proof. State that the
true reduced angle lies in `[0,pi/2]` when intersecting with `[0,1]`; do not
assume monotonicity beyond a rounded half-pi endpoint.

**Working-source disposition:** resolved in the checker developer's released
Section 5 pair: journal SHA256
`1404238517dd7c9828b909ef37e6cedd30f71e6e4adacd4d972c7e8252b19dac`,
companion SHA256
`28335bfbf1ee84c176ea9c179b7e387a516ef448c2fdeb24dcf2ce32466631b5`.
Read the complete new arithmetic derivation at companion lines 1614–1799
against J03. The normal-operation backward induction, 38 rounding factors,
absolute-coefficient majorant below two, `77+1+6=84<128` budget,
true-angle intersection, pairwise summation and exact rational normalization
are now explained correctly. The journal has the compact error statement;
the degree-two example is restored. All these changes are present in the
verified final integrated freeze.

### E2 — MINOR definite notation/prose repairs

All locations are in the frozen baseline. The final source delta has been
inspected and corrects every item.

| File | Location / defect | Exact repair |
| --- | --- | --- |
| Journal comparison | 883–884: “The remaining estimates ... are” followed by a new sentence | Delete the unfinished first line. |
| Companion comparison | 2292–2293: same unfinished line | Same repair. |
| Companion comparison | 1163: “definition of bar L” in the finite-part calculation | Use definition of H, equation `uc:H`. |
| Companion comparison | 1502–1503: obsolete “two-radius ... two domains” | Delete; the theorem now has only the radius-one relative bound. |
| Companion comparison | 3323: obsolete “two phase domains” | Use the single radius-one domain. |
| Companion comparison | 3037: undefined V in the outer-origin sum | Use V_F, defined in `uc:origin-variation`. |
| Companion comparison | 3898: three uses of J_sigma | Use the current J_W allowance. |
| Companion comparison | 598: “f''=f'' decreases” | Remove the tautological equality. |
| Companion certification | 118: second phase frequency pi k | Use pi mu; mu=n/(n+1). |

The baseline also has one inherited 30.217pt overfull display. Root identified
the correct source as the three new trigonometric identities at journal
`corner-unified.tex:180` / companion `:343`, and assigned a three-row aligned
layout and antecedent repair. The mathematical identity is sound.

**Working-source disposition:** the released comparison delta corrects the
hanging sentences and stale H, V_F, J_W, radius and derivative aliases. The
released certification pair corrects pi mu. The corner display is split into
three aligned rows without changing any identity. The final source identity
and PDF reflow checks pass.

### E3 — NOTE optional diagram improvement

Figure 2 on journal p.16 is small; the half-radius and radius-one cuts and
dashed corner square are cramped. Enlarge it or give a near-origin inset if
layout permits. The companion phase-certificate diagram on p.128 clearly
separates the actual near seam, analytic far guard and corner patch. Root
may explicitly defer the Figure 2 enlargement; it is not a correctness issue.

**Final disposition:** root enlarged the phase figures from scale 0.85 to
1.3 in both versions. Inspected journal p.16 and companion p.52; labels and
region cuts are legible. No remaining action requested.

### E4 — First-use notation and named-tool clarification

AC subsequently made the no-guessing criterion explicit: named results must
be cited or stated in the form used. A focused scan of both complete section
sets identified the following local exposition repairs. These locations refer
to the released working sources, before root's final freeze. None changes
the mathematics or needs a new numbered block.

| Location | Omission and concrete remedy |
| --- | --- |
| Journal introduction 5–6 | Define `Q=[-1,1]^2`, `||f||_infty=max_Q|f|` and the induced operator norm before the first displayed error bound. The companion already does so. |
| Journal introduction 116 | Define Euler's constant by `gamma=lim_R(H_R-log R)`; naming it alone is less explicit than the companion's definition. |
| Journal preliminaries 21–24, 52–59 | Define the checkerboard scalar product `sum_{j+k even} w_jk F(cos theta_j,cos phi_k)G(cos theta_j,cos phi_k)` and Gram entries as pairwise scalar products. Explain unisolvence as unique interpolation for every set of nodal data. The companion already supplies these definitions and the full linear-algebra argument. |
| Journal comparison 13 | Define `r_+=max(r,0)` before its first use. |
| Journal comparison 92–95, 119 | Define `zeta(s)=sum_{k>=1}k^(-s)` for `s>1`. Define Lip as the least Lipschitz constant, Var_per as full-circle total variation, delta_pi as unit point mass with the endpoints identified, and df' as the derivative measure; state the measure inequality through nonnegative test functions. The companion already gives these definitions. |
| Journal localization 330 | State the trigonometric Bernstein inequality `||T^(r)||_infty<=d^r||T||_infty` and cite Boas at this first fourth-derivative use. Explain the scaled factors 1 and mu. The journal's later second-derivative use is cited, and the companion states and proves the precise finite inequality. |
| Journal certification 15–17, 31 | Define `B_i^n(s)=binom(n,i)s^i(1-s)^(n-i)` and `s=(a-a0)/(a1-a0)`, `t=(b-b0)/(b1-b0)` before the lemma; state nonnegativity and partition of unity. Companion has all these definitions. |
| Journal certification 59 | State the midpoint de Casteljau averaging recurrence, with its existing Lorentz reference, rather than naming the algorithm alone. Companion 414 onward gives its full derivation. |
| Both corner 139 / 302 | The displayed convergent series already defines psi. The otherwise unused `Gamma'/Gamma` alias introduces an undefined Gamma; omit the alias instead of adding irrelevant Gamma-function theory. |
| Journal comparison 185, 222, 224, 539 | State the local forms of dominated convergence, Fubini, layer cake and Tonelli: pointwise limits under one integrable absolute majorant commute with integration; absolutely integrable double integrals can be reordered (here with total variation `|df'|`); `h(x)=int_0^infty 1_{h(x)>r}dr` for `h>=0`; nonnegative double integrals can be reordered. Preserve the actual domination and arc-intersection arguments. |
| Companion comparison 643 | Add the just-mentioned absolute-integrability form of Fubini. Its bounded weight and finite derivative variation already verify the hypotheses. DCT, Tonelli and layer cake are explicitly stated elsewhere in the companion. |
| Journal comparison 473 | Display `pi=16 arctan(1/5)-4 arctan(1/239)` beside the first Machin construction. The explicit A39/A40 brackets have correct signs, and the companion later derives the identity by rational tangent addition. |

The Abel passage is an explicit damped geometric identity with a concrete
majorant, not an unexplained appeal to Abel's theorem. Quadrature and positive
interpolation are stated in their exact forms and proved locally. Peano
kernel masses and their positivity are supplied, with the full elementary
kernel derivations in the companion. No Riesz or Dirichlet theorem is actually
invoked, so no citation for either is requested. Elementary Taylor and
mean-value formulas are accompanied by their needed inequalities or integral
remainders. No broad reference or jargon expansion is needed.

Root received this list before final acceptance. The released notation,
certification and analytic-source deltas have now been read. They resolve the
listed items correctly, including a precise first-use Bernstein inequality,
all four integration-tool forms, the explicit Machin identity, normalized
Bernstein coordinates and the de Casteljau recurrence. The unused Gamma alias
is gone. The final journal sentence spelling out the order of measures via
nonnegative periodic test functions is present and checked at comparison
SHA256 `8ccd98838c84d07b560755875834a5ac7005970425e187f93d1c6da112717bcf`.
E4 is resolved in the released sources and the final source freeze.

## Compression proposals and tradeoffs

Do not delete gate monotonicity, the fixed-segment argument, exact endpoint
values, the matched-reference limit, any certificate-consumed floor tier, or
the squared-corner normalization to meet a page target. The comparison model
still needs a finite, auditable origin constant. Savings below are estimates
from the baseline PDFs, not promises about reflow; they are not all additive.

| Manuscript / location | Proposed change | Estimated saving | Tradeoff |
| --- | --- | ---: | --- |
| Journal certification 103–128, pp.42–43 | **WITHDRAWN after AC steering:** the initial proposal to move the degree-two four-leaf example entirely to the companion is not adopted. | None sought | Retain the worked example in both manuscripts for pedagogical grounding. |
| Journal comparison 432–527, pp.22–23 | Keep all numbered formulas, coefficient bounds, K=3 tail and explicit elementary construction rules; consolidate repeated coarse consequences into one rational input/output table. | 0.5–1 page | Exact finite arithmetic remains checkable; avoid replacing the proof by a bare software result. Root assigned this cut. |
| Companion certification 1345–1448 | Replace the second full squared-Peano/evenness proof with a reference to the complete first-use derivation in localization's Corner descent proof. Keep ALL subsequent witness points, q/g and pi^4 normalization. | 1.5–2 pages | Requires an internal cross-reference, with no loss of an elementary proof. |
| Companion certification 1034–1072 | Replace the second full separate-reflection/even-lattice/triangle proof by a reference to localization's explicit board reindexing. Keep compactness/existence of M_* and the subsequent absorption argument. | 0.6–0.8 page | One proof in the same document replaces its duplicate. |
| Companion certification 918–963 | Remove the second expansion of the finite sine product/root factorization and logarithmic derivatives. Keep the preceding csc^2 identity, coefficient-norm calculation and reference to comparison's finite-product proof. | 0.6–0.8 page | Preserves the finite proof of Bernstein's inequality and every derivative hypothesis. |
| Companion comparison 2912–2928 | Delete compressed component estimates after numbered `uc:origin-variation`; retain the full following “Derivative calculations for the signed origin bound.” | 0.3–0.4 page | Preserve the derivative-matching observation if it is not clear in the expanded calculation. |
| Companion comparison 1741–1762 | Merge “Algebra of the telescope” into “Collecting the finite sums...” at 1687–1739. Retain its exact singular-sample and h2−hn/g2−gn identities before B_ord. | 0.3–0.5 page | One complete algebraic derivation remains; delta_a's later explanation stays. |
| Companion comparison 560–570 | Delete the compact third-derivative sign argument; retain the full sine-ratio differentiation and evaluated-integral proof at 572–596. Keep the separate absolute f''' bound. | 0.2–0.3 page | Retains the complete proof and its rational negative margin once. |

The six companion cuts above offer about 3.5–4.8 pages without lowering the
analysis depth. Further optional consolidation:

* Corner 500–569: one coefficient-level equal-mesh square proof is enough;
  retain the geometric explanation and degree-two check, removing the earlier
  compressed proof of the same coefficient bookkeeping (about 0.3–0.5 page).
* Comparison 2197–2225: the general cancellation-variation proof is stated
  twice almost verbatim. Keep it once before the expanded perturbation count
  (about 0.15–0.25 page). Similar short-before-expanded duplicates occur in
  the pole error, retained near-index arithmetic, relative product-rule
  coefficients and endpoint derivative ledger; deleting them needs care to
  preserve definitions that occur only in the short version.
* Certification 1805–1814: delete the repeated elementary 280+191=471,
  2*471=942 paragraph; the table and immediately preceding coverage prose
  already give the same inventory (about 0.2 page).
* Introduction's initial operator explanation and repeated interpolation
  opening, and preliminaries' two injectivity arguments, can be consolidated
  locally. Keep one complete linear-algebra proof and the perturbation-norm
  construction, rather than cutting needed background wholesale.

The released journal constant compaction retains the important construction
steps listed above. Its explicit 39/40-term Machin bracket has the correct
signs, and no numerical constant becomes an unexplained software premise.
The full companion derivation remains. No further compression is required
merely to reach an estimated length.

The new absolute/relative gates, uniform half-radius floor and explicit
verification proposition have clear consumers. Removing them as “secondary
results” would weaken the proof architecture. The general cancellation and
central-pair tools similarly serve later charges; their stronger domains
are not automatically redundant. Prefer cutting repetition before removing
these working interfaces. The worked example remains under AC's latest
instruction.

## Companion depth and prose assessment

The companion explains BV/derivative measures and the cusp atom, finite parts,
complete cancellation, dominated convergence, layer cake, Tonelli, matched
half-line defects, positive Bernstein weights, Peano kernels and norm
absorption in concrete terms. Its derivations are substantially at university
analysis depth. The smooth sinc extension, convergence criterion for
termwise differentiation, equal-mesh weights and finite row identity close
the earlier specific omissions. No new broad jargon glossary is needed.

At baseline E1 was the material unexplained step introduced by the trust-route
change; the final full arithmetic derivation resolves it. The adopted cuts preserve one elementary proof of each fact and
remove second explanations rather than the teaching itself. Several phrases
still sound like internal audit reminders: “must still be retained,” “keeps
the last row,” “preserves m=n+1 and all finite origin values,” “with both
meshes ... intact,” and “included once.” Where the same point is already
proved in a displayed identity, state what that identity contributes or omit
the reminder. This is a small prose cleanup, not an instruction to suppress
endpoint/collision reasoning.

## Final revision checkpoint

The complete delta from dcb to source freeze
`24a98db4c3c4c4d0eede2e3929532956df87911b` has been read: the full
arithmetic insertion, compact journal constant construction, retained
degree-two example in both versions, six safe companion cuts, alias/layout
repairs and first-use/tool clarifications. No correctness or exposition
finding remains in those source changes.

Executed read-only final-source checks: all twelve working section files
equal their frozen Git bytes and the reviewed released hashes. The pair has
four theorems, nine lemmas, two propositions, three corollaries and one
remark, for 19 exact formal blocks; all 85 numbered display environments,
116 labels, section/subsection headings and counter controls agree.
Every formal block and numbered environment is byte-identical to dcb.
Both main files and bibliographies are unchanged from dcb, and the two
bibliographies match each other. Scoped `git diff --check` passes.

Final output checks are complete. Verified both PDF identities and page/byte
counts, compared all 116 built label numbers, and inspected final journal
pp.9 and 16 and companion pp.52 and 143, including the enlarged phase figure,
repaired trigonometric display and full Horner/roundoff derivation. Both
retained baseline PDF hashes also match. No reviewer build, native run,
certificate replay or broad test campaign was performed. The optional
further consolidation proposals above are not acceptance requirements.

The supplemental correctness and exposition verdicts are ACCEPT at the
identified source/PDF freeze. The substantive Claude audit and AC's external
deposit/DOI work remain outside this acceptance.
