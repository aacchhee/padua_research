# C2 decisive hard round — full Krawtchouk upper rate

2026-11-06. Codex, requested gpt-6-astra ultra, as expressly permitted for
this decisive step by handoff01. Coordinator owns allocation justification,
Git, shared records and audit handoff. Worker owns only this file and
../theory/c2-sharp-upper.md. Rules local snapshot:
76ba4214b100c86a44941f5e9a662ce9ce48efb8; assigned published input:
b4a04981d42c7cd872957facf5e3995e4096ca67.

## Gate and candidate scope

Read ../novelty-gate-C2.md, its complete documentary gate coverage and
retained C2-01 candidate. Read the relevant IDEA-533/535 records and full
PD-T432/433/437 theory. This is that registered quantitative continuation,
not a newly proposed mechanism or a historical-priority claim. Its
separation criterion remains control of all triangle fields and nodes.

## Round outcome

Written analytic proof of the fixed-pair sharp rate, with explicit bound

    kappa_N <= 3,000,000 N^13 (5+2sqrt(6))^(N−1), N>=2,

in ../theory/c2-sharp-upper.md. Status PROVED as mathematical development;
independent checks and Claude audit pending. Every a/b field is included.
The proof uses Bernstein jets at .4 and .5, two rectangular residue
contours separated by Re u=sqrt(6)−2, and top-three-coefficient extraction.
Common node forcing is split into a shared analytic term and constant
logit multiples of weight-type terms; the shared term has a smaller
exponential estimate. Mixed a extraction uses a single divisor at least
1/5 and only polynomial losses. The degree-N support polynomial is handled
directly rather than applying the degree-M Bernstein inverse to it.

## Retained routes and rejected shortcuts

- Terminal parity alone: retained predecessor lower witness; cannot prove
  an all-triangle upper bound or control arbitrary node directions.
- Small circles centered on each jet, using absolute Taylor coefficients:
  abandoned for this proof because numerator majorization loses the target
  base. No theorem that such contours can never succeed is asserted.
- Bounding P' in each separate jet source before combining the common
  node forcing: abandoned estimate. Weighted grid differentiation can
  spread endpoint contributions and the resulting crude product loses
  the desired base. Equation (7) combines the common source first.
- Recursive layer error bounds: not pursued; direct extraction of A1,A2
  from the first three polynomial coefficients controls every field with
  one denominator (21). The scalar denominator by itself is not claimed
  to explain conditioning, consistently with PD-N162.
- General two-parameter rate and Hahn: owned by C2; no claim here beyond
  the exact Krawtchouk pair in the assigned metric.

## Checks and runs needed

Completed: source/proof reads, exact symbolic derivation of (3)–(21),
and hand checks of the t=0, t=1, M=1 and terminal-support conventions.
The supplementary exact check below has now been executed; it is not a
premise of the theorem.

Requested separate reconstruction: verify the contour ratios, node-jet
identity, weighted Lagrange differentiation matrix, extraction of both a
fields, support-polynomial endpoint and finite constants. Exact small-N
checks should independently solve the mixed moment equations and test
the Bernstein polynomial and differentiated jets for individual node and
weight coordinates. Any failed identity blocks the claimed closure until
resolved; finite agreement alone never proves the all-N estimate.

Worker made no Git mutations and no changes to merged files.


## Completed exact producer check

Executed `/tmp/c2_sharp_upper_check.py` using Python 3.12.14 and SymPy
1.14.0. Exact rational arithmetic at N=2,3,4,5,6 passed 50 independent
moment-polynomial/Bernstein identities, 735 full-coordinate differentiated
jet checks, 1050 a-field derivative comparisons against direct norm-ratio
differentiation, and 330 degree-N support-polynomial coordinate checks.
Every node and both relative-weight coordinates were checked separately;
linearity covers their sums. This is supplementary finite evidence only.

The exact executed script SHA256 was
`452d72d73b7116068a6b7b2f7fabebdb2eb77e5e51d83ae25507173014fecb66`.
The exact executed source is now retained byte-for-byte as
[`code/c2_hard_check.py`](../code/c2_hard_check.py). Run from the repository root:

```sh
python3 topics/nn-mop-conditioning-20261106/code/c2_hard_check.py
```

The script constructs its own exact moment systems and never imports the
NN producer implementation. Extraction preserves the historical SHA256
above and all finite-check counts; it adds no premise to the theorem.
