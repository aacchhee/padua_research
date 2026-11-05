# PD-T?lanczos-nonproduct-codex-P4-04 — moment-preserving aggregate capacity transfer

ID kind: PD-T.
Aliases: atomless same-support moment transfer; bounded-density quotient
comparison; finite cubature source-domain distinction.
Split from: P4-02 model candidate and P3 transfer obligation.
Split into: none.

## Statement

Fix n, a graded monomial order and admissible coordinate parent rule R.
Let mu,nu be compactly supported probability measures with U(n), agreeing
on every polynomial in Pi_(2n). For the monic aggregate source model of
p4-weighted-normal-quotient.md and p4-continuous-capacity.md, the exact
polynomial b_k, alpha_kl, d_k, sigma_h and response polynomials g_kh
coincide through degree n. In particular their pointwise matrices C_n
coincide. The following implications hold for any fixed declared source
subset J.

1. If both measures are atomless and have the same closed support K, then

       kappa_mu(n;J)=kappa_nu(n;J)=max_K ||C_n(z)||_2.        (1)

2. More generally, suppose mu=rho nu on a common underlying measure space
   and 0<a<=rho<=b<infinity almost everywhere. In the full arbitrary-L2
   source model (finite atomic or continuous),

       sqrt(a/b)*kappa_nu <= kappa_mu
                           <=sqrt(b/a)*kappa_nu.            (2)

3. If nu is atomless with support K and mu is a positive finite cubature
   on nodes z_i in K, exact on Pi_(2n), with U(n), then

       max_i sqrt(1-P_mu,ii)*||C_n(z_i)||_2
          <=kappa_mu<=max_i||C_n(z_i)||_2<=kappa_nu.         (3)

No reverse finite-cubature comparison follows from polynomial exactness
alone: if the finite measure has M=N_n then kappa_mu=0, while the atomless
capacity is positive for every nonempty J.

## Definitions

Both measures use the same physical x,y multiplication directions, order,
fixed rule and relative-raw-product source convention. A capacity
comparison between different rules uses each rule's own sigma values.
Pi_n as a subspace of L2 is the same algebraic polynomial space, but its
orthogonal projector generally depends on the measure. P_mu,ii is the
finite represented normal-leverage diagonal of the weighted theorem.

## Assumptions

Moment matching is through degree2n, not only through n. Every source is
an arbitrary L2 function. Compactness, positivity and U(n) ensure all base
polynomial constructions exist. For (2), measure equivalence and the
uniform density bounds are essential to its norm-comparison proof.

## Status by part

Overall status: PROVED (analytic fixed-degree transfer theorem).

| Part | Status | Evidence |
|---|---|---|
| Polynomial identities and (1)–(3) | PROVED | Written proof below |

Candidate disposition: retained support lemma. A family-specific
all-degree application remains the owning direction's responsibility.

## Depends on

PD-T?lanczos-nonproduct-codex-P4-02 and P4-03. PD-T039 is the earlier
polynomial-moment-matching predecessor; its product recurrence statement
does not itself transfer arbitrary-source capacities.

## Checks

Analytic proof only; no executed high-degree scan or independent audit.
No positive cubature of a specified degree is asserted to exist here.

## Sources

Repository predecessors as above; no external theorem or priority claim.
The P3 bounded-density obligation was relayed by the coordinator.

## Proof or evidence

All inner products used to Gram–Schmidt monomials through degree n are
integrals of degree<=2n polynomials. Moment matching therefore identifies
the unique monic orthogonal polynomials and their d_k. Each alpha_kl
uses a raw parent product of degree at most the target degree<=n and
an earlier b_l of degree<=n, again degree<=2n. Each raw-product squared
norm sigma_h^2 has degree<=2n. Hence alpha,sigma and the scalar frozen
g recursion are identical. Formula (1) follows directly from P4-03's
atomless identity. No equality of the two Hilbert-space projectors was
assumed.

To prove (2), use function-value sources f rather than represented
Euclidean coordinates. For a matrix Y=[V_k(f)/sqrt(d_k)] of L2 functions,
the normal-output norm is

    ||(I-P_mu)Y|| = sup_(||c||=1) dist_mu(Yc,Pi_n).

The pointwise Y is the same algebraic function of f for both measures.
Norm equivalence gives sqrt(a)||h||nu<=||h||mu<=sqrt(b)||h||nu. Taking
the infimum over polynomial approximants preserves these inequalities
for every distance, and then the supremum over c preserves them for
the normal-output norms. The identical sigma scales give the same
sqrt(a),sqrt(b) comparison of source norms. Thus a nu-unit source has
mu-source norm between sqrt(a) and sqrt(b); rescaling and taking the
supremum proves both sides of (2). The argument works for finite atoms
as well as for continuous measures.

For (3), equality of C is already proved, and the finite bounds in P4-03
give its first two inequalities. The support inclusion and atomless
identity give the last inequality. If M=N_n, U(n) implies the finite
polynomial space fills its entire ambient space, so the capacity is
zero. Conversely C(z)_(h,h)=sigma_h/sqrt(d_h)>0 for each h in J at
every z, hence the atomless formula gives a strictly positive capacity.
This demonstrates why arbitrary-source moment transfer cannot be
asserted without retaining the ambient model.

## Scope

If a density perturbation preserves the moments through2n and stays
between two degree-independent positive constants, finite capacities for
each fixed rule remain comparable within a degree-independent factor.
For a BJ/comparator ratio the possible multiplicative loss is at most
b/a. In the atomless same-support case there is no loss at all. This is
only an implication: the construction, positivity, exactness and genuine
non-product status of a perturbation are separate obligations. Sources
in the two models can depend on degree; no fixed IEEE realization follows.

## Open items

Family-specific use in P3 or other directions; required exact scans;
independent mathematical audit; finite-epsilon source restrictions.

## History

- 2026-11-05: Codex P4 developer, gpt-6.1-sol xhigh allocation, runtime
  metadata unexposed; rules head ed5515ed84e0e7b12163175dce9f22a859c89c99.
  Transfer statement proved rather than inferred from matching moments.
