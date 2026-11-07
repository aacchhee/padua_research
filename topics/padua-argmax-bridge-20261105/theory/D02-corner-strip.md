# PD-T?argmax-bridge-codex-D02-strip — Coordinate averaging of the finite collision strip

ID kind: PD-T. Aliases: D02 half strip charge; rectangular polynomial
remainder. Split from: supporting strip obligation for D02's OPEN
uniform corner target. Split into: none.

## Statement

Use the corrected polynomial and physical odd-board conventions of
C02/C07. For every integer n>=1000, m=n+1, and alpha,beta>=0 with
alpha+beta<=1/2, put r2=alpha^2+beta^2 and a=(cos alpha+cos beta)/2.
On B={(j,j+1):0<=j<=n,2j>=n}, let e_j,f_r be endpoint half weights,
F0=F_jr(0,0), and sum_four mean the four signed phase copies. Then

    (1/(nm))sum_B e_j f_r |sum_four(F_jr-aF0)|
        <=(14/5)[floor(n/2)+1/4]/(n+1) * r2.          (1)

All copies, weights and finite polynomial endpoint values are included.
The same bound applies at the parity-correct other nonnode corner,
using its node-preserving reflection without exchanging the meshes.

## Definitions and assumptions

P_n=T_(n+1)+T_n,
D_n(u,v)=[P_n(cos u)-P_n(cos v)]/[cos u-cos v], evaluated by its
polynomial extension at collisions, G_n=D_n-cos(nu), and

    F_jr(gamma,delta)=(-1)^j
         G_n((j*pi+gamma)/n,(r*pi+delta)/m)/2.

The rectangular path set is |gamma|<=alpha,|delta|<=beta, hence
|gamma|+|delta|<=1/2. Exact real arithmetic and the original exceptional
first-coordinate correction are retained.

## Status and scope

Overall status: **PROVED**, by the written analytic argument below.
This is a separate supporting result; D02's uniform K_new<=7.8 target
and any strict actual-corner conclusion are not parts of this theorem.
Distinct review remains separate; the developer does not self-approve.

This changes the allocation of B relative to D01/C07. D01's primary
failure, alternative failure and kill remain frozen for its old budget.
The method is the standard rectangular identity already used for
regular f in C05 §4/C07 §3, applied on B. No historical novelty claim.

## Depends on

C02 §5/C07(17)'s exact finite U/V factorization, C02 §1's corrected
four-copy normalization and parity reflection, and elementary Fourier
moments. All degree-sensitive estimates used below are re-established
on n>=1000, rather than invoking an old n>=1000000 theorem there.

## Proof

### 1. Pure phase second derivatives on the lower domain

For (j,r)=(j,j+1) in B put h=n-j, so0<=h<=floor(n/2), and

    x=(h*pi-gamma)/n, y=(h*pi-delta)/m,
    X=(x+y)/2, T=(x-y)/2,
    U_k(z)=sin(kz)/sin z,
    V_n(z)=cos((n+1/2)z)/cos(z/2).

U_k is its finite Fourier polynomial at every apparent sine collision.
The exact factorization is

    D_n=(-1)^n[V_n(X)U_m(T)+U_n(X)V_n(T)].          (2)

The finite frequency sums give, for all real z and integers k>=1,

    |U_k|<=k, |U_k'|<=k^2/2,
    |U_k''|<=k(k^2-1)/3<=k^3/3.                  (3)

Indeed the frequencies are k-1,k-3,...,1-k; their absolute first
moment is k^2/2 for even k and(k^2-1)/2 for odd k, and their second
moment is k(k^2-1)/3.

On the whole phase rectangle,

    |X|<=pi/2+1/(4n)<8/5,
    |T|<=pi/(4m)+1/(4n)<8/5.                      (4)

For |z|<=8/5, the elementary secant estimates used in C07 are

    |sec(z/2)|<=3/2, |(sec(z/2))'|<=1,
    |(sec(z/2))''|<=3/2.

For explicit rational verification, cos(z/2)>=1-(4/5)^2/2=17/25,
and |tan(z/2)|<=|z/2|/[1-(z/2)^2/2]<=20/17<6/5.
Insert these bounds in s'=s tan(z/2)/2 and
s''=s[tan^2(z/2)+sec^2(z/2)]/4; the stated three bounds follow.
Writing q=n+1/2 and differentiating V_n=s cos(qz) gives

    |V_n|<=3/2,
    |V_n'|<=3n/2+7/4<=(151/100)n,
    |V_n''|<=3n^2/2+7n/2+23/8<=(151/100)n^2.       (5)

Both last inequalities hold at n=1000 and improve thereafter:
7/4<=n/100 and7n/2+23/8<=n^2/100 for n>=1000.
Every first phase derivative of X,T has absolute value<=1/(2n),
and their second derivatives vanish. Thus for i=gamma or delta,
(2)–(5) imply

    |D_n,ii|<=(n/4)[(151/100)tau+(151/100)tau^2
                                 +(1/2)tau^3+88/25]
             <(71/40)n, tau=m/n<=1001/1000.         (6)

The final comparison follows directly by substituting tau=1001/1000
in the positive polynomial; the bracket is less than71/10. The
corrected -cos(nu) has either pure phase second derivative bounded by1,
so

    |F_jr,ii|<=(71/80)n+1/2<=(9/10)n             (7)

on n>=1000. In particular the exceptional correction is charged.

### 2. Baseline, including the removable endpoint

At h=0 the exact polynomial gives F0=n. For h>=1 set
x0=h*pi/n,y0=h*pi/m,X0=(x0+y0)/2,T0=(x0-y0)/2. The noncolliding
baseline identity gives

    F0=sin^2(y0/2)/(sin X0 sin T0)>0.

Here0<X0<=pi/2 and0<T0<=pi/(4m)<1/1000 on n>=1000. Therefore
sin X0>=2X0/pi, sin T0>=(99/100)T0 (by sin t>=t-t^3/6), and
sin(y0/2)<=y0/2. Consequently

    F0<=50pi n^2/[99(2n+1)]<25pi n/99<n.          (8)

This proves |F0|<=n on all B, without assigning signs to its phase
perturbations.

### 3. Coordinate averaging before absolute values

Define E(gamma,delta)=F_jr(gamma,delta)-a(gamma,delta)F0. It is a
smooth finite polynomial on the rectangle, E(0,0)=0, and
|a_gamma,gamma|,|a_delta,delta|<=1/2. Equations(7)–(8) give

    |E_gamma,gamma|,|E_delta,delta|<=(7/5)n.        (9)

For any C^2 function H on this rectangle, average first in gamma
and then in delta. The one-dimensional symmetric Taylor identity in
each coordinate gives

    |Av_four H-H(0,0)|
       <=alpha^2 sup|H_gamma,gamma|/2
                         +beta^2 sup|H_delta,delta|/2.         (10)

For example split the difference as the delta-average of
[(H(alpha,delta)+H(-alpha,delta))/2-H(0,delta)], plus the
delta symmetric difference of H(0,delta). Both segments stay inside
the rectangle. No mixed derivative or sign hypothesis occurs.
Since E(0,0)=0, multiplying(10) by4 and using(9) yields

    |sum_four E|<=(14/5)n r2.                     (11)

The B endpoint(n,m) has weight1/4; the other floor(n/2) B indices
have weight one. Their total weight is exactly floor(n/2)+1/4.
Multiply(11) by these weights, sum and divide by nm. This proves(1).
The original parity-preserving reflection transports the entire
identity to the other nonnode corner. QED.

## Degree-floor inventory and limitations

Every floor used for(1) is checked above: tau<=1001/1000; the X,T
geometry; secant estimates; both V derivative comparisons; the positive
polynomial in(6); the corrected F bound(7); and sin T0>=(99/100)T0
in(8). Endpoint counting is exact for both parities. No rounded strip
count or unproved sign continuation is used.

The old C05 small-j estimate(1-120/n)^(-2)<101/100 fails at1000;
it is not used in this strip lemma or transferred to that degree.
C07's logarithmic regular-sum constants and C13's n>=500000 comparison
are also not invoked below their domains. A complete lower-domain
corner comparison requires separate regular/sine bounds and the actual
corner-value lower bound.

## Checks and history

Written exact argument; no computation is a proof premise. The new
allocation is structurally separate from frozen D01. Its later
MEASURED sanity subtraction, if run, belongs in the D02 attempt.
2026-11-06; rules/input084a64f6465956f9c75b5538f83752c30318f151;
Codex parent-assigned Sol xhigh, serving metadata unexposed.

## Dated record clarification — 2026-11-06

In the initial Split-from line, OPEN denotes the parent target's
preregistration status. The separate D02 sum and comparison proofs now
establish the uniform bracket and actual-corner descent for n>=10000;
the [distinct review](../independent-checks-D02-corner.md) accepts their
mathematics. This resolves MINOR D02-C1 without changing any preceding
byte, theorem, proof, hypothesis or degree floor. Formal Claude audit
remains separate.
