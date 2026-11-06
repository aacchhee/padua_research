# Padua-type points in three dimensions — development report

2026-11-06. Branch `codex/padua-3d-20261106`,
[draft PR #33](https://github.com/aacchhee/padua_research/pull/33).
Coordinator: Codex, assigned gpt-6-astra high. Worker models, input SHAs,
execution history and limitations are recorded in [LOG](LOG.md).
All IDs remain provisional. The original development account below is
historical; the dated audit-response addendum supersedes its audit, gate,
selection and attribution wording.

## Main outcomes

**No total-degree 3-D interpolation family with a proved polylogarithmic
Lebesgue bound was found.** The campaign produced a restricted-class
nonexistence theorem, an unexpected instability theorem for a natural
baseline, a sharp fixed-grid cubature obstruction, and an explicit
reconstruction of a known universal lower bound.

1. **Single reflection-invariant torus cosets are excluded, for every n>=2.**
   If the whole finite coset A=a+H in T^3 is preserved by negating any one
   coordinate, its cosine image cannot be both Pi_n-unisolvent and have
   binom(n+3,3) nodes. No cubature or orthogonality assumption is needed.
   The proof classifies the possible coupling by binary codes, then uses
   short-axis and Chebyshev-alias obstructions before exact node counting.
   It admits 2-D Padua points and a degree-one 3-D exception.
   [Classification](theory/t1-reflection-classification.md),
   [obstruction](theory/t1-minimal-obstruction.md).
   Arbitrary cosine images, noninvariant cosets and unions of cosets remain
   outside this theorem; the original [C_k target stays OPEN](theory/t1-open-class.md).

2. **Monotone Padua-plane stacking has at least exponential growth.**
   Put Pad_{n-k} on z_k=cos(k*pi/n), k=0,...,n. This is unisolvent for
   every n, but its continuous cube Lebesgue constant satisfies

       liminf log Lambda_M(n)/n >= 3*zeta(3)/(2*pi^2) > 0.

   Thus no fixed polynomial upper bound holds for this ordering. An exact
   Newton block determinant and a comparison with the mean over all height
   permutations give the proof. The unisolvence/determinant statements hold
   for every distinct-height ordering; the exponential conclusion is proved
   only for monotone order (and its reflection).
   [Unisolvence](theory/t4-stack-unisolvence.md),
   [determinant](theory/t4-stack-determinant.md),
   [lower bound](theory/t4-monotone-lower.md),
   [coarse exact-greedy upper bound](theory/t4-stack-upper.md).

3. **A 27-point Gaussian grid cannot be positively thinned to 20 nodes
   while retaining degree-five Chebyshev cubature.**
   On G={-sqrt(3)/2,0,sqrt(3)/2}^3, every exact degree-five weight vector is
   w_x(t)=(1+t product_j T_2(x_j))/27. Nonnegativity is equivalent to
   -2<=t<=1. The sharp positive support minimum is 21; the sharp signed
   minimum is 15. This is a hand proof for arbitrary weights on that fixed
   support, without a symmetry assumption. A separately verified positive
   14-node rule outside G shows why the restriction matters.
   [Sharp support theorem](theory/t5-gaussian-grid-obstruction.md).
   [All-q commutator-rank formulas](theory/t5-chebyshev-section-rank.md)
   reconstruct the known necessary completion bound; they do not decide
   compatibility or attainability of a commuting completion.

4. **Every unisolvent total-degree cube set has a logarithmic-cubed lower
   bound, with a fully explicit local certificate.** For n>=2,

       Lambda(X) >= max(1, H_floor(n/2)^3/(648*pi^3)).

   Here H_m=sum_{j=1}^m 1/j. The local proof calculates the cosine-lift
   translation multiplier, corrects it with a norm-at-most-27 operator,
   and uses an explicit bounded sawtooth test for the octahedral Fourier
   kernel. **The universal logarithmic order and factor 3^-d comparison
   are already in Subbotin (1983).** No historical novelty is claimed for
   them or for the displayed coarse constant.
   [Projection comparison](theory/t6-universal-lower-bound.md),
   [Fourier bound](theory/t6-fourier-lower-bound.md),
   [primary source coverage](literature-T6.md).

## Positive construction screen and best tested families

T2 sampled unshifted cyclic cosine orbits with N=binom(n+3,3), M=2N-1,
and a unit first generator coordinate. Exact product-to-sum gives an
integer folded-frequency matrix describing the **actual algebraic cosine
nodes**, rather than random generic axes. The canonical
[rank reduction](theory/t3-cyclic-rank.md) and
[degree-valid short-relation polynomials](theory/t3-short-relations.md)
are analytic known-mechanism prerequisites.

Three preregistered generator formulas failed at n=2 by explicit quadratic
annihilators. A subsequent exhaustive normalized screen found four
full-rank cases at n=2, none among 171 generators at n=3, and four at n=4.
The compact cubic null cover and a separate full-Laurent checker are
committed and were actually rerun by a distinct checker, who additionally
reconstructed all witnesses by Fraction convolution. The
[normalized finite obstruction](theory/t2-normalized-screen.md) and
[extension to every unshifted order-39 generator](theory/t3-degree3-extension.md)
are therefore PROVED computer-assisted finite statements, with their
arithmetic trust and source identities recorded. The other detailed rank
distributions and all quality values remain MEASURED.
These results exclude neither even-degree subsequences nor shifted or
corrected samples.

The following are **MEASURED maxima on the same 21^3 Lobatto mesh**, not
certified continuous maxima or growth laws. The QR reference is extraction
from a tensor Lobatto mesh, not the literature's curve-specific extraction.

| n | Best tested cyclic orbit | Monotone stack | Alternating stack | Leja-height stack | Leja lower-set reference | QR reference |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 7.05326 | 13.6667 | 6.06066 | 6.06066 | 7.00000 | 7.00000 |
| 3 | singular in normalized class | 54.4706 | 12.8401 | 12.8401 | 13.1747 | 8.32067 |
| 4 | 37.4870 | 253.793 | 29.5126 | 18.5994 | 19.4982 | 11.2449 |
| 5 | not run | 1490.56 | 66.0962 | 33.5400 | 26.3366 | 13.8575 |
| 6 | not run | 8902.40 | 160.305 | 44.2656 | 40.2764 | 22.1915 |
| 7 | not run | 56185.9 | 373.415 | 51.7598 | 49.8126 | 26.9351 |

The best n=4 cyclic value belongs to z=(1,21,29), with the equivalent
near tie (1,15,19); neither beats either control. The best registered stack
at n=4 is the Leja-height ordering, but it loses to the QR reference and
later loses to the Leja reference twice consecutively. None passes D2's
promising gate. No growth fit is promoted from these short killed screens.
Actual solve residuals, condition numbers, selected nodes, commands and
scope are in [T2](attempts/T2.md), [T4](attempts/T4.md) and their receipts.

## Gate outcomes

| Gate | Development verdict | Scope |
|---|---|---|
| D0 | PASS | Exact PD-T082/093 controls, two PD-N037 rows and both references, 2-D ranks through 10 and four-corner identities through 8 |
| D1 | PASS | Actual-node rank lifting distinguished from generic-axis witnesses; original numerical controls reproduced |
| D2 | No promising family | Three fixed cyclic formulas killed at degree 2; all three stack orderings killed at degree 7; finite cyclic survivors lose quality comparisons |
| D3 | PASS for the stated bounded class | 20,304 3-D reflection-invariant cosets with coordinate projection orders <=12, 450 2-D cases with orders <=10; separate all-degree Padua escape proof and finite n<=10 sanity |
| D4 | PASS | Known exact degree-five 2-D/3-D rules reproduced before any support obstruction |

Preregistrations and distinctions between finite evidence and hand proofs
are in [gates](gates.md). Actual supplementary independent checks are
recorded in [mathematical reconstruction](independent-checks-math.md) and
[computation/stack/cubature reconstruction](independent-checks-computation.md),
with separate small receipts and additional independently written code.
Claude's substantive audit remains a separate required step.

## Directions, budgets and expectations

Budgets were ceilings. Each completed round delivered a theorem, a sharper
bound, a certified finite property or a gate verdict; the ledger is
[rounds](rounds.md). No ultra escalation, remote compute campaign or large
degree sweep was needed. No killed family was rescued by changing its
definition after the run.

| Direction | Outcome / remaining boundary |
|---|---|
| T1 | Restricted-class all-n obstruction; arbitrary C_k/weights remain OPEN |
| T2 | Concrete cyclic formulas rejected and finite design space diagnosed; phase/coset-union/correction routes deferred until a separated construction removes both alias and quality defects |
| T3 | Exact prerequisites delivered; all-n surviving-family proof remains blocked on D2 |
| T4 | Proved baseline and monotone instability; other orderings' asymptotic rates remain OPEN |
| T5 | Exact pipeline and sharp fixed-grid theorem; nonlinear completion minimization explicitly unexecuted/deferred, general minimal cubature OPEN |
| T6 | Known universal order verified in primary literature and reconstructed locally with an explicit constant; matching construction OPEN |

BRIEF E1 gains support only for the reflection-invariant single-coset
subclass, not the whole conjectured class. E2's polynomial expectation is
refuted for monotone stacking; its statements about other orderings remain
open. E3 found no promising family in the tested cyclic slice. E4 was not
tested by a complete union/correction screen and remains a judgment.
E5 is unresolved globally; the fixed-support theorem does not settle it.
E6 is confirmed as an established literature fact, not a newly open problem.

## For a paper

The elementary reflection-coset theorem and the monotone-stack exponential
lower bound are the strongest candidates for a short structural note,
subject to the independent audit and a targeted fulltext novelty comparison.
The fixed-grid support theorem is a useful finite cautionary example;
the universal lower bound is known background with an explicit local proof.
This is not a paper claiming a 3-D Padua construction, a universal lattice
obstruction, or the Li–Sun–Xu cubature conjecture. Historical novelty and
publication suitability remain unresolved.

The next step is the substantive Claude audit of the pinned complete batch,
including independent reruns and the retained failed/deferred candidates.
No merge or final-ID allocation is requested at this development boundary.

## Audit-response addendum — 2026-11-06

[Claude audit01](audit-01.md) accepted all original mathematical statuses,
including both cubic computer-assisted upgrades. It returned five MAJOR
record/gate findings and fifteen MINOR items. [Response01](response-01.md)
records their dispositions; PartA material changes require a focused Claude
re-audit. [Handoff04](handoffs/04-work.md) also assigns new T7–T9 research.
The PR remains a draft, with no final IDs or shared-registry edits.

- T1's hypothesis is invariance under **each** coordinate reflection.
  DMVX2009 (LIT-306/322) is the nearest parity-grid/node-excess comparator.
  The local theorem classifies all admitted codes, orders and half phases
  without cubature. Historical novelty and suitability for a structural
  note remain unestablished. T5's 16-node same-parity control is DMVX's rule.
- D3(b)'s old capped enumeration was only partial coverage. The new
  [full-class diagnostic](evidence/t1-full-enum.json) covers n2..6 at m_j<=2N:
  636,1392,757,2520,4803 target-count cases, zero necessary-screen survivors.
  This is not an unperformed rank computation or the proof of the all-n theorem.
- Exact [survivor symmetries](evidence/t2-symmetry-check.json) give two node
  sets per successful degree. At n4, (1,15,19) and (1,21,29) are equivalent,
  with exactly equal mesh maxima; the tiny numerical gap is rounding.
  The preregistered lexicographic choice is **(1,15,19)**. The other class
  is (1,11,15)~(1,25,30); at n2, (1,3,7)~(1,4,6)~(1,5,8).
  Counts36/171/561 reduce to18/100/301 classes, a finite MEASURED result.
- The cubic obstruction leaves every degree sequence omitting n3 open,
  including odd degrees n>=5, as well as other moduli and phases. Missing
  variant dispositions and concrete resume conditions are preserved in
  [candidate retention](candidates-response-01.md) and
  [deferred routes](candidates-deferred-response-01.md).
- Subbotin's Russian original is1982, English translation1983. Attribution
  rests on the developer's recorded primary reading; Yudin's prerequisite
  was unread, and neither supplementary Astra nor Claude independently
  opened Subbotin. The accepted local analytic proof is separate. T6-01
  is a literature duplicate retained as a local reproof. The displayed
  harmonic lower term exceeds1 only near n=7.2e11; at practical degrees
  it gives only Lambda>=1. The producer multiplier sanity is tautological;
  audit01's actual-projection check is separate evidence.
- Short relations now use **PD-T?padua-3d-20261106-codex-T3-02**. The old PD-N alias
  is retained only as provenance; the accepted statement/status is unchanged.
  Full provisional namespace mappings will be applied at PR preparation.

The original T2 gate-timing deviation, unexecuted T5 completion probe,
historical model-attribution correction and unused original budgets are
preserved once in [canonical deviations](response-deviations-01.md).
AC's acceptance is not presumed. The new gates do not repair old chronology.

## Handoff04 completed development — 2026-11-06

The [continuation report](report-continuation-04.md) supersedes this report's
historical next-step language. T7 supplies the general-H/phase reduction,
an exact shifted rank-two cubic survivor and its all-weight quartic cubature
obstruction. T8 finds the unique finite cubic M38 class, proves the all-phase
M10 obstruction and stops a prospectively chosen odd-degree continuation
after measured quality losses. T9 proves Lambda>=3/4+3/(2pi)>1.2274 at
every n>=1 and the leading log³ lower coefficient1/(24pi³),27 times the
earlier local explicit coefficient. The Haar packing threshold remains
CONDITIONAL; refined numerical maxima and fits remain MEASURED.

The matching minimal-node polylogarithmic construction is OPEN. New results
and PartA material fixes pass next to Claude; the original accepted T1–T6
theorems are not reopened. Provisional IDs and source-reading limits remain
explicit, with no shared-registry application or merge request.

## Audit02 response clarification — 2026-11-06

The assigned completed-section n<=4 optimization was not executed; the
exact uncompleted-section census does not replace it. Earlier garbled
"not an unperformed rank computation" wording is superseded here.
The historical direction-wide stop decisions are withdrawn under C1;
handoff06 resumes their untried routes. Full provisional IDs use the
padua-3d-20261106 slug; abbreviated old-slug IDs are historical aliases,
not separate allocations. C4's scoped negative mappings and the response
are in response-02.md; no accepted positive reduction is removed.
