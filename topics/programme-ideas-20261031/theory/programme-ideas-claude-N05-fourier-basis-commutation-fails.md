# PD-N?programme-ideas-claude-05 — No change of basis makes the truncated sections of the tested trajectory measures commute; the commutator is the boundary-block skew product

ID kind: PD-N.
Aliases: "exact commutation in the Fourier basis" refuted (gen3-1 sub-problem 3); trajectory-measure sections; Lissajous/rhodonea commutators.
Split from: `checks/adversarial-gen3-1.md` (iii), first bullet, at `614709d` (the mechanism refutation); the identity it uses is `PD-T?programme-ideas-claude-03`.
Split into: none.

## Statement

For the sampled trajectory measures tested — rhodonea k = 7, a generic degree-4 trigonometric curve and the Lissajous (5, 6) curve, each sampled at M ∈ {64, 128, 512} equispaced parameter values with equal weights — and degrees n = 1…6 for M = 64 and n = 1…8 for M = 128, 512 [response-02, audit-02 B4.2; earlier wording "n ≤ 8"], the degree-n section pair (H_x, H_y) has ‖[H_x, H_y]‖₂ between 0.08 and 0.50 (relative 0.09–0.71). By PD-T?programme-ideas-claude-03 this norm is the same in every orthonormal basis of the graded Krylov space and under every unitary change of coordinates of ℂ^M, in particular in the Fourier basis. Hence the proposed mechanism "the truncated sections commute (to O(u‖H‖)) in the Fourier basis" fails on all tested instances.

## Definitions

As in PD-T?programme-ideas-claude-03; trajectory measures as in `checks/adversarial-gen3-1.md`.

## Assumptions

The tested curves, sample sizes and degrees above.

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| basis/coordinate invariance of the commutator norm | PROVED | PD-T?programme-ideas-claude-03 |
| nonzero commutators on the tested instances | MEASURED | `checks/code/adv/gen3-1/commutator_sections.py`, `commutator_out.txt` (equality with ‖B_xᵀB_y − B_yᵀB_x‖₂ to ≤ 8e-15, except the generic degree-4 curve at n = 8, where conditioning raises the discrepancy to ≤ 2e-12 [response-02, audit-02 B4.2]; identical after mapping to the Fourier basis); independent QR replay by the Codex audit for rhodonea-7, M = 64 (norms 0.25, 0.375, 0.0833333, 0.2414547 at degrees 1–4) |

Candidate / claim disposition: the mechanism of gen3-draft-1 sub-problem 3 (IDEA?programme-ideas-claude-11) is REJECTED.
Rejection reason: refuted within the tested scope (its negation — the sections do not commute in the Fourier basis — is MEASURED on every tested instance, and no change of basis can alter it).

## Negative-result scope (PD-N only)

Attempted mechanism: exact (or O(u)) commutation of truncated sections of trajectory measures in the Fourier basis (IDEA?programme-ideas-claude-11, sub-problem 3).
Parameter range: the curves, M and n listed (n = 1…6 at M = 64; n = 1…8 at M = 128, 512). **Not covered:** a claim that the commutator is nonzero for every proper Krylov space (false in general, e.g. Y = cI); non-uniform or weighted time sampling (a different candidate).

## Depends on

PD-T?programme-ideas-claude-03.

## Checks

`python checks/code/adv/gen3-1/commutator_sections.py > checks/code/adv/gen3-1/commutator_out.txt` (frozen at `614709d`); audit replay `audit-support/rejections-check.py/.json`.

## Sources

None.

## Proof or evidence

Invariance by PD-T?…-03; nonzero values MEASURED as tabulated. The draft's own pre-registered kill criterion (sections not commuting to O(u‖H‖) in the Fourier basis) fires.

## Scope

The tested trajectory measures only.

## Open items

None.

## History

- 2026-11-01, gen3-1 adversarial agent (claude-fable-5-1, xhigh): mechanism refuted; nonvanishing clause over-generalised.
- 2026-11-01, Codex audit-01 A9.5: clause withdrawn; refutation and numbers confirmed.
- 2026-11-01, response-01 addendum (claude-opus-5-5), at AC's instruction "register negative results": registered as this MEASURED PD-N.
