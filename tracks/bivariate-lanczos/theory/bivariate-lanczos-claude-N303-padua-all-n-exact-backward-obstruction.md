# PD-N?bivariate-lanczos-claude-303 — Reading (E): exact-section backward representation of perturbations given as data, with δ(ε) → 0, fails for Padua points of every degree n ≥ 4 (reading (G) OPEN)

ID kind: PD-N.
Aliases: Padua obstruction, all n; extends PD-N?…-301 (n = 3); R05.
Split from: none (case of the target PD-T?bivariate-lanczos-claude-300).
Split into: none.

## Statement

For every n ≥ 4 and any positive weights on the Padua points of degree n there is δ_0(n) > 0 such that, for every ε ∈ (0, ε_1] (M_n(L_μ + E) ≻ 0 for ‖E‖ ≤ ε_1) and every functional E on Π_{2n+1} with ‖E‖ ≤ ε and E(P_n) < 0 (P_n of PD-T?…-313; e.g. E = −ε ev_ζ/‖ev_ζ‖ (so ‖E‖ = ε) with P_n(ζ) > 0), the consistent degree-n section pair Φ(L_μ + E) (structural pattern, all interior commutativity conditions exact) is not the exact section pair of any positive measure supported within δ_0(n) of the nodes; any positive measure on K_δ, δ ≤ δ_0(n), has functional distance ≥ |E(P_n)|/‖P_n‖_* from L_μ + E (the unnormalised reference, convention (R1) of PD-T?…-302; for the mass-normalised representative L̂ = s_E(L_μ + E) of the same sections, convention (R3), the bound is multiplied by s_E = m/(m + E(1)), PD-T?…-302(b3)). Together with PD-N?…-301: in reading (E), no δ(ε) → 0 exists for any Padua degree n ≥ 3. Here δ_0(n) is a chosen radius (it may be taken nonincreasing in n); the certified lower bounds for the positivity radius of P_n decrease over n = 4..12 (PD-T?…-313 Open items). No uniform-in-n obstruction radius is established here; whether one exists is OPEN (PD-T?…-319). The statement concerns exact representation (or a sufficiently smaller residual) of specified consistent perturbations given as data; it does not address the finite-precision Greenbaum reading (G), which remains OPEN (PD-T?…-300).

## Negative-result scope (PD-N only)

Attempted mechanism: IDEA?bivariate-lanczos-claude-307 (exact Greenbaum-type commuting/graded backward model in the square case).
Parameter range: Padua points (this family), n ≥ 4, any positive weights, perturbative regime, exact representation, or a residual measured against L_μ + E (convention (R1)) smaller than |E(P_n)|/‖P_n‖_* (against the mass-normalised representative, convention (R3): smaller than s_E|E(P_n)|/‖P_n‖_*); [IDEALIZED: perturbations given as data] — reading (E) only. Not covered: residuals of the order of the perturbation; actual floating-point error directions and the Greenbaum reading (G) (OPEN); support beyond δ_0(n); uniformity in n (PD-T?…-319, OPEN).

## Status by part

Overall status: PROVED under the stated assumption that the Padua points are Π_n-unisolvent (LITERATURE: Caliari–De Marchi–Vianello / Bos et al., record bos-dmv-xu-2007; verified exactly for n ≤ 4 by L3-reconstruction-01) — a trusted dependency, needed so that the sections exist.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| reduction (PD Hessian certificate ⇒ obstruction) | PROVED | PD-T?…-303(e), 302, 301 |
| certificate P_n for all n ≥ 4 | PROVED | PD-T?…-313 (PROVED: independent exact check n = 4..16 and symbolic re-derivation by L3-reconstruction-02; fresh reruns and an independently written symbolic check by Codex audit-01 L3-certificates); independent support for n = 4: exact certificate of L3-reconstruction-01 (`padua_n4_generator_cert.py`, a different C ⊥ Hankel) |
| Padua unisolvence for Π_n (needed for sections to be defined) | LITERATURE | Caliari–De Marchi–Vianello / Bos et al. (record bos-dmv-xu-2007, UNVERIFIED there) |

Candidate / claim disposition: mechanism REJECTED: refuted for Padua n ≥ 4 in reading (E) (under the unisolvence assumption). Rejection reason: refuted (within the stated scope; reading (G) not covered).

## Depends on / Checks / Sources

PD-T?…-301, 302, 303, 309, 312, 313; checks as in 313.

## Proof or evidence

PD-T?…-303(e) with p* = P_n.

## Scope / Open items

Dependence of the radius on n (PD-T?…-319, OPEN); whether real rounding errors realise E(P_n) < 0 (for Padua the computed entries are overdetermined, so the sign is not defined at the O(u) level); reading (G) (PD-T?…-300, OPEN).

## History

2026-10-31T23:23+01:00, Claude Opus 5.5 (xhigh, requested), L3 developer, round R05.
- 2026-10-31T23:54:40+01:00, L3 developer: quantifier ε ≤ ε_1 (finding L1 of L3-reconstruction-01, carried over) and the reviewer's independent n = 4 certificate cited.
- 2026-11-01T00:47:14+01:00, L3 developer: finding L11 of L3-reconstruction-02 (reviews/L3-reconstruction-02.md, audited head ae991c1) — original wording of the passages replaced at 2026-10-31T23:54 (round-1 response): «| certificate P_n for all n ≥ 4 | CONDITIONAL | PD-T?…-313 (symbolic-expansion obligation) |»; «for every ε > 0 and every functional E on Π_{2n+1} with ‖E‖ ≤ ε».
- 2026-11-01T00:47:14+01:00, L3 developer (Claude Opus 5.5, xhigh requested): upgrade to PROVED under the stated unisolvence assumption (trusted dependency listed); findings L6 (normalised example), L7 (δ_0(n) → 0) of L3-reconstruction-02 (reviews/L3-reconstruction-02.md, audited head ae991c1). Original wording of the replaced passages: «Overall status: CONDITIONAL.»; «e.g. E = −ε ev_ζ with P_n(ζ) > 0»; «Together with PD-N?…-301: no δ(ε) → 0 exists for any Padua degree n ≥ 3 (CONDITIONAL on the rerun obligations of both files).»; «mechanism REJECTED: refuted for Padua n ≥ 4 (conditional as above).».
- 2026-11-01T08:33:39+01:00, L3 developer (Claude Opus 5.5, xhigh requested): findings LC-M1 (no-uniform-radius inference withdrawn → PD-T?…-319 OPEN), LC-L1 (stale CONDITIONAL status row) of Codex audit-01 (audit-01/L3-certificates.md; candidate 5ccfac2), consolidated item 4 (headline restricted to reading (E); (G) OPEN) and propagation of LF-M1 (residual convention named; normalised factor s_E). Statement of the obstruction itself, its proof and the overall status are unchanged. Original wording of the replaced passages: «# PD-N?bivariate-lanczos-claude-303 — Exact-section (Greenbaum-type) backward interpretation with δ(ε) → 0 fails for Padua points of every degree n ≥ 4»; «any positive measure on K_δ, δ ≤ δ_0(n), has functional distance ≥ |E(P_n)|/‖P_n‖_* from L_μ + E. Together with PD-N?…-301: no δ(ε) → 0 exists for any Padua degree n ≥ 3. The radius δ_0(n) shrinks with n (rigorous reviewer bounds 5.63e-4 … 6.55e-8 for n = 4..12, PD-T?…-313 Open items), so the obstruction is per degree, not uniform in n.»; «Parameter range: Padua points (this family), n ≥ 4, any positive weights, perturbative regime, exact representation or residual < |E(P_n)|/‖P_n‖_*; [IDEALIZED: perturbations given as data]. Not covered: residuals as large as the perturbation; actual floating-point error directions; support beyond δ_0(n).»; «| certificate P_n for all n ≥ 4 | CONDITIONAL | PD-T?…-313 (symbolic-expansion obligation); independent support for n = 4: exact certificate of L3-reconstruction-01 (`padua_n4_generator_cert.py`, a different C ⊥ Hankel) |»; «Candidate / claim disposition: mechanism REJECTED: refuted for Padua n ≥ 4 (under the unisolvence assumption). Rejection reason: refuted.»; «Explicit δ_0(n); whether real rounding errors realise E(P_n) < 0 (for Padua the computed entries are overdetermined, so the sign is not defined at the O(u) level).».
