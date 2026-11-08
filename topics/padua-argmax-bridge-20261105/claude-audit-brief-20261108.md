# Claude audit brief — mathematics and both manuscripts

Prepared 8 November 2026, Europe/Oslo. Branch:
`codex/padua-argmax-bridge-20261105`. Content snapshot:
`59ffb4026ab4faca278b6de67be3e039e42314fe`; base/main:
`f70a260e5b5f9a01209dc8a05faabdcf8db1feeb`.

## Assignment

Conduct an independent substantive Claude audit of the completed results
and **both current manuscripts**, with separate verdicts for mathematical
support, the journal paper, the explanatory companion, and their agreement.
Manuscript quality is a primary part of this assignment. Read both texts
in full and assess their different readers and purposes.

Recommended allocation: Claude Opus 5.5 xhigh for the mathematical audit
and integration; choose and record an appropriate model/effort for bounded
editorial or technical tasks. Record actual identities and execution.
Read `AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md`,
the current log and the open handoff. The coordinator owns Git; only AC
merges. This brief prepares the audit; Claude has not performed it yet.

The older instructions in [handoff 18](handoffs/18-audit-manuscript-and-results.md)
describe an 88-page draft. The current targets below replace that draft
as manuscript inputs. Carry forward the deferred scientific/evidence
scope in [handoff 13](handoffs/13-audit-complete-gap.md),
[handoff 15](handoffs/15-audit-sharp-correction.md) and
[handoff 16](handoffs/16-audit-with-literature-refresh.md), using the
current completed degree coverage and source records. Their dated open
gaps and draft metadata are historical checkpoints.

## Frozen inputs

Paths in this brief are relative to this topic unless shown as repository
paths. At the content snapshot, the manuscripts have these identities:

| Target | Sources | Source baseline | Recorded PDF |
|---|---|---|---|
| Journal paper | [paper/main.tex](paper/main.tex), all active `paper/sections/*.tex`, `paper/references.bib` | Complete paper tree frozen at `c6e195fa5211d4504fd2638f3c7686368e28daee`; latest mathematical prose source `177be83bcb03204ae30c74355ad387ac52f42cb5` | 48 pages; 640116 bytes; SHA-256 `07db86350e74f66a46269965ace65300750f5405ddcd9d30f8daeb59411ca0f0` |
| Explanatory companion | [companion-paper/main.tex](companion-paper/main.tex), all active `companion-paper/sections/*.tex`, `companion-paper/references.bib` | `ac945041ce73b74c2c4ec29c42ebeb8773e7a9b8` | 162 pages; 1153227 bytes; SHA-256 `2ec6b0723ccea6eef1368dfa0c974c4ec679a3279ef84d6ccb696c4a42c7d2f7` |

The actual checkout may also contain this brief and its handoff. Record
that head and verify the paper tree and companion TeX/bibliography
sources still match these freezes. Companion documentation was added
after its manuscript source freeze.
Read both README/BUILD records and [template provenance](paper/template/README.md).
The exact used Springer class and numbered bibliography style match AC's
uploaded December 2024 package. There are 13 references in alphabetical
numerical order. The original journal paper and its existing PDF are to
remain intact during this audit; write proposed manuscript edits as findings.

Existing distinct Sol max reviews are inputs to challenge and check:
[consolidation](paper/consolidation-audit.md),
[affirmative prose](paper/affirmative-style-review.md),
[expanded Section 5](paper/section5-expansion-review.md), and
[complete companion](companion-paper/review.md). Their stated coverage
helps locate prior corrections. Independently reconstruct consequential
arguments and new explanatory calculations.

## 1. Mathematical and computational support

Reconstruct the two results at the exact Padua convention: nodes
`(cos(j*pi/n),cos(k*pi/(n+1)))`, `j+k` even, total degree at most `n`,
with the exceptional highest first-coordinate kernel coefficient **one**.

- **Sharp corner expansion**, both parities, `N=n+1/2`:
  `Lambda_c=(4/pi^2)(log N+gamma+log(8/pi))^2+kappa-1/N+O(log N/N^2)`.
  Check the exact finite rows, endpoint weights, uniform summation and
  limit interchanges, the nonzero smooth residual correction, the
  cancellation ledger and half-step substitution. The corner theorem
  is analytic; its remainder constant is finite and degree independent,
  with no claimed numerical value. Start from
  [H](theory/H-sharp-corner-expansion.md), H01/H04/H05 and the current
  Section 3, then follow their canonical dependencies.
- **Exact global maximizers**, every integer `n>=2`: even degrees have
  `{(-1,-1),(1,-1)}`, odd degrees `{(-1,-1),(-1,1)}`. Check strictness
  at every other point, physical chart coverage, parity and collisions;
  the completed-model/finite-row comparison; selected-pair floors;
  near/far/corner estimates and degree-dependent norm. Start from
  [G01](theory/G01-all-degrees.md), E14, the current Section 4 and its
  included comparison source. The analytic tail starts at 320 and
  retains its certified constant input. The hybrid far and corner
  branches start at 192 and 256 respectively, with their own guards.
- **Finite completion**: one Bernstein scheme for `2..40`, phase covers
  for `41..319`, and the analytic tail cover every required degree.
  Check the signed positive-interpolation implication, strict corner
  leaves, complete closed covers, true global norm, mandatory grid norm
  with analytic leaves, actual-near defect guards and squared-corner
  scaling. Read [small-degree unification](paper/small-degree-unification.md)
  and its exact run inventory: fresh `2..16` checking and reused accepted
  `17..40` witnesses. Degree one has a separate elementary explanation.
- **Actual evidence**: [compact return](compact-return.md), its linked
  technical/mathematical checks, the frozen hybrid engine and essential
  evidence index. The Syvert return has 280 primary/fresh pairs covering
  exactly `41..319` plus control 511; all 560 essential rational proofs
  were reconstructed locally. Complete histories at random degrees 199
  and 238 were inspected, and fresh native verification ran at those
  degrees. Full unsampled histories remain on Syvert under AC's approved
  selective-retention policy. Inspect arithmetic trust, source/account
  links and replay limits at their actual scope.

Independently execute consequential checks appropriate to concrete proof
obligations and record their inputs/results. Use the existing manifests,
preregistrations and caps for a native replay. A missing artifact is an
identified verification limit with a retrieval/regeneration route. Keep
bulk histories on Syvert; a whole campaign or gigabyte transfer needs a
specific unresolved audit reason. The existing analytic H proof requires
paper reconstruction rather than a numerical fit or degree campaign.

## 2. Journal manuscript: independent editorial assessment

Read the 48-page paper first as a standalone submission aimed at
**Constructive Approximation**, before using the companion to fill gaps.

- Does the introduction identify the problem, both mathematical strands
  and their value? The earlier asymptotic/structural results already had
  paper value before the all-degree bridge. Assess the contribution and
  balance accordingly.
- Is there one understandable proof chain, with conceptual signposting,
  clear definitions and checkable essential steps? Locate places that
  remain too compressed for its intended specialist reader. The
  companion can explain routine details; the journal article must state
  its own premises and complete proof obligations.
- Assess the balance of Sections 3–5, especially the long comparison and
  finite certificate explanation. Section 5 was deliberately restored
  from three to five pages. Recommend concrete improvements to order,
  exposition, redundancy or secondary material, preserving necessary
  details and the main results. Explain the benefit of each proposed cut.
- Check notation, claims versus displayed estimates, cross-references,
  figures/tables, abstract/title, references and rendered readability.
  AC prefers direct affirmative prose: remove redundant defensive
  contrasts, or state the actual required hypothesis plainly.
- Check author information, disclosures, journal template, applications
  paragraph and data/code availability for accuracy. Intermediate IDs
  are authorized until PR preparation; list final-ID/cosmetic cleanup
  separately from substantive missing premises.

Give a clear editorial verdict and prioritized revision list for this
paper. Mathematical acceptance alone does not settle its presentation.

## 3. Companion: university-analysis reader assessment

Read all 162 pages against the intended background: some university
analysis. AC's screenshot illustrated the required depth **throughout**
the document. Assess the later technical chapters as closely as the
preliminaries.

- Are specialized words and notation explained before use and connected
  to the construction? Examples include unisolvence, cardinal and
  angular kernels, checkerboard scalar products, Gram matrices,
  geometric sums, completed models, finite parts, derivative variation,
  defect floors, norm witnesses and interval certificates.
- Can that reader reconstruct the intermediate algebra and analysis:
  matrix entries, reciprocal sums, endpoint/cutoff estimates, quadrature,
  uniform limits, scalar/row coefficient tables, phase and degree
  monotonicity, and strict continuous-domain coverage? Check concrete
  passages that still hide work behind “direct”, “standard” or “summing”.
  State any additional prerequisite that is genuinely needed.
- Are standard tools given a usable statement, their meaning and the
  hypotheses needed here? Check every new worked example and derivation,
  including the finite trigonometric Bernstein proof, elementary
  cotangent limit, and BV half-cell bound. Equality of original formula
  blocks does not verify the added explanations.
- Assess motivation, transitions, pacing, notation reuse, local roadmaps,
  repetition and the phase diagram. Identify useful examples or figures
  and exact remaining gaps in explanation. The allowance is up to 240
  pages; use space where it improves understanding rather than targeting
  a page count.

Give a separate pedagogical verdict and concrete revision plan. A clarity
failure can be major for this goal while the underlying theorem remains
mathematically supported.

## 4. Agreement, literature and practical checks

Verify the same five-section/subsection structure, 13 formal statements,
90 numbered display environments, all 211 original display blocks and
113 reference labels/numbers. Additional companion derivations are
unnumbered. Compare theorem hypotheses, constants, coordinate conventions,
equality sets, evidence claims and bibliography directly. If the longer
text reveals a missing short-paper premise, record the issue in both
assessments and propose a coordinated remedy.

Read [literature refresh](literature-refresh-20261107.md),
[positioning](paper-positioning.md) and
[applications/source scope](paper/application-context.md). For novelty,
priority or mechanism judgments, apply the full IDEAS/literature gate in
the rules and inspect the primary sources needed for the judgment. In
particular distinguish the published leading growth, earlier numerical
fits/corner observation, generic rigorous Chebyshev-mesh norm bounds,
and the precise sharp expansion and equality-set theorem. Check the
three application citations at their actual scope. Give qualified
attribution/contribution recommendations and identify any important
remaining source comparison.

Preserve historical audit findings and their dispositions. The earlier
P1–P4 chronology findings remain recorded in audit-02-interim.md and LOG;
their status is distinct from mathematical correctness. Review the
relevant inherited obligations in handoffs 13/15/16. Final human review,
public evidence release and final-ID/readiness preparation are still
separate tasks. PR 27 remains draft; this audit does not authorize merge.
Its description predates the current manuscripts; use this brief and the
pinned branch records for current manuscript and evidence inventories.

Build into **new audit output directories** so the delivered originals
stay intact. From repository root, for example:

```bash
TOPIC=topics/padua-argmax-bridge-20261105
mkdir -p local-output/padua-argmax-bridge-20261105
PADUA_AUDIT_OUTPUT=$(mktemp -d "$PWD/local-output/padua-argmax-bridge-20261105/claude-audit03.XXXXXX")
PADUA_PAPER_OUTPUT_DIR="$PADUA_AUDIT_OUTPUT/paper" bash "$TOPIC/paper/build.sh"
PADUA_COMPANION_OUTPUT_DIR="$PADUA_AUDIT_OUTPUT/companion-paper" bash "$TOPIC/companion-paper/build.sh"
python3 "$TOPIC/companion-paper/check_correspondence.py"
python3 "$TOPIC/code/evidence_index.py" --check
```

Compare actual label numbers from the **fresh** `.aux` files and inspect
both PDFs/logs, including representative dense proof pages, figures and
page breaks. The existing `aux_numbers` helper can read those files.
`check_correspondence.py --artifacts` checks the default saved output
paths; distinguish that preservation check from your fresh-build audit.
Record dependency/version failures and the commands actually run.
Sources/build records permit regeneration; portable byte-identical PDF
output is not assumed. Keep outputs off Git. The current evidence index
is 396 entries / 32414 bytes; the conservative generated bound is
9774001 bytes against AC's 10000000-byte cap.

## Deliverables and next step

Write **audit-03.md** for the combined scientific/evidence assessment and
**audit-03-manuscripts.md** for the two manuscript assessments and their
agreement. If these names have since been used, select the next audit
number and record it. Each report should identify the candidate, actual
read/reconstruction coverage, model/effort, executed checks and limits.

Give separate verdicts for mathematics/evidence, journal presentation,
companion pedagogy and manuscript correspondence. For each finding give
a unique ID, severity, precise source/PDF location, reason, impact and a
concrete proposed fix; distinguish correctness defects from editorial
judgment. Report coverage of every section in each manuscript. End with
a short prioritized plan and your own useful proof/presentation ideas.

Follow the later-audit MINOR-fix rule for eligible record/link issues,
committing fixes separately. Preserve both frozen manuscript versions;
return proposed manuscript edits and material findings to Codex for a
coordinated response and focused review. The completed Sol max reviews
remain available as prior checks; this is the independent Claude audit.

Commit the actual audit outputs first. Then close the open handoff and
create a new numbered Codex response or publication-preparation handoff
in a separate handoff-only commit; push the working branch before the
reply. Keep external communication, submission, main, force pushes,
tags, `.github` and repository settings outside this task. Only AC merges.
