# PD-N?argmax-bridge-codex-D10-axis — A quadratic true-constant upper fails through the origin

ID kind: PD-N. Aliases: limiting constant fractional obstruction; failed through-origin K(1-a) bound.
Split into: none. The positive near and global bounds have separate records.

Rules/input `9d5e8c7a1a8fab6017d5dd9406daec0d834b0bbf`; latest main
`64409c47a717aef074f611b31a9fd48b7a15101b`. Parent-assigned Sol xhigh;
serving metadata unexposed. **PROVED**, analytic developer result, distinct
review required. Exact real arithmetic; no numerical premise.

Split from: original combined D10-relative-constant first freeze, whose
EXACT complete text is preserved at
[attempts/D10-relative-constant-first-freeze.md](../attempts/D10-relative-constant-first-freeze.md),
SHA256 `56c69c6e39fc0fddf9ada3505c99c293d89fe56d74c2c1a7aa1d643d30c697af`.
This is a substantive split, with no new mathematics or altered constants.
Mapping/history: [attempt](../attempts/D10-relative-constant.md).

## Exact negative statement

For D02's TRUE completed constant C_infty there is no finite real K such that

    C_infty(alpha,beta)-C_infty(0,0)<=K[1-a(alpha,beta)]

on a full neighborhood of phase zero. It already fails along beta=0,
alpha decreasing to zero. Candidate disposition: REJECTED: refuted only
for this through-origin quadratic upper; the far-only22(1-a) bound is
outside this negative scope. No physical Lebesgue or finite-degree theorem
is refuted. The result is independent of n.

## Dependencies and supporting exact limit

Use the exact decomposition and local H proof in
[D10-relative-constant.md](D10-relative-constant.md), and accepted
C01-near-axis-limit.md section3's actual central-root calculation. With
k_frac=(4/pi^2)integral_0^1 sqrt(1-y^4)dy>0, the proof gives

    C_infty(alpha,0)-C_infty(0,0)
                      =k_frac alpha^(3/2)+o(alpha^(3/2)).

This supporting limit is a direct transfer through the exact decomposition,
not through the old uniform eta0 bridge or a numerical root-width fit.
k_frac is distinct from kappa_shift and the limiting deformation D_infty.

## Proof preserved from the combined first freeze

Equation(2) below is the exact decomposition in the near companion.

### 6. The genuine axis term and the failed quadratic form

For beta=0, C01-near-axis-limit.md section3 computes the exact central
root correction by scaling epsilon_c=sqrt(alpha)y. Its justified
dominated limit is

    E_c(alpha,0)/alpha^(3/2)
                ->(4/pi^2)integral_0^1 sqrt(1-y^4)dy.

This is the actual E_c in(2), not a bound inferred from a root width
or from the approximate T bridge. All other terms in(2) change by
O(alpha^2). E_infty and a are smooth even functions locally. For H,
the same near part of(13) is O(x^2) in absolute value. On v>=1/2,
the accepted finite variation V of f' gives
integral |D_x f(v)|dv<=V*x^2 by the elementary L1 second-difference
identity used in C01's axis proof; the kernel is bounded there and
D_x f(0)=O(x^2). Thus |H(x)-H(0)|=O(x^2) locally as well.
This proves(6) directly from the exact decomposition. Since
1-a(alpha,0)=alpha^2/4+O(alpha^4), every finite quadratic K(1-a)
upper through zero contradicts the positive coefficient in(6).
No conclusion is transferred to the physical Lebesgue function.

## Scope, checks and history

Only the specified quadratic constant upper is rejected. No obstruction is
transferred to physical lambda, a far-only bound, or a fractional/entropy
allowance. Full finite S-aS(0) remains OPEN. The original primitive
PD-N079 concerns a different ordered limit and is not the present proof.
No computation, numerical integration or degree job. 2026-11-06 split
under root authorization, with original exact text preserved above; no
new mathematical derivation beyond the developer first freeze.


### Supplementary review closure — 2026-11-06

Distinct Astra xhigh reconstruction ACCEPTED the preceding unchanged
final split scope; no unresolved findings. See
[independent-checks-D10-relative-constant.md](../independent-checks-D10-relative-constant.md),
report SHA256bdcadf119fb905f898612ad25b9123bf8ff58184d6ef573e1503a740d987964c.
The substantive split, inherited-Arb provenance and cutoff-domain wording
findings are closed there. This records no new analytic onset or finite
certificate. Final Claude review remains pending.
