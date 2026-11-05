# PD-T?nn-mop-stability-codex-32 — native direct-solve comparison

ID kind: PD-T. Aliases: orthobasis whole-triangle bake-off; node-space QR.
Split from: none. Split into: none.

## Statement and status

Overall status: **MEASURED**. Two explicit whole-triangle native NN designs
(direct orthobasis mixed systems A, and node-space constraint QR B) were
implemented and tested at N4/8/12/16/24/32 on both frozen rational families.
A was tested with LU, pivoted QR and untruncated SVD. All48 outputs were
finite. Relative field sup errors against the frozen 220-digit C4 reference
are tabulated in [attempts/D3.md](../attempts/D3.md). Reference 140/220
agreement was below1e-60 in every case; N4 exact defining-system checks
were executed. No stability theorem or novelty claim.

The native LU comparison gains2.78digits at KrawN8 (E3.09634e-12 versus
1.87057e-9) and2.79 at HahnN8 (E4.23819e-10 versus2.61430e-7).
Native nodeqr gains2.96 at HahnN8 (E2.84468e-10). Both algorithms gain
over2digits at N16 on both families, hence neither hits G4's stated kill.
Some N24/32 variants are worse. Gains on one finite problem do not prove
a general method bound.

## Definitions and assumptions

Exact input family convention and forward metric E are PD-T290's frozen
ones. Input rounding occurs in binary64; reference input starts as exact
Fractions. At every nu with s=|nu|<N use R_nu=gamma_s P_nu expressed in
a common uniform discrete orthonormal basis phi_s of leading gamma_s.
Only coefficient output through degree N-1 is requested. A formal final
phi_N proportional to the node polynomial supplies the terminal extension;
its lower coordinates vanish. No division by terminal d occurs.

## Algorithm identity (routine exact check, not a numerical theorem)

For any exact degree-ordered basis, invertible changes of the polynomial
and test bases transform the defining mixed systems of PD-T286 without
changing their solutions. Row scaling or an orthonormal basis for the
complete node constraint row space likewise preserves the nullspace.
Thus A and B are defining-system reformulations in exact arithmetic.
For t_s=gamma_(s-1)/gamma_s, multiplication gives

    x R_nu-t_(s+1)R_(nu+ej)
      = b_(nu,j) R_nu + sum_h (a_(nu,h)/t_s) R_(nu-eh).

The leading degree-s coordinate determines b; normality gives independent
predecessors, so the remaining coefficients are uniquely determined by
the lower-coordinate solve. The two directions have the same a in exact
arithmetic. Averaging the computed estimates is only a numerical choice.
This identity explains the implementation's scales; it does not bound its
rounding error. The uniform-basis recurrence is implemented explicitly;
its orthogonality residual is reported as a diagnostic.

## Depends on, checks and sources

PD-T286 and the frozen input/code of PD-T290. Producer
`code/native_mixed.py`; all commands/hashes/environment and raw-output
identities are in D3. Known moment, QR and node-value formulations are
predecessors, not claimed new ideas. LIT-347 §4.4 is known here through
the pinned repository assessment only; no fresh primary comparison or
external public-code experiment is claimed.

Independent whole-array exact-Fraction reference comparisons were assigned
separately. Their actual executed receipt must be linked before independent
verification is claimed; a developer's reference check is not that rerun.

## Scope and open items

The imported D1 kappa places the N8 gains in attainable precision regimes;
it does not make these algorithms weakly stable at all sizes. Path recovery
is separately measured and is not full NN backward error. A full-data
feasible witness has both a data perturbation and coefficient correction,
and may be worse than choosing the original input. A certified nearest
projection and any full rounding theorem remain OPEN.

## History

2026-11-05, Codex requested gpt-6.1-sol xhigh; source/rules
823cf6a4ef7c01b4ef3d2a6fec3e9f19d4b4f6f1. A's initial exploratory runs
fixed two programming errors (empty-array scalar handling and a duplicate
metadata key) before successful output. No result uses those failed runs.
Later additions only added warning counts, exact N4 check, input identities
and the separately pre-registered B factorization.
