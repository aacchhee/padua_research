# PD-T?proof-attempts-2-codex-10 — Degree-four strict local maxima count

Final ID: **PD-T165**. Provisional ID `PD-T?proof-attempts-2-codex-10` is retained as an alias. Registered after accepted Claude audit-01 and response-01; historical pending-audit notes below are superseded.

Canonical Split from (registration): PD-T100 / OPEN_TARGETS A5 (exact finite case, supporting result or separately OPEN obligation; source measurement retained).

Current audit note, 2026-11-01: Claude audit-01 accepted this record at its stated scope. Historical audit-pending statements below describe development checkpoints.

LITERATURE attribution (audit-01 F8): arXiv 2605.23299v1, §3.3 Table 3, LIT-388. Its reported counts are source statements; the local certificate/proof and candidate-correction scope are separate.

ID kind: PD-T.
Aliases: A5 n4 certificate; 27 closed-square / 13 interior maxima.
Split from: n4 case of `PD-T?programme-ideas-claude-06` / OPEN_TARGETS A5.
Split into: none. The n5,…,8 cases remain OPEN.

## Statement

For degree-four even-checkerboard Padua interpolation, λ_4 has exactly13 strict local maxima in the open square, exactly12 on its open edges, and exactly2 at corners. Thus it has exactly27 strict relative local maxima on the closed square. The edge counts in order `(x=-1,x=+1,y=-1,y=+1)` are `(3,3,2,4)`; the two maximum corners are `(-1,-1)` and `(1,-1)`.

## Definitions

Nodes are `(cos(pi*j/4),cos(pi*k/5))`, `0<=j<=4,0<=k<=5,j+k even`, lexicographic `(j,k)` order. The cardinal polynomials are the exact total-degree4 monomial Vandermonde inverse, with monomials ordered total degree then decreasing x exponent. λ_4=Σ|L_i|. Maxima are strict and relative to the physical closed square.

## Assumptions

Exact polynomial field Q(sqrt2,sqrt5); outward rational/dyadic intervals; complete finite certificate and independent checker. The source's measured list is not an assumption or a seed. Every case must be accepted without an unresolved record.

## Status by part

Overall status: **PROVED** (complete exact certificate, independent checker implementation and actual different-agent producer/checker execution; required Claude audit pending).

| Mathematical part | Status | Evidence / remaining obligation |
|---|---|---|
| exact13/12/2 count on respective strata | PROVED | complete exact certificate, independent checker and actual different-agent rerun passed; commands, identities and receipts below |

The supporting finite-reduction and certificate-correctness theorems08–09 are separately PROVED; they do not make this count PARTIAL.

## Depends on

`PD-T?proof-attempts-2-codex-08` (quartic finite reduction including singular criticals); `PD-T?proof-attempts-2-codex-09` (spatial/edge certificate correctness). No part1 mathematical result is used. No cubic negative-definite necessity or blanket common-factor exclusion is used.

## Checks

Developer executed from repository root (all bytecode disabled):

```text
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a5_n4_boxes.py --boxes 200000 --seconds 600 --depth 40 --ambiguity 8 --certificate --boundary --output topics/padua-proof-attempts-2-20261101/outputs/a5_n4_certificate.json.gz
```

Python3.12.14; SymPy1.14.0; fixed outward dyadic precision96; no random seed. The mathematical decisions are deterministic. Producer hash `1d389bedef41bc08cf9cd008012870d9dc25eb4960c029020d235324b0afa4c0`; boundary producer hash `4cba7f4c8acb97127cc6ffa12a53bce88a093acfcb36b9ba1aba3b19dd9b70cb`. Separate checker: `../code/a5_checker_n4.py`, independently implemented without producer imports or search. Final frozen checker SHA256 `1fe4f74ffe21447134e1c2f34e6364f3ca73929f207c7ebd8f3ea8977e53d143`. Its implementer actually replayed the full developer certificate plus global-value file in159.835996067s, exit0, with accepted/count_certified/global_argmax_verified all true (`../outputs/a5_checker_n4_developer.json`, SHA256 `1d98031e4c14c5f1150782a0013ff52bfbc1a0e1c576664bba70b6215e46b1d6`).

Developer essential artifact `../outputs/a5_n4_certificate.json.gz`: 64360bytes; SHA256 `14a69a131b3c20416fd5521bd971efdadd4e3741f70546d0fc5f0d9f25a2cf61`. Whole interior tree:5463 visited boxes,2732 final leaves,490672 supplied compatible-pattern dispositions (489824 gradient,714 flat,82 strict Hessian,52 root references),13 disjoint accepted root boxes. Every compatible pattern in every leaf occurs in the certificate's implicit sorted-mask order. Zero missing tree paths and zero unresolved leaves were reported. Search profiling counts include partial trial lists and are not the supplied-leaf counts.

Four edges have19,19,29,19 sampled actual sign masks after exact full-line arrangement norm-root isolation; squarefree norm degrees19,19,31,19. Supplied residual critical root dispositions:480 wrong-embedding derivative exclusions,100 strict tangent minima,78 incompatible signs,172 outside-open-edge roots,12 accepted edge maxima; no zero-normal or tangent-degenerate unresolved case. Four corners give two nodes and two all-active inward-descent maxima. Developer interior stage64.45s; boundary stage139.63s (timings are diagnostics, not proof predicates).

Preliminary independent interior checker execution by `/root/a5_n4_checker` passed2732leaves/490672patterns/13roots in33.69s against `/tmp/a5-n4-spatial-2.json.gz`. This supplements but does not replace final combined-certificate execution.

### Actual different-agent execution (completed10:16UTC)

Codex `/root/input_manifest` independently executed the frozen producer, separate global-value producer, final checker on its own regenerated artifacts, final checker on the developer artifacts, and all11 supplied positive/counterfeit controls. Its exact arithmetic used the pure-Python backend; no producer/checker source hash changed. Both complete checker receipts returned accepted=true, count_certified=true, boundary_complete=true, total27=13+12+2, global_argmax_verified=true and global_no_nonstrict_plateau_above_cut=true. The own-artifact checker took469.407148359s and the developer-artifact checker466.305697942s. These are actual executions, not inspection of the first output. Full commands, environment and chronology are in `../independent-execution-a5-n4.md`; analytic review is in `../independent-checks-a5-n4-reduction.md` and checker implementation/controls in `../independent-checks-a5-n4-checker.md`.

| Separate execution artifact under outputs/ | Bytes | SHA256 |
|---|---:|---|
| a5_independent_n4_certificate.json.gz | 64371 | 774910755f7213c5e7bb8392c6d0d93e120145e5c896772ec9814516ac6b6032 |
| a5_independent_n4_global.json | 4148 | bd5cf543aab16c80ee945c32a17e1827601ebf1cce1efdc160a7065e78b225e0 |
| a5_independent_n4_checker.json | 9357 | 55c86e23cedc47b6747da62337f05d990dc0fd7bc1489a3d3e9cc9590550e496 |
| a5_independent_n4_developer_certificate_check.json | 9357 | 32202bda458d3385fa054809903b34b2e9939e1c7289dc927115bc405b34aed3 |
| a5_independent_n4_controls.json | 1945 | 654dc65be0e02b667769abc43ceedfa3256fa63c7e00cd742b3e083ccaf0dd73 |
| a5_independent_n4_producer.jsonl | 1014 | c440e48f1f3abe1b7c0c739ebe0cc2ba0a1e0b21fdf758784a388026a2638836 |

The raw producer receipt contains progress and final-summary JSON lines. It was initially redirected to a .json filename and then renamed to .jsonl preserving every byte; the execution receipt records that chronology. Different gzip filenames/timings cause different compressed identities; all verified mathematical records agree. All essential artifacts are individually below1MB and no file was split.

## Sources

Authoritative programme head `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e`, THEORY06 and A5. Closest IDEA048 / programme IDEA17. Direct primary comparison on2026-11-01: arXiv2605.23299v1 (22May2026), printedpage9 §3.3 Table3, n4 row13interior/27whole-square, agrees with this certified result; bounded reading receipt `../outputs/a5_n4_literature-comparison.md`. The paper frames its table as numerical evidence, and its row is a comparison only, not a proof dependency or seed. No n6–8 disagreement or correction is inferred from the n4 case, and no contact with authors is authorized.

## Proof or evidence

The full finite certificate is produced. Theory09 proves that acceptance of its complete interior compatible-mask tree, every boundary arrangement/root disposition, disjoint root witnesses and all-active corner tests gives exactly the stated counts. All supplied positive interior witnesses verify strict signed-cardinal signs, negative definite Hessian and exact Krawczyk existence/contraction; all exclusion inequalities are valid for quartics. No regular-point or common-gradient-factor fallback predicate was required in this particular certificate. Thus singular-Hessian/common-factor possibilities were not silently discarded: every compatible mask was covered by a verified stronger predicate.

The final frozen checker and actual separate producer/checker executions recorded here all passed. By theory09 the count is therefore PROVED. Required Claude audit of the Part2 branch is distinct and still pending.

## Scope

Exactly degree4. No statement about n5–8, a universal formula, completeness of frozen floating searches, or historical novelty. Global argmax requires separate value bounds and is not inferred from the strict count alone.

## Open items

Required Claude audit of Part2 remains pending. The n5–8 cases remain separate OPEN targets. The separately proved A4(d) n4 value corollary is result11; source-record changes remain proposals for the orchestrator.

## History

2026-11-01, Codex `/root/a5_n4`, inherited gpt-6.1-sol xhigh; rules readat95ca473cc21b2db6a9a46c62e86495ebe94eb397. Producer completed09:59UTC; exact candidate count written with OPEN status until final checks, preserving the original source MEASURED scope.

2026-11-01,10:16UTC: upgraded OPEN→PROVED only after the frozen independent checker passed and a different agent actually regenerated and checked both certificate sets, replayed11 controls, and the separate analytic reviewer found no gap in08–11. Required Claude audit remains pending.
