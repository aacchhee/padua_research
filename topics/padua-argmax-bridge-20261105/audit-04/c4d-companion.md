# C4D — Companion audit-04: Section 4 localization (outside the comparison insert) and Section 5 certification

Auditor: Claude Opus 5.5, xhigh effort. Sub-auditor C4D in the substantive Claude audit-04 (handoff 30).
Role: independent mathematical and pedagogical reviewer. I made no repository writes and no Git state change.
Rules read at branch head `70a50d7b2a72a30fd7a2af3b2ead54ae14470bf9` (`codex/padua-argmax-bridge-20261105`):
AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md, handoff 30, and the onset512 brief (both-manuscripts
half and the finite-certificate criteria). Also read: companion README/BUILD/review.md, audit-03/c3-companion.md and
response-03.md. The novelty gate does not apply: this audit makes no novelty, mechanism or priority judgment.

Audited sources (the head bytes equal the TeX freeze `24a98db4c3c4c4d0eede2e3929532956df87911b`, rehashed):

| File | SHA-256 (prefix) | Read |
|---|---|---|
| companion `sections/localization-unified.tex` (1153 lines) | `4cb2a225fba90e6c` | every line except the `\input{sections/comparison-unified}` (l.323) |
| companion `sections/certification-unified.tex` (1842 lines) | `28335bfbf1ee84c1` | every line |
| paper `sections/localization-unified.tex` (432) / `certification-unified.tex` (443) | `14df874b…` / `6fe37603…` | every line |
| `code/independent_phase_checker/check.py` (I25 core) | `1501ce9435a17e9c` (= RESULTS.json pin) | every line |

For definitions I consulted, without auditing them, comparison-unified.tex l.1240–1539 and 3860–4020 (constants,
Theorem uc:finite-bounds, both gate corollaries, Lemma uc:central-pair) and corner-unified.tex l.110–150 (the sine-ratio
kernel). I also read the trust sources theory/G01 (all), theory/J03 (all), RESULTS.json, local-onset512-summary,
compact-return and a grep of paper/small-degree-unification.md. Page numbers refer to B4's fresh companion build
`$A/build/companion/main.pdf` (147 pages; I did not build), located via `$A/build/text/companion.txt` and
`$A/build/page-index.md`: §4 p.47, 4.4 p.105, 4.5 p.112, §5 p.115, 5.1 p.119, 5.2 p.126, 5.3 p.139.

Labels: [D] derived or checked by hand or exact algebra; [E] executed (scripts in `$A/c4d-code/`); [I] inspection or
judgement. MEASURED results are labeled and upgrade no claim.

## 1. Verdicts

**Mathematics (C4D range): SUPPORTED; no BLOCKING finding.** I re-derived or recomputed every added or changed
derivation, worked example and table entry ([D]/[E], §5), and all are correct:
- the selected-pair constants and the finite-floor tiers;
- the uniform floor from 295 (F_h(294)<1/20<F_h(295), so 295 is sharp for this F_h);
- the n=512 radius-one polynomial values and the absolute-gate values at (512,1) and (192,π/2);
- the corner-256 gate arithmetic and its L-monotonicity;
- the corner-witness geometry, the exact n=2 certificate, the Riesz identity, the arithmetic error budget (84εt<128εt)
  and all counts.
The audit-03 C3-03 block has been removed under architecture B. I checked the replacement (the absolute-gate proof,
consumed here) and it is correct ([D], §5.6). The only premise I did not trace is the bound E_c ≤ t_* sin x, taken from
Lemma uc:master in the comparison, which is outside my range.

**Trust boundary: SUPPORTED, with wording repairs.** The content is now complete and consistent with G01 and J03:
- Python/Fraction, guarded NumPy, IEEE binary64 round-to-nearest with gradual underflow and nextafter, and OS/hardware;
- C++/GMP, 192-bit rounding, compiler and Python driver for 2..40;
- floors, physical cover, corner and far lemmas remain premises.
Three wording points need repair (MINOR C4D-03/04/05): the two witnesses per degree are byte-identical proofs of one
tree; the text never says that native endpoints are neither used nor validated; and the table merges "proved" with
"computed".

**Pedagogy (C4D range): ACCEPT WITH REVISIONS.** There is one MAJOR clarity finding (C4D-01: the corner-lemma losses
δ_A, δ_D are asserted, not derived). The rest is MINOR, NOTE or EDITORIAL. Section 5 is excellent: its elementary proofs
are complete and well paced, and the tiny n=2 certificate and the arithmetic derivation are good additions. §4.4 is
careful. Two paper repairs from audit-03 were never carried into the companion (C4D-02).

**Agreement with the paper: AGREES.** The two texts have the same formal statements, displays, hypotheses, constants,
thresholds and counts: 41; the floor tiers 41≤n<64, 64≤n<160, 160≤n<512; 192, 256, 295, 512; 39 / 280+191=471 /
560+382=942. An automated sentence-containment check ([E] `containment.py`) finds every paper sentence in the companion
except two (C4D-02).

## 2. Findings (prioritized)

### C4D-01 — MAJOR (companion pedagogy; theorem sound) — corner-lemma losses δ_A, δ_D are asserted, not derived
**Location.** Companion loc.tex 1035–1069 (p.113); paper loc.tex 357–374 (terse; acceptable for the paper).

**Reason [D][I].** The two formulas
δ_A = q_h(𝔗−ē+𝔧) − 1/4 − C_4 − h k_Wy and δ_D = 2q_h(𝔗+𝔧) − 4/15 − C̄_E − (3/2)K_D − ē
are the core of the corner lemma. That lemma is consumed by the n≥512 tail and by every certificate for 256..511. Their
derivation needs four comparison outputs from up to 60 pages earlier, and the companion gives only a verbal gloss
(l.1054–1069: "q_h is a rational lower bound for the axis value of u …"). I reconstructed the missing chain:

- **Axes.** Use (uc:relative-comparison) at (h,0) and (0,h): Λ_c − S_n ≥ uU_W − E_c − C_4 − k_Wx x − k_Wy y.
  - U_W ≥ 𝔗−ē+𝔧, since A_4+ρJ_W ≥ 0.
  - u = 1−𝖺 = (1−cos h)/2 > q_h.
  - E_c(h,0) < 6/25 by (uc:central-pair-general), and E_c(0,h) = −B_β ≤ 0.
  - k_Wy = k_Wx + d_β ≥ k_Wx, which is why k_Wy is the single coefficient used for both axes. The text never says so.
- **Diagonal.** Λ_c − S_n = [M_∞(0) − M_∞(φ)] + E_n(0) − E_n(φ) > u(𝔗+𝔧) − E_c − ē − C̄_E − K_D P.
  This combines the model loss of Lemma uc:master, (uc:origin-lower) and (uc:global-error). In it:
  - u = 1 − cos h > 2q_h = 7/24;
  - P = sin x + sin y = √2 < 3/2;
  - E_c < 4/15.

None of u, 𝖺, p, q, P, U_W, E_c, B_β, 𝔧 or k_Wy is recalled locally. The re-entry table (l.326–335) lists only four
outputs and omits Lemma uc:master's loss u(𝔗+𝔧)−E_c and the constants list (uc:constants).

**Impact.** The reader cannot reconstruct the two gates without a long search. This is exactly the kind of hidden step
AC's criterion excludes. C3-02 part (iii) and the C3-04 analogue remain open for the corner lemma.

**Fix.** Insert about eight unnumbered lines after l.1040 that display both chains above, with a one-line reminder of
u=1−𝖺, p=sin x, q=sin y, P=p+q and (uc:constants). Extend the re-entry table with Lemma uc:master (model loss) and
Lemma uc:central-pair (E_c bounds).

### C4D-02 — MINOR (companion fidelity; response-03 C3-06 and C3-09 are marked FIXED but are fixed only in the paper)
**Location.** The paper carries both audit-03 repairs; the companion carries neither. My `containment.py` check found
these as the only real misses.
- Paper loc.tex 208–209 adds "the upper condition is equivalent to q≡1−i, since 2m̄ is even" (C3-09b). Companion
  l.567–578 (p.108) lacks it and still says only "The displayed upper-endpoint parity accounts for precisely this
  change", the wording C3-09 criticized.
- Paper loc.tex 270–271 adds "A phase satisfying ρ≤ρ̄≤1/2 also satisfies ρ≤1/2, so the following fixed-radius bounds
  apply to it" (C3-06). Companion l.837 (p.110) lacks it. Without it, the 1/64 and 1/32 tiers (which come from the
  ρ̄=1/2 bound B♯) are not justified for a chart with smaller ρ̄. The similar sentence at l.883–885 concerns only the
  tail floor.

**Fix.** Insert both paper sentences verbatim at those places. This is wording only, so it is eligible as a listed
auditor MINOR fix.

### C4D-03 — MINOR (both texts; evidence boundary) — "two trees per degree" are byte-identical proofs of one tree
**Location.**
- Companion cert.tex 1470–1471 ("both retained phase trees"), 1484–1487 ("reconstructs both complete trees … All 942
  trees pass"), 1566–1567 (caption "Each phase pair supplies two trees"), 1580, 1813–1816 and 1831–1832 ("two complete
  checked trees").
- Paper cert.tex 312–329, 408–409 and 422.

**Reason [E].** `pair_trees.py` and `pair_diff.py` read data only from the old return and found the following. At all
280 old degrees the primary and fresh certificates have the identical tree, S keys and stored uppers. Every proof field
agrees; only CPU time and the raw-evidence identity differ. The local summary records the same agreement for the 191 new
pairs, and J03/I25 reuses intervals within a degree. So the 942 checked inputs are 471 distinct trees, each recorded
twice by two native passes.

**Impact.** A reader counts 942 independent trees or two proofs per degree. The second record adds native-replay
redundancy, not mathematical content.

**Fix.** Add one sentence: "At each degree the primary and fresh native passes produced the same tree and keys; I25
checks both records, so its 942 checks cover 471 distinct trees." Say "two certificate records" instead of "two trees".

### C4D-04 — MINOR (both texts; trust boundary) — stored native endpoints are neither used nor validated, but this is unstated
**Location.** Companion cert.tex 1505–1506 and 1588–1593 (p.139, 141); paper 347–348 and 430–435.

**Reason [I].** The text says "All 942 witnesses passed its complete revalidation". J03 and RESULTS.json state the
facts plainly:
- `all_native_endpoints_validated: false`;
- 42174 of 43116 stored S uppers satisfy new ≤ old, and 942 do not;
- no native value is a premise.

"Revalidation" can be read as validation of the native certificates.

**Fix.** Use "recertification with substituted bounds". Add: "No stored native numerical endpoint is a premise or is
asserted valid; only the trees and exact phase keys are reused."

### C4D-05 — MINOR (both texts) — trust table merges "proved in the text" with "evaluated by the program"
**Location.** Table cert:trust, companion 1527–1554 (p.140); paper 369–396.

**Reason [I].** The middle column, "Mathematical assertion checked or used", mixes lemmas proved in §§4–5 with
quantities the program computes. Examples of proved lemmas: the kernel and cardinal-reflection identities, the
selected-pair floors, the squared-Peano descent and parity. Examples of computed quantities: interval sums, the GRID/TREE
norm, polygon maxima and strict margins.

The "Analytic branches" row gives "Implementation trust: The stated rational checks", which suggests machine trust in
analytic lemmas. The I25 checker only verifies their metadata and degree guards (check.py l.181–190, 224–230).

OS/hardware trust appears only in the "Closed cover" row, although it applies to every Python row. C3-01's content
items are otherwise all present (G-4 satisfied).

**Fix.** Split the column into "Proved in the text (premise)" and "Computed by the program". In the analytic row write
"none (proved; displayed rational arithmetic)". Move OS/hardware to a footnote covering all rows.

### C4D-06 — MINOR (companion; NOTE for paper) — the leaf test described is not the one I25 executes
**Location.** Companion cert.tex 1166–1174 and 1220–1235 (p.134–135); paper 224–228.

**Reason [E][I].** The companion says "The checker may establish an upper bound for q_R on the whole rectangle and use
that stronger bound … This is the simple constant V_R+θ_RM". "Stronger" is also the wrong word here: a whole-rectangle
bound is weaker. It then proposes the test Q̂_R<L_c.

I25 instead maximizes the quadratic q_R exactly over the clipped polygon R∩T∩proxy (check.py l.121–155). It examines the
polygon vertices, the stationary points along segments and the interior critical point; J03 justifies the
singular-Hessian case. That routine is sound ([D]), but the manuscripts never state it.

MEASURED, using stored native uppers only (not independent arithmetic): on 276 old certificates all 9590 proxy tests
that pass with the polygon maximum also pass with the constant Q̂_R (`tree_stats.py`). So the described predicate
plausibly suffices.

**Fix.** State the polygon maximization and its two-line justification: a quadratic on a convex polygon attains its
maximum at a vertex, at an edge stationary point or at an interior critical point. Say that Q̂_R is a simpler sufficient
alternative.

### C4D-07 — MINOR (companion) — R_ℓ is undefined, and the evaluated kernel form is not displayed
**Location.** Cert.tex 1669 ("Removable quotients use the exact value R_ℓ(jπ)=ℓ(−1)^{j(ℓ−1)}"; p.142) and 1494–1499.

**Reason [D].** R_ℓ(x)=sin(ℓx)/sin x appears nowhere in the companion; the comparison's R_r denotes row sums. I25
evaluates G_n(u,v) = R_{n+1}(s)R_{n+1}(t) + R_n(s)R_n(t) − cos(nu), with s=(u+v)/2 and t=(v−u)/2. That is the corner
section's 𝒟_n minus cos(nu) (corner l.118–125), not the divided-difference form of loc. l.68. The removable value is
correct: lim_{x→jπ} sin(ℓx)/sin x = ℓ(−1)^{j(ℓ−1)} ([D]).

**Fix.** Display the product form with a pointer to §3 and define R_ℓ there.

### C4D-08 — MINOR (both texts; notation collision introduced by architecture B) — P_n has two meanings in §4
**Location.**
- P_n = T_{n+1}+T_n: loc.tex 68 and 418–421.
- The radius-one quadratic P_n(ρ): figure l.312 and caption l.316–317, l.336–337, l.1139.
- A third use: "P<3/2" (l.1050), where P = sin x + sin y.
- Paper: l.20–21, 107 and 418.

**Reason.** The reader can parse "P_n(1/2)<−1/7" as T_{n+1}(1/2)+T_n(1/2).

**Fix.** Rename the quadratic (for example 𝒫_n or Π_n) in both texts. Renaming a numbered-display symbol is a paired
edit, so the correspondence helper must be rerun.

### C4D-09 — MINOR (both texts) — A_* is used with opposite roles inside one proof
**Location.** A_* is a lower bound for numerators at loc. l.452, 581, 589 and 608, but at l.863 and 878 it is an upper
bound for A(b_−). Paper: l.173, 210 and 218 versus 287 and 302.

**Fix.** Rename the tail constant (for example V_*, matching V_ρ̄).

### C4D-10 — MINOR/EDITORIAL (collisions inside one argument)
- In the selected-pair lemma, W_ρ̄ (a constant in the statement) and W (the cosine span, l.452) share a letter (both
  texts).
- The squared-Peano identity integrates in t (l.946, paper 344) where t=B²/2 was defined two lines earlier. Use u_1, u_2.
- In cert, M is both the norm and an integer denominator in "π/M, with M≥2" (l.590, 600); m is the split midpoint
  (l.362) and a mantissa (l.1520) although m=n+1; and E is both the quarter grid (l.1038) and the error allowance
  (l.1771).
- Machin's θ (l.536) is local and acceptable.

### C4D-11 — MINOR (both texts) — ρ, A and B are used before definition
**Location.** The roadmap table (loc. l.284–295, p.48; paper 79–90) and the figure caption use ρ, A and B. ρ is defined
only inside the comparison insert (comparison l.32), and A, B only in the corner lemma.

**Fix.** At l.92 or l.276 add "write ρ=|α|+|β| for the phase radius, and A=|α|, B=|β| for inward phases at a corner
chart".

### C4D-12 — MINOR (companion) — the n=256 substitutions are shown only as results
**Location.** Loc. l.1071–1077 (p.114).

**Reason [E].** I confirmed every bound:
- 𝔗=10.777, ē=0.1874, C̄_E=1.405, C_4=0.0172, k_Wy=0.716 and M(256)=25.39;
- K_D=0.19929, which against 1/5 leaves a margin of 7×10⁻⁴;
- with the coarse rationals, δ_A−r_UM = 2729/21000 and δ_D−2r_UM = 49/1000 exactly.

The tight K_D line, and 𝔗>107/10 (which needs π<22/7; π²<10 is not enough), deserve displayed substitutions.

**Fix.** Show the K_D, 𝔗 and M(256) lines.

### C4D-13 — EDITORIAL — repetition and forward/backward pointers
- The corner proof explains Bernstein scaling three times (l.931–942, 964–973, 975–985).
- Cert restates the phase-to-physical conclusion four times (l.1426–1464; C3-19 is still partly open).
- The arithmetic overview (l.1508–1525) says "the arithmetic proof in the reproducibility package derives this bound"
  although the companion derives it at l.1614–1779. Say "derived below".
- "How the numerical premises are obtained" (l.1494), "The independent calculation has three parts" (l.1603) and
  l.1801–1811 overlap.
- ε_fp is defined twice (l.1511, 1622).
- The jargon "phase keys", "compact returns", "computation sites" and "independently authored" (independent of what?)
  is not explained. GRID/TREE are first named at l.1503 without a pointer to (cert:grid-norm)/(cert:tree-norm).

### C4D-14 — NOTE — folding sentence and the C3-10 display
L.383–385 ("endpoint rows retain the factor f_k or e_j") suggests that endpoint rows contribute. In fact the rows k=0
and k=m are self-paired (s=K, s=K+m), so their defect is zero ([D]). The double-count factor 2 against 1/(4N) is still
explained only in words. One displayed line would close C3-10 completely.

### C4D-15 — NOTE — tight decimal and sharp onset
max P_512 < 0.040785999758 against the displayed 0.040786: the margin is 2.4×10⁻¹⁰ ([E]). It is valid and matches
J01's receipt, and only 41/1000 is consumed. B_41(1/2)<0, so the 1/512 tier is genuinely used; RESULTS.json reports
`minimum_used_floor 1/512`. MEASURED: B_n(ρ̄) decreases in ρ̄ on a grid, although no such monotonicity is needed.

## 3. Audit-03 dispositions verified in this range

| ID | State in current text | Verdict |
|---|---|---|
| C3-01 | Trust table and Proposition present; G01's trusted items named | FIXED in content; wording residue in C4D-03/04/05 |
| C3-02 | Four-output re-entry table (l.326) and §5 role table (l.714); collisions remain | PARTIAL: see C4D-01, 08, 09, 10, 11 |
| C3-03 | Outer-geometry block removed by architecture B; absolute gate replaces it | FIXED; replacement argument correct ([D]) |
| C3-04, C3-15, C3-16, C3-17, C3-21 | Old tuples, 1/8 split, tail-floor radius dependence and G constant removed; corner gate derivative displayed (l.1100–1114) | FIXED |
| C3-05 | C=a−ρ̄/2 grouping (l.805) and tail grouping (l.875–879) displayed | FIXED ([E] all groupings exact) |
| C3-06 | Missing in the companion; present in the paper | NOT CARRIED: C4D-02 |
| C3-07 | Σ_σ endpoint identity with factorization (l.141–148) | FIXED |
| C3-08 | (uc:central-pair-general) with p, 𝖺, I_4 bounds (l.1044–1046) | FIXED ([E]) |
| C3-09 | (a) strict cosine interval present; (b) parity equivalence missing in the companion | PARTIAL: C4D-02 |
| C3-10 | Normalized count displayed (l.583); folding still in words | MOSTLY: C4D-14 |
| C3-11, C3-12, C3-14, C3-20 | Index versus phase units; native stage now historical and "witness" defined (l.492); figure fixed (corner patch drawn, region text corrected); ties covered | FIXED |
| C3-13 | n=2 four-leaf certificate and diagram (l.626–679) | FIXED ([E] reproduced exactly) |
| C3-18 | 𝖺 revealed by the derivation at l.431 | FIXED, adequately |
| C3-19 | Tail summaries merged into Theorem ul:tail-location; cert repetition remains | PARTIAL: C4D-13 |
| G-1 | Proposition and §5.3 use I25 direct sums; native implementation "search" only | FIXED |
| G-4 | C++/GMP/192-bit/compiler/driver and Python/Fraction/NumPy/IEEE/OS named | FIXED |
| G-5 | No Arb/PD-T271 premise in range; "elementary constants of Section 4" | FIXED |
| G-6 | Outward-rounded de Casteljau averages (l.276, 474–487) | FIXED |
| P-08 | Formal Proposition cert:finite-verification with premises table | FIXED |

## 4. Trust-boundary conclusion (task 3) [I][E]

**What the computer certifies.** For each of the 942 records (471 trees), I25 does the following:
- recomputes the interval enclosures of S_n at all retained keys, plus the 15-point GRID set modulo the seam fold;
- recomputes the corner lower endpoint L_c and, for n<256, the three actual-λ uppers;
- builds its own norm M (GRID or TREE);
- runs the exact-rational closed-cover parse;
- maximizes q_R on the polygon for every nonempty near and far proxy, with the degree-correct finite floor;
- checks the strict margins and the corner gap g>0 with PHI⁴.

RESULTS.json margins: near > 289/50000, far > 33/200, corner > 159/5. For n≥192 and n≥256, I25 checks only guards and
metadata.

**What is trusted.**
- Python integer/Fraction arithmetic, guarded NumPy int64 operations, binary64 RN with gradual underflow and nextafter,
  separate ufunc operations (no FMA), strict parsing, and the OS and hardware.
- For 2..40: the C++/GMP checker, 192-bit rounding, g++ and the Python driver.

**What remains mathematical premise (proved in §§2–5).**
- The kernel and cardinal-reflection identities;
- the odd-chart cover and folding;
- λ_n = S_n − Δ and Δ ≥ max(Q_h, Q_v);
- the selected-pair floors;
- positive interpolation and Bernstein;
- the squared-Peano descent;
- corner256, far192, the parity reflection and J02's constants.

**Consistency with G01 and J03.** The manuscripts match G01 §"Current direct-sum route" and J03. The certificate
metadata (floor tiers, the far guard |α/π|+|β/π|≥1/2 with gap 3/100, the corner patch [0,π/4]² with loss 1/30) match the
manuscript statements exactly (check.py l.177–186 and 224–230 against ul:finite-floors, ul:far192 and ul:corner256).

**Data reads [E, MEASURED].** Old tree node range 51..101 (n=41 has 101 nodes). ACTUAL_THREE corners occur exactly for
n≤255 and analytic corners from 256. Analytic far leaves and the GRID norm occur from 192.

**Not verified.** I could not check from data the 320..510 shape "51 nodes, 26 leaves, three analytic far leaves, GRID";
the new certificates are not available locally. The claim is consistent with the 511 record (51/26/3 far, GRID).

## 5. Independent verification record (all in `$A/c4d-code/`)

Environment: Python 3, mpmath 1.3.0, sympy and numpy from `$A/../audit3/pylib`. Total CPU about 2 minutes. No build, no
native engine, no Syvert and no Git state change. No archive code was executed; the return tar was read as data only
(`python3 -I`).

1. `gates.py` [E] — mpmath interval arithmetic at 200 bits, from definitions transcribed from (uc:constants),
   (uc:uniform-allowance) and (uc:analytic-norm).
   - **n=512:** d_x > 2.76; d_β = 5.08×10⁻⁴ ∈ (0, 5/48); max P < 0.0407860; vertex < 0.14735 < 3/20;
     P(1/2) < −0.1430697 < −1/7; x_*, y_* > 0.22.
   - **G(512,1)** > 0.5342647, with (t_*+2K_D)/Θ < 0.0475 < 3/50 < tan(1/2).
   - **G(192,π/2)** > 0.098319, with ratio < 0.0981 < 1/10.
   - **n=256:** all seven displayed bounds hold.
   - **Corner gates:** with π⁴/6144 exact the gates are 0.3256 and 0.1033 (claim > 49/2000). MEASURED: the gates rise at
     n = 300, 400, 10³, 10⁴ and 10⁶.
2. `exact_constants.py` [E] — 90 Fraction or interval checks, all pass.
   - **Class constants:** class 1 = 37/(224(π+1/2)) > 1/32, and 225/(1040(π+1/2)) > 1/20; class 2 > 35/656; class 3 >
     1/512; the slack is (17π−21)/41.
   - **Band constants:** T_c ∈ (239/100, 12/5); the trigonometric and logarithmic brackets; the U, V, W groupings at five
     values of ρ̄; the B_n coefficients; B♯ and both exact margins.
   - **Tail constants:** I_*, R_*, A_*, the tail coefficients, and F_h(295) > 50064/10⁶ with F_h(294) < 1/20.
   - **Corner constants:** 2729/21000, 49/1000, 10451/30000, 49/1250, the E_c pieces and (9/25)/√2 < 4/15.
   - **§5 constants:** 784/663; 2²⁶/27! < ε; the majorant < 2; the normal guard > 1/4; 1/25! > 2⁻⁸⁵; 2γ₃₈ < 77ε; the
     ϑ/t ratio within 1 ± 6ε; 128ε = 2⁻⁴⁶; p_fp = float(π) with |π/p_fp − 1| ≤ 2ε; the Machin tangents; the A₈₀
     orientation; the corner witness (u'+v' = 25/512, max(u', μ⁴v') = u', 3π/16 > 1/2).
   - The single reported "failure" is mine: 6π/25 > 471/625 holds strictly because π > 157/50, while my check
     substituted the bound itself.
3. `n2_and_cover.py` [E] — exact sympy Vandermonde inversion, independent of the kernel formula.
   - The node list equals Padua(2), and Λ_c(2) = 3 at (−1,−1) and (1,−1).
   - The lower-left Bernstein sum matrix is exactly (3,5/3,2; 11/6,2,5/3; 1,2,5/3); the lower-right has 3 at index
     (2,0); both upper leaves have maximum 5/2.
   - Odd-centre cover for n=2..8: every mesh rectangle has exactly two opposite odd vertices with distances summing to 2,
     and a 1/12-index grid has 0 uncovered points.
4. `riesz_reflection.py` [E] — at 40 digits: c_j multipliers ip for p = −d..d (including the aliased −id), the
   alternative coefficient formula, and Σ|c_j| = d for d = 1..8, all to 10⁻³⁰. MEASURED for n=3..6:
   λ = S−Δ to 2×10⁻¹⁴, Δ ≥ max(Q_h, Q_v), the S symmetries, S(0,0) = Λ_c and Δ(corner) = 0.
5. `containment.py` [E] — whitespace-normalized sentence containment of the paper in the companion. There are 17 and 10
   raw misses; all but two are paraphrases or display-boundary artifacts (C4D-02).
6. `tree_stats.py`, `pair_trees.py`, `pair_diff.py` [E, data-only, MEASURED] — the old certificates' node range,
   norm/corner/far kinds by degree, the identity of the primary and fresh pairs (280/280), and the comparison of Q̂ with
   the polygon test (0 of 9590 differ). These imported only the pure helpers of the pinned `check.py` (parse, fold,
   maximum, floor, PHI). No interval evaluator ran; this was not a rerun of I25.

Hand derivations [D]:
- the numerators A(u,v) for both projections (vertical and horizontal parity and sign);
- the class-1 parity at both endpoints;
- the folded Q_v factor;
- the layer-cake row bound, including the case b > θ_c;
- the rectangle-rule bracketing;
- the squared-variable double integral (mass 1/3);
- the bilinear Peano assembly and the corner coefficient (16/π²)(δ − Mπ⁴/6144);
- the absolute-gate R(h) argument;
- the relative-polynomial line maximum and the vertex identity ℓ_x/(2d_x) + ℓ_y/(2d_y);
- the de Casteljau left and right lists, power-to-Bernstein, the arctan and cosine remainders, Horner's 38-factor count,
  and the n=1 formula.

## 6. Standard tools, figures and pacing (tasks 4 and 6) [I]

**Usable statements with hypotheses are given for:**
- the trigonometric Bernstein inequality, with a complete finite Riesz proof, global-norm emphasis and frequency rescaling;
- Bernstein basis positivity, partition of unity, power conversion and exact de Casteljau;
- the interval rules (±, ×, ÷ excluding 0, |·|, floor/ceil averages, adjacent-float widening, pairwise sums);
- the Peano kernel (exact kernel and mass; no mixed derivative), layer cake, the rectangle rule and the lattice counts;
- the mean-value theorem, used for the argument error.

Lipschitz covers are not used, and curvature covers replace them consistently. Still missing: the exact polygon
maximization (C4D-06).

**Figures.**
- §4 folded triangle (p.52): correct regions and labels. It floats into the comparison insert, so it appears 50 pages
  before the lemmas it summarizes. Add a "see Figure" pointer at Theorem ul:tail-location.
- §5 (a,b) diagram (p.127): correct cuts 1/(2π) and 1/2, the corner patch (1/4, 3/16) and correct region text.
- n=2 diagram (p.125): correct.
- The trust table (p.140) is readable but needs the column split (C4D-05).

**Pacing.** §4.4 is well paced and each constant is explained. The corner lemma is uneven: Bernstein is over-explained
three times while the δ formulas are under-explained (C4D-01). §5.1–5.2 are excellent. §5.3 is dense but complete; trim
the repetitions (C4D-13).

## 7. Prioritized fix list

1. C4D-01: derivation chains for δ_A and δ_D, and the re-entry rows for uc:master and uc:central-pair (companion).
2. C4D-02: insert the two missing paper sentences into the companion (eligible auditor MINOR fix).
3. C4D-03, C4D-04, C4D-05: evidence-boundary wording (identical pairs, no native endpoints) and the trust-table column
   split (both texts).
4. C4D-06, C4D-07: state the polygon maximum and the product kernel form with R_ℓ (companion).
5. C4D-08, C4D-09, C4D-11: rename the radius-one P_n and the tail A_*, and define ρ, A, B before the roadmap (both
   texts, paired edit).
6. C4D-10, C4D-12, C4D-13: local renamings, the n=256 substitution lines, the repetition trims and the pointers.

## 8. Coverage and limits

**Covered.**
- Every line of companion localization-unified.tex outside the comparison input, every line of companion
  certification-unified.tex, and both paper counterparts.
- check.py, G01, J03, RESULTS.json, local-onset512-summary, compact-return, audit-03 C3, response-03, the brief and
  handoff, and the companion README/BUILD/review.

**Not covered.**
- The comparison text (consulted only for definitions);
- Sections 1–3;
- the J01/J02 checkers and I25 runs;
- the new 320..510 certificates, which are unavailable locally.

**Limits.** Native data reads are MEASURED and validate no endpoint. Paired renamings (C4D-08, C4D-09) touch numbered
blocks, so the correspondence helper must be rerun after them.
