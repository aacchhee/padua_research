# beberok-2025 — T. Beberok, A lower bound for the Lebesgue constant of the Morrow–Patterson points, J. Approx. Theory 311 (2025) 106191

Registration (2026-11-14, PR36 preparation): LIT-721 and LIT-722. Provisional labels: none were used; the topic cited the source as "Beberok 2025" (`topics/padua-xu-lebesgue-20261114/lit-notes/X2-sources.md` §0 and §1b). [Exact map](../../topics/padua-xu-lebesgue-20261114/pr-preparation/final-id-map.json).

- DOI / URL / supplied location: [10.1016/j.jat.2025.106191](https://doi.org/10.1016/j.jat.2025.106191) (Crossref: single author, print date Nov 2025, 13 references). ScienceDirect pii S0021904525000498.
- Access and reading date: 2026-11-14. The topic orchestrator read the full HTML on ScienceDirect through NTNU institutional access. No PDF and no page image was seen.
- Reading coverage: **complete HTML text as read by the orchestrator; no page, section or equation locators were recorded (pending).** The literature subagent did not read it (access blocked), and neither did the auditor of audit-01 (finding A-m7 and its remaining-uncertainty note). The numbering "Theorem 0.1" and "(2)" is the orchestrator's transcription of the HTML.
- Reader, model and effort: Claude, claude-opus-5-5 (topic orchestrator); effort not recorded.
- Named gaps requiring future re-reading: page and equation locators; the exact display of the final inequality, in particular the denominator, which the notes transcribe as "(n/2+n+2)²"; whether the constant is stated anywhere in the text. Re-read before any manuscript or any LIT-based claim uses the number below.

## Extracted published statements

### LIT-721 — lower bound of order n² for the Morrow–Patterson Lebesgue constant

- Statement in faithful paraphrase: Theorem 0.1: there is a constant c > 0 such that the Lebesgue constant of the Morrow–Patterson points satisfies Λ^MP_n ≥ c n². The constant c is existential in the statement.
- Hypotheses and notation: MP points of even degree n as in CDMV 2005 and BBDM (LIT-729, LIT-378). The proof evaluates the Lebesgue function at the corner (1,1), with the cubature weights 8 sin²w_m sin²v_k/((n+2)(n+3)).
- Page / theorem / equation: Theorem 0.1 (as transcribed; locator pending).
- Reading evidence and limitations: orchestrator's reading of the HTML (see above). Crossref lists no abstract.
- Relation to campaign claims (no inherited proof status): this publishes the BRIEF target X2.1 in substance, so it is not claimed as new. PD-T703 (X2-26) gives the explicit and vertex-sharp constant c* = 0.5169… for every even n ≥ 2, proved locally and independently of this paper.

### LIT-722 — closed form of the corner kernel at (1,1), and the explicit final inequality (as transcribed)

- Statement in faithful paraphrase:
  - Equation (2): for nodes with angles w = w_m, v = v_k,
    K(1,1,w,v) := Σ_{i+j≤n}(i+1)(j+1)U_i(cos w)U_j(cos v) = (−1)^m (2+cos w+cos v)/(2(cos v−cos w)³) + (−1)^m (2n+5)/(4(cos w−cos v)²).
  - The final display, for n ≥ 8, as transcribed: Λ_n ≥ (√3−1)²(n/4−1)(2n+5)(n+2)(n+3)/(16π²(n/2+n+2)²), a leading constant of about 7.5·10⁻⁴·n². The orchestrator's later note writes the denominator as (3n/2+2)², a simplification of the transcription, not a re-reading.
- Hypotheses and notation: even n, MP nodes as above.
- Page / theorem / equation: (2) and the final inequality (locators pending; display not re-checked).
- Reading evidence and limitations: equation (2) was reproduced by the literature subagent against the defining double sum, with relative difference ≤ 2·10⁻³⁷ at 40-digit precision over all nodes for n = 4 and 10 (CHECKED-NUM, `lit-notes/X2-sources.md` §1b). The explicit inequality and its constant are **as transcribed; display not re-checked** (audit-01 A-m7).
- Relation to campaign claims: PD-T698 (X2-21) re-derives and extends (2). PD-T703 compares its constant c* with the 7.5·10⁻⁴ "as transcribed". The comparison number must not enter a manuscript before the display is re-checked.

## Search and attribution notes

- Forward-citation search: `lit-notes/X2-sources.md` §5 (rows 1–15). This is the only lower-bound result found for Λ_MP in the documented search. BBDM do not cite it (LIT-378 addendum).
- OpenAlex conflates this paper with BBDM (W4410230682 lists both DOIs); Crossref gives two distinct records with different authors and titles. Cite them as two works.
- Its reference list (13 entries, from Crossref) includes BBDM 2024 preprint, Bos 2001, BCDMVX 2006 (JAT 143), BDMVX 2007, CDMV 2005, De Marchi–Sommariva–Vianello 2014, Erb 2016 (two papers), Liu 2019 (Acta Math. Hungar. 159), Morrow–Patterson 1978, Sloan 1995, Xu 2012 and Xu 2017.
- It cites Xu JAT 164 (2012) and JAT 214 (2017) as generalizations of MP points (see LIT-725 notes); the Xu papers were not read for an "MPX" definition.

## History

2026-11-14: created at PR36 preparation from the topic's lit-notes; coverage and open locators stated above.
