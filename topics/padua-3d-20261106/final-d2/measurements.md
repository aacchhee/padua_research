# PD-T?padua-3d-20261106-codex-D2-measured-01 — bounded exact algebra and matrix searches

ID kind: PD-T. Aliases: D2 finite algebra; Padua syzygy calibration;
ORSV border probes; compatible Jacobi fit; matrix-parameter Λ measurement.
Split from: none (finite supporting observations for original C2 target).
Split into: none. The separate written real-calibration existence result
retains PROVED and is not downgraded by this finite record.

## Statement

The frozen D2 drivers, on the recorded environment and inputs, produced the
finite observations in [outcome.md](outcome.md) and their essential JSON
receipts. Quantifiers are solely over the listed24 exact pipelines,
three ORSV/extension pencils, four Jacobi starts, and the prospectively
specified R3 trajectories when actually executed. No unlisted pencil,
seed, degree, input normalization or global supremum is covered.

## Definitions

N=binom(n+3,3). A pencil is affine in three variables. EN uses maximal
minors of (n+3)×(n+1); symmetric uses submaximal minors of size n+2.
Standard monomials use grevlex order (x,y,z). A squarefree multiplication
characteristic polynomial certifies reducedness of the finite computed
algebra; a repeated value of the chosen separating form makes that test
inconclusive, not a nonradicality certificate. Λ samples are maximum sums
of absolute cardinal values over specified finite query sets.

## Assumptions

Trusted CPython/SymPy exact polynomial implementation; floating NumPy/SciPy
for real and quality probes, one BLAS thread. Software versions and platform
are recorded in [fd2-runtime.json](../evidence/fd2-runtime.json), introspected
after R1/R2 in the same environment. Timings and stopping behaviour are
implementation/environment observations. Exact-algebra claims are retained
here as finite observations; the completed coordinator replay does not
upgrade the broad construction target.

## Status by part

Overall status: **MEASURED**.

| Part | Status | Evidence / limit |
|---|---|---|
| n2/3/4 exact Padua syzygy/minor identities | MEASURED exact arithmetic | explicit rational matrices in R1 receipt; independent Padua-syzygy replay PASS, fdr-d2-padua-replay.json |
|20 completed exact algebra pipelines | MEASURED exact arithmetic | quotient dimensions, standard monomials and8 squarefree charpolys; actual coordinator replay agrees |
|4 random n4 pipelines | OPEN | actualCPU25 caps; no exact conclusion returned |
| Known natural-lattice realization | Separate PROVED claim | [real-calibration-theory](real-calibration-theory.md), written proof; not part of this measurement status |
| ORSV real-root lower counts and Jacobi residuals/guards | MEASURED | R2 receipt; search completeness and exact cubature unproved |
| R3 quality | MEASURED | eight completed499-objective paths; best sampled5478.14834/546899.58091 atn3/4; failed initial engineering receipt separate |

Candidate disposition: broad C2 remains OPEN, with its exact known calibration
retained. No broad negative theorem is claimed from these observations.

## Depends on

Source input for ORSV: D5's primary-read quartic matrix, p7 in arXiv1311.3675v2,
(rho,sigma)=(10,10). The developer's executed numerical lower count stands
on its own input bytes. Source facts are coverage-qualified LITERATURE.
GT4.05/5.09 are external measured benchmarks; they are not certified global
optima. The written natural-lattice proof independently justifies the known
starting configuration's real finite geometry.

## Checks

Frozen drivers: [exact](../code/fd2_exact.py), [real](../code/fd2_real.py),
[optimization](../code/fd2_optimize.py). Full commands, seeds, run-go commits,
hashes and caps are in [protocol](protocol.md) and [outcome](outcome.md).
Receipts: [R1](../evidence/fd2-exact.json), [R2](../evidence/fd2-real.json),
[R3](../evidence/fd2-optimize.json).
R3's initial engineering failure is preserved separately in
[fd2-optimize-failed.json](../evidence/fd2-optimize-failed.json); every path
ended at its initial-only checkpoint before a proposal objective.

Actual checks already performed by this developer: exact code executions
R1/R2; Python compilation; synthetic identity-matrix batched RHS mock at
sizes20/35 for the R3 NumPy2 repair. No independent rerun has been executed
by this developer and no code inspection is represented as a rerun.

The distinct coordinator actually replayed all20 completed exact pipelines:
[receipt](../evidence/fdr-d2-exact-replay.json),92.8136s, every non-timing
field exactly equal. It separately assessed the two best R3 sets using
monomials/SVD:
[receipt](../evidence/fdr-d2-quality-replay.json), sampledΛ5478.148340739174
and546899.5809121559, with count/cube/pencil-singular-value guards.
The four original randomn4 caps remain unresolved. Formal Claude audit is
separate; these checks do not establish a broader-family quality bound.

## Proof or evidence

The committed short receipts preserve successful, failed, capped and
inconclusive cases separately. The R1 structured repeated-form issue is
resolved for that known baseline by R2's exactN distinct rational common
zeros plus the R1 dimensionN calculation, while retaining the failed
separating-form diagnostic. It does not resolve any random n4 case.

The numerical Jacobi residual minima are not rigorous zero certificates.
Their exterior joint spectra do not meet the original cube support guard.
No affine normalization is used to claim the original Chebyshev cubature.
R3's41³+512-query assessment gives best sampledΛ5478.148340739344 atn3
and546899.580912354 atn4. All eight500-total-call paths (oldinitial1 plus
repaired499) improved the poor exact baseline, without attaining competitive
quality. A few local paths around that baseline do not bound the full family.

## Scope

Finite software observations only. They establish neither a generic-family
lower bound on Λ, absence of better matrix parameters, real-node
nonexistence, an all-n Padua transfer, nor a log³ family. Computed matrix
rank at rounded optimized nodes is not exact unisolvence certification.

## Open items

Formal mathematical audit; random n4 algebra;
projective completeness of numerical perturbed loci; any exact Jacobi
cube cubature certificate; Padua-specific 3D structure. Original C2 stays
OPEN rather than becoming PARTIAL from supporting lemmas or measurements.

## History

2026-11-12, Codex gpt-6.1-sol xhigh, rules04ef28b: finite record created after
R1/R2, preserving their statuses and the preregistered R3 repair separately.
R3 completed after its repaired source7b844e2c was published in3bea991.
