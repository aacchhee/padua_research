# C2A: companion §4.1 and start of §4.2 (comparison-unified.tex lines 1–2050)

Auditor: Claude Opus 5.5, xhigh effort. This is an independent subagent in the substantive Claude audit (handoff 28).
Rules read at f366535e1fa4ede566cb83bdc554220c12b307cf: AGENTS.md, agents/WORKFLOW.md,
agents/claude/CLAUDE_ROLES.md, claude-audit-brief-20261108.md (§3 in full), companion README/BUILD/review.md.
Target: `topics/padua-argmax-bridge-20261105/companion-paper/sections/comparison-unified.tex`,
SHA-256 `6fa8e0b2…a092`. This equals the frozen identity in review.md; the file last changed in 5d9d2b92.
Paper counterpart: `paper/sections/comparison-unified.tex`, SHA-256 `be20756e…50ce`.
No state-changing git commands were run and no repository file was written. All outputs are in this file and `c2a-code/`.
Page numbers come from X's build (`build/companion/main.pdf`, `build/text/companion.txt`, `build/page-index.md`).
My range covers companion pp. 50–81: §4.1 starts p. 50 and §4.2 starts p. 70.

Labels: [D] means derived by hand here. [E] means executed numerically here, with the script named.
[I] means inference or judgment. A numerical check supports an inequality only at the sampled points. It is not a proof.

## Verdict

**Mathematics of the added explanations: sound.** I redid every added derivation, worked example and rational constant in lines 1–2050.
That covers about 1024 added non-paper lines out of 1926 non-blank lines (`c2a-code/added_lines.txt`).
I found no sign error, wrong constant, wrong index range or wrong quantifier in any added argument.
There are three small imprecisions: C2A-04, C2A-08, and the "ℓ=1 term" wording in C2A-03.
All numbered blocks in the range match the paper (X's block-diff reports NO PROBLEMS).
I also cross-checked them numerically (see Executed checks).

**Pedagogy for a reader with some university analysis: good locally, two MAJOR structural gaps.**
- The local roadmaps are a real improvement over the paper. Examples: "The task of the comparison model", "What is being cancelled", the interval table for J, "Uniform control near an endpoint", "Keeping phase losses together", "Reading the five-term decomposition", "Algebra of the telescope".
- The cotangent partial fraction is derived from a finite product, and the BV cell kernel is given explicitly. Both are exemplary.
- MAJOR gap 1: the reader is never told where the completed model M∞ comes from. The text claims "This proves the coefficient" before the link that actually proves it (C2A-01).
- MAJOR gap 2: the row identity that all of §4.2 rests on is stated without derivation (C2A-02).
- Secondary problems:
  - the expansion was interleaved with the original compressed prose, so many claims appear two or three times, and one sentence is broken in the PDF (C2A-03, C2A-09);
  - notation is heavily reused (C2A-10);
  - about fifteen elementary numerical bounds are asserted without their one-line reason (C2A-07);
  - pp. 50–110 contain no figure at all (C2A-11).

## Executed checks [E]

All scripts and outputs are in `c2a-code/`. The environment is Python 3.13 with mpmath 1.3.0 and sympy 1.14 (`audit3/pylib`) and scipy 1.18.1. Total CPU use was under 2 minutes.

| Script | What it checks | Result |
|---|---|---|
| v1_cancellation.py | J closed forms (s≤v entropy; s>v root and beyond-threshold) against direct 30-digit quadrature of I over 64 random and special (v,s,e); R≤0; \|R\|≤max(2v,s+v)log2; R_s and R_e formulas (central differences); \|R_s\|≤log((v+s)/\|v−s\|); 0≤R_e≤2v cot e; E≤Z with equality for s≥v; R(v,s,0+)=2(c log c+v log v−b log b); I(−w,w,t)=4w log sin t | max \|J_direct−J_closed\| = 4e−30; 0 violations |
| v1b_reflect.py | I(C,D,e)=I(D,C,e)=I(−C,−D,e)=I(C,D,π−e) | agree to 1e−8 |
| v2_scalar.py, v2b_recheck.py | C₀; f-series (35); 1/2<f≤1, Lip, \|g\|, \|f‴\|, g≤3/π², f‴<0 on (0,π) on a 400-point grid; J₀ (jump of f′ at π); Var f′; f-integral (36); the cosine-moment formula; the Abel kernel closed form and its 5/(8cos πt) bound; the f‴ integral formula; Q bounds; Q″(1/2)=28ζ(3)−16; T″ bounds; Φ″ and Φ′ maxima; the sine inequality; t(1/2−t)/(1−t²)²≤3/40; rational constants 2822/81, 608/27, −311/71680; λ₀; H by direct finite-part limit and by pairing; H≤H₀ with the −(π−3)w²/(4π³) margin on 40 points; W-representation; W(π−w)≥w²/4 | all hold. Measured: min f=f(0)=0.521252; max\|f′\|=0.2138; max\|g\|=0.1411; max\|f‴\|=0.1056; max f‴/sin(w/2)=−0.103 (<−311/71680); jump=−0.361291=−J₀; Var f′=0.855; **H₀=0.310002264407** |
| v3_kappa_constants.py | κ by the c_k series (K=64) and by direct quadrature of (eq:main-kappa); bounds on 𝔞_p, 𝔟_q, c_k; coarse input (47); **origin identity (46)**; all constants in (49); every rational step at lines 1305–1328 and 1440–1462; log/atanh bounds; I₄ | κ=0.91971011838849253510 (series and integral agree); C*=1.846160310; κ/2+(2k₀/π²)log(2/π)=0.310002264407, which **matches my independent finite-part H₀ to 12 digits**; every claimed range holds |
| v4_model_grid.py (906 phases), v4b_envelope.py, v7_small_claims.py | b_full−b_c≤3u/π²; b_full<79/(5π²); xp+yq≤4u; aD≤7u/2; (44); (45); C∞−C*≤−ju+t₀p−(H₀+v₀)z; C∞<9/4; central decomposition (41) (two independent integrals agree to 1e−8); (43); Lemma 4.4 (50)–(51); E_c(0,y)=−B_β; b≤ρ; b≥y; the envelope (39) and its four sub-bounds; the bound 10\|log sin t\|+4log2 on the E_c integrand; "subtracted integrand ≤1" | 0 violations. Largest measured ratios: envelope lhs/rhs 0.254; \|N_s−U₀\|/(12t/π) 0.080; \|I−4w log sin t\|/allowance 0.390; E_c integrand 0.22; subtracted integrand 0.811 at the origin. Smallest C∞ slack against 9/4 is 0.400 |
| v4_model_grid.py, coef block | b_full = 2D₀ + π⁻¹∫₀^π{A(t)+A(2π−t)−8a/(πt)}dt at 6 phases | holds to 1e−13 (relevant to C2A-01) |
| v5_finite.py, v5b_offsets.py | (61) for n=2..79 and 100…1000 on 801 offsets; tail braces ≤1/(3k³); the c″ series and 16/π³; half-line defect ≤4/π; ψ estimate; **row identity (line 1633) against the defining G_n sum (n=7)**; **fractional pole offsets ≡ η∓(v_r) mod 1**; the singular-sample identity; Σ\|cot(v_r/2)\| over r∉A₆ against all rows | max n²·err=0.677<5; braces·3k³≤0.993; half-line max 0.318; row identity holds to 4e−12; offsets match to 1e−14; the Σ over r∉A₆ is within bound, but over **all** rows it diverges as y→0 (C2A-08) |
| v6_cutoff_model.py | M∞ − E∞ against (1/π)∫_{π/n}^{2π−π/n}ℋ(log n,v)dv at 2 phases, n=10³,10⁴,10⁵ | \|diff\| ≤ 3e−7 (supports the explanation proposed in C2A-01) |
| v8_allowances.py, v9_example.py | numerical values of (52)–(54) at n=32…1000; model quantities at sample phases | used for C2A-11 |

## Findings (prioritized)

**C2A-01 — MAJOR (companion clarity); MINOR (paper, coordinated).** The completed model is presented without its origin, and the coefficient is "proved" before its proof is complete.

Location: comparison-unified.tex:693–766 (row profile, (37)–(38), pp. 60–61); 847–897 (logarithmic coefficient, pp. 62–63); 895 "This proves the coefficient in (38)". Paper analog: paper/sections/comparison-unified.tex:298.

Reason:
- M∞ in (38) is a definition. The reader is told what "completed" means (lines 703–708) but not why M∞ approximates S_n.
- The integral computed at lines 864–866 equals {8a log(2/π)+4a log a+2(xp+yq)}/π. The second part of b_full is (8a log2+4a log a+2(xp+yq))/π², so the two differ by 2D₀ = 2U₀/π+8a logπ/π².
- The identity b_full = 2D₀ + π⁻¹∫(A+A′−8a/(πt)) first appears 870 lines later (1760–1763, p. 75). The paper never states it.
- The conceptual reason is never given. Cutting the row-profile integral one mesh step from each endpoint (ε=π/n, so log(ε/π)=−L) turns the finite-part counterterms B₀log²(ε/π)+2D₀log(ε/π) into −B₀L²+2D₀L. [D] [E v6]
- E∞ is also introduced (p. 60) with no forward pointer to where it is identified (lines 2099–2154, pp. 80–81).

Impact: the central object of §4.1 cannot be motivated or checked when it is introduced. A careful reader at line 895 sees an apparent mismatch.

Fix:
- After (38), add: "Model meaning. With ℋ=AL+ℬ and ε=π/n one has log(ε/π)=−L, and the definitions give exactly M∞ = E∞ + (1/π)∫_{π/n}^{2π−π/n}ℋ(log n,v)dv + r_n, where r_n is the part of the finite part removed by the short end intervals. By (39), r_n=O(log n/n). Thus M∞ is the Riemann-integral version of the row average S_n=(nm)^{-1}ΣR_r, and E∞ is the completed contribution of the rows nearest the endpoint (identified in §4.2, eq. (62)ff)."
- At line 895, replace "This proves the coefficient" with "Adding the counterterm coefficient 2D₀=2U₀/π+8a logπ/π² gives b_full, as in (38)". Use the same sentence in the paper at line 298.
- Optionally include the numbers: at (x,y)=(0.4,0.3) and n=10⁴, M∞=45.27143802 and the cut integral plus E∞ gives 45.27143800 [E].

**C2A-02 — MAJOR (companion clarity).** The foundational row identity is not derived, and neither are the fractional offsets η∓.

Location: 1633–1637, p. 73 ("At regular samples the exact polynomial identity is …"). Related: 710–718, p. 60 (η∓ and the Φ(η∓) in ℬ); 1951–1956, p. 79; 2000 ("actual fractional pole offsets").

Reason:
- Every later estimate rewrites a row of G_n as C(v_r)cot((u−v_r)/2)+D(v_r)cot((u+v_r)/2).
- The companion gives no derivation and no pointer. The only similar computation appears later, in §4.3, for a different projection (localization-unified.tex:383–417, p. ≈113).
- The reader also cannot see why ℬ contains Φ(η∓(v)): the offsets of the two pole channels in row r are exactly η∓(v_r) mod 1 [D, E v5b]. This comes from the parity choice δ_r and from n v_r = rπ+y−v_r.

Concrete fix (6 lines, checked [D] and [E] for n=7, max deviation 4e−12):
- With nu=δπ+x+2kπ and mv=rπ+y, and (−1)^r=−(−1)^δ, angle addition gives
  (−1)^δP_n(cos u)=cos x(1+cos u)−sin x sin u and (−1)^δP_n(cos v)=−cos y(1+cos v)−sin y sin v.
- The divided-difference form of G_n then gives
  (−1)^δG_n/2 = [a(1+cos v)−(p/2)sin u+(q/2)sin v]/(cos u−cos v).
- With A=(u−v)/2 and B=(u+v)/2, use cot A+cot B=2sin u/(cos v−cos u) and cot A−cot B=2sin v/(cos v−cos u), together with sin v·cot(v/2)=1+cos v. This yields C+D=p/2 and C−D=−q/2−a cot(v/2), which are exactly the C, D of (37).
- The offsets follow from n(u−v)/(2π) ≡ 1/2+(x−y+v)/(2π) and n(u+v)/(2π) ≡ 1/2+(x+y−v)/(2π) (mod 1).
- Place this at p. 73, or better, right after (37) on p. 60, with a pointer from line 1633.

**C2A-03 — MINOR (editorial defect visible in the PDF).** There is a broken sentence and a duplicated estimate.

Location: 1046–1069, p. 65.

Reason:
- The paper sentence "… = 3/4−log2, by partial fractions. Therefore" (line 1048) is now followed by an inserted paragraph, "The summand identity is …". The PDF prints "Therefore The summand identity is".
- The same estimate is then displayed twice (1061–1062 and 1066–1069), joined by "This gives the following displayed estimate".
- Line 1057, "the ℓ=1 term is 1/(1−s²)", is imprecise: the ℓ=1 term of the increment is 4s²/(1−s²). The factor 4s² is absorbed into the weighted prefactor. The tail prefactor 4cs²/(1−c) also needs the remark 1−s²≤1.

Fix: delete "Therefore" at 1048, keep a single display, and write "after factoring 4s², the ℓ=1 term is 1/(1−s²) and the remaining terms are at most 3/4−log2. Since 1−s²≤1, both weighted prefactors are at most 8/π²."

**C2A-04 — MINOR (gap in an added proof).** Location: 485–488, p. 57 (sine comparison c_s≥(3/4)(1−s²)).

Reason: the conclusion "h′ first increases and then decreases to zero, staying positive" also needs h′(0)=π/2−3/2>0. Without it, h′ could start negative.

Fix: add "and h′(0)=π/2−3/2>0".

**C2A-05 — MINOR (definition before use; the paper too).** N_s is undefined, and the envelope assembly is hidden.

Location: 830–834, p. 62. The same occurs in the paper at line 278. N_s is used again at 2386 and in the paper at 872 and 1265.

Reason:
- "pole numerator N_s" is never defined. It is N_L(t)=c_e f(x−y+t)+c_d f(x+y−t) and N_R(t)=c_e f(x−y−t)+c_d f(x+y+t).
- The bound "|N_s|≤8" puzzles the reader, since in fact |N_s|≤c_e+c_d≤2.
- "The sine chord gives a pole remainder at most 6+πt/6" and "These estimates give (39)" hide the arithmetic. I reconstructed it [D] as follows:
  - pole remainder = (N_s−U₀)/t + N_s(1/(2sin(t/2))−1/t);
  - |·| ≤ 12/π + 8·πt/48, using t−2sin(t/2)≤t³/24 and sin(t/2)≥t/π;
  - the I term is ≤ (P/π)(11/4+2log(4π/t)) with ε=P/4;
  - the sum is ≤ 6+πt/6+(P/π)(11/4+2log(4π/t))+at(1+|log t|)/π, and t≤π/4 gives π²/24+0.311<1.

Fix: define N_s at the envelope. Say that 8 is a deliberately crude bound. Display the four-line sum above.

**C2A-06 — MINOR (definition domain).** The separation range of I(C,D,e) is not spelled out.

Location: 59–68, p. 51; 98 (Lemma 4.1 assumes 0<e≤π/2); 716–717, p. 60 (ℬ uses I(C(v),D(v),v) for 0<v<2π).

Reason:
- I is defined only for 0<e<π, but ℬ evaluates it at e=v∈(0,2π).
- Lemma 4.1 needs e≤π/2.
- The reductions are not stated: I is π-periodic in e, and I(C,D,π−e)=I(C,D,e) (my v1b check).
- At v=π the separation is ≡0 and I=−∞ when CD<0, that is when q>p. This is the integrable "central logarithm" (d₊/π)log|π−v| that F_s later subtracts (line 1703). Line 57 only hints at it.

Fix: add after (29): "I is π-periodic and even in e, so I(C,D,π−e)=I(C,D,e) and Lemma 4.1 covers every separation. At e≡0 the integral diverges logarithmically when CD<0. In ℬ this happens at v=π, with coefficient d₊; see F_s."

**C2A-07 — MINOR (hidden steps; a reader can fill each in, but the companion standard asks for them).** Each needs one or two lines:
- 1088–1089, p. 66, "then aD≤(7/2)u": use (44) as c(C−C₀)≤(7/2)(1−c). Then aD≤(7/2)(c_d+c_e−2c_ec_d)=(7/2)(u−z)≤(7/2)u.
- 1090–1093, "Substitution … gives exactly": insert U₀=a(C₋+C₊−4logπ)/π and 2C₀−4logπ+4log2=4(γ+log(8/π)) [D].
- 619–623, p. 59, λ₀: ∫_ε^π dt/(2sin(t/2)) = −log tan(ε/4), and log(ε/π)−log tan(ε/4)→log(4/π). For e^{1/4}>32/25 use e^{1/4}≥1+1/4+1/32=41/32.
- 630: the atom sits at w+s≡π, so |s|=π−|w|. W(π)=0 at w=0.
- 545–556, p. 58: show the moment calculation, ∫₀^{1/2}cos(wt)cos(ℓπt)dt=(−1)^jℓπcos(w/2)/(ℓ²π²−w²) minus (−1)^jcos(w/2)/(ℓπ). State that the moment series is O(j⁻³), so its r↑1 limit (Abel's theorem, or simply absolute convergence) is immediate.
- 563–564, |f‴|<13/20: say "the numerator vanishes at t=1/2, so |num|≤(23/20)(1/2−t); with cos πt≥2(1/2−t) the quotient is ≤23/40 on an interval of length 1/2".
- 1297–1308, p. 68:
  - log(π/2)<log(11/7)<23/50, because e^{0.46}>1.582>11/7;
  - log(25/16)=2atanh(9/41)>18/41 (first term), with π>25/8;
  - π²>197/20, because π>157/50;
  - k₀<9/5 and k₀<2 (line 408), from γ<3/5, log2<0.6932, logπ>11/10;
  - γ+log(8/π)<8/5 (line 1108) also needs e>8/3=1+1+1/2+1/6.
- 1440–1446, p. 70: a≥c_e²≥(1−ρ²/8)², which gives 15/16 and 49/64; q≥(23/24)y from sin y≥y−y³/6; Z≤2v∫_e^{π/2}dt/sin t=2v log cot(e/2)≤2v log(2/e).
- 1403, p. 70: "For τ=v/a≤1" holds on ρ≤π/2 because 2a≥p+q (line 1199). Say so.
- 1268–1276: show (8/π)∫₀¹(2t/π)c_k t^{2k}dt=(8/π²)c_k/(k+1).

**C2A-08 — MINOR (precision).** Location: 1957–1960, p. 79.

Reason:
- The bound Σ|cot(v_r/2)|≤4mH_n/π holds only over the ordinary rows r∉A₆. Their endpoint-distance indices are ≥2.
- Over all 2m rows it diverges as y→0 or y→π [E v5]: at n=32 and y=1e−6 it is 6.6e7, against 99.7 for r∉A₆.
- The text says "the two endpoint distance indices" without naming the range.
- Also, |C|+|D|≤max(p,q)/2+a|cot(v/2)| is sharper than "1+a|cot|". The stated bound is valid but loose (it doubles 10/n²).

Fix: write "summed over r∉A₆ …", and either state that the constant 1 is crude or use 1/2.

**C2A-09 — MINOR (pacing; systemic).** Interleaving produces repeated or out-of-order statements.

Pattern: the original compressed sentence and the new expansion often both remain, so a claim is read two or three times. Examples:
- 467–470 and 490–494 (derivative bounds 2,5,4 and sum <35), plus 484 and 503 (Φ″<12), all p. 57;
- 645–653 and 655–659 (layer cake), plus 660–663 and 666–674 (quadratic comparison), p. 59;
- 269–272 and 279–283, p. 54;
- 800–807 and 812–820, p. 62;
- 847 and 857 ("checks the logarithmic coefficient", twice), p. 62;
- 1031–1044 and 1046, p. 65;
- 1182–1186 and 1196–1197, plus 1199–1207 and 1209–1218, p. 67;
- 1260–1270 and 1272–1282, p. 68.

Impact: the hardest section is longer than it needs to be, and some derivations follow their conclusion.

Fix: in each pair keep the expanded version and fold the compressed sentence into it, or turn it into a one-line summary. The correspondence checker constrains display blocks and statements, not this prose (README; review.md acceptance criterion 2).

**C2A-10 — MINOR (notation).** Many symbols carry several meanings in pp. 50–81:
- g is both the integrand g(C,D;t) (line 65, used again at 2003) and f″ (line 327);
- H is 1+L, the finite part H(w), H_n, ℋ(L,v), ℋ_j, H_n^*, H_j(q);
- D is the coefficient D(v), D₀, D_*, the sum D (1088) and the allowance D (1493);
- T is the sinc T(t), T_t, the loss T, T₀, T_R;
- ε is the cutoff, the displacement (800), min(t,π−t) (1138), 3π/(2m) and ε_n;
- v is the coefficient sum in J and also the row angle;
- b, c, k, K, r, u and w each have several meanings.

Fix: add a short notation table at the start of §4.1. Rename the worst clashes, for example 𝔤 for the cancellation integrand, ε_sep for 1138, and λ₁ for the constant k=2γ−2logπ.

**C2A-11 — NOTE (figures and worked examples; strongest recommendation after the MAJORs).** pp. 50–110 contain no figure. I suggest three:
1. |C cot t| and |D cot(t+e)| on (0,π), for one same-sign and one opposite-sign case, shading the four intervals in the table at lines 177–183 and marking the roots y₀, y₁ or t₁, t₂.
2. f and H on [−π,π]. f is largest at the cusp π while H is largest at 0 (the point made at 675–677).
3. One row's samples u_{rk} against the poles ±v_r, showing the offsets η∓, and the 2m rows on the circle with A₆ marked.

Worked numbers, all verified [E]:
- J(1,0.5,e)=−1.12467 for every e (entropy regime);
- J(0.5,2,0.1)=−8.55698 against 2s log sin e=−9.21701 (root regime);
- J(0.5,2,1.2)=4 log sin 1.2=−0.28152 (beyond the threshold);
- the phase table at (0,0), (0.4,0.3), (0,0.4) and (0.4,0) from v9_example.py, for instance C∞(0.4,0.3)=1.80159<C*=1.84616 while the global bound −ju+t₀p−(H₀+v₀)z gives only +0.163. This shows why E_c is isolated.
- In §4.2, a table at n=160 and n=320 (v8_allowances.py), for example T=11.73, ē=0.154, C₄=0.0135, k_Nx=0.552 at 320, would make the hierarchy of losses and charges announced at line 18 concrete.

**C2A-12 — NOTE (agreement).**
- All numbered statements and displays in the range match the paper.
- The thresholds in this range are only n≥32 and n≥160, identical in both texts. 320, 192 and 256 belong to the localization sections.
- Lemma 4.2 matches E07 (311/71680; −(π−3)x²/(4π³); the atom is kept).
- Lemma 4.4 matches E11-central-pair. Its general bound on ρ≤π/2 and the decomposition (41) match E11-model-radius-halfpi; E10 is the weaker predecessor.
- My numerical values agree with (46) and (47).
- The non-circularity claim at 1222–1226 is consistent [I]: the global error (55) uses no H₀ bound.
- No discrepancy found.

**C2A-13 — NOTE (standard tools).** Usable statements with hypotheses are given for dominated convergence (541), Tonelli (285), layer cake (645), the Leibniz moving-boundary rule (252), Taylor with integral remainder (1858, 1893), the trapezoid and midpoint errors (1910, 2027) and the BV half-cell kernel (1921–1947). The last is correct, including assigned pole values [D]. Missing:
- Abel summation and Abel's theorem (548);
- concavity (Jordan) inequalities, used unnamed: sin θ≥2θ/π, cos πt≥2(1/2−t), sin u≥u/π on [0,2π/3];
- "Arb" (1291) is unexplained; suggest "a C library for rigorous ball arithmetic";
- "entropy formula" (196, 266) needs the phrase "r log r+(1−r)log(1−r), the negative binary entropy".

## Block-by-block coverage (purpose → prerequisites/gaps)

- **1–57 (p. 50)** Roadmap, phase meaning and notation. Good. u≈(x²+y²)/4 and z≈(x+y)²(x−y)²/64 checked [D]. Gap: C2A-10.
- **59–95 (pp. 51–52)** Definition of I and J, sign identity, finiteness at the poles, v,s coordinates. Good. Gap: C2A-06.
- **97–289 (pp. 52–54), Lemma 4.1** Interval table, root formula, R_s and R_e, endpoint value, Leibniz rule, E≤Z. All [D] and [E] correct. Excellent block.
- **291–346 (pp. 54–55)** Motivation of 𝒞 and Φ, derivative measure, finite part against principal value, ζ. Good.
- **348–691 (pp. 55–60), Lemma 4.2** Q series, derivative table, curvature, f-integral, Abel/DCT, f‴ sign, pairing, W kernel, layer cake. All correct. Gaps: C2A-04, C2A-07 (λ₀, moments, f‴ steps, atom), C2A-09.
- **693–897 (pp. 60–63)** Row profile, model, endpoint convention, counterterms, origin check b_full(0)=b_c [D], envelope, logarithmic coefficient. Correct. Gaps: **C2A-01**, C2A-05, C2A-06.
- **899–1329 (pp. 63–69), Lemma 4.3** Correlated losses; cotangent partial fraction from a finite product; tangent partial fraction; Q_* rearrangement; product with the −v₀z term; atanh; Li₂ primitive; cutoff calculation for the central decomposition (−(1/3+g₀)a verified [D]); κ reduction; constants; the Cauchy–Schwarz 9/4 bound. All correct. Gaps: C2A-03, C2A-07.
- **1331–1463 (pp. 69–70), Lemma 4.4** Heuristic for p^{3/2}, s₊+s₋ identity, Tonelli with Jacobian, rearrangement, F formula, K bound, I₄, chord bound for B_β. All correct. Note: the chord step does not need b≤1, because −log sin t≥0 is used first. Gap: C2A-07 (τ≤1, a bounds, q bound).
- **1465–1603 (pp. 70–73), Proposition 4.5 setup** Purposes of the allowances, the two kinds of bound, real-n monotonicity. Good roadmaps.
- **1605–1746 (pp. 73–75)** Rows, parity, collisions, A₆, mesh series, C₂, the five-term identity. Gap: **C2A-02**.
- **1748–1830 (p. 75)** Full telescope algebra, verified line by line [D]: B_ord, 𝓘_F, (Z_n−D₀)ℋ₂, the singular sample, h₂−h_n. Excellent.
- **1832–1962 (pp. 77–79)** Pole estimate (61) and its derivation (h²/3, π/(4n²), tail 1/(2πn²); total 4.234<5 [D]); c″ series; BV half-cell bound; weighted row errors. Gap: C2A-08.
- **1964–2050 (pp. 79–81)** Half-line defect (≤4/π [E]), B_j and Ξ_j, ψ estimate, ℓ_j partial fractions. These lines are checked up to 2050; the other agent covers 2001 onward.

## Prioritized fix list
1. C2A-01: add the model-meaning paragraph and the 2D₀ link. Fix line 895 here and line 298 in the paper.
2. C2A-02: derive the row identity and the offsets η∓, after (37) or at p. 73.
3. C2A-11: add three figures and one worked phase/degree table.
4. C2A-03 and C2A-09: repair the broken "Therefore"; merge duplicated passages.
5. C2A-05, C2A-06, C2A-08: define N_s, the domain of I, and the summation range.
6. C2A-07 and C2A-04: add the one-line justifications.
7. C2A-10 and C2A-13: notation table, renames, named standard inequalities.

## Limits
- This report covers comparison-unified.tex lines 1–2050. Beyond 2050 I only skimmed lines 2085–2165, for E∞ context.
- The numerical checks are float or 25–40-digit spot and grid checks. They are not certificates.
- I did not rebuild the PDF and did not run check_correspondence.py. I relied on X's build and block-diff.
- The coarse-input certificate (Arb run) was not replayed. Only an independent high-precision evaluation agrees with it.
