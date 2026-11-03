# Padua Lebesgue-function follow-ups (T1–T4): log

- Branch: `codex/padua-lebesgue-followups-20261103` · Base: main `440d107` · Developer: Codex · Auditor: Claude (Opus 5.5)
- Stage: WORK · Next: `Codex (gpt-6.1-sol xhigh): Continue codex/padua-lebesgue-followups-20261103.` · Open handoff: [handoffs/01-work.md](handoffs/01-work.md)
- Reserved final-ID ranges: PD-T266–285, PD-N092–099, IDEA356–375, LIT474–481; [reservation and pinned union scan](ALLOCATIONS.md). No final assignments during WORK.
- Claims: T2–T4 core theorems PROVED with accepted supplementary independent checks; T1 exact counts OPEN while complete runs continue. Required Claude audit PENDING.
- Open for AC: none at setup. Ask AC before using any machine outside the sandbox.

## 2026-11-03 — Claude, claude-opus-5-5 (configured; effort not exposed) — topic setup

- AC: "Now make one more codex handoff for Small follow-ups: Argmax and Lebesgue paper". The scope is the four follow-ups listed in Claude's frontier assessment of the same day:
  - the n = 8 count;
  - centre-minimality of g_v and g_h;
  - the general-β series;
  - the A3 constant term.
- Literature reading for the paper and the effective all-n bridge are deliberately excluded. The bridge runs on `codex/padua-argmax-effective-20261103`.
- Rules read at `440d107` (unchanged since that morning's read). Branch created from main `440d107`. Only this LOG, handoff 01 and the results stub were added. No computation was run and no claim made.

## Runs needed

- T1–T4 as in handoff 01.

## 2026-11-03 — Codex development resumed

- User requested `Codex (gpt-6.1-sol xhigh): Continue codex/padua-lebesgue-followups-20261103.` Orchestrator/developer configured accordingly; serving metadata is not separately exposed.
- Rules read at initial local `2b52b432fe59c9a50aef9deebe5152c5d6874465`, then current main `440d1079e42c3ef21c40d1cf8870f5b206410c6a`; branch head `3f5196cf3639407c25b021fa30f70cc1d3ae113a` has byte-identical rules to current main. Open handoff 01 and topic log read. Current main is an ancestor; no merge needed.
- Cloud runtime startup completed; initial restricted shell fetch could not reach the proxy. The supported per-command network grant succeeded. No alternate machine or proxy bypass was used.
- Parallel disjoint workers: t1_certification (gpt-6.1-sol medium), t2_t3_defects and t4_constant (gpt-6.1-sol xhigh), allocation_scan (gpt-6.1-sol medium). Independent T1 checker t1_independent uses gpt-6-astra high. Parent alone owns Git/log/results/PR/handoff state.
- [Plan](plan.md) records time ceilings, evidence requirements and acceptance criteria. Workers own target attempt/gate/theory/code files; frozen and shared scientific files remain unchanged.
- Target novelty gates are in the workers' gate files; setup/allocation itself adds no scientific mechanism. No new claim is promoted by this entry.
- Development in progress. Handoff 01 remains open. Required Claude audit remains PENDING.

## 2026-11-03 — T2/T4 checked analytic checkpoint

- First plan/reservation checkpoint `514e3763a827c106c5170eecd55d849b39265da2` pushed; draft [PR20](https://github.com/aacchhee/padua_research/pull/20) opened and attached to this chat. T2 first proof/pre-run gates pushed in `4cfad03`.
- T2 gives exact representations of both inherited limiting defects, strict centreward monotonicity and unique minima: vertical g, horizontal exactly 1. A separate theorem gives the common endpoint expansion with coefficient `8 log(2)/pi^2` and constant `1/3+12 log(2)^2/pi^2`, with explicit errors. These do not establish finite-degree ordering or effective convergence.
- T4 proves the parity-independent signed corner defect limit, an integral/geometrically convergent series, an explicit coarse `604 n^(-1/5)` comparison, the local one-dimensional bound `|L_n-A_n|<=1/(4n^2)`, and the corner constant with an explicit vanishing remainder. The full PD-T098 sharper expansion stays OPEN.
- Distinct gpt-6-astra high reconstruction accepted the T2 and T4 proofs at the hashes in [independent-checks-analytic.md](independent-checks-analytic.md). T4 enclosure code was actually rerun at order64/bits320 and order80/bits384; the rational brackets for kappa and c agree. This supplementary acceptance does not replace Claude audit.
- Primary source LIT-388 was reread in complete extracted fulltext for the bounded numerical-table comparison; see [literature-comparison.md](literature-comparison.md). No author contact or external priority claim.
- T1 remains in progress: fresh producer, repaired boundary persistence/native evaluation, independent frozen-predicate controls and exact memoization equivalence checks. Partial progress is not count certification. T3 series/evaluation remains in development.

## 2026-11-03 — T2–T4 core development complete

- T4 analytic proofs and accepted independent evidence pushed in `34150d0`. T1 frozen execution wrappers and exact-equivalence controls pushed in `f346d99261aa695a55d118f6d543b8fb417c2bb7`; count status remains OPEN.
- T3 now proves general-position vertical/horizontal series with explicit geometric tails. The vertical expansion and selected horizontal chart have ratio at most one half at every fixed interior angle. Exact-Fraction evaluation at five rational squared cosines and coarser outward Decimal Darboux integration agree. Distinct Astra high actually reran both final routes and reviewed all proofs/code; no unresolved analytic finding remains.
- The final analytic [independent report](independent-checks-analytic.md) pins all T2–T4 theory/code hashes and actual outputs. It also repeats T4's two bounded PSLQ searches; their null outcomes are MEASURED only, not a theorem excluding a closed form.
- T2–T4 meet the handoff's core done criteria. The sharper T4 correction and remainder are deferred stretches, while full PD-T098 remains OPEN. T1 continues within its six-hour ceiling. The [report](report.md) and topic results distinguish these scopes.
- Parent identified absent explicit optimized-Python refusal in new T1 wrappers. Current runs use normal `python -B`; executed sources remain frozen. Add/test refusal after active runs, retain exact executed source blobs and a guard-only mapping rather than changing artifact provenance. This hardening item is not a failed mathematical predicate in the active executions.
- T2/T3's final gate discloses later completion of some linked full candidate/attempt reads. Distinct Astra review records this as an acknowledged prospective-gate timing deviation, not retroactively cured by later reading. Mathematical acceptance is scoped separately; clean protocol clearance is not asserted. Carry this qualification into the Claude handoff.
- T1 remaining runtime justified a bounded fifteen-minute `t1_native_loop` technical subtask (configured gpt-6.1-sol medium): compiled exact Python-integer endpoint summation, disjoint new files only, crossvalidated against frozen n4–7 and edge cases. No live source or acceptance predicate may change; independent checking is required before use. Existing jobs continue.

## 2026-11-03 — T1 exact backend and verification checkpoint

- Native exact-integer endpoint sums and optional producer/checker wrappers pushed in `1b7ebd8`. Distinct Astra high rebuilt and checked the backend against frozen historical n4–7 endpoints, actual n8 evaluator/leaf cases, arbitrary-size integer rounding, ownership/refcounts, and malformed/publication failures. The native evaluator preserves ordered per-term rounding; it changes no acceptance predicate. Its modest speed gain does not justify restarting active runs.
- Existing normal-mode producer, boundary and two independent full interior replays remain in flight with their executed source bytes frozen. The archived proposal is a reference input, not mislabeled fresh generation. Fresh generation and full final acceptance are still required.
- New native entry points and the unused join/payload entries explicitly reject optimized Python. The live legacy-wrapper guard hardening remains pending until those processes end; `f346d99261aa695a55d118f6d543b8fb417c2bb7` retains their executed source blobs.
- The main evidence manifest now includes completed technical control/source records as well as analytic evidence. Controls establish only their stated finite equivalence/failure cases, not a complete degree-eight count. No temporary unpublished receipt is treated as an output.
