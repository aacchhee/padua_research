# Affirmative prose and application-context review

Status: **ACCEPT for the frozen editorial diff**, 7 November 2026. No
unresolved finding within this scope.

Auditor: distinct Codex review agent, requested Sol, max effort, under
AC's persistent explicit preference in place of the default Astra audit
allocation. Actual serving-model metadata is not independently exposed.
Rules read at `c4d692874bc7f5b98d4b55b2679308d35c8e706a`: `AGENTS.md`,
`agents/WORKFLOW.md`, and `agents/codex/CODEX.md`. The orchestrator controls
Git. This reviewer edited only this report and ran no native certifier,
new numerical campaign, or manuscript build.

## Scope and verdict

Reviewed the complete eight-file manuscript diff from
`c4d692874bc7f5b98d4b55b2679308d35c8e706a` to the frozen source commit
`4050f6861a44a88ec5d7941787703fbbe9d9ce4a`, including the surrounding
definitions, statements, proofs and certificate predicates at every
changed passage. Also read the complete prior
[consolidation audit](consolidation-audit.md), the
[approved application proposal and source-reading limits](application-context.md),
the Van Barel--Chesnokov reading record, and the existing author/disclosure
scope recorded in the topic log and baseline `main.tex`.

The changes replace methodological nonclaims with direct descriptions of
the argument and its requirements. They preserve the previously reviewed
mathematics and computational premises. The approved application paragraph
fits its sources and adds motivation for the interpolation operator's
data sensitivity. It makes no new claim about the rounding error of the
2010 recurrence algorithm or a truncated least-squares projector.

This is a focused fidelity and editorial review. It introduces no
mechanism, priority claim, theorem, status upgrade or new computation;
the full IDEAS novelty gate and a new broad mathematical/native audit are
outside this task. The completed consolidation review remains the
mathematical baseline, with its stated computational and release limits.

## Findings and preserved obligations

No BLOCKING, MAJOR or MINOR finding remains. No manuscript fix was made by
this auditor.

- All **204 displayed math blocks** across the seven active TeX sources
  are byte-identical to the baseline. Both main theorem environments are
  byte-identical. Of the twelve theorem/lemma/proposition environments,
  the sole prose difference removes “rather than two” after the unchanged
  cardinal-kernel coefficient one. Its formula and Gram-matrix proof are
  unchanged.
- The all-degree range, parity-specific equality set, uniform asymptotic
  remainder, exact corner normalization, unequal meshes, endpoint weights
  and collision continuations are preserved. The replacement domain
  remark explicitly includes all nodes, edges and collisions.
- The projection bound remains `Delta >= max(Q_h,Q_v)`. The finite-row
  telescope retains its actual rows, cancellation increments, two relative
  radii, one-sided actual-origin bound and separate norm. Deleting the
  origin nonclaim leaves the strict statement `E_n(0) > -bar_e` for
  `n >= 160` and its proof intact. The certified limiting-constant input
  remains explicit in the comparison, global completion and introduction.
- The selected-pair proof keeps its degree-41 coverage. The closed phase
  charts, strict regional comparisons, degree-192 far implication,
  degree-256 corner descent and degree-320 analytic onset are unchanged.
  The corner gate still uses the degree-dependent `M(n)`. The final
  coverage sentence now states directly that every integer `n >= 2` is
  covered.
- Positive interpolation still acts on smooth signed sums before the
  maximum over signs. The Bernstein vertex exception, strict punctured
  leaf test, complete closed partition, tangencies, actual-near physical
  guard, overlapping closed proxies, direct corner witness and entire
  triangle-intersection guard for analytic far leaves remain explicit.
  A tree with an analytic far leaf is still required to use the grid norm;
  the wholly numerical tree norm retains its own premise.
- The finite evidence inventory, exact rational reconstruction of 560
  essential proofs, arithmetic/compiler/native trusted base and selective
  retention remain stated. The final wording accurately distinguishes
  inspection of complete histories at degrees 199 and 238 from fresh
  native verification run at both degrees with distinct review. Those
  sample checks supplement the checks of all essential proofs and links.
  The unsampled histories stay on the production machine; permanent public
  release remains pending. The execution-record reference still identifies
  which small degrees were freshly rerun, so the established `2..16`
  replay versus reused `17..40` distinction is preserved.
- Author identity, correspondence, affiliation, ORCID, funding, conflicts,
  contributions and substantive AI disclosure are unchanged. Removing the
  redundant AI-authorship sentence leaves the sole human author and
  responsibility/final-review statements explicit.

The whole-source phrase searches were reviewed in context. Remaining
negative wording expresses mathematical exclusions, exact equality
conditions, elementary comparisons or the approved declarations. No
remaining defensive rhetorical nonclaim requires another prose pass.

## Added citations

Checked the paragraph and added metadata against the approved source
proposal's primary-source reading notes and the existing fulltext record
for Van Barel--Chesnokov. This review did not fetch or reread the three
primary papers anew.

| Citation | Supported scope used in the paragraph |
|---|---|
| Van Barel and Chesnokov (2010), DOI `10.1007/s11075-010-9392-y` | Discrete bivariate orthogonal-polynomial computations and least-squares examples using Padua sampling; the retained fulltext record locates these in Section 5, Examples 1--2, pp. 396--399. |
| Laguardia and Russo (2022), DRNA 15, 39--50 | Nyström and collocation methods for two-dimensional Fredholm integral equations on the square, within the proposal's inspected abstract/introduction and Section 2.1. |
| Landon-Cardinal, Govia and Clerk (2018), DOI `10.1103/PhysRevLett.120.090501` | Continuous-variable quantum tomography using Padua interpolation. The proposal's inspected accepted-manuscript Eq. (5) directly uses the Lebesgue constant in reconstruction error. |

The text stays at this application/motivation level. It imports neither a
new optimal-sampling theorem nor a final density-matrix guarantee. This
bounded check makes no exhaustive literature or priority claim.

The bibliography, actual citation set and explicit `nocite` set contain
exactly the same thirteen distinct keys. The built bibliography matches
the intended alphabetical author order: Beberok; the two Białas-Cież
entries; the two Bos entries; the three Caliari entries; De Marchi;
Kolomoitsev; Laguardia; Landon-Cardinal; Van Barel. Within equal leading
authors, the author-list and year order is correct.

## Checks actually performed

- Read-only `git show`/`git diff` against the two full commit IDs above,
  plus full reads and bounded line-context reads of the affected sources
  and existing records.
- Python byte comparisons of all displayed math blocks and claim
  environments; SHA-256/byte counts for all eight frozen files; comparison
  of working bytes with the frozen commit. All working sources matched.
- Citation, bibliography, built `.bbl`, input-graph, label and reference
  checks: seven active TeX sources, thirteen distinct citation keys,
  113 distinct labels and no missing reference target.
- Whole-active-source searches for defensive contrast phrases and review
  of each remaining match; `git diff --check` over the frozen paper diff
  passed.
- Inspected the orchestrator's existing PDF with `pdfinfo` and extracted
  pages 1--2 with `pdftotext -layout`, confirming the application paragraph,
  author/frontmatter and **46-page** artifact. Read the existing build log:
  no LaTeX error, undefined reference/citation, multiply defined label,
  package warning or overfull box was found. Underfull-box diagnostics are
  present. This was artifact/log inspection, not an independent build.

## Frozen identities

Paths are relative to this paper directory; the frozen commit is
`4050f6861a44a88ec5d7941787703fbbe9d9ce4a`.

| Active source | Bytes | SHA-256 |
|---|---:|---|
| `main.tex` | 5005 | `013789e91d291ae6763dcd8aa0caac8e35d18e26c394a16c074e3d37c7da66c9` |
| `sections/introduction.tex` | 8043 | `c8c9c35ba0577a6a17b0089b8413277024d03c1a904aa582f7967d082db1ba78` |
| `sections/preliminaries.tex` | 3719 | `f5cd4b1dc6ab98e31a1a51a5ef91a7d1336d531fe06bdf0026992cff45ec920b` |
| `sections/corner-unified.tex` | 19836 | `c74e94d3aa15d446d49c425705e241475cd00cbded7728d76576f5efdbf73bf6` |
| `sections/localization-unified.tex` | 24867 | `180efdc2bc10d00d9a5f6aa47befe538023b2c349db853a5481042b7a7cfe361` |
| `sections/comparison-unified.tex` | 58736 | `be20756e98358fbd483135adddf545128640ae3e4c90f763ba427283a0a250ce` |
| `sections/certification-unified.tex` | 7845 | `6a9b8845f04d246445cba5cbb1b684fecff83770aea16e475aaf4f7fa1b10d3e` |
| `references.bib` | 4514 | `8d59b40ae352413ca57afe5a33b4427244a00c767d4ba558adfb9b0775bd2cb7` |

Observed off-Git artifact at
`local-output/padua-argmax-bridge-20261105/paper/main.pdf`: 632068 bytes,
SHA-256 `919058546f5d3ac09a64a05f24511da6cd0b91022fe28a459a2d23e8781cefd9`.
The corresponding `main.log` is 40026 bytes, SHA-256
`6e38775113847636befef7128de304e07b7cad8522390f17c2d4e018a6c97f31`.

The verdict applies to this editorial diff. It preserves the prior
consolidation audit's separate outstanding whole-batch audit, native,
priority, human-review and publication-release boundaries.
