# PD-T?argmax-bridge-codex-N5-03 — All noncorner vertical-edge centers through phase radius 1/2

ID kind: PD-T. Aliases: N5-03; adaptive edge defect; tightened endpoint
middle lines; all-center actual-lambda/model margin.
Split from: none; quantitative variant of T222/T224/T366 and N5-02.
Split into: none. Whole-cell E-C and PD-T099 remain OPEN.

## Statement

For every integer n>=64, m=n+1, epsilon in {-1,1}, and interior
complementary index q satisfying

    1<=q<=m-1, epsilon^n*(-1)^q=-1,

put phi=(q*pi+s)/m, where |s|<=1/2. Then the **actual** edge Lebesgue
function satisfies

    lambda_n(epsilon,cos phi) < S_n(0,s)-1/1024.        (1)

Here S_n(0,s) is the corrected odd-board vertical primitive, identical
to PD-T185/189's two-copy vertical primitive. The physical point is
automatically in the square, since q is interior and |s|<=1/2<pi.

With N1's explicit cotangent row model M_n and N5's quadrature error,

    r_n=[7*pi^4/1800+7*pi^3*H_n/900]/n^4,
    |S_n(0,s)-M_n(0,s)|<=r_n,

one has the finite-n comparison

    lambda_n(epsilon,cos phi) < M_n(0,s)+r_n-1/1024
                              < M_n(0,s)-511/524288.   (2)

The estimate is uniform in both endpoints, both phase signs, degree and
every complementary center except the actual nonnode corners.

## Definitions and assumptions

Exact real arithmetic, even Padua checkerboard. Set N=nm,
a_j=j*pi/n, b_k=k*pi/m, j+k even and w_jk=2*e_j*f_k/N, with endpoint
factors 1/2 and interior factors 1. For epsilon=1 put J=0,u_j=a_j;
for epsilon=-1 put J=n,u_j=pi-a_j. Thus the reflected first-index grid
r with u=r*pi/n has r+k=J mod 2 in physical second row k.

Put A=cos^2(s/2), B=sin(s)/2 and tau_j=epsilon^n*(-1)^j. The signed
half kernels, retaining their finite polynomial collision values, are

    H_+=[tau_j*D_n(u_j,phi+b_k)-1]/2,
    H_-=[tau_j*D_n(u_j,phi-b_k)-1]/2.

As in PD-T185 and N5-02, define the nonnegative physical point defect
and total defect by

    d(j,k)=|H_+|+|H_-|-|H_++H_-|,
    Delta=sum_(j+k even) w_jk*d(j,k).

The exact corrected polynomial identity is

    lambda_n(epsilon,cos phi)=S_n(0,s)-Delta.           (3)

At regular denominators, both halves have the exact numerator formula

    H_+=[A*(1+cos v_+)+B*sin v_+]/[cos u_j-cos v_+],
    H_-=[A*(1+cos v_-)+B*sin v_-]/[cos u_j-cos v_-],
    v_+=phi+b_k, v_-=phi-b_k.                          (4)

The corrected exceptional highest mode stays in x. All selected terms
below are explicitly regular; no rational value is assigned at a pole.

## Status by part

Overall status: **PROVED**, complete analytic developer proof below.
Distinct mathematical review and required Claude audit are pending.

| Part | Status | Evidence / limitation |
|---|---|---|
| Uniform actual-lambda bounds (1)–(2) | PROVED | Finite numerator, band, parity and count estimates; N1/N5 error |

Candidate disposition: retained quantitative domain variant. This is an
extension of the existing finite-block method, not a new mechanism.

## Depends on

PD-T185/189/191/364 and N5-02 for exact identities (3)–(4). N1's
PD-T?argmax-bridge-codex-N1-01, based on
PD-T?argmax-bridge-codex-N5-01, for the model error in (2).
T222/T224/T366 supply the predecessor constructions, read in full;
their smaller-radius bounds are **not** extrapolated as black boxes.
All estimates for radius 1/2 are proved here. No external source theorem.

## Proof

### 1. Common facts and finite counts

Throughout |s|<=1/2,

    A>=1-s^2/4>=15/16, |B|<=|s|/2<=1/4.             (5)

Whenever a half's actual target cosine has 1+cos v>=1/2, its numerator
is at least (15/16)/2-1/4=7/32. Whenever 1+cos v>=2/5, it is at least
(15/16)*(2/5)-1/4=1/8. These estimates allow either sign of sin v.

A shifted grid of spacing h has at least ell/h-1 points in a closed
interval of length ell. This remains a valid bound in an open interval.
The physical second grid has spacing pi/m; in any fixed physical row
the allowed reflected first grid has spacing 2*pi/n. Every selected
first and second index below is interior, so its physical weight is
exactly 2/N. Every unselected point defect is nonnegative.

### 2. Endpoint-distance indices 1 through 4

Let a=min(q,m-q) in {1,2,3,4}. Use every integer l with

    3*n/8 <= l <= n/2.                               (6)

There are at least n/8-1>=n/16 such l. Define w=l*pi/n.
For a bottom center q=a, put

    t=(a*pi+s)/m, phi=t,
    eta=0 if a is odd, eta=1 if a is even,
    k=l+eta, b=k*pi/m, reflected first index r=l, u=w.

For a top center q=m-a, put

    t=(a*pi-s)/m, phi=pi-t,
    eta=1 if a is odd, eta=0 if a is even,
    k=l+eta, b=k*pi/m, reflected first index r=n-l, u=pi-w.

The displacement is exactly m*(w-b)=l*pi/n-eta*pi in both cases.
Its magnitude is at most 5*pi/8, whereas

    m*t >= pi-1/2 > 5*pi/8.

The final strict inequality follows from 3*pi/8>1/2. Hence w lies
strictly between b-t and b+t. All selected k and r are physical interior
indices for n>=64, and distinct l give distinct physical second rows.

For the bottom, the two target cosines are cos(b-t),cos(b+t), with
cos u=cos w strictly between them. For the top they are
-cos(b-t),-cos(b+t), with cos u=-cos w strictly between them. Thus the
two denominators in (4) are nonzero and opposite in sign.

The folded target angles satisfy

    3*pi/10 <= b-t < b+t <= 3*pi/5.                  (7)

Indeed their lower bound is
[((3*n/8-4)*pi)-1/2]/(n+1), and their upper bound is
[((n/2+5)*pi)+1/2]/(n+1). After clearing denominators, (7) follows from
(3*n/40-43/10)*pi>=1/2 and (n/10-22/5)*pi>=1/2. Both left sides
increase with n and are already >=pi/2 and 2*pi at n=64.

On [3*pi/10,3*pi/5], both 1-cos v and 1+cos v exceed 2/5.
For the first, cos(3*pi/10)=sin(pi/5)<3/5: its square is
(5-sqrt(5))/8<7/20<9/25 using sqrt(5)>11/5. For the second,
3*pi/5<2*pi/3 gives cos v>-1/2. Thus (5) bounds **both actual
numerators** below by 1/8, including the top case's 1-minus-cos baseline.

The denominator magnitudes are bounded by the full cosine span,
which is at most 2*t<27/m, since 2*m*t<=8*pi+1<27. Therefore both
half magnitudes exceed m/216 and

    d(j,k)=2*min(|H_+|,|H_-|)>m/108.                (8)

It remains to check the physical checkerboard parity. At the bottom,
r+k=2*l+eta=eta mod 2, and J+q odd gives J=1-a mod 2=eta.
At the top, r+k=n+eta, while J+(m-a) odd gives J=n+a mod 2;
eta=a mod 2. Thus every selected point is in the required physical
checkerboard after reflecting the first coordinate for epsilon=-1.

Using at least n/16 interior rows, each with weight 2/N, proves

    Delta > [2/(nm)]*(n/16)*(m/108)=1/864>1/1024.    (9)

### 3. Remaining centers have sufficient physical endpoint distance

If min(q,m-q)>=5, set gamma=min(phi,pi-phi). Then

    gamma >= (5*pi-1/2)/m > 4*pi/n, gamma<=pi/2.     (10)

The strict inequality is equivalent to n*(pi-1/2)>4*pi, valid already
at n=64 and increasing thereafter. This supplies the exact scale needed
by the following adaptive selections.

If phi=gamma, select physical b=b'. If phi=pi-gamma, select b=pi-b'.
In the second case cos(phi+b)=cos(gamma+b') and
cos(phi-b)=cos(gamma-b'). Thus in either orientation the denominator
targets are exactly cos(gamma+b'),cos(gamma-b'). Reflection preserves
the second-grid spacing, counts and interior factors. Sine signs in the
actual numerators are handled absolutely by (5).

### 4. Adaptive far-center small-angle block

For 4*pi/n<=gamma<=pi/6 choose

    pi/3<=b'<=pi/2, b'-gamma/2<=u<=b'+gamma/2.        (11)

The folded target angles b'-gamma,b'+gamma lie in [pi/6,2*pi/3].
Their 1-plus-cos baselines are at least 1/2, so both numerators are
at least 7/32. The selected first interval is strictly inside the
target interval. Its denominators are nonzero, opposite in sign, and
bounded in magnitude by the cosine span 2*sin(b')*sin(gamma)<=2*gamma.
Consequently d(j,k)>=7/(32*gamma).

There are at least m/6-1>=m/12 physical second rows. In each row,
the first-grid count is at least n*gamma/(2*pi)-1>=n*gamma/(4*pi),
using gamma>=4*pi/n. All intervals lie strictly inside the physical
first range, so either required parity has that count. Direct physical
normalization gives

    Delta >= [2/(nm)]*(m/12)*(n*gamma/(4*pi))*[7/(32*gamma)]
          = 7/(768*pi)>1/1024.                      (12)

For example pi<4 makes this last bound greater than 7/3072.

### 5. Adaptive far-center middle-angle block

For pi/6<=gamma<=pi/2 choose

    pi/12<=b'<=pi/6, gamma-b'/2<=u<=gamma+b'/2.        (13)

The target angles gamma-b',gamma+b' lie in [0,2*pi/3], giving both
numerators at least 7/32. The selected first angles lie strictly between
the targets, with positive separation b'/2. The cosine span is at most
2*sin(gamma)*sin(b')<=1, so d(j,k)>=7/16.

The physical second-row count is at least m/12-1>=m/16 because m>=65>48.
The selected first interval has length b'>=pi/12 and hence has at least
n/24-1>=n/48 points of either required parity, since n>=64>48.
Every selected index is interior. Therefore

    Delta >= [2/(nm)]*(m/16)*(n/48)*(7/16)
          = 7/6144>1/1024.                          (14)

At gamma=pi/6 either far selection is valid. Cases (9), (12), (14)
exhaust every interior complementary center and prove (1) using (3).

### 6. Explicit cotangent-model margin

N1's model theorem applies at (alpha,beta)=(0,s). Its upper inequality
in (1) gives the first bound in (2). As in N5-02, pi^4<100, pi^3<32
and H_n<=n yield

    r_n<7/(18*n^4)+56/(225*n^3).

The right side decreases with n. At n=64 its product with 524288 is
7/576+112/225=66087/129600<1. Thus r_n<1/524288. Since
1/1024=512/524288, the remaining strict margin is 511/524288, proving (2).

## Checks and sources

The gate/candidate and this proof preceded any round-3 numerical run.
The developer then actually executed `../code/n5_all_edge_defect.py`:
exact rational constants/endpoint-budget checks, followed by 56 selected-block
cases at n=64/65, both physical endpoints and phases s=-1/2,+1/2.
There were 32 endpoint-line, 16 far-small and 8 far-middle cases. All
selected numerators, parity/count conditions and case-floor checks passed.
The smallest selected-defect/case-floor ratio was 11.8382054813763;
the maximum finite-polynomial/quotient discrepancy was 2.003860985e-77
at 80 decimal digits. These are supplementary **MEASURED developer
diagnostics**, not independent agent checks or proof premises. They
evaluate only the selected subsets, without a phase maximization or
degree-ordering scan. The exact command and source/bulk hashes are in
`../attempts/N5.md` and `../evidence/n5-all-edge-defect.json`.
Distinct review is pending. No classical fulltext was read or transferred;
the source-access limits in `../literature-N5.md` remain unchanged.

## Scope and open items

This finite theorem removes N5-02's physical central-strip restriction
and covers a larger phase window than T366 on exact vertical edges.
It does not extend T366 to two varying physical coordinates, include
nonnode corner centers, or bound the primitive model's own maximum.
At an actual nonnode corner center the zero-phase defect is zero, so
the excluded corners cannot be added to (1). Phases outside [-1/2,1/2],
independently optimized whole-cell E-C and PD-T099 remain OPEN.

## History

2026-11-05, Codex, parent-requested gpt-6.1-sol xhigh; runtime metadata
not independently exposed. Input/rules
`c000899f3fb10d6ba0f1725341a045fe11ec943a`. Parent supplied the prospective
tighter endpoint band, with constants explicitly unproved. Candidate and
kill gate were recorded before development and numerical diagnostics.
The gate sought d>=1/8192; the analytic geometry yields the stronger
d=1/1024. Round-1/2 theory/code/receipts remain frozen. No Git/shared
registry operation, external proof transfer, self-audit or round 4.
