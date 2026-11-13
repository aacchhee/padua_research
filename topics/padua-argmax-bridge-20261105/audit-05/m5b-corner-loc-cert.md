# M5B — focused audit-05: §§1–3, §4.3–4.5 and §5 changes since audit-04 (both manuscripts)

Part of Claude audit-05 of Codex response-04 (handoff 32). Auditor: Claude Opus 5.5, xhigh (instructed);
independent mathematical/pedagogical reviewer, distinct from the Codex developers and the Astra
supplementary reviewers. Read-only on the repository: no repository file written, no state-changing
git command (`git status --short` empty before and after). Outputs: this file and `m5b-code/`.

- **Rules** read at branch head `33b9eca8167980cad0b0a491da7de64280c9a158`: AGENTS.md, agents/WORKFLOW.md,
  agents/claude/CLAUDE_ROLES.md, handoff 32, response-04, audit-04, audit-04-manuscripts, and audit-04
  reports c4a, c4d, p4, n4, j03. No novelty content: this is a manuscript/delta audit, so the full
  `state/IDEAS.md` read is omitted (scoped exception, as handoff 32 states).
- **Audited identity.** TeX/Bib freeze `ad908acb21d3589d85635618ff68f63dd01cfbca`; `git diff --quiet ad908acb
  33b9eca` over both `sections/`, both `main.tex` and the bib is empty, so head = freeze. Old baseline
  `24a98db`. Both trees extracted with `git archive` into `m5b-code/trees/`. SHA-256 prefixes (head):
  paper main `14c4ba40`, intro `898086d2`, prelim `ea22564e`, corner `8ecffbf2`, loc `cac0abf4`, cert `0827c220`;
  companion main `b3a9eb5f`, intro `32d30750`, prelim `8e536da1`, corner `fa59b595`, loc `e2c527a2`,
  cert `9bad33ea`; `references.bib` `138871f1`, byte-identical in both trees.
- **PDFs.** B5's fresh builds in `$A/build/` (paper 57 pp, companion 150 pp), its `page-index.md`, text
  extracts and renders; I rendered paper p.41 and companion p.114 myself (`m5b-code/png/`).
- **Labels.** [D] own derivation or reconstruction; [E] executed by me (MEASURED unless exact);
  [I] inspection/judgement.

## 1. Verdict

**Mathematics in range: SUPPORTED — no BLOCKING finding, no mathematical error found.** Every changed
proof clause I reconstructed is correct: the corner-lemma axis/diagonal chains, the C3-09(b) parity
equivalence, the C4A-06 algebra (numerator, subtraction, Euclid, shell count, sine-product constant,
sinc integration by parts), B ∈ C^∞(−1,2), the non-circular ψ′(1/2)/ζ(2) order, the corrected
reproducing-kernel sentence, the Cor 4.6/4.7 clauses (J1-02/P4-06), the Q_v folding identity, the
product-form kernel with its removable values, the polygon-maximum justification, the periodic
Bernstein replacement (P4-04) and the explicit proof of Theorem 1.1.

**Numbers: all reproduce.** The four gates, all 60 entries of the new base-value table, the corner-256
coarse chains and the three displayed n = 256 substitutions are confirmed by an independent
implementation, with exact Fractions where the claim is exact. The frozen J01 checker, rerun from a
byte copy, matches its receipt field for field.

**Exposition and evidence language: improved, but not yet complete.** One MAJOR finding: the companion
still asserts current custody of absent evidence. Six MINOR findings: companion fidelity to the new
paper text, a mislabelled trust-table cell, reasons lost in the C4A-01 consolidation, first-use slips,
table provenance and placement, Fig. 2 label collisions and a stale data-availability snapshot.
Editorial notes follow.

**Paper and companion agree** on all numbered blocks. `check_correspondence.py` passes on 19 statements,
85 numbered displays and 116 labels. The companion still lacks three new paper passages (M5B-02).

## 2. Executed checks [E]

| # | Command (cwd / inputs) | Exit | CPU | Result |
|---|---|---|---|---|
| E1 | `cp -p code/onset512_analytic/* $A/m5b-code/onset512_copy/` (check.py `ff2859ee…`, receipt `fd8bd62b…`); `python3 -B check.py > run.out` (Python 3.13.18) | 0 | 0.2 s | `assertions PASS`. P512_max [0.040785,0.040786], P512_half [−0.143070,−0.143069], vertex [0.147341,0.147342], G512_one [0.534264,0.534265], G192 [0.098316,0.098317], floor295 [0.050064,0.050065], kappa_K3 [0.917166,0.921489], Cstar [1.841232,1.847940]. **All nine fields equal the receipt**; run.out `bd22eb01…` |
| E2 | `PYTHONPATH=$A/../audit3/pylib python3 -B m5b-code/base_table.py`. Uses mpmath 1.3.0 `iv` at 80 digits with its own π and log, plus exact `Fraction`. Formulas transcribed from uc:constants, uc:uniform-allowance, uc:analytic-norm, Cor 4.6/4.7 and Lemma 4.9; check.py is not reused | 0 | 0.1 s | **60/60 table entries contain the true value; each is the tightest outward 6-decimal enclosure.** 𝒢(512,1)=0.5342647023 (ratio 0.04740<3/50<tan½); 𝒢(192,π/2)=0.0983189868 (ratio 0.09801<1/10); max 𝔭₅₁₂=0.0407859998 (margin to 40786·10⁻⁶ is 2.4·10⁻¹⁰); 𝔭₅₁₂(½)=−0.1430696691; vertex 0.1473414757<3/20; d_x(512)>1; 0<d_β<5/48; x*=0.2763, y*=0.2237. Coarse corner chains, exact: δ_A−r_UM ≥ **2729/21000**, δ_D−2r_UM ≥ **49/1000**; true values at 256 are 0.3219 and 0.1991. r_U=2/125>π⁴/6144=0.015854. Companion substitutions exact: 𝔗(256) bound = 6501467/605000 > 107/10; K_D(256) bound = 240503/1205760 < 1/5; M(256) bound = 12590867/492980 < 26. log π=1.14473>11/10 |
| E3 | `python3 -I -B m5b-code/kernel_checks.py` (floating point, MEASURED) | 0 | <0.1 s | Lemma 2.1 sentence p(z)=Σ_B w_B p(B)K̃_n(z,B) holds for n=1..7 (err 1.3e−15); product-form kernel equals definition (eq:angular-kernel) for n=1..9, including collisions with R_ℓ(jπ) (err 8.7e−13); sine product with constant 2^{n−1} (3.5e−15); 𝒟_n(π,π)=(−1)^n(2n+1) exact for n=1..11; companion Q_v folding identity (err 1.3e−15) |
| E4 | `python3 -B companion-paper/check_correspondence.py` (repo root; read-only, git show) | 0 | 0.15 s | PASS against baseline ad908acb: 19 statements, 85 numbered displays, 116 labels, bibliography |
| E5 | `python3 -I m5b-code/containment.py` (paper sentences added since 24a98db, searched in the companion) | 0 | <1 s | 77 raw misses, almost all paraphrases. Real omissions are listed in M5B-02 |
| E6 | `pdftoppm -r 80` paper p.41, companion p.114; viewed B5's paper-p18/p54 and companion-p51 renders | 0 | — | Table 1 floats into the Cor 4.7 proof and is legible. The trust table renders cleanly. In the paper's Fig. 2 the hypotenuse still crosses both labels (M5B-06) |

The total metered CPU is well under one minute, against a cap of about 30 CPU-minutes. No native engine,
archive code, Syvert job or Git state change was involved.

## 3. Audit-04 findings in range: reconstruction of the changed text

**C4D-01 (corner losses): FIXED in both texts [D].** The companion's chain is complete. In the paper the
chain is shorter, but it is now present (paper loc 388–425; companion 1060–1105).

- *Axis vertices.* (uc:relative-comparison) holds on ρ ≤ 1 for n ≥ 160, and h = π/4 < 1. It gives
  Λ_c − S_n ≥ uU_W − E_c − C_4 − k_Wx·x − k_Wy·y.
  - U_W = 𝔗 − ē + A_4 + ρJ_W + 𝔧 ≥ 𝔗 − ē + 𝔧, because A_4 ≥ 0 and J_W ≥ 0.
  - On the axis 𝖺 = (1 + cos h)/2, so u = (1 − cos h)/2 = 0.14645 > 7/48.
  - 𝔗 − ē + 𝔧 > 0 at n ≥ 256 (10.68 at n = 256), so u may be replaced by q_h.
  - Since d_β = (17L+27)/n² > 0, k_Wy = k_Wx + d_β ≥ k_Wx. So h·k_Wy pays for both axes: k_Wx·h at
    (h,0) and k_Wy·h at (0,h). This is the "why k_Wy serves both axes" point.
  - E_c(h,0) ≤ (4·319/360/π²)·p^{3/2}/√𝖺 = 0.2311 < 6/25 < 1/4. E_c(0,h) = −B_β ≤ 0.
  - Hence both axis losses exceed δ_A.
- *Diagonal vertex.* Λ_c − S_n = [M_∞(0) − M_∞(h,h)] + E_n(0) − E_n(h,h).
  - (uc:completed-model), (uc:model-loss) and (uc:regular-loss) give the model loss
    ≥ (4u/π²)L² − (3u/π²)L + 𝔧u − E_c = u(𝔗 + 𝔧) − E_c. This holds on the closed domain
    ρ ≤ π/2, and ρ = π/2 here.
  - E_n(0) > −ē, and −E_n ≥ −C̄_E − K_D·P.
  - At this vertex u = 1 − cos h = 0.29289 > 7/24, P = √2 < 3/2 and E_c ≤ (9/25)/√2 < 4/15. Hence the
    loss exceeds δ_D.
- *Assembly.* With c = 32δ/π² and U = V = π²/32, the vertex losses are cU = δ and c(U+V) = 2δ. The
  squared-Peano coefficient (16/π²)(δ − Mπ⁴/6144) > (16/π²)(49/2000) > 49/1250 > 1/30.
- *Re-entry table.* The companion's "Returning to the comparison outputs" now lists Lemma uc:master
  (model loss) and Lemma uc:central-pair (the E_c bounds). FIXED.

**C4D-02: FIXED [D].** Both paper sentences are now in the companion (loc 610–611 and 879–880).

- The parity equivalence: m̄ + q ≡ 1 − m̄ + i ⟺ q ≡ 1 − 2m̄ + i ≡ 1 − i (mod 2).
- The ambiguous phrase "accounts for precisely this change" was replaced.

**Strict positivity, interior only, with closed-boundary continuation (paper comparison 1121–1127),
spot-checked [D].**

- f_j = 4𝖺/(w² − z²) is positive iff |z| < w when 𝖺 > 0.
- 𝖺 = cos(ρ/2)cos((x−y)/2) > 0 on ρ < π.
- At 𝖺 = 0 the text correctly falls back on the sinc continuation.

**C4A-04: FIXED in both texts [D].**

- B(x) = cot(πx) − 1/(πx) + 1/(π(1−x)). On (−1,2) its only poles are at 0 and 1, where the residues
  cancel.
- So B ∈ C^∞(−1,2) ⊃ [−1/4, 5/4] (paper corner 150–152 and 522–525; companion 282–286).

**C4A-05: FIXED, not circular [D].**

- ψ′(1/2) = π²/2 comes from the finite csc² identity.
- ζ(2) is then derived from ψ′(1/2).
- ψ(1/2) = −γ − 2 log 2 comes from the recurrence and 2H_{2R} − H_R = log R + γ + 2 log 2 + o(1). That
  limit needs only H_k − log k → γ.
- The old display, which ran ζ(2) → ψ′(1/2), is gone.

**C4A-06: FIXED in the companion, and items 2–7 also in the paper [D][E].**

- Item 1: (−1)^p cos pθ = cos p(π−θ), with T_n(−1)T_n(cos θ_j) = (−1)^{n+j}.
- Items 2–3: with (−1)^k = −(−1)^j, the numerator is ½(−1)^j(2 + cos θ + cos φ). Subtracting
  (−1)^j(cos θ − cos φ) gives 2(1 + cos φ).
- Item 4: shell |p|+|q| = s has 4s points, so 1 + 4Σ_{s=1}^{n}(−1)^s s = (−1)^n(2n+1). Verified exactly
  for n ≤ 11 [E].
- Item 5: Euclid gives n | j.
- Item 6: ∫₀¹ t sin(tz) dt = −cos z/z + sin z/z², so z cos z − sin z = −z²∫₀¹ t sin(tz) dt. Then
  sin(tz) = tz·sinc(tz) gives the sinc formula.
- Item 7: the companion's proof is complete. Π(1 − Xω^ℓ) = 1 − X^n, 1 − e^{2iθ} = −2ie^{iθ}sin θ and
  Π e^{iℓπ/n} = i^{n−1} give Π sin = 2^{1−n} sin nz. Checked [D] and [E].
- Item 8: log(k+1) − 1/(2(k+1)) = log k + 1/(2k) + O(k⁻²).
- Item 9: done.
- Item 10: the cryptic S_u sentence was deleted. The retained telescoping identity was checked at R = 1
  and by differences [D]; it gives S_u = 1 + 2 log 2 − π²/4.

**P4-01: FIXED in the paper [I].**

- "Proof of Theorem 1.1" now applies Thm 4.10 for n ≥ 512 and Prop 5.3 for 2 ≤ n ≤ 511 (cert 493–497).
- Figs 1 and 2, Table 3, Lemmas 4.1 and 4.2 and Prop 3.2 are now cited.
- **The companion did not receive the proof** (M5B-02).

**P4-04: FIXED [D].**

- In u = πa/n and v = πb/m every signed sum is a 2π-periodic trigonometric polynomial of degree ≤ n in
  each angle.
- The chain rule then gives (π/n)²n²M = π²M and (π/m)²n²M = π²μ²M.
- The exponential-type citation is no longer load-bearing.

**P4-05: the table is correct ([E] E2).** Its provenance and placement have gaps (M5B-05).

**P4-06 / J1-02: FIXED in both texts [D].**

- *Cor 4.6.* Let h = ρ/2, δ = (x−y)/2 and C = t* + 2K_D. Then
  u𝔗* − t* sin x − K_D(sin x + sin y) = 𝔗* − (A cos δ + B sin δ), with A = 𝔗* cos h + C sin h and
  B = t* cos h, checked by angle addition.
  - On [h₁, π/2] both A and B are nonnegative and nonincreasing, using tan h ≥ tan h₁ ≥ C/𝔗*.
  - Hence R(h) ≤ R(h₁) ≤ A(h₁) + B²/(2A) ≤ A(h₁) + t*² cos h₁/(2𝔗*), because A(h₁) ≥ 𝔗* cos h₁.
- *Cor 4.7.*
  - u ≥ 11(x²+y²)/48, and x^{3/2} ≤ x² + x/4 by AM–GM.
  - u ≥ 0, 𝔧 > 𝔧* and U* ≥ 0 are now stated.
  - ℓ_x − ℓ_y = 5/48 − d_β ∈ (0, 5/48), with d_β decreasing.
  - Together these put x* and y* on the fixed segment, which the pointwise-monotonicity argument needs:
    off the segment ℓ_x·x increases with n when x < 0.

**P4-10: FIXED [I].** The paper now says the model comparison controls the envelope and the selected
reflected pairs bound the lost cancellation from below; the companion is equivalent. The abstract is
accurate.

**J2-01: FIXED in the text.** The input list (paper comparison 114) now has 11/10 < log π < 23/20, and
log π > 11/10 is stated where it is used (199). See M5B-05(d) for the checker attribution.

**J2-03 and J2-09: FIXED in the paper.**

- check.py and receipt.json are named (paper comparison 125–129; trust table).
- "Numerical values; not used in any proof" now appears in the paper abstract and introduction and in
  the companion introduction. **It is not in the companion abstract** (M5B-02).

**Evidence language (C4D-03/04/05/06/07, J3-01) [I], checked against J03 L196–262, the G01 2026-11-13
addenda, local-onset512-summary L12–45 and compact-return.**

- *Supported in the paper:*
  - "471 distinct trees, each recorded twice; the second record adds native replay redundancy".
  - "No stored native numerical endpoint is a premise or is asserted valid", which matches
    `all_native_endpoints_validated:false`.
  - The four-column trust table.
  - The exact clipped-polygon maximum, with a correct singular-Hessian argument [D].
  - The R_ℓ product form, which is 𝒟_n − cos(nu) from §3 with s = u₊ and t = u₋ [D][E], and its
    removable values R_ℓ(jπ) = ℓ(−1)^{j(ℓ−1)} [D].
- *The 191 new pairs.* The statement that primary and fresh records carry identical trees and keys rests,
  for these pairs, on the local summary's record ("retained proof fields agreed"). It was not
  data-checked: the canonical ZIP is absent, as J03 L253–254 says.
- *The Popen/ECHILD limitation* is correctly kept in J03 L257–261. The manuscripts make no
  waitpid-level exit claim, so nothing needed to change there.
- *Companion residues:* the custody text (M5B-01), the "Rounding model" cell (M5B-03) and the "I25"
  jargon (M5B-07).

**C4D-14: FIXED [D][E].** The folding display is correct.

- Pairs k′ ↔ −k′ in ℤ_{2m} give two representatives of weight η_k.
- Homogeneity gives 𝔡(2·), so (1/4N)·2η_k·2 = η_k/N.
- The parity condition r + k ≡ J (mod 2) follows from J + K odd.
- At k = 0 and k = m the two indices coincide, so the defect is zero.

**C4D-12: FIXED and exact (E2).**

**Lemma 4.8: FIXED [D].**

- A* (the numerator floor) and A♯ (the upper bound for A(b₋)) are now separated.
- C was renamed A(0) = a_ρ̄ − ρ̄/2, which is consistent with A(b) = a_ρ̄(1 − sin b) − ρ̄/2.
- A(b) ≥ (15/16)(1 − 71/100) − 1/4 = 7/320 > 0.
- The discrete layer-cake statement is correct and is used correctly.

**Theorem 4.10: correct [D].**

- The four regions are noncorner ρ ≤ 1/2 (λ_n < Λ_c − 9/1000, using Q > 1/20 from n ≥ 295), 1/2 ≤ ρ ≤ 1
  (𝔭_n(1/2) < −1/7, since the vertex is below 1/2), ρ ≥ 1 (𝒢 > 1/2), and corner charts with ρ ≤ 1/2
  (A, B ≤ 1/2 < π/4).
- Odd endpoint pairs: (n,m) ↔ (−1,−1); (0,m) ↔ (1,−1) for even n; (n,0) ↔ (−1,1) for odd n. Checked
  against the introduction's parity rule.

**Renames [D] (map `paper/notation-renames-audit04.json`, 31 entries; 12 in range).**

- e_j,f_k → ε_j,η_k: the same weights as §2. w_jk = 2ε_jη_k/𝖭 equals §2's 2ε_jη_k/(n(n+1)).
- P_n(ρ) → 𝔭_n. The kernel P_n = T_{n+1} + T_n is correctly kept in the divided-difference formula.
- The other renames are G → 𝒢, Θ → 𝔗*, U → U*, j* → 𝔧*, C → C_rem (Thm 1.2) and C → C_Λ (its proof).
- Meaning is preserved everywhere. No residual old token appears in loc, cert or the gates subsection
  (grep).
- The map is a scanner aid. Its literal `P_n(` entry for localization would also match the kernel's
  P_n(cos u) if applied textually. The source correctly does not apply it there.

## 4. Findings

### M5B-01 — MAJOR (companion; evidence custody) — stale claims that absent evidence is "retained"
- **Location.** Companion certification-unified.tex 1623–1629 (p.≈144):
  - "All essential certificates and the independent verification records are retained."
  - "Full histories for the other degrees remain at their recorded computation sites."
  - "The compact returns additionally include …", which is undefined jargon.
- **Reason [I].** The current records contradict these present-tense custody claims:
  - Handoff 32 ("Still absent"): the onset512 return, the I25 evidence ZIP and the 632 MiB unsampled
    histories are missing, and AC does not know where the I25 ZIP is.
  - local-onset512-summary L42–43: "their present availability is unverified".
  - G01, 2026-11-13 limitation.

  The paper's matching passage was rewritten (P4-08). The companion's was not, although response-04
  rows P4-08 and C4D-13 read DEVELOPED.
- **Impact.** The companion would tell readers that evidence is retained which the project currently
  cannot locate or retrieve. This is exactly the blanket custody claim handoff 32 excludes. It affects
  no theorem.
- **Fix.** Replace 1623–1629 with the paper's text (cert 505–509, "…identified by the inventories in the
  package… Selected native histories are auxiliary provenance; they supply no numerical premise…") and
  drop "compact returns" and "recorded computation sites". The edit is wording only, but it is an
  evidence-status statement, so it should be returned to development rather than fixed by the auditor.

### M5B-02 — MINOR (companion fidelity to the revised paper)
- **Location and reason [E5][I].** Paper additions absent from the companion:
  - (a) the explicit **Proof of Theorem 1.1** (paper cert 493–497). The companion still ends with
    "Section 4 supplies the analytic proof for every n ≥ 512. Together these ranges cover every integer
    n ≥ 2" (1609–1610). In the companion `ul:tail-location` and `cert:finite-verification` are never
    cited, so P4-01 is fixed only in the paper.
  - (b) Thm 4.10's naming of the physical corners, "corresponding to (−1,−1) and respectively (1,−1) or
    (−1,1)" (paper loc 473–474; companion 1194). P4-12 is likewise paper-only.
  - (c) the companion abstract (main.tex 36, 39) lacks J2-09's "numerical value is not used in any
    proof" and keeps P4-09's "retains the cancellation lost".
- **Impact.** The companion is meant to contain every paper sentence (C4D's containment standard). A
  reader of the companion alone finds no assembled proof of the main theorem.
- **Fix.** Copy the paper's proof block, the corner clause and the abstract qualifier. All are prose; the
  correspondence baseline is unaffected for numbered blocks.

### M5B-03 — MINOR (companion trust table) — an assumed model listed as "proved"
- **Location.** Companion cert 1564, "Interval endpoints | Rounding model and error bound derived below
  | …".
- **Reason.** The IEEE binary64 round-to-nearest model is an assumed trusted semantics. J3-09 and the G01
  dated addendum say so explicitly. Only the 84ε_fp·t enclosure is derived under it. The paper's
  corresponding row is correct.
- **Fix.** Write "Error bound derived below (under the assumed IEEE model)". The model stays in the
  implementation-trust column.

### M5B-04 — MINOR (companion §3.3; C4A-01 consolidation removed unique reasons)
Each item below is a one-line reason that the consolidation deleted together with its duplicate [D].
- (a) Corner 1077, "+O(z⁻²), where the bound is independent of J". The deleted reason was that each
  unit-cell trapezoid error is ≤ (1/8)∫|f″|, so the total is ≤ (1/8)∫₀^∞ 2(z+t)⁻³ dt = 1/(8z²).
- (b) Corner 1402, "The exact formula for F gives R(1−y)=A₁+yb log y". The recurrence
  ψ(y/2) = ψ(1+y/2) − 2/y, which supplies the 2/y and hence A₁(0) = π − a·d₀, is no longer stated.
- (c) Corner 1196 and 1212, "the infinite-interval midpoint estimate" and "proving the stated estimate".
  The estimate ψ′(r+½) = 1/r + O(r⁻³), equivalently |ψ′(r+½) − 1/r| ≤ 1/(3r³), is no longer stated, so
  both phrases have lost their antecedent.
- (d) Corner 1692. The step C_Λ = κ cites "the earlier independent mesh comparison", not
  \eqref{cu:kappa}, which is now cited nowhere in the companion.
- (e) Corner 823–841. κ is used as the name of 4ΣΣ∫h_{σ,ℓ} before the pairing identifies it with
  (eq:main-kappa), and "we have proved (cu:kappa)" precedes that identification.
- (f) Corner 1020 and 1065. "A derivation of (cu:psi-est) follows after the half-integer calculation"
  is out of order: it follows the ψ′(½) calculation and precedes ψ(½). "Can also be viewed" now
  introduces the only derivation.
- **Impact.** No mathematical gap; each fact is true and nearby. AC's criterion, no hidden step, is not
  quite met.
- **Fix.** One clause each. In (e), write κ_∞ until the pairing.

### M5B-05 — MINOR (paper and companion; base-value table and checker attribution; the numbers are correct)
- (a) Table 1 ("Outward rational enclosures…", paper comparison 1728ff, p.41; companion 4012ff) has no
  `\label` and is cited nowhere, although it is the hand-check record for Cor 4.6, Cor 4.7, Lemma 4.8
  (F_h(295)) and Lemma 4.9 (n = 256).
- (b) It is placed, and its caption ("the same coefficient formulas") is written, before Cor 4.7 defines
  U*, d_x, d_y, ℓ_x, ℓ_y. The role table only names them.
- (c) Its provenance is not stated. The executed `check.py` receipt does not contain these 60 values; per
  supplementary-manuscript-review L88 they were computed by calling its API ad hoc. P4-05 asked for "one
  sentence identifying the … checker as the executed record".
- (d) The elementary-constants paragraph says the listed consumed comparisons "are evaluated by …
  check.py". check.py asserts log π < 23/20 but **not** the newly added 11/10 < log π (J2-01).
- **Fix.**
  - Label the table and cite it from the gate proofs, Lemma 4.8 and the corner lemma; add "(defined in
    Corollary 4.7)".
  - Caption: "computed with the exact interval routines of check.py; these intermediate values are not
    part of its receipt" (or add a receipt).
  - For (d), add the hand reason log π > log(157/50) > 11/10, since e^{11/10} < 3.01.
  - All entries are confirmed by E2, and none needs to change.

### M5B-06 — MINOR (paper Fig. 2; B4-01/P4-14 partly fixed) — labels still crossed by the hypotenuse
- **Location.** Paper loc 134–136. Rendered at 500 dpi (B5 `paper-p18-fig2-zoom500.png`), x+y = π passes
  through "gate" and between "ρ" and "≤1".
- **Fix.** Use the companion's placement (labels outside the triangle, `fill=white`, arrows).

### M5B-07 — MINOR (first use and notation slips introduced by the response; wording only)
- Paper cert 396 uses ε_fp in the new IEEE paragraph. It is defined only at 407 ("Let ε_fp = 2⁻⁵³"),
  so move the definition up.
- Paper prelim 79: w_B is undefined; §2 defines w_jk.
- Paper cert 374–379 defines R_ℓ(x) with x, the reserved phase symbol. The same paragraph uses
  t = (v−u)/2 and then, at 408, "t" for the rounded reduced argument.
- The companion uses the internal label "I25" three times (cert 1186, 1496, 1570) without defining it;
  write "the independent phase checker".
- Paper data statement (main.tex 82–84) and companion (main.tex 88–89) cite a433c7d. The companion says
  the "manuscript and checker sources are available in the pinned repository snapshot …/tree/a433c7d".
  Per zenodo-deposit/README 30–33, a433c7d holds the 24a98db manuscripts and pre-repair reader and is
  "not a final reviewed source snapshot"; a new snapshot is pending. The data statement needs the
  post-repair snapshot (AC decision) or must call a433c7d historical.

### EDITORIAL / NOTE (no action required for correctness)
- **M5B-E1.** Paper cert 221–222, "…leaf ratio yields / The \emph{tree norm} is (85)", renders as
  "yields The tree norm is" (B5 text p.≈50). Delete "yields" or "The … is".
- **M5B-E2.** The paper states the inward-phase sentence twice within about 25 lines (loc 79–80 and
  102–103).
- **M5B-E3.** Paper corner lemma.
  - The axis display omits "A_4 + ρJ_W ≥ 0" and the positivity of 𝔗 − ē + 𝔧 needed to replace u by
    q_h; the companion has both.
  - The diagonal chain names "model loss, origin lower bound and absolute error" without citing
    Lemma uc:master, (uc:origin-lower) or (uc:global-error).
  - The Peano variables u₁, u₂ sit beside u = 1 − 𝖺 in the same proof.
- **M5B-E4.** The paper's Cor 4.6 proof states A′ ≤ 0 twice in consecutive sentences.
- **M5B-E5.** The weights in L_n are d_r in the paper (corner 231) but δ_r in the companion (504). δ_r
  also meets δ = v₀ − v₁ and the strip width δ in companion §3.2.
- **M5B-E6.** The paper trust table's "Proved in the text" cell lists "rational sine bounds", but the
  paper only outlines the 84ε bound and still says "the arithmetic proof in the reproducibility package"
  (cert 412). J3-08's response says the pointer is explicit; it is explicit only inside the companion.
  Cite the companion section from the paper.
- **M5B-E7.** The trust tables differ in structure: the paper has a separate "Elementary bases" row and
  the companion merges it into "Analytic branches". Both are accurate apart from M5B-03.

## 5. Response-04 dispositions in range, checked against the text

| Row | Response | Verified state |
|---|---|---|
| C4D-01 | DEVELOPED | **Supported** (both texts, §3) |
| C4D-02 | DEVELOPED | **Supported** |
| C4D-03/J3-01 | DEVELOPED | **Supported**; companion jargon M5B-07 |
| C4D-04 | DEVELOPED | **Supported** |
| C4D-05 | DEVELOPED | Paper supported; companion cell wrong (M5B-03) |
| C4D-06/07/08/09/10/11/14 | DEVELOPED | **Supported** |
| C4D-12 | VERIFIED supplementary | **Supported and independently exact** (E2) |
| C4D-13 | DEVELOPED scoped | Partly: companion custody text kept (M5B-01) |
| C4A-01 | DEVELOPED | Consolidation done, three unique reasons lost (M5B-04) |
| C4A-02/03/07/08 | DEVELOPED | **Supported**; δ_r note (M5B-E5) |
| C4A-04/05/06 | DEVELOPED | **Supported** |
| P4-01 | DEVELOPED | Paper supported; companion missing (M5B-02a) |
| P4-03/04/06/10 | DEVELOPED | **Supported** |
| P4-05 | VERIFIED supplementary | Values **supported** (E2); provenance/labels open (M5B-05) |
| P4-08 | DEVELOPED | Paper supported; companion not (M5B-01) |
| P4-12 | DEVELOPED | Paper supported; companion missing (M5B-02b) |
| P4-14/B4-01 | DEVELOPED | Companion fixed; paper Fig. 2 still collides (M5B-06) |
| P4-16 | DEVELOPED | **Supported** (outline 77+1+6=84) |
| J2-01 | DEVELOPED | Text supported; checker attribution M5B-05(d) |
| J2-03/J2-09 | DEVELOPED | Paper supported; companion abstract M5B-02c |
| J3-08 | DEVELOPED | Partly (M5B-E6) |
| N4-01/02 (range items) | DEVELOPED | **Supported**: ρ, x, y, A, B, 𝔭_n before the roadmap/figure; Li₂ and U_{n−1} defined; Lemma 5.1 quantified with W_z and I_RW defined; discrete layer cake, sine product, Fourier uniqueness (Katznelson) and binary64/Higham stated. New slips M5B-07 |
| N4-12 | VERIFIED | **Supported** (E4) |
| C3-09 / C3-02 (reopened) | DEVELOPED / recheck due | **Now supported** |

None of these rows is labelled FIXED in my range. The only VERIFIED claims (C4D-12, P4-05, N4-12) are
borne out numerically. The partial rows above are where a DEVELOPED label overstates what changed in the
companion.

## 6. Coverage and limits

- **Read in full.** Every changed hunk of `git diff 24a98db ad908acb` for both texts' introduction,
  preliminaries, corner, localization and certification, both main.tex and the bib. I also read the
  surrounding context of each hunk: paper loc 1–484 in full, paper cert 1–510 in its changed regions,
  companion corner 495–905, 960–1100, 1185–1440, 1560–1700, companion loc 270–370, 380–640 and
  1040–1200, and companion cert 1160–1270, 1400–1640 and 1820–1846. For the gate corollaries I read
  paper comparison 1630–1840 and the definitions at 1–30, 85–130, 408–445, 576–600 and 636–720.
- **Not covered.**
  - The §4.1–4.2 comparison deltas (C4B/C4C) beyond the gate corollaries, the strict-positivity spot
    check and the definitions consumed here.
  - The E4 reader and the code.
  - Unchanged analytic components (Thm 4.5 charges, §3.3 aggregate constants, Lemma 4.2), which were not
    re-derived.
  - Companion lines outside the hunks listed above, which were not read line by line.
- **Data access.** No new-range (320..510) certificate, I25 bundle or onset512 return was available. The
  "same tree" statement for the 191 new pairs therefore rests on the recorded local summary.
- **Status of numerical checks.** E3 is floating point and MEASURED; it confirms identities that are
  proved [D] and confers no status. E2's interval and Fraction results are rigorous for the numbers they
  check.

Scripts and outputs: `$A/m5b-code/` — `base_table.py` (`dd753ffa…`) and `.out` (`41efeacd…`),
`kernel_checks.py` (`ed64f478…`) and `.out` (`74b92527…`), `containment.py` (`01a46e5e…`) and `.out`
(`706646d7…`), `onset512_copy/` (byte copy and `run.out` `bd22eb01…`), `trees/` (24a98db and ad908acb
`git archive` extracts), `png/`.

2026-11-13 · Claude Opus 5.5 (instructed xhigh; effective effort not exposed) · rules read at 33b9eca.
