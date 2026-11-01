# PD-T?proof-attempts-2-codex-53 — Uniform compatible-pattern gradient exclusion

Final ID: **PD-T178**. Provisional ID `PD-T?proof-attempts-2-codex-53` is retained as an alias. Registered after accepted Claude audit-01 and response-01; historical pending-audit notes below are superseded.

Canonical Split from (registration): PD-T100 / OPEN_TARGETS A5 (exact finite case, supporting result or separately OPEN obligation; source measurement retained).

ID kind: PD-T.
Aliases: A5 all_gradient leaf; exact background plus ambiguous derivative majorant.
Split from: degree-seven spatial coverage performance obstacle.
Split into: finite degree-seven count remains51.

## Statement

Let Q be a rectangle in the square, and L_i polynomial cardinals. Fix an inclusion-preserving interval for each L_i(Q). Let F contain indices whose cardinal intervals exclude0, with forced signs sigma_i, and A the remaining ambiguous indices. Put P_F=sum_(i in F) sigma_i L_i. For one physical coordinate nu, suppose interval G encloses partial_nu P_F(Q) and rational r satisfies

r >= sum_(i in A) sup_Q |partial_nu L_i|.

If0 is excluded from G+[-r,r], then Q contains no interior relative local maximum, strict or non-strict, of lambda=sum_i |L_i|. This holds for every degree and every finite coefficient field in a specified real embedding; exact creases and crossings are included.

## Definitions

Every compatible mask has the forced sigma_i on F and arbitrary signs on A. Node leaves and other predicates remain as in18; this is one additional direct whole-leaf predicate. Serialization uses {path,all_gradient:nu}. It asserts a universal inequality for all compatible masks, not that an arbitrary subset of them was checked.

## Assumptions

Exact coefficient identities, inclusion-preserving intervals, rigorous derivative absolute bounds, and strict exclusion of0. No sign decision or small nonzero derivative is supplied by a tolerance.

## Status by part

Overall status: **PROVED** (written supporting implication; required Claude audit PENDING). The degree-seven finite use has independently passed in51/52. No count is asserted by this lemma alone.

## Depends on

The every-active-polynomial comparison proved in18 and elementary interval inclusion.

## Checks

NewN7 implementation only. Each direct leaf records its coordinate and is independently verified by reconstructing P_F and all ambiguous derivative intervals. G may be the intersection of natural and centered mean-value intervals using exact first/second derivatives of P_F; the ambiguous derivative majorant remains natural. Existing cardinal bounds and compatible-mask order are unchanged. Counters distinguish direct all_gradient leaves from ordinary mask records. The separately implemented checker accepted all50412 such leaves in the complete degree-seven certificate, including their weak-global-maximum exclusion. Both the implementer's full verification and the different executor's fresh own full verification and developer-pair controls actually passed, with frozen source guards; exact receipts and commands are in51/52, independent-checks-a5-n7-checker.md and independent-execution-a5-n7.md.

## Sources

Registered A5 complete-pattern obligation. Refreshed registry53 gate is the N7 gate in T-A5-n7.md, including derivative/Bernstein/uniform/interval/crease synonyms. This is an exact universal-bound shortcut to the existing gradient test, no novelty or priority claim. It is introduced after the recorded ambiguity3/8 pilots showed boundary-strip cost, before testing its effect.

## Proof or evidence

For every compatible signed polynomial P_s,

partial_nu P_s = partial_nu P_F + sum_(i in A) s_i partial_nu L_i.

Triangle inequality and interval inclusion place every such derivative, at every point of Q, in G+[-r,r]. Strict exclusion of0 therefore prevents every compatible P_s from being stationary anywhere in Q. At an interior local maximum z of lambda, every active P_s is a local maximum and has zero gradient, because P_s<=lambda with equality atz. Every active mask atz is compatible by the cardinal interval inclusions. This contradicts the uniform derivative bound. No differentiability of lambda atz is assumed; polynomial P_s supplies the necessary condition even on creases/crossings. ∎

## Scope

Interior local maxima only. Boundary feasibility and maxima are still covered by separate exact edges/corners. This lemma does not assert that the inequality always succeeds or that a finite search terminates.

## Open items

Required Claude audit of Part2. Complete degree-seven finite use, independent implementation and actual independent executions are recorded in51/52. Success for other instances is not guaranteed by this implication.

## History

2026-11-01, Codex /root/a5_develop, allocated gpt-6.1-sol xhigh, rules4bd1d65. New N7 supporting predicate; all earlier-degree sources remain frozen.

2026-11-01 after13:33UTC: application checks synchronized after complete degree-seven independent acceptance, without changing this proof or any frozen code. Required Claude audit remains PENDING.
