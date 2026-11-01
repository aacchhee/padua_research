# PD-N063 — Three scoped Padua negative-witness mechanisms fail: no negative point on the equal-phase path or on the edges x=1, y=1, and no eventual (all-large-n) negative witness on any fixed-A/n^3 path

Provisional alias: `PD-N?drift-codex-32`. Final ID assigned at PR preparation, 2026-11-01 (handoff 11, after Codex audit-04 acceptance).

ID kind: PD-N.
Aliases: E5 equal-phase path failure; positive square-edge paths; coarse common-angle A/n^3 path failure.
Split from: failed witness-path tests originally retained within IDEA-257.
Split into: none; the three precisely specified failed mechanisms have their own IDEA entries 32–34.

## Statement

Let n>=4, `g_m=T_(n-m)(x)T_m(y)-T_m(x)T_(n+1-m)(y)`, `m=0,1,2,3`, and

`P_n=9(g_1^2-g_0*g_2/2)+g_2^2-g_1*g_3`,

as in PD-T069. The following proposed mechanisms fail within their stated ranges. In cases 1–2 the stated path contains no point with `P_n<0`, at any integer n>=4. In case 3 the mechanism that fails is the *eventual* one: for each fixed A!=0 the path gives `P_n>0` for all n>=N(A), so it supplies no negative witness for all sufficiently large n. Case 3 does **not** say that a fixed-A path contains no negative point; it does contain finite-n negative points (Remark after item 3).

1. **Equal phase (IDEA-259).** For every real alpha,

   `P_n(cos(alpha/n),cos(alpha/(n+1)))`

   `=10*sin^2(alpha)*sin^2(alpha/[n(n+1)])>=0`.

2. **Two square edges (IDEA-260).** `P_n(1,y)>=0` for every `y in [-1,1]`, and `P_n(x,1)>=0` for every `x in [-1,1]`. More precisely, on either edge the generators are `g_m=b*sin(C-m*d)` and

   `P_n=b^2*[(9/2)*sin^2(C-d)+(11/2)*sin^2(d)]>=0`,

   with `(b,C,d)=(2*sin((n+1)phi/2),(n+1)phi/2,phi)` when `(x,y)=(1,cos phi)`, and `(b,C,d)=(-2*sin(n theta/2),n theta/2,theta)` when `(x,y)=(cos theta,1)`.

3. **Fixed nonzero coarse increment (IDEA-261).** For each fixed real `A!=0`, put

   `eta_n(A)=(cos(pi/n+A/n^3),cos(pi/(n+1)+A/n^3))`.

   Then `n^10*P_n(eta_n(A))->(9/2)*A^4>0` as n tends to infinity through integers. In particular, for each such fixed A there is an `N(A)` such that `P_n(eta_n(A))>0` for every `n>=N(A)`.

   *Remark (finite-n negative points on fixed-A paths; not part of the negative claim).* Item 3 is an eventual statement only. Fixed-A paths do contain negative points at finite n. With `a=20*pi^3/9` and `zeta_n` as in PD-T144, the identity `(a/n0)/n0^3=a/n0^4` gives exactly `eta_(n0)(a/n0)=zeta_(n0)` for every integer n0>=4. By PD-T144 (PROVED), `P_(n0)(zeta_(n0))<0` for every sufficiently large n0. Hence, for every sufficiently large n0, the fixed-A path with `A=a/n0` has a negative point at `n=n0`. Such points give finite-n upper bounds on rho_(n0); they are not an all-large-n witness at a fixed A, so they are consistent with item 3. MEASURED illustration only (80-digit mpmath, n=4..3000, not a proof and not used by any claim here): the set of n with `P_n(eta_n(A))<0` is one run of consecutive integers, namely A=0.25: [191,358]; A=0.5: [93,181]; A=1: [44,92]; A=2: [19,47]; A=5: [5,20]; A=10: [4,10]; A=20: [4,5]. For A=-1 the set is empty. Sources: auditor script `topics/padua-lanczos-drift-20261101/checks/audit-01/scripts/E5/f_coarse_window.py` (audit-01 E5 cmd 9, min/max of the set) and `tracks/bivariate-lanczos/code/drift/response01_e5_checks.py`, output `topics/padua-lanczos-drift-20261101/evidence/response-01-e5-checks.json` part B (full runs; it also reproduces `P_50(eta_50(a/50))=P_50(zeta_50)=-2.28174077277e-17`). Heuristic, unproved: `eta_n(A)=zeta_n(A*n)` in the general-a notation of PD-T144 (remark "General common increment a/n^4"), so one expects negativity roughly for `A*n` in the admissible interval (49.41, 88.39). That limit is not uniform in a, so this does not prove the windows.

These failures are restricted to the prescribed point paths, and for case 3 to the eventual (all-large-n) regime at fixed A. They neither reject the positivity-radius target U1 nor imply nonnegativity near these paths. The successful common increment `a/n^4` in PD-T144 lies outside case 3's fixed-A assumption.

## Definitions and assumptions

Exact real arithmetic; `T_j(cos v)=cos(jv)`. Cases 1–2 hold at every integer n>=4 and for all stated parameters. Case 3 fixes A before taking the limit; its threshold is permitted to depend on A. Case 3 is an eventual statement: it does not exclude negative points at finitely many n for a fixed A (Remark after item 3). No uniform statement for an n-dependent sequence A_n is asserted. No weight, unisolvence, or computed-recurrence hypothesis is used.

## Status by part

Overall status: PROVED (analytic identities and limits). Independent reconstruction completed: `topics/padua-lanczos-drift-20261101/checks/independent-math-01.md` Supplement 01, "New E5 failed paths, file 32", which pins the pre-response content SHA-256 `12e8cbfb…`. External Claude audit-01 (`topics/padua-lanczos-drift-20261101/audit-01.md`, `checks/audit-01/E5-records-30-32.md`): CONFIRMED-WITH-CORRECTIONS. Corrections E5-F1/F2 are applied in response-01; Codex re-audit pending.

| Negative mathematical statement | Status | Evidence |
|---|---|---|
| Equal-phase path has no negative P_n point | PROVED | Exact identity in part 1 |
| The two stated square edges have no negative P_n point | PROVED | Exact sine-sequence identity in part 2 |
| Every fixed nonzero A/n^3 path is eventually positive | PROVED | Fixed-order Taylor argument in part 3 |

Candidate disposition: IDEA-259/33/34 are **REJECTED: failed**, solely as negative-witness mechanisms in their respective stated ranges; for IDEA-261 only as an eventual (all-large-n) negative-witness mechanism at each fixed A!=0. P_n's positive-radius theorem, the upper-rate theorem, and U1 itself are not rejected.

## Negative-result scope

Attempted mechanisms: find an upper-bound witness for the positivity radius of the named P_n (i) at some point of the equal-phase path, (ii) at some point of the edge x=1 or the edge y=1, or (iii) as an eventual negative witness, i.e. one negative point for every sufficiently large n, at a fixed nonzero common angular displacement A/n^3 from the `(j,k)=(1,1)` node.

Covered parameter range: exactly cases 1–3 above. Not covered: finite-n negative points on fixed-A paths (they exist; Remark after item 3), x=-1 or y=-1, arbitrary interior curves, perturbations off the specified paths, n-dependent A_n, other obstruction certificates, a matching rate for rho_n, or the optimal obstruction radius delta_obs(n).

## Depends on

Definitions of PD-T069. For case 3, the exact derivative formulas and Taylor bound proved in PD-T144 are reproduced below to make this failure independently checkable. No computer-assisted proof or external theorem is used.

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

As in PD-T144, direct differentiation and the sine addition formulas give

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

The proofs are exact identities and fixed-order Taylor estimates. Exact coverage of the developer checker `e5_exact_checks.py` for this record: (1) the identity `9 sin^2 d+sin^2 2d-sin d sin 3d=10 sin^2 d` only, not the reduction of g_m to `sin(alpha)sin(m d)`; (2) the sine-sequence identity for `h_m=b sin(C-m d)`, not the edge reductions of g_m; (3) the derivative formulas shared with PD-T144, entered after the node reduction, and the substitution of four equal limits `-A^2` into the quadratic. It does not check the limits `n^5 g_m->-A^2` themselves. A run/output/hash manifest is recorded in the direction file. Finite computation is not the reason for any universal quantifier. Independent reconstruction of all three parts: `topics/padua-lanczos-drift-20261101/checks/independent-math-01.md` Supplement 01. External audit: audit-01 (`checks/audit-01/E5-records-30-32.md`), which also rechecked parts 1–2 from the raw recurrence at random parameters (cmd 8) and the fixed-A series exactly (cmd 4).

## Sources

Internal predecessors PD-T069/PD-T075 and PD-T144. No external source or historical novelty claim.

## Scope and open items

Only the three failed negative-witness mechanisms are rejected. The successful rho_n=O(n^-5) theorem is unchanged. Uniformity of delta_obs(n), matching radius rates, actual finite-precision reading (G), and all other paths are outside the negative claim. Case 3 rejects only the eventual negative-witness mechanism at fixed A; finite-n negative points on fixed-A paths exist (Remark after item 3). Independent reconstruction (independent-math-01 Supplement 01) and external audit-01 are completed. Next verification: Codex re-audit of the response-01 scope wording.

## History

2026-11-01, Codex E5 developer, requested gpt-6.1-sol xhigh; rules/base `806cc7b4509fd93bae652f9545d32d95529f8281`. At AC's explicit instruction that failed mechanisms receive IDEA entries and scoped PD-N records, split the three retained failed path mechanisms from IDEA-257 into IDEA-259/33/34 and this PD-N record. Removed the earlier unsupported minor-path exemption; it had no user-authorized basis. No mathematical scope beyond the actually considered paths is added. No Git/shared-registry mutation by this worker.
- 2026-11-01 (Claude response-01, Opus 5.5 high): audit-01 E5-F1. Title, preamble, case-3 assumptions, disposition, attempted mechanism and covered range reworded so case 3 rejects only the eventual (all-large-n) negative-witness mechanism at fixed A. Added a Remark after item 3: fixed-A paths contain finite-n negative points (exact identity eta_n0(a/n0)=zeta_n0 plus PD-T144; MEASURED windows as illustration only). The theorem in item 3 is unchanged. Original wording: title «Three scoped Padua paths fail to provide negative witnesses»; preamble «The following proposed paths fail to supply a point with `P_n<0` within their stated ranges:»; attempted mechanism «Attempted mechanism: find an upper-bound witness for the positivity radius of the named P_n by evaluating along equal high-frequency phases, on the edges x=1 or y=1, or at a fixed nonzero common angular displacement A/n^3 …»; scope «These failures are restricted to the prescribed point paths. They neither …»; disposition «… solely as negative-witness mechanisms in their respective stated ranges.»; covered range «Covered parameter range: exactly cases 1–3 above. Not covered: x=-1 or y=-1, …».
- 2026-11-01 (Claude response-01, Opus 5.5 high): audit-01 E5-F2/E5-F3. Metadata only: the stale "independent reconstruction pending" lines now cite independent-math-01 Supplement 01 and audit-01. Status unchanged (PROVED). Checks now state the developer checker's exact coverage. Original wording: «Overall status: PROVED (analytic identities and limits; independent reconstruction pending).»; «The E5 exact symbolic checker corroborates the sine-sequence identities, common derivative formulas, and the coarse limiting quadratic; … Independent mathematical reconstruction and the required external Claude audit are pending for this new record.»; «Next verification: independent reconstruction of the exact identities and the fixed-A asymptotic, followed by external audit.».
