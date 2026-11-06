# PD-T?padua-3d-codex-T9-02 — odd-harmonic universal lower estimate

ID kind: PD-T. Aliases: T9-SQ; positive-facet square-wave dual.
Split from: none; retained-kernel comparison T9-K is a dependency.
Split into: none.

## Statement

Under T9-K's d=3 hypotheses, for n≥1 and m=floor(n/2), set
O_m=Σ_{a=0}^m1/(2a+1). Then

**||P||≥max{3/4+3/(2π), O_m³/(3π³)}.**

In particular liminf_{n→∞}||P_n||/(log n)^3≥1/(24π³) for any
sequence of such projections. This is27 times the explicit leading lower
coefficient in T6; neither estimate claims a sharp coefficient.
A stronger finite-degree formula is

||P||≥(8/π³)Σ_{|k|≤n, r₁(k),r₂(k),r₃(k) odd}
                 2^{-s(k)}/(r₁(k)r₂(k)r₃(k)),

where r(k)=(n+1)1+Ak and
A=[[-1,-1,-1],[-1,1,-1],[-1,-1,1]].

## Definitions / assumptions / status

All sums include integer k. Probability Haar measure and real operator
norms as in T9-K. Overall status: PROVED (analytic proof).
Candidate disposition: quantitative known-mechanism variant, no priority claim.
No asymptotic conclusion is drawn from a numerical fit.

## Depends on / sources

T9-K's ||P||≥||K_n||₁. T6 facet proof is the closest local predecessor;
literature-T9.md preserves source limits. No unread source is a premise.

## Proof

Every r_j(k)≥1 because each row of A has entries±1 and |k|≤n.
The matrix A has determinant−4, so k↦Ak is injective. The endomorphism
t↦Aᵀt preserves probability Haar measure: integration of any character
e^{ik·Aᵀt} is0 unless Ak=0, hence unless k=0; density then identifies
the pushforward with Haar. Thus
F(t)=e^{i(n+1)(t₁+t₂+t₃)}K_n(Aᵀt)
has L1 norm||K_n||₁ and only strictly positive frequencies r(k), with
positive coefficient2^{-s(k)}.

Let b(t)=sign(sin t), defined arbitrarily at its null set of zeros.
For positive integer r,
∫e^{irt}b(t)dμ(t)=2i/(πr) if r is odd, and0 if r is even.
This follows by integrating separately over(0,π),(π,2π).
Pair F with b(t₁)b(t₂)b(t₃), of absolute value1 almost everywhere.
All nonzero contributions have common phase i³, so their absolute sum is
exactly the finite formula in the statement; Hölder proves that formula.
No complex norm extension of P is being used: this is a scalar inequality
for the already identified real kernel's L1 norm.

For 0≤a₁≤a₂,a₃≤m choose
k=(n−a₂−a₃,a₂−a₁,a₃−a₁).
Every coordinate is nonnegative, |k|=n−2a₁≤n, and
r=(2a₁+1,2a₂+1,2a₃+1). The weight2^{-s(k)}≥1/8.
Let S_j be the sum of∏(2a_i+1)^{-1} over cube indices0≤a_i≤m
with a_j a minimum coordinate. Symmetry gives S₁=S₂=S₃. Every cube
index belongs to at least one such region, hence3S₁≥O_m³; ties do
not hurt this direction. Keeping only the j1 region in the positive sum
gives (8/π³)(1/8)(O_m³/3), as asserted.

Finally O_m=H_{2m+1}−H_m/2=(1/2)log m+O(1), while
log floor(n/2)/log n→1. The coefficient is1/(24π³).

## Checks / scope / open items

t9_checks.py computes the exact rational finite sum and checks its
domination of O_m³/24 (the factor before8/π³) for the frozen degrees.
Those finite checks support but do not replace the all-n argument.
Threshold decimals use mpmath and are MEASURED scalar evaluations,
not rigorous decimal enclosures. Sharpness and constructive upper remain OPEN.

## History

2026-11-06 Codex: replace the T6 sawtooth test by an odd square wave and
retain its averaged kernel. Proof inclusion and parity are explicit so the
improvement is not attributed merely to numerical kernel norms.
