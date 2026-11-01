# PD-T?proof-attempts-2-codex-10 — Degree-four strict local maxima count

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

Overall status: **OPEN** pending the final independent checker and actual different-agent producer/checker execution.

| Mathematical part | Status | Evidence / remaining obligation |
|---|---|---|
| exact13/12/2 count on respective strata | OPEN | producer completed with full certificate and zero unresolved; final checker and independent producer/checker execution pending |

The supporting finite-reduction and certificate-correctness theorems08–09 are separately PROVED; they do not make this count PARTIAL.

## Depends on

`PD-T?proof-attempts-2-codex-08` (quartic finite reduction including singular criticals); `PD-T?proof-attempts-2-codex-09` (spatial/edge certificate correctness). No part1 mathematical result is used. No cubic negative-definite necessity or blanket common-factor exclusion is used.

## Checks

Developer executed from repository root (all bytecode disabled):

```text
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a5_n4_boxes.py --boxes 200000 --seconds 600 --depth 40 --ambiguity 8 --certificate --boundary --output topics/padua-proof-attempts-2-20261101/outputs/a5_n4_certificate.json.gz
```

Python3.12.14; SymPy1.14.0; fixed outward dyadic precision96; no random seed. The mathematical decisions are deterministic. Producer hash `1d389bedef41bc08cf9cd008012870d9dc25eb4960c029020d235324b0afa4c0`; boundary producer hash `4cba7f4c8acb97127cc6ffa12a53bce88a093acfcb36b9ba1aba3b19dd9b70cb`. Separate checker: `../code/a5_checker_n4.py`, independently implemented without producer imports or search. Final checker hash/command/output and actual different-agent execution remain Runs needed until recorded below.

Developer essential artifact `../outputs/a5_n4_certificate.json.gz`: 64360bytes; SHA256 `14a69a131b3c20416fd5521bd971efdadd4e3741f70546d0fc5f0d9f25a2cf61`. Whole interior tree:5463 visited boxes,2732 final leaves,490672 supplied compatible-pattern dispositions (489824 gradient,714 flat,82 strict Hessian,52 root references),13 disjoint accepted root boxes. Every compatible pattern in every leaf occurs in the certificate's implicit sorted-mask order. Zero missing tree paths and zero unresolved leaves were reported. Search profiling counts include partial trial lists and are not the supplied-leaf counts.

Four edges have19,19,29,19 sampled actual sign masks after exact full-line arrangement norm-root isolation; squarefree norm degrees19,19,31,19. Supplied residual critical root dispositions:480 wrong-embedding derivative exclusions,100 strict tangent minima,78 incompatible signs,172 outside-open-edge roots,12 accepted edge maxima; no zero-normal or tangent-degenerate unresolved case. Four corners give two nodes and two all-active inward-descent maxima. Developer interior stage64.45s; boundary stage139.63s (timings are diagnostics, not proof predicates).

Preliminary independent interior checker execution by `/root/a5_n4_checker` passed2732leaves/490672patterns/13roots in33.69s against `/tmp/a5-n4-spatial-2.json.gz`. This supplements but does not replace final combined-certificate execution.

## Sources

Authoritative programme head `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e`, THEORY06 and A5. Closest IDEA048 / programme IDEA17. The source MEASURED n4 counts13interior/27total are a comparison only. No n6–8 disagreement or correction is inferred from the n4 case, and no contact with authors is authorized.

## Proof or evidence

The full finite certificate is produced. Theory09 proves that acceptance of its complete interior compatible-mask tree, every boundary arrangement/root disposition, disjoint root witnesses and all-active corner tests gives exactly the stated counts. All supplied positive interior witnesses verify strict signed-cardinal signs, negative definite Hessian and exact Krawczyk existence/contraction; all exclusion inequalities are valid for quartics. No regular-point or common-gradient-factor fallback predicate was required in this particular certificate. Thus singular-Hessian/common-factor possibilities were not silently discarded: every compatible mask was covered by a verified stronger predicate.

The count remains OPEN here until the final independent checker and actual separate producer/checker execution complete. Required Claude audit of the Part2 branch is distinct and still pending.

## Scope

Exactly degree4. No statement about n5–8, a universal formula, completeness of frozen floating searches, or historical novelty. Global argmax requires separate value bounds and is not inferred from the strict count alone.

## Open items

Final independent checker; actual different-agent producer and checker execution with separate outputs; file hashes and evidence manifests; required Claude audit. Optional A4(d) value certificate is result11.

## History

2026-11-01, Codex `/root/a5_n4`, inherited gpt-6.1-sol xhigh; rules readat95ca473cc21b2db6a9a46c62e86495ebe94eb397. Producer completed09:59UTC; exact candidate count written with OPEN status until final checks, preserving the original source MEASURED scope.
