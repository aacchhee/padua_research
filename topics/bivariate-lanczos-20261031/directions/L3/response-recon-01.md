# Response to L3-reconstruction-01 (developer response)

Developer: L3, Claude Opus 5.5 (xhigh, requested). Written 2026-10-31T23:56+01:00. Review: `topics/bivariate-lanczos-20261031/reviews/L3-reconstruction-01.md` (audited head 0b7b396; not edited). Every finding is answered below with fix / evidence-based rejection / unresolved. All edits carry a dated History line naming the finding (theory files) or a dated "Corrections" section (round records); STATUS.md gained an appended correction line (old lines unchanged).

| Finding | Response | Where |
|---|---|---|
| **M1** literal reading trivial only under forward accuracy | **Fixed.** The readings are now: (L0) relations on the sections alone — trivially negative; (L) plus an added forward-accuracy hypothesis — trivially positive; (E) a recorded substitution with a stronger conclusion; (G) OPEN. "L3-Q1 decided/made precise" is qualified as "in reading (E)" throughout. (plan.md History and LOG.md are the orchestrator's; the plan History was already corrected by the orchestrator.) | 302(c) + History; 300 Statement/table + History; R01 §3 and §11; STATUS correction line |
| **M2** residual "for some c > 0" vacuous | **Fixed.** Residual defined with fixed scale c = 1 (L̂ normalised by L̂(1) = L_μ(1)); the proofs already used c = 1; propagated to N302 (N301's bound |E(p*)|/‖p*‖_* is a distance to the cone and was correct). | 302 Definitions + History; N302 + History |
| **M3** kill criteria not evidenced as pre-registered | **Accepted, disclosed, not backdated.** R01–R03 headings and candidates.md header now say the criteria were recorded with or after the deciding runs. R04–R06 criteria were written to file before their runs (file times in R01 §11); K15 was added after K13/K14 and before its own test, disclosed in R06 §3a. | R01 §2, §11; R02, R03 headings + Corrections; candidates.md header |
| **L1** quantifier ε > 0 needs M_n(L_μ + E) ≻ 0 | **Fixed.** ε ∈ (0, ε_1] with M_n(L_μ + E) ≻ 0 for ‖E‖ ≤ ε_1. Also carried to N303. | 303(e); N301; N303 |
| **L2** δ_0 100× conservative | **Fixed (cited).** N301 cites the reviewer's rigorous interval certificate (radius 0.04) as a reviewer computation; the developer-certified δ_0 ≈ 3.89e-4 is kept as the developer's own value. | N301 + History |
| **L3** 304(c) isomorphism unproved | **Fixed by relabelling.** The factorisation part stays PROVED; the isomorphism part is MEASURED (reviewer: rank n(n+1)/2 for n = 2, 3). Proof left OPEN. | 304 table + History |
| **L4** 301(d) formed-entries convention | **Fixed.** Convention stated (degree-n data include the products of the degree-n vectors); difference from L1's PD-T?…-101(4) convention noted with the reviewer's e′ values. | 301(d) + History |
| **L5** 307 wording | **Fixed.** Marginal cases no longer counted as failures (7 of 9 robust failures for random n = 4..6; sorted-uniform draw 1 n = 6 marginal); grid residual stated as an upper bound, evidence only within the certified positivity radius. | 307 + History; R01 §4 |
| **L6** 309(b) injectivity conjunct | **Fixed.** | 309(b) + History |
| **L7** 309 status wording | **Fixed** ("PROVED under the stated assumption (Padua unisolvence)"; reviewer verified unisolvence exactly for n ≤ 4). | 309 + History |
| **L8** STATUS R01 timestamp also estimated | **Accepted.** Correction line appended to STATUS.md; R04–R06 lines use `date -Iseconds`. | STATUS.md |
| **L9** Greenbaum-width remark contested | **Fixed (withdrawn).** Marked unresolved with the conflicting sources; comparison withdrawn (it also mixed unit roundoff with perturbation size). Greenbaum 1989 stays pending-reference. | 300 literature note; R03 §3; lit_reading.md |
| **L10** PD-N classification of IDEA 303/310/311 | **Fixed.** Created PD-N?…-304 (compression ⇏ section, PROVED via 308 + N301), PD-N?…-305 (C1 fails n = 2..12, MEASURED), PD-N?…-306 ((H) not decided by the count, MEASURED). Final classification remains the orchestrator's/AC's. | new theory files; candidates.md |
| **L11** "unisolvent" → "determining" | **Fixed.** | 303(a) |
| **L12** explicit δ(ε) only as a rate | **Accepted and stated.** | 303 Open items; R01 §11 |
| **L13** support inclusion vs Hausdorff | **Fixed.** One paragraph: support inclusion is the definition; in the square case the existence results also give Hausdorff ≤ δ (masses w_i + O(δ + ε) > 0 via ℓ_i²); overdetermined δ = 0 trivially. | 302 Definitions |
| **304(a)** positive cluster masses | **Fixed.** Added the Lagrange-basis step W_i = w_i + O(δ + ‖Φ(μ′) − H‖) > 0. | 304 proof + History |
| **N302** "atom" | **Fixed** ("support point"). | N302 |
| Informational: 306, N301 eligible for PROVED | **Applied** after the L1 fix: 306 and N301 now PROVED, citing the reviewer's independent exact rerun (`indep_exact_check.py`, log `reviews/logs_L3/indep_exact_check.log`) and the byte-identical developer rerun. | 306, N301, 300 |
| Informational: exact n = 4 certificate (reviewer) | **Cited** as independent support for PD-N?…-303 at n = 4 (a different C ⊥ Hankel). Not self-approved. | N303 |
| Informational: S_1 = {p_C} exactly for n ≤ 3 | **Cited** in 307 History. | 307 |

Unresolved items: none of the findings is left unresolved. Open mathematics flagged by the review remains open (304(c) isomorphism proof; reading (G); explicit constants).

Not audited by this review (post-0b7b396): R04–R06, PD-T?…-310–315, PD-N?…-303–306, and the scripts `exact_checkerboard.py`, `r05_*.py`, `r06_*.py`. The ten audited scripts are unchanged.
