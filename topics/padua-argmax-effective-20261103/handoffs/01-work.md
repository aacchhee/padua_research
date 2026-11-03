# Handoff 01 — padua-argmax-effective-20261103 — effective all-degree Padua argmax (adventurous campaign)

- Status: superseded by 02: AC added the requirement that large-n certification use a C/FLINT port run in the sandbox (2026-11-03)
- Previous handoff: none

- Next agent / model / effort: Codex, **gpt-6-astra at ultra** for the orchestrator and all mathematics. This follows AC's explicit instruction (2026-11-03: "This looks like a topic that warrants astra with ultra reasoning"), which overrides the WORKFLOW allocation table for this campaign; record that justification in LOG. Use gpt-6.1-sol medium for code, ports, timing and replays. Use a separate gpt-6-astra high instance for supplementary independent checks.
- Role: orchestrator and developer
- Branch: codex/padua-argmax-effective-20261103
- Input head SHA: `0a3071a270ac7d248e01607f93156fa617d90deb` (brief and pilot record; the commit that publishes this file comes later)
- Main / base: `440d107` (PR #17 merged)
- Stage: WORK
- Written by / date: Claude, claude-opus-5-5 · 2026-11-03

## Task

**Objective:** close PD-T099 for every n ≥ 2, or make the largest possible effective progress toward it.

- Finite certificates already cover 2 ≤ n ≤ 16.
- PD-T229 covers n ≥ N_*, but N_* is non-effective.
- The campaign succeeds if it supplies an **explicit** n₀ with a proof for n ≥ n₀ plus certificates for 17 ≤ n < n₀, or an exact all-n argument that needs no enumeration.
- A certified counterexample is an equally valid outcome.

Everything known is in [BRIEF.md](../BRIEF.md): exact structure, the proof of PD-T229 and where it stops being effective, the measured margins, the finite-certifier capacity, the refuted routes, routes R1–R6 and gates G0–G8. Read it in full first.

This campaign is more adventurous than the previous gated one:
- Run several routes in parallel subagents with disjoint file ownership.
- Generate and test conjectures freely.
- Follow surprises.

The honesty rules do not relax:
- Statuses follow AGENTS.md.
- Floating-point evidence is MEASURED.
- A computer-assisted claim needs a written reduction, exact or outward-rounded arithmetic, committed checker code with small evidence (large artifacts go to cold storage with a manifest), and an independent rerun by a different subagent.
- Every failed mechanism gets an IDEA disposition and, where it is a genuine negative statement, a scoped PD-N.

### Order

0. **Setup.**
   - Read AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md at the branch head, and record the SHA.
   - Fetch main. If it moved, merge it, recording the impact first.
   - Run the relaxed novelty gate (WORKFLOW). Closest entries: IDEA-206, IDEA-305, IDEA-316…335 (PR #17), IDEA-290…302 and IDEA-320.
   - Independently replay Claude's pilot (`code/g2_pilot.py`, `code/g3_pilot.py`, and the certifier commands in the pilot record), using a different subagent with its own outputs.
1. **Easy gates G0–G5 (BRIEF §8), first.** The pre-registered decision criteria are below. Do not change them before running. If one proves ill-posed, add a dated new criterion and keep the old one.
2. **Route selection by the decision rule** (BRIEF §8). Run R6 (effective corner zone) as one bounded round in any case: the true margin factor there is about 3 (G2).
3. **Main routes in parallel**, as justified by the gates: R1/R2 (effective asymptotics), R3 (exact comparison), R4 (generating curve, starting with its kill test), R5 (wild card, at most one bounded round unless it shows a mechanism).
4. **Finite range.** Keep extending certified degrees (G0/G1) as long as cost allows. Port the certifier (C, FLINT or arb, parallel leaves) if G1 shows that it pays. Ask AC before using NTNU servers.
5. **Assembly.** If an explicit n₀ and certificates up to n₀ − 1 both exist, write the all-n theorem with its dependency list. Otherwise write the precise remaining obligations, with every partial theorem in its own record.

### Pre-registered gate criteria

- **G0.** Each degree 17 ≤ n ≤ 24 counts as certified only when the PD-T210 producer and checker both accept, and a different subagent has replayed it. Any degree whose cover cannot complete within 24 h of CPU gets a scoped record, not a failure claim about PD-T099.
- **G1.** Report the fitted cost exponent and the projected n_cert for 24 h and for 7 days of single-core time, both for the current code and for an estimated port.
- **G2/G3/G4.** Report the measured true constants: the local K(n), the global C(n), the far-coset margin, and the minimal λ-gap and Δ near every non-corner coset class. Kill R1 in its "constants within a factor 2 of the truth" form if the projected n₀ (G5) exceeds 10 × n_cert(7 days, port).
- **G5.** If projected n₀ ≤ n_cert, R1/R2 plus finite certification is the main line. Otherwise prioritize R3/R4/R5, and keep R1/R2 only for the corner zone (R6).
- **G6.** Kill the all-n E-C route in its stated whole-cell form if any exact counterexample appears at some n ≤ 60. Float reversals must be confirmed exactly before they count.
- **G7.** As written in IDEA-319: kill it if no cell-wise sign-stable envelope exists at n = 4.
- **G8.** Required before any 1-D technique is transferred into a proof.

## Read first

- [BRIEF.md](../BRIEF.md) and [the pilot record](../theory/argmax-effective-claude-01-pilot-measurements.md).
- From `topics/padua-argmax-alln-20261101/`:
  - report.md and gated/REPORT.md;
  - theory gated-codex-01…17 and N01/N02, argmax-alln-codex-02…08 and N01;
  - attempts/P0-finite.md and code/part3/;
  - audit-01.md and response-01.md.
- From `topics/padua-proof-attempts-2-20261101/`: theory 01–04 (PD-T156–159) and 70–77 (PD-T185–192).
- PD-T101, plus PROOF_STATUS rows PD-T098–101, PD-T156–235 and PD-N072–083.
- state/IDEAS.md entries IDEA-206, 290–305 and 316–335.
- literature/INDEX.md, LIT-312, LIT-379 and LIT-388.

## Scope limits

- Write only inside `topics/padua-argmax-effective-20261103/` and `results/padua-argmax-effective-20261103.md`. Edit no merged topic, theory or registry file. Put proposed shared-record changes in `proposed-record-changes.md` as literal old→new blocks, for PR preparation.
- Provisional IDs: `PD-T?argmax-effective-codex-NN`, `PD-N?…`, `IDEA?…`, `LIT?…`. When the draft PR opens, reserve final ranges by the WORKFLOW fresh-range procedure, covering main, every open PR, retired reservations and the batch ledgers, with headroom.
- Storage (WORKFLOW after PR #18): commit only code, short summaries, receipts and small essential evidence (normally under 16 KiB per file). Regenerable outputs and large certificates go to cold storage via `tools/cold_storage.py`, recorded in `cold-storage.json` and `COLD_STORAGE.md`, and handed to AC.
- Never commit third-party PDFs or fulltext extracts (the repo is public). You may open any public page holding relevant literature, and list fulltexts you cannot reach for AC with DOI and journal link.
- Commits are authored as Andrey Chesnokov <aacchhee@gmail.com>, with trailers `Agent: Codex` and `Model: <exact model and effort>`. Never commit to main, merge, force-push, create tags or touch .github/. Only AC merges.

## Acceptance and outputs

- `LOG.md` with one entry per step boundary.
- `plan.md` with routes, owners and kill criteria, written before each run.
- `attempts/<route>.md`, `theory/` records in THEORY-template form, `independent-checks*.md`, `evidence-manifest.json`, and `results/padua-argmax-effective-20261103.md`, kept current.
- Push at every step boundary and at least every ~10 minutes while something has changed. Open a draft PR to main early, with WORK / AUDIT (PENDING) / PR sections and the ID reservation.
- A final `report.md` covering:
  - the gate verdicts;
  - each route's outcome, with its records;
  - the certified finite range;
  - any explicit n₀;
  - counterexamples, if any;
  - what remains OPEN and why.
- When done, commit the outputs. Then, in a following commit, set this status to `done in <sha>` and open handoff 02 for the audit by Claude, Opus 5.5 xhigh, which reads the complete state/IDEAS.md because this branch carries mechanism and novelty content. Reply to AC only with `Claude (Opus 5.5 xhigh): Continue codex/padua-argmax-effective-20261103.`
