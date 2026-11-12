# D3 — one-round certification protocol (prospective)

Rules/input head: `04ef28b6139ad15b8cfc31f865c7bb9ba0d56d9b`.
Developer: Codex, assigned gpt-6.1-sol high;
provider metadata beyond the assigned model is not runtime exposed.
Authority: handoffs 19 and 18, D3=C7; one round maximum. No Git authority.

## Scope and gate

Certify one set of exactly 20 distinct nodes in the open cube with strictly
positive weights, exact on Pi_5 for normalized product first-kind Chebyshev
measure, and unisolvent on Pi_3. Record sampled Lambda as MEASURED only.
No optimization, n>=4 search, family/asymptotic conclusion, or new priority claim.

The inherited C7 mechanism is the one candidate retained here:
`IDEA?padua-3d-20261106-claude-07` (S1 I2, assessment C7).
Gate: complete state/IDEAS headings, aliases and summaries scanned, including
obstruction/disposition tables; INDEX scanned across source/claim rows;
targeted searches used `Krawczyk`, `interval Newton`, `nonlattice`,
`Padua-type`, `20-node`, `moment fit`, `minimal cubature`, `joint spectrum`.
The closest full entries are IDEA-029, IDEA-120 and the original
`bivariate-lanczos-20261031/baseline-candidates.md` row 044; full linked
topic records read include r08-lattice-complement, r08-lattice-reduction,
t7-survivor-cubature and S1 with S1-pt2.py. Also read full narrowed handoffs,
late 2026-11-08 LOG, frontier assessment and workflow/CODEX.
Source records read: Cools–Poppe, Li–Sun–Xu, Degani–Schiff–Tannor,
Collowald–Hubert, Xu-Pitman. Their reading limitations remain unchanged.
D5 owns primary-source follow-up. This is a certification variant of an
existing proposal and scout observation, not a newly claimed mechanism.

Applicable obstructions: R08 excludes full unshifted cosine subgroup rules,
not general nodes. T7-07 rejects one translated survivor's degree-5 marker,
not arbitrary coordinates. IDEA-029/120 already retain the broad goal and
known moment/commuting-extension mechanisms; an isolated finite certificate
does not establish their all-degree target. The separating property is a
rigorously enclosed degree-5 rule with full cubic rank outside a single
translated finite torus subgroup image. Failure of any exact enclosure,
rank-transfer or nonlattice check kills this proposed certificate.

## Fixed run, bounds and ordering

Code: `../code/fd3_certify.py`, SHA256
`b8ca61f9c46610f20e81ea234ae6a583b3003095947317951d74cf72fbd780db`.
No numerical search or checker execution preceded this registration.

1. Reconstruct a scout-style proposal with numpy LM: n=3, N=20,
   56 tensor-Chebyshev equations of total degree <=5, 60 angle variables
   and 20 squared-weight variables. RNG PCG64/default_rng seed 20261112,
   at most 12 starts, at most 4000 iterations per start. Initial angles
   uniform [0,pi), squared-weight roots (1+.1*normal)/sqrt(20).
   Damping starts .01; accept decreases, divide by 3 down to 1e-12;
   reject multiply by 4; regularizer mu*diag(diag(J'J)+1e-12).
   Break a start at squared residual <1e-28 or damping >1e12.
   Search wall cap 180 seconds. Select the first proposal with residual
   squared <1e-24, min weight >1e-5, max |x| <1-1e-8 and monomial
   Pi_3 Vandermonde condition <1e7. Retain every attempted start receipt.
2. Convert to 80 physical x/w variables. Pivoted QR of the 56x80 monomial
   moment Jacobian chooses 56 active variables; freeze the other 24 to
   nearest dyadics with denominator 2^60. Refine that square system with
   mpmath 100 decimal digits, at most 12 Newton iterations, stopping below
   1e-75 infinity residual. Combined search/refinement cap 300 seconds.
3. Round all 80 centers to denominator 2^180. Active coordinate radius
   exactly 2^-100; fixed coordinates have zero radius. All enclosures use
   signed Python integers at scale 2^256, floor/ceiling after each product.
   Decimal 85-digit elimination proposes an inverse rounded to dyadic
   denominator 2^60. The inverse approximation is never a trusted premise.
4. Exact interval Newton/Krawczyk test: for F the 56 monomial moment
   equations, prove q=||I-RJ(B)||_infinity<1 and
   ||RF(c)||_infinity+q*2^-100<2^-100 by integer comparisons. Check all
   box coordinates inside (-1,1), positive weights and pairwise distinct
   node boxes. These inequalities give contraction and a root; invertibility
   of R follows from ||I-RJ(c)||<1. All 56 polynomial moment equations,
   including mass one, therefore hold exactly at that root.
5. Exact cubic rank: nonzero determinant of the dyadic-center monomial
   Vandermonde modulo prime 65537, plus the separate exact interval test
   ||I-R_V V(B)||_infinity<1 transfers rank to every enclosed node set.
   A modular center rank alone is explicitly insufficient.
6. Nonlattice check: find two fixed rational coordinates a,b on the same
   axis with D=(1-a²)(1-b²) not a rational square and 4ab nonintegral.
   Then 2cos(theta +/- phi) has degree two, trace 4ab, so is not an
   algebraic integer. Theta +/- phi cannot be a rational multiple of pi.
   Thus the nodes cannot lie in the cosine image of any single coset of
   any finite subgroup of (R/Z)^3, regardless of phase or weights.
   Arbitrary unions of unrelated singleton cosets are not excluded.
7. Only after exact pass: measure Lambda on 31^3 endpoint cosine mesh
   plus 20000 independent random-angle queries (seed 20261113), using
   monomial cubic evaluation and linear solves. Save maximum and witness;
   no continuum bound, optimizer or certified Lambda is claimed.

Round stop: any exhausted search, missing fixed rational pair, failed Newton,
exact enclosure/rank/nonlattice failure, or external timeout ends D3 after
one round. Preserve the exact remaining gap; do not start another seed,
radius, parameter or optimization campaign. Routine code-defect repair and
rerun must be separately disclosed to root, not silently treated as success.

## Commands and artifacts

Run only after root publishes this protocol and grants run permission:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 timeout 450s python -B topics/padua-3d-20261106/code/fd3_certify.py produce --certificate topics/padua-3d-20261106/evidence/fd3-certificate.json --receipt topics/padua-3d-20261106/evidence/fd3-producer.json
```

Frozen certificate replay, not a second research round:

```sh
timeout 120s python -B topics/padua-3d-20261106/code/fd3_certify.py check --certificate topics/padua-3d-20261106/evidence/fd3-certificate.json --receipt topics/padua-3d-20261106/evidence/fd3-replay.json
```

Record Python/numpy/scipy/mpmath versions, commands, code/certificate hashes,
elapsed time, seeds and failures. Certificate and each receipt <=32 KiB;
32 KiB allowance is approved in handoff19; no bulk coordinates/mesh archive.
Independent auditor rerun remains required before repository PROVED status.
Developer replay does not count as that independent rerun. Complete theory
and measurement records live only under final-d3; root owns shared updates.
