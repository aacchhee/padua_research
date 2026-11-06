# Padua-type points in three dimensions: log

- Branch: `codex/padua-3d-20261106` · Base: main `76ba421` · Developer: Codex · Auditor: Claude (Opus 5.5 xhigh)
- Stage: WORK · Next: `Codex (gpt-6-astra, high): Continue codex/padua-3d-20261106.` · Open handoff at publication: [handoffs/04-work.md](handoffs/04-work.md)
- Reserved final-ID ranges: none. Reserve when first needed (PR #29 rules).
- Claims: provisional records in [report.md](report.md); no final IDs allocated.

## 2026-11-06 — Claude, claude-opus-5-5 (configured; effort not exposed) — topic setup

- AC asked what is known about 3-D Padua. Claude summarized it and noted that earlier campaign-scoping documents had marked "3D Padua" out of scope (IDEA-120, IDEA-013).
- AC: "I do not remember ruling this out of scope, I guess it applied to one specific fact. Make a proper adventurous reasoning topic on 3D, write what you know and what you expect. Allow Astra Ultra when necessary, 25 rounds, otherwise usual rules".
- **3-D Padua is in scope for this topic by AC's instruction.**
- Claude wrote [BRIEF.md](BRIEF.md) and handoff 01:
  - BRIEF: the knowledge base, how the 2-D mechanism breaks in 3-D, the repository's 3-D results, expectations E1–E6 and a literature list.
  - Handoff: T1 obstruction theory, T2 aliasing-designed positive constructions, T3 proofs, T4 a proved Radon-stack baseline, T5 cubature non-existence and joint spectra (bounded), T6 Lebesgue lower bounds (bounded); gates D0–D4.
- Budget: 25 rounds per direction (Claude's reading of "25 rounds"; AC may correct it), with T5/T6 capped at 8.
- Models: Astra ultra allowed when necessary; coordinator Astra high; Sol for easier jobs.
- Rules read at `76ba421`. Branch created from main `76ba421`. No computation was run and no claim made.

## Runs needed

- D0–D4 and T1–T6 as in handoff 01.

## 2026-11-06 — Codex, gpt-6-astra high — continuation initialization

- Role: orchestrator/developer, AC's explicit model selection retained.
- Rules read in full at input head `ccd9e905d19c0c625c196c4a3f3e707058ed042a`:
  AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md.
- Fetched main `76ba4214b100c86a44941f5e9a662ce9ce48efb8` and requested topic
  head. Main is an ancestor; no reconciliation commit is necessary.
- Read BRIEF and open handoff 01. Its explicit parallel-worker instruction
  authorizes delegation. Coordinator scope is [plan.md](plan.md), written
  before research execution; [round ledger](rounds.md), [gates](gates.md).
- D0 reproduction adds no novel content. New mechanisms remain gated on D0
  and the full repository predecessor scan. No final ranges needed yet.

## 2026-11-06 — replay round 1 and research launch

- Bounded replay developer: Codex, assigned gpt-6.1-sol medium; resolved runtime
  metadata is not independently exposed. [D0/D1 both PASS](replay-notes.md).
  Exact counts, normalized symbolic determinant, modular rank controls and
  all four 2-D corner identities reproduced. Two PD-N037 fibre/baseline rows
  match all six historical binary floating values exactly. Compact receipt
  records input hashes, versions and commands; historical artifacts were
  recovered read-only from a pinned pushed Git commit.
- After clearance, launched T1–T6 with disjoint files as requested. T2 code
  developer uses assigned gpt-6.1-sol medium; T1/T3/T4/T5/T6 mathematical
  developers use assigned gpt-6.1-sol xhigh. The coordinator retains Astra high.
  Workers do not control Git or shared records. A supplementary distinct-agent
  reconstruction and Claude's substantive audit remain separate obligations.
- Opened draft [PR #33](https://github.com/aacchhee/padua_research/pull/33),
  audit PENDING, with no IDs reserved and no shared-registry edits.

## 2026-11-06 — first mathematical checkpoint

Coordinator Codex, assigned gpt-6-astra high; mathematical workers assigned
gpt-6.1-sol xhigh, T2 screen worker gpt-6.1-sol medium. Runtime model metadata
is not independently exposed. No Astra-ultra escalation has been needed.

- T1 round 1: elementary binary-code classification and a hand proof excluding
  a **single coordinate-reflection-invariant whole coset** at minimal node
  count for every n>=2. [Classification](theory/t1-reflection-classification.md),
  [scoped obstruction](theory/t1-minimal-obstruction.md). Developer PROVED;
  D3 enumeration and supplementary independent review still in progress.
  The original unrestricted C_k target remains OPEN.
- T2 round 1: three frozen cyclic formulas fail at n=2 by explicit quadratic
  annihilators, [scoped proof](theory/t2-cyclic-screen.md). Round 2: complete
  normalized generator census at n=2,3,4 finds 4,0,4 full-rank cases; all
  eight finite survivors lose to same-degree controls on the frozen mesh.
  [Attempt](attempts/T2.md). Exact computations remain conservatively MEASURED
  until a separate replay of the committed cover; no D2-promising family.
- T3 round 1: [exact cyclic rank reduction](theory/t3-cyclic-rank.md) and
  [short-relation annihilators](theory/t3-short-relations.md), developer PROVED
  analytic prerequisites. [Whole order-39 exclusion](theory/t3-degree3-extension.md)
  is CONDITIONAL on the separately checked H39 finite cover. Survivor-dependent
  T3 remains blocked on D2, not PARTIAL.
- T4 round 1: all-n stack unisolvence, exact determinant height factor, and
  a [monotone-order exponential lower bound](theory/t4-monotone-lower.md),
  developer PROVED. This contradicts the polynomial expectation only for
  the specified monotone ordering. Other orderings and actual numerical
  diagnostics remain in progress.
- T5 round 1: D4 passed by exact known degree-five cubature controls before
  any nonexistence claim; [code](code/t5_exact.py), [receipt](evidence/t5-exact.json).
  The fixed-grid sharp support theorem is being written separately.
- T6: explicit universal logarithmic-cubed lower-bound proof is being written;
  not included as a completed result in this checkpoint.
- This is an honestly unfinished development checkpoint. Claude audit is
  PENDING; no shared scientific registry, final allocation or readiness change.

## 2026-11-06 — completed development and supplementary checks

Coordinator Codex, assigned gpt-6-astra high. T1/T3/T4/T5/T6 developers
were assigned gpt-6.1-sol xhigh, T2/replay gpt-6.1-sol medium; actual runtime
metadata is unexposed. No ultra escalation was used. Direction rounds and
their bounded stops are finalized in [rounds](rounds.md).

- T1: D3 passed for 20,304 canonical 3-D cosets and 450 2-D cases.
  The classification and all-n>=2 obstruction are hand-proved. All-degree
  Padua admission is explicit, with finite sanity through n10. The original
  unrestricted class and arbitrary-weight cubature questions stay OPEN.
- T4: added an explicit Newton recursive upper majorant and an
  exp(O(n log n)) upper bound for exact-greedy heights. All three registered
  numerical orders triggered D2 KILL at n7 after consecutive n6/n7 Leja
  losses. No n8..20 screen or asymptotic fit was run after that stop.
- T5: D4 passed before obstruction testing. The fixed Gaussian-grid
  degree-five support theorem is hand-proved (21 positive / 15 signed),
  and the known all-q commutator-rank formulas are reconstructed locally.
  Nonlinear completion minimization was explicitly not executed; that
  distinct route and universal cubature remain OPEN/deferred.
- T6: universal comparison and explicit Fourier bound are hand-proved;
  the primary-source trail identified Subbotin1983's already-known general
  comparison and logarithmic order. [Actual source coverage](literature-T6.md).
  No historical novelty is claimed for these facts.
- A distinct Astra high supplementary mathematical checker reconstructed
  T1/T6 and actually reran their scripts in an isolated pinned checkout;
  it also enumerated tiny subgroups/translations independently. No
  BLOCKING/MAJOR finding; its MINOR T1 scope wording fix was made and
  reviewed. [Canonical check](independent-checks-math.md).
- A second distinct Astra high supplementary checker reconstructed T3/T4/T5
  and actually reran the replay, cyclic census/quality/cover, stack and
  cubature code in another pinned checkout. It separately reconstructed
  H39's 171 Laurent witnesses. [Canonical check](independent-checks-computation.md).
  Its exact finite-cover execution discharged H39: only the normalized
  cubic obstruction and full unshifted M39 extension were upgraded from
  MEASURED/CONDITIONAL to PROVED. Statements/scopes, rank distributions,
  quality observations and infinite-degree targets were not upgraded.
- Reading-coverage caveat: the canonical T2 disclosure is in
  [its attempt](attempts/T2.md); the substantive auditor must disposition it.
  Remaining source-comparison and novelty limits stay in their own records.
- Code/data identities are in [evidence manifest](evidence-manifest.json).
  Optional raw catalogues remain regenerable local working output;
  [storage boundary](COLD_STORAGE.md). Essential finite witnesses/code
  and small receipts are committed; no archival delivery is claimed.
- Final report and [topic results](../../results/padua-3d-20261106.md) are
  synchronized. No final ranges needed: **no range**. No shared registries,
  main, tags, workflows or repository settings were changed.
- Stage AUDIT: draft PR33 preserves the work. Required Claude Opus5.5 xhigh
  substantive audit is PENDING and is not replaced by either Astra check.
  [Handoff 01](handoffs/01-work.md) closes in the following handoff commit;
  [handoff 02](handoffs/02-audit.md) carries the exact audit scope/source pin.
  No readiness or merge decision is requested from AC at this boundary.
- Integration verification actually passed: code/data manifest (31 artifacts,
  177,823 bytes), eight producer-code/receipt identities, all topic JSON,
  every topic file below 16KiB, Markdown links (except the successor handoff
  until its following commit), and `git diff --check`. Final successor-link
  verification follows handoff publication. The manifest verifier command is
  `python topics/padua-3d-20261106/code/artifact_manifest.py --verify`.

## 2026-11-06 — Claude, claude-opus-5-5 xhigh — substantive audit 01

- Role: independent auditor of Codex development (handoff 02). Rules read at
  `d0e1bbb267db9928de97538d9b524fb0068538cd`; audited candidate
  `f1a5b0936d8fb2b033c69af59a6366550f170999`; main `76ba421` unchanged.
- [Audit 01](audit-01.md), with five Opus 5.5 xhigh subagent scope reports in
  [audit-01/](audit-01/), audit code in [audit-01/code/](audit-01/code/) and
  orchestrator receipts in [audit-01/receipts.txt](audit-01/receipts.txt).
  Full `state/IDEAS.md` read performed.
- Actually executed: manifest verify PASS before reruns; all 11 handoff-02
  producer commands in a detached `f1a5b09` worktree, every scientific field
  identical to the committed receipts (Python 3.13.18 vs 3.12.14 recorded);
  an independent third-method exact H39 checker over the 171 witnesses and all
  59,319 residue triples mod 39; T1 brute force/full-cap enumeration; T4/T5/T6
  reconstructions. Details in the audit.
- Outcome: no BLOCKING. All claimed PROVED/MEASURED/OPEN statuses accepted,
  including the two H39 PROVED upgrades. Five MAJOR record/gate findings
  (missed predecessors; candidate retention and handoff-01 item dispositions,
  including the unexecuted T5 commuting-completion probe; the T2 gate-coverage
  deviation, dispositioned as a disclosed uncurable timing deviation for AC;
  the D3(b) capped-enumeration verdict; the PD-N kind of short relations),
  15 MINOR and NOTEs. Stage returns to **WORK** for a Codex response; only
  material changes get a focused re-audit.
- No IDs reserved or allocated; no shared registry, main, tags or `.github/`
  changed. Draft PR #33 AUDIT section updated after push.
- [Handoff 02](handoffs/02-audit.md) done in `64292b5`; [handoff 03](handoffs/03-response.md) opened for the Codex development response.

## 2026-11-06 — AC redirection: new directions T7/T8/T9 (recorded by Claude, claude-opus-5-5 xhigh)

- AC: "Write a handoff for what you know about Cosets without reflection symmetry and Untested variants of cyclic orbit, and set the branch to work so that codex uses same restarted budget on those directions".
- AC: "Add also what you know on Closing the gap between log³ n and everything observed."
- New directions: T7 cosets without whole-coset reflection symmetry; T8 untested cyclic-orbit variants; T9 the log³ n gap. Budget 25 rounds each, restarted from zero, with the handoff-01 rules. Claude reads "same restarted budget" as 25 for T9 too (not T6's 8); AC may correct this.
- Stage stays **WORK**. [Handoff 03](handoffs/03-response.md) is superseded by [handoff 04](handoffs/04-work.md), which carries the audit-01 response unchanged as Part A and adds T7–T9 as Part B.
- Handoff 04 marks Claude's sketches as hypotheses, not results: the general-H short-relation lemma, the fold bound |X| ≥ |H|/8, and the octahedral lattice-packing obstruction to single-coset Padua-type cubature for n ≥ 110. Claude's two unrecorded exact checks of the 10-point example (unisolvence; a degree-2 equal-weight rule exists, no degree-3 rule) must be reproduced by the developer.
