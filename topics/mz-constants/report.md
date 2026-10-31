# Campaign report and development briefs

Rules/base: d36722823441dc40c6e19d69a174459348dd309c. Scientific checkpoint: 2dc9264333cdf8372947448f4b9bdd3bb577d0e1. Final mapping and shared reservations are in [the batch ledger](../padua-batch-20261031/ALLOCATIONS.md). Analytic validity was independently accepted within the declared Astra scope; Claude audit-01 accepted the original mathematical statements; focused Claude re-audit of response-01 remains PENDING. Novelty remains unresolved where named historical fulltexts were unavailable. This is a development report, not a submission or merge request.

## Ranked results

| Rank | Result | Status and practical significance | Limit |
|---|---|---|---|
| 1 | PD-T017/PD-T018: λ_min(N,N−1) asymp (1+log N)^−2 | PROVED analytic comparison with explicit loose constants; an exact parity-compatible harmonic-U witness matches a cardinal-cell Schur lower bound | no leading limit constant; historical interpolation overlap high-risk |
| 2 | PD-T022 endpoint corollary: λ_max(N,N−1)≤2−4/N+4/N²<2; qualitative PD-T014 retained | PROVED; answers the strict CC upper-threshold question through the full requested subspace | upper gap degenerates; sharp limit near1.004437 OPEN |
| 3 | PD-T022/023/024: explicit fixed-ratio strong MZ bound | PROVED for every θ<1, with Aθ=(1−θ)²/[12(1+π)^4(1+2/π)] and upper1+max(2θ−1,0)² | constants deliberately loose; classical weighted-MZ overlap unresolved |
| 4 | PD-N004 and PD-T025: applicability correction and upper-Gram hyperinterpolation application | PROVED exact η_512>3/4; separately uniform error factor≤(1+√2)√V at the stated reproduced degree | An–Wu's conditional corollary is not refuted; generic upper-Gram mechanism already appears in ASV |
| 5 | PD-T021: Padua marginal is2Q_m and CC Gram is an isometric compression | PROVED with signed individual weights permitted | only domination/liminf consequence, no2D upper/positivity theorem |
| 6 | PD-T026: reproduced CC/Padua spectra, Schur/HSS diagnostics | MEASURED with actual separate Astra replay | CC≤1280, ratio/Schur≤640, Padua≤40, HSS≤512; imported larger outputs unreproduced |

Foundations and scoped mechanisms are independently registered: PD-T013 exact weights/alias/defect, PD-T015 coefficient floor, PD-T016 full-degree obstruction, PD-T019 exact U quotient; PD-N002/003/005/006 retain the failed PSD, plain-row-dominance, cardinal-L1 and unconstrained alternating-vector mechanisms.

## Development briefs

**M0 — literature.** Completed the requested bounded baseline before proof exploration, then a 43-query primary-source/access screen. The original nineteen LIT entries distinguish selected fulltext, abstract, metadata and UNVERIFIED input statements. Trefethen's mode aliasing is classical. Sloan–Smith1978/1980, Mastroianni–Milovanović, historical MZ inequalities, Widom/Wilf and journal-version comparison remain named pending-reference gaps. Passi is listed as a bachelor's thesis; the supplied book-chapter description was corrected. No matching result was found in the documented inspected portions, which is not an exhaustive novelty verdict. Audit M2 added20 targeted queries and five records LIT-061–065 on weighted mean convergence/converse quadrature sums (Erdős–Feldheim, Askey, Nevai III/addendum, Lubinsky147 and Smith Lobatto), plus named Mastroianni–Russo/Xu follow-ups. Selected primary theorems were reached, but the exact CC nodal-weight/critical-logarithmic translation remains a named pending-reference gap.

**M1 — upper spectrum.** Four conceptual rounds, two retained failures. The successful matrix A=2M−R has nonpositive off-diagonal entries; replacing coefficients by their absolute values bounds its quadratic form below by a positive continuous norm because the defect has nonnegative entries. The degree-sensitive PD-T022 specialization gives the stronger endpoint gap4/N−4/N². The telescoping mass floor PD-T015 is retained independently; its original2/(πN) quantitative application is valid but dominated. Exact checks N2..40 supplement the all-N proof. Stop condition: frozen first question solved. The sharper asymptotic target remains PD-T027 OPEN with a precise resumption condition.

**M2 — endpoint spectrum.** Five conceptual rounds, including failed cardinal-column and degree-constraint transfers. A direct cardinal decay bound and angular-cell weighted Schur argument prove the lower order even on Π_N. An endpoint-cancelled harmonic sum of same-parity U polynomials gives Q=O(logN), continuous squared norm≳log³N, and an admissible degreeN−1 vector. A separate exact U calculation gives the finite512 counterexample. Sharp-limit target PD-T020 stays OPEN. No private result is needed by any public proof.

**M3 — fixed ratio and application.** Activated after M1 completion, keeping at most two substantive directions. Degree-sensitive sign comparison gives upper1+max(2n/N−1,0)²; filtered Fejér reconstruction on the2N-point circle and weighted Schur give a positive fixed-ratio lower constant. Three conceptual rounds retain the generic operator estimate as known-context application. Exact Fourier/sign checks covered all324 pairs N2..25. The original fixed-ratio target was proved, not replaced by a weaker application theorem.

**M4 — Padua.** The requested source fact is reconstructed in PD-T021. The full signed-weight target PD-T028 is OPEN; no univariate compression argument is promoted to a two-dimensional upper bound. This campaign selected M1/M2/M3 for substantive exploration and did not claim failure of a never-launched2D proof. Comparisons with tensor-CC, Xu, Morrow–Patterson and Lissajous rules are deferred with explicit conventions to check.

**M5 — other rules.** Candidate retained, no classification round launched. Resume with a specified node/weight/measure triple and historical-screen result. Node-vanishing polynomials are a kill test in the degree range where they belong, not a blanket classification.

**M6 — computation.** Bounded source reproduction plus independent replay completed. No large run or interval-spectrum proof is necessary for the analytic theorems. Tolerance-dependent HSS ranks are measurements. No computer-assisted universal theorem is claimed; all-N claims have written analytic reductions/proofs.

**M7 — manuscript.** The gate was met only after M1/M2/M3 prior-art dispositions and separate Astra reconstruction. The complete 15-page revised draft in tracks/mz-constants/paper/ uses final IDs and compiles without final-pass warnings. It retains historical gaps, the eta-rate limitation, and signed-Padua scope; compilation and independent manuscript review are recorded there. Submission readiness requires Claude audit and bibliography/overlap resolution.

## Important corrections to the input narrative

The U witness alone proves a vanishing minimum eigenvalue, hence only liminf eta≥1. The separate upper theorem supplies CC eta→1, and that convergence already gives the unconditional Padua liminf consequence through PD-T021. The Padua marginal gives no corresponding upper control, so Padua convergence remains OPEN. Even for CC, 1−eta=min(λ_min,2−λ_max): the proved λ_min order and current upper gap do not identify eta's endpoint deficit rate or its eventually binding side.

The quantity1/√λ_min grows logarithmically, and the Gram condition number grows like log²N because1≤λ_max<2. The ordinary quadrature hyperinterpolant does not invert G; its upper-Gram norm estimate stays uniformly bounded. Thus the input's description of logarithmic growth as the true hyperinterpolation stability is unsupported. The failed eta≤3/4 application assumption does not invalidate An–Wu's explicitly conditional corollary or establish an unverified published erratum.

N denotes one less than the CC point count. Its ADE is N for oddN and N+1 for evenN; use exactness through at leastN unless the parity improvement matters. At full degreeN the T_N quotient exceeds2, so extending the theorem by one degree is false.

## Independent evidence and remaining handoff

The separate gpt-6-astra xhigh auditor reconstructed all accepted mechanisms, directly checked selected primary ASV/An–Wu/Trefethen passages, ran its own rational checker, reran M1/M2/M3 checkers and all reproduction suites. Reproduction comparison covered637 numeric values with zero discrepancy; M2 replay was byte-identical; M3 passed324 exact cases and matching printed spectra. Numerical values remain MEASURED. [Audit report](independent-astra-01.md) pins scope, source/checker hashes and limitations; final-ID substitutions are traced separately.

Contacting An, Sommariva or Vianello before submission is advisable, after the required audit and resolution of the closest historical references, because their numerical observation is a direct predecessor and Sommariva's CV lists neighboring work with Xue in preparation. No contact has been made or authorized by this report.

Required remaining actions: focused Claude re-audit of response-01; documented historical fulltext/journal comparison before priority claims; Windows cold-storage receipt. Charter main is already merged into MZ, and identical ledger bytes are actually propagated to both active Claude branches. Later member branches must still merge the charter/MZ-bearing main and reconcile their own future reservations before readiness. No development scientific run is outstanding for the stated analytic results. Optional sharp asymptotic and large-scale experiments are future work, not hidden proof obligations. Only AC merges.

Audit-response clarification: PD-T018's explicit128000/(logN)² falls below the trivial bound1 only when logN>sqrt(128000)≈357.77; it is vacuous over all feasible reproduced spectra. The proved order is analytic; finite values do not display the asymptotic leading constant. PD-T017 applies on the full Π_N, including its stated λ_min(N,N) consequence. See [response-01](response-01.md) for the disposition of every audit finding and the focused re-audit scope.
