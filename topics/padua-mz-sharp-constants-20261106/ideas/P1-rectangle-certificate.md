# IDEA?mz-sharp-codex-P1-02 — integrate scalar kernels before certification

Aliases: rectangle row integral; semicircle endpoint formula;
positive-vector Schur certificate.

- Question / scope: give an exact finite certificate format for bounding
  r=||B||=-c_minus after the P1 kernel identification, using positive
  simple trial functions and rigorous integration. This record does not
  assert that any chosen mesh or arithmetic budget delivers three digits.
- Mechanism and hypotheses: integrate the scalar kernels against a' da'
  over source intervals before enclosing them. Their arcsine convolution
  gives elementary square-root integrals with no elliptic diagonal
  singularity. Tensor rectangle integrals then bound A=-B on the triangle.
  A positive simple function h and a verified Ah<=U h give r<=U; its
  Rayleigh quotient gives a lower bound. All inequalities use the actual
  weighted measure, including triangle boundary cells.
- Closest registry entries and exact links: full gate ../novelty-gate-P1.md;
  IDEA-058 finite rigorous certificates, IDEA-420 / PD-T331 weighted
  positive-vector inequality, IDEA-470 and accepted S3-03 exact B, and
  ../ideas/P1-kernel.md with its already registered positive-vector scope.
  The scalar semicircle formula is derived in the new P1 kernel proof.
- Separation criterion: remove the weak elliptic singularity exactly by
  source integration, rather than evaluate a pointwise kernel on a grid.
  The decisive property is a finite, independently checkable upper bound
  for every target point and all source cells, including cells cut by D.
- Literature baseline / limitation: elementary Tonelli, square-root
  integration and the known weighted 2ab inequality suffice. No new
  historical mechanism or priority is claimed. No external theorem is
  imported beyond the already named dependencies.
- Applicable obstructions: a smooth Nystrom eigenvalue is not an upper
  bound; diagonal point evaluations of S_all diverge; replacing the
  triangle by unaccounted full rectangles changes the operator. These
  are avoided only when the stated positive enclosure inequalities are
  proved and checked literally.
- Novelty verdict: known certificate variant with a useful exact local
  integration formula; a child of the supplied P1 route, not a new global
  research direction. The earlier gate covers its Schur mechanism.
- Cheapest decisive test: derive the one-dimensional interval row
  integrals and explicit moduli, then state a finite upper/lower
  certificate. Analytic work only; no numerical execution by this worker.
- Kill criterion written before testing: a wrong normalization or a
  missing triangle/sliver contribution rejects that proposed certificate.
  A broad interval or excessive cost only leaves three-digit feasibility
  unproved, and does not reject the exact kernel or norm identity.
- Discriminability: the finite inequalities imply a spectral enclosure
  independently of agreement with floating approximations; failure to
  prove them cannot be replaced by numerical convergence.
- Resources / cost ledger: continuation as bounded round 3 of the
  existing six-round P1 budget; two consecutive no-progress rounds stop.
  No code/numerical runs. The coordinator must publish any numerical
  prediction and execution protocol before computational testing.
- Actual test results and evidence: round 3 derived the exact interval
  source integrals and explicit finite inequalities in
  ../theory/P1-rectangle-certificate.md. No numerical run or concrete
  certificate was executed. The distinct supplementary reconstruction
  in ../independent-checks-P1-kernel.md found no mathematical gap in the
  frozen file; focused Claude audit and formal readiness remain pending.
- Disposition / reason: retained; the analytic finite certificate format
  is PROVED as development, with supplementary reconstruction complete.
  Certified decimal success remains OPEN and
  its exact output obligation is stated in the theory file.
- Canonical theory / negative-result ID: provisional P1-03 in
  P1-rectangle-certificate.md; no final ID or PD-N allocated here.
- Topic / completed audit / history: 2026-11-06, requested gpt-6.1-sol
  xhigh; runtime model and effort metadata unexposed. Rules/input
  0205690b9c4e959a28e949083e9a1808735abf4b. Saved before this extension's
  local derivation; accepted S3 proofs remain unchanged.
