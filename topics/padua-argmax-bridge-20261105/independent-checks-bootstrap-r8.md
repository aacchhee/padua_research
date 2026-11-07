# Supplementary independent review — N3 maximum-bootstrap cover, round8

2026-11-06. Rules/input `8dc1521cf68f7780bd10e02495f6f71a639c03c6`.
Distinct reviewer `/root/review_bootstrap_r8`, coordinator allocation Astra
high; serving model/effort metadata is not independently exposed. This is
a supplementary mathematical/source check, not the required Claude audit.
Only this report, its new controls and its small evidence receipt are owned
by this worker. No Git operation, author proof edit or old receipt edit.

## Scope and identities

Read AGENTS, WORKFLOW, CODEX role, handoff04, the complete PD-T227,
PD-T251 and PD-T364 proofs, round7 bootstrap proof and its independent
review, phase-checker reduction, round6 report, new source and author gate.
Full `state/IDEAS.md` was not reread: this review checks mathematical
sufficiency, source semantics and finite controls, and makes no novelty or
priority judgment. The author gate records its complete registry scan,
obstruction/disposition reads, searches, shortlist and variant distinction;
that recorded scope is inspected, not independently certified as exhaustive.

Author-frozen source identities, checked against actual bytes:

| Source | SHA256 |
|---|---|
| code/n3_bootstrap_r8.py | 9058deac09eec2ddd7cfae4815fdf79d702e52099de13820e44af4f82db0a12c |
| code/phase_checker/check_r8.py | 3c71ada8e49829cb897ee1c064fcdc70d08c846afcb1fb067c6c84673e205bb9 |
| code/phase_checker/r8_controls.py | 13cdf5da05e1ce31416dc5685b0be1c8c3565feb2e3606675607be7c1fc56944 |

The complete author-frozen theory N3-bootstrap-cover-r8.md has SHA256
1353085bfe6cf4190774647d182b27baf950fb0a42eaddddc313008ceb01446d.
It was read in full and agrees with the independent reconstruction below.
The gate/attempt hashes are a4a7b266dddf27a4d66fbc37d6796f185b0bc8ed1c432bbf6cb8c8d9d191bcc7
and55ccba8e64e1e0d8357827cda2d9e24f3003d2311a4f86772db699e342a96e22.
These prose hashes identify this review only, never runtime proof guards.

The imported old check_r6.py remains437378a5..., build_snapshot.py remains
19a5a7c2..., and hybrid_kernel_v2.cpp remains17fea91d4fa02e4183823e5d70b44705e96da7acfd26b04a0f3ed1cac443d9a2.
The producer C remainscfeae9fe... and its interval header6dca513d..., matching
the existing frozen evidence. Old pointwise checker/arithmetic sources are
not widened or rewritten. The receipt supplies the full new/source hashes.

## Independent mathematical reconstruction

PD-T364 covers every point of the physical angle square by an admissible
odd-center phase chart: in any mesh rectangle the distances to its two odd
vertices sum to2, so at least one is<=1 in normalized units. This includes
edges, nodes and ties. Endpoint centers impose alpha>=0 at J=0,
alpha<=0 at J=n, beta>=0 at K=0 and beta<=0 at K=n+1. A box covering
additional nonphysical phases remains safe; excluding a center requires
that its whole physical intersection be absent.

The unchanged Arb kernel computes all projected profiles and minimizes over
all odd noncorner physical centers. It omits endpoint centers only on
strictly wrong-sign boxes, retaining the zero boundaries. Its lower Delta
bound therefore applies to every admissible noncorner chart. For every
nonfar bootstrap leaf, the exact checker inequality S_upper-Delta_lower
<Lc_lower supplies strict comparison for those centers, including phase0.
No representative-center sample or corner-only energy estimate replaces it.

There are exactly two odd endpoint-pair centers: (n,n+1), together with
(0,n+1) for even n or (n,0) for odd n. Only these are the actual nonnode
corners. At such a center the physical inward increments are
h_x=1-cos(|alpha|/n), h_y=1-cos(|beta|/(n+1)). Thus if the complete box has
maxabs(alpha)+maxabs(beta)<=1/2, any nonzero phase satisfies

    0<z=n^2(h_x+h_y)
      <(alpha^2+(n/(n+1))^2 beta^2)/2
      <=(|alpha|+|beta|)^2/2<=1/8.

Both closed diamond boundaries and axes are covered. In this domain z=0
occurs precisely at alpha=beta=0; the inward corner signs do not introduce
another zero. Node corners belong to other, nonzero-phase chart boundaries
and have cardinal value1, not an additional equality exemption.

Independently recovering the absorption step from PD-T227 and PD-T251:
with the fixed energy premise W<=(3/4)n^4 Lambda_c and true global norm M,

    lambda<=Lambda_c(1-z/8+3z^2/8)+M R(z),
    R(z)=exp(z)-1-z<=4z^2/7<=1/112.

On0<z<=1/8, z/8-3z^2/8-R(z)>=3z/448>0. At a putative global maximizer
only, lambda=M, giving M(1-R)<Lambda_c(1-R), impossible since M>=Lambda_c.
This argument retains the true unknown norm in the remainder and never
uses M=Lambda_c before global closure. Zero-cardinal derivatives enter the
full slopes; their omission from W is exactly PD-T227's nonzero mask.
Parity-valid reflection transfers the same energy/slopes to the second
corner.

Now choose an attained global maximizer. Every representing chart is
covered by a full accepted tree. Outside leaves contain no physical phase.
Far/ordinary defect/orbit leaves give strict comparison. Old local leaves
give strict actual-corner comparison away from their corner and strict
noncorner comparison. New bootstrap leaves give strict noncorner comparison
and exclude nonzero-phase actual-corner maximizers. The maximizer must
therefore be one of the two actual corners. Equal corner values establish
M=Lambda_c; any other point with that value would itself be an excluded
global maximizer. This proves the exact equality set, not merely existence
of a maximizing corner. A partial cover proves none of this closure.

## Source and premise inspection

The new format/mode/kind are explicit. `bootstrap_range` uses exact
Fractions of finite numeric endpoints and tests the sum of endpoint maxima,
not the separate square tests. It rejects reversed/malformed boxes and
noninteger/bool/out-of-range degrees. The fixed receipt is
f0c48ea7f55e3a926b36537ebe46724b4305cacb9f1254c6417b2abd9676425b;
source/runner pins3646f4e8.../915c6c7c..., all127 integers2..128, threshold3/4,
independent execution flags, exact new predicate and evidence identity are
validated. A caller descriptor neither selects a receipt nor supplies the
premise. Runtime guards read fixed code/evidence, never theory prose.

The full four-root prefix partition rejects duplicates, ancestors,
uncovered siblings and absent roots. Paths reconstruct the declared
binary64 midpoint operation; stalled splits fail. Roots must enclose the
independent pi upper bound. Outside uses strict exact minimum-distance
comparison. Pending leaves and bounded replays cannot accept. Unknown
accepted-leaf kinds, old schema, wrong mode and false completeness fail.
Numeric candidate leaf bounds are ignored and recomputed using Arb/GMP.
Final strict subtraction is exact rational; equality cannot round into a
pass. The existing n>=48 defect enhancement retains its full-box1/10 guard.

Before freeze the coordinator found that the unchanged MPFR C early exit
could skip defect calculation whenever the old local flag was false and
corner_upper>=Lc. That was a completeness/performance problem, not false
independent acceptance. The frozen response adds explicit
`producer_bounds(..., always_compute_defect)` and passes oldlocal OR
bootstrap_geometry only to request calculation. Inspection of the complete
C source finds that flag used solely in the early exit at line39. The
legacy local acceptance branch still uses oldlocal alone; the bootstrap
branch retains its distinct kind, geometric condition and strict defect
comparison. No pointwise theorem is asserted by the calculation flag.
The compact projection removes only diagnostic numeric leaf fields and
preserves format/mode/premise/root/path/kind metadata; its own bytes require
full independent replay.

## Executed independent controls

Actual command:

    python topics/padua-argmax-bridge-20261105/code/phase_checker/r8_independent_controls.py

Final control source SHA256397a1fbe740d2bccaf9626f89832cd95e59bf0a8dc3ab0dfc40674920a64763a.
**105 checks PASS, exit0**, final own CPU0.973762735s and waited child
CPU1.565174s. An earlier102-check version also passed before the separate
producer-flag integration was added (own0.261313678s, child1.143212s).
Total controls remain well below the120CPU-second budget. No full cover
or energy sweep was executed by these controls.

The small receipt `evidence/bootstrap-r8-review.json` records all labels,
actual signed boundary boxes, numerical outputs, compile command and hashes.
Synthetic bounds exercise parser/partition/branch semantics only and are
explicitly not numerical proof. Controls reject strict equality and a
one-ULP smaller defect whose exact subtraction lies above equality; changing
the bootstrap leaves to the old local kind fails, showing no radius widening.
All four signed closed quarter-by-quarter boxes pass the half-diamond guard
at degrees2,3,32,127,128; one-ULP-outside endpoints fail.

A fresh unchanged Arb build evaluated six n2 boxes, including origin,
all four signed quarter boxes and the closed half-axis endpoint. All bounds
are finite. At origin its corner interval encloses exact3 while
S_upper-Delta_lower<Lc_lower for noncorner centers: the origin is not a
blanket noncorner equality exception.

A separate fresh MPFR build tested n32 box[-.25,0]x[0,.25], which is inside
the bootstrap diamond and outside the old local patch. Both flag settings
return identical S_upper12.01904528050516 and corner_upper11.967214606614945.
The old early exit returns defect0/computed-marker0; the explicit request
returns defect0.31109586590547306/computed-marker1. These are calculation
controls, not a valid accepted leaf or an independent arithmetic input.

## Focused guard finding and developer response

MINOR specification mismatch, reported to the coordinator before any fix:
the initial checker427c93ad... compared n2_control dictionaries by equality,
so its private semantic helper accepted both_enclosed=1,
zero_cardinals_omitted=True and nonzero_cardinals=5.0. The fixed production
receipt SHA already rejected every such changed byte snapshot. This was no
false-certificate or mathematical finding, but it contradicted the explicit
exact-type specification. No author proof/source was edited by this reviewer.

The developer added `is True` and exact `type(...) is int` guards and
refroze the final checker3c71ada8.../developer controls13cdf5da... listed
above. Independent focused execution rejected six bool/float/false aliases
and accepted the actual published premise:7/7 PASS, CPU0.000814222s.
The evidence retains the original105-check source identities and separately
records these final response hashes/results. The unchanged arithmetic was
not rerun for this metadata fix. Finding disposition: **resolved**.

## Prereplay disposition

**ACCEPTED before calibration:** the frozen mathematical sufficiency
reduction, source/interface semantics and independent negative/boundary
controls have no unresolved finding within this scope. The coordinator may
release its one preregistered n32 calibration. No full n32 producer or
checker run has been executed by this reviewer, and this review does not
claim a completed certificate. Required Claude audit remains pending.

If the coordinator releases the one n32 calibration, the proposed checker
command is check_r8.py on the exact frozen n32-phase-compact.json, with
`--kernel round5 --output` to a new raw replay, and no `--max-leaves`.
A separate launcher must enforce<=1200 total child/process CPU seconds,
record compiler/build-helper and checker CPU, exact argv, input/source/hash
closure, all leaves, zero pending/failed leaves and actual exit status.
Any failure, incomplete tree or cap stops the block; no internal rescue,
retry, n64/128 job or degree-range claim follows. A full pass would validate
only known n32 and measure cost against the reviewed round6 baseline.
