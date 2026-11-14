# G-assembly: substantive Claude audit of the all-degree argmax assembly (handoff 28, brief §1 bullets 2–3)

Auditor: Claude Opus 5.5 (`claude-opus-5-5`), xhigh, independent mathematical subagent. Developer of all audited work:
Codex. Role: auditor only; no Git state change and no repository edit. Outputs: this file and `g-assembly-code/`
beside it. Labels: **[D]** own derivation, **[E]** own execution, **[I]** inspection/reading only.

- Candidate: branch `codex/padua-argmax-bridge-20261105`, head `f366535e1fa4ede566cb83bdc554220c12b307cf` (= HEAD of
  the checkout).
- Rules read at that head: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md`, then
  `claude-audit-brief-20261108.md`.
- Novelty: no candidate generation or novelty claim is audited here; the full `state/IDEAS.md` read is omitted for
  that reason (CLAUDE_ROLES). §10 lists my own proof ideas as suggestions, not registered candidates.

## 1. Verdict

**Mathematics of the assembly: SUPPORTED, no BLOCKING finding.** I reconstructed the degree partition, the PD-T210
Bernstein implication, the PD-T101 cardinal normalization, the PD-T364 chart/defect identities and the whole D32
finite-phase implication (Peano vector bound, D14/D19 norms, FAR/NEAR guards, squared-variable corner descent) at the
level needed to see that a verified certificate implies `lambda_n<Lambda_c` off the two parity-correct corners at its
exact degree. Every degree 41..319 uses only premises whose degree hypotheses hold (§3.4). Independent reruns written
from the theory statements reproduce all of 2..17 and 24 and re-verify the committed phase receipts (§4–§6).

**One MAJOR finding (G-1):** the vertex enclosures `W_z` of the phase certificates are not plain interval sums: S
comes from the C02/D23 row-cotangent truncation with a proved analytic remainder, and actual lambda from the D06/C11
row reductions. These accepted theorems are mathematical premises of every degree 41..319, but they are absent from
G01's dependency/trust list and from the paper's premises and evidence boundary. Four MINOR findings (G-2 to G-5),
one EDITORIAL (G-6) and three NOTEs (G-7 to G-9) follow in §9; none affects validity. The P1–P4 chronology findings are
preserved, unwaived (§8). Manuscript builds and prose are outside this assignment and were not done.

## 2. Scope actually covered

Read fully: G01; E14-assembly320 (incl. addenda); native-finite-range; small-degree-unification; PD-T101; PD-T210;
PD-T364 (phase-structure); D32; final hybrid SPEC; paper `certification-unified.tex`, `localization-unified.tex`,
`preliminaries.tex`, theorem part of `introduction.tex`, comparison lines 400–468 (kappa input); audit-02-interim,
response-02, audit-02-record-response; independent-checks-compact-return-math. Read in part: D23 (statement),
D29-radius41, C02 (statement), D06 (statement), compact-return, cold-storage entry, PD-T271 (statement),
consolidation-audit (small-degree part), paper/review.md, statements of PD-T162/166/169/174/177/181/209/214/246, E15
header. Grep-level: the other reviews named in the assignment (read after my reconstruction).

## 3. Reconstruction of the logical assembly

### 3.1 Degree partition [D]
{2..40} ∪ {41..319} ∪ {n>=320} is every integer n>=2, disjointly. 2..40: historical records PD-T209 (2),
PD-T162/166/169/174/177 (3..7), PD-T181 (8), PD-T214 (9..16), PD-T246 (17..32), native-finite-range (33..40); each
states the exact two-point equality set [I] (I checked the closed forms for n=3..7 against my Arb corner values [E]).
41..319: the compact return, 279 degrees + control 511 = 280 pairs; 273 residual + controls 41,42,63,64,159,160 [D].
n>=320: E14.

### 3.2 Common normalization [D]
PD-T101: discrete orthogonality of `Q_M` (trapezoid exactness for `cos rt`, 1<=r<=2M-1), the checkerboard alternating
part vanishes because `p+r=n, q+s=n+1` contradicts total degree <=2n, Gram `h_p^(n) h_q^(n+1)`, inverse coefficients
`nu_p nu_q` except `(n,0)` -> 1 (since `h_n^(n)=h_0^(n+1)=1`), and `V H^-1 V^T = W^-1` gives the cardinals. This is
exactly "exceptional highest first-coordinate coefficient ONE" (the records' "halved (n,0) mode" means the same 2->1).
Parity reflections `j->n-j` (even n) / `k->n+1-k` (odd n) preserve parity and weights, so the two designated corners
have equal values; both are nonnodes (`n+(n+1)` odd; `0+(n+1)` odd for even n; `n+0` odd for odd n).

### 3.3 Degrees 2..40: PD-T210 implication [D]
On a leaf, `lambda <= sum_ij A_ij B_i(s)B_j(t)` with `A_ij=sum_l|c_l,ij|` (triangle inequality, nonnegative partition
of unity). Bound leaf: all `A_ij<C_-<=C`, so `lambda<C`. Corner leaf: the vertex coefficient equals `L_l(e)`, so
`A_vertex=C` exactly; all others `<C_-`. Then `lambda <= C - (C-D)(1-w_*)` with `w_*=(1-s)^n(1-t)^n` (or the analogous
endpoint product), `w_*=1` only at the vertex since n>=1. Closed children cover shared edges; a leaf containing both
designated corners cannot pass (the second vertex sum is `C`, not `<C_-`). Hence max = C with equality exactly at the
designated pair. No collision issue arises (polynomials). The paper's §5.1 text is a faithful statement of this.

### 3.4 Degrees 41..319: the D32 phase implication [D]
- **Charts.** In every mesh cell the two odd vertices have scaled L1 distances summing to 2, so one is <=1: admissible
  charts `|alpha|+|beta|<=pi` cover the closed square including ties/edges. `lambda=S-Delta_JK`,
  `Delta>=max(Q_h,Q_v)>=0` from (1)–(4) of PD-T364 (I re-derived the endpoint-residue identity and the odd-board
  translation). S is even in each phase and invariant under even-lattice translation, so `(|alpha|,|beta|)/pi` lies in
  T and the global real-phase sup is attained on T.
- **Peano vector bound.** For fixed signs, each signed board sum is a trigonometric polynomial of degree <=n in `pi
  a/n` and `pi b/m`; Bernstein gives `|f_aa|<=pi^2 M*`, `|f_bb|<=pi^2 k^2 M*` with `M*` the real-phase sup. With `f -
  I_aI_b f=(f-I_a f)+I_a(f-I_b f)` this yields (8) of D32 / (cert:phase-bound) with `theta_B=(p_hi^2/8)[da^2+k^2
  db^2]`.
- **Norms.** D19: a leaf containing the maximizer gives `M*<=V_B+theta_B M*`, so `M*<=max V_B/(1-theta_B)` when every
  `theta_B<1` and every leaf is numerical. D14: ten quarter squares, folded vertices in the 15-point grid (13
  canonical keys), and `1/(1-(22/7)^2/64)=784/663` exactly. An f leaf supplies no `V_B`; the engine's GRID-only
  policy with f leaves is therefore a valid sufficient choice (I-3 shows TREE would also remain valid).
- **Leaf rules.** FAR `U<L`; NEAR needs `2p_hi*high<=1` (whole leaf actual-near), then `U-delta(r_B)<L` with
  `r_B=min(1/2,p_hi(a_h+b_h))>=rho`. A leaf containing the origin can never be FAR (`U>=S(0,0)=Lambda_c>=L`), so the
  corner premise is always invoked there. SPLIT is never needed with `V_N=V_F=U` (then it is FAR).
- **Floors are uniform over rho<=r** (C02 (1)–(4), D29-radius41 (1)–(2)) [I], so no monotonicity in r is required; the
  `max{tier, min(cap,B_n)}` clamp equals the class-wise minimum [E: `floor_consts.py`]. I verified exactly
  `E_64-1/64`, `E_160-1/32`, the `B_n` coefficient identities and `(7/8)(29/492)^2>1/512` [E].
- **Corner descent (41..255).** Cardinals are even in each inward phase; for even f of type sigma, `g(u)=f(sqrt(2u))`
  has `g''(u)=int_0^1 int_0^1 t^2 f''''(rt sqrt(2u)) dr dt` (I re-derived it via `A f''-f'=int_0^A r f'''`), so
  `|g''|<=sigma^4 M/3` (vector form via signed sums). Physical `(-cos(A/n),-cos(B/m))` stays in the square for all
  real A,B, so the phase M bounds every signed cardinal sum. Vertex losses `q u', q v', q(u'+v')` interpolate to
  `(q/pi^2)(u+v)`, giving (14) with the essential `pi^4` factor. `pi/4, 3pi/16 > 1/2`. The receipts query exactly
  `1/(4n)` and `3/(16(n+1))` turns [E].
- **Equality set.** Only the two actual corner origins survive; node corners have value 1 and lie at nonzero odd-chart
  phases.

| Degrees | Floor premise (domain) | Norm | Corner | Analytic far |
|---|---|---|---|---|
| 41–63 | D29-radius41 (n>=41) | TREE or GRID (all n>=2) | 3 points + D08 (all n>=2; D07 source 2..2048) | none |
| 64–159 | C02 tier 1/64 (n>=64) | same | same | none |
| 160–191 | C02 tier 1/32 (n>=160) | same | same | none |
| 192–255 | C02 tier 1/32 | GRID if any f leaf | same | E15 (n>=192, whole-cell rho>=pi/2) |
| 256–319 | C02 tier 1/32 | GRID if any f leaf | E12 (n>=256) | E15 |

Every hypothesis holds on its range. **161–191** (and 41–191 generally) are certified by the model-free D32 route:
numerical FAR/NEAR leaves, C02's n>=160 floor, D14/D19 norm and the three-actual-point corner. Their lack of E12/E15
shortcuts is not a gap (response-02 PA3 states the same). D23's uniform 2e-7 corollary is only for n>=160; its general
formula (2) holds for all n>=2 and SPEC says actual widths are charged below 160 [I] (my §6 direct sums support this
at 41, 199, 238).

### 3.5 n>=320 (E14 / paper §4) [D, arithmetic only]
The closed cover is complete: noncorner rho<=1/2 (near exclusion), noncorner 1/2..3/5 (annulus), all centers 3/5..1
and 1..pi (S bounds), corner charts rho<=3/5 inside `[0,pi/4]^2` (corner256). I re-checked the displayed closing
arithmetic: radial maximum `e,f,g` for both lines (`72/59`, `3029/4720`, `3/5900`; `g<1/4000` holds with 0.3% slack),
`34161^2<32*8233*4431` (it is exactly the completed square at `1/20000`), `P(1/2)=607/20000`, `P(3/5)=-99/2500`, the
1/30 descent (`(16/pi^2)(49/2000)>49/1250`) and `r_U=2/125>pi^4/6144`. The underlying constants (T, ebar, C4, k's,
M(n)) were not re-derived (§11).

### 3.6 "Neither a finite search nor numerical agreement supplies this argument"
Accurate: each finite degree is a complete closed cover with strict predicates, implied by proved reductions; no
sampling or fit is used. The numerical content is rigorous outward enclosures, whose trust base is G-1/G-4. For 277 of
279 degrees those enclosures were produced and fresh-verified only on Syvert (disclosed in G01).

## 4. Independent small-degree verification (task 2)

Own code `g-assembly-code/bern_indep.py`, written from PD-T101/PD-T210 only; it imports no repository code.
Arithmetic: python-flint 0.9.0 (Arb balls, 256 bits) for every `cos(p j pi/n)`, `cos(q k pi/(n+1))` (exact 0, ±1 at
special angles); exact `fmpq` for the Bernstein coefficients of each `T_p` on each dyadic box (composition, then
`C(i,r)/C(n,r)`); one `arb_mat` product gives all cardinals' tensor coefficients, with the `(n,0)` mode reduced from 2
to 1; strict Arb `<` (certain-only) against the directly evaluated corner ball. Own closed midpoint DFS, x first,
depth cap 14; exact covered area 4. Corner values agree to 25 digits with the separate PD-T101 product-U corner
formula (2..16) [E].

| n | bound/corner leaves | depth | CPU s | `Lambda_c(n)` (Arb) |
|---|---|---|---|---|
| 2, 3 | 2/2 | 2 | <0.01 | 3; 3.7761423749 |
| 4, 5 | 14/2 | 4 | 0.04 | 4.4097254355; 4.9478057490 |
| 6, 7, 8 | 18/2, 24/2, 32/2 | 5, 6, 6 | 0.6 | 5.4174994301; 5.8356577106; 6.2134596469 |
| 9..14 | 40, 46, 48, 52, 54, 56 /2 | 6–8 | 15.7 | e.g. n9 6.5587136027 |
| 15, 16 | 80/2, 94/2 | 8 | 23.3 | 8.1866320759; 8.4074362847 |
| 17 | 104/2 | 8 | 22.1 | 8.6179478250 |
| 24 | 152/2 | 10 | 155.9 | 9.8725125358 |

Every degree 2..17 and 24 is **independently certified** with the exact two-corner equality set. My leaf counts and
depths equal the repository's witnesses exactly (table in small-degree-unification; n17/24 stats in the PD-T246
certificates). The 2..7 values equal the closed forms of PD-T209/162/166/169/174/177. **Replays** of repository
certificate paths (data only, my arithmetic, my prefix-completeness check): fresh common witness n16 (94/2), reused
PD-T246 witnesses n17 (104/2) and **n32** (280/2, depth 11, 596 CPU s) all pass with complete partitions.
**Controls:** wrong-parity corners at n=4 fail (incomplete at depth 10); sympy exact Vandermonde inversion equals the
PD-T101 formula at n=1,2,3 (3, 6, 10 cardinals). Not run: 33..40 (estimated from my n=32 replay, roughly 0.5–1
CPU-hour each at 37–40); I did not run the repository checker. Interpretation: the "one Bernstein scheme for 2..40" is
sound as mathematics; at 2..17, 24, 32 it now has a second, independently written arithmetic implementation.

## 5. Degree one
The paper (§5.1 end) and small-degree-unification state nodes `(1,1),(1,-1),(-1,0)`, cardinals `(1+x±2y)/4`,
`(1-x)/2`, `lambda_1=max{1,|y|+(1-x)/2}`, maximum 2 only at `(-1,±1)`; the main theorem keeps n>=2. **Correct** [D,
E]: `|a+b|+|a-b|=2max(|a|,|b|)` with `a=1+x>=0`; sympy Vandermonde inversion reproduces the three cardinals and the
PD-T101 formula at n=1 exactly; the identity holds exactly at 409 rational points; values 2,2,1,1 at the four corners.
The consolidation audit's split-at-y=0 Bernstein witness (vertex sums 1,1,2,1) also checks.

## 6. Phase receipts: independent rational layer and direct sums

**Rational layer** (`phase_rational_indep.py`, exact Fractions, from the D32/D14/D19/D29/C02/D08/E12/E15 statements,
not importing `checker.py`): tree grammar and full token use, closed cover area 1, `OUTSIDE` iff `al+bl>1`, canonical
folding, presence of all 13 grid and all vertex keys, GRID (`M>=784V_E/663`) or TREE (`M>=max V/(1-theta)`, no f
leaf), Peano uppers, FAR/whole-NEAR with the degree tier floor, f-leaf guard (`n>=192`, `1/2<=al+bl<=1`), three-point
corner with exact physical turns and `q>M p_hi^4 max(u',k^4v')/6`, or no actual rows from 256 [E].

| Receipt (committed) | Norm | FAR/NEAR/f/outside | Corner | Result |
|---|---|---|---|---|
| primary+fresh 41 | TREE 13 (grid 14.21) | 43/5/0/3 | 3 points, threshold 190333/28812 | pass |
| primary+fresh 199 | GRID 24 | 17/6/3/0 | 3 points, 29282/2401 | pass |
| primary+fresh 238 | GRID 25 | 17/6/3/0 | 3 points, 366025/28812 | pass |
| primary+fresh 511 | GRID 30 | 17/6/3/0 | E12 branch | pass |

My q values and thresholds equal the receipts' own fields.

**Direct finite sums** (`direct_sum_validate.py`, Arb 160 bits): I recomputed every retained S key (64 at n41, 45 at
n199/n238), the three actual lambda points and `S(0,0)=Lambda_c` straight from PD-T364 (4) and (1), with exact
detection of `z=l*pi` collisions, using none of D23/C02/C06/N5/D06/C11 or engine code. Every native S upper is
strictly above my enclosure except at key `(0,1)`, where `S=1` exactly and the native upper is exactly `1.0` (a valid
tight upper; diagnostic `diag_keys.py`); native lambda uppers exceed my values by 3–6e-12 (n41) and about 1e-14
(n199/238); native origin lowers are below `Lambda_c`. Substituting **my** uppers and lower, all predicates still
pass. So degrees 41, 199 and 238 are re-certified by an evaluation route independent of the row-truncation theorems
and engine code (trusting only Arb/FLINT as a library and PD-T364). 511 was not done (about 9 CPU-min in Python).

## 7. F-series and trusted dependencies (tasks 3–4)

**F-series [E, grep].** G01 mentions F01–F10 only (line 111) to say they are separate supports and unused. No F
reference occurs in any paper section, `main.tex` or the bibliography. No file of the G01 chain (E12, E14*, E15, D08,
D14, D19, D29, D32, hybrid SPEC/engine sources) cites an F file. Only `H-sharp-corner-expansion.md:55` cites F03
(routine identities), outside this scope. **Confirmed: the F-series are not premises of G01, and the paper never cites
them.**

**Trust lists [I].** G01 (lines 75–79) names PD-T271, Arb/GMP/MPFR, the captured runtime, finite-polynomial collision
formulas, compiler/native interfaces and the exact-rational checker. It honestly scopes Syvert-only primary/fresh
execution, the two sampled native replays, the lack of an independent arithmetic implementation and selective
retention. Missing: the evaluator theorems (G-1); FLINT, the Python interpreter/parsing and the LP64/binary64
conventions (G-4). PD-T271 enters every degree 256..319 (E12) and 192..255 only through f leaves (SPEC degree table;
receipts 199/238 carry f leaves). The paper's evidence paragraph (cert lines 245–265) is honest about the production
machine, sampled replays and retention. It omits G-1, the 2..40 trust base (G-4) and PD-T271's entry into the analytic
leaves (G-5).

**PD-T271 input rechecked independently [E].** The paper uses only (uc:coarse-input) `9/10<kappa<23/25`,
`C_*<1847/1000`. I re-derived the series (uc:kappa-series): the cotangent partial fraction gives `a_p`, and the odd-l
reciprocal expansion gives `b_q`, with `|c_k|<=4^-k(10/9+4/5)<2*4^-k`. `kappa_rational.py` uses exact rational
intervals only: Machin pi, Bernoulli-exact `zeta(2r)`, convex-tail `zeta(odd)`, the log series and
`H_K-log(K+1)<gamma<H_K-log(K+1/2)`; no Arb is used. Results: `kappa in [0.9197101183789, 0.9197101183963]`,
`C_*<=1.84616032320`, and `C_*>4383/2420`. All three paper/E14 numbers hold and agree with PD-T271's decimals (1.3 CPU
s).

## 8. Audit-02 dispositions (task 5)

- **P1–P4:** preserved and unwaived in response-02 (Chronology), E14-assembly320 addenda, SPEC/SOURCE, LOG (the G01
  adoption entry, about line 1840) and compact-return-math. No current record waives or relabels them. G01 and the
  paper rightly do not repeat them ("disclose once"). Their AC disposition is still required before readiness.
- **Math-relevant A-items:** each appended addendum exists. The preserved accepted prefixes rehash correctly [E]: E14
  11628 B `b348ec55…`, E12 9921 B `586c4e07…`, E15 13855 B `b420adbd…`, E08-obstruction 6353 B `cbaa95e1…`,
  E12-obstruction 5627 B `c82eed5a…`. A-3: the E14 node paragraph now names D08/PD-T271 (and is redundant; rho=pi lies
  in the outer domain). A-5: E12 lines 263–272 tabulate four components, each n>=32 on closed rho<=1. A-6: PD-T271 is
  cited in both obstruction addenda. A-4/A-9: the SPEC addendum and degree table match the receipts (41 model-free;
  199/238 f leaves; 511 E12). A-1/A-2: dated pointers and hash labels are present. A-11 is accepted (size only).
- **PA3's mathematical claim** that 161–191 have a valid numerical route matches §3.4. PA1/PA2/PA4/A-7/8/10/12 are
  operational and not re-checked here.
- **Coverage added beyond audit-02:** audit-02 listed PD-T101/PD-T364, D08 squared-Peano and the full D32/D14/D19
  proofs as not re-derived. This audit re-derives them (§3).

## 9. Findings

**G-1 — MAJOR — vertex-evaluator theorems missing from the stated premises.**
- *Locations.* G01 lines 51–53 ("outward point bounds") and 75–79 (trusted list). Paper `certification-unified.tex`:
  17–34 (`W_z>=F(z)` is assumed), 110–141, and 245–253 ("Native outward endpoints come from the frozen
  Arb/FLINT/MPFR/GMP implementation…"). `paper/README.md` 58–60 (source-dependency list).
- *Reason.* SPEC 109–118 and FREEZE rows (`post_audit_D23_backend/point.cpp`,
  `post_audit_D07_fourcopy_point/point.cpp`, `cheap_rows_C11/point.cpp`) show how the enclosures are made. Each S
  vertex upper is computed from the exact C02 row decomposition with a truncated smooth residual, harmonic
  prefix/order formulas and endpoint series. It adds the proved remainder `E_n(J,K,L,W,a)` of D23 (2), which rests on
  C02, N5 and C06. Actual lambda uppers use the D06 four-copy row reduction and C11 rows. These are accepted
  *mathematical* theorems, and every degree 41..319 depends on them. The compact-return math review already lists "the
  accepted D23/D07/C11 sources" as trusted (its lines 172–175). G01 and both manuscripts do not; the paper presents
  the endpoints as pure library arithmetic.
- *Impact.* The theorem's stated premises and computational scope are incomplete. A referee or re-implementer would
  not learn that a truncation theorem is part of the proof. The result itself stands: the theorems are accepted, and
  §6 direct sums at 41/199/238 confirm the native uppers.
- *Fix.* (a) G01: add "S vertex enclosures: D23 (2) with C02/N5/C06; actual lambda: D06 and C11 rows (accepted reviews
  …)". (b) Paper §5: add a short "vertex enclosures" paragraph or lemma stating the exact row identity and the
  explicit remainder bound, proved in the companion (or cited). Name it in the evidence boundary and in README's
  dependency list. (c) Alternatively adopt I-1, after which only PD-T364 and interval arithmetic are needed.

**G-2 — MINOR — G01's registry claim for 33..40.**
- *Location.* G01 lines 33–38, "Their canonical links and completed audits remain in PROOF_STATUS.md".
- *Reason.* `native-finite-range.md` (33..40, provisional `PD-T?argmax-bridge-codex-F1`) has no PROOF_STATUS row. Its
  Claude audit is this topic's audit-01 (X4 n37 replay, assembly review), yet its own line 25 still says that audit is
  "pending".
- *Impact.* Record accuracy only.
- *Fix.* "2..32: PROOF_STATUS; 33..40: native-finite-range, accepted in audit-01, registration at PR preparation". Add
  a dated pointer in native-finite-range.

**G-3 — MINOR — floor citation.** G01 lines 51–53 credit the "D32/D29 … exact defect floors" for 41..319. D29-radius41
covers only 41..63; 64..319 (245 of 279 degrees) use C02's n>=64 and n>=160 tiers (D32 table; SPEC line 106). *Fix:*
name C02 and give the tier map of §3.4.

**G-4 — MINOR — trust-base completeness.**
- *G01 (lines 77–79):* omits FLINT (Arb's library; SPEC line 123 and the paper name it), the Python interpreter/JSON
  parsing and the LP64/binary64-to-rational convention.
- *Paper:* its 2..40 paragraph (cert lines 88–100) gives no trust base (C++/GMP checker, compiler, Python driver),
  while the phase paragraph does.
- *Fix:* one sentence each.

**G-5 — MINOR — PD-T271 in the finite certificates is not stated where it is used.** The introduction (lines 102–104)
attributes the constant enclosure to "the analytic argument". Section 5 applies (ul:corner256) on 256..319 and
(ul:far192) on f leaves at 192..319, yet its evidence paragraph lists only arithmetic, compiler and interfaces. *Fix:*
in §5, add "the analytic leaves and corner estimate inherit (uc:coarse-input)", or remove the dependency by I-2.

**G-6 — EDITORIAL.**
- (a) Cert line 57 says "exact de Casteljau averages"; the checker rounds integer averages outward (PD-T210). Say
  "rounded outward".
- (b) G01 line 27 still says "prescribed" fresh checks. Use "executed and independently reviewed", as
  compact-return-math suggested.
- (c) "Halved (n,0) mode" (small-degree-unification 24, PD-T246) and "coefficient ONE" mean the same 2→1. Use one
  phrase.

**G-7 — NOTE — SPLIT is dead.** With `V_N=V_F=U`, SPLIT implies FAR. All receipts I checked use only FAR/NEAR/f, and
audit-02 T1 calls SPLIT unreachable. Paper lines 171–195 could state FAR and whole-leaf NEAR only.

**G-8 — NOTE (cross-scope, evidence).**
- *Limitation.* The 560 essential receipts of the unsampled 277 degrees are neither in Git nor retrievable from a
  fresh cloud checkout: `local-output/` is absent, and cold-storage.json records "external cold delivery/retrieval
  unverified". So I could not run §6 on them, and no fresh independent re-check of G01 is possible from the repository
  alone. G01 discloses this.
- *Size.* Each primary is about 5.7 KB.
- *Recommendation (for the evidence auditor and AC):* make that set durably retrievable before readiness.

**G-9 — NOTE.** The degree-one statements are correct (§5), and the n>=2 scope agrees across G01, the paper and
small-degree-unification.

## 10. Own proof ideas (task 6)

- **I-1. Direct finite-sum vertex enclosures.** By PD-T364 (4), S is an exact finite sum of `2n(n+1)` terms, so no
  truncation is needed.
  - *Cost.* For n<=319 that is at most about 2e5 kernel calls per vertex, and about 1e7 per degree. Arb in C should take
    seconds per degree (estimate, not run); my Python prototype took about 1.7 s per vertex at n=199.
  - *Demonstrated (§6):* this route re-certifies 41, 199 and 238.
  - *Proposal:* re-validate every retained key of all 280 receipts this way. That would remove D23/C02/C06/N5/D06/C11
    from the trusted base of 41..319 (G-1), and it is an independent evaluation path. It needs the essential receipts
    (G-8).
- **I-2. Elementary proof of the only PD-T271 input the paper uses.**
  - *Margin.* `kappa<23/25` has margin 2.9e-4. The tail bound `8/(3(K+2)4^(K+1))` is already 9.3e-5 at K=5. So six
    coefficients `c_0..c_5` (Bernoulli `zeta(2..10)`, odd `zeta(3..13)` with simple tails) together with `gamma` and
    `log(8/pi)` brackets give a hand-checkable lemma. My exact-rational run shows it closes.
  - *Gain.* This would make the analytic tail, E12 and E15 free of computer-assisted constants. The caveat: confirm
    that no E-record needs more PD-T271 digits than (uc:coarse-input). The paper's derivation and audit-02's M2 note
    suggest none does.
- **I-3. TREE norm remains valid with f leaves.** On an f leaf, `S<Lambda_c-3/100<Lambda_c=S(0,0)<=M*`, so a global
  maximizer on T never lies in an f leaf. It lies in a numeric leaf, and therefore `M*<=max_numeric V_B/(1-theta_B)`
  holds even when f leaves are present. The SPEC's rationale for forcing GRID ("numerical leaves alone need not
  contain a global maximizing point") is overly conservative. The current GRID policy is valid. Allowing TREE with f
  leaves is an optional tightening.
- **I-4. Simplify the exposition** by dropping SPLIT and the proxies (G-7). The far proxy is then needed only for FAR.
- **I-5. Second implementation for 2..40.** My Arb-based implementation could be adopted, under the workflow, as a
  second, independently written replay record for the common scheme. To extend it to 33..40, vectorize the
  absolute-sum loop.

## 11. Execution record, coverage and limits

Scratch directory `A` = this file's directory. Python 3.13.18. I installed `pip install --target A/pylib mpmath sympy
python-flint` (exit 0; mpmath 1.3.0, sympy 1.14.0, python-flint 0.9.0; 5.9 s). Exits: all 0 except the intentional
control (1). CPU is user time.

| Command (in `A/g-assembly-code`, `PYTHONPATH=A/pylib`) | CPU s | Outcome |
|---|---|---|
| `python3 bern_indep.py N`, N=2..16 (loop) | 40.6 | all complete; table §4 |
| `python3 bern_indep.py 4 --wrong-parity --maxdepth 10` | 0.1 | exit 1, incomplete (control) |
| `python3 bern_indep.py 17` / `24` | 22.1 / 155.9 | complete 104/2, 152/2 |
| `python3 bern_indep.py N --cert …/nN.json.gz`, N=16, 17, 32 | 7.5 / 11.3 / 596.4 | complete replays |
| `python3 exact_checks.py` (run twice; first had a float-weight leak in my own script, fixed) | 8.5 | Vandermonde n1–3 equal; n1 identity; corner values |
| `python3 -I phase_rational_indep.py` on 8 receipts | 0.1 | all pass |
| `python3 direct_sum_validate.py` on primaries 41/199/238 | 186.7 | predicates pass with own enclosures |
| `python3 diag_keys.py` (41; 199, 238) | 4.8 + 204.2 | only tie `(0,1)`, S=1 exactly |
| `python3 kappa_rational.py` | 1.3 | coarse PD-T271 input holds |
| `python3 -I floor_consts.py` | 0.1 | floor constants exact |

Total is about 1250 CPU s (about 21 CPU-min), within the 40-min cap. Script SHA-256 prefixes: `bern_indep.py`
8ea4dd26, `phase_rational_indep.py` 52fbe070, `direct_sum_validate.py` 0c1572a6, `kappa_rational.py` da4f152f,
`exact_checks.py` 2e5d9b0b. Outputs are the `*.json` and `*.time` files beside them. Repository inputs were read in
place and never modified.

**Not re-derived (honest limits).**
- *n>=320:* the E14 component proofs and constants (halfnear320, outer320, annular320, E13 geometry, E08 CEphi and
  origin, E09/E14 signed T, E10/E11 model, E07 H, D37/E04/E02 rows). I checked only the closing arithmetic in §3.5.
- *E12 and E15:* the E12 interior (`delta_A`, `delta_D`, the D27 adapter, M(n)) and the E15 allowances.
- *PD-T271:* the t4-01/t4-02 proofs. I rechecked only the coarse numbers.
- *Floors:* the C02/D29 selected-pair geometry. I checked only the displayed constants and clamps.
- *Evaluator theorems:* D23 (2) and the C02/N5/C06/D06/C11 row theorems.
- *Code and execution:* the correctness of the native kernels and of the hybrid producer/checker/pack code, and every
  Syvert execution.
- *Finite degrees:* 33..40 and degrees 18..23 and 25..31 were not replayed; the historical proofs of 3..8 were
  compared by value only.
- *Manuscripts:* the comparison section beyond lines 400–468, and prose or editorial quality (another agent's scope).
