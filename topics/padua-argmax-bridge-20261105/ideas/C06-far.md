# IDEA?argmax-bridge-C06-far — Full-phase one-sided logarithmic profile

Aliases: H4 far-budget reuse; constant-remainder far primitive bound;
full-diamond logarithmic coefficient; cancellation retained at endpoints.

- Question / scope: prove an explicit useful onset for
  S_n(alpha,beta)<Lambda_c(n) whenever 1/2<=|alpha|+|beta|<=pi.
  Primary practical target n>=10^6 remains OPEN unless proved; a first
  concrete alternative onset substantially below log n=10^7 is allowed.
- Mechanism and hypotheses: use the original full-diamond N1-02/04/05/06/07/08
  formulas with R=2, delta=pi/4. Retain the endpoint cancellation and exact
  coefficient A(v) log n, while taking a one-sided bound on the interior
  constant part using I<=0. Treat central rows and every collision through
  finite-polynomial continuity of the combined regularized pole products.
  This is a different far-comparison scope, not another correction of the
  already fixed near model. No corrected near-only formula is used outside
  rho<=1/2.
- Closest full entries: IDEA-326/327/329/331 and original gated/fallback
  candidate bodies; IDEA-336/337; IDEA-455/456/459/461; bridge N1-01/02/03/04
  and their retained variants; N2-01/02; C01-effective. Full linked proof
  reading includes PD-T216; N1-01/02/04/05/06/07/08, N2-row-decomposition,
  N1-round4-budget, N1-round5-assembly (domain boundary), N1-16 coefficient
  algebra, C01-effective-global, and PD-T271. No unread near formula is
  transferred to the far diamond.
- Gate coverage: before this candidate, scanned all 1075 lines' headings,
  identifiers, aliases and summaries in state/IDEAS.md at input
  b6e67b3c78cb668b6d2f9da5a5560537d2960bf3, including every obstruction and
  disposition table and PR30's IDEA570–584/unnumbered aliases. Long outputs
  that truncated were reread in smaller sections. Searches across state,
  theory, ideas, topic logs and literature INDEX used full-phase,
  full-diamond, far-phase, log-graded, cotangent row, endpoint profile,
  cancellation quadrature, primitive, coefficient and collision synonyms.
  Full shortlisted records above were then read. No historical priority
  claim, external fulltext or imported source theorem.
- Separation criterion: a full-diamond upper with exact quadratic and
  linear logarithmic coefficients and a numerical constant remainder,
  rather than C01's phase-blind 60000 log(n+1) remainder. If the interior
  coefficient integral or exceptional-row error leaves an uncontrolled
  logarithmic term, this stated distinction fails. The coefficient formula
  overlaps N1-16 algebra but its proof there establishes a near-model
  expansion, not this far-domain one-sided actual-primitive inequality.
- Applicable obstructions: PD-N132 forbids a leading-only approximation;
  the linear coefficient is retained, including a=0. PD-N079's primitive
  cusp is allowed in the constant remainder. The N1-04 old error floor
  applies only to the stated small-margin near certificate through10^6;
  this far comparison instead uses a growing quadratic-logarithmic gap.
  Fixed-sign/coarse-cell and mesh-swap hypotheses are not used.
- Verdict: quantitative/domain variant within IDEA-459, not a new mechanism.
- Preregistered exact candidate: for n>=10^6 and the full closed diamond,
  with L=log n and a=(cos alpha+cos beta)/2, prove
      S_n <= (4a/pi^2)L^2 + b_full(alpha,beta)L + 200,
  where absolute phases are used in
      b_full=2U0/pi+[8a log2+4a loga
                   +2(alpha sin alpha+beta sin beta)]/pi^2,
  a loga is zero at a=0, and U0 is exactly N1-05's continuous pole profile.
  A coarser numerical bound b_full<=8/3 is a supporting target; an initial
  far consequence to test is all integer n>=ceil(exp(256)). This onset is
  explicitly a first alternative, not a claim that n>=10^6 is settled.
- First kill / proof order: check the a=0 boundary and both endpoint-vertex
  limits in the combined row products; prove a uniform interior-row upper
  at polynomial collisions and v=pi before replacing any sum. Then control
  the positive A mesh by a bounded-variation integral, join its coefficient
  to H4, and sum every error with R=2,delta=pi/4. Stop the constant200 claim
  if any uncharged singularity, finite mode or exceptional row appears.
- Verification plan: analytic proof first, no fit or large-degree scan.
  A bounded scalar diagnostic may check constants but is MEASURED only;
  no computation is a mathematical premise. Distinct Astra high review is
  required before parent publication. Computational cap, if needed:180CPU-s.
- Initial disposition: active; candidate and far onset OPEN at this writing.
- Canonical theory: new theory/C06-far-*.md only; no old proof edits.
- History:2026-11-06, parent-assigned hard mathematics under its prospective
  Astra-ultra justification in LOG; serving metadata not independently
  exposed. Rules/head b6e67b3c78cb668b6d2f9da5a5560537d2960bf3.

## Alternatives retained

1. Recount C01's strip/deformation constants: not pursued; it retains the
   phase-blind logarithmic loss and misses the requested coefficient-sensitive
   distinction. The existing theorem is valid and is not rejected.
2. Reuse corrected N1-12/15 central estimates on the entire diamond:
   abandoned as an inference; their written rho<=1/2 hypothesis forbids it.
3. Fully validated interior cancellation integrals: deferred until the
   explicit constant-remainder upper is assessed. Resume to lower the
   onset only with a precise compact function and rigorous quadrature tails.
4. Globally assert b_full<=b_c: not assumed; the exact boundary midpoint
   has b_full=4/pi, so the formula itself is the first necessary test.

## C06 follow-up, after the first analytic freeze

The first profile/comparison proof is frozen for separate review. Its
coefficient-sensitive far onset log n>=256 is a first step, not the primary
n>=10^6 target. The next retained quantitative variant completes the same
uncorrected full-phase H4 model with R=64,delta=1/100, keeping the interior
cancellation integral instead of dropping it:

    M_far=(4a/pi^2)L^2+b_full L+C_R+c_mesh
                    +(1/pi) integral_delta^(2pi-delta) B(v)dv.

B=V+I/pi is exactly N1-05's constant profile. No near-model correction is
added. Proposed approximation target: |S_n-M_far|<=1/2 uniformly for
n>=10^6 and the full diamond. This is a new error target, OPEN. Its
separation is a genuinely small constant error for the actual full-phase
primitive. N1-13's regular numerator argument and N1-14's general J(u,s,e)
identities were read in full. Their stated near-domain theorems are not
assumed on the full diamond: every required expanded parameter bound,
central log-cell and exceptional-row correction must be proved afresh.

First analytic kill: write the full-domain regular/BV and central-log
constants with u<=1/2,s<=3/2 before invoking a continuous model. If the
full error exceeds1/2, preserve that failed certificate and assess the
actual far margin; do not infer success from a sampled model value.

A cheap pre-validation diagnostic is also preregistered: evaluate the
explicit M_far at L=log(10^6), rho in{1/2,3/4,1,3/2,2,5/2,pi}, with
alpha/rho in{0,1/4,1/2,3/4,1}. Compare against PD-T271's limiting corner
quadratic using its recorded constant. This is35 floating cases with
SciPy special functions/adaptive integrals and fixed4096-term g_R tails.
The run is MEASURED only, not a proof of M_far's error or maximum. A
sampled positive comparison destroys only the proposed cheap1/2-margin
planning route; all-phase agreement proves nothing. Budget180totalCPU-s,
no degree-sized sums, no fit, and no extra sampled degree. Record source,
versions, actual CPU, failures, convergence warnings and output hash.
