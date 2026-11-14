# Supplementary independent result check — D07 actual four-copy points

Rules/read input `084a64f6465956f9c75b5538f83752c30318f151`; rules and
registry unchanged at numerical input/release
`d4956aea3bda9d5ff9917a5b410778fc7adf4fb7`.
Reviewer `/root/d01_far_review`, parent-requested Astra xhigh; actual
serving metadata unexposed. Formal Claude audit remains separate.

## Verdict

**ACCEPTED at the stated finite point-measurement scope; no unresolved
finding.** A fresh independent build and driver executed all 13 fixed
point cases, all ten n<=128 finite references, all six invalid-input
controls and the single common-S context call. Every returned production
interval, radius and counter vector reproduced the author exactly; all
reference intervals and containment verdicts also matched exactly.

The complete fresh run used **12.008287 CPU seconds**, including the
supervisor, compilation and all waited descendants. Receipt processing
used a further 0.021041 seconds. The 120-second review allocation was
not approached. Generic n512 took **2.093014 CPU seconds**, passing the
preregistered <=10-second finite performance gate. This is an actual
separate execution, not a replay of the author's output or controller.

No universal O(n) runtime, uniform tightness, whole-box enclosure, new
degree certificate, comparison speedup or global argmax conclusion
follows. The three n512 calls have no independent full-board reference;
their validated source and exact reproducibility are the evidence there.
The common-S call remains context only.

## Preregistration, source and actual execution

Before any numerical call, the reviewer wrote the exact scope, pass/fail
conditions, output location and resource stops in
[PREEXEC.md](code/post_audit_D07_fourcopy_result_review/PREEXEC.md).
Its SHA-256 is
`7c1e5c7719d40509b5f657fbdb2b657ac4da6733a7fda64af653a00112173aca`.
The parent was notified before execution. The mathematical/source check
and closed F1/F2 findings remain documented in
[the source review](independent-checks-D07-fourcopy-source.md).
No new novelty claim or mathematical mechanism is introduced by this
consequential computational check.

Frozen numerical inputs were verified before and after:

| Input | SHA-256 |
| --- | --- |
| point.cpp | `03dc79bbbc7563ba9066137c0a52467624c810a758f865f9931511c82985ff6f` |
| controls.cpp | `5db13088e9fff85a134c95851337750ca03ea62be2f5d3ecf07e1f6e7d49c3fa` |
| author controller, provenance only | `af8d357badba85786fec088c735cc988f0950587d112e2e63a8d5b39cc14a9a5` |
| FREEZE.json | `c8b8e49e5c5af5ff520f00f8b7bac655a6c31cc132a5cb06cd87397c36fa33fb` |
| CASES.json | `fbfad19f2b6b00dd094b728716a3bcd7371ba0573321fd71c978dd5c06025d01` |
| author result receipt | `f6e574e8e9ce3523d2dfc257c9597e80b62973dd4b4d9f419a686dfd4b07206b` |

Executed once, exit zero:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-argmax-bridge-20261105/code/post_audit_D07_fourcopy_result_review/run.py

The independent [driver](code/post_audit_D07_fourcopy_result_review/run.py)
has SHA-256
`01234e8d306a2aa7ffe8fbb89b615ffbbc86dda6f1c252177186a248a804dec1`.
It imports the unchanged accepted builder with only its output directory
redirected. It never invokes the author controller, touches the author
registration, reuses its binary, or writes its result paths. The copied
translation unit still includes the unchanged actual point/reference
and C11 arithmetic sources. Precision and orders remain fixed.

The fresh binary is
`local-output/argmax-bridge-20261105/post-audit-D07/result-review/build/check-mzi8eqxp/libphase_checker.so`,
167808 bytes, SHA-256
`5d47a2399906ef2dc41244fea945ef0ad132b92d849f29b9e0c511b983810060`.
The manifest records the fresh preprocessed unit, g++14 Debian
14.2.0-19, four compiler tools, 13 toolchain dependencies, 230 source/header
entries and eight linked dependencies. The actual loaded dependency
identities matched before and after. Source, preprocessed unit, binary,
toolchain and dependency postchecks passed.

Separately, 300 recorded identity entries in the author's receipt,
raw manifest and loaded-closure records were verified against existing
bytes. This count includes repeated entries and does not claim 300
distinct files. The published evidence is JSON; no result CSV is listed
by this D07 point trial. Reading/verifying those historical outputs is
distinct from the independent execution reported above.

## Reference, API and finite performance results

The exact CASES inventory was used: generic, node and nonnode corner
at n=2,17,32; generic n=128; then generic and both axis points at n512.
The generic inward turns are xi=1/(16n), zeta=1/(32(n+1)); axis entries
set the respective coordinate to zero. The source-reviewed 512-bit
Chebyshev divided-difference reference uses its exact derivative at
rational-angle collisions. This reference shares neither the production
sine-ratio evaluation nor the root/partial-sum assembly.

Seven nonnode production Arb balls contain their complete finite
reference balls. The other three controls are exact physical nodes:
production is exactly [1,1], and its exact value is contained by the
reference ball. Only those node cases use the documented converse
exception. Overlap alone is never the acceptance test. The n128 generic
comparison passed with one numerical root-row fallback; all direct,
signed-block and partial-call counters reproduced the author.

All six invalid degree, domain and malformed-rational inputs returned
failure with three NaNs. No point outside the declared API was admitted.
There was no first numerical failure, retry, changed input, order or
precision. Source/root guards, full weighted C11 balls and finite-row
fallbacks are the same ones accepted in the source review.

| n512 point | CPU seconds | Native Arb radius | Numerical fallback rows | Eta-degenerate retained rows |
| --- | ---: | ---: | ---: | ---: |
| generic | 2.093014 | 2.5832150776591865e-16 | 3 | 0 |
| zeta=0 | 2.003413 | 3.073393623261679e-16 | 0 | 2 |
| xi=0 | 2.035292 | 1.0934878704314532e-15 | 0 | 0 |

The generic exported interval is
[25.032197529883806,25.03219752988381]. Its three fallback rows are
root-coverage failures, not omitted rows. All 514 physical rows are
included. The radii in the table are the native Arb-radius diagnostics,
not half the width of the outward binary64 endpoint intervals. Every
endpoint/radius/count value exactly matches the author receipt.

The n512 timing is the measured call within this fixed sequence, after
earlier cases have initialized the backend; the total run separately
includes fresh compilation and startup. No standalone cold-call or
asymptotic throughput claim is inferred. The axis timings also pass the
per-call stops, without suggesting that zero fallback on these two
points holds for arbitrary phases.

The single common-S context call took 0.600666 CPU seconds and reproduced
its recorded interval and counters. Its upper-context role is unchanged:
it is not an independent actual-lambda reference or a basis for a claimed
method-to-method speedup.

## Resource accounting and durable evidence

The independent supervisor verified Linux subreaper setup, enforced
110 CPU-second safety and 120 aggregate cap, used a 90-second reserve,
20/25 completed/unfinished-call stops, and a 240-second wall cap. It
waited the worker and completed descendant cleanup. Final accounting is
complete; no stopped or unreaped helper is hidden. The final CPU sample
follows the supervisor summary serialization and explicitly precedes
its own tiny final write/print. Stdout/stderr were separate immutable
files; both worker streams are empty. The one-shot raw checkpoints,
registration and closure records remain under the reviewer-only local
output subtree named above.

The [small independent receipt](evidence/d07-review-fourcopy-result.json)
is 10340 bytes, SHA-256
`07fb1b23f58c1149cb445538aada06922fac8166801448f017f62ea7b21c6a50`.
It pins the reviewer sources, build, full raw records, exact case
outputs/counts and all timing/containment dispositions. Its reproducible
postprocessor is
[summarize.py](code/post_audit_D07_fourcopy_result_review/summarize.py).
Bulk raw manifests stay local and regenerable; remote cold-storage
retrieval is not claimed.

No author source, earlier review, shared record or Git state was changed
by this reviewer. Only the assigned result report, disjoint reviewer
code/preregistration and short receipt were written. This closes the
requested independent finite computational check; formal Claude review
and broader evaluator/certifier objectives remain separate.
