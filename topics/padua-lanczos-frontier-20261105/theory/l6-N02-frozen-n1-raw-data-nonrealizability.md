# PD-N?lanczos-frontier-codex-L6-02 — The frozen fourteen raw n1 coefficients have no exact orthonormal-section realization

ID kind: PD-N.
Aliases: frozen raw-data symmetry obstruction; exact fourteen-slot nonrealizability; actual-n1 raw exact-match failure.
Split from: [PD-T?lanczos-frontier-codex-L6-03](l6-03-frozen-n1-output.md), separating the exact finite-data implication from the measured host execution.
Split into: none.

## Statement

Let D be the **unchanged fourteen raw coefficient scalars** in the fixed l6-02 n1 run, identified by the word-level producer receipt and independently reconstructed in `evidence/l6-n1-independent.json` (hashes in Checks). Interpret every binary64 word as its exact dyadic rational. These slots include all nine entries of Hx in the prescribed degree-one orthonormal gauge with polynomial order `(1,y,x)`.

There is no mass-one positive measure nu, anywhere in the plane, with finite moments through degree three and positive-definite degree-one moment matrix, whose exact degree-one orthonormal section data agree with all fourteen slots of D in that gauge. More basically, no normalized real functional L on `Pi_3` with `M1(L)>0` has exact orthonormal sections agreeing with those slots. The obstruction is already in two fully formed Hx entries, so it is independent of the C1 completion of the omitted Y column.

## Definitions

Exact degree-one orthonormal section means the symmetric projected multiplication matrix in the positive-leading orthonormalization of `(1,y,x)` for the functional or measure, as fixed by l6-02 and PD-T057. Equality here means exact equality to each unmodified rational slot, not equality within O(u). In particular, the stored coefficients are not reinterpreted as matrices in a nonorthogonal basis.

## Assumptions

The finite D is the one independently verified output at binary64 `u=2^-53`; its Hx words `bfce2b7dddfefa66` and `bfce2b7dddfefa67` occupy positions `(0,1)` and `(1,0)`. The fixed-gauge interpretation and all fourteen raw slots are retained. No input, precision, operation order, coefficient convention, completion, rescaling or correction is varied.

## Status by part

Overall status: **PROVED** (exact finite-data certificate plus the written necessary-symmetry argument; distinct exact trace reconstruction PASS).

| Mathematical part | Status | Evidence / limit |
|---|---|---|
| Fixed raw Hx has `Hx[0,1]-Hx[1,0]=2^-55` | PROVED for this finite output | Exact word interpretation, packed complete trace, distinct executed interpreter |
| No functional/positive measure has those exact orthonormal-section slots | PROVED | Multiplication sections are necessarily symmetric; proof below |
| Changed or toleranced raw data, positive nearby model, general PD-T056(G) | OPEN | Not rejected or decided by this equality obstruction |

Scoped claim disposition: **REJECTED: refuted** for the claim that the unchanged fourteen raw slots of this one frozen execution are exact orthonormal-section data, a sub-route of IDEA-262 / IDEA?lanczos-frontier-codex-L6-02. The necessary-symmetry violation refutes that exact-match claim only. The parent actual-run candidate remains deferred; it is duplicate as a mechanism and its corrected/toleranced target is not rejected.

## Negative-result scope

Attempted mechanism: regard the frozen raw fourteen-slot output directly as exact n1 orthonormal section data of a positive measure, without a consistency correction or residual allowance.

Parameter range: precisely the fixed nodes, row order, binary64 u, scalar contract, raw words and orthonormal-section gauge of l6-02. Support may be anywhere; the theorem does not require proximity to the original nodes. Thus no support optimization can overcome this exact raw mismatch. The result does not exclude a small correction, a toleranced positive model or a different actual run. It does not establish a nonzero lower support radius under an O(u) allowance, a PD-T145 perturbation family, or a universal actual-(G) obstruction.

## Depends on

The fixed l6-02 data map; finite trace and output certificate in l6-03; distinct word-level checker below. Only the necessary symmetry of real orthonormal multiplication sections is used analytically, proved directly. No sufficiency claim from PD-T070, arbitrary-data reading-(E) obstruction or external source is used.

## Checks

Producer `code/l6_n1_producer.py`, SHA256 `d001e22e4ed8713721c6af429d5089d6c462afef60f9835e3802f79f03738be5`; producer receipt `evidence/l6-n1-producer-receipt.json`, SHA256 `7c5ea62e8639a7bd0c5bb2743eb77697a0f99d56142cbca24d445d76e56b316f`; exact-analysis certificate `evidence/l6-n1-exact-analysis.json`, SHA256 `d34f67ec26873e04914ccc640554330f842fe2ad8717b995a0f5b65365c19aeb`; lossless essential trace `evidence/l6-n1-trace-packed.json`, SHA256 `81928b468a0b8a65483a438f2aec83e60c38993826b0bcac892932d06ca83b8e`. The finite reduction is the two-word symmetry witness in the proof, not an inference from a floating decimal comparison.

Distinct executed checker `code/l6_n1_independent.py`, SHA256 `269dfb1efe51edc5972509a600267991514c0cd7795881cf1a35a168894f2585`, independently generated all 367 primitive operand/result words and 47 states from integer IEEE encodings, including those two Hx words. Its compact executed receipt is `evidence/l6-n1-independent.json`, SHA256 `51216448294dfd4b15edd6a1ff44b9520b5ce148b855c1eaabb2aeb5d56bb45d`, **PASS**. Full commands, finite-input pins and norm/corruption controls are in [l6-03](l6-03-frozen-n1-output.md). The mathematical developer read both complete sources, methods/provenance and certificates after that distinct PASS and performed no extra scientific execution.

Durable independent execution/scope review: [independent-checks-frontier-05.md](../independent-checks-frontier-05.md), "L6 actual distinct exact trace execution", reviewer `/root/reviewer`, requested `gpt-6-astra` high, runtime metadata not independently exposed. Later required Claude audit remains pending.

The distinct reviewer subsequently read this entire finite negative record at SHA256 `8714cd12a6294517e8fd12bb52465928ce688b210694805527ca98d7e624432a` and its separate measured output record at SHA256 `8707e96c6c1997ef862395affb778f766f376f9f3c8ac65ed06a9d95f7e2eb0a`, independently decoded the two witness words and returned **PASS for the proof, exact raw-slot scope and PROVED/MEASURED split**. The present paragraph only adds that review metadata; the statement, assumptions and proof body are unchanged. No additional scientific execution was required or performed.

## Sources

Internal exact data and code above; PD-T057 for section conventions. No external theorem, priority claim or general reading-(E) negative result is imported.

## Proof or evidence

From the two certified words, exact dyadic interpretation gives

`Hx[0,1]=-4246034448350515/2^54`,

`Hx[1,0]=-8492068896701031/2^55`.

Their difference is

`(-2*4246034448350515+8492068896701031)/2^55=1/2^55!=0`.                  (1)

For any real functional L with `M1(L)>0`, let `p0,p1,p2` be its exact orthonormal polynomials in the fixed order. Its x-section entries satisfy

`H_x[i,j]=L(x p_i p_j)=L(x p_j p_i)=H_x[j,i]`.

Every product in this equality has degree at most three, so the stated finite moment assumptions suffice. A positive measure with nondegenerate degree-one moment matrix defines such a functional, regardless of where its support lies. Exact equality to the nine raw Hx slots would contradict (1). Since those nine slots are part of D, no exact realization of all fourteen exists. No choice of the remaining/completed Y column can alter the contradiction in already formed Hx. ∎

## Scope

The raw exact branch fails a necessary algebraic condition even though this finite run passes its complete residual and Gram budgets. Complete local O(u)-scale residuals at a fixed u do not by themselves supply exact structured data or a positive representing functional. This does not refute Greenbaum-style approximation, which may allow a specified residual or consistency correction. Neither correction/model searches nor support-radius claims are made here. PD-T056(G) remains OPEN, not PARTIAL or refuted.

## Open items

Parent-owned status/ID integration and later required Claude audit. A corrected/toleranced branch needs a separately tasked certificate and total-error/nontriviality analysis. No extra run is needed for the stated raw exact contradiction. The prospective correction/model branches in l6-02 remain unexecuted.

## History

2026-11-05, Codex mathematical developer, requested `gpt-6.1-sol`, xhigh; runtime variant/effort not independently exposed; rules `9825d184517db81d0aad8542fbd6639f2164b803`. Root assigned the finite statement after the one frozen run and distinct actual PASS. New substantive exact raw-data negative consequence split from the MEASURED output record, with no new mechanism: the symmetry stop was frozen in l6-02 before execution. The argument applies to the unchanged raw slots only; original PD-T056(G) scope/status is preserved. No Git/shared-registry change or additional scientific execution by this developer.

2026-11-05 audit-01 response, Codex statement/metadata worker; requested gpt-6.1-sol high; runtime variant/effort not independently exposed. Rules read at `7f50cae80f5372db7c278aef4ba4a0a05e1137ea`. L6-3: rejection applies to the fixed raw exact-match claim, not IDEA L6-02 or IDEA-262 as a whole; the broader corrected/toleranced continuation remains deferred. The [contract companion](l6-02-execution-metadata-20261105.md) points to its unchanged frozen correction/nontriviality rules and later execution. This finite negative descends from saved pre-gate L6-02; the exact-consistency stop was frozen before execution after the gate. The saved candidate draft first entered Git at `0574c47` before its prospective source gate was complete. Later completed reading does not cure or waive that deviation; acceptance remains AC's decision. The dated chronology and missing-read/gate checkpoints are in [gate-timing-response-01.md](../gate-timing-response-01.md). No novelty or priority claim is added.
