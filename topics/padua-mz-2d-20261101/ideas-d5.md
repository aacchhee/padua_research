# D5 candidates: signed hyperinterpolation

Rules/base `cf89b140530d5838bdb208a8c28f3e7aa676ace3`; 2026-11-01.
Codex mathematical worker, allocated xhigh; runtime model metadata unexposed.
D5 activated by the orchestrator after D1 PASS and the source review in
[literature.md](literature.md). Git and shared registries are orchestrator-owned.

## Gate and frozen tests

Registry headings, identifiers, aliases and summaries were scanned across
the complete current state/IDEAS.md, with its obstruction and disposition
tables inspected. Relevant full entries: IDEA-055/056/072/075; full M3
candidate record; PD-T025; the M2 Padua foundation; campaign definitions,
plan and D1 record. Literature: the existing MZ records and prior-art
comparison, plus the primary source review in literature.md. Search terms
were `signed`, `hyperinterpolation`, `upper Gram`, `absolute weight`,
`negative mass`, `total variation`, `aliasing`, `tensor`, and `operator bound`
across Markdown theory/topic/state/literature records. A broad search also
matched generated JSON; those output lines were not used as evidence.

No historical novelty is claimed. The closest mathematical predecessor is
the positive-rule duality estimate PD-T025 / IDEA-075. The change of
hypothesis to signed weights is material: Cauchy--Schwarz must use an
absolute measure. SVZ's total-variation limit concerns an integration
functional, and ASV's general estimates assume positive weights. Neither
is silently promoted to a signed Padua operator theorem.

### IDEA-219 — transfer the signed upper Gram bound alone

Aliases: signed analogue of PD-T025; free positivity transfer.

- Question/scope: for any signed quadrature exact at constants, infer
  `||H_n||_(C->L2)<=sqrt(V lambda_max(G_n))` from its signed Gramian.
- Mechanism/hypotheses: reuse positive weighted Cauchy--Schwarz on a signed
  nodal functional.
- Closest predecessor read: IDEA-075 and PD-T025, which explicitly require
  positive weights and make no conclusion for signed rules.
- Separation criterion: remove positivity without adding an absolute-weight
  control. A signed exact rule with fixed `G_n` and unbounded operator norm
  erases that proposed distinction.
- Applicable obstruction: signed quadratic forms are not norms on arbitrary
  nodal data, even when their restriction to polynomials is positive.
- Verdict: proposed extension, not a duplicate theorem; expected failure is
  tested explicitly rather than attributed to an unread source.
- Cheapest decisive test / prewritten kill criterion: test the constant
  approximation space on three nodes `-1,0,1`, Lebesgue measure, and weights
  `(t,2-2t,t)`, `t>1`. Kill if its Gramian stays one but its operator norm
  exceeds `sqrt(2)`.
- Test discriminability: exact three-node algebra decides the universal
  transfer claim; it says nothing adverse about a separate Padua bound.
- Actual result: kill fires, with norm `(4t-2)/sqrt(2)`; analytic proof in
  PD-N050.
- Disposition: **REJECTED: refuted**, general signed transfer only. The
  actual Padua norm is not refuted.
- Canonical negative record: `theory/mz2d-hyperinterpolation-signed-obstruction.md`
  under tracks/mz-constants.

### IDEA-220 — absolute-weight duality and negative leverage

Aliases: signed hyperinterpolation adjoint norm; absolute Gram repair.

- Question/scope: bound the signed quadrature coefficient map by the Gramian
  of the absolute weights and their total variation.
- Mechanism/hypotheses: on a compact metric domain with distinct nodes,
  continuous bounded inputs realize arbitrary nodal signs. The exact norm is
  the supremum of `sum |w_i| |p(x_i)|` over unit continuous-L2 polynomials.
- Closest predecessor read: IDEA-075 / PD-T025; elementary duality is the
  same mechanism, with a changed measure in its Cauchy--Schwarz step.
- Separation criterion: the conclusion explicitly uses `G_abs` instead of
  `G_signed`. A sign pattern whose absorption fails for continuous inputs,
  or a missed mass factor, would kill the asserted identity.
- Applicable obstructions: negative signed weights and the one-sided Padua
  marginal cannot be treated as positive sampling norms.
- Novelty verdict: **variant with explicit hypothesis repair**, no claim
  that this elementary duality is historically new.
- Cheapest decisive test / prewritten kill criterion: write coefficient
  duality before estimating; verify that a continuous function of norm one
  can attain each required nodal sign. Then verify `G_abs=G+2G_minus`.
- Actual result: analytic identity and bounds survive; see
  PD-T112. No numerical test is required for this calculation.
- Disposition: retained as a PROVED supporting result in development;
  independent audit pending.

### IDEA-221 — reproduce only the degree permitted by exactness

Aliases: signed relaxed-exactness error; `m>=n+r` reproduction.

- Question/scope: give an error estimate for the actual signed Padua
  coefficient operator, with a stated reproduced degree.
- Mechanism/hypotheses: if `0<=r<=n` and `n+r<=m`, every product of a
  degree-r input and a degree-n basis member lies in the exactness space.
- Closest predecessor read: IDEA-055/075 and PD-T025. The product-degree
  argument is identical and uses no positivity; only the norm estimate
  needs the repair in IDEA-220.
- Separation criterion: none claimed as a new reproduction mechanism.
  Failing to check the degree of each coefficient product would invalidate
  the application.
- Literature limits: CDMV uses positive Chebyshev rules; its log-squared
  uniform norm is not this signed operator estimate.
- Cheapest decisive test / prewritten kill criterion: check `r=1,n=m-1`
  and `r=n` separately. The latter is justified by this argument only when
  `2n<=m`; no endpoint projection is inferred.
- Actual result: `||f-H_m,n f||_2 <= (2+sqrt(tau_m beta_abs(m,n)))E_r(f)`
  proved in PD-T113.
- Disposition: equivalent reproduction argument with a signed-norm variant,
  retained; no PD-N for equivalence.

### IDEA-222 — uniform signed Padua bounds: target and failed majorants

Aliases: absolute Gram closure; negative-leverage control.

- Question/scope: is `sup_m ||H_(m,m-1)||_(C->L2)` finite, or can the actual
  signed coefficient operator be given a useful explicit all-m bound?
- Mechanism/hypotheses: IDEA-220 reduces one sufficient route to bounds
  on `tau_m` and `beta_abs(m,m-1)`, or on signed `lambda_max` together with
  negative leverage `chi_m=sum_(w<0)|w|K_(m-1)(x,x)`.
- Closest predecessors: IDEA-056/075, IDEA-220, SVZ integration-functional
  stability. The new unresolved obligation is quantitative control of the
  absolute nodal measure on the Legendre polynomial space.
- Separation / kill criterion: total variation alone is insufficient, and
  signed `lambda_max<2` alone is insufficient. A diverging sufficient bound
  kills only that majorant, not the actual operator norm.
- Novelty verdict: deferred quantitative application, no priority claim.
- Actual result, updated after the supplementary Astra finding: D3's exact
  negative corner gives `beta_abs,chi >= |w_c|K_(m-1)(c,c)` with the latter
  equal to `(log m)/6+O(1)`. Since `tau_m>=4`, the proposed uniform
  `tau_m beta_abs` majorant diverges, as does the negative-leverage majorant.
  Proof: PD-N052. Their degree-dependent upper-bound inequalities
  remain valid. The actual operator norm has not been shown to diverge.
- Disposition split: **REJECTED: failed** for the uniform absolute-Gram and
  bounded-negative-leverage mechanisms; the actual operator-norm target
  remains **deferred, OPEN**. Resume that target with direct weighted-L1
  control, a useful degree-dependent estimate, or another specified majorant
  that escapes this corner obstruction.
- Canonical records: target PD-T114, OPEN; failed-majorant
  obstruction PD-N052, PROVED in development.
- History: original title “uniform signed Padua operator bounds” and exact
  question above are preserved. The original “neither sufficient route has
  been closed” disposition is superseded only for the two uniform majorants
  by the new analytic obstruction; the actual-norm target is unchanged.

### IDEA-223 — promote endpoint reproduction beyond degree one

Aliases: endpoint E2 estimate; endpoint projection error bound.

- Question/scope: for the actual Padua operator `H_(m,m-1)`, `m>=3`, can
  the exactness argument be improved to reproduce `Pi_2`, or give an
  error bound solely in terms of `E_2` (and consequently `E_(m-1)`)?
- Mechanism/hypotheses: polynomial exactness is tested on every coefficient
  product, rather than identifying the cubature degree with the reproduced
  degree.
- Closest predecessors read: candidates 30--32, IDEA-055/075, D1 nodal
  aliasing and PD-T021's exact marginal. This is a diagnostic obstruction,
  not a new approximation construction.
- Separation / cheapest kill criterion frozen before writing the proof:
  test `q=T_2(x)` against `T_(m-1)(x)` for odd m; for even m test
  `q=T_2(y)` against `T_(m-1)(y)` and use the checkerboard relation
  `T_(m+1)(y)=T_m(x)`. Any nonzero product defect kills reproduction of
  `Pi_2` and every E2-only estimate for all continuous inputs.
- Actual result: the defects are respectively `h_(m-1)-h_(m+1)` and `h_m`,
  both nonzero. Written proof: PD-N051.
- Disposition: **REJECTED: refuted** for this precise reproduction/error
  mechanism. No obstruction to an estimate with an aliasing term or to
  convergence for a fixed function is claimed.

## Round ledger

1. Exact sign-data counterexample rejects the positive-rule transfer in its
   stated general signed scope.
2. Absolute-weight duality supplies the valid signed norm identity and bound.
3. Product exactness supplies the error estimate at the correct reproduced
   degree; the actual uniform Padua norm remains a separate OPEN target.
4. Exact quadratic tests show that degree one is the maximal complete
   reproduced space at `n=m-1`, for `m>=3`.
5. Supplementary Astra identified, and the developer reconstructed, the
   logarithmic negative-corner obstruction to the uniform absolute-Gram
   and negative-leverage majorants. The actual norm target remains OPEN.

No new source was contacted, no numerical execution is claimed, and no
shared registry or manuscript was modified by this worker.
