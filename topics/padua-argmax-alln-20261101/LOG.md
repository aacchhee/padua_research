# All-degree Padua argmax (A4 / PD-T099): strategy topic

- Branch: `claude/padua-argmax-alln-20261101` · Base: main `2b52b43` (merged in `280fea4`; initially `28aaa20`) · Developer: Claude (planning, MEASURED records); Codex (part 3 development, from handoff 02) · Auditor: Codex for Claude's records, Claude for Codex's
- Stage: WORK · Active: [handoff04](handoffs/04-gated-development.md), AC-authorized sequential gated development; previous audit remains PENDING.
- Permanent reserved ranges (no final IDs assigned): PD-T206–225, PD-N078–083, IDEA-316–335, LIT-460–465; first published405febab, [draft PR17](https://github.com/aacchhee/padua_research/pull/17), [ledger](ALLOCATIONS.md).
- Claims:
  - PD-T?argmax-alln-claude-01 — float64 majorant/gap observations — MEASURED — [theory](theory/argmax-alln-claude-01-measured-observations.md).
  - PD-T?argmax-alln-claude-02 — float64 edge/strip gap profiles and n = 2 scans — MEASURED — [theory](theory/argmax-alln-claude-02-measured-edge-profile.md).
  - IDEA?argmax-alln-claude-01 — REJECTED: failed (MEASURED), retained as a sub-tool.
  - IDEA?argmax-alln-claude-02 and -05 — active in part 3; -03 and -04 deferred. See [ideas.md](ideas.md).
- For the PR: register the IDEA and PD-T rows, `results/padua-argmax-alln-20261101.md` → `RESULTS.md` section, Codex audit.
- Open for AC: none.
- Current part3 claims: PROVED codex-02/03/04/05/07/08 and scoped codex-N01; MEASURED codex-01/06. See [report.md](report.md) for exact scopes and provisional prefixes. Required Claude audit PENDING.

## 2026-11-01 — Claude, claude-opus-5-5 (configured; effort not exposed)

- Role: orchestrator and developer. Rules read at `28aaa20861d08074b77efc74eaef75cdcb36234d`: AGENTS.md, agents/WORKFLOW.md (including the repository-only results rule from PR #16), agents/claude/CLAUDE_ROLES.md.
- Trigger: AC asked for ideas toward an all-n proof of the A4 argmax ("any ideas how to create complete proof for all n in pr12?"), then "write this down on a new branch, then we'll update it after part2 is done".
- Pinned inputs:
  - main `28aaa20`;
  - part 2 `codex/padua-proof-attempts-2-20261101` at `b5bba7cf1328b1f207aea001a439c3fe4af0146f` (read only; LOG claims lines and theory list; records 70–73 by title and LOG summary only);
  - programme-ideas OPEN_TARGETS A4 (on main).
- Changes and evidence:
  - [plan.md](plan.md) (strategy), [gate.md](gate.md) (novelty gate), [ideas.md](ideas.md) (four candidates), and the MEASURED [observations record](theory/argmax-alln-claude-01-measured-observations.md).
  - Code: code/maj.py, check.py, cell.py, interior.py. Outputs: outputs/*.out and environment.txt. The scripts were first run in chat exploration, then rerun on this branch to produce the committed outputs.
- Novelty gate: [gate.md](gate.md). The closest entry is IDEA-206 (owner of PD-T099). Verdicts: variants or new within the documented search. No literature claim.
- Kill criteria: written in [ideas.md](ideas.md) and plan §5 before any test, except IDEA-01, whose test (cell.py) ran in chat before this file existed. Its kill criterion ("max S > S(coset) at any n ≥ 3") is recorded retrospectively and the output is unchanged.
- Subagents: none.

## 2026-11-01 (evening) — Claude, claude-opus-5-5 (configured; effort not exposed) — handoff 01

- AC: "now everything is merged. Update claude/padua-argmax-alln-20261101." PR #12 merged as `2b52b43`; PR #15 merged as `67bd07c`. Fetched main `2b52b43`. Rules unchanged since `28aaa20` (empty diff over AGENTS.md, agents/, templates/), re-read in the changed-file sense.
- Merged main into this branch as `280fea4` (no conflict).
- Read:
  - part 2's final A4(a) records PD-T185–192 (theory 70–77; statements in full for 74–77);
  - attempts/T-A4a.md (final done boundary and route notes (b)/(c));
  - the report A4 section;
  - PROOF_STATUS rows PD-T156–197 and PD-T099/100;
  - the IDEAS PR12 addenda;
  - the Claude audit-01 summary of part 2 (accepted, minor F1–F8).
- New measurements: code/edgeprofile.py, strips.py and n2_edges.py, with outputs/edgeprofile.out, strips.out, maj_n2.out and n2_edges.out → [PD-T?argmax-alln-claude-02](theory/argmax-alln-claude-02-measured-edge-profile.md) (MEASURED).
  - An initial "n = 2 near-tie" reading of the 161-grid was corrected before commit: those grid points neighbour a maximal corner, and a 4001-point edge scan shows no competitor.
- Plan revised to v2 ([plan.md](plan.md)); v1 is preserved verbatim under History. The main change: part 2 already proves the S − Δ mechanism on the central vertical edge (PD-T189–192). The remaining obligations P0–P6 and the pre-registered tests T1–T5 are in plan v2 §4 and §6.
- ideas.md and gate.md amended (append-only). New IDEA?argmax-alln-claude-05 (global-max-only finite certifier).
- Handoff 01 closed. Handoff 02 opened: part 3 development by Codex on this branch.

## 2026-11-01 — Codex part 3 setup checkpoint

- Role: orchestrator/developer; actual model gpt-6.1-sol xhigh, as AC requested. Mathematical and setup work in this turn retains that configured effort; bounded replay uses gpt-6.1-sol medium. Rules read at `328be35e55143013047ec03a70e9906e82b95353`.
- GitHub connector confirmed main `2b52b432fe59c9a50aef9deebe5152c5d6874465` already belongs to this head; no merge is needed. Original `/workspace/padua_research` checkout stays intact. Selected source files were fetched into a separate snapshot; [input-snapshot.json](input-snapshot.json) records every pinned path/blob.
- Snapshot materialization initially added a trailing newline. Before freezing evidence, every fetched file was restored to its exact pinned Git blob; the replay worker then reran all six scripts. All six stdout files are byte-identical to Claude's outputs. [Independent record](independent-checks-claude-records.md) documents scope and versions.
- Parallel roles: replay (Sol medium), pre-registered T1–T5 numerical tests (Sol xhigh), finite certifier/P0 (Sol xhigh), and compact-edge proof preparation (Sol xhigh). All have disjoint topic file ownership and no Git authority. This is explicitly requested in handoff 02.
- Novelty gate: existing candidates are being tested under their pre-registered criteria; no new mechanism or priority claim is introduced by setup/replay. Complete state/IDEAS headings/aliases and obstruction/disposition tables scanned; full shortlist IDEA-206/290–305 and linked part-2 material available to the relevant workers. literature/INDEX read for attribution context; no transferred unread literature theorem is used.
- Fresh-range transition adopted. [ALLOCATIONS.md](ALLOCATIONS.md) permanently reserves PD-T206–225, PD-N078–083, IDEA-316–335, LIT-460–465; no final IDs assigned. All 15 returned PRs are merged, none open or closed-unmerged. Main ledger and all four registries checked; [scan](allocation-scan.json). The local ledger respects handoff 02's topic-only write scope; proposed shared links wait for PR preparation.
- Stage remains WORK; handoff 02 remains open while its step runs. Tests/proofs and any finite-range extension will be recorded in a subsequent checkpoint, without upgrading the all-degree target.

## 2026-11-01 — Codex part3 output boundary

- Rules/source pin remains `328be35e55143013047ec03a70e9906e82b95353`; main `2b52b432fe59c9a50aef9deebe5152c5d6874465` was already integrated. GitHub connector used for every remote read, commit/ref update and draft PR17.
- Completed T1–T5 with original criteria preserved and separate dated interpretations. T1 noncorner profile retained at selected degrees through400; its requested general-beta series remains unfulfilled. T2 and T3 raw profile forms fail their numerical planning tests. T4 literal existing-bound projection is about1.33e14 using inferred constants, not a rigorous threshold. [Tests](attempts/T1-T5.md).
- P0 exact rational proof and Bernstein correctness developed. Exact-field n8 certificate plus general rational-trigonometric n9–16 certificates complete; every new degree independently replayed. With inherited n3–7 the finite range is2–16. No degree>=17 run. [Finite attempt](attempts/P0-finite.md), theory02/03/07/08.
- P1 compact positive-gap vertical envelope proved; horizontal supporting decomposition/defect theorem proved separately. P2 envelope and P3–P6 remain OPEN. The whole-square all-degree PD-T099 remains OPEN. [Edge attempt](attempts/P1-P2-edges.md), theory04/05.
- After the T4 literal-architecture kill, tested precise pairing variants. Exact n4 O-Lt finite ordering is refuted (scoped PD-N?argmax-alln-codex-01); measured O-R/E-C screens retained separately in06. One displayed rational rounding unit was corrected and independently rechecked. Original ambiguous IDEA03 and other pairings are not refuted. [Fallback](attempts/P3-P5-and-pairing.md).
- Sequence disclosure: P1/P2 and n8 discovery began after the decisive first-pass tests/T5 were available while the final high-degree T1 extension still ran; the complete T1 range was then recorded. No kill criterion was retroactively changed. No unread one-dimensional literature theorem was transferred into P3.
- Supplementary checks: distinct Astra high worker reviewed and reran finite2,8–16, mutation controls, fullT2–T4 and T1n12; reviewed edge04/05. A separate Astra high worker verified pairing O-Lt with an independent rational reconstruction. [Part3 checks](independent-checks-part3.md), [pairing checks](independent-checks-pairing.md). These do not replace Claude's required topic audit.
- A separate followup Astra high review of the original Claude measured records accepts the six-script-covered claims with minor C-01: cumulative-strip wording corrected to separate one-cell-thick offset bands. Old wording is preserved in record02 History. All six targeted central optimizer locations stayed in the stated box; standalone whole-square maj.py scans remain unrerun. [Original-observations audit](independent-checks-claude-observations-audit.md).
- Actual models: Sol xhigh development/orchestration under AC's explicit request; Sol medium replay; Astra high supplementary mathematical checks. Runtime metadata was not independently exposed to subagents; requested/configured settings are recorded.
- Connector commit identity is Andrey Chesnokov with the account noreply email, rather than the handoff's requested gmail email: the connector exposes no author-email selector. Published history is preserved; no force-push or main mutation.
- [report.md](report.md), [results](../../results/padua-argmax-alln-20261101.md), [evidence-manifest.json](evidence-manifest.json) and [literal shared proposals](proposed-record-changes.md) record the boundary. No final IDs assigned or shared registry changed. Stage AUDIT; [handoff03](handoffs/03-audit.md) is published in the following status-only/handoff commit after the scientific output SHA is known.

## Runs needed (updated during part 3)

## AC-authorized gated continuation

AC authorizes at most7 rounds each in direction1 (defect domination), then2 (uniform physical-coordinate corners), then3 (centreward edge comparison/horizontal primitive), continuing only on explicit positive gates. [Protocol](gated/PROTOCOL.md) registers the round/stop rules and direction1 round1 before execution. Rules reread at7d308b10d946b607ae0690454f6c0103690775a4; main remains2b52b432fe59c9a50aef9deebe5152c5d6874465. Role Codex orchestrator/developer, configured/requested Sol xhigh; exact-runtime metadata not independently exposed. Handoff03 is redirected to04, not approved or completed. Existing theory and audit records remain intact.

### Gated direction1, round1 checkpoint

- Sol xhigh mathematical worker wrote global/local two-phase primitive bounds, including a new square-root numerator-sign-change estimate and finite-sum collision control. Root wrote the pairwise projected-defect theorem, uniform in the unused macroscopic coordinate. Neither proof uses numerical agreement as a premise.
- A distinct Sol xhigh worker executed the predeclared n16/32/64/128/256 phase and defect screen; all finite kill flags false. Astra xhigh independently reconstructed the analytic estimates and exactly replayed20,997 numeric and1,062 other raw JSON leaves (timing/argv and documented note-completion hash excluded). [Independent check](gated/checks/d1-r01.md).
- GO to round2 is based on these new analytic lemmas, not only the screen. [Round2 contract](gated/d1/r02-contract.md) requests a compact-complement assembly and a quantitative diagnosis. No direction2/3 development has started.
- The860,021-byte full numerical payload is committed losslessly as81,843-byte gzip; see [packaging](gated/PACKAGING.md). Working uncompressed output was moved to/tmp after replay. No historical evidence is deleted or overwritten. Prior main evidence manifest remains the frozen previous-step record until final campaign integration refresh; WORK checkpoints are not claims that the previous manifest includes new campaign files.

### Gated rounds2–3 checkpoint

- Round2 proves a uniform positive gap outside fixed corner neighborhoods and an explicit finite projected-defect rectangle. The latter removes the need for a defect-convergence modulus in that comparison. The exact primitive endpoint cusp has its own durable06, and the purely quadratic/coset-maximality obstruction its scoped PD-N home. Independent Astra review accepted all stated scopes and closed the linear-plus-rho^(3/2) wording correction.
- Round3 derives and independently checks explicit local constants242000/2048/640 on radius1/64. They yield only an unusable local scale exp(10^7), without global phase-entry constants. STOP applies to that coarse quantitative implementation. A distinct adaptive finite geometry candidate justifies GO to round4, pre-registered before execution. [Round ledger](gated/ROUND_LEDGER.md).
- New files remain topic-only; no new final IDs or shared registry mutations. Directions2 and3 have not started.

### Gated rounds4–5 checkpoint

- Both finite geometry rounds independently pass. Adaptive positive rectangles give projected defect≥1/1536 outside4π/n corner boxes. Sparse parity-correct middle mesh lines handle the first1–4 endpoint cells and give Δ≥1/4096 near every odd coset except an actual non-node corner.
- The resulting qualitative theorem confines all global maximizers to actual non-node corner phases with uniformly vanishing scaled distance. This does not prove exact corner equality or an effective threshold; the global phase-entry/effectivity frontier remains OPEN.
- GO to one bounded exact primitive row-resummation repair in round6, with a registered STOP if no sharper uniform bound emerges. No direction2/3 work has started. [Round ledger](gated/ROUND_LEDGER.md).

- Six prescribed independent replays: COMPLETE at the setup checkpoint; see independent-checks-claude-records.md. Standalone maj.py whole-square scans remain outside that replay's coverage.
- Claude Opus5.5 xhigh topic audit under handoff03; complete state/IDEAS read required because the branch carries mechanisms and scoped negative content.
- General-beta series, center-minimality, P2 primitive estimates, P3–P5 and a rigorous effective threshold remain unresolved. Further development follows audit/disposition; no additional finite discovery is implicitly claimed.
