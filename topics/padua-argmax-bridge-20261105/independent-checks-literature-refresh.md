# Independent bounded source/claim review, 2026-11-07

Rules/input head: `f937bf2339ebcd7e81d6992d31b9c169cae9e22e`.
Reviewer: distinct Codex subagent; actual serving model/effort metadata is not exposed to this subagent. This is an independent source-comparison check, not the substantive Claude mathematical audit or a publication-readiness decision.

## Scope and input identity

Read `AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`, the relevant Padua rows/addenda of `literature/INDEX.md`, the existing KL2021, De Marchi2022 and geometry2026 source records, and the earlier [P1 comparison](../padua-literature-20261103/p1-comparison.md). Read the complete two fresh source notes and the H/G01 target statements and dependency boundaries. The attempted bulk index read was output-truncated; only relevant rows/addenda are claimed as read here.

The limited no-novelty exception applies: this checks provenance, operator/claim scope, and whether the search reports exceed their declared reading. It generates no mechanism and makes no exhaustive novelty or historical-priority judgment. The complete `state/IDEAS.md` was not reread. No scientific numerical computation, Git mutation, source upload, or author contact was performed.

Reviewed prose snapshots (SHA256, recorded for review identity, not a checker invariant):

| File | SHA256 |
|---|---|
| [Recent sources](literature-refresh-recent-20261107.md) | `c6364f803d086f1e24b77317a832d92ca8cc76992eb37435055849f6102efe86` |
| [Asymptotics](literature-refresh-asymptotics-20261107.md) | `ced2349697ec423b7156022997b5380c81e787669013f44fda10b06cdd7092aa` |
| [H sharp expansion](theory/H-sharp-corner-expansion.md) | `b31aae9417c31bcdb705f018ccfe0fbe342015e4612dff46f55373338eed4a01` |
| [G01 all degrees](theory/G01-all-degrees.md) | `646cca0b0fd8c1faccbff504e263545b073318da3211c150cfc06a827aead86f` |

## Independent primary inspection

The web connector was rediscovered and invoked independently. Critical passages were opened by direct source URL, checking returned title/URL, rather than trusting another agent's turn identifiers. Coverage below is text-layer/HTML reading; no source proof was independently reconstructed and no figure pixels were inspected.

1. **KL2021:** [arXiv metadata](https://arxiv.org/abs/2009.07114) and [v1 PDF](https://arxiv.org/pdf/2009.07114), pp.3–4, plus matching HTML Theorem2.1. The Padua consequence is explicitly `(4/pi²)log² n+O(log n)`. This verifies published leading-term attribution and does not identify the finer coefficients. The metadata page currently lists only v1 (15 September2020). Journal body and its numerical-fit section were not independently read here. The asymptotics note correctly labels `1.2 log(m+1)+1.5` as search-returned empirical text; it must not become a theorem or fresh primary verification. Failed text searches for `1.2` in arXiv text add no substantive source claim.
2. **De Marchi2022:** [journal PDF](https://dergipark.org.tr/en/download/article-file/2240064), §3.3 on journal pp.22–23. Item(2) states the unoccupied-corner observation within the open-problem list. This supports attribution of the statement, without supplying an all-degree proof.
3. **Białas-Cież–De Marchi–Suder2026:** [arXiv metadata](https://arxiv.org/abs/2605.23299) and [v1 HTML](https://arxiv.org/html/2605.23299v1), §§3.1–3.3 and Tables3–4. The independently read bivariate passage reports numerical local-maxima counts and expressly describes the suggested lower counts as numerical. It does not state the G01 exact all-degree global maximizer theorem. The metadata currently lists v1 dated22 May2026 and no journal reference; that is not proof that no journal version exists elsewhere. The separate worker's author-draft inspection was not repeated.
4. **MP2025/2026:** [publisher version of record](https://link.springer.com/article/10.1007/s00365-025-09710-x), Theorem4, §7.1, and bibliographic footer. Theorem4 states an `O(n²)` upper bound for Morrow–Patterson nodes; §7 reports numerical corner attainment and §7.1 leaves its proof open. Metadata distinguish online publication14 May2025 from volume63,31–65(2026), issue February2026. The setting and growth differ from Padua. The lower-bound sequel remains a discovery lead in the reviewed recent-source note; this review did not acquire it or infer its bound.
5. **ETNA2024 certification antecedent:** [journal PDF](https://etna.ricam.oeaw.ac.at/vol.60.2024/pp428-445.dir/pp428-445.pdf), title page, pp.429–430 (Lemma2.1, Proposition2.2, proof and Remark2.3), and §3.3 p.438. Authors are L. Białas-Cież, D. J. Kenne, A. Sommariva and M. Vianello; title is *Evaluating Lebesgue constants by Chebyshev polynomial meshes on cube, simplex, and ball*, ETNA60(2024),428–445, DOI10.1553/etna_vol60s428. For a total-degree polynomial projection on the cube, Proposition2.2 bounds the global norm between the mesh maximum of its Lebesgue function and that maximum times `sec(pi/(2m))`. Section3.3 applies the method to Padua and other square node sets. This is relevant published generic certification machinery. These passages do not identify exact Padua maximizers or give H's fine expansion. The method's analytic error guarantee should be distinguished from a separately audited rounding-error implementation.

## Findings and comparison boundaries

**No BLOCKING or MAJOR finding in the reviewed source notes within this limited scope.** They retain the distinction between fresh primary reading, inherited reading, search snippets, and inaccessible/unread material. Their bounded no-match language is acceptable only with those attached limits. It cannot be shortened to “the theorem is new” or “no such theorem exists.”

- **NOTE — leading term already published.** KL2021 is the closest independently reconfirmed global asymptotic theorem. Its `O(log n)` remainder does not determine `b=(8/pi²)(gamma+log(8/pi))`, the constant, the centered reciprocal correction, or the stated small remainder. This logical comparison does not audit H's proof or certify the first appearance of those terms.
- **NOTE — location statement already observed.** De Marchi2022 gives the location observation, and the older2008 conjecture is documented in P1 but was not independently reopened here. Credit the statement even when describing G01's proof as the local contribution. The earlier P1 local range (`2..16` plus eventual, with intermediate degrees open) is a historical snapshot; the current comparison must use G01's `n>=2` scope and named computer-assisted dependencies.
- **NOTE — prior certification must be credited.** ETNA2024 prevents presenting rigorous finite-mesh evaluation of a Lebesgue constant as an unqualified new capability. G01's exact equality set and strict exclusion of every other point are stronger, different output claims than the displayed generic enclosure. This comparison alone establishes no novelty for either implementation or proof mechanism.
- **NOTE — numerical and operator mismatches.** Local-maxima tables are not global-argmax proofs. MP upper bounds are not Padua asymptotics. Classical one-variable Fourier/Chebyshev expansions are not two-variable Padua formulas. The latter comparisons rely on the fresh notes' declared reading and inherited source records; this reviewer did not independently reread those old full texts.
- **NOTE — centered target must remain exact.** H uses `N=n+1/2` and `-1/N`, with one constant valid for both parities and `O(log N/N²)`. A search hit containing the same gamma/log fragment or a numerical decimal does not establish this theorem. H is analytic at the corner; transfer to the global constant invokes G01 (eventual argmax suffices asymptotically). This review does not alter their proof statuses.

## Executed searches and residual limits

Three additional independent queries were executed on2026-11-07:

- `"Padua" "Lebesgue" "1.846160"`
- `"Padua" "Lebesgue" "sharp" asymptotic corner`
- `"Morrow-Patterson" "Lebesgue constant" 2025 2026`

The combined returns supplied the MP primary publisher link and lower-bound discovery records; no matching fine Padua theorem was identified in the returned material. This small search is a cross-check, not independent replication of every developer query. Shell commands read the named files, searched relevant index rows, read the branch reference for the input SHA, and calculated the four prose SHA256 values. No mathematical program was run.

The two source notes' complete citation graphs, inaccessible journal bodies, old Russian-source formulas/page images, and every URL/query result were not independently replicated. The root's eventual synthesis is not covered until separately listed in an addendum. This record therefore accepts the stated bounded source/claim distinctions only. It supplies neither an exhaustive novelty/priority audit nor manuscript/submission readiness.

## Focused addendum: root synthesis, 2026-11-07

Read the complete [root synthesis](literature-refresh-20261107.md), SHA256
`7334282c5e875a51618b9eb4ab7105bdbc9e94ea556a6e52f78db8cf2c5020e1`.
Requested reviewer configuration as recorded by the root: Astra high;
actual serving metadata remains unexposed. This addendum extends the
wording/source-comparison review to that snapshot, not the mathematical
proofs, Git/process changes, or all original tool executions.

**No BLOCKING or MAJOR finding in the synthesis within this scope.**
It credits ETNA's generic rigorous mesh bounds, states the cube factor
correctly, and expressly separates discretization guarantees from
independently checked outward rounding. It treats the KL numerical fit
as publisher-indexed evidence with direct-access/version limitations,
not an arXiv theorem or a freshly read journal PDF. The bounded no-match
conclusion, classical leading-term credit, historical corner observation,
and distinction between H's analytic corner result and G01's
computer-assisted global identification are preserved. Source-reading
statements are assigned to their actual readers rather than implying
that this reviewer repeated every inspection.

The query table contains ten rows of four displayed strings. This is a
review of the documented ledger's structure and wording, **not independent
verification that all forty queries executed**. Execution provenance is
the root's tool history. The text correctly prohibits adding overlapping
worker counts or treating query counts and decimal no-hits as exhaustive
coverage. The extra De Marchi2005 primary passages, root author-page sweep,
and exact publisher-indexed fit transcription were not independently
reopened by this reviewer; their attributed coverage remains root-reported.
No whole-paper negative conclusion is inferred for those sources.

The final link's reference to checking fresh facts and wording is bounded
by the explicitly listed independent passages and this addendum. It must
not be read as blanket independent verification of all search execution,
all primary-source claims, novelty, or publication readiness. No prose
correction or mathematical change is required for this limited acceptance.
