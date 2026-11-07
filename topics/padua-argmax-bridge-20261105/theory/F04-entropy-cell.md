# F04 — Uniform entropy crossing-cell and boundary-corrected quadrature bound

ID kind: PD-T; final allocation belongs to root.
Alias: PD-T?argmax-bridge-codex-F04-entropy-cell; logarithmic derivative atlas.
Split from: the OPEN full four-component I06/D13 remainder. Split into: none.

## Statement and exact objects

For EVERY integer n>=32 put m=n+1,h=pi/m. On the CLOSED signed band
1/32<=rho=|alpha|+|beta|<=1 use the inherited separate-absolute-phase
comparison convention. In the formulas below alpha,beta denote those
absolute phases. Set a=(cos alpha+cos beta)/2,p=sin alpha,q=sin beta,
d=(q-p)_+,t=beta/pi,tau_L=t,tau_R=1-t. Use EXACTLY E12/E14's profiles

    C_s(z)=I_s(phi,z)-aI_s(0,z)-d log(pi-z),
    B_L=C_L-q logz, B_R=C_R+q logz,
    Q_tau[f]=(1/m)sum_(k=2)^(m-2)f(h(k+tau))
                                     -(1/pi)integral_0^pi f.

The endpoint values of B_s mean their finite continuous limits. Then

    |sum_s Q_(tau_s)[B_s]
       +(1/m)sum_s[(3/2+tau_s)B_s(0)+(3/2-tau_s)B_s(pi)]|
                       <=120000(1+logm)/m^2.             (T)

The constant is explicit, independent of the phase box, feature spacing,
sample position and degree parity. Thus it supplies one conservative
K_box=120000 for every closed box meeting the stated band. Axes, p=0,
coefficient-zero/root coincidences and a feature exactly at a sample or
cell boundary are included. No five-fourths domain is asserted.
For a box extending beyond the band, the quantified points are its
intersection with the band; no larger phase domain is being inferred.

Overall status: **PROVED developer PAPER theorem**, distinct mathematical
review/root adoption pending. This is a FEASIBILITY bound with a large
constant, not a useful onset budget or full I06 closure. No numerical
endpoint or degree threshold was assessed. Finite Var(B_s') is neither
assumed nor inferred; F01's obstruction remains valid.

## Accepted formulas and the actual feature ledger

Dependencies are N1-14/C06 compact sections1--2 for generic J and its
derivatives; D37 section6 for their literal radius-one application;
E12 for B_s; E14/D07 for the unchanged Q, masks and four holes. No
external theorem, numerical premise, source evaluator or model change.
In particular a>=49/64>3/4 and a-(p+q)/2>=17/64>0.

On the initial half the accepted no-root identities give EXACTLY

    B_L=q log(sinz/z)-d log(pi-z),
    B_R=-q log(sinz/z)-d log(pi-z).                     (1)

Their endpoint limits at0 are finite. Also |B_s'|<2 and
Var_[0,pi/2](B_s')<3: use0<=csc^2z-z^(-2)<1,
|cotz-1/z|<=2/pi<1 and integrate the second derivative bound
q+d/(pi-z)^2 to get at most pi/2+2/pi<3.
The first inequality follows directly from csc^2z=1+cot^2z and
0<=cotz<1/z; its positivity follows from sinz<z.

On the central half put e=pi-z in[0,pi/2],u=p/2 and

    s0=a tan(e/2), s_L=s0+q/2, s_R=|s0-q/2|,
    k_s=2(s_s-u)_+, b_s=k_s-2s0-d,
    R(u,s,e)=J(u,s,e)-2(s-u)_+ log(sine).

Then, with sigma_L=-1,sigma_R=+1,

    B_s(pi-e)=R(u,s_s(e),e)+b_s(e)log(sine)
                 +d log(sine/e)+sigma_s q log(pi-e).   (2)

Here b_s(0)=0. The N1 entropy limits give finite endpoint values of R,
including u=0 and s=u; the other terms have finite limits as well.
In particular b_s log(sine) tends to0. All joins are continuous.

The actual possible features are endpoints, the joining point pi/2,
s_R=0, s_s=u, and root/no-root thresholds s_s*sine=u. No feature is
deleted from a quadrature cell. To count them set x=tan(e/2) in[0,1].
On each side s is piecewise affine: the left has one affine piece and
the right at most two. Define

    P(x)=u^2(1+x^2)^2-4s(x)^2x^2.                     (3)

This is quartic. For the right side s^2=(q/2-ax)^2, so the SAME
quartic applies on both affine pieces. It is nonzero (its leading
coefficient u^2-4a^2 is negative). Hence each side has at most four
P zeros. The left has at most one coefficient zero, the right at most
two, and the right has at most one absolute-value switch. Include
P zeros even when not an active threshold. Counting0,pi/2,pi as well
gives feature sets F_L,F_R with at most8 and10 points, respectively.
Coincident features are merged. This count is uniform as phases move.

## 1. Uniform logarithmic derivative envelope and crossing-cell modulus

The accepted generic formulas, away from their displayed features, are

    |R_s|<=log((u+s)/|u-s|), R_s=0 if u=0,
    R_e=2[u cose-sqrt((u^2-s^2sin^2e)_+)]/sine (s>u),
    R_e=0 (s<=u).

They imply the useful UNIFORM bound0<=R_e<=2s<=3. In the root regime,
write D=sqrt(u^2-s^2sin^2e). Since D<=u cose,
u cose-D<=sqrt(u^2cos^2e-D^2)=sine*sqrt(s^2-u^2).
In the no-root regime u<=s*sine, so2u cote<=2s cose. The u=0
case is used directly; no inverse-u estimate is introduced.

On each monotone affine-sign piece of s(e), |s'| is between a/2>1/3
and a<=1. If s=u has a solution, its distance controls |s-u| by
integration of that lower derivative bound. If there is no solution
on a piece, the same inequality follows from distance to the endpoint
where |s-u| is smallest. Every such endpoint belongs to the feature
ledger. Thus, with D_s(z)=dist(z,F_s),

    |R_s|<=log(6/D_s(z))                              (4)

at central nonfeature points; use u+s<=2. A superfluous closer feature
only increases the majorant. The direct u=0 formula also satisfies(4).

The explicit maxima defining b_s show |b_s'|<=4 and b_s(0)=0,
so |b_s|<=4e. Moreover |cote-1/e|<1 and |q/(pi-e)|<1.
Differentiate(2) only off features; using |s'|<=1 and(4) gives

    |B_s'(z)|<=9+5log(6/D_s(z)).                      (5)

Here b'log(sine) costs at most4|log(sine)|; b*cote costs at most4;
R_e costs3; the last two smooth derivatives each cost1. The endpoint
site pi implies D_s<=e and |log(sine)|<=log(2/e)<=log(6/D_s).
On the initial half(5) follows already from |B_s'|<2. All logarithms
on the right are positive since distances are below pi<6.

For an interval I of length ell and any site r, direct integration gives

    integral_I log(6/|z-r|)dz<=ell[1+log(12/ell)].

The maximum occurs when r is the interval midpoint: splitting the
integral into the two distances verifies this, and an exterior r gives
no larger value. The maximum over sites is bounded by their sum.
Since each F_s has at most10 points, (5) proves, for0<ell<=pi,

    integral_I |B_s'|<=60ell[1+log(12/ell)].            (6)

B_s is globally absolutely continuous: it is continuous, is piecewise
C1 off finitely many features, and(5) gives an integrable derivative
through every feature/end. Applying the fundamental theorem on truncated
pieces and passing to their continuous limits proves this assertion,
without assigning an artificial derivative at a cusp. Therefore(6) also
bounds |B_s(y)-B_s(x)| for |y-x|=ell. It is a UNIFORM crossing-cell
modulus, including merged features and u=0, not a fixed-phase BV' norm.

## 2. Variation on cells separated from the finite feature set

Let0<delta<=h and retain any union G_s of closed intervals whose
distance from F_s is at least delta. Variation here means the sum of
variations over connected retained intervals, without bridging gaps.
Put A=log(6/delta)>1. Then

    sum_s Var_(G_s)(B_s')<=400 A.                     (7)

The finite-monotonicity justification is given explicitly to cover
degenerate parameters; polynomial degrees alone are not the assertion.
For u=0, R is identically0, so its two derivative terms are absent.
For u>0, fix an affine piece s=A0+b x, b=+a or-a.
In the same-sign region s<u,

    R_s=log((u+s)/(u-s))

is monotone. In the opposite-sign root region s>u,P>0 put
X=s(1-x^2),Y=sqrt(P). There X>Y>=0, because
X^2-P=(s^2-u^2)(1+x^2)^2>0, and

    R_s=log[(X-Y)/(X+Y)].

Its critical points solve2X'P-XP'=0, a polynomial of degree at most6.
If that polynomial vanishes identically, the displayed derivative is
identically zero on the root region. Otherwise it has at most6 roots.
Partition additionally at s=u (at most1) and P=0 (at most4). In the
no-root region R_s=0. Hence at most12 monotone pieces per affine piece,
at most24 for either full folded side. Restricting a monotone piece to
disjoint retained intervals cannot increase its total variation beyond
its range on retained points. By(4) that range is at most2A. Thus
Var_(G_s)(R_s)<=48A per side. Since |s'|<=1 and its full variation
is at most4 (smooth variation at most a/2 and the possible sign reversal
at most2a), the product R_s*s'
has retained variation at most52A per side.

For R_e the root-region formula becomes

    R_e=[u(1-x^2)-sqrt(P)]/x.

Its derivative zeros require

    2P-xP'=2u(1+x^2)sqrt(P).

Squaring gives a polynomial of degree at most8. If it is not identically
zero there are at most8 candidate zeros. If it is identically zero,
2P-xP' has constant sign on a connected P>0 region; the derivative
either vanishes identically or has a fixed negative sign. Thus this
exception also gives monotonicity. In the no-root region R_e=2u cote
is monotone; for s<=u it is0. The previous1+4 boundaries and at most8
critical points give at most14 monotone pieces per affine piece, at most28
per side. Since0<=R_e<=3, its retained variation is at most84 per side.
R_e is continuous at the branch boundaries: the generic formula tends
to0 at s=u, and the root/no-root values agree when P=0. R_s also
agrees with0 at the latter boundary. Its divergent s=u sites were
excluded. At s_R=0 the u>0 entropy derivative is0; for u=0 all R
terms are0. Thus no uncharged derivative-factor jump is hidden in
these monotone-piece counts.

For the remaining terms in B_s', the explicit b derivatives are piecewise
coefficients0,-a,-2a times sec^2(e/2), with at most4 pieces. Their smooth
variations total at most8 and their at most3 jumps cost at most12.
Consequently Var(b_s')<=20 and sup|b_s'|<=4. Since log(sine) is
monotone with sup/variation at most A on e>=delta,

    Var(b_s'log(sine))<=24A.

Also |b_s|<=4e and |b_s'|<=4 imply

    Var_(e>=delta)(b_s cote)
       <=integral_delta^(pi/2)[4cote+4e csc^2e]de
       <=(4+pi^2)log(pi/(2delta))<=14A.

The smooth terms d(cote-1/e),sigma_s q/(pi-e) have variation at most2
and1, respectively. Initial-half variation adds less than3 by(1).
Even charging a joining derivative jump by4 is sufficient, since both
one-sided derivatives there have magnitude below2. This yields, per side,

    Var_(G_s)(B_s')<=52A+84+24A+14A+2+1+3+4
                                      =90A+94.

Sum both sides and use A>1 to obtain(7). Root thresholds with an
unbounded second derivative cause no gap in this count: their first-
derivative factors above have bounded ranges, and each monotone-piece
variation is charged by that range. No feature-separation lower bound
or inverse-p constant enters(7).

## 3. Actual fixed cells, all holes and the explicit constant

For each side the ACTUAL cells are centered at h(k+tau_s),k=2,...,m-2.
Their union starts at l_s=h(3/2+tau_s) and ends at pi-c_s,
c_s=h(3/2-tau_s). The four lengths lie between h/2 and5h/2.

Call a cell bad if its distance from F_s is less than h. A fixed site
can affect at most5 cells of a grid of spacing h (their centers lie in
an interval of length3h). Since the two feature counts sum to at most20,
there are at most100 bad cells in total. This remains true on an exact
sample/feature or cell-boundary coincidence, including duplicate sites.

For one bad cell, (6) bounds its unnormalized midpoint error by
60h^2[1+log(12/h)]; integrate the difference from its center. The entire
bad-cell contribution, after normalization1/pi, is at most

    (6000h^2/pi)[1+log(12/h)].

Every remaining cell has distance at least h from F_s. Its derivative
has bounded variation by(7). The centered Peano kernel has magnitude
at most h^2/8, so the total good-cell contribution is at most

    (h^2/(8pi))*400log(6/h)
                      <=(50h^2/pi)[1+log(12/h)].

This is the kernel for the actual fixed centers, not an inference from
an averaged translation modulus. At a feature-boundary equality the cell
may simply be put in the bad set; the same count/bound remains valid.

It remains to subtract the four MISSING intervals. After adding precisely
the boundary values in(T), each hole of length ell contributes only
its integral of B_s minus its own endpoint value. By(6) its absolute
unnormalized contribution is at most

    60integral_0^ell r[1+log(12/r)]dr
                    =30ell^2[3/2+log(12/ell)].

Here h/2<=ell<=5h/2, so their total, normalized by1/pi, is bounded by

    (1125h^2/pi)[1+log(24/h)];

use sum ell^2<=25h^2 and
3/2+log(12/ell)<= (3/2)[1+log(24/h)]. All four hole lengths and both
endpoint values are included, with their actual signs before the upper.

Combining gives at most

    (7175h^2/pi)[1+log(24/h)].

Since h=pi/m,pi<4,pi>3 and log8<3, this is less than
114800(1+logm)/m^2, hence proves(T) with120000. All these are written
analytic inequalities; no scalar run or selected-degree evaluation.

## Scope and remaining obligations

This resolves the registered entropy-cell FEASIBILITY target, with a
deliberately conservative constant. It does not give the small K_box
needed for an improved onset. T's analytic initial/scalar logarithms,
log-n max profiles, pole numerators, fixed-origin Shift, actual retained/
ordinary rows, scalar mesh and true-origin allowance keep their separate
charges. The signed finite alpha cusp remains; no complete I06/D13 claim.
No T1 implementation/measurement or extension to rho<=5/4 is supplied.

## Provenance and checks

Gate and durable ROOT target registration preceded all F04 algebra. The
explicitly requested LOCAL idea/attempt did NOT precede initial hand
algebra; this sequencing error was immediately disclosed and canonically
preserved. Root then explicitly directed continuation from the actual
record, without waiving/accepting the ordering. Registered P2 and its
feature/cell/truncated-variation route preceded the continued full proof.
No success is used to rewrite chronology; final protocol audit is separate.

2026-11-07, requested Sol xhigh, serving metadata unexposed. Rules read
4a5de2012bad94601c713b2ff5517f2e3fb80af2; unchanged hashes verified at
0a14af36b581e2c8ed7771144a9daafdded05ed4. Only owned F04 prose edited.
No scripts, source/imports, numerical/scalar/phase/degree/endpoint/native/
root/quadrature/compiler/build/pack jobs, shared-file or Git mutations.
Distinct mathematical review and root adoption remain pending.


## Root disposition after distinct mathematical review —2026-11-07

Root adopts the exact uniform band/n>=32 theorem with K120000 as a feasibility result; no useful onset or wholeI06 conclusion. The original frozen proof prefix is preserved and identified in [independent mathematical review](../independent-checks-F04-F05.md). Novelty/priority, disclosed chronology and final Claude/readiness judgments remain separate and unwaived.
