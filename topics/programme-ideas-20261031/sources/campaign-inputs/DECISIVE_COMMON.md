# Common instructions for decisive-test agents (Step 5)

Read, in this order: /home/claude/inputs/CAMPAIGN_CONTEXT.md; the gate entry for your candidate in /home/claude/padua_research/topics/programme-ideas-20261031/gate.md; your candidate's draft(s) in checks/state/; the adversarial report checks/adversarial-<id>.md IN FULL (its "Required changes if it survives" section names the fastest kill); and the scripts under checks/code/adv/<id>/ (reuse them).

Your candidate was WOUNDED, not killed: it survives only as a 1–3-paper project. Step 5 settles, by a cheap decisive computation, whether that residue is real and worth AC's time, and whether any escalation path remains that the adversary did not close. You are neutral: neither advocate nor adversary.

## Procedure (binding order)

1. FIRST write /home/claude/padua_research/topics/programme-ideas-20261031/checks/decisive-<id>.md with sections `# Decisive test — <id>: <title>`, `Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator) · Decisive test · 2026-11-01`, `## Residue under test` (one paragraph: exactly what survived the adversarial check), `## Pre-registered tests and kill criteria` (two or three tests; for each: the exact quantity, the scope (n, M, N, seeds, tolerance), the runtime budget (seconds to a few minutes), and the KILL criterion as a numeric inequality or a yes/no outcome written BEFORE running), `## Results` (empty), `## Verdict` (empty). Tell the orchestrator in one line of your final reply that the pre-registration was written before any run (the orchestrator commits it).
2. THEN write and run the scripts under /home/claude/padua_research/topics/programme-ideas-20261031/checks/code/decisive/<id>/ (save outputs as .out/.log next to them; keep every output file under 100 kB).
3. THEN fill `## Results` (tables; every number MEASURED within its stated scope; record what you did not run) and `## Verdict`: one of `RESIDUE CONFIRMED (project of K papers; no programme)`, `RESIDUE KILLED`, or `ESCALATION FOUND (state the new mechanism and why the adversary's closure fails)`. End with `## For the proposal/report` — five to ten lines the report writer can use verbatim: what AC would get, with whom, in what time, and the risk.

Do not edit any other file. Do not quote PDFs or bttb-research at length. Web search is allowed only for a specific fact the test needs (record query and date). Final reply: verdict, the kill criteria and whether each fired, runtime, files written.
