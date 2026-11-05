# PD-T?lanczos-frontier-codex-L5-03 — certified n4 lower obstruction radius

ID kind: PD-T. Aliases: PD-T?lanczos-frontier-codex-L5c; L5c; P4 whole-ball Taylor certificate; n4 G3 lower endpoint.
Split from: finite n4 certificate task of L5/G3. Split into: none.

## Statement

For the15 Padua nodes `P_4={(cos(j*pi/4),cos(k*pi/5)):0<=j<=4,0<=k<=5,j+k even}`, and the union K_delta of their closed Euclidean radius-delta balls in all of R², the optimal obstruction radius for the entire real degree<=9 polynomial class satisfies

`delta_obs(4) >= 1/2048`.

This is a lower bound, not an optimal value or a two-sided bracket. It supplies no upper estimate, trend or all-degree conclusion about PD-T075(U2).

## Definitions and assumptions

The optimal radius and complete-ball convention are those of [L5a](l5-01-finite-optimal-radius-certificates.md). Let T_k be the Chebyshev recurrence and `g_m=T_(4-m)(x)T_m(y)-T_m(x)T_(5-m)(y)`. Use the existing polynomial

`P4=9(g1²-g0*g2/2)+g2²-g1*g3`.

Its actual25 nonzero rational coefficients are stored in the small exact lower certificate. All15 nodes, all55 degree<=9 monomials and every local Taylor term are retained. Exact computation uses Q(sqrt5)(sqrt2) with both radicals positive, with independently checked exact sign/embedding rules. No positivity between sampled directions is assumed.

## Status

PROVED, finite computer-assisted. The reduction is the accepted whole-ball Taylor implication of L5a; independent exact execution verifies its complete premises. Required later Claude scientific/protocol audit remains pending. Original U2 and the full n3–8 G3 decision remain OPEN.

## Dependencies and provenance

The polynomial is the named existing PD-T069/144 certificate, also identified in the repository review_L3b helper, not a new general construction. Its named positivity radius supplies only a lower bound for the optimal radius. L5a proves the exact finite Taylor criterion; no upper bound for the named polynomial is transferred to the optimal radius.

Producer code/g3_n4_producer.py uses Python exact Fraction field arithmetic. Distinct code/g3_n4_independent.py uses SymPy1.14.0 QQ(sqrt2,sqrt5) and DomainMatrix, with Python3.12.14. Floating HiGHS is used only in the separate upper search and is not a lower-acceptance dependency. JSON, SHA256 and exact arithmetic/library implementations remain trusted computational dependencies.

## Proof and finite evidence

The producer and distinct checker independently reconstruct P4 from its formula, identify the ordered node lists using exact polynomial/radical identities, and verify that P4 is nonzero of degree9. At every node its value and first partials vanish exactly. Every Hessian H_i satisfies H_11>0 and det(H_i)>0 in the specified embedding. Put `mu_i=det(H_i)/trace(H_i)>0` and write the full finite translated expansion as

`P4(z_i+h)=h^T H_i h/2 + sum_(a+b>=3) t_iab h_x^a h_y^b`.

All15 exact checks pass at L=1/2048:

`sum_(k=3)^9 sum_(a+b=k)|t_iab| L^(k-2) <= mu_i/2`.

Since |h_x|,|h_y|<=||h||, the quadratic term dominates the complete higher-degree sum for every ||h||<=L, including the ball boundary. Thus P4 is nonnegative on K_L, is nonzero and vanishes at P_4, proving the stated lower bound by L5a.

The distinct checker additionally reconstructs the full45-by55 jet matrix, obtains rank45/kernel10 and verifies exact rank and annihilation. This supports the complete-space setup but is not a replacement for the Taylor inequalities or an upper certificate. Its actual lower execution took16.874s and checked all21 saved dyadic radii; 1/2048 is the largest passing saved dyadic radius for this sufficient Taylor test, not its largest passing real radius or a maximal positivity radius. Exact margins, source/input identities and malformed controls are recorded in [independent receipt](../evidence/g3-n4-independent-lower.json) and [independent report](../independent-checks-g3-05.md).

The fixed lower certificate has4961bytes and SHA256 `ee25f934fdb934b9ca5286c3d6206171525364aebb7c4e0f8f867cd97d24a7c6`. Independent checker source SHA256 is `335bb5c3908b4da12df779e856757ac4c28a22c4239977662316b96e167da474`; its lower-certificate input SHA256 is `ee25f934fdb934b9ca5286c3d6206171525364aebb7c4e0f8f867cd97d24a7c6`. Exact commands, versions and measured producer stage costs are in [n4 methods](../g3-n4-methods.md) and the independent receipt. Regeneration needs the committed small polynomial certificate and repository checker, not original temporary kernel or LP output. New-directory recipes are distinct from the recorded actual execution.

## Scope and remaining work

Upper-certificate search outcomes, including caps or LP failures, are separate and INCONCLUSIVE unless the full exact positive-dependence/rank/membership conditions pass. This lower theorem keeps PROVED regardless of that search. No n5–8 value, optimal upper bound, monotone trend, U2 decision or actual working-precision recurrence realization follows. No primary-literature novelty claim is made. Raw arrays remain outside Git, with local retention and physical archival limitations in COLD_STORAGE.md.

## History and independent check

2026-11-05: Codex root, requested gpt-6.1-sol xhigh, rules9825d184517db81d0aad8542fbd6639f2164b803. Written only after producer and distinct medium checker actual lower passes, under the separately reviewed n4 field/certificate plan. This record integrates their finite evidence and the previously proved L5a implication; it is not a new root execution. Supplementary mathematical/technical review and required Claude audit remain separately recorded.

2026-11-05 audit-01 response, Codex statement/metadata worker; requested gpt-6.1-sol high; runtime variant/effort not independently exposed. Rules read at `7f50cae80f5372db7c278aef4ba4a0a05e1137ea`. L5-1/L5-5: the dyadic endpoint is not the best previously recorded Taylor lower bound. PD-T075 already cites the stronger reviewer bound `b_4=5.6302e-4` for the same polynomial and criterion; [audit-01/L5.md](../audit-01/L5.md) independently reproduced its scope. No new endpoint computation is claimed. Canonical ID is `PD-T?lanczos-frontier-codex-L5-03` (aliases old PD-T L5c, L5c). The audit also reran the committed checker under both SymPy ground-types backends (flint and python); original receipts do not identify the developer's backend. Proof and certificate bytes are unchanged. The saved candidate draft first entered Git at `0574c47` before its prospective source gate was complete. Later completed reading does not cure or waive that deviation; acceptance remains AC's decision. The dated chronology and missing-read/gate checkpoints are in [gate-timing-response-01.md](../gate-timing-response-01.md). No novelty or priority claim is added.
