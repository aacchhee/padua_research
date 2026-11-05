# PD-T330 — Explicit finite-error selection bound

Final registration (2026-11-05): **PD-T330**; status **PROVED** unchanged. Canonical provisional/historical aliases: `PD-T?lanczos-frontier-codex-L3-01`; `PD-T?lanczos-frontier-codex-L3a`. See [complete map](../preparation/final-id-map.json). This is ID metadata only; original statement/proof and frozen input bytes retain their scopes.

Provisional scoped ID; no final assignment. Codex, requested
`gpt-6.1-sol` xhigh; rules read at
`bb67c1ee830d468fa33007e15008d5574d00ccf4`.

ID kind: PD-T.
Aliases: PD-T?lanczos-frontier-codex-L3a; L3a explicit-radius majorant;
L3b adaptive finite-union corollary; explicit finite-error selection bound.
Split from: related reformulation of PD-T143's OPEN item "provide a
finite-u transfer radius" and handoff01's possible shape "a finite-u
radius for the first-order guarantee, with an explicit O(u²) remainder".
This is a supporting result with changed source hypotheses, not a proved
conjunct of the broader selection target.
Split into: none; the adaptive corollary stays in this uniformly PROVED record.
Polynomial score/radius bounds, acceptance at a prescribed error size or
prescribed score filters uniformly in degree, and efficient online
selection remain OPEN.

## Statement and model

Fix a finite positive discrete measure `sum_i w_i delta_(x_i,y_i)`, with
`sum_i w_i=1`, whose evaluation map is injective on `Pi_s` (U(s)). Put
`N=dim Pi_s`, with `s>=1`, and use the fixed graded monomial order and
admissible parents of PD-T142. Work in represented Euclidean coordinates:
`q_0=(sqrt(w_i))_i`, `X=diag(x_i)`, `Y=diag(y_i)`. A complete fixed
selection `R` assigns to every `k=1,...,N-1` a previous admissible parent
`p(k)<k` and its creator `A_k` in `{X,Y}`. The chosen parent monomial
times its coordinate is the intended kth monomial. No (C) condition is
needed.

Let `q_k^*, beta_k^*>0, c_kl^*` be its exact full-projection recurrence.
For given nonnegative finite numbers `lambda_k`, consider **any** run

```
yhat_k = A_k qhat_p(k) + e_k,
chat_kl = qhat_l^T yhat_k                 (0<=l<k),
rhat_k = (I-Phat_(k-1)) yhat_k,
betahat_k = ||rhat_k||_2,
qhat_k = rhat_k/betahat_k,
Phat_(k-1) = sum_(l<k) qhat_l qhat_l^T,
||e_k||_2 <= u lambda_k ||A_k qhat_p(k)||_2,                 (1)
```

starting at exact `qhat_0=q_0`. Every displayed operation except the
declared sources is exact. Errors can depend arbitrarily on all history
and on `u`; no continuity, derivative, common direction, independence or
second-order source expansion is assumed. Let `P_s` project onto the
represented weighted polynomial space, and define the final span error
`theta_s=||Phat_(N-1)-P_s||_2`.

All constants below use only the exact baseline and the prescribed budgets.
Set `a_k=||A_k||_2`, `v_k=||A_k q_p(k)^*||_2`, and recursively define

```
h_0=0,
H_(k-1) = (sum_(l<k) h_l^2)^(1/2),
C_k = a_k(1+lambda_k)h_p(k) + lambda_k v_k + v_k H_(k-1),
h_k = 2C_k/beta_k^*,
b = max_(1<=k<N) C_k/beta_k^*.                            (2)
```

For each node `i`, write `alpha_ki=(A_k)_(ii)` and define

```
D_kl = a_k(1+lambda_k)h_p(k) + lambda_k v_k + v_k h_l,
T_kl(i) = 2D_kl/beta_k^*
          + 2|c_kl^*|C_k/(beta_k^*)^2
          + 1_(l=p(k)) 2|alpha_ki|C_k/(beta_k^*)^2,
Delta = max_i (sum_(k=1)^(N-1) sum_(l<k) T_kl(i)^2)^(1/2).  (3)
```

The exact node matrix `Lbar_R^*(i)` is unit lower triangular with

```
(Lbar_R^*(i))_kl
 = (c_kl^* - alpha_ki 1_(l=p(k)))/beta_k^*       (l<k),
(Lbar_R^*(i))_kk=1.                                      (4)
```

Choose any finite `K>=max_i ||Lbar_R^*(i)^(-1)||_2`. Finally put

```
F = (sum_(k=1)^(N-1) (lambda_k v_k/beta_k^*)^2)^(1/2),
J = (sum_(k=1)^(N-1) (lambda_k a_k h_p(k)/beta_k^*)^2)^(1/2),
d = K Delta,
r_R = min(1, 1/(2b), 1/(2d)),
B_R(u) = u K(F+uJ)/[(1-ub)(1-ud)].                       (5)
```

An inverse of zero in a radius means `+infinity`, so it imposes no
restriction. Every constant is finite and `r_R>0`. For every
`0<=u<=r_R` and every sequence obeying (1), the run completes with
positive pivots, its columns are orthonormal, and

```
||qhat_k-q_k^*||_2 <= u h_k,
|betahat_k-beta_k^*| <= u C_k,
betahat_k >= beta_k^*(1-ub) >= beta_k^*/2,                 (6)

theta_s <= B_R(u)
        <= u K F + 4u^2 K[J+F(b+d)].                     (7)
```

This is a uniform finite-error estimate, including an explicit quadratic
remainder and explicit neighborhood, for the **per-column finite-error model (1)**.
It does not assert uniformity over the merely first-order Hres families of
PD-T143. Model (1) is a zeroth-order budget relative to each computed
parent product and permits nonsmooth errors; Hres is an aggregate
derivative budget on smooth families. Neither full class contains the
other. Thus "stronger" means the finite-error control required for this
reformulation, not set inclusion of all error families. Covering every
Hres direction by prescribed per-column budgets forces
`lambda_k v_k/beta_k^* >= C_loc sqrt(N-1) chi_R` for each k and hence
`F >= C_loc (N-1) chi_R`, a factor `sqrt(N-1)` above Hres's aggregate
coefficient. The smaller coefficient in the special case below covers
that per-column model and is not a uniform transfer for all Hres directions.
The radius limitation is quantified in the dated audit-response scope note below.

For the special budget `lambda_k=C_loc`, PD-T143's exact local ratio
`chi_R=max_k v_k/beta_k^*` gives
`F<=C_loc sqrt(N-1) chi_R`. Hence additional certified filters
`K<=K_0` and `chi_R<=chi_0` recover its stated linear coefficient
`C_loc sqrt(N-1) chi_0 K_0`, now with the explicit radius and quadratic
coefficient in (5),(7), under the stronger model (1).

## Finite selection and adaptive corollaries

Let `mathcal F` be a nonempty finite class of complete admissible selections,
with the same prescribed per-column `lambda_k`. Construct (2)–(5) for each
path. The class can consist of (C)-staircases or all admissible paths.
For a specified `u>=0`, accept the paths satisfying `u<=r_R`, and minimize
`B_R(u)` among them, with fixed ties; return no accepted selection if the
set is empty. An accepted path satisfies (7), and at least one is accepted
whenever `0<=u<=max_(R in mathcal F) r_R`. This assertion is finite-degree
and includes no bound on enumeration cost or the size of its positive radius.

There is also an explicit **nonvacuous tolerance** version. For a prescribed
`0<eta<1`, define

```
r_R(eta) = min(r_R, eta/[4K(F+J)]).                       (8)
```

Use the same zero-denominator convention. Requiring both `u<=r_R` and
`B_R(u)<=eta` accepts at least one path for
`0<=u<=max_R r_R(eta)>0`, and every accepted path has `theta_s<=eta`.
The accepted minimizer is chosen from exact data before the perturbed run.
These definitions do not assume any unknown computed coefficients or drift.

For rational or represented real-algebraic nodes, positive weights,
budgets, `u` and tolerance, all this is a finite computable criterion:
one can compute the exact baseline and take, for example, the algebraic
Frobenius upper `K=max_i||Lbar_R^*(i)^(-1)||_F`. Algebraic arithmetic and
comparison then decide acceptance and fixed-tie minimization. Certified
upper enclosures can instead give conservative acceptance: the majorants
and B_R(u) are nondecreasing in their nonnegative inputs b, Delta, K, F
and J while the denominators are positive; lower enclosures of positive
exact pivots give upper majorants, and upper b,d give a conservative radius.
General real
inputs define a finite mathematical minimizer, without an asserted
computation absent an appropriate comparison representation/oracle.

An adaptive policy is covered without freezing its exact-data branch if
it always chooses an admissible next edge, with every chosen prefix
extendible to at least one member of `mathcal F`. The policy may depend
discontinuously on the perturbed history, including ties. For

```
0<=u<=r_all := min_(R in mathcal F) r_R,
```

every such run completes, its realized complete path `Rhat` belongs to
`mathcal F`, and

```
theta_s <= B_Rhat(u) <= max_(R in mathcal F) B_R(u)
        <= u max_R(K_R F_R)
           + 4u^2 max_R {K_R[J_R+F_R(b_R+d_R)]}.           (9)
```

For all admissible selections every admissible prefix has a completion;
thus (9) includes an always-defined admissible pivot policy, even when it
switches at an exact-data tie. No (C)-based implicit-section interpretation
is inferred for its non-(C) branches. This corollary is a finite-union
consequence, not a new online score or a frozen-branch differentiability
argument.

## Definitions

The represented weighted coordinates, fixed admissible paths, exact
baseline, computed projectors and source budgets are defined in Statement
and model. Equations (2)–(5) define every majorant and the zero-denominator
radius convention. All vector norms are Euclidean and matrix norms
spectral except the explicitly specified Frobenius upper for K.

## Assumptions

Positive fixed normalized weights; evaluation injective on Pi_s, s>=1;
fixed graded order and admissible immediate monomial parents; exact start,
projection and normalization; finite nonnegative prescribed lambda_k;
only sources satisfying (1) and 0<=u<=r_R. Adaptive policies must have
every selected prefix extendible within the declared finite class.

## Status by part

Overall status: **PROVED, analytic**. The broader L3 target is **OPEN**.

| Mathematical part | Status | Evidence / classification |
|---|---|---|
| Explicit finite-error nonbreakdown and bounds (6)–(7) | PROVED | Main analytic theorem; proof below |
| Finite exact-data selection and tolerance (8) | PROVED | Corollaries of the same explicit bound |
| Represented-algebraic decidability | PROVED | Finite algebraic construction and comparison |
| Adaptive prefix completion and bound (9) | PROVED | Corollary; finite union with completion before division |

Candidate disposition: retained quantitative variant, with adaptive
corollary; no independent adaptive mechanism or new PD-N is introduced.

## Proof

**Exact feasibility and constants.** Injectivity and admissibility give a
positive intended leading monomial in `A_k q_p^*`. Projection onto the
earlier monomials cannot remove it; hence every exact residual is nonzero
and `beta_k^*>0`. All exact data and (2)–(3) are finite. Each node matrix
(4) is unit lower triangular, so its inverse exists; a finite `K` exists
because there are finitely many nodes. This proves `r_R>0`. For represented
algebraic data, finite exact Gram–Schmidt and positive square roots give
algebraic baseline data and all displayed constants. Positivity of the
input weights and exact pivots determines the square-root choices.

**Projection and normalization lemmas.** If `Q` and `Qtilde` have the same
number of orthonormal columns, then

```
||Qtilde Qtilde^T-QQ^T||_2 <= ||Qtilde-Q||_2
                            <= ||Qtilde-Q||_F.           (10)
```

Indeed the first norm equals `||(I-QQ^T)Qtilde||_2`, by the equal-rank
orthogonal-projector identity (equivalently, both are the largest principal
angle sine). Multiplying `Qtilde-Q` by the orthogonal complement projector
proves the inequality. The identity includes equal full-dimensional spaces.
For nonzero vectors `r,r^*` of lengths `beta,beta^*`, writing the difference
of normalized vectors with denominator `beta^*` yields

```
||r/beta-r^*/beta^*||_2
 <= (||r-r^*||_2+|beta-beta^*|)/beta^*
 <= 2||r-r^*||_2/beta^*.                                 (11)
```

In particular, (11) needs no small perturbed denominator after nonzeroness
has been established.

**Noncircular pivot induction.** Suppose the columns preceding `k` have
been constructed, are orthonormal and satisfy (6)'s vector bound. Then
(10) gives

```
||Phat_(k-1)-P_(k-1)^*||_2 <= u H_(k-1).
```

Since `u<=1`, (1) and the parent bound give

```
||yhat_k-A_k q_p^*||_2
 <= u a_k h_p + u lambda_k(v_k+u a_k h_p)
 <= u[a_k(1+lambda_k)h_p+lambda_k v_k].                   (12)
```

Subtract the exact residual `(I-P_(k-1)^*)A_k q_p^*` from the proposed
perturbed residual. Use (12), contraction of `I-Phat_(k-1)`, and the
projector difference acting on the **exact** product of norm `v_k`:

```
||rhat_k-r_k^*||_2 <= u C_k.                              (13)
```

The reverse triangle inequality now gives the pivot statements in (6)
before dividing by `betahat_k`; they use `ub<=1/2`. Thus `rhat_k` is
nonzero, exact normalization defines `qhat_k`, exact full projection makes
it orthogonal to all prior columns, and (11),(13) prove its vector bound.
This starts from the exact zeroth column and completes the induction.

**Normalized coefficients.** Expand
`chat_kl-c_kl^*=qhat_l^T(yhat_k-A_k q_p^*)
 +(qhat_l-q_l^*)^T A_k q_p^*`. Unit norm and (12) imply
`|chat_kl-c_kl^*|<=u D_kl`. The pivot bound gives

```
|1/betahat_k-1/beta_k^*|
 <= 2u C_k/(beta_k^*)^2,
|chat_kl/betahat_k-c_kl^*/beta_k^*|
 <= 2u D_kl/beta_k^* + 2u|c_kl^*|C_k/(beta_k^*)^2.
```

Including the parent entry `-alpha_ki/betahat_k` gives exactly (3)'s
entrywise `u T_kl(i)` bound. Consequently the computed row-normalized
matrix in PD-T142 satisfies

```
||Lbarhat_R(i)-Lbar_R^*(i)||_2 <= u Delta.                 (14)
```

Neumann inversion with `ud<=1/2` therefore yields
`max_i||Lbarhat_R(i)^(-1)||_2 <= K/(1-ud)`.

**Source and span bound.** Rearranging (1) gives PD-T142's exact residual
relation with `f_k=-e_k`; the start residual is zero. The computed columns
are orthonormal, so its singular-value denominator is exactly one. By the
parent bound and (6), the residual budget satisfies

```
epsilon_s = (sum_k ||e_k||_2^2/betahat_k^2)^(1/2)
 <= u/(1-ub)
       (sum_k [lambda_k(v_k+u a_k h_p)/beta_k^*]^2)^(1/2)
 <= u(F+uJ)/(1-ub).                                     (15)
```

Apply PD-T142 to (14)–(15) to obtain `theta_s<=B_R(u)`.
For the remainder, put `D(u)=(1-ub)(1-ud)>=1/4`. Direct subtraction gives

```
B_R(u)-uKF
 = u^2 K[J+F(b+d)-uFbd]/D(u)
 <= 4u^2 K[J+F(b+d)],
```

which proves (7) uniformly for every allowed source sequence. Also
`B_R(u)<=4uK(F+uJ)<=4uK(F+J)`, proving (8)'s tolerance implication.

**Finite and adaptive quantifiers.** A finite nonempty set of positive
radii has positive minimum and maximum. The selection assertions now
follow by minimizing a finite set of explicit bounds. For the adaptive
assertion one must first prove completion, not assume it. At a currently
defined prefix, take any complete symbolic path in `mathcal F` extending
the policy's next chosen edge. The prefix of its exact baseline, and its
constants `C_k,h_k`, depend only on that prefix. Since `u<=r_all<=r_R`,
the preceding noncircular induction applies to the actual errors through
this next step, regardless of its later edges: the next pivot is positive.
Iterate this finite argument to complete the run. Only then call its
realized path `Rhat` and apply the fixed-path bound. Taking finite maxima
and then bounding each linear and quadratic coefficient separately proves
(9). No limit, tie margin or smooth policy is used. ∎

## Checks

Current status: **PROVED, analytic**, with distinct supplementary
independent mathematical reconstruction accepted. The saved L3a formulas
were retained without algebraic change;
the tolerance corollary and prefix-completion proof make acceptance and
adaptive nonbreakdown explicit. No code, numerical score evaluation,
experiment or scalar-rounding realization was performed.

The configured Astra high reviewer independently reconstructed the entire
proof at input SHA256
`cdcf4214a6ae251db66954baeb3cfce41a2c17340ab2a85220dfd988164c3a8a`;
the developer then read its complete L3 review and protocol section in
[independent-checks-frontier-04.md](../independent-checks-frontier-04.md).
All constants, radius/remainder steps, tolerance acceptance, represented-
input qualifications and adaptive prefix quantifiers passed. There was
no mathematical correction. The reviewer requested only sharper wording
distinguishing the proved finite-degree positive-radius acceptance from
degree-uniform usefulness. That scope clarification and this status/check
metadata leave the mathematical statement, constants and proof unchanged.

The uncommitted reviewed draft `cdcf...` cannot be reconstructed from
repository bytes. Claims above or in historical records that formulas
were unchanged describe the developer's account; they are not a
repository-verifiable comparison. Claude audit-01/L3 directly audited
the committed final input `d42f4e89795349c94e59209527e05f8b41039142bac4e78d8eed39e892768a96`
and accepted its mathematics. No new scientific execution accompanies this response.

## Depends on

PD-T142's residual-to-span certificate; PD-T143 supplies the
closest inverse-score criterion and its Hres quantifier limitation;
PD-T054 supplies staircase/admissible-path context. PD-T046 explains why
positive-pivot and local-product factors cannot simply be omitted. The
source gate and prospective claim/kill/verification are in
[ideas-l3-continuation.md](../ideas-l3-continuation.md).

## Sources

PD-T142/143 and PD-T054/046 are repository theory dependencies/context as
specified above. The projector identity, normalization inequality,
Neumann inversion and real-algebraic comparison are standard ingredients.
No new primary literature was read or priority claim made in this response.

## Scope

The bound is for the specified aggregate full-projection implementation.
An actual scalar or IEEE implementation needs its own finite-error
reduction, including loss of orthogonality and local source budgets;
first-order scalar certificates alone do not establish that reduction.
Hres alone permits arbitrarily large second-order terms, so this theorem
does not remove PD-T143's family dependence without changing hypotheses.
No degree-uniform useful radius, polynomial score/radius bounds,
acceptance at a prescribed error size or score filters uniformly in degree,
or efficient online theorem follows. Finite-degree acceptance at the
displayed positive radius is proved. Large inverse scores supply no drift
lower bound.
The finite adaptive argument supplies no (C)-based section interpretation.

Required later Claude scientific/protocol audit, final IDs and canonical
registry integration remain pending. In particular the previously disclosed
prospective-gate timing deviation is historical and is not cured by the
completed reading before this continuation. Supporting this finite-error
item does not upgrade L3's original broader safety target.

### Dated radius limitation — 2026-11-05 (audit-01/L3, L3-4)

The auditor derived `d>=sqrt(2)b`, so `1/(2b)` is redundant in (5).
For lambda_1>0 the auditor also derived the universal ceiling
`r_R<=5^(-(N-3)/2)/(4 sqrt(2) lambda_1)`; for lambda identically 1 this
is below 2^-53 for every s>=9. These are attributed consequences of this
frame-based majorant recorded by the independent audit, not a new
theorem or an alteration of (2)–(9). They explain why this majorant cannot
supply useful radii at higher degree. The original formula is retained,
including its conventions when budgets vanish. No radius ceiling is
asserted by division by lambda_1 when lambda_1=0.

## Open items

The broader unconditional selection target remains OPEN: useful
degree-uniform radii and polynomial scores, prescribed-u/filter acceptance
uniformly in degree, efficient online selection and an actual scalar/IEEE
finite-error reduction. PD-T143's Hres alone cannot yield this model's
uniform radius/remainder, because unconstrained second-order terms remain.
Final IDs and registry application await focused Claude re-audit and
PR preparation; AC's gate-timing decision remains open.

## History

- 2026-11-05, response to A-M1 / L3-1: original attempt wording
  "PARTIAL for the broader L3 target" and continuation wording
  "PARTIAL/OPEN" are superseded by OPEN. L3-01 is a PROVED supporting
  reformulation with a stronger per-column finite-error budget, not an
  explicit decomposition of the original target. Original "completes the
  handoff01 finite-u item" wording means only this reformulation; no
  uniform Hres-only version is established. Proof and displayed (1)–(15)
  are unchanged. Template, model-comparison and attributed audit-limit
  metadata answer L3-2–5 and L3-8; no status upgrade.
- 2026-11-05, A-P1/R2: L3a/L3b candidates and the constants (2)–(5)
  were drafted before the mandatory reading gate and first committed at
  `0574c47`. They survived unchanged according to the developer's
  historical account; the unretained draft limits byte verification as
  stated in Checks. Later completed gates preceded the proof and do not
  waive or cure the deviation. Acceptance is AC's decision. See
  [gate-timing-response-01.md](../gate-timing-response-01.md).

- 2026-11-05, handoff01: unchecked formulas first saved in attempts/L3 and
  ideas-l3-l4 before G0 stopped campaign development; the incomplete gate
  timing was explicitly disclosed. No proof or run was claimed.
- Handoff02: broad mandatory reading completed and G0 additively resolved;
  L3 stayed deferred while L4 proceeded. Handoff03 addressed L1/L2.
- Handoff04: full new relevant registry delta and closest sources read;
  prospective target/kill/verification recorded before new derivation.
  The proof above reconstructs the saved formulas in their stronger
  finite-error source model and includes an adaptive prefix-completion
  argument. Distinct Astra high reconstruction subsequently passed in
  full; after the developer read its durable report, status/check metadata
  and the degree-uniform scope wording were finalized. No formula changed
  and no scientific execution was required.

## Preparation errata — 2026-11-05

R2-1 erratum: every earlier L3 use of “stronger” in this file describes a different per-column zeroth-order finite-error budget: the model (1) error-family class neither contains nor is contained in Hres. It does not assert hypothesis inclusion or a uniform result over Hres alone. This qualifies each occurrence in: model-comparison prose; coefficient statement under model (1); supporting-reformulation History; saved-formulas reconstruction History.

R2-4 erratum: the complete pre-gate majorant system and constants are verifiable in `0574c47:topics/padua-lanczos-frontier-20261105/attempts/L3.md`; they match theory displays (2)–(5) and (7), up to the recorded notation changes. They survived unchanged. The unretained `cdcf4214a6ae251db66954baeb3cfce41a2c17340ab2a85220dfd988164c3a8a` caveat concerns only the intermediate reviewed draft, not that committed pre-gate draft.

## History addendum — 2026-11-05 (handoff10; A-P1)

This result descends from L3a/L3-01 explicit-radius majorant and L3b/L3-02 adaptive decision tree, drafted before completion of the mandatory reading gate and first committed at `0574c47`. AC accepted the disclosed deviation on 2026-11-05. The deviation remains permanently disclosed, not waived and not cured. Completed-gate receipt: G34: `aab7bbe`; G3: `844e812`; these are publication SHAs, not worker input/rules SHAs. The reported gate-before-development order inside shared publication `aab7bbe` is not established by Git. G3 and L3-01 share `844e812`; the reported gate-before-proof order within that commit is not established by Git. Earlier pending-decision wording is historical and is superseded by this dated acceptance record. See [gate-timing-response-01.md](../gate-timing-response-01.md).
