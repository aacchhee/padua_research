# PD-N?padua-xu-lebesgue-20261114-claude-35 — the unshifted lattice does not maximise the shifted-lattice sum Ξ_n (pointwise "shift rigidity" fails)

ID kind: PD-N.
Aliases: X2-N35; shift rigidity; J(ψ) is not maximal at ψ = 0.
Split from: none.
Split into: none.

## Statement

MEASURED (float64, scope under Checks). For M = n + 2 ∈ {62, 102, 202} there are shifts (a₁, a₂) with Ξ_n(a₁, a₂) > Ξ_n(0, 0) = λ_n(1,1) (Ξ_n as in X2-34): at (a₁, a₂) = (0.9/M, −0.9/M), Ξ_n(a)/Ξ_n(0) = 1.0796 for M = 202 (Ξ_n(a)/M² = 0.5553 against Ξ_n(0)/M² = 0.5144).

Heuristic limit (derivation in `attempts/X2-round3.md` §4; OPEN as a theorem, MEASURED agreement): Ξ_n(φ₁/M, φ₂/M)/M² → |cos((φ₁+φ₂)/2)|·J((φ₂−φ₁)/2), with
J(ψ) := (4/π)∫_𝒮 |sin 2τ sin τ|·κ(τ + ψ) dτ, 𝒮 := ∪_{j∈ℤ}(jπ, jπ + π/2), κ(x) := |sin x − x cos x|/|x|³,
a π-periodic function with J(0) = c* and (quadrature) max J ≈ 0.56058 at ψ ≈ −0.92, min J ≈ 0.47741 at ψ ≈ 0.64.

Consequence: the mechanism "Λ_n ≤ sup_a Ξ_n(a) and sup_a Ξ_n(a) = Ξ_n(0)" cannot prove Λ_n = λ_n(1,1), nor lim Λ_n/n² = c*. The averaged bound X2-34 (b) is not affected: it involves symmetric box means of Ξ_n, for which the linear term cancels.

## Definitions

As in X2-34.

## Assumptions

None beyond the definitions; finite scope.

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Ξ_n(a) > Ξ_n(0) at the listed shifts and M | MEASURED (float64; closed form of G̃ checked against the double sum to 3.6e−14) | a ball-arithmetic certificate at one n would make it PROVED at that n; not done |
| limit formula with J | OPEN (heuristic); MEASURED agreement within 0.006 at M = 202 on 10 shifts and a 13-point scan | no proof |
| max J > c* | MEASURED (quadrature, error estimated < 1e−5) | — |

Candidate / claim disposition: REJECTED (the mechanism below).
Rejection reason: failed (measured within the stated scope).

## Negative-result scope (PD-N only)

Attempted mechanism: bound λ_n(P) by the supremum over shifts of Ξ_n (Jensen applied to the translation formula X2-34 (a) before averaging) and show that the supremum is attained at the zero shift.
Parameter range: M ∈ {62, 102, 202}, shifts of size ≤ π/M; measured failure only, not a universal refutation.

## Depends on

X2-34 (definition of Ξ_n).

## Checks

- `python3 code/mp/research/x2r3_checks.py shift` (float64; 2026-11-14; 10 s). M = 202, (Mφ₁, Mφ₂) ↦ Ξ/M² [heuristic]: (0,0) 0.5144 [0.5170]; (0.9,−0.9) 0.5553 [0.5606]; (−0.9,0.9) 0.4837 [0.4843]; (1.8,0) 0.3404 [0.3485]; (0,1.8) 0.2939 [0.3010]; (0.6,0.6) 0.4200 [0.4267]; (−0.6,0.6) 0.4774 [0.4777]; (π,π) 0.5071 [0.5170]; (π,0) 0.0047 [0]; (0,π) 0.0079 [0]. Scan Ξ(s/M, −s/M)/M² against J(−s), s = −1.5…1.5: agreement within 0.006. `Jmax_on_grid` 0.560585, `Jmin_on_grid` 0.477408, `J(0)` 0.516954.
- Independent rerun: done in audit-01 §2.1 (R1–R8): the auditor's ball-arithmetic certificate of Ξ_n(a)/Ξ_n(0) > 1 at M = 62, 102, 202 is in `evidence/audit-x2-separate-path.json` (see the dated note under Checks). Per-record verdict: audit-01 §6.
- 2026-11-14 (orchestrator, response to audit-01 A-m5; status unchanged, MEASURED): accuracy note and the missing M = 62, 102 values. (i) The developer's float64 closed form of G̃ cancels catastrophically near x = y. At M = 102 the recorded ratio Ξ_n(a)/Ξ_n(0) = 1.0752491 (`evidence/mp-x2r3_checks_b.json`, shift rows) differs from the certified 1.0752352 ± 2.6e−8. Per audit-01 A-m5 the cause is the node (p,q) = (43,44), where x − y = −4.3e−6 and the float64 closed form gives 72661.5 against a true G̃ = 72566.1 (auditor's finding; not re-derived here). The conclusion Ξ_n(a) > Ξ_n(0) is unaffected. (ii) The Statement lists M ∈ {62, 102, 202}, while the Checks above quote only M = 202. The developer's float64 values at a = (0.9/M, −0.9/M) are in `evidence/mp-x2r3_checks_b.json`: Ξ_n(a)/M² = 0.543423 (M = 62), 0.550158 (M = 102), 0.555322 (M = 202) and Ξ_n(a)/Ξ_n(0) = 1.0698576, 1.0752491, 1.0796016. (iii) Ball-arithmetic values from the defining sums for G̃ (auditor's script `code/audit/audit_x2_misc.py xi`, committed output `evidence/audit-x2-separate-path.json`, section `xi_certificate`): Ξ_n(0) = 1952.52004567117 ± 3.8e−13 (= λ_60(1,1)), 5323.27284670304 ± 2.3e−12 (= λ_100(1,1)), 20988.6274884779 ± 1.3e−11; Ξ_n(a)/Ξ_n(0) = 1.0698576 ± 3.9e−8 (M = 62), 1.0752352 ± 2.6e−8 (M = 102), 1.0796015 ± 4.8e−8 (M = 202), each flagged `certified_Xi_shift_gt_Xi0: true`. The status of this record stays MEASURED (the Statement is the developer's float64 claim); upgrading it to PROVED at these M (audit-01 n2) would be a status change and is not taken here.

## Sources

None.

2026-11-14 (orchestrator, response to audit-01 A-m1): this record is the Morrow–Patterson variant of IDEA-316 (shifted-lattice primitive maximal at the coset), which PD-N079 refutes for the Padua primitive for every fixed n ≥ 3 (see also IDEA-333). The MP kernel differs (Ξ_n is built from G̃ with absolute values on the MP lattice), so PD-N079 does not transfer and the test here was legitimate; the result is REJECTED: failed, with MEASURED scope as stated above. See `novelty-gate-X2.md`, Round X2-3 addendum, row X2-R3-C3.

## Proof or evidence

Measured evidence only.

## Scope

A measured failure of one mechanism. It says nothing against the target Λ_n = λ_n(±1,1).

## Open items

Certificate at one n (cheap; ball arithmetic of a finite sum). Proof of the limit formula (part of item W in the X2-28 addendum).

## History

- 2026-11-14, Claude Fable 5.2 (xhigh), researcher subagent of round X2-3; uncommitted at writing. First version.
