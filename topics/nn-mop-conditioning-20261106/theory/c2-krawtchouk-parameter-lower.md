# PD-T?nn-mop-cond-codex-C2-01 — parameter-dependent Krawtchouk lower base

ID kind: PD-T.
Aliases: two-parameter terminal parity bound; binomial Hermite response sum;
explicit rho lower; digits capacity versus measure separation.
Split from: none; this lower bound is a supporting dependency of PD-T448,
not a resolved full general-parameter matching-rate target case.
Split into: none. This is a lower bound, not the matching-rate target.

## Statement

For every integer N>=2 set M=N-1. On z_k=2k/M-1, k=0,...,M, let

    w_(s,k)=binom(M,k) p_s^k (1-p_s)^(M-k),
    0<p1,p2<1, p1!=p2.

Let kappa_N be the PD-T432 induced derivative norm of the full monic NN
triangle through degree M: input |dot z_k|<=1 and
|dot w_(s,k)|<=w_(s,k), independently; output is the maximum of the four
fieldwise sup errors divided by the corresponding unperturbed field sup.
Define

    s=max(|1-2p1|,|1-2p2|)>0,
    q_*=min(p1(1-p1),p2(1-p2))=(1-s^2)/4,
    A=(p1+p2-2p1p2)/|p2-p1|>1,
    rho=A+sqrt(A^2-1)
       =(p1+p2-2p1p2+2sqrt(p1p2(1-p1)(1-p2)))/|p2-p1|.

Then every required mixed index through degree N is normal and

    kappa_N >= 2q_*/(s M^2) * (rho^(M-1)+rho^(-(M-1))).       (1)

Consequently liminf_(N->infinity) kappa_N^(1/N)>=rho for each fixed
distinct pair. With the same coordinate bounds and with both masses
fixed, the induced condition satisfies at least one half of (1).
If one marginal has parameter 1/2, its parity direction directly gives
the stronger prefactor 1/(2sM^2), without the fixed-mass factor loss.
At p1=2/5,p2=1/2 that stronger bound is PD-T437(13):

    kappa_N >= 5/(2M^2)*((5+2sqrt(6))^(M-1)
                         +(5-2sqrt(6))^(M-1)).

The conservative constant in (1) itself is 12/(5M^2) for this pair;
the asserted exponential base is the same.

No upper bound or equality of the true exponential rate is asserted.

## Definitions and assumptions

The NN convention and terminal support polynomial are PD-T286/289.
Weights are perturbed independently of their binomial parameterization;
directions may leave the two-parameter binomial family. Exact real
arithmetic and fixed distinct parameters are used throughout. All four
field scales are positive; the b1 and b2 field scales both equal s.

## Status by part

Overall status: PROVED (written analytic proof; supplementary exact finite
checks are separate verification, not premises).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| All-N lower bound (1), fixed distinct pair | PROVED | Terminal jet and positive summed-response proof below |
| Fixed-mass factor-one-half corollary | PROVED | Explicit removal of the mass-null direction below |

Candidate disposition: retained quantitative parameter variant of
IDEA-533/535. No historical novelty claim. PD-T448 and the matching
two-parameter rate remain OPEN; no PARTIAL label follows from this lemma.

## Depends on

PD-T286/289 (moment-defined map, terminal successor), PD-T432 (induced
norm), PD-T437 (elementary binomial polynomial and NN coefficient proofs).
The predecessor's normality proof applies unchanged to every distinct
pair in (0,1), because the weight ratio is a nonconstant positive
exponential. Its coefficient proof gives, in the integer coordinate k,

    B_(n,m,j)=p_j(M-n-m)+(1-p1)n+(1-p2)m.                    (2)

For completeness, that dependency proves the scalar axis recurrence by
the generating polynomials
(1+(1-p)t)^k(1-pt)^(M-k), then verifies (2) in the exact layer equations;
it does not import a source formula. No external theorem is invoked here.

## Proof

### Symmetries and field normalization

Exchanging the two weights permutes the NN directions and fields.
Reflecting the support k->M-k replaces each p_s by 1-p_s, negates the
b fields and preserves the a fields, up to relabeling the nodes.
Both transformations preserve the input cube and output norm exactly.
We may therefore arrange

    0<p1<p2<1, p2>=1/2, p2(1-p2)=q_* .                    (3)

Indeed choose a marginal with the largest |1-2p_s|, reflect if its p_s
is below 1/2, and put it second. After that reflection it is the larger
parameter. A tie can be settled either way. Formula rho is invariant
under these symmetries.

Under z=2k/M-1, b_j=2B_j/M-1. Formula (2) makes b2 affine on the
triangle with vertex values 2p2-1, 1-2p1, 1-2p2. Its sup magnitude is s.
The b1 vertex values are 2p1-1, 1-2p1, 1-2p2, so its scale is also s.
The a fields have a nonzero first marginal variance, hence positive
scales. No componentwise-output division at individual zero entries is used.

### Exact terminal derivative

Put

    a=p1/(1-p1), b=p2/(1-p2), h=1+b,
    A=(a+b)/(b-a), B=2b/(1+b)=2p2.

Here A>1, b>=1. Fix n+m=M, m>=1, and let P be the monic type-II
polynomial in k. Its binomial transform

    H(z)=sum_(k=0)^M binom(M,k) P(k) z^k

has zeros of orders n at a and m at b, by the ordinary/Euler derivative
jet equivalence at nonzero points. Thus

    H(z)=C(z-a)^n(z-b)^m, C!=0.                            (4)

The Mth finite-difference identity for a monic polynomial gives
H(-1)=(-1)^M M!. Applying it to kP(k) minus the monic support
polynomial gives the terminal diagonal coefficient

    B_(n,m,2)=-H'(-1)/H(-1).                               (5)

This is the same elementary identity used in PD-T437; it applies to
the present arbitrary positive a,b as well.

Perturb only the second weights by relative parity,

    w_(2,k)(epsilon)=w_(2,k)(1+epsilon(-1)^k).

This direction has norm one, fixes nodes and the first weights, and
retains positivity for |epsilon|<1. Normality persists locally. The
differentiated constraints and monicity are

    (z-a)^n divides dot H(z),
    (z-b)^m divides dot H(z)+H(-z),
    dot H(-1)=0.                                          (6)

Write dot H=(z-a)^n S, deg S<=m. Let T be the Taylor polynomial through
degree m-1 at z=b of -H(-z)/(z-a)^n. Then (6) gives

    S(z)=T(z)-T(-1)(z-b)^m/(-h)^m,
    S'(-1)=T'(-1)+(m/h)T(-1).                             (7)

Define

    D_(n,m)(y)=(1+y/(a+b))^n (1+y/(b-a))^(-n)
                                             (1+y/(2b))^m,
    R_(n,m)=sum_(j=0)^(m-1) (m-j)(-h)^j [y^j]D_(n,m)(y).

Since

    -H(-(b+y))/(b+y-a)^n
       =-C(-1)^M A^n(2b)^m D_(n,m)(y),

substituting (7) into the derivative of (5) yields exactly

    dot B_(n,m,2)=(-1)^n A^n B^m R_(n,m)/h.                (8)

For example the scalar factor in (8) follows directly by dividing
-S'(-1) by C(-h)^m. This retains signs and all degree shifts.

### Sum the actual signed responses

Let r=m-1. The finite coefficient sum above can be written

    R_(n,r+1)=[t^r](1-t)^(-2)(1-t/B)^(r+1) F(t)^n,
    F(t)=(1-h t/(a+b))/(1-h t/(b-a)).                      (9)

For any formal power series g and scalar c,

    sum_(r>=0) x^r [t^r](1-ct)^(r+1)g(t)
       =(1+cx)^(-2)g(x/(1+cx)).                          (10)

To prove (10), use linearity and g(t)=t^j. The coefficient of x^r on
either side is zero for r<j and is
(-c)^(r-j) binom(r+1,r-j) otherwise. All operations are formal, so no
analytic-convergence assumption enters.

Set x=Bz,c=1/B and use

    F(Bz/(1+z))=(1-z/A)/(1-Az).

Summing (9) with the factors in (8), first in r and then in n, gives

    sum_(L>=0) z^L sum_(n+r=L) A^n B^(r+1) R_(n,r+1)
       = B(1-Az)/((1+(1-B)z)^2(1-2Az+z^2)).              (11)

By (3), e=B-1=2p2-1 lies in [0,1). Also

    [z^L](1-Az)/(1-2Az+z^2)=(rho^L+rho^(-L))/2,           (12)

since rho+rho^(-1)=2A. This follows either by the two geometric
series or their second-order recurrence, including L=0,1. Every
coefficient on the right of (12) is positive, and the coefficients
of (1-ez)^(-2) are nonnegative with constant term one. Equations
(8),(11),(12) imply

    sum_(n+m=M,m>=1) (-1)^n dot B_(n,m,2)
      >= (B/h)*(rho^(M-1)+rho^(-(M-1)))/2
       = q_* (rho^(M-1)+rho^(-(M-1))).                    (13)

Individual terms need not be assigned positive signs in advance;
(13) sums their actual derivatives for one admissible global direction.
There are M terms. Their maximum absolute value is at least the
absolute value of their signed sum divided by M. The conversion from
B to b multiplies derivatives by 2/M, and the output field scale is s.
Thus (13) proves (1).

Finally, A^2-1=4p1p2(1-p1)(1-p2)/(p2-p1)^2, proving the displayed
closed formula for rho. At fixed distinct parameters its prefactor
is positive and polynomial in N, so taking Nth roots proves the liminf.

### Fixed masses

The second mass derivative under parity is
c0=sum w_(2,k)(-1)^k=(1-2p2)^M. Replace parity by

    zeta_k=((-1)^k-c0)/(1+|c0|).

Then |zeta_k|<=1 and sum w_(2,k) zeta_k=0. The constant relative
weight direction is an exact null direction of the NN map. Hence every
response in (8) is divided by 1+|c0|<=2, giving the stated one-half
bound. When the perturbed marginal has p2=1/2, c0=0 and there is no
factor loss. For a pair with a symmetric marginal, use that orientation
directly in (8)–(13), without the optional q_*-minimizing choice (3).
If the nonsymmetric parameter exceeds1/2, first reflect k to M-k and
then relabel so it is the first parameter below1/2 while the symmetric
second remains1/2. In that orientation b=1, e=0 and q2=1/4, proving the
stronger specialization above.

## Checks

`../code/c2_rate_checks.py` independently solves the defining moment
systems and their differentiated equations in Fraction arithmetic,
compares all selected terminal rows with (8), and compares their signed
sum with (11), and checks the field-scale formula. This script tests
selected exact derivatives/orientations, not a direct general verification
of PD-T437(13); the latter specialization was checked separately in
audit-01's C/t2 and C/t7 scripts. The receipt `../c2-rate-checks.json` records actual
scope, hashes and platform. These finite checks support the algebra;
the all-N proof has no computational premise. Supplementary independent
rerun and Claude audit remain separate records, when performed.

## Sources

No new primary literature result. Frozen predecessor proofs above and
the prospective gate `../novelty-gate-C2.md` supply provenance.

## Scope and open items

This is an explicit exponential *lower base* for local worst-case
conditioning in the stated monic, fieldwise metric. It does not identify
the true rate, a finite-perturbation radius or actual rounding loss.
The input direction leaves the binomial family, as the input model permits.
The matching upper, gauge-optimal interpretation, full Hahn lower and
general solver stability remain separate tasks. The original PD-T448
statement and registered OPEN display are preserved in this response;
the [parent classification proposal](../classification-proposal.md) proposes
PARTIAL through the separately solved benchmark rate conjunct, with all
remaining target conjuncts OPEN.

## History

2026-11-06: Codex gpt-6.1-sol xhigh, rules/local source
`76ba4214b100c86a44941f5e9a662ce9ce48efb8`, coordinator pinned topic
`b4a04981d42c7cd872957facf5e3995e4096ca67`. First written parameter
extension after the C2 gate. No predecessor edits or Git mutations.

2026-11-06 response, Codex gpt-6.1-sol high, rules/source `3d5b29d`:
the former “Split from: PD-T448 (sharp matching rate target, OPEN)”
label is corrected to a supporting-dependency relation (MINOR-6).
This general-pair lower does not settle the full matching-rate target;
the benchmark rate conjunct is solved by the separate sharp-upper result
with PD-T437. Statement, proof and PROVED status remain unchanged.
