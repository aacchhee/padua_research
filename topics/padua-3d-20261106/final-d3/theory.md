# PD-T?padua-3d-20261106-codex-D3 — one nonlattice cubic Padua-type rule

ID kind: PD-T. Aliases: C7; 20-node positive precision-five certificate.
Split from: none. Split into: none. No final ID or priority claim.

## Statement

There exist 20 distinct points X_j in (-1,1)^3 and strictly positive real
weights w_j such that

    sum_j w_j p(X_j) = integral p(x) dmu(x),  p in Pi_5,

where dmu(x)=pi^-3 product_d (1-x_d^2)^(-1/2) dx_d, and evaluation
Pi_3 -> R^20 at X is bijective. Moreover X is not contained in

    { (cos(2pi t_1),cos(2pi t_2),cos(2pi t_3)) : t in a+H }

for any a in (R/Z)^3 and finite subgroup H of (R/Z)^3.
This is a single finite-degree statement, with no all-degree continuation.

## Status by part

Overall status: **PROVED** (computer-assisted finite theorem). The proved
finite reduction, committed certificate/checker, actual independent frozen
rerun and separate exact Fraction reconstruction are documented in the
[supplemental audit](../final-check/d3-audit.md). Formal Claude review is
separate; no audit acceptance is inferred from the developer's label.
The separate [Lambda record](measurements.md) is **MEASURED**.

## Definitions, assumptions and finite reduction

Flatten the 20 triples x_j to coordinates 0..59 and weights to 60..79.
Let A_m={(i,j,k)>=0:i+j+k<=m}. Order A_m by increasing i, then j,
then k as `idx(m)` in fd3_certify.py. For alpha in A_5 define

    F_alpha(x,w)=sum_j w_j product_d x_(jd)^alpha_d - M_alpha.

Here M_alpha=0 if any alpha_d is odd, otherwise
product_d binom(alpha_d,alpha_d/2)/2^alpha_d. To derive this,
expand cos(theta)^k into exponentials and retain the zero Fourier
coefficient; averaging over [0,pi] has the same cosine-power mean.
The product measure factors the three one-variable means. Thus F=0
is equivalent to precision at least five, since these 56 monomials
are a basis of Pi_5. This is a proved finite reduction, independent
of the numerical proposal mechanism.

The certificate specifies 80 exact dyadic centers c with denominator
2^180 and a sorted subset A of 56 active coordinates. The remaining
24 stay exactly fixed. The active box B has radius r=2^-100 in
every active coordinate. Restrict F to these 56 variables; it is a
polynomial map R^56 -> R^56. Positivity, strict containment in the
cube, and distinctness of every pair of node boxes are checked
directly from the rational endpoints.

## Interval Newton proof

The checker evaluates the residual F(c), full polynomial Jacobian
J(B), and cubic evaluation matrix V(B) by directed dyadic arithmetic.
All intervals are integer endpoint pairs divided by S=2^256.
Addition adds endpoints, negation reverses them, and multiplication
takes the minimum and maximum of the four integer endpoint products,
then applies floor and ceiling division by S. Integer scalar products
use the sign to select endpoints and divide only after summation.
These formulas enclose the exact real operations by induction. Python
signed floor division and arbitrary-size integers supply exact rounding;
no hardware floating operation participates in an accepting predicate.

Decimal elimination proposes a rational matrix R; its accuracy is
irrelevant until checked. Let q bound ||I-RJ(B)||_infinity and z
bound ||RF(c)||_infinity. The exact integer predicates are

    q < 1,        z + q r < r.

For T(y)=y-RF(y), the mean-value integral on convex B gives
||T(y)-T(v)||_infinity <= q ||y-v||_infinity. Also
||T(y)-c|| <= z+qr < r, so T maps B into itself and is contracting.
Iteration from c converges inside the closed finite-dimensional box
to its unique fixed point. At c, ||I-RJ(c)||<1, so the Neumann series
inverts RJ(c); square R is therefore invertible. A fixed point
satisfies RF(y)=0, hence F(y)=0. This proves an actual degree-five
positive rule, conditional only on the finite predicates passing.
It gives uniqueness on the chosen 24-coordinate slice; no uniqueness
of cubature rules in 80 variables is asserted.

## Exact rank and transfer to the true root

The cubic monomial Vandermonde has rows indexed by the 20 nodes and
columns A_3. Reduce its dyadic-center entries modulo prime 65537;
the dyadic denominator is invertible there. A nonzero determinant
proves the center matrix has exact rational rank 20. This alone
would not prove rank at the enclosed true root.

The checker separately constructs rational R_V and verifies
||I-R_V V(B)||_infinity<1 by the same directed exact arithmetic.
For every possible node set in B, Neumann's series inverts R_V V,
so V has rank 20. Since dim Pi_3=20, the enclosed true nodes are
Pi_3-unisolvent. No tolerance-dependent numerical rank is used.

## Nonlattice proof

The checker chooses two fixed rational coordinates a,b on the same
axis. It verifies D=(1-a^2)(1-b^2)>0 is not a rational square and
4ab is nonintegral. Both tests use exact reduced fractions and
integer square roots. For theta=arccos(a), phi=arccos(b),

    u=2cos(theta +/- phi)=2ab +/- 2sqrt(D)

has degree two over Q and minimal monic polynomial

    t^2 - 4ab t + 4(a^2+b^2-1).

Its trace 4ab is not an integer; hence u is not an algebraic integer
(Gauss's lemma: a rational minimal monic polynomial dividing a monic
integer polynomial has integer coefficients). If theta +/- phi were
a rational multiple of pi, u would instead be an algebraic integer:
the integer recurrence C_0=2, C_1=t, C_(k+1)=t C_k-C_(k-1) gives
the monic relation C_q(u)-2=0 whenever q(theta +/- phi) is 0 mod 2pi.
This contradiction covers either sign and also their negatives.

If both nodes came from one finite coset a0+H, each coordinate
difference of torus lifts would be rational. Folding by cosine only
changes each angle's sign modulo 2pi, so one of theta +/- phi would
be a rational multiple of pi. The rational pair therefore excludes
every such coset, including arbitrary phase, order and noncyclic H.
Arbitrary unrelated coset unions are outside this definition.

## Checks and evidence

Protocol and frozen command: [protocol](protocol.md).
Producer/exact checker: `../code/fd3_certify.py`.
Certificate: `../evidence/fd3-certificate.json` (5574 bytes, SHA256
`3677318c6dcf793f256750c0f270eb9be8eaa1143534428fcc096e497aa18a7d`).
Producer `fd3-producer.json` and developer `fd3-replay.json` both pass.
The exact integer numerators imply the following readable rational bounds
(also checked with Fraction in a separate developer summary conversion):

| Quantity | Exact strict bound |
|---|---|
| q | < 3/10^17 |
| z | < 4/10^55 |
| q_V | < 2/10^17 |
| each weight | > 47/10000 |
| every coordinate's absolute value | < 999924/1000000 |

The modular center determinant is 60293 modulo 65537. The nonlattice
pair uses fixed flattened coordinates 0 and 3 (x of nodes 0 and 1):
a=-8375088658315393/9007199254740992 and
b=-1233507562271173/4503599627370496. Their exact D and nonintegral
trace are recorded in both receipts. In particular the pair stays
unchanged at the true root.

Independent rerun and independent Fraction reconstruction both passed; see [D3 supplemental audit](../final-check/d3-audit.md) and its pinned receipts.

Execution assumption: normal CPython with optimization disabled (`sys.flags.optimize=0`); `assert` predicates are part of the trusted checker.

Trusted basis: integer arithmetic, standard Python Fraction/Decimal
(Decimal only proposes matrices), the displayed formulas and finite
algorithm. Search numpy/scipy and high-precision refinement mpmath
are proposal generators, not proof dependencies.

## Scope and open items

The general all-degree Padua target stays OPEN. No quality conclusion
follows from exact cubature or rank. No historical priority is claimed;
the existing S1 scout mechanism and IDEA-029/120 remain predecessors.
Runs needed: focused formal Claude audit; the independent exact reruns are complete.
The one registered producer and developer replay have completed. D3 stops
with success after one round; no refinement of quality or higher degree is
launched. The remaining verification obligation does not reopen research.

## History

2026-11-12, Codex, assigned gpt-6.1-sol high, input rules 04ef28b.
Statement, finite reduction and interval arithmetic were written before
the authorized numerical run. No prior scout result is inherited as proof.
The root authorized execution after publication at `db8c3cc`; the first
proposal passed and the complete producer took 1.78 seconds. See runs.md.
