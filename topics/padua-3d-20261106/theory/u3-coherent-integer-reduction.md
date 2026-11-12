# PD-T?padua-3d-20261106-codex-U3-02 — coherent half-cosets have integer rank dictionaries

ID kind: PD-T. Aliases: rephased coherent Fourier matrix; half-group phases.
Split from: none. Split into: none. No final ID allocated.

## Statement

Let H be a finite subgroup of T^d, L=H^perp in Z^d, and a a real phase
such that2a belongs to H. For any finite set of multi-indices I, form
product-Chebyshev evaluation on the distinct nodes cos(2pi(a+H)).
Its real rank equals the rational rank of an explicit integer matrix.
For each character class r in Z^d/L choose any integer representative
rho_r. Define

    D[r,alpha]=sum_(epsilon:epsilon*alpha∈rho_r+L)
                (−1)^[2a·(epsilon*alpha−rho_r)].

The exponent is an integer. Thus exact rational elimination decides
both positive and deficient ranks without a modular upper-bound inference.

## Definitions and assumptions

Angles are in turns, cosine coordinatewise. Signs at zero exponents are
repeated in the sum. A chosen representative need not occur among the
signed frequencies. H may be cyclic or noncyclic; no no-fold hypothesis.
The statement concerns a single coherent coset, not an arbitrary union
with unrelated257-denominator phases.

## Status by part

Overall status: **PROVED**, direct reduction below. Finite classifications
that use the reduction are separate computer-assisted claims.
Candidate disposition: retained exact tool; no novelty/priority claim.

## Depends on

[General-H character factorization](t7-general-character.md), read in full.
Only finite Fourier invertibility is used; its proof is written there.

## Proof

For u in L and2a in H, u·2a is an integer, proving integrality of each
exponent. In the general-H Fourier coefficient matrix B the contribution
of signed frequency beta in character class r is exp(2pi i beta·a).
Factor the common nonzero row scalar exp(2pi i rho_r·a). Its quotient is

    exp(2pi i(beta−rho_r)·a)=(−1)^[2a·(beta−rho_r)].

After this invertible diagonal row operation B becomes exactly D.
The general-H Fourier factorization gives rank_C(B)=rank_R(evaluation),
including repeated cosine rows, because the Fourier matrix is invertible
and deleting repeated evaluation rows preserves the kernel. Since D has
integer entries, its complex, real and rational ranks coincide by the
minor criterion. This proves the statement.

For U3-F, H has generators h1=(1/a,0,r/a),h2=(1/b,1/b,s/b)
with a|b. The exact embedding is injective, because second coordinate
identifies v mod b and first-minus-second then identifies u mod a.
Characters are the pairs(f1 mod a,f2 mod b), where
f1=beta_x+r beta_z, f2=beta_x+beta_y+s beta_z. For phase
(e1 h1+e2 h2)/2, the displayed general sign becomes

    (−1)^[e1(f1−f10)/a+e2(f2−f20)/b],

using any row-reference pair(f10,f20) with the same residues. All divisions
are exact integers, including negative frequencies. Replacing a row by
a nonzero rational multiple and deleting duplicate/zero rows also preserves
rank, justifying the finite checker's row normalization and cache.

## Checks, sources and scope

The exact-completion protocol is appended prospectively in
[usable3](../usable3.md). Frozen original source/receipts remain unchanged;
new code is [u3_folded_exact.py](../code/u3_folded_exact.py). Its execution
and independent integer-rank reconstruction are separate obligations for
the finite classification, not for this analytic statement. No external
source theorem, cubature premise, numerical agreement or deficient modular
rank is used. The conclusion proves neither a norm bound nor a cubature rule.

## Open items and history

Use the reduction to complete the exact same registered U3-F finite universe.
Arbitrary free phases generally yield noninteger coefficient ratios and are
outside this reduction. 2026-11-07, Codex mathematical developer assigned
gpt-6.1-sol xhigh, rules/input38227202bc6908d5a5a874950145761a8ca4312f.
The checker independently reconstructed the canonical-residue version before
the new exact run; only executed evidence will establish its finite coverage.
