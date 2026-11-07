# N6 exact formulation gate

2026-11-05. Codex N6 mathematics developer, parent-assigned
gpt-6.1-sol xhigh; effective runtime metadata are not independently exposed.
Rules/input read at `98d6c00d8a474cf97602c9cfdea631a837191ac0`.
No external novelty or priority claim.

The global gate is [the delegated baseline](novelty-gate-baseline.md), whose
complete-registry scan and full obstruction/disposition-table reads apply
unchanged: the current `state/IDEAS.md` SHA-256 is still
`948c30b35cdb3ffacefe398acfb35439fc7e69f8be33fd94bc605b052b8d03c6`.
This worker additionally inspected the complete registry headings, aliases
and summary tables, and reread broad portions of those tables; the complete
global table reading is credited to the baseline scanner, not claimed as
an independent full reread here.

Own searches covered `state tracks topics literature -g '*.md'`, with
`generating.curve|lissajous|rank.one.lattice|rank.1.lattice|numerator.factor|convex.sum|common.factor|envelope|parallel.*curve|shifted.*curve`
(232 matching files, including the new bridge topic). A targeted search
also used `convex.hull|phase.*chord|two.*curves|diagonal.*translation|equal.*phase`.
No absence claim follows from these bounded searches.

Full mathematical records read before formulating a candidate:

- IDEA-206, complete IDEA-17 record in programme `ideas/candidates.md`;
- IDEA-319, original `alln/ideas.md` and canonical `FINAL_CANDIDATES.md` entry;
- IDEA-341 and342, complete effective `ideas/comparison-r4.md`;
- PD-N086, complete coarse-cell sign obstruction;
- PD-T101, complete corrected cardinal and rhombic-kernel proof;
- PD-T364, complete phase/reflection structure and scope, including its
  classification of the orbit formula as a routine inherited identity;
- alln fallback candidates, including the distinctions between O-R, O-L,
  E-C, E-P and direct pointwise comparisons.

`literature/INDEX.md` coverage warnings and the LIT-014/312/379/380 rows
and their dated addenda were inspected. No external fulltext is used,
no source theorem is transferred, and no fresh LIT ID is needed.

## Exact predecessor comparison

The route is a continuation of deferred IDEA-319/341. A covering family
and its one-variable restriction are only an identity variant of T101/T364;
their existence alone is not progress toward argmax. The proposed
family is

    Gamma_s(t)=(cos((n+1)t+s), cos(nt+s)),  (t,s) in (R/2pi Z)^2.

The angular matrix has determinant1, so its fibers, boundary behavior and
restricted degree can be stated exactly. The special trace s=pi contains
the two nonnode corners; this differs from bare s=0, whose failure to
reach them is already recorded in N086 and is not re-registered here.

A falsifiable extra comparison, independent of the desired constant, is
the two-trace bound

    lambda_n(Gamma_s(t)) <= max(lambda_n(Gamma_0(t)),
                                lambda_n(Gamma_pi(t))).       (C)

This is not an unrestricted envelope: both comparison points are fixed
explicitly by t, without optimization or use of Lambda_c. It would reduce
the square supremum to two fixed one-dimensional traces while preserving
the original cardinal sum. The first exact n2 rational/radical example
violating (C) kills only this comparison. A proof of the torus identity
without (C) does not survive as a new mechanism.

N086 does not already kill (C): it concerns each cardinal's sign on
coarse diamonds, whereas (C) permits all sign changes and sums complete
cardinals first. N079 still prohibits replacing each four-copy absolute
sum by the absolute values of its individual kernels as a final comparison.

Gate disposition before test: **variant with difference**, specifically
an operationalization of319/341 by the explicit family and comparison(C).
The family identity itself is **equivalent / verification**, with no new
registered theory claim planned unless a further distinct lemma needs it.
