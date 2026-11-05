# N6 round2 — Precisely gate full-vector trace mixtures

2026-11-05. Codex N6, parent-assigned gpt-6.1-sol xhigh;
effective runtime metadata not independently exposed. Rules/input
`714f3cad18859c07cd13f31561f2a185f9591a7f`. Round1 published at
`0bca52bc1b8edf2e91d3749b710d2df285dc3e6b`; its files are unchanged.

## Gate before application

The exact predecessor gate remains [round1's gate](../novelty-gate-N6.md),
which credits the unchanged complete-registry baseline. Additional reads
at the current head: complete N4 variance-rigidity record
`PD-T?argmax-bridge-codex-N4-02`, round1's N6 candidate and attempt, and
the parent's round2 scope. Searches over the registry and the bridge,
alln and effective topics used `probability.*mixture|evaluation.*vector|variance.rigidity|signed.*(mass|variation)|invertible.*group|trace.*supremum`.
No external fulltext, literature transfer or novelty claim.

The application below is informed by the already written N4 proof. It is
not a blind preregistration or a new generic variance theorem. The closest
previous attempts are319/341's common envelope/convex sum,342's distinct
coarse individual-sign mechanism, N6-01's same-t two-norm comparison, and
N4-02's full-vector rigidity. No norm inequality follows from the family
substitution alone.

## IDEA?argmax-bridge-codex-N6-02 — Probability mixtures on fixed traces

Aliases: arbitrary-time trace transference; positive full-cardinal lift.

- Question / scope: for n>=2 and a fixed finite phase set S, can every
  square point z satisfy L(z)=integral L(y) dmu_z(y), with mu_z a
  probability measure supported on U_S=union_(s in S) Gamma_s(T)?
- Mechanism and hypotheses: retain the entire signed cardinal vector;
  integrate whole vectors before applying the norm. S is fixed
  independently of z. In particular S={0,pi} allows arbitrary comparison
  times along both complete traces, rather than round1's same-t endpoints.
- Closest entries read in full:319/341/342, N6-01, and N4-02.
- Separation criterion: positive trace transference could imply a global
  trace-supremum comparison without assuming it. A point z outside U_S
  at which the required representation is impossible kills this class.
- Literature limits: internal elementary results only.
- Applicable obstructions: N4-02 applies to complete vectors, n>=2 and
  probability measures. N086's individual-sign hypotheses are not used.
- Novelty verdict: variant/application of N4-02 to319/341; no generic
  theorem duplication.
- Cheapest decisive test: apply N4-02; certify an exact off-support point
  using T_n(x)^2 != T_(n+1)(y)^2 for S={0,pi}. No sampling is needed.
- Kill criterion before application: mu_z must equal delta_z by N4-02,
  but its prescribed support excludes z.
- Test discriminability: this excludes full-vector positive lifts only;
  a scalar norm bound can hold without such a lift.
- Actual result: N4-02 forces mu=delta_z. For S={0,pi}, exact trace
  support is T_n(x)^2=T_(n+1)(y)^2, which excludes
  z_n=(cos(pi/(2n)),1) for every n>=2 and the existing n2 witness.
- Disposition: **REJECTED: failed**, for the universal full-vector lifting
  mechanism only. The off-support existence statement is refuted; global
  scalar trace comparison remains OPEN. No new independent check claimed.
- Canonical record: [PD-N?argmax-bridge-codex-N6-02](../theory/N6-trace-mixture-application.md),
  PROVED analytic application of the existing N4 theorem.
- History: informed formulation after reading N4-02, before writing its
  trace-support application.

## IDEA?argmax-bridge-codex-N6-03 — Mass-one signed contraction lift

Aliases: signed trace weights with total variation at most one.

- Question / scope: replace mu in N6-02 by a real finite signed measure
  nu of mass1 and total variation<=1, preserving the full vector identity.
- Mechanism: signed weights could appear to permit a larger representation
  class while the triangle inequality would preserve the norm bound.
- Closest predecessor: N6-02's positive mixtures; parent's explicit
  elementary total-variation gate.
- Separation / kill criterion: Jordan decomposition decides whether any
  negative part is possible. If mass1 and TV<=1 force positivity, the
  claimed repair is equivalent and receives no new negative theorem ID.
- Cheapest decisive argument: compare positive and negative masses.
- Literature / obstruction scope: no source transfer; exact real measures
  only. No statement about signed lifts with TV>1 is intended.
- Actual result / disposition: **equivalent**, consolidated with N6-02.
  Positive and negative masses p,q obey p-q=1,p+q<=1, forcing q=0.
  No new negative ID; signed lifts with TV>1 remain outside scope.

## IDEA?argmax-bridge-codex-N6-04 — Scalar envelope or invertible grouping of full vectors

Aliases: normalized envelope times evaluation mixture; exact pair grouping.

- Question / scope: can a common scalar E>=0 times a probability mixture,
  or a common invertible linear regrouping R of all cardinal coordinates,
  repair N6-02 while still proving a contraction?
- Mechanism: L(z)=E integral L(y)dmu(y), or
  R L(z)=integral R L(y)dmu(y), with the same R in both sides.
- Closest predecessor:319/341, N6-02 and N4-02. Individual fixed signs
  from342 are not required.
- Separation / kill criterion: partition of unity tests E; invertibility
  tests whether grouping changes the mathematical identity. If E=1 and
  grouping can be undone, consolidate with N6-02 rather than duplicating it.
- Cheapest decisive argument: apply the constant functional, or R inverse.
- Exact grouping example to assess: pair two cardinals as
  E_pair=(L_i+L_j)/2, O_pair=(L_i-L_j)/2, so
  |L_i|+|L_j|=2 max(|E_pair|,|O_pair|). Keep both features, including
  zeros and collisions. This changes the displayed norm, not the vector
  information. Discarding O_pair is a different, unjustified step.
- Literature limits: internal algebra only.
- Actual result / disposition: **equivalent**, consolidated with N6-02.
  Partition of unity forces E=1; applying R inverse restores the original
  identity. Exact pair grouping preserves signs and norm but is invertible.
  Nonlinear block-norm features are outside this equivalence and remain
  undeveloped, not rejected. No separate negative ID.

## IDEA?argmax-bridge-codex-N6-05 — Unrestricted scalar trace mixtures

Aliases: one-block nonlinear feature; scalar probability comparison.

- Question / scope: replace L by the single scalar lambda_n and ask for
  lambda_n(z)=integral_U lambda_n(y)dmu_z(y), mu_z a probability measure,
  with U=Gamma_0(T) union Gamma_pi(T).
- Mechanism: taking the scalar norm before forming a mixture avoids N4's
  complete-polynomial reproduction hypothesis.
- Closest predecessors: N6-02 and broad319/341; it is distinct from the
  pointwise same-t comparison in N6-01.
- Separation / cheapest decisive gate: compare feasibility with
  lambda_n(z)<=max_U lambda_n, before testing any measures or grids.
- Actual result: min_U lambda_n=1, the maximum is attained, and every
  scalar value between them is a two-point probability mixture. Thus
  feasibility is exactly the desired global trace-supremum bound at z.
  The argument and degenerate-maximum case appear in the disposition record.
- Verdict / disposition: **equivalent**, not a new mechanism; no PD-N.
  The global comparison remains OPEN and is not rejected by N6-01/02.
- Sources / limits: elementary compactness and partition of unity; no
  external literature, computation or novelty assertion.
- Canonical record: [N6 round2 disposition](../theory/N6-round2-disposition.md).
- History: considered and algebraically gated in round2; no scalar
  feasibility experiment was run or relied on.

## Broader comparison kept separate

Let C_S=max_(s in S) max_t lambda_n(Gamma_s(t)). The independent scalar
question is whether lambda_n(z)<=C_S everywhere. Failure of N6-01 or
N6-02 does not refute this question. A one-block positive mixture of
scalar values lambda_n(y), y in U_S, may evade vector rigidity, but its
feasibility must first be compared with that scalar question itself.
No unrestricted scalar envelope was tested or treated as a mechanism.
Broader319/341 is **deferred** with the exact resumption criterion in the
round2 disposition. N6 ends after this productive gate round; no round3
development began and no direction-wide impossibility is claimed.
