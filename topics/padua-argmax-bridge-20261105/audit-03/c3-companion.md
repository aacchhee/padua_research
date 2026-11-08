# C3 — Companion audit: Section 4 localization material and Section 5 certification

Auditor: Claude Opus 5.5, xhigh effort (sub-auditor C3 in the substantive Claude audit, handoff 28).
Role: independent mathematical and pedagogical reviewer; no repository writes, no Git state changes.
Rules read at head `f366535e1fa4ede566cb83bdc554220c12b307cf` (AGENTS.md, agents/WORKFLOW.md,
agents/claude/CLAUDE_ROLES.md, claude-audit-brief-20261108.md in full, companion README/BUILD/review.md).
Branch `codex/padua-argmax-bridge-20261105`.

Audited sources (hashes re-computed, equal to the frozen values in companion-paper/review.md):
- `companion-paper/sections/localization-unified.tex` 600c06cc…dc41 (1873 lines): read every line
  except the included comparison text (line 271 `\input{sections/comparison-unified}`), which is outside
  C3 scope; comparison passages were consulted only to find definitions (a, j, U_N, U_W, M(n), I_4,
  central-pair bounds, constant enclosure).
- `companion-paper/sections/certification-unified.tex` a9d9874f…4b09 (1641 lines): every line.
- Paper counterparts `paper/sections/localization-unified.tex` (559 lines) and
  `certification-unified.tex` (265 lines): every line.
- Trust sources: `theory/G01-all-degrees.md` (all), `compact-return.md` (lines 1–60 plus searches),
  `paper/small-degree-unification.md` (all).
Page references are to X's fresh companion build in `$A/build/companion/main.pdf` (via
`$A/build/text/companion.txt` and `$A/build/page-index.md`): §4 starts p.46, §4.3 p.111, §4.4 p.119,
§4.5 p.124, §4.6 p.128, §5 p.133, §5.1 p.137, §5.2 p.144, §5.3 p.158. I did not build anything.

Labels: [D] = derived/checked by hand or exact algebra; [E] = executed computation (scripts in
`$A/c3-code/`); [I] = inspection/judgment. Measurements are labeled as such; none upgrades a claim.

## 1. Verdicts

**Mathematics of the added explanations in C3 scope: SUPPORTED, no BLOCKING finding.** Every added
derivation, worked example and numeric table entry in the localization material and in Section 5 that
I re-derived or recomputed is correct ([D]/[E], §4 below), including the finite trigonometric Bernstein
(Riesz) proof, the de Casteljau and power-to-Bernstein identities, Machin and Taylor remainders, the
odd-centre cover, the pair-defect identity, all selected-pair constants, E_n margins, the radial
quadratic and discriminant, the outer gate, the far-192 anchor and the corner-256 gate arithmetic.
One stated **reason** in an original sentence is wrong although its conclusion is true (C3-03), and the
grid-norm, tree-norm, proxy and corner-witness logic is complete.

**Pedagogical verdict for the C3 range: REVISE** (MAJOR: C3-01 trust boundary, C3-02 notation and re-entry; C3-03 is a MAJOR proof-reason repair). Section 5 is close to the required
standard: its elementary proofs are complete and well paced. The localization material after the
60-page comparison insert (§4.3–4.6, pp.111–133) is locally careful but hard for the intended reader to
follow globally: symbols and constants are reused with several meanings and imported from the
comparison without a re-entry summary (C3-02), and §4.4 still hides its central coefficient
derivations (C3-04). The evidence/trust paragraph of §5.3 is clear in tone but incomplete against G01
(C3-01).

**Agreement with the paper (C3 range): AGREES.** Same numbered statements and formulas, hypotheses,
thresholds and counts: 41, floor tiers 41≤n<64 / 64≤n<160 / 160≤n<512 (and the 511 control in the
third tier), 192, 256, 320, 280 = 279+1 pairs, 560 proofs, ranges 2..40, 41..319, n≥320. All original
sentences survive except one harmless paraphrase (C3-21). Findings C3-01, C3-03, C3-07, C3-08 apply
equally to the paper and need a coordinated fix.

## 2. Findings (prioritized)

### C3-01 — MAJOR — §5.3 trust boundary incomplete and partly inconsistent with G01 (both texts)
Location: companion cert.tex 1535–1641 (pp.158–161); paper cert.tex 245–265; intro.tex ~267 (p.6).
Reason: G01 (lines 74–90) lists as trusted implementation inputs: Arb/GMP/MPFR arithmetic, the captured
compatible runtime, **finite-polynomial collision formulas**, compiler/native interfaces and the
**exact-rational checker**, plus PD-T271 (the constant enclosure) as a named computer-assisted
dependency. It also says explicitly that the unsampled native premises were *not* independently
replayed and that the two samples are not a statistical proof. §5.3 names only "arithmetic
implementation, compiler and native interfaces". Missing for the reader:
(a) the limiting-constant enclosure (Arb, 320 bits, K=64; described only inside the comparison, p.68,
and in one sentence at the end of §4, p.133). It feeds not only n≥320 but also the far-192 and
corner-256 branches used *inside* 41..319. The introduction (p.6) says "These dependencies are described
in Sections 4 and 5", but §5 does not describe it;
(b) collision-value formulas used by the native kernel evaluations;
(c) the exact-rational checker and its runtime;
(d) the small-degree trust chain: one C++/GMP checker, 192-bit outward integer rounding and g++
(small-degree-unification.md), which §5.1/§5.3 never name;
(e) G01's negative scope statement: unsampled histories were validated by the collector on the
production machine and not inspected locally; samples 199 and 238 are not statistical evidence for the
other degrees;
(f) "companion reproducibility notes" (p.160) points nowhere. In the companion it even reads as a
self-reference.
Impact: a reader cannot tell exactly what the computer certifies and what is trusted; the companion
understates the trusted base relative to the canonical theory record.
Fix: add a short table to §5.3 (both texts): *stage | what is proved mathematically | what is computed |
by which component | what was independently re-executed | what is trusted*. Rows: constant enclosure;
native vertex/point enclosures (Arb balls → binary64 endpoints, collision formulas); exact-rational
checker; small-degree C++/GMP checker; retention/sampling. Copy G01's negative sentence. Replace
"companion reproducibility notes" with repository paths (compact-return.md, compact_pack/README.md,
small-degree-unification.md).

### C3-02 — MAJOR (pedagogy) — symbol overload and missing re-entry after the comparison insert
Location: §4.3–4.6 (pp.111–133) and §5 (pp.133–161); worst instances listed.
Reason [I]: after pp.50–111 the reader returns to dense arithmetic in which many letters carry 2–4
meanings within a few pages:
L (periodic mesh, p.113, vs log n, p.120 and p.131);
H (H_rs; H(g), p.117; H=1+L, p.120);
K (centre index; outer-gate slope, p.126; curvature bound K, p.133);
A (numerator A(u,v); A(b); A_r; gate coefficient A, p.126; corner phases A,B, p.128);
C (a_r−r/2, p.118; 1+8a_0m/(3π), p.124; Λ_c in §5.1, p.138);
r (radius vs periodic index in the Q_v formula on the same page, p.112);
s (periodic index, endpoint distance, squared variable);
a (a_j; a in A(u,v), defined only in the comparison, p.51; a_r; band endpoint a_0 vs a_0=337/384;
rectangle a_0,a_1 in §5);
j (node index; model constant j=H_0+d_0−g_0, p.63; j_*);
q (offsets; q=sin y; q_0; the corner-witness q in §5);
U,V (U_r,V_r vs the corner rectangle U,V); M (physical mesh vs norm M, M(n)).
The comparison constants T, D, 𝓜, ē, C_4, k_{Nx}, k_{Ny}, k_{Wx}, k_{Wy}, U_N, U_W, J_N, A_4, K_D, W_n,
C̄_E, j, I_4, E_c are used in §4.4–4.6 with no reminder of meaning or location. The companion flags only
r (p.111) and a_0,b_0 (p.124).
Impact: the intended reader cannot reconstruct §4.4–4.6 without repeatedly searching 60 earlier pages.
This is a clarity failure on the central proof chain.
Fix (numbered blocks must stay byte-identical, so use unnumbered text): (i) open §4.3 with a one-page
re-entry box listing the four outputs of §4.1–4.2 used later — (uc:relative-comparison),
(uc:global-error)/(uc:phase-allowance), (uc:model-loss), (uc:origin-lower) and (uc:analytic-norm) —
with their pages and one-line meanings; (ii) give a symbol table per subsection, marking local
reuses explicitly ("in this subsection L denotes the periodic mesh; from §4.4 on, L=log n"); (iii) at
first use in §4.4 give a table of the constants with their defining equation and value at n=320.

### C3-03 — MAJOR (stated reason wrong; conclusion true; one-line repair; both texts)
Location: loc.tex 1285–1287 (p.124); paper loc.tex 364–366.
Reason [E]: "The cases x≤1/2 and x≥1 follow from sin(1/2)<p_0 and u≥11/48". For x≥1, u≥11/48 only
gives v≥41/384 and p_0+η√v ≥ 12/25+(3/2)√(41/384) = 0.9701, while sin x reaches 1 for
x∈[1,π] (sin x>0.9701 for x≈1.33–1.81). The inequality max(p,q)≤p_0+η√v is nevertheless
true: for x≥1, cos y≤1 gives u≥(1−cos x)/2, and
sin x ≤ 12/25+(3/2)√((1−cos x)/2−47/384) on [1,π] with minimum slack 0.1302 (grid of 10^5 points,
`outer_geom.out`; provable because the right side increases on [1,π] and already exceeds 0.97 at
x=1 while it reaches 1.40 at π/2). A full grid of (ul:outer-geometry) on 1≤ρ≤π found every
inequality satisfied (min slacks 3.9e-5, 0.0050, 0.0088, 0.0012).
Fix: replace "u≥11/48" by "u≥(1−cos x)/2, so v≥(1−cos x)/2−u_1, and the one-variable inequality …
holds on [1,π]". In the companion, also write the step for 1/2≤x≤1 explicitly:
sin x ≤ sin(1/2)+c h ≤ sin(1/2)+√(96c v/47) with √(96c/47)<3/2.

### C3-04 — MINOR (hidden derivation; central for the reader) — §4.4 coefficient tuples and the ρ=1/8 split
Location: loc.tex 1107–1115, 1148–1149, 1176–1179, 1186–1189 (pp.121–122).
Reason [D][E]: (ℓ1,ℓ2,d1,d2)=(12531/20000, 11056/20000, 1911/800, 24539/8000) are asserted. The
reconstruction is ℓ1=k_{Nx}+(3/8)(1/5) (from x^{3/2}≤5x²/4+x/5); ℓ2=k_{Ny};
d1=(47/192)(U_N)−15/32; d2=(47/192)U_N+1679/8000, with U_N>23337/2000+(21/500)ρ.
**The split at ρ=1/8 is forced here**: with ρ≥1/8, d1 ≥ (47/192)(23337/2000+21/4000)−15/32 = 2.388887
≥ 1911/800=2.38875. Without the ρ-term one gets 2.387602 < 1911/800. The companion's explanation (p.122:
"uses the substantial positive floor available at the centre") does not give this reason. The wide
tuple (11/16, 47/80, 9/4, 8/3) similarly needs U_W≥T−ē+j>2331/200 and x^{3/2}≤x²+x/4:
(11/48)(2331/200)=2.6709≥8/3, minus 5/12 =2.2543≥9/4, and 583/1000+5/48=0.68717≤11/16 (all [E]).
Fix: display these four short lines for each tuple and state the true reason for the 1/8 split.

### C3-05 — MINOR — derivation of U_r, V_r, W_r and of the tail band constants
Location: loc.tex 887–892, 938–945 (p.118–119).
Reason [D][E]: the inequalities I>U_r, A_0<V_r, R<W_r hold only when the reader keeps
C=a_r−r/2>0 as a single factor: I = C·π/5 + a_r(cos π/4−cos π/20) > (157/250)C + (707/1000−247/250)a_r =
U_r. If a_r and r are separated and π<22/7 is used on −rπ/10, one obtains −11r/35, which looks
inconsistent with −157r/500. The same holds for R (factor C·log ratio < (5/3)C) and for I_h, R_h, I_w,
R_w (6π/25>942/1250, 47π/300>7379/15000; all reproduced exactly).
Fix: show I = C(b_0−a_0)+a_r(cos b_0−cos a_0) with C>0 and the one-line substitution for each of the
seven constants.

### C3-06 — MINOR — why r=1/2 controls every r≤1/2 in the finite floor tiers
Location: loc.tex 919–936 (p.119).
Reason [D]: the tiers 1/64 and 1/32 come from E_n, which uses r=1/2 constants (A_0<11/20 and R<14/25
hold at r=1/2, not at r=0). The valid argument is monotonicity of the *hypothesis*: a point with
ρ≤r≤1/2 also satisfies ρ≤1/2, so the lemma at r=1/2 applies. This is not stated, and "the maximum
with the universal floor" is unexplained. Note [E]: B_41(1/2)=−0.00195<0, so the 1/512 tier is genuinely
needed for small n.
Fix: one sentence plus the observation B_41(1/2)<0.

### C3-07 — MINOR (both texts) — endpoint identity and multiplicity statement
Location: loc.tex 136–144 (p.48); paper loc.tex 40–43.
Reason [E]: Σ_{0≤j≤n, σj≡r (2n)} e_j = 1 is true only when σ=±1 is summed as well. With σ fixed the
sum is 1/2 at r≡0 (checked n≤11). The "conversely … precisely the multiplicity" step also omits that
j+k even is automatic for (r,s)∈Γ⁻ and that the weight sum factorizes.
Fix: write Σ_{σ=±1}Σ_{j:σj≡r} e_j=1 and give the three cases r≡0, r≡n and the others; add the
factorization line.

### C3-08 — MINOR (both texts) — which central-pair bound gives E_c(h,0)<1/4
Location: loc.tex 1702–1703 (p.131); paper 498–499.
Reason [E]: the displayed (uc:central-pair-bounds) branch for ρ≤1 gives 5h^{3/2}/12=0.2900>1/4 at
h=π/4. The claim follows from (uc:central-pair-general) with p=sin h, a=(1+cos h)/2:
(4I_4/π²)p^{3/2}/√a ≤ 0.2311 (using I_4<319/360). The true value is I_4=0.874019.
Fix: cite (uc:central-pair-general) and show the two values.

### C3-09 — MINOR — straddling and parity details in the first centre class
Location: loc.tex 535–557 (p.114).
Reason [D]: (a) |w−b|<γ implies that cos w lies strictly between the targets only because cosine is
monotone on [b−γ,b+γ]⊂(0,π). This holds since b≥π/4>1/3>γ, but the text does not say it. (b) The
upper-endpoint parity M+q≡1−M+s is equivalent to q≡1−s, since 2M is even. So the same offset list
serves both ends. The text says the displayed parity "accounts for this change", which suggests a
different condition.
Fix: two clauses.

### C3-10 — MINOR — Q_v folding and pair-count assembly shown only in words
Location: loc.tex 360–386 (p.112); 559–566 (p.114).
Reason [D]: the folded formula follows because each unordered pair {s,2K−s} occurs twice in Γ⁻ and the
self-paired s=K, K+m contribute zero defect; this gives the factor 2f_k against 1/(4N). The class-1
bound is (1/(ML))·(#rows≥M/4−1)·(2s pairs)·(2A_*/W), with W≤2(sπ+r)/M. Both are reconstructible
([D] reproduced 37/(224(π+1/2)) and 225/[1040(π+1/2)] exactly), but neither appears as a displayed
line until the η_r version on p.115.
Fix: one displayed line each.

### C3-11 — MINOR — inconsistent "scaled distance" units in one paragraph
Location: loc.tex 87–99 (p.47). The added sentence says a chart is "scaled distance … at most π"; the
original says "scaled distances … sum to two, so one is at most one". Define index distance and phase
distance (phase = π × index distance) once.

### C3-12 — MINOR (pedagogy, §5) — native stage and evidence vocabulary
Location: cert.tex 487–493, 657, 1244 ("witness" used before its definition at p.159); 1536–1620.
Reason [I]: Arb "ball" (midpoint–radius) arithmetic, MPFR (correctly rounded floating point) and GMP
(exact integers/rationals) are never described. Nor is how the vertex data W_z for S_n are produced
(a sum of 2nm outward kernel enclosures, with collision values). Further undefined terms:
"primary/fresh pass", "account/exit links", "collector", "selective retention" and "production machine"
(the paper's Syvert).
Fix: one paragraph "What the native stage computes", and define "witness" at first use (p.141).

### C3-13 — MINOR (pedagogy, §5) — add one tiny explicit certificate
Location: §5.1 (pp.137–144).
Reason [E]: an exact four-leaf certificate exists for n=2, auditor-constructed in `n2_cert.py`
independently of the kernel formula, by Vandermonde inversion. Its nodes are (1,1),(1,−1/2),(0,1/2),
(0,−1),(−1,1),(−1,−1/2), and Λ_c(2)=3=λ_2(1,−1). Split x at 0, then y at 0.
On [−1,0]×[−1,0] the 3×3 tensor Bernstein coefficient sums are
(3, 5/3, 2; 11/6, 2, 5/3; 1, 2, 5/3), indexed (i,j). The vertex (0,0) is exactly 3, and every other sum
is ≤2<3. The mirror leaf [0,1]×[−1,0] has 3 at index (2,0). The leaves y≥0 have maximum 5/2<3. This
matches the small-degree inventory (2 strict leaves, 2 corner leaves, depth 2), and all numbers are
rational. A half-page with this tree, its picture and one coefficient matrix would make §5.1
concrete. A schematic phase tree showing the near/far proxy strip and the corner rectangle would do
the same for §5.2.

### C3-14 — MINOR — phase diagram (p.145)
Reason [I][D]: the geometry is correct (blue a+b≤1/(2π) ⇔ ρ≤1/2; grey 1/2≤a+b≤1 ⇔ ρ≥π/2). However:
(a) the label "ρ=π(a+b)" sits inside the grey region and reads as a region label;
(b) the corner-witness rectangle a≤1/4, b≤3/16 (A≤π/4, B≤3π/16) and the rational proxy strip, both discussed
in the text, are not drawn;
(c) "The unshaded region is handled by the appropriate numerical predicates" (cert.tex 689) is
incomplete: the blue region is also numerical (defect-floor test, or the corner witness below 256), and
so is the grey region for n<192.
Fix: move the label to the axis, add the corner rectangle and the proxy strip, and rephrase (c).

### C3-15 — MINOR — monotonicity derivatives asserted
Location: loc.tex 1024–1029 (p.120), 1396–1399 (p.126), 1743–1745 (p.131).
Reason [I][E]: "(T+A_4+ρJ_N)' > 45/(16n)−184/(15n²)−78/n³" is checked only at its final rational step.
The derivative itself (T'=(8L−3)/(π²n), A_4', J_N', and absorbing the H/n² terms) is not shown. I
measured n·[(T+A_4+ρJ_N)'−RHS] ≥ 1.565 for n∈[320, 320e^7], ρ∈{0,1/2} (measurement only). "Every cost
decreases" relies on the template on p.120. Listing which template each cost uses would close the gap.

### C3-16 — NOTE — tail floors are negative at their stated start n=64
Location: lemma, loc.tex 338–356 (p.112). [E] min(F_near,F_small,F_h)≈−0.051 at n=64, ρ=0; positive by
n=160 (0.072) and used only from 320. This is harmless (the inequality is trivial there), but a sentence
avoids confusion.

### C3-17 — NOTE — outer-gate G constant
Location: loc.tex 1390 (p.126). Substituting the displayed component bounds gives
G>196691/2400000; the text states 195191/2400000. The stated value is weaker and therefore valid; show
the substitution. Also p.131 uses π²<10 (for 16/π²>8/5) without stating it.

### C3-18 — NOTE — first use of a in A(u,v)
Location: loc.tex 387–389 (p.112). a is defined 60 pages earlier (comparison, p.51, a=c_ec_d) and in
§4.3 only implicitly (p.112) or explicitly (p.115). Add "a=(cosα+cosβ)/2" at first use. Note also
that "(\sin\alpha/2)" in the retained display means (sin α)/2, as the companion's p.112 display shows.

### C3-19 — EDITORIAL — repetition
Repeated passages: loc.tex 4–12 vs 37–42 (p.46); the proof of Theorem 1.1 restates the case division
three times (1807–1857) and the dependency sentence twice (1859–1872, pp.132–133); cert.tex 1495–1533
(four overlapping completion summaries, pp.158–159); cert.tex 1599–1608 vs 1633–1641. Trimming frees
space for C3-02/C3-13.

### C3-20 — EDITORIAL — chart-tie statement
Location: loc.tex 1838–1840. "chart ties also retain the strict conclusion" is correct but would read
better as "every chart containing the point yields a strict bound, so the choice does not matter".

### C3-21 — NOTE — single paraphrase of an original sentence
Location: loc.tex 1352. "Positive majorization at an actual phase using (ul:outer-geometry) therefore
gives" became "Combining these substitutions with all the remaining positive allowance terms gives".
The new wording loses the explicit reference to (ul:outer-geometry); restore it. No other
original sentence in the C3 range was altered (automated containment check).

## 3. Subsection assessment (purpose, prerequisites, definitions, gaps)

- **§4 opening and reflection geometry (pp.46–50, loc.tex 1–269).**
  Purpose: reduce λ_n to a phase-only majorant S_n minus a nonnegative loss Δ.
  Prerequisites: the cardinal formula, G_n and product-to-sum (preliminaries).
  Definitions: odd centre, chart, Γ⁻, S_n, Δ_JK, the pair defect 𝔡 and the projections Q_h, Q_v are
  all defined before use, with good motivation (sign-loss example 3,−2,1,−1; the four-term defect
  identity; the symmetry reductions done on indices).
  Gaps: C3-07, C3-11, C3-18.
- **§4.3 selected-pair lemma (pp.111–119).**
  Purpose: a uniform positive floor for an eligible projection.
  Well explained: homogeneity, the numerator derivation by angle addition, the 2A_*/W bound,
  lattice counting with open arcs, the three classes, layer cake, the rectangle rule for monotone
  sums, concavity by H''≤0 with explicit signs, the endpoint subtraction (1/14, 5/64) and the
  coefficient substitutions.
  Gaps: C3-05, C3-06, C3-09, C3-10, C3-16. A figure of the circle showing two target cosines, the
  periodic parity grid and the selected arcs for the three classes would help most here.
- **§4.4 near/annulus (pp.119–124).**
  Good: the log-series tail bound, the derivative template, the radial maximisation without case
  analysis, the discriminant explanation and the short-radius computation.
  Gaps: C3-04 (main), C3-15, C3-02 (constants).
- **§4.5 outer and far-192 (pp.124–128).**
  Good: the u-quotient monotonicity is verified term by term; Ψ_r, Ψ_s; the entropy concavity and
  tangent; the completion of the square.
  Gaps: C3-03, C3-17, C3-02.
- **§4.6 corners and proof (pp.128–133).**
  Good: the signed-maximum identity, the squared-variable double integral and its continuity at 0,
  Bernstein frequency scaling, the bilinear Peano assembly and the gate monotonicity in L.
  Gaps: C3-08, C3-17, C3-19, C3-20.
- **§5 intro and Lemma 5.1 (pp.133–137).**
  Excellent: certificate/leaf/enclosure/checker/predicate are defined first; the |x| example; Peano
  kernel derivation with exact mass and the t² example; slack propagation.
- **§5.1 (pp.137–144).**
  Correct and complete: Bernstein basis, strict corner leaf (C−(C−D_R)(1−w_*)), toy pattern, tree
  coverage by induction, power-to-Bernstein, de Casteljau left/right, interval averaging with
  floor/ceil, arctan/Machin/cosine remainders, monotone cosine bracketing, absolute-value and product
  enclosures, and degree 1.
  Gaps: C3-13, and the checker identity (C3-01d).
- **§5.2 (pp.144–158).**
  Correct: frequencies, the Riesz identity, the global norm via folding and compactness, tree and grid
  norm absorption, the quarter grid (15 points, 10 squares, 13 representatives), proxies and
  nonemptiness tests, the corner witness scaling and the analytic substitutions with full guards.
  Gaps: C3-12, C3-14.
- **§5.3 (pp.158–161).**
  Plain and accurate about what it states (counts, binary64 exactness, levels of evidence).
  Incomplete on what is trusted: C3-01.

Definitions-before-use status for the terms in the brief: unisolvence, cardinal and angular kernels
(Section 2, outside range; used consistently); checkerboard parity (p.47 ✓); charts (✓); defects (✓);
floors (p.111 ✓); norm witnesses (the term "witness" is used before its definition, C3-12); Bernstein
coefficients (✓); interval certificates and enclosures (✓); phase cover (✓); strict continuous-domain
coverage (✓, induction pp.140–141 and 152).

## 4. Independent verification record

All scripts and outputs are in `$A/c3-code/`
($A=/tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit3).
Python 3 with mpmath 1.3.0, sympy 1.14.0 and numpy 2.5.3 from `$A/pylib`.

- `geom_checks.py` [E]:
  - Cardinal deltas at nodes ≤1e-15 (n=2..5); unisolvent dimension equals the node count.
  - The divided-difference G_n equals the defining sum (≤5e-12).
  - Exact Fraction enumeration for n=2..8: every mesh rectangle has exactly two odd vertices, which
    are opposite, and their L1 index distances sum exactly to 2. A 1/12-index grid has no uncovered
    point.
  - The periodic S_n equals Σ_jk (w/4)Σ|g| (≤6e-15).
  - Δ−(eligible projection) ≥ −1e-15 (n=2..6, random charts).
  - The S_n symmetries (±α, ±β, +2π, (π,π)-shift, (π−x,π−y)) hold to 6e-15.
  - S_n(0,0)=Λ_c (n=3,4,6).
  - Vertical and horizontal half-kernels equal A(u,v)/(cos u−cos v), with a=(cosα+cosβ)/2 and the
    stated signs (≤4e-13).
  - The endpoint identity holds only when σ is summed (C3-07).
- `cert_identities.py` [E]:
  - Riesz coefficients c_j=(−1)^{j−1}/(4d sin²(τ_j/2)): multipliers ip for p=−d..d (including the
    aliased −id) to 1e-39, Σ|c_j|=d exactly, the alternative Fourier formula agrees, and signs
    alternate (d=1..8, 40 digits).
  - T'=Σc_jT(x+τ_j) for random real T (d=3,8,15); ‖T'‖≤d‖T‖ and ‖T''‖≤d²‖T‖.
  - The sine product 2^{1−p}sin(px), the csc² sum, and zG'=2z^{1−d}/(1−z)² at z^{2d}=−1.
  - The power-to-Bernstein identity and the de Casteljau left d_0^{(j)} and right d_j^{(n−j)} lists
    with a shared midpoint, exact for n=2,3,5,7; the s(1−s) example.
  - Peano kernel identity and mass (x−u)(v−x)/2.
  - Arctan partial-sum parity and bound; Machin: tan2θ=5/12, tan4θ=120/119, tan(4θ−φ)=1.
  - The cosine remainder sign and bound (z≤2).
  - λ_1 formula, maximum 2 at (−1,±1).
  - Quarter grid as stated above; 784/663.
- `loc_constants.py` [E]: 66 checks, all OK (exact Fractions or 60-digit mpmath).
  - Class-1/2/3 constants (37/(224(π+1/2))=0.04536; 225/[1040(π+1/2)]=0.05941; 33/(16π√3)(1/6−1/41)
    =0.05393>35/656; (7/8)(29/492)²=0.00304).
  - 2/(3π√3)>35/286 with margin 1.4e-4 and the exact 572/105 route; T_c bounds; the
    trigonometric/log-ratio bounds.
  - I>U_r, A_0<V_r, R<W_r on r∈[0,1/2]; all coefficient substitutions; the E_n formula and both exact
    margins.
  - B_n(1/2)≥E_n; I_h, R_h, I_w, R_w derivations; A_h, B_h, A_w, B_w recomputed exactly from F_h, F_w at
    n=320; the (11/100) comparison.
  - e, f, g (near and wide); the maximiser on the line (sympy); 8867/100000; 34161²<32·8233·4431;
    60987/800000; L_h(1/8)=58203/640000; P(1/2), P(3/5).
  - Annulus floors (F_near 0.0753, F_small 0.0719 at 3/5; F_h(21/40)=0.0487).
  - Outer: 337/384, √33887/192, 674/√33887; G, K, A, 13/500. Far: 1/√2<17/24, anchor exactly 79/2000,
    1013/600.
  - Corner: (1−cos π/4)/2>7/48, 2/125>π⁴/6144, 10451/30000, 49/1250>1/30, (9/25)/√2<4/15.
- `outer_geom.py` [E]: grid check of (ul:outer-geometry) and of the far majorants F_u, Q_u, A_u, C_u
  (all hold), plus min u=1−1/√2>7/24 on ρ≥π/2. It also detects the C3-03 gap.
- `floor_test.py` [E, MEASURED only]: every eligible projection Q_h(J), Q_v(K) computed directly with a
  cancellation-free sine-ratio kernel (validated against the defining sum, including exact
  collisions):
  - n=41, 64, 160: 10 phase samples per radius;
  - n=320: 2 samples per radius;
  - ρ up to 1/2 (finite floors) and up to π/4 (tail floors).
  The minimum projection is 0.46–0.57 in every case, against floors ≤0.10; there is no violation. The
  floors are very conservative. This supports, but does not prove, Lemma (ul:selected-pairs).
- `corner_small.py` [E]: the squared-variable identity d²/ds² f(√2s)=∫∫t²f''''(rt√2s) and
  h_uu=(Ap_AA−p_A)/A³ hold for test functions.
  [MEASURED] A 241² grid argmax for n=2..8 lies exactly at the stated parity-dependent corners.
- `near_deriv.py` (C3-15), `corner_ec.py`/`corner_ec.out` (C3-08; M(256) main part 23.59, so
  M(256)<26 is consistent), `n2_cert.py` (C3-13).
Total CPU ≈ 3 min. No native certifier, build or Git command was run; I did not replay the evidence.

## 5. Passages hiding work ("direct", "standard", "one checks", "immediate", "gives")

- p.48 "endpoint identity … show that summing … gives exactly S_n": missing the σ-sum and the
  factorization (C3-07).
- p.112 "Folding … leaves coefficient 1/N": missing the double count and zero self-pairs (C3-10).
- p.114 "Counting 2s points in at least M/4−1 rows gives": missing the assembly line (C3-10).
- p.118 "The elementary bounds … give I>U_r, A_0<V_r, R<W_r": missing the C>0 grouping (C3-05).
- p.119 "At r=1/2 one can also use": missing the monotonicity of the hypothesis (C3-06).
- p.120 "direct differentiation gives (T+A_4+ρJ_N)'>…" and "The costs decrease": missing the
  derivatives (C3-15).
- p.121 "(uc:relative-comparison) gives (ℓ1,ℓ2,d1,d2)" and p.124 "the wide line … gives": missing the
  coefficient lines and the 1/8 reason (C3-04).
- p.124 "The cases x≤1/2 and x≥1 follow from …": wrong reason (C3-03).
- p.126 "the sufficient bounds" for C_b, C_s, C_l, Γ_b, …: only ℓ and the C_s bracket are illustrated.
  Show at least C_b's four parts (a_0D_a+10/n², G_b, R_b, 𝓜_b → 3/25+9/25+17/50+2/125=209/250, an
  exact sum I checked [D]).
- p.131 "The central estimate gives E_c(h,0)<1/4": wrong displayed bound (C3-08).
- p.127 "Its quotient by u decreases: this is immediate for the nonentropy terms": adequately
  repaired by the companion's following explicit verification (pp.127–128).

Genuinely needed extra prerequisites: none beyond the stated analysis (Taylor with remainder, the
mean-value theorem, convexity and concavity, basic series). Ball/interval arithmetic should get the
one-paragraph statement of C3-12.

## 6. Standard tools and figures

Usable statements with hypotheses are given for: Bernstein positivity/partition of unity; the
trigonometric Bernstein inequality (complete Riesz proof; global real-argument norm stressed,
pp.146–150; rescaled frequencies); the Peano kernel (exact kernel and mass; no mixed derivative);
interval rules (±, ×, |·|, floor/ceil averages, monotone bracketing); log-series tails; layer cake;
rectangle-rule bracketing; concavity endpoint comparison. Lipschitz/mean-value covers are not used
(curvature covers replace them, as in the paper). Missing: Arb ball arithmetic (C3-12).
Recommended figures/examples, in order: the n=2 certificate (C3-13); a circle diagram of the three
selected-pair classes (p.113); phase-diagram additions (C3-14); symbol and constants tables (C3-02);
a trust table (C3-01).

## 7. Prioritized fix list

1. C3-01 trust table and G01-consistent wording (both texts).
2. C3-02 re-entry box and symbol/constants tables.
3. C3-03 corrected reason (both texts).
4. C3-04 coefficient derivations and the 1/8 reason.
5. C3-13 n=2 worked certificate.
6. C3-05, C3-06, C3-07, C3-08, C3-09, C3-10 short derivation lines.
7. C3-12 native-stage paragraph and definitions.
8. C3-14 diagram; C3-15 derivative lines.
9. C3-19/C3-20 trims; C3-16, C3-17, C3-18, C3-21 notes.

## 8. Coverage and limits

Covered: every line of companion localization-unified.tex outside the comparison include; every line
of companion certification-unified.tex; both paper counterparts; G01; small-degree-unification;
compact-return (head and searches); review.md, README.md, BUILD.md, and the brief. I did not audit the
comparison text, Sections 1–3 or the native evidence, and I did not re-read the full compact-return
technical checks. The floor and maximizer computations are measurements; the exact rational checks
reproduce displayed arithmetic only.
