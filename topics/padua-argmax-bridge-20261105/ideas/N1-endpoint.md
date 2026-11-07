# IDEA?argmax-bridge-codex-N1-03 — Uniform endpoint cancellation tail

Aliases: equal-opposite pole subtraction; integrable endpoint defect;
joint logarithmic cancellation; boundary-uniform two-channel perturbation.

- Question / scope: continue the full-diamond compact profile after N1-02.
  Its outer row count remains degree-dependent. This candidate isolates an
  explicitly removable endpoint tail; the original full profile stays OPEN.
- Mechanism and hypotheses: in the first phase quadrant set
  a=(cos alpha+cos beta)/2, p=sin alpha, q=sin beta, P=p+q,
  C=(p-q-2a cot(v/2))/4 and D=(p+q+2a cot(v/2))/4.
  For d=min(v,2pi-v)<=pi/4, subtract
  J0(d)=2a cot(d/2) log(sin d) from I(C,D,v), the exact cancellation
  integral of N1-02. Proposed bound:
  |I-J0|<=P[3+2log(4pi/d)]. Proposed consequence: after excluding the
  two closest endpoint rows, the absolute contribution of both endpoint
  tails d<=delta to the normalized outer I-sum is at most
  2P delta/pi^2 [5+2log(4pi/delta)], for every degree and phase.
- Closest entries read in full: IDEA-329/337/459, T216/T217/T221/T226,
  T269/T270, T365; the N1/N2/N5 round-1 records and N1-02. The exact
  cotangent row identity and single-channel subtraction are dependencies.
- Separation criterion: an endpoint residual integrable uniformly over
  the **entire** diamond, including a=0, with a count-free discrete-tail
  bound. A constant diverging as a->0 or a residual behaving as 1/d kills
  this distinction. Removing only the row's inner cutoffs is insufficient.
- Literature baseline / limitations: the inherited full campaign scan
  and round-3 supplemental search are in ../novelty-gate-N1.md. No new
  external fulltext, theorem transfer or historical novelty claim.
- Applicable obstructions: N132 forbids a leading-factor-only full
  profile; here J0 is only a subtraction and the residual remains bounded
  explicitly. No sign-fixed phase region or positive lower bound on a is
  assumed. The exceptional corrected mode remains in N1-01/N1-02.
- Gate verdict: variant with difference, the uniform residual tail.
- Cheapest decisive test: compute I(-s,s,v) exactly, s=a cot(v/2)/2;
  then divide into two pole neighborhoods of radius v/8 and their
  complement. Prove a uniform Lipschitz-integral bound by separating
  s>=P from s<P, with elementary fixed constants.
- Kill criterion before testing: if the pole-neighborhood proof needs
  inverse a, more than logarithmic endpoint loss, or a fixed coefficient
  sign pattern, stop this subtraction after at most one explicit repair.
  The original B3 kill for the eventual model is still binding and is not
  evaluated on this one supporting error term.
- Test discriminability: analytic bounds cover approaching boundary
  phases and arbitrarily small endpoint distance; finite samples cannot.
- Initial status/disposition: active at formulation, no computation or fit.
  The exact proof, if completed, receives its own PD-T and frozen file.

## Retained parallel and deferred variants

1. Absolute bounds on I and its two channels separately: abandoned for
   this endpoint estimate, because they do not subtract its explicit
   (log d)/d leading part. This is a scope decision, not a new PD-N.
2. Coefficient-ratio Taylor expansion about (-s,s): deferred. A remainder
   involving P/s would not be uniform at a=0. It may be used only after
   an independent small-s chart, which is the direct proof's second case.
3. Multiply pole coefficients by sin(pi t) before expanding B_n(t):
   retained as the next joint-profile correction, separate from the
   present integral-tail claim. The limiting pole products must be kept
   together at exact collisions. No uniform pole-profile expansion is
   asserted by this candidate record.
4. Nearest-pole sinc charts: retained from round 2 for the exact exceptional
   rows. No derivative bound or all-h certificate has yet been proved.

History: 2026-11-05, round 3 authorized after c000899. Codex mathematical
developer, requested gpt-6-astra ultra; runtime metadata not independently
exposed. Reviewed round-1 and round-2 mathematical bodies remain unchanged.

## Gated companion test: regularized single-pole norm

Before any computation, retain a second precise supporting test needed to
combine the integral subtraction with the pole norms. T365 proves an
even-length shifted cotangent expansion. Its paired-cell argument and
T270's local bound |(cot x-1/x)''|<1 on [0,pi/2] were read in full. The
companion proposes the all-integer estimate, n>=2 and 0<t<1,

    |B_n(t)/n-[2log n+C(t)-2log pi]/pi| <=5/n^2,

where C(t) is exactly T365's convergent harmonic constant. Multiplying by
sin(pi t) should then give a profile continuous at the pole offsets.
This is a **variant** of T365, with the specific difference being odd n's
central absolute-value cusp and its uniform phase-dependent row use.
The cheapest test is to subtract 1/x+1/(pi-x) from |cot x|, remove the
central |x-pi/2| cusp, and prove a paired quadrature estimate. Failure of
that residual's bounded second derivative or a lost odd-n cusp term
kills the asserted 5/n^2 constant. This is no claim that replacing the
inner pole norm alone removes the outer row count.

If both supporting tests survive, the next open step is the joint outer
profile with these regularized pole factors and the exact endpoint
logarithm. No independent errors are to be mistaken for a B3 budget.

## Gated joint test after the two supporting estimates

The supporting analytic estimates survived their first proof checks.
Before any fit or computation, the next precise test is now fixed. Write
the regularized pole profile as Phi_L(t)=sin(pi t)[2L+C(t)-2log pi]/pi,
periodically extended with endpoint value 1. For e=alpha+beta,d=alpha-beta,
c_e=cos(e/2),c_d=cos(d/2), eta_-=1/2+(d+v)/(2pi),
eta_+=1/2+(e-v)/(2pi), form

    H(L,v)=[c_e Phi_L(eta_-)+c_d Phi_L(eta_+)]/[2sin(v/2)]
             +I(C(v),D(v),v)/pi = A(v)L+B(v).

Keep the explicit piecewise trigonometric A(v) exactly. The proposed
joint endpoint subtraction for B is

    [U0+(4a/pi)log z]/z,
    U0=c_e Phi_0(1/2+d/(2pi))+c_d Phi_0(1/2+e/(2pi)),
    z=min(v,2pi-v).

Target error: at most 7+(P/pi)[3+2log(4pi/z)] for 0<z<=pi/4.
Unlike discarding an O(L*delta) strip, this gives an endpoint-tail error
uniform in both n and L after retaining A(v)L. The cheapest decisive
test is a global Lipschitz constant 12 and sup bound 4 for Phi_0,
including integer offsets, followed by elementary cot/log endpoint
remainders. A residual containing L*delta or a coefficient depending on
inverse a fails this stronger separation criterion. Exact collision rows
remain exceptional; continuous pole-profile values alone do not replace
their polynomial values. Interior outer quadrature and exceptional h
charts remain OPEN even if this joint endpoint test succeeds.

## Round-3 outcome and disposition

All three precise supporting tests survived analytic proof. Retain:

- PD-T?argmax-bridge-codex-N1-03, ../theory/N1-endpoint-tail.md:
  boundary-uniform perturbation of the cancellation integral, with an
  explicit degree-free endpoint-tail envelope.
- PD-T?argmax-bridge-codex-N1-04, ../theory/N1-regularized-pole.md:
  all-integer pole profile with 5/n^2 error, including the odd central
  cusp, and periodic constant-profile bounds sup<=4, Lip<=12.
- PD-T?argmax-bridge-codex-N1-05, ../theory/N1-joint-endpoint-profile.md:
  exact A(v)L separation and joint endpoint residual bounded by
  7+(P/pi)[3+2log(4pi/z)], uniformly in L and every phase.

The joint result gives endpoint residual-tail cost
Q=2delta/pi[7+(P/pi)(5+2log(4pi/delta))], with no degree-dependent row
count or log n factor. This satisfies the stronger round-3 separation
criterion. A bounded independent analytic critique reconstructed each
supporting estimate and found no gap; full distinct review is pending.
No mathematical computation, numerical integration, sample or fit was
needed. The earlier candidate variants remain retained with their stated
dispositions; no new PD-N is allocated.

The original compact model and onset remain OPEN. **GO only to the next
specific missing proof test**, after the parent pushes this round:
combine the explicitly subtracted endpoint harmonic/logarithmic mesh sum
with the finitely many exceptional polynomial rows in uniform h=1/n
charts. Prove a remainder through coalescing phase/collision endpoints,
or preserve a precisely scoped obstruction and one explicit repair.
Interior outer quadrature and the central chart must also close before
any all-degree finite certificate. Additional algebraic O(n) rewrites or
phase samples alone would not count as progress. No B3 PASS, usable n1,
or permission to run a finite B4 certificate is inferred.
