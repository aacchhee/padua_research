# INTERIM audit-01: Claude's own ideas for closing 41–499999

This is the second mandatory deliverable of handoff 07, a companion to
[audit-01.md](audit-01.md). **Claude proposes; Codex implements.** Claude
launched no proposal, campaign or validated run. All numbers below are
**MEASURED**: binary64, finite samples, no enclosure. They are not proof
premises, counterexamples or cost laws. The provisional idea IDs
`IDEA?argmax-bridge-claude-I01..I05` are not final IDs.

## Orchestrator synthesis and review

The idea review (Opus 5.5, instructed xhigh) ran the full novelty gate
before it generated any candidate (section 1 below). I checked its output
against the audit findings and made one independent reproduction:
`python3 far_slack.py 128,1024` (scripts in
[audit-01/code/ideas/](audit-01/code/ideas/); kernel
`topics/padua-argmax-effective-2-20261105/code/phase_probe.c`, sha256
prefix 692d4afd89d3bbda, built with
`cc -O3 -std=c11 -shared -fPIC phase_probe.c -lm -o probe.so`). It took
about 7.5 s of CPU and exited 0. The rerun reproduced these values:

- min(Λ_c−S): 0.33891 at n=128 and 0.65547 at n=1024, both at α=β=1/4.
- max|S−M_far|: 0.01510 at n=128 and 0.00268 at n=1024.
- The proved bound E_far: 4.33·10^5 at n=128 and 6.90·10^3 at n=1024.

**The main conclusion.** The half-million threshold comes from proof
constants, not from the fixed models.

- The measured model error is about 0.4·L/n at every tested degree from 41
  to 4096.
- The true worst far margin stays at or above 0.21 down to n=41.
- C13's slack of 8.2·10^-4 is an artifact of its error allocation.

So the cheapest productive direction is to replace hand constants with
phase-local, degree-free validated constants (P1, P4). Running the old
technology on more degrees is not that direction.

**My own sensitivity check** (`audit-01/code/root/root_far_floor.py`).
Keep C13's hand margin side, C_far<8821/3000, d(n)→16/25 and the fixed
error 7/50+2/63, and set every degree-dependent error term to zero. The
far comparison then still fails below:

| Near/far split ρ0 | Hand-margin floor |
|---|---|
| 1/2 | n≈1.1·10^5 |
| 3/4 | ≈2.7·10^3 |
| 1 | ≈430 |
| 3/2 | ≈70 |

The binding phase is the diagonal point α=β=ρ0/2, because the uniform
u=1−cos(ρ0/2) bound is weakest there. Crediting the 1/16 noncorner defect
in the far region moves the ρ0=1/2 floor only to about 9·10^4.

This independently supports the review's finding 2 (sharpening E_far alone
fails) and identifies the near/far seam geometry as a second lever. That
lever applies only if the near noncorner comparison and the actual-corner
patch are re-proved on ρ<=ρ0 for ρ0>1/2. P1 (the far model used on the
near domain) and P3 (a degree-dependent split ρ0(n)) both carry it. It is
recorded there and not as a separate candidate.

**Ranking I endorse.** It differs from the review's numbering only in
presentation:

1. **P4.** The corner bracket is the cheapest test (seconds of CPU), and
   the corner is probably the binding onset once the far case improves.
2. **P1.** A validated degree-free model with phase-local constants. It
   has the largest leverage and covers the far case and, through the
   defect, the near noncorner case.
3. **P2.** Taylor models in h=1/n for the fixed-R endpoint blocks only,
   resuming IDEA-337 under its stated condition.
4. **P3.** Near- and corner-only finite certificates below the analytic
   onset, with ρ0(n).
5. **P5.** A declared first-order far correction, used only if P1's
   componentwise route turns out to be cancellation-limited.

**Review cautions for Codex:**

- P1 T1-c, the non-decaying ~10^-3 discrepancy of S−M_far near the a=0
  edge, must be resolved before any uniform C(L+1)/n error form is
  written. It is harmless to C13, because the fixed 0.17 allowance and the
  margin above 10 there dominate. But it may expose a diagnostic-quadrature
  artifact or a missing model term.
- Each proposal is a new candidate with its own records. None may edit the
  frozen C13 proofs or reuse their quantifiers below n0.
- The one-correction near model stays fixed. Using M_far on the near
  domain (P1) is a separate route against the defect floor, not a second
  near-model correction.
- The 41–63 window needs existing-style full certificates, because the
  1/64 floor needs n>=64. No Syvert pack is justified until an analytic
  onset and a measured whole-certifier throughput exist.

---

# Idea review (gate, measurements, proposals)

The full idea review follows. It was drafted by the ideas subagent, and the synthesis above records the orchestrator's review of it. Section numbers are local to this part.

## 0. Bottom line

1. **The 500000 onset comes from loose constants, not from the fixed models.** Sampled far phases give a true
   fixed-model error |S_n − M_far| ≈ 0.40·L/n for every tested n from 41 to 4096 (0.037 at n=41). The proved
   bound is E_far(n) ≈ 4.2·10^6 at n=41 and ≈ 1.8·10^3 at n=2048. The true far margin is 0.21 at n=41 and
   0.79 at n=2048. The corner and near cases show the same pattern (§2).
2. **Idea (a) as phrased cannot work: tighter E_far constants alone cannot reach 10^4–10^5.** With every
   E_far term set to zero, C13's hand margin side still fails below **n ≈ 131000**. The binding pieces are
   C_far<8821/3000 (measured ≈1.82 at the binding phase), d(n)=(0.64n−28000)/(n+1) (negative below 43750,
   while the measured Λ_c−A_n² ≈ 0.92) and the weak coefficient bound. The margin side must be sharpened too.
3. **The degree-free model M_far is accurate on the whole diamond, near domain included.** At sampled near
   phases (ρ≤1/2), max|S_n−M_far| ≈ 0.37·L/n, and the model increment sup[M−M(0,0)] (≈8·10^-5 at n=41)
   tracks the true S-excess. So one validated, degree-free model plus one explicit error constant could
   settle both the far case and the near-noncorner case. Only the two actual corner patches need a separate
   local argument. Caveat: next to the a=0 diamond edge, S_n−M_far tends to a non-decaying value of about
   ±1·10^-3 (§2.4). The error form must allow it.

Recommended order for Codex: P1 → P4 → P2 → P3, with P5 as an alternative to P1/P2. Details in §3 and §5.

## 1. Novelty / obstruction gate (done before any candidate below)

**Registry.** `state/IDEAS.md` (1112 lines; sha256 `68bf789c82967944421e6fc54f8164dbdb91d1096fa10694008261fbd54f9e9d`,
the same SHA the C13 gate recorded):

- All 64 headings and every `Aliases:` line scanned.
- Read in full: the canonical/seed tables (l.1–125); the obstruction tables at l.106, 256, 396, 462, 505, 764 and 845; and the full Padua-argmax sections.
  - PR17 IDEA-316–335 (l.852–890).
  - PR19 IDEA-336–348 and its scoped obstruction table PD-N084/085/086 (l.891–920).
  - T2–T4 IDEA-356–358 (l.921–933).
  - PR25 IDEA-454–461 (l.990–1016).
  - PR12 IDEA-286–311 with PD-N072/073 (l.814–851).
- Coverage limit: the MZ, lattice, Lanczos, NN-MOP and signed-MZ sections (l.125–813, l.934–989, l.1017–1112) were scanned by heading, alias column and obstruction table only, not row by row. A grep confirmed no argmax/Lebesgue-function mechanism there, apart from Padua nodes used as Lanczos benchmarks.

**Searches run** (rg or grep over `state/IDEAS.md` and `topics/padua-argmax-*`):

- Bernstein, Markov, Remez, Christoffel, harmonic, sinc, Euler–Maclaurin, two-scale, homotopy, sum-of-squares, Taylor model, batch, monoton*.
- "monoton* in n/degree", "increas* in n", consecutive degree, degree block, interval of degrees, "in 1/n", h=1/n, continuous/real/fractional degree.
- "1/n correction", first-order correction, next order, O(L/n), O(log n/n), subleading.
- far threshold, split radius, rho0, near/far split.
- validated (fixed-domain) enclosure, phase-only, degree-free, degree-independent.
- `literature/INDEX.md` (sha256 `6f514c10…c064c6f`) grepped for Berz/Makino/Taylor model/Euler–Maclaurin/validated/interval/Caliari/Lebesgue-constant attribution.

**Shortlist read in full.**

| Shortlisted record | What it rules out or requires |
|---|---|
| IDEA-337 (R2, h=1/n interval Taylor enclosure) in `padua-argmax-effective-20261103/ideas/r1-r2-r5.md` | Deferred. Resumption condition: "a precise uniform remainder … below the defect budget". This is P2's direct predecessor. |
| IDEA-336 (explicit E,d,f) | Deferred. Generic predecessor of every sharp-constant proposal. |
| IDEA-338 (Bernstein, SOS deferred) | Rejects a Bernstein-envelope "novelty". |
| IDEA-454 (common-primitive three-region cover, PD-T364) | Base architecture for P3. |
| IDEA-456 / PD-N132 | The model must keep the phase-dependent L term. Every proposal keeps the C06 model. |
| IDEA-459 (corrected interior profile, deferred) | — |
| IDEA-460 (Markov shortcut ≡ PD-T227) | A Markov corner shortcut is a duplicate. |
| IDEA-330/457 (corner energy; larger corner zones OPEN) | — |
| IDEA-321 / PD-N081 (O-R whole-diamond monotonicity: failed, measured, within fixed n) | — |
| IDEA-318/324/325 | — |
| C13-onset idea record | Explicitly *excludes* changing R/δ/J/H8 and *defers* "sharpening new hard phase functions". |
| C08-far-comparison idea | Lists, undeveloped, "a validated fixed-domain enclosure after an exact reduction" for C_far≤5/2. This is P1's closest predecessor. |
| C06-far idea and its 35-case diagnostic receipt | — |
| N3-corner-batch (n2–128 corner patch, 5.25 CPU-s total) | — |
| C01-near-quadratic obstruction (PD-N, the α^{3/2} term must be kept) | — |
| C08 row-box obstruction (Ω(n²w) direct moving-root enumeration, scoped) | — |
| N4 diagonal-translation, N5 quarter-certificate (PD-N), N6 two-trace (PD-N) | — |
| C01-allclass (defect >1/2048 n≥64); C02 dense band (1/64 / 1/32 / 1/16 at n≥64/160/4096) | — |
| All seven C13 records and C06-far-compact-error §3–5 | — |
| C07-corner-million-onset §2–4 (origin of the corner "+16") | — |
| margin-anatomy, margin-measurements, phase-cover-measurements | — |
| independent-checks-C03-cheap-n32 | Leaf classes: 280 far / 28 corner-orbit / 24 max-exclusion / 32 outside. |

No external theorem is imported. The Taylor-model technique is standard validated numerics with no LIT record in INDEX. No priority or novelty claim is made beyond "variant with a stated difference within this documented search".

File identities (sha256, first 16 hex characters):

- report.md `89b43388fe296deb`; results `1118b1125fc13416`; campaign `a223871ee41d4e56`; handoff 07 `5f8f39edef9bf966`; gates `6c0bcc8909c32e7c`; rounds `4c18f7f9b88d3c75`.
- C13: onset-budget `bc975d53831052f5` (matches handoff); far-representation `11b27272af82cc3c`; far-comparison `e34aec6ac187dc77`; near-representation `fa861e5908cad7ad`; near-comparison `44f412f3adaa7ca3`; corner-value-lower `6b4bd8029f593ff5`; corner-comparison `b951104ecd48154b`.
- C06-far-compact-error `64d88fd3bce38763`; C08-far-model-comparison `0b69e38a8d27f362`.
- ideas: C13-onset `cc79e196ba50e17b`; C08-far-comparison `5b163289a6870f39`; C06-far `c01733dc09a004d7`; N3-corner-batch `e94919046f967b3f`; effective r1-r2-r5 `db7588b9ec1b44c7`.
- margin-anatomy `47039e201cd87b48`; margin-measurements `2017c6de553396ae`; phase-cover-measurements `6ad0baf7382c237f`.
- obstruction records: C01-near-quadratic `a1e217f904857d4d`; N4 `3fe6e396e37c5231`; N5 `0e86fe06ccf8845c`; N6 `5aba89fdfc98ae01`; C08-row-box `283eca3471dc7495`.
- C01-allclass `858634a7f38bbd87`; C03-cheap-n32 check `1996b1375077eed5`; c06 diagnostic receipt `55ea1ba9634c0b44`.
- Imported read-only code: phase_probe.c `692d4afd89d3bbda`; c06_far_profile_diagnostic.py `14d16dd46e2bfbf9`.

## 2. Sanity measurements (MEASURED; ~3.5 CPU-min total)

All scripts live in `audit-01/code/ideas/ (run in the auditor scratch directory)`. They use the inherited floating kernel `phase_probe.c` (`phase_s` = PD-T364 odd-board primitive S_n, `phase_lambda` = λ_n), compiled with `cc -O3 -std=c11 -shared -fPIC phase_probe.c -lm -o probe.so`, and the inherited C06 model `profile()` imported read-only. SciPy 1.18.1 was pip-installed in the session for that import. Commands:
`python3 far_slack.py 41,64,128,256,512,1024,2048`; `python3 far_dense.py 41,128,512,1024`;
`python3 far_order.py`; `python3 corner_near.py 41,64,128,256,512,1024`; `python3 near_full_model.py 41,128,512,2048`;
`python3 vertex.py`; `python3 onset_scan.py`. Outputs are in the transcript and in `far_slack_1.jsonl`. The scripts and far_slack_1.jsonl are now committed under audit-01/code/ideas/.

### 2.1 Far: true margin and true model error vs the proved budget

The sample is 127 first-quadrant phases on 1/2≤ρ≤π (13 radii × 9 directions plus axis points). S is even in each phase separately.

| n | Λ_c | min(Λ_c−S) (at α=β=1/4) | max\|S−M_far\| | ·n/L | proved E_far(n) (23) |
|---|---:|---:|---:|---:|---:|
|41|12.014|0.2114|0.0368 (α≈1.38,β=0)|0.407|4.2·10^6|
|128|17.346|0.3389|0.0152|0.401|4.3·10^5|
|512|25.268|0.5378|0.0049|0.399|2.7·10^4|
|1024|29.815|0.6555|0.0027|0.399|6.9·10^3|
|2048|34.753|0.7853|0.0015|0.40|1.8·10^3|

Λ_c(n) minus the limiting corner polynomial (4/π²)L²+b_cL+1.84616 is positive and decreasing: 0.027 at n=41, 0.0013 at n=2048. In the far comparison, the margin side's corner constant can therefore be ≈0.92 above A_n², not d(n).

### 2.2 Shape of the error

At (1.38,0), (1/4,1/4) and (1,1), S_n−M_far is fitted on n=128..1024 by (c1·L+c0)/n with residual ≤1.2·10^-5 up to n=4096:

| Phase | c1 | c0 |
|---|---:|---:|
| (1.38,0) | 0.385 | 0.078 |
| (1/4,1/4) | 0.358 | −0.239 |
| (1,1) | 0.087 | 0.188 |

The residual grows slowly, consistent with model-evaluation noise. The error is therefore a clean first-order term with an O(1) coefficient, not a 10^5 constant.

### 2.3 Near domain and corners

| n | max\|S−M_far\| on ρ≤1/2 (·n/L) | sup[M_far−M_far(0,0)] | sup(S−Λ_c) | min (Λ_c−λ)/r² at actual corner, ρ≤1/2 | C13 corner coefficient p(L) |
|---|---|---:|---:|---:|---:|
|41|0.0317 (0.350)|8.2e-5|8.4e-5 (α-axis, ρ=.008)|1.99|−14.9|
|128|0.0137 (0.362)|3.1e-5|3.0e-5|3.11|−14.0|
|512|0.0045 (0.372)|5.8e-6|1.0e-5|4.82|−12.5|
|1024|—|—|6.6e-6|5.82|−11.7|
|2048|0.0014 (0.381)|3.8e-6|3.8e-6|—|—|

C13's corner proof needs p(L)>0 and uses p>1/6. The true descent coefficient is about Λ_c/6 and is already ≥2 at n=41.

### 2.4 Caveat at the a=0 edge

At (1.45,1.45) (a=0.12), S_n−M_far = +9.1·10^-4, +9.0·10^-4, +9.1·10^-4, +9.3·10^-4 at n=1024, 2048, 4096, 8192. At (π/2,π/2), it moves towards ≈−1.1·10^-3. So, at least as evaluated by the diagnostic quadrature, there is a non-decaying ~10^-3 discrepancy near the a=0 diamond edge. It is harmless for the comparisons, since the margin there is >10. It does mean that any uniform error form of the type C·(L+1)/n is **false** near a=0 unless an ε0(α,β) term is allowed, or the discrepancy turns out to be a diagnostic artifact. This is a mandatory check in P1.

### 2.5 What-if onsets (`onset_scan.py`)

These are the C13 formulas with constants rescaled; planning only.

**Far case.**

| Scenario | Far onset |
|---|---:|
| Current proof | 492221 (≈ the proved 500000) |
| All 1/n and 1/n² terms of E_far → 0 (Q, 2/63 kept), hand margin | 189368 |
| Every E_far term → 0, hand margin | **131044** |
| True model margin (fit 0.0126L²+0.06 at the binding phase), current E_far | 135015 |
| True model margin, 1/n-constants ×10^-2 | 9569 |
| True model margin, 1/n-constants ×10^-3 | 3267 |
| True model margin, 1/n-constants ×10^-4 and constant terms ×0.1 | 1061 |

Error-constant budget: if E(n)=C(L+1)/n+0.02 against the true margin, the far case closes at N if C ≤ 1.86 (N=41), 5.5 (N=100), 81 (N=1000) or 1086 (N=10^4). The measured C is ≈0.35–0.40.

**Near noncorner, (18) form.** Scaling the 1/n constants (11270+200(L+1)) by 1, 10^-1, 10^-2, 10^-3 gives onsets 232804, 22463, 4097, 436, using the floors 1/64, 1/32, 1/16. The allowed total K/n numerator is 0.87 (N=64), 4.7 (160), 29 (1000), 247 (4096).

**Actual corner.** The "+16" in [L/3+16] must be at most 1.09 (N=41), 1.78 (100), 4.29 (1000), 7.83 (10^4) or 12.4 (10^5). It is built from 7/2+5/2+3 (regular sums A1, A2, A3) + 3 + 3 (sine channel) + 1/100 (C07 §3–4).

## 3. Ranked proposals

Provisional IDs: `IDEA?argmax-bridge-claude-I01..I05`. No final IDs are assigned (ALLOCATIONS refresh is Codex/root's).

### P1 (rank 1) — `IDEA?argmax-bridge-claude-I01`: degree-free validated model plus phase-local error constants on the full diamond

Aliases: hybrid onset; validated phase-only margin; one-model full-diamond comparison; computer-assisted constants for C06/C08/C13.

1. **Target, domain and distinction.**
   - **Target:** prove, for every integer n≥N1 with N1 aimed at ~10^2–10^3 (far) and ~10^3–4·10^3 (near noncorner), both parities and the full closed signed diamond ρ≤π:
     |S_n(α,β)−M_far(α,β;log n)| ≤ E(α,β;n) := C(B)·(L+1)/n + C'(B)/n² + ε0(B),
     with the constants computed once per phase box B by validated (Arb or MPFR interval) evaluation of the **degree-independent** quantities in the C06 decomposition. These are the sup/variation of A, W and V on cells, the cancellation and single-pole terms, the endpoint residual Q, the exact h_R/g_R tails, and b_full and C_far. Then check, with exact rational arithmetic per box, m(B;L) − 2·E > floor for all L ≥ log N1. The leading-L coefficient (4u/π²) is positive away from the origin, so this is a one-variable polynomial-in-L check.
     - Far use: Λ_c − S > 0 on ρ≥ρ0.
     - Near-noncorner use: S − Λ_c ≤ [M−M(0,0)] + E(α,β) + E(0,0) < defect floor (1/64, 1/32 or 1/16).
     - Corner value: a validated lower Λ_c(n) ≥ (4/π²)L²+b_cL+1.84616 − c_Λ(L+1)/n replaces d(n).
   - **Closest predecessors:** C08's undeveloped "validated fixed-domain enclosure" alternative (C_far≤5/2 only), IDEA-336 (explicit E,d,f), and C13 itself.
   - **Distinction:**
     1. Every constant on both the margin side and the error side becomes phase-local and is computed from n-independent functions. The one computation covers all n≥N1, with no per-degree work.
     2. The far model is used on the near domain too, against the projected defect, so no near-model increment is needed for noncorner centers.
     3. (R,δ) become proof parameters chosen per degree range while the model function stays fixed.
   - **Distinction falsifier:** if M_far depends on (R,δ) beyond O(L/n), point 3 fails. If the C06 decomposition's components each carry a true floor, point 1 cannot beat that floor.
2. **Scoped failures and assumptions.**
   - PD-N132 (the a·b_n form) does not apply: the L-term is kept. PD-N079 (primitive-only corner maximality) does not apply: actual corners are excluded and handled by P4. C01-near-quadratic does not apply: the α^{3/2} cusp is inside M, which is evaluated, not modelled quadratically. The C08 row-box obstruction does not apply: there is no per-degree enumeration.
   - **Assumptions:**
     - (i) The model is (R,δ)-free in the limit. Measured agreement to ~10^-5 supports this.
     - (ii) The C06 BV and quadrature pieces admit a second-order (midpoint/Euler–Maclaurin) remainder with δ adaptive, so that h²∫|f''| ~ L/(n²δ²) replaces the first-order h·Var ~ 255L/n at δ=1/100.
     - (iii) The ~10^-3 a=0 discrepancy (§2.4) is either an artifact or is charged as ε0 only near a=0.
   - Obligations: exceptional x mode, collision rows sweeping with phase, central rows, all closed boundaries, both parities, and the closed ρ0 seam. The corner value must be a lower bound valid for every n≥N1.
3. **Cheapest decisive tests.**
   - **T1-a (MEASURED, ≤10 CPU-min).** Instrument the existing C06/N1 decomposition at n ∈ {512, 2048, 8192} and the binding phases (1/4,1/4), (1.38,0), (1.45,1.45) and (π/2,π/2). Print each component's **signed actual value**: endpoint rows minus sinc profiles, mesh, collision, ordinary-interior quadrature, E_n, D_n and Q.
     - *Success:* Σ|component| ≤ 5·(0.4L/n) away from a≈0, and the O(1)-bounded components (Q, 2/(R−1)) are actually ≤ 0.02 at n=8192.
     - *Kill:* the O(1) components really sum to more than 0.3 at n=8192, cancelling only jointly. A componentwise route then cannot reach n≈10^3 and a joint, cancellation-preserving remainder is needed.
   - **T1-b (validated, ≤20 CPU-h).** Arb enclosure of b_full and C_far on a far-diamond box cover, then an exact check of m(B; log 1000) ≥ 0.3.
     - *Kill:* any box with an upper m below 0.05 at L=log 10^4.
   - Precision: 128–256-bit balls suffice. The integrands have integrable log singularities, so use the exact J/I closed forms already in the diagnostic.
   - **T1-c.** Decide §2.4: re-evaluate M at (1.45,1.45) with a tighter quadrature and an exact g_R tail. If the ~10^-3 persists, find which model term is missing at small a.
4. **Effect on the actual gap and full cost.**
   - If C ≤ ~80 (≤200× the measured value), the far case closes at n≥10^3. If C ≤ ~5, it closes at n≈100; C ≤ ~10 gives n≈200; C ≤ ~1.8 gives n=41. If C ≤ ~12, near noncorner closes at n≈4096 (floor 1/16).
   - This removes the far region from every finite certificate. At n32 that region is 280 of 364 leaves (77%).
   - The theorem would then be: global argmax for n≥max(N_far, N_near, N_corner). The corner onset is P4's job. Below N_near the near-noncorner case falls to P3.
   - Missing obligations to carry: the corner-value lower uniform in n, the closed seam ρ=ρ0, the a=0 strip and collision sweeps.
5. **Priority HIGH. First task for Codex:** implement T1-a as a single read-only diagnostic script. Use the existing c06 diagnostic and n1_rows/C06 code, no new model, a cap of 600 CPU-s, and a MEASURED receipt. Then preregister T1-b's box cover and acceptance before any validated run. Do not change C13's proved records. This is a new candidate with its own records.

### P2 (rank 3) — `IDEA?argmax-bridge-claude-I02`: resume IDEA-337 — Taylor models in h=1/n ∈ [0,1/N] for the finite endpoint blocks

Aliases: degree-block endpoint enclosure; h-interval rows; IDEA-337 resumption.

1. **Target and distinction.**
   - **Target:** replace the analytic finite-n corrections of the endpoint blocks by validated Taylor-model enclosures in h over [0,1/N] per phase box. These blocks are the far R=64 rows with error e_rows=(763L+86237)/n+7.08·10^9/n² (the largest single term, 0.22 of the 0.554 at 5·10^5), and the near R=128 block whose C05 Hessian bound is |E_end,ij|<45000/n, giving 11270/n in (18).
   - Each endpoint row is an explicit finite cotangent/sinc expression. After extracting log n and the digamma-type limits, it is analytic in h. One enclosure covers every n≥N, including the limit h=0.
   - **Closest predecessor:** IDEA-337 (deferred until "a precise uniform remainder" exists). C06/N1-06–08/C05 now supply exactly that remainder structure, so its resumption condition is met for the endpoint blocks.
   - **Distinction from IDEA-337:** the Taylor models are applied only to the fixed-R endpoint blocks inside an already proved uniform decomposition, not to the whole near field.
   - **Distinction falsifier:** if the per-row h-derivative enclosures are as large as the analytic per-row 763/n bound.
2. **Scoped failures and assumptions.** IDEA-337 was deferred, not failed, so no obstruction applies. PD-N085 (per-cardinal sign shortcut) is not used. Assumptions: analyticity in h of each endpoint row on phase boxes away from row collisions; collision rows keep their polynomial treatment, and parity is handled as two separate blocks. Caution: near noncorner also needs the rest terms (75(L+1)/n absolute, ×2 in (15)) handled as increments or shrunk about 10×. P2 alone cannot bring the near onset below ~2·10^4. In P1's route the near increment is not needed.
3. **Cheapest test.**
   - First a floating measurement: n·[row_r(h)−profile_r] summed over r≤64 at the binding far phases, and n·|∂²E_end| for the near block at n=10^3 and 10^4, against 86237 and 45000.
   - *Success:* a measured ratio ≤10^-2.
   - Then one Arb Taylor model (order 3 in h, 256 bit) for one far phase box with h∈[0,10^-3].
   - *Kill:* the enclosure of the h-coefficient summed over rows exceeds 10^3·(L+1). That gives e_rows ≥ (L+1)/1 at n=10^3 and cannot support a far onset below ~10^4.
   - Cost: ≤1 CPU-h.
4. **Effect.** This is the dominant error component in both the far and near budgets. Together with P1 it is what moves the near onset from 2.3·10^5 to ≤4·10^3 (§2.5 E row: ×10^-2 is needed). It is not needed for the far case if P1's interior and margin sharpening succeed.
5. **Priority MEDIUM. First task:** the floating per-row measurement above, recorded MEASURED. Write the preregistered Taylor-model contract only after T1-a shows which component dominates.

### P3 (rank 4) — `IDEA?argmax-bridge-claude-I03`: near- and corner-only finite certificates below the analytic onset, with a degree-dependent split radius ρ0(n)

Aliases: far elimination; near-only cover; split-radius optimisation; (c)-route.

1. **Target and distinction.**
   - For n in the residual finite window [41, N1), certify only ρ≤ρ0(n): actual corner orbits and near-noncorner classes. The far region ρ≥ρ0 comes from P1's degree-free theorem, made valid down to n=41 for ρ≥ρ0. Since the measured far margin at ρ=1/2 is 0.21 at n=41 against an error of 0.037, this looks feasible.
   - ρ0 is chosen per degree to balance the far requirement (true margin ∝ ρ0²L²) against the near and corner cost (∝ ρ0² in C05's r²-terms and in box count).
   - **Closest predecessors:** IDEA-454 (three-region common-primitive cover, fixed geometry) and N3-corner-batch (corner square 1/128, n≤128).
   - **Distinction:** removal of the far region from per-degree work through an analytic far theorem valid at small n, plus a degree-dependent split. Falsifier: P1 cannot reach small n for ρ≥ρ0.
2. **Scoped failures.** The C08 Ω(n²w) moving-root enumeration obstruction concerns far whole-box rows, which are removed here. The near cover then contains only the small-|∇S| near region.
3. **Cheapest test.**
   - Zero-compute accounting: tabulate leaves and checker CPU by class in the existing n17/24/32 receipts. At n32 the split is 280 far / 52 near / 32 outside.
   - Then a MEASURED floating near-only pilot with the existing N3 float code at n ∈ {128, 512, 2048} and ρ0 ∈ {1/2, 1/8}, cap 1800 CPU-s.
   - *Success:* projected near+corner cost per degree ≤ 10^3 CPU-s at n=2048. This would make Σ_{41}^{4096} feasible in ~300 CPU-h.
   - *Kill:* box count growing ≥ n, for example corner-annulus boxes forced to width ∝ r². In that case corner work must go through P4.
4. **Effect.** This turns the finite window from "full certificates for every degree" (infeasible beyond ~10^3) into near+corner-only certificates. Remaining obligations: physical admissibility at boundaries, both corners per parity, and the 41–63 window, where the 1/64 floor is unproved (C01/C02 need n≥64) and existing full native certificates are needed. The C10 producer stays deferred until a cost gate is passed.
5. **Priority MEDIUM. First task:** the zero-compute class accounting plus one bounded floating pilot at n=512.

### P4 (rank 2) — `IDEA?argmax-bridge-claude-I04`: sharpen the actual-corner bracket [L/3+16] to [L/3+O(1)] by exact/validated evaluation of C07's regular sums

Aliases: corner-bracket recomputation; exact A1/A2/A3; sine-channel constants.

1. **Target and distinction.**
   - **Target:** λ_n ≤ aΛ_c + [L/3+K0]r² on inward ρ≤1/2 with K0 ≤ 4.3, giving an analytic corner onset ≈10^3. With K0 ≤ 7.8 the onset is ≈10^4.
   - The "+16" is the sum of crude bounds on the three reciprocal sums A1≤(7581/4000)L+21, A2<6, A3<7 (weighted to 7/2, 5/2, 3), the sine channel 3+3 and 1/100. These are explicit finite sums over fixed index sets: compute them exactly (rationally bounded tails) per degree range, or prove sharper analytic bounds.
   - Also replace the crude Λ_c ≥ (2/5)(L+3/2)² with the true Λ_c (measured: the coefficient is about Λ_c/6 ≈ 2 at n=41).
   - **Closest predecessor:** C07/C13 corner comparison (same argument). Variant: constants only. IDEA-460/PD-T227 (Markov) is not used.
   - **Distinction falsifier:** the exact sums are within 20% of the bounds.
2. **Scoped failures.** PD-N079 is irrelevant because this is the actual λ, not the primitive. IDEA-330 "larger zones OPEN" concerns energy-based radii; this is the derivative route. Assumption: the C07 normalisation and strip geometry hold below 10^6. C13 shows they hold from ~5·10^5, and smaller n need the floor checks redone (for example (1−120/n)^-2 and the enlarged-strip count).
3. **Cheapest test.**
   - Floating, then exact, evaluation of A1, A2 and A3 and of the sine-channel sums at n ∈ {10^3, 10^4, 10^5}. Seconds of CPU.
   - *Success:* K0_actual ≤ 4 at n=10^3.
   - *Kill:* K0_actual ≥ 0.1L² − L/3 at n=2·10^4, meaning the C07 triangle-inequality route itself loses. Then the corner below 2·10^4 goes to P3 per-degree corner patches (N3 energy reduction for the tiny square, plus boxes on the annulus).
4. **Effect.** The corner case is probably the binding onset once P1 has removed the far case: its current analytic onset is ≈4·10^5 and needs only a factor ~4 in K0 for ~10^3. This is the cheapest high-leverage item.
5. **Priority HIGH, cheapest. First task:** a MEASURED script that evaluates C07's A1, A2, A3 and sine-channel sums exactly as defined (same index sets R, S, g) at the three degrees. Then a written lemma with rational tail bounds if successful.

### P5 (rank 5) — `IDEA?argmax-bridge-claude-I05`: declared first-order far correction M1/n (order raising) so that crude hand constants suffice

Aliases: next-order asymptotic model; (c1L+c0)/n term; order-raising.

1. **Target and distinction.**
   - Derive analytically M1(α,β;L) = c1(α,β)L + c0(α,β). Likely sources: the log m vs log n and n/m normalisation, the single shared ordinary-row term E_n=2(p+q)H_n/n, the special-row counts and the first h-correction of the endpoint rows.
   - Then prove |S_n − M_far − M1/n| ≤ K·L²/n² (+ε0 near a=0) with crude K. A K up to ~10^6 then still gives far onsets ~10^4 without validated numerics.
   - **Closest predecessor:** the C06 model plus IDEA-459 (corrected profile, deferred).
   - **Distinction:** one more asymptotic order instead of sharper constants at the same order. This is a **new model term**: it must be openly registered and is not a silent second correction. It concerns the far model, not the one-correction near model.
   - **Distinction falsifier:** a residual after M1 that does not decay faster than L/n.
2. **Scoped failures.** PD-N132 is respected. Risks: collision rows make M1 piecewise in phase, and the a=0 discrepancy (§2.4) shows the model already has a non-decaying ~10^-3 term there.
3. **Cheapest test.** Compare an analytic c1 with the fitted c1 = 0.385, 0.358, 0.087 at (1.38,0), (1/4,1/4), (1,1), and check that n²·residual stays bounded on n=512..8192. *Kill:* a mismatch >10^-2 or an unbounded n²·residual. Cost: minutes.
4. **Effect.** This is an alternative to P1/P2 for the far case if validated numerics stall. It does not help the corner case.
5. **Priority LOW-MEDIUM. First task:** only if T1-a shows the componentwise route is cancellation-limited.

## 4. Retained, duplicate, failed and deferred candidates

| Candidate | Verdict | Scoped reason / evidence |
|---|---|---|
| (a) Sharpen only the E_far terms of (23), keeping C13's margin side | **failed (MEASURED planning scope)** | Every E_far term set to 0 still leaves the far onset at 131044 (§2.5). Not a theorem rejection; superseded by P1, which also sharpens the margin side. |
| Raise R/δ at fixed proof constants | equivalent to part of P1 / P2 | The C13 record excludes this from C13's scope. It is folded into P1(3) as proof parameters. |
| (b) Whole-S degree-block certification in h=1/n | duplicate of IDEA-337 (deferred) | Resumed only for the endpoint blocks as P2. A whole-field version still lacks a uniform remainder below defect level at small n. |
| (d) Monotonicity or comparison in n at fixed phase (Λ_c−S_n increasing in n) | **deferred** | The sampled worst-phase margin increases (0.21→0.79), but there is no proof mechanism. IDEA-321's failure concerns within-n cell ordering and does not apply. Resume only with an identity linking S_n and S_{n+1}. |
| (e1) FFT/NUFFT evaluation of cardinal sums | **rejected (equivalent/inapplicable)** | S is a sum of absolute values, so convolution structure is lost. C02 row reduction is already O(n) per point. The cost bottleneck is box count, not point cost. |
| (e2) Chebyshev-grid caching of S across leaves | deferred | |·| kinks and moving collision rows destroy the smoothness needed for interpolation error bounds. Resume only per kink-free box class. |
| (e3) One-sided Lipschitz or derivative box bounds | duplicate | IDEA-320/N3 mean-value forms and IDEA-460/PD-T227. |
| SOS certificate for Λ_c−λ_n ≥ 0 | deferred (as IDEA-338 notes) | Degree n bivariate SOS on |·| sums has no concrete family. |
| Christoffel / Cauchy–Schwarz global bound | rejected | It gives an O(√N) scale against log² n and cannot separate the corners. |
| Markov-inequality corner patch | duplicate | IDEA-460 ≡ PD-T227 (6)–(7). |
| Homotopy in n, two-scale, Remez | rejected as named | No mechanism beyond the existing near/far split (two-scale = IDEA-337/C06 split). |
| Full-diamond use of M_far for near-noncorner (inside P1) | retained inside P1 | Measured error is 0.35–0.38·L/n on ρ≤1/2 (§2.3). Needs C ≤ ~12 at n=4096 (floor 1/16) or ≤ ~2 at n=1000. |
| Validated lower Λ_c(n) ≥ limit polynomial − c(L+1)/n (inside P1) | retained inside P1 | Measured Λ_c minus the limiting polynomial is positive and decreasing (0.027 at n=41). The sharp −1/N remainder is OPEN under IDEA-358, but only a weak form is needed. |

No PD-N is created by these dispositions. All "failed" or "rejected" labels apply only to the stated mechanism and scope.

## 5. Prioritised Codex plan (bounded first tasks; nothing launched by Claude)

1. **P4-T (≤5 CPU-min, MEASURED):** exact or floating evaluation of C07's A1, A2, A3 and sine-channel sums at n=10^3, 10^4, 10^5, giving K0_actual. Gate: K0_actual ≤ 4 at n=10^3.
2. **P1 T1-a (≤600 CPU-s, MEASURED):** signed component audit of the C06 decomposition at n=512/2048/8192 and the four binding phases (incl. a≈0); also T1-c (the a=0 discrepancy). Gate: §3 P1 success/kill.
3. **P1 T1-b preregistration:** box cover, Arb precision, acceptance m(B;log N1) − 2E > 0 and the CPU cap (≤20 CPU-h). Run only after T1-a passes.
4. **P2 measurement:** per-row n·[row−profile] and the near n·|Hessian| against the bounds 86237 and 45000.
5. **P3 accounting:** leaf and CPU class split from existing receipts; then the bounded near-only pilot.

Frozen: all seven C13 records and their proofs, the 2–40 finite theorem and certificates, the C03 checker, the one-correction near model, the 15/15 campaign count, and the PR27 draft state. New work gets new provisional records. No old n≥10^6 or n≥5·10^5 quantifier is extended without a new proof.

Rules 02beaef. Claude Opus 5.5 xhigh, independent idea proposer, interim audit, 2026-11-06.
