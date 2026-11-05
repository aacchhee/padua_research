# Execution plan — 2026-11-05

Rules and input head: `8359bf7a047d9a212bd841224fb97a458cb7435e`; base/main: `440d1079e42c3ef21c40d1cf8870f5b206410c6a`. Rules unchanged from base. Orchestrator: Codex, requested gpt-6.1-sol xhigh; runtime does not independently expose effort. Supplementary checker: gpt-6-astra high.

1. G0: independent replay first, approximately 30 minutes setup/replay allowance. No new scientific runs until its mismatches are resolved.
2. Read the prior campaign and novelty memory. Prepare disjoint L1/L2, L3/L4, L5/L6 and L7 work packages. Record candidates and gates before runs.
3. After G0, work in bounded rounds toward the handoff limits: L1 10 h, L2 6 h, L3 6 h, L4 4 h, L5 4 h, L6 4 h, L7 6 h. Limits are ceilings, not claims of elapsed work. Preserve unsuccessful routes and exact remaining obligations.
4. Independent exact checks for substantive computational claims; Claude audit remains a separate handoff.
5. Checkpoint at gate/target boundaries. Open draft PR after refreshing allocation ledgers and reservations; no final IDs or shared registry writes during exploration.

## Ownership

- g0_replay: `independent-checks-g0.md` only; working outputs outside Git.
- Orchestrator: plan, gates, log, integration, Git, results and handoffs. Further workers receive separate ownership before starting.

## Storage

Large regenerable outputs stay in `/tmp/padua-lanczos-frontier-*` or a Padua-specific workspace directory. Windows cold-storage delivery is pending; no external machine is authorized. Commit short receipts and regeneration code only.
