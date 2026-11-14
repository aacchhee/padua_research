# P — Independent referee report: journal paper (Constructive Approximation)

**Auditor:** Claude Opus 5.5 (xhigh), subagent of the handoff-28 substantive Claude audit;
independent referee, read-only, no Git or repository writes. Branch
`codex/padua-argmax-bridge-20261105`, head `f366535e1fa4ede566cb83bdc554220c12b307cf`.
Rules read at that head: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md`,
`claude-audit-brief-20261108.md` (scope: section 2, and section 4 as it concerns the paper).

**Inputs.** Read in full first, as a standalone submission: `paper/main.tex`, all six sections,
`references.bib`, README, BUILD, CONSOLIDATION, template/README, application-context,
small-degree-unification. Then G01, E14, E12, E15, E13 (one step), PD-T271, `compact-return.md`,
`cold-storage.json`, positioning, literature refresh, cited companion passages; last, the prior
reviews (consolidation, affirmative-style, section 5; `review.md` skimmed, companion scope).

**PDF.** Agent X's fresh build `audit3/build/paper/main.pdf`: 48 pages, SHA-256
`08197e7d…0ce0` (bytes differ from the recorded `07db8635…`, as expected; same page count).
No errors, warnings, undefined or multiply defined labels, or overfull boxes; 55 underfull hbox
diagnostics. X's index: 113 labels, 92 numbered equations, 12 labelled statements plus one
remark, no paper/companion number mismatches.

**Evidence labels.** **[D]** verified by my own reading and reconstruction. **[E]** computation I
executed in `audit3/p-code/` (MEASURED; see `p-code/README.md`; about 2.4 CPU-min in total).
**[I]** inference or editorial judgment. Each finding is also tagged *correctness/accuracy* or
*editorial*.

## 1. Verdicts

**Mathematics as presented: no correctness defect found within my reconstruction depth.**
- **Sections 2–3** (corner expansion) [D][E]: reconstructed line by line; correct.
- **Section 4:** I reconstructed the main chain (reflection identities, regional assembly, corner
  descent, outer gate) and checked every displayed rational constant [E]. I did not re-derive each
  charge in the 11-page proof of Proposition 4.5, the band formula, or every derivative bound of
  Lemma 4.2; for those I verified the consequences numerically, with wide margins [E].
- **One proof-text gap:** the justification in (ul:outer-geometry) is insufficient as written,
  though the claim is true (P-09).
- **Section 5:** the implications are correct [D].
- **Self-containedness:** the paper depends on repository records in two places, the κ evaluation
  (P-03) and the certificate data (P-01).

**Editorial verdict for Constructive Approximation: MAJOR REVISION (presentation, not mathematics).**
Strengths: both results clearly stated; Sections 2, 3 and 5 well organized and checkable.
Weaknesses: Section 4 (29 of 48 pages) has no visible architecture (P-04) and colliding notation
(P-05); the abstract omits "computer-assisted" (P-02); the data statement is inaccurate (P-01).
Cheap win: six series terms make the n ≥ 320 theorem fully analytic (P-03).

## 2. Prioritized findings

### P-01 MAJOR — correctness/accuracy of declarations [D]
**Location:** Data and code availability (main.tex l.85–93, PDF p.46); §5.3 l.255–265 (p.46).

**Problem.** "The current repository contains the manuscript source, pinned checker code and
essential certificate records" is false for 41 ≤ n ≤ 319.
- Only degrees 199 and 238 have committed certificates (`evidence/compact-return/`).
- All 560 essential phase proofs exist only in a 36,045,486-byte archive in sandbox
  `local-output` and chat attachments. `cold-storage.json` (`compact-actual-return`) records
  external delivery as unverified; the manifest has 0 delivered entries. The archive is absent
  from this audit session.
- The 2–40 certificates are committed (15 + 16 + 8 files), so that part is accurate.
- "The current repository" is never identified (no URL, no DOI). "Production machine",
  "selective-retention policy" and "companion reproducibility notes" (§5.3 l.263) are not
  citable objects.

**Impact.** A referee cannot check the computer-assisted part of Theorem 1.1. Springer's
mandatory data statement requires a location for the data that supports the results.

**Fix.** Before submission, deposit the compact return, both checkers
(`compact_pack/verify_compact.py` and the small-degree checker), the frozen engine source and the
2–40 certificates in a public archive with a DOI (36 MB fits Zenodo). Then state, e.g.: "All
certificates (degrees 2–319 and the control degree 511), the exact-rational checkers and the
certificate-generating engine are archived at [DOI]. The full execution logs of the production
runs are not needed to check the proof and are available from the author." With the essential
proofs public, selective retention of the logs is accurate and sufficient.

### P-02 MAJOR — accuracy of title/abstract [D]
**Location:** abstract, main.tex l.28–41 (p.1).

**Problem.** The abstract never says "computer-assisted", only "rigorous finite certificates".
It presents the n ≥ 320 part as purely "quantitative localization", although that part currently
also uses the certified κ enclosure (uc:coarse-input). Its last sentence ("We describe the
certificate implications, arithmetic dependencies and reproducibility boundary separately…") is
process language.

**Fix.** Proposed abstract (assumes P-03; otherwise add "and a certified enclosure of κ" after
"for n ≥ 320"):
> For Lagrange interpolation of total degree n at the Padua points on the square, we prove that
> the Lebesgue function attains its maximum exactly at the two corners that are not nodes, for
> every n ≥ 2, and that Λ_n = (4/π²)(log N + γ + log(8/π))² + κ − 1/N + O(log N/N²),
> N = n + 1/2, where κ = 0.91971… is an explicit integral. The expansion is derived analytically
> from an exact formula for the corner value. For n ≥ 320 the location of the maximum is proved
> analytically by comparing the Lebesgue function with a periodic majorant and quantifying the
> cancellation lost in the triangle inequality. For 2 ≤ n ≤ 319 the proof is computer-assisted:
> positive-interpolation bounds on closed covers of the square are verified in exact rational
> and outward interval arithmetic.

### P-03 MAJOR — self-containedness of the n ≥ 320 theorem; removable dependency [E][D]
**Location:** §4.1 l.407–449 (p.19–20), especially l.443–449 ("The inherited certificate
evaluates this explicit finite sum through K=64 by outward Arb arithmetic at 320 bits … the
reproducibility record describes the arithmetic receipt"); echoed in intro l.101–106 and §4.6
l.555–558.

**Problem.** The paper's own series (uc:kappa-series) with K = 5 already suffices.
- I recomputed the paper's a_p, b_q, c_k; the K = 64 sum equals the κ integral to 20 digits [E].
- c_0..c_5 ≈ 1.05180, 0.139453, 0.0319855, 0.00785526, 0.00195572, 0.000488442; partial sum
  0.9196920; stated tail bound at K = 5 is 8/(3·7·4^6) < 9.31e-5. Hence κ ∈ [0.919599, 0.919785]
  (interval check [E]).
- With 4d²/π² = 0.926450 this gives 9/10 < κ < 23/25 and C_* < 1.846236 < 1847/1000. The margins
  are 2.9e-4 and 8.4e-4, so ζ(3..13) to 6 digits and the exact ζ(2r) suffice. True κ =
  0.9197101184, agreeing with PD-T271.

**Impact.** The n ≥ 320 theorem now rests on a repository receipt. A six-row table of rational
enclosures of c_0..c_5 would make Theorem 1.1 for n ≥ 320 and the Λ_n asymptotics of Theorem 1.2
fully analytic.

**Fix.** Replace l.443–449 by that table (classical ζ(odd) values), and delete the three "separately
certified constant enclosure / trusted computational input" sentences (intro l.103–104, §4.6
l.555–558, abstract). If AC prefers to keep the Arb receipt, cite it with a DOI (P-01).

### P-04 MAJOR — proof architecture and signposting of Section 4 [D][I]
**Location:** §4 (p.13–41).

**Problem.**
- The six regional conclusions are unnumbered displays inside prose: (ul:near-exclusion),
  (ul:annulus), (ul:wide-exclusion), (ul:outer-exclusion), (ul:far192), (ul:corner256).
- Never cited by number (unreferenced-label scan of the sources [D]): Lemmas 4.1–4.4,
  Propositions 3.2 and 4.5, Figure 1, and `ul:wide-polynomial`, `ul:outer-gate`. The proof of
  Theorem 1.1 cites only equation numbers.
- §4.2's four paragraphs ("Pole norms…", "Absolute charges…", "The actual origin", "Relative
  charges…") run 11 pages with no overview of what each proves.

**Impact.** There is no visible proof chain; a referee must reverse-engineer which inequality
feeds which.

**Fix (in order of benefit/cost).**
1. Promote the six regional results to Propositions 4.7–4.12 with explicit hypotheses (degree
   range, ρ-range, corner/noncorner centers) and gap.
2. Open §4 with a roadmap paragraph and this table, noting the ingredients: model (Lemmas
   4.1–4.4), finite comparison (Proposition 4.5), floors (Lemma 4.6).

   | ρ range | centers | gap | from |
   |---|---|---|---|
   | ρ ≤ 1/2 | noncorner | λ_n < Λ_c − 1/20000 | n ≥ 320 |
   | 1/2 ≤ ρ ≤ 3/5 | noncorner | λ_n < Λ_c − 3/1000 | n ≥ 320 |
   | 3/5 ≤ ρ ≤ 1 | all | S_n < Λ_c − 99/2500 | n ≥ 320 |
   | 1 ≤ ρ ≤ π | all | S_n < Λ_c − 13/500 | n ≥ 320 |
   | π/2 ≤ ρ ≤ π | all | S_n < Λ_c − 3/100 | n ≥ 192 (certificates only) |
   | corner charts | 0 ≤ A,B ≤ π/4 | descent (A²+B²)/30 | n ≥ 256 |
3. Add a figure of the phase diamond with these annuli and the corner squares.
4. Cite by number ("By Proposition 4.5 and Lemma 4.6…").
5. Optional: move the charge-table derivations (p.23–33) into an in-paper Appendix A, "Proof of
   Proposition 4.5". No page change, but a ~18-page main-text chain: geometry → model → finite
   comparison (statement) → floors → regions → Theorem 1.1.
6. Split Lemma 4.6's statement into (a) tail floors used for n ≥ 320 and (b) finite floors
   consumed by the certificates.

### P-05 MAJOR — notation collisions [D]
Each symbol below has two or more meanings, often within one section:
- **a:** 2/π (eq:main-constants, §3) vs c_e c_d (§4.1 l.10, all of §4); also a_r, a_j = jπ/n
  (§4 l.14), a_0 = 337/384 (§4.5), a_0 as a band endpoint (Lemma 4.6), [a_0, a_1] (Lemma 5.1).
- **d_0:** γ + 2 log 2 (§3 l.321) vs C_0 b_*/π² (Lemma 4.3). **q_0:** π²/4 − 1 (§3) vs 7/48 (§4.6).
- **H:** 1 + L (§4.1 l.4) vs H(w), H_0 (Lemma 4.2, same subsection); also H_n, H_{rs}, H_h,
  𝓗(L,v), 𝓗_j, 𝓗_m, H_k.
- **L:** log n vs the periodic mesh size in Lemma 4.6's proof ((M,L) = (m,n); "row sum at least
  L𝒯_cA(b)/π"); also L_n (§3), L_c (§5), L_B, L_{jk}, L_h(ρ), L_{n,k}.
- **E_n:** S_n − M_∞ (uc:origin-lower) vs 245931/6050000 − … (Lemma 4.6 proof), both in §4.
- **B_n:** floor B_n(r) (Lemma 4.6) vs pole sum B_n(t) (uc:pole-error).
- **r:** radius bound (Lemma 4.6, ρ ≤ r) vs periodic index r in the same proof's Q_v formula.
- **j:** constant (Lemma 4.3) vs index; also j_*. **c:** expansion constant vs c = 5/4, c = 2
  (band formula) vs §4.5 constants.
- **Endpoint weights:** ε_j, η_k (§2, \epsilon), \varepsilon_j (§3), e_j, f_k (§4); node angles
  θ_j, φ_k become a_j, b_k in §4.

**Fix.** Add a notation table at the head of §4; use one weight notation throughout. Renames:
a = c_e c_d → **ā**; H = 1 + L → **ℓ_n**; mesh pair (M,L) → **(M,M')**; floor B_n(r) →
**β_n(r)**; Lemma 4.6's E_n → **e_n**; §3's d_0, q_0 → local tildes.

### P-06 MAJOR (editorial) — introduction: contribution balance and literature context [D][I]
**Location:** §1 (p.1–4).

**Problem.** Theorem 1.2's value gets two sentences (l.140–146), although the project's own
positioning record says the asymptotic strand had standalone paper value. A CA referee from the
Padua community will expect:
1. **Prior numerical fits** (`literature-refresh-20261107.md` l.36, 66–74): De Marchi's empirical
   squared-log fit with offset 1.1 (SIMAI 2004/2005), and the numerical model h(m,n) with
   1.2 log(m+1) + 1.5 in the journal version of Kolomoitsev–Lomako. The exact b = 1.2255221…,
   c = 1.8461603… explain those fits.
2. **Explicit attribution** of the O(log² n) bound (l.15–21 cites five papers as a group).
3. **Numerical values** of b, c, κ.

**Fix.** Add one paragraph with the values and the fit comparison (cited as numerical
observations with their version caveat); optionally a 4-row table of n, Λ_n and residual
(measured [E]: 2.25e-5 at n = 64, −1.15e-6 at 512, −4.2e-8 at 4096). State that Theorem 1.2 for
Λ_n needs Theorem 1.1 only for n ≥ 320 (P-07). Optional: "[1] proves an O(n²) bound for
Morrow–Patterson points and leaves corner attainment open", which names the gap Theorem 1.1
closes for Padua points.

### P-07 MINOR — accuracy of a dependency statement [D]
**Location:** intro l.133 and l.136–138 ("Consequently (5) also holds for Λ_n"; "Its global
version uses Theorem 1.1, with the computer-assisted dependencies just described").

**Problem.** As an n → ∞ statement this needs only the n ≥ 320 part; the computer-assisted range
matters only for a constant uniform in n ≥ 2.

**Fix.** "By Theorem 1.1 (for n ≥ 320 its analytic part suffices), (5) holds for Λ_n; with the
finite range the same constant C works for all n ≥ 2."

### P-08 MAJOR — §5.3 is in project-process language; no formal statement of the computational step [D][I]
**Location:** §5 (p.42–46), especially §5.3 l.246–265 and §5.1 l.98–100.

**Problem.** Terms undefined for a journal reader: "primary/fresh pairs", "essential proofs",
"proof/account/source links", "with distinct review", "selective-retention policy", "production
machine", "accompanying execution record identifies which degrees were newly rerun". No formal
statement says what the computation establishes, and the paper does not say how the vertex
bounds W_z and L_c are obtained (outward Arb evaluation of (ul:primitive) and (cu:positive)).

**Fix.**
1. Add "Proposition 5.2 (computer-assisted). For 2 ≤ n ≤ 40 [resp. 41 ≤ n ≤ 319] the certificate
   in [DOI] satisfies the predicates of §5.1 [§5.2]. Assuming correct outward rounding in
   Arb/FLINT, MPFR and GMP and the checker of [DOI], Theorem 1.1 holds for 2 ≤ n ≤ 319."
2. Rewrite §5.3 affirmatively: each degree was certified twice by independent runs of one
   released engine; every certificate was re-verified by an exact-rational checker; vertex
   enclosures were independently recomputed for two random degrees (199, 238); list the trusted
   base.
3. Add a small statistics table (degree range, norm method, analytic leaves, tree size, CPU),
   about 1/3 page, from `compact-return.md` and `small-degree-unification.md`.
4. Drop who reran what and when (l.99–100); it belongs in the deposit's README.

### P-09 MINOR — correctness of a proof step (claim true) [D][E]
**Location:** §4.5 (ul:outer-geometry), localization l.364–366 (p.38); same text in the
companion, localization l.1285–1286.

**Problem.** "The cases x ≤ 1/2 and x ≥ 1 follow from sin(1/2) < p_0 and u ≥ 11/48." For x ≥ 1,
u ≥ 11/48 gives only v ≥ 41/384, so p_0 + η√v ≥ 0.970, while sin x reaches 1 on [1.33, 1.81]:
the literal route fails. The claim holds (minimum slack of max(p,q) ≤ p_0 + η√v is 0.0050 on a
1201² grid [E]). E13 (`theory/E13-joint-radius-outer.md` l.67–74) has the full argument: if
u ≤ 1/4 then cos x ≥ 1/2, so p ≤ √3/2 < 93/100; if u ≥ 1/4 then v ≥ 49/384 and the bound
exceeds 1.

**Fix.** Insert those two lines in both manuscripts (coordinated remedy).

### P-10 MINOR — steps a specialist cannot check without the companion [D]
- **(a) Lemma 4.6 proof, class 1** (l.147–152, p.35) uses undefined "effective angle w",
  "periodic phase", "physical phase". Fix: import companion l.505–523 (about five lines): ξ, ζ;
  w = ((l+q)π ± ξ)/L; M(w−b) = qπ + ((M−L)/L)(l+q)π ± (M/L)ξ; the 24/41 bound.
- **(b) (uc:telescope) "Direct subtraction…"** (l.670–681, p.23). Fix: add the reconstruction
  (verified [D]): L + log(π/m) = log π − ε_n, so the normalized singular part of F_s at z = h(k+τ)
  is exactly Z_n/(k+τ) + B_0 log(k+τ)/(k+τ) with Z_n = D_0 − B_0 ε_n, and h_j, g_j telescope its
  cell primitives between j = 2 and j = n.
- **(c) H(w) ≤ H_0** (Lemma 4.2 proof l.218–221) is a rearrangement inequality on the circle for
  symmetric-decreasing W, g. Fix: cite Hardy–Littlewood–Pólya Thm 378 or Baernstein,
  *Symmetrization in Analysis*, or add one sentence to the arc argument.
- **(d) Lemma 4.3's proof uses (uc:origin-identity)**, which needs Proposition 4.5 at φ = 0
  (proved later) and Theorem 1.2. Fix: one sentence stating that (uc:global-error) at the origin
  uses none of Lemma 4.3's bounds, so the order is not circular. The consolidation audit says so;
  the paper should too.

### P-11 EDITORIAL — residual defensive/audit register [D]
The explicit "not X but Y" contrasts are gone, but the audit-history register remains, shown by
many uses of "retain/retained/kept/intact/included once" (17), "actual" (30) and "legal radius".
Suggested rewrites:
- **Intro l.145–146** "The corner calculation is independent of the global maximizer argument."
  → delete. With intro l.136, the end of §3 (l.453–455) and the end of §4 (l.556–558) the point
  is made four times; keep it once in the intro.
- **Intro l.163–164** "our finite proof also needs strict exclusion and equality classification"
  → "Our certificates add strict exclusion near the maximizing corners, which identifies the
  equality set."
- **Intro l.173** "The onset 320 is sufficient for the global location argument." → delete
  (orphan). **Abstract l.39–41** → see P-02.
- **§3 l.7** "We retain that displacement throughout the proof." → delete. **§3 l.303** "Two
  summable endpoint sequences must still be retained." → "We also need two summable sequences."
  **§3 l.416–417** "The calculation keeps the last row as well as both outer endpoint
  corrections." → delete.
- **§4 l.8–9** "We retain this loss until it has paid for the possible increase of the majorant
  near the origin." → "This loss compensates the growth of the majorant near the origin."
- **§4 l.34** "All ties are retained." → "A point with ties belongs to every chart it satisfies."
- **§4 l.64** "Each mesh retains its coordinate." and **§4.1 l.15** "The two mesh directions
  retain their original roles throughout." → one sentence: "Throughout, x refers to the n-mesh
  and y to the m-mesh."
- **Delete outright:** §4.1 l.680 ("This derivation preserves m=n+1…"), l.1240–1241 ("with both
  meshes and their finite collisions intact"), l.1348 ("including every root switch"), §4.4
  l.348–349 ("This uses the middle floor on its two stated guards…"), Lemma 4.6 preamble
  l.72–74 ("…its degree-511 control uses the same third floor tier"; process).
- **§4.2 l.1096–1097** "the two columns retain their distinct finite-row denominators" → "the
  columns differ in their finite-row denominators". **l.1259** "…with its scalar logarithm
  included once" → "It remains to prove the last row."
- **l.112** "At fixed legal radius" → "For each admissible radius". **§5 l.184** "Their overlap
  retains the seam ρ=1/2." → "The two proxies overlap on ρ = 1/2." **§5 l.265** "This evidence
  boundary is part of the theorem's computational scope." → the P-08 statement.
- **"Actual":** keep it only where it contrasts with the model ("actual origin" vs model origin);
  elsewhere use "corner chart" or "noncorner center".

### P-12 MINOR — citations of tools [D]
- Cite Arb/FLINT (Johansson 2017), MPFR (Fousse et al. 2007) and GMP, which form the trusted base.
- Cite Bernstein's inequality for bounded functions of exponential type (§4.6 l.472–473, §5.2
  l.131–133). "Trigonometric Bernstein inequalities" is imprecise, since the frequencies p/n are
  non-integer.
- Optional: cite DLMF for ψ(1/2), ψ'(1/2) and the cotangent partial fraction, replacing §3
  l.255–266 (the cos(zs)-series derivation, about 6 lines).

### P-13 MINOR — AI disclosure accuracy [D]
**Location:** main.tex l.73–83. The disclosure lists Claude Opus 5.5, GPT-6 Astra and GPT-6.1
Sol, but Claude Sonnet 5.5 also orchestrated audit-02 in this topic (LOG l.1595). **Fix:**
"Anthropic Claude (Opus 5.5, Sonnet 5.5) and OpenAI (GPT-6 Astra, GPT-6.1 Sol)", after checking
predecessor topics for other models; replace "in the Padua project" by "in this work".

### P-14 MINOR — title, section titles, MSC
- **Title:** "exact maximizers of the … Lebesgue constant" mixes up the constant (a number) and
  the Lebesgue function. Suggest "Sharp asymptotics of the Padua Lebesgue constant and the
  maximum of the Lebesgue function" or "The Padua Lebesgue constant: sharp asymptotics and exact
  location of the maximum".
- **Section titles:** "One finite-row telescope", "One selected-pair argument…", "One polynomial
  certificate…" reflect the consolidation history. Suggest "Finite-degree comparison with the
  model", "Lower bounds for the reflection loss", "Bernstein certificates for 2 ≤ n ≤ 40",
  "Phase certificates for 41 ≤ n ≤ 319".
- **MSC:** add 65G20 (algorithms with automatic result verification).

### P-15 MINOR — tables and figures [D]
Table (68) on p.30 has vertical rules misaligned against its \multicolumn rows; the V_B table
(p.27), displacement table (p.31) and P_s table (p.32) also use \begin{array}{c|…}. Use
booktabs-style tables without vertical rules. Figure 1 is never referenced; cite it at l.86 or
l.97.

### P-16 MINOR — bibliography metadata [I]
LaguardiaRusso2022 has only an emis.de URL: check for and add the DRNA DOI.
BialasCiezDeMarchiSuder2026 (arXiv 2605.23299): check for a published version. The 13-item
alphabetical order is correct, including Sommariva < Vianello among the Caliari entries [D].

### P-17 NOTE — applications paragraph [D]
Accurate at the recorded reading scope (`application-context.md`). Strengthen the motivation:
the reconstruction error bound in [12, Eq. (5)] is explicitly proportional to the Lebesgue
constant; say so in one clause. [13] is a self-citation; acceptable, but its link is to Padua
sampling rather than to the interpolation operator.

### P-18 NOTE — records coordination (outside the paper text) [D]
G01 step 1 cites the historical PD-T routes for 2..16, while the paper cites the unified fresh
2–16 witnesses of `small-degree-unification.md`. Both are valid; add a one-line pointer in G01
so the paper's stated evidence has a canonical home.

## 3. Placeholders and final-ID/cosmetic leftovers (separate from substantive premises)
No internal IDs (PD-T, IDEA, LIT, Syvert, E/G records) appear in the paper text [D].
To fix at publication preparation:
- **Draft text to remove:** main.tex l.45–47 ("Development draft…", p.1); AI declaration l.82–83
  ("Final human review … remain to be completed"); data statement l.92–93 and §5.3 l.264
  ("durable public release … remain to be arranged" → DOI, P-01).
- **ORCID** sits inside "Author contributions" (l.71); move it to the author metadata/form.
- **Funding:** taken from Paper F under AC's authorization (README l.75–77); AC should confirm it
  applies to this work.
- **Submission package:** inline the six \input files into one TeX file (template/README
  l.58–61).
- **Repository records** (not the paper): README, BUILD and CONSOLIDATION have many missing spaces
  ("finite41–63", "degrees2–40", "46pages", "Trondheim,Norway"). BUILD.md's older dated sections
  are correctly historical.

## 4. Self-containedness: statement-by-statement [D]
| Statement | Hypotheses | Proof states its premises? | Relies on companion/record |
|---|---|---|---|
| Thm 1.1 | integer n ≥ 2 | n ≥ 320: §4.6 proof, complete given §4. 2..319: §5 implications complete; certificate data external | κ receipt (P-03); certificates, trusted arithmetic, deposit (P-01, P-08) |
| Thm 1.2 | n ≥ 2, N = n+1/2 | yes (§3), uniform constant C; Λ_n version via Thm 1.1 | none for Λ_c |
| Lemma 2.1 | none | yes (Gram/alternating-part argument) [D][E] | none |
| Remark 2.2 | convention | — | — |
| Lemma 3.1 | g ∈ C(0,1)∩C²(open), \|g''\| ≤ C(x⁻¹+(1−x)⁻¹), endpoint moduli | yes | none |
| Prop 3.2 | m = n+1 ≥ 3 | yes; R(0), R(1), S_u, (cu:cancel), β-algebra all reconstructed [D][E] | none |
| Lemma 4.1 | v,s ≥ 0, 0 < e ≤ π/2 | yes, terse ("differentiation gives"); closed forms match quadrature to 1e-8 [E] | none |
| Lemma 4.2 | none | yes, terse rearrangement step (P-10c); bounds hold with wide margins [E] | none |
| Lemma 4.3 | phase triangle | uses (uc:origin-identity) ← Prop 4.5 (later) + Thm 1.2, and the coarse κ input | κ receipt (P-03); forward reference (P-10d) |
| Lemma 4.4 | x,y ≥ 0, ρ ≤ π/2 (diagonal needs p/2 ≤ a) | yes | none |
| Prop 4.5 | n ≥ 32; origin and relative bounds need n ≥ 160 | yes, 11 pages; telescope identity terse (P-10b) | none mathematically |
| Lemma 4.6 | (ul:charts), ρ ≤ r ≤ 1/2, 41 ≤ n < 512; tail: n ≥ 64, r ≤ 21/40 or π/4 | class-1 terms undefined (P-10a); band derivation terse | companion supplies the class-1 definitions |
| Lemma 5.1 | f_σ ∈ C², uniform second-derivative bounds | yes | none |
| Unnumbered regional results (6) | as in the P-04 table | yes, but not stated as results | — |

## 5. Constants and evidence statements versus the records [D][E]
**Constants (Sections 3–4).**
- **Coverage:** every displayed rational bound I recomputed at n = 320, 256 and 192 holds
  (`check_constants.out`, 100+ checks): (ul:near-base); A_h, B_h, A_w, B_w recomputed exactly
  from the lemma's F_h, F_w; L_h(ρ), the quadratic e, f, g and 34161² < 32·8233·4431; P(1/2),
  P(3/5); the outer list (C_b, C_s, C_l, G, K, A); the corner list (M(256) < 26, 49/1250 > 1/30);
  the far list (Ĉ_E < 1013/600, anchor exactly 79/2000); E_64 − 1/64 and E_160 − 1/32 (exact).
- **H_0:** the direct finite part equals κ/2 + (2k_0/π²)log(2/π) to 1e-31, independently
  confirming the model/corner link (uc:origin-identity).
- **Agreement with the records:** floors 1/20000, 3/1000, 99/2500, 13/500 match E14; 1/30 from 256
  with q_0 = 7/48 and r_U = 2/125 matches E12; 79/2000 > 3/100 from 192 with u_0 = 7/24 matches
  E15; the 320/256/192 onsets match G01.
- **Onset margins [E]:** the outer gate is 0.069 at 320, 0.064 at 319 and negative at 300, so 320
  is near-minimal for that argument. Floors sit 5.5–54× below the actual projections. The corner
  descent 1/30 compares with a true coefficient ≈ L²/π² ≈ 3.4.

**Evidence statements.** "280 primary/fresh pairs, 41..319 plus 511, 560 proofs, histories and
native replays at 199/238" matches `compact-return.md` and G01. The 2..40 single Bernstein scheme
(fresh 2–16, reused 17–40) matches `small-degree-unification.md`; the paper does not state that
split (good for a journal), but its pointer to an "execution record" should go (P-08). Degree 1
is correct as stated: λ_1 = max{1, |y| + (1−x)/2}, maximum 2 at (−1, ±1) [D].

## 6. Section-by-section coverage
| Unit (PDF pp.) | Read | Verdict | Issues |
|---|---|---|---|
| Front matter, abstract, keywords, MSC (1) | fully | accurate except computer-assisted omission | P-02, P-14, §3 placeholders |
| §1 Introduction (1–4) | fully | clear problem and theorems; weak contribution/literature balance | P-06, P-07, P-11, Fig. 1 unreferenced |
| §2 Normalization (4–5) | fully, reconstructed | correct and self-contained | weight notation (P-05) |
| §3 preamble, 3.1 exact rows (6–8) | fully, reconstructed + [E] | correct | none substantive |
| §3.2 square reference, defect, κ (8–9) | fully, reconstructed + [E] | correct | none |
| §3.3 Lemma 3.1, Prop 3.2, proof of Thm 1.2 (9–12) | fully, every identity reconstructed + [E] | correct; good | P-11 (l.7, 303, 416); optional DLMF cut (P-12) |
| §4 preamble, reflection geometry (13–14) | fully, reconstructed | correct | P-04 roadmap missing; P-05 |
| §4.1 completed model, Lemmas 4.1–4.4 (14–20) | fully; Lemma 4.2 bounds and κ link [E]; Lemmas 4.1/4.4 key steps [D] | correct; model definition unmotivated | P-03, P-05, P-10c,d |
| §4.2 Prop 4.5 and its proof (21–33) | read fully; structure and telescope [D]; individual charges not re-derived | plausible; consequences hold numerically | P-04 (appendix option), P-10b, P-15 |
| §4.3 Lemma 4.6 (34–36) | fully; constants [E]; floors vs actual [E] | correct; compressed | P-10a, P-05 (L, r, B_n, E_n), P-11 |
| §4.4 near exclusion (36–38) | fully, every number [E] | correct | P-04 (unnumbered results) |
| §4.5 outer/far (38–40) | fully, structure [D] + numbers [E] | correct; one step gap | P-09 |
| §4.6 corners and proof of Thm 1.1 (40–41) | fully, reconstructed + [E] | correct | P-12 (Bernstein citation) |
| §5 preamble, Lemma 5.1 (42) | fully | correct, clear | none |
| §5.1 small degrees, degree 1 (42–43) | fully | correct | P-08 (execution-record sentence) |
| §5.2 phase certificate (43–46) | fully, every implication reconstructed | correct; well explained | P-08 (W_z provenance) |
| §5.3 Evidence (46) | fully | accurate vs records; process language | P-01, P-08 |
| Declarations (46–47) | fully | data statement inaccurate; placeholders | P-01, P-13, §3 list |
| References (47–48) | fully | 13 items, correct order | P-12, P-16 |

**Balance of Sections 3–5.** Section 3 (7 pp.) and Section 5 (4.5 pp.) are right-sized; the
restoration of Section 5 to five pages was worthwhile, since every implication is checkable.
Section 4 (29 pp.) is where the reader is lost. Cuts and benefits, none removing a proof
obligation: (1) tabulate the base-degree constants (~0.7 page saved, scannable numbers);
(2) delete the four repeated disclaimers (~10 lines, better tone); (3) P-03 removes the κ-receipt
paragraph and its echoes; (4) cite classical ψ/cotangent facts (~6 lines); (5) an appendix for
the Proposition 4.5 charges (no pages saved, but a followable main-text chain).

## 7. Prioritized revision list (top 10)
1. **P-01** DOI deposit and corrected data/code statement. 2. **P-02** "computer-assisted" in the
abstract. 3. **P-03** six-term κ table replacing the Arb receipt. 4. **P-04** numbered regional
results, roadmap table and figure. 5. **P-08** formal Proposition 5.2 and affirmative §5.3.
6. **P-05** notation table and renames. 7. **P-06/P-07** value of Theorem 1.2, fits, attribution,
precise Λ_n dependency. 8. **P-09/P-10** the four compressed steps (P-09 coordinated with the
companion). 9. **P-11** prose pass. 10. **P-12 to P-16** and the §3 placeholders.

## 8. Suggestions on proof presentation [I]
- **Lead §4 with λ_n − Λ_c = (S_n − S_n(0)) − Δ_JK** (CONSOLIDATION.md's organizing identity,
  never displayed in the paper): the model bounds the first bracket, the floors bound Δ.
- **Explain M_∞ before defining it:** a Riemann sum over rows of the profile 𝓗(L, v); one mesh
  gives log n, summing rows the second log (companion comparison l.691–697 has three lines).
- **State the sharpness of the constants:** floors 5–50× and corner descent ~100× conservative
  [E]; the n ≥ 320 onset is set by the outer gate (negative near n = 300).
- **Optional:** a table of Λ_n vs the four-term expansion (P-06); a remark posing the next term
  (α log N + β)/N² as a question (no claim made).

## 9. Execution record and limits
- **Commands and outputs:** `p-code/README.md` and `p-code/*.out`; about 2.4 CPU-min in total,
  all MEASURED. The scripts implement the paper's displayed formulas directly; the projections
  use the half formula A(u,v)/(cos u − cos v), which I derived independently and validated against
  the Chebyshev sum (4.5e-13). The K = 5 κ check used mpmath interval arithmetic around ζ values
  ±1e-25 (illustrative, not a certified proof).
- **Not done:** no native or certificate replay (the compact return is absent here); no
  line-by-line re-derivation of every charge in the Proposition 4.5 proof, the band formula
  (ul:band-formula), or every derivative constant of Lemma 4.2; no fresh literature search (P-06
  relies on the recorded refresh).
- **No repository files were edited.**
