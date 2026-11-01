# All-degree Padua argmax (A4 / PD-T099): strategy topic

- Branch: `claude/padua-argmax-alln-20261101` · Base: main `2b52b43` (merged in `280fea4`; initially `28aaa20`) · Developer: Claude (planning, MEASURED records); Codex (part 3 development, from handoff 02) · Auditor: Codex for Claude's records, Claude for Codex's
- Stage: WORK · Next: `Codex (gpt-6.1-sol xhigh): Continue claude/padua-argmax-alln-20261101.` · Open handoff: [handoffs/02-part3-work.md](handoffs/02-part3-work.md)
- Reserved final-ID ranges: none yet. No PR is open; reserve by the WORKFLOW fresh-range procedure when the draft PR opens.
- Claims:
  - PD-T?argmax-alln-claude-01 — float64 majorant/gap observations — MEASURED — [theory](theory/argmax-alln-claude-01-measured-observations.md).
  - PD-T?argmax-alln-claude-02 — float64 edge/strip gap profiles and n = 2 scans — MEASURED — [theory](theory/argmax-alln-claude-02-measured-edge-profile.md).
  - IDEA?argmax-alln-claude-01 — REJECTED: failed (MEASURED), retained as a sub-tool.
  - IDEA?argmax-alln-claude-02 and -05 — active in part 3; -03 and -04 deferred. See [ideas.md](ideas.md).
- For the PR: register the IDEA and PD-T rows, `results/padua-argmax-alln-20261101.md` → `RESULTS.md` section, Codex audit.
- Open for AC: none.

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

## Runs needed

- Independent rerun of `code/check.py`, `cell.py`, `interior.py`, `edgeprofile.py`, `strips.py` and `n2_edges.py` (commands in the two observations records), by an agent other than Claude, before any result here is used as evidence in a PR. Assigned to Codex as step 0 of handoff 02.
- Plan v2 §6 tests T1–T5: not run. Assigned to handoff 02.
