# C4B: companion §4.1 and start of §4.2 (comparison-unified.tex lines 1–2050)

Auditor: Claude Opus 5.5, xhigh effort. Independent subagent in the substantive Claude audit-04 (handoff 30).
Rules read at branch head `70a50d7b2a72a30fd7a2af3b2ead54ae14470bf9`: AGENTS.md, agents/WORKFLOW.md,
agents/claude/CLAUDE_ROLES.md, handoff 30, claude-audit-brief-onset512-20261108.md, companion README/BUILD/review.md/CORRESPONDENCE-REVISION.md,
audit-03/c2a-companion.md, response-03.md (C2A rows), paper/section4-onset512-response.md, notation-pass.md, J01 (definitions and contracts).

Target: `companion-paper/sections/comparison-unified.tex`, SHA-256 `78a5b1b9…55a5`. It is byte-identical at the freeze
`24a98db4` and at HEAD `70a50d7` (`git diff 24a98db..HEAD` touches no TeX/Bib). The audit-03 version (`ac945041`, SHA `6fa8e0b2…a092`)
was diffed against it (`c4b-code/diff-comparison.txt`) so that every changed passage could be identified.
Paper counterpart: `paper/sections/comparison-unified.tex` at the same freeze.
No state-changing git command was run and no repository file was written. All outputs are this file and `c4b-code/`.
Pages refer to B4's fresh build (`build/companion/main.pdf`, `build/text/companion.txt`, `build/page-index.md`).
My range is companion pp. 52–80: §4.1 runs pp. 52–71 and §4.2 starts on p. 72.

Labels: [D] means derived by hand here. [E] means executed here, with the script named. [I] means inference or judgment.
Numerical checks support an inequality only at the sampled points. They are not proofs.

## Verdict

**Mathematics in lines 1–2050: sound. No BLOCKING finding.**
- I re-derived every changed or added derivation in the range:
  - the row identity and pole offsets (C2A-02 fix);
  - the b_full integral identity and the cut-integral meaning of M∞ (C2A-01 fix);
  - the five-term telescope, collected term by term;
  - the weight identity C∓ = ∓c sin(πη∓)/(2 sin(v/2));
  - the ℓ_j partial fraction and its constant πD₀;
  - the cutoff recurrence;
  - the new elementary-constant rules (ul:log-series, Machin, ζ and γ brackets) and every rational consequence in (uc:scalar-constants) and the C∞<9/4 proof.
- I found no sign error, wrong constant, wrong index range or wrong quantifier.
- All 26 numbered blocks in the range are byte-identical to the paper [E `blocks.py`].
- The constants and the thresholds n≥32 and n≥160 agree with the J01 contracts.

**Companion pedagogy for this range: improved, but not yet acceptable as the teaching text AC asked for. One MAJOR finding and a cluster of MINOR findings.**
- The audit-03 MAJOR items are resolved to the extent requested:
  - C2A-01: the model's meaning and the 2D₀ link are in place, and the coefficient is no longer "proved" before its proof.
  - C2A-02: the row identity and the pole offsets are derived.
- C4B-01 (MAJOR): merging duplicated passages (the C2A-09 fix) deleted four reasons in Lemma 4.2's proof that the *paper* still states. In those places the companion is now less complete than the paper, and two sentences point to a step that no longer exists.
- Several audit-03 items that response-03 marks FIXED are only partly fixed in the text: C2A-05, C2A-07, C2A-09 and C2A-10 (details below).
- The notation pass introduced a wrong symbol (𝔗 for T_t).
- The revision introduced a paired collision of P_n.

## Executed checks [E]

Scripts and outputs are in `c4b-code/`. Python 3.13 was used with mpmath 1.3.0 (`audit3/pylib`), numpy 2.5.3 and scipy 1.18.1.
Total CPU was under 1 minute, well inside the cap.

| Script | What it checks | Result |
|---|---|---|
| r1_rational_constants.py | Fresh exact-Fraction implementation written from the companion text alone (lines 1268–1319): Machin with 40 alternating terms; log series with J=48 after power-of-two reduction; ζ(s) convexity brackets for s=2,3,4,5,6,7,9; γ from H₂₅₆; 𝔞_p, 𝔟_q, c_k for k≤3; tail 8/(3(K+2)4^{K+1}) | tail = 1/480 exactly. κ ∈ [0.91716658, 0.92148844], inside the claimed (917166, 921489)·10⁻⁶. C* ≤ 1.847939405 < 1847940·10⁻⁶ < 4629/2500. All listed brackets hold. Also log π>11/10, which is used but not listed, and γ+log(8/π)∈(3/2,8/5). Exact: 828/4925 = 2(9/5)(20/197)(23/50); H₀ lower bound 5553/19700 > 7/25; C₀>391/100; d*≥39/250; g₀<8464/24625<43/125; 𝔧>23/250; t₀<0.44131<221/500; δ=249/625; δ²+δ𝔧−t₀² = 71/6250000 exactly |
| m1_analytic.py, m1b_jump.py (30–40 digits) | (uc:f-series); (uc:f-integral); the f‴ formula; max f‴/sin(w/2) = −0.1033 < −311/71680; \|f‴\|≤0.106; f(0)=0.521<3/5; Q″(1/2)=17.658<19; 2822/81; f′ jump at π equals J₀ (0.36129077); λ₀<1/(2π); e^{1/4}≥41/32>32/25; origin identity H₀ = κ/2+(2𝔨₀/π²)log(2/π) with κ from eq:main-kappa (H₀=0.310002264407); the (uc:H) finite part directly vs paired (7e−7 at ε=1e−6); H(w)−H₀ ≤ (3−π)w²/(4π³) on 7 points; 𝒲(π−w)≥w²/4; **b_full = 2D₀+(1/π)∫(A+Ã−8𝖺/(πt))** at 7 phases (2e−31); subtracted integrand ≤ 0.810 ≤ 1 | all PASS (the first jump test used a two-sided difference across the cusp and was replaced by one-sided differences in m1b) |
| m2_rows.py | divided-difference form = eq:angular-kernel sum (n=3,7,10); **row identity**, both displayed forms (n=7,12,33, random phases/rows/samples); **offsets ≡ η∓ mod 1**; **weight identity C∓**; (uc:pole-error) for n=2…512, t∈[1e−6,0.999], max n²·err = 0.611<5; −c″(π/2)=16/π³; π²/3+π/4+1/(2π)=4.234; half-line defect max 0.298 ≤ 4/π; **ℓ_j digamma form with constant D₀**; harmonic estimate; h₂−h_n telescoping | all PASS (max deviations 1e−27 to 1e−31) |
| m3_worked.py (float64/scipy; MEASURED) | J closed forms vs quadrature (4e−8); C∞ via the subtracted integral; S_n by direct row sums; row decomposition R_r/n vs 𝒱(L,v_r) | At (x,y)=(0.4,0.3): C∞=1.801591, E∞=1.862235, b_full=1.217561; C∞(0,0)=1.846160=C*. n=160: S_n−M∞=0.0100 (allowance C̄_E+K_DP=2.349). n=512: 0.0041 (allowance 0.826). Ordinary row r=253, n=512: R_r/n=5.265493 vs 𝒱=5.265474 |
| m4_small.py, m5_examples.py | \|2cot(t/2)log sin t−(4/t)log t\| ≤ 0.454·t(1+\|log t\|); envelope constant sum 4.54≤7; min 𝖺=0.7706≥49/64 on ρ≤1; 2𝖺≥p+q on ρ≤π/2; the amplitude–phase step for C∞<9/4; worked J values | all hold. J(1,½,e)=−1.12467 for every e; J(½,2,0.1)=−8.55698; J(½,2,1.2)=4 log sin 1.2=−0.28152 |
| blocks.py | paired numbered statements and displays (35 each); refs in range | all 26 in-range blocks SAME |
| hand [D] | five-term telescope: E_row+E_out+E_ret+(d₊/π)R_log+R_mesh = S_n−M∞, collected term by term; 𝓘_F=(b_full−2D₀)L+C∞−E∞−(d₊/π)𝓛_c; cutoff primitives and −(1/3+g₀)𝖺; C*=B−g₀+2H₀; origin identity; Lemma 4.4 Tonelli/Jacobian, K(k)≤1/√(2k), I₄<319/360; Lemma 4.3 product algebra (coefficient −v* of z) | all correct |

## Disposition of audit-03 findings, checked against the text

| ID | response-03 | Actually in the text (line, page) | Assessment |
|---|---|---|---|
| C2A-01 | FIXED | 719–725 (p.62): "completed integral of the row profile … cutting at ε=π/n … E∞ … proved in (63)". 891–897 (p.65): b_full=2D₀+π⁻¹∫…, which closes the identity. "This proves the coefficient" is gone. The paper's line 290–296 and 346–351 match. | **Fixed as requested; correct [D,E].** Residual: the *row-level* reason 𝒱 is the row average is not displayed (C4B-02). |
| C2A-02 | FIXED | 1551–1569 (p.74), identical to paper 671–689 | **Correct [D,E].** It copies the paper's compressed form; the cot sum/difference identities and the solved 2×2 system are not written out. No forward pointer from (uc:row-profile). (C4B-02) |
| C2A-03 | FIXED | 1048–1063 (p.67): the stray "Therefore" is gone; factoring is correct | Fixed. The 8/π² bound is still stated three times (1038, 1043, 1048). |
| C2A-04 | FIXED | 492 (p.59) | Fixed. |
| C2A-05 | FIXED | N_L, N_R defined at 788–793 (p.64) | **Partial.** "\|N_s\|≤8" is still unexplained (in fact ≤c_e+c_d≤2). The decomposition (N_s−U₀)/t+N_s(1/(2sin(t/2))−1/t) and the sum giving 7 are not displayed. The response's "the expanded proof gives the pole decomposition" is not true of lines 826–830. (C4B-06) |
| C2A-06 | FIXED | 67–71 (p.53) | Fixed and correct [D]. |
| C2A-07 | FIXED | Only the \|f‴\| item (558–560) and the τ≤1 item (1416–1417, placed after its use) were inserted. The rational-bound items were replaced by the new elementary rules. | **Mostly not inserted.** The developer record itself says not every line was added. Remaining items are listed in C4B-06. |
| C2A-08 | FIXED | 1881–1883 (p.78) | Fixed and correct [D,E]. |
| C2A-09 | FIXED | Three of the eight listed duplicate pairs were merged. The others remain, and new ones exist (C4B-05). The merge also deleted needed reasons (C4B-01). | **Partial, with a regression.** |
| C2A-10 | FIXED | Renames applied (𝔨, 𝒱, 𝒲, f″, s_Φ, 𝖣*, 𝖺, L̄, 𝔗, 𝔧). No notation table. | **Partial.** A new collision and a wrong symbol were introduced (C4B-03, C4B-04, C4B-07). |
| C2A-11 | FIXED (partly declined) | Phase-region figure 2 (p.52) belongs to §4.3–4.5. pp.53–102 have no figure and no numeric worked example of J or of the model. | Decline recorded. NOTE C4B-09 re-recommends one figure and one table. |
| C2A-12 | FIXED | Paired blocks SAME [E] | Fine. |
| C2A-13 | DECISION | A Fubini statement was added (630–633). Abel's theorem for the series side is not mentioned. The concavity inequalities cos πt≥2(½−t) and sin(t/2)≥t/π are used without a reason. "Entropy formula" (199) is still not explained. | Acceptable; small items in C4B-06. |

## Findings (prioritized)

**C4B-01 — MAJOR (companion clarity; regression against the paper).** Merging the C2A-09 duplicates deleted reasons that the paper keeps.

Location: Lemma 4.2's proof, lines 481–486, 556–590 and 637–660 (pp. 59–61).

Reason. Four deletions, each a missing step:
1. Lines 561–590 (p.60). "The sine-ratio step follows from ordinary differentiation" and "After this substitution" refer to a step that the companion never states. The paper (lines 225–231) states it: "For 0<w≤π, monotonicity of r cot r gives sin(tw)/sin(w/2)≤sin πt. Since f(0)<3/5, split [0,1/2] at 1/4,3/8, use sin πt≤(22/7)t and t³ sin πt≤27/512, and discard the negative last part."
   - The companion keeps only the proof of R_t≤sin πt.
   - It uses "f(0)/8<3/40" (584) without any reason. In fact f(0)=𝔨₀/π, and 𝔨₀<9/5 only appears at 1298.
   - It never says what is being bounded or why: "show f‴(w)<0 on (0,π); divide by sin(w/2)>0 and use the r cot r bound."
2. Line 486 (p.59). "Thus 2Q′cos πt≤3π/4" follows the polynomial 3+34t²+3t⁴−20t>0, but the inequality that links them is gone. The missing link is t(½−t)/(1−t²)²≤3/40, which the paper states (paper 172–175). The reader also needs Q′≤5t/(1−t²)² and cos πt≤π(½−t) multiplied together.
3. Line 651–655 (p.61). 𝒲(π−w)≥w²/4 has no reason. The paper (258–259) gives it: the derivative of log cot((π−s)/4) is 1/(2cos(s/2))≥½.
4. Lines 643–660 (p.61). The concluding chain is missing:
   H(w)−H₀ ≤ λ₀(f(w)−f(0)) − (J₀/π)𝒲(π−|w|) ≤ −(π−3)w²/(4π³) ≤ 0, closed endpoints by continuity and periodicity.
   The paper states it (260–261). The companion says only "these yield the negative coefficient (3−π)/(4π³) in H(w)−H₀". This is the conclusion H(w)≤H₀ of the lemma.
5. The leftover one-sentence paragraph "The value 𝒲(π)=0 counts the atom once." (647) has lost its context. It means: the atom of df′ sits at w+s≡π, so it enters as −(J₀/π)𝒲(π−|w|), and at w=0 it sits where 𝒲(π)=0.

Impact:
- The scalar-maximum lemma (H≤H₀ and the radial decrease of f″) feeds both correlated losses and C*.
- In the companion its proof now has dangling references and missing steps that the shorter paper supplies. This is contrary to AC's "needed derivations kept" and "no step without its reasoning".

Fix: about eight lines.
- Restore the paper's sentences 1, 2 and 3.
- Add "f(0)=𝔨₀/π<9/(5π)<3/5 by the brackets in the proof of Lemma 4.3".
- State the goal before line 561.
- Display the chain in item 4.
- Fold line 647 into the sentence on the convolution formula.

**C4B-02 — MINOR (high priority; residual of C2A-01 and C2A-02).** The link between one actual row and the profile 𝒱(L,v) is never displayed.

Location: 676–725 (pp.61–62), 1551–1569 (p.74), 1756–1759 (p.76), 1873–1881 (p.78), 1924–1927 (p.79).

Reason:
- At (uc:row-profile) the reader gets C∓, η∓, A and 𝓑 with only verbal motivation. The pairing c_e↔η₋ and c_d↔η₊ is unexplained there.
- The identity that explains it, C₋=−c_e sin πη₋/(2sin(v/2)) and C₊=c_d sin πη₊/(2sin(v/2)) [D, E m2], appears about 1180 lines later and is used only for error weights.
- The decomposition that makes 𝒱 the row average is assembled nowhere in 1–2050:
  - by the row identity and |A+B|=|A|+|B|+(|A+B|−|A|−|B|),
    R_r/n = |C₋|𝒩_n(η₋)/n + |C₊|𝒩_n(η₊)/n + n⁻¹Σ_k g(C₋,C₊;X_{rk});
  - then (uc:pole-error) gives 2(|C₋|+|C₊|)L/π + [c_eΦ(η₋)+c_dΦ(η₊)]/(2sin(v/2)) = A(v)L + pole part of 𝓑;
  - and the Riemann sum of g gives I(C₋,C₊,v)/π.
- The row identity itself copies the paper verbatim. It does not show nu_{rk}≡δ_rπ+x (mod 2π), mv_r=rπ+y, (−1)^r=−(−1)^{δ_r}, cot A±cot B=2sin u, 2sin v over (cos v−cos u), or the 2×2 system C₋+C₊=p/2, C₋−C₊=−q/2−𝖺cot(v/2).
- The text cites "the divided-difference kernel (7)", but eq. (7) is the double-sum definition. The divided-difference form is the unlabeled formula at the start of §4 (localization 68–69, p.47).

Impact: the central construction of §4.1 can be checked only by assembling four passages spread over about 20 pages.

Fix:
- After (37), add a forward pointer: "By the row identity in the proof of Theorem 4.5, each row is C₋cot+C₊cot; …".
- Add the three-line display above, with the weight identity.
- Expand the row identity by the three missing lines.
- Label the divided-difference form and cite that label instead of (7).
- Worked numbers [E m3]: at (0.4,0.3), n=512, row r=253 has R_r/n=5.265493 against 𝒱=5.265474.

**C4B-03 — MINOR (wrong symbol from the notation pass).** Location: line 1146 (p.68), "For 𝔗≥0, the positive parts used here satisfy".

Reason: the old text had T, meaning T_t=2𝖺cot(t/2). The global rename T→𝔗 caught this local T. 𝔗=(4L²−3L)/π² is the model loss and has nothing to do with this inequality. (The PDF shows a fraktur T.)

Fix: write "T_t≥0". This is MINOR and eligible for an in-place auditor fix, since it is wording or notation with no claim change.

**C4B-04 — MINOR (paired collision introduced by this revision).** P_n has two meanings in §4.

Location:
- Comparison line 1555 (p.74) and paper line 675 use P_n=T_{n+1}+T_n, the Chebyshev sum defined at localization 68 (p.47).
- Comparison 3965ff (§4.3), paper 1586ff, figure 2 and its caption (p.52) use P_n(ρ), the radius-one gate polynomial.

Impact: a reader meets "P_n on ρ≤1" in figure 2 three pages before "P_n(cos u)". The notation pass had planned P(ρ)→𝔭(ρ).

Fix: rename one of them in both texts, for example 𝔭_n(ρ) for the gate, or 𝒯_n for T_{n+1}+T_n. This touches paired formal blocks, so it needs a new freeze and baseline.

**C4B-05 — MINOR (pacing; C2A-09 residual).** Claims still appear two or three times:
- 240–250 / 267–270: the endpoint value of R.
- 270–275 / 282–287: E≤Z.
- 408–410 / 489–492: c_s≥(3/4)(1−s²).
- 801–803 / 808–816: the Lipschitz difference on the complement.
- 843–852 / 853–858: X and Y introduced twice. "The next calculation independently checks" is misleading, since this *is* the derivation.
- 1038 / 1043 / 1048: the 8/π² bound.
- 1101–1105 / 1115–1119: the 3u/π² bound.
- 1133–1139 / 1144–1153: the positive-part bound and ∫|log sin|.
- 1141–1143 / 1173–1180 / 1190–1191: −(1/3+g₀)𝖺.
- 1182–1201 / 1203–1220: root-free endpoint half and C*=B−g₀+2H₀.
- 1364–1371 / 1373–1376: translation by δ.
- 1399–1400 / 1408–1411: the I₄ bound, which also switches variable r/s.
- 1774–1799 / 1800–1841: the pole estimate, summary then details.

Fix: keep the expanded version once and reduce each compressed version to a one-line roadmap *before* it. Check every deleted sentence for a reason not stated elsewhere, the failure mode of C4B-01.

**C4B-06 — MINOR (hidden steps; C2A-05 and C2A-07 residuals, and constants before derivation).** Each needs one or two lines.

Constants used before their derivation:
- The brackets γ>23/40, log2>69/100, logπ<23/20 (414), γ<3/5 and logπ>11/10 (454), 𝔨₀<2 (412), f(0)<3/5 (584), π>25/8 and e^{1/4}>32/25 (612) are all used about 850 lines before the rules at 1268–1300 derive them, with no pointer.
- logπ>11/10 is not in the "same brackets imply" list (1298–1300), although it is used at 454 and in J₀>1/π.
- Fix: move "Here are explicit rational rules…" (1268–1300) to a short "Elementary constants" paragraph before Lemma 4.2, or add a forward pointer at 412. Add logπ>11/10 to the list, and e^{1/4}≥1+¼+1/32=41/32.

Other steps:
- **612:** λ₀ needs ∫_ε^π dt/(2sin(t/2))=−log tan(ε/4), so log(ε/π)−log tan(ε/4)→log(4/π).
- **1082–1083:** 𝖺D≤(7/2)u. Apply (44) to each factor: 𝖺(𝒞_e−C₀)≤c_d(7/2)(1−c_e), and similarly for the other factor. The sum is (7/2)(c_e+c_d−2𝖺)=(7/2)(u−z)≤(7/2)u.
- **1084–1088:** "Substitution … gives exactly" needs U₀=(𝖺/π)(D+2C₀−4logπ) and 2C₀−4logπ+4log2=4(γ+log(8/π)).
- **1102–1105:** the upper bound γ+log(8/π)<8/5 does not follow from "23/40<γ<3/5, 3<π<22/7" alone. It also needs log(8/3)<1, that is e>8/3, or the J02 log brackets.
- **826–830 (C2A-05):** display the pole decomposition, |N_s|≤c_e+c_d≤2 (call 8 deliberately crude), and the sum 12/π+πt/6+(P/π)(11/4+2log(4π/t))+𝖺t(1+|log t|)/π ≤ 7+(P/π)(3+2log(4π/t)).
- **829:** the explicit bound ≤𝖺t(1+|log t|) needs explicit constants for cot(t/2)−2/t and log(sin t/t). Measured ratio 0.454 [E m4].
- **898:** "bound each subtracted integrand by one". Show 4𝖺(2/t−cot(t/2))/π ≤ 8/π² on the first piece, and the analogous estimate on the others. Measured max 0.810.
- **1193:** 2𝖺≥p+q on ρ≤π/2 follows from (cos x+cos y)tan(ρ/2)=p+q, which is stated only later at 1340.
- **1310–1311:** the amplitude–phase step: −𝔧(1−cos x)/2+t₀sin x ≤ −𝔧/2+√(𝔧²/4+t₀²).
- **1414:** 𝖺≥c_e²≥(1−ρ²/8)²≥49/64.
- **1418:** Z≤2v log cot(e/2)≤2v log(2/e).
- **537–552:** the moment calculation; the closed form of the Abel sum (the real part of z/(1+z²) with z=re^{iπt}, which conflicts with "the only use of complex exponentials" at 973); and the series-side limit r↑1 (absolute convergence, since the moments are O(j⁻³)).
- **1296:** say at the point of use that the brackets 917166/10⁶ and 1847940/10⁶ come from exact rational arithmetic, carried out by the stated checks in Table 1. At J=48 and 40 Machin terms they are not hand calculations.
- Concavity reasons for cos πt≥2(½−t) (525, 549, 560) and sin(t/2)≥t/π.

**C4B-07 — MINOR (notation; C2A-10 residual).** Notation is used before its definition, or overloaded within a few pages.
- t_d and t_e are used at 1984–1989 (p.80) but defined only at 2073–2074.
- h is π/m at 1591 (p.74, also in Q_τ and z=h(k+t)), then "h=π/n" at 1793 and 1819 (p.77), then a generic cell width at 1844.
- In the finite-product proof (p.66) 𝖪/K and 𝗄/k sit side by side: "Σ_{k=1}^{𝗄}" and "independent of 𝖪,k … tail after K … 𝖪→∞ then K→∞". In print the sans and italic letters are nearly indistinguishable.
- p and q are summation indices in (uc:kappa-series) ("c_k=Σ_{p+q=k}𝔞_p𝔟_q") inside the proof where p=sin x and q=sin y. This is paired.
- H₀ (finite part at 0) sits next to H_n (harmonic number), for example "20𝖺H_n/(πn²)" against "H≤H₀".
- w carries at least six local meanings in pp.63–80.
- v is a coefficient sum in J and also the row angle.
- e is Euler's number (612) and also the separation.
- D is the coefficient in I(C,D,e), a local sum (1082) and an allowance (1450).
- The comparison's row index r is the localization's second index s (ul:primitive); this is not stated.

Fix: a one-page table of §4 symbols at the start of §4.1 (requested in C2A-10 and in the notation pass's deferred list), plus local renames (𝗄→k_0 or q, h_n:=π/n). Define t_d and t_e at 1984.

**C4B-08 — EDITORIAL.**
- Line 495 (p.59): `$|f\prime\prime|$` renders as "|f//|" (rendered crop `c4b-code/png/crop59b-059.png`). Fix: write `f''`.
- Line 494: "The table gives Lip(f)<6/π": the Lipschitz bound comes from the first-derivative bounds 2, 5 and 4 (471–474), not from the table.
- Line 999: "independent of 𝖪,k" should read "independent of 𝖪 and k".

**C4B-09 — NOTE (figures and worked examples; C2A-11 re-stated with numbers).** pp.53–102 still contain no figure and no numerical example of J, M∞ or E_n.

Highest value: one figure of a row's samples u_{rk} against the poles ±v_r, showing the offsets η∓, plus a 6-row table. All values verified [E]:
- J(1,½,e)=−1.12467 for all e;
- J(½,2,0.1)=−8.55698;
- J(½,2,1.2)=−0.28152;
- C∞(0.4,0.3)=1.80159 < C*=1.84616;
- E_n(0.4,0.3)=0.0100 at n=160 and 0.0041 at n=512, against the allowances 2.349 and 0.826;
- row r=253 above.

Measured values only, not certificates.

**C4B-10 — NOTE (agreement).**
- All numbered statements and displays in 1–2050 match the paper.
- Thresholds in range: n≥32 (constants (53) and the absolute bound (55)–(56)) and n≥160 ((57)–(58)), the same as J01's contracts.
- The constants D, 𝓜, ē, K_D, G_g, W_n, C̄_E, A₄, C₄, d_β, J_W, k_Wx, k_Wy and U_W equal J01's definitions symbol for symbol (H↔L̄, b↔b₀).
- The consumed J02 constants κ>9/10, C*<4629/2500, 𝔧>23/250, t₀<221/500 and C∞<9/4 are stated and re-derived [E r1].
- J01's M∞(φ)−M∞(0)≤−u(𝔗+𝔧)+t₀sin x follows from (40) as explained at 901–911 [D].
- 192, 256 and 512 do not occur in this range. The H₂₅₆ bracket is unrelated to them.
- The non-circularity of the origin identity (1217–1226) is consistent [I].

## Pedagogical verdict for lines 1–2050 (pp. 52–80)

| Criterion | Verdict |
|---|---|
| Sufficient explanation | **Not yet.** Lemma 4.1 and the telescope algebra (1681–1743) are exemplary. Lemma 4.2's proof has regressed (C4B-01). The row → profile link is only sketched (C4B-02). About fifteen one-line reasons are missing (C4B-06). |
| Notation before use | Mostly. Exceptions: elementary constants (about 850 lines early), t_d/t_e, J_end/J_cen (named at 1574 and explained only implicitly), and the P_n collision. |
| Named tools stated | Good: DCT, Fubini, Tonelli, layer cake, Leibniz, Taylor with integral remainder, the trapezoid and midpoint errors, the BV half-cell kernel, the finite-product cotangent partial fraction, and Machin. Missing: Abel limit on the series side; concavity inequalities. |
| Derivations and worked examples kept | Derivations: yes, except the deletions in C4B-01. Worked examples: only "5 and −2", b_full(0)=b_c and the measured pole facts; no numerical model example. |
| Pacing and repetition | Much duplication remains (C4B-05). Lemma 4.3's proof bundles four unrelated tools: cot partial fraction, atanh, Li₂ and the constant rules. Moving the constant rules and the cot partial fraction to a short toolkit before Lemma 4.2 would shorten the proofs and fix the use-before-derivation problem. |
| Figures | None for §4.1–§4.2 (C4B-09). |

## Prioritized fix list
1. **C4B-01:** restore the four deleted reasons in Lemma 4.2 (paper 172–175, 225–231, 258–261) and state f(0)<3/5 with its source. MAJOR.
2. **C4B-02:** forward pointer at (37); display the row decomposition with the C∓ weight identity; expand the row identity; label the divided-difference form.
3. **C4B-03:** 𝔗 → T_t at line 1146 (eligible for an auditor MINOR in-place fix). **C4B-08:** f'' typo and the wording slips.
4. **C4B-06:** move the elementary-constant rules ahead of Lemma 4.2 (or add a pointer); add the listed one-line reasons. Correct the response-03 status for C2A-05 and C2A-07 to "partial".
5. **C4B-05:** merge the remaining duplicates, checking each deleted sentence for unique content.
6. **C4B-04 and C4B-07:** resolve the P_n collision (paired, so a new freeze is needed); add a §4 notation table; rename 𝗄, h and the indices p,q.
7. **C4B-09:** one row-sample figure and one worked-number table.

## Coverage and limits
- Read every line 1–2055 of the companion file. Compared the audit-03 version (full diff), the paper's §4.1–4.2 prose where relevant (paper 150–360, 640–700), localization 1–135 and 280–323, the introduction constants, preliminaries 530–545, J01 lines 1–140, response-03 C2A rows and the Section 4 response record.
- Rendered and viewed pp.59, 60, 61, 62, 66, 67, 68 and 74. Other pages were checked through the text extraction only.
- Not re-audited: unchanged audit-03-verified items that did not change. Examples are Lemma 4.1's closed forms (spot-checked again in m3 and m5) and the BV variation bounds outside the range. Lines after 2050 belong to the other agent; I read only 2160–2265 and 2073–2081 for context.
- The float64 and mpmath checks are sampled measurements. The exact-Fraction script r1 is my own independent implementation of the stated rules. I did not run the developer's `code/onset512_analytic/check.py`.
- No build was run by me (B4's artifacts were used), and check_correspondence.py was not run.
