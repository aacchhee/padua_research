# PD-T513 — Hahn terminal parity-row rate

ID kind: PD-T. Aliases: positive half-grid Hahn dual; balanced terminal
parity response; algebraic Hahn lower base; finite-type coefficient bound.
Split from: none; the row rate and full-map liminf lower are supporting
dependencies of PD-T448, not a resolved full sharp-Hahn target case.
Split into: none. This proves a row rate and a full-map lower, not a
matching rate for the full NN map.

## Statement

Use the exact Hahn input and PD-T432 mixed-input/four-field output metric
of `c2-hahn-normality.md`. For every N>=3 set M=N-1 and
nu=(ceil(M/2),floor(M/2)). Let D_M be the magnitude of the integer-node
terminal B2 derivative for the single relative second-weight direction
eta_k=(-1)^k, with first weights and nodes fixed. Define positive integers

    T_(M,k)=sum_(h=0)^k binom(k,h)binom(M+k+3-h,M-k),
    A_M=sum_(k=0)^M T_(M,k)
             *sum_(i=0)^(floor(M/2)-1)
                    binom(M-1,2i+1)binom(k+i,k).

Then, for every integer M>=2,

    A_M/54 <=D_M<=3(M+1)^2 A_M,
    kappa_N>= A_M/[27M(2M+3)].                             (1)

Moreover

    lim_(M->infinity) A_M^(1/M)
      =lim_(M->infinity) D_M^(1/M)=rho_H,
    liminf_(N->infinity) kappa_N^(1/N)>=rho_H,              (2)
    rho_H=(7+3sqrt(3)+sqrt((7+3sqrt(3))^2-4))/2
          =12.1136005841... .

Equivalently rho_H is the largest real root of
r^4-14r^3+24r^2-14r+1. The numerical decimal is only a rounded
evaluation of this exact algebraic number. With fixed masses the same
full-map lower in (1) divided by two holds, and the lower base in (2)
is unchanged. All M>=2, including both parities, are covered.

The limit in (2) is the rate of this terminal parity row, not a proved
rate for the complete Hahn condition number. A matching full-map upper
and the full sharp Hahn part of PD-T448 remain OPEN.

## Definitions and assumptions

Use M+1 integer nodes k=0,...,M, alpha1=1,alpha2=3/2,gamma=1 and
unnormalized weights W_s from `c2-hahn-normality.md`; their normalization
cancels from moment equations for independent relative-weight directions.
The monic terminal polynomial has degree M, and its successor is the
fixed support polynomial. All normalities and positive field scales
are proved in that dependency. Exact arithmetic; perturbations may
leave the named family, as the PD-T432 input model permits.

## Status by part

Overall status: PROVED (written analytic proof).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Every-M positive comparison and lower (1) | PROVED | Exact terminal values/dual and polynomial comparison below |
| Terminal-row limit and full-map liminf (2) | PROVED | Positive coefficient saddle bound with elementary finite-type lower |
| Fixed-mass lower-base corollary | PROVED | Remove a constant mass-null direction, cost at most two |

Candidate disposition: retained quantitative continuation of C2-03 and
IDEA-534/535. No historical novelty claim. The original full-map sharp
Hahn target remains OPEN, without an upper bound of this rate.

## Depends on

PD-T286/432, and `c2-hahn-normality.md` for all-N normality, the exact
transformed moment kernel, rational-polynomial representation and
||b2||<=2M+3. The coefficient asymptotic proof below is self contained;
no saddle-point theorem, central limit theorem, or unread Hahn formula
is imported. The weaker `c2-hahn-lower.md` remains a simpler independent
terminal lower, not a rejected argument.

## Proof

### 1. A perfect half-grid for either parity

For nu=(ceil(M/2),floor(M/2)), the sorted transformed row parameters are

    x_j=1+j/2, j=0,...,M-1.

The second-weight rows are precisely odd j=2i+1. This remains true at
odd M; no subsequence transfer is needed. Put y=-M-1 and let ell_j(y)
be the Lagrange coefficients for interpolation at the x_j. With L=2M+4,

    ell_j(y)=(-1)^j (L)_M/[(L+j)j!(M-1-j)!].              (3)

Thus all second-weight coefficients have the same negative sign.

### 2. Terminal polynomial values

The rational function F for the terminal monic P, from the normality
proof's (6),(7), is

    F(x)=C*prod_j(x-x_j)/(x+1)_(M+2),
    C=(M+1)!/prod_j(M+2+x_j).

Write F=sum_(j=0)^M d_j/((x+j+1)(x+j+2)), where
d_j=c_j(-1)^j/(M-j)! for P(k)=sum c_j(-k)_j. At x=-l-1 its residue
is d_l-d_(l-1), with d_(-1)=d_(M+1)=0. The product expression gives

    d_l-d_(l-1)=C(-1)^(M-l) V(l)/[l!(M+1-l)!],
    V(l)=prod_j(l+1+x_j)=2^(-M)(2l+4)_M.

Substitute the resulting partial sums into
P(k)=k! sum_(j=0)^k d_j(M-j)!/(k-j)!. The elementary identity

    sum_(j=l)^k (M-j)!/(k-j)!
         =(M-l+1)!/[(M-k+1)(k-l)!]

follows by summing binomial coefficients. It yields

    P(k)=C(-1)^(M+k) Delta^k V(0)/(M-k+1),                (4)

where Delta f(l)=f(l+1)-f(l). Since
(2l+4)_M=M![z^M](1-z)^(-2l-4),

    Delta^k V(0)=M!2^(-M) T_(M,k),
    T_(M,k)=[z^(M-k)](2-z)^k/(1-z)^(2k+4).               (5)

Writing 2-z=1+(1-z) in (5) proves the positive binomial sum in the
statement. Thus the signs in (4) alternate strictly at every grid node.

### 3. Terminal derivative dual

For dot P of degree <=M-1, its rational transform dot F has denominator
E(x)=(x+1)_(M+1), and its numerator has degree <=M-1. Interpolate this
numerator at the M row parameters. At x_j=alpha_s+i, the differentiated
constraint gives dot F(x_j)=-dot L_s((k+alpha_s+1)_i P)/R_s(x_j),
where R_s(x)=Gamma(x+M+3)/Gamma(alpha_s+1) is the row factor.
Also

    E(x_j)/R_s(x_j)
       =1/[(alpha_s+1)_i(M+alpha_s+i+2)].

The residue of dot F at y=-M-1 is minus dot tau, because only its
last partial-fraction column contributes there. Since E'(y)=(-1)^M M!,
the resulting second-weight derivative is

    dot tau=(-1)^M/M! *sum_k W2(k) eta_k P(k) Q2(k),
    Q2(k)=sum_(i=0)^(floor(M/2)-1) ell_(2i+1)(y)
               *(k+5/2)_i/[(5/2)_i(M+7/2+i)].            (6)

All terms of Q2(k) are negative for k>=0 by (3). Combining this with
(4), eta_k=(-1)^k makes every term of (6) have the same sign. The
terminal B derivative has the same magnitude as dot tau. Consequently
there is no cancellation in this one admissible parity response.

Insert (3)–(5) and W2(k)=(5/2)_k(M-k+1)/k! into (6). The factors
simplify to the exact positive sum

    D_M=K_M*sum_(k=0)^M sum_(i=0)^(floor(M/2)-1)
      T_(M,k) binom(M-1,2i+1)
       *(i+5/2)_k/k!
       /[(2M+5+2i)(M+7/2+i)],                            (7)
    K_M=M(M+1)*(2M+4)(2M+5)/[(3M+4)(3M+5)].

Mass normalization introduces no extra Z2: the normalized moment row
and its perturbation have the same common factor 1/Z2, which cancels.

### 4. Polynomial comparison and norm transfer

For M>=2 and 0<=i<floor(M/2), 0<=k<=M,

    binom(k+i,k)<=(i+5/2)_k/k!
                   <=4(M+1)^2 binom(k+i,k).

The upper bound follows by replacing 5/2 by 3 and telescoping
(i+3)_k/(i+1)_k; the lower follows termwise. Furthermore

    (4/9)M^2<=K_M<=(3/2)M^2,
    2M^2<=(2M+5+2i)(M+7/2+i)<=24M^2.

These bounds in (7) give A_M/54<=D_M<=3(M+1)^2 A_M.
The parity direction has input norm one, and integer B derivatives
scale to z derivatives by 2/M. Divide by ||b2||<=2M+3 to prove (1).

For fixed masses subtract c0=sum w2(k)(-1)^k from eta and divide by
1+|c0|<=2. A constant relative-weight direction is an exact null
direction of the NN map. The new direction has zero mass, norm at most
one, and loses at most a factor two. This proves the stated corollary.

### 5. Exact coefficient representation

Put

    X(z)=(1-z)^(-2)-1,
    Y(z)=(1-X(z))^(-1/2)
         =(1-z)/sqrt(1-4z+2z^2),
    H(z)=1+Y(z), f(z)=Y(z)/(2(1-z)^4).

Since T_(M,k)=[z^M](1-z)^(-4)X(z)^k and
sum_(k>=0)binom(k+i,k)X^k=(1-X)^(-i-1), the finite positive sum defining
A_M has the exact representation

    A_M=[z^M]f(z)[(1+Y(z))^(M-1)-(1-Y(z))^(M-1)].        (8)

Extending the k sum to infinity changes no z^M coefficient, as X
vanishes at zero. The odd-binomial sum in i gives (8) for both M
parities. Since Y=1+z+3z^2+O(z^3), the second term is explicitly

    [z^M]f(z)(1-Y(z))^(M-1)=(-1)^(M-1)(3M+2)/2.          (9)

All coefficients of H and f are nonnegative, and H has positive
constant, linear and quadratic coefficients. For example
Y'(z)=(1-4z+2z^2)^(-3/2) has strictly positive coefficients. Their
common positive radius of convergence is R=1-1/sqrt(2).

### 6. A self-contained coefficient-rate lemma

For this positive H let r in (0,R) be the unique solution

    r H'(r)/H(r)=1.                                      (10)

Existence/uniqueness can be checked without an asymptotic theorem:
normalize p_j=[z^j]H(z) r^j/H(r) to a probability distribution.
Its mean is rH'/H, and the derivative of that mean with respect to
log r is its strictly positive variance. The mean tends from zero
to infinity as r increases from zero to R: H' is of order
(R-r)^(-3/2), while H is of order(R-r)^(-1/2). All moments are finite
at each r<R. Thus (10) has exactly one solution.

Let b_M=[z^M]f(z)H(z)^(M-1). Positivity gives, at any a in (0,R),
b_M<=f(a)H(a)^(M-1)/a^M, so
limsup b_M^(1/M)<=H(r)/r, the minimum of H(a)/a.

For the matching lower, fix r from (10), so p has mean one, with
p0,p1,p2>0. For K>=2 define a finite distribution q by

    q_j=p_j (2<=j<=K),
    q1=1-sum_(j=2)^K j p_j,
    q0=sum_(j=2)^K (j-1)p_j.

Then q0,q1>0, q has mean one, and q approaches p as K increases.
Its relative entropy is
D(q||p)=q0 log(q0/p0)+q1 log(q1/p1), which tends to zero (the omitted
coordinates have q_j=0). For L=M-1 choose integer counts
n_j=floor(Lq_j) for j>=2, n1=L+1-sum_(j>=2)j n_j, and
n0=L-n1-sum_(j>=2)n_j. At all sufficiently large L they are
nonnegative, sum to L, have weighted sum L+1, and n_j/L->q_j.
The probability of this single multinomial type is a lower bound
for Pr(S_L=L+1), where S_L sums L independent p-distributed variables.

The elementary estimate log n!=n log n-n+O(log(n+1)) follows by
upper/lower integral bounds for sum log j. Applied to this fixed
finite type, it gives

    liminf_(L->infinity) (1/L)log Pr(S_L=L+1)>=-D(q||p).

Let K increase after taking the liminf. Since probabilities are at
most one, Pr(S_L=L+1)^(1/L)->1. Therefore

    [z^(L+1)]H(z)^L=H(r)^L r^(-L-1)Pr(S_L=L+1)

has (L+1)th-root limit H(r)/r. The positive constant coefficient
f(0)=1/2 transfers this lower bound to b_M. This proves
b_M^(1/M)->H(r)/r. Equations (8),(9), subtracting only an alternating
linear term, imply the same limit for A_M. Polynomial comparison in
(1) proves the D_M limit and full-map liminf.

### 7. Evaluate the saddle base

Here H'=Y'=(1-4r+2r^2)^(-3/2). Writing w=1-r in (10) gives
(2w^2-1)^(3/2)=1-2w^3. The unique interior solution satisfies

    2w^4+4w^3-2w-1=0,
    Y(r)=1+w=2-r,
    H(r)/r=(3-r)/r.

Substitution rho=(3-r)/r gives
rho^4-14rho^3+24rho^2-14rho+1=0. The corresponding positive
solution has rho>12; writing u=rho+rho^(-1) reduces its equation to
u^2-14u+22=0, hence u=7+3sqrt(3) and rho is exactly rho_H in (2).
The other root for u is below two and cannot yield rho>1 real.
The reciprocal real branch rho_H^(-1)<1 would give
r=3/(1+rho)>3/2>R, so it is excluded by the saddle domain.
Conversely this value gives r=3/(rho_H+1) in (0,R), satisfies (10),
and all quantities in the unsquared equation are positive. For explicit
bounds, 12<rho_H<61/5 gives10/13<w<17/22; hence
2w^2-1>31/169>0.18 and1-2w^3>822/10648>0.07. Uniqueness
in (10) therefore excludes extraneous roots from squaring.

## Checks

`../code/c2_hahn_terminal.py --max-m 10` independently solves the
defining Fraction moment equations and their parity derivative for
every M=2,...,10, compares it with (7), checks terminal alternating
signs and both polynomial bounds. Receipt: `../c2-hahn-terminal.json`.
Both M parities are explicitly included. These finite checks support
the formulas, not the all-N asymptotic argument. Independent review
and replay, and the required Claude audit, are separate records.

## Sources, scope and open items

No external theorem or novelty attribution. The exact moment kernel
dependency and prospective C2 round3 gate give provenance. This
identifies a *terminal parity-row* rate and proves that the full Hahn
condition has at least that lower base. It does not prove a full-map
upper, equality of the full-map liminf/limsup, a finite-error radius or
realized floating-rounding loss. The observed finite growth near11.8
is not a proof premise and is not claimed equal to rho_H at finite N.

## History

2026-11-06: Codex gpt-6.1-sol xhigh, rules/local source
`76ba4214b100c86a44941f5e9a662ce9ce48efb8`, topic pin
`b4a04981d42c7cd872957facf5e3995e4096ca67`. Written after the C2
round3 subroute gate and exact first check. No predecessor/shared
registry edits or Git mutations.

2026-11-06 response, Codex gpt-6.1-sol high, rules/source `3d5b29d`:
the former “Split from: PD-T448 (sharp full-map Hahn growth, OPEN)”
label is corrected to a supporting-dependency relation (MINOR-6).
The [parent classification proposal](../classification-proposal.md) separates
the proved benchmark Krawtchouk rate conjunct from the remaining OPEN
conjuncts. An exact Hahn row rate and a full-map lower do not settle a
full-map matching-rate conjunct. Statement, proof and PROVED status remain
unchanged.

## Final ID aliases (2026-11-06)

- `PD-T?nn-mop-cond-codex-C2-04` → `PD-T513`.

Additional historical aliases retained: `C2-03 round 3`, `historical C2-04 result ledger alias`.
