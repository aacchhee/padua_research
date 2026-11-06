# Focused independent check 02 — Hahn terminal rate

2026-11-06. Supplementary checker, separately requested by the coordinator
after independent-checks-01.md was frozen. This record does not amend that
earlier scope or approve final readiness. No Git, developer-file or shared
registry edits. Rules/topic source:
`b4a04981d42c7cd872957facf5e3995e4096ca67`; local materialized rules snapshot
`76ba4214b100c86a44941f5e9a662ce9ce48efb8`. Allocation/identity limitations
are as recorded in independent-checks-01.md.

## Finding and exact scope

**No unresolved mathematical defect found** in the reviewed
`theory/c2-hahn-terminal-rate.md` proof. Its stated exact every-M comparison,
terminal parity-row root limit, and full-map lower liminf follow from the
displayed argument. The constant is

    rho_H = 12.1136005841302404957748402233263025450790694193003340300324...

The proof does not give a matching upper bound for the full Hahn Jacobian,
equality of its liminf/limsup, a finite-perturbation estimate, or a floating
stability theorem. The measured finite base near 11.8 is not a premise.
The claim is for the exact alpha1=1, alpha2=3/2, gamma=1 family and its
declared input/output norm. Both M parities are essential and are covered.

The full state/IDEAS and relevant predecessors/gates were read during
check01. For this focused continuation, read the new C2-03 round-3 gate,
complete new theorem and producer checker, and used the independently
reconstructed all-N Hahn normality dependency. This is verification of the
registered terminal-dual continuation, not a priority or novelty finding.

## Independent analytic reconstruction

1. **Half-grid and signs.** At the balanced terminal index the row points
   are exactly 1+j/2 for j=0,...,M-1 at both parities. Direct products in
   the Lagrange formula at y=-M-1 give the stated sign (-1)^j and magnitude
   (2M+4)_M/[(2M+4+j)j!(M-1-j)!]. Every second-marginal row has odd j.

2. **Terminal values.** The residue difference d_l-d_(l-1), its partial
   sum, and the finite-difference conversion produce the displayed
   alternating values of P(k). Expanding 2-z as 1+(1-z) proves the positive
   binomial expression for T_(M,k). There is no sign estimate replacing a
   cancellation-prone sum at this step.

3. **Derivative normalization.** The transform of dot P has denominator
   E=(x+1)_(M+1), whose derivative at -M-1 is (-1)^M M!. Its residue there
   is -dot tau. Interpolation therefore has the sign and row-factor
   cancellation in equation (6). The second weight normalization Z2
   cancels between the defining moment row and its perturbation.
   Telescoping (2M+4)_M/(2M+6)_M gives exactly K_M in equation (7).
   Parity makes every term have the same sign.

4. **Polynomial and metric factors.** Replacing i+5/2 by i+3 bounds the
   rising-factorial ratio by a polynomial uniformly for 0<=k<=M and
   0<=i<floor(M/2). The stated bounds on K_M and both denominator factors
   imply precisely A_M/54 and 3(M+1)^2 A_M. The affine derivative factor
   is 2/M. The already proved upper field scale 2M+3 is sufficient for
   the full relative condition lower. Subtracting the weighted parity
   mean removes a constant relative-weight null direction, and dividing
   by 1+|mean| loses at most two. It preserves zero mass exactly.

5. **Generating function.** Since X has zero constant term, extending
   its k-sum to infinity changes no coefficient of degree M. The odd
   binomial sum gives equation (8) for odd and even M. Y begins
   1+z+3z^2, while f begins 1/2+(5/2)z; consequently the subtracted term
   is exactly (-1)^(M-1)(3M+2)/2. H and f have positive coefficients
   with the asserted common radius.

6. **Entropy lower, including integer degree.** At the unique interior
   mean-one saddle, p has positive p0,p1,p2 and finite moments. For each
   fixed K, q0=sum_{j=2}^K(j-1)p_j is positive and q1 is the original p1
   plus a positive tail mean. These give a probability distribution of
   mean one. Its entropy relative to p tends to zero as K increases;
   the coordinates 2,...,K coincide with p and omitted coordinates have
   q=0. The proposed type counts satisfy

       n0 = sum_{j=2}^K (j-1)n_j - 1,

   so n0 is eventually positive. n1 is eventually positive too. Their
   sum is exactly L and weighted sum exactly L+1, for every sufficiently
   large integer L, without a lattice/parity subsequence restriction.
   The elementary factorial estimate applies with K fixed. Taking
   liminf in L first and then K to infinity proves the subexponential
   probability cost. The upper probability bound one completes the root
   limit. Positive f(0) transfers the lower; the alternating linear
   subtraction cannot change an exponential rate greater than one.

7. **Algebraic base.** Squaring the saddle equation gives the stated
   quartic in w after removing the boundary factor (w-1)^2. The selected
   solution lies on the unsquared positive branch. The rho quartic is
   reciprocal, with rho+1/rho=7+3sqrt(3); the other possible sum is below
   two. The unique interior saddle excludes the extraneous branches.

The dependence on all-N normality is valid: the degree-M mixed polynomial
and degree-(M+1) support successor both lie in the already proved normal
domain. Here the nodes are fixed, so the successor derivative is zero.

## Fresh exact checks

`code/independent_hahn_rate.py` imports no developer implementation.
It constructs rational Hahn weights directly, solves the defining
monomial moment systems by its own Fraction elimination, and solves every
second-weight coordinate derivative before summing the parity response.
Direct Lagrange products provide a separate derivative dual evaluation.

Executed from the topic directory:

```sh
python code/independent_hahn_rate.py > independent-hahn-rate-receipt.json
```

Exit status zero. Coverage:

- M=2,...,11: ten balanced defining-moment systems; 75 separate relative
  second-weight derivatives; exact terminal values, dual signs and
  positive-sum formula; both polynomial bounds; ten fixed-mass directions.
- M=2,...,20: nineteen exact generating-function coefficient identities,
  using independent formal-series multiplication from
  Y=sum_j binom(2j,j)X^j/4^j.
- 110-digit evaluation of the radical, original unsquared saddle relation
  and reciprocal quartic. Residuals are below 1e-100. This numerical check
  supports the analytic elimination; it is not an algebraic root proof.

Representative exact values are A_2=25, D_2=48/11 and A_3=184,
D_3=68400/1183. The saddle is approximately
0.228770121581293760864387008978935023271585671773222321786321.
All complete finite values and source hashes are in the small receipt.
Finite checks support the formulas; they are not premises replacing the
analytic all-M or asymptotic proofs.

## Reviewed identities and remaining disposition

Reviewed theorem SHA256:
`5945fdde195b45f2e5476f2846686137652f88685efff1694881242378e09a63`.
Normality dependency SHA256:
`a8c2fc56a4876b92798f88ef7d763c102fee1839885668fb2cdf642337bb1da5`.
Independent checker SHA256:
`056062a1e6e1ac337f8a56e9503d319e2fac3f8d1f86261be30b1a1054b0dce9`.
These record the reviewed snapshots and are not prose-hash execution gates.

No correction to the new proof was needed during this review. The
coordinator and required final Claude auditor retain their separate
disposition responsibilities. Full-map sharp Hahn growth remains OPEN
without a matching full-input, full-field upper bound.

Final bounded corollary check: read the updated
`theory/c1-hahn-gauge-lower.md`, SHA256
`f6f5250585a49eaa9b61d6cf016ebc57fdf201b4d94836eafc7830e86690ed1b`.
The stronger full-NN gauge bounds follow: b2 is the identical input
function under each positive fixed gauge and local positive C1 section,
so its derivative and field scale preserve the C2-04 witness and its
rho_H lower liminf. For fixed masses only this invariant b2 row needs
to annihilate constant relative-weight changes; other fields of an
input-dependent gauge need not do so. The finite denominators 27 and 54,
N>=3 restriction for the stronger bound, node/log-weight variants and
retained N2 base-two bound are consistent with the dependencies. No
defect found; no numerical rerun was needed. This corollary gives no
full-map rate equality, matching upper or step-line claim. Check01 and
the focused numerical receipt remain unchanged.

## Scoped upper-envelope failure check

At the coordinator's additional request, read the complete
`theory/c2-hahn-upper-envelope.md` and its round-4 gate. Reviewed SHA256:
`580011e688ca4c29a23b25e1bbfdd62d04c6822adaa97d6d6173230702f31227`.
No defect found in its analytic rejection of the specified product of
global maxima. This is an additional focused proof review, with no new
numerical premise or rerun.

The exact terminal signs give D_M as the full second-weight row support,
and D_M<=E_M is the elementary valid decoupled envelope. On M=4l+2,
k=M/2 is an admissible node and j=M/2 is an odd second-weight row.
For G=(2-z)/(1-z)^2 the mean-one equation reduces to
r^2-3r+1=0, with interior saddle (3-sqrt(5))/2 and
G(r)/r=(11+5sqrt(5))/2. The prior finite-type argument applies with
weighted sum exactly s rather than s+1: the resulting n0 is
sum_{j>=2}(j-1)n_j, eventually positive. The analytic prefactor
(1-z)^(-4) does not change the coefficient root limit.

The factorial ratios give exactly 4/27 for the polynomial factor and
27/2 for the chosen dual interpolation factor. The remaining rising
factorial ratio has root (3125/256)^(1/4). Fixed shifts and the weight
mass have root one. Thus their product gives the stated subsequence
lower beta=2 sqrt((11+5sqrt(5))/2)(3125/256)^(1/4) for E_M's root
limsup. The rational comparisons sqrt(5)>559/250,
sqrt(lambda)>333/100 and the fourth-root lower 1863/1000 imply
beta>12.40758; rho_H<7+3sqrt(3)<12.2. All constants and signs in the
separation are consistent.

A single subsequence with root lower above rho_H suffices to rule out
any uniform C M^a rho_H^M bound for this E_M. It does not give a lower
bound of beta for D_M, a larger full-map rate, or a contradiction to a
sharp full-map upper at rho_H. Retaining the pointwise P(k)Q2(k)
correlation is outside the rejected estimate. The full Hahn upper target
remains OPEN, and the previously checked exact correlated row rate is
unchanged. Check01 and both independent checker scripts/receipts were
not changed in this additional review.

## Final bounded upper-search representation check

Read `theory/c2-hahn-upper-search.md`, its rounds5–6 gate and the complete
finite checker. This record states unresolved estimates, not a new full
upper theorem. No substantive defect found in its retained formulas or
the two narrowly stated failed routes.

For degree t, the residue of dot F at -t-1 is
-dot tau/(M-t+1)!, and E'(-t-1)=(-1)^t t!. The row-factor ratio is
1/[(alpha_s+1)_i(x_j+t+2)_(M-t+1)], giving equation (1)'s exact
normalization. The polynomial-value expression (2) correctly gains the
factor (t+2-l)_(M-t); its zeros allow extension of the residue sum to
l<=k. The explicit M=3,t=1 counterexample gives U(0)=24,U(1)=18,
so unchanged terminal finite-difference positivity genuinely fails.
This does not invalidate the exact representation or a correlated bound.

The direct node channel in equation (4) contains both P'Q_s and P Q_s'.
The latter differentiates the fixed row test (k+alpha_s+1)_i. The dual
coefficients are frozen at the base point; no derivative of a weight
with respect to its independently specified location is introduced.
The same node displacement is shared between both marginal channels.
The binomial ratio and sign in the grid differentiation matrix are
correct. A single central column entry gives its exponential lower
2^M/[M(M+1)], ruling out the proposed universal polynomial unweighted
grid-supnorm derivative transfer. This does not rule out a weighted
bound on the actual P,Q_s or force a larger condition-number rate.

Fresh independent execution of the developer checker, exit status zero:

```sh
python code/c2_hahn_upper_search.py --max-m 6 > /tmp/nn-mop-conditioning-20261106/independent-c2-hahn-upper-search.json
```

All 75 indices at M=2,...,6 passed: 430 polynomial values, 860 separate
relative-weight coordinates and 430 common-node coordinates agree
exactly with defining Fraction moment systems. The rational separation
constants in the preceding envelope lemma also pass. This is a separate
execution of the producer implementation, supplemented by the analytic
reconstruction above; no second implementation is claimed for this
attempt record. No finite checks resolve its missing uniform estimates.

Reviewed attempt SHA256:
`7346a84d9d69bf9adef8af59db99bf57480bfba8a6f6779e74dace43840bbdde`.
Executed checker SHA256:
`5b2f7a4576bbe183e2156caa12faee0625b9eb9f3aed4a55a283e27d5b9555f3`.
The 795-byte local JSON has SHA256
`633c4c7a10b685ab912d093e2a5c5a1cfcbe3dd00699ebc6286229ec498ac4ca`
and records both helper hashes and Python version. It is a regenerable
local artifact, not a claimed cold-storage delivery. No new mechanism,
rate conclusion or readiness approval follows from this final check;
the established lower results and the OPEN full-upper target are
unchanged. Check01 and the two independent checker scripts/receipts
remain untouched.
