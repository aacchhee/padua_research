# Claude audit-04 (manuscripts): the 51-page paper, the 147-page companion and their agreement

Part of the focused audit of handoff 30; candidate, models, rules, disclosures, executed
checks and the scientific assessment are in [audit-04.md](audit-04.md) (stated there once).
Reviews and scripts: [audit-04/](audit-04/). Both delivered manuscripts and the old 48/162-page
PDFs and freezes are left intact; everything below is a proposed change returned to Codex. This
audit does not authorize submission, external communication or merge.

AC's current criteria (from the brief): mathematical coherence and sufficient explanation matter
more than page count; notation introduced before use; named tools cited or stated in the form
used; keep needed derivations and worked examples. AI declaration, ORCID and contributions are
reserved to AC and are not assessed beyond factual consistency.

## Verdicts

| Target | Verdict |
|---|---|
| **Journal paper** (51 pp, Constructive Approximation) | **Mathematics accepted; exposition accepted with minor revisions.** The new Section 4 chain was reconstructed line by line; all 38 displayed rational identities check exactly. The audit-03 paper findings P-02, P-03, P-06, P-07, P-09, P-14, P-16 and all X items are fixed and correct. No correctness defect |
| **Companion** (147 pp) | **Mathematics sound; pedagogy: accept after revision.** Every added or changed derivation was re-derived. One **regression** (C4B-01: four reasons deleted from Lemma 4.2 during the duplicate merge), three teaching MAJORs in the second half of the comparison chapter, one in localization |
| **Agreement** | **Agrees.** Source baseline 24a98db: 19 statements, 85 numbered environments (86 equation numbers), 116 labels, 16 numbered headings, all compiled numbers equal in fresh `.aux`; bibliography identical (22 entries); paired silent mutations fail the baseline |
| **Notation and first use** | **Not yet meeting the criteria** at a bounded, listed set of places (N4-01, N4-02 MAJOR as groups of local edits; N4-03..N4-09 MINOR) |

## Builds, correspondence and mutation test (B4)

Fresh builds (TeX Live 2023 Debian, pdfTeX 1.40.25, latexmk 4.83, outputs under the auditor's
scratch directory; `latexmk -outdir` wrote nothing next to the sources): paper 51 pages, 733,624 B,
sha256 `ad416ae09df923fe3967e95c2c2f591a3248ab99987e79897ce802067cf8e21d`; companion 147 pages,
1,171,239 B, sha256 `febea0067b656d0f0fc34de07098237b87e3cb2bf3d19b5ffe31af6279dcde79`. The recorded
builds (733,598 B `1346fc28…`; 1,171,187 B `83ca42c8…`) are not byte-identical, as expected. Logs:
0 errors, warnings, undefined references or citations, multiply-defined labels, overfull boxes or
font warnings; only underfull boxes (17 `\hbox` each, 13 from Table 1). The companion is within
five times the paper (147 <= 255). No `.tex` or `.bib` file changed since 24a98db. The original
48/162-page PDFs were **not** verified (`local-output/` absent).

Correspondence helper (source-baseline mode, exactly as documented) PASS; what the numbers mean:
19 formal statements (4 theorems, 9 lemmas, 2 propositions, 3 corollaries, 1 remark); 85 unstarred
numbered display environments carrying 86 equation numbers (only one `align` has two numbered rows);
116 `\label` commands; 16 numbered headings compared in order. The reviewer reproduced all of it from
the fresh `.aux` files with its own parser. **Mutation test** (copy trees, read-only access to the
24a98db baseline): every identical paired silent mutation fails the source baseline while pairwise
comparison passes: a constant in Corollary 4.6 (j* = 23/250 → 24/250), the quantifier of Theorem 1.1
(n >= 2 → n >= 3), a numbered display, an unnumbered display, the `.bib` file, the theorem numbering
in `main.tex`, and an extra `.tex` file. A companion-only change fails both checks; a README edit
passes by design. A paired rename of a symbol fails the final helper with or without a map (it has no
rename feature); the audit-03 notation scanner passes it only with a declared map, and **also passes
a constant change declared as a "rename"**, so a rename map is not a semantic check (B4-08).

## Coverage

**Paper** (every unit read fully by P4; per-unit verdict in [p4-paper.md](audit-04/p4-paper.md)):
front matter and abstract; §1; §2 (Lemma 2.1 reconstructed); §3.1–3.2 (reconstructed and computed);
§3.3 (correct as far as reconstructed; the aggregate constants were re-derived in audit-03);
§4 preamble and Fig. 2; §4.1–§4.2 (the 11-page proof of Theorem 4.5: charges not re-derived this
round); §4.3–§4.5 (fully reconstructed and computed); §5 preamble, §5.1–§5.3 with both tables;
Declarations; the 22 references.

**Companion** (every line read): C4A: `main.tex`, introduction (489 lines), preliminaries (645),
corner section (1868); C4B: `comparison-unified.tex` lines 1–2055 (pp. 52–80); C4C: lines 1990–4020
(pp. 80–104); C4D: localization (1153 lines, excluding the `\input` comparison text) and certification
(1842 lines). The notation reviewer covered the companion by script plus hand inspection of every
flagged site (not line by line).

## Findings: journal paper

IDs are the reviewers' own (P4-, N4-, B4-, J1-, J2-). All MINOR unless marked.

- **N4-01 (MAJOR, as a group of local edits): symbols used before definition.** ρ, the phases A, B and
  the gate P_n first appear in the §4 roadmap table and Fig. 2 (localization lines 82–114, p. 16),
  before §4.1 defines ρ (p. 17). I_s and the phase point φ (comparison lines 1387, 1495); M in
  "M tan(e/2)" (887), c (1351), θ_0 (1281); U_{n−1} (1334) and Li_2 (441) are undefined in the paper
  (the companion defines them); D_φ is used (909) before its definition (915); the J_end/J_cen split is
  never stated; Lemma 5.1 does not quantify M, ω_a, ω_b and uses W_z and I_R before introducing them;
  L_{jk} is never defined; also F_r, "leaf", I_n in the introduction and γ in the abstract
  (P4-03, C4D-11, B4-02).
- **N4-02 (MAJOR, as a group): named tools only named.** The tangent partial fraction
  (comparison:396), the triangular-kernel second difference (:241), Li_2, the discrete layer cake
  (localization:246), centered-cell BV quadrature, the finite sine product, the Fourier step behind
  the cot partial fraction (corner:361), the binary64/Horner/pairwise error model (delegated to the
  package), and the exponential-type Bernstein inequality in §5.2 (P4-04) are named without a usable
  statement. The companion already states most of them; the fix is copying one to three lines each.
  Four bibliography entries (IEEE 754, NumPy/Python, Higham, a Fourier-uniqueness theorem) are missing.
- **P4-02 / N4-03 / C4B-04 / C4D-08 (notation collisions in numbered blocks, both texts):**
  P_n is both T_{n+1}+T_n (localization:20 and the proof of Theorem 4.5, lines 675–676) and the
  radius-one gate polynomial P_n(ρ) (Cor 4.7, Theorem 4.10, Fig. 2, (74)–(75)); the notation pass had
  renamed the latter 𝔭, and the rewrite brought P_n back. G is both the kernel G_n and the gate
  function G(n,ρ_1); Θ in (62) vs Θ = 𝔗 + j_* in (71) and Cor 4.6; U in Cor 4.7 vs U = π²/32 in Lemma
  4.9 and §5; plain j_* instead of 𝔧_*; A_* is a lower bound and then an upper bound inside the one proof
  of Lemma 4.8; V and W clash in Lemma 4.8; the constant C of Theorem 1.2 against C = −1 + C_H + C_B in
  its proof. All proposed names (𝔭_n, 𝔗_*, 𝒢, U_*, 𝔧_*) are free tokens; renaming P_n to 𝔭_n passes the
  rename-aware check with a 3-entry map and fails without it on exactly Cor 4.7, (74) and (75).
- **P4-01 proof chain not assembled.** Add an explicit proof of Theorem 1.1 (Theorem 4.10 plus
  Proposition 5.3); Lemmas 4.1–4.2, Proposition 3.2, Figure 1 and Table 2 are never cited.
  **P4-05** the gate base values are not hand-checkable: add a table of rational enclosures at n =
  192/256/295/512 and name the exact checker as the executed record (G(512,1) = 0.5342647 is
  consumed only as > 1/2, a true margin of 0.034; the stated 0.534264 bound is tight to 7e-7 and
  max P(512) < 40786/10⁶ holds with margin 2.4e-10, so state < 4079/10⁵ instead; the J01 slack is
  2.1e-4).
- **P4-06 compressed steps:** Cor 4.6 needs R(h) <= R(h_1) and A(h_1) >= Θ cos h_1 written out; Cor
  4.7 needs the 𝔧 → j_* replacement and U >= 0 stated (same as J1-02). **P4-07** display the five
  termwise maxima and 42 + 2L + (49L̄ + 24)/π <= 64 + 16L + 3L̄. **J2-01** log π > 11/10 is used and
  never stated. **J2-03 / J2-09** name `check.py` as the source of the base values and K = 3
  enclosures; label the 12-digit κ, b, c as numerical values not used in any proof.
- **P4-08 / N4-06 project language and undefined terms of art in §5:** "phase pair", "two trees per
  degree" (never explained; **J3-01 / C4D-03**: they are two identical records of one tree, 942
  records over 471 distinct trees), "compact returns", "recorded computation sites", "board sum",
  "real-phase norm", "collision", "centre", "reproducing kernel", the GRID/TREE names.
  **C4D-04** say outright that stored native endpoints are neither used nor validated.
  **C4D-05** split the trust table into what the text proves and what the program computes.
- **P4-10 introduction inaccuracy:** it says the model comparison controls "the competing reflection
  defects"; those are bounded by the selected-pair floors of Lemma 4.8. **P4-11** move the Peano half
  of Lemma 5.1 ahead of Lemma 4.9. **P4-12** a five-step roadmap for the proof of Theorem 4.5.
  **P4-13 (trim):** the −(H_0 + v_*)z term and the B_β boundary identity are never used downstream;
  the board-sum part of the analytic norm and the n = 1 example are not needed; the §5.3 archival
  paragraphs can move to the data statement. **P4-09** residual audit-history prose.
- **B4-01** Fig. 2 label collisions (the diagonal x + y = π cuts "absolute gate" and "P_n on ρ <= 1").
  **B4-06** the data statement cites github.com/aacchhee/padua_research, but `main` has no
  padua-argmax-bridge-20261105 directory; cite the a433c7d snapshot or the Zenodo DOI once it exists.
  **B4-04** response-03's X-13 row (FIXED, "earlier identification mistaken") is inaccurate: eq. (54)
  and (11), (20), (25), (38), (50) still push their number onto its own line (paper p. 26).
  **B4-09** Table 1 justification, roles-table and node-column notation. **B4-10** γ in the abstract,
  companion PDF title metadata vs printed title, stale "48-page" comment, class text on both title pages.
  **B4-11** Laguardia–Russo is DRNA 15 issue 5 (X-03 can add `number={5}`); LIT-378 is marked UNVERIFIED
  though the version of record was read.
- **Process, important:** every item above is a TeX edit. Any edit breaks the 24a98db byte freeze and
  needs a new paired source commit, a `FINAL_BASELINE` update in the checker, a rebuild and the artifact
  check. Return them as one editorial batch with a focused diff review; treat the P_n renames and the
  P4-05..P4-07 proof clauses as material for review purposes.

## Findings: companion

- **C4B-01 (MAJOR, a regression).** Merging duplicated passages (the C2A-09 fix) deleted four reasons
  from Lemma 4.2's proof (pp. 59–61) that the paper still gives: (a) the f‴ argument refers to "the
  sine-ratio step" and "this substitution", never stated, and uses f(0)/8 < 3/40 without a reason (the
  source is f(0) = 𝔨_0/π with 𝔨_0 < 9/5 from line 1298); (b) the bound t(½−t)/(1−t²)² <= 3/40 linking the
  polynomial inequality to 2Q′cos πt <= 3π/4; (c) the reason for 𝒲(π−w) >= w²/4; (d) the closing inequality
  H(w) − H_0 <= −(π−3)w²/(4π³) <= 0 with the closed endpoints; a one-sentence paragraph "𝒲(π) = 0 counts
  the atom once" (line 647) is left without context. Fix: restore paper lines 172–175, 225–231 and 258–261
  (about 8 lines).
- **C4C-M1 (MAJOR): the second half of the telescope is printed twice and has no map** (pp. 80–102).
  Nineteen blocks state the compressed argument and then re-derive it, sometimes inconsistently (lines
  2443 and 2485 are verbatim; 2133 uses an undefined z). No ledger opens the roughly 30-page proof and no
  worked column shows how small the allowances are. Fix: one claim plus one proof per block; add a table
  of the five telescope terms against their absolute, origin and relative bounds; add an n = 512 column
  (𝔗 = 13.88 against C̄_E = 0.750, ē = 0.102, K_D = 0.110, C_4 = 0.008, k_Wx = 0.380).
- **C4C-M2 (MAJOR): notation traps** in 4.2: F_j is both the actual sample (2519/3300) and (τ_j − 1)/ν
  (3111); w = 𝖺cot(z/2) at 2404 is twice the w = 𝖺cot(v/2)/2 used at 795, 1924, 3246; e = ρ (3575, 3613)
  and e = π − z (3671) within 60 lines; b has three or more meanings; r is both a residual and c_e + c_d −
  2𝖺; K, M, δ collide; "x = z/2" at 2904 while the phase x is live; "support I_i" at 2251 is stale after the
  rename to Ω_i; φ is never defined as a phase point and I_s at 3586 is undefined. Fix: local renames plus a
  one-page symbol table for §4.2.
- **C4C-M3 (MAJOR): four row identities are still only asserted** (lines 2536–2540, 3297–3302): f_j =
  4𝖺/(w² − z²) (needs the parity and sine-shift computation); Σf_j = −sin b/w; the positive set is exactly
  |z| < w; and the signed row (1/nm)ΣF_j = 𝖺/m − sin b·τ(v/2)/w, whose intermediate form
  −(1/m)[C_− tan((x−b+v)/2) + C_+ tan((x+b−v)/2)] the reviewer verified numerically for the fix. About 10
  lines. (The first half had the same issue as **C4B-02**: nothing shows that one actual row averages to
  the profile 𝒱(L,v); the missing display is R_r/n = |C_−|𝒩_n(η_−)/n + |C_+|𝒩_n(η_+)/n + (1/n)Σg, giving
  A·L + ℬ, and the row identity cites eq. (7), the double-sum definition, not the divided-difference form.)
- **C4D-01 (MAJOR): the corner-lemma losses δ_A and δ_D are asserted, not derived** (loc 1035–1069, p. 113).
  Reconstructing them needs four results from 60 pages earlier (the relative comparison, the model loss,
  the origin and global error bounds, the central-pair bounds); u, 𝖺, p, q, P, U_W, E_c and k_Wy are used
  without recall, and the text never says why k_Wy (>= k_Wx) serves both axes. Fix: about eight displayed
  lines plus two rows in the re-entry table.
- **C4D-02 (MINOR, companion fidelity):** the paper's fixes for C3-09(b) (the parity condition is equivalent to
  q ≡ 1 − i, paper loc 208–209) and C3-06 (the fixed-radius sentence, 270–271) are absent from the companion
  (lines 567–578 still carry the ambiguous "accounts for precisely this change"), although response-03 marks
  both FIXED. Insert the two sentences verbatim.
- **C4A group (MINOR):** C4A-04 corner:1653 uses that B, B′, B″ are bounded on [−1/4, 5/4] but only proves
  smoothness on [0,1] (the paper has the same sentence at corner:494; true because B is smooth on (−1,2));
  C4A-06 about ten one-line steps still hidden (the numerator substitution, the subtraction giving 2f, 𝒟_n(π,π)
  = (−1)^n(2n+1) via counting 4s lattice points, the sine-product constant 2^{n−1}, the integration by parts
  behind the sinc identity, log(k+1) − 1/(2(k+1)), Euclid's lemma, a cryptic S_u sentence); C4A-01 the
  compressed paragraph is still followed by one or two full re-derivations throughout §3 ((13) is derived three
  times; the continuity of the κ integrand is shown four times); C4A-02/03/07 notation and ordering (K_M and K
  not identified with κ; a = 2/π reused as a generic real; B vs B(x), d_r vs d; h_n^{(n)} used at prelim:175 before
  its definition at 282; midpoint rule used at corner:579 without a forward pointer); C4A-05 the ψ′(½)/ζ(2)
  display at corner:1133–1137 looks circular; C4A-08 `$csc^2$` in italics (p. 26), a garbled G_n sentence at
  prelim:190–192, "Development draft." on the title page.
- **C4B group (MINOR):** C4B-06 the elementary constants are used about 850 lines before they are derived (412–612
  vs 1268–1300) with no pointer, log π > 11/10 is not in the list, and several derivations are still missing (why
  𝖺D <= (7/2)u, the substitution into b_full, λ_0 and e^{1/4} > 32/25, e > 8/3, the pole-remainder sum and |N_s| <=
  8, 𝖺 >= 49/64, the amplitude–phase step for C_inf < 9/4, the Abel closed form, a note that 917166/10⁶ and
  1847940/10⁶ come from exact computer arithmetic); C4B-05 about 13 claims still appear two or three times;
  C4B-07 t_d, t_e used at 1984 and defined at 2073, h means π/m at 1591 and π/n at 1793, 𝖪/K and 𝗄/k nearly
  indistinguishable on p. 66, no notation table for §4; C4B-03 line 1146 "For 𝔗 >= 0" should read "T_t >= 0"
  (a global-rename casualty; a TeX edit, so not an in-place fix); C4B-08 `|f\prime\prime|` prints as "|f//|"
  (line 495), a wrong table attribution (494), "independent of 𝖪,k" (999); C4B-09 no figure or numerical worked
  example in pp. 53–102 (one figure of a row against its poles plus a small table; verified numbers are in the
  report).
- **C4C group (MINOR):** m1 the false reason for N_s ("Var N_s <= 12 follows from (uc:scalar-bounds)" needs Lip f <=
  6/π; D̄_φ = 4(c_e + c_d)/π and |f| <= 4 are unexplained 4× overestimates; the paper shares this at 965); m2 the
  omitted-collision event, its condition and count are unexplained; m3 "Consequently E_ret(0) = −2/m + …" (2821)
  depends on an identity proved only at 3296; m4 the residual-increment sentence at 3243 is garbled and the
  residual = −2wΣ𝓔 identity is not derived (𝓔 must be evaluated at v_0 to reproduce 4π²/27; the paper has the
  same sentence at 1285); m5 hidden steps at 2133, 2140, 2178, 2671, 2861, 3526; m6 a result at 3106 precedes its
  derivation and the reflection formula at 2785 is unlabelled; m7 (64 + 16L)/n is not a bound for C_{6,φ} alone
  (its termwise maximum is about (65.2 + 17.6L)/n; it works only with the 3L̄/n saving); m8 say where R <= A +
  B²/(2A) is used and cite E_c <= (5/12)x^{3/2} for the 5/12 and 5/48; n1 state max P(512) < 4079/10⁵.
- **C4D group (MINOR):** C4D-06 the leaf test the companion describes (the constant bound Q̂_R) is not what I25
  executes (the exact maximum of q_R over the clipped polygon); the stated predicate plausibly suffices (it also
  passes all 9590 proxy tests on 276 old certificates) but the actual routine should be described; C4D-07 R_ℓ is
  undefined at certification:1669 and the sine-ratio product form of the kernel that I25 evaluates is never
  displayed; C4D-09 A_* is a numerator lower bound at 452–608 and an upper bound for A(b_−) at 863; C4D-10 further
  clashes (W vs W_ρ̄; t as integration variable and t = B²/2; M as norm and integer denominator; m as midpoint and
  mantissa; E as grid and error); C4D-12 the n = 256 substitutions are shown only as results; C4D-13 repetition
  (Bernstein scaling explained three times, the conclusion restated four times in §5, ε_fp defined twice); C4D-14 the
  folding explanation (C3-10) is in words only.
- **Audit-03 dispositions, companion, checked against the text.** Fixed and correct: C1-01 (the corner formula (8)
  can now be reconstructed), C1-06, C1-07, C1-12, C2A-01, 02, 03, 04, 06, 08, 12, C2B-M2, M3(a,c,d,e,g), m1–m6, m8,
  m10, m11, e1–e4, C3-01, 03 (removed under architecture B; the absolute-gate argument replacing it is correct), 04,
  05, 07, 08, 11–18, 20, 21, G-1, G-4–G-6, P-08. Partly fixed: C1-02 (R_1 is still at prelim:482 although
  notation-pass.md says renamed throughout; the offset-cutoff rename M → L_0 was never applied), C1-03/04/05/08/09,
  C2A-05, 07, 09, 10, C2B-M1, M3(f), M4, m7, m9, C3-02, 09, 10, 19, H-C06. Not fixed: C2B-M3(b) (the false reason
  "each channel has supremum at most four" at lines 2352–2353) and C2B-m12 (the duplication persists in 19 blocks).
  The audit-03 ledger table, worked column and figures were not adopted in the second half of the comparison chapter;
  C2A-11's figure recommendation was declined with a recorded reason. So response-03's FIXED status for these rows is
  not fully supported.
- **Trust and teaching, localization/certification (C4D):** the §5.3 trust text is consistent with G01 and J03
  (Python/Fraction, guarded NumPy, IEEE binary64, the OS and hardware; for 2..40 C++/GMP with 192-bit rounding, g++ and
  the Python driver; the floors, physical cover, corner, far and Peano lemmas as premises). Section 5 is close to the
  standard; the tiny worked n = 2 certificate was reproduced exactly (all four matrices).

## Cross-cutting items that must be changed in both texts together

1. The notation batch: P_n/𝔭_n, G/𝒢, Θ/𝔗_*, U/U_*, j_*/𝔧_*, the symbols-before-definition clauses (ρ, A, B, x, y), the
   four tables (§4 preamble, start of 4.2, start of 4.3, start of §5), the named-tool statements (N4-02), the Fig. 2
   labels; use the rename-aware check with a declared rename map (AC decision 2) and re-baseline once at the end.
2. Proof clauses in both texts: J1-02, P4-06, P4-07, C4C-M3 (with the one-clause addition at paper line 931 and the
   companion lines), C4B-02, C4B-01 (companion only: restore the four reasons), C4D-01 (companion; add a short forward
   statement in the paper), C4D-02.
3. Evidence language: "two trees per degree" → 471 distinct trees, each recorded twice (J3-01, C4D-03); stored native
   endpoints neither used nor validated (C4D-04); the split trust table (C4D-05).
4. References: IEEE 754, NumPy/Python, Higham, a Fourier-uniqueness theorem; `number={5}` for Laguardia–Russo; update the
   checker's frozen-bib baseline in the same commit.
5. Data availability: cite the a433c7d snapshot now and the Zenodo DOI when AC creates it (B4-06); keep the marked
   placeholder until then.

## Literature, novelty and attribution

No new novelty or priority claim was made in this round, and none was assessed beyond audit-03. The bibliography
(22 entries, alphabetical, all cited, all 21 link targets exact) now includes Kuznetsova 1995 [17] and Pimenova 1979
[21] (audit-03 X-05); metadata matches the repository literature records, with web confirmation for Landon-Cardinal et al.
and Laguardia–Russo. No DOI was resolved directly (the Crossref API is outside the session's allowed network).

## Prioritized revision plan

1. Fix E4-01 and complete the evidence checks (see [audit-04.md](audit-04.md)); these gate the 320..510 claim.
2. One editorial batch with a new paired freeze: first the regression C4B-01 and the two N4 groups, then the
   proof clauses, the tool statements and the tables, then the rest of the MINOR items; use the rename-aware check.
3. Companion pedagogy: merge the remaining duplicates (19 blocks in C4C; about 13 claims in C4B; C4A-01), add the
   ledger table with the n = 512 worked column, one figure of a row against its poles with a small table, a
   five-step roadmap for the proof of Theorem 4.5.
4. Optional simplifications: J1-01 (the quadrant monotonicity), an "Elementary constants" lemma at the start of 4.1,
   a short toolkit before Lemma 4.2, trimming the atlas material listed in P4-13.
5. After the batch: a focused re-check by a distinct agent, fresh builds and the correspondence check. A new
   substantive audit is needed only for changed analytic text, not for wording.

2026-11-08 · orchestrator `claude-sonnet-5-5`; review work by Claude Opus 5.5 subagents (instructed xhigh) · rules read at
be9a831, unchanged at 70a50d7.
