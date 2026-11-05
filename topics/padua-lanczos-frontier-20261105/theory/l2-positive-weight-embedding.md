# PD-T?lanczos-frontier-codex-L2-03 — positive-weight extension of the finite smooth-rule closure reduction

ID kind: PD-T.
Aliases: weighted evaluation embedding; DST-compatible source normalization.
Split from: the uniform-measure limitation of L2-01; the uniform record is unchanged.
Split into: none.

## Statement

Fix a finite injective graded degree n and arbitrary positive weights
w_i, held fixed under perturbation. Put W=diag(sqrt(w_i)) and

    [p]=W(p(z_i))_i, S_s={[p]:deg p<=s}, b_0=[1],
    b_k=[p_k], d_k=sum_i w_i p_k(z_i)^2, q_k=b_k/sqrt(d_k),

where p_k is the monic graded polynomial orthogonal to earlier monomials
in the discrete weighted inner product. Let fixed admissible parents,
exact starting q_0 and the saved smooth exact-base rule class operate
on these Euclidean represented vectors. Then the complete first-order
rule invariance, actual X-closure derivative and W/R certificate formulas
of L2-01 hold with these b,d and their weighted monic recurrence.

In particular the source conversion and budget remain

    F_h=sqrt(d_parent) f_h,
    tau_h²=||A_h b_parent||²,
    sigma_h²=||A_h q_parent||²=tau_h²/d_parent,
    sum_h ||f_h||²/sigma_h²=sum_h ||F_h||²/tau_h².            (1)

The saved random law is **unchanged in represented-vector coordinates**:

    f_h(i)=sigma_h xi_hi/sqrt((N_n-1)M),
    Cov(f_h)=sigma_h² I_M/((N_n-1)M).                       (2)

There is no additional sqrt(w_i) multiplier in this law. Its full-law
expectation is the same nonnegative source/stage trace, divided by
`(N_n-1)M||X||²`. The weights affect the basis, projectors and source
scales; they do not replace the specified covariance by diag(w_i).

This is a finite embedding theorem, with no all-degree growth or IEEE claim.

## Definitions and assumptions

Uniform L2-01 notation is reused after substituting the weighted b,d:
`Q_s=B_s D_s^(-1/2)`, `P_s=Q_s Q_s^T`, `R_s=I-P_s`, the exact
weighted coefficients alpha, frozen scalar responses g, coordinate
expansion C_X,s, and monic sourced response V. Injectivity concerns
unweighted polynomial evaluation and is equivalent to weighted injectivity
because W is invertible. Weights need not sum to one; q_0=[1]/sqrt(sum w).
Sources are arbitrary Euclidean vectors in this represented space.

Class R_smooth reproduces the exact normalized weighted basis at zero;
its coefficient/normalization functions are differentiable for each fixed
source. It has the same exclusions as the saved class. Weights, nodes,
parents and initial vector are not perturbed. X-norm normalization requires
||X||>0. All formulas are finite at each chosen degree; no uniform radius
or common bound on rule derivatives is asserted.

## Status by part

Overall status: PROVED, analytic. Distinct supplementary mathematical
reconstruction accepted; required later Claude audit remains pending.

| Part | Status | Reason |
|---|---|---|
| Weighted polynomial kernel and rule invariance | PROVED | Coordinate-weight commutation and the complete derivative induction below |
| Actual closure and source scaling | PROVED | Same two-projector calculation with weighted orthonormal basis |
| Full independent-sign trace and partial-trace lowers | PROVED | Euclidean covariance (2), with cross terms removed before bounding |

## Depends on

L2-01's written finite-dimensional proof; its uniform restriction is
explicitly extended here. No SH_n recurrence or growth estimate is needed.
Positive-weight monic orthogonalization is defined directly above.

## Checks and sources

No code or numerical experiment is needed for this analytic result.
The distinct supplementary reviewer read and reconstructed the full
initial draft SHA256
`c84368610d33030f6f50480488fc9135c34c275e3bdab91dfbfb4b8e81e2949e`
without a mathematical finding, including the covariance and rationality
qualifications. Its separate report is independent-checks-l1-l2.md;
this verification metadata does not alter the proof.
The prior uniform-grid G2 certificates are separate finite evidence, not
weighted test runs. Closest repository sources are PD-T136/137 and
PD-N062; relevant scope and source-law distinctions are in the completed
L2 gate. No new original paper or historical-priority claim.

## Proof

**Weighted polynomial spaces.** X and Y commute with W, being diagonal,
so A[p]=[a p] and A S_s is contained in S_(s+1). The weighted inner
product is positive definite on the injective polynomial space. Graded
Gram–Schmidt therefore yields the stated positive pivots and monic basis.
For an admissible product the leading monomial is the target, hence the
weighted recurrence has exactly the same triangular form

    b_k=A_k b_parent-sum_(l<k)alpha_kl b_l.

At the exact normalized baseline its coefficient and pivot identities
are still `c_kl=alpha_kl sqrt(d_l/d_parent)` and
`beta_k=sqrt(d_k/d_parent)`.

**Normal quotient.** Differentiate the saved normalized recurrence and
put `w_k=sqrt(d_k) dot(q_hat_k)`. Exactly as in L2-01, it becomes

    w_k=A_k w_parent-sum_(l<k)alpha_kl w_l+F_k+h_k,

where h_k is a scalar combination of the weighted polynomial vectors
q_0,...,q_k, and hence belongs to S_deg(k). Subtract the frozen V
recurrence. If E_parent is in its weighted polynomial space, then A_k
E_parent belongs to the next such space because A_k W=W A_k. Induction
gives `w_k-V_k in S_deg(k)`, including all normalization derivative
terms and all earlier parent changes. Consequently

    Z_s=R_s dot(Q_hat_s)=R_s V_s D_s^(-1/2).

Projector differentiation is Euclidean on represented vectors, so the
same formula `Pdot_s=Z_s Q_s^T+Q_s Z_s^T` applies. Exact weighted
closure gives `XQ_s=Q_(s+1)H_X,s`. Both moving-projector terms therefore
give

    D_X,s=R_(s+1)X Z_s-Z_(s+1)H_X,s
          =R_(s+1)[X V_s-V_(s+1)C_X,s]D_s^(-1/2).           (3)

The full closure-operator derivative is D_X,s Q_s^T and has the same
spectral/Frobenius norms. The nonempty-class and pointwise-limit arguments
in L2-01 consequently remove the infimum over the saved weighted class.

**Source metric and covariance.** Multiplying the normalized local source
by sqrt(d_parent) in the derivative gives (1) exactly. Thus `u_h=F_h/tau_h`
has joint Euclidean norm one. The saved sign law has
`u_hi=xi_hi/sqrt((N_n-1)M)` and diagonal covariance I/((N_n-1)M)
on all represented-coordinate source positions. Independence and zero
means remove cross-source terms in the expected squared Frobenius norm
of the common linear map (3). The expected sum is therefore its full
Hilbert–Schmidt trace divided by the same global denominator and ||X||².
Every source/stage contribution is nonnegative; a subset gives a lower
only **after expectation**, not a pointwise lower on each realization.

The node impulse formula remains

    ell_s,h,i=tau_h² R_(s+1),ii sum_(j<N_s)omega_s,j,h(i)²/d_j.

All spectral, trace and row inequalities of L2-01 follow from the same
Euclidean norm arguments. They require no artificial weight factor in
the source law.

**Arithmetic qualification.** For rational nodes and positive rational
weights, p coefficients, alpha, d, tau², C_X,s, g and omega are rational.
Although b entries and off-diagonal projector entries may contain square
roots of weights,

    R_s,ii=1-w_i sum_(k<N_s)p_k(z_i)^2/d_k

is rational, so ell, H², U² and the exact expectation trace remain rational.
The statement does not pretend that every off-diagonal R entry is
rational. A variational certificate may set r=Wz: then
`R_s r=W(I-P_values)z`, with
`P_values=P_poly D_s^(-1)P_poly^T diag(w)`. Its numerator and denominator
are rational quadratic forms in rational z, and W is invertible, so no
test directions are lost. General real/algebraic weights retain the
analytic theorem; computational claims require their stated exact or
outward arithmetic rather than a rationality assertion.

## Scope and open items

This supplies the required positive-weight bridge for a later SH_n
application once that family's hypotheses and the actual closure response
are supplied. It is not itself a growth theorem. No weight perturbation,
unweighted-value random law, literal working-precision storage, actual
IEEE activation or unrestricted PD-T055 conclusion is established.
The accepted independent mathematical check and required still-pending
Claude protocol/scientific audit remain separate. The uniform L2-01
record and its hash are unchanged.

## History

- 2026-11-05: Codex, configured gpt-6.1-sol xhigh. Written on root's
  explicit post-G2 authorization, before applying the finite reduction
  to the saved nonuniform DST family. The global random law, thresholds
  and source metric are preserved; the extension is stated separately.
- 2026-11-05: Verification metadata updated after distinct mathematical
  reconstruction accepted the complete initial draft. Statement and
  proof are unchanged; required Claude audit remains pending.

- 2026-11-05, audit response A-P1/R2: this result descends from W/R
  definitions drafted before the mandatory reading gate, first committed
  at `0574c47`. The completed-gate receipt was first preserved at `aab7bbe`
  (`684849d` was the worker input/rules SHA); the later proof and G2
  certificates followed the reported completed reading, and actual G2 acceptance preceded all-degree development.
  Later reading does not waive or cure the deviation. AC decides its
  acceptance; see [gate-timing-response-01.md](../gate-timing-response-01.md).
  This additive metadata preserves the statement/proof and status; the
  required focused Claude re-audit remains pending.
