# D01 P4 finite-sum contract, frozen before execution

Rules/input: `4cf68980fa0538b53e2aea7174ed6e5782a34908`.
2026-11-06; Codex mathematics worker, parent-assigned Sol xhigh;
serving metadata unexposed. This implements Claude P4/I04 without a new
mechanism or historical novelty claim. Gate coverage is recorded in
`../../ideas/D01-corner.md`; no personal complete-registry read is claimed.

## Exact objects and normalization

For integer n>=1000 put m=n+1, tau=m/n, L=log m, N=nm. Use C07's
physical odd board and enlarged collision family exactly:

    O={(j,r):0<=j<=n,0<=r<=m,j+r odd},
    B={(j,r) in O:r=j+1,2j>=n}, R=O\B,
    S=j+r, d=2n+1-S, g=|j-r+j/n|, a0=1/6.

The sums below are **unweighted**, as in C07; endpoint weights were
omitted upward when bounding regular contributions. They are not sums
of cardinal Hessians and they are not evaluated at sampled phases.

    A1=sum_R (S-a0)^(-1)(g-a0)^(-3),
    A2=sum_R (S-a0)^(-3)(g-a0)^(-1),
    A3=sum_R (S-a0)^(-2)(g-a0)^(-2),
    G2=sum_R (g-a0)^(-2),
    B20=sum_R (S-a0)^(-2), C20=sum_R (d-a0)^(-2).

Define the fully accounted **C07 envelope**, the object called
K0_actual in this diagnostic, by the following fixed allocation:

    H=1+log(2m),
    C_f=16 tau^3 A1/pi^4 +4 tau^3(A2+A3)/pi^2,
    C_rem=30m^2/(pi^2 n^3)+18mH/(25n^3)
             +3456mH/(25pi^2 n^3)+8/(nm),
    C_sine=50m G2/(9pi^2 n^2)+m(B20+C20)/(2n^2),
    W_B=floor(n/2)+1/4,
    C_strip=(28/5)W_B/m,
    K0_C07=C_f+C_rem+C_sine+C_strip-L/3.

The notation K0_C07 prevents confusion with the least possible constant
for the actual function. Every charge in this envelope is included.
C_rem retains C07(13)'s analytic harmless-term bound; C_sine retains its
csc envelope; C_strip retains C07(24)'s Hessian bound with the actual
endpoint-weight count. No measurement of derivatives is substituted.

C07(3)'s reflected normalization is lambda=(1/N) sum_O e_j f_r
|sum_four F_jr|, Lambda_c=(4/N) sum_O e_j f_r|F_jr(0,0)|.
For the regular f second differences it gives 2/(N n^2) times the
sum of C07(7)'s majorant. Its first three terms give exactly C_f.
The last four are bounded by C_rem, without rounding them to 1/100.
C07(15) gives [1/(2n^2m)] sum_R(csc^2 T+csc^2 P).
Using csc^2 T<=(25/9)T^(-2), and
csc^2 P<=pi^2(P^(-2)+Z^(-2))/4, with its lower bounds (5),
gives exactly C_sine above. C07(24) costs (14/5)n rho^2 per B index;
rho^2<=2r2 and division by N give C_strip. At (n,m) the weight is
1/4, and the other floor(n/2) B indices have weight one.

These facts identify the analytic candidate inequality

    lambda_n<=a Lambda_c+[L/3+K0_C07(n)]r2,

on alpha,beta>=0,alpha+beta<=1/2, with a=(cos alpha+cos beta)/2.
The frozen C07/C13 theorems are not invoked below their degree floors.
A separate written floor check is required before claiming this
inequality at n>=1000. Numerical evaluation cannot establish it.

## Finite grouping and positive-tail enclosure

Write l=j-r. It is always odd. The exact diagonal ranges are:

* l=k>0: j=k,...,n, r=j-k;
* l=-k, k>=3: j=0,...,min(n,m-k), r=j+k;
* l=-1: j=0,...,ceil(n/2)-1, r=j+1.

Preregister D=127 and enumerate only |l|<=D. All omitted terms are
positive. For q=D+2-7/6 and p>1 set

    H_p(q)=q^(-p)+q^(1-p)/[2(p-1)].

Since omitted k run in steps of two, g-a0>=k-7/6 and
S-a0>=2t+k-1/6 for a diagonal parameter t>=0. The decreasing
integral comparison gives the following tails after summing both signs:

    0<=tail(A1)<=2H_4(q)+log(1+2n/q)H_3(q),
    0<=tail(A2)<=2H_4(q)+H_3(q)/2,
    0<=tail(A3)<=2H_4(q)+H_3(q),
    0<=tail(G2)<=2(n+1)H_2(q).

For A1 use sum_(t=0)^n(2t+b)^(-1)
<=1/b+log(1+2n/b)/2. For A2/A3 use respectively
sum_(t>=0)(2t+b)^(-3)<=b^(-3)+1/(4b^2) and
sum_(t>=0)(2t+b)^(-2)<=b^(-2)+1/(2b).
The code may intersect these bounds with the independently valid bound
on each omitted finite diagonal given by its exact length times the
product of the separate denominator minima. Taking the minimum is an
intersection of two positive upper bounds, not a fitted correction.

B20 and C20 use full O(n) grouping by odd S. Set
jlo=max(0,S-m), jhi=min(n,S), and start with count=jhi-jlo+1.
Subtract one exactly when j=(S-1)/2 is in that range and 2j>=n.
Multiply this count by the respective inverse square. A zero count at
S=2n+1 contributes zero, not a regular endpoint term.

In exact real arithmetic these are rigorous truncation bounds. The
long-double program and Python arithmetic are not outward rounded;
therefore the computed intervals are **MEASURED truncation envelopes**,
with explicit analytic positive-tail bounds and no certified numerical
rounding bound. They are not interval proofs.

## Prospective tests, fixed before launch

Compute n=1000,10000,20000,100000 and odd companions n+1. The n=20000
case is included before any kill decision. Report every sum, each charge,
the K0_C07 lower/upper truncation endpoints and L. Both parity-correct
corner reflections retain this same board convention; no x/y mesh swap.

* Primary success: upper K0_C07<=4 at n=1000.
* Kill: lower K0_C07>=0.1L^2-L/3 at n=20000.
* Weaker prospective alternative: upper K0_C07<=7.8 at n=10000.
  Passing it does not relabel a failed primary test as success.

If a truncation interval crosses a threshold, report inconclusive; no
post-hoc D increase or replacement envelope is preregistered. A failed
envelope gate is not a refutation of an optimal actual-function bound.
Cap: 300 aggregate process CPU seconds, including build and controls.
No old-degree certificate or full lambda/phase scan is allowed.

Controls: full independent board enumeration at n=17,1000,1001;
exact Fraction board sums at n=17; truncated/full comparisons where
available. Small-n controls verify indexing only, not the n>=1000
analytic floor. No retuning or rescue run is included.
