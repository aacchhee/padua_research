# P4 — Referee report: revised journal paper (Constructive Approximation), audit-04

**Auditor:** Claude Opus 5.5 (xhigh), independent referee subagent of the handoff-30 substantive
Claude audit. Read-only: no Git state changes, no repository edits. Outputs only this file and
`p4-code/`.
**Identity.** Branch `codex/padua-argmax-bridge-20261105`, head `70a50d7b2a72a30fd7a2af3b2ead54ae14470bf9`.
Rules read at that head: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md`, handoff
30 and `claude-audit-brief-onset512-20261108.md` (journal half of "Both manuscripts"). Paper TeX/Bib
at the freeze `24a98db4…`: `git diff --stat 24a98db HEAD -- paper/` touches only `README.md` and
`BUILD.md`, so the audited TeX equals the freeze [D].
**PDF.** B4's fresh build `audit4/build/paper/main.pdf`: 51 pages, SHA-256 `ad416ae0…e21d` (bytes
differ from the recorded `1346fc28…`, as expected). The log has no errors, undefined or multiply
defined references, or overfull boxes, and 68 underfull diagnostics. B4's page index:
19 statements, 116 labels, numbering equal to the companion's. Pages below are printed pages.
**Read.** The full paper first, as a standalone submission: `main.tex`, all six section files,
`references.bib` and the rendered bibliography. Then README, BUILD, template/README, the three
onset-512 response files, `notation-pass.md`, `audit-03/p-paper.md` and its `response-03.md` rows. For
constants and evidence: J01, J02 §2–3, J03, E12-corner256, E15, `local-onset512-summary.md`,
`compact-return.md`, `RESULTS.json` and the statistics in `zenodo-deposit/README.md`. The Sol max
review was skimmed only to avoid duplicate items. The companion was not used except as noted.
**Labels.** [D] my own reading or reconstruction; [E] computation I executed (MEASURED, `p4-code/`);
[I] inference or editorial judgment. Each finding is marked *correctness* or *editorial*.
**Novelty scope.** None. This is a manuscript and constant audit of an approved architecture with
no novelty or priority judgment, so the full `state/IDEAS.md` read was omitted.

## 1. Verdicts

- **Mathematics: ACCEPT.** I found no correctness defect at my reconstruction depth.
  - The new Section 4 chain was reconstructed line by line [D] and every displayed base constant
    re-evaluated [E]. This covers the absolute gate and the tangent-condition argument, the
    radius-one polynomial with completed square, both maximum identities, the half-radius
    fixed-segment argument and real-n monotonicity, the uniform 1/20 floor from 295, the
    corner-256 lemma and Theorem 4.10.
  - Sections 2–3: Lemma 2.1 and the §3.1–3.2 identities were reconstructed [D] and spot-checked to
    1e-29 [E]. The Section 5 implications were reconstructed [D], and the n=2 Bernstein table was
    recomputed exactly [E].
  - Not re-derived this round: each individual charge in the 10-page proof of Theorem 4.5 and the
    §3.3 aggregate constants. Audit-03 covered both and that text is unchanged in substance. I did
    re-derive the new assembly steps in Theorem 4.5: the uniform constant with its 3L̄/n saving
    and the coefficient bookkeeping for the relative comparison.
- **Exposition: ACCEPT WITH MINOR REVISIONS.** The audit-03 MAJOR items P-02, P-03, P-04, P-08
  and P-09 are substantially resolved. The paper now has a visible proof architecture (organizing
  identity, roadmap, two named gates, corner lemma, tail theorem) and a formal computer-assisted
  proposition. What remains is mostly notation and signposting. The notation collisions in
  P4-02 and P4-03 are the most important remaining items under AC's criterion that notation be
  introduced before use; the rest is editorial.
- **Self-containedness: adequate.** The n≥512 theorem is fully analytic, with only elementary
  rational checks (no Arb premise remains). The paper still gives final rational base values
  without intermediate enclosures (P4-05). It defers the floating-point error derivation to the
  package (P4-16, acceptable for a computer-assisted proof).
- **Evidence statements against the records: no mismatch** (§5).

## 2. Audit-03 findings: is each fix in the text, correct and complete? [D]

| ID | response-03 | In text? | Residual |
|---|---|---|---|
| P-01 | PENDING | Yes. The data statement names the GitHub URL and **DOI pending** in bold; no claim that the proofs are in Git (main.tex l.80–87). | §5.3 still has non-citable "recorded computation sites" (P4-08). Whether the repository is public was not verified [I]. |
| P-02 | FIXED | Yes. The abstract says "computer-assisted", gives the 512 split and κ. | γ is not named in the abstract (P4-03). "retains" register (P4-09). |
| P-03 | FIXED | Yes, and correct: K=3 endpoint-cancelled series, tail 1/480, Machin/log/γ/ζ brackets, outputs 0.917166<κ<0.921489 and C_*<1.84794 [D][E]. | None. |
| P-04 | FIXED | Mostly. Organizing identity, roadmap array, Fig. 2, Cor 4.6–4.7, Lemma 4.9 and Thm 4.10 are present. | No explicit proof of Thm 1.1. Thm 4.10, Prop 5.3, Lemmas 4.1–4.2, Prop 3.2, Figs 1–2 and Table 2 are never cited (P4-01). The Thm 4.5 proof has no roadmap (P4-12). |
| P-05 | FIXED | The register was applied (𝖺, L̄, 𝔗, 𝔧, B_n^♯, m̄/n̄, q_h, …). | The onset-512 rewrite re-introduced collisions: P_n, G, Θ, A_*, V/W, D, e_j, C (P4-02). |
| P-06 | FIXED | Yes: b, c, κ values, De Marchi fit with locator, 2006/2005 credit. KL fit omitted by decision X-06. | None (optional n-vs-Λ_n table not added). |
| P-07 | FIXED | Yes (intro l.145–149). | None. |
| P-08 | FIXED | Prop 5.3, Table 1 (trust) and Table 2 (coverage) are present. | "phase pair", "compact returns", "both retained phase trees" unexplained (P4-08). |
| P-09 | FIXED | The outer-geometry block was deleted. Cor 4.6 replaces it, and I re-derived Cor 4.6 [D]. | None. |
| P-10 | FIXED | (a) effective angle, ξ/ζ and the 24π/41 bound (l.188–202), verified [D][E]; (b) singular-sample sentence (l.736–737); (c) arc argument kept; (d) non-circularity sentence (l.457–458). | (c) has no citation, which is acceptable because the arc argument is elementary. |
| P-11 | FIXED | Reduced. | Residuals at §3 l.403, 423, 516; comparison l.740, 1357; certification l.237; abstract l.36 (P4-09). |
| P-12 | FIXED | Boas, Lorentz, Arb, FLINT, MPFR, GMP and Mesh2024 Prop 2.2 are cited. | The Section 5 exponential-type Bernstein inequality is cited but not stated (P4-04). Li₂ is undefined (P4-03). |
| P-13 | DECISION (AC) | Unchanged. | The factual inconsistency persists (P4-15). |
| P-14 | FIXED | New title, section titles and MSC 65G20 [D]. | None. |
| P-15 | FIXED | Vertical rules removed; `\hline` arrays remain, which is acceptable. | **Fig. 1 is still never referenced**, and neither are Fig. 2 and Table 2 (P4-01). Table 1 column justification (P4-14). |
| P-16 | FIXED | DRNA DOI and arXiv id are present. 22 entries, alphabetical [D]. | None. |
| P-17 | DECISION | — | None. |
| P-18 | FIXED | A records item outside the paper. | None. |
| X-01–X-05, X-07, X-08, X-10 | FIXED | Verified in the rendered bibliography and the introduction (Kuznetsova Thm 1 and Pimenova Thm 1 at periodic/equal-parameter scope; poster plus DeMarchi2022 §3.3) [D]. | None. |
| X-06, X-09, X-11, X-12, X-14, X-15, X-18, X-19 | DECISION | Consistent with the text. | None. |
| X-13 | FIXED | B4's log shows no overfull boxes [D]. | None. |
| X-16 | FIXED | B4's index: 116 labels and 19 statements, matching the companion. | None. |
| §3 placeholders | — | "Development draft" (l.42) and the AI "final human review … remain" sentence are still present; DOI pending is marked. ORCID placement and contributions are reserved to AC. | NOTE for submission. |

## 3. Findings (prioritized)

### P4-01 MINOR (editorial; P-04/P-15 residual): the proof chain of Theorem 1.1 is never assembled
**Location.** The only assembly is two sentences after Table 2 (§5.3, certification l.427–428, p.48):
"Section 4 supplies … Together these ranges cover every integer n≥2."
An unreferenced-label scan of the sources [D] finds these labels never cited:

- the statements `ul:tail-location` (Thm 4.10), `cert:finite-verification` (Prop 5.3),
  `uc:cancellation-lemma` (Lemma 4.1), `uc:scalar-maximum` (Lemma 4.2) and `cu:aggregate` (Prop 3.2);
- the figures `fig:padua-nodes` and `fig:phase-regions`, and the table `cert:coverage`.

**Impact.** A referee must infer that Theorem 1.1 = Thm 4.10 ∪ Prop 5.3. Lemmas 4.1 and 4.2 are
used only by phrase ("the cancellation lemma", "Apply H≤H_0").
**Fix.**
1. Add "*Proof of Theorem 1.1.* For n≥512 this is Theorem 4.10; for 2≤n≤511 it is
   Proposition 5.3." Place it after Prop 5.3, or at the end of §4 with a forward reference.
2. Cite Fig. 1 at intro l.90, Fig. 2 in the §4 roadmap (l.78) and Table 2 at l.422.
3. Replace the phrase-only uses: "the cancellation lemma" (l.332, 447) → "Lemma 4.1";
   "Apply H≤H_0" (l.450) → "Lemma 4.2"; cite Prop 3.2 at its consumer in the proof of Thm 1.2.

### P4-02 MINOR (notation; residual of P-05 introduced by the onset-512 rewrite) [D]
Collisions inside Section 4, each with two meanings a reader meets within a few pages:

- **(a) P_n.** P_n=T_{n+1}+T_n (localization l.20–21; Thm 4.5 proof l.675–676) versus the gate
  polynomial P_n(ρ) (Cor 4.7 l.1586; Thm 4.10; Fig. 2 label and caption). `notation-pass.md` had
  renamed this quantity to 𝔭(ρ); the rewrite brought P_n back.
- **(b) G.** The kernel G_n(u,v) versus the gate function G(n,ρ₁) (Cor 4.6).
- **(c) Θ.** The half-line defect Θ in (uc:halfline) (l.793–795) versus Θ=𝔗+j_* (l.1514ff).
- **(d) A_*.** Within one proof of Lemma 4.8, A_* is first a *lower* bound for numerators
  (l.173–174, 210, 218) and then an *upper* bound for A(b_-) (l.287, 302).
- **(e) V, W.** V_ρ̄ and W_ρ̄ in the statement of Lemma 4.8, versus V_± (l.162) and the span W
  (l.173, 210) in its proof.
- **(f) D.** The allowance D (uc:constants) versus "If D=𝒞(…)+𝒞(…)−2C_0" (Lemma 4.3 proof l.415).
- **(g) e_j.** Endpoint weights e_j (localization l.13) versus the endpoint comparison e_j (l.1229).
- **(h) B.** B=C_0²/π² (Lemma 4.3) versus the inward variable B (Lemma 4.9) versus B(h)
  (Cor 4.6 proof) versus B_β.
- **(i) C.** The remainder constant C in Thm 1.2 versus "C=−1+C_H+C_B" (corner l.539), which is
  then identified with κ.

**Fix (renames only).**
- (a) Gate polynomial → 𝔭_n (restore the checkpoint name), or rename T_{n+1}+T_n → Π_n.
- (b) G(n,ρ₁) → 𝒢(n,ρ₁). (c) Halfline Θ → Θ_r. (d) Tail A_* → Ā (and similarly Ī, R̄).
- (e) Span W → w_span. (f) D → D_𝒞. (g) e_j at l.1229 → ε̂_j. (i) C at l.539 → C_Λ.
- Also add one sentence in the §4 preamble explaining why θ_j, φ_k, ε_j, η_k become a_j, b_k,
  e_j, f_k there (collision with η_±, ε_d).

### P4-03 MINOR (notation introduced before use; named objects undefined) [D]

1. **ρ and x, y are used before they are defined.** ρ appears in "phase radius" (l.34), the
   roadmap (l.82–89) and Fig. 2, but is defined only at §4.1 l.8 (ρ=x+y). Likewise x,y appear at
   l.67–68 and A,B in the roadmap before Lemma 4.9. Fix: put x=|α|, y=|β|, ρ=x+y in (ul:charts)
   and say that A,B are the inward corner phases.
2. **"Complete signed board sum" is undefined at its first use** (Thm 4.5, l.645). It is defined
   only as f_ε in §5.2. Fix: define it in the theorem as (2𝖭)^{-1}Σ_{Γ⁻}ε_{rs}H_{rs}.
3. **Li₂ is used without definition** (Lemma 4.3 proof l.441–442). Fix: Li₂(z)=Σ_{k≥1}z^k/k².
   I verified the stated primitive by differentiation: its derivative is
   4𝖺cot(t/2)log sin t [D].
4. **"positive Cauchy sum"** (§3 l.4) is undefined. Fix: "a positive sum of quotients
   (1+cos v)/|cos u−cos v|".
5. **The abstract does not name γ.** Fix: add "(γ Euler's constant)".

### P4-04 MINOR (named tool not stated in the form used; P-12 residual) [D]
**Location.** §5.2 l.181–184: "The Bernstein inequality for functions of bounded exponential type
[Boas] supplies |f_aa|≤π²M …". The only Bernstein statement in the paper is the periodic one in
Lemma 4.9's proof.
**Fix (simplest).** Reduce to the stated periodic inequality. In the unscaled angles u=πa/n and
v=πb/m every f_ε is a 2π-periodic trigonometric polynomial of degree ≤n in each angle, so
∂_a²=(π/n)²∂_u² gives π²M and ∂_b² gives π²μ²M. The sup over a full period is the real-phase norm
M_*, which already appears. This removes the exponential-type citation. Alternatively, state
"f entire of exponential type τ, bounded on ℝ ⇒ ‖f''‖≤τ²‖f‖".

### P4-05 MINOR (self-containedness of the gate base checks) [D][E]
**Location.** Cor 4.6 base table (l.1556–1562), Cor 4.7 base bounds (l.1622–1627), Lemma 4.8
"F_h(295)>50064/10⁶" (l.305), Lemma 4.9 base list (l.376–381).
**Problem.** Only final rational bounds are printed. Intermediate enclosures appear only for n=256,
and only for L and L̄. The paper does not say that these were checked by the exact Fraction
checker that J01 cites, nor where that checker is. G(512,1)>0.534264 has a true margin of
7·10⁻⁷ [E], so it cannot be checked by hand without the intermediate values.
**Fix.**
- Add one table of rational enclosures at n=192, 256, 295, 512 for L, 𝔗, ē, K_D, C̄_E, C_4,
  k_Wx, k_Wy, d_β, M(n), U, d_x, d_y, ℓ_x and ℓ_y.
- Add one sentence identifying the deposited exact checker as the executed record of these
  comparisons (it is J01's `code/onset512_analytic/check.py`).
- All values were confirmed by `gates.out`; see §5.

### P4-06 MINOR (compressed proof steps in the gates) [D]
- **Cor 4.6 proof (l.1545–1552).** The argument is correct but compressed. "Hence R decreases
  there. Moreover R≤A+B²/(2A)≤A+t_*²cos h/(2Θ). This holds at h=π/2 by continuity" leaves three
  things implicit:
  - the key step R(h)≤R(h₁) for h∈[h₁,π/2], followed by evaluation at h₁;
  - A(h₁)≥Θcos h₁>0, because C sin h≥0;
  - monotonicity of tan, which gives A′≤0 for h≥h₁.

  Fix: write these three clauses. My reconstruction confirms
  uΘ−t_*sin x−K_D(sin x+sin y)=Θ−(A cos δ+B sin δ), with A=Θcos h+C sin h and B=t_*cos h.
- **Cor 4.7 proof (l.1597–1602).** The replacement of 𝔧 by j_* (which needs u≥0 and 𝔧>j_*) and
  the condition U≥0 are implicit. Fix: one clause.

### P4-07 MINOR (explanation of the uniform constant) [D]
**Location.** Thm 4.5 proof l.1102–1103: "Define the separated upper bound C_{E,sep}=C̄_E+3L̄/n.
Termwise maximization is at most this bound."
**Problem.** The reader must reconstruct the termwise maxima D, G_g,
(42+2L+(49L̄+24)/π)/n+318/n², 𝓜 and W_n. The inequality 42+2L+(49L̄+24)/π ≤ 64+16L+3L̄ is the
nontrivial step, with slack ≈1.76+1.4L. I reconstructed it, together with the correlated saving
(A=398/(11π²), B=48/π, 2(A−3)(B−3)>9) [D][E].
**Fix.** Display the five maxima and that inequality in two lines.

### P4-08 MINOR (P-08/P-01 residual: project language in §5) [D]
**Location.** Prop 5.3 (l.312: "both retained phase trees"); Table 2 caption (l.408: "Each phase
pair supplies two trees"); l.403–404 ("The small-degree route retains its independently authored
C++/GMP … driver", which repeats Table 1); l.436–443 ("compact returns", "complete numerical
histories for selected degrees 199, 238, 475 and 458", "remain at their recorded computation
sites").
**Problem.** The paper never says why there are two trees per degree, which come from two
independent search runs. "Compact returns" and "recorded computation sites" are not citable
objects.
**Fix.**
- Add one sentence: "each degree was searched twice independently; both trees were recertified,
  and either alone proves the degree."
- Move the archival history details into the Data availability statement or the deposit README.
- Write "grid norm (5.x)" and "tree norm (5.x)" instead of the code labels GRID/TREE (l.346,
  387, 424).

### P4-09 MINOR (prose register; P-11 residual) [D]
Remaining audit-history phrasing, with suggested rewrites:

| Location | Current | Suggested |
|---|---|---|
| corner l.403 | "must still be retained" | "We also need two summable sequences" |
| corner l.423 | "keeping e_r,u_r intact" | delete |
| corner l.516 | "The calculation keeps the last row …" | delete |
| comparison l.740 | "This derivation preserves m=n+1 and all finite origin values." | delete |
| comparison l.1357 | "with both meshes and their finite collisions intact" | delete |
| certification l.237 | "Their overlap retains the seam" | "The two proxies overlap on ρ=1/2" |
| abstract l.36 | "retains the cancellation lost by a periodic majorant" | "quantifies the cancellation that a periodic majorant loses" |

### P4-10 MINOR (correctness of a descriptive sentence) [D]
**Location.** Intro l.174–175: "A single comparison with a completed model then controls that
envelope and the competing reflection defects."
**Problem.** The reflection defect is bounded below by the selected-pair floors (Lemma 4.8), not by
the model comparison.
**Fix.** "A single comparison with a completed model controls that envelope, and explicit
selected reflected pairs bound the lost cancellation from below."

### P4-11 EDITORIAL (structure: a forward reference across sections) [I]
**Location.** Lemma 4.9 (§4.5) uses the "signed-vector interpolation principle of Lemma 5.1".
**Suggestion.** Move the Peano half of Lemma 5.1 (cert:peano) into §2 or just before Lemma 4.9,
and keep the Bernstein-coefficient half (cert:bernstein) in §5.1.
**Trade-off.** It costs one moved lemma and makes the analytic chain linear. The intro already
advertises "the same interpolation principle".

### P4-12 EDITORIAL (signposting inside the 10-page proof of Theorem 4.5) [I]
**Location.** pp. 26–36.
**Suggestion.** Open the proof with a five-step map:
1. the exact telescope (uc:telescope);
2. the row error |E_row|≤D_φ+K_D P;
3. the absolute components, giving (uc:global-error) and (uc:analytic-norm);
4. the origin, giving (uc:origin-lower);
5. the relative components, giving (uc:relative-comparison).

Optionally move the whole proof into an appendix (P-04 option 5). The main text would then read
geometry → model → Thm 4.5 → gates → floors → corner → Thm 4.10, with no page change.
In Thm 4.10's proof, "Thus only odd endpoint pairs remain" (l.422) should name the physical points
(−1,−1), (1,−1) and (−1,1).

### P4-13 EDITORIAL (residual atlas-like material) [D][I] — see §6.

### P4-14 EDITORIAL (rendering) [D]
- Table 1 (p.48) uses justified p-columns, which leaves large gaps ("Polynomial cer- tificates",
  "Direct phase sums"). Fix: `\raggedright` in the columns.
- Figure 2 (p.16) is legible, but "absolute gate" touches the dashed π/4 square and the arrow
  label sits on the ρ=1 cut. Fix: shift the labels or add a near-origin inset.
- The roadmap `array` (l.80–87) would read better as a small booktabs table that cites Fig. 2.

### P4-15 NOTE (declarations reserved to AC; factual consistency only) [D]
- **AI declaration** (main.tex l.69–72) lists Claude Opus 5.5, GPT-6 Astra and GPT-6.1 Sol. The
  topic LOG records Claude Sonnet 5.5 as an orchestrator/auditor model (LOG l.1595, 2693, 2703).
  This is the P-13 inconsistency, which persists by AC decision. I propose no wording.
- **Draft markers to resolve at submission:** "Development draft, 8 November 2026" (l.42) and the
  declaration's "remain to be completed".
- **Data statement.** Accurate as a pre-deposit statement: DOI pending is clearly marked, and the
  package contents match `zenodo-deposit/README.md` (frozen engine, independent checker, pins,
  commands). I did not verify that the GitHub repository is public [I]. If it is private at
  submission, the statement must change.
- **Funding, ORCID and contributions:** no factual inconsistency found. Funding is AC-confirmed.

### P4-16 NOTE (arithmetic premise deferred) [D]
**Location.** §5.3 l.355–360 (sentence at l.358): "The arithmetic proof in the reproducibility package derives this
bound (84ε t; allowance 128ε t)."
**Assessment.** Acceptable for a computer-assisted proof, and the premise is listed in Table 1.
**Optional.** A three-line sketch would make the paper self-contained here: at most 38 rounding
factors give γ₃₈ and 77ut; the Taylor tail is 2²⁶/27!<u; the argument error is 6ut; total 84ut
(J03 §4).

## 4. Self-containedness, statement by statement [D]

| Statement | Hypotheses | Does the proof state its premises? | Notes |
|---|---|---|---|
| Thm 1.1 | integer n≥2 | Yes, via Thm 4.10 (n≥512) and Prop 5.3 (2..511) | The assembly is not written as a proof (P4-01). |
| Thm 1.2 | n≥2, N=n+½ | Yes (§3); the Λ_n form uses Thm 1.1 | Analytic; one constant for all n≥2. |
| Lemma 2.1 | none | Yes: Gram split, alternating part vanishes (p+q+r+s=2n+1), inverse coefficient 1 at (n,0) | "Evaluation matrix invertible" follows from the positive Gram matrix (implicit). |
| Lemma 3.1 | C(0,1)∩C²(open), \|g''\|≤C(x⁻¹+(1−x)⁻¹), endpoint moduli | Yes | — |
| Prop 3.2 | m=n+1≥3 | Yes | Unchanged since audit-03 [D][E] there. |
| Lemma 4.1 | v,s≥0, 0<e≤π/2 | Yes (terse) | — |
| Lemma 4.2 | none | Yes; the f''' sign computation was rechecked: −311/71680 [E] | — |
| Lemma 4.3 | phase triangle; decomposition on ρ≤π/2 | Yes. The constants (uc:coarse-input), (uc:scalar-constants) and C_∞<9/4 were rechecked [E]. | Li₂ undefined (P4-03); unconsumed v_* z (P4-13). |
| Lemma 4.4 | x,y≥0, ρ≤π/2 (p/2≤𝖺) | Yes | B_β is not needed downstream (P4-13). |
| Thm 4.5 | integer n≥32; origin and relative parts need n≥160 | Yes, compressed; the new assembly was reconstructed | "signed board sum" undefined (P4-03); P4-07, P4-12. |
| Cor 4.6 | integer n≥160, 0<ρ₁≤π, tangent condition | Yes, reconstructed | P4-06; G and Θ collisions (P4-02). |
| Cor 4.7 | n≥512, ρ≤1 | Yes, reconstructed, including the fixed-segment argument for P_n(½) | P_n collision (P4-02); P4-06. |
| Lemma 4.8 | (ul:charts), ρ≤ρ̄≤½; tiers for 41≤n<512; tail n≥295 | Yes; all three classes and both band instances reconstructed [D][E] | A_*, V, W collisions (P4-02). |
| Lemma 4.9 | integer n≥256, A,B∈[0,π/4] | Yes. It uses Lemma 5.1 (forward reference), the periodic Bernstein inequality (stated) and Thm 4.5. | P4-11. |
| Thm 4.10 | integer n≥512 | Yes; seams and ties closed | P4-12 (name the points). |
| Lemma 5.1 | uniform second-derivative bounds for every σ | Yes | The Peano kernel is named, with its mass given. Sufficient. |
| Cor 5.2 | integer n≥192, ρ≥π/2 | Yes (Cor 4.6 at ρ₁=π/2) | — |
| Prop 5.3 | 2≤n≤511 | Yes, conditional on Table 1's arithmetic model | P4-08 wording. |

## 5. Constants and evidence statements against the records [D][E]

**The gate constants equal J01 exactly.** Each of the following is identical in the paper and in
J01 [D]:
- 𝔗, D, 𝓜, ē, K_D, M_A, g_n, G_g, W_n, C̄_E, A_4, C_4, d_β, J_W, k_Wx and k_Wy;
- U, ℓ_x, ℓ_y, d_x, d_y, 𝔢, 𝔣 and 𝔤;
- j_*=23/250 and t_*=221/500;
- G(n,ρ₁) and the tangent condition.

The consumed J02 constants match: κ>9/10, C_*<4629/2500, 𝔧>23/250, 0<t₀<221/500, C_∞<9/4. So
do the bracket constructions (J=48, A₄₀/A₃₉ Machin brackets, H₂₅₆, Z_s with 10 terms,
s∈{2,3,4,5,6,7,9}, K=3 tail 1/480).

**Values measured from the paper's own formulas** (`gates.out`, 50 digits):

| Quantity | Value [E] | Paper claim | OK |
|---|---|---|---|
| G(512,1) | 0.5342647 | >0.534264 (>½) | yes, margin 7·10⁻⁷ |
| G(192,π/2) | 0.0983190 | >0.098316 (>3/100) | yes |
| (t_*+2K_D)/Θ at 512 / 192 | 0.04740 / 0.09801 | <3/50, <1/10 | yes |
| max P₅₁₂ (both identities) | 0.0407860 | <40786/10⁶ <41/1000 | yes |
| P₅₁₂(½) | −0.1430697 | <−143069/10⁶ <−1/7 | yes |
| vertex 𝔣/(2𝔢) at 512 | 0.147341 | <3/20 | yes |
| d_x(512), d_β(512) | 2.763, 5.1·10⁻⁴ | >1, (0,5/48) | yes |
| x_*, y_* at ρ=½ | 0.276, 0.224 | both positive | yes |
| F_h(295) | 0.0500643 | >50064/10⁶ >1/20 | yes (exact Fraction) |
| corner-256 values | 𝔗=10.777, ē=0.1874, K_D=0.1993, C̄_E=1.405, C_4=0.0172, k_Wy=0.716, M=25.39 | >107/10, <1/5, <1/5, <3/2, <9/500, <93/100, <26 | yes |
| δ_A−r_U M, δ_D−2r_U M | 0.3295, 0.2142 | >2729/21000, >49/1000 | yes |
| descent coefficient | 0.1796 | >49/1250 >1/30 | yes |

Further checks:
- **Exact identities.** All 38 displayed rational identities in `exact.out` hold, including
  B♯₆₄−1/64=34466881/729484800000, B♯₁₆₀−1/32=88079689/182371200000, 71/6250000, 37/224,
  225/1040, 663/784 and 398/11, and the coefficient reconstructions of B_n(ρ̄) and F_h.
- **Monotonicity.** On samples up to 10¹², G(n,π/2) increases and max P_n, P_n(½) and the vertex
  decrease. This is illustrative only; the proof is analytic and I re-derived it [D].
- **How sharp is the 512 onset?** The illustrative scan gives max P_n<1/20 first at n=457,
  G(400,1)=0.155 and G(300,1)<0. So 512 is a convenient onset, and the paper makes no minimality
  claim.

**E12/E15 contracts.**
- The corner lemma keeps E12's contract (n≥256, π/4 square, (A²+B²)/30). It now consumes J01's
  smaller k_Wy, from the E14 signed outer ((23/3)L+155/2, versus E12's 15L+265/3); the base
  inequality still holds.
- The far-192 contract (n≥192, ρ≥π/2, gap 3/100) is kept. It is now proved by G(192,π/2)>0.0983
  instead of E15's 79/2000.
- Neither change conflicts with the frozen certificate metadata.

**Evidence statements.** Every count matches the records:
- **Phase degrees.** Table 2 lists 280 (41..319 and 511) + 191 (320..510) = 471 degrees with
  560+382=942 witnesses, i.e. two per degree, matching `compact-return.md`,
  `local-onset512-summary.md` and RESULTS.json.
- **Polynomial witnesses.** 39 cover 2..40.
- **Tree sizes.** 51..101 nodes for the old range (statistics.json); for 320..510, 51 nodes,
  26 leaves, three analytic far leaves and the grid norm (section5 response).
- **Independent rerun.** Both witnesses were checked at 41, 458 and 511 (RESULTS
  independent_rerun).
- **Sampled histories.** 199, 238, 475 and 458.
- **Phase-checker premises.** Actual-function uppers are used below 256 only (645 keys =
  3×215 degrees).

**Trust boundary.** The paper correctly presents the native Arb/FLINT/MPFR/GMP search as provenance
only, not as a premise. The independent direct-sum checker replaces the native evaluator's
row-reduction and actual-function premises. The finite floors, folding, squared Peano argument,
corner-256 and far-192 remain as stated mathematical premises (Table 1) [D].

## 6. Redundant or atlas-like material (task 4) [D][I]

| Location | Material | Needed by the chain? | Cut or keep |
|---|---|---|---|
| Lemma 4.3 statement and (uc:regular-loss); v_* in l.355–364 | −(H₀+v_*)z term | No. Every consumer uses only −𝔧u+t₀p or −𝔧u. | Keep z inside the proof (2−c_e−c_d=u+z), drop it and v_* from the statements: −2 lines, −1 symbol, no risk. |
| Lemma 4.4: b, B_β, E_c(0,y)=−B_β | boundary identity | No. Lemma 4.9's axis bound E_c(0,h)≤0 follows from (uc:central-pair-general) with p=0. | State E_c≤(4I₄/π²)p^{3/2}/√𝖺, with B_β only inside the proof: −5 lines. |
| (uc:analytic-norm), "every complete signed board sum" | board-sum norm | No. Only cardinal sums are consumed (Lemma 4.9); §5 certifies its own M_*. | Drop the clause or keep it as harmless. |
| §5.1 l.152–158 | the n=1 example | No; it lies outside Thm 1.1. | Turn it into a footnote or remark, or keep it (6 lines, pedagogical). |
| §5.3 l.403–404 and l.429–443 | native-search provenance, compact returns, histories | No (provenance). | Move to the Data statement or deposit README: ≈10 lines. |
| §1 l.5–10 versus §2 l.2–3; §4 l.68 versus §4.1 l.16; ψ in §3 (cu:psi) versus §4.1 l.93 | repeated definitions | Reminders | Keep, or shorten to "as in §2". |
| §3.2 (κ limit, (cu:deform)) | identification of the constant | **Yes**: it identifies C=κ in the proof of Thm 1.2. | Keep. |
| Finite floor tiers (ul:finite-floors) and Cor 5.2 | certificate premises | **Yes**, for 41..511. | Keep. |

The old annular, near-relative and outer-geometry branches are gone from the paper. No E13/E14
annular application remains [D]. The atlas residue is now small.

## 7. Section-by-section coverage

| Unit (pp.) | Read | Verdict | Issues |
|---|---|---|---|
| Title, abstract, keywords, MSC (1) | fully | accurate; says computer-assisted | γ unnamed; "retains" (P4-03, P4-09) |
| §1 Introduction (1–4) | fully | both strands balanced; correct credits (KL, Kuznetsova, Pimenova, 2005/2006, poster/2022) | P4-10; Fig. 1 not cited (P4-01) |
| §2 Normalization (4–6) | fully, Lemma 2.1 reconstructed [D] | correct, self-contained | weights renamed in §4 (P4-02) |
| §3 preamble, 3.1 (6–9) | fully; identities and Λ_c(2)=3 [D][E] | correct | "Cauchy sum" (P4-03) |
| §3.2 (9–11) | fully; (cu:square), (cu:deform) and the κ limit [D][E] | correct | none |
| §3.3 (11–15) | fully; Lemma 3.1 and ψ facts [D]; aggregate constants not re-derived this round | correct (audit-03 [D][E]) | P4-09; C clash (P4-02i) |
| §4 preamble, Fig. 2 (15–17) | fully; reflection formula, chart cover and organizing identity [D] | correct; good roadmap | ρ before definition (P4-03); P_n (P4-02a); figure labels (P4-14) |
| §4.1 model and Lemmas 4.1–4.4 (17–25) | fully; constants block [D][E]; Lemmas 4.1/4.2/4.4 key steps [D] | correct | Li₂, D, B (P4-02, P4-03); P4-13 |
| §4.2 Thm 4.5 (25–36) | fully; row identity, telescope, row bound, uniform constant and relative assembly [D]; individual charges not re-derived | correct as far as reconstructed | P4-07, P4-12; Θ (P4-02c) |
| §4.3 Cor 4.6–4.7 (36–38) | fully, reconstructed [D] and all base values [E] | correct | P4-05, P4-06; G, P_n (P4-02) |
| §4.4 Lemma 4.8 (38–40) | fully; three classes and both bands [D][E] | correct | A_*, V, W (P4-02d,e) |
| §4.5 Lemma 4.9, Thm 4.10 (40–42) | fully, reconstructed [D][E] | correct | P4-11, P4-12 |
| §5 preamble, Lemma 5.1 (42–43) | fully | correct | — |
| §5.1 small degrees (43–44) | fully; n=2 table recomputed exactly [E]; n=1 [D] | correct | n=1 (P4-13) |
| §5.2 phase certificate, Cor 5.2 (44–47) | fully; norms, proxies, floor radius and corner witness [D] | correct | P4-04 |
| §5.3 evidence, Tables 1–2 (47–48) | fully; checked against the records [D] | accurate | P4-08, P4-14, P4-16 |
| Declarations (49) | fully | accurate pre-deposit | P4-15 (AC-reserved items) |
| References (49–51) | fully | 22 items, alphabetical, metadata as recorded | none |

## 8. Prioritized revision list (top 10)

1. **P4-02** Section 4 notation collisions: P_n, G, Θ, A_*, V/W, D, e_j, B, C.
2. **P4-03** Define ρ, x, y and A,B before use; define the signed board sum, Li₂ and "Cauchy sum";
   name γ in the abstract.
3. **P4-01** Add an explicit proof of Thm 1.1 and cite Thm 4.10, Prop 5.3, Lemmas 4.1–4.2,
   Prop 3.2, Figs 1–2 and Table 2.
4. **P4-05** Add the base-value table at n=192/256/295/512 and name the exact checker.
5. **P4-04** Reduce the §5.2 Bernstein step to the stated periodic inequality.
6. **P4-06** Add the missing clauses in the Cor 4.6 and Cor 4.7 proofs.
7. **P4-07** Display the five termwise maxima for C_{E,sep}.
8. **P4-08** Explain two trees per degree; move archival detail to the Data statement.
9. **P4-10** Correct the intro sentence about reflection defects.
10. **P4-09, P4-12, P4-13, P4-14** Prose pass, Thm 4.5 roadmap, atlas trims, Table 1 and Fig. 2.

**Process note.** All of these are TeX changes under the paired freeze `24a98db` and its
correspondence baseline (19/85/116). Under the third-round rule, items P4-01, P4-03, P4-09 and
P4-14 are wording or formatting. However, any edit forces a new paired freeze, a re-baselined
correspondence helper and a rebuild. I therefore recommend returning all of them to development
as one editorial batch, with a focused diff review, rather than auditor in-place edits. The
renames in P4-02 and the added proof clauses in P4-05–P4-07 should be treated as material for
review purposes, since they touch proofs.

## 9. Proof-presentation suggestions [I]

- **End §4 with a summary table.** List the four regions with each one's statement number, so that
  Thm 4.10 becomes a five-line citation of Cor 4.6, Cor 4.7, Lemma 4.8 and Lemma 4.9.
- **Keep the organizing identity as a displayed, numbered equation.** Thm 4.10 and §5.2 should
  cite it by number.
- **State the conservatism once in §4.** The floors are 5–50× below the actual projections, the
  descent coefficient is ~1/30 against a true ~L²/π², and 512 is a convenient rather than minimal
  onset (G(n,1)>½ from about 400; max P_n<1/20 from 457 [E]). Referees will ask.
- **Optionally add a residual table for Theorem 1.2.** For example n=64: Λ_c minus the
  four-term expansion is 2.25·10⁻⁵, and N²/log N times the residual is bounded [E]. It shows the
  O(log N/N²) order without claiming a next coefficient (X-19 decision).
- **Mark the computational propositions as such.** Phrase Prop 5.3 as "the predicates hold for
  the deposited trees, as verified by the checker [DOI]", rather than in the perfect tense
  "have been recertified".

## 10. Execution record and limits

- **Scripts.** `p4-code/README.md` gives the commands, exits and walls: gates.py 20.8 s,
  exact.py <1 s, n2_and_kernel.py 1.3 s, sec3.py ~3 s. That is about 0.5 CPU-min in total, all
  MEASURED except the exact Fraction checks. The scripts implement the paper's displayed formulas.
  No repository or archive code was executed.
- **Not done.**
  - No line-by-line re-derivation of each charge in the proof of Thm 4.5, or of the §3.3
    aggregate constants (both accepted at audit-03; the text is substantially unchanged).
  - No companion reading beyond B4's numbering index.
  - No native, I25 or polynomial-checker rerun; these belong to other audit parts.
  - No verification that the GitHub repository is public.
  - No new literature search.
- **No repository files were edited.**
