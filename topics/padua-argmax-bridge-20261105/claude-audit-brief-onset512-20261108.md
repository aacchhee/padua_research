# Claude audit brief — onset 512, independent arithmetic and revised manuscripts

Prepared 2026-11-08. Branch: `codex/padua-argmax-bridge-20261105`.
This is the next substantive audit of the changed proof and its integrated
presentation. It supplements [the earlier brief](claude-audit-brief-20261108.md),
[audit-03](audit-03.md) and [response-03](response-03.md); it does not repeat
every historical case or reopen accepted unchanged results without a concrete
dependency or defect. No audit execution or acceptance is claimed by this brief.

## Frozen inputs for the next substantive audit

| Field | Identity |
|---|---|
| Final integrated manuscript source commit | `24a98db4c3c4c4d0eede2e3929532956df87911b`; later material revisions require a new reviewed freeze |
| Final paired TeX/Bib source-freeze commit | `24a98db4c3c4c4d0eede2e3929532956df87911b` |
| `check_correspondence.py` final source baseline | `24a98db4c3c4c4d0eede2e3929532956df87911b`, adopted in source/reproduction snapshot a433c7d; root final artifact check PASS19/85/116 |
| Revised paper PDF | `local-output/padua-argmax-bridge-20261105/onset512-paper-20261108/main.pdf`;51 pages;733598 B; SHA-256 `1346fc2891e2cdd5deb6db4b1a5928a2a7bac05c1838999b1a1dee1fc0db1d2c` |
| Revised companion PDF | `local-output/padua-argmax-bridge-20261105/onset512-companion-20261108/main.pdf`;147 pages;1171187 B; SHA-256 `83ca42c8052ccd760c3929ff0c30cd1667971476ae111736fe371b30e4581af2` |
| I25 full result and independent rerun | Complete: 942 certificates / 471 degrees; six-certificate independent replay passed; see J03 and RESULTS.json |
| Supplemental Sol max frozen-candidate review | ACCEPT correctness/exposition at 24a and these PDFs; report SHA-256 `fe935ea03a245dd6301370cc02b4ac826cacec55d036b8c99942a4d00d44dff9` |
| Complete reproduction source snapshot | `a433c7dfc61d1ed61799a7d919beb8334a2593b6`; ZIP22,105,198bytes, SHA-256 `66acbadb34ba51a5a2c99bd34a681deef6de433da193202830d00c0aa0f4cc03`; see deposit inventory |

The source freeze and helper adoption are two ordered commits in one reviewed
batch: commit final paired TeX/Bib sources, then install that existing SHA in
the checker. See [revision boundary](companion-paper/CORRESPONDENCE-REVISION.md).
Do not substitute the historical 48/162-page artifacts for the revised PDFs.
The [small-bundle recipe](zenodo-deposit/RECHECK-SMALL-BUNDLE.md) can recheck
JSON witnesses directly from the2.84MB I25 bundle using separately trusted
source. It is an alternative future-audit input recipe, not an additional
reported execution. The completed runs retain their original preregistrations.

## Assignment and authority

Use Claude Opus 5.5 xhigh for substantive mathematical audit/integration;
record actual model and effort, audited identities, coverage, commands, exits
and limitations. Read the repository rules, Claude role, current LOG and open
handoff first. This is approved architecture B and the already approved I25
route, with no new novelty or priority claim. Apply the literature/IDEAS gate
only if making a new novelty, mechanism or priority judgment.

Audit locally: **no Syvert access or remote computation**. Do not launch a new
native campaign, retry a failed scientific run, alter thresholds, or execute
archive code. Consequential reruns must use the actual pinned data and existing
reviewed commands/caps; propose a concrete prospective bounded run if those do
not address a finding. Root owns Git, handoffs and integration. No external
publication/contact or PR-readiness promotion is authorized; PR 27 remains a
draft and only AC merges. AI declaration, ORCID and contribution text remain
reserved to AC. AC confirmed the existing no-specific-grant funding statement;
the earlier funding question is resolved. DOI/public deposit remain AC's task.
See the dated decisions in [handoff 29](handoffs/29-onset512-and-manuscript-revision.md)
and their canonical LOG disposition, rather than repeating or reversing them.

## Read first, then follow material dependencies

1. [J01: all-n gates](theory/J01-onset512-gates.md),
   [J02: elementary constants](theory/J02-elementary-constant-enclosure.md),
   [analytic preregistration](code/onset512_analytic/PREREGISTRATION.md),
   [checker](code/onset512_analytic/check.py),
   [receipt](code/onset512_analytic/receipt.json), and the
   [distinct supplementary reviews](independent-checks-onset512-response.md).
2. [Local campaign summary](local-onset512-summary.md),
   [preregistration](preregistration-onset512-local.md),
   [data-only return reader](code/local_onset512_campaign/return_bundle.py),
   and the independent campaign/archive review in the review record above.
3. [J03: independent arithmetic soundness and implication](theory/J03-independent-phase-checker.md),
   all four source files in [its directory](code/independent_phase_checker/),
   pilot/full preregistrations and prospective amendments there;
   [completed summary](code/independent_phase_checker/independent-phase-summary.md)
   and [RESULTS.json](code/independent_phase_checker/RESULTS.json). Distinguish
   original prospective record wording from the completed accepted outcome.
4. [E-01–E-04 repair and actual commands](compact-verifier-audit03-response.md),
   [verifier](compact_pack/verify_compact.py),
   [focused controls](code/compact_verifier_audit03/check.py), and their distinct
   review. Then the [deposit preparation](zenodo-deposit/README.md) and
   [small custody index](cold-storage.json) for access limitations.
5. Both final manuscripts in full: [paper](paper/main.tex),
   [companion](companion-paper/main.tex), their included sections and Bib files,
   both BUILD/README records and template provenance. Read
   [Sol max supplement](manuscript-onset512-solmax-review.md),
   [notation pass](notation-pass.md), [audit-03 manuscript findings](audit-03-manuscripts.md)
   and their response-03 dispositions. The supplement is additional evidence,
   not a substitute for this Claude audit.

The inherited sharp-corner theorem remains in scope when reading the complete
texts. Follow [H](theory/H-sharp-corner-expansion.md) and its corrected canonical
dependencies as needed. [F03 identities](theory/F03-identities-support.md) are
proved support; the original [F03 sign target](theory/F03-origin-sign.md) remains
OPEN and is not a premise. Audit dated source corrections, including H04's
alternative majorant: both historical and revised coefficient orderings are
valid; the revised one is weaker. Preserve historical source pins and reports.

## Mathematical acceptance criteria

Reconstruct the exact original Padua convention, endpoint weights, highest
first-coordinate coefficient one, unequal meshes, physical charts and parity
maps. Require an explicit chain to the two exact nonnode-corner maximizers for
every integer n>=2 and to the sharp corner expansion for both parities.

- **J01:** derive the radius-one quadratic from the signed relative bound;
  verify positive curvatures, square completion, the maximum/vertex identities,
  and all-real-n monotonicity, including the fixed half-radius maximum. Check
  the n=512 rational bases: maximum <41/1000, vertex <1/2 and P(1/2)<-1/7.
  Reconstruct the selected-pair class coverage and uniform Q>1/20 floor from
  295; no interpolation in radius or sampled-degree extrapolation is a proof.
  Verify every sign in the absolute gate, tangent condition and persistence,
  monotonicity, G(512,1)>1/2 and G(192,pi/2)>3/100. Check seams at radii 1/2
  and 1, actual-corner descent on the closed pi/4 square, ties and strictness.
- **J02:** reconstruct endpoint cancellation, uniformly convergent series,
  signs and convolution, analytic K=3 remainder, and elementary pi/log/gamma/
  even and odd zeta brackets. Independently run the small Fraction checker.
  Verify the consumed kappa>9/10, j>23/250, 0<t0<221/500,
  Cstar<4629/2500 and C_infinity<9/4; no old Arb decimal or unproved upper
  bound on kappa may reappear as a premise.
- **Integration:** the analytic tail now starts at 512, finite phase coverage
  is 41..511, and Bernstein completion is 2..40. Verify the retained far-192
  and corner-256 guards, finite floor tiers, global norm, actual-value guards,
  corner rectangle and pi bracket consumed by frozen certificates. The new
  analytic tail has no finite-certificate premise. J01's source map identifies
  obsolete annular applications and retained component estimates; inspect that
  map rather than treating every historical E01–E15 theorem as newly required.

Give an actionable proof improvement when it makes a dependency clearer or
removes a real gap. If a new gap blocks completion, issue a clearly labeled
**interim audit** with its exact statement, obstruction, plausible proof routes
and a concrete discriminating check. The older request for interim gap/proof
ideas concerned a gap subsequently closed; it is not an instruction to declare
that old gap open again or start a general research campaign.

## Evidence identities and distinct trust routes

All following payloads remain off Git under
`local-output/argmax-bridge-20261105/`. Authenticate independently before use.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| Original `actual-return-20261107/return.tar.gz` | 36045486 | `b00fd57f85ce6d96a6c1fa01e2307abd815088bb8fcb28b1587657ef142b109a` |
| New canonical `onset512-return-20261108.zip` | 81602992 | `da63280a7e4aec86fa52e3f8384620fbf07939006ab5f6f70222fa2485816e7e` |
| New derivative `onset512-certificates-20261108.zip` | 945235 | `c22d600cb67462918587b01f2ef5adcbf9030b825fb0f2cc79c1b9c27c7da8c8` |
| New `onset512-local-20261108-essential-inventory.json` | 75479 | `d7cea34dd64d9df329d1398c2418fbf984a9084b135cad695866a9c437551740` |
| Completed `i25-evidence-20261108T112304Z.zip` | 2843611 | `d1d03156dde4248fecaa25d0144cd73c7c5414f28b66a39099342b31f2f7e0f8` |
| Separate `onset512-independent-review-20261108.zip` | 51749 | `96f84b294b724b74bc33c112a2633bde14fed5c9220cb11196c60dae5c12ab28` |

The original return contains 280 primary/fresh pairs, exactly 41..319 plus
511, or 560 certificates. The auditor's 276 unsampled native replays plus the
four earlier replays completed all 280 degrees locally; see
[actual replay record](audit-03/replay276.md). Those use the same scientific
engine, with a disclosed non-pinned Ubuntu runtime: **not independent arithmetic**.

The new canonical ZIP contains all 191 new pairs, 382 passes, for 320..510,
with recorded EXIT0/ECHILD and no retry, timeout or cleanup kill. Its sampled
complete histories are 475 and 458; all essential proofs were reconstructed
by the data-only reader and independently reviewed. The small certificate ZIP
is byte-matched derivative data, not the provenance closure. Check source/runtime
pins, admissions/accounting, fresh linkage, coverage and sampled closure against
the actual canonical ZIP. The review includes twelve corruption controls;
neither packaging nor archive integrity proves interval-evaluator soundness.

I25 is a different route: from-paper finite sums and its own interval bounds
recertify every retained key, full closed trees and strict predicates. Its
accepted v2 pilot covers eight certificates with 31 arithmetic and 27 corruption
controls; failed v1 and the prospective seam amendment remain recorded.
The full plan is exactly **942 (n,pass) inputs**, every n=41..511 twice,
in four disjoint deterministic degree groups. Full preregistration SHA-256 is
`9e4da4615cc40c7e23f8061a560e2f3fd8e696d13c64db3f0249ebb489e9cb4a`;
amendment 01 is
`228fd0230efd1e76661d02c03d886b5dbf80d41df844b3e2ffd7346a90c73f18`.
The latter distinguishes measured total CPU acceptance from kernel process
limits. Full result is **complete and accepted by distinct supplementary review**:
all 942 trees / 471 degrees, four EXIT0 workers, 31 arithmetic controls each;
2519.420775278 inclusive CPU-s and 646.839168173 wall-s. A distinct reviewer
separately accepted both passes at 41,458,511 (six trees) plus 31 controls.
These are recorded executions, not extrapolation from the pilot. The substantive
Claude audit remains pending.

Audit J03's explicit Python/Fraction, NumPy indexing and IEEE binary64 trusted
base; rational pi, argument reduction, Taylor error, outward rounding and
pairwise summation; removable collisions; reflection and closed-seam aliases;
exact key reconstruction; polygon maxima and degenerate cases; GRID/TREE norm;
near/far overlap and ACTUAL_THREE squared Peano. Own bounds must establish
strict margins, not merely overlap native intervals. This is substituted-bound
recertification, not universal containment of stored native endpoints. Analytic
kernel identities, folding, selected-pair floors and squared Peano remain proof
premises. Verify the completed full run’s exact 942-input union, source
and input hashes, all four exits, controls, no retries and measured resource
acceptance before concluding which G-1 evaluator premises it replaces.

## Focused operational checks and reruns

Independently rerun the small analytic check and the actual data-only verifiers
using the precise commands in their linked records. Do not trust a replacement
synthetic archive as the positive test. For the new canonical return:

```sh
python3 -B topics/padua-argmax-bridge-20261105/code/local_onset512_campaign/return_bundle.py verify local-output/argmax-bridge-20261105/onset512-return-20261108.zip
```

For E-01–E-04, inspect the focused patch and rerun both the old actual return
with `--expect-plan all` and its 30 controls, using separate audit output paths.
Require trusted/archive namespace separation and forced trusted provenance;
ledger/history/admission, status, receipt, attempt and raw-hash linkage; exact
fresh tree/key sets; explicit subset/full-plan behavior; and cumulative-size
rejection before reading the next member or charging an alias. Allow fresh
numerical bounds to differ. A rehashed semantic corruption must still reject.
The early existing 24-GiB cap is not a low-memory claim; absent unsampled raw
histories have recorded identities, not locally rehashed bytes. The old package
retains its old verifier identity; current repairs cannot be attributed to the
historical release. Distinct Astra reruns are already recorded; audit their
scope and execute consequential independent checks, without a new native job.

For I25 use the actual completed full outputs, including per-worker inputs,
observations, controls, summaries and outer accounting. Record exactly what
the auditor reruns. A further full replay requires a concrete unresolved reason
and prospective reviewed resources; historical prospective strings do not
override the completed outcome.
Deposit preparation is not custody: empty delivered entries and a compatible
storage-tool smoke do not prove Zenodo delivery, DOI creation or remote retrieval.

## Both manuscripts: correctness and whole-text editorial assessment

The supplemental Sol max review and final root build/artifact checks are now
complete, including E1/E2/E4, the full arithmetic derivation and readable phase
figure/trust table. Final logs have no errors/warnings, undefined references,
multiply-defined labels or overfull boxes; underfull-box diagnostics remain.
This is input evidence for the next substantive Claude audit, not a claim that
Claude has already performed that audit. AC’s latest criteria make page count
secondary to necessary explanation: no step should appear without its reasoning;
named tools should have usable statements/hypotheses or citations. Optional
further cuts are not acceptance conditions.


Read the revised paper as a standalone Constructive Approximation submission,
then the entire companion for a reader with some university analysis. Give
separate verdicts for mathematics, paper exposition, companion pedagogy and
their agreement. The sharp expansion and location theorem both need appropriate
weight. Check every section, including late technical chapters, for definitions,
tools, hypotheses, equality cases, derivations, proof consumers and cross-links.
The paper must contain its own necessary premises. The companion should explain
the actual reasoning, rather than repeat compressed assertions or require an
unstated prerequisite. Recommend specific cuts, reorderings or expansions with
locations and their mathematical/pedagogical tradeoffs; no fixed page projection
overrides proof completeness.

Verify paired headings, formal statements, numbered displays, labels and compiled
numbers, bibliography, both main numbering setups, constants and scope. Use the
final correspondence helper and new build/output directories, with preserved
original PDF paths supplied explicitly, as documented in the revision note.
The companion limit is five times the actual revised paper page count. Check
both rendered PDFs, build logs, dense proofs, figures and page breaks. The old
48-page paper SHA is
`07db86350e74f66a46269965ace65300750f5405ddcd9d30f8daeb59411ca0f0`;
the old 162-page companion SHA is
`2ec6b0723ccea6eef1368dfa0c974c4ec679a3279ef84d6ccb696c4a42c7d2f7`.
Keep those originals intact. A paired identical silent statement mutation must
fail the independent source baseline even when pairwise comparison passes.

## Deliverable

Write a substantive audit record at the root-allocated next audit path; do not
allocate a handoff or overwrite audit-03. State audited identities and complete
coverage, distinguish inspection/execution, and give separate acceptance verdicts
with BLOCKING/MAJOR/MINOR findings, locations, evidence and remedies. Include a
dependency/trust conclusion for the new tail, finite coverage and I25 route;
whole-manuscript and paired-artifact findings; unresolved data-access limits;
and concrete proof-improvement ideas when useful. Cross-reference response-03
for inherited findings instead of silently upgrading its pending rows. P1–P4
remain historical process findings under AC's recorded disposition, with no
mathematical remedial work, waiver or backdating. Any new material repair gets
a focused review; unchanged accepted historical claims do not need a blanket
restart. Final IDs, public deposit and PR readiness remain separate work.
