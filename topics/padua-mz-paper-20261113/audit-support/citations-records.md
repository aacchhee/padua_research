# Supplementary audit: citations, exposition and records

- Auditor: Codex, gpt-6-astra, high (inherited audit assignment).
- Date: 2026-11-14.
- Rules and manuscript input: `be28d3267bf6117878190b10f2d29840e524eac7`.
- Scope: check the actual citation sentences against durable source-reading records; abstract/introduction against the stated results; cross-paper locators; availability and record consistency. No manuscript or development-record edits, Git mutations, source-PDF rereads, certificate reruns or builds were performed by this worker. Root handles the mathematical audit and reruns.
- Novelty boundary: this report adds no mechanism, candidate, novelty verdict or historical-priority clearance. It checks the attribution and coverage of already written comparisons. The overarching audit owns any full `IDEAS.md` novelty check.

## Findings

### C1 — MAJOR: the availability statements assert an archive and witness delivery that do not exist

Locations: MZ-CC `manuscript.tex` lines 1504–1511 and 2235–2243; MZ-SP `manuscript.tex` lines 1596–1597, 1708–1710 and 1736–1739. MZ-CC says the files “are archived” and “a README lists the files”; MZ-SP says the arrays and exact norm files “are archived with the deposit”. The DOI placeholders do not make these present-tense claims true. The topic report §6.2 explicitly states no delivery occurred, the old staging directory is unavailable, no deposit exists, and no archive README was found. The README statements that the manuscript makes no deposit claim are consequently inaccurate.

Required response: make the current-draft availability language describe the actual state and the intended future deposit, preserving the distinction between committed code/small receipts and absent exact witness inputs. Correct the two paper READMEs' “no deposit claim” assertions as needed. Do not claim the witnesses have been delivered or independently replayed from the pinned arrays. Supply an actual accessible package before claiming archival availability at submission. This finding concerns evidence availability, not a mathematical refutation of PD-T376.

### C2 — MAJOR: a measured minimum is asserted to lie in a certified trial interval

Location: MZ-SP `manuscript.tex` lines 1635–1638, Measurements item (2): “The minimum of the Gram spectrum … (at m=1600 it lies in the interval of Proposition [8.2])”. Proposition 8.2 explicitly bounds a trial Rayleigh quotient, not an eigenvalue. The valid variational implication is only that the true minimum is no greater than the trial quotient; it need not exceed the interval's lower endpoint. Numerical agreement with the displayed measured minimum supplies no rigorous lower endpoint.

Required response: remove or qualify the parenthetical so the text says the computed minimum agrees with the certified trial quotient at the displayed precision, without transferring the interval to the true eigenvalue. Retain the useful explicit distinction following Proposition 8.2. No new computation is needed for this wording repair, but it corrects the scope of a statement and must be identified in the response.

## Citation coverage checked

An independent regular-expression inventory of actual `\\cite`, `\\citet` and `\\citep` commands gives MZ-CC 33 commands / 37 key occurrences / 28 distinct keys, including MZ-SP; MZ-SP 22 commands / 22 occurrences / nine keys, including MZ-CC. Earlier task-5 counts describe earlier drafts. Each present occurrence was read in context. The bibliography `coverage` fields are not used as a substitute for the authoritative dated source records.

| MZ-CC keys | Present claim and record check |
|---|---|
| LIT-045 | Numerical predecessor and weak/strong distinction, CC theoretical-open report, and upper-Gram versus least-squares formulas. The source record covers published §§1–2/3.1/3.6; published (7)/(8) numbering was additionally checked by the developer and recorded in LOG and task-5 disposition. Its canonical LIT addendum remains a PR-preparation obligation. No independent published-PDF verification is claimed here. |
| LIT-046 | The m-point convention, eta=3/4 assumption, positive weights, conditional error bound and range n+2≤m≤2n+1 match the published-version reading. The manuscript correctly limits its criticism to applicability, preserves the conditional theorem, and says only it knows of no correction. |
| LIT-047/048/297/298 | Weight-sum functional norm, heuristic 1980 estimates, uniform-input mean-convergence relation, and Jacobi-zero product integration match the latest Sloan–Smith record. The previously unsupported attribution of mean convergence to LIT-298 was removed. |
| LIT-049/053/054/058/295 | Chapter 4 uniform interpolation, Hankel matrix problems, pulled-back GLL stability form and Sobolev-input CGL estimates are restricted to the covered setting. No CC spectral theorem is attributed to them. |
| LIT-050/051/052 | Unspecified forward upper constants, unspecified sampling window, and Gauss converse survey statements agree with the records. The Mastroianni–Totik wording now says no **explicit** information beyond exactness, avoiding the prior logical problem. |
| LIT-055/056 | Folded mode aliasing and coefficient-decay quadrature context match selected Trefethen and Xiang–Bornemann coverage. The latter DOI update is already flagged for the canonical LIT record at preparation. |
| LIT-061/062/063/065 | Uniform-input versus nodal weighted-input distinction is retained; Erdős–Feldheim is now attributed only mean convergence at Chebyshev abscissae in Chebyshev measure. Nevai's CC specialization is supported at recorded extraction/parameter-identification level; its formulas were not independently page-image verified here. The 1990 correction letter is read in the existing record. |
| LIT-064 | The excluded full-space exponent at the CC/Lebesgue/p=2 borderline agrees with the record's local translation and is not presented as a source-specific CC theorem. |
| LIT-293/294/296/299 | Gauss versus Lobatto distinctions, same-weight versus mixed-weight distinctions and qualitative full-space subsequence consequence are preserved. König–Nielsen's body coverage is arXiv, not a journal-body reread; no unverified journal locator is used. Source necessity proofs are cited, not claimed as locally audited proofs. |
| LIT-490/511 | Oversampled explicit constants and the extended converse theorem's CC excluded endpoint agree with the dated records. No broad claim that these sources lack approximation rates remains. |
| MZ-SP | Concluding pointer only; no CC proof depends on SP. It therefore does not make the SP→CC proof dependency circular. Bibliographic preprint placeholder remains for submission. |

| MZ-SP key / LIT record | Present claim and record check |
|---|---|
| BCDMVX06 / LIT-312 | Corrected fundamental kernel, order-only Lebesgue constant and density attribution match generating-curve Theorems 2–3 and the journal-version addendum. Coordinate swap and normalization are explained in the proof rather than copied from the SVZ misprint. |
| Xu96 / LIT-314 | Broad parity-separated CGL interpolation context only; no strengthened full-space or p=∞ claim. |
| SVZ08 / LIT-427 | Integrated interpolant (33), signed weights and few/small negatives, and density provenance are within pp.409–421 reading. The normalized density is proved using corrected kernel, avoiding uncritical use of the printed (25) denominator. |
| CDMV07 / LIT-428 | Positive Chebyshev-measure Xu hyperinterpolation and generic coefficient operator definition agree with the complete author/journal reading; no signed Lebesgue theorem is attributed. |
| KLP18 / LIT-488 | Positive Chebyshev weights, anisotropic space, unspecified constants and Erb attribution for 1<p<∞ agree with Lemma 5.1 and its journal addendum. |
| ASV27 / LIT-045 | Finite-degree observations remain scoped to m≤20 and a Padua-based rule. Section 8 uses the conditional identification “If that rule is the interpolatory rule studied here”, avoiding an unverified node/rule identification. |
| Wu26 / LIT-489; AW22 / LIT-046 | Positive-rule hypotheses and Galerkin eta<alpha/beta / hyperinterpolation eta<1 distinction are preserved. No signed-rule applicability is attributed. |
| MZ-CC | Both introductory recap and Proposition 2.2 cite Corollary 3.2, Theorem 4.3 and Proposition 8.1, which are the frozen numbers for the three required spectral facts. The paper explicitly declares the cited inputs are not reproved and that CC goes first. |

No additional unsupported citation sentence was found at the source-record coverage level. This is not an exhaustive historical search or a new proof audit of external sources. Unread optional references are correctly excluded from the bibliographies; optional resolver checks and author/DOI/arXiv placeholders remain submission tasks.

## Exposition and durable records

- Abstracts and introductions distinguish the analytic limits from the computer-assisted one-sided/coarse bounds and from the finite negative trial directions. The finite brackets, witness results and enclosure are labelled computer-assisted. Aside from C2, the measured section is explicitly separated and not used in a proof.
- Executable TeX was searched for IDs, statuses, audit/referee/receipt/campaign terms and availability language. PD source IDs and epistemic-status tokens are comments or bibliography keys rather than printed theorem headings. Repository paths in the availability statements serve reproducibility. Author/declaration/DOI/commit placeholders are intentional and visible. Root's built-PDF inspection owns any final visual/text assertion.
- Both README scope tables match the intended theorem identities, omitted results, analytic-versus-machine-assisted bounds, and OPEN lists. They accurately distinguish trial quotients from eigenvalue brackets. Their availability assurances require C1's correction.
- The M7 append preserves earlier historical records and records the split, journal classes, page counts, provisional claims, internal checks and actual missing witness delivery. Its source pin is explicitly `a0206a8`; the later `a03a4f7` removes the literal duplicated fragment “checks used are:The” from SP. Consequently that historical source hash differs from the audited head by a disclosed nonmathematical deletion; it should not be interpreted as a hash of the current source.
- Independently checked every repository-file size/SHA256 row of report §6: **53 rows, all pass**. Also checked the six current-paper source/class/bst rows in the M7 append: five match the working head; the SP source row is the historical a0206a8 pin just described. No absent cold-storage file was hashed or claimed retrieved.
- Source inspection and inventory commands used: `rg -n '\\\\cite'` and targeted `sed`/`cat` of actual manuscripts, bibs, rules, handoff05, BRIEF, LOG, report, literature scope record, both READMEs, M7 append, INDEX excerpts and the linked source records/addenda above. A Python `pathlib`/`re`/`hashlib.sha256` check parsed report table rows and compared their recorded byte counts/hashes to current file bytes. No network or source PDF was needed.

## Residual limits

Root retains ownership of builds, frozen-label validation, mathematical proof correspondence, computer reruns, overall audit verdict, and handoff. Witness payloads are unavailable locally, so present records do not permit byte-pinned revalidation of Proposition 8.2. The canonical LIT-045 and LIT-056 addenda, final IDs, shared registries and submission metadata belong to preparation after the developer responds.
