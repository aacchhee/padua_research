# IDEA?argmax-bridge-codex-N4-02 — Exact Chebyshev mode-diagonal nodal translation

Aliases: spectral translation; dual nodal product-Chebyshev operator; finite nodal closure.

- Question / scope: can a matrix whose dual nodal operator is diagonal
  in all q_ab=T_a(x)T_b(y),a+b<=n, send L(c) to L(z) and remain
  nonnegative for every z in the square and n>=2?
- Mechanism and hypotheses: fix the mode-diagonal class independently
  of the target. The identity forces eigenvalues
  d_ab=q_ab(c)q_ab(z); define M_ij=(tau_z L_i)(B_j). Partition of
  unity then forces column sums1. This uses no target norm bound.
- Closest registry entries (read in full): IDEA-331/PD-T364 (reflection
  before absolute values) and IDEA-345/346/PD-N084 (signed-polynomial
  coefficient positivity). These do not assert positivity of this
  finite nodal matrix. The exact imposed diagonal action distinguishes
  this class from unrestricted matrices.
- Separation criterion vs closest entry: an exact identity independent
  of lambda plus positivity of all matrix entries. One exact negative
  entry, or a necessary moment invariant violated at one z, kills the
  all-z claim for this class. Diagonal action and identity together
  force a unique candidate, so an arbitrary eigenvalue refit cannot
  repair the class.
- Literature baseline and search limitations: precise gate completed
  in novelty-gate-N4.md before formulation. No Askey–Gasper or
  Koornwinder–Schwartz theorem is used; their fulltexts remain unread
  by this worker. Elementary cosine addition supplies the formula.
- Applicable obstructions and exact hypotheses broken: no S-only
  comparison is assumed, so PD-N079 does not directly kill this class;
  matrix positivity differs from PD-N084's coefficient positivity.
  Corner zero masks are retained and no individual L_i(c) is divided by.
- Novelty gate verdict: **variant with difference**, within documented
  repository scope only; no historical novelty or priority claim.
- Cheapest decisive test: examine the B00 column, which is L(-z), and
  test its coordinate-square moments at rational z=(0,0).
- Kill criterion written before testing: failure of nonnegative matrix
  entries at one certified point kills only this frozen diagonal class.
  No unrestricted N4 kill follows.
- Test discriminability: the dual class and transport identity determine
  all entries, so the obstruction is structural rather than a failed
  choice among free eigenvalues. The written proof handles all n>=2;
  the requested n3–8 exact checks are supplementary.
- Actual test results and committed evidence: analytic classification:
  M_z>=0 iff -z is a node, equivalently z is on the complementary
  checkerboard. Center(0,0) therefore fails every n>=2; explicit n3
  entry=-1/8. Exact rational cyclotomic checks at n3–8 reproduce
  partition, zero first/second moments, positive squared-node-distance
  invariant and4871positive-grid translation columns. No LP run.
- Disposition and precise rejected scope: **REJECTED: failed**, universal
  all-z positive mode-diagonal nodal translation. Positive matrices at
  the finite complementary grid remain valid; their scalar bound is
  already inherited from PD-T364.
- Disposition reason: **failed** by the exact class-wide positivity
  classification, not by failure of the target inequality.
- Canonical theory / negative-result ID:
  PD-N?argmax-bridge-codex-N4-01,
  theory/N4-diagonal-translation-obstruction.md; supporting generic
  variance lemma PD-T?argmax-bridge-codex-N4-02.
- Topic / audit / history: N4 round1,2026-11-05, Codex parent-assigned
  gpt-6.1-sol xhigh; runtime metadata not independently exposed.
  Formula frozen before exact run; sharp positive-locus construction
  was added after the initial analytic obstruction. Independent review
  pending; no final ID allocated.
