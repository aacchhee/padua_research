# PD-T?padua-3d-20261106-codex-T7-R06-n2 — complete all-phase n2 coset census

ID kind: PD-T. Aliases: minimal10-node finite cosine-coset classification.
Status: PROVED, computer-assisted finite classification. Analytic finite
reductions, committed regenerating checkers and compact witness receipt,
actual distinct full replay and an independently implemented full census
are all present. Split from/into: none. No priority claim. The canonical
round06 gate retains its dated reading-coverage qualification.

## Exact statement

For every finite subgroup H≤T³ and every real a, let X=c(a+H), with
c(t)_j=cos(2pi t_j). Suppose |X|=10. The computed complete classification
of Pi2-unisolvent cases is, up to translation of a by H and independent
coordinate sign changes of X:

* Four row-HNF subgroups of order16 with rows(1,r,s),(0,4,0),(0,0,4),
  r,s∈{1,3}, at phase a=0.
* Thirty-two order19 subgroups, explicitly listed in the compact
  t7-r06-certificate.json, at phase a=0. Every target-count phase for
  these prime-order groups is coordinate-sign-equivalent to that set.

There is no positive-dimensional phase stratum with unisolvent10-node
sets. Every positive nonprime representative has phase[0,0,0], and the
prime-order reduction removes all remaining phases exactly. This is a
classification of the stated finite-coset class, not of arbitrary
10-node interpolation sets. It is not an all-degree construction.

## Reduction and finite predicates

1. Cardinality gives10<=|H|<=80; the upper bound is T7-03's8-to1 fold
   bound. Every subgroup is covered exactly by the row-HNF enumeration
   in T7-03, with A3(m)=sum_(abc=m) b*c². The sum for m10..80 is344054;
   groups below10 cannot have10 cosine nodes.
2. The necessary projection bounds2<m_j<=20 remove groups for every
   phase, as proved in [C reductions](t7-r06-census-reductions.md).
3. Every mixed special/free mask is retained. Special indices modulo
   m_j are quotiented by the exact integer-lattice image of H; the
   same proof establishes that node count and symbolic rank survive.
4. Prime-order groups use the proved complete prime collision reduction.
   Only order19 can fold to10. All its target-count phases are sign
   changes of c(H). Its integer zero-phase character dictionary has
   exact rational rank, so finite-field deficient ranks are never
   mistaken for characteristic-zero deficiencies.
5. Nonprime strata are eliminated only by exact wrong node count,
   low axis count, fixed-point trace mismatch, or the written T7-02
   compatible short-relation polynomial. The fixed-point test is
   proved for folded cosets in C reductions. Support<=2 relations
   with max coordinate magnitude<=2 have degree<=2. Compatibility is
   checked exactly and never assumed on a free active phase coordinate.
6. Remaining strata receive exact cyclotomic-to-finite-field full-rank
   witnesses. T7-01 transfers character rank to polynomial evaluation;
   equivalently the direct product-Chebyshev node matrix is evaluated
   through a ring homomorphism Z[1/2,zeta_D]->F_p with a certified
   primitive Dth root. Nonzero finite-field minors prove nonzero real
   minors. No remaining deficient specialization occurs in this run.

## Completed finite execution

The full entrypoint was actually run, separately from the two earlier
120-second pilots. It finished in173.688seconds:

| Predicate / count | Value |
|---|---|
| Every HNF group, order10..80 |344054|
| Low projection group kills |30582|
| High projection group kills |294204|
| No-fold order10 trace kills after projection pruning |112|
| Prime groups delegated after pruning |824|
| Quotient strata visited, nonprime |2705380|
| Wrong node count |2510229|
| Low projected cosine count |192793|
| Target-count nonprime strata |2358|
| Exact fixed-trace kills |2342|
| Exact compatible short-relation kills |12|
| Exact full-rank nonprime classes |4|
| Unresolved rank cases |0|

The separate complete prime block covers42282 HNF groups across
18 primes11..79. At p19,324 groups have all nonzero coordinate
projections; exact rank counts are {3:4,5:24,6:72,7:24,8:48,9:120,
10:32}. The other57 order19 groups have a constant coordinate.

## Checkers, evidence and trust

Producer: code/t7_r06_census_finish.py, using the committed reduced
phase/pruning helpers and the inherited exact dictionary. Compact
coverage receipt: evidence/t7-r06-census-n2-complete.json. The complete
positive witness list is evidence/t7-r06-certificate.json, generated
and checked by code/t7_r06_certificate.py. Raw rejection rows and the
per-order table are regenerate-only; sizes/hashes/commands appear in
the receipt. No raw catalogue is required as an unexplained premise:
the committed checker regenerates every finite predicate from integers.

Trusted software: Python integers, NumPy integer arithmetic under the
checked<2^26 prime bound, SymPy HNF/primality/primitive root/rational
matrix rank; the field products are pairwise, so signed64-bit products
cannot overflow. Independent check06 has already reconstructed the
hand reductions and the entire prime-block integer rank distribution.
Its actual distinct full producer execution finished in179.102seconds,
matching all scientific fields and BOTH raw rejection-catalogue hashes.
The independently written code/independent_r06.py, frozen SHA256
ed352441b145a900f375eb6bf03543e186976c31824ec9baf2b882fb5d64d296,
then independently covered all344054 HNF groups and2,705,380 quotient
strata with identical predicate counts, and certified the four order16
positive sets through its own actual-node monomial evaluation. Its own
integer Fourier dictionaries separately reconstructed all324 relevant
order19 ranks. Durable receipts: independent-r06-t7-census.json,
independent-r06-t7-primes.json, independent-r06-t7-replays.json.
The [independent report](../independent-checks-round06.md) explicitly
reconciles generic-rank checker boilerplate with this run: every positive
nonprime stratum is all-special, and the prime argument handles every
remaining target-count phase. There is no unclassified exceptional
phase locus at n2. Check06 read this complete theorem and accepted the
computer-assisted PROVED status on2026-11-06 after these actual runs.

## Quality and limits

Every one of the36 positive representatives was actually measured on
the21³ mesh: all four order16 representatives give Lambda21≈7, while
the32 prime representatives range from7.05325615906 to8.13406903712.
All equivalent sign images have the same true Lebesgue constant by
coordinate symmetry, and the mesh is also invariant. Numerical values
remain MEASURED, without global-max or rounding certificates.

The full all-phase n3 census remains OPEN. The handoff06 permitted
fallback consists of this complete n2 classification plus the exact
256-draw n3 rational-phase sample; its full-n3 feasibility pilot has a
separate measured record. Neither fallback nor finite n2 classification
closes the broad degree-uniform Padua-type quality target.
