# PD-T?proof-attempts-2-codex-15 — Exact physical node-cone exclusion

Final ID: **PD-T167**. Provisional ID `PD-T?proof-attempts-2-codex-15` is retained as an alias. Registered after accepted Claude audit-01 and response-01; historical pending-audit notes below are superseded.

Canonical Split from (registration): PD-T100 / OPEN_TARGETS A5 (exact finite case, supporting result or separately OPEN obligation; source measurement retained).

ID kind: PD-T.
Aliases: A5 degree-five node gap; radial absolute-cardinal derivative; exact unit-square breakpoint minimum.
Split from: node-neighbourhood coverage in the degree-five case of programme A5.
Split into: none; actual degree-five count requires a separate certificate.

## Statement

Let polynomial cardinals L_0,…,L_{N−1} on S=[−1,1]² reproduce constants. At an interpolation node z with L_q(z)=1 and L_i(z)=0 for i≠q, let B be a closed convex rectangle containing z in its interior. Require that B meets no square face except possibly faces that contain z. Let D_z be the feasible direction set at z intersected with ||d||∞=1 and put

F_z(d)=∇L_q(z)·d+Σ_{i≠q}|∇L_i(z)·d|.

Suppose verified numbers m>0, R>0 and H_i≥0 satisfy:

- F_z(d)≥m for every d∈D_z;
- ||w−z||∞≤R for every w∈B;
- L_q>0 throughout B;
- |dᵀHessL_i(w)d|≤H_i for every w∈B and ||d||∞=1;
- RΣ_iH_i<m.

Then no point of int(B)∩S is a strict relative local maximum of λ=Σ|L_i|. Every point other than z has a feasible radial direction of strictly positive one-sided derivative; z is excluded by λ≥1=λ(z).

The minimum of F_z on D_z is a finite exact check. Parameterize the feasible portions of the four sides of [-1,1]². On each segment, check the endpoints and every breakpoint ∇L_i(z)·d=0 for i≠q. A rational lower bound m for all these values is a lower bound for F_z everywhere.

## Definitions

All coordinates and derivatives are physical. At a face x=−1 feasible directions have d_x≥0; at x=1 they have d_x≤0, and likewise for y. Directions are unrestricted in a coordinate where z is interior. Every feasible nonzero displacement has a unique form td with t=||w−z||∞>0, d∈D_z.

## Assumptions

Exact polynomial node identities and partition of unity; exact or outward arithmetic; complete feasible-side breakpoint lists; a convex rectangle with the stated face condition and strict leaf containment. No degree bound, nonsingular Hessian assumption or sign-pattern enumeration is needed for this local theorem.

## Status by part

Overall status: **PROVED** (written analytic implication; no degree-five node gap or count is asserted without finite evidence).

| Part | Status | Evidence |
|---|---|---|
| radial derivative lower bound | PROVED | integral remainder identity below |
| finite breakpoint reduction of the node gap | PROVED | piecewise affine function on four closed segments |
| node-cube strict-max exclusion | PROVED | positive radial derivative and λ≥1 |

Required Claude audit of Part2 remains PENDING. This supporting theorem alone leaves the degree-five count OPEN.

## Depends on

Elementary calculus, polynomial interpolation identities and the finite maximum/absolute-value formula. The spatial all-pattern certificate correctness argument is result09 for the existing n4 implementation; an n5 extension must explicitly add and verify this predicate. No floating node-cone data is inherited.

## Checks

Implemented code: `../code/a5_n5_nodes.py` and copied/adapted `a5_n5_boxes.py`. The independent verifier must check supplied gradients/breakpoints, all lower values, node rectangles, positivity and Hessian bounds, and strict containment of each referenced leaf. Completed degree-five computations and actual independent runs are recorded in result16; they verify the application hypotheses, not this analytic implication itself.

## Sources

Programme IDEA17/source06 and old T3 N-node-cone mechanism at the pinned programme head9bd14a6d2c4da69139a10107d8a787f2be0c5c9e; current target gate in T-A5-n5.md. The old floating cone and Bernstein estimates are predecessors, not proof dependencies. Part1 auditF2 expressly leaves separate boundary handlers uncertified; the present statement covers only rectangles actually meeting its exact hypotheses. No novelty/priority claim.

## Proof or evidence

Fix d∈D_z and set u_i(t)=L_i(z+td) while the ray stays in B. Write a_i=u_i'(0) and b_i(t)=u_i''(t), so |b_i|≤H_i. For i≠q, u_i(0)=0 and exact integral Taylor identities give

u_i(t)=t a_i+∫_0^t(t−s)b_i(s)ds,

u_i'(t)−u_i(t)/t=(1/t)∫_0^t s b_i(s)ds.

Hence |u_i(t)|/t≥|a_i|−tH_i/2 and |u_i'(t)−u_i(t)/t|≤tH_i/2. Whenever u_i(t)≠0,

(d/dt)|u_i(t)| = |u_i(t)|/t+sign(u_i(t))(u_i'(t)−u_i(t)/t) ≥ |a_i|−tH_i.

At u_i(t)=0 its right derivative is |u_i'(t)|≥0. The first Taylor identity then forces |a_i|≤tH_i/2, so the same lower bound remains valid at the zero. Thus this is an exact one-sided bound even at crease crossings.

Since L_q>0 on B, its absolute value is L_q and its radial derivative is at least a_q−tH_q. Summing gives

D_d^+ λ(z+td) ≥ a_q+Σ_{i≠q}|a_i|−tΣ_iH_i ≥ m−RΣ_iH_i>0.

For any w∈int(B)∩S other than z, the outward radial direction d remains in B for a sufficiently small positive step. It also remains feasible in S: a square face met by B must contain z; if w lies on that face then the corresponding component of d is zero. Thus the positive one-sided derivative supplies a nearby feasible point of larger value and rules out a relative local maximum. At z, partition of unity gives λ≥|ΣL_i|=1=λ(z), so z cannot be a strict local maximum either.

Finally, F_z is continuous and piecewise affine on every feasible side segment of the unit square. Its only changes of affine formula occur when one of the linear forms ∇L_i(z)·d for i≠q vanishes. Every minimum of an affine function on a closed subsegment occurs at an endpoint. Checking the feasible-side endpoints and all contained zero breakpoints therefore proves the stated global lower bound m. Identicallyzero linear forms add no breakpoint and contribute0 identically. ∎

## Scope

Only certified node rectangles with m>0 and the complete remainder inequality may be discarded. A zero node gap, a rectangle reaching another square face, an uncovered breakpoint or a leaf not strictly inside its node rectangle fails the predicate and remains unresolved. The estimate excludes non-node local maxima of any strictness inside the rectangle; the node itself is excluded only from strict maxima by λ≥1.

## Open items

The degree-five application is now complete under result16:21 accepted node rectangles and738 complete breakpoints were independently verified and included in the full count/global certificate. Higher-degree applications still need their own exact hypotheses, data and independent checks. Required Claude audit remains PENDING.

## History

2026-11-01, Codex `/root/a5_develop`, allocated gpt-6.1-sol xhigh. Rules re-read at44be0080c69495cc6959e3d4c2b602fa73678d76. Written before any degree-five node computation. The n4 lead separately supplied the radial integral-bound route; this file states its feasible-boundary and strict-leaf-containment hypotheses explicitly. All n3/n4 files remain frozen.
