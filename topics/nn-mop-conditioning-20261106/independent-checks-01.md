# Supplementary independent checks 01

2026-11-06. Role: supplementary independent checker requested by handoff01;
requested allocation gpt-6-astra high. Serving model/effort are not independently
exposed. This is not the final Claude audit and does not approve readiness.
Rules/source: `b4a04981d42c7cd872957facf5e3995e4096ca67`; local main snapshot
`76ba4214b100c86a44941f5e9a662ce9ce48efb8` plus topic setup/development files.
No Git operations or developer-file edits were made by this checker.

## Coverage and gate

Read AGENTS.md, complete WORKFLOW.md, CODEX.md, handoff01, topic plan/log/gates.
Initial M0 and C4 interface review has no novelty content: it verifies an
existing computation, the honest amendment, and a coordinate interface.
Before C1/C2 mechanism review, read complete 1112-line state/IDEAS.md,
including all obstruction and disposition tables. Shortlist: IDEA-090/117,
376–379,530–536,554–555. Read full NN-IEP candidates; predecessor D1 and
D1-hard gates/candidates; deferred alternatives; local derivative PD-T432,
terminal witness PD-T437 and proximity obstruction PD-N162. New C2 gate
classifies the work as a continuation; no historical priority is established
by this supplementary check. Further reviewed files are listed below.

## M0 replay and amendment

**PASS within M0a only.** Fresh independent 210-dps executions cover both
families, N=4,16,32, and both NN and monic step-line maps. All twelve cells
agree with the developer's 260-dps outputs to better than 2.8e-170 relative
and round to the historical seven-significant-digit cells. The worst
independent relative discrepancy is 2.710067787e-170 (Hahn N32 step-line).
The original historical 1e-10 comparison remains **UNASSESSABLE** because
the available committed historical table lacks the precision needed for it.
The amendment states this explicitly and does not turn that original gate
into PASS. Reading stored developer output alone was not counted as rerun.

The independent checker verifies all four original raw-file SHA256/byte
records and identical code/input identities across 180/210/260 dps. The
code and raw identities are in [independent-check-receipt.json](independent-check-receipt.json).
The inherited full AD and a distinct defining-moment derivative path were
also freshly evaluated at N4 for both families; all value/gradient differences
are below 1e-150. These are floating implementation checks, not enclosures.

Commands actually executed from `/workspace/padua_research`:

```sh
python topics/nn-mop-stability-20261105/code/conditioning.py --sizes 4 16 32 --family krawtchouk --dps 210 > /tmp/nn-mop-conditioning-20261106/independent-m0-krawtchouk.json 2> /tmp/nn-mop-conditioning-20261106/independent-m0-krawtchouk.log
python topics/nn-mop-stability-20261105/code/conditioning.py --sizes 4 16 32 --family hahn --dps 210 > /tmp/nn-mop-conditioning-20261106/independent-m0-hahn.json 2> /tmp/nn-mop-conditioning-20261106/independent-m0-hahn.log
python topics/nn-mop-conditioning-20261106/code/independent_check.py > topics/nn-mop-conditioning-20261106/independent-check-receipt.json
```

All exited zero. Raw outputs are ephemeral local artifacts pending the
coordinator's archival disposition; the short receipt pins their bytes.

## C4 local interface

Read `code/c4_normalization.py` and `theory/c4-interface-validation.md`.
Freshly ran the developer's exact Fraction checks at both families N4,6,8:
evaluation identity XV=VH, fixed diagonal similarity/monic roundtrip, and
integer-node affine conversion all pass. The independent script adds both
families N5, a nongeometric signed diagonal, and negative affine scale
s=-3/7 with shift5/11, reconstructed from defining moments; all pass exactly.

The column convention requires D=diag(s^k) and
H_t=D^-1(sH_z+bI)D. The resulting powers s,s²,s³ on beta,gamma,delta and
unit subdiagonal are consistent. Monic products use a_i H_(i,i+1) and
a_i a_(i+1) H_(i,i+2), which cancel any nonzero diagonal gauge exactly.
A single path does not determine the full NN triangle; a general diagonal
similarity does not preserve a relative matrix norm. The record states both
limits and makes no unsupported external fidelity claim.

Additional command actually executed (exit0):

```sh
python topics/nn-mop-conditioning-20261106/code/c4_normalization.py > /tmp/nn-mop-conditioning-20261106/independent-c4-interface.json
```

## C1 gauge, scalar and matrix checks

Read and reconstructed `c1-gauge-invariants.md`, `c1-scalar-derivative.md`,
`c1-matrix-metric.md`, `c1-gauge-sharp-rate.md` and the measurement record.
The fixed and C1 input-dependent gauge formulas retain all six NN/four
step-line fields. The diagonal fields are identically invariant, including
their derivatives and field scales; the identity gauge supplies the upper
bound. The balanced terminal binomial index is central for both parities,
including M=2,3. The resulting NN and step-line lower bounds are valid.
The sharp NN gauge-rate corollary is a direct squeeze after the C2 upper
proof checked below. It does not prove a sharp step-line or Hahn rate.

Fresh 200-dps scalar/terminal runs at N4,8,16 for both families agree with
all-coordinate frozen AD; the largest scaled discrepancy is 2.469e-180.
The independent code also enumerates primal box/hyperplane vertices in
135 exact rational cases, verifying the fixed-mass weighted-median support.
Scalar zero shift fields use absolute scale one as declared. No polynomial
all-N scalar theorem follows from the modest measured growth.

Independently assembled all 16 signed OLS endpoint intervals from the
260-dps terminal files and historical displayed cells, including their
half-last-place rounding radii. All agree with the summary within 1e-12.
The mixed NN intervals are Krawtchouk [9.181247,10.370243], Hahn
[10.355428,13.261407]; step-line intervals are [9.745755,9.755462] and
[11.685726,11.765131]. Negative regression weights must choose the upper
pointwise endpoint for the lower slope. This was raised during checking
and is now handled explicitly. These are numerical evaluations of valid
analytic bounds, not outward-certified intervals or exact gauge optima.

The matrix proof correctly uses max-entry <= spectral <= Frobenius,
without assuming different scalar row supports are jointly attained.
The integer-node lower numerator T_x+dT_w and normalized-node numerator
d(T_x+T_w) have the correct affine factors. The upper bound is valid
because d>=1. Exact Fraction defining moments at both families N4,6,8
give monic integer H spectral norms agreeing with the stored norms within
1e-14. The specific monic-H exponential lower follows from a polynomial
Frobenius bound. Neither this argument nor diagonal gauge invariance
controls an arbitrary similarity's relative matrix denominator.
Independently recomputed all 348 C1 matrix error/condition diagnostics,
including the reported extrema and first large-condition indices; all
match. These remain first-order diagnostics, not stability bounds.

Commands executed, each family/mode combination separately, exit0:

```sh
python code/c1_metrics.py --mode scalar --family krawtchouk --sizes 4 8 16 --dps 200 --verify
python code/c1_metrics.py --mode terminal --family krawtchouk --sizes 4 8 16 --dps 200 --verify
python code/c1_metrics.py --mode scalar --family hahn --sizes 4 8 16 --dps 200 --verify
python code/c1_metrics.py --mode terminal --family hahn --sizes 4 8 16 --dps 200 --verify
```

JSON/log destinations are `/tmp/nn-mop-conditioning-20261106/independent-c1-{mode}-{family}.{json,log}`;
the receipt pins all four JSON files. Full 61-size developer sweeps were
read for aggregation, not represented as independently repeated.

## C2 parameter lower, sharp upper and Hahn proofs

**No unresolved mathematical defect found in the reviewed proofs.** This
is a supplementary finding, not final audit approval or a novelty verdict.

For the parameter lower bound, reconstructed the terminal transform,
partial Hermite quotient, signed generating function and positive
convolution after orientation. The independent Fraction Gauss-Jordan
implementation checks 140 terminal derivatives for N2–8 and five rational
parameter pairs, plus 35 summed generating coefficients, exactly. A found
specialization error was corrected: the conservative q_min formula gives
12/5 at (2/5,1/2), whereas the original PD-T437 prefactor is 5/2. The
stronger symmetric-marginal bound legitimately bypasses the q_min
orientation and uses q=1/4 directly; its parity direction preserves mass.

For `c2-sharp-upper.md`, reconstructed every step independently:

- Bernstein degree preservation and exact (M)_t normalization.
- Differentiated jets with independent weights and common moving nodes;
  the logit source is common only after removing each constant logit.
- The residue kernel giving the leading three coefficient functionals.
- Both sharp separating-rectangle ratios at c=sqrt(6)-2; other sides
  have denominators at least one, and their combined length is 14.
- The weighted Lagrange differentiation identity and column l1 bound
  3H_M; the common analytic source has the smaller contour base <3.
- Inverse Bernstein transfer, the separate degree-N support derivative,
  and all a fields via the two-by-two top-coefficient system whose base
  denominator has magnitude at least 1/5.

The displayed loose constants dominate each intermediate bound, giving
3,000,000 N^13 rho^(N-1), and the retained lower squeezes the Nth-root
rate to rho=5+2sqrt(6). The independent exact implementation checks all
77 degree<=M polynomials at N2–7, including 252 differentiated jet
conditions under simultaneous common-node and distinct weight forcing,
and the weighted differentiation identity at every grid point. These
finite checks support the analytic argument, not its all-N premise.

For Hahn, reconstructed the transformed rows, determinant constant
product_{r=1}^t r!, the two residues giving tau, and the terminal support
case. The scalar cross expectation and fixed-mass signed-binomial
direction yield the stated nonsharp base-two lower, including M=1.
The loose positive field scales suffice; no sharp base near 11.8 follows.
Independently reran the developer's exact checker through N10: 273
defining systems, 219 kernel determinants, 54 cross expectations and
nine terminal derivatives, all pass. This rerun uses the developer code;
the analytic reconstruction is separate.

```sh
python code/c2_hahn_checks.py --max-n 10 > /tmp/nn-mop-conditioning-20261106/independent-c2-hahn.json
```

## C3 measured stability scope

Independently reran both families at N7,14,19 using the native grid driver.
Every selected stored nine-digit error/ratio is reproduced. In particular
Hahn N14's C4 ratio is 40533.1034, Krawtchouk N19's A-LU ratio is
1.13269396 (already kappa*u>1), and Hahn N7's A-LU ratio is .469315695.
The denominator is the explicit seven-digit historical kappa, not an
exact condition. Neither the selected reruns nor full developer grid
establish a weak-stability theorem or activate conditional M3.

A found derivative-reduction omission is resolved in the final prose:
with extraction F(p)=G(c(p),p), Q=D_pG, the derivative is
DF=Q-L M^-1 H. The terminal/direct input term cannot be omitted from
the common-input condition. The corrected file retains the unresolved
algorithmic source-operator comparison and nearby-input algorithm domain.

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python code/c3_grid.py --sizes 7 14 19 --output /tmp/nn-mop-conditioning-20261106/independent-c3-grid.json --raw /tmp/nn-mop-conditioning-20261106/independent-c3-grid-raw.json > /tmp/nn-mop-conditioning-20261106/independent-c3-grid.log 2>&1
```

## C4 authenticated execution and final comparison

The supplied 1,020,330-byte archive has SHA256
`cdd0e98d2b411f24cfcecb49d83e16f9d50a7622a0d4f0d3eb17eb334a405145`.
Independently compared all 27 extracted member byte strings to that archive.
Read CORE/KRYL/REORTH, initialization/LU, both family data/exact generators,
the inherited driver and current wrapper. These authenticate the executed
code, not an unread primary paper's theorem or every licensed experiment.

Fresh independent Octave execution of the inherited M4 driver reproduces
the selected paper-N10 Krawtchouk CORE error 2.691214553706643e-10,
log10 ratio -0.4058177524 to the inherited quoted paper value. The gate's
one-decade condition passes. The entire driver ran; only this selected
comparison is the asserted paper gate.

After the developer found decimal JSON input drift, repeated independent
M2 with the corrected IEEE-hex wrapper. Verified the shared N6 node and
weight bits against Python's rounded rational input. Own Fraction
subtraction before the spectral norm gives exact-generator relative
error 7.184849749e-17, CORE 7.472429295e-15, KRYL 5.301648865e-12 and
REORTH 7.258603595e-15. M2 normalization fidelity passes; the stronger
exploratory all-solver 1e-12 check fails for KRYL and is not concealed.

With `LD_LIBRARY_PATH=/tmp/c4-apt/root/usr/lib:/tmp/c4-apt/root/usr/lib/x86_64-linux-gnu:/tmp/c4-apt/root/usr/lib/x86_64-linux-gnu/octave/9.4.0`
and `OCTAVE_HOME=/tmp/c4-apt/root/usr`, used executable
`/tmp/c4-apt/root/usr/bin/octave-cli --no-init-file --no-site-file --quiet --eval`
with these literal evaluation arguments:

```matlab
addpath('/workspace/padua_research/topics/nn-mop-stability-20261105/g5-run'); driver('/tmp/c4-iep-source/IEP-MOP-main/src','/tmp/nn-mop-conditioning-20261106/independent-g5');
addpath('/workspace/padua_research/topics/nn-mop-conditioning-20261106/code'); c4_external('/tmp/c4-iep-source/IEP-MOP-main/src','/tmp/c4-shared-input.json','/tmp/nn-mop-conditioning-20261106/independent-c4-m2.json','m2');
```

Separately read the H+d0 lift and reran six exact Fraction moment/full-NN
reconstructions. Then independently reran final comparison postprocessing
on the developer's bit-preserving external raw run and native grid.
All 116 comparison records and 58 shared input identities match exactly.
This is a complete independent **postprocessing** replay, not a second
execution of all 348 external solver calls. The full NN external output
is the explicit solver+input-anchor+high-precision-lift composite, not a
native source output or positive-input backward solution.

```sh
python code/c4_lift.py > /tmp/nn-mop-conditioning-20261106/independent-c4-lift.json
OPENBLAS_NUM_THREADS=1 python3 code/c4_compare.py --external /tmp/c4-external-grid-bits.json --native /tmp/nn-mop-c3-grid-raw.json --raw /tmp/nn-mop-conditioning-20261106/independent-c4-comparison.json --evidence /tmp/nn-mop-conditioning-20261106/independent-c4-evidence/tables > /tmp/nn-mop-conditioning-20261106/independent-c4-comparison.log 2>&1
```

## Reviewed proof checkpoints and remaining limits

SHA256 of the substantive proof snapshots reviewed (paths relative to
`theory/`; these are evidence identifiers, not prose-hash execution gates):

| File | SHA256 |
|---|---|
| c1-gauge-invariants.md | 6beb350a41ac92812b2ff8043b9a79a2d3583b08272953fa0f98853362d5a91b |
| c1-scalar-derivative.md | 10b0034a408c61a3821fde9600da02bce53a314a4d8ae7d3745c912676807704 |
| c1-matrix-metric.md | 2a9eb2294ccad6cacb760131577444f9766ea47fdad45c60885912197ca7c7f6 |
| c1-gauge-sharp-rate.md | 7fcdd4fe2deb8b322d6dbacd58907b3e98b5cde8d92f61403466491f20301972 |
| c2-krawtchouk-parameter-lower.md | 94797e1c03171cb577b2b37ab366fe96cb404a877a3b6a7a928da53d97bdca71 |
| c2-sharp-upper.md | 62acd71e03212d3ee4a83832c13ad526e8b16f229119f21a82d1e69c25f14150 |
| c2-hahn-normality.md | a8c2fc56a4876b92798f88ef7d763c102fee1839885668fb2cdf642337bb1da5 |
| c2-hahn-lower.md | a11612e33d5b80591c5b0b644b32119d3f613270e22439b4e3bfcaffd0161de3 |
| c3-weak-stability-open.md | 40ad400355e07e83192e0e25c46444455fc5541fde239f8c2650d29099f15a78 |

The final checker receipt is below 16KiB and records executable/raw hashes,
versions, counts and selected values. It is regenerated by the command
above; large local files remain ephemeral and no archive upload is claimed.
No all-N Hahn sharp rate, all-N scalar polynomial bound, exact gauge
optimizer, arbitrary-similarity matrix rate, finite perturbation radius,
or stable floating algorithm has been established by these checks.
The independent Claude audit and coordinator's final disposition remain
separate. This report does not approve readiness.
