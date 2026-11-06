# PD-T?padua-3d-20261106-codex-T7-04 — what abstract rank two does and does not imply

ID kind: PD-T. Aliases: rank-two plane-shortcut counterexample.
Split from: none. Split into: none. Supports the OPEN T7 target.

## Statement, definitions and status

Here rank means the minimum number of abstract finite-group generators,
not the rank of H^⊥ (which is always3), nor a dimension of finite H.
A rank-two subgroup of T³ lies in a connected rational plane torus,
but this supplies neither a degree-uniform short character nor its
compatible phase. In particular

    H_5={(i,j,2i+2j)/5 mod1:i,j∈Z/5} ≅ C_5×C_5

has no nonzero u∈H_5^⊥ with q(u)≤3, despite |H_5|=25≤160.
Its shortest q-degree is4. Thus abstract rank two alone does not justify
the handoff's proposed cubic exclusion.

Overall status: PROVED by the following hand proof. This statement is
a counterexample to an inference, not a theorem that H_5 interpolates
Π_3 at a minimal count. H_5 at phase0 is not such a candidate.

## Proof and exact scope

Smith reduction of the integer annihilator gives invariants
(1,s_2,s_3) when the quotient has at most two generators. Its first
unit invariant supplies a primitive integer vector in H^⊥; the
kernel of that primitive torus character is a connected two-torus.
This proves the plane-containment fact. The integer vector's size is
not controlled by the number of generators. Translation also gives
the plane equation u·θ=u·a, whose constant need not be0 or1/2.

For H_5 the exact dual conditions are

    u_1+2u_3≡u_2+2u_3≡0 mod5.

If support has size at most2 and q≤3, a zero coordinate among u_1,u_2
forces u_3=0 mod5, and then both other coordinates are0 mod5; if
u_3=0 the same conclusion holds directly. Since every absolute
coordinate is≤3, this gives the zero vector. If support has size3
and q≤3, every absolute coordinate equals1. None of ±1+2(±1) is
0 mod5. So there is no such nonzero vector. Finally (1,1,2) satisfies
the dual conditions and has q=max(2,2,4,4)=4.

The degree cap of the supplied H4 plane family is a fact about its
specific relation (1,1,−1), not about abstract rank two. The translated
order20 example in [T7-06](t7-rank-two-survivor.md) further supplies a
Π_3-unisolvent rank-two coset, with a phase that breaks compatibility
of a q=2 relation. No rank-three-only conclusion survives.

## Checks, sources and open items

The code also enumerates every integer vector with q≤3 for this one
group; that is a diagnostic cross-check, not a full general-H census.
Finite-subgroup rank and Smith terminology are standard algebra.
No unread published theorem or novelty claim is invoked. Literature
limits: [literature-T7](../literature-T7.md). The general minimal-node
rank-two and rank-three construction problems stay OPEN.

2026-11-06, Codex, assigned gpt-6.1-sol xhigh; rules e5b6445.
Provisional ID.
