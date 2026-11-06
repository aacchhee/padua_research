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
| T9-MAX; refined maxima | T2/T4, inherited c3_lebesgue.py; IDEA-203–205 mesh/Leja controls | Same nodes, nested21→41 angular meshes and bounded local search, not a new family. Abort ill-conditioned inversions; never infer a theorem from fits. | Measurement continuation; freeze preregistration before run. |
| T9-HAAR; dual packing | T1 open-class packing sketch; Cools–Poppe LIT323/381, DMVX LIT322; IDEA-178 density and IDEA-185–189 finite lattice controls | Prove exact unshifted equivalence with integer dual and folding factor; test 2D and phase cancellation. Density18/19 is not inspected, so its corollary stays conditional. | Analytic reduction retained; no universal impossibility claim. |
| T9-K; retained averaged kernel | T6 universal lower; IDEA-206 Fourier/projection intermediary and its nonsharp ceiling | Keep multiplier2^-s rather than invert it at cost27. A bounded dual witness must give a strictly larger explicit lower bound. | Quantitative continuation; kill claimed improvement if normalization or positivity fails. |
| T9-SQ; positive-facet square wave | T6 sawtooth/facet argument; IDEA-206, classical Fourier log powers | All shifted frequencies positive, sign(sin) has coherent odd Fourier coefficients. Kill if signs, facet inclusion, or minimum-coordinate covering fails. | Quantitative variant; no sharpness or novelty claim. |
| T9-LOWERSET; hierarchical upper transfer | Carnicer–Godés LIT310; Chkifa–Cohen–Schwab lead in handoff04; IDEA-203 discrete Leja | Derive norm transfer from declared univariate prefix bounds. Full explicit polynomial family requires a verified prefix theorem, absent locally. | Standard reduction retained; explicit bound deferred with source resume condition. |
| T9-EXTRACT; near-Padua projection | DMVX LIT322, LIT391 O(log³) hyperinterpolation lead, LIT382 extraction | Prove exact interpolation correction and expose inverse submatrix norm. Node count or small projection norm alone is insufficient. | Standard reduction retained; explicit controlled subset deferred. |
| T9-FEKETE; polynomial existence | Classical maximum determinant; LIT382/383 | No distinction: compactness and Cramer give Λ≤N. | Gate killed as a new result; baseline retained only. |
| T9-LOCALDET; locally optimized Fekete proxy | LIT321/322/382, T2 QR baseline | Finite determinant ascent, not global Fekete optimality. Use only preregistered small n. | Measurement control, no construction theorem. |
| T9-LOCALIZED; exact positive-packet dual | Root suggestion after full gate; same retained-kernel duality as T9-K | Finite nonnegative packet with rational phases could strengthen individual-degree bounds. | Screened, deferred: simple analytic all-n witness already suffices; resume only if a sharper finite bound is needed. |

No prior disposition is overwritten. T4's killed monotone stack is not revived;
its n4–7 Leja-height variant is measured only within its inherited tested range.
No fresh code or receipts claim a computational proof without independent rerun.
