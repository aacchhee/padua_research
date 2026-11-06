# PD-T?argmax-bridge-codex-D11-far — Full closed far exclusion from degree16000

ID kind: PD-T. Aliases: true-constant twenty-two-u onset budget;
full-phase primitive comparison at16000.
Split from: D11 prospective global onset. Split into: none; the near and
global comparisons have separate D11 records.

## Statement and definitions

For every integer n>=16000 and every signed phase pair with

    1/2<=rho=|alpha|+|beta|<=pi,

D02/PD-T364's original corrected primitive satisfies

    S_n(alpha,beta)<Lambda_c(n)-19/100.                (1)

Here Lambda_c(n)=S_n(0,0), L=log n, m=n+1,
a=(cos|alpha|+cos|beta|)/2,u=1-a, and

    M_infty(psi,L)=(4a/pi^2)L^2+b_full(psi)L+C_infty(psi)

is D02's TRUE completed model. All quantities have their original
continuous weighted endpoint values, including a=0, axes, vertices,
both degree parities and finite-polynomial collisions.

## Status and assumptions

Overall status: **PROVED**, developer analytic assembly with the frozen
directed scalar endpoint under the numerical contract linked below.
Distinct D11 mathematical/source/arithmetic review is **PENDING**; no
independent acceptance or root range adoption is asserted. Analytic
arithmetic is exact and all logarithms are natural.

## Depends on

- [C08 weighted coefficient](C08-far-weighted-coefficient.md):
  b_full-b_c<=3u/pi^2 on the closed diamond.
- [D10 far constant](D10-far-relative-constant.md):
  C_infty(psi)-C_infty(0)<22u on the CLOSED domain rho>=1/2. Its
  accepted PD-T271 origin-constant Arb enclosure, analytic coefficient
  reduction and exact tail remain explicit inherited numerical premises;
  see [D08 constant provenance](../attempts/D08-corner-limit.md).
- [D05 full comparison](D05-outer-comparison.md), equation(2), at fixed
  R=2,delta=pi/8: valid for every integer n>=ceil(2pi R/delta)=32.
- [D08 near representation](D08-near-representation.md), full formula
  Ehat(n) valid at the ORIGIN for n>=32, with decreasing Ehat. Its
  Ehat<1/80 conclusion at40000 is not used here.

D10's accepted supplementary report is
[independent-checks-D10-relative-constant.md](../independent-checks-D10-relative-constant.md),
SHA256 `bdcadf119fb905f898612ad25b9123bf8ff58184d6ef573e1503a740d987964c`.

## Proof

### 1. Keep the relative constant and the actual coefficient inequality

Use absolute phases without exchanging the n,m meshes. Set

    T(n)=(4log^2 n-3log n)/pi^2.

C08 and D10 give on the complete closed FAR domain

    M_infty(0,L)-M_infty(psi,L)>u[T(n)-22].            (2)

Indeed the quadratic coefficient loss is4u/pi^2, and the possible
linear coefficient increase is at most3u/pi^2. The constant charge is
22u, not a phase-independent difference of two absolute constants.

Writing e=|alpha|+|beta|,d=|alpha|-|beta| gives
a=cos(e/2)cos(d/2)<=cos(e/2)<=cos(1/4). The alternating cosine
remainder at1/4 yields

    u>=1-cos(1/4)>=1/32-1/6144=191/6144.             (3)

The endpoint below has T(16000)>35>22. Also
T'(n)=(8log n-3)/(pi^2*n)>0 on n>=16000. Therefore (2)--(3) imply

    M_infty(0,L)-M_infty(psi,L)>F(n),
    F(n)=(191/6144)[T(n)-22],                         (4)

and F increases on the entire unbounded degree range. All divisions
above are by fixed positive constants; a=0 requires no separate inverse-a
argument.

### 2. Use the full finite FAR allowance on its actual n>=32 domain

Define U_F(n) to be EXACTLY the D05-outer-comparison(2) right side

    U_F=E_D04+e4+I_n+D_pole+T_Z                       (5)

at R=2,delta=pi/8 and the conservative independent substitutions

    a=1,p=1,P=2,d=1,abs(U0)=8,H_n<=1+log n.          (6)

Every named component in (5) retains its complete formula from that
theorem; e4=e_mesh+e_rows+e_collision. In particular, none of the
positive e_rows or I_n terms is dropped. The error is evaluated on the
entire closed diamond, with no fixed R64/.01 old-model theorem applied
at16000. The nonnegative formulas are nondecreasing in these inputs.
For the only nonlinear input dependence, u0[1+log(1+S/u0)] is
nondecreasing in u0,S>=0, with its continuous value at u0=0: its u0
derivative is1+log(1+x)-x/(1+x)>0, x=S/u0. Thus (6) is a valid
uniform majorization, and

    |S_n(psi)-M_infty(psi,L)|<=U_F(n), n>=32.         (7)

Here is a fresh monotonicity verification of the EXACT fixed-parameter
formula, consistent with D08's earlier check. Put X=m/8>=33/8.
The E_D04 and D_pole terms are positive sums of (cL+d)/n^j,j>=1,
which decrease for L>3. The exact e_rows=(181+19L)/n+21600/n^2
decreases. The L/m term of e_mesh has derivative numerator
1+1/n-L<0. Its C_X shares are positive multiples of

    [c+(1/2)log(X+1/2)]/(X-1/2)^q, (c,q)=(5,1),(6,2).

Their derivative signs are those of
(X-1/2)/[2(X+1/2)]-q[c+(1/2)log(X+1/2)]<1/2-q*c<0.
The remaining mesh inverse powers decrease. The collision term is a
positive (c+d*log(2m))/m whose numerator exceeds d, plus inverse
products, and therefore decreases.

In I_n all auxiliary constants are fixed after (6). Its form is
(cL+d0+e0*log m)/m with nonnegative fixed constants and d0>0.
Its derivative numerator is
c(1+1/n-L)+e0(1-log m)-d0<0. Finally retain D05's exact definitions

    h=pi/m, epsilon=3h/2, ell=5h/2,
    W(z)=7+(2/pi)[3+2log(4pi/z)],
    Q(z)=(2z/pi)[7+(2/pi)(5+2log(4pi/z))],
    T_Z=[32+6log(6/epsilon)]/(2m)+Q(ell)
                          +[W(delta-h/2)+2W(2h)]/m.

The BV, Q(ell), and W(2h)/m terms have the form
(c*log m+d0)/m. Their numerators exceed c for m>=33, so they
decrease. Since delta-h/2 increases to delta and W is positive
decreasing there, W(delta-h/2)/m decreases too. All its arguments
are positive in the valid n>=32 geometry. This proves that U_F
decreases for all real n>=32. Ehat also decreases there, by its full
formula and the explicit check in [the near proof](D11-near-comparison.md).

### 3. Transfer the scalar margin to every degree

The preserved16000 receipt gives outward bounds

    T(16000)>35.036379764739078,
    F(16000)>0.405265061045762,
    U_F(16000)<0.179267903978979,
    Ehat(16000)<0.027003655663226,
    F-U_F-Ehat>0.198993501403557>19/100.              (8)

Exact terminating-decimal subtraction of the displayed bounds already
gives the final strict19/100 comparison; the50-digit endpoints retain
the tighter lower bound shown. Since F increases and both errors
decrease, the same comparison holds for every n>=16000. At zero use
the NEAR representation, rather than substituting the larger FAR error:

    Lambda_c-S_n(psi)
       >=M_infty(0,L)-M_infty(psi,L)-Ehat(n)-U_F(n)
       >F(n)-Ehat(n)-U_F(n)>19/100.

This proves (1). The strict constant estimate, the signed coefficient
loss and the two actual finite representations have all retained
their separate valid domains.

## Checks, scope and open items

See [the canonical attempt](../attempts/D11-onset.md) for frozen source,
receipt, command, numerical trusted base, actual chronology and required
distinct replay. No new scalar/native/board/quadrature/phase-grid run was
made while completing this proof. Physical lambda<=S_n is a separate
PD-T364 consequence. Global equality classification additionally needs
the near noncorner and actual-corner cases. No finite corner lower is
deduced merely from the limiting constant, no old quantifier is moved,
and the full relative S_n-a*S_n(0) estimate remains OPEN.

## History

2026-11-06, resumed Codex mathematical developer, parent-assigned Sol
xhigh; serving metadata unexposed. Rules/input read at
`5ecf97801631192fd10d84089c5a8c79bfb95138`. This applies accepted D10
phase bounds in a new sufficient budget and makes no new-mechanism or
historical-priority claim. D11 independent acceptance remains pending.


### Supplementary review closure — 2026-11-06

Distinct Astra high reconstruction and independent directed scalar check
ACCEPTED this unchanged developer scope; no unresolved finding. See
[independent-checks-D11-onset.md](../independent-checks-D11-onset.md),
report SHA25650376e8ebf3dc6484763e8d3a68d7d416f25a62420edf3c2d5ba1605f9380217.
All28 independently reconstructed intervals lie inside the author bounds.
The preserved first hash-guard failure and single reviewed hash-only
recovery are documented there; author chronology remains in the attempt.
Final Claude audit remains pending. No finite enumeration was performed.
