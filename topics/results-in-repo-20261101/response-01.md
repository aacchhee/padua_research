# Response-01 to Codex audit-01 — results-in-repo-20261101

- **Date:** 2026-11-01.
- **Branch and rules:** branch `claude/results-in-repo-20261101`. Input head and rules read at `e62b19d8152c54ffd84eb824c94666a1590962e6`, which publishes handoff 03 at input `2df41fe`. main is `e0d9e3d08ee26c3b82a295f33b6ff99d928f22b9`, unchanged and an ancestor.
- **Agent:** Claude, acting as developer and topic orchestrator. AC requested "Claude (Sonnet 5.5, medium)". The session's configured model is `claude-opus-5-5`, and the serving model is not separately exposed. I record it truthfully rather than claiming Sonnet.
- **Scope:** all three findings are accepted and fixed. These are mechanical transcription and link corrections to summaries. No rule, accepted claim, dependency, status, code or evidence changed, so no fresh audit is required (audit-01 Disposition).

## F1 — P2: operator summary constraints (fixed)

`results/padua-mz-2d-20261101.md`, PD-T112/113 bullet.

- **Before:** "The exact signed hyperinterpolation C→L² norm is sup Σ|w||p(z)| ≤ √(τ β_abs). The operator reproduces Π_r when n+r ≤ m."
- **After:** the norm is now stated as the supremum over **p ∈ Π_n with ‖p‖_(L²(dx dy)) = 1**. τ_m (total variation of the weights) and β_abs (largest eigenvalue of the absolute-weight Legendre Gram matrix) are defined, with links to PD-T112. Reproduction now states **both 0 ≤ r ≤ n and n+r ≤ m**, including the endpoint consequences r=1 for m ≥ 2 and r=0 for m=1, n=0.

**Source comparison.** I compared the new text with the merged statements:
- [PD-T112 statement](../../tracks/mz-constants/theory/mz2d-hyperinterpolation-absolute.md) (eq. 1): the supremum over p ∈ P with ‖p‖_L²(μ) = 1 is at most √(τβ_abs), with P = Π_n and V = 4 for the campaign.
- [PD-T113 statement](../../tracks/mz-constants/theory/mz2d-hyperinterpolation-reproduction.md): "For every integer 0 ≤ r ≤ n, n+r ≤ m … reproduces Π_r"; "For m=1, n=0, use r=0".

The new text matches both. The source theorems are unchanged.

## F2 — P3: m40 audit method (fixed)

`results/padua-mz-2d-20261101.md`, PD-T107 bullet.

The text now distinguishes three things:
- the developer's signed-dominance certification, with its two reruns (the Codex worker and Claude R1);
- Claude's Sylvester-minor certification, at m=10/20/30 only;
- Addendum A1's independent certification at m=40 by a Cholesky-proposed exact congruence plus exact positive strict dominance, with exact Rayleigh quotients.

It links A1 and keeps A1's caveat about the shared general congruence-and-dominance principle. I compared this with [audit-01 R3 and Addendum A1](../padua-mz-2d-20261101/audit-01.md). The brackets and their status are unchanged.

## F3 — P3: links to records and evidence (fixed)

The migrated file now has a grouped source trail:
- the report, log, definitions, audit-01 with the A1 anchor, the auditor evidence manifest, response-01, PROOF_STATUS, the ID map and IDEAS;
- four compact evidence JSON files;
- a direct link from each result ID to its durable theory record (all 22 records plus PD-T028).

No proof or evidence is copied. All targets were checked to resolve from `results/` (see Checks).

**Additional correction, within scope:**
- The stale history line saying PR14 was "still draft, awaiting AC's squash-merge" now records the merge.
- The OPEN section now separates the campaign's three OPEN records (PD-T110/116/114) from the pre-existing PD-T028, as audit-01 §4 noted.

## Handoff step 5 — this topic's own results

- Added [results/results-in-repo-20261101.md](../../results/results-in-repo-20261101.md).
- Appended this topic's section to the root `RESULTS.md`. The PR14 section is preserved byte-for-byte.
- No other topic was migrated.

## Checks

The results of these checks are recorded in LOG.md:
- Every Markdown link in `results/`, `RESULTS.md` and this topic's directory resolves to a file, and the A1 heading anchor matches GitHub's slug.
- `git diff --check origin/main..HEAD` reports no whitespace errors.
- `agents/`, `AGENTS.md`, `templates/`, theory, code and evidence are unchanged in this response, relative to the audited candidate `715b182`.
