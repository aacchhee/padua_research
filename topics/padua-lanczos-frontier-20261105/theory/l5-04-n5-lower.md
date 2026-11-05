# PD-T335 — certified n5 lower obstruction radius

Final registration (2026-11-05): **PD-T335**; status **PROVED** unchanged. Canonical provisional/historical aliases: `PD-T?lanczos-frontier-codex-L5-04`; `PD-T?lanczos-frontier-codex-L5d`. See [complete map](../preparation/final-id-map.json). This is ID metadata only; original statement/proof and frozen input bytes retain their scopes.

ID kind: PD-T. Aliases: PD-T?lanczos-frontier-codex-L5d; L5d; P5 whole-ball Taylor certificate; n5 G3 lower endpoint.
Split from: finite n5 certificate task of L5/G3. Split into: none.

## Statement and model

For the21 Padua nodes `P_5={(cos(j*pi/5),cos(k*pi/6)):0<=j<=5,0<=k<=6,j+k even}`, let K_delta be the union of their closed radius-delta Euclidean balls in all of R². The optimal obstruction radius for nonzero real polynomials of degree<=11 vanishing on P_5 satisfies

`delta_obs(5) >= 1/16384`.

This is a finite lower endpoint, not an optimal value, a bracket or an all-degree conclusion. The complete n3–8 G3 decision and PD-T075(U2) remain OPEN.

## Definitions and assumptions

Use the unchanged optimal-radius definition and [L5a](l5-01-finite-optimal-radius-certificates.md) whole-ball Taylor criterion. Let T_k be the exact Chebyshev recurrence and `g_m=T_(5-m)(x)T_m(y)-T_m(x)T_(6-m)(y)`. The actual existing polynomial is

`P5=9(g1²-g0*g2/2)+g2²-g1*g3`.

The exact33 nonzero rational coefficients are supplied in [the lower certificate](../evidence/g3-n5-producer-lower.json). All21 nodes, all78 degree<=11 monomials and all Taylor terms are retained. Both radicals are positive in Q(sqrt5)(sqrt3); independently reconstructed ordered U4/U5 roots fix the node embedding. No floating positivity between directions or clipped balls are used.

## Status

PROVED, finite computer-assisted. Exact certificate data, an accepted analytic reduction and actual distinct checker execution establish the statement. Required later Claude audit remains pending. The named P5 certificate supplies only a lower bound for the optimal radius; its own radius upper bounds are not transferred to delta_obs.

## Dependencies and proof

L5a proves the lower-certificate implication. PD-T069/144 and the existing review_L3b helper identify the polynomial; the actual coefficients and every required condition are freshly checked rather than imported from a printed radius.

The exact producer and distinct checker reconstruct a nonzero degree11 P5. At each of the21 nodes its value and both first partials vanish. Every Hessian H_i is positive definite by H_11>0 and det(H_i)>0. Put mu_i=det(H_i)/trace(H_i). In the complete exact translated expansion, both implementations evaluate every Taylor coefficient t_iab and verify

`sum_(k=3)^11 sum_(a+b=k)|t_iab| (1/16384)^(k-2) <= mu_i/2`.

For ||h||<=L=1/16384, |h_x|,|h_y|<=||h|| imply that the positive quadratic term dominates the full finite higher-degree sum. Hence P5>=0 on all of K_L, including each boundary, and the stated optimal-radius lower bound follows. This is exact whole-ball checking, not sampled-direction extrapolation.

The independently rebuilt full63-by78 jet matrix has rank63 and a complete rank15 nullspace with exact annihilation. These complete-space checks support the upper-search setup but supply no upper certificate. All21 saved dyadic radii are checked for the Taylor test; L is its largest passing saved endpoint, not the maximal positivity radius of P5.

## Executed checks and trusted dependencies

[Producer methods](../g3-n5-methods.md), [independent report](../independent-checks-g3-06.md), [exact checker](../code/g3_n5_independent.py), [main receipt](../evidence/g3-n5-independent-lower.json) and [malformed controls](../evidence/g3-n5-independent-controls.json) pin sources, actual commands, inputs, environment, node margins and timing. The distinct main check actually ran35.255533s with52,808KiB peakRSS. It shares no producer arithmetic implementation. Five malformed controls reject altered coefficients/radius/field encoding and a proper kernel subspace; the original rechecks afterward. No additional scientific run was performed by this record's author.

Trusted components are Python3.12.14 exact integers/Fraction for the producer and SymPy1.14.0 QQ(sqrt3,sqrt5)/DomainMatrix for the distinct checker, with independent exact real-embedding sign routines. HiGHS is only an upper proposer and is not a lower-acceptance dependency. JSON/SHA256 provide content identity, not mathematical proof by themselves.

The fixed lower certificate has 7912 bytes, SHA256 `35e804b2a25e693e616e909ca61897b0958f0d990fd590ded1bc649a5ca66311`; independent checker source SHA256 is `40ec8b62636665aa8ff83102c3fdb0fe2c841d85ee50a16287106d7bf448acea`. A fresh check reconstructs nodes, polynomial, complete kernel and all Taylor predicates from the committed small certificate; no old temporary kernel or LP output is required. The independent report gives the actual command; choosing new scratch paths is a prospective rerun, not another executed one.

## Scope and remaining work

Upper-search failures/caps remain INCONCLUSIVE. No n5 upper bound, n6–8 value, G3 trend, asymptotic U2 claim or actual working-precision recurrence model follows. This finite verification reuses a known certificate mechanism and makes no novelty or priority claim. Raw files remain temporary outside Git; no archival retention or Windows delivery is claimed.

## History and review

2026-11-05: Codex root, requested gpt-6.1-sol xhigh, rules9825d184517db81d0aad8542fbd6639f2164b803. Root allocated one explicit n5 field/cost pilot after reviewing n4 costs; the field/source plan received independent mathematical review before science. This finite statement is written only after actual distinct lower/kernel checking and controls. Its PROVED lower status is separate from the completed, capped and inconclusive upper search and required later Claude audit.

2026-11-05 audit-01 response, Codex statement/metadata worker; requested gpt-6.1-sol high; runtime variant/effort not independently exposed. Rules read at `7f50cae80f5372db7c278aef4ba4a0a05e1137ea`. L5-5: this saved dyadic lower endpoint is weaker than the reviewer bound `b_5=1.0225e-4` already cited in PD-T075 for the same polynomial and Taylor criterion; [audit-01/L5.md](../audit-01/L5.md) independently reproduced its scope. No new endpoint computation is claimed. Canonical ID is `PD-T?lanczos-frontier-codex-L5-04` (aliases old PD-T L5d, L5d). The audit reran the committed checker under both SymPy ground-types backends (flint and python); original receipts do not identify the developer's backend. Proof and certificate bytes are unchanged. The saved candidate draft first entered Git at `0574c47` before its prospective source gate was complete. Later completed reading does not cure or waive that deviation; acceptance remains AC's decision. The dated chronology and missing-read/gate checkpoints are in [gate-timing-response-01.md](../gate-timing-response-01.md). No novelty or priority claim is added.

## History addendum — 2026-11-05 (handoff10; A-P1)

This result descends from L5-01 full-kernel finite positive spanning, drafted before completion of the mandatory reading gate and first committed at `0574c47`. AC accepted the disclosed deviation on 2026-11-05. The deviation remains permanently disclosed, not waived and not cured. Completed-gate receipt: G5: `844e812`; these are publication SHAs, not worker input/rules SHAs. G5 was first preserved in ideas-l5-continuation blob `6b811daa2449644dcf81a5ca822f88e8e5f5cfa3`, not first at `b6bf1f6`. L5a/L5-01 shares `844e812` with that receipt; its reported gate-before-development order is not established by Git. Earlier pending-decision wording is historical and is superseded by this dated acceptance record. See [gate-timing-response-01.md](../gate-timing-response-01.md).
