# PD-T?charter-u0-codex-02 — Rationality and the four Padua torus sign types

ID kind: PD-T. Aliases: field-validity dictionary, split/nonsplit axes.
Split from: supplied finite_field_padua.md §1.
Split into: none.

## Statement

For `n>=1`, `q` an odd prime power of characteristic not dividing `n(n+1)`, and the canonical set of [gram-unisolvence.md](gram-unisolvence.md), all coordinates lie in `F_q` if and only if

`q congruent +/-1 modulo 2n` and `q congruent +/-1 modulo 2(n+1)`.

The set is independent of the primitive roots chosen. For `n>=2`, the four sign choices give the four distinct residue classes modulo `M=2n(n+1)` below. At `n=1`, the x signs coincide modulo `2`, leaving only two distinct classes modulo `4`.

| x sign | y sign | residue modulo M |
|---|---|---|
| + | + | 1 |
| + | - | 2n+1 |
| - | + | 2n²-1 |
| - | - | -1 |

In the `+` case the axis roots lie in `F_q^*`; in the `-` case they lie in the norm-one subgroup of `F_(q²)^*`. When the sign is ambiguous at order `2`, both descriptions apply. Every admissible `q` is at least `2n+1`; equality is admissible whenever `2n+1` is a prime power.

## Definitions and assumptions

All nodes means every node of the canonical set, rather than a subset of rational points. Its two projections contain every node on their respective axes: for every fixed index, the other axis has an index of matching parity.

## Status by part

Overall status: **PROVED** (developer proof; independent acceptance PENDING). No rejected candidate or novelty claim.

## Depends on

Definitions in `PD-T?charter-u0-codex-01`; basic finite-field Frobenius arithmetic.

## Proof

For a root `rho` of exact order `L=2m`, the element `c=(rho+rho^-1)/2` is fixed by Frobenius exactly when `rho^q+rho^-q=rho+rho^-1`. The two roots of `t²-2ct+1` are `rho,rho^-1`; thus this happens exactly when `rho^q=rho` or `rho^q=rho^-1`, equivalently `q congruent +/-1 mod L`. In either case all axis nodes are fixed by Frobenius. Necessity for the full Padua set follows because each axis node, in particular the index-one node, occurs in a projection. This also handles `m=1`, when the roots are already `+/-1`.

The intrinsic set is the image of `{(u,v):u^(2n)=v^(2n+2)=1, u^n=v^(n+1)}` under `(u,v)->((u+u^-1)/2,(v+v^-1)/2)`. Each inverse-pair has a representative among the half-axis indices, and its `n`-th or `(n+1)`-th power is its parity sign. This description proves primitive-root independence.

The two moduli have gcd `2`, and every choice of the odd residues `+/-1` agrees modulo `2`. The elementary Chinese remainder theorem therefore gives one residue modulo `M` for each sign pair. Direct substitution verifies the displayed values. If `n>=2`, both moduli are at least `4`, so their `+` and `-` residues differ, giving four distinct classes. For `n=1`, the two x residues agree and the table collapses as stated.

If `rho^q=rho^-1`, then `rho^(q+1)=1` and `rho^(q²)=rho`, the norm-one description; the positive sign gives `rho^(q-1)=1`. Finally `2(n+1)` divides either `q-1` or `q+1`, so `q+1>=2(n+1)` and `q>=2n+1`. At equality, the congruences are `q=1 mod 2n`, `q=-1 mod 2n+2`; its characteristic cannot divide `n(n+1)` because `2n=-1` and `2(n+1)=1` in that characteristic.

## Checks and sources

Read supplied §1 and secondary predecessor records `LIT?charter-unisolvence-codex-02,14,15`; no original literature proof is a dependency. The source `padua_ff.py` cannot construct every good-characteristic set, because it only implements `F_p` and `F_(p²)`; absence from that implementation is not nonexistence in the algebraic closure. It checks 76 admissible prime cases and one partial-rationality example. See [measurements.md](measurements.md).

## Scope and open items

This establishes the exact finite-field rationality criterion, not arbitrary extension-degree complexity. The source already notes the `n=1` degeneration; it is not a counterexample to an intended four-type statement. No PD-N is warranted. Independent audit pending.

## History

2026-10-31, Codex U0; rules/base `d36722823441dc40c6e19d69a174459348dd309c`; assigned `gpt-6.1-sol xhigh`. Explicitly separated algebraic-closure existence from `F_q`-rationality and prime-only code coverage.
