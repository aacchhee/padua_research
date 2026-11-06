# PD-T?padua-3d-codex-T9-04 — prefix-bound transfer

ID kind: PD-T. Aliases: T9-LOWERSET; hierarchical Cartesian upper bound.
Split from: none. Split into: none. T9 route4 is its task provenance.

## Statement and definitions

Let x₀,x₁,… be any distinct real nodes in[−1,1]. Let I_m be interpolation
on the first m+1 nodes, λ_m=||I_m||, I_{−1}=0, λ_{−1}=0. Let A be a
finite lower set in N₀^d: α∈A and0≤β≤α coordinatewise imply β∈A.
Then interpolation on X_A={(x_{α₁},…,x_{α_d}):α∈A} in
P_A=span{x^α:α∈A} is uniquely defined and satisfies

||I_A||≤Σ_{α∈A}∏_j(λ_{α_j}+λ_{α_j−1}).

Consequently, **if** an explicit infinite sequence has the uniform prefix
bound λ_m≤C(m+1)^p (C≥1,p≥0), its total-degree lower set |α|≤n
has exactly N=binom(n+d,d) nodes, and

Λ(X_n)≤(2C)^d N(n+1)^{dp}=O(n^{d(p+1)}).

## Assumptions / status

Overall status: PROVED as an implication and norm-transfer theorem.
No existence of a sequence satisfying the premise is asserted here.
The desired concrete polynomial family is separately DEFERRED, not proved
by this conditional application. Candidate disposition: standard reduction
retained; known lower-set framework, no novelty or priority claim.

## Depends on / sources

Only ordinary univariate interpolation. Carnicer–Godés2015, LIT310,
Thm2.1 is the closest source precedent, inherited bounded excerpts only.
The Chkifa–Cohen–Schwab2014 lead is not a verified premise. See literature-T9.

## Proof

Define Δ_m=I_m−I_{m−1} and S_A=Σ_{α∈A}⊗_jΔ_{α_j}.
Its range lies in P_A because each summand has coordinate degree≤α_j
and A is lower. Each Δ_m f vanishes at the earlier nodes x₀,…,x_{m−1}.
At node indexed by γ∈A, only summands α≤γ can survive, and all of them
belong to A. Thus at this node S_Af equals
(⊗_j Σ_{a=0}^{γ_j}Δ_a)f=(⊗_j I_{γ_j})f=f.

Unisolvence also follows directly from the tensor Newton polynomials
ν_α(x)=∏_j∏_{i<α_j}(x_j−x_i). Their evaluation matrix on X_A,
ordered by any linear extension of the coordinate partial order, is
triangular with nonzero diagonal. Its size and the dimension of P_A are
both |A|. Therefore S_A is precisely I_A.

The tensor operator norm is at most the product of its factors' norms,
by iterated application in each variable, and ||Δ_m||≤λ_m+λ_{m−1}.
The triangle inequality gives the norm transfer. Under the prefix premise,
every summand is at most(2C)^d∏(α_j+1)^p≤(2C)^d(n+1)^{dp},
and there are N terms, proving the stated polynomial bound.

## Checks / scope / open items

Analytic proof, no executable premise. It does not imply that arbitrary
distinct sequences, monotone Lobatto prefixes or the measured discrete
Leja arrays satisfy the prefix assumption. The finite grids used in T9-MAX
change with n and their binary64 measurements supply no such theorem.
Resume route4 with a primary source giving an explicitly defined nested
real sequence and a verified all-prefix polynomial bound, then substitute
its constants here. Alternatively prove that prefix bound directly.

For comparison the classical existence bound Λ≤N needs no prefix
sequence: a maximum-absolute-determinant tuple exists by compactness and
has nonzero determinant; replacing one node in that determinant shows
each cardinal polynomial has absolute value≤1 on the cube. Summing
gives Λ≤N. This is a known Fekete baseline, not an explicit closed formula
or a new theorem claimed by this campaign.

## History

2026-11-06 Codex: screen lower-set upper route with a complete elementary
transfer; retain missing source/prefix premise rather than promote an
unread bibliographic lead to an explicit polynomial construction.
