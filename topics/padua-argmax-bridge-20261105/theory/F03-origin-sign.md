# PD-T?argmax-bridge-codex-F03-origin — Actual-origin sign target and the unresolved one-dimensional reduction

ID kind: PD-T; provisional target only, no global allocation.
Aliases: I10 origin nonnegativity; compensated corner deformation;
origin-only cotangent/digamma expansion.
Split from: none. Split into: none.

## Statement

The registered primary target is, for EVERY integer n>=160,

    E_n(0)=Lambda_c(n)-A_n^2-kappa>=0.                 (T)

The explicitly weaker useful target is E_n(0)>=-ebar(n)/4, with the
SAME accepted E08 ebar(n)=D(n)+Mesh(n)+1/n. Neither target is proved.

## Definitions and assumptions

Use m=n+1 and the actual corrected Padua corner value, original endpoint
weights and finite polynomial collision values. Let A_n,L_n,kappa be
EXACTLY PD-T269/270's quantities, and put

    q_n=L_n^2-A_n^2,
    b_n=A_n/(2n^2)+1/(16n^4),
    C_n=Delta_n-kappa-(L_n^2-1)/m.

The inherited identities give C_n=Lambda_c-L_n^2-kappa and
E_n(0)=C_n+q_n, with |q_n|<=b_n. No F01 draft or fitted asymptotic
coefficient is a premise. All logarithms are natural.

## Status by part

Overall status: **OPEN**. Candidate disposition: **DEFERRED after the
first reduction screen**. No origin sign or improved lower correction,
global onset, exact O(n) evaluator or impossibility theorem is claimed.

The finite algebra below consists of routine origin specializations of
PD-T226 and PD-T159. It records the exact missing object; these supporting
identities neither complete the target nor give it PARTIAL status. No
new PD-N is created for an unavailable identity or deferred proof route.

## Depends on

- PD-T159: corrected corner identity, original half weights, exceptional
  contribution1/m, exact same-mesh square.
- PD-T226: actual periodic rows, signed full cotangent sum, absolute-row
  negative-part representation, including polynomial endpoint rows.
- PD-T269/270: limiting kappa and the already proved square-error bound.
- E08-origin-lower: the complete accepted fallback ebar on n>=160.

## Proof/evidence of the routine exact reduction

### 1. Actual origin rows, including both exceptional endpoints

For 1<=r<=n set v_r=r*pi/m. In the periodic first-coordinate grid the
origin samples are

    u_j=j*pi/n, j=1-r mod2, considered modulo2n,
    F_r(u_j)=(1+cos v_r)/(cos u_j-cos v_r).

There is no collision in these folded interior rows: n,m are coprime
and 0<r<m. Since their numerator is strictly positive, their positive
samples have centered representatives |j|<nr/m. Now
r-1<nr/m<r, so the positive set is EXACTLY

    j=-r+1,-r+3,...,r-1.                              (1)

It has r samples, for either parity of n or r. Define their sum P_r.
PD-T226's signed full row is n; hence its absolute row is

    R_r=2P_r-n.                                      (2)

The actual polynomial endpoint rows are R_0=n^2 and R_m=n. Fold the
remaining periodic rows into their two equal copies, without exchanging
the n and m meshes. The exact corner value is therefore

    Lambda_c=1/m+n/m+(2/(nm))sum_(r=1)^n(2P_r-n)
            =1-2n/m+(4/(nm))sum_(r=1)^n P_r.          (3)

The first1/m is displayed separately in the first line: it is the SAME
exceptional polynomial contribution in PD-T159. The n/m is the other
actual endpoint row. Folding the periodic mesh is exactly equivalent
to its original first-coordinate half weights and second-coordinate
endpoint half weights; no endpoint is silently discarded. Formula(3)
also follows by writing the original first-coordinate weighted Cauchy
row as one half of R_r, with its k=0 half row and the exceptional k=m
value kept separately. Thus(3) is an inherited exact normalization,
not a new corner formula assumed from finite comparisons.

### 2. The surviving partial cotangent sum

Put

    t_r=r/m, a_r=(1-t_r)/2, w_r=cot(pi*r/(2m)),
    T_(n,r)=sum_(l=0)^(r-1)cot(pi*(l+a_r)/n).

Then exactly

    P_r=w_r*T_(n,r).                                 (4)

To verify this without a pole assignment, on the positive set(1) use

    F_r(u)=(cot(v_r/2)/2)
                 [cot((v_r-u)/2)+cot((v_r+u)/2)].

The set is symmetric in u, so its two cotangent sums agree. Enumerating
j=r-1-2l gives (v_r-u_j)/2=pi*(l+a_r)/n and proves(4).
Every displayed cotangent is regular. This calculation preserves the
complete positive/negative-row split; it does not turn an absolute row
into a signed row.

The complete n-term cotangent identity, locally proved in PD-T226,
instead gives

    sum_(l=0)^(n-1)cot(pi*(l+a_r)/n)
                   =n*cot(pi*a_r)=n*tan(v_r/2).       (5)

Thus replacing the partial sum in(4) by(5) gives P_r^full=n. This is
exact only for r=n; for every r<n the actual row has negative samples
and P_r>n. Indeed the exact omitted quantity is

    Z_r=P_r-n=sum_(negative samples)(-F_r)>0 (r<n),
    Z_n=0,
    Lambda_c=1+2n/m+(4/(nm))sum_(r=1)^n Z_r.           (6)

These are the origin instances of IDEA329/PD-T226's OLD absolute
partial-row obstruction. They are not a new negative mechanism.
Replacing every partial by its complete signed sum gives only
1+2n/m<3. The omitted mass is Lambda_c-1-2n/m; by the inherited
PD269/270 asymptotics it is asymptotic to (4/pi^2)log^2 n. It is not
a permissible vanishing remainder for either target(T) or its fallback.
This rules out THAT substitution, not another endpoint-complete identity.

### 3. Two-sided digamma subtraction does not by itself collapse the row

For a>0 define H_r(a)=sum_(l=0)^(r-1)1/(l+a). If desired this equals
psi(a+r)-psi(a), with psi defined by its convergent harmonic series;
subtracting the two series telescopes and proves that equality locally.
For 0<x<1 put

    B(x)=cot(pi*x)-1/(pi*x)+1/(pi*(1-x)).

The two singularities cancel: B extends continuously (in fact
analytically) to [0,1], with B(0)=1/pi and B(1)=-1/pi. Exact algebra
in every term of(4) gives

    T_(n,r)=(n/pi)[H_r(a_r)-H_r(n-r+1-a_r)]
                       +sum_(l=0)^(r-1)B((l+a_r)/n). (7)

The two H terms have positive arguments. All endpoint and parity terms
are retained. Subtracting only1/(pi*x) would leave the pole at x=1;
one cannot infer smoothness at BOTH endpoints from that subtraction.
Subtracting both poles really does regularize the summand, as(7) shows.

But the weighted smooth residual

    V_n=sum_(r=1)^n w_r
                       sum_(l=0)^(r-1)B((l+a_r)/n)   (8)

still contains n(n+1)/2 indexed terms. Writing a partial cotangent as
an incomplete product derivative or leaving(8) under a new function
name would not establish the registered genuinely one-dimensional
finite expression or its proposed O(n) evaluation cost.

Even the elementary boundedness of B is insufficient as a final error
allocation: if |B|<=M, using w_r<=2m/(pi*r) gives

    (4/(nm))*sum_r w_r*|sum_l B((l+a_r)/n)|<=8M/pi.

This only supplies a nonvanishing constant charge. It does not provide
the required signed quadrature comparison and normalization compensation
at scale log(n)/n. No assertion that the TRUE residual has constant
size as an approximation error follows from this coarse bound.

## Exact unresolved step and scope

No endpoint-complete finite ONE-index identity evaluating(8), nor an
equally complete one-index formula plus PROVED explicit uniform signed
remainder, was obtained in this bounded first test. Consequently the
registered exact1D prerequisite did not pass. The subsequent expansion,
its log^2(n)/n normalization compensation and the sign/uniform lower
allowance were NOT assumed or pursued as established premises.

Equations(3),(4),(7),(8) specify the precise remaining object. A future
route must actually control it together with the explicit harmonic
part and -(L_n^2-1)/m, retaining the endpoints, before claiming either
C_n>=b_n or C_n>=b_n-ebar/4. C07's Delta_n>=0, PD271's limiting
constant and E12's zero origin-relative coupling do not fill that gap.

This record does not prove that a classical special-function collapse,
an endpoint-complete quadrature identity or the origin-sign theorem is
impossible. Its disposition is DEFERRED, not REJECTED. It supplies no
new allowance to the current global argument.

## Checks, sources and open items

PAPER algebra only; ZERO executable/import, numerical/scalar/degree/
endpoint/corner/phase/native/quadrature/compiler/source/control jobs.
No external theorem or PDF used. No Git or shared-file mutation.
Distinct review has not occurred. The target stays OPEN and no
substantive PROVED F03 result is offered for adoption.

Resume only with an actual endpoint-complete reduction or a uniform
signed estimate for(8) that survives the normalization test. Do not
execute I10's proposed exact O(n) evaluation on the assumption that
the accepted row identity already supplies that algorithm.

## History

2026-11-07, requested/API Codex gpt-6.1-sol xhigh. Rules/input
4a5de2012bad94601c713b2ff5517f2e3fb80af2. Root separately released
PAPER after the completed gate and durable prospective campaign/LOG
entry. Owned idea/attempt were written at07:12 UTC BEFORE derivation.
The newly narrowed full-row screen triggered an additional full read
of IDEA329's original/final records, PD-T226 and its round6 record
BEFORE further pursuit of that exact predecessor. No alternative new
mechanism, signed h-expansion, finite test or second round was launched.


## Root disposition after distinct mathematical review —2026-11-07

Root accepts the routine identity/normalization and OPEN/deferred disposition; no improved finite origin bound or O(n) evaluator is adopted. The original frozen proof prefix is preserved and identified in [independent mathematical review](../independent-checks-F02-F03.md). Novelty/priority, disclosed chronology and final Claude/readiness judgments remain separate and unwaived.


## Dated canonical-source correction — 2026-11-08 (F-01, H-C02)

Sections 1–3 above are preserved historical text. Their classification as
only routine support and the statement that no substantive PROVED F03 result
is offered are superseded: H depends on the exact identities, so their
canonical PROVED record is now
[PD-T?argmax-bridge-codex-F03-identities](F03-identities-support.md).
Split into: that supporting result; its original-to-split mapping awaits the
orchestrator's reviewed crosswalk application. The source and audit pins at
`b45e29fa1fe3dbfa2517ff8043e5d9c440870530` remain historical evidence.

The original target (T), E_n(0)>=0 for every integer n>=160, and the useful
E_n(0)>=-ebar(n)/4 target remain **OPEN**, with the same accepted E08 ebar.
The exact identities are supporting lemmas, not proved cases or conjuncts
of either target; neither target becomes PARTIAL. H uses only the split
identities, not the OPEN sign or proposed one-index evaluator. The H theorem
can imply eventual positivity without an explicit onset; it supplies no
proved n>=160 sign bound or adopted useful allowance here.
