# PD-T?proof-attempts-2-codex-19 — Quadratic reproduction forces a positive physical node gap

Final ID: **PD-T171**. Provisional ID `PD-T?proof-attempts-2-codex-19` is retained as an alias. Registered after accepted Claude audit-01 and response-01; historical pending-audit notes below are superseded.

Canonical Split from (registration): PD-T100 / OPEN_TARGETS A5 (exact finite case, supporting result or separately OPEN obligation; source measurement retained).

ID kind: PD-T.
Aliases: uniform radial node-gap positivity; squared-distance reproduction; explicit node-separation lower bound.
Split from: the positive-gap hypothesis of the supporting node-cone result15.
Split into: none. Finite maxima counts remain separate results.

## Statement

Let distinct nodes B_0,…,B_{N−1} lie in S=[−1,1]². Let their continuously differentiable cardinal functions L_i reproduce every polynomial of total degree at most2. Fix a node z=B_q and define

F_z(d)=∇L_q(z)·d+Σ_{i≠q}|∇L_i(z)·d|.

Set δ²=min_{i≠q}||B_i−z||_2²>0, Q=max_{i≠q}||B_i−z||_2² and r=max_{i≠q}||B_i−z||∞>0. Then every direction with ||d||∞=1 satisfies

F_z(d)≥2δ²/[r(δ²+Q)]≥δ²/(δ²+8)>0.

In particular this supplies a positive physical gap in every direction, hence in every feasible boundary direction, for every Padua polynomial cardinal family of degree n≥2. Any verified positive rational lower bound0<ε≤δ² gives the rational gap bound ε/(ε+8).

## Definitions

Cardinals mean L_i(B_j)=δ_ij. Reproduction means p(w)=Σp(B_i)L_i(w) for every p∈Π_2. The gradient is taken in physical coordinates on a neighbourhood of the nodes; no cosine-angle normal degeneracy is introduced. N≥2 is implicit in quadratic reproduction at distinct determining nodes.

## Assumptions

Distinct nodes, differentiability and exact reproduction of constants, both coordinate functions and the squared-distance polynomial used below. No special Padua weight, field or sign formula is needed. The explicit second bound uses only S=[−1,1]². This is an analytic theorem, with no numerical run as a hypothesis.

## Status by part

Overall status: **PROVED** (written proof; required Claude audit pending).

| Part | Status | Evidence |
|---|---|---|
| every nonzero physical direction has positive node gap | PROVED | squared-distance and linear reproduction identities |
| explicit node-separation lower bound | PROVED | positive/negative derivative mass comparison |
| application to Padua n≥2 | PROVED under ordinary cardinal reproduction | Π_2 is contained in Π_n |

This supporting result does not certify any maxima count or replace the Hessian/remainder and geometric checks of result15.

## Depends on

Elementary differentiation of polynomial reproduction and finite sums. Ordinary Padua cardinals reproduce Π_n by unisolvence; the exact implementations independently verify their interpolation identities. No measured node gap is used.

## Checks

No computation is needed for the theorem. A certificate using this coarse lower bound must independently verify distinct node separations and the reproduction assumptions, and still verify node-cardinal positivity, Hessian bounds, radius and leaf geometry. The current frozen degree-five code instead uses larger exact breakpoint minima; this theorem changes none of its predicates or outputs.

## Sources

Same complete target-specific registry gate as result15 and T-A5-n5.md, followed by searches for quadratic reproduction, node gaps, nonnegative directional derivatives and radial cardinals. Closest computational predecessor is the old N node cone, not a proved structural positivity claim. This is proof completion/support for the registered A5 mechanism; no priority or novelty claim.

## Proof or evidence

Put a_i=∇L_i(z)·d. Differentiating constant reproduction gives Σa_i=0. Let

A_+=Σ_{i≠q,a_i>0}a_i,  A_−=Σ_{i≠q,a_i<0}(−a_i).

Then a_q=A_−−A_+ and

F_z(d)=a_q+Σ_{i≠q}|a_i|=2A_−.

Reproduce p(w)=||w−z||_2². Since ∇p(z)=0 and p(z)=0, differentiation in direction d gives

Σ_{i≠q}||B_i−z||_2² a_i=0.

The positive and negative weighted derivative masses therefore agree. With δ²≤||B_i−z||²≤Q, this yields δ²A_+≤Q A_− and hence A_+≤(Q/δ²)A_−.

Differentiating the reproduced coordinate vector gives ΣB_i a_i=d. Subtracting zΣa_i=0 gives d=Σ_{i≠q}(B_i−z)a_i, so

1=||d||∞≤r(A_++A_−)≤r(1+Q/δ²)A_−.

Multiplying by2 proves F_z(d)≥2δ²/[r(δ²+Q)]. In particular A_− cannot be zero. Since r≤2 and Q≤8 on the square,

2δ²/[r(δ²+Q)]≥δ²/(δ²+Q)≥δ²/(δ²+8)>0.

The function t↦t/(t+8) is increasing for t>0, so a verified positive lower bound0<ε≤δ² yields ε/(ε+8). The estimate holds for all normalized directions, a larger set than the feasible boundary directions required by result15. Finally Π_n contains Π_2 for every n≥2, giving the Padua application. ∎

## Scope

This proves positivity and a coarse explicit bound, not the exact minimum and not a useful radius by itself. A coarse bound may require deeper spatial refinement than the sharper breakpoint minimum. Cardinal families reproducing only affine functions need not satisfy this theorem. Zero angular gaps caused by singular coordinate changes are not contradicted by a theorem about physical derivatives.

## Open items

Independent mathematical inspection and required Claude audit. Optional future certificates may use the coarse bound as a separate exact gap predicate; such a schema extension must be stated and checked. The frozen current degree-five producer and its independent runs continue unchanged.

## History

2026-11-01, Codex `/root/a5_develop`, allocated gpt-6.1-sol xhigh; rules44be0080c69495cc6959e3d4c2b602fa73678d76. Derived while the full degree-five count and independent execution were running. Written separately so the substantive analytic positivity statement is not conflated with an unfinished finite count. No numerical evidence or literature priority assertion is used.
