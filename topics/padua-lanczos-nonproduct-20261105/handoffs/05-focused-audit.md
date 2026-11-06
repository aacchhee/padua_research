# Handoff05 — focused A3 re-audit and preparation inputs

- Status: open
- Previous handoff: [04-response.md](04-response.md)
- Next agent / model / effort: Claude, Opus 5.5 high
- Role: focused auditor and topic orchestrator
- Branch: codex/padua-lanczos-nonproduct-20261105
- Input head SHA: `84f3d50ae265a0bc510cb6bb232fbc23f71f1b40`
- Main/base: `be9a8318150204711d5446d2ea26284cf1ed0819`
- Stage: AUDIT (material A3 statement correction only)
- Written by/date: Codex, requested gpt-6-astra high, 2026-11-06

## Read first

Read AGENTS.md, WORKFLOW and Claude role at the current head; then
[audit01](../audit-01.md), [response01](../response-01.md), LOG's canonical
AC decisions and handoff04. No existing audit report was edited.

The substantive independent audit is complete and accepted every proof at
its stated scope. This is the required focused re-audit of a material
statement correction, not a second substantive campaign audit.

## Exact material diff

Review only this material mathematical correction:

```sh
git diff 1f809519b353512a447661b35df9e92ad0ec6e06 3b0a990dda7a630cf4ea904639c01dad717c2ea9 -- topics/padua-lanczos-nonproduct-20261105/theory/p1-continuous-creator-probe.md topics/padua-lanczos-nonproduct-20261105/ideas/P1.md
```

A3 qualifies the degree-eight `g_j=1/binom(2j,j)` finite source chain and
all uses as **under BJ**, retaining MEASURED status. Check the exact code
`code/p1_moment_probe.py:153–161`, which uses only `records["BJ"]`, and the
frozen evidence if needed. No mirror/alternating values, new computation or
proof were added. The response-output commit separately replaces one stale
P1 rerun-status table entry with the completed audit link; that is mechanical.
Choose any targeted verification independently, record executed commands,
and preserve the original evidence. No new high scan is required.

No new novelty claim or mechanism is introduced; a full catalogue reread is
not necessary for this narrowly bounded correction if you explicitly state
that exception and its reason. Read the relevant existing P1 record and
prior accepted audit rather than reopening unrelated proofs.

## Mechanical response and decided matters

Review the response's mechanical dispositions by diff, primarily
`3b0a990..04ba07b` and `04ba07b..84f3d50`. MINOR16 was fixed by weakening
wording to D4-invariant/not rotation-invariant; no symmetry proof was added.
The P5 checker change is comments only and has identical executable AST.
Receipts, inventories, audit01 and audit01-check code are byte-unchanged.

AC Q1–Q3 are decided in LOG: the gate-timing deviation with the A2 qualifier
is accepted, P3 is accepted as the formal goal's weaker variant, and the
P3/P5 proof-without-screen deviation is accepted. Do not re-ask these.
A2's exact proposal time, per-entry unread list and independently pinned
original formula/range identity are not preserved; the response explicitly
records those historical precision limits instead of inventing them. Confirm
that the record does not claim they were verified. These limitations do not
reopen the accepted Q1 decision or the mathematics.

Retain P3's required title/scope: **non-affine-product measures
moment-equivalent to SH_n through degree 2n+1, with an n-dependent weight
mode**. Gram matrices, monic basis, creators, pivots, source scales and
frozen response are eta-independent; only the ambient normal projector
changes. The n-independent perturbation target is OPEN/deferred to a
follow-up, not a precondition for this PR. Optional Padua2–16/four-rule
scans are listed under Runs needed only. No P3 scan is required.

Do not reopen accepted P3/P4/P5 proofs, P1/P2 admissions, reflection method,
P6 outcomes or the three INCONCLUSIVE screens. NOTEs need no action.

## Readiness inputs for subsequent preparation

No final ID or reservation exists; no shared registry was edited. PR30 stays
draft. After focused acceptance, hand Codex preparation the following:

- reserve fresh ranges under the current-main/all-open-PR/retired-reservation
  procedure before assigning IDs; record every checked head;
- apply accepted claims, candidates and literature to shared registries by
  reviewed diff, preserving all provisional-to-final mappings;
- disambiguate namespaces in the crosswalk, notably PD-T/IDEA/PD-N P4-01,
  PD-T/IDEA P4-04, P2-03/P2-04, and the existing lowercase P5 theory labels;
- retain the successful P3 weaker variant and deferred fixed-perturbation
  IDEA separately, with no new proof status for that deferred target;
- include the covariance PD-N and finite P1/P2/P6 measured records at their
  exact scopes; no support lemma upgrades an OPEN rate target;
- the single readiness check reviews the applied registry diff and refreshes
  reservations; it is not another substantive audit absent material changes.

No allocation or registry application is authorized as part of this focused
audit. Storage is AC's separate cleanup topic: no moving/deleting/compacting
while the repository stays below10MB. External archival delivery remains
pending, and the old inventory is a historical observation, not a current
archive guarantee. Only AC merges; no force-push, tags, rule/.github changes.

## Outputs and transition

Write `audit-02.md` with focused scope, exact commits, model/effort, actual
checks, findings/dispositions and residual limits. If accepted, stage PR and
hand off preparation to Codex gpt-6-astra high; otherwise return actionable
findings to Codex. Do not re-audit unaffected accepted results.

Commit audit outputs first. Then change only this handoff's status to
`done in <audit-output-sha>` and add handoff06 with its exact input head and
complete next tasks. Update LOG/PR as appropriate, push and end with the
short next-agent continuation prompt. Never overwrite earlier handoff bodies.
