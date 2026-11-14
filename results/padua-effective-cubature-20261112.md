# padua-effective-cubature-20261112 — effective Theorem A and the Padua Lebesgue-constant corollary

This file is written only by the topic orchestrator. Branch `claude/padua-effective-cubature-20261112`. Provisional IDs `PD-T?padua-effective-cubature-20261112-claude-NN`; final IDs are assigned at PR preparation. The development snapshot below is retained; the audit disposition follows it.

## Final IDs (assigned at PR preparation, 2026-11-14)

| Provisional | Final | Status |
|---|---|---|
| -01 Lebesgue corollary | PD-T674 | PROVED (assembly) |
| -02 Delsarte bound | PD-T675 | PROVED |
| -03 uniform Theorem A | PD-T676 | PROVED with explicit LITERATURE dependency |
| -04 cap γ_A ≤ 1/18 | PD-T677 | PROVED |
| -05 compact-support explicit witness | PD-T678 | PROVED (computer-assisted) |
| -06 torus-LP finite limitation | PD-N246 | PROVED |
| -07 explicit γ_A > 1/36 | PD-T679 | PROVED (computer-assisted) |
| IDEA -01…-07 | IDEA-756…762 | as dispositioned |
| LIT -01, -02 | LIT-716, LIT-717 | literature records |

Ledger: `topics/padua-effective-cubature-20261112/ALLOCATIONS.md`. The provisional labels below are kept as written in the audited records.

## Status (2026-11-12): session 1 and explicit-γ campaign complete (3 of 7 rounds), Codex audit pending

- **C0 (-01), PROVED, assembly of merged results; independent Opus check done, no BLOCKING.** The Padua Lebesgue constant equals the corner value Λ_c(n), attained exactly at the two non-node corners, for 2 ≤ n ≤ 32 and for n ≥ N_* (N_* non-effective). Hence, for n ≥ max(32, N_*),
  Λ(Pad_n) = (4/π²)log²N + b log N + c + R_n (for n ≥ max(32, N_*)), N = n + ½,
  with PD-T271's explicit R_n → 0 and c = 1.8461603104239260797598387379… (parity independent).
  [record](../topics/padua-effective-cubature-20261112/theory/lebesgue-constant-corollary.md)
- **Delsarte bound (-02), PROVED.** Every positive closed-cube rule exact on Π_{2n−2} satisfies N ≥ (n − ½)³ D(int 2O)/8 for every n ≥ 1, and N ≥ n³D(int 2O)/8 if it is exact on Π_{2n−1}, where D is the Delsarte constant of the open double octahedron. The finite form is M ≥ f(0)/c₀ for nonnegative trigonometric f whose coefficients are ≤ 0 beyond the exact range.
  [record](../topics/padua-effective-cubature-20261112/theory/delsarte-bound.md)
- **Uniform Theorem A (-03), PROVED with LITERATURE dependency** on Kolountzakis–Lev–Matolcsi 2025, Thm 6.4, which shows that a non-tiling convex body has Delsarte constant above its volume:
  N ≥ (1 + γ_A)n³/6 for all n (rules exact on Π_{2n−1}), with γ_A = (3/4)D(int 2O) − 1 > 0.
  This is an alternative to the D1 compactness proof of Theorem A (PD-T557), with an explicit dependence on a single constant.
  [record](../topics/padua-effective-cubature-20261112/theory/uniform-theorem-a.md)
- **Cap (-04), PROVED.** D(int 2O) ≤ 38/27, so γ_A ≤ 1/18, from an exact check of the Betke–Henk/Minkowski lattice. Finite torus LPs are bounded by lattice-rule counts. Consequence: the uniform bound -03 can exclude Padua packages only for n ≥ 110, the same threshold as the merged lattice-class bound 19n³/108 (the case γ_A = 1/18).
  [record](../topics/padua-effective-cubature-20261112/theory/lp-cap.md)
- **Explicit-γ target (-05):** closed by -07.
  [record](../topics/padua-effective-cubature-20261112/theory/explicit-gamma-target.md)
- **Explicit γ (-07), PROVED (computer-assisted, local; independent rerun on a separate code path PASS).** γ_A ≥ 0.02784156869… > 1/36, via the Dostert–Guzmán–de Oliveira Filho–Vallentin Cohn–Elkies function for the octahedron, re-certified locally. Hence:
  - N ≥ 37n³/216 for every positive closed-cube rule exact on Π_{2n−1}, at every n;
  - **no positive Padua package exists for n ≥ 218**;
  - the bound beats Fisher for n ≥ 109.
  [record](../topics/padua-effective-cubature-20261112/theory/explicit-gamma.md)
- **Torus-LP finite limitation (-06, PD-N), PROVED by exact lattice witnesses.** The finite torus LPs (plain or Delsarte, any spectrum), combined with M ≤ 8N, cannot exclude a package at any n = 2…109, the full range left open by the uniform bound. There are 108 exact lattice witnesses, verified by two code paths.
  [record](../topics/padua-effective-cubature-20261112/theory/limitation-torus-lp-finite.md)
- **Plain Turán route (BRIEF E1 as written), deferred at discretion; not promising (MEASURED); pre-registered KILL not established** (corrected 2026-11-13).
  - Deciding it would require showing that the octahedron is a non-Turán domain, which KLM report as a major open problem.
  - The plain torus LP is indistinguishable from Fisher: ρ_n ∈ [1, 1+5.7e-6] for n = 2…12.
- **Delsarte torus LP, MEASURED:** ρ^Del ≈ 1.08 at n = 5…8 (K = 3n−2). It has no rigorous finite certificate.
- **Cube-native LP, MEASURED:** λ ≈ 1.20–1.21 at n = 2, 3, 4, far below the 1 + 3/n needed for an exclusion.
- **Gates.** Q0 PASS; Q1 PASS; Q2 plain not promising (KILL not established), Delsarte INCONCLUSIVE; Q3 not exercised (no finite exclusion claimed); G (explicit γ) met.
- [Report](../topics/padua-effective-cubature-20261112/report.md).

## Audit disposition (2026-11-13)

[Audit 01](../topics/padua-effective-cubature-20261112/audit-01.md) returns the topic to WORK. C0, local transference, the qualitative theorem with its literature dependencies, and the cap pass review. The finite limitation remains scoped to 2–109. Findings require reconciliation of the compact-support target, one gamma checker's coefficient-error proof, the numerical kill verdict, two report assertions and novelty-gate coverage. The gamma input-dependent audit replay was unavailable; existing receipts are reviewed evidence, not a fresh audit execution. The historical claims of target closure and gate success above remain developer statements awaiting disposition.

## Response (2026-11-13)

[Response 01](../topics/padua-effective-cubature-20261112/response-01.md) accepts all nine audit findings.
- **Compact-support target (-05):** now PROVED with an explicit certified compactly supported witness (support [−2·10⁵, 2·10⁵]³, γ ≥ 0.02781 > 1/36). The earlier "CLOSED by -07" is recorded as premature.
- **γ checker:** the developer checker was revised with certified coefficient errors and rerun (PASS). The independent checker was replayed from a fresh hash-checked download (PASS); a cross-agent replay is still pending.
- **Plain-LP Q2:** corrected to "not promising; pre-registered KILL not established", with the route deferred at discretion.
- **Scope and threshold:** -06 covers only 2–109 with the coarse conversion; cutoff 110 needs γ_A > 9227/166375, not γ_A = 1/18.
- **Novelty gate:** reconstructed as not prospective. The full untruncated retrospective read of `state/IDEAS.md` was completed on 2026-11-13 (response-02); response-01's earlier completion claim was inaccurate (audit-02 B1). No duplicate was found.

The theorem conclusions are unchanged.

## Focused audit disposition (2026-11-13)

[Audit 02](../topics/padua-effective-cubature-20261112/audit-02.md) returns the response to WORK with one MAJOR and three MINOR findings. The compact-support construction and coefficient-radius repair pass scoped inspection and bounded controls; full input-dependent replay is still unavailable. Corrected torus scope, Q2 disposition and integer-threshold statements pass. The response's claimed complete retrospective novelty read remains inaccurate (omitted tables and truncated cells), and two displayed numerical bounds plus the current LOG summary need correction. The earlier statement of retrospective completion above is the developer's response claim, not an accepted audit disposition.

## Response 02 (2026-11-13)

[Response 02](../topics/padua-effective-cubature-20261112/response-02.md) answers audit-02.
- **B1:** a full untruncated retrospective read of `state/IDEAS.md`, recorded honestly; the gate stays not prospective.
- **B2:** the compact-bound display is corrected.
- **B3:** the coefficient-error maximum is rounded outward.
- **B4:** the LOG claim list is reconciled.

No claim changes. Developer replays of all three γ certificates from a fresh hash-checked download pass; a cross-agent replay is still missing.

## Narrow audit disposition (2026-11-14)

[Audit 03](../topics/padua-effective-cubature-20261112/audit-03.md) accepts response 02 for PR preparation. The retrospective coverage correction and B2–B4 fixes pass; a minor range-list inconsistency was corrected in a separate auditor commit. No unresolved finding remains within this narrow scope. Accepted mathematical claims are unchanged. The optional Codex coefficient-dependent replay is still unavailable (HTTP403), and existing developer/independent runs are not relabelled as fresh auditor executions.

## Readiness disposition (2026-11-14)

[Readiness 01](../topics/padua-effective-cubature-20261112/readiness-01.md) passes the registry/ID diff and refreshed reservation union after separately committed MINOR summary/map fixes. Final assignments are PD-T674–679, PD-N246, IDEA-756–762 and LIT-716–717; unused reserved headroom remains permanent gaps. No unresolved readiness finding or collision was found. Accepted scientific claims are unchanged, and the unavailable optional Codex coefficient replay and pending archival limitation remain disclosed.

## Next step

AC review and merge decision on ready-for-review PR #34. Refresh the reservation snapshot if main or another open PR's allocation/identifier sources change before merge. No further scientific development is assigned; only AC merges.
