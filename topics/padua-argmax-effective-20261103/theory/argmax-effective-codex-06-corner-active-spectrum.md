# PD-T?argmax-effective-codex-06a — Exact spectrum of the inward corner-active polynomial

ID kind: PD-T.
Aliases: R6 diagonal-sign DCT; corner-active cosine coefficients; positive mixed spectrum.
Split from: R6 effective local comparison, which remains OPEN on a fixed scaled phase neighborhood.
Split into: quantitative slopes and a smaller explicit physical radius are in codex-06b.

## Statement

For every integer n>=2 put m=n+1, N=nm and c=(-1,-1). Use precisely
the even-checkerboard Padua cardinals L_jk of PD-T101. Define the nodal
signs on j+k even by

    sigma_00=(-1)^n,
    sigma_j0=-(-1)^n                    (j>0),
    sigma_jk=(-1)^(n+j)                 (k>0, j>=k),
    sigma_jk=-(-1)^(n+j)                (k>0, j<k).

Let P_n(x,y)=sum sigma_jk L_jk(x,y). Write

    P_n(-cos xi,-cos eta)=sum_(a+b<=n) C_ab cos(a xi) cos(b eta),
    h_0=1, h_a=2 (a>0).

Its coefficients are exactly:

    C_n0=1/N;

    C_ab=(h_a h_b/N)
         *[1+(-1)^(n+a+b) cos(a*pi/n)]
          /[cos(a*pi/n)+cos(b*pi/m)]             (1<=a<n, 0<=b<=n-a);

    C_0b=(h_b/N)*[(1+epsilon_b)/(1+cos(b*pi/m))-n*epsilon_b],
    epsilon_b=(-1)^(n+b)                        (0<=b<=n).

Every coefficient with a>0 is strictly positive. All row sums
R_a=sum_b C_ab are positive, satisfy R_0=1+1/N, R_n=1/N and
R_a=R_(n-a) for 1<=a<n. All column sums D_b=sum_a C_ab are positive.
Moreover

    C_(n-b),b >= 2/m               (1<=b<n),
    C_0n >= 8/15,
    Lambda_c=P_n(c)>=1+2/N+2(n-1)/m.                 (1)

No coefficientwise positivity is asserted for a=0; for example C_00=-1/6
at n=2. P_n is not asserted to majorize lambda globally.

## Definitions and assumptions

Exact real arithmetic. The cardinal weights are 2 e_j f_k/N, with half
endpoint factors. The exceptional coefficient (n,0) is 1, not 2. The
canonical zero-row signs are the signs of the inward first derivatives;
they do not assert sign stability on an n-independent neighborhood.

## Status by part

Overall status: **PROVED** (development proof; independent and Claude review pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Exact coefficient formulas, row symmetries, positivity and bounds (1) | PROVED | Finite cosine sums and elementary sine concavity below |

Candidate disposition: retained quantitative variant of IDEA-330/331.

## Depends on

PD-T101 corrected cardinal coefficient formula and cardinality.
PD-T227 exact corner signs, zero mask and zero-row gradients. No asymptotic
estimate, external one-dimensional theorem or computational acceptance.

## Proof

### 1. Reflection and the finite row sum

Reflect original node indices to j=n-p, r=m-q. The reflected board is
O={0<=j<=n,0<=r<=m,j+r odd}. Endpoint weights are preserved. In these
indices the sign data are (-1)^j t_jr, where t_jr=+1 for r>j and -1 for
r<j, except that t_jm=-1 for j<n and t_nm=+1. (There is no r=j on O.)
These exceptions are exactly the original zero row and the nonzero 00
corner cardinal. The coefficient formula of PD-T101 therefore gives

    C_ab=(2 c_ab/N) sum_j e_j cos((n-a)j*pi/n) H_j(b),               (2)
    H_j(b)=sum_(r+j odd) f_r t_jr cos(b r*pi/m),

where c_ab=h_a h_b except c_n0=1. This uses
(-1)^j cos(a j*pi/n)=cos((n-a)j*pi/n).

For 1<=b<=n set t=b*pi/m. The weighted cosine sum over either parity
subgrid is zero. Telescoping

    2 sin(t) cos(rt)=sin((r+1)t)-sin((r-1)t)

over r=j+1,j+3,...,m, retaining a half weight if the last point is m,
gives upper-tail sum -sin(jt)/(2 sin t). Thus

    H_j(b)=-sin(jt)/sin t-(-1)^b 1_{j=n mod 2, j<n}.                (3)

For b=0 the parity subgrid has total weight m/2, the upper-tail weight
is (m-j)/2, and instead

    H_j(0)=m/2-j-1_{j=n mod 2, j<n}.                               (4)

### 2. Evaluate the outer sums

Put A=n-a and s=A*pi/n. For integer 1<=A<=n-1,

    sum_(j=n mod 2) e_j cos(sj)=0,
    sum_j e_j sin(j omega)=(1-cos(n omega))*cot(omega/2)/2.         (5)

Both follow by summing the finite geometric progression; endpoint halves
are included. The right side in the second identity is interpreted by
continuity at its removable points. Product-to-sum in (5), followed by

    cot((t+s)/2)+cot((t-s)/2)=2 sin t/(cos s-cos t),

yields, with epsilon=(-1)^(A+b),

    sum_j e_j cos(sj) H_j(b)
      =-(1-epsilon*cos t)/(2*(cos s-cos t))+epsilon/2
      =(1-epsilon*cos s)/(2*(cos t-cos s)).                         (6)

Here the +epsilon/2 is the removed j=n endpoint in the indicator of
(3). No denominator in (6) vanishes in the stated total-degree range.
Since cos s=-cos(a*pi/n), substitution into (2) is the claimed formula.

For b=0 use

    sum_j e_j j cos(sj)=-(1-(-1)^A)/(4 sin^2(s/2)).                 (7)

One obtains (7) by differentiating a finite geometric sum, or by pairing
its real terms. Equations (4), (5) and (7) give the same expression (6)
with cos t=1.

For a=0, A=n. The parity sum in (5) is now (-1)^n n/2. Its additional
term in (3) or (4) subtracts (-1)^(n+b)n/2 from (6). Since h_0=1,
(2) gives the displayed C_0b formula. Finally a=n,b=0 has A=0;
sum_j e_j(m/2-j)=n/2 and the indicator in (4) has weight (n-1)/2.
The resulting sum is 1/2, giving C_n0=1/N with the corrected c_n0=1.

### 3. Positivity and the diagonal lower bound

For 1<=a<n and a+b<=n, a*pi/n+b*pi/m<pi, so
cos(a*pi/n)+cos(b*pi/m)>0. Its numerator is positive since
|cos(a*pi/n)|<1. Thus all these coefficients are positive.

For a=n-b, 1<=b<n, set u=b*pi/n and r=n/m. Then

    C_(n-b),b=(4/N)*(1-cos u)/(cos(ru)-cos u).

Concavity of sine on [0,pi] gives sin(ru/2)>=r sin(u/2), whence

    cos(ru)-cos u <= (1-r^2)(1-cos u),
    1-r^2=(2n+1)/m^2 <= 2/n.

This proves C_(n-b),b>=2/m. For 1<=b<n, C_0b is positive if
epsilon_b=-1 and is bounded below by -2/m otherwise. Its single positive
diagonal partner dominates that possible negative coefficient, strictly
because the discarded numerator term is positive. Hence D_b>0.
Also D_0 equals 1 if n is odd and 1-2/m if n is even, hence is positive.
This exact identity is established at the end of section 4.

At b=n, only a=0 occurs and epsilon_n=1. Since sin t<=t and pi^2<10,

    C_0n=(2/N)*(csc^2(pi/(2m))-n)
         >=4m/(5n)-2/m >= 8/15.

The last inequality is equivalent to 2(2n-3)(n-2)>=0. Thus D_n>0 too.

### 4. Edge interpolation gives the row symmetry and constant columns

At every Padua node on y=-1 the sign sigma is +1. In the inward x mesh
these are exactly xi=i*pi/n with i odd. Consequently the polynomial
sum_a R_a cos(a xi)-1 vanishes at these points. At an odd i,
cos((n-a)xi)=-cos(a xi). Pair the modes a and n-a. For n odd the
remaining cosine polynomial has degree at most (n-1)/2 and vanishes at
(n+1)/2 distinct cosines. For n even the middle mode vanishes at these
points, and the remaining polynomial has degree at most n/2-1 and n/2
distinct roots. It is identically zero in both cases. Hence

    R_0-R_n=1, R_a=R_(n-a) (1<=a<n).

The already proved C_n0=1/N gives the asserted R_0 and R_n. The other
R_a are positive sums. Adding the n-1 positive diagonal terms proves
the lower bound for Lambda_c in (1); equality P_n(c)=Lambda_c follows
from PD-T227 and the fact that zero cardinals contribute nothing there.

For completeness D_0 can be obtained by averaging P_n(-1,-cos eta)
over the parity-odd m-grid with endpoint half weights. All modes
1<=b<m have zero such average. At these nodes the sign data are +1,
apart from eta=pi when n is even, where the zero-row sign is -1.
The total grid weight is m/2 and that endpoint has weight 1/2. Thus
D_0=1 for n odd and 1-2/m for n even, as asserted. QED.

## Checks

Analytic proof. Exploratory float64 reconstruction against the full
coefficient matrix at n=2,3,4,5,8,16,32,64 agreed within 4.2e-14;
this is a diagnostic, not a premise. Reproducible diagnostic code and
the precise pending independent review are recorded in the R6 attempt.

## Sources and scope

Only the named repository identities are inherited. No external source
theorem or priority claim. The exact coefficients control one active
signed polynomial. They do not assert a global envelope or uniform
corner sign stability.

## Open items

Control aggregate sign changes and Taylor remainders on a fixed phase
zone rho<=1/64. Codex-06b uses a smaller explicit physical radius.

## History

2026-11-03, Codex gpt-6-astra ultra, handoff02 explicit allocation.
Rules/input 8a1f394739293953e1566fd24a0a193cc78ff26f, base 440d107.
New quantitative variant; no prior claim silently narrowed.
