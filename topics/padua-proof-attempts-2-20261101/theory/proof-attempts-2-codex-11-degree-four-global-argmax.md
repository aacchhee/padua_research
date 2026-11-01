# PD-T?proof-attempts-2-codex-11 — Degree-four global Lebesgue maximum at the non-node corners

Final ID: **PD-T166**. Provisional ID `PD-T?proof-attempts-2-codex-11` is retained as an alias. Registered after accepted Claude audit-01 and response-01; historical pending-audit notes below are superseded.

Canonical Split from (registration): PD-T099 (finite global or exact edge/central-scope split; full-square all-n statement remains OPEN).

ID kind: PD-T.
Aliases: A4(d) n4; degree-four corner argmax; quartic plateau exclusion by value bounds.
Split from: n4 case of `PD-T?programme-ideas-claude-05` / OPEN_TARGETS A4(d).
Split into: none; all other degrees retain their separate statuses.

## Statement

For the degree-four Padua Lebesgue function λ_4 on the closed square,

max λ_4 = (13+sqrt2+2sqrt5+sqrt10)/5,

attained exactly at the two non-node corners `(-1,-1)` and `(1,-1)`.

## Definitions

The precise nodes, cardinal ordering, physical coordinates and strict-maxima certificate are those of result10. The global proof permits non-strict maxima and does not infer their absence solely from a strict local-maxima list.

## Assumptions

The complete degree-four count certificate and its independently verified predicates, plus the separate exact value certificate `a5-n4-global-v1`. Every used flat interior signed polynomial is bounded on its actual leaf; accepted interior and edge root values are bounded on their rigorous root enclosures. No cubic null-line or nonsingular-Hessian necessity is used.

## Status by part

Overall status: **PROVED** (separate exact value certificate, frozen independent checker and actual different-agent producer/global/checker executions; required Claude audit pending).

| Mathematical part | Status | Evidence / remaining obligation |
|---|---|---|
| exact value and uniqueness of the global argmax set | PROVED | every flat/root/corner bound independently checked and actually rerun by a different agent; receipts below |

The finite exact value predicates were accepted by the frozen checker and independently executed again by a different agent. The complete analytic argument is below; Claude audit remains pending.

## Depends on

`PD-T?proof-attempts-2-codex-09` (complete spatial and boundary certificate correctness) and the complete accepted n4 certificate of result10. No part1 mathematical result is needed. `PD-T?proof-attempts-2-codex-08` supplies the exact regular-crease exclusions inherited by09.

## Checks

Developer actually executed:

```text
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a5_n4_global.py topics/padua-proof-attempts-2-20261101/outputs/a5_n4_certificate.json.gz --output topics/padua-proof-attempts-2-20261101/outputs/a5_n4_global.json
```

Producer SHA256 `4dbba47a21a47137ea417a015895aa8c08538215827315da6a5f24caf0c98af3`. Output4148bytes, SHA256 `7bc43988a28848037f0b10b4e6c59cadb9dffa772e939175853e3769f7f6003a`, bound to count-certificate SHA256 `14a69a131b3c20416fd5521bd971efdadd4e3741f70546d0fc5f0d9f25a2cf61`. Python3.12.14 / SymPy1.14.0 / exact96-bit outward dyadic intervals, no random seed. The output's own hash and final independent checker receipts belong in the evidence manifest.

Observed exact inequalities: every714 flat interior leaf occurrence has signed-polynomial upperbound at most

195815277203118945162885237409 / 79228162514264337593543950336 < 4.

All13 accepted interior-root value intervals and all12 accepted edge-root value intervals have upper endpoint below4. The two non-node corner values agree exactly and are `(13+sqrt2+2sqrt5+sqrt10)/5 > 4`. Node corner values are1. All exact root ids and every flat occurrence must be replayed by the separate checker; an unchecked reported bound is insufficient.

The frozen separate checker SHA256 `1fe4f74ffe21447134e1c2f34e6364f3ca73929f207c7ebd8f3ea8977e53d143` actually passed the developer certificate/value pair in159.835996067s. A different agent, `/root/input_manifest`, actually regenerated both artifacts and executed this checker on both the independent and developer pairs, passing in469.407148359s and466.305697942s respectively. Both report global_argmax_verified=true and global_no_nonstrict_plateau_above_cut=true, all714 flat occurrences bounded, and exactly the claimed corner set/value. The independent value artifact is4148bytes, SHA256 `bd5cf543aab16c80ee945c32a17e1827601ebf1cce1efdc160a7065e78b225e0`; its checker receipt is `../outputs/a5_independent_n4_checker.json`, SHA256 `55c86e23cedc47b6747da62337f05d990dc0fd7bc1489a3d3e9cc9590550e496`. The developer-pair independent receipt is `../outputs/a5_independent_n4_developer_certificate_check.json`, SHA256 `32202bda458d3385fa054809903b34b2e9939e1c7289dc927115bc405b34aed3`. Full commands/environment/chronology: `../independent-execution-a5-n4.md`; separate analytic review: `../independent-checks-a5-n4-reduction.md`. These are actual executions, not rereading the developer output. Required Claude audit is separate and pending.

## Sources

Pinned programme OPEN_TARGETS A4(d), THEORY05 at `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e`; no general corner conjecture or floating experiment is inherited as a proof. No historical novelty claim.

## Proof or evidence

Let C=(13+sqrt2+2sqrt5+sqrt10)/5. Exact corner evaluations give λ_4(-1,-1)=λ_4(1,-1)=C>4. Continuity on the compact square guarantees a global maximum, of value at least C. We exclude any other location using the complete certificate, explicitly including non-strict maxima.

Suppose an interior z is a global λ maximum and s is active at z. For nearby w,

P_s(w)≤λ(w)≤λ(z)=P_s(z),

so P_s has a possibly non-strict local maximum at z. A gradient exclusion, a strictly positive diagonal Hessian entry, or strictly negative Hessian determinant excludes even a non-strict local maximum. All such predicates in the n4 certificate therefore remain valid for global maxima. A `root` leaf forces every stationary point to equal its unique accepted root, by injectivity on the hull of the leaf and root box; the separate value enclosure gives λ(z)<4, impossible. For a `flat` disposition, strict-maximality alone would be insufficient, but the separate bound P_s(Q)<4 on this actual leaf contradicts P_s(z)=λ(z)≥C. These are all predicates actually used by the complete n4 certificate. Thus no interior global maximum is missed through a ridge or plateau.

On an open edge, every actual cardinal crease is regular in the tangent direction by the exact multiplicity-one cover, and hence is not even a non-strict maximum. Away from creases the complete sign-pattern and derivative enumeration applies. Derivative, incompatible-sign, outside and strictly positive second derivative exclusions are valid for non-strict maxima as well. Each accepted tangent maximum with positive inward derivative is excluded, and each accepted edge maximum has value below4. If a restricted signed polynomial q is constant (`flat`), evaluate it at any interpolation node on that edge: exactly one cardinal is1 and the others0, so the constant is+1 or−1. This also lies below C. There are no unresolved zero-normal or degenerate tangent cases in the accepted certificate. Hence no open-edge global maximum remains.

The other two corners are exact nodes with value1. Consequently only the two displayed non-node corners attain the global maximum, and its exact value is C. Their strict local maximality is already independently covered by all-active inward-descent corner tests, although it is not needed to infer their attained global value. ∎

## Scope

Exactly n4. This finite value argument avoids extending the cubic non-strict maximum lemma to quartics. It does not prove the general n corner conjecture, a uniform neighbourhood estimate, or the n5–8 cases.

## Open items

Required Claude audit remains pending. No n5–8 or all-degree global result is inferred. The actual checker and separate execution obligations for this n4 result are complete.

## History

2026-11-01, Codex `/root/a5_n4`, inherited gpt-6.1-sol xhigh; rules95ca473cc21b2db6a9a46c62e86495ebe94eb397. The parent proposed value-bounding flat leaf cases as the quartic replacement for the cubic plateau argument; developer verified the route and produced a separate exact certificate. Original general A4 remains OPEN outside reached certified degrees.

2026-11-01,10:16UTC: upgraded OPEN→PROVED after the frozen checker and different-agent producer/global/checker executions accepted every bound and the separate analytic reviewer found no gap. The original OPEN development state is preserved in the preceding history and topic attempt; required Claude audit remains pending.
