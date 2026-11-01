# Audit-02 support: retained Ritz bound, parity refutation, rational-window negative

Audited source/rules SHA: `cadb35066160e466cb1704b9791ad6f374446422`.
Auditor: independent Codex supplementary agent; user-requested/inherited `gpt-6-astra xhigh`. Runtime model/effort metadata are not independently exposed. Root alone controls Git. This agent changed only new `audit-02-support/rejections-*` artifacts; developer sources and audit-01 are untouched.

Scope: PD-T?programme-ideas-claude-02; PD-N?programme-ideas-claude-02 and -03; response-01 A2, A5.3/A5.4 and A9.5/A9.6; corresponding summary/disposition corrections; OPEN_TARGETS B1/B4 as open formulations. This is not acceptance of the full response, manuscript, or other new proofs.

## Verdict

The one-sided Ritz theorem and the general parity-cancellation theorem are mathematically accepted under their written hypotheses. The exact grid examples reproduce. The rational-window record correctly retains MEASURED status, limits the failure to tested implementations/settings, and leaves other algorithms unexcluded. A2, the assigned portion of A5, and A9.5/A9.6 are resolved in the operative report and source annotations.

Two minor wording/formulation points remain below. Neither exposes a gap in the retained one-sided bound or parity proof.

## Independent reconstruction

For PD-T?…-02, the kernel has norm squared `K(B,B)>0`, because constants belong to Π_k and the positive inner product is nondegenerate. Reproduction gives `sum_C w_C K(C,B)^2=K(B,B)` and hence `0<s(B)<=1`. Removing the B term and using coordinate diameter 2 bounds the squared norm of `(x-x_B)K` by `4K(B,B)(1-s(B))`. Orthogonal projection is contractive, and its coefficient vector is `(H_x-x_B I)` times that of K. Dividing by `sqrt(K(B,B))` proves the bound in any real orthonormal gauge; the y argument is identical. Normalizing the total mass of μ is unnecessary, since common weight scaling cancels in s and in the section pair.

For PD-N?…-03, central symmetry makes the kernel representer of evaluation at the origin even, by uniqueness of the representer and unitary invariance under `p(z)->p(-z)`. For an even test polynomial, the product `xKp` is odd and integrates to zero. For an odd test polynomial in Π_k, with k even, its degree is at most k−1, so `xp` remains in Π_k and reproduction gives `<xK,p>=<K,xp>=(xp)(0)=0`. Thus the projection of xK vanishes; likewise yK. No coordinatewise reflection symmetry, product structure, equal weights, or preferred orthonormal basis is required. Injectivity on Π_k supplies the nondegenerate inner product and unique reproducing kernel. The submitted statement includes that hypothesis. The result is analytic; exact scripts verify instances rather than replace the general proof.

The general no-universal-lower-bound conclusion follows from an instance with `s<1`; the 5×5 k=2 case supplies exactly that, with `s=27/175`. It does not require every symmetric measure to have `s<1`.

For PD-N?…-02, the new status and scope correctly distinguish dense reference-block experiments in floating point, tested recurrence instabilities, and unproved universal algebraic statements. Its negative disposition is `failed` for the tested mechanism; alternatives explicitly retained include Givens IEPs, selective/partial reorthogonalisation and pole-cancelled candidates. The frozen submitted producer code has not materially changed; the actual primary-setting audit-01 rerun remains applicable, with its separate version-dependent outputs recorded. No additional long recurrence/approximation sweep was needed for this scope-only response.

## Minor corrections

**R2.1 — distinguish parity cancellation from failure at every centre.** N03 line 34 says the converse's negation is established "for every centrally symmetric node set"; response-01 addendum line 125 and OPEN_TARGETS line 84 similarly say the converse fails at every centre. The valid universal statement is **zero residual at every such centre**. A positive-deficit lower bound is contradicted only when `s_k(0)<1`. For example, with equal weights on

`{(0,0), ±(1,0), ±(0,1), ±(1,1)}`

Π₂ is injective, but the origin is already saturated: `s₂(0)=1`. Indeed `1-x²-y²+xy` is its cardinal function. Both residuals vanish, consistently with either side of the inequality. The exact independent checker below verifies injectivity and `s=1`. The formal N03 Statement (lines 10–14) already makes the right distinction, saying cancellation holds whatever s is and using an explicit unsaturated instance to refute the universal bound. Align the rejection-reason/summaries with that statement. Likewise OPEN_TARGETS B4 line 71 needs an exclusion of **unsaturated even-degree symmetry-centre cases**, not a categorical exclusion of all symmetry centres (odd-degree or already saturated centre cases are not ruled out by this proof).

**R2.2 — make B1's finite-dimensional domain explicit before development.** OPEN_TARGETS line 39 is correctly presented as an unproved target, with "proof or counterexample" as completion. Its proposed statement should explicitly require all denominators through `ell_(t+1)` to be nonzero on the nodes and evaluation injective through Π_(t+1), or an equivalent full-dimension hypothesis on V_0,…,V_(t+1). The listed `dim W_t=t+1` alone does not specify the next block and a finite M cannot admit this dimension growth for all `t>=2`. Define the intended real/complex pole class and what "general position" includes. These are target-formulation notes, not a claim that the open lemma is true or false. No proof development of B1/B4 was undertaken in this audit.

## Actual independent executions

From `/workspace/programme-integration`:

```
PYTHONDONTWRITEBYTECODE=1 python -I topics/programme-ideas-20261031/checks/code/response-02/ritz_converse_parity.py > topics/programme-ideas-20261031/audit-02-support/rejections-developer-parity-replay.json
PYTHONDONTWRITEBYTECODE=1 python -I topics/programme-ideas-20261031/audit-02-support/rejections-exact-check.py > topics/programme-ideas-20261031/audit-02-support/rejections-exact-check.json
```

Environment: Python 3.12.14, SymPy 1.14.0; exact rational arithmetic. The developer replay is semantically identical to the committed JSON (`json.loads` equality asserted). It reproduces 5×5 k=2 `27/175`, 5×5 k=4 `541/1225`, 7×7 k=2 `11/147`, with both residuals exactly zero in all three cases.

The independently written checker uses rational monomial Gram matrices, weighted projectors, and normalized residual squares, and asserts projector idempotence/W-self-adjointness and the two upper inequalities **at every node** of each tested measure:

| Independent case | Degree | Origin leverage | Origin compressed residuals |
|---|---:|---:|---|
| equal-weight 5×5 grid | 2 | 27/175 | both 0 exactly |
| 9-node central-only symmetry, unequal positive weights, non-product directions | 2 | 2153617/13312597 | both 0 exactly |
| 7-node symmetric saturated-centre example above | 2 | 1 | both 0 exactly |
| asymmetric 7-node non-product positive measure | 2 | 175849/1215349 | nonzero; squared residuals satisfy the bound exactly |

The asymmetric example verifies the norm/saturation normalization in a case where cancellation is absent. These finite checks supplement the analytic proofs and do not claim new historical novelty or an asymptotic theorem.

## Reading and evidence identity

Read current AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md and templates/THEORY.md. Read the complete current `state/IDEAS.md` (496 lines), including charter/MZ/lattice/programme disposition and obstruction tables; the new campaign registry entries point to the appropriate retained claims and provisional statuses. Read the three scoped theory files in full, response-01 and its addendum, OPEN_TARGETS, the new developer exact checker/output, and operative report/source corrections for A2/A5/A9. No novelty gate exemption is claimed for this negative-result audit. No new programme/mechanism was generated and no literature priority clearance was made.

Input blob identities, SHA-256 hashes, sizes and audit artifacts are recorded in `rejections-manifest.json`. No external archival receipt or cold-storage completion is claimed. The support artifact is for the root's audit-02 integration; only the root can set the full topic's disposition.
