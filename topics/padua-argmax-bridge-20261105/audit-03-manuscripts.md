# Claude audit-03 (manuscripts): the 48-page paper, the 162-page companion and their agreement

Part of the substantive Claude audit of handoff 28; the scientific and evidence
assessment is [audit-03.md](audit-03.md) (candidate, models, rules, disclosures
and executed checks are stated there once). Review reports and scripts:
[audit-03/](audit-03/). Both delivered manuscripts and their recorded PDFs are
left intact; everything below is a proposed change returned to Codex. This
audit does not authorize submission, external communication or merge, and PR
27 stays a draft.

## Verdicts

| Target | Verdict |
|---|---|
| **Journal paper** (Constructive Approximation, 48 pp) | **Major revision.** No correctness defect found at the depth reconstructed (Sections 2–3 line by line; every displayed rational at n=320, 256, 192; 100+ checks). The revision is for presentation, one removable computational dependency, an inaccurate data/code statement, an incomplete trust description and notation |
| **Companion** (162 pp, reader with some university analysis) | **Mathematics sound; pedagogy: accept after revision.** All added derivations were re-derived or recomputed and none changed a constant. Load-bearing steps are still asserted in places, symbols are heavily reused, repeated compressed-plus-expanded text, no figure in pp. 50–110 |
| **Agreement** | **Agrees.** Same five sections and 12 subsections; 13 statements, 90 numbered environments (92 equation numbers) and all 211 original display blocks identical; 113/113 labels with identical numbers in fresh `.aux` files; bibliographies byte-identical (13 entries, correct order); evidence claims and constants agree. Several fixes must be made in both texts together (below) |

## Builds and correspondence (X)

Fresh builds (TeX Live 2023 Debian, pdfTeX 1.40.25, latexmk 4.83, outputs under
the auditor's scratch directory): paper 48 pages, 640141 B, sha256
`08197e7d781fb809fde854c6b520e3fe20ae6dd4b3ee13e19ea8e3bfa1520ce0`;
companion 162 pages, 1153282 B, sha256
`dec7c44c93abfe8fcbd975ef9a0475a967dda2d25c87f64d628675b28769aed3`. The recorded
builds (TeX Live 2025: 640116 B, `07db8635…`; 1153227 B, `2ec6b072…`) are not
byte-identical, as the build records say they need not be. Logs: 0 undefined
references or citations, 0 overfull boxes, no font substitutions, all fonts
embedded Type 1. `check_correspondence.py` passes (read-only); `--artifacts` could
not run because `local-output/` is absent here, so preservation of the recorded
PDFs was **not** re-verified. Source freezes hold: paper tree `c6e195f`, paper
prose `177be83`, companion TeX and bibliography `ac94504`. The evidence index
passes (396 entries, 32,414 B). Printed-constant check (float64, MEASURED):
kappa=0.919710118388, b=1.225522125742, c=1.846160310424; the remainder is
far below 1/N and R·N²/log N stays in [-0.043, 0.174] for n=10..401.
A page index for all 113 labels is in [audit-03/page-index.md](audit-03/page-index.md).

## Coverage

**Paper** (every section and subsection read fully; per-unit table in
[p-paper.md](audit-03/p-paper.md) section 6):

| Unit (pages) | Verdict | Main issues |
|---|---|---|
| Front matter, abstract, keywords (1) | accurate except one omission | P-02, P-14, placeholders |
| 1 Introduction (1–4) | clear problem and theorems; weak contribution and literature balance | P-06, P-07, P-11; X-05, X-07 |
| 2 Normalization (4–5) | correct, self-contained | weight notation (P-05) |
| 3.1–3.3 corner expansion (6–12) | correct; reconstructed and confirmed numerically | compressed kappa-limit sketch and endpoint claims (H review); P-11 |
| 4 preamble and geometry (13–14) | correct | P-04 (no roadmap), P-05 |
| 4.1 completed model, Lemmas 4.1–4.4 (14–20) | correct but compressed; model definition unmotivated | P-03, P-05, P-10 |
| 4.2 Proposition 4.5 and proof (21–33) | structure verified, consequences verified numerically; the individual charges of the 11-page proof were **not** re-derived by the paper referee | P-04, P-10b; the companion readers (C2A, C2B) re-derived the companion's expansions |
| 4.3 Lemma 4.6 (34–36) | correct; compressed | P-10a, C3-02 |
| 4.4 near exclusion, 4.5 outer and far, 4.6 corners and proof of Theorem 1.1 (36–41) | correct | P-04, **P-09/C3-03** (wrong stated reason), P-12 |
| 5 preamble, 5.1 small degrees, 5.2 phase certificate (42–46) | correct and well explained | P-08 |
| 5.3 Evidence, Declarations (46–47) | inaccurate or process-language | **P-01, P-08, C3-01, G-1** |
| References (47–48) | 13 items, correct order | X-01..X-04, X-05, P-12, P-16 |

**Companion** (every line of `main.tex` and the six section files read by
one of four readers; pages from the fresh build):

| Reader | Range (companion pages) | Verdict |
|---|---|---|
| C1 | `main.tex`, introduction, preliminaries, corner section (2–46) | mathematics sound; two MAJOR clarity items |
| C2A | `comparison-unified.tex` lines 1–2050 (50–81) | sound; two MAJOR clarity gaps |
| C2B | `comparison-unified.tex` lines 2001–4037 (79–110) | sound; four MAJOR pedagogical items |
| C3 | localization material around the comparison (46–50, 111–133) and Section 5 (133–161) | sound; three MAJOR items |

## Findings: journal paper

Full detail, locations and rewrites are in [p-paper.md](audit-03/p-paper.md)
and the other reports. IDs are the reviewers' own and are unique.

### MAJOR

- **P-01 data/code availability is inaccurate** (`main.tex` lines 85–93; Section
  5.3, p. 46). It says the repository contains the essential certificate
  records; for 41..319 only degrees 199 and 238 are committed. The 560
  essential proofs sit in a 36 MB archive whose custody is unverified
  (`cold-storage.json` lists 0 delivered entries), and "repository",
  "production machine" and "companion reproducibility notes" are not
  identified or citable. Fix: deposit certificates, checkers and the engine
  with a DOI; draft wording is in the report. (Related: E-10, G-8.)
- **P-02 the abstract never says "computer-assisted"** and omits the kappa
  enclosure dependency of the n>=320 part. Rewritten abstract in the report.
- **P-03 PD-T271 can be removed** (also I26, S, G-I2). The paper's own kappa
  series cut at K=3 gives 0.91720 < kappa < 0.92151 and C_* < 1.84802 from
  elementary bounds, which implies the only inequalities consumed
  (kappa > 9/10, hence j > 23/250, and C_* < 1.8516, hence C_infinity < 9/4).
  About ten lines replace the K=64, 320-bit Arb input (Section 4.1 lines
  443–449). The analytic part of Theorem 1.1 then has no computational
  dependency. Delete `kappa < 23/25` and the H0 upper bound (no consumer; the
  former has margin only 2.9e-4).
- **P-04 Section 4 runs 29 of 48 pages without visible architecture.** Its six
  regional results are unnumbered displays; Lemmas 4.1–4.4, Propositions 3.2
  and 4.5 and Figure 1 are never cited by number. Fix: number the regional
  results as Propositions 4.7–4.12, add the supplied roadmap table and a
  phase-diamond figure; optionally move the Proposition 4.5 charges to an
  appendix. (Superseded in part by the onset-512 restructuring below.)
- **P-05 notation collides, often within Section 4** (a=2/pi vs a=c_e c_d;
  d_0 and q_0 each carry two values; H=1+L vs H(w); L=log n vs L the mesh;
  E_n and B_n each have two meanings; r radius vs index; weights written three
  ways). Master register: [audit-03/n-notation.md](audit-03/n-notation.md).
- **P-06 the introduction undersells Theorem 1.2:** no values for b=1.2255,
  c=1.8462 and kappa; the earlier numerical fits are not mentioned; the
  O(log^2 n) attribution is not specific; it overstates the dependency (the
  Lambda_n asymptotics need only the analytic n>=320 part together with
  Theorem 1.2).
- **P-08 Section 5.3 uses project-process language** ("primary/fresh pairs",
  "essential proofs", "distinct review", "selective retention") and has no
  formal statement of what the computation proves and no account of how the
  vertex bounds W_z and L_c are obtained. Fix: a formal computer-assisted
  Proposition 5.2, an affirmative Section 5.3 and a statistics table. This
  merges with **C3-01** (complete trust boundary, both texts) and **G-1**
  (evaluator theorems D23/C02/C06/N5 and D06/C11 as premises).
- **P-09 / C3-03 a stated reason in the proof of the outer-geometry case is
  wrong** (`ul:outer-geometry`, p. 38, lines 364–366; companion p. 124). "x>=1
  follows from u>=11/48" yields only 0.970 < 1 while sin x reaches 1. The
  inequality is true: with u >= (1-cos x)/2 the minimum slack is 0.130 (the
  full two-case argument is in E13 lines 67–74). The reviewers differ on
  severity (P: MINOR; C3: MAJOR); I classify it **MAJOR** because it is a
  wrong reason in a proof, with a one-line repair, to be made in both texts.
- **X-05 attribution** (introduction lines 140–146, both texts). Kuznetsova
  1995 (Ukr. Math. J. 47, 259–266, DOI 10.1007/BF01056716) and Pimenova 1979
  (Dokl. 249, 52–54) are the source of the leading term in the published
  (4/pi^2)log^2 n + O(log n) result and are not cited. One sentence plus two
  bibliography entries in both trees (and update the checker's frozen-bib
  baseline). It also strengthens the motivation for Theorem 1.1.

### MINOR / EDITORIAL (selected)

- References: X-01 (ref [2] prints no arXiv ID), X-02 (ref [6] URL `~`
  rendering and "No DOI."), X-03 (ref [11] URL and DOI), X-04 (stray
  "Published online"), P-12 (cite Arb/FLINT, MPFR, GMP, Bernstein's
  inequality), X-08 (cite [3, Prop 2.2] at (91)–(92)), X-06 (mention the
  earlier empirical lower-order fits after checking locators), X-07 ([6]
  conjectured the location and size; optionally "confirming a conjecture of
  [6]" in the abstract).
- Compression: P-10 (Lemma 4.6 class 1 uses an undefined "effective angle";
  the "direct subtraction" telescope; the circle rearrangement in Lemma 4.2;
  Lemma 4.3's forward dependency on Proposition 4.5).
- Process words: P-11 (about 20 audit-history phrases with exact locations
  and rewrites; four repeated analytic/computational disclaimers).
- Disclosures: P-13 (the AI disclosure omits Claude Sonnet 5.5, which
  orchestrated audit-02 and this audit), P-14 (title says "maximizers of the
  ... constant" but means the Lebesgue function; section titles "One ..."
  reflect consolidation history; add MSC 65G20), P-15 (misaligned rules in
  table (68), p. 30; Figure 1 unreferenced), P-16 (check for a DRNA DOI and a
  published version of the arXiv preprint), P-17, P-18.
- Placeholders (separate from substantive premises): the "Development draft"
  line; the AI-declaration and data-statement "remain to be completed"
  sentences; Section 5.3 line 264; ORCID placement; funding text copied from
  another paper (AC to confirm); inlining the inputs for submission; missing
  spaces in README/BUILD/CONSOLIDATION. No internal IDs appear in the paper
  text.
- Layout: X-13 (number of eq. (54) falls onto its own line, p. 22), X-14,
  X-12 (companion p. 144 about 45% blank).
- Proof presentation (P report): display the organizing identity
  lambda_n - Lambda_c = (S_n - S_n(0)) - Delta_JK at the start of Section 4;
  motivate M_infinity as a row Riemann sum before defining it; say how
  conservative the constants are and that the 320 onset comes from the outer
  gate (0.069 at n=320, negative at 300).

## Findings: companion

Details with line numbers are in the four reports. Because the companion keeps
the paper's numbered blocks verbatim, most fixes are unnumbered additions
and cost no correspondence risk.

### MAJOR (clarity; the theorems stay supported)

- **C1-01** the exact corner formula (8), pp. 20–22 (`corner-unified.tex`
  77–160), cannot be reconstructed: the kernel evaluation
  K_n((-1,-1),B)=D_n(pi-theta_j, pi-phi_k) is only in words, D_n=G_n+cos(nu)
  is never linked to (7), and the numerator hint cites sin(m theta_j) and
  sin(n phi_k), which do not do the work. The working step is product-to-sum
  plus cos(n theta_j)=(-1)^j, cos(m theta_j)=(-1)^j cos theta_j,
  cos(m phi_k)=(-1)^k, cos(n phi_k)=(-1)^k cos phi_k, together with the fact
  that (-1)^j is constant along an odd-checkerboard row. Exact replacement text
  is in the report. The paper's corner section (lines 25–46) has the same two
  gaps, so the fix is coordinated.
- **C1-02, C2A-10, C2B-M4, C3-02** symbol overload and no re-entry summary after
  the 60-page comparison; many letters carry 2–6 meanings within a few pages.
  Resolved by the master register and per-section notation tables
  ([n-notation.md](audit-03/n-notation.md)).
- **C2A-01** the completed model M_infinity appears without an account of where
  it comes from (pp. 60–63; line 895 says "This proves the coefficient" though
  the integral differs from b_full by 2D_0; the link first appears at line 1763
  and the paper, line 298, never states it). One sentence, checked numerically
  (difference at most 3e-7 for n from 10^3 to 10^5), plus a corrected line 895
  and paper line 298.
- **C2A-02** the row identity at line 1633 (p. 73), on which every later
  estimate rests, is never derived. A checked six-line derivation is in the
  report. **C2B-M1** (lines 2572, 3328–3341) "partial fractions show
  sum|f_j| = l_r" and "the signed-row sum gives e_r" are asserted; about 15
  lines needed, with a one-clause addition at paper line 931.
- **C2B-M2** the half-line residual increment (p. 99, lines 3276–3290) cannot be
  rebuilt because the text never says the residual is 2w·Sum±E(h_*,v,theta±).
  **C2B-M3** seven allowances have no derivation (M_A^phi and V_A^phi, N_s used
  before it is defined, the central cancellation supremum, the relative hole
  envelopes, J_cen, the omitted-collision charge, the cutoff references); all
  verified numerically.
- **C3-01** the Section 5.3 trust boundary (pp. 158–161) is incomplete against
  G01: no PD-T271 enclosure (which also feeds the 192 and 256 branches used
  inside 41..319), no collision formulas, exact-rational checker with its
  runtime, small-degree C++/GMP checker with its compiler, and no statement
  that the unsampled native premises were not replayed; the introduction (p. 6)
  wrongly says Section 5 describes the enclosure; "Companion reproducibility
  notes" (p. 160) points nowhere. Fix: a trust table in Section 5.3 of both
  texts. **C3-03** see P-09.

### MINOR / NOTE / EDITORIAL (selected)

- C1: C1-03 (verbatim original text interleaved with explanations causes
  repetition and a lost antecedent, corner:306), C1-04 (hidden trigonometric
  steps, corner:265, 274, 300), C1-05/06 (the H_k expansion is used on p. 27
  before it is proved on p. 35; psi(1/2), psi(m) asserted before derived; psi
  never named the digamma function; the termwise-differentiation theorem is
  not stated), C1-07 (a misleading sentence at intro:392: the expansion is
  parity-free in the midpoint scale N because N absorbs the logarithmic
  reciprocal term), C1-08 (Kronecker delta used before defined; trapezoidal
  rule never defined; heading "surviving reflections" unclear), C1-09, C1-10
  (add a hand-checkable n=2 corner value: terms 3/2, 1, 1, 1/2 giving
  Lambda_c(2)=3, and a table of Lambda_c(n) against the four-term expansion:
  differences 0.091 at n=2, 0.0037 at n=10, -3e-6 at n=200), C1-11 (figures: the
  index array and checkerboard, the diamond-to-square map, the corner row with
  folding, the square-reference triangle), C1-12.
- C2A: C2A-03 (broken sentence "Therefore The summand identity is", p. 65, lines
  1046–1069), C2A-04..08 (sine comparison needs h'(0)=pi/2-3/2>0; N_s undefined
  and the bound |N_s|<=8 is crude, the truth is <=2; I(C,D,e) used outside
  0<e<pi without the reflection reduction; sum|cot(v_r/2)|<=4mH_n/pi holds only
  over the rows outside A_6, diverging over all rows), C2A-07 (about fifteen
  elementary bounds without their one-line reason, each with a concrete fix),
  C2A-09 (systemic duplicated compressed-plus-expanded statements), C2A-11 (pp.
  50–110 contain no figure; three proposed with verified numbers).
- C2B: m1 ("<=" for "="), m2 (u<pi/4 needs nu<=n/2+1/pi), m3 (the tail-derivative
  bound fails at j=2 and holds for j>=3; it is used only for j>n/2), m4 (160 is
  a round choice, not an arithmetic threshold), m5..m11, m12 (duplicates at
  L2250/2267, 2386/2393, 2756/2766, 3248/3252, 3662/3757), e1 (|C|cot e),
  e3, e4, and a recommended ledger table at the start of 4.2, a worked n=320
  column and three figures.
- C3: C3-04 (the coefficient tuples in 4.4 are not derived; the split at
  rho=1/8 is needed because d_1=1911/800 needs the (21/500)rho term of U_N: 2.388887
  with it, 2.387602 without), C3-05..C3-11, C3-13 (add a tiny worked
  certificate; an exact n=2 one: four quadrant leaves, Lambda_c(2)=3), C3-12
  (define Arb ball arithmetic, witness, primary/fresh, account/exit,
  collector), C3-14 (phase diagram accurate but a misplaced rho label and
  incomplete shading description), C3-15..C3-21.
- Overall pacing: the added derivations are locally careful; the companion
  fails the depth standard mainly where the original compressed sentence and its
  expansion are both kept (systemic) and where a routine bound hides its
  reason. The four readers recommend, in this order: fix the MAJORs above, merge
  the duplicates, add the ledger tables, the n=320 worked columns and the
  figures, then the MINOR items.

## Literature, positioning and applications (X)

Qualified, from bounded searches; no primary full text was reopened because
the proxy blocked arxiv.org and the university host, and every source-content
judgment is [I] (repository records) or [E] (search metadata). The defensible
"new" claims:
(a) the exact equality set for every n>=2 (proving the 2008 poster
conjecture [6] in sharpened two-nonnode-corner form); (b) the exact b and
c=c_1^2+kappa, the -1/N term on the half-integer scale and the O(log N/N^2)
remainder; (c) at method level, cancellation-retaining strict-exclusion
certificates, not mesh certification as such. The published leading growth is
O(log^2 n) (Bos–Caliari–De Marchi–Vianello–Xu 2006) and the (4/pi^2)log^2 n +
O(log n) constant (Kolomoitsev–Lomako 2021, through Kuznetsova 1995 and
Pimenova 1979, whose lower bound is evaluated at a non-corner point). Earlier
numerical fits and the corner observation (De Marchi 2022 section 3.3(2),
KL numerical section, the 2008 poster) must be cited with locators checked
against AC's copy (X-06). The three application citations ([11] Nystrom and
collocation, [12] Wigner/Husimi reconstruction, [13] discrete orthogonal
polynomials and least squares) are accurate at their actual scope. Keep the
bounded-search qualification (X-18); no exhaustive priority conclusion.

## Cross-cutting items that must be changed in both texts together

1. Section 5.3 trust boundary and the abstract/introduction "computer-assisted"
   statements (P-02, P-08, C3-01, G-1, G-4, G-5).
2. The wrong reason at the outer-geometry case (P-09, C3-03).
3. The corner-formula derivation (C1-01), the row identity clause (C2B-M1), the
   M_infinity link (C2A-01, paper line 298), and the endpoint identity needing
   the sum over sigma (C3-07), the E_c(h,0)<1/4 source (C3-08).
4. Any rename touching numbered display blocks (P-05, H-C06). The repository's
   `companion-paper/check_correspondence.py` enforces the 1:1 structural match,
   so every restructuring must be mirrored there unless AC relaxes that rule
   (the master register says how it changes).
5. The two bibliography additions and reference formatting fixes (the checker's
   frozen-bib baseline must be updated in the same commit).

## Proof-architecture options (AC's question)

[s-streamline.md](audit-03/s-streamline.md) maps the dependency graph and
evaluates five architectures. With the onset kept at 320 the paper is already
near its minimum (about 1.5 pp more, to 46–47 pp). **AC decided on onset 512**
(about 43 pp): near and wide regions become one quadratic bound on rho<=1, far-192
and the outer region become one closed-form absolute gate (G(192,pi/2)=0.0990>3/100;
G(512,1)=0.534), the annulus and its seams, the radius-dependent floors and the
outer-geometry block drop out, and the near-region margin rises from about
5e-5 to about 9e-3. Cost: certificates for degrees 320..510 on the frozen
engine (about 1 CPU-hour, worst case about 2.4, about 25 MB cold evidence), new
short scalar lemmas (monotone steps for the radius-one polynomial and the
gates) and a re-do of the structural reviews. The rejected options and their
reasons (absolute-only tail at onset about 6000: about 115 CPU-hours, 0.7 GB, two
engine changes, about 37 pp; effective corner expansion; replacing the 2..40
Bernstein scheme; dropping far-192 or corner-256) are in the report. These
numbers are Arb enclosures at base degrees and projections, not proofs or
measured costs. Material that must stay for referees: the 41/64/160 floor
formulas, the far-leaf guard, the corner lemma with the pi/4 square and 1/30,
the corner-witness geometry, both norm witnesses with 784/663, the pi bracket,
the 2..40 / 41.. split and the evidence boundary.

## Prioritized revision plan

1. Decide and carry out the onset-512 restructuring (it changes Sections 4–5
   and the numbers everywhere; do the notation renames and the shared
   items at the same time, to review once).
2. P-03: remove PD-T271 (rational enclosure); delete dead statements.
3. Trust and data: P-01, P-08, C3-01, G-1 (one trust table, formal
   computer-assisted proposition, deposit with DOI).
4. P-02, P-06, X-05 (abstract, introduction, attribution, references).
5. Notation: master register, then the section notation tables.
6. Companion clarity: C1-01, C2A-01/02, C2B-M1/M2/M3, merge the duplicated
   sentences (C1-03, C2A-09, C2B-m12), add the ledger tables, worked
   n=2 and n=320 examples and the figures.
7. P-04 (numbering, roadmap, phase-diamond figure), P-09/C3-03, P-10, P-11.
8. Remaining MINOR and EDITORIAL items, placeholders and final-ID leftovers.

After the changes: a focused re-check of both manuscripts by a distinct agent,
a fresh build and the correspondence check. A new substantive audit is needed
for the changed analytic part (onset 512 gates and the new certificates),
not for wording.

## Own presentation ideas

From I and the readers: a proof-map figure with the trust inputs marked; a
rho-region figure with the proved gaps 1/20000, 3/1000, 99/2500, 13/500 and the
corner loss (A^2+B^2)/30 (the companion has a phase diagram; the journal paper
only the node figure); a before/after trust table; one worked FAR leaf and the
corner witness from the real n=199 certificate (M=24, L_c=19.6977..., margin
1.48e-3); a supplementary per-degree table for the certificates; stating
Theorem 1.1 for every n>=1 (lambda_1 = max{1, |y|+(1-x)/2} obeys the
odd-degree rule; n=0 is a genuine exception), which consolidation-audit lines
290–301 suggested and was never adopted.

2026-11-08 · orchestrator `claude-sonnet-5-5`; review work by Claude Opus 5.5
subagents (instructed xhigh) · rules read at be9a831, unchanged at f366535.
