# PD-T?lanczos-frontier-codex-L6-03 — One frozen binary64 n1 output has small complete residuals and inconsistent raw data

ID kind: PD-T.
Aliases: frozen actual-n1 output; fourteen-slot raw inconsistency; complete residual budget with failed exact-section consistency.
Split from: IDEA?lanczos-frontier-codex-L6-02 / IDEA-262's prospective actual-run test, under the fixed [l6-02 contract](l6-02-actual-n1-implementation-contract.md).
Split into: the exact finite raw-data nonrealizability implication is [PD-N?lanczos-frontier-codex-L6-02](l6-N02-frozen-n1-raw-data-nonrealizability.md). Execution and certified diagnostic observations stay here as MEASURED; no broader target is narrowed or upgraded.

## Statement

One actual execution of the frozen scalar binary64 n1 constructor produced the saved fourteen raw coefficient values D and square Q. At `u=2^-53`, the independently checked rational certificates establish

`det(Q)!=0`, `||Q^TQ-I||_2<=1/2`,

`||XQ-Q Hx||_2<=64u||Q||_2`, `||YQ-Q Hy||_2<=64u||Q||_2`,                 (1)

where `X=diag(0,1,0)`, `Y=diag(0,0,1)` and Hy is exactly the prescribed C1 completion of D. Both residuals in (1) contain all three columns, including the unformed `Yq2` column.

The same exact byte interpretation is **INCONSISTENT** as raw orthonormal degree-one section data. In zero-based indexing its fully formed Hx satisfies

`Hx[0,1]-Hx[1,0]=2^-55`, `Hx[0,2]-Hx[2,0]=-2^-54`.                     (2)

The constructor's 367 ordered primitive operations and 47 named stored states were reproduced exactly by a distinct integer/rational binary64 interpreter. This is one fixed finite output, not a uniform-in-u O(u) theorem. No correction branch, consistent moment reconstruction after the failure, PD-T145-family match or positive-model search was performed.

## Definitions

Input: unit-mass intended base measure on the ordered nodes `(0,0),(1,0),(0,1)`, scalar binary64 round-to-nearest/ties-even after every prescribed operation, basis order `(1,y,x)`, Y injection and X full products. Q is exactly the saved computed array, interpreted as dyadic rationals.

D consists of all nine formed Hx entries, the two nonzero slots of `j0=g0 e0+beta1 e1` and three formed j1 entries; the third j0 slot is a prescribed exact zero. The fixed exact completion is

`j2=(Hx j0-h0 j0-h1 j1)/beta2`, `Hy=[j0,j1,j2]`,

with `Hx e0=h0 e0+h1 e1+beta2 e2`. It is algebra on stored words, not an extra floating-point computation or a fitted correction. It forces `[Hx,Hy]e0=0`; it implies neither symmetry nor the complete structured-consistency conditions. All norms in (1) are spectral norms with conservative rational bounds, not exact norm values or ordinary floating SVD outputs.

## Assumptions

Only the fixed contract, source and input pins listed below. Raw data are not symmetrized or changed; the exact-match branch stops at the necessary symmetry failure. The construction's fixed orthonormal-section interpretation is not replaced by a nonorthogonal basis or a different coefficient map. The measured host trace is distinct from the exact finite-data implication in l6-N02.

## Status by part

Overall status: **MEASURED** (one actual host execution, exact finite trace/certificate reconstruction independently PASS).

| Part | Status | Evidence / limit |
|---|---|---|
| Frozen host output and 367-operation / 47-state trace | MEASURED | Actual producer execution and distinct exact interpreter agree word for word |
| Rational Q, complete residual and consistency diagnostics for that output | MEASURED, certified for this finite instance | Exact analysis plus distinct rational reconstruction; all complete 64u budgets PASS, raw branch INCONSISTENT |
| Exact nonrealizability of the fixed raw orthonormal-section slots | PROVED separately | l6-N02; elementary symmetry implication from the independently checked finite witness |
| Toleranced/corrected positive model and general PD-T056(G) | OPEN | No correction/model search; no status upgrade from these supporting finite observations |

Candidate disposition: the **raw exact-match branch** of this one frozen execution stops INCONSISTENT. The broader deferred IDEA-262 / actual-(G) target is not rejected.

## Depends on

The l6-02 operation/data contract; producer and distinct checker listed below; exact IEEE word interpretation; elementary rational norm inequalities. PD-T057 supplies the section convention. Necessary section symmetry is proved directly in l6-N02 and does not require importing a sufficiency statement from PD-T070. The l6-01 family-specific theorem is not applied, because no PD-T145 match was established.

## Checks

Mathematical developer read the complete producer (168 lines), independent checker (275 lines), methods, pre-start provenance, producer receipt, exact-analysis certificate and independent receipt after the distinct actual PASS. The completed reading gate for this saved route is [ideas-l6-continuation.md](../ideas-l6-continuation.md); this is an executed test of that route, not a new mechanism or priority claim.

| Essential input / evidence | SHA256 |
|---|---|
| `code/l6_n1_producer.py` | `d001e22e4ed8713721c6af429d5089d6c462afef60f9835e3802f79f03738be5` |
| `code/l6_n1_independent.py` | `269dfb1efe51edc5972509a600267991514c0cd7795881cf1a35a168894f2585` |
| Reviewed fixed contract l6-02 | `9d857e30146be3e2f8963f20cf89a4441fa72b1b542a5dcb79245384198e3a35` |
| [Pre-start provenance](../evidence/l6-n1-start-provenance.json) | `e6d1a410a9f0862a02b2dd9623f5159100689d3125b121772c835faec0819ef3` |
| [Producer receipt](../evidence/l6-n1-producer-receipt.json) | `7c5ea62e8639a7bd0c5bb2743eb77697a0f99d56142cbca24d445d76e56b316f` |
| [Exact analysis](../evidence/l6-n1-exact-analysis.json) | `d34f67ec26873e04914ccc640554330f842fe2ad8717b995a0f5b65365c19aeb` |
| [Lossless packed trace](../evidence/l6-n1-trace-packed.json) | `81928b468a0b8a65483a438f2aec83e60c38993826b0bcac892932d06ca83b8e` |
| [Distinct executed checker receipt](../evidence/l6-n1-independent.json) | `51216448294dfd4b15edd6a1ff44b9520b5ce148b855c1eaabb2aeb5d56bb45d` |

The packed trace reconstructs 69921 original bytes with SHA256 `c3f9950dc198f17fde858d887bde0a4ebf61713c64145e5e4d44291c908eff5c`. It preserves the complete essential finite operation trace, including operand/result words and exact-target annotations; no temporary file is the sole evidence for (1) or (2).

Before the first primitive, source/plan/contract, input arithmetic, invocation and caps were persisted separately. Actual execution head: `60126006dcc7c814680ed87d4fef8d9f9404a3d7`; rules remained `9825d184517db81d0aad8542fbd6639f2164b803`. Actual producer command from repository root:

```sh
timeout 60s python3 topics/padua-lanczos-frontier-20261105/code/l6_n1_producer.py --out /tmp/padua-lanczos-frontier-l6-n1/producer
```

Python 3.12.14 scalar binary64; producer receipt status is completed (not INVALID_OR_CAP), elapsed 0.027141867 seconds, 13440 KiB peak RSS. Every producer primitive passed exact midpoint/ties-even checks. The producer's original receipt preserves "independent verification PENDING" as its historical emission; the later separate independent receipt supplies the completed PASS.

Distinct reviewer `/root/reviewer`, requested `gpt-6-astra` high (runtime metadata not independently exposed), first reviewed the pinned source and interpreter, then **actually executed** an independently written exact interpreter with no producer helper imports:

```sh
timeout 60s python -B topics/padua-lanczos-frontier-20261105/code/l6_n1_independent.py --producer-root /tmp/padua-lanczos-frontier-l6-n1/producer --out /tmp/padua-lanczos-frontier-l6-n1-independent/run --receipt topics/padua-lanczos-frontier-20261105/evidence/l6-n1-independent.json
```

Exit 0; elapsed 0.123643894 seconds. It independently generated the full flow from exact binary64 encodings, reproduced every operand/result word and state, rebuilt raw D/Q, C1, all residual entries and the omitted Y column, and verified producer norm endpoints by exact squaring. Distinct conservative enclosures used Gram maximum absolute row sums, residual column lower/Frobenius upper bounds and outward rational square roots. Normal/subnormal ties-even and signed-zero controls passed. Five corrupted controls were rejected: changed primitive result, omitted primitive, altered C1 column, altered omitted-Y residual and invalid zero residual upper bound. The original then passed again.

Durable review: [independent-checks-frontier-05.md](../independent-checks-frontier-05.md), "L6 producer pre-execution source review" and "L6 actual distinct exact trace execution". Details and historical prelaunch plan are in [l6-n1-methods.md](../l6-n1-methods.md). No additional scientific execution was performed by the mathematical developer for this record.

After these finite records were written, the same distinct reviewer read both full records at l6-03 SHA256 `8707e96c6c1997ef862395affb778f766f376f9f3c8ac65ed06a9d95f7e2eb0a` and l6-N02 SHA256 `8714cd12a6294517e8fd12bb52465928ce688b210694805527ca98d7e624432a`, independently decoded the two-word witness and returned **PASS for finite statement, scope and status**. The measured host output is correctly separated from the proved exact raw-data implication, and neither rejects corrected/toleranced (G). This review-metadata paragraph is the only post-review change; no statement, evidence, diagnostic threshold or proof changed. Later required Claude audit remains pending.

## Sources

Internal contract, code and certificates above; PD-T057/070 as context for consistent orthonormal sections. No external source is used as proof and no novelty claim is made.

## Evidence and finite interpretation

The exact trace comparison connects the observed host output to the fixed scalar contract. The rational analysis then interprets those output words without additional rounding. Nonzero detQ and rational Gram/residual certificates establish (1). The residuals explicitly include `Yq2-Qj2`; the C1 completion is not treated as a residual bound by itself.

The four relevant Hx words are `Hx[0,1]=bfce2b7dddfefa66`, `Hx[1,0]=bfce2b7dddfefa67`, `Hx[0,2]=3fda20bd700c2c3e`, `Hx[2,0]=3fda20bd700c2c3f`. Exact dyadic interpretation gives (2). Three additional nonzero symmetry witnesses are retained in the certificates. C1's first-column commutator is zero; its row zero is nonzero, so the full interior consistency condition also fails. Symmetry failure already decides the raw exact branch, independently of that additional diagnostic.

## Scope

At this fixed u and these exact words, small complete local residuals and small Gram error coexist with failure of exact structured section consistency. Neither (1) nor the presence of a commuting original X,Y supplies a positive section functional. The separate exact nonrealizability is an equality claim for unchanged raw slots in the prescribed orthonormal gauge; it is not a lower bound on a toleranced model radius, a rejection of the corrected branch, or a refutation of general (G). There is no PD-T145 match, inferred e/u separation, nearby measure, Padua n3/4 result or all-precision IEEE statement.

## Open items

Parent-owned status/ID integration and later required Claude audit. No additional experiment is required to finalize this frozen raw stopping outcome. A corrected/toleranced branch or new n1/n3/n4 instance needs a separately authorized contract and its own consistency, total-residual and nontriviality certificates. PD-T056(G) remains OPEN, not PARTIAL.

## History

2026-11-05, Codex mathematical developer, requested `gpt-6.1-sol`, xhigh; runtime variant/effort not independently exposed; rules `9825d184517db81d0aad8542fbd6639f2164b803`. Root assigned finite statement preparation after distinct actual PASS and source/certificate reading. The producer and distinct checker are different agents; their actual commands and outputs are recorded above. This file was written after the frozen execution and independent PASS, not presented as a pre-run plan. The prewritten exact-consistency stop was already in l6-02. Original early-draft gate timing remains disclosed in the attempt/candidate record. No Git/shared-registry edit by this developer.
