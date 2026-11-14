# Claude audit-05 (manuscripts): the 57-page paper, the 150-page companion and their agreement

Part of the focused audit of handoff 32; candidate, models, rules, disclosures, executed checks and the evidence assessment are in
[audit-05.md](audit-05.md) (stated there once). Reports: [audit-05/](audit-05/). Both manuscripts are left intact; everything below
is a proposed change returned to Codex. AI declaration, ORCID, contributions and the draft marker are AC's and are reported only.

## Verdicts

| Target | Verdict |
|---|---|
| Journal paper (57 pp) | **Mathematics accepted; paired wording batch required.** Every restored or added reason in the changed text reconstructs |
| Companion (150 pp) | **Mathematics accepted; wording batch required**, including one stale custody statement (M5B-01) and reasons lost in consolidation (M5A-02, M5B-04) |
| Agreement | **Agrees.** Source baseline `ad908acb`: 19 statements, 85 numbered environments (86 equation numbers), 116 labels, 16 numbered headings; the 35 formal blocks and 56 labels of the two comparison files are identical; bibliography identical (26 entries); baseline controls pass; every paired silent mutation fails the freeze |
| Disposition accuracy | Response-04 overstates several rows (listed in audit-05.md) |

## Builds, correspondence and baselines (B5)

Fresh builds (TeX Live 2023 Debian): paper 57 pages, 787,050 B, sha256 `c1547cda…`; companion 150 pages, 1,216,569 B, sha256 `1cd9ac98…`
(BUILD.md records TeX Live 2025/dev; +51 and +41 bytes). Logs: no errors, warnings, undefined references or citations,
multiply-defined labels, overfull boxes or font warnings; underfull boxes only (paper 4 hbox, companion 8 hbox, one vbox per page).
Companion 150 <= 5 x 57. `check_correspondence.py` PASS (19/85/116), `--archival` PASS (13/90/113), `check_baseline_controls.py` PASS
(7 controls); `--artifacts` cannot run without the original PDFs (exit 2); historical PDF preservation was not verified. The TeX/Bib
freeze `ad908acb` changes only five `.tex` files and the one-line `FINAL_BASELINE` update is the separate commit `98261ae`. The
rename-aware scanner against 24a98db with the declared 31-entry map reports 19 numbered and 3 statement blocks (matching the LOG);
aligned by content what remains beyond the map is: one moved display (`ul:log-series`, unchanged), one rename missing from the map
(`F_0(hk` → `F_0(h_m k` in `uc:signed-outer`), and three statement edits (Lemma 5.1 states its hypotheses explicitly; Proposition
5.3 says "certificate records" instead of "phase trees"; Theorem 4.5 defines the signed board sum inline). These are material edits,
not renames, and no permissive map hides them. The bibliography's four new entries (NumPy, Higham, IEEE 754-2019, Katznelson) were
confirmed by web search; Laguardia–Russo renders as 15(5); the Pimenova Math-Net ID could not be checked.

## Findings

IDs are the reviewers' own and unique (M5A-, M5B-, B5-). Locations are in the linked reports.

### Mathematical-exposition findings (a false clause in a proof)

- **M5A-01 (MAJOR by my classification; the reviewer rates MINOR; same issue in both texts; companion 2178–2180, p. 82; paper 936–938, p. 31).**
  The new omitted-collision sentence "It forces |x−y| >= π−v" is false. On the right-endpoint rows the eta_+ channel collides exactly
  when x + y = π − v; a collision occurs with |x−y| about 2.3 < π−v about 3.1 (counterexample script `s8_collision.py`, n = 32, 192, 512).
  The correct statement is rho >= π−v, which still gives a <= Pv/2, so no constant changes. The wording came from audit-04's own
  C4C-m2 suggestion. The paper sentence also has a comma splice. Classified MAJOR here for consistency with P-09/C3-03 (a wrong reason
  in a proof, one-line repair).

### Companion

- **M5B-01 (MAJOR, stale custody statement).** `certification-unified.tex` lines 1623–1629 still say the essential certificates and
  verification records "are retained" and that full histories "remain at their recorded computation sites". The records show the onset-512
  return, the I25 ZIP and the 632 MiB histories absent or unverified. The paper's version was fixed under P4-08; the companion's was not.
- **M5B-02** paper additions missing from the companion: the explicit proof of Theorem 1.1 (P4-01; Theorem 4.10 and Proposition 5.3 are never
  cited in the companion), the physical-corner naming in the proof of Theorem 4.10 (P4-12), in the abstract the "not used in any proof" note
  (J2-09) and the reworded "retains" phrase (P4-09).
- **M5B-03** the companion trust table lists the IEEE "Rounding model" under "Proved in the text"; it is assumed (J3-09, G01 addendum).
- **M5B-04** consolidating duplicated passages in companion section 3.3 (C4A-01) lost reasons: the trapezoid error bound 1/(8z^2) for the psi
  estimate; the recurrence psi(y/2) = psi(1+y/2) − 2/y behind the endpoint value pi − a·d_0; the statement of the psi'(r+1/2) estimate (two phrases now
  refer to nothing); the reference to (cu:kappa), now cited nowhere; kappa is used as a name before the pairing step identifies it.
- **M5B-05** the base-value table is correct (all 60 entries contain the true values, each the tightest outward 6-decimal enclosure) but has no
  label and is cited nowhere, appears before Corollary 4.7 defines U*, d_x, d_y, l_x, l_y, states no provenance (`check.py`'s receipt does not
  contain these 60 values) and the text never asserts the new log pi > 11/10.
- **M5B-07** eps_fp is used before its definition in the new IEEE paragraph; w_B is undefined in the proof of Lemma 2.1; R_l(x) reuses x and t has two
  meanings in one paragraph; the companion uses the internal name "I25" without defining it.
- **M5A-02 (companion)** three needed one-line reasons were lost in the consolidations although the ledger and supplementary review record them as retained:
  (a) pair C1, 2167–2175: the prefactor identity 2aτ(v/2)/(π²ν) with τ(w) = w cot w and the per-row wrap cost 8P/(3πm(j−1)) (τ is used about 360 lines before
  its in-text definition; the paper keeps both); (b) pair B5, near line 980: the primitive ∫T_t dt = 4a log sin(t/2); (c) pair C10, 2817: the reason
  A cos x + B sin x <= sqrt(A²+B²) for the stated minimum. **M5A-03** C4B-06 residuals: the chord bound sin t >= 2t/π (paper line 380) and the alternating
  sine/cosine remainder rule are missing from the companion (lines 933, 3993); the reason for |N_s| <= 8 appears about 1450 lines after first use; the envelope's pole
  decomposition and its sum to 7 are not displayed; still unexplained: line 999 ("bound each subtracted integrand by one"), the amplitude–phase step at 1310 and the
  concavity reason at 620. **M5A-06** the new ledger table (1557, p. 74) uses D_phi, G_phi, C_{6,phi}, M_phi and B_out about 750–1500 lines before they are defined.
  **M5A-07** Figure 3 and the worked-number table (pp. 90–91) sit 16 pages after the row decomposition they illustrate (p. 75); Figure 3 has no label or
  reference; the table says "the independent audit's" values (project-internal provenance).

### Paper

- **B5-01** paper Figure 2 is not fixed: on p. 18 the line x + y = π still crosses "gate" and "rho <=" in the labels (`localization-unified.tex` lines 134–136); the
  companion version (p. 51) is fixed with white-filled labels. Copy the companion's node and arrow lines. **M5B-06** same, at 500 dpi.
- **B5-02** equation numbers are still set on their own line at (11) (paper p. 9, companion p. 24), (20) (p. 14 / 39), (25) (p. 16 / 47), (39) (formerly (38)) (p. 23 / 63),
  (50) (p. 26 / 70) and (54) (p. 27 / 73). Response-04 marks B4-04/X-13 verified on the grounds of "no overfull boxes", but the finding was never about overfull
  boxes. Split the G_g row or record a DECISION accepting the fallback at these locations.
- **B5-03** B4-05 was not implemented: the companion sentence at `comparison-unified.tex` 302–303 still lacks the explicit bracket
  16 A_40(5) − 4 A_39(239) < π < 16 A_39(5) − 4 A_40(239) that the paper displays.
- **B5-04** both data statements cite snapshot a433c7d, which contains the 24a98db manuscripts and the pre-repair readers and which the deposit README calls
  historical; the companion's "Manuscript and checker sources are available in the pinned snapshot" is false for the current version. Cite the post-audit snapshot or
  the DOI before readiness (AC's snapshot).
- **B5-05 / B4-09** the roles table (paper p. 17, companion p. 50) still has touching columns (`l@{\quad}…`); **B5-09** companion Figure 3: the eta_− arrow has collapsed and
  its label is detached; **B5-10** companion line 1604: "The last two rows" lands under the trust table instead of Table 3.
- **M5A-04** one sentence defines both the number h_m = π/m and the series family h_j(t) ("For t=y/π, h_m=π/m, set h_j(t)=…"), so the renamed products h_m(k+τ) and
  F_0(h_m(k+t)) in `uc:signed-outer`, Q_τ and R_log read as the series h_m evaluated at k+τ (both texts; touches a numbered display).
- **M5A-05** the notation collisions were not "corrected in both texts" (response-04 C4C-n3): the paper keeps e = rho (line 1513) against e = π−z (1569) and r(w) (1384)
  against r = c_e + c_d − 2a (1551), and uses tau (1360–1361) right after tau_j and tau(w); in the companion w is the half-amplitude at 3311–3326 but r·π + b at 3376–3402 while
  the section 4.2 symbol table lists only the latter; smaller reuses: eta_± = log(1 ± c/n) near Fig. 3's offsets eta_±, e = π−z at 3027 and 3872, zeta = z/2; the paper lacks the
  factor-four note for the bound on D_phi.
- Editorial: M5A-08 a merge artefact at companion 2920–2922, a parity citation at 2578 where the first equivalence comes from a > 0, the paper's dangling sentence at 948;
  M5B editorial: "yields The tree norm is" renders broken in paper section 5.2, the inward-phase sentence appears twice, "A' <= 0" is stated twice in the proof of Corollary 4.6,
  the weights are d_r in the paper but delta_r in the companion (delta is taken), the paper still points to "the reproducibility package" rather than the companion section (J3-08).
- Notes: M5A-09 both row identities still cite `eq:angular-kernel` (the double-sum definition (7)), not the divided-difference form, and the −cos(nu) cancellation step is
  not stated in the comparison; M5A-10 the unnumbered termwise-maximum constant differs ((317 + 5/12)/n² in the companion, 318/n² in the paper), both valid; B5-06 the scanner is
  index-based (the LOG's "19 blocks" are 1 move, 17 unchanged shifts and 1 unmapped rename); B5-12 (AC-reserved) the AI declaration still omits the Sonnet 5.5 use recorded in
  the LOG, the paper's draft marker is dated 8 November against 13 November sources, funding matches AC's confirmation and the ORCID check digit is valid.

## Process

Every item above except the report-only ones is a TeX edit and breaks the ad908acb byte freeze: one paired batch, a new freeze, a `FINAL_BASELINE` update in a separate
commit, a rebuild, the correspondence and mutation controls, and a focused re-check by a distinct agent. Treat M5A-01 (the corrected statement rho >= π−v) as material for
review purposes. A new substantive audit is needed only for changed analytic text.

2026-11-13 · orchestrator `claude-sonnet-5-5`; review work by four Claude Opus 5.5 subagents (instructed xhigh) · rules read at be9a831, unchanged at 33b9eca.
