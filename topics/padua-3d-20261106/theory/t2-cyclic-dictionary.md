# T2 verification/specialization note — exact folded cosine dictionary

Verification note, no separate mathematical result ID. Historical provisional alias PD-T?padua-3d-codex-T2-01 consolidated into canonical T3-01 (not rejected). Aliases: signed-frequency reduction; actual Chebyshev-specialization rank.

## Statement

For every n≥1, N=binom(n+3,3), M=2N−1 and integer vector z=(1,b,c), define X(z) as the cosine image of the cyclic subgroup {kz/M:k∈Z/M}, retaining representatives k=0,...,N−1. Then |X(z)|=N. Let A={a∈N₀³:|a|≤n}. For r=0,...,N−1 and a∈A, set D[r,a] to the number of ε∈{−1,1}³ such that ±(ε₁a₁z₁+ε₂a₂z₂+ε₃a₃z₃)≡r mod M (where the ± means fold to the representative min(s mod M,−s mod M), not double counting). The total-degree product-Chebyshev evaluation matrix has the same rank over R as the integer matrix D has over Q.

Consequently a nonzero determinant of D modulo any prime proves unisolvence of the actual algebraic-cosine nodes. An integer nullvector Dv=0 proves singularity at those same nodes. A deficient modular rank alone proves neither singularity nor an upper bound for rational rank.

## Definitions and assumptions

T_j(cos θ)=cos(jθ), including T₀=1. There are eight signs even when some components a_j vanish: multiplicities are retained. V[k,a]=∏T_{a_j}(cos(2πkz_j/M)). C[k,r]=cos(2πkr/M). No generic axes, random data, orthogonality, or positive cubature hypothesis.

## Status by part

Canonical mathematical claim: [PD-T?padua-3d-codex-T3-01](t3-cyclic-rank.md). This note records the exact specialization implemented by T2 and its verification obligations; no separate PD-T status or allocation. Finite checker outputs retain their separate MEASURED records until independent replay. No historical novelty claim.

## Proof

For k=0,...,N−1, θ_k=2πk/M is strictly increasing in [0,π). Thus x_k=cos θ_k are distinct; first coordinates alone give exactly N nodes. Conversely the remaining M parameter values fold by k↔M−k to those representatives because every coordinate is an unshifted integer-frequency cosine.

The exponential identity cos u=(e^{iu}+e^{−iu})/2 gives
∏_{j=1}³cos(a_jz_jθ)=1/8 ∑_{ε∈{±1}³}exp(i(ε·(a*z))θ).
Pairing ε and −ε shows the imaginary sum vanishes; replacing each exponential sum by the corresponding cosine sum leaves the same factor1/8. At θ=θ_k, frequencies reduce modulo M and cosine identifies r and −r. Therefore V=(1/8)CD exactly. C is the evaluation of T₀,...,T_{N−1} at N distinct real numbers x_k; these polynomials have degrees0,...,N−1 and nonzero leading coefficients. The polynomial root bound proves C invertible. Multiplication by C/8 preserves rank, and rational versus real rank of an integer matrix agree because ranks are characterized by nonzero integer minors. Reduction mod a prime sends zero integer determinants to zero, so a nonzero residue proves a nonzero integer determinant. Finally Dv=0 implies Vv=0 and a nonzero Chebyshev coefficient vector defines a nonzero polynomial.

## Root-of-unity dictionary for direct checks

Use R=Z[ζ_M,1/2], with a primitive complex Mth root ζ_M; nodes are (ζ_M^{kz_j}+ζ_M^{−kz_j})/2. If p odd and M|(p−1), choose g primitive in F_p and ω=g^{(p−1)/M}. Check ω^M=1 and ω^{M/q}≠1 for every prime q|M. Reduction ζ_M↦ω is a ring map: ω is a root of Φ_M modulo p, since p∤M and its order is exactly M. It specializes the actual algebraic cosine values and Chebyshev recurrence, so a nonzero determinant here also proves the complex/real determinant nonzero. This does not use independent random axis labels. The rational D route is stronger operationally: it needs no splitting prime and handles nullvectors exactly.

## Depends on / sources

Only elementary exponential product identity, polynomial root bound, integer determinant reduction. Literature is background, not load bearing.

## Checks

Producer code: ../code/t2_screen.py, functions dictionary and root_check. Runs include direct algebraic-root checks at n1,2 for K/T/O, with prime/order/primitive-root data in ../evidence/t2-cyclic-screen.json. V=CD/8 verified exactly in finite fields. Initial code also records a prose digest as provenance, not an acceptance dependency; subsequent checker uses code/data pins only. Independent replay remains needed for finite computational verdicts.

## Scope / open items

No all-degree invertibility claim for any b,c formula, no conditioning bound, no phase-shifted formula without a separate lift. T3 independent derivation/check requested. Historical priority unassessed.

## History

2026-11-06, rules SHA ccd9e905d19c0c625c196c4a3f3e707058ed042a; written reduction follows pre-run gate and screen design.
