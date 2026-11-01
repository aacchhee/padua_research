# Part 2 input and registry provenance

Mechanical review only. No new mathematical result, numerical rerun, certification,
or priority claim is made here. Rules were read at
`a09d910ae7d5526b1e216066421a0bee7fc20da4`.

## Immutable sources

| Role | Full commit |
|---|---|
| Part 1 head and initial rules | `a09d910ae7d5526b1e216066421a0bee7fc20da4` |
| Part 1 Claude audit that arrived during this run | `95279b833bca5967fcf47c1b71a56ff622185b4e` |
| Part 1 response and completed minor dispositions | `7b8884a2f98518784ff3698dd2f3f9c49c9cdd62` |
| Main observed by orchestrator | `9739a0c56b7a3976422ce60a8441bfbbfd6554df` |
| Programme PR #6 head | `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e` |
| Part 1's pinned programme | `cadb35066160e466cb1704b9791ad6f374446422` |
| Lanczos head | `a2dd845b8a231e1b00733e1361e2a9ad3bad222f` |

The complete file inventory, source commit, Git blob, byte size and SHA-256 for
each selected input are in `evidence-manifest.json`. Inputs are read with
`git show COMMIT:PATH`, not inferred from mutable working-tree bytes. The script
fetches no remote files. The inventory is the complete Git-object retrieval list
for this mechanical manifest; it is not a claim that every listed source was
scientifically verified. All Part 1 topic files (including its three theories,
LOG, B1 attempt, every code file and every output) are pinned. Both complete
`checks/code/decisive/gen4-2/` and `checks/code/decisive/gen1-3/` trees are pinned.
The old programme versions retained for comparison have their own source labels.

Resolved requested theory names under `topics/programme-ideas-20261031/theory/`:

- `programme-ideas-claude-04-padua-corner-expansion.md`
- `programme-ideas-claude-05-padua-corner-argmax.md`
- `programme-ideas-claude-06-padua-lebesgue-maxima-counts.md`
- `programme-ideas-claude-N01-symmetrised-product-inertia-count.md`
- `programme-ideas-claude-N02-windowed-rational-lanczos-instability.md`

The B3 prerequisite is
`tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-304-square-case-commutator-bounds.md`
at the Lanczos pin. Cite the requested local ID
`PD-T?bivariate-lanczos-claude-304(a)`; its allocated upstream ID does not change
the task's citation convention.

Part 1 dependencies retain the literal label
`PD-T?proof-attempts-codex-0N (audit pending)` as required by the user's original
instruction. That label now records the historical requested wording; current
audit acceptance and completed dispositions are qualified below. Hashing or
reading a Part 1 proof alone does not constitute its Claude audit.

Update during this run: the Part 1 Claude audit arrived at `95279b833bca5967fcf47c1b71a56ff622185b4e`.
The orchestrator stopped dependent work, read the audit, recorded the impact and
merged it at `818ca4ad0942eb4743860f913a299ff30d959dae` before resuming. The
manifest separately pins its `audit-01.md` and all nine-file audit/support scope
(the report plus eight support files), while retaining every original scientific
input at `a09d910…`. At that delivery the report accepted the three proofs with
minor findings awaiting disposition; that historical qualification was not an
audit of Part 2. In particular F2 requires rigorous corner handler (D) and edge-node
handler (E) coverage for A5: Part 1 theorem 03 does not make its separate
MEASURED decision trace a proof of those handlers.

Subsequent update during the same run: the Part 1 response arrived at
`7b8884a2f98518784ff3698dd2f3f9c49c9cdd62`. The orchestrator reports reading it,
recording the impact and merging it at `95ca473cc21b2db6a9a46c62e86495ebe94eb397`.
All minor findings F1–F6 now have accepted documented dispositions. The three
Part 1 mathematical proofs remain accepted; no proof body, developer code or
scientific output changed. Result 03 moved its explicitly MEASURED execution
paragraph from Statement to Checks; result 02 clarified the source of its
dimension claim. The original `a09d910…` scientific pin and `95279b8…` audit pin
remain in the manifest. A distinct `part1_response_arrived` source pins all 12
paths changed between the audit and response commits, derived with read-only
`git diff --name-only`, so editorial changes do not overwrite earlier provenance:

- `LOG.md`
- `attempts/T-A1.md`
- `attempts/T-A5-partial.md`
- `attempts/T-B5.md`
- `evidence-manifest.json`
- `pr-prep.md`
- `preparation-checks.json`
- `proposed-record-changes.md`
- `response-01.md`
- `theory/proof-attempts-codex-01-padua-corner.md`
- `theory/proof-attempts-codex-02-generic-commutant.md`
- `theory/proof-attempts-codex-03-degenerate-maxima.md`

These paths are relative to `topics/padua-proof-attempts-20261101/`.
The F2 disposition preserves the additional rigorous (D)/(E) handler obligations;
accepting the Part 1 local theorem does not discharge them. This update records
the actual sequence rather than retroactively calling the initial audit pending
state accepted. It supplies no Part 2 audit or new mathematical execution.

## Actual upstream changes and integration

Compared the complete requested source paths between `cadb350…` and `9bd14…`.
The three rule files have identical blobs. The five requested theory files and
both decisive code/output trees have identical blobs. The B1 decisive and
adversarial records are unchanged. The authoritative `OPEN_TARGETS.md` and
`checks/decisive-gen4-2.md` changed, so the user's exception requiring integration
is triggered by inputs actually used here.

`OPEN_TARGETS.md` changes that affect this task:

- A1 specifies the continuous extension of the sine quotient at integer multiples
  of pi.
- A2 corrects the cited global theorem to supply only the corner upper bound;
  the matching corner lower bound is explicitly still required.
- B1 fixes nonvanishing poles, injective evaluation, the admissible degree range,
  and the specified meaning and parameter class of general position.
- A4 separates local neighbourhood control, global control and finite verification;
  point expansions alone do not cover neighbourhoods.
- B3 now fixes computed and commuting classes, the pivot bound, the pair metric,
  marginal spectral boundary gap, and the nearby reference class. It specifies
  nonempty reference class and count equality as separate obligations, with
  positive gap, finite positive C, and a fixed n,p negative family. It explicitly
  requires reading the Lanczos square-case prerequisite.
- B5 replaces a disconnected-domain analytic argument with a polynomial-minor
  route; this matters when checking the inherited Part 1 dependency.
- Optional B4 excludes unsaturated symmetry centres and distinguishes saturated
  centres from counterexamples.

`checks/decisive-gen4-2.md` adds response-02 and PR-preparation qualifications:
legacy certification/theorem/precision language is corrected, and the proposal
section is historical. Counts remain MEASURED; expansion and argmax remain OPEN.
No stored data or code in the requested trees changed.

Other compared metadata changes are `literature/INDEX.md`, `literature/CORPUS.md`,
`state/IDEAS.md`, `ideas/candidates.md`, the finite-Favard theory, N03 and N05;
these are source qualification, registry or adjacent-scope changes. Exact
old/new blobs for every changed compared path are in the manifest. New audit and
response records at the programme pin are also explicitly pinned rather than
mistaken for pre-existing Part 1 input.

Recommendation sent to the orchestrator: merge the pinned programme head, never
rebase or rewrite. The orchestrator reports the integration was completed without
conflicts at `b3c333b6519740c21953ed41501a66d37768c1f2`, after recording the impact.
No main merge was needed. The manifest's `inputs` are immutable inherited source
objects; its `outputs` include only new files beneath this Part 2 topic directory.
Imported upstream changes are consequently not listed as newly generated outputs.

## Relaxed registry scan and source shortlist

Read `state/IDEAS.md` at the programme pin across its complete headings,
identifiers, aliases and summaries, including historical rows and every
obstruction/disposition table. This covers the charter, MZ, lattice and programme
sections. Read the five requested full programme theory records and the full
Lanczos prerequisite. Read the literature index before source-specific records.
The scan is mechanical support for the developer's per-target gate; it does not
replace reading each shortlisted full entry before developing that target.

Executed a case-insensitive content scan of Markdown under `tracks/`, `topics/`
and `literature/` in the pinned programme tree, with:
`Lebesgue|corner|degenerat|crease|inertia|symmetri.ed.product|windowed.rational|top.form|Ppt|Kachkov|Bultheel|2605.23299|Kolomoitsev`.
It matched 137 paths. The registry itself was read separately in full. Source
references and nearest records for the developer's gate are:

| Target | Closest registered entries and source paths | Applicable recorded obstruction / cheapest gate test |
|---|---|---|
| A2 | `IDEA?programme-ideas-claude-17` (gen4-draft-2); programme theory -04; `LIT?programme-ideas-claude-63` in `topics/programme-ideas-20261031/lit/baseline.md`; `LIT?lattice-codex-13` in `literature/lattice-unisolvence/records/padua-2006.md` | Global asymptotics supply only a corner upper bound; fit agreement proves no lower bound. Check the exact corner identity and theorem domain before transferring a method. |
| A5 | charter `IDEA-048`; programme IDEA-17 and theory -06; Part 1 theory -03; `LIT?programme-ideas-claude-72` in the programme baseline | Degenerate tolerance tests, early sign-pattern return, discarding by an escaping Newton iterate, and approximate crease coincidence do not prove completeness. First require a finite reduction and a checker-verifiable exclusion rule. |
| A4(a) | programme IDEA-17 and theory -05; source paths for A2; `checks/adversarial-gen4-2.md` as a follow-up source locator | A bounded measured gap and point expansions do not bound neighbourhoods or the global square. Check the edge identity before attempting its asymptotic gap. |
| B3 | `IDEA?programme-ideas-claude-09` (gen2-draft-3), programme N01; Lanczos local -304(a); `LIT?programme-ideas-claude-86` in the programme baseline | General symmetric cluster pairs need not be computed sections with fixed positive pivots. Verify class membership, pivot lower bound and spectral boundary gap first. |
| B1 | `IDEA?programme-ideas-claude-03` (gen1-draft-3), programme N02; `checks/decisive-gen1-3.md`, `checks/adversarial-gen1-3.md`; Part 1 `attempts/T-B1-optional.md` | The three-block projection fails in the recorded finite tests; a dimension count alone is not a structural proof. Fix the pole class and identify the precise leakage functional first. |

All five are completion/continuation of registered targets: verdict **registered
target variant; no novelty claim**. Other matches include MZ IDEA-054, -058,
-065, -069 and -071, whose norm, certification and cardinal-column warnings are
analogies only; their CC or signed-weight scopes do not establish these targets.

Source coverage is not silently promoted: the Padua 2006 record reports bounded
primary excerpts, with corrected-kernel Theorem 2 and order-bound Theorem 3
(author-preprint pp.8 and 10). The programme baseline's -63, -72 and -86 rows
are coverage-qualified secondary reports. A2 requires a separate full-paper
reading of Kolomoitsev–Lomako before borrowing its method, including Theorem 2.1
and the actual discretisation lemma locator. A5 comparison is restricted to
arXiv 2605.23299 Table 3 / section 3.3, Remark 2 and section 4 as reported in
the source theory; this review performs no fresh fulltext verification.
No third-party PDFs or fulltext extracts were written.

## Reproduction and limitations

Run `python topics/padua-proof-attempts-2-20261101/code/evidence_manifest.py`
after final topic edits. This uses only Python's standard library and read-only
Git commands; it runs no mathematical computation and requires no independent
numerical rerun. Output files are SHA-256/size identified. The manifest excludes
itself to avoid recursive self-hashing, and excludes interpreter caches. It must
be regenerated after subsequent topic-file changes. It is provenance evidence,
not an audit or a mathematical checker.

## Current rules and final programme provenance — 2026-11-01

Main e24b21fe43cdd090f6dfac269147e75185f04c5b changed AGENTS/WORKFLOW handoff and allocation rules. Read all3 rules and HANDOFF before merging; scientific statements/computed inputs unchanged. Adopt numbered handoffs; no range under AC local-ID scope. Final programme PR6 head b46b4dea18ce2c933489a211b0b6819dfd32ca70 adds final-ID aliases, without changing depended-on proof bodies or OPEN_TARGETS. Initial scientific pins remain; manifest now includes both versions and current rule/template/registry provenance. Branch deletions after AC merges are handled with immutable SHA pins.

## Literature-index boundary refresh

Main cf89b140530d5838bdb208a8c28f3e7aa676ace3 changed required INDEX/CORPUS only in MZ source comparisons. Full index/corpus diff read: no Padua source/rule/computation change. Prior impact recorded in LOG before merge; source pins retain all original inputs plus this two-file update. No arithmetic rerun is required by these unrelated source-coverage edits.

## Part1 administrative synchronization

Part1 advanced93da3be26dbddf9ec2446af578fe8015bb4eeada. Six administrative paths changed; no theory/code/scientific output/audit/response changed versus7b8884a (direct Git comparison). Its same-main import matches current rules/state/INDEX. Read relevant full diffs/receipts/handoff and logged impact before clean merge. Preserve scientific initial/audit/response provenance; separately pin the six sync administrative inputs. No arithmetic rerun follows from these unchanged scientific dependencies.

## Merged Part1 accepted source updates

AC merged PR9 at main806cc7b4509fd93bae652f9545d32d95529f8281 (final source head752ba068589683afe644b505d673f8da1529cbf0). Full relevant source/metadata diff and mechanical integration review read. Only final-ID/provenance/Open-items metadata changes in the3Part1theorems; Statement-through-Scope/code/output/audit bytes unchanged. Programme source04/06 and OPEN_TARGETS now incorporate the accepted split local results, while A2/A4/highercount obligations stay unchanged. New provenance includes changed Part1/source/registry blobs. Imported IDs101–105 belong to Part1; Part2 has no range.
