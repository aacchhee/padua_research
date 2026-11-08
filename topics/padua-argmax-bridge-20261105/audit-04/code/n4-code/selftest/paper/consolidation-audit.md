# Manuscript consolidation audit

Status: final consolidated-source review complete; ACCEPT within the scope below.

Auditor: distinct Codex agent, requested Sol, max effort, at AC's explicit
request in place of the repository's default Astra audit allocation. Actual
serving-model metadata is not independently exposed. Rules and input head:
`971959024c038870c504322b485cc1dcf958e189`. Read `AGENTS.md`,
`agents/WORKFLOW.md`, and `agents/codex/CODEX.md`. The orchestrator alone
controls Git. This auditor owns only this file and makes no manuscript,
canonical-theory, evidence, or Git changes.

This is an architecture, exposition, and proof-fidelity review of an
already established manuscript. It introduces no candidate, mechanism,
priority claim, or status upgrade, so the IDEAS novelty gate does not
apply. It supplements, and does not replace, the pending substantive
Claude batch audit, native reruns, novelty/priority clearance, or publication
release obligations.

## Initial conclusion

The 88-page draft is an inventory of proof interfaces rather than one
integrated proof. A credible consolidation target is 42--45 total PDF
pages in the same Springer class, including references. It requires
rewriting the proof chain, not moving the existing appendices to an
unpriced companion file. No reduction in font size or display spacing
is proposed. The final page count must come from an actual build.

The main source of length is the repeated passage from finite rows to a
completed model, then from an absolute error to a matched relative error,
followed by several restatements of exactly the same scalar allowances.
The correct organizing principle is one common finite-row theorem whose
outputs are consumed once by the global comparison and certificate proof.
The corner expansion should likewise be presented once, with its endpoint
arguments at the point where they are needed.

The old PDF was inspected through `pdftotext -layout`. Its page starts are:
corner formula 6, sharp expansion 10, argmax 12, certificates 15, asymptotic
appendix 18, finite rows 30, pole estimates 47, cancellation model 55,
scalar estimates 58, quantitative assembly 69, references 87. These starts
confirm that a short main text concealed approximately 69 pages of proof
support. The target below counts all of that support.

## Page budget and unified route

| Component | Target pages | Required content |
|---|---:|---|
| Title, abstract, introduction, normalization | 4--5 | Two results, useful motivation, exact exceptional-mode coefficient, parity convention |
| Corner identity and sharp expansion | 9--10 | Exact row sum, uniform centering, harmonic/smooth quadrature, identification of kappa, half-step cancellation |
| Exact reflection and phase geometry | 1.5 | Common envelope, full defect, closed physical cover |
| Scalar model and central cancellation | 5 | Completed coefficients, scalar maximum with cusp atom, paired root estimate |
| One finite-row comparison theorem | 7--8 | Fixed cutoff 2, five-term telescope, absolute/origin/relative columns, actual retained rows |
| Defect floors | 2 | One selected-pair argument, parameter table for finite and tail requirements |
| Global scalar gates and corner patch | 5--6 | Near/wide/outer assembly, base checks and monotonicity, corner 256, far 192 |
| Finite certificate soundness and evidence boundary | 2--3 | Closed partitions, Peano/norm/corner predicates, degree inventory and arithmetic trust |
| Declarations and references | 2 | Short release statement and bibliography |

The allocation is approximately 42--45 pages with ordinary editorial
overlap between section breaks. The global lead should aim for about 24
pages before the separate certificate section. A 45-page target is an
acceptance goal, not evidence that the first rewrite will meet it.

Use the following interfaces rather than many historical result variants.

1. **Exact geometry.** With `m=n+1`, the corrected finite polynomial
   `G_n` and its periodic sum `S_n` satisfy
   `lambda=S_n-Delta`, `Delta>=max(Q_h,Q_v)>=0`, and
   `S_n(0,0)=Lambda_c(n)`. Endpoint multiplicities, closed-chart ties,
   both parities, and polynomial collision values are part of this one
   lemma. The two projected floors must never be added.
2. **One model comparison.** Define the completed polynomial in `L=log n`
   once, with coefficients `4a/pi^2`, `b_full`, `C_infty`.
   Set `u=1-a` and `T=(4L^2-3L)/pi^2`. Prove the coefficient loss,
   `C_infty-C_*<=-ju+t_0 sin(x)`, its central refinement retaining
   `E_c`, and the global upper `C_infty<9/4` together. Keep one
   scalar-profile proof of `H<=H(0)`; its negative periodic derivative
   atom is essential.
3. **One central correction.** Define the complete cancellation integral
   once. Combine the root-integral calculation, convolution argument,
   and rational root bounds into one proof of
   `E_c<=c_R*x^(3/2)-B_beta`. The half-radius column needs
   `c_R=3/8` and `B_beta>=1679*y^2/8000`; the wide column uses
   `c_R=5/12`. Do not split and bound the two channels before pairing.
4. **One finite-row theorem.** Fix the retained set of six actual rows
   and cutoff `R=2`. Write the exact error telescope once:
   ordinary rows + outer quadrature + retained rows + singular mesh +
   central scalar logarithm. Its statement gives only the outputs used
   later: a one-sided actual-origin error, matched relative errors on
   radii `1/2` and `1`, a full-phase norm allowance, and the correlated
   outer allowance. Derive them from one component table. The absolute
   and matched-relative outputs are both necessary; a large absolute
   norm cannot replace the cancellation in the near comparison.
5. **One defect argument.** State the folded interior-row normalization
   and periodic open-arc count once. The nearest, small-angle, and
   middle-angle center classes are exhaustive. A parameterized middle
   band/cap formula can serve the finite `41..319` floors and the sharper
   `n>=320` regional floors through a small constants table.
6. **One assembly.** Collect the half-near, annulus, wide, and outer
   scalar comparisons after all prerequisites. Only then prove the
   two-corner equality classification. The finite soundness proposition
   is a second consumer of the same reflection, floor, norm, and squared
   Peano lemmas, not another proof-development chronology.

## Specific deletions and mergers

| Original source | Action and preserved obligation |
|---|---|
| Introduction, preliminaries, argmax | Define the nodes and parity corners once; state the two main theorems once; shorten repeated explanations of samples versus continuum bounds |
| Corner formula and asymptotics plus Appendix A | Integrate statements and proofs; replace exact `1/(4n^2)` reference error by `O(n^-2)` if only the limiting constant is used; retain its parity-complete proof |
| Smooth asymptotic residual | Replace `17/n^2` and the strict sign of `beta_B` by the needed `O(n^-2)` conclusion; the sign proof is not consumed by the main theorem |
| Pole estimates | Specialize the public theorem to `R=2`; a temporary cutoff tending to infinity may still identify the endpoint constant inside the proof. Delete the otherwise unused general-cutoff theorem family |
| Pole and scalar estimates | Prove `Phi_0` bounds, reciprocal series, elementary quadrature, and periodic variation once; later arguments cite that lemma rather than repeat its derivation |
| Scalar maximum | Keep `H<=H(0)` and the cusp argument; the exact strict quadratic-drop coefficient and equality classification are stronger than their consumers need |
| Model and argmax-details | Merge the duplicated definitions of `J`, `Z`, `E_c`, and the root constants; state their complete domains once |
| Row and argmax-details | Eliminate repeated tables of `D`, mesh, `J_N/J_W`, `k_N/k_W`, and global norms; give one table at their definition and use named columns |
| Full-phase error | Retain the actual phase dependence needed for outer 320 and far 192, but do not present unused strengthened and historical uniform variants as separate results |
| Numerical constant | Use coarse certified consequences such as `9/10<kappa<23/25` and `C_*<1847/1000`, with provenance, in place of two repetitions of 30-decimal endpoints; preserve the computer-assisted dependency |
| Finite verification history | Remove seeds, server paths, control-degree history, individual leaf counts, archive byte counts, and full SHA displays from mathematical prose. Preserve them in the already existing reproducibility/evidence records |
| Traceability appendix | Keep the development mapping in repository documentation; publication prose uses mathematical names and a permanent code/evidence citation |

These cuts are changes of exposition and unconsumed auxiliary precision.
They do not authorize narrowing the all-degree theorem, assuming the
corner asymptotic is a finite lower bound, or weakening a quantitative
premise that is actually used by a retained certificate.

## Nonnegotiable proof and evidence obligations

**Finite floor gap identified in the input exposition.** The input row
appendix proves its three-class floor only for `n>=64`, whereas the
published phase-certificate description starts at 41. Inspection of
`code/final_hybrid_engine/checker.py` shows that `41..63` uses
`max(1/512,min(1/32,B_n(r_B)))`, `64..159` uses
`max(1/64,min(1/20,B_n(r_B)))`, and `160..319` uses
`max(1/32,min(1/20,B_n(r_B)))`. A generic statement assuming an abstract
valid `delta_B` does not itself prove these actual premises. The
consolidation must include the D29 floor/radius proofs and the C02 tiers,
or prove that its displayed replacement dominates every accepted
floor on the used domains. The canonical D29 records contain a short
finite open-arc argument; this is transfer of an established proof,
not new research. The original manuscript's inherited-theorem status
is not upgraded or downgraded by this observation.

The following quantitative distinctions are necessary:

- The half-radius `n=320` margin is only `1/20000`. Wide constants
  cannot replace the near column without a new valid gate calculation.
- Raising the analytic onset above 320 creates an uncovered interval.
  The existing finite certificates stop at 319. No new certificate
  campaign is authorized by a request to simplify prose.
- The far estimate from degree 192 and actual-corner patch from degree
  256 are used inside accepted finite certificates. They are not optional
  optimizations that can be removed from a complete proof.
- The `3H/n` correlated absolute-error saving and the ordinary
  cancellation coefficient six enter tight corner/outer budgets. If the
  same final constants are retained, their derivations must remain.
- `E_n(0)>=-bar_e` is a one-sided finite-origin estimate. The global
  absolute norm and limiting `C_*` cannot silently substitute for it.
- The relative outer error includes the scalar logarithmic correction
  exactly once. Its companion mesh charge is separate.
- Both tree and grid norms occur in the finite infrastructure. A tree
  containing an analytic far leaf requires the grid norm; numerical
  leaves alone may not contain a maximizer. Deleting one norm proof
  requires actual revalidation of affected witnesses, not prose alone.
- Squared-variable Peano interpolation applies to smooth signed sums,
  followed by the maximum over signs. It must not differentiate the
  nonsmooth Lebesgue function or substitute a sampled maximum for a
  global signed-sum norm. The finite certificate has the required
  `pi^2` Peano and `pi^4` corner factors.
- Near-proxy membership is not a premise for a full-box defect floor.
  Apply the floor only at an actual near point under its radius guard;
  retain tangent intersections and strict comparison at closed seams.
- The sharp asymptotic proof must preserve the exact `-1+2/m`, all
  endpoint rows, the nonzero smooth first correction, the summable
  trigamma endpoint contribution, and the shift `N=m-1/2`.

If 45 pages cannot contain a complete derivation of the retained
finite-row inequalities, the honest alternative is an explicitly priced
publication supplement containing the missing proofs, with its page
count reported alongside the article. That is not achievement of the
requested factor-two total reduction. Machine-readable certificates,
checker code, and reproducibility metadata are appropriate companion
artifacts; unchanged analytic appendix prose is not a hidden substitute
for a shorter proof.

## Initial coverage and commands actually executed

Read all main manuscript sections, the six proof appendices and source
mapping, the existing manuscript review/build records, and the relevant
canonical H, G01, E14/E15, C02, D29 floor/radius records. Read the exact
finite checker's floor, norm, corner, far, and partition interfaces to
identify which branches are actually consumed. This architecture stage
does not claim a fresh exhaustive reproof of every upstream constant.

Executed read-only file inventories, line/label searches, SHA-256 source
identification, and `pdftotext -layout` against the existing PDF. No native
certifier, new numerical experiment, compilation, code/evidence mutation,
or Git command was run by this auditor.

The input 16 source identities exactly match those already recorded in
`review.md` at source commit `a948b24c3faeba1e475ce64f4c7fc9d4123d42a5`;
they were independently recomputed in this session. In particular:

| File | SHA-256 |
|---|---|
| `main.tex` | `108186035fe08991fa1a847018a3778707a61c47dd32c975348a68ae5995ed5d` |
| `sections/row-estimates.tex` | `b6f153f90f607f907b014298f0d2f32ce78d1574db209db88330ec83228845ba` |
| `sections/pole-estimates.tex` | `31a72591e353f41d4733546eea71c36b4115570b99082cd64fa60049e36a7084` |
| `sections/model-estimates.tex` | `ecfe3fded8992321de4cc47d28a90dc019310f5b25e7f088a4944d2f666dc7cd` |
| `sections/scalar-estimates.tex` | `b70ca3383a2a71fcb93155a2eec5e8f8c0ee9cb41272ebb86887fbdeaf865f7f` |
| `sections/argmax-details.tex` | `2559fbbe7a2c4f1278cd4452bbc3bf27055a863c2f8d4c67444e20975f127620` |

## Final consolidation review

Completed after the restructuring, at AC's renewed explicit request for
Sol max review of correctness and redundancy. The final verdict, exact
active-source identities and measured artifact are recorded below. The
architecture-stage findings above are superseded where their resolutions
are stated; the separate research and release obligations remain.

### Additional steering: one small-degree certificate route

AC subsequently requested one certifier for degrees `1..40`. The
orchestrator assigned a separate small-degree worker. This is part of the
consolidation acceptance scope: describe the final route actually checked,
not historical solver names or a wrapper around unrelated certificate
semantics. Existing valid same-format witnesses may be reused honestly;
fresh native execution must be distinguished from exact rational replay.

Independent replay preregistration, before this auditor compiles or runs
the checker: inputs are exactly retained `n2.json.gz` through
`n16.json.gz` under `code/small_degree_unification/certificates/`, pinned
by the developer's frozen source manifest and `producer-summary.json`.
Compile the unchanged C++/GMP checker once into a fresh exclusive
`/tmp/padua-consolidation-small-review-*` directory, then run its unchanged
Python driver sequentially at those 15 fixed degrees with fresh outputs.
Compiler limit: 30 CPU seconds; each replay limit: 15 CPU seconds; each
process address-space limit: 4 GiB; file limit: 1 MiB. Aggregate process
group stop: 115 CPU seconds or 175 wall seconds, before the 120/180
envelopes. Stop on the first mismatch, failed exit, incomplete result,
source drift, or resource stop; no retry or precision/cap rescue. Exact
final source/input/output identities and actual exits will be recorded.
This small-degree common-route check is newly authorized by AC's
additional steering and remains separate from the pending whole-batch
native audit.

**First replay result: failure, no retry.** The unchanged checker compiled
successfully using GCC/G++ 14.2.0 and GMP 6.3.0. At degree 2 its Python
driver exited 1 with `ValueError: metadata x_cosine_seed`. The retained
producer witness records the seed interval `[-1,1]` at scale `2^192`;
the C++ checker overwrites the exact midpoint cosine with zero and emits
`[0,0]`. The strict metadata equality detects this mismatch before
acceptance. No degree `3..16` was replayed and no claim of accepted
common-route new evidence is made. Source and input prechecks passed.
Fresh output directory is `/tmp/padua-consolidation-small-review-1hhnptij`;
compilation consumed 1.729327 child CPU seconds, and the failed degree-2
driver 0.075171. This is a concrete compatibility issue for development,
not a failure of the original all-degree theorem. A new reviewed
compatibility disposition and fresh replay authorization are required
before continuation; this auditor made no source or witness change.

**Authorized compatibility variant, source review before execution.** AC's
orchestrator authorized a narrow reporting correction after that stopped
attempt. Independently read and reconstructed the two literal replacements
in `code/small_degree_unification/metadata-patch.json`: recompute the
original initial x seed using the existing rational Machin/Taylor routines,
then report that seed instead of the postreplacement `x[1]`. All other
native bytes match the baseline. The actual axis, cardinal coefficients,
thresholds, subdivision, and strict predicates remain unchanged. For
`n>=3`, no exact-axis override affects index 1, so old native output is
identical and accepted `17..40` evidence is unaffected. Certificates are
not rewritten. The new invocation wrapper calls the unchanged strict
loader/check and records the actual variant source and binary separately
from the baseline identities.

Before native execution, verified all five source pins and exact bytewise
patch reconstruction. Variant kernel: 6842 bytes,
`9b07d16a691261772e3057323dd3fb7e4934adf5bd2d6cb150f0f825db173667`;
wrapper: 2107 bytes,
`dfb3d3621fa2888e96033d8121f6486e9957fcdc54b40da219eb977bd6dd37b4`;
`METADATA-FREEZE.json`:
`99ec898e46825b1a8e3b3bf8ec1d6bb5dce6c3620d19020903e044c8b52723d6`.
Source review accepts this reporting-only compatibility correction.
Fresh replay preregistration: same limits as above and a new exclusive
temporary directory; compile this variant once, execute only degree 2
first, and proceed to fixed degrees `3..16` only after its actual strict
acceptance. Stop at the first failed predicate or resource guard. This is
an explicitly authorized new source candidate, not relabeling the failed
baseline attempt or silently retrying it.

Degree one admits the same Bernstein corner rule with a tiny exact
witness. Its nodes are `(1,1),(1,-1),(-1,0)`, with cardinals
`(1+x+2y)/4`, `(1+x-2y)/4`, `(1-x)/2`. Thus
`lambda_1=max(1,abs(y)+(1-x)/2)`, its norm is 2, and equality occurs
exactly at `(-1,1),(-1,-1)`. Split the square at `y=0`. On each
half the tensor degree-one Bernstein coefficient sums are 1 at three
vertices and 2 only at its unique nonnode corner. Positivity and
partition of unity prove strict exclusion off that corner in each
closed leaf. This is the existing corner-leaf mechanism specialized to
a routine affine case, not a new research mechanism. The actual checker
and witness implementation, its guards, and any main-theorem extension
to degree one remain for the assigned worker and orchestrator to adopt
and submit for final review.


**Independent compatibility-variant replay: PASS.** After the source
review above, compiled the new variant once into the fresh exclusive
`/tmp/padua-consolidation-small-metadata-review-_twddn_u` directory. The
compilation exited 0. The degree-2 pilot strictly accepted; only then the
fixed continuation at degrees `3..16` executed. All 15 direct exits were
0, with `accepted=true`, `complete_partition=true`,
`all_supplied_bounds_verified=true`, and exactly two corner leaves in
every result. Pre/post source and input identity checks passed. The actual
binary is 67584 bytes, SHA-256
`e35d6a80952d98edc1927f827346cc436d9f0da31837f9d000918aadada137c7`.
All declared resource guards held; compilation plus replays used
19.153825 child CPU seconds and 19.359040 wall seconds. This result does
not erase or relabel the stopped baseline attempt.

The complete off-Git execution receipt is 36259 bytes, SHA-256
`871629615eb61427ce7720bf062fcc6e4781a8bb1a5ae485f381cc4451e94668`.
The developer transcribed its compact retained counterpart,
[`checker-summary.json`](../code/small_degree_unification/checker-summary.json),
7367 bytes, SHA-256
`b3dfe4babf8acc9edd15bc1c5612d09be73bf0d671d1ec9f476c7d49abab1e15`.
Independently compared that compact summary to the actual receipt:
source/binary identities, compilation, all 15 input and acceptance-receipt
hashes, leaf counts, direct exits, per-degree CPU/wall observations and
totals agree. Independently checked all 39 raw witness identities in the
common index and their degree/producer flags. The latter is a static
inventory check, not native replay at `17..40`. The common mathematical
scheme and unchanged-predicate implementation cover `2..40`; the degree-1
affine proof is explicit, and the executable's `n>=2` guard remains.
The companion small-degree note accurately distinguishes these scopes.


### Final verdict, 7 November 2026

**ACCEPT for the requested consolidation and mathematical manuscript
review, under the explicitly stated computational premises.** Read every
active TeX source in full, including the complete compressed proofs rather
than only their interfaces. Rechecked the algebra and asymptotic endpoint
bookkeeping, the scalar/cancellation arguments, the finite-row telescope,
closed regional guards and certificate implications against the canonical
proof records. No unresolved substantive mathematical or proof-completeness
finding remains in this review. This is an independent reviewer judgement,
not formal verification or a claim to have rerun every numerical premise.

The actual root-built document is **46 total pages**, including declarations
and references, against 88 previously: 42 pages removed, a **47.7% reduction**
and a size factor of 1.91. It slightly exceeds the initial 42--45 page
allocation but honestly achieves approximately half the original size.
The actual Springer class, fonts and page geometry are retained. There is
no appendix or hidden analytic proof supplement in the compiled source
graph. The removed analytic support has been rewritten into the active
proofs, not relocated unchanged and omitted from the page count.

The final page starts are introduction 1, normalization 4, corner proof 5,
reflection geometry 13, completed model 14, finite-row theorem/proof 21,
selected pairs 34, near exclusion 37, outer/far comparison 38, actual corner
and global completion 40, certificates 42, references 45. The greatest
remaining cost is the single finite-row comparison proof; its absolute,
actual-origin and matched relative outputs are each consumed later.
Further major cuts would require a different proof or a reduced theorem
scope, rather than deleting an unconsumed historical branch.

The following proof obligations were checked in the final text.

- The corrected kernel has coefficient one in the exceptional mode, with
  a local Gram-matrix proof of unisolvence. Reflection, endpoint weights,
  the odd-chart cover and `Delta>=max(Q_h,Q_v)` use the same normalization.
  The projections are never incorrectly added. Phase folding preserves
  the unequal mesh directions.
- The corner proof retains its exact `-1+2/m` row identity, endpoint and
  collision values, the small-index sequences `S_e,S_u`, the nonzero smooth
  contribution, uniform endpoint quadrature, and the `N=m-1/2` transfer.
  They yield the actual coefficient `-1/N` and uniform
  `O(log N/N^2)` error for both parities. The identification of kappa and
  this expansion are analytic and do not assume the global maximizer.
- The scalar argument includes the negative periodic derivative atom.
  Its root formulas use complete cancellations and include moving equality
  roots. The paired convolution bound is proved through the closed radius
  `pi/2`, which the diagonal corner gate actually needs. The near and wide
  constants retain their different necessary strengths.
- The completed model is defined once. Its limiting constant is identified
  from an absolute error that is proved independently of the subsequent
  norm consequence, so that use introduces no circular norm premise.
  The coarse kappa enclosure now has its explicit coefficient series,
  uniform convergence and analytic tail in the paper; only the finite
  outward evaluation is imported from the retained arithmetic evidence.
- The fixed-cutoff finite telescope keeps all six actual rows, both meshes,
  linked collision limits, the exact endpoint reference and the central
  scalar logarithm once. Ordinary perturbations retain coefficient six;
  the uniform allowance retains the correlated `3H/n` saving. The origin
  bound concerns the actual finite value and is one-sided. Separate
  matched radii `1/2` and `1` feed the tight regional gates.
- The shared selected-pair proof covers both physical orientations and
  parities. In particular, it now proves the degree-41 floor and its
  radius-dependent refinement; the input draft's missing `41..63`
  justification is resolved. Every finite floor used in the `41..319`
  certificates and the stated control range is supplied. The unused
  `n>=512` special floor and its separate arithmetic paragraph were cut.
- The near, annular, wide and outer gates cover every closed phase diamond
  for every integer `n>=320`. The far implication from 192 and actual
  corner descent from 256 are proved because accepted finite certificates
  consume them. The corner gate uses the growing analytic norm inside its
  monotonic comparison; it never treats `M(256)` as a uniform tail bound.
- Positive interpolation is applied to smooth signed sums before the
  maximum over signs. The bilinear, global norm, squared-variable Peano
  and Bernstein corner predicates preserve strict exclusion off the
  designated vertices. The numerical-tree norm is restricted to wholly
  numerical trees; mixed analytic far trees use the independent grid norm.
  Near floors are restricted to their actual physical guards, and closed
  overlapping proxies preserve every seam and tangent.
- The finite range `2..319` and analytic range `n>=320` are consecutive.
  Degrees `2..40` now use one mathematical Bernstein scheme and a common
  strict implementation. Degree one is explicitly proved from its affine
  cardinals; the unchanged executable is not claimed to accept degree one.
  The main theorem remains stated for `n>=2`.

Findings corrected during the review were the initially absent actual row
definitions and their exact cotangent identity; the omitted degree-41
floor proof; the diagonal root-bound domain; the initially unspecified
kappa coefficient-series/tail reduction; and the strict entropy-derivative
wording at `p=0`. The last is now treated as the identically zero case.
Independently reconstructed the final comparison source backwards to
its previously reviewed `b59203e3...` identity: the last two source changes
are exactly that closed-boundary wording and renaming the separated
allowance. No additional mathematical change was hidden in the final pass.

Redundancy review accepted removal of the standalone discussion, repeated
main theorems, historical cutoff variants, unused smooth constants and
unconsumed special floor. A few short reminders of parity and of the
analytic/computational boundary remain useful locally. No further whole
lemma or proof branch is presently an obvious safe deletion: the apparently
secondary 192/256 regional results, norm alternatives and one-sided origin
estimate all have actual consumers. The one-page difference from the
initial target is not a reason to remove these obligations or compress the
font. No new research mechanism or numerical search was introduced.

### Final source and artifact identities

The orchestrator identifies the final active-source commit as
`eddf2276ad33937b69c4374b56510686c978e23a`. Git remained exclusively
under the orchestrator's control; this auditor independently read and
hashed the actual file bytes below. Paths are relative to this paper's
directory. Only seven TeX files are active; `localization-unified.tex`
inputs `comparison-unified.tex`. The bibliography is the eighth identity.

| Active source | Bytes | SHA-256 |
|---|---:|---|
| `main.tex` | 3406 | `0d9c3457d4c60078fc40a62fd6dc2e7d70b05d11681cd2f9646a99e9c695853f` |
| `sections/introduction.tex` | 7714 | `19c04f0575d1eba31970ef5cd4e2595575f330df70d64e7977b9657e15724b31` |
| `sections/preliminaries.tex` | 3818 | `908df5bcc7fb420f503782a4b3835723669fc39f4d5ea8bf3fdcb67b24364e58` |
| `sections/corner-unified.tex` | 19925 | `b84fb7768eac5aba32686d6f49a4baf9d6d75b81db2f5728a640288521983333` |
| `sections/localization-unified.tex` | 25115 | `f1b4765a363ffec5ba90c23ae9bb837289a1e31fd6c85e3b4eade9e6bcb46775` |
| `sections/comparison-unified.tex` | 59038 | `9b8c313be33fd609ed7563938aa31b5f20d49361f6a288e87d61a20161ae0ca9` |
| `sections/certification-unified.tex` | 8085 | `642e7c7ef48747f0432bcce9e3d27ba6c87411b8557ade5448ec2201a4b0f544` |
| `references.bib` | 3487 | `4f63b445f1b6de8ce0e670eada083934a8da5440a4ab7b18810d6433e36bbc65` |

Independently inspected the actual root-built artifact at
`local-output/padua-argmax-bridge-20261105/paper/main.pdf`:
628901 bytes, SHA-256
`7beea935ea68b0e7aaaf5b6bb0fad4d597eb256cdb27c8c0dc9a840901f78d2c`.
`pdfinfo` and text extraction confirm 46 pages. The corresponding log is
39864 bytes, SHA-256
`44bfa3a8d0ea9357ddfa27a9466c4db85801f1b92699a1121ae941fc17664d69`.
Its scan has no overfull box, undefined reference/citation, multiply defined
label, or LaTeX error. The active graph has 113 distinct labels, no missing
reference target, all ten citation keys present in the bibliography, and
no unexpected control bytes. The build was performed by the orchestrator;
this auditor inspected its artifact and log rather than claiming a
separate compilation.

### Independent computation and remaining boundaries

The separate newly authorized native replay is complete: every fixed
degree `2..16` strictly accepted under the source-reviewed metadata-only
variant, with 15 actual zero exits. Source, input, binary and receipt
identities and actual resource use are recorded above and in the retained
compact summary. The original stopped metadata mismatch is preserved.
All 39 witness raw identities for `2..40` were statically checked. Accepted
`17..40` native evidence was reused under exact source-output equivalence;
those cases were not rerun. There was no new kappa computation or full
phase-batch native rerun in this manuscript audit.

The result remains computer-assisted exactly where the paper says:
the finite outward kappa evaluation, finite polynomial certificates, and
phase-certificate numerical endpoints use the stated arithmetic and
implementation trusted base. The accompanying records carry source pins,
strict predicate reconstruction and the stated evidence-retention limits.
The full unsampled phase histories and permanent public code/data release
retain their separately disclosed status. This consolidation review does
not replace the pending whole Claude batch audit, any independently
outstanding native rerun obligation, novelty/priority clearance, author
disclosures, or publication preparation. None of those statuses is upgraded
by reducing the manuscript's page count or by this ACCEPT verdict.
