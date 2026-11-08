# Audit-03 (handoff 28): Claude's own proof and presentation ideas

Rules f366535. Branch `codex/padua-argmax-bridge-20261105`, read-only head
`f366535e1fa4ede566cb83bdc554220c12b307cf`. Role: independent idea proposer inside the
substantive Claude audit; Claude proposes, Codex implements. Model: Claude Opus 5.5, xhigh
(WORKFLOW row "adversarial audit / novel mechanism" and ideas campaigns). 2026-11-08.
No git command changing state, no repository file edited. Outputs only here and in `i-code/`.

Labels. **MEASURED**: binary64 or mpmath floating evaluation, no enclosure. **ENCLOSED**:
exact `Fraction` arithmetic, or the prototype binary64 interval code of `i-code/rig_S.py`
(valid under the stated IEEE-754 assumption; prototype, not a reviewed checker).
**DERIVED**: my own elementary derivation, not independently reviewed. Nothing here is
PROVED, no proof premise changes, no degree status changes. Provisional IDs continue the
earlier series: I01–I10 were proposals, I11–I24 retained candidates (audit-01/02 ideas), so
new labels start at `IDEA?argmax-bridge-claude-I25`.

## 0. Bottom line (ranked)

1. **I25 (proof/verification): a second-arithmetic, from-the-manuscript replay of all 560
   phase certificates (41–319 and 511).** The only numerical premises are per degree
   ≤256 S-vertex uppers (45 in the sampled degrees), 3 actual λ uppers below 256, one corner
   lower L_c and the grid norm. All of them are O(n²) sums of products of sines of
   *exactly rational* multiples of π. An independent evaluator written from the paper's
   formulas (no Arb, MPFR, GMP or libm) reproduced **all 90 S premises and all 6 λ premises**
   of the committed 199/238 primary and fresh certificates to 1.3e-15 and 1.4e-14 (MEASURED).
   A rigorous-interval prototype gives enclosures of width ≤1.05e-9, consistent with every
   native upper and exceeding none by more than 2.5e-11 (ENCLOSED). The smallest leaf margins
   are 1.48e-3 (FAR) and 3.43e-3 (NEAR). That leaves at least 6 orders of magnitude of headroom (enclosure width 1e-9 against margin 1.5e-3; the shift from native uppers is about 8 orders below the margin). Cost:
   1.2–3 CPU-s per degree in floating point and about 36–55 CPU-s per degree in the
   unoptimised interval prototype, so roughly 2–3 CPU-h in total. This closes exactly the
   limits G01 records: no local rerun of all 273 degrees and no independent arithmetic.
2. **I26 (proof): an exact-rational lemma for the coarse constants removes the PD-T271
   dependency from the whole global chain.** The paper's own series (uc:kappa-series) with
   K=6, its stated tail and ζ/γ/log/π brackets in `Fraction` give κ∈(0.919677, 0.919784)
   and C_*∈(1.846102, 1.846328) (ENCLOSED, under 1 s). These imply every consumed
   consequence: 9/10<κ<23/25 and 923/500<C_*<1847/1000. The analytic tail n≥320 and the
   E12/E15 analytic leaves then need no outward-arithmetic premise at all.
3. **I27 (proof): a third term of the corner expansion.** MEASURED, n≤12800 with a
   cancellation-free exact-row evaluator:
   R_n·N² = −(7/36)·log N + e0 − 1/(2N) + o(1/N), with e0 = 0.9115265.
   - The Richardson estimate of the log coefficient is −0.1944437. The candidate −7/36 is
     −0.1944444.
   - The form holds for both parities through order N⁻³.
   - The guess −(1+κ)/π² is refuted at relative error 3e-4 (MEASURED).
   This would show that the theorem's O(log N/N²) is attained, and it gives a concrete
   H-campaign target.
4. **I28 (presentation): make the computer-assisted part refereeable for Constructive
   Approximation.** Proposed contents:
   - one formal "finite reduction" proposition listing the exact premises;
   - a before/after trust table;
   - a per-degree certificate table;
   - one worked leaf and corner witness taken from the real n=199 certificate;
   - a referee checker (I25) and a ledger of displayed rational constants;
   - a data-availability statement.
5. **I29 (presentation): figures and remarks for the journal paper.** The journal paper has
   only the node figure. Proposed additions:
   - a proof-map figure and a ρ-region figure;
   - a remark that the O(log N/N²) remainder is attained (I27, labelled numerical);
   - the true isolation gap g≈0.5485 next to the proved 1/20000 (I30);
   - Theorem 1.1 stated for n≥1;
   - after I26, deletion of the sentence about a separately certified enclosure.
6. **I30 (proof, structural): sharp second maximum.** MEASURED at n≤256: the largest value of
   λ_n outside the corner cells lies at the centres of the edges x=±1. Λ_c−λ there is
   0.600, 0.577, 0.561, 0.555, 0.552 at n = 16, 32, 64, 128, 256, approaching PD-T187's
   g = 0.54851 (computed from the PD-T188 series). Target: λ_(2)(n) → Λ_c − g. The upper
   half is PD-T187, a duplicate. The lower half is OPEN.

**Onset 320 (asked).** 320 is essentially the limit of the present recipes. The three
non-corner regions bind at 304–320, ideal radial optimisation gives only 312, and F01–F10
lowered nothing (audit-02 §2.2–2.6, campaign-F-summary). A lower analytic onset now has
low value because I25 makes the whole 41–319 range independently re-checkable in a few
CPU-hours. It is deferred (§4).

## 1. Novelty gate (completed before §3)

**Registry.** `state/IDEAS.md` sha256 `d7ec3aa6cf36f72e…`, 1154 lines, 312947 B. This is the
same blob that audit-02 read in full.
- Read in full this session: lines 1–125 (canonical seed/contextual tables, executed
  corrections, obstruction table) and 256–292 (Lanczos obstruction and seed tables).
- Also read in full: 400–520 (MZ obstruction memory, current MZ, lattice and programme
  dispositions with their obstruction tables) and 818–937 (PR12 and PD-N072/073, PR17
  IDEA-316–335, PR19 IDEA-336–348 with PD-N084–086, T2–T4 IDEA-356–358 with route memory).
- Also read in full: 994–1020 (PR25 IDEA-454–461).
- Scanned at ID/alias-column level: all 66 headings and lines 521–741, 938–993 and
  1021–1154.
- Coverage limit: lines 742–817 (MZ 2D, drift) were scanned by heading and first rows
  only. Their tool output was truncated; they contain no Lebesgue-argmax or corner
  mechanism.

`literature/INDEX.md` (sha256 `1f6f2acea05a6c65…`) was grepped for: Białas-Cież/LIT-388,
local maxima, computer-assisted, interval, validated, Arb/MPFR, Kolomoitsev, Günttner,
Euler–Maclaurin/Navot/Sidi and log-singular quadrature.

Files read (sha256[:16], bytes; full unless noted). T = topics/padua-argmax-bridge-20261105.

| File | sha | bytes |
|---|---|---|
| AGENTS.md / agents/WORKFLOW.md / CLAUDE_ROLES.md / templates/IDEA.md | c44a76f1… / 65e6b726… / 35c6146f… / 38e6a12c… | — |
| T/claude-audit-brief-20261108.md | 1a62653a1f430d07 | 14972 |
| results/padua-argmax-bridge-20261105.md (top 80 lines); T/report.md (first 60 lines) | 45710a98… / dca4abcb… | — |
| T/theory G01, H, E14-assembly320, E06-H-consequences (lines 1–100) | 646cca0b… / b31aae94… / 4b10b0ca… / a6a39e13… | 6253/8175/14078/17137 |
| T/campaign-F-summary, campaign-H-summary, campaign-H-gate, campaign-analytic-F (lines 1–80) | d86fb002… / 8bb94867… / 5c2ee705… / 96df1114… | — |
| T/audit-01-ideas (§0–5), audit-02-ideas (full), audit-02/m2-H-model (lines 100–250) | cb5929c0… / 16394a5f… / 278bef29… | — |
| T/paper introduction, preliminaries, corner-unified (lines 1–260), certification-unified (full) | c8c9c35b… / f5cd4b1d… / c74e94d3… / 80c4e3e7… | — |
| T/paper localization-unified (lines 1–110, 530–560), comparison-unified (lines 395–470), main.tex | 180efdc2… / be20756e… / 013789e9… | partial |
| T/compact-return.md; code/final_hybrid_engine/SPEC.md (lines 1–140) | a57409f8… / d8af873f… | — |
| T/evidence/compact-return/{primary,fresh}-n{199,238}.json | 4e58080f… / 2bc59c54… / 52f26a6f… / de740bcb… | ≈5.7k each |
| PD-T271 t4-03; PD-T266 t2-01 (lines 1–60); PD-T187/188 (head) | 957802f2… / 88bddbbb… / e7753a40… / 59a669b5… | — |
| IDEA-344 finite-native.md; T/ideas/D08-corner-limit.md; T/paper/consolidation-audit.md (grep + lines 284–304) | e4f9b8f3… / e07e7e19… / 74ea079a… | — |

**Searches.** Case-insensitive rg over IDEAS, T/ideas, T/attempts, T/novelty-gate-*,
T/audit-0*, paper and companion records:
- second/independent arithmetic or implementation, reimplement, pure-python, numpy;
- a-priori rounding, nextafter, IEEE, directed rounding, libm;
- PD-T271 remove/replace/elementary, κ>9/10;
- next term, third order, log N/N² coefficient, 1/N³;
- second-largest maximum, runner-up, gap constant;
- proof map, dependency diagram, worked example, tiny n, data availability, zenodo,
  supplementary;
- degree one, n≥1.

**Shortlist and what each fixes.**

| Entry | Bearing |
|---|---|
| IDEA-344 (independently written C++/GMP replay of Bernstein certificates; used for 2–40 per small-degree-unification) | Closest predecessor of I25, but it covers the exact-rational Bernstein scheme only. For 41–319 the only arithmetic is the frozen Arb/D23 native code. Fresh replays reuse it: independent-checks-D23-result says "not an independent implementation of Arb"; G01 states "not … an independent arithmetic implementation". |
| IDEA-418 / IDEA-466 (binary64 run with exact dyadic certificate; dyadic outward certifier, other topics) | Generic validated-numerics technique precedents. No priority claimed. |
| D08-corner-limit idea (κ>9/10 by elementary positive offsets: **equivalent**, consolidated into PD-T271, alternative unexecuted); consolidation-audit row 117 (coarse consequences, "preserve the computer-assisted dependency"); my audit-02 NOTE m2-N3 | I26 predecessors. I26 differs: aim = removing the trust base, scope = all consumed constants (upper bounds and C_* included), method = paper's own series in exact rationals, and it is executed. |
| PD-T098/H (O(log N/N²) proved, no next coefficient claimed); T4 PSLQ route memory (κ closed form, MEASURED none); LIT-487 Günttner (1-D Chebyshev expansions) | I27 predecessors. No 2-D next-order coefficient appears in the registry or the INDEX grep. |
| PD-T187/188 (edge-centre gap → g, 47/(9π²)<g<1651/(300π²)), PD-T266/268 (edge-defect integrals minimal at the centre), IDEA-318/324/339/340 (maxima-ordering and edge-cell comparisons, deferred/OPEN), LIT-388 (local-maxima counts only, no location of maxima) | I30's upper half is a **duplicate** of PD-T187; the lower half is a variant of PD-T187's OPEN "central envelope comparison". |
| IDEA-337 / I17 / I16 / I13; E/F constants (F04 K 120000, F09 K 41000) | Lower-onset routes; see §4 and §5. |

Binding obstructions respected:
- PD-N079/IDEA-333: no quadratic primitive maximality is used.
- "Projections are never added" (I30 uses max, not sum).
- E03 cusp: no uniform quadratic through the origin.
- PD-N132: no a·b_n form.
- Actual-origin lower is never used as a norm.

## 2. Sanity computations (all in i-code/; Python 3.13.18, numpy 2.5.3, mpmath 1.3.0)

**2.1 Independent evaluator (I25).** `indep_S.py` implements
G_n = R_{n+1}(S)R_{n+1}(T) + R_n(S)R_n(T) − (−1)^r cos(πa), with R_k(x) = sin(kx)/sin x.
- S = (u+v)/2 and T = (v−u)/2 are written as π·integer/(2nmQ) and reduced exactly in
  integers.
- There are no cancellation-prone differences of cosines. Removable values are exact.
- λ uses ul:cardinal-reflection with four G values per node.

Validation steps:
- `check_small.py` compares against brute-force Vandermonde interpolation at n=1–5 and 8,
  four points each, plus the corner. Maximum difference: 8.9e-15 (MEASURED).
- `timing_and_mp.py` compares against mpmath at 40 digits at n=41, five vertices:
  5.2e-16 (MEASURED).
- `check_certs.py` runs on the four committed certificates:

| Certificate | 45 S premises: native upper − independent | 3 λ: upper − indep. | indep. corner − native L_c | CPU |
|---|---|---|---|---|
| primary/fresh n199 | within ±1.33e-15 | 1.07e-14…1.42e-14 | +9.88e-9 | 1.2 s |
| primary/fresh n238 | within ±1.33e-15 | 7.1e-15…1.07e-14 | +6.09e-9 | 1.6 s |

`rig_S.py` is a rigorous prototype. Every float operation's result is widened by one ulp
with nextafter. It uses its own degree-25 Taylor sine with Lagrange remainder (no libm) and
bounds the summation error by γ_N ≤ 2Nu on any summation tree. Result on primary n199 and
n238: maximum width 6.97e-10 / 1.05e-9, `lo ≤ native upper` for all 90 S points, and
max(hi − native upper) = 1.78e-11 / 2.54e-11, at 36.0 / 54.9 CPU-s (ENCLOSED under the IEEE
assumption). Margins recorded in the certificates: FAR 1.48e-3, NEAR 3.43e-3, used floor
0.0337, corner gap g = 57.4, GRID norm M = 24. At n=319 the floating evaluation of 45 S, 3 λ
and the corner takes 2.97 CPU-s.

**2.2 Coarse constants (I26).** `kappa_rational.py K M` uses only `Fraction`:
- 𝔞_p, 𝔟_q, c_k from uc:kappa-series;
- tail 8/(3(K+2)4^{K+1}) as stated in the paper;
- ζ(s) as Σ_{k≤M} k^{-s} plus the integral tails [∫_{M+1}^∞, ∫_M^∞];
- 333/106 < π < 355/113;
- log via atanh series with geometric tails (log 2, log(4/π));
- γ ∈ (H_64 − 6log2 − 1/128, H_64 − 6log2 − 1/128 + 1/(8·64²)). DERIVED: the trapezoid
  error of 1/x is positive and at most Σ_{k≥M} 1/(6k³) < 1/(8M²).

| K, M | κ enclosure | C_* enclosure | 9/10<κ | κ<23/25 | 923/500<C_* | C_*<1847/1000 |
|---|---|---|---|---|---|---|
| 4, 60 | (0.919111, 0.920188) | (1.845536, 1.846732) | yes | no | no | yes |
| 5, 60 | (0.919508, 0.919923) | (1.845933, 1.846467) | yes | yes | no | yes |
| **6, 200** | **(0.919677, 0.919784)** | **(1.846102, 1.846328)** | yes | yes | yes | yes |

PD-T271's 30-digit κ lies inside, which also checks the paper's displayed series
transcription. The κ>9/10 bound alone needs only K=2.

**2.3 Corner remainder (I27).** `corner_next2.py` computes Λ_c exactly from cu:positive.
Each f = 2cos²(v/2)/(2|sin((u+v)/2) sin((u−v)/2)|) has exact integer half-angles, and the
sum uses math.fsum. R_n = Λ_c − [(4/π²)(log N + d)² + κ − 1/N]. The table gives N²R_n
(MEASURED).

| n | 300 | 600 | 1200 | 2400 | 4800 | 9600 | 12800 |
|---|---|---|---|---|---|---|---|
| N²R_n | −0.1995267 | −0.3333149 | −0.4675971 | −0.6021271 | −0.7367814 | −0.8714976 | −0.9274212 |

- Doubling increments: −0.13379, −0.13428, −0.13453, −0.13465, −0.13472. Their differences
  halve, and the Richardson limit is −0.1347781, giving e1 = −0.1944437 against
  −7/36 = −0.1944444.
- With e1 = −7/36, N²R_n + (7/36)log N + 1/(2N) equals 0.9115263–0.9115265 for every
  n = 600…9600.
- Odd and even n give the same smooth function of N. For example, the 6400/6401 difference
  −3.02e-5 equals e1·Δlog N.
- Alternative e1 = −(1+κ)/π² = −0.194507 makes the residual drift (−0.52 → −1.16 in the 1/N
  slope). REJECTED: refuted, MEASURED.

**2.4 Second maximum (I30).**
- `gap_full.py`: full square at n=16 and 17, resolution 1/6 mesh cell, excluding the two
  corner cells. The maximum is at the edge-centre vertices (J=0 or n, K≈m/2), with gaps
  0.59992 and 0.59056.
- `gap_probe.py`: over all odd vertices up to n=33, the top non-corner values are edge
  centres.
- `gap_probe2.py`: local 1/16-cell search around them. Gaps 0.5771, 0.5612, 0.5547 and
  0.5516 at n = 32, 64, 128, 256. The increments halve, so the extrapolated limit is about
  0.5485.
- `g` from the PD-T188 series is 0.548515 (MEASURED). Total CPU of all runs ≈ 3.5 min.

## 3. Ranked proposals

### Rank 1 — I25: second-arithmetic replay of every phase certificate, written from the manuscript
Aliases: from-paper referee checker; trust-base diversification; independent S/λ evaluator;
binary64 interval replay.
- **Target.** For each of the 560 essential certificates in the compact return (`return.tar.gz`,
  sha b00fd57f…), the checker takes only the tree token string, n, the declared floor tier
  and the analytic-branch flags. Everything else is recomputed independently:
  - every vertex S upper, every actual λ upper and L_c, using a separate arithmetic;
  - the GRID norm by cert:grid-norm;
  - every FAR/NEAR/SPLIT predicate (cert:phase-bound with ul:finite-floors);
  - the corner g-test and the analytic-leaf guards (ρ≥π/2 from 192, corner from 256).

  All of this uses exact rationals, from paper §5 and §4 formulas only. Success means all
  560 accept with the independent values substituted.
- **Distinction from IDEA-344.** That replay targets the exact Bernstein scheme 2–40. Here
  the target is the transcendental premises of 41–319. Arb/FLINT/MPFR/GMP/libm, the compiler
  and the D23/D07 native kernels are replaced by IEEE-754 basic operations, Python integers
  and an own sine polynomial.
- **Falsifier of the distinction.** The distinction disappears if the checker imports
  engine code or copies its numerical algorithm (row reductions J2/K8/…). The direct O(n²)
  board sum from ul:primitive is a different algorithm.
- **Scoped failures.** None apply; no mathematics changes. The shared-specification risk
  (IDEA-344 test-discriminability note) is reduced by writing from the manuscript, and every
  place where the manuscript is insufficient is itself a finding.
- **Cheapest decisive test (done here, §2.1).** Pre-stated criterion: independent values
  agree within 1e-9 and no rigorous lower bound exceeds a native upper. Kill: any
  discrepancy >1e-6 (a native or formula error) or any lo > native upper. Outcome: pass at
  4/560 certificates.
- **Remaining risk.**
  - Floor-tier or B_n(r) transcription mismatches between paper and engine. These would
    surface as predicate failures, which is useful.
  - Retrieval of the off-Git archive (chat file IDs aa/ab).
- **Cost.** About 7 CPU-min floating; about 2–3 CPU-h with the unoptimised interval
  prototype, a few times less after vectorising the Taylor kernel. It runs in the sandbox,
  so no Syvert job is needed.
- **Effect.** G01's verification boundary becomes "two independently written arithmetic
  implementations agree on every premise of all 280 pairs; the cover predicates were
  re-decided twice in exact arithmetic". For a referee this replaces trusting a native
  ball-arithmetic stack with a short, readable Python checker.
- **Priority HIGH, cost LOW–MEDIUM.**
- **First task for Codex.** Port `i-code/rig_S.py` (S, λ, L_c) and write a ≤400-line
  parser and predicate module from paper §5 only. Run it on 41, 199, 238 and 511 (the
  committed or known certificates) with 20 corruption controls (flipped token, perturbed
  floor tier, a vertex value lowered by 10% of the margin). Use a MEASURED receipt and a
  60 CPU-min cap. Prepare the all-560 run as a separate preregistered release.
- **Verdict.** New within documented search (implementation-level verification), no
  mathematical novelty claim.

### Rank 2 — I26: exact-rational coarse-constant lemma; PD-T271 leaves the global chain
Aliases: elementary κ lemma; trust-free H0>7/25; rational corner-constant bracket.
- **Target.** Lemma: 9/10 < κ < 23/25 and 923/500 < C_* < 1847/1000. Proof: the paper's
  series with K=6 plus the brackets of §2.2, evaluated in exact rationals. It is one short
  displayed computation that any CAS reproduces in under a second; a table of c_0…c_6
  brackets can be printed.
- **Consumers to re-point.**
  - uc:coarse-input / uc:scalar-constants: H0, j > 23/250, C∞ < 9/4.
  - E12-corner256 and E15-far192: j, t0, C∞ < 9/4.
  - D08/E14 node paragraph: C∞(0) > 4383/2420, which is redundant.
- **Distinction from D08 and consolidation-audit row 117.** D08 dropped an equivalent
  κ>9/10 route because PD-T271 already proved it; row 117 kept the computer-assisted
  dependency. I26's separation is the trust base and the full consumed set, not a new
  constant. Falsifier: some consumer needs more than these rational consequences. Even then
  the route survives with larger K and M (still exact rationals); it dies only if a
  consumer needs a quantity outside the series.
- **Test.** Done: ENCLOSED pass at K=6, M=200. The remaining paper test is a grep of all
  PD-T271 consumers.
- **Effect.**
  - The n≥320 theorem and the E12/E15 analytic leaves become fully analytic.
  - The introduction's "also uses a separately certified constant enclosure" and the
    end-of-proof trust sentence (localization lines 555–557) can be deleted.
  - G01's dependency list loses PD-T271.
- **Priority HIGH, cost very LOW.**
- **First task.** A PAPER note listing every PD-T271 consumer and the rational fact it
  uses, plus `kappa_rational.py` made into a committed checker with a receipt.
- **Verdict.** Variant with difference (it resolves m2-N3 and resumes D08's unexecuted
  alternative with a broader target).

### Rank 3 — I27: the third corner term
Aliases: next corner coefficient; −7/36 law; second half-step correction.
- **Target.** Λ_c(n) = A(N)² + κ − 1/N + [−(7/36) log N + e0]/N² + O(log N/N³), with e0
  explicit. Measured e0 = 0.9115265, and the next term looks like −1/(2N³).
- **Distinction from H.** H proves O(log N/N²) and disclaims the next coefficient. A
  rational log coefficient is natural: generalized Euler–Maclaurin terms for x·log x endpoint
  singularities carry B₂/2 = 1/12-type rational factors, while a²-weighted logs cancel
  against 1/a endpoint weights. That is a heuristic only.
- **Route.** Extend the quadrature lemma cu:quadrature to the next order. That means the
  endpoint expansions of g with x·log x and x² log x terms (Navot-type generalized
  Euler–Maclaurin), H05 centering through O(m⁻³ log m), the H04 smooth part through
  O(n⁻³), and the shift N = m − 1/2 kept one order further.
- **Kill.** An independent 30-digit evaluation (mpmath, the second identity of cu:exact, a
  different code path, n ≤ 2·10⁴) gives a Richardson e1 differing from −7/36 by more than
  1e-6, or a parity split appears at order N⁻².
- **Cost.** Test ≤ 30 CPU-min; proof is a 3–6 round campaign.
- **Effect.**
  - A genuine new term in the expansion.
  - Even unproved, a numerical remark that N²R_n/log N → −7/36 shows the published
    remainder order is attained (I29).
  - It also gives e0 for a PSLQ attempt once 25+ digits exist.
- **Priority MEDIUM.**
- **First task.** The kill test only, MEASURED.
- **Verdict.** New within documented search (no registry or INDEX entry for a 2-D next
  coefficient).

### Rank 4 — I28: refereeable computer-assisted part (paper §5 plus supplement)
Aliases: finite-reduction proposition; trust ledger; worked certificate; referee kit.
- **Proposal.**
  - (a) State one Proposition 5.x. Given a midpoint tree and branch flags, list the premises
    as finitely many inequalities: ≤256 vertex uppers W_z ≥ S_n(z), 3 actual λ uppers (n<256),
    L_c ≤ Λ_c and M ≥ M_*. Then list the rational predicates. Conclusion: Theorem 1.1 at
    degree n. Section 5 currently spreads this across prose.
  - (b) A trust table: before is Arb/FLINT/MPFR/GMP plus compiler plus PD-T271; after I25
    and I26 it is "two independent arithmetic implementations; no external constant".
  - (c) A supplement table for n = 41…319: nodes, leaves, #S, minimum FAR and NEAR margins,
    M and L_c. It documents margins ≥1e-3 against arithmetic radii ≤1e-14.
  - (d) One worked FAR leaf and the corner witness from the real n=199 certificate:
    M = 24, L_c = 19.697755…, FAR margin 1.48e-3, q = 69.60, g = 57.41, u′ = 1/32,
    v′ = 9/512.
  - (e) A constants ledger: an exact `Fraction` script with one line per displayed rational
    inequality of §§3–5, keyed by equation label. Audit-02 checked about 30 such links ad
    hoc, so referees can concentrate on the analysis.
  - (f) A data-availability statement naming the archive, its SHA-256 and the replay
    command. The DOI is AC's decision.
- **Distinction.** Present §5 states implications and the evidence boundary, but gives no
  premise count, margins or worked numbers (read in full).
- **Test.** The I25 author records each point where §5 or the companion did not suffice to
  re-implement (with zero allowed engine-source reads). Kill for (a): no such point and the
  editors find the proposition redundant. Items (c)–(f) still stand.
- **Cost.** LOW; (c) and (e) are scripts.
- **Priority HIGH for submission.**

### Rank 5 — I29: journal-paper figures and remarks
- **Proposed additions.**
  - (1) A proof-map figure of about one third of a page, with the trust inputs marked. One
    chain runs kernel → exact rows → square and mesh defect → κ → quadrature lemma →
    Theorem 1.2. The other runs λ = S − Δ → completed model and telescope → selected-pair
    floors → four ρ-regions plus corner squares → n ≥ 320 → finite §5 → Theorem 1.1.
  - (2) A ρ-region figure for §4 with the proved gaps 1/20000, 3/1000, 99/2500, 13/500 and
    the corner loss (A²+B²)/30. The companion has a phase diagram; the journal paper has
    none.
  - (3) A remark, labelled numerical: the remainder of Theorem 1.2 is of exact order
    log N/N² (−7/36, I27). The true localisation gap is about g = 0.5485 at the edge centres
    (I30, PD-T187), which shows how conservative the proved 1/20000 is.
  - (4) State Theorem 1.1 for n ≥ 1. λ₁ = max{1, |y| + (1−x)/2} obeys the odd rule exactly
    (§5 already proves it; consolidation-audit lines 290–301 offered this and it is still
    unadopted). n = 0 is a genuine exception: one node, λ₀ ≡ 1.
  - (5) After I26, remove both trust sentences.
- **Test.** Compile; each figure must fit within a third of a page and be readable in
  greyscale.
- **Cost.** LOW. **Priority MEDIUM.**

### Rank 6 — I30: sharp isolation constant
- **Target.** lim (Λ_c − λ_(2)(n)) = g, where λ_(2) is the largest value of λ_n outside the
  two corner mesh cells.
  - Upper bound on the gap: PD-T187 (duplicate).
  - Lower bound: OPEN. It is a variant of PD-T187's split "central envelope" and
    IDEA-318/339.
- **New route (asymptotic, non-effective).**
  - E14 handles ρ ≥ ρ0, and the S margin grows like (4u/π²)L², so only ρ ≲ C/L matters.
  - There, S_n − Λ_c ≤ o(1): the cusp is ℓ_n|α| = O(log n/n).
  - Then show uniform convergence of Δ_JK(φ) on |φ| ≤ C/L to the limiting edge integrals
    (PD-T266/268 minimum g) and to interior full-defect integrals. Their infimum must be
    shown to be ≥ g; that is the decisive new lemma.
- **Kill.**
  - MEASURED full-square scans at n = 32, 48, 64 (1/4 cell) plus local maximisation.
  - The edge-centre form dies if any interior or near-corner local maximum has a gap
    below g − 0.02 at n ≥ 48.
  - The interior route dies if a computed interior limiting defect is below g.
- **Cost.** About 30 CPU-min test, then a medium-size proof.
- **Priority LOW–MEDIUM.** It is a follow-up result, not needed for the paper.

## 4. Can the analytic onset go far below 320?

Not by the present method. Audit-02 §2.5 (reproduced by its orchestrator) shows the required
uniform shrink of every finite-error charge: 0.74–0.79 for 256, 0.52–0.56 for 200 and
0.24–0.29 for 128. Floors alone stall at 307, and Fh(n,0) < 0 for n ≤ 82.

The F campaign produced only feasibility-size uniform constants: F04 K = 120000,
F09 K = 41000, and F08 K ≤ 100 is still OPEN. These are orders of magnitude above the
measured truth, which is 480–10⁵ times smaller than the charges.

A different mechanism would need a relative error within about 2× of the measured proxy, or
degree-interval certificates. The latter are a duplicate of IDEA-337 and need the same
uniform error.

Deferred. Resume only if a journal requires a smaller computer-assisted range or a sharp
uniform relative error appears. With I25 the cost of the finite range is a few CPU-hours of
doubly verified computation.

## 5. Retained, duplicate, failed and deferred candidates

| Label (IDEA?argmax-bridge-claude-…) | Candidate | Closest prior entry | Disposition, scope, reason |
|---|---|---|---|
| I31 | Second implementation via python-flint/Arb | D23/D36 native Arb | **REJECTED: failed** as independence (same library). Retained note. |
| I32 | numpy np.sin with an assumed ≤4-ulp libm bound | I25 | **abandoned** in favour of the own Taylor sine (removes libm trust). Possible speed fallback with the stated assumption. |
| I33 | mpmath full O(n²) evaluation of every premise | I25 | **abandoned**: MEASURED 0.4 s per S point at n=41 scales to about 25 s per point at n=319, about 90 CPU-h for ~13.7k premises. Keep mpmath only for spot checks. |
| I34 | Certified interval quadrature of the H0 integral (m2-N3) | audit-02 m2-N3 | **superseded by I26**: the series route needs no quadrature. |
| I35 | Hand-only proof of κ<23/25 (margin 2.9e-4) | D08 | **deferred**: possible with K=5, but a CAS-checked rational table is simpler. |
| I36 | e1 = −(1+κ)/π², and Ñ = N − (1+κ)/(8N) absorbing the log term | I27 | **REJECTED: refuted (MEASURED)**: off by 3e-4 relative; residual drifts (§2.3). No PD-N. |
| I37 | PSLQ for e0 from 7 digits | T4 PSLQ memory | **deferred** until there are ≥25 digits (I27 kill test). |
| I38 | Lower analytic onset by recipe retuning or EM2 constants | I13, F01/F04/F08/F09 | **equivalent** to the completed E/F programme; §4. |
| I39 | Degree-interval (h=1/n) batched certificates | IDEA-337, I17 | **duplicate**; deferred with IDEA-337 (needs a uniform error within ~20× of truth). |
| I40 | Monotonicity of the gap in n (n↔n+1) | I16, audit-01 (d) | **deferred**: no cross-degree identity; same topology at 159/160/511/512 is geometry only. |
| I41 | Uniform-in-n finite-row identity for S_n(φ) (digamma form like H05) | H05, F09 | **equivalent** to the F09 first-order expansion route (feasibility constants). |
| I42 | Edge-centre gap ≤ g + o(1) | PD-T187 | **duplicate**. |
| I43 | State and prove for n = 0 | — | **abandoned**: λ₀ ≡ 1, every point maximises (genuine exception). |
| I44 | Theorem 1.1 for n ≥ 1 | consolidation-audit lines 290–301 | **duplicate** suggestion, still unadopted; folded into I29(4). |
| I45 | Same theorem for other checkerboard/Lissajous families | IDEA-206 programme, LIT-379/380 | **deferred**: out of scope; needs a new kernel identity per family. |
| I46 | Cross-degree tree templates (I08) | I08 | **moot**: all degrees closed. Template statistics belong in I28(c). |

No candidate creates a PD-N. "Failed" and "refuted" apply only to the stated mechanism and
scope.

## 6. Recommended Codex sequence (bounded; nothing launched by Claude)

1. **I26 paper note** (minutes): the consumer grep plus a committed `Fraction` checker.
   Then delete the trust sentences (I29(5)).
2. **I25 pilot** (≤60 CPU-min, MEASURED/ENCLOSED receipt): from-paper checker on
   41, 199, 238 and 511 with corruption controls. Then a preregistered all-560 run in the
   sandbox, with the archive retrieved by its pinned SHA.
3. **I28/I29 drafting**: proposition, trust table, certificate table, worked n=199 leaf,
   figures, n≥1 and the sharpness remark.
4. **I27 kill test** (≤30 CPU-min).
5. **I30 scans** (≤30 CPU-min). Proof work only with a fresh release.

**What not to do.**
- Do not treat MEASURED agreement as a proof before the full I25 checker is reviewed.
- Do not change frozen engine, evidence or proof bytes.
- Do not drop PD-T271 from the records until I26 is reviewed.
- Do not claim the −7/36 law or g-sharpness as theorems.

## 7. Execution record

All runs were in `i-code/` (scratch), `PYTHONPATH=../pylib`; every command exited 0 except
two scripting errors that were fixed and rerun (a missing `PYTHONPATH`, and an mpmath
`Fraction` conversion).

```
python3 check_small.py ; python3 check_certs.py ; python3 rig_S.py
PYTHONPATH=../pylib python3 timing_and_mp.py
for K in 2 3 4 5 6 8; do python3 kappa_rational.py $K 60; done; python3 kappa_rational.py 6 200
PYTHONPATH=../pylib python3 corner_next.py ; PYTHONPATH=../pylib python3 corner_next2.py
PYTHONPATH=../pylib python3 corner_next2.py 300 600 1200 2400 4800 9600 12800 > corner_next2b.txt
python3 gap_probe.py 8 9 16 17 32 33 ; python3 gap_probe2.py 32 64 65 128 256
python3 gap_full.py 16 6 ; python3 gap_full.py 17 6
```

Script hashes (sha256[:16]):

| Script | sha |
|---|---|
| indep_S | 32357817afd2369f |
| rig_S | 393ed0606bfb6e90 |
| check_certs | 38c4fefd70972c25 |
| check_small | 7ee4a218d06012d0 |
| kappa_rational | 0e7e1c0c6b2de8ce |
| corner_next | ead728ff0f9fce7b |
| corner_next2 | 58756191d62604e6 |
| gap_full | 331134eaf63b9a7f |
| gap_probe | 9c7319ca5ae1abf3 |
| gap_probe2 | e34d151e388a23f1 |
| timing_and_mp | 7c5a766e2fe628ea |

Outputs: `corner_next_out.json`, `corner_next2_out.json` (overwritten by the 300–12800 run;
the 100–6401 values are quoted in §2.3 from the transcript) and `corner_next2b.txt`.

Total CPU ≈ 3.5 min (cap 25). Inputs from the repository were read-only: the four committed
certificates and the paper formulas. No archive, native, Syvert, compiler or degree job ran.
