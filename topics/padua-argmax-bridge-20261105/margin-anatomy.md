# B1 finite margin anatomy

Status: MEASURED finite diagnostics completed after coordinator B0 PASS. Developer: Codex; runtime model and
effort are not exposed to this worker. Rules read at
`274630887938c573a041cacb306d59c6c0cb2e18`. This is implementation of the
inherited B1 diagnostic, with no new mechanism or novelty claim; a new novelty
gate is inapplicable. Only the coordinator changes Git/shared records.

Original B1 wording, unchanged:

> For n ∈ {33, 48, 64, 96, 128, 192, 256}, map the true margins:
> Λ_c − max λ on the far region;
> (1/8192 or the sharper class defect) − (S − Λ_c) on near-noncorner rings ρ ≤ 1/10;
> Λ_c − λ on dyadic corner shells.
> This fixes the accuracy N1/N2 must reach and the enclosure tightness N3 needs.
> No pass or kill; it is required input for B3 and B4.

## Operational refinement, 2026-11-05, before execution

The original omits the far cutoff/domain, corner-shell coordinates and sample
coverage. “True margins” and region maxima require continuous control that
finite floating values cannot provide. The coordinator agreed to the following
finite diagnostic interpretation; the original obligations remain unresolved.

Use the inherited phase chart theta=(J*pi+alpha)/n,
phi=(K*pi+beta)/(n+1), J+K odd, with rho=|alpha|+|beta| and the closed diamond
rho<=pi. Every signed direction is explicitly evaluated; no symmetry reduction.
Physical admissibility is checked as 0<=J*pi+alpha<=n*pi and
0<=K*pi+beta<=(n+1)*pi, including inward sign restrictions at boundaries.
Degrees are 33,48,64,96,128,192,256.

All nonzero-radius direction pairs are the distinct
(sx*t,sy*(1-t)) for t in {0,1/4,1/2,3/4,1} and sx,sy in {-1,1}:
16 spokes, including signed axes and three slopes in each quadrant.
At zero radius use the origin once.

- Far: rho in {.1,.125,.25,.5,1,pi/2,2,2.5,pi}. Evaluate S on all 144
  phase points and actual lambda at inherited selected centers: every nonnode
  corner, admissible edge distances 1,2,3, nearcorner interior offsets (1,2),
  (2,1) with reflections, and the inherited central centers. Every attaining
  center and its labels remains in raw output. This is selected-center
  sampling of lambda; it does not enumerate all centers or maximize a region.
- Near: rho in {0,.00025,.0005,.001,.002,.004,.008,.016,.032,.064,.1}.
  The 161 phase points include smaller phases than the predecessor grid.
  Compute the full odd torus S and both complete projection profiles;
  enumerate every admissible noncorner odd center, reporting the smallest
  computed max(Qh(J),Qv(K))-(S-Lambda_c) at each phase with an attaining center.
  This retains all center signs/orientations. The algebraic projected defect
  bound is inherited from PD-T364. Floating profile values have no error
  bound and do not become rigorous class defects. Also compute
  1/8192-(S-Lambda_c) at n>=48, using PD-T366's precise applicability; n33
  receives null for this comparison. No uniform n33 defect is inferred.
- Corner: for each of the two nonnode corners, shell k=0..23 is the closed
  phase-rho annulus [2^(-k-1),2^(-k)]. Sample both endpoints and the arithmetic
  midpoint on every admissible inward spoke. Record Lambda_c-lambda and
  physical square displacement H=|cos(theta)-cos(theta_corner)|+
  |cos(phi)-cos(phi_corner)|. This is evaluated stably as
  2*sin(alpha/(2*n))^2+2*sin(beta/(2*(n+1)))^2. H is distinct from phase rho;
  shell membership uses rho, not H. Shared shell endpoints are deliberately
  repeated. Cancellation at tiny rho can hide positive physical margins.

The script imports the predecessor Python direct cosine-polynomial kernel and
selected-center function read-only, and compiles the predecessor C value and
projection evaluators read-only. Source hashes identify all imported sources.
No inherited evidence file is modified. Direct polynomial checks at n=3,4,5,6,17
use every selected admissible center and all 33 signed phase points at
rho=0,.001,.1; this checks lambda, S and the projected lower-bound relation on
another formula path, but remains developer validation without an independent
agent or rigorous numerical error bound.

## Reproduction and limits

Prepare-only syntax check executed:
`python -m py_compile topics/padua-argmax-bridge-20261105/code/margin_b1.py`.
Mathematical runs require the coordinator's B0 PASS, then:

```sh
OPENBLAS_NUM_THREADS=1 B0_PASS=1 python topics/padua-argmax-bridge-20261105/code/margin_b1.py
```

The guard prevents an accidental mathematical run before release. The source
uses compiled O(n²) values and O(n³) projection profiles. Initial bounded
schedule is expected to take a few minutes, not a certified throughput claim.
Raw per-sample data and shell/detail/validation records go to
`local-output/argmax-bridge-20261105/b1/`; only the <16KiB receipt is committed.
The receipt pins command, versions, source and raw byte counts/hashes.
Cold-storage transfer to AC's prescribed Padua storage remains pending.

These measurements do not certify continuous margins, a complete cover,
all-center far actual lambda extrema, a floating error bound, strict corner
descent, a B2/B3/B4 pass, or PD-T099. A nonpositive tiny-shell floating value
cannot establish a counterexample. Continuous extrema, especially a shrinking
S-excess peak between the prescribed near radii, remain unresolved.

## Executed map

The declared run completed successfully after coordinator B0 PASS, using the
command above. Sum of per-degree wall times: 118.42 s. The 12,069-byte
[evidence receipt](evidence/b1-margins.json) records source/raw identities and
versions. Every recorded source and raw SHA-256 and byte count was checked
after execution. Inherited C sources also passed
`cc -std=c11 -Wall -Wextra -Wpedantic -fsyntax-only` without diagnostics.
Direct polynomial validation covered 1,672 admissible samples; maximum absolute
lambda and S disagreement were 7.99e-15 and 3.73e-14. The largest computed
projection-minus-direct-defect was 7.33e-15. These are floating agreement
checks with no rigorous error bound or independent-agent acceptance.

Each degree has 144 far phase samples, 1,782 admissible selected-center far
lambda samples, 161 near phases, and 720 corner-shell samples. Near-center
counts range from 90,923 at n33 to 5,301,541 at n256, including every physical
noncorner odd center at each phase.

All entries in this table are **finite sampled minima/maxima**, not continuous
region extrema. Far lambda is restricted to the 19 selected centers. Analytic
margin means the analytic constant minus a sampled S excess; the S values
remain uncertified. Projection margin uses computed profiles at all centers.

| n | Far min Lambda-S | Far min Lambda-lambda, selected | Near max S-Lambda | Near min analytic margin | Near min projection margin |
|---|---:|---:|---:|---:|---:|
|33|.00603897|.00916855|.000101825|inapplicable|.574407|
|48|.00757056|.0108156|.0000779111|.0000441592|.566529|
|64|.00880534|.0121763|.0000594725|.0000625978|.561152|
|96|.0107026|.0142364|.0000360716|.0000859987|.557081|
|128|.0121615|.0157991|.0000297012|.0000923691|.554737|
|192|.0143046|.0181442|.0000226585|.0000994119|.552633|
|256|.0159363|.0199092|.0000174385|.000104632|.551571|

The sampled S-excess peak lies on an alpha axis at rho=.008 for n33 through
n96 and rho=.004 for n128 through n256. In particular, the expanded grid sees
positive S excess at n128/256 missed by the predecessor's sparse radius grid.
This is a finite-grid observation, not a fitted phase law or located maximum.
The weakest near projection comparisons occur at edge midpoints and phase
radii zero down to .0005; details retain the exact attaining centers/phases.
Projected sampled margins are much larger than the deliberately conservative
analytic-defect comparisons. A proof must control their continuous variation.

For n33,48,64,96,128,192 the computed shell minima are positive for k=0..22,
and the smallest shell k23 includes zero or negative values at cancellation
scale. At n256 this starts at k22. The smallest computed margin overall is
-1.17e-13, at n256. These are unresolved floating signs, not confirmed
noncorner maximizers or a violation beyond a proved error bound. Shell detail
records provide minima/maxima and margin/H values; tiny H amplifies rounding
in the ratio, so it cannot be used as a certified derivative estimate.

B1 now supplies the requested finite accuracy anatomy for downstream model
and enclosure choices. The original “true margins”/continuous extrema remain
OPEN. This diagnostic has no pass/kill verdict and proves no global margin,
certified degree or all-degree argmax conclusion. Cold-storage archival remains
pending; the raw outputs are reproducible from the pinned code.
