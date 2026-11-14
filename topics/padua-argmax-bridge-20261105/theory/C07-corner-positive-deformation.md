# PD-T?argmax-bridge-codex-C07-corner-01 — A nonnegative finite corner deformation

ID kind: PD-T. Aliases: finite paired Cauchy deformation; one-sided
same-mesh square comparison. Split from: quantitative continuation of
PD-T159 and PD-T269. Split into: none.

## Statement and status

Use exactly the corner and same-mesh quantities Lambda_c(n), L_n of
PD-T159. For every integer n>=2,

    Lambda_c(n)>=n L_n^2/(n+1)+1/(n+1).                 (1)

In particular, for every integer n>=10^6 and ell=log n,

    Lambda_c(n)>=(2/5)(ell+3/2)^2-1/1000.               (2)

**PROVED**, written analytic developer result. Distinct reconstruction
and formal campaign audit are separate. This is only a corner value
bound; no global argmax premise or conclusion is used. No computation,
asymptotic fit, numerical integral or new Padua family is introduced.

Dependencies: PD-T159's exact positive corner sum and exact same-mesh
square; PD-T270's all-n one-dimensional error; N1-16's elementary
gamma+log(8/pi)>3/2 bound. The latter is recalled below. The full
PD-T159 and PD-T269–271 proofs were read for this continuation.
Gate and candidate: ../ideas/C07-corner.md.

## 1. Pair the finite deformation

Set m=n+1, tau=n/m, a_j=j*pi/n, b_j=tau*a_j and

    f(a,b)=(1+cos b)/|cos a-cos b|.

Write epsilon_j=1/2 at j=0,n and1 otherwise. On indices0,...,n,
the actual second-mesh weights eta_j equal epsilon_j except eta_n=1.
PD-T159 proves exactly

    Lambda_c=4/(nm) sum_(j+k odd,0<=j,k<=n)
                         epsilon_j eta_k f(a_j,b_k)+1/m,
    L_n^2=4/n^2 sum_(j+k odd,0<=j,k<=n)
                         epsilon_j epsilon_k f(a_j,a_k).       (3)

The +1/m is the actual finite polynomial value at the removed (n,m)
endpoint. The reference k=n row vanishes, and there is no diagonal
on the odd board. These facts are part of (3), not limiting conventions
for a rational pole.

Fix j<k with j+k odd, and put

    A=cos a_j, B=cos a_k, d=A-B>0,
    u=cos b_j-A>=0, v=cos b_k-B>=0.

The angular ordering b_k>a_j follows from
n(k-j)>j, since j<=n-1. Consequently 0<=v<d. Exact subtraction gives

    f(a_j,b_k)-f(a_j,a_k)=(1+A)v/[d(d-v)],
    f(a_k,b_j)-f(a_k,a_j)=-(1+B)u/[d(d+u)].           (4)

For 0<=x<pi define

    q(x)=(cos(tau*x)-cos x)/(1+cos x)
        =[cos(tau*x/2)/cos(x/2)]^2-1.

The logarithmic derivative of its positive squared ratio is
tan(x/2)-tau*tan(tau*x/2)>=0. Thus q is nondecreasing. If k<n,
q(a_k)>=q(a_j) says

    (1+A)v>=(1+B)u.

The first denominator d(d-v) in (4) is no larger than d(d+u),
so the sum of the two increments in (4) is nonnegative. If k=n,
then B=-1 and the second increment is zero; the first is nonnegative
directly. This also treats the endpoint case without dividing by1+B.

Pair every two orientations with the symmetric positive weight
epsilon_j epsilon_k. Their total signed deformation is nonnegative.
Finally eta_n-epsilon_n=1/2 adds only nonnegative actual summands at
k=n; it adds zero to the reference. Equation (3) therefore proves (1).
No positivity is asserted for each individual signed deformation.

## 2. A useful lower bound at every n>=10^6

Put kappa0=gamma+log(8/pi) and A_n=(2/pi)(ell+kappa0).
PD-T270 gives |L_n-A_n|<=1/(4n^2), and the elementary bound
A_n<=ell+2 is recorded in PD-T159/271. Also kappa0>3/2. For clarity,
N1-16 proves gamma>23/40 from
gamma>=H_10-log10-1/20, log10<2303/1000; the last logarithmic bound
follows from the positive exponential series through degree10. With
pi<22/7 and w=17/39,
log(8/pi)>log(28/11)>2(w+w^3/3)>37/40. These give the claimed sum.

Since A_n-1/(4n^2)>0 on this degree domain, (1) implies

    Lambda_c>=A_n^2-A_n^2/m-A_n/(2n^2)
       >=(2/5)(ell+3/2)^2
                    -(ell+2)^2/n-(ell+2)/(2n^2).              (5)

Here 4/pi^2>2/5, and positive terms were discarded. The two error
functions on the last line decrease for n>=10^6. At n=10^6,
ell<14 and their sum is less than

    256/10^6+8/10^12<1/1000.

This proves (2) uniformly over all integer degrees in its domain.
The standard elementary bounds log10<7/3 and pi^2<10 already
suffice for this last comparison.

## Scope, checks and history

PD-T269's positive limiting paired integrand is the closest predecessor;
the present proof establishes the finite signed pairing needed for (1).
This is recorded as a quantitative variant without a historical novelty
claim. No existing result is replaced or its remainder silently sharpened.
Every step is analytic and endpoint-aware. Distinct review is pending.

2026-11-06, rules/input 4b728b04216a5490910780bc609a82b853058426.
Codex, coordinator-requested Astra ultra; serving metadata unexposed.
