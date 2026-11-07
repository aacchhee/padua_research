# IDEA?argmax-bridge-codex-D03-joint-finite-h — Subtract symmetric cancellation before quadrature

Aliases: A-channel cancellation reference; perturbation BV quadrature;
floor-free sine-channel error; D03 joint finite-h preparation.

- Question/scope: obtain a practical pointwise-phase finite-n remainder
  for D02's bias-completed M_infty, or isolate a genuinely useful bounded
  lemma without calling it the full rate. Full closed phase diamond,
  actual corrected kernel, both parities. No global onset claim.
- Fresh gate: rules/input
  `084a64f6465956f9c75b5538f83752c30318f151`. Refreshed complete IDEAS
  headings, identifier/alias columns and explicit Aliases lines; all
  obstruction tables (unisolvence, Lanczos, MZ, lattice, programme,
  Padua-MZ, PR12 and argmax PR19). Searched joint, relative, normalization,
  cancellation, moving-zero/root, finite-h, finite-part, paired and tail
  across current argmax ideas/theory, IDEA336/337/459 and literature INDEX.
  Full shortlist: N1-outer and N1-endpoint candidates, N1-02 cancellation,
  N1-03 equal-opposite integral perturbation, N1-07 exact sinc row charts,
  N1-09 finite-h/jump correction, D01 signed failure, D02 bias/limit/target,
  audit01 P1/P2/P5, and IDEA336/337/459. No external source or historical
  priority claim. The actual finite endpoint kernel and ordinary row
  numerator were inspected before this candidate.
- Mechanism: write C=-w+c, D=w+d, w=a*cot(v/2)/2,
  c=(p-q)/4, d=(p+q)/4. For N1-02's bounded cancellation function g,
  subtract g0=g(-w,w,v;x) before estimating quadrature. Unlike separating
  whole pole norms, g-g0 stays bounded at both poles and coefficient
  switches. A min-channel sandwich should give
  sup|g-g0|<=P*cot(e/2), e=dist(v,pi*Z), P=p+q.
- Closest predecessors: N1-03 subtracts the same equal-opposite integral
  to get an integrable endpoint tail. It does not control the variation
  of the *difference of discrete cancellation functions* or compare their
  finite mesh errors. N1-09 removes pole jumps on a near-only positive
  numerator domain and retains an O(1/R^2) floor. D02 identifies the exact
  limit but its auxiliary positive bounds retain O(a/R) floors.
- Separation: prove a full-phase difference-quadrature error bounded by
  a universal constant times P*H_n/n, with no fixed R floor and no inverse
  a or coefficient-distance factor. Merely bounding g and g0 separately
  restores a/(n z^2) and erases the distinction.
- Cheapest exact test: use g=-2min(|C cot x|,|D cot(x+v)|) on opposite-sign
  channels and zero otherwise. Split |w|>P/4 and |w|<=P/4, then count
  sign arcs and derivative zeros of g-g0. Proposed conservative explicit
  target Var_per(g-g0)<=56P/e, giving ordinary-row summed quadrature
  error <=56P*H_n/n. The analytic preliminary sandwich was obtained after
  the gate and before this written record; no prospective earlier timestamp
  is claimed for that paper step.
- Kill: an unbounded difference at a pole, more sign pieces than the
  finite count covers, a derivative estimate requiring inverse a, or any
  collision substitution losing the actual polynomial value kills this
  lemma as stated. Do not replace a failing claim by sampled agreement.
- Main joint-reference obligation: the exact symmetric reference's mesh
  error must telescope with the actual endpoint rows and C08 E_infty at
  finite n. If only a separate fixed-R floor or singular unweighted pole
  reference results, the practical finite-n candidate remains OPEN even
  if the bounded perturbation lemma is proved. Do not claim the symmetric
  reference alone models S: N1-outer already records its missing boundary
  logarithm when sine channels are dropped.
- Alternatives retained: phase-relative subtraction of S(phi)-S(0),
  deferred until its actual cancellation estimates are supplied; smooth
  h-Taylor through moving zeros, not assumed; optimizing D02 auxiliary
  R,delta floors alone, not pursued because it misses the joint target.
- Resources: at most twenty analytical minutes for this first D03 block,
  parent-requested Sol xhigh; runtime metadata not independently exposed.
  No native run, full-board evaluation, quadrature, fit or extra correction.
- Outcome: the bounded perturbation lemma is developer-PROVED in
  theory/D03-cancellation-perturbation.md, with the stronger summed constant
  112P/pi instead of56P. The practical joint remainder is OPEN because the
  finite-n symmetric-reference/endpoint telescope remains unproved.
  The naive whole-A-kernel comparison is abandoned: at n4,alpha3pi/5,
  beta0,r2,j1 its unweighted pole is singular while the actual corrected
  polynomial is finite. This does not reject bounded g0 subtraction.
  Keep exact special/central exclusions and phase-even extension; no
  n/m mesh exchange. No numerical run occurred.
- Canonical records: attempts/D03-joint-finite-h.md and the standalone
  theory/D03-cancellation-perturbation.md. Distinct review is requested
  before any harder reference follow-up; no practical rate is claimed.
