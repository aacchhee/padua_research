# Effective all-degree Padua argmax (PD-T099): campaign log

- Branch: `codex/padua-argmax-effective-20261103` · Base: main `440d107` · Developer: Codex (gpt-6-astra ultra, at AC's instruction) · Auditor: Claude (Opus 5.5 xhigh)
- Stage: WORK · Next: `Codex (gpt-6-astra ultra): Continue codex/padua-argmax-effective-20261103.` · Open handoff: [handoffs/01-work.md](handoffs/01-work.md)
- Reserved final-ID ranges: none yet. Reserve when the draft PR opens (WORKFLOW fresh-range procedure).
- Claims: PD-T?argmax-effective-claude-01 — pilot gate measurements — MEASURED — [record](theory/argmax-effective-claude-01-pilot-measurements.md).
- For the PR: final IDs, PROOF_STATUS/IDEAS/INDEX rows, a RESULTS.md section, and the Claude audit.
- Open for AC: none at setup. Ask AC before using the NTNU servers.

## 2026-11-03 — Claude, claude-opus-5-5 (configured; effort not exposed) — campaign setup

- AC's requests:
  - "Reassess the frontier at Padua repo …"; then
  - "I want this work to be divided. First, write a handout for codex for Effective all-n argmax. This looks like a topic that warrants astra with ultra reasoning. Write all what you know about the problem, possible routes, and some easy gates. This campaign may be more adventurous."
- Rules read at `440d107`. Since `2b52b43` only agents/WORKFLOW.md changed (PR #18 storage rule: regenerable outputs to cold storage, small committed evidence). AGENTS.md and the role files are unchanged.
- Branch created from main `440d107`. The topic was opened by Claude for Codex development under AC's instruction.
- Read for the brief:
  - PR #17's report.md and gated/REPORT.md;
  - statements of gated-codex-01…05, 07–11, 13–15;
  - attempts/P0-finite.md;
  - PROOF_STATUS rows PD-T099, PD-T181, PD-T206–235 and PD-N078–083;
  - IDEAS rows 316–335;
  - literature INDEX entries LIT-312, 379 and 388.
- Pilot measurements (MEASURED; [record](theory/argmax-effective-claude-01-pilot-measurements.md)):
  - G2: true local corner constant;
  - G3: true global primitive constant and far-coset margin;
  - G0/G1: timings of the existing PD-T210 certifier at n = 17, 20, 24, 32, with the checker run on n = 17.
  - These are scratch runs: the certificates are regenerable and not committed, and no independent replay has been done. Degrees 17+ are therefore **not** certified.
- Written: [BRIEF.md](BRIEF.md) (knowledge base, routes R1–R6, gates G0–G8), [handoff 01](handoffs/01-work.md) (binding instruction and pre-registered gate criteria), and `results/padua-argmax-effective-20261103.md`.
- Novelty gate: deferred to the developer (handoff step 0). The brief lists the closest entries; no new mechanism is claimed here.
- Subagents: none.

## Runs needed

- Independent replay of the pilot (handoff step 0).
- Gates G0–G8 and routes R1–R6, as in handoff 01.
