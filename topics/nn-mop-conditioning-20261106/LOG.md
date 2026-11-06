# NN MOP conditioning: intrinsic or metric? Sharp rates, weak stability, IEP-MOP comparison: log

- Branch: `codex/nn-mop-conditioning-20261106` · Base: main `76ba421` · Developer: Codex · Auditor: Claude (Opus 5.5 xhigh)
- Stage: WORK · Next: `Codex (gpt-6-astra high): Continue codex/nn-mop-conditioning-20261106.` · Open handoff: [handoffs/01-work.md](handoffs/01-work.md)
- Reserved final-ID ranges: none. Reserve when first needed (PR #29 rules).
- Claims: none yet.

## 2026-11-06 — Claude, claude-opus-5-5 (configured; effort not exposed) — topic setup

- AC asked what can still be done on the IEP/Leuven line. Claude proposed step 1, a focused round, and then a note. AC: "yes open a codex branch for step 1".
- Claude's reading of PD-T434 (arithmetic only) shows the step-line κ has the same exponential base as NN, about 4 times smaller. The open question is therefore whether the exponential survives the 1-D control, diagonal gauges and the LIT-347 normalization.
- Directions:
  - C1: the metric question;
  - C2: sharp rates (Krawtchouk upper, Hahn lower, ρ(p₁, p₂));
  - C3: weak stability;
  - C4: the IEP-MOP field-by-field comparison.
- Up to 8 rounds per direction, in parallel; coordinator gpt-6-astra high.
- Rules read at `76ba421`. Branch created from main `76ba421`. Only this LOG, handoff 01 and the results stub were added. No computation was run and no claim made.

## Runs needed

- M0–M4 and C1–C4 as in handoff 01.

## 2026-11-06 — Codex coordinator, requested gpt-6-astra high — replay and launch

Rules read at full topic head `b4a04981d42c7cd872957facf5e3995e4096ca67`;
AGENTS/workflow/Codex role blobs equal the local main rules already read.
Refreshed main through GitHub connector: `76ba4214b100c86a44941f5e9a662ce9ce48efb8`,
the topic's parent. No base integration required. Shell fetch failed at the
configured proxy; pinned-file snapshot and publication route are in plan.md.
GitHub connection profile reports the prescribed author name/email.
Serving model identity/effective effort are not independently exposed.

Plan written before first run. First parallel launch had a shell redirection
race creating the temporary output directory: Hahn did not start; restarted
after directory creation. Both 180-dps and both separate 260-dps runs then
completed successfully. Original M0 cannot be assessed to 1e-10 against a
seven-digit historical table. Dated M0a amendment in gates.md preserves that
limitation. All twelve values pass fresh precision agreement and historical
rounding checks: code/replay_gate.py and m0a-receipt.json. This is numerical
repeatability, not a certified enclosure or historical raw-file recovery.

After M0a, delegated disjoint C1 metrics and C2 sharp-rate mathematics to
Sol xhigh, C3 stability mathematics to Sol xhigh, and C4 source/metric/code
comparison to Sol medium, as handoff01 explicitly requests. No final IDs or
shared scientific registry changes. Open handoff01 remains open while this
session carries the work. Commands: predecessor conditioning.py --sizes
4 16 32 --family {krawtchouk,hahn} --dps {180,260}, followed by this topic's
code/replay_gate.py /tmp/nn-mop-conditioning-20261106. Receipts pin raw outputs.


## 2026-11-06 — canonical publication-author exception

Checkpoint 8666d8e0a4f99f9f4f751c8b0b16f9064b23881d was created by
the connector as Andrey Chesnokov <59649991+aacchhee@users.noreply.github.com>,
despite get_profile reporting the prescribed Gmail address. Coordinator
verified the commit author after publication, disclosed the mismatch to AC,
and requested continuation under the predecessor's exception. AC explicitly
answered “Allow the GitHub noreply author.” This author exception now applies
to continued publication here; do not rewrite the existing checkpoint.
Draft PR: https://github.com/aacchhee/padua_research/pull/32.

## 2026-11-06 — C4 checkpoint and decisive C2 hard step

C4 completed two useful preparation rounds: source-access/fulltext review,
then exact local coordinate-interface validation (six cases). Required pinned
archive bytes remain absent; M2/M4 are BLOCKED, not numerical failures.
See attempts/C4.md and external-code.md. No external solver ran.
The two preparation rounds are published together at this checkpoint.

C2 requested the all-triangle Krawtchouk upper-rate hard step after the
novelty gate. Assigned a bounded distinct Astra ultra worker: matching the
full node/weight Jacobian upper rate is the decisive hard step explicitly
authorized in handoff01, beyond the routine terminal-witness algebra.
C2 retains parameter-dependent lower/Hahn work; upper worker owns only
theory/c2-sharp-upper.md and attempts/C2-hard.md. No result claimed yet.
Supplementary distinct Astra high checker independently reruns M0 and C4,
then checks new gauge/rate mathematics; this supplements, not replaces,
the eventual Claude audit.
