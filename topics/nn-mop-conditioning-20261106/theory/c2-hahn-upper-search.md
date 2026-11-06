# C2 Hahn full-upper search — retained unresolved estimates

Record kind: attempt record (parent candidate C2-03); no PD-T/PD-N ID
or overall theorem status is assigned to this unresolved search ledger.
Open targets: the correlated arbitrary-index and common-node estimates
below. Scoped negative statements have their own PROVED PD-N homes:
[positivity failure](response-c2-positivity-failure.md) and
[unweighted node-transfer failure](response-c2-node-transfer-failure.md).
Full retained candidate records:
[C2-03-r5 and C2-03-r6](../candidates-response-C2.md).

This is an attempt record, not a new proved full-map rate claim or a
historical novelty claim. It continues C2-03 after the PROVED terminal
rate and the separately PROVED rejection of the global-maxima envelope.
The full Hahn upper in PD-T448 remains OPEN. These were rounds5 and6
of the bounded C2 search; neither supplies a new quantitative upper.
The full parent target's classification proposal, distinguishing its
proved benchmark Krawtchouk rate conjunct from the open Hahn obligations,
is in [classification-proposal.md](../classification-proposal.md).

## Round5: arbitrary-index Cauchy inverse

Fix 1<=t=n+m<=M and the t row parameters x_j from
`c2-hahn-normality.md`. Let ell_j(y) be their Lagrange coefficients,
y=-t-1, and let row j belong to s,i, so x_j=alpha_s+i. Differentiating
the same rational interpolation system gives the integer-node
subleading-coefficient derivative for independent relative weights:

    dot tau=(-1)^t (M-t+1)!/t! *sum_s sum_k W_s(k)eta_s(k)P(k)Q_s(k),
    Q_s(k)=sum_(j belonging to s,i) ell_j(y)
           *(k+alpha_s+1)_i
           /[(alpha_s+1)_i(x_j+t+2)_(M-t+1)].            (1)

Indeed the denominator of dot F is E=(x+1)_(t+1), its numerator has
degree<=t-1, E(x_j)/R_s(x_j) is the final reciprocal factor in (1),
and its residue at y is -dot tau/(M-t+1)!. Interpolation of that
numerator and E'(y)=(-1)^t t! give (1). At t=M it reduces to the
terminal formula. Equation (1) is a representation; it supplies no
sharp uniform estimate for the sum of absolute values.

The polynomial values themselves exhibit the obstruction to simply
reusing terminal positivity. Put

    V(l)=prod_(j=1)^t(l+1+x_j),
    U(l)=V(l)(t+2-l)_(M-t),
    C=(t+1)!/[(M-t)! prod_j(t+2+x_j)].

The residue and hockey-sum derivation of the terminal values now gives

    P(k)=C(-1)^(t+k) Delta^k U(0)/(M-k+1), 0<=k<=M.     (2)

To verify (2) algebraically, the residue of F at -l-1 is
C(-1)^(t-l)V(l)/(l!(t+1-l)!) for l<=t+1. In the hockey-sum formula
it acquires (M-l+1)!, converting the ratio to (t+2-l)_(M-t).
For t+2<=l<=M this last product is zero, so the finite sum can
be extended through k and identified as the difference in (2).

At the balanced index, V(l)=2^(-t)(2l+4)_t; however the complementary
factor of U has decreasing factors. An exact counterexample to the
unchanged positive-difference extension is M=3,t=1,nu=(1,0):

    U(l)=(l+2)(3-l)(4-l), U(0)=24,U(1)=18, Delta U(0)=-6.

Thus Delta^k U(0)>0 is false below terminal degree, even at a balanced
index. The terminal proof's positive sum cannot be carried over as
written. The canonical scoped PROVED negative statement and candidate
disposition are [PD-N182](response-c2-positivity-failure.md)
and [C2-03-r5](../candidates-response-C2.md).
An upper could still bound the cancellations in (2), use a
different coefficient representation, and prove uniformly over n,m,t

    (M-t+1)!/t! *sum_s,k W_s(k)|P(k)Q_s(k)|
         <=poly(M)rho_H^M.                              (3)

No such inequality was obtained in this bounded round. Absolute
values of the complementary factors or separate global maxima lose
the needed correlated structure. Disposition: REJECTED: failed for
the unchanged positivity extension; the correlated arbitrary-index
estimate (3) remains OPEN. This is not a failure of the shared kernel
representation or a counterexample to a matching full-map upper.

## Round6: common-node transfer through grid differentiation

For the same dual and integer-node perturbations delta k, differentiating
each moment product gives the exact node forcing in dot tau:

    (-1)^t (M-t+1)!/t! *sum_s,k W_s(k)delta k
                     *(P'(k)Q_s(k)+P(k)Q_s'(k)).        (4)

The same delta k appears in both channels, as required by the input
model. On z=2k/M-1 a node displacement of norm one corresponds to
|delta k|<=M/2, only a polynomial factor. Formula (4) therefore
requires a weighted correlated derivative estimate, beyond (3).

The cheapest proposed transfer was to control each derivative by a
polynomial times the unweighted supnorm on the M+1 grid nodes. This
fails at degree M. The interpolation differentiation matrix satisfies,
for j!=k,

    D_(k,j)=(-1)^(j-k)binom(M,j)/[binom(M,k)(k-j)].       (5)

Formula (5) follows by differentiating the grid's Lagrange cardinal
polynomials. With k=0 and j=floor(M/2), M>=2,

    ||D||_infinity >=binom(M,j)/j >=2^M/[M(M+1)].        (6)

The last inequality uses that the central binomial coefficient is a
maximum among M+1 positive coefficients whose sum is 2^M. Hence no
polynomial-in-M unweighted grid-supnorm derivative transfer can hold
for all degree<=M polynomials. A bound that uses this operator norm
introduces exponential growth, so it does not give a rho_H upper.
The actual terminal P and Q can have additional weighted correlation;
(6) does not rule out exploiting it, nor assert the node condition is
larger than rho_H. Disposition: REJECTED: failed for the polynomial
unweighted transfer; the weighted estimate for (4) remains OPEN.
Canonical scoped PROVED negative statement:
[PD-N183](response-c2-node-transfer-failure.md);
retained candidate: [C2-03-r6](../candidates-response-C2.md).

## Stop and remaining task

Finite developer check `../code/c2_hahn_upper_search.py --max-m 6`
compares (1),(2),(4) with defining Fraction moment systems at every
index and each forcing coordinate for M=2,...,6. Receipt:
`../c2-hahn-upper-search.json`:75 indices,430 polynomial values,860
weight coordinates and430 common-node coordinates pass. These checks
support the representations, not the missing uniform inequalities.
Exact rational separations in the envelope proof are checked as well.

After productive rounds1--4, these two bounded full-upper attempts
produced no new quantitative conditioning bound. Stop at six rounds
of an up-to-eight budget under the two-empty-round rule. No claim
that all eight rounds or all possible upper mechanisms were exhausted.
Full closure still needs estimates (3),(4) and transfer to every NN
a/b field with only polynomial loss. The fixed-pair Kraw upper uses
a different analytic factorization; its closure does not imply these
Hahn estimates. The exact rho_H row rate and full-map liminf lower
are retained unchanged.

2026-11-06: Codex gpt-6.1-sol xhigh; rules/local source76ba421,
published topic pin b4a04981d42c7cd872957facf5e3995e4096ca67.
Gate: C2-03 rounds5--6. No predecessor/shared edits or Git mutations.

2026-11-06 response, Codex gpt-6.1-sol high, rules/source `3d5b29d`:
explicit attempt label and candidate links added for MAJOR-3; the two
already audited negatives receive standalone provisional PD-N homes.
The formulas and unresolved estimates are unchanged.

## Final ID aliases (2026-11-06)

- `PD-N?nn-mop-cond-codex-response-C2-positivity` → `PD-N182`.
- `PD-N?nn-mop-cond-codex-response-C2-node-transfer` → `PD-N183`.
