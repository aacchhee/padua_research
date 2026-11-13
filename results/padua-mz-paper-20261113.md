# padua-mz-paper-20261113 — finalizing the MZ papers (MZ-CC, MZ-SP)

This file is written only by the topic orchestrator. Branch `claude/padua-mz-paper-20261113`; no PR yet.

## Status (2026-11-13): WORK, draft PR #35

Target: split *Marcinkiewicz–Zygmund constants of Clenshaw–Curtis and Padua rules beyond half-exactness* (AC, 2026-11-13) into two submission-ready manuscripts for AC's decision:

- **MZ-CC:** Clenshaw–Curtis, with the sharp endpoint constants;
- **MZ-SP:** signed Padua, beyond half-exactness.

MZ-CC comes first. The work:

- integrate PR #31's sharp results: lim (log N)²λ_min = π⁴/8; λ_max ≤ 5/3 for all N; the CC upper limit as an endpoint-operator norm; the signed Padua log limits as inf/sup spectrum of a compact corner operator;
- restructure around them;
- finish the literature after PR #21;
- meet AC's manuscript criteria.

Plan: [BRIEF](../topics/padua-mz-paper-20261113/BRIEF.md) and [handoff 01](../topics/padua-mz-paper-20261113/handoffs/01-work.md).

## Results so far (2026-11-13)

- Split done (gate W0 PASS): MZ-CC → SIAM J. Numer. Anal. (`siamart251216`); MZ-SP → J. Approx. Theory (`elsarticle`). [split-map](../topics/padua-mz-paper-20261113/split-map.md).
- MZ-CC now contains, with full proofs at their record scopes:
  - the uniform bound λ_max ≤ 5/3 (PD-T526);
  - the sharp limit (log N)²λ_min → π⁴/8 with its finite bound (PD-T546, PD-T523, PD-T522/544/545; Appendix A);
  - λ_max → Λ_edge ∈ [1,3/2] (PD-T530, PD-T529 weakened; Appendix B).
  It builds clean at 28 pp.; the introduction and §6/§8/§9 are still to rewrite.
- New provisional claim PD-T?mz-paper-claude-01 ([record](../topics/padua-mz-paper-20261113/theory/cc-defect-condition-corollary.md)), PROVED by the developer:
  - 1−η_N = λ_min(G_{N,N−1}) for every N ≥ 57, and (log N)²(1−η_N) → π⁴/8;
  - κ₂(G_N)/(log N)² → 8Λ_edge/π⁴;
  - ‖𝓘_N‖_{ℓ²_w→L²}/log N → 2√2/π²;
  - CC hyperinterpolation factor (1+√(5/3))√2.
  An independent check passed for (a)–(c); (d) is pending. Codex audit pending.
- MZ-SP: post-split text in `elsarticle`; integration not started.

## Next step

`Claude (Opus 5.5 xhigh): Continue claude/padua-mz-paper-20261113.`
