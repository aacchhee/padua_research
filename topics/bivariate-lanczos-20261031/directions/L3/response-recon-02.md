# Response to L3-reconstruction-02 (developer response)

Developer: L3, Claude Opus 5.5 (xhigh, requested). Written 2026-11-01T00:49+01:00 (`date -Iseconds` stamps on all edits: 00:47:14, 00:48:09). Review: `topics/bivariate-lanczos-20261031/reviews/L3-reconstruction-02.md` (audited head ae991c1; not edited). No new rounds. Every edited theory file carries a dated History line naming the finding and quoting the original wording of each replaced passage; round records carry dated "Corrections" sections (original text kept).

| Finding | Response | Where |
|---|---|---|
| **M1** 315 reference artefact | **Fixed.** Item 4 now leads with the reviewer's 80-bit-reference result (linear regime up to n = 20, ρ = 0.45–0.79, K15 killed in the linear regime at n = 18–20, extras ≤ 0.07); the developer's original item 4 is kept and marked as an artefact for n ≥ 16. | 315; R06 Corrections; PD-N?…-308 |
| **M2** overreach on the random square | **Fixed.** Claims restricted to the rotated square; the random-square near-symmetry of inaccurate F data recorded as a Greenbaum-like counter-indication (unresolved). | 315 item 2 and conclusion; 300 (G) row; R06 Corrections; SUMMARY text |
| **L1** 314(b) missing step | **Supplied the argument** (symmetry + upper band ⇒ block tridiagonal; symmetry kills block-window extras and gives the F echelon pattern; 301(b) needs only the computed J-columns' pattern; J echelon a posteriori). Exact-window hypothesis dropped. Status stays PROVED. | 314 Statement (b), proof (b) |
| **L2** "dist_max(data, 𝒞_n)" | **Fixed** to (Ĥ_F, Ĥ_J). | R06 §4 row + Corrections |
| **L3** 315 ranges | **Fixed** (2.2–10.2; 0.005–0.09). | 315 item 1 |
| **L4** 311 values | **Fixed** (t_D(7) = 6.78e-11 high precision; ratios incl. 680, 16 400; margin ≈ t_D/2 not separate; n = 8 resolved by the reviewer). | 311; R04 Corrections |
| **L5** N304 hypothesis | **Fixed**: ε < min(ρ(δ)/L_Φ, ε_1). | N304 |
| **L6** normalised example | **Fixed** in N301 and N303 (E = −ε ev_ζ/‖ev_ζ‖). | N301, N303 |
| **L7** δ_0(n) → 0 | **Fixed**; reviewer's rigorous δ_0(n) bounds for n = 4..12 cited as a reviewer computation (not independently rerun). | 313 Open items; N303 Statement |
| **L8** missing IDEA/PD-N for R06 hypotheses | **Fixed**: IDEA 314 (A), 315 (B), 316 (C); PD-N?…-307 (A refuted, completed-pair version, MEASURED) and PD-N?…-308 (C refuted, MEASURED). | candidates.md; new theory files |
| **L9** stale text | **Fixed**: 306 Checks sentence; N301 "n ≥ 4 MEASURED only"; IDEA 307 disposition; 300 "unisolvent" → "determining"; 307 item 6 (R04 correction applied). plan.md ledger row R01 is the orchestrator's file — not edited (please apply the M1 wording there). | files named |
| **L10** trusted dependencies of 306/N301 | **Fixed** (Python ints/Fraction; cvxpy proposer only; reviewer: sympy QQ<√2>, DomainMatrix, own sign test). | 306, N301 Depends on |
| **L11** History lines without original wording | **Fixed**: back-filled History lines quoting the original wording of every passage replaced in the round-1 response (all eleven files), plus original wording in every new History line. The nine identical 23:54:00 stamps came from one `date -Iseconds` call passed to the single patch run (not rounded). | 300–309, N301, N302, N303 |
| **L12** pre-registration self-reported; run record | **Accepted and disclosed** in R05/R06 Corrections (only R04 is evidenced by commit order); the first 23:29 weight-fit run and the stopped bounded run are now recorded. | R05, R06 |
| **L13** stale "No independent rerun yet"; N305 n = 2 | **Fixed** (313 Checks updated; N305 n = 2 entry annotated as automatic). | 313, N305 |
| Dispositions | **Applied**: 313 → PROVED; N303 → PROVED under the stated Padua-unisolvence assumption (trusted LITERATURE dependency listed); 310 → PROVED for n = 1..7 (citing `review_L3b/equi_H_cert.py` as the independent rerun); N306 refutation → PROVED (survey parts moved out of the statement, MEASURED in 307); 314 stays PROVED; 311, 315 stay MEASURED; N304 stays PROVED; N305 stays MEASURED. Equispaced n = 8 recorded as a reviewer computation pending an independent rerun. | files named |
| Informational: κ-family fails n ≤ 3 for every real c | **Recorded** in R05 Corrections. | R05 |

Unresolved: none of the findings. Open mathematics remains open (reading (G); 304(c) isomorphism; explicit constants; equispaced n ≥ 9).
