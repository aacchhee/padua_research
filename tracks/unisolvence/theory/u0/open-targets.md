# PD-T011 — Unverified source extensions beyond bounded U0 registration

ID kind: PD-T. Aliases: ideal/recurrence transfer, arbitrary-length fast-transform bound.
Split from: supplied finite_field_padua.md Theorems 4–5.
Split into: none. Independently established core results have their own IDs `PD-T004–PD-T008` and do not change this target's status.

## Statement

Two remaining supplied universal assertions are registered as verification targets:

1. For every `n>=1` in good characteristic, the stated `n+2` vanishing polynomials generate the canonical Padua ideal, are an H-basis and a Gröbner basis for every degree-compatible order; their stated reduction rules give multiplication matrices with at most two nonzero entries per column and the stated weighted symmetry.
2. For every admissible finite field and every `n>=1`, the finite-field DCT-I construction admits evaluation and interpolation in `O(n² log n loglog n)` field operations for arbitrary transform lengths, with the required root extensions and convolution arithmetic cost included.

## Definitions and assumptions

Target 1 uses the precise polynomials and reduction rules in the supplied note §2 Theorem 4, reproduced unchanged in committed `input-code/ff_padua/padua_ff.py`. Target 2 is the note's unrestricted-length complexity assertion, not the supplied implementation's mixed-radix cost `O(n² times sum of prime factors)` or its finite timing table.

## Status by part

Overall status: **OPEN** as local verification targets.

| Part | Status | Missing obligation |
|---|---|---|
| Ideal/H-basis/recurrence universal statement | OPEN | Full explicit algebraic proof and independent reconstruction; finite code checks only are retained in `PD-T009` |
| Arbitrary-length complexity statement | OPEN | Cost model, necessary extension-degree/root availability, exact convolution algorithm and proved operation count; supplied code has quadratic prime-length DFT leaves |

Disposition: deferred after bounded quick registration, not rejected. Neither a failed proof nor refutation is claimed. No PD-N is warranted.

## Depends on

Definitions and good-characteristic unisolvence in `PD-T004`. The target 2 baseline must compare with `LIT-011`, `LIT-012`, `LIT-013`; these literature records remain secondary/unverified here.

## Checks and sources

The source finite checks were actually reproduced, but do not close these universal targets. No additional targeted run or proof development is claimed. Source provenance: `LIT-025`, supplied note Theorems 4–5. Original-source priority and a complete duplicate screen remain pending.

## Scope and next unresolved steps

For target 1, first prove the displayed relations vanish identically on the root-of-unity parameterization, then establish ideal equality by a normal-form/dimension argument and verify every boundary reduction. For target 2, write the exact convolution/root-of-unity assumptions before comparing asymptotics. These are concrete handoffs, outside further U0 development in this bounded registration.

The independent adversary's `q=7` all-code optimality bound is handed separately to the orchestrator; it is not included in these OPEN targets or silently inherited as proved. General decoding and weight distributions are deferred candidates, not registered conjectures.

## History

2026-10-31, Codex U0, assigned `gpt-6.1-sol xhigh`; rules/base `d36722823441dc40c6e19d69a174459348dd309c`. Preserved exact unverified source extensions without letting them weaken the separate proved core or pretending that finite measurements settle them.
