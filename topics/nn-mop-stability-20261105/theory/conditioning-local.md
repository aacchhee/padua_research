# PD-T?nn-mop-stability-codex-D1-01 — local derivative and induced condition numbers

ID kind: PD-T. Aliases: NN Jacobian; mixed componentwise-input conditioning;
fieldwise coefficient sup metric; monic step-line derivative.
Split from: D1 growth-law target (OPEN). Split into: none.

## Statement

For N distinct real nodes and two positive weights, assume every mixed
moment matrix of total degree at most N is nonsingular (PD-T286 convention).
The NN coefficient map F through degree N−1 is real analytic locally in
the 3N ordinary coordinates q=(x,w1,w2). Its derivative is given below.
For arbitrary fixed nonnegative input scales s_i, and positive output
field scales A_f=max_nu |F_(nu,f)(q)|, the exact first-order condition is

    kappa(s)=max_(nu,f) [sum_i |J_(nu,f),i| s_i]/A_f,   J=DF(q).

That is the limit as eps decreases to zero of the supremum of the
fieldwise relative output error divided by eps, over |h_i|<=eps*s_i.
The same statement applies to the monic alternating step-line map below,
with its own three field scales. If some field is identically zero at
the base point, use absolute scale one there or specify an extended-real
relative convention; no division by zero is silently performed.

## Definitions

The output metric is exactly PD-T290's E: max over four fields of the
sup error divided by the base field's sup magnitude. The following input
models are different quantities:

- mixed: node scales ||x||_infinity and weight scales w_(s,l);
- componentwise-input: node scales |x_l| and weight scales w_(s,l);
- block-normwise: node scales ||x||_infinity, weight scales ||w_s||_infinity;
- ordinary global normwise: every coordinate scale ||q||_infinity.

The first three are computed by conditioning.py. The primary table uses
mixed; nodes are in [−1,1], so its node scale is one. Componentwise-input
freezes a zero node and can give a smaller condition. Independent weight
perturbations need not preserve each mass. Scaling either complete weight
vector leaves F unchanged, giving two exact null directions. We do not
impose a fixed-mass tangent constraint, whose induced norm would differ.

Fully componentwise *output* conditioning is instead max_j
sum_i|J_ji|s_i/|F_j|, with 0/0=0 only when the numerator is zero. A zero
coefficient with nonzero sensitivity makes it infinite. For the Krawtchouk
p2=1/2 inputs, b2_(0,0)=0 and its weight derivative is nonzero, so this
full-output condition is infinite. Floating values close to zero cannot
be used as substitutes for an exact zero classification.

## Assumptions

Fixed N; distinct real nodes; strictly positive weights; all stated
normalities; nonzero field scales for the relative metric; exact real
arithmetic in the theorem. The implementation evaluates the formulas in
mpmath, which gives measured approximations, not certified enclosures.

## Status by part

Overall status: PROVED (written analytic proof; independent audit pending).
The conditioning table and any inferred growth law are separate records.
Candidate disposition: retained standard derivative specialization; no
historical novelty or algorithmic stability claim.

## Depends on

PD-T286 (defining moment systems, h ratios and subleading b differences),
PD-T288/289 (nonzero interior divisors and exact layer reconstruction).
PD-T136/137 are methodological predecessors read at the pinned head:
they concern a different span quotient and Euclidean source model; their
numerical conditions are not substituted for this coefficient condition.

## Proof or evidence

Write mu_(s,r)=sum_l w_(s,l)x_l^r. Its directional derivative is

    dot mu_(s,r)=sum_l [dot w_(s,l)x_l^r
                        +r w_(s,l)x_l^(r−1) dot x_l],

where the second term is zero when r=0. At nu of degree k, write the
defining system M_nu c_nu=−v_nu. Differentiate it to obtain

    dot c_nu=−M_nu^(−1)(dot v_nu+dot M_nu c_nu).

Let c_(nu,k)=1 and dot c_(nu,k)=0 for the monic coefficient. Then

    dot h_(nu,s)=sum_(j=0)^k [dot c_(nu,j)mu_(s,nu_s+j)
                              +c_(nu,j)dot mu_(s,nu_s+j)],
    dot a_(nu,s)=(dot h_(nu,s)−a_(nu,s)dot h_(nu−e_s,s))
                 /h_(nu−e_s,s),
    dot b_(nu,j)=dot t_nu−dot t_(nu+e_j).

Absent predecessor coefficients and their derivatives are zero. Every
matrix inverse and every ratio denominator is nonzero at q. Finitely many
such denominators remain nonzero in an open neighborhood. Thus these
rational expressions define an analytic map and the displayed derivatives
are its ordinary Jacobian, including at terminal coefficient sites. The
terminal equality b1=b2 holds throughout this common-support neighborhood,
so its differentiated equality holds as well.

For a row j of J and scales s, the maximum of |sum_i J_ji h_i| over
|h_i|<=eps*s_i is eps sum_i|J_ji|s_i: triangle inequality is attained by
choosing the signs of the h_i to match that row. Maximizing over finitely
many output rows gives the formula. Analyticity gives a uniform O(eps^2)
Taylor remainder on this compact scaled input cube. This proves the
stated limit even when some input scales are zero.

The implementation uses exact differentiation rules for +,−,*,/ through
monic Stieltjes marginals and the PD-T289 layer graph. Both evaluate the
same rational map on the neighborhood; their real-arithmetic derivatives
therefore agree with the defining-moment derivative above. This certifies
the *analytic derivative algorithm*, not its floating numerical accuracy.

For comparison fix nu_k=(ceil(k/2),floor(k/2)), Q_k=P_(nu_k), first step e1.
The monic four-term recurrence is

    x Q_k=Q_(k+1)+beta_k Q_k+gamma_k Q_(k−1)+delta_k Q_(k−2).

Here beta_k=b_(nu_k,1) for even k and b_(nu_k,2) for odd k;
gamma_k=a1_(nu_k)+a2_(nu_k). For k>=2, put eta=nu_k−e1−e2:
delta_k=a2_(nu_k)d_eta for odd k, and −a1_(nu_k)d_eta for even k.
Set gamma_0=0 and delta_0=delta_1=0. These formulas follow by inserting
P_(eta+e1)−P_(eta+e2)=d_eta P_eta into the NN recurrence; the sign depends
on which predecessor is Q_(k−1). They are polynomial formulas in NN data,
so ordinary chain differentiation and the same row-sum argument apply.
This monic step-line convention need not equal a literature algorithm's
diagonally scaled Hessenberg output; no unverified numerical equivalence
to LIT-347's condition number is asserted.

## Checks

code/conditioning.py computes all 3N derivative columns and exact induced
row sums in real arithmetic, with mpmath evaluation. Its separate small
moment_map constructs all moment matrices, performs pivoted elimination,
and applies the h/t formulas; the N4 comparison and precision checks are
recorded in attempts/D1.md. These support the implementation; the theorem
is the written argument and does not depend on a computer proof.

## Sources

No new primary-source claim. PD-T290 specifies the source input families.
PD-T058/059's localized moment-cone framework is contextual: its inradius
and residual normalizations are not this forward coefficient norm.

## Scope

Local first-order sensitivity with input/output norms explicit. A large
kappa is a worst-case capacity. It neither predicts error for every
perturbation nor proves that a rounding algorithm realizes a maximizing
direction. E/(kappa*u) is a gate diagnostic, not a backward-error theorem.

## Open items

Sharp all-N growth, informative finite-eps remainder radii, numerical
outward derivative enclosures, fixed-mass constrained induced norms and
the effect of alternate diagonal scaling of the step-line output.

## History

2026-11-05: D1 Codex developer, requested gpt-6.1-sol xhigh. Rules and inputs
823cf6a4ef7c01b4ef3d2a6fec3e9f19d4b4f6f1; base b4d292eea5eed373002506d5e16a3761bd7ae10e.
The local theorem is split from the growth-law target, which remains OPEN.
