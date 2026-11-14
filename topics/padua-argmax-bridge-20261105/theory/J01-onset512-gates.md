# PD-T?argmax-bridge-codex-J01 — Two scalar gates for the analytic tail from 512

ID kind: PD-T. Aliases: onset512 analytic refactor; radius-one polynomial;
single absolute gate. Split from: none. Split into: none. This is the
approved architecture B in handoff 29, not a new mechanism or novelty claim.

## Statement and status

Use the original corrected Padua kernel, highest first-coordinate
coefficient one, unequal meshes n,m=n+1, original endpoint weights, actual
polynomial collision values, and the closed odd physical charts of
`paper/sections/localization-unified.tex` at input
`b45e29fa1fe3dbfa2517ff8043e5d9c440870530`. Write S for the periodic
primitive, Lambda_c=S(0,0) for the actual nonnode-corner value, and
lambda=S-Delta, with Delta>=max(Q_h,Q_v)>=0. Separate absolute phases
x=|alpha|,y=|beta| satisfy rho=x+y<=pi. Coordinates are never exchanged.

The following gates imply that every integer n>=512 has precisely the
two parity-correct nonnode corners as maximizers:

1. For integer n>=512 and rho<=1,
   S-Lambda_c<=P_n(rho)=C4+g+f*rho-e*rho^2, defined below.
   For every real n>=512 its unrestricted maximum is <41/1000,
   P_n(1/2)<-1/7, and its vertex is <1/2. The unrestricted maximum and
   P_n(1/2) strictly decrease with n.
2. At every eligible noncorner projection, rho<=1/2 and integer n>=295
   imply Q>1/20. In particular lambda<Lambda_c-9/1000 on the noncorner
   half-radius region for n>=512.
3. For n>=160 and 0<rho1<=pi, if
   tan(rho1/2)>=(t+2KD)/(T+j0), then every rho>=rho1 satisfies
   Lambda_c-S>G(n,rho1), where j0=23/250,t=221/500 and

       G=(T+j0)(1-cos(rho1/2))-(t+2KD)sin(rho1/2)
              -t^2*cos(rho1/2)/(2(T+j0))-CEbar-ebar.

   This explicit scalar function strictly increases with real n>=160,
   and the tangent condition persists once true. In particular
   G(n,1)>1/2 for n>=512 and G(n,pi/2)>3/100 for n>=192.

Initial status, before the preregistered exact check: **CONDITIONAL** on
the finite rational comparisons specified in section 6. The all-n
reductions and proofs are written below. Distinct mathematical review
and an independent execution are required before root adoption. This
status is updated by a dated addendum after execution; no audit planning
number is used as a premise.

## Definitions and exact premises

All scalar functions below are extended to real n; finite Padua objects
are used only for integral n. Set L=log n,H=1+L,b=4/pi^2 and
r0=log(5/2)+1/18. The unchanged uniform functions are

    T=(4L^2-3L)/pi^2,
    D=((52/pi^2)H+7)/n+10/n^2+20H/(pi*n^2),
    Mesh=b(2L+2r0)/n+[4+b(L+1/n)]/(4n^2-1)
           +b/(2n-1)^2+[5+b(log(n+1/2)+2)]/[4(n-1/2)^2],
    ebar=D+Mesh+1/n,
    KD=((6+16/(3pi))H+2/pi)/n,
    MA=1/pi+4/pi^2, gn=1+log(2+8m/(3pi)),
    Gg={7MA*L+111/2+
         [63+log2+4logpi+7logm+16log(2m)+(3/2)gn]/pi}/m,
    W=(3logm+log2+2logpi+2)/(pi*m),
    CEbar=D+Gg+(64+16L)/n+318/n^2+Mesh+W,
    A4=4/n+40H/(pi*n^2), C4=A4+20/n^2,
    db=(17L+27)/n^2,
    kx=((19/2)H+(23/3)L+155/2)/n+152/n^2, ky=kx+db.

The exact accepted component contracts used are:

    |S-M_infty|<=CEbar+KD(sin x+sin y), n>=32, rho<=pi;
    Lambda_c-M_infty(0)>-ebar, n>=160;
    M_infty(phi)-M_infty(0)<=-u(T+j)+t0*sin x, rho<=pi;
    S-Lambda_c<=Ec-u(T-ebar+A4+rho*JW+j)+C4+kx*x+ky*y,
                                      n>=160,rho<=1;
    Ec<=(5/12)x^(3/2), rho<=1,
    u=1-(cos x+cos y)/2, JW=((3/2)H+6)/n+148/n^2>0.

Here j>j0 and 0<t0<t follow analytically from [J02](J02-elementary-constant-enclosure.md).
The global logarithmic coefficient gives the -uT loss; the relative
contract uses the regular model loss after isolating Ec. In particular
the full ebar is paid in the absolute gate, and only u*ebar appears
in the matched relative gate. No sign assumption on the actual origin
error is made. The 64+16L term is the combined correlated allowance,
not a standalone retained-row bound.

## 1. Radius-one reduction to a quadratic

For 0<=z<=1, the cosine Taylor inequality gives
(1-cos z)/2>=z^2/4-z^4/48>=11z^2/48. Also
sqrt(x)<=x+1/4, since (sqrt(x)-1/2)^2>=0. Define

    U=T-ebar+A4+j0,
    l1=kx+5/48, l2=ky,
    d1=11U/48-5/12, d2=11U/48, S0=d1+d2,
    e=d1*d2/S0, f=(d2*l1+d1*l2)/S0,
    g=(l1-l2)^2/(4S0).

Whenever U>=0 and d1,d2>0, dropping the favorable rho*JW and j-j0
terms, then applying the preceding inequalities, gives

    S-Lambda_c<=C4+l1*x+l2*y-d1*x^2-d2*y^2.             (1)

On the line x+y=rho, completion of the square gives, for every real x,

    l1*x+l2*(rho-x)-d1*x^2-d2*(rho-x)^2
       =g+f*rho-e*rho^2-S0*(x-xstar)^2,
    xstar=(d2*rho+(l1-l2)/2)/S0.                       (2)

Thus (1) implies the stated P, even if xstar lies outside the physical
segment. Only the n>=512 application needs positive curvatures here.
The displayed formula itself is usable at any earlier n where they are
positive; it asserts no new degree conclusion there.

## 2. All-real-n monotonicity of the coefficients and both needed maxima

On n>=32, L>1 and every D,Mesh,KD,CEbar,C4,kx,ky term is positive
and strictly decreasing. Here are complete elementary checks, so the
transfer does not depend on a sampled n-grid:

- (aL+c)/n^p decreases when a,c>=0 and p(aL+c)>a.
  This covers H/n,H/n^2,kx,db,(64+16L)/n and inverse powers.
- For Mesh, split its second term into (4+bL)/(4n^2-1)
  and b/[n(4n^2-1)]. The denominator's logarithmic derivative is
  >2/n, whereas the first numerator's derivative is b/n and its
  numerator is >b. The last Mesh numerator has derivative
  b/(n+1/2); its denominator has logarithmic derivative 2/(n-1/2),
  and its numerator is >b. All remaining terms have the previous form
  or are manifest decreasing inverse powers.
- For Gg and W, log n/m decreases because m/n<=33/32<L
  (indeed log32=5log2>3 by J02);
  logm/m and log(2m)/m decrease because their logarithms exceed one.
  Also m*gn'=cm/(2+cm)<1<gn, c=8/(3pi), so gn/m decreases.
  Positive linear combinations prove the assertion, including ebar.

Although A4 decreases, T+A4 increases on n>=32. Indeed using pi>3,
pi^2<10, 8L-3>=5L, and 1+2L<=3L gives

    (T+A4)'>(L/n^3)(n^2/2-4n-40)>0.                  (3)

The polynomial is positive at 32 and increasing thereafter. Since ebar
decreases, U and both d's strictly increase. At the base 512 the exact
comparison gives d1>1, hence all curvatures stay positive.

Two useful identities avoid any unsupported assertion about f alone:

    max_(rho in R) P_n(rho)=C4+g+f^2/(4e)
                          =C4+l1^2/(4d1)+l2^2/(4d2),
    rho_vertex=f/(2e)=l1/(2d1)+l2/(2d2).              (4)

The positive l's strictly decrease and the positive d's strictly
increase. Thus the maximum and the vertex strictly decrease for every
real n>=512. The base vertex is <1/2. Consequently P_n decreases on
[1/2,infinity), proving the full half-to-one interval assertion.

For the separate assertion that P_n(1/2) decreases, put
delta_l=l1-l2=5/48-db. The base check has 0<db(512)<5/48; since db
decreases, 0<delta_l<5/48 for every n>=512. At rho=1/2, both coordinates
of the optimizer in (2) are positive: xstar>0 and
ystar=(d1/2-delta_l/2)/S0>0, because d1>1>5/48. Thus P_n(1/2)
is exactly the maximum of the right side of (1) on the fixed compact
segment x+y=1/2,x,y>=0. That right side strictly decreases at every
point as n increases. More explicitly, for n2>n1 every point drops by
at least C4(n1)-C4(n2)>0, so the maxima strictly decrease too. This
establishes the requested real-n step without differentiating a moving
optimizer or presuming that f decreases.

## 3. Uniform twentieth floor from 295

Use the three exhaustive selected-pair center classes, with exactly the
same physical projections, folded branches, endpoint weights and finite
collisions as C02 and the selected-pair lemma. At radius 1/2 the nearest
four center distances and the remaining small-angle centers each have
the existing strict Q>1/20 proof for n>=64. The only needed middle-class
band is c=2 on [pi/100,pi/4]. Its existing band formula gives

    Q>=Fh(n)=539*Ih/1936-(140*A+400*Rh)/(157n)-800*A/(3n^2),
    A=97*(15/16)/100-1/4,
    Ih=2303*(15/16)/5000-471/2500,
    Rh=4837*(15/16)/1875-5/6.                         (5)

All three constants are positive rationals. Therefore Fh increases
strictly for every real n>0. The exact rational comparison at 295
gives Fh(295)>1/20. This proves the floor for every integer n>=295;
no monotonicity in radius, extrapolation from n4096, or radius-dependent
floor function is needed in the new tail. The ordinary finite floor
tiers for 41<=n<512 remain unchanged for certificates.

## 4. The absolute gate and its tangent condition

Combining the global model loss, full global error and one-sided actual
origin bound gives, for n>=160 and every physical phase,

    Lambda_c-S>u*Theta-t*sin x-KD(sin x+sin y)-CEbar-ebar,
    Theta=T+j0.                                          (6)

Put h=rho/2 and delta=(x-y)/2. Then a=cos h*cos delta and
sin x+sin y=2sin h*cos delta. The bracket subtracted from Theta in (6)
is A(h)cos delta+B(h)sin delta, where

    A=Theta*cos h+C*sin h, B=t*cos h, C=t+2KD.

It is at most R(h)=sqrt(A^2+B^2), by Cauchy--Schwarz, for either sign
of delta. If tan h>=C/Theta then A'=-Theta*sin h+C*cos h<=0 and
B'=-t*sin h<=0. Both A,B are nonnegative for h in [0,pi/2], so R
is nonincreasing there. The same conclusion holds at pi/2 by continuity.
Since tangent increases, the condition at h1=rho1/2 suffices for all
h>=h1. For rho1=pi the condition is interpreted at its infinite limit;
A(h1)>0 and B(h1)=0, so the argument still applies.

Finally for h1<pi/2, A>=Theta*cos h1>0, and

    sqrt(A^2+B^2)<=A+B^2/(2A)
                     <=A+t^2*cos h1/(2Theta).             (7)

At h1=pi/2 this inequality holds directly with B=0. Substitution gives
G in the statement. No physical phase is replaced by an independently
majorized fictitious tuple; these are inequalities at each actual phase.

For fixed rho1, Theta strictly increases, while KD,CEbar,ebar decrease
on the relevant real half-line. Each term in G therefore increases:
1-cos h1>0, sin h1>=0, cos h1>=0, and Theta>0. Hence G strictly
increases. The ratio C/Theta decreases, proving persistence of the
tangent condition. The base checks at (512,1) and (192,pi/2) give the
stated uniform gaps. The far guard, onset 192 and gap 3/100 are exactly
those consumed by the frozen hybrid certificates.

## 5. Assembly and source map for removing the old tail geometry

For n>=512, a noncorner chart with rho<=1/2 has
lambda<=S-Q<Lambda_c+41/1000-1/20=Lambda_c-9/1000.
For 1/2<=rho<=1, P_n(rho)<=P_n(1/2)<-1/7 excludes every chart.
For 1<=rho<=pi the absolute gate gives S<Lambda_c-1/2. At an actual
corner, the existing corner-256 theorem excludes every nonorigin point
of the closed pi/4 square by the loss (A^2+B^2)/30; that square contains
the rho<=1/2 physical diamond. All closed charts, ties and seams are
covered. Parity reflection gives the other corner and the exact equality
classification. This is an analytic n>=512 theorem, with no finite
degree certificate premise.

| Retained input | Exact source needed | Consumer here / in frozen certificates |
|---|---|---|
| Kernel, lambda=S-Delta, projections | PD-T101/364, C01/C02; paper `ul:primitive`--`ul:projections` | physical reduction and floors |
| Cancellation/root formulas and scalar maximum including cusp | E07-H; E11 central pair, with E06 regular-loss map | model loss, full finite comparison, corner-256 |
| Uniform correlated error CEbar | E08-phase-global-error (3),(4), including combined 3H/n saving | G, analytic norm and corner diagonal |
| One-sided actual origin | E08-origin-lower (4), n>=160 | both gates and corner-256 |
| Radius-one signed outer block | E14-wide-signed-outer (1), n>=32,rho<=1 | relative row telescope; its theorem stays, annular application is unnecessary |
| Ordinary, retained and scalar mesh pieces | D37-relative-wide; E04-wide-retained-origin; Rmesh separately | relative comparison, kx,ky and corner axes |
| Central bound 5/12 and general root convolution | E11-central-pair and E11-model-radius-halfpi | P; corner axis/diagonal bounds |
| Middle-class band at radius 1/2 | C02 band argument / E01 floors; paper `ul:band-formula` | (5) only; no radius-dependent tail statement needed |
| Finite floor tiers 41/64/160 | C02/D29, paper `ul:finite-floors` | unchanged certificates only |
| Corner squared Peano, n>=256, pi/4 square, 1/30 | E12-corner256 and D08 signed-family interpolation | tail and frozen corner branch; unchanged |
| Far branch n>=192,rho>=pi/2,gap 3/100 | section 4 above | replacement proof for existing frozen far branch |
| Limiting constants | J02 and analytic kappa/origin identities | j,t and global norm constant 9/4; no PD-T271 computation |

The E14 annular theorem is used above only as a locator for its component
collection (3), which is independently reconstructed in the input table:
6+10+11+50+1/2=155/2, 148+4=152, and 8H+3H/2=19H/2.
Its regional conclusions, E14-halfnear320, E14-outer320, E13 outer
geometry, E15's separate u-dependent majorant, the near relative column,
the 3/8 central specialization and Bbeta lower bound are not premises.
The phase-dependent CEphi formulas may remain proof intermediates for
CEbar, but their standalone statements and fixed-phase monotonicity are
not needed by this architecture. Retain the correlated 3H/n saving:
discarding it would alter the consumed CEbar and is not this theorem.

The finite certificates still require their own u',v', signed norm
witnesses, rectangle and pi bracket. This refactor neither removes nor
revalidates those finite premises. Historical E01--E15 files and reviews
remain frozen.

## 6. Exact checks, trusted arithmetic and history

The prospective commands and kill condition are recorded before any
calculation in [PREREGISTRATION](../code/onset512_analytic/PREREGISTRATION.md).
The finite reduction consists of rational interval expressions for
exactly five bases: the relative quantities at 512, G at (512,1),
G at (192,pi/2), and the floor at 295; J02 supplies constants.
`check.py` uses Fraction with outward rational rounding. Its logarithm,
pi and trigonometric brackets have the elementary proofs in J02.
For rho1=pi/2 it uses sin(pi/4)=cos(pi/4)<707107/10^6,
verified by 2*(707107/10^6)^2>1, in every adverse occurrence.
Only standard Python integer/Fraction semantics and the short source
are trusted by this finite check. Section 2--4 supply the all-n proof;
finite agreement alone would not do so.

Runs needed at initial write: the single preregistered command, its
small receipt, and distinct review with an independent execution.
No native, threshold-scan, certificate, quadrature or manuscript job is
part of this developer scope. No failed attempt has occurred at this
initial boundary; any failed assertion must be preserved and reported
before changing the gate.

2026-11-08: assigned Codex mathematical developer, requested Sol xhigh;
serving metadata unexposed. Root owns Git. Approved existing architecture,
so no novelty campaign applies. Rules/source SHA is given above.

### Developer execution addendum — 2026-11-08

The single registered command ran successfully using Python 3.12.14;
all assertions passed, exit 0, observed wall time 0.16123836 seconds.
The [small receipt](../code/onset512_analytic/receipt.json) pins the exact
checker and preregistration sources. Its outward six-place intervals are
P512 maximum [0.040785,0.040786], P512(1/2) [-0.143070,-0.143069],
vertex [0.147341,0.147342], G(512,1) [0.534264,0.534265], and the
conservative linearized G(192,pi/2) lower [0.098316,0.098317]. The
floor at 295 is [0.050064,0.050065]. The far value differs from the
audit's square-root gate planning value because (7) and the rational
square-root upper bound deliberately weaken it.

The registered finite obligations are discharged by exact arithmetic.
The written proof and finite reduction are complete; independent
execution and mathematical review remain pending before root adoption.
No failed assertion, retry, changed cutoff, fallback or other scientific
job occurred. The initial CONDITIONAL status above is historical;
current claim status awaits the distinct review's independent execution.

### Current status after distinct review — 2026-11-08

**PROVED** at the statement and dependency scope above. The distinct Astra
xhigh reviewer reconstructed the all-real-n arguments and independently
executed the frozen Fraction checker, exit 0. Its
[review](../independent-checks-onset512-response.md#analytic-gates-and-elementary-constants--accepted-at-the-written-scope)
identifies the exact reviewed source hashes and remaining finite-coverage
obligation. This addendum adopts that reviewed proof; it does not claim that
the new certificate campaign or the next Claude audit is complete.
