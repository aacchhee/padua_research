# M6: focused audit-06 of the response-05 analytic, notation and wording changes (both manuscripts)

- **Auditor:** Claude Opus 5.5, instructed at xhigh (effective effort not exposed). I am an independent
  mathematical and pedagogical subagent in Claude audit-06 (handoff 34) of Codex response-05, and I am distinct
  from the Codex developers and the Astra supplementary reviewers. I chose this depth because the scope is a
  mathematical delta audit; there is no adversarial or novelty content.
- **Rules:** AGENTS.md, agents/WORKFLOW.md and agents/claude/CLAUDE_ROLES.md, read at branch head
  `5b1a4942af498e60e9da4c8860c57cb4f67be4ef`.
- **Inputs read in full:** handoff 34, handoff 33, response-05, audit-05, audit-05-manuscripts, audit-05/m5a-section4.md
  and audit-05/m5b-corner-loc-cert.md. I read `supplementary-manuscript-review-response05-20261113.md` only after my
  own reconstruction and used it as evidence, not as a substitute.
- **Novelty exception:** this is a delta audit of repairs to existing arguments, notation and evidence wording. It
  involves no new mechanism, theorem, threshold or final-ID assignment, so the full `state/IDEAS.md` read is omitted,
  as handoff 34 states.
- **Read-only:** I ran no state-changing git command and wrote no repository file; `git status --short` was empty
  before and after. My outputs are this file and `m6-code/`. I did not touch Syvert, native or archive code.
- **Labels:** [D] = derived by hand here. [E] = executed here; floating results are MEASURED, while iv/Fraction/sympy
  results are rigorous for the numbers they check. [I] = inspection or judgement.

**Audited identity.** The TeX/Bib freeze is `8937d3b723c09c004f49d3e565d0b02976713a37`. It is diffed against the
previous audited freeze `ad908acb21d3589d85635618ff68f63dd01cfbca`; the 33-entry rename map is checked against
`24a98db`. `git diff --quiet 8937d3b 5b1a494` over both `sections/`, both `main.tex` and the bib is empty, so the head
equals the freeze. I extracted the trees with `git archive` into `m6-code/trees/{base24,old,new}` and wrote the
per-file diffs to `m6-code/diffs/`.

Source SHA-256 prefixes match the supplementary review table exactly:

| Text | main | cert | comparison | corner | localization | preliminaries |
|---|---|---|---|---|---|---|
| paper | `060786ff` | `b3f0099d` | `8c57a0a9` | `355ca7fc` | `bed0dcbd` | `54682f15` |
| companion | `40cea7c5` | `4dcdb37d` | `c31e6a71` | `d5370dfb` | `bc187e0b` | `8e536da1` |

The bib is `138871f1` and is identical in both texts. The rename map `paper/notation-renames-audit05.json` is
`3f44543a`. Page numbers are from B6's fresh builds in `$A/build/` (58 and 152 pages; `page-index.md` and text
copies). The changed text spans paper pp. 9–56 and companion pp. 24–150.

## 1. Verdict

**Mathematics of the response-05 changes: ACCEPTED. There is no BLOCKING or MAJOR finding.**

- **M5A-01:** the false implication is replaced in both texts by the correct statement ρ ≥ π−v. I re-derived the
  statement from the offset algebra and reproduced the counterexample to the old clause at n = 32, 192 and 512 on
  non-retained rows. The consequence 𝖺 ≤ Pv/2, and hence every charge, is unchanged.
- **Restored reasons:** every restored or added reason reconstructs, as does every changed proof clause I examined.
  This covers the prefactor/τ, wrap cost, primitive, amplitude–phase, chord, alternating-remainder,
  |N_s| bound, pole decomposition and sum to 7, domination, concavity, the §3.3 trapezoid/recurrence/ψ′/κ items,
  the cosine cancellation, the Peano and corner-lemma clauses, and the Cor 4.6 monotonicity reorder.
- **Base-value table:** all 60 entries contain the true value and are the tightest outward 6-decimal enclosures
  (own iv transcription). The table now follows every definition it uses, is labelled and cited, and states its provenance.
- **Changed numbered blocks:** all 9 are identical between paper and companion.
- **Remaining items:** 4 MINOR (two notation/reference items, one evidence-status clarity item, one stale record), 3
  EDITORIAL and 4 NOTE. None affects a claim, constant or threshold.
- **Response-05 dispositions in this range:** supported, except M5A-05 and M5B-E6, which are only partly supported
  (M6-01, M6-02). The response's "Corrections to response-04" section is accurate.

## 2. Executed checks [E]

All runs used the copied `$A/pylib` (mpmath 1.3.0, sympy 1.14.0) under Python 3.13.18. Total metered CPU was about
15 s, well under the ~30 CPU-min cap. Commands ran from `$A/m6-code`, except where noted.

| # | Command | Exit | Result |
|---|---|---|---|
| E1 | `PYTHONPATH=../pylib python3 -B m6_checks.py trees` (`d80a640e`) → `m6_checks.out` (`699271aa`) | 0 | 61 PASS, 0 FAIL. Contents in §3 |
| E2 | `python3 -B map_check.py trees …/notation-renames-audit05.json` (`f99f1d6a`) → `map_check.out` | 0 | per-entry counts on 24a98db/8937d3b (§4) |
| E3 | `python3 -I -B blocks.py trees` (`f6ff11f3`) → `blocks.out` | 0 | changed numbered/statement blocks and paper/companion equality (§5) |
| E4 | byte copy of `code/onset512_analytic/check.py` (`5ce8cc07`): `python3 -E -B check.py` and `python3 -E -B -O check.py` | 0 / 1 | normal run PASS, and all 8 receipt fields equal `receipt.json`; the optimized run refuses before any verdict. Line 146 asserts `log(PI).lo > 11/10` |

Not run here: builds, `check_correspondence.py`, the baseline/mutation controls and rendered-tag inspection. These
belong to B6. I used B6's text copies only to locate pages.

## 3. Reconstruction of the changed analytic text

**(1) M5A-01, the omitted collision (companion comparison 2229–2269, p. 84; paper 997–1006, p. 32).**

Derivation [D]:
- Rows have u_rk = (δ_rπ+x+2kπ)/n and v_r = (rπ+y)/m, with δ_r+r odd.
- Then n(u∓v_r)/(2π) ≡ ½+(x∓y±v_r)/(2π) (mod 1), independently of k. This is exactly η_∓ of (uc:row-profile).
- **Left rows** (r = j ≥ 2, v = v_r). A collision requires x−y = π−v (η₋). The η₊ condition x+y ≡ π+v (mod 2π) is
  impossible on the folded triangle.
- **Right rows** (r = 2m−j′ with j′ ≥ 3, v = (j′π−y)/m, v_r = 2π−v). A collision requires y−x = π−v (η₋) or
  x+y = π−v (η₊).
- The text's offset (1−s±ξ)/2+ν/(2m) = ½+(∓′y±x+v)/(2π) agrees with these up to sign mod 1.
- Since x, y ≥ 0, each case gives ρ = x+y ≥ π−v. Since cot is decreasing and tan(v/2) ≤ v on (0, π/2],
  𝖺 = (P/2)cot(ρ/2) ≤ (P/2)tan(v/2) ≤ Pv/2. The parenthetical "(one of x−y, y−x, or x+y equals π−v)" is exactly the case list.
- Each channel's unwrapped offset increases strictly in j. η₋ can collide on only one side, because x−y and y−x
  cannot both be positive, so there are at most two rows. ν ≥ 2 holds on all non-retained rows (j ≥ 2 left, j′ ≥ 3
  right), so |Ξ_j| ≤ 2P/(πmν) ≤ P/(πm) applies.

Measurements [E1]:
- On rows r = 2m−3 and 2m−7 with y = 0.4 and x = π−v−y, an actual sample hits the −v_r pole (fractional distance
  0 at 50 digits, cos u = cos v_r):
  - n = 32: |x−y| = 2.068 < π−v = 2.868;
  - n = 192: 2.295 < 3.095;
  - n = 512: 2.324 < 3.124.
- So the old clause is false, ρ ≥ π−v holds, and 𝖺 ≤ Pv/2 holds; for example at n = 512, 𝖺 = 3.50e−3 against
  Pv/2 = 6.99e−3.
- A randomized test placed points on all three loci for random rows at n = 32, 192 and 512. Of these, 2,940 were
  actual collisions, with 0 violations of ρ ≥ π−v or 𝖺 ≤ Pv/2.
- Converse: 600 sampled rows with ρ < π−v had no collision.
- Audit-05's j = 2 (r = 2m−2) example used a retained row; my examples avoid A₆. The paper's comma splice is gone.

**(2) Restored companion reasons and both texts' envelope.**
- **Prefactor:**
  - Identity: 2𝖺τ(v/2)/(π²ν) = 𝖺cot(v/2)/(πm) for v = πν/m [E sympy], consistent with the wrap prefactor ≤ Pτ(v/2)/(πm) ≤ P/(πm).
  - Definition order: τ(w) = w cot w, with τ(0) = 1, is now defined at its first use in running text (companion 2232). Before
    that it appears only in the §4.2 table and as the offset subscript Q_τ (M6-10).
- **Wrap:**
  - z_arg−1 ≥ j−5/4 ≥ 3(j−1)/4 for j ≥ 2 [E].
  - Two wraps give 2·(P/(πm))·4/(3(j−1)) = 8P/(3πm(j−1)) per row.
  - Summing j ≤ m/2 on both sides gives ≤ 16PH_n/(3πm) ≤ 16PH_n/(3πn) [D].
- **Primitive:** d/dt 4𝖺 log sin(t/2) = 2𝖺cot(t/2) = T_t [E sympy]. The sentence (companion 1012, p. 67) follows the
  display that uses it, and the display's algebra 2[·]^{t₁}+[·]^{t₂}_{t₁} = 4𝖺 log 𝖺 − 8𝖺 log sin(ε/2) checks [D].
- **Domination (old line 999):**
  - The max formulas reduce to πA(t) = max(p, q+T_t) and πA(2π−t) = max(p, |q−T_t|) [D, E 20,000 samples].
  - Hence |πA−T_t| ≤ 1 on both sides (attained) and |cot(t/2)−2/t| ≤ 2/π on (0, π].
  - The subtracted integrand is therefore bounded by (2+8/π)/π independently of phase; dominated convergence is correct [D].
- **Amplitude–phase (old line 1310):**
  - Step: u ≥ (1−cos x)/2 gives C_∞ ≤ C_*−𝔧/2+(𝔧/2)cos x+t₀sin x (𝔧 > 0), and Cauchy–Schwarz bounds the last two
    terms by √(𝔧²/4+t₀²) [D]; δ²+δ𝔧−t₀² = 71/6250000 [E Fraction].
  - Minimum: A cos x + B sin x ≤ √(A²+B²) gives A+B−√(A²+B²) (increasing in A and B), which is > 3 ⟺ 2(A−3)(B−3) > 9 [E sympy].
    With A = 398/(11π²) = 3.6660 and B = 48/π = 15.279, the minimum is 3.2323 > 3 [E iv].
- **Chord and concavity (old line 620):** cos is concave on [0, π/2], so cos πt ≥ 1−2t for t ∈ [0, ½]. The "same chord bound"
  reference at 655 is apt. The alternating-series rule (companion 330–332) is the Leibniz remainder statement in the
  form used.
- **The Machin bracket (B5-03):** 𝒜₄₀ < arctan(1/q) < 𝒜₃₉ for q > 1. The displayed π bracket takes the correct sides [D].
- **|N_s| and the pole decomposition (both texts; companion 941–961, p. 65; paper 379–399, p. 24):**
  - |N_s| ≤ c_e+c_d ≤ 2 ≤ 8 follows from ½ < f ≤ 1 on the circle.
  - The displayed split N_s/(2 sin(t/2)) − U₀/t = (N_s−U₀)/t + N_s{…} is exact.
  - 0 ≤ (2 sin(t/2))⁻¹−t⁻¹ ≤ πt/48 holds on (0, π]: the measured supremum ratio is 0.0578 ≤ π/48 = 0.0654 [E], and
    t−2 sin(t/2) ≤ t³/24 [E].
  - Hence 12/π + 8·πt/48 ≤ 6+πt/6 (12/π < 6) [E].
  - Reference error: t(1+|log t|)/π ≤ 1/π on (0, π/4] (the maximum of t(1+|log t|) is 0.9751 at π/4) [E].
  - Constants: 6+π²/24+1/π = 6.7295 < 7 [E iv]. Displacement: (P/4π)(11+8 log(4π/t)) ≤ (P/π)(3+2 log(4π/t)).
  - Conclusion: (uc:endpoint-envelope) follows exactly as displayed [D].
- **Paper factor-four note (p. 33):** f > ½ gives 0 < U₀ ≤ c_e+c_d, so |D₀| ≤ (c_e+c_d)/π + 𝖺b₀ log π ≤ D̄_φ. "|f| ≤ 4" is
  indeed a coarse consequence [D].

**(3) Section 3.3 (companion corner) and other changed clauses.**
- **Trapezoid:** each unit-cell trapezoid error is ≤ (1/8)∫|f″|, because the kernel s(1−s)/2 has maximum 1/8. The total is
  ≤ (1/8)∫₀^∞ 2(z+t)⁻³ dt = 1/(8z²), uniformly in J [E sympy] (1076–1080, p. 36).
- **Recurrence:** ψ(y/2) = ψ(1+y/2)−2/y [E 40 digits]. With w(1−y) = yb(y), it gives F(1−y) = L(y)+log y+2/y and hence
  R(1−y) = A₁+yb log y with A₁(0) = 2b(0)−P₁(0) = π−𝖺d₀ [D] (1415–1424).
- **ψ′ estimate:** |ψ′(r+½)−1/r| ≤ 1/(3r³) for real r ≥ 1. It follows from the midpoint bound h³‖g″‖/24 = 1/(4(r+k)⁴) and
  Σ(r+k)⁻⁴ ≤ 4/(3r³) [D, E]. The true worst ratio is ¼ of the bound [E]. "Proving the stated estimate" now has its
  antecedent; its "cell bound just proved" phrase does not (M6-06).
- **κ:**
  - κ_∞ is used until the pairing identifies κ_∞ = κ of (eq:main-kappa); only then is (cu:kappa) asserted (845–852).
  - 1705 cites (cu:kappa) for the uniqueness-of-limit step.
  - The ψ-estimate order sentence matches the actual order: ψ′(½) at 1022–1060, the derivation at 1068–1088, ψ(½) at 1090.
  - d_r replaces δ_r (505), removing the clash with the row parity δ_r.
- **Cosine cancellation (paper 757, companion 1658):** u = u_rk gives nu = δ_rπ+x+2kπ, so cos(nu) = (−1)^{δ_r}cos x. Writing
  1+cos u = (1+cos v_r)+(cos u−cos v_r) shows that the divided difference contains the constant cos x/2, which −cos(nu)/2
  cancels. The displayed numerator 𝖺(1+cos v_r) − (p/2)sin u + (q/2)sin v_r and the C± form hold to a relative error of
  4e−28 at random rows for n = 32, 33 and 192 [E].
- **Kernel label (eq:kernel-evaluation), number (25) in both texts:** the formula is byte-for-byte the former inline
  evaluation form, now displayed and labelled. It equals (eq:angular-kernel) with ν₀ = 1, ν_p = 2. The product (sine-ratio)
  form with u± = (u±v)/2 also equals it, including collisions and removable R_ℓ(jπ) values (error ≤ 3e−29, n = 1..9) [E].
- **Cross-references:** every reference is `\eqref`/`\ref`. A search found no hard-coded internal equation, table or figure number
  in either source [E]. The two row identities now cite (25), and (7) remains cited only for the kernel's definition.
- **Corner lemma (paper localization 408–425):**
  - A₄+ρJ_W ≥ 0 holds.
  - 𝔗−ē+𝔧 > 0 for n ≥ 256 follows from 𝔗(256) > 107/10, ē < 1/5, 𝔧 > 23/250 and the stated monotonicity, so u may be replaced by q_h.
  - The diagonal chain now cites Lemma uc:master, (uc:origin-lower) and (uc:global-error) correctly.
  - The Peano dummies v₁, v₂ leave the weight-⅓ double integral intact [D].
- **Cor 4.6 reorder (paper 1764–1767):** it is the same argument, with A′ ≤ 0 now stated once [D].
- **Parity versus positivity (companion 2661–2665):** 𝖺 > 0 gives f_j > 0 ⟺ |jπ+x| < rπ+b, and parity gives the index
  set because x+|b| < π [D].
- **Merge artefact (companion 2968–2983):** the μ-monotonicity reason is now stated once, and the 56/(9π²) bound is intact [D].
- **Base-value table (Table 2; paper p. 43, companion p. 108):**
  - Values [E1]: an independent mpmath.iv transcription (60 digits) of (uc:constants), (uc:uniform-allowance),
    (uc:analytic-norm) and Cor 4.7 gives 60/60 containment and 60/60 tightest outward 6-decimal enclosures. The tables in
    the two texts parse identically.
  - Order: every symbol is defined before the table in source and on the page. 𝔗, ē, K_D, C̄_E, C₄, k_W·, d_β are defined in
    (uc:constants)/(uc:uniform-allowance), M(n) in Thm 4.5, and U*, d_x, d_y, ℓ_x, ℓ_y in Cor 4.7 (p. 41/106).
  - Citations: the table is cited from the Cor 4.6 and Cor 4.7 proofs and from the n = 256 corner step.
  - Provenance: the sentence is accurate. `check.py` `constants()` returns 8 of the 15 quantities, and the receipt
    contains none of the 60 values (M6-11).
- **Lemma 5.1 and Proposition 5.3:** Lemma 5.1 (cert:positive) is byte-identical between ad908acb and 8937d3b in both texts
  [E3]. Its audit-04 change was accepted by audit-05. Prop 5.3 changes only "retained" → "recorded", identically in both
  texts, which removes the present-custody connotation. The mathematical predicate is unchanged.

## 4. Notation and the cumulative 33-entry map

**Map against 24a98db [E2].**
- Applying the 33 entries in order to the 24a98db sources matches every `from` string (applied = base count) and yields
  the 8937d3b target forms.
- **New entries.**
  - Entry 31: `F_0(hk` → `F_0(h_m k`, one occurrence in uc:signed-outer, as required by audit-05.
  - Entry 32: `h_m` → `\vartheta_m`. In ad908acb all 26 (paper) and 63 (companion) occurrences of h_m denoted π/m, and
    24a98db has no h_m.
  - Sequential application gives F_0(ϑ_m(k+t)) and F_0(ϑ_m k), matching the source.
  - No bare h meaning π/m remains [E grep]. The remaining h are local: h = ρ/2 (Cor 4.6, declared local at companion
    3995), h(r) and h(t) in §4.1, and h_j(t), h_*, h_pole.
- **Earlier entries.** I verified the 31 earlier entries by count; their meanings were verified by audit-05 (M5A §4,
  M5B renames).
- **Caveat (NOTE M6-09):** entries 2 and 9 textually over-match the kernel polynomial P_n(cos ·), which the sources
  correctly keep.
- **Meaning:** every entry preserves meaning at the occurrences it is meant for.

**Collisions remaining in the same section (audit-05 M5A-05 list).**

Paper:
- e = ρ → e_ρ and Δ_x (1580–1585); e = π−z → e_c (1129–1144, 1368–1370, 1638–1678).
- r(w) → r_hl (1452–1489); r → r_c (1621).
- The dot-path τ → λ (1430).
- All are scoped and correct. The remaining bare e is the separation variable of I/J (§4.1 and the perturbation lemma),
  which is its declared meaning. The D̄_φ factor-four note has been added.

Companion:
- η± = log(1±c/n) → η_log,± (2838–2844); ζ = z/2 → χ (3039–3048); e = π−z → e_c (3074–3080, 3922).
- The §4.2 table now lists w (rπ+b) and w_r (half-amplitude).
- **Residual:** bare w still denotes the row half-amplitude at 2270–2274, contradicting the table, and likewise in the paper
  at 1006–1009 (M6-01).
- Minor local reuses that are not same-display traps are listed in M6-10.

## 5. Paper/companion agreement for changed blocks [E3]

Nine numbered or statement blocks changed between ad908acb and 8937d3b, and each is now identical in the two texts:

| Kind of change | Blocks |
|---|---|
| Layout splits for B5-02 | cu:D, cu:row-expand, ul:charts, uc:completed-model, uc:scalar-constants, uc:uniform-allowance |
| New label | eq:kernel-evaluation |
| ϑ_m rename | uc:signed-outer |
| Wording | cert:finite-verification (Prop 5.3) |

I checked each split algebraically against its predecessor; for example, G_g's split numerator sums to the old one [D].
The labelled sets are equal (0 labels in only one text).

Prose additions present in both texts:
- the pole decomposition and sum to 7;
- the domination bounds;
- the collision parenthetical;
- the cancellation clause;
- Figure 3, Table 1 and Table 2 with their provenance;
- the custody paragraph;
- the data statements;
- the Theorem 1.1 proof.

The companion now also has the abstract qualifiers and the physical-corner clause; M5B-02 is supported.

## 6. Evidence and custody wording (both texts)

- **Recorded versus present.**
  - Both certification sections say that inventories "record past computation and do not establish current custody", that
    the onset-512 return archive and the independent-checker bundle are unavailable, that four data-only checks remain open,
    and that the availability of the 632 MiB histories is unverified (paper p. 56, companion p. 145).
  - The companion no longer says "are retained" or "remain at their recorded computation sites", and "compact returns"
    has gone (M5B-01 supported).
  - "I25" no longer occurs in either text [E grep].
  - Every remaining "retained" refers to mathematical objects (rows, leaves, vertices, terms).
- **IEEE model.**
  - The companion trust cell reads "error bound derived below (under the assumed IEEE model)".
  - The paper places binary64 semantics in the implementation-trust column and derives only the 84ε_fp t bound.
  - ε_fp is now defined before use.
  - M5B-03 is supported.
- **Data statements.** Neither cites a433c7d. Both say a permanent post-repair snapshot is being prepared and the DOI is
  pending, and they point to §5 for retrieval limits. B5-04 is an honest placeholder; the snapshot and DOI remain OPEN for AC.
- **Response-04 corrections.** Response-05's section names B4-01/P4-14, M5B-06, B4-04/X-13, B4-05, P4-01/08/12, C4A-01,
  C4D-05, C4C-n3 and the supplementary B5/C1/C10 rows. This matches audit-05's overstated list, and response-04 itself is
  unedited (`git log`). The supplementary review has a dated correction. The duplicate-dispositions record does not (M6-04).
- **Clarity gap.** The new custody sentences use project jargon and an ambiguous witness count (M6-03).

## 7. Findings

**M6-01: MINOR. Bare w for the row half-amplitude still contradicts the §4.2 symbol table.**
- **Location:** companion `comparison-unified.tex:2270–2274` (§4.2, p. 84), against the table at 1468 (p. 74); paper `:1006–1009` (p. 32).
- **Reason [D]:**
  - The table assigns w = rπ+b and w_r = 𝖺cot(v_r/2)/2.
  - The cited lines, "16|w|/π per row", "w ≤ 𝖺m/(πν)", "8|w cot v|" and "4|w|/|sin v| = 𝖺/sin²(v/2)", are true only for
    w = w_r. I checked 4w_r/sin v = 𝖺/sin²(v/2).
  - w_r is defined at companion 2057 and paper 928, and redefined identically at 3360 and 1477.
- **Impact:** a notation trap of the kind M5A-05(c) targeted. No claim is affected.
- **Fix:** write w_r (and v_r) on these lines. Optionally point the table's w_r entry to the half-line paragraph rather than (uc:sinc-row).
- **Disposition:** M5A-05 "developed scoped" is partly supported. This is a TeX edit, so it breaks the freeze.

**M6-02: MINOR. The paper points to "the expanded companion" without identifying it.**
- **Location:** paper `certification-unified.tex:413–416` (p. 54); data statement `main.tex:81–90` (p. 56).
- **Reason [I]:**
  - The paper never introduces or cites a companion manuscript; its only occurrence is this sentence.
  - `Section~\ref{sec:certificates}` resolves to the paper's own Section 5. It renders "Section 5" correctly only because
    both documents share the section structure.
- **Impact:** for a journal reader the derivation of the 84ε_fp t bound, which J3-08 and M5B-E6 asked to point to, is not
  locatable. AC's "named tools cited" criterion is not met.
- **Fix:** identify the companion once, in the data statement or the bibliography (title and location in the repository or
  deposit), and refer to it as "Section 5 of [companion]" in plain text or by citation, not by a paper-internal label.
- **Disposition:** M5B-E6 is partly supported.

**M6-03: MINOR (both texts; clarity of an evidence-status statement). The custody sentences use undefined jargon and an ambiguous witness count.**
- **Location:** paper `certification-unified.tex:505–517` (pp. 55–56); companion `:1624–1635` (p. 145).
- **Reason [I]:**
  - "canonical onset-512 return archive", "independent phase-checker evidence bundle" and "data-only checks" are project
    terms that the text does not define.
  - The text counts two "witnesses" per degree (Table 4: 382 for 191 degrees; "both witnesses at each of degrees 41, 458
    and 511"). "The four witnesses at degrees 320, 384, 458 and 510" is therefore ambiguous: four or eight records?
  - Degree 458 appears both as separately re-executed and as open, without explanation.
  - The reader is not told that these four degrees are a preregistered audit re-inspection sample rather than a premise of
    Prop 5.3, nor that Prop 5.3 at 320–510 rests on recorded executions whose outputs cannot currently be re-examined.
- **Impact:** an accurate but opaque disclosure; a reader may misjudge the status of Prop 5.3.
- **Fix:** describe the archive as "the output archive of the degree 320–510 certificate run" and the bundle as "the stored
  outputs of the independent checker". Say that an independent re-inspection of the stored records (planned on a sample
  of degrees 320, 384, 458 and 510, both records each) has therefore not been possible, and that the stated verification
  for these degrees rests on the recorded executions. Keep it consistent with the LOG.
- **Process:** this is an evidence-status statement, so return it to development, not an in-place fix.

**M6-04: MINOR (record). The dated correction for the lost reasons was not applied to `manuscript-duplicate-dispositions-20261113.md`.**
- **Location:** rows C1 (line 9, "tau error, wraps … retained"), C10 (line 18) and B5 (line 37, "branch/primitive derivation").
- **Reason [I]:**
  - Audit-05 M5A-02 asked for a dated note in both this file and the supplementary review.
  - Only the supplementary review received one. Handoff 33 named only that file, and response-05 claims only that one.
- **Impact:** a stale positive record.
- **Fix:** add a dated note mirroring the supplementary review's. This record wording is eligible for the orchestrator's
  third-round in-place MINOR rule.

**M6-05: EDITORIAL (both texts). Wrong punctuation after the ul:charts split.**
- **Location:** paper localization 35–37 (p. 16); companion 97–99 (p. 47).
- **Problem:** the display now ends "(θ,φ)∈[0,π]²." and the sentence continues "where 0 ≤ J ≤ n". Before the B5-02 split it
  ended with a comma.
- **Fix:** restore the comma.

**M6-06: EDITORIAL (companion corner 1203–1204, p. 39). "Apply the cell bound just proved" lacks a clear antecedent.**
- **Problem:** the nearest preceding cell bound is the trapezoid bound (1076–1080). The bound actually used,
  1/(4(r+k)⁴), is the midpoint bound h³‖g″‖_∞/24 of Lemma cu:quadrature (line 944).
- **Fix:** cite Lemma cu:quadrature's midpoint bound.

**M6-07: EDITORIAL. Two sentence-level slips.**
- **Paper comparison 1004–1006 (p. 32):** "Its normalized |Ξ_j| ≤ 2P/(πmν) ≤ P/(πm), and there are at most two such rows …,
  costing 2P/(πn), and the residual … costs …" has no verb for its first clause. It sits in the paragraph of the M5A-01
  repair. Suggested wording: "Its normalized reference satisfies …; there are at most two such rows …".
- **Prop 5.3, both texts (paper cert 341, companion 1478):** "both recorded certificate records" is redundant; write
  "both certificate records".

**M6-08: NOTE. The cosine-cancellation clause is correct but terse.**
- **Location:** paper comparison 757–758, companion 1658–1659.
- **Suggestion:** "since 1+cos u = (1+cos v_r)+(cos u−cos v_r), the divided difference contains the constant
  (−1)^{δ_r}cos x/2, which −cos(nu)/2 cancels". Optional.

**M6-09: NOTE. Map entries 2 and 9 textually over-match the kernel polynomial.**
- **Location:** `paper/notation-renames-audit05.json` entries 2 (`P_n` → `\mathfrak p_n`, comparison) and 9 (`P_n(`,
  localization).
- **Over-matches:** in 24a98db these entries match the kernel P_n(cos u) and P_n(cos v_r) twice in comparison (the row
  identity) and twice (paper) or four times (companion) in localization. One of the localization occurrences is now
  inside the numbered (eq:kernel-evaluation).
- **Effect:** the sources correctly keep P_n there. The map is meaning-preserving only for the gate occurrences, and a
  scanner using it reports (25) as changed, which is correct here because it is new.
- **Suggestion:** record the exclusion or anchor the patterns (e.g. `P_n(\rho`, `P_n(1/2`). Audit-05 M5B noted entry 9 only.

**M6-10: NOTE. Remaining local reuses (no same-display trap).**
- τ is the offset subscript in Q_τ (paper 851, companion 1789) before τ(w) = w cot w.
- χ = z/2 (companion 3039) reuses the §4.1 test-function letter χ (606).
- Bare η = ϑ_m t (companion 3885) sits beside the pole offsets η±.
- ϑ_m (§4) sits against ϑ = πr/d (cert §5).
- Paper 588–589 still states C_∞ ≤ C_*−𝔧/2+√(𝔧²/4+t₀²) without the amplitude–phase reason that the companion now gives.

**M6-11: NOTE. The table provenance is accurate, but no committed command reproduces the 60 values.**
- `check.py` `constants()` returns 𝔗, ē, K_D, C̄_E, A₄, C₄, k_Wx and k_Wy.
- L, d_β, M(n), U*, d_x, d_y, ℓ_x and ℓ_y are composed ad hoc.
- The table is not a proof input (the gates and the corner step display their own rational bounds), and all 60 values are
  confirmed here.
- **Suggestion:** say "composed from check.py's exact routines", or commit the few composition lines with a receipt.

## 8. Response-05 dispositions in this range, checked against the text

| Row | Response-05 | Verified |
|---|---|---|
| M5A-01 | Developed | **Supported** (both texts; §3(1)) |
| M5A-02 | Developed | **Supported**: prefactor, τ before use, wrap cost, primitive, amplitude reason |
| M5A-03 | Developed | **Supported**: chord, alternating rule, |N_s| at first use, decomposition and 7, 999/1310/620 reasons |
| M5A-04 | Developed | **Supported**: ϑ_m in both texts, separate from h_j(t); no residue |
| M5A-05 | Developed scoped | **Partly**: paper e/r/τ, companion η/ζ/e and the table are done; bare w = w_r remains (M6-01) |
| M5A-06 | Developed | **Supported**: forward pointers to (uc:phase-allowance) and the origin estimate |
| M5A-07 | Developed | **Supported** in source (labels, refs, "not proof inputs", arrows pole → right sample, matching η∓ ≡ n(u∓v_r)/2π); rendering is B6's |
| M5A-08 | Developed | **Supported** |
| M5A-09 | Developed | **Supported** (M6-08 optional) |
| M5A-10 | Retain | **Agree** (both maxima valid) |
| M5B-01 | Developed | **Supported** (wording clarity M6-03) |
| M5B-02 | Developed | **Supported** (proof of Thm 1.1, corner naming, abstract) |
| M5B-03 | Developed | **Supported** |
| M5B-04 | Developed | **Supported**, all six sub-items (antecedent M6-06) |
| M5B-05 | Developed; supplementary recomputed | **Supported**: 60/60 independent; order, label, citations, provenance; log π > 11/10 asserted and executed |
| M5B-07 | Developed | **Supported** (ε_fp, w_B, ξ/u±, I25) |
| M5B-E1..E6 | Developed | E1–E5 **supported**; E6 **partly** (M6-02) |
| B5-03 / B5-04 / B5-10 | Developed / placeholder | **Supported**; snapshot and DOI OPEN |
| Corrections to response-04 | Accepted | **Accurate**; dispositions record still uncorrected (M6-04) |

No row in this range claims FIXED or VERIFIED beyond what the text supports, except the two partly supported rows above.
The supplementary review's "FIXED within the listed scopes" for M5A-05 did not notice M6-01. Its other analytic
reconstructions agree with mine.

## 9. Coverage and limits

- **Read in full:** every hunk of `git diff ad908acb 8937d3b` for both texts (paper: comparison, corner, localization,
  certification, preliminaries, main; companion: the same except preliminaries, which is unchanged). I also read the
  surrounding context: companion comparison 290–340, 600–660, 815–830, 925–1032, 1296–1350, 1451–1475, 1575–1760,
  2195–2300, 2400–2425, 2650–2670, 2955–2992, 3355–3380 and 3995–4182; paper comparison 1–30, 150–180, 328–432,
  580–592, 657–730, 740–860, 986–1012, 1052–1080, 1110–1130, 1575–1600 and 1755–1916; companion corner 770–862,
  1010–1110, 1180–1245 and 1395–1445; both localization and certification sections around every hunk; both
  data statements.
- **Not re-audited:** unchanged analytic components accepted by audit-05; E5 code and reader items (E5-01..E5-04); builds,
  correspondence, mutation and rendered-tag checks (B6).
- **Rendered layout:** I used page numbers from B6's text copies only; I viewed no images.
- **Measurement status:** the counterexamples, randomized locus tests, kernel identities, J(1,½,e) (constant −1.1246703 at
  six e ∈ (0, π), matching Table 1's "for 0 < e < π") and the domination samples are MEASURED. The base table, envelope
  constants, amplitude minimum and Fraction identities are rigorous for the numbers checked. Universal statements rest on
  the [D] derivations above.
- **Not available:** the onset-512 archive and the I25 bundle; no custody claim is made. The status of Prop 5.3 at
  320–510 remains AC's evidence decision.

2026-11-13 · Claude Opus 5.5 (instructed xhigh) · rules read at 5b1a494 · outputs `$A/m6-analytic.md`, `$A/m6-code/`.
