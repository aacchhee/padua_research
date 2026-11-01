# PD-N?drift-codex-32 — Three scoped Padua paths fail to provide negative witnesses

ID kind: PD-N.
Aliases: E5 equal-phase path failure; positive square-edge paths; coarse common-angle A/n^3 path failure.
Split from: failed witness-path tests originally retained within IDEA?drift-codex-30.
Split into: none; the three precisely specified failed mechanisms have their own IDEA entries 32–34.

## Statement

Let n>=4, `g_m=T_(n-m)(x)T_m(y)-T_m(x)T_(n+1-m)(y)`, `m=0,1,2,3`, and

`P_n=9(g_1^2-g_0*g_2/2)+g_2^2-g_1*g_3`,

as in PD-T069. The following proposed paths fail to supply a point with `P_n<0` within their stated ranges:

1. **Equal phase (IDEA?drift-codex-32).** For every real alpha,

   `P_n(cos(alpha/n),cos(alpha/(n+1)))`

   `=10*sin^2(alpha)*sin^2(alpha/[n(n+1)])>=0`.

2. **Two square edges (IDEA?drift-codex-33).** `P_n(1,y)>=0` for every `y in [-1,1]`, and `P_n(x,1)>=0` for every `x in [-1,1]`. More precisely, on either edge the generators are `g_m=b*sin(C-m*d)` and

   `P_n=b^2*[(9/2)*sin^2(C-d)+(11/2)*sin^2(d)]>=0`,

   with `(b,C,d)=(2*sin((n+1)phi/2),(n+1)phi/2,phi)` when `(x,y)=(1,cos phi)`, and `(b,C,d)=(-2*sin(n theta/2),n theta/2,theta)` when `(x,y)=(cos theta,1)`.

3. **Fixed nonzero coarse increment (IDEA?drift-codex-34).** For each fixed real `A!=0`, put

   `eta_n(A)=(cos(pi/n+A/n^3),cos(pi/(n+1)+A/n^3))`.

   Then `n^10*P_n(eta_n(A))->(9/2)*A^4>0` as n tends to infinity through integers. In particular, for each such fixed A there is an `N(A)` such that `P_n(eta_n(A))>0` for every `n>=N(A)`.

These failures are restricted to the prescribed point paths. They neither reject the positivity-radius target U1 nor imply nonnegativity near these paths. The successful common increment `a/n^4` in PD-T?drift-codex-30 lies outside case 3's fixed-A assumption.

## Definitions and assumptions

Exact real arithmetic; `T_j(cos v)=cos(jv)`. Cases 1–2 hold at every integer n>=4 and for all stated parameters. Case 3 fixes A before taking the limit; its threshold is permitted to depend on A. No uniform statement for an n-dependent sequence A_n is asserted. No weight, unisolvence, or computed-recurrence hypothesis is used.

## Status by part

Overall status: PROVED (analytic identities and limits; independent reconstruction pending).

| Negative mathematical statement | Status | Evidence |
|---|---|---|
| Equal-phase path has no negative P_n point | PROVED | Exact identity in part 1 |
| The two stated square edges have no negative P_n point | PROVED | Exact sine-sequence identity in part 2 |
| Every fixed nonzero A/n^3 path is eventually positive | PROVED | Fixed-order Taylor argument in part 3 |

Candidate disposition: IDEA?drift-codex-32/33/34 are **REJECTED: failed**, solely as negative-witness mechanisms in their respective stated ranges. P_n's positive-radius theorem, the upper-rate theorem, and U1 itself are not rejected.

## Negative-result scope

Attempted mechanism: find an upper-bound witness for the positivity radius of the named P_n by evaluating along equal high-frequency phases, on the edges x=1 or y=1, or at a fixed nonzero common angular displacement A/n^3 from the `(j,k)=(1,1)` node.

Covered parameter range: exactly cases 1–3 above. Not covered: x=-1 or y=-1, arbitrary interior curves, perturbations off the specified paths, n-dependent A_n, other obstruction certificates, a matching rate for rho_n, or the optimal obstruction radius delta_obs(n).

## Depends on

Definitions of PD-T069. For case 3, the exact derivative formulas and Taylor bound proved in PD-T?drift-codex-30 are reproduced below to make this failure independently checkable. No computer-assisted proof or external theorem is used.

## Proof

### 1. Equal phase

Set `theta=alpha/n`, `phi=alpha/(n+1)`, and `d=theta-phi`. Then `n*theta=(n+1)*phi=alpha`, so the cosine subtraction formulas give

`g_m=cos(alpha-m theta)cos(m phi)-cos(m theta)cos(alpha-m phi)`

`=sin(alpha)*sin(m(theta-phi))`.

Thus `g_0=0`. The elementary identity `sin^2(2d)-sin(d)sin(3d)=sin^2(d)` yields the displayed formula for P_n. Since `d=alpha/[n(n+1)]`, it is nonnegative for every real alpha.

### 2. The two square edges

At `(x,y)=(1,cos phi)`,

`g_m=cos(m phi)-cos((n+1-m)phi)=2*sin(C)*sin(C-m phi)`,

where `C=(n+1)phi/2`. At `(x,y)=(cos theta,1)`,

`g_m=cos((n-m)theta)-cos(m theta)=-2*sin(C)*sin(C-m theta)`,

where `C=n theta/2`. These are the claimed sine sequences.

For any real b,C,d and the sequence `h_m=b*sin(C-m d)`, the identity

`h_j^2-h_(j-1)*h_(j+1)=b^2*sin^2(d)`

holds for j=1 and j=2 by the sine addition formulas. Therefore

`h_1^2-h_0*h_2/2=(b^2/2)[sin^2(C-d)+sin^2(d)]`,

and `h_2^2-h_1*h_3=b^2*sin^2(d)`. Substitution proves the stated nonnegative P_n formula. Every point of either stated edge is covered by a real angle theta or phi.

### 3. Fixed nonzero common increment A/n^3

Fix `m in {0,1,2,3}`, set `theta=pi/n`, `phi=pi/(n+1)`, and define

`f_(n,m)(t)=g_m(cos(theta+t),cos(phi+t))`.

As in PD-T?drift-codex-30, direct differentiation and the sine addition formulas give

`f_(n,m)(0)=0`,

`D_(n,m):=f'_(n,m)(0)=[sin((2n+1)m d)-(2n+1)sin(m d)]/2=O(n^-3)`,

where `d=pi/[n(n+1)]`, and

`f''_(n,m)(0)=-(2n+1-2m)cos(m theta)cos(m phi)-2m sin(m theta)sin(m phi)`.

Consequently `f''_(n,m)(0)/n->-2`. The product-to-sum formula bounds the third derivative, for every real t, by

`|f'''_(n,m)(t)|<=n^3+(n+1)^3`.

Take `t=A/n^3`, for the fixed real A in the statement. Taylor's theorem gives

`f_(n,m)(A/n^3)=(A/n^3)D_(n,m)+(A^2/(2n^6))f''_(n,m)(0)+O(n^-6)`.

The first term is O(n^-6), and the second term multiplied by n^5 tends to `-A^2`. Hence, for each m,

`n^5*g_m(eta_n(A))->-A^2`.

Substituting these four equal limits into the fixed quadratic expression for P_n yields

`n^10*P_n(eta_n(A))->9(A^4-A^4/2)+(A^4-A^4)=(9/2)A^4`.

For `A!=0` this is strictly positive, proving eventual positivity. At A=0 the point is the original node and P_n=0; the claim does not assert strict positivity in that excluded case. An n-dependent sequence A_n tending to zero is outside this argument: in particular `A_n=a/n` gives the separately successful a/n^4 witness, so no broader failure conclusion is available.

## Checks

The proofs are exact identities and fixed-order Taylor estimates. The E5 exact symbolic checker corroborates the sine-sequence identities, common derivative formulas, and the coarse limiting quadratic; a run/output/hash manifest is recorded in the direction file. Finite computation is not the reason for any universal quantifier. Independent mathematical reconstruction and the required external Claude audit are pending for this new record.

## Sources

Internal predecessors PD-T069/PD-T075 and PD-T?drift-codex-30. No external source or historical novelty claim.

## Scope and open items

Only the three failed negative-witness mechanisms are rejected. The successful rho_n=O(n^-5) theorem is unchanged. Uniformity of delta_obs(n), matching radius rates, actual finite-precision reading (G), and all other paths are outside the negative claim. Next verification: independent reconstruction of the exact identities and the fixed-A asymptotic, followed by external audit.

## History

2026-11-01, Codex E5 developer, requested gpt-6.1-sol xhigh; rules/base `806cc7b4509fd93bae652f9545d32d95529f8281`. At AC's explicit instruction that failed mechanisms receive IDEA entries and scoped PD-N records, split the three retained failed path mechanisms from IDEA?drift-codex-30 into IDEA?drift-codex-32/33/34 and this PD-N record. Removed the earlier unsupported minor-path exemption; it had no user-authorized basis. No mathematical scope beyond the actually considered paths is added. No Git/shared-registry mutation by this worker.
