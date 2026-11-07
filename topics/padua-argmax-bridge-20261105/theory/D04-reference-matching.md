# PD-T?argmax-bridge-codex-D04-reference — Symmetric reference matched to the endpoint constant

ID kind: PD-T. Aliases: floor-free reference sum; displaced digamma
matching; weighted endpoint cutoff cancellation. Split from: D04 practical
joint remainder, OPEN. Split into: none.

## Statement and definitions

Let alpha,beta>=0, alpha+beta<=pi, integer R>=2, integer n>=8R,
m=n+1, H_n=sum_{k=1}^n 1/k, and

    a=(cos alpha+cos beta)/2, P=sin alpha+sin beta,
    x=alpha/pi, t=beta/pi, v_r=(r*pi+beta)/m.

Use the corrected G_n=D_n-cos(nu), the odd board, and N1-02's exact
special-row set A_R: rows 0,...,R-1 and 2m-R,...,2m-1, rows m-1,m,
and every row containing an actual polynomial collision. It has at most
2R+4 members. Let O be its complement among r=0,...,2m-1. For r in O set

    w_r=a cot(v_r/2)/2,
    x_rk=(u_rk-v_r)/2,
    u_rk=((1-r mod 2)*pi+alpha+2k*pi)/n,
    g0_r(X)=|-w_r cot X+w_r cot(X+v_r)|
                  -|w_r cot X|-|w_r cot(X+v_r)|,
    T0_r=sum_{k=0}^{n-1}g0_r(x_rk)
                    -(n/pi)*integral_0^pi g0_r(X)dX.

Ordinary samples avoid both poles and v_r is not a multiple of pi.
The value zero may be assigned at the poles for the integral.
For s in [-1,1] with x+|s|<=1 and j>=2 define

    nu=j+s, q_+=(1+s+x)/2, q_-=(1+s-x)/2,
    B_j(s)=psi(j+q_+)+psi(j+q_-)-2log(j+s),
    Xi_j(s)=(2a/pi^2)*B_j(s)/(j+s),
    Delta_R=sum_{j=R}^infinity[Xi_j(t)+Xi_(j+1)(-t)].  (1)

This series converges absolutely and has the exact value

    Delta_R=E_infty-E_R,                              (2)

where E_R and E_infty are precisely C08-far-endpoint-constant.md's
unchanged quantities. In particular E_R=C_R+D0[h_R(t)+h_R(1-t)]
+B0[g_R(t)+g_R(1-t)], B0=4a/pi^2, and
E_infty=a/3+a C(t_d)C(t_e)/pi^2 with its weighted continuous boundary
values; t_d=(1+x-t)/2, t_e=(1+x+t)/2 and
C(y)=-psi(y)-psi(1-y). Here D0=U0/pi+B0 log pi as in N1-05/06.
The convergent h_R,g_R series and the finite sinc C_R are unchanged
N1-06/07 definitions, not new truncations.

The reference sum obeys the explicit full-phase estimate

    |(nm)^-1 sum_{r in O}T0_r-Delta_R|
      <= { [52a/pi^2+16P/(3pi)]H_n+7a+2P/pi }/n.    (3)

Thus its nondecaying endpoint contribution is exactly Delta_R; it must
be retained before the reference error is bounded. No 1/R or 1/R^2
floor remains in (3). Equation (3) is not a full S_n-M_infty rate.

Status: **PROVED**, analytic developer result, distinct review pending.
Dependencies: D04-half-line-defect.md; accepted D03 only for the later
row-reduction corollary, not for (3); N1-02's exact mesh/collision count;
N1-05/07 definitions; C08's exact endpoint increment and limit. The
extension of the C08 increment identity to R>=2 is justified below.
No computation, fit or external source theorem is a premise.

## 1. Exact displaced endpoint expression

For a left endpoint row use j=r, b=beta, s=t, z=v_r.
For a right endpoint row use j=2m-r, b=-beta, s=-t, z=2pi-v_r.
Only z<pi/2 belongs to this endpoint part. The ordinary endpoint ranges
are respectively j>=R and j>=R+1, apart from the collision exclusions.
In either case nu=j+s, z=pi*nu/m and nu>=2. Evenness of G_n in v
interchanges the two original cotangent channels on the right, giving
the standard folded reference with coefficients (-w,w),

    w=a cot(z/2)/2>=0,
    d=n*z/pi=(n/m)*nu, delta=nu/(2m)<1/4,
    theta_+=(1-s+x)/2+delta,
    theta_-=(1-s-x)/2+delta,
    k_+=floor(theta_+), k_-=floor(theta_-),
    y_+=j+q_+-delta, y_-=j+q_--delta.

The two positive distances from the poles have offsets
frac(theta_+) and frac(theta_-). They lie strictly between zero and one
on ordinary rows. Since 0<theta_+,theta_-<5/4, each k is zero or one.
The arguments d+frac(theta_+/-) equal y_+/- - k_+/-, exactly.
The half-line theorem therefore gives

    Theta_(j,s)= (a*n/pi)*cot(z/2)
         *[psi(y_+-k_+)+psi(y_--k_-)-2log d],
    |T0_r-Theta_(j,s)|<=16w/pi.                       (4)

The displayed digamma formula also defines a finite bookkeeping value
Theta when theta=1; (4) is asserted only on ordinary rows. At a collision
this assigned Theta is not a replacement for the actual polynomial row.

For the right endpoint this formula uses the reflected row of the same
polynomial, with signed b=-beta; it does not exchange n and m or alpha
and beta. In particular the displacement is delta=nu/(2m), not zero.

## 2. Scalar bounds and the exact C08 constant

The defining series implies psi'(u)=sum_{k>=0}(u+k)^-2>0.
The elementary trapezoid estimate proved in C08 gives

    log u-1/(2u)-1/(8u^2)<=psi(u)<=log u-1/(2u).

Since q_+/- - s=(1-s+/-x)/2 belongs to [0,1], each j+q lies in
[nu,nu+1]. For nu>=1 monotonicity and the preceding estimate imply

    |psi(j+q)-log nu|<=1/nu,
    |B_j(s)|<=2/nu,
    |Xi_j(s)|<=4a/(pi^2*nu^2).                       (5)

This proves absolute convergence in (1), including every boundary
phase. C08's exact increment algebra gives

    E_(j+1)-E_j=Xi_j(t)+Xi_(j+1)(-t).                 (6)

Although its numerical tail bound was stated for j>=64, the algebra
uses only the exact h,g recurrences and the finite row identity

    ell_j(alpha,b)=[D0+(2a/pi^2)
                (psi(j+q_+)+psi(j+q_-))]/(j+s).

These expressions have positive large digamma arguments and nonzero
j+s for j>=2, so (6) holds already there. Sum (6) from R to a larger
cutoff, then use C08's accepted limit E_infty. This proves (2) without
extending its old R>=64 tail inequality to smaller R.

## 3. Compare the finite endpoint defect with Xi

Because j>=2 and delta<1/4,

    psi'(u)<=1/u+1/u^2<=2/j, u>=j-1/4.

Each unwrapped digamma displacement therefore costs at most
2delta/j=nu/(mj). Also |log(n/m)|=log(1+1/n)<=1/n and nu<=j+1.
Consequently

    |psi(y_+)+psi(y_-)-2log d-B_j(s)|<=5/n.          (7)

The normalized prefactor in (4) is

    A_j=a cot(z/2)/(pi*m)
       =[2a/(pi^2*nu)]*tau(z/2), tau(u)=u cot u.

On 0<=u<=pi/4, 0<=1-tau(u)<=u^2. Indeed
sin u-u cos u<=u^3/3 and sin u>=2u/pi imply
1-tau(u)<=pi*u^2/6<u^2. Thus (5) bounds the error of replacing A_j
by 2a/(pi^2*nu), when multiplying B_j(s), by a/m^2. Equation (7)
costs at most 10a/(pi^2*n*nu).

A wrap k=1 contributes exactly -1/(y-1), by the psi recurrence.
It can occur only when theta>=1, equivalently one of +/-alpha-b is
at least pi-z. Hence alpha+beta>=pi-z. Put e=alpha+beta. The identity

    a=(P/2)cot(e/2)

holds for e>0, with continuous values where a and P vanish. Since
z<pi/2 and e>=pi-z, it implies

    a<=(P/2)tan(z/2)<=P*z/2.                         (8)

The last inequality follows from sec^2 u<=2 on [0,pi/4]. Also

    y-1>=j-5/4>=(3/4)(j-1), A_j<=P/(pi*m).

Both possible wraps therefore cost at most
8P/[3pi*m*(j-1)] in that row. Combining these estimates gives

    |Theta_(j,s)/(nm)-Xi_j(s)|
      <=10a/(pi^2*n*nu)+a/m^2
                         +8P/[3pi*m*(j-1)].          (9)

The last term may be omitted on a row with no wrap. The uniform form
(9) uses it everywhere. It is not a Taylor argument through a moving
root or pole; the integer change has been accounted for exactly.

## 4. Sum endpoints, omissions and the central part

On the ordinary endpoint sets, sums of 1/nu and 1/(j-1) are each at
most 2H_n. There are fewer than 2m endpoint rows. Thus (9) sums to

    [20a/pi^2+16P/(3pi)]H_n/n+2a/n.                 (10)

The infinite tails absent from the endpoint region start at nu>=m/2.
By (5), their combined absolute sum is at most

    16a/(pi^2*m)+32a/(pi^2*m^2)<2a/n,               (11)

using m>=17 and pi^2>9. An exact collision omitted from the endpoint
set satisfies theta=1, so (8) applies. Its Xi magnitude is at most
2P/(pi*m*nu)<=P/(pi*m). There are at most two collision rows, so
these omitted Xi terms cost at most 2P/(pi*n). Equations (10)-(11)
therefore compare the endpoint Theta sum with Delta_R at cost

    [20a/pi^2+16P/(3pi)]H_n/n+4a/n+2P/(pi*n).       (12)

The error in (4) sums as follows. Since w<=a/z=a*m/(pi*nu), its
normalized sum over the two endpoint sets is at most
32a H_n/(pi^2*n).

For the remaining ordinary rows pi/2<=v_r<=3pi/2, N1-02's half-variation
bound applied to g0 gives

    |T0_r|<=4|w_r|/|sin v_r|=a/sin^2(v_r/2)<=2a.

The central polynomial rows with v_r=pi, or its closest designated rows,
are special and absent. There are at most m+1 rows in this closed
central interval, so the normalized total is below 3a/n. Add this and
the preceding endpoint error to (12). The result is exactly (3).

## 5. Why this is the endpoint match

For each fixed signed endpoint index j>=2, (9) implies uniformly over
its closed phase triangle that Theta_(j,s)/(nm) tends to Xi_j(s).
N1-05's uniform endpoint remainder and its exact leading coefficient
likewise give

    H(log n,pi*(j+s)/m)/m
          ->[D0+(4a/pi^2)log(j+s)]/(j+s).

On the right use H(log n,2pi-pi*(j+s)/m), with s=-beta/pi.
For example the bounded difference A(v)-4a/(pi*z), multiplied by
(log n)/m, tends uniformly to zero; the B residual is O(1+log m)/m.
The residual log(n/m) term tends to zero as well. Adding Xi cancels
its two logarithms exactly, leaving the finite row ell_j in section 2.
Thus the bounded reference defect supplies the actual endpoint profile;
the separate pole norms were never replaced by an unweighted kernel.
The exceptional j=0 and j=1 signed charts are not asserted here: they
are among the retained exact endpoint rows for R>=2.

## Limits, checks and history

Every phase bound includes a=0, both axes, coefficient sign changes,
integer wraps and the polynomial collision exclusions. Other quadrants
use separate phase evenness. There is no n/m mesh exchange, assumption
of a smooth absolute-value Taylor expansion, or omitted corrected mode.
No numerical execution was used. The formulas and constants are written
for independent adversarial review, which remains pending.
2026-11-06, input 2db4a226dad798491be3ec2fe5ce0238e21cfaec, parent-requested Astra ultra; runtime serving
metadata unexposed. Main practical M_infty remainder remains OPEN.
