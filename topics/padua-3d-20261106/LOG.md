# Padua-type points in three dimensions: log

- Branch: `codex/padua-3d-20261106` · Base: main `76ba421` · Developer: Codex · Auditor: Claude (Opus 5.5 xhigh)
- Stage: WORK · Next: `Codex (gpt-6-astra high): Continue codex/padua-3d-20261106.` · Open handoff: [handoffs/01-work.md](handoffs/01-work.md)
- Reserved final-ID ranges: none. Reserve when first needed (PR #29 rules).
- Claims: none yet.

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
