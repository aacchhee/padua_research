# PD-N?padua-3d-codex-T2-02 — Finite normalized cyclic rank screen

ID kind: PD-N. Aliases: odd cyclic M39 null cover; normalized z1=1 diagnosis. Split from: none. Split into: finite quality separately in t2-finite-survivors.md.

## Statement

For n=3, N=20, M=39, every integer generator z=(1,b,c) with 1≤b<c≤19 gives a singular product-Chebyshev evaluation on Π₃ at the twenty folded cyclic cosine nodes defined in T3-01. All171 generators have explicit nonzero rational Π₃ null polynomials. No degree3 generator in this slice can supply an all-degree unisolvent family.

## Definitions / assumptions

Nodes (cos(2πk/M),cos(2πkb/M),cos(2πkc/M)), k=0,...,19. First coordinate distinct, so cardinality20 is exact before rank screening. Signs of b,c do not change their cosines; swapping b,c is a coordinate permutation. Equal b=c or b=0 gives an immediate linear annihilator and is outside the enumerated strict positive slice. Cases with neither a unit coordinate nor first coordinate1 require a separate argument; this record does not silently cover them.

## Status by part

Overall status: MEASURED exact finite screen, computer-proof acceptance pending independent checker execution. Candidate disposition: REJECTED: failed only for an every-degree rule that uses this normalized odd-cyclic slice at n3. Even-degree subsequences and other orders/phases remain OPEN.

## Negative-result scope

Attempted mechanism: IDEA?padua-3d-codex-T2-01 as the subsequently preregistered exhaustive normalized generator class, not only the three killed formulas. n3 only; no all-large-n obstruction.

## Depends on

Canonical [PD-T?padua-3d-codex-T3-01](t3-cyclic-rank.md); its T2 specialization in t2-cyclic-dictionary.md. No generic-axis rank theorem is substituted for the algebraic specialization.

## Finite reduction and exact evidence

The normalized search space is exactly the171 pairs from combinations({1,...,19},2). The committed8,054-byte evidence/t2-n3-null-cover.json lists each pair once, an observed rank, and a primitive integer coefficient vector indexed by total-degree Chebyshev modes. The standalone checker code/t2_check_cover.py checks exact coverage, nonzero coefficients, distinct valid modes of total degree≤3, and vanishing Laurent remainder for each polynomial: expand each product Chebyshev mode using eight sign choices, reduce exponents modulo39, and add coefficient integers in Z[t,t^{-1}]/(t^39−1). Every one of the39 remainder coefficients must vanish. Hence substitution t=e^{2πik/39} proves that nonzero polynomial vanishes at every node. The untrusted recorded ranks are explicitly excluded from checker acceptance: the null witnesses alone suffice for singularity.

The full exact-rank screen separately reports max19/20 at n3. More detailed rank distributions are MEASURED and have no universal content.

## Checks

Developer executed:

- OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/t2_generators.py
- python topics/padua-3d-20261106/code/t2_check_cover.py

Evidence receipts: t2-generators.json and t2-cover-check.json. The latter checks every171 exact Laurent remainder with a separately implemented full-exponent method (producer uses folded cosine rows). This is same-agent execution, not independent rerun. The proof-essential null cover and checker are committed and require no large scratch retrieval. Large rank catalogues for n2/3/4 are reproducible off-repository, with SHA256 and lengths in the compact generator receipt.

## Sources / scope / open items

No literature theorem used. Independent execution required before PROVED computer-assisted status. T3 may extend the normalized class by unit reparameterization and short-axis arguments; that is a different record. Higher-degree even subsequences, rational phases and unions remain OPEN. Resume positive work only for a concrete separated correction that both removes displayed nulls and addresses the n4 quality deficit.

## History

2026-11-06; all pair domains/rank methods preregistered after fixed-formula kills and before exhaustive screen. Actual developer model gpt-6.1-sol medium. Rules ccd9e905d19c0c625c196c4a3f3e707058ed042a. Canonical dictionary consolidated with T3-01, no duplicate PD-T.
