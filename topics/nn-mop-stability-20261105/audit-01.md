# Audit 01 — independent Claude audit of the NN MOP stability campaign

- Auditor: Claude, Opus 5.5, effort xhigh, as handoff02 requires. Role: independent mathematical auditor and topic orchestrator. I developed none of the audited claims or code. The model and effort follow the WORKFLOW row for an adversarial audit with novel mechanisms and negative claims.
- Date: 2026-11-06 (UTC).
- Rules: AGENTS.md, agents/WORKFLOW.md and agents/claude/CLAUDE_ROLES.md were read at candidate head `680dca3690f5a7ef1fc1ccf1ebad5a463b408d59`. Current main `be9a8318150204711d5446d2ea26284cf1ed0819` (PR #29: proportionate audit and records) was then merged at `67248cec2915a722dc9715a4f091fc919c495375`. That merge changes rules, templates and an unrelated topic, and no file of this topic. Those rules govern this report and the next steps.
- Audited scientific candidate: `ff783d59587100ab291cb83d690ef27a09f0f154`. Between it and `67248ce`, this topic differs only in handoffs/01-work.md (status line) and handoffs/02-audit.md. Every audited theory, code and evidence file is therefore byte-identical to the candidate.
- **Verdict: FINDINGS. Stage → WORK.**
  - **BLOCKING:** none. Every claimed PROVED, MEASURED, OPEN and BLOCKED status within the declared scopes is supported.
  - **MAJOR:** four findings (M1–M4) must be fixed before PR.
  - **Material changes:** M1–M4 change proof text, measured values or wording, evidence and candidate records. Under WORKFLOW they are material, so the response returns to a focused re-audit of those changes only.
  - **MINOR:** the MINOR items may be fixed together with them and confirmed by diff.

## Method and coverage

I audited priority 1 myself: the lower bound, the proximity theorem, the exact coefficients, and the induced-norm convention. Five independent Claude subagents (Opus, xhigh) each audited one disjoint scope:
- A: priority 2;
- B: priorities 3–4;
- C: priorities 5–7;
- D: priorities 8–10;
- E: novelty, status and records, including the complete `state/IDEAS.md`.

The subagents changed no Git state. Each reran developer commands and wrote independent code from the PD-T286 definitions. Their checker scripts are committed under [audit-01/](audit-01/README.md), with commands and results. Raw outputs stayed in local scratch storage. They are regenerable, and none is claimed as archived. Reading developer output is described as review below, never as a rerun.

The environment differs from the developer's: Python 3.13.18, NumPy 2.5.3, SciPy 1.18.1, mpmath 1.4.1. The developer used Python 3.12.14 and mpmath 1.3.0.

Novelty coverage: subagent E read `state/IDEAS.md` in full at the candidate (1031 lines, 261,705 bytes, in 13 consecutive complete chunks). That read covers every obstruction and disposition table, all seven topic novelty-gate files, both candidate files, plan/gates/rounds, and the PD-T286–290, PD-N100, PD-N118 and PD-T337 records. It also covers LIT-112/113/119/347/348/365/562–568.

### Audited theory hashes (SHA-256 prefixes at `ff783d5`)

| File | SHA-256 |
| --- | --- |
| theory/conditioning-lower-krawtchouk.md | `9047c95c8bc8b6ca…` (= final freeze in attempts/D1-hard.md) |
| theory/conditioning-lower-proximity.md | `c8939f19ad9f3504…` (= final freeze) |
| theory/conditioning-local.md | `64374b2120a2c269…` |
| theory/conditioning-krawtchouk-bound.md | `2b61bf54ab2e7507…` |
| theory/conditioning-normality-certificate.md | `6692f54ea21b77eb…` |
| theory/conditioning-hahn-normality-finite.md | `eadbb94053a564a4…` |
| theory/conditioning-measurements.md | `d48e69b27ff4b970…` |
| theory/d2-stage-isolation.md | `fe8f1ba5c0e4f182…` |
| theory/d2-path-diagnostic.md | `afb456df6ebcc5f9…` |
| theory/native-measurements.md | `89312d58aa3699f7…` |
| theory/backward-local-manifold.md | `d9cef81be5e0fa1f…` |
| theory/backward-dyadic-obstruction.md | `ee0130cc506d96ef…` |
| theory/backward-projection-measurements.md | `a8ff5c650e3afdc6…` |
| theory/integrable-christoffel.md | `896077bc42bd094e…` |
| theory/integrable-toda.md | `120488e3e03ce6af…` |
| theory/integrable-normality-obstruction.md | `2da91f328bc60771…` |
| theory/integrable-ratio-obstruction.md | `878633d91df42f1f…` |
| theory/integrable-predivide-failure.md | `b483749fae2d194d…` |
| theory/dictionary-graph.md | `283f589eda93e466…` |
| theory/dictionary-lifts.md | `47e5a59c72bc0be4…` |
| theory/dictionary-obstructions.md | `8696595fe1abfd4f…` |
| theory/dictionary-target.md | `5672a8947854f557…` |

Subagent E also recomputed SHA-256, Git blob and bytes for all 49 evidence-manifest rows at `ff783d5` and `680dca3`; all match.

## Results by priority

### 1. Krawtchouk lower bound and proximity theorem (auditor)

**Lower bound (conditioning-lower-krawtchouk.md): accepted as PROVED.** I reconstructed every step by hand:
- **Normality:** the Chebyshev-system argument for 1,…,x^(n−1), e^{λx}, …, x^(m−1)e^{λx} (Rolle, including Q=0 and n=0), then the constant sign across ordered subsets and Cauchy–Binet, for indices through degree N.
- **Scalar Krawtchouk algebra:** E_p G G = (1+p(1−p)st)^M, the norms, α_r and β_r.
- **Formula (5).** The axis values are the scalar recurrence. Against PD-T289's (A), (B1) and (B2) (`topics/nn-mop-iep-20261103/theory/marginal-reconstruction.md`), the a-update gives n q1(M−t+1). The b-update uses (q1−q2)/d = −(1−p1−p2) to give B_(ν+e2,1). Adding d(M−t) gives B_(ν+e1,2). The induction covers the terminal layer.
- **Scaling to z:** b2 = n/(5M) and ‖b2‖∞ = 1/5.
- **Terminal coefficient:** the leading-coefficient finite-difference identity, H(−1) = (−1)^M M!, and B = −H'(−1)/H(−1).
- **The jets (9).** The parity direction maps the second-weight evaluation at 1 to H(−z) at 1. The degree bound deg S ≤ m and S(−1) = 0 give (10). The z=1+y substitution gives A(y), and S'(−1) = −C(−1)^M 5^n 2^(m−1) R gives (11).
- **The formal identity** [t^r](1−t)^(r−1)F(t) = [u^r]F(u/(1+u)), checked on monomials including j=0 and r=0, gives (12) and (4).
- **The bounds:** (1), the central-binomial step for (2), (3) by the binomial theorem, and the summed generating function (1−z)/(1−2z+z²/25) with roots 1±√(24/25) for (13), including M=1.
- **Admissibility:** the parity witness has input norm one, zero second mass, and fixed nodes and first weights. It is therefore admissible under the mixed, componentwise-node and fixed-mass conventions.

The text correctly presents a lower exponential base (5+2√6), not a sharp rate. The matching upper rate stays OPEN.

**Proximity theorem (conditioning-lower-proximity.md): accepted as PROVED.** I checked:
- E_q K_j = (M)_j δ^j;
- the two-term terminal form P = K_M − cK_(M−1), with c = δ;
- the direction ζ_k = (−r)^k/r^M, with r ≥ 1 for q ≤ 1/2, so |ζ| ≤ 1, and w2ζ = q^M C(M,k)(−1)^k annihilating degree < M;
- |ċ| = q^M/δ^(M−1);
- ‖b2‖∞ = 1/5 from the affine vertex values, and d_min = 2δ/M;
- divergence for M−2 ≥ 1, so N ≥ 4. The restriction is correct: at N=3 the product is bounded.

**Independent exact code ([audit-01/claude/](audit-01/README.md)).** Dual numbers over Fractions; it builds P_ν from the moment systems and extracts NN coefficients by polynomial matching, with a full residual check. It imports nothing from the developer.
- Formula (5) holds for every site with |ν| ≤ M, M = 1..12, for (p1,p2) = (2/5,1/2), (1/3,3/4), (2/5,9/20) and (7/10,1/5).
- The terminal derivative (4) and its sign formula (11) hold exactly at every terminal pair.
- The maximum terminal ratio is at least the bound (13).
- The proximity derivative, ‖b2‖∞, d_min and the κ lower bound hold exactly for δ = 1/10, 1/37 and 1/1000, M = 3..12.
- My first run had an elimination bug in my own code: it skipped rows whose pivot-column entry had zero value part but nonzero derivative part. I found it, fixed it and reran everything; the results above are from the corrected code only.
- The exact mixed condition number, computed independently over all 3N directions, is 4126/25, 77996/45, 307633/25 and 151421899/1250 for Krawtchouk N=4..7. Subagent A independently obtained the same values and Hahn N=4..6. These equal the committed table, which confirms the norm convention in conditioning-local.md.

### 2. Coarse upper bound, normality reduction, finite Hahn theorem (subagent A)

Accepted as PROVED: conditioning-krawtchouk-bound.md, conditioning-normality-certificate.md and conditioning-hahn-normality-finite.md.

The coarse bound's proof was reconstructed independently. The constants and quantifiers check, and it is honestly labelled very coarse. At N=64 its log10 is 94,449, against a measured κ of about 1.2e61.

The normality reduction is noncircular:
- axes are normal by positive-definite Gram matrices;
- the difference identity at η needs only η, η+e1 and η+e2;
- bordering gives the corner with sign +1;
- degree-k normality and the terminal layer are never used.

The 43,676 tested d values correspond one-to-one with the mixed targets: Σ N(N−1)/2 over N=4..64 = C(65,3)−4.

Reruns:
- **Developer checker:** `conditioning_verify_normality.py` gives PASS 61/43,676; its output is byte-identical to the receipt in independent-checks-03.
- **Producer:** the producer rerun for Hahn N=4..64 passes, with min|d| = 524/10614807 at N=64.
- **Independent code** (`indep_hahn.py`):
  - mod-p determinants at two primes: all 61 sizes normal, 47,885 nonzero determinants;
  - the literal moment definition at N=4..32, 40, 48, 63 and 64;
  - an exact NN-value recursion at all 61 sizes, re-verifying 1,441,430 orthogonality conditions.
  - All 61 input and payload fingerprints match the committed receipt.
- **Determinant identity:** `indep_identity.py` checks it exactly at 146 sites, including a planted zero.

### 3–4. Local derivative, full conditioning table, D2 gates (subagent B)

**Local derivative and induced norm (conditioning-local.md): accepted as PROVED.** The conditioning table and the D2 gate verdicts are accepted as MEASURED.

The derivative was re-derived:
- the moment derivative, ċ = −M⁻¹(v̇ + Ṁc), and the h, a and b updates;
- the induced row-sum norm attained by choosing signs, with an O(ε²) analytic remainder;
- the terminal b1 = b2 identity.

The implementation was checked for:
- all 3N columns;
- both mass-scaling directions, exactly null for the NN and step-line maps;
- positive field scales;
- structural zeros (a1 at n=0, a2 at m=0, γ0, δ0, δ1) with zero derivative rows;
- consistent N versus M;
- u = 2⁻⁵³ distinguished from ε = 2⁻⁵².

**Step-line extraction.** The formulas β_k, γ_k = a1+a2, and δ_k = −a1·d_η (even k) or +a2·d_η (odd k) were verified exactly, with their derivatives, at N=3..8 in both families. The verification matches xQ_k − Q_(k+1) directly, independent of the D1-01 formulas.

**Independent exact Jacobian** (`exact_jacobian.py`): dual numbers over Fractions, all 3N directions, N=3..8, both families.
- Exact values include κ = 4126/25 (Krawtchouk N4) and 49126640/31213 (Hahn N4).
- Against `conditioning.py`, the largest relative difference is 2.80e-112 over 72 norms at 120 dps, and 8.39e-252 at 260 dps for N=4..8.

**Full-table rerun.** The producer was rerun with the timing wrapper for every N=4..64, both families, at 180 and 260 dps. It used 4146.7 CPU-seconds, and all four runs exited 0.
- `conditioning_compare.py` passes. The worst 180/260 agreements are 1.7632664200e-115 (Krawtchouk) and 1.2841742107e-93 (Hahn), as in attempts/D1.md.
- The regenerated markdown table is byte-identical to the committed 61-row table: 0 of 244 cells differ.
- For N=9..64 this is an identical rerun of the developer's formulation, not an independent formulation.
- The table is correctly labelled MEASURED (precision agreement, not an outward enclosure).

**C4 gates (D2).**
- **G0:** passes 12/12, bit-identical E with matching input hashes.
- **Stage-isolation reruns:** both `stage_isolation.py` runs (100 and 160 path dps) reproduce all 48 E and 48 B values bit-identically. They also reproduce:
  - the input-rounding effects;
  - the N24/32 complex-node and negative-weight observations;
  - the exact-path bound 2.4277e-98.
- **G1** fails exactly where listed:
  - Krawtchouk N8 17.5638 and N16 17.1456;
  - Hahn N8 100.6929, N12 63.2900 and N16 113.4901.
- **G2** applies only at Hahn N8/N16, where the stable-marginal ratios are 182.3905 and 220.6828. G2 fails as recorded.
- Input rounding is at most 0.136κu.
- No general stability or instability theorem is claimed.

**Path-plus-anchor traps (independent `trap.py`, exact, N=4/6/8, both families).**
- **Missing anchor.** The genuine positive input w2' = w2 + w1/3 leaves the alternating-path matrix exactly unchanged. It changes d0 and 17/40, 38/84 and 67/144 NN entries; E between the two genuine arrays is 0.14–16.9.
- **With the anchor.** The anchor plus the mass gauge recover w2' to about 1e-100, so for compatible arrays the diagnostic determines the input.
- **Unread entries.** Perturbing every entry `recover()` never reads leaves it bit-identical while E is 3.3–4.5. The unread entries include terminal b2 at ν_(N−2) and b1 at ν_(N−1).
- Both claimed traps are correct.
- `independent_check_diagnostics.py` exits 0.

### 5. Native whole-triangle designs (subagent C)

**Accepted as MEASURED, finite attainable cases only.** These have no novelty or stability-theorem claim.

Reruns and exact reference:
- `native_mixed.py` rerun at N=4/8/12/16, both families: the N8 LU errors reproduce exactly, 3.09634e-12 (Krawtchouk) and 4.23819e-10 (Hahn), gains of 2.781 and 2.790 digits. κu = 1.065e-10 and 2.596e-9 respectively, both ≤ 1e-4.
- An independent exact Fraction reference (`native_exact_ref.py`) reproduces every developer E at N=4/8/12/16.

Analytic checks:
- the coefficient extraction b = r[s], a = sol·t[s];
- the Gram α_k formula;
- the terminal φ_N = γ_(N−1)F step;
- the reduction of design B under full row rank.

### 6. Joint-data image and dyadic obstruction (subagent C)

**Accepted as PROVED:** backward-local-manifold.md and backward-dyadic-obstruction.md.

Manifold theorem, reconstructed:
- the marginal axes equal the Jacobi data, Q is orthogonal, and the weights are the squared first components;
- analytic ordered eigenvalues give the left inverse G∘F = id, rank 3N−2 and injectivity;
- the nearest-point argument and the first-order formula (AᵀWA)Dp* = AᵀW.

An exact dual-Fraction Jacobian at N=4 and 6 confirms rank 3N−2, the marginal-row rank, the exact mass null directions and zero structural rows.

Dyadic obstruction:
- **Necessary condition.** I proved it independently from the NN identities at (1,0) and (0,1). It needs normality through degree 2, not positivity.
- **Certificate.** The certificate's residual is exactly 25700541873527631/649037107316853453566312041152512 ≈ 3.96e-17; its denominator is a power of two. Integer and Fraction evaluations agree, and the residual is 0 on the true N4 array and on 50 random exact inputs.
- **Reproduction.** `backward_dyadic.py --reproduce` regenerates the developer's receipt hash on this platform. The standalone certificate is platform-independent; that the producer emits these five fields is platform-dependent reproduction, which happens to succeed here.

### 7. Projection fits (subagent C)

**Accepted as MEASURED, with M2 and M3.**

Preparation was recorded separately from the checker's own fit. The two 160-dps producer receipts were regenerated locally at `/tmp/backward-projection-{family}-r2-160.json`; their hashes differ from the developer's because of timing fields and platform-dependent nodeqr arrays.

The projection checker passes, but its "equals developer" comparison then compares the regenerated receipts with themselves (M3).

Exact rebuilds of the N4 LU and nodeqr witnesses and all six N8 witnesses:
- reproduce η_d/u, η_c/u and √Q to ≤ 2.2e-16 relative;
- every mixed system is nonsingular, and positivity, order and unit mass hold;
- 48 exact probes increase Q at N4 LU, consistent with a local minimum but not a certificate.

The stated separations hold: optimizer convergence vs returned-witness stationarity; η_c vs η_d; strict β = +∞ for raw arrays. No global-nearest claim and no general 100u claim is made.

### 8. Integrable transport and obstructions (subagent D)

**Accepted:**
- Christoffel transport, PROVED;
- finite Toda flow, PROVED;
- positivity-to-normality counterexample, PROVED;
- common-ratio orbit obstruction, PROVED;
- predivide-C4-restore failure, MEASURED.

Developer reruns, all reproducing the stated values:
- `integrable_transport.py` in exact, float and Toda modes;
- `independent_check_backward_integrable.py`;
- `independent_check_moments.py`.

Independent exact code:
- Christoffel transport in 40 random cases, with shifts below, above and inside the hull;
- the Toda derivative in 25 cases;
- the counterexample determinants and the transformed D11 = 0;
- the exponential-path D11(a) = 9a − 4a² − a³, with first positive zero a* = √13 − 2;
- cross-ratio invariance.

An exact Fraction reference for predivide-C4-restore at N=4..16 reproduces E: 0.0966694 vs 0.2233090 (Krawtchouk N16) and 70.3138 vs 79.7731 (Hahn N16). Both triangles are certified exactly normal. "Oracle initialization is not an IEP solution" is stated at D4.md:72 and in the Toda, candidates and report records.

### 9. Graph encoding and dictionary obstructions (subagent D)

The graph identity, the scoped obstructions G and C, the lift identities and the lattice argument are correct, with one exception: M1. The full NN-to-Padua dictionary and stable transfer correctly remain OPEN, not PARTIAL.

The D6 gate-timing disclosure (novelty-gate-D6-D7.md:18–25, D6.md:11–14) is honest and claims no retrospective clearance. Git cannot independently order the writing: gate, probe and receipts first appear together in `f75964b`. The qualification must never later be upgraded to "prospective gate passed".

### 10. Source access and literature (subagent D)

G5 BLOCKED is confirmed from this session:
- CONNECT 403 for gitlab.kuleuven.be (IEP-MOP), the SIAM supplement ZIP and landing page, and arXiv;
- WebFetch refuses the GitLab host;
- GitHub searches find no mirror;
- Octave is absent.

No external run, paper-configuration reproduction or Leuven contact is claimed. Cited sources supply attribution and context only; no proof is imported.

Unblocking G5 needs gitlab.kuleuven.be and/or epubs.siam.org allowed in the environment's network settings. That is AC's decision.

## Findings

### BLOCKING

None.

### MAJOR

**M1 — arithmetic error inside a PROVED proof.**
- Location: `theory/dictionary-obstructions.md:55–57`.
- The proof states w2 moments "(15,34,86,232)" and the equation "15c0+34c1=-86". For w2 = (1,2,4,8) on nodes 0..3 the moments are (15,34,90,250), and the equation is 15c0+34c1 = −90.
- The stated solution (32/23, −75/23) satisfies −90, not −86; the displayed equation would give c0 = 20/23.
- The conclusion ⟨P,x⟩ = −30/23 and the probe code are correct.
- Found by D; confirmed by the auditor with an independent computation. The supplementary checker missed it.
- Fix the three numbers. This is a proof-text change, so it gets a focused re-audit.

**M2 — platform dependence of binary64 measurements is undisclosed, and one stated bound fails on independent rerun.**
- `attempts/D3.md:87` and `attempts/D5.md:224` call the runs deterministic. On this platform several binary64 values differ:
  - Krawtchouk N16 LU E = 4.13854e-4 vs 3.78170e-4, a gain of 2.37 digits vs the 2.41 at `candidates-D3-D5.md:74`;
  - Krawtchouk N12 LU 4.85781e-8 vs 4.44444e-8;
  - every nodeqr fit row;
  - Krawtchouk N8 LU fit 1258.09/5692.66 vs 1258.75/5692.26;
  - the set of 100-dps stalled fits.
- Krawtchouk N4 nodeqr gives η_c = 30.78u, which contradicts "nodeqr has both components <=30u" (`attempts/D3.md:132`, `candidates-D3-D5.md:98`) and "below 30u" (`theory/backward-projection-measurements.md:17`).
- No gate verdict changes: N4 stays below 100u, and N8 still fails 100u.
- Fix:
  - label every binary64 value as environment-dependent, with the producer platform;
  - replace the 30u statements with a platform-qualified value or with < 100u;
  - keep the 100u conclusions.

**M3 — the returned rational witnesses of the MEASURED projection fits are neither committed nor hash-pinned.**
- No witness hash appears in the topic. The projection checker reads `/tmp` receipts that any re-auditor must regenerate. Its developer-equality check therefore becomes a same-platform self-comparison, and for nodeqr it does not survive a platform change.
- Fix: commit the small rational N4 and N8 witnesses, or at minimum their SHA-256 and the producer platform. Make the checker compare against the committed identity. Per AC's 2026-11-06 instruction, this small evidence needs no storage action while the total stays under 10 MB.

**M4 — candidates prescribed by handoff01 are not preserved as candidate records.**
- `handoffs/01-work.md:76–82` prescribes four D3 candidates:
  - (a) NN core transformations, a whole-triangle IEP_CORE;
  - (b) lattice biorthogonal Lanczos with all-path reorthogonalization;
  - (c) multi-path step-line redundancy combined under zero curvature;
  - (d) the coupled updater, IDEA-378.
- Only LOG.md:16 mentions (a)–(c), and candidates-D3-D5.md:61 says "not newly claimed biorthogonal Lanczos or a core updater". They have no provisional IDEA records.
- D1's alternative mechanisms named in the plan are likewise unrecorded: Vandermonde conditioning and potential-theoretic node density.
- AGENTS.md requires every considered candidate to be preserved with a scoped reason.
- Fix: give each a provisional IDEA record containing:
  - closest entries: LIT-347 IEP_CORE, IDEA-378/379, IDEA-031/090;
  - a `deferred` or not-attempted disposition with its reason and resume condition;
  - one line on why designs A/B were chosen instead.

  This does not reopen D3.

### MINOR

To fix with the response, unless stated otherwise; confirmed by diff:

1. **Stale "independent check pending" text** where independent-checks-01/02/03 record completed supplementary checks:
   - backward-dyadic-obstruction.md:36–38 and :74–75 (contradicting report.md:55);
   - native-measurements.md:63–65;
   - d2-stage-isolation.md:89;
   - dictionary-obstructions.md:77–78, dictionary-target.md:61 and D6.md:70;
   - the Checks sections of integrable-christoffel.md (:72), integrable-normality-obstruction.md (:57) and integrable-ratio-obstruction.md (:51);
   - conditioning-hahn-normality-finite.md:28–30 and :189–190 ("ready for the coordinator's round2 publication").

   integrable-predivide-failure.md:26/:62 is accurate. Where the evidence manifest pins a prose file, update the pin in the same commit (be9a831 rule). Keep the Claude audit status in the log and handoff only.
2. **Disposition reasons.** conditioning-lower-proximity.md:36 and backward-dyadic-obstruction.md:39 say `REJECTED: failed`, while gates.md:10 says "refuted analytically". The PD-N118 precedent uses `refuted` for the same raw exact-match claim. Each statement negates a stated claim, so choose `refuted` or justify `failed`, consistently.
3. **PD-N template sections.**
   - The proximity record lacks the negative-result scope, attempted mechanism and parameter range sections.
   - The dyadic record lacks parameter range.
   - dictionary-obstructions.md bundles (G) refuted and (C) failed under one provisional PD-N. Split it, or justify the bundle before final IDs.
4. **OPEN parent targets have no durable home.** "D1 sharp growth-law target (OPEN)" is cited as the Split-from target by four files, and the general stable-solver / strict joint-backward-stability target has the same gap. WORKFLOW requires the original target to stay registered with its true status. Also:
   - conditioning-normality-certificate.md:4 reverses the split direction relative to conditioning-hahn-normality-finite.md:4;
   - mark dictionary-lifts.md as a sub-target of dictionary-target.md, or consolidate them.
5. **Closest predecessors.**
   - D1-01's gate omits Fischer 1998 (LIT-113/365: recurrence-coefficient derivatives and conditioning in the univariate case), Fischer 1996 (LIT-112) and IDEA-012/087/088.
   - IDEA?…-34 and backward-dyadic-obstruction.md should name PD-N118/IDEA-262 as the closest predecessor (variant), not only in the gate addendum.
   - IDEA-090's mechanism (block-Krylov angles) needs a one-line pointer that it stays deferred.
6. **Duplicate literature IDs.** LIT?…-D4-01 (arXiv 1511.08098v3) is LIT-567, and LIT?…-D4-02 (arXiv 2407.13946v2) is LIT-568. State the equivalence in literature-D4.md (lines 3, 7, 15) and reuse those IDs; only D4-03 (Branquinho–Foulquié-Moreno–Mañas 2022) is new.
7. **proposed-record-changes.md is superseded by be9a831.**
   - Registries are now edited directly and reviewed by diff.
   - Block1's new text carries process stage, now forbidden in registries.
   - Block2 should keep IDEA-378 `deferred`, with its resume condition, rather than "remains OPEN", since no updater was attempted (novelty-gate-D3-D5.md:33).
8. **Unconsolidated or missing gate records.**
   - D1-03 in novelty-gate-D1.md still says "abandoned… No PD-N", although D1-hard-03 produced a PROVED PD-N for that mechanism. Consolidate.
   - novelty-gate-D2.md:21–23 defers to a coordinator full gate that does not exist. State that the gate does not apply, since D2 claims no mechanism, or record the gate.
9. **One canonical disclosure.** The D6 gate-timing deviation and the post-run prospective record of D4-C1a (novelty-gate-D4.md, final paragraph) each need one canonical disclosure, linked once elsewhere, and an explicit AC decision at PR. No retrospective clearance.
10. **Wording overstatements.**
    - native-measurements.md:19–20: "Both algorithms gain over 2 digits at N16" holds only for design A with LU and for design B; A's QR and SVD gain 0.97 and 1.21 digits at Krawtchouk N16.
    - candidates-D4.md:82: the Toda range "4.8e-15–7.24e-14" should be 4.91e-16–7.23e-14.
    - integrable-toda.md:15: "a compatible array" should say the moment-defined array at t0 on the connected normality interval.
    - "Independently executed fits" (`independent_check_followup_projection.py:77`, `independent-checks-02.md:113`) ran the developer's own fit code. Only the exact rebuild, objective and gradient are independent. Say so.
11. **Localized lemma.** conditioning-normality-certificate.md:59–65 says "precisely the induction in PD-T289", but PD-T286/289 are stated under global normality. State the localized NN-identity lemma with its degree bookkeeping. A checked it is valid, so the result stands.
12. **Checker robustness.**
    - conditioning_verify_normality.py:14,18–21 and conditioning_exact_normality.py:21,28 use bare `assert`. A demonstrated on a scratch copy with a corrupted N64 payload digest: the run fails normally but prints PASS under `python -O`. Use explicit raises.
    - The verifier also prints code hashes without comparing them to the pins in conditioning-hahn-normality-finite.md:136–138. Compare them.
13. **Exposition.** backward-local-manifold.md:113–116 uses the continuity-of-G argument that appears only at :140–143. Move or cite it.
14. **Infinite componentwise output.** conditioning-local.md:45–47, conditioning-measurements.md:24–25 and attempts/D1.md:45–46 name only Krawtchouk as having infinite fully componentwise output. Hahn's is infinite as well: its symmetric w1 gives b1 = 0 at every axis site, with nonzero sensitivity. Krawtchouk also has sensitive interior zeros, for example b1_(1,1) at N4. Name both families.
15. **G2 margin.** The Hahn N8 ratio that makes G2 applicable is 100.6929, an excess of 2.003 digits against the "more than 2 digits" threshold, a 0.7% margin. With ε = 2⁻⁵² no case would trigger G2. The verdict correctly follows the pre-registered u (plan.md:28). Disclose the margin and its dependence on the convention in gates.md:9, report.md:43 and attempts/D2.md:78.
16. **Path-diagnostic wording.** d2-path-diagnostic.md:82 says only "discard off-path entries". The diagnostic also never reads terminal b2 at ν_(N−2) or b1 at ν_(N−1); say so. Optionally, cite the genuine positive-input missing-anchor witness above in place of the hand-edited incompatible array.

### NOTE

- Shared registries are unchanged on the branch relative to its main merges. No final ID is assigned. The reservation (T432–471, N162–177, IDEA530–569, LIT614–629, first published `d879256`) was not fully refreshed against open PR heads in this audit; that belongs to the readiness check.
- The finite Hahn theorem's supplementary rerun re-executed the developer's producer. Independent implementations now exist at all 61 sizes (subagent A, above); the record may cite this audit.
- Supplementary checks partly reviewed earlier file versions: the certificate at `e2e48c81`, never committed, while the committed file is `6692f54e`. independent-checks-03 rechecked the committed version. They remain supplementary.
- G4's pass condition asks for a "new D3/D4 algorithm". Designs A/B are known reformulations, so G4 must stay "forward threshold met; strict backward stability not achieved", never shortened to PASS.
- The dyadic identity holds for any linear functionals normal through degree 2, so the stated positive-measure claim is weaker than what is proved.
- D1's κ uses unnormalized masses, while D5's η_d uses fixed masses. They are not comparable, and the topic does not compare them.
- D4: in general a common multiplier only scales the degree-N determinants, so they cannot cross zero along common paths. The D11 crossing is the first zero on the stated path; strengthening the statement is optional.
- Storage (per AC, 2026-11-06, NOTE only): the committed topic is 576,212 bytes in 87 files. No cleanup action was taken. cold-storage.json correctly says `delivered: false`. The developer's 59 local `/tmp` artifacts are not present in this container; the essential exact evidence is committed.

## Residual uncertainty

- Random-case exact checks are finite: Christoffel N ≤ 6, Toda N ≤ 5, Krawtchouk closed form M ≤ 12, exact κ N ≤ 8. Generality rests on the written proofs, which were reconstructed by hand.
- For N=9..64 the conditioning table is a rerun of the developer's own formulation at two precisions, not an independent formulation.
- Floating tables are compared across precisions and platforms; none is an outward enclosure.
- The Q-fit witnesses are local measurements; no global minimality is certified.
- The primary literature for D4 sources was not re-read (arXiv is blocked here), and journal metadata was not verified.
- The reservation refresh against open PR heads is deferred to readiness.

## Required next step

Codex responds in `response-01.md` with a fix, an evidence-based rejection or an explicit unresolved item for every finding above. Material changes (M1–M4 and any status, value or evidence change) then receive a focused Claude re-audit. Registry application, final IDs and the reservation refresh follow at PR preparation, with the readiness check. Only AC merges.
