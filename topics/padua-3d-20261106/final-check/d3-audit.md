# D3 supplemental independent audit — 2026-11-12

Reviewer: Codex supplemental agent, assigned gpt-6-astra xhigh. Provider
metadata beyond the assigned model/effort is not independently exposed.
Rules read at `4ab7e93ee19d60c5cfbf3626a23e43fd871a38ef`: AGENTS,
WORKFLOW and CODEX; handoffs 19 and 18. No Git operations or developer
file edits. This is **not the required formal Claude acceptance**.

## Verdict and scope

**PASS within the finite D3 statement.** No unresolved mathematical
finding was identified. The separately executed frozen checker and an
independent rational-interval reconstruction support the existence of
20 distinct interior nodes, positive precision-five weights, cubic
unisolvence, and exclusion from the cosine image of a single translated
finite torus subgroup. The workflow's independent-rerun obligation is
now discharged for these pinned inputs. Formal cross-agent-family audit
and repository integration remain the coordinator's work.

This does not verify an all-degree construction, optimality, or a
continuum Lebesgue bound. The floating quality receipt concerns the
rounded center; `final-d3/measurements.md` correctly excludes certified
transfer to the exact root. No new mechanism or priority is claimed.

## Pinned inputs and actual commands

The producer protocol was published at `db8c3cc`. Audited input hashes:

| File relative to topic | SHA256 |
|---|---|
| code/fd3_certify.py | b8ca61f9c46610f20e81ea234ae6a583b3003095947317951d74cf72fbd780db |
| evidence/fd3-certificate.json | 3677318c6dcf793f256750c0f270eb9be8eaa1143534428fcc096e497aa18a7d |
| final-d3/theory.md, read version | dfc95cd7aaa781a64c70e2d84e9caf0c163f261a372a5128eb772e21044b1b1c |

Executed from `/workspace/padua_research`:

```sh
timeout 120s python -B topics/padua-3d-20261106/code/fd3_certify.py check --certificate topics/padua-3d-20261106/evidence/fd3-certificate.json --receipt topics/padua-3d-20261106/evidence/fdc-d3-independent.json
timeout 120s python -B topics/padua-3d-20261106/code/fdc_d3_audit.py
```

Environment checked explicitly: CPython 3.12.14, `sys.flags.optimize=0`,
`__debug__=True`. No `-O`, no `PYTHONOPTIMIZE`-enabled execution. Frozen
replay elapsed 0.20095 seconds; final independent reconstruction elapsed
4.41278 seconds (measurements, not performance guarantees). An earlier
4.34618-second reconstruction preceded adding the independent modular
determinant checks; the final receipt supersedes that audit-only run.

| Audit artifact relative to topic | SHA256 |
|---|---|
| evidence/fdc-d3-independent.json | 452f16689dedfb597c102661da937960cf7b855514aab9a2bb759771bc33d08b |
| code/fdc_d3_audit.py | a19d8a913247ccf806df986f9e73c4d7c36a8ee22b36c595e40c7c49809db914 |
| evidence/fdc-d3-rational-audit.json | 34f5f23938dc9c2f5a1a1e10c0f9baf94afdf022194597c630ead15ff47882b7 |

No producer search was repeated. The independent script reuses the
frozen checker's matrices only as **untrusted preconditioner proposals**;
its residuals, derivative intervals, matrix defects and inequalities are
recomputed with exact Fraction arithmetic. Agreement of proposal matrices
is never an assumed accuracy result.

## Reconstruction of the finite proof

1. **Measure and indexing.** The x-to-angle substitution sends normalized
   arcsine measure to uniform angle measure on [0,pi]. Its even moment
   recurrence is M_(k+2)/M_k=(k+1)/(k+2), with odd moments zero. This
   independently reproduces every `moment(alpha)` through degree five.
   The product/filter enumeration independently gives 56 monomials of
   total degree at most five, and 20 through degree three, in exactly
   the checker's order. F=0 is therefore the full required cubature
   system, including mass one, not a subset of equations.
2. **Square restriction.** The certificate has 80 centers, 56 distinct
   active indices and 24 fixed coordinates. All weights are active.
   The inactive node coordinates remain exact dyadics, rather than
   being allowed to drift during root certification. Each active
   variable has radius 2^-100 about its denominator-2^180 center.
   Strict positivity, open-cube containment and all 190 node-pair
   separations are exact endpoint comparisons.
3. **Enclosures.** The frozen checker uses integers scaled by 2^256.
   Signed Python floor division gives downward lower bounds; negated
   floor of a negated numerator gives upward upper bounds. Four-corner
   multiplication, sign-selected linear combinations, and the explicit
   monomial derivatives give inclusive interval enclosures. The audit
   implementation instead uses exact rational endpoint powers (including
   the even-power zero case) and direct derivative monomials. It verifies
   inclusion of its independently computed residual, center Jacobian,
   box Jacobian and box Vandermonde in the production intervals.
4. **Root, not just residual.** For rational R, q bounds the infinity
   norm of I-RJ throughout the 56-dimensional box, and z bounds RF(c).
   The accepted inequalities q<1 and z+q r<r make T(y)=y-RF(y) a
   contraction from the closed convex box into itself. The derivative
   mean-value integral remains enclosed, so Banach's fixed-point
   argument applies. At the center, I-RJ(c) has norm below one;
   consequently RJ(c), and hence the square matrix R, is invertible.
   Thus the fixed point solves F=0. The result asserts uniqueness only
   on this fixed-coordinate slice.
5. **Exact rank and transfer.** The production modular elimination was
   inspected. The audit uses a different normalized-row elimination
   on exact rational central monomials, verifying primality by trial
   division: determinants are 60293 mod 65537 and 80489 mod 1000003.
   Nonzero reduction implies nonzero rational determinant because all
   denominators are powers of two. Independently, q_V<1 proves every
   V in the interval box invertible: R_V V has a Neumann inverse, so
   square V is nonsingular. The true root, not merely the center, is
   therefore Pi_3-unisolvent.
6. **Nonlattice property.** Fixed flattened coordinates 0 and 3 lie
   on the same axis and remain fixed at the true root. Their rational
   D=(1-a^2)(1-b^2)>0 is nonsquare and 4ab is nonintegral. Each
   2ab +/- 2sqrt(D) has degree two and rational minimal polynomial
   t^2-4ab t+4(a^2+b^2-1). A degree-two algebraic integer has integral
   trace, so neither value is integral over Z. If either corresponding
   angle sum or difference were a rational multiple of pi, that value
   would be a sum of two roots of unity, hence an algebraic integer.
   In a single coset of a finite torus subgroup, differences of lifts
   are torsion in every coordinate; folding cosine can only select
   signs. It would force one of these angle sums/differences to be
   rational in units of pi. This contradicts the exact pair witness.
   No exclusion of arbitrary unrelated coset unions is inferred.

Both implementations verify the displayed rational bounds
q<3/10^17, z<4/10^55 and q_V<2/10^17. The frozen integer numerators
agree exactly with the producer receipt. This is an exact finite
certificate with a proved reduction, rather than a floating root fit.

## Negative controls and residual risk

The audit script changes one property at a time in an in-memory copy of
the pinned certificate. All four mutations are actually rejected by the
normal-interpreter frozen checker:

| Mutation | Intended challenged predicate | Observed result |
|---|---|---|
| Add 2^-20 to the first weight center | Moment self-map | AssertionError |
| Set first weight center to zero | Positive box | AssertionError |
| Put fixed coordinate 0 at +1 | Open-cube containment | AssertionError |
| Repeat an active coordinate index | Square restriction schema | AssertionError |

**NOTE — execution boundary.** The frozen checker implements acceptance
predicates with Python `assert`; optimized Python disables those predicates.
Only normal CPython executions are accepted here. The independent script
uses explicit runtime failures and requires optimization zero. No claim
is made for `python -O`, and no optimized-interpreter result was used.

Trusted dependencies are CPython integer/Fraction semantics, the reviewed
finite algorithms and standard contraction/Neumann arguments. Decimal
elimination only proposes R matrices. NumPy, SciPy and mpmath search
accuracy is not a proof dependency. The supplemental script independently
checks the decisive arithmetic but shares the mathematical monomial
reduction; this is not a formal proof-assistant verification.

## Novelty-gate scope

This D3 audit verifies a frozen finite instance of inherited C7/S1,
IDEA-029/120, and standard interval-Newton/rank machinery. It generates no
new mechanism or novelty claim; that is the finite-verification exception
to a fresh mechanism-generation gate. The separate D1 audit reads the
complete current IDEAS registry and relevant predecessor/source records.
No consequence here upgrades the open all-degree interpolation target.
