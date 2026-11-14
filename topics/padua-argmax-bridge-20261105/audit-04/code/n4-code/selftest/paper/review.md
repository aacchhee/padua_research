# Supplemental manuscript consistency review

Status: COMPLETE — accepted as a faithful research-draft assembly within
the supplemental scope below; no unresolved material consistency finding.

Reviewer: distinct Codex supplemental mathematical/manuscript reviewer,
requested model `gpt-6-astra`, high effort; actual serving metadata is not
independently exposed. This is not the required Claude audit and gives no
PR/submission readiness decision.

Rules read at input commit
`1f5ad866189944d905129ca078ca1cbd46d1c9c4`: `AGENTS.md`,
`agents/WORKFLOW.md`, `agents/codex/CODEX.md`. Only this review file is
owned by this reviewer. No Git operations or manuscript edits were made.

## Scope and method

Review the expository assembly against the established canonical records,
with particular attention to the corrected cardinal normalization, parity,
first-correction coefficients, exact equality classification, and analytic
versus computer-assisted dependencies. This adds no new mechanism or
novelty claim; the full candidate-generation gate is therefore outside
scope. Literature checking is a comparison of manuscript wording with the
completed source-refresh records, not a new external priority search.

Primary mathematical source comparisons: H-sharp-corner-expansion, H01,
H04, H05, G01, and E14 assembly, together with the manuscript's displayed
proofs. The H01 and E14 records retain historical pending/open snapshots;
the parent adoption records supply their current accepted scopes.
Additional primary comparisons read in full: PD-T159 positive corner
formula/reference-square/deformation argument, PD-T269 defect limit, and
PD-T270 one-dimensional remainder.
No native certifier, numerical mathematics, or finite-degree experiment
was rerun for this manuscript review. Existing verification is described
as existing verification, never as a new independent execution.

## Findings communicated during assembly

1. **Material attribution correction requested.** The initial introduction
   attributed “quadratic growth” of the Morrow--Patterson Lebesgue constant
   to Beberok--Białas-Cież--De Marchi. The completed recent-source refresh
   reports their Theorem 4 as an upper bound `O(n^2)`; the separate 2025
   lower-bound article remained unread. Use the precise upper-bound
   wording, and do not infer an exact distinct growth scale from that
   citation alone. The discussion needs the same scope discipline.
   **Disposition:** corrected by the author in both sections; checked.
2. **Certificate proposition clarification requested.** The initial
   proposition imposed strict primitive comparison against a retained
   corner lower endpoint on every rectangle, including rectangles meeting
   the corner origin. State the actual alternatives: primitive exclusion
   where valid, defect-assisted exclusion at noncorner centers, and
   punctured local descent at actual corners. The separate local descent
   permits equality at the two intended origins.
   **Disposition:** revised alternatives checked and accepted.
3. **Minor transcription fixes requested.** Two `quad` tokens in the
   argmax region display lacked backslashes. The missing-degree union
   displayed an extraneous plus sign. These are editorial errors, not
   changes to the accepted estimates. A later missing backslash before
   `operatorname{sinc}` in the row appendix was also reported.
   Additional scans found escaped carriage returns that silently rendered
   broken `\rm` notation in several parity sums and scalar subscripts.
   Both raw control bytes and normalized newline fragments were reported.
   **Disposition:** corrected by the authors. Final byte scan found no
   control characters other than line feeds, no literal tabs, and no
   remaining standalone `m odd/even/end/vertex` corruption fragments.
4. **Notation clarity suggestion.** The argmax section locally reused
   `N=nm`, while the main expansion uses `N=n+1/2`. The local definition
   prevents a formal contradiction, but a different product symbol makes
   normalization easier to follow.
   **Disposition:** author changed the mesh product symbol to `\mathsf N`.

5. **Phase normalization clarification requested.** The phase-certificate
   proof used frequencies `1,n/(n+1)` while its rectangles were expressed
   in normalized coordinates `(a,b)`. The normalized frequencies are
   `pi,pi*n/(n+1)`.
   **Disposition:** the detailed certificate predicates explicitly retain
   the necessary `pi^2` Peano and `pi^4` corner factors.
6. **Standalone definition gap identified and resolved.** The first row
   appendix referred to `M_infty` without displaying the completed
   model coefficients. The scalar appendix now defines the full model,
   proves the finite-part normalization, and supplies the coefficient-loss
   inequality that yields `T=(4*log(n)^2-3*log(n))/pi^2` and the
   `79/(5*pi^2)` coefficient in the global norm. The addition was checked.

## Mathematical observations

The displayed main expansion agrees with the canonical target:
`a=2/pi`, `d=gamma+log(8/pi)`, `b=2*a^2*d`,
`c=a^2*d^2+kappa`, coefficient `-1/N`, and the same
`O(log(N)/N^2)` remainder on both parity subsequences. The proof retains
`-1+2/m`, the harmonic logarithmic correction, and the nonzero smooth
correction before changing to `N=m-1/2`.

The cardinal coefficient of the exceptional `(n,0)` mode is one.
Endpoint weights and the separate `1/m` corner collision contribution
are retained. The periodic row normalization and the parity-correct
corner pairs agree with the canonical records. The stated all-degree
partition is `2..319` plus the analytic tail from `320`.

The corner expansion is explicitly analytic and independent of argmax.
The global consequence correctly retains the finite certification and
PD-T271 quantitative constant dependency. The draft distinguishes 560
local rational reconstructions from only two fresh local native replays
and does not infer a continuum maximum from samples. The main draft
notice acknowledges pending standalone exposition and cross-agent audit;
this reviewer will check that unfinished foundations remain visible in
the assembled version.

The full asymptotic appendix was read and its algebra reconstructed. It
supplies the uniform diagonal deformation bound, endpoint-complete defect
limit, one-dimensional quadratic error, uniform centering, convergent
small-index correction, logarithmic quadrature, and explicit smooth
`17/n^2` estimate. No unsupported asymptotic premise was identified in
that chain. The new appendix consistently reproduces the canonical
H01/H04/H05 and PD-T159/269/270 ingredients.

The geometric appendices were read as they were assembled. Checks include
the exact reflection normalizations, no addition of projected floors,
closed guard domains, full origin error versus global absolute norm,
near/wide coefficient collection, paired central integral, scalar
maximum with its negative cusp atom, all-real-degree transfer of the
scalar gates, and exact finite certificate predicates. These constitute
a supplemental assembly check, not a new exhaustive audit of every
upstream inequality or computational implementation.

## Final frozen review — 2026-11-07

Candidate source commit: `a948b24c3faeba1e475ce64f4c7fc9d4123d42a5`. The rules-input commit remains
the earlier commit recorded above.

**Verdict:** no unresolved material mismatch was found between the displayed
main results and their canonical records. The reviewed text is suitable as
an explicitly labeled research manuscript draft. This verdict does not
supply the separate Claude audit, an exhaustive independent reproof of all
upstream estimates, or submission/PR readiness.

The final late additions were read: the combined endpoint envelope,
sharp cancellation variation, the regular variation constants, completed
model coefficients and coefficient loss, and the complete pole appendix.
The pole appendix's weighted error, symmetric reference matching,
triangular-convolution endpoint constant, closest-row estimate, and relative
half-line increment match their row-appendix interfaces. The main data
availability paragraph correctly restricts the compact-return assertion to
degrees 41–319, without implying that the compact return contains every
inherited small-degree certificate. The proof claims retain their stated
analytic and computer-assisted boundaries.

The main draft notice continues to state that a complete standalone
exposition check and final cross-agent audit are pending. No explicit
unproved hypothesis or hidden replacement of a true corner value by a
numerical endpoint was identified in the reviewed assembly. Several long
row/model arguments remain compressed and should receive that final audit;
absence of a finding in this supplemental check is not a completeness
certification of every upstream inequality. Publication also requires the
human authors' metadata/declarations and a durable public code/evidence
release. These are visible obligations, not a weakening or upgrade of the
canonical mathematical records.

### Checks actually performed

- Read the rule files, canonical mathematical records listed above, both
  main proof chains, all included technical appendices, bibliography, and
  the final data/evidence scope wording.
- Compared attribution with the bounded literature refresh records; no new
  external search, exhaustive novelty verdict, or priority claim.
- Executed a Python static scan of final manuscript sources: no duplicate
  labels, no unresolved `ref`/`eqref` labels, no unresolved cited BibTeX
  keys, no raw control bytes other than line feeds, and no remaining
  normalized carriage-return notation fragments of the reported kind.
- Read the build instructions. Compilation, final PDF inspection and build
  log checks are the orchestrator's separately executed checks; this
  reviewer did not perform or claim a new compilation or visual PDF review.
- No native certifier, numerical mathematics, or Git command was executed.
  Only `paper/review.md` was modified by this reviewer.

### Reviewed source identities

Paths below are relative to this `paper/` directory. SHA-256 hashes identify
the final source freeze reviewed; later material edits require an impact
check. The review record itself is excluded to avoid a self-hash.

| File | Bytes | SHA-256 |
|---|---:|---|
| `main.tex` | 4425 | `108186035fe08991fa1a847018a3778707a61c47dd32c975348a68ae5995ed5d` |
| `references.bib` | 3487 | `4f63b445f1b6de8ce0e670eada083934a8da5440a4ab7b18810d6433e36bbc65` |
| `sections/argmax-details.tex` | 42779 | `2559fbbe7a2c4f1278cd4452bbc3bf27055a863c2f8d4c67444e20975f127620` |
| `sections/argmax.tex` | 9545 | `e0a3225008c5b3e9af0318043687ca5ef4ed59f81958b8d1a586a0f290191a11` |
| `sections/asymptotics-details.tex` | 28059 | `00570d9282de11969835869fbc5a889a009c6f0bf04e7c6b732ee40ffc0b6bad` |
| `sections/asymptotics.tex` | 7104 | `a6ae833c577a14f283bc2008c3270fa4a9f183a893c45eedd6463ee086e1c6e0` |
| `sections/certificates.tex` | 6745 | `b38326e77f62999084f781414bf4bd28a33cc484eeefbd140debf9ef89980f06` |
| `sections/corner-formula.tex` | 8896 | `086e781a1dacea730b01c583c5b760ed81660e42ce32eab5f412dbaa2453befe` |
| `sections/discussion.tex` | 1420 | `120a6eba43025538a37e9a6b7eec708dfb6df4039bad2034a9ddb8f6f1988aef` |
| `sections/introduction.tex` | 9384 | `cc2787e6a362cc0503983c35add053e09533106a5f8e41afcc3629b48cb15d73` |
| `sections/model-estimates.tex` | 8946 | `ecfe3fded8992321de4cc47d28a90dc019310f5b25e7f088a4944d2f666dc7cd` |
| `sections/pole-estimates.tex` | 26758 | `31a72591e353f41d4733546eea71c36b4115570b99082cd64fa60049e36a7084` |
| `sections/preliminaries.tex` | 3474 | `c9a7a26306a9f6858a9e129f6639d0553efa478584b87252f6cd1c35c7320f71` |
| `sections/row-estimates.tex` | 54181 | `b6f153f90f607f907b014298f0d2f32ce78d1574db209db88330ec83228845ba` |
| `sections/scalar-estimates.tex` | 32326 | `b70ca3383a2a71fcb93155a2eec5e8f8c0ee9cb41272ebb86887fbdeaf865f7f` |
| `sections/traceability.tex` | 1754 | `f329d90c1b6a36bbe752c68aa6f8cbb2dde4ed2218a90021d7f75da021fe9629` |
