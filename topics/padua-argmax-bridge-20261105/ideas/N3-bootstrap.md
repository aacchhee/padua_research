# IDEA?argmax-bridge-codex-N3-bootstrap-01 — Exclude global maximizers by absorbing the unknown norm

Aliases: N3 round7 bootstrap; self-consistent global maximum; unknown
Lebesgue norm absorption; half-phase corner maximum exclusion.

## Prospective gate and exact candidate — 2026-11-06

- Question / scope: for each n>=2, can the inherited PD-T227 model
  exclude noncorner **global maximizers** on a much larger corner
  patch without an a-priori global-to-corner norm ratio? The reduction
  assumes exactly W_n<=(3/4)n^4 Lambda_c. A separate complement cover
  remains necessary for a global conclusion.
- Mechanism / hypotheses: retain PD-T227's true M=max lambda_n in
  its exponential remainder. At a putative global maximizer set its
  left side to M and absorb M*R(z), R(z)=exp(z)-1-z, for
  0<z=n^2(h_x+h_y)<=1/8. Use PD-T251's all-n slopes
  A_n,B_n<=-n^2 Lambda_c/8 and the specified aggregate energy bound.
  Since R(z)<=4z^2/7, the exact algebra leaves the positive gap
  3z/448. No assumed global argmax or prior bound M<=K Lambda_c.
- Exact conditional conclusion: no noncorner point in either inward
  physical patch 0<z<=1/8 is a global maximizer. Each inward corner
  phase diamond |alpha|+|beta|<=1/2 lies in that patch, with z<1/8
  away from its origin. If every point outside the two chosen patches
  is certified strictly below Lambda_c, the exact global equality set
  is the two nonnode corners. This is not pointwise corner descent
  before that global closure.
- Closest registry records read in full: IDEA330 including its
  original gated candidate; IDEA454 H1; IDEA457 and its full H2/H3
  record (including equivalent IDEA460 and deferred IDEA461).
  Full linked proof reads: PD-T227, PD-T251, PD-T367, PD-T368.
  Current N3 corner-radius reduction, common n2..128 patch and
  round6 calibration records were also read in full.
- Registry / search baseline: complete unchanged 1031-line
  state/IDEAS.md coverage from the preceding round is reused before
  this candidate and every finite check. SHA256 remains
  0e1813b1f53e6aa4a970f19b86ebb3864dd6546b7f55c0bc2ffc4033320825f7
  at published input88e702321cd5d9c3395a551fc8a55a2f7cb8bc10.
  New read-only searches across Padua topics/theory/ideas, state and
  literature used bootstrap, self-consistent, unknown Lambda/norm,
  global norm at maximum, rearrangement/absorption, maximum principle
  and a-priori synonyms. Storage-bootstrap and unrelated Lanczos hits
  were discarded after scope inspection; N4's unknown norm restriction
  concerns constructing positive transport maps, not this inequality.
- Separation criterion: T227 already supplies the unknown-M Taylor
  inequality; that ingredient is inherited. IDEA330/457 instantiate
  a known ratio K to prove pointwise descent, and IDEA454 requests a
  pointwise corner predicate. Here rearrangement is used only at an
  unknown global maximizer, retaining a separate strict-complement
  obligation and potentially allowing a half-phase corner patch.
  An existing identical maximum-absorption reduction would erase this
  distinction; no such record was found within this bounded search.
- Literature baseline / limits: internal quantitative continuation;
  no external theorem transfer, historical novelty or priority claim.
- Applicable obstructions: PD-N085 prevents a uniform per-cardinal
  ratio shortcut, but this candidate assumes a summed W bound and
  allows sign changes. PD-N079's primitive cusp is not a premise of
  the actual-function T227 model. Initially zero cardinals and the
  removable00 term must retain their inherited exact treatment.
- Gate verdict: **quantitative variant with difference** of
  IDEA330/454/457, not a new Taylor/energy mechanism. It does not
  revive N5's quarter-projection formula or its failed certificate.
- Cheapest logical kill, completed read-only before this candidate:
  inspect original T227(3),(6),(7). It genuinely uses M=max lambda,
  not an assumed known upper bound, and includes zero-cardinal
  inward contributions in the slopes. The rearrangement is valid
  because M>=Lambda_c and 1-R(z)>0. No logical kill was found.
- First finite countertest, **not yet run at preregistration**:
  inspect the existing source-identified MPFR producer and independent
  GMP endpoint tables for every integer n2..128. Test exactly

      4E <= 3*n^4*ell,

  with ell<=Lambda_c and E>=W_n, using exact fractions. These old
  endpoints are a cheap countertest, not fresh independent acceptance
  of the new threshold and not a uniform all-n claim.
- If the countertest passes: freshly build the unchanged MPFR corner
  producer SHA256a0497ca1219850e28f2bf51e72cb4fc8f78cde238b81fd678262d646511402bd
  and execute n2..128 exactly once at256 bits. A new wrapper checks
  the new exact threshold, range, masks, counts, n2 controls
  Lambda_c=3 and W_2=331/18, per-degree CPU and identities. Cap
  total child CPU at1200 seconds. Raw output stays local; only a small
  aggregate receipt is essential evidence.
- Verification plan: the root assigns a distinct fresh127-case
  reconstruction with the unchanged GMP kernel
  SHA2563646f4e8b6b16957b9e1114f95ad2f0a7c18eec4687b49d5e6f1947a25eea6e3,
  checking this new threshold, not merely its old kappa predicate.
  Until that replay, the finite energy theorem is CONDITIONAL.
- Kill criterion: stop at the first failed threshold, invalid mask,
  source mismatch, arithmetic/process error or CPU cap. Preserve the
  witness and bounds; no adaptive constant, extra degrees, repeated
  energy arithmetic or automatic successor. A failed upper-endpoint
  certificate need not refute the true energy inequality.
- Test discriminability: exact endpoint comparisons decide whether
  those valid certificates suffice for the finite threshold. Fresh
  outward generation and separate exact replay can prove only the
  fixed n2..128 energy bound. Uniform all-n energy, complement
  certification, cost scaling and PD-T099 remain separate OPEN targets.
- Ownership / resource boundary: only new bootstrap idea, two theory
  records, wrapper, small receipt and attempt record. No old source,
  receipt, theory, N5 file, phase producer/checker, shared state or Git
  change. No full phase rerun this step; no new prose hash pins.
- Disposition at preregistration: retained bounded helper, finite
  execution not yet started. Parent authorized one round7 after
  publishing88e7023; serving model/effort metadata unexposed.

## Runs needed at preregistration

The new wrapper's fixed command and pinned input manifest will be
written in ../attempts/N3-bootstrap.md before execution. First the two
old endpoint tables, then the one unchanged fresh MPFR sweep; distinct
fresh GMP replay belongs to the root's separate checker.

## Bounded developer outcome

Both old identified127-case endpoint tables passed the exact new
threshold. One fresh unchanged MPFR256-bit sweep then passed all127
degrees, with362045 nonzero contributions,4096 zero omissions, no
failed/unrun case, and5.048074 total child CPU seconds. Maximum
certified E/(n^4ell) occurred at n2, approximately0.383101851852;
the fixed3/4 threshold was retained. Source/receipt/raw identities and
all actual commands are recorded in ../attempts/N3-bootstrap.md.

The exact maximum-absorption and finite-cover implication is
**PROVED analytically** in ../theory/N3-bootstrap-corner.md,
PD-T?argmax-bridge-codex-N3-bootstrap-01. The fixed n2..128 energy
claim is **CONDITIONAL** in ../theory/N3-bootstrap-finite.md,
PD-T?argmax-bridge-codex-N3-bootstrap-02, pending the separately
assigned fresh GMP new-threshold replay. Candidate disposition:
retained bounded helper; uniform all-n energy and complement coverage
remain OPEN. No new unconditional pointwise local predicate, phase
rerun, global degree extension or automatic next round. Stop here.

## Dated independent acceptance — 2026-11-06

The separate checker freshly compiled unchanged GMP arithmetic and
executed all127 degrees for the new threshold, without producer
endpoint imports. Every case passed; the completed report
../independent-checks-bootstrap.md accepts the frozen pure implication
and finite energy result. Accordingly N3-bootstrap-finite.md is now
**PROVED** at exactly n2..128, preserving the initial CONDITIONAL
launch above and in its original producer receipt. No constant, range,
source or pure-proof change. Uniform all-n energy, strict complement
coverage, new phase predicates and additional global degrees remain
outside this accepted helper. Required Claude audit is separate.
