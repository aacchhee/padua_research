# Paper positioning after completion of the bridge

AC clarified on2026-11-07 that earlier Codex/Claude work was already
considered sufficient paper material without the finite argmax bridge.
That remains the assessment. An outline centered solely on the bridge
would undersell those independent mathematical results. This is editorial
planning, not a novelty/priority verdict or a new research campaign.

## Two mathematical strands

1. **Asymptotic structure.** Exact finite corner identities, the explicit
   logarithmic coefficient, the parity-independent constant and proved
   vanishing remainder provided a substantial standalone result. PD-T271
   is the accepted corner expansion; PD-T229's eventual argmax already
   suffices to transfer it asymptotically to the global Lebesgue constant.
   A known numerical onset or certification of every small degree is NOT
   needed for that asymptotic implication. The effective n>=320 theorem
   later supplied an explicit uniform onset. The phase/cancellation
   representation and selected uniform signed-error results explain the
   mechanism beyond a fitted expansion.
2. **Exact global location for every degree.** G01 now removes the formerly
   unresolved finite bridge and proves exactly the parity-correct two
   corner maximizers for every integer n>=2. The analytic tail and finite
   continuous-domain certificates are the two proof components. This
   strengthens the first strand rather than supplying its original reason
   to exist. The cheap certification method supports this result.

The logical connection is Lambda(n)=Lambda_c(n) in the argmax range. With
N=n+1/2, PD-T271 gives

    Lambda_c(n)=4/pi^2 log^2N+b logN+c+R_n,
    b=8/pi^2 (gamma+log(8/pi)), c=c1^2+kappa, R_n ->0.

Its precise explicit remainder now also bounds the GLOBAL Lambda for every
n>=32 by G01. The earlier eventual theorem had already justified the same
asymptotic expansion for sufficiently large n. The finite bridge therefore
does not newly create the asymptotic corollary. This direct substitution
is independently checked in the mathematical review's follow-up message;
it requires no new computation. At this pre-H paper-planning checkpoint, the sharper -1/N and
O(logN/N^2) refinement of original PD-T098 was not proved. It is now
proved by the separate [six-round Hcampaign](campaign-H-summary.md),
with its complete [analytic theorem](theory/H-sharp-corner-expansion.md).

## Recommended combined narrative

- Introduction: state the asymptotic theorem and exact all-degree argmax
  theorem side by side, explaining which advances were already independent.
- Definitions and exact representations: fix the Padua convention, corner
  formula, phase function and cancellation identity.
- Asymptotic analysis: derive coefficients, constant, the now-proved -1/N
  correction and O(logN/N²) remainder,
  retaining its named computer-assisted constant dependency.
- Global localization and effective analytic comparison: eventual mechanism,
  then sufficient n>=320 with complete closed-region/equality proof.
- Finite completion: certificate semantics, mathematical reduction, coverage
  and exact checks, yielding all n>=2.
- Reproducibility and scope: source/runtime trust, fresh verification, actual
  sampled regime, selective retention and costs. Append technical estimates
  and implementation details; include F supports only where their own
  mathematical value or proof role warrants the space.

If this becomes too long, an asymptotic/profile paper and an exact-argmax
computer-assisted paper are defensible, with precise dependency separation.
Do not manufacture separate papers from successive onset improvements or
round history. A standalone certifier paper needs its own broader method
contribution assessment; cheap runtime alone is not that assessment.

## Prior published context and coverage limits

The repository's primary-reading records confirm Kolomoitsev–Lomako2021's
Padua leading4/pi^2 log^2n+O(logn) statement and DeMarchi2022section3.3(2)'s
corner-maximizer observation. Those frame the two strands above. Read
literature/records/kolomoitsev-lomako-2021.md and
literature/lattice-unisolvence/records/demarchi-2022.md for actual reading
coverage. No exhaustive literature/priority claim follows. Final Claude
audit should assess proof, contribution and presentation before readiness.

## Fresh literature refresh —2026-11-07

[Documented internet search and source comparisons](literature-refresh-20261107.md)
yielded no matching sharp Padua expansion or exact all-degree cornerproof
in its declared readscope. This is not certainty of historicalpriority.
The leadingterm is published; cornerlocation was conjectured/observed;
older numerical lower-orderfits must be distinguished from exactproof.

An important explicitmethodantecedent is Bialas-Ciez–Kenne–Sommariva–
Vianello, ETNA60(2024),428–445, DOI10.1553/etna_vol60s428: rigorous
Chebyshevmesh bounds on Lebesgueconstants, including Padua examples.
Credit that work; any certifiercontribution must identify its specific
strictargmax/cancellation/cheap-arithmetic advance beyond generic mesh
evaluation. Primarysourcecomparison and access/versionlimits are in the
refreshnote and its independent boundedreview. No publicationready or
firstproofverdict follows.
