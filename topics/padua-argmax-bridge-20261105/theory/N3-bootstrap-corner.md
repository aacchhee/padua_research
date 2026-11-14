# PD-T?argmax-bridge-codex-N3-bootstrap-01 — A corner cover reduction using the unknown global maximum

ID kind: PD-T.
Aliases: N3 round7; global-maximum bootstrap; norm absorption; half-phase
corner maximum exclusion.
Split from: none; quantitative application of PD-T227 / IDEA330.
Split into: finite energy verification is a separate result in
N3-bootstrap-finite.md; the all-n energy premise remains OPEN.

## Statement

Fix an integer n>=2, m=n+1, and precisely the even-checkerboard Padua
interpolation of PD-T101. Let lambda_n be its Lebesgue function,
M=max_[-1,1]^2 lambda_n, and Lambda_c its value at either of the two
parity-correct nonnode corners. In inward physical coordinates at a
nonnode corner c, let A_n,B_n and W_n be exactly those of PD-T227.
Assume

    W_n <= (3/4)*n^4*Lambda_c.                         (E)

Then no point c+h with h_x,h_y>=0 and

    0<z=n^2*(h_x+h_y)<=1/8                            (P)

is a global maximizer. The assertion holds at both nonnode corners.
It requires no prior upper bound for M/Lambda_c.

Let P_1,P_2 be their closed physical patches z<=1/8, or let
D_1,D_2 instead be their inward closed scaled-phase diamonds

    |alpha|+|beta|<=1/2,
    alpha=n*xi, beta=m*eta,                            (D)

where xi,eta are angular distances from that corner's sides. Each
D_i is contained in P_i, and z<1/8 on D_i away from the corner.
For either chosen pair of patches, if every point outside their union
has lambda_n<Lambda_c, then

    M=Lambda_c,
    argmax lambda_n = {the two nonnode corners}.       (C)

This is a proved implication with the explicit energy and complement
premises. It does not assert those premises for all n, and does not
give pointwise descent on (P) or (D) before the global closure (C).

## Definitions and assumptions

All arithmetic is exact real arithmetic. The cardinal polynomials
are the corrected PD-T101 cardinals, with the exceptional highest mode
in the first coordinate and all finite removable values retained.
Inward h denotes signed physical distance after the parity-preserving
corner reflection; H=h_x+h_y. In PD-T227's canonical corner c=(-1,-1),

    W_n=sum_(L_jk(c)!=0)
         [L_jk,x(c)^2+L_jk,y(c)^2]/|L_jk(c)|.

The removable00 index is included. Exactly k=0,j>0 even are omitted
from this energy because their corner value is zero. Their equal
inward derivative components are included in A_n,B_n, so they have
not been omitted from the Lebesgue derivative or the Taylor model.
The signed-cardinal model allows later sign changes.

## Status by part

Overall status: **PROVED analytic reduction**. Its explicit assumptions
are not assertions that all-n energy or a complement cover is known.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Maximum exclusion under (E) on (P), and cover implication (C) | PROVED | Exact absorption argument below |
| Containment of the half-phase diamonds (D) in (P) | PROVED routine coordinate corollary | Sine bound below |
| Energy premise for every n>=2 | OPEN external target | PD-T367 proves only the much larger constant10^10 |
| Energy for n2..128 | Separate finite result | N3-bootstrap-finite.md; independent new-threshold replay required |
| Strict complement coverage outside the chosen patches | OPEN external obligation | No phase source/checker change or cover rerun in this step |

Candidate disposition: retained quantitative variant with difference,
IDEA?argmax-bridge-codex-N3-bootstrap-01. No historical novelty or
priority claim; T227 supplies the inherited model and derivative norm.

## Depends on

PD-T101: finite corrected cardinal polynomials and continuity.
PD-T227(1),(3),(6),(7): exact inward slopes including zero cardinals
and the aggregate Taylor bound using the true global M.
PD-T251(2a): A_n,B_n<=-n^2 Lambda_c/8 for every n>=2, and the
parity-preserving reflection identifying the two nonnode corner values.
No PD-T368 global norm ratio, numerical energy value, fitted profile,
unproved sign stability or existing global argmax is a premise.

## Proof

### 1. Why the unknown global norm is a legitimate variable

The finite sum of absolute cardinal polynomials is continuous on the
compact square. Hence M exists and M>=Lambda_c>0. PD-T227 proves,
for every inward physical h in the square,

    lambda_n(c+h)<=Lambda_c+A_n*h_x+B_n*h_y
                    +(W_n/2)*H^2+M*R(n^2 H),
    R(z)=exp(z)-1-z.                                 (1)

Its M is the actual global maximum, not a substituted known upper
bound. For clarity, T227's endpoint norm step chooses signs sigma_jk
for each mixed derivative and applies the Lobatto endpoint functional
to p=sum sigma_jk L_jk. At every point |p|<=lambda_n<=M. Thus
its derivative norm and Taylor remainder use M without assuming a
location or value for a maximizer. Initially zero cardinals enter
the exact first variation via |gradient L_jk(c).h|. Their inward
linearity is proved in T227 and is already part of A_n,B_n in (1).

Use the all-n slope bound and (E) in (1), with z=n^2 H:

    lambda_n(c+h)<=Lambda_c*(1-z/8+3z^2/8)+M*R(z).   (2)

### 2. Strict absorption at a putative global maximizer

For 0<=z<=1/8, the exponential series gives

    R(z)<=z^2*exp(z)/2<=4z^2/7.                      (3)

Indeed (k+2)!>=2*k! gives the first estimate term by term, and
exp(z)<=sum_(k>=0) z^k=1/(1-z)<=8/7 gives the second.
In particular R(z)<=1/112, so 1-R(z)>0.

Suppose a point with (P) is a global maximizer. Substituting
lambda_n(c+h)=M in (2), while keeping the same M in the remainder,
gives

    M*(1-R(z))<=Lambda_c*(1-z/8+3z^2/8).

On (P),

    z/8-3z^2/8-R(z)
      >=z/8-(3/8+4/7)*z^2
       =z/8-(53/56)*z^2
      >=(3/448)*z>0.                                (4)

Consequently

    M*(1-R(z))<=Lambda_c*(1-R(z)-3z/448)
                <Lambda_c*(1-R(z)),                  (5)

contradicting M>=Lambda_c and 1-R(z)>0. This proves maximum
exclusion. It does not replace M by Lambda_c in (2) at an arbitrary
point before the global comparison is established.

### 3. Phase geometry, the second corner and global closure

At a corner write the nonnegative inward angular distances as
xi,eta and the scaled magnitudes as |alpha|=n*xi, |beta|=m*eta.
The physical increments are

    h_x=1-cos xi=2*sin^2(alpha/(2n)),
    h_y=1-cos eta=2*sin^2(beta/(2m)).

If at least one phase is nonzero, the strict sine inequality yields

    z < [alpha^2+(n/m)^2*beta^2]/2
       <=(|alpha|+|beta|)^2/2<=1/8.                  (6)

At zero phase z=0 is the corner itself and is intentionally excluded
from maximum exclusion. The node-preserving x reflection for even n,
or y reflection for odd n, permutes cardinals and weights, transfers
the same Lambda_c,W_n and inward slopes, and proves the assertion
at the second nonnode corner. This is the reflection used in T251.

Now assume strict complement coverage for the chosen pair P_1,P_2
or D_1,D_2. A global maximizer exists and has value at least
Lambda_c, so it cannot lie outside their union. Inside the union,
(5) excludes every point except its two centers. The centers have
equal value Lambda_c. Thus M=Lambda_c and the exact equality set
is those two corners, proving (C). Equality at a patch boundary is
also excluded by (4); the centers are the sole z=0 exceptions.

After, and only after, that global closure one may substitute
M=Lambda_c into (2) and obtain the routine pointwise consequence
lambda_n(c+h)<=Lambda_c*(1-3z/448)<Lambda_c on (P). This consequence
is conditional on completed closure and is not a new standalone local
predicate available to an unchanged phase checker.

## Checks, scope and open items

The proof is analytic. The old exact endpoint data are a separate
cheap countertest; the fresh producer and distinct GMP reconstruction
belong to N3-bootstrap-finite.md. No all-n energy follows from
n2..128 endpoints. No full phase cover, cost law, degree extension,
effective onset or all-degree PD-T099 result is asserted here.

The inherited T227 inequality, slopes and zero-cardinal treatment
were read before candidate development; the existing unknown-M
remainder ingredient is attributed to T227 rather than relabeled new.
IDEA330/457 used an a-priori K for pointwise descent, and IDEA454's
existing corner predicate also supplies pointwise strictness. The
specific maximum-absorption application and its separate complement
obligation are the documented quantitative distinction. No external
source or priority claim is used.

## History

2026-11-06, Codex developer, parent allocation inherited; serving
model/effort metadata unexposed. Input/rules
88e702321cd5d9c3395a551fc8a55a2f7cb8bc10. Parent authorized one
round7 helper after the prospective read-only gate. The exact
energy bound3/4, z<=1/8, gap3z/448, finite range2..128 and
stop criteria were written before its first finite countertest.
All earlier source, proof and receipt bytes remain frozen. Required
Claude audit and a distinct mathematical check remain separate.
