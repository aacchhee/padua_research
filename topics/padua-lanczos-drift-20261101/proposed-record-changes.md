# Literal proposed upstream record changes

Rules/base read at cf89b140530d5838bdb208a8c28f3e7aa676ace3; synchronized main806cc7b4509fd93bae652f9545d32d95529f8281. **Not applied.** Existing theory files stay byte-identical to main. Apply only at PR preparation after the Claude audit, refreshed reservations and final-ID mappings. The blocks below are literal replacements against the current original files, not paraphrases. Provisional IDs must be mapped without changing scientific scope. Reserved ranges live in the shared batch ledger; no final IDs are assigned here.

## PD-T055: retain OPEN; add quantified scope distinctions

Target: `tracks/bivariate-lanczos/theory/bj-universal-reorthogonalization-obstruction-open.md`.

OLD
```text
## Open items
```

NEW
```text
## Later independent results (original target remains OPEN)

PD-N?drift-codex-14 refutes only a pathwise positive lower bound for every model-admissible error realization when the zero-error exact-real run is admitted. It does not refute literal working-precision storage or a fixed IEEE implementation. PD-N?drift-codex-15 gives a ten-point triangle, exact prefix, fixed degree-two BJ products and one aggregate source for which every prior-vector subtraction rule leaves the same drifted span and a nonzero J-closure defect. Its conclusion is O(u), not exponential, and neither implicit-section in-span error nor scalar-operation realizability follows. A final formalization must distinguish every-error, worst-case-error and deterministic-IEEE quantifiers. (U) remains OPEN.

## Open items
```

## PD-T056: retain OPEN; record concrete square-case test

Target: `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-300-l3q1-backward-interpretation-target.md`.

OLD
```text
## Open items
```

NEW
```text
## Independent residual-aware square-case example

PD-T?drift-codex-31 gives an explicit n=1 square family with moment-infinity perturbation epsilon, exact positive noncommuting sections, support upper sqrt(6epsilon), and residual-aware lower sqrt((1-3gamma)epsilon/3) for unit-mass fits with gamma<1/3. This is reading (E): no recurrence realization with local error u=o(epsilon) is proved. Reading (G), including Padua n=3/4, remains OPEN. The original measure fits at residual epsilon and radius zero.

## Open items
```

## PD-T075: proposed status by the original two-question decomposition

Target: `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-319-padua-obstruction-radius-uniformity.md`.

OLD
```text
Overall status: OPEN.
```

NEW
```text
Overall status: PARTIAL: original subquestion (U1) is PROVED in split result PD-T?drift-codex-30; original subquestion (U2) remains OPEN. This is a decomposition of the original target, not aggregation with a supporting lemma.
```

## PD-T075(U1): exact row replacement

Target: `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-319-padua-obstruction-radius-uniformity.md`.

OLD
```text
| (U1) ρ_n → 0 | OPEN | reviewer-certified lower bounds and floating samples below; no all-n argument |
```

NEW
```text
| (U1) ρ_n → 0 | PROVED | PD-T?drift-codex-30: explicit eventual negative witness gives rho_n=O(n^-5) and limsup n^5 rho_n <=20sqrt(2)pi^4/9; analytic proof independently reconstructed |
```

## PD-T075: replace absent-proof paragraph, keep U2 OPEN

Target: `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-319-padua-obstruction-radius-uniformity.md`.

OLD
```text
## Proof or evidence

No proof. The routine facts follow from the definitions.
```

NEW
```text
## Proof or evidence

(U1) is proved in split result PD-T?drift-codex-30 by zeta_n=(cos(pi/n+a/n^4),cos(pi/(n+1)+a/n^4)), a=20pi^3/9: n^14 P_n(zeta_n) tends to -6400pi^12/729 and n^5 times its distance to the (1,1) node tends to 20sqrt(2)pi^4/9. No matching lower rate or explicit finite negativity threshold is claimed. (U2) stays OPEN. In particular rho_n<=delta_obs(n), so this upper bound for rho_n does not upper-bound delta_obs(n) or disprove a uniform obstruction radius. The earlier certified lower bounds and sampled measurements remain historical evidence, not the proof of decay.
```

## PD-N013: retain MEASURED; add actual-code ordering/fit evidence

Target: `tracks/bivariate-lanczos/theory/reorthogonalization-does-not-restore-graded-spaces.md`.

OLD
```text
## Open items
```

NEW
```text
## Independent public-code extension (MEASURED)

PD-T?drift-codex-50 executes actual polyrat 0.2.2 numerical source at commit6903d7af9995c9d88e661fb229626696e00fdfba on the frozen suite. Upstream input [y,x] matches campaign dev including column order; default [x,y] is mirror with reversed within-degree order and is not numerically equivalent to forward mirror. Separate root execution reproduces the rotated-square n24 gap0.004105 and triangle n20 gap0.010164. Post-hoc worst-polynomial fit residuals match those gaps, while independently fixed exp(x+y) is fit near machine precision. Ill-conditioned/rank-deficient references elsewhere do not certify span drift. This is additional scoped measurement, not an upgrade of this negative result or a proof of every-rule failure. The scalar-operation and aggregate sensitivity statements in the new E1 records remain separately scoped.

## Open items
```

## PD-N015: retain MEASURED; add actual-code ordering/fit evidence

Target: `tracks/bivariate-lanczos/theory/one-relation-selections-do-not-keep-spans-near-Sn.md`.

OLD
```text
## Open items
```

NEW
```text
## Independent public-code extension (MEASURED)

PD-T?drift-codex-50 executes actual polyrat 0.2.2 numerical source at commit6903d7af9995c9d88e661fb229626696e00fdfba on the frozen suite. Upstream input [y,x] matches campaign dev including column order; default [x,y] is mirror with reversed within-degree order and is not numerically equivalent to forward mirror. Separate root execution reproduces the rotated-square n24 gap0.004105 and triangle n20 gap0.010164. Post-hoc worst-polynomial fit residuals match those gaps, while independently fixed exp(x+y) is fit near machine precision. Ill-conditioned/rank-deficient references elsewhere do not certify span drift. This is additional scoped measurement, not an upgrade of this negative result or a proof of every-rule failure. The scalar-operation and aggregate sensitivity statements in the new E1 records remain separately scoped.

## Open items
```

## Preparation and external results

At preparation also update the corresponding PROOF_STATUS rows, split crosswalk, IDEA dispositions and topic indexes, after checking the exact audited source snapshot. Final-ID assignment is still pending. PD-T075 needs a recorded original-to-split mapping for its solved U1; retain original wording/history. The other original target statuses remain unchanged.

Intended local results file: C:\Users\andreyac\Downloads\padua\results\padua-lanczos-drift-20261101.md. No bridge/write is claimed; the intended entry is in LOG Runs needed. Shared RESULTS.md must preserve other topic sections and use the required modification-time guard when actual access exists.
