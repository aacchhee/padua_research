# T9 gate — 2026-11-06

Rules read at e5b6445; unchanged at integration head120a19e (main f70a260).
Assigned Codex developer; runtime model metadata unexposed. No priority claim.

## Reading completed before mechanisms

AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md; handoffs01/04;
BRIEF.md; full state/IDEAS.md, including every historical table (long output
was reread in bounded chunks, with truncated middle rows reread); literature
INDEX relevant lower-set, cubature, lattice, projection, Fekete and Lebesgue
entries; T1 packing lead and literature-T1; T4/T5/T6 theory and literature;
audit-01/T5-T6 and novelty-records. The main delta76ba421..f70a260 in IDEAS
and INDEX was read before writing mechanism code. New sharp MZ and NN-MOP
results change no total-degree interpolation or Haar-packing hypothesis here.
The source records Carnicer–Godés2015, De Marchi–Vianello–Xu2009 and
Bos–De Marchi–Vianello2017 were read in full as records, not as their primary
papers. Existing source coverage is preserved in literature-T9.md.

This gate was completed before executable mechanism experiments. The analytic
ideas below were developed while reading; no pre-gate numerical run occurred.

## Predecessor comparisons and frozen decisions

| Candidate / aliases | Closest predecessor and obstruction | Distinction and prospective decisive test | Disposition at gate |
|---|---|---|---|
| T9-MAX; refined maxima | T2/T4, inherited c3_lebesgue.py; IDEA-185–189 finite lattice controls, especially IDEA-187 | Same nodes, nested21→41 angular meshes and bounded local search, not a new family. Abort ill-conditioned inversions; never infer a theorem from fits. | Measurement continuation; freeze preregistration before run. |
| T9-HAAR; dual packing | T1 open-class packing sketch; Cools–Poppe LIT323/381, DMVX LIT322; IDEA-178 density and IDEA-185–189 finite lattice controls | Prove exact unshifted equivalence with integer dual and folding factor; test 2D and phase cancellation. Density18/19 is not inspected, so its corollary stays conditional. | Analytic reduction retained; no universal impossibility claim. |
| T9-K; retained averaged kernel | T6 universal lower; IDEA-206 Fourier/projection intermediary and its nonsharp ceiling | Keep multiplier2^-s rather than invert it at cost27. A bounded dual witness must give a strictly larger explicit lower bound. | Quantitative continuation; kill claimed improvement if normalization or positivity fails. |
| T9-SQ; positive-facet square wave | T6 sawtooth/facet argument; IDEA-206, classical Fourier log powers | All shifted frequencies positive, sign(sin) has coherent odd Fourier coefficients. Kill if signs, facet inclusion, or minimum-coordinate covering fails. | Quantitative variant; no sharpness or novelty claim. |
| T9-LOWERSET; hierarchical upper transfer | Carnicer–Godés LIT310; Chkifa–Cohen–Schwab lead in handoff04; IDEA-187 lower-set controls | Derive norm transfer from declared univariate prefix bounds. Full explicit polynomial family requires a verified prefix theorem, absent locally. | Standard reduction retained; explicit bound deferred with source resume condition. |
| T9-EXTRACT; near-Padua projection | DMVX LIT322, LIT391 O(log³) hyperinterpolation lead, LIT382 extraction | Prove exact interpolation correction and expose inverse submatrix norm. Node count or small projection norm alone is insufficient. | Standard reduction retained; explicit controlled subset deferred. |
| T9-FEKETE; polynomial existence | Classical maximum determinant; LIT382/383 | No distinction: compactness and Cramer give Λ≤N. | Gate killed as a new result; baseline retained only. |
| T9-LOCALDET; locally optimized Fekete proxy | LIT321/322/382, T2 QR baseline | Finite determinant ascent, not global Fekete optimality. Use only preregistered small n. | Measurement control, no construction theorem. |
| T9-LOCALIZED; exact positive-packet dual | Root suggestion after full gate; same retained-kernel duality as T9-K | Finite nonnegative packet with rational phases could strengthen individual-degree bounds. | Equivalent bounded-dual implementation suggestion, not pursued: simple analytic all-n witness already suffices; resume only if a sharper finite bound is needed. |

No prior disposition is overwritten. T4's killed monotone stack is not revived;
its n4–7 Leja-height variant is measured only within its inherited tested range.
No fresh code or receipts claim a computational proof without independent rerun.

Gate-record correction: an initial transcription incorrectly labeled the
mesh/Leja comparison IDEA-203–205, which concern unrelated programme routes.
The actual comparison is the read C3/IDEA-185–189 record and T2/T4. Corrected
before final freeze; no experimental choice or result depended on that label.

## Dated audit-02 correction and retrospective completion — 2026-11-06

This section repairs the published gate; it is not a new prospective gate.
The historical heading "Reading completed before mechanisms" is too broad:
this record itself says analytic ideas developed while reading. Its
pre-executable-run statement does not establish pre-analytic full-read
compliance. The published 51c031a gate was subsequently edited before
publication of e80e000: IDEA-203–205 was replaced, and T9-LOCALIZED changed
from deferred to equivalent. "Before final freeze" did not mean before
first publication. The original text remains retrievable in Git. The
canonical disclosure is [response-deviations-02.md](response-deviations-02.md).

This repair worker read rules at 7afa6a54a4db4652267e38cd48658ba435d20481,
the audit appendices, the complete shortlisted registry rows and OBST-11,
the linked Xu/Li–Sun–Xu/Xu-2025 local records and the T6/T9 source records.
It did not personally re-read the complete raw IDEAS registry and generates
no new mechanism. Earlier workers' full-read attestations remain their
attestations. This section makes no primary-source or exhaustive novelty
claim and changes no accepted mathematics.

Search actually executed with rg across state/IDEAS.md, literature/INDEX.md,
relevant source records and programme/bivariate candidate files: Haar,
packing, octahedron/octahedral, lattice, cubature, minimal cubature,
Li–Sun–Xu, Xu, Gamma, joint spectra, dominant submatrix, RRQR, maxvol,
Fekete, weighted Fekete, lower set, Morrow–Patterson, hyperinterpolation,
Subbotin, projection, even space, Corollary 1; identifiers below were
searched explicitly. Search coverage is repository text, not external
primary literature. The original missing search log cannot be backdated.

| Route | Added closest predecessors and exact comparison | Coverage / disposition |
|---|---|---|
| T9-HAAR / PACK | IDEA-029/120 are the same 3D Padua/minimal-cubature target; IDEA-044/109 connect flat/completed moment data and commuting Jacobi sections to cubature. T9 restricts to one unshifted Haar subgroup and proves a shortest-dual-vector reduction, rather than general completed sections. LIT-010/307 reports a conjectural n^3/4 count, stronger in leading coefficient than this conditional class-specific 19n^3/108 bound. | Li–Sun–Xu is secondary, UNVERIFIED and conjectural; neither theorem nor finite-n exclusion is imported. |
| T9-HAAR / PACK | LIT-389 reports no known d>2 family attaining Möller's bound; this is a reported knowledge statement, not nonexistence. LIT-413 preserves Noskov–Schmid/Hirao–Sawa/Schmid certificate leads; finite certificates cannot settle the asymptotic conjecture. | Qualified INDEX/baseline rows read; fulltexts not newly inspected. No novelty or universal exclusion survives solely from this comparison. |
| T9-HAAR / PACK | OBST?bivariate-lanczos-claude-11 and LIT-192/374: Xu 1994 concerns dim Pi_(n-1), one Gamma, degree 2n-2, with a d=3 second-kind-weight n=2 example and an author expectation at n=3. Padua uses the different Gamma_2 extension. | Complete local Xu source record read, not its PDF. Source-reader fulltext coverage is inherited provenance only. Product second-kind weight/degree hypotheses differ from T9's arcsine Haar model; the expectation is no theorem. |
| T9-EXTRACT | IDEA-027's dominant-submatrix/maxvol Lebesgue bound is the closest algebraic predecessor. IDEA-049/LIT-387 warns that Padua degree-2n exactness is missing and a rank-one Gram correction may be needed. The T9 correction lemma exposes a separately bounded inverse, rather than deriving interpolation quality from node count or projection quality alone. | Standard reduction/known mechanism; no new construction or inverse bound. LIT-387's later primary-section screen is separately qualified in INDEX; no fulltext inherited here. |
| T9-FEKETE / LOCALDET | IDEA-209 already covers Padua asymptotically Fekete and weighted stationarity, absorbed as an abandoned programme. Global compactness/Cramer Λ<=N is classical; finite determinant ascent is an optimization proxy, not the global maximizer or an asymptotic theorem. | Fekete novelty remains gate-killed/equivalent. Localdet is a MEASURED control. No administrative PD-N. |
| T9-LOWERSET | IDEA-047/LIT-378 already reports an explicit 2D Morrow–Patterson O(n^2) upper bound. T9's explicit 3D lower-set target and conditional prefix-to-multivariate transfer differ in dimension and hypotheses. | Source statement remains secondary/UNVERIFIED here; neither a first polynomial bound nor a verified univariate-prefix theorem is claimed. |
| T9-K / SQ | The closest external projection comparator is Subbotin's Corollary 1 (1983 English translation p.564), covering arbitrary projections on the even space, not only Theorem 1's 3^-d interpolation comparison. This is reported by literature-T6.md's primary-reading record. | This worker did not retrieve the primary Corollary 1 or verify its exact multiplier/constant. No improvement over Subbotin is established. The factor 27 refers only to the earlier local T6 displayed coefficient; local proofs and their accepted statuses stand independently. |

Lattice rules of fixed trigonometric degree are established prior art:
Cools–Lyness K-optimal 3D rules, Noskov, Lyness–Sørevik and Cools–Nuyens
are additional leads. T10 requires its own pre-run gate, source coverage
and candidate records before any run; this retrospective repair gives no
novelty clearance for T10. Betke–Henk is the density-source lead, not an
inherited proof of 18/19 in this section.

T9-LOCALIZED has one current disposition: equivalent implementation
suggestion, not pursued; no separate mathematical failure or PD-N. The
previous deferred wording and subsequent change are preserved in the
canonical deviation record. Full namespaced candidate IDs, aliases and
resume conditions are in [candidate retention](candidates-T9-response-02.md).
