# Supplementary obstruction audit: M1, M2 and gen2-3

Rules/source candidate: `614709d4a60fb0c2593b05764e8d5aceda1be381`.
Base main: `07c5f5465d6de306aa81dbe8ca1f615295163864`.
Auditor: independent Codex subagent `/root/audit_obstructions`; user-requested
`gpt-6-astra xhigh`, inherited by this subagent. The runtime does not expose a
separate resolved model/effort identifier. Date: 2026-11-01.

## Scope and coverage

Read AGENTS, WORKFLOW, Codex role; the full 423-line `state/IDEAS.md`, including
all disposition/obstruction tables; the full 83-line `literature/INDEX.md`;
the programme brief; the M1, M2 and gen2-3 adversarial records; corresponding
candidate/disposition entries and report rows; the consequential code rerun
below; and the normalized-pencil construction. No new candidate or novelty
claim is proposed. This is a bounded supplementary audit, not independent
approval of the entire campaign or its literature baseline. The source draft
files deleted before the candidate head were not reconstructed here.

The candidate snapshot preserves repository paths and is supplied by the root
orchestrator. Input SHA-256 values for the reruns are in
`obstructions-check.json`; the root's fetched-file manifest supplies GitHub
blob provenance. Developer files were not changed. All writes are new files in
this audit-support directory, and no Git operation was performed.

Primary-source inspection through the web connector on 2026-11-01:

- [Degani–Schiff–Tannor, arXiv math/0408076v1](https://arxiv.org/html/math/0408076):
  introduction and theorem/argument excerpts around Theorems 2, 3, 9–12 and
  compatibility equation 65. This independently confirms that positive-weight
  odd-degree cubature gives symmetric commuting extensions, that the converse
  requires compatibility, that its weights are squares, and that the rank
  lower bound is a published result. Coverage is selected excerpts, not a
  complete rereading of the paper or the 2005 journal version.
- [Kreuzer–Robbiano, arXiv 2503.01752v1](https://arxiv.org/html/2503.01752):
  introduction, Proposition 5.4 and Proposition 5.6 with its proof. For the
  planar simplicial order ideal, the published ideal chart is an affine space
  of dimension twice its colength. This supports the ideal-chart overlap; it
  does not prove a global orthonormal recurrence-entry chart with weights.

Other bibliography claims, Humet's local PDF and all cited papers not listed
above remain outside this supplementary primary-source verification.

## Findings requiring developer dispositions

### O1 — P2: restrict the pattern-commutant identification to its measured scope

Locations: `report.md:41`; `checks/adversarial-M2.md:35`;
`ideas/candidates.md:175` and `:177` already give the narrower measured reading.

The report places the finite Favard/dimension statement and
`commutant = span{I,Hx,Hy}` in one result row with a P status referring to
steps (a)–(g). Those steps do not prove the commutant assertion. The developer
script checks random instances only. The assertion is false if read over all
positive-pivot Padua/generalized-Hessenberg pairs.

Independent exact check: take the n=2 Padua points, in row order,

`x = [1,1,0,0,-1,-1]`,
`y = [1,-1/2,1/2,-1,1,-1/2]`,
`w = [1/12,1/6,1/3,1/6,1/12,1/6]`.

The determinant of the monomial Vandermonde in order
`1,x,y,x^2,xy,y^2` is `-27/2`. Exact weighted Gram–Schmidt gives commuting
real symmetric section matrices and positive recurrence pivots. Among the 17
symmetric variables allowed by pattern(Hy), the exact commutator map
`E -> [Hx,E]` has rank 11, hence kernel dimension 6, exceeding the
three-dimensional span. `obstructions-check.py` reconstructs this over exact
SymPy rationals/radicals; it records both matrices and the variable list.
Additional numerical checks on Padua n=2,...,7 gave dimensions
`6,8,9,11,12,14` in pattern(Hy), unlike the random instances' dimension 3.

Required response: separate the finite Favard/dimension claim from the
commutant observation, leave the latter MEASURED in the random finite scope,
and do not use it as a universal structural theorem. If a generic theorem is
desired, formulate and prove it separately. The exact Padua countercheck is
audit evidence, not a new registered PD-N.

### O2 — P2: the GL-orbit count does not exclude the normalized-pencil family

Locations: `checks/adversarial-M2.md:43`, `:52`; `report.md:43`;
`gate-rejected.md:104`–`:105`; `ideas/candidates.md:218`.

The dimension argument concerns all pencils obtained by arbitrary invertible
left/right changes of generators and syzygies for a fixed ideal. Under its
generic stabilizer assumption it can obstruct an orthogonal reduction of
that entire GL-gauged class to only 2N parameters. The candidate's tested
construction is narrower: `m2_pencil_conditioning.py:7`–`:11` and `:47`–`:83`
first choose orthonormal generators in a fixed Chebyshev coefficient inner
product, then orthonormal syzygies. These choices remove the additional
nonorthogonal gauge freedom before orthogonal equivalence is considered.
The resulting family modulo O×O is already determined by the 2N node
coordinates. Local smooth choices of the two orthonormal bases exist.

Consequently the unrestricted orbit count does not prove that a compact
unitary staircase description of this normalized family is impossible. This
audit does not establish such a staircase or any numerical advantage. The
measured conditioning comparison and the literature-based programme
assessment can stand with their stated scopes, but the recorded blanket
normal-form refutation does not follow from the argument provided.

Required response: state the unrestricted-gauge theorem's hypotheses and
limit the negative conclusion to that class; retain the normalized-family
normal-form question as unproved, or give an obstruction that applies to it.
Likewise do not replace the draft's explicit >1000 Padua sensitivity kill
threshold with "never better than the pair" and call the former refuted:
the developer itself says that threshold did not fire.

### O3 — P2: transfer only the failed inertia formula and explicit pair class

Locations: `checks/adversarial-gen2-3.md:99`;
`ideas/candidates.md:197`–`:199`; transfer interpretation of `report.md:37`.

The cluster example and its square-root scaling are sound for the
symmetrised-product count and the broad symmetric banded class. They do not
show that every delta-only certificate fails, nor establish the same
negative theorem for pairs produced by the positive-pivot recurrence
algorithm. The N=38 construction is a direct sum with a 2x2 cluster; it is
reducible with noncyclic constant vector and is not of size dim(Pi_n). The
N=45 rotated-eigenbasis construction generally destroys the recurrence
pattern. These are valid tests of the broader claimed hypothesis class,
but neither supplies the missing transfer into the narrower computed-section
class. Other count objects in the developer's own experiment stayed correct.

Independent exact reconstruction of the tested mechanism: let
`Hx=diag(0,e)`, `Hy=R diag(0,e) R^T`, with R a 45-degree rotation, and use
the box `(-e/10,1)^2`. Put `a=e/10`, `b=11e(1-e)/10`. The two quadratic
box matrices are orthogonally conjugate with eigenvalues a,b. Their
symmetrised product has determinant

`-(a+b)^2 (a^2-6ab+b^2)/16`.

For `0<e<=1/10` this is negative, so its positive inertia is one, although
both reference cluster points lie inside the box and each quadratic matrix
has positive inertia two. The proposed formula returns 3/2 rather than 2.
The commutator norm is `delta=e^2/2`; the boundary distance `e/10` therefore
has square-root scale. The exact determinant checks for five rational e
values are stored in the independent checker. This reconstructs a restricted
method failure without relying on a fitted exponent or a cited source's
sharpness claim.

Required response: use a title such as "symmetrised-product inertia count
can fail at square-root commutator scale for symmetric banded pairs" and
state the reference pair, noncyclicity and pattern limitations. Do not
allocate or transfer a broad computed-section PD-N without a reduction or
example satisfying its actual hypotheses.

### O4 — P2: word-order dependence does not exclude all specified-lift bracketing

Locations: `gate-rejected.md:40`; `checks/adversarial-M1.md:43`.

The rerun confirms the word-order and lift dependence and hence the absence
of an automatic commutative polynomial calculus for the sections. This does
not imply that no bracketing theorem exists once a lift/function class is
specified. The same record exhibits a specified positive lift and reports
196–200 successful brackets out of 200 finite instances; this is neither a
general theorem nor a universal refutation. Its next sentence that
univariate Lanczos wins for every larger k extrapolates from k<=4 and a
comparison of exactness degrees, which alone does not order approximation
errors for every function/measure.

Required response: limit the rejection to an unspecified/lift-independent
functional and the finite tested claims; retain the known words/anti-Gauss
identities and DST overlap. A fixed-lift theorem remains a different,
unproved question; no proposal need be revived merely for this correction.

## Additional minor precision correction

`checks/adversarial-M1.md:33` and the summary in `ideas/candidates.md:365`
call positive first-component weights automatic from real symmetry. Squares
give nonnegative weights. Strict positivity needs cyclicity/nonzero overlap
with the constant vector, or removal of zero-weight modes. Appending a
decoupled simultaneous eigenvector to any compatible extension gives a
zero-weight mode while preserving symmetry, commutation and compatibility.
The independent checker records the elementary diagonal example with weights
`[1,0,0]`. This does not invalidate DST's cubature implication; it corrects
the exact node-count/strict-positivity wording.

## Checks completed and interpretation

Command from the snapshot root:

```sh
python topics/programme-ideas-20261031/audit-support/obstructions-check.py > topics/programme-ideas-20261031/audit-support/obstructions-check.json
```

This independently executed all three developer scripts in subprocesses
with one BLAS/OpenMP thread, preserving stdout/stderr and input hashes:

- `m2_favard_commutant.py`: tangent dimensions 29/44/62/83 and
  39/64/97/139 reproduced; random pattern commutants 3/2/3 reproduced;
  joint-eigenvector residuals at most 1.7e-15.
- `m1_word_rule.py`: words through 2k+1 reproduced to <=4e-16,
  order dependence at the next degree reproduced, anti-Gauss error flips
  reproduced to <=9e-16 at both tested lengths; the finite functional
  comparisons matched the printed developer results.
- `t3_delta_exponent.py`: cluster wrong counts reproduced, including
  N=38, delta=5e-7, boundary distance 2e-4, numerator 7 rather than 8.

Independent implementations in the audit wrapper additionally check the
rational cluster determinants, exact n=2 Padua pattern-commutant dimension,
and a zero-weight commuting pair. Environment: Python 3.12.14, NumPy 2.3.5,
SciPy 1.17.0, SymPy 1.14.0, Linux x86_64. The wrapper's first attempted run
had a wrong local root-parent index and failed before executing any
developer script; this was corrected before the recorded successful run.

The finite Favard argument independently reconstructs correctly on the
explicit nondegenerate positive-pivot graded-pattern class: polynomial
recursion makes the constant vector cyclic, joint eigenspaces are simple,
weights are strictly positive, and the weighted Vandermonde is invertible.
The node/normalized-weight count gives 3N-1; the degree-block orthogonal
gauge count gives the stated additional binomial term on that nondegenerate
class. This should be preserved with exact hypotheses and durable result
format if the developer elects to retain it as a scientific by-product.

This audit finds no reason to demand a surviving programme. It does find
unsupported negative/status statements that must be corrected even when
the administrative decision to abandon the programme remains justified.
No independent Möller-extension optimizer, large pencil-conditioning run,
Humet fulltext rereading, or external branch handoff was performed here.

Suggested next prompt: `Claude (Fable 5.1 xhigh): Continue claude/programme-ideas-20261031 — respond to the Codex audit findings with scoped claims and durable evidence.`
