# Novelty gate X2 — Morrow–Patterson Lebesgue function

Orchestrator: Claude (Opus 5.5), 2026-11-14, rules `2d60e22`. Relaxed scan; the scan scope and terms are shared with [novelty-gate-X1.md](novelty-gate-X1.md). Repository hits are IDEA-047 (survey MP; deferred contextual) and LIT-378 / LIT-388. There is no PD-T or PD-N row on MP points.

## Literature verdict first

The BRIEF's X2.1 target, Λ_MP(n) ≥ c n² with explicit c, is published: Beberok, JAT 311 (2025) 106191, Thm 0.1 (see [literature-xu-mp.md](literature-xu-mp.md) §3.1). It is not pursued as new. Any local reproof is recorded as LITERATURE-reproduction only.

## Shortlist and verdicts

| Provisional candidate | Closest entries | Separation criterion (falsifiable) | Cheapest decisive test | Verdict |
|---|---|---|---|---|
| X2-C1: exact values of λ_n at the four vertices; the conjectures λ_n(±1,−1) = n+1, and λ_n(±1,1) in closed form | Beberok 2025 eq. (2) (kernel at (1,1)); BBDM §7 (numerical "(n+1)(n+2)/2 at each corner") | Beberok gives the kernel at (1,1) and a lower bound, not the value. BBDM give numerical values at all four corners, which our numerics contradict. **Killed if** the G0 path-A values at (±1,−1) equal those at (±1,1), i.e. BBDM's corner statement is right. | C-MP corner check (gates addendum) | **new** pending C-MP |
| X2-C2: negative answer to BBDM §7.1: λ_n(x,y) ≠ λ_n(−x,−y), and Λ_n is not attained at the corners (±1,−1) | BBDM §7.1 open problems | A certified inequality at one even n settles the symmetry question negatively. **Killed if** the enclosures overlap at every tested n. | C-MP | **new** (negative result to a published open problem) |
| X2-C3: sharp constant lim Λ_n/n² and its closed form, together with argmax = {(±1,1)} | Beberok 2025 (lower bound only); BBDM Thm 4 (O(n²), no constant) | No source gives a limit or an argmax proof. **Killed if** the limit is a trivial consequence of Beberok's computation, i.e. the dominant lattice sum is already evaluated there. It is not: Beberok keeps only one diagonal and bounds it crudely. | Numerical limit estimate (MEASURED), then proof | **new** |
| X2-C4: MPX variants | none (undefined in sources read) | — | find a defining source | **deferred**: no definition found; resume if Xu JAT 2012/2017 defines them |
