# PD-T?nn-mop-cond-codex-C1-02 — scalar and fixed-mass derivative controls

ID kind: PD-T. Aliases: scalar Jacobi control; polynomial functional
derivative; weighted-median mass constraint; log-weight equivalence.
Split from: none. Split into: none.

## Statement and definitions

Fix N distinct real nodes x_l and positive weights w_l. Write L(f)=sum w_l
f(x_l), p_k for its orthonormal polynomials with positive leading
coefficient, and x p_k=b_(k+1)p_(k+1)+alpha_k p_k+b_k p_(k-1), with
b_k>0 for 1<=k<N and b_0=0. Set beta_k=b_k². For each k<N define

    A_k(x)=(x-alpha_k)p_k(x)²-2b_k p_k(x)p_(k-1)(x),
    B_k(x)=beta_k[p_k(x)²-p_(k-1)(x)²],

with p_(-1)=0. Then the scalar coefficient derivatives are

    dot alpha_k=dot L(A_k), dot beta_k=dot L(B_k),
    dot L(f)=sum_l [dot w_l f(x_l)+w_l dot x_l f'(x_l)].       (1)

For k>=1, dot b_k=dot beta_k/(2sqrt(beta_k)). For each coefficient
row, the exact support norm under |dot x_l|<=s_l and
dot w_l=w_l z_l, |z_l|<=1, sum w_l z_l=0, is

    sum_l s_l |g_(x,l)|+min_lambda sum_l w_l |g_(w,l)-lambda|. (2)

A weighted median of the g_(w,l) attains the minimization. Without the
mass constraint replace the second term by sum_l w_l |g_(w,l)|.
For two measures with separate mass constraints, add the two independent
weighted-median supports. Logarithmic weight coordinates have the same
first-order boxes as componentwise-relative weights.

Input variants used in measurements are: mixed s_l=1; natural-spacing
s_l=2/(N-1); componentwise-node s_l=|x_l|; fixed-mass s_l=1 with (2).
The phrase "relative node perturbations in natural spacing" is ambiguous;
both spacing and componentwise-node models are explicitly computed.

## Assumptions and status

Overall status: PROVED. Finite positive support, degrees through N-1,
exact real arithmetic; no asymptotic statement. Candidate disposition:
standard derivative/control variant, historical novelty unclaimed.
PD-T432 is the corresponding NN induced-norm predecessor, and PD-T286
supplies the scalar moment formulation. No external theorem is imported.

## Proof

Differentiate L(p_k p_j)=delta_kj. For j<k, polynomial degree makes
L(p_k dot p_j)=0, so L(dot p_k p_j)=-dot L(p_k p_j). The p_k component
of dot p_k is -dot L(p_k²)/2. Multiplication by x couples p_k to only
p_(k-1), p_k and p_(k+1), and dot p_k has degree at most k. Differentiating
alpha_k=L(x p_k²) therefore gives the first formula in (1).

Let P_k be monic, h_k=L(P_k²). Since dot P_k has lower degree,
dot h_k=dot L(P_k²). Thus beta_k=h_k/h_(k-1) gives
dot beta_k=beta_k dot L(p_k²-p_(k-1)²). This remains valid at k=N-1;
no nonexistent positive terminal norm is used. The dot b identity is the
ordinary derivative of the positive square root. The formula for dot L
is the chain rule at fixed polynomial f.

For (2), subtract lambda sum w_l z_l=0 from the weight objective. Its
absolute value is at most sum w_l |g_l-lambda| for any lambda. A weighted
median splits the total mass into at most half strictly above and at most
half strictly below. Choose z_l=sign(g_l-lambda) off the median and choose
the values on median indices in [-1,1] to balance the mass. Their available
mass is enough by those two inequalities. This attains the upper bound.
The independent node signs attain their support simultaneously. Symmetry
of the tangent box makes the absolute support equal the signed support.
For log weights w_l(epsilon)=w_l exp(epsilon z_l), differentiating at zero
gives dot w_l=w_l z_l, proving the local equivalence.

## Metrics and checks

Monic scalar output is the pair (alpha,beta), separately field-sup scaled;
symmetric orthonormal output is (alpha,sqrt(beta)), again separately
scaled. An exactly zero alpha field from symmetric weights uses absolute
scale one under PD-T432's stated convention. It is not assigned an
artificial near-zero relative denominator. Consequently the symmetric
controls are mixed absolute/relative metrics, not fully relative alpha.

`code/c1_metrics.py` implements (1) in O(N²) work and compares all row
entries against the distinct frozen forward-AD recurrence at small N.
The measured grid/fits and exact executed commands are in
`attempts/C1.md` and `c1-summary.json`; no computer proof is claimed.

## Scope and open items

The derivative and constrained supports are exact. All-N polynomial
upper bounds for these particular scalar families remain unproved here;
finite small growth ratios are evidence only. No error theorem for an
algorithm follows from a condition number.

## History

2026-11-06, Codex gpt-6.1-sol xhigh; source/rules
`b4a04981d42c7cd872957facf5e3995e4096ca67`.
