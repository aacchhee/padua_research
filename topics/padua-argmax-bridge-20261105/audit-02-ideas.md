# INTERIM audit-02: Claude's own ideas for closing 43–319 (handoff 10, task 3)

Companion to [audit-02-interim.md](audit-02-interim.md). **Claude proposes;
Codex implements.** Claude launched no proposal, no pack case and no
residual-degree job. Everything numerical below is **MEASURED** (floating)
or **ENCLOSED** (rational interval arithmetic) evaluation of the stated
*sufficient allowance formulas* or of the Padua primitive. None of it is a
proof premise, a counterexample or a cost law, and nothing new is claimed
proved. Provisional IDs `IDEA?argmax-bridge-claude-I06..I10` continue I01–I05
of [audit-01-ideas.md](audit-01-ideas.md). They are not final IDs.

## Orchestrator synthesis and review

The idea review (Claude Opus 5.5, instructed xhigh) ran the full novelty
gate before it generated any candidate. The gate covers all 1154 lines of
`state/IDEAS.md` (sha256 `d7ec3aa6…`) with every obstruction and disposition
table, about 45 topic records with hashes, and a mechanism-term search. The
Euler–Maclaurin, Peano-kernel and validated-numerics terms have no
`literature/INDEX.md` record, so no priority is claimed. It is stated
there that the D/E idea and attempt files were read through their
candidate/disposition tables and term hits only, which is a coverage limit.

**Orchestrator check.** I re-ran the combined onset-scenario script from a
copy (`PYTHONPATH=<pylib> python3 combined_scenarios.py`, mpmath 20 digits,
14.7 CPU-s, exit 0; output committed as
`audit-02/code/ideas/root_combined_rerun.out`). It reproduces the planning
table exactly: common onset 320 for the current recipes, 312 with ideal
radial optimisation, 307 with floors ×2, 254 with the outer seam at 1.25,
248 with floors ×4, 195 with all finite-error charges halved, and 120 with
errors ×0.25 and floors ×2. (A first attempt with `python3 -P` exited 1
because `-P` blocks the script-directory imports; that is my invocation
error, not a defect of the script.) This reproduces the **formula
evaluation**; whether the underlying constants can really be sharpened is
exactly what proposals I06–I10 test.

**What I take from it.**

1. **Three regions bind together near 300–320.** With the current
   constants, half-near closes at n=320, the annulus/wide region at 304 and
   the outer region at 307. The corner (239) and the far region (181) do
   not bind. Ideal radial optimisation alone moves only the half-near and
   wide regions (to 312 and 279). The same uniform shrink factor of the
   finite-n error charges closes all three regions: about 0.74–0.79 for 256,
   0.52–0.56 for 200, 0.36–0.40 for 160 and 0.24–0.29 for 128. Better
   floors alone stall at 307.
2. **The true relative error is far below the charges** (MEASURED proxy
   E_true = ΔS − ΔM_far: at most 2.3·10⁻³ at the binding phases for n≥128,
   against charges of 0.16–1.40, a factor of about 480 to 10⁵). The lever is
   therefore a much sharper relative finite error (I06), not new floors or
   models. This is the same picture as my audit-01 finding that the proof
   constants, not the models, set the onset.
3. **Certifier CPU is not the bottleneck** (planning projection from
   committed finite accounts: 6.3–9.4 CPU-s per pass at n=41–160 and about
   7.5 CPU-s at 511, so about 1.3–1.5 CPU-hours for all 280 cases, primary
   plus fresh). This is a projection from a few finite measurements, not a
   law: degrees 161–191, where neither the n≥192 nor the n≥256 premise
   applies, may need larger trees or fail (audit-02 PA3). If it holds, the
   operational risk of the one-shot Syvert2 run (audit-02 PA1–PA4), not CPU,
   is what matters. Running all 280 cases on a local machine is recorded
   in the review only as an operational option for AC, not as an idea.
4. **A finite floor barrier below about 90**: Fh(n,0)=0.1282−7.44/n−259/n²
   is negative for n≤82, so the analytic route cannot reach the low
   degrees whatever the other constants do. The window 43–62 stays a
   finite-certificate job in any case.

**Ranking I endorse (this follows the review's order).**

1. **I06 EM2-box**, the highest leverage: replace the first-order BV charges
   of the E14 relative error by an exact first-order Euler–Maclaurin term
   plus a validated degree-free second-order remainder on phase boxes
   (1/32 ≤ ρ ≤ 5/4). T1 is a MEASURED check (at most 600 CPU-s) of the four
   signed telescope components at eight probe phases; it fails if any
   component is at least 0.1 with cancelling partners. It revives my
   audit-01 P1, which D01 killed on mesh/interior cancellation in the old
   C06 decomposition; this version works on the E14 telescope and checks
   component sizes first. Planning effect: onset about 195 if errors are
   halved (removing 125 of the 273 open degrees), about 120 at ×0.25 with
   floors ×2 (removing 198).
2. **I07 outer seam re-anchoring** (ρ1 ≈ 6/5–13/10) with the E14-wide
   relative bounds extended to ρ≤5/4; the no-root margin identity
   a−P/2=√2·cos(δ/2)·cos(ρ/2+π/4) shows this proof route cannot reach π/2
   (margin 0.349 at ρ=1, 0.183 at 5/4, 0 at π/2). Alone it removes no
   degree; it is a necessary outer complement (254 together with floors ×2).
3. **I08 cross-degree templates plus a floating risk map**: one tree per
   degree band (43–62, 65–158, 161–255, 256–319) verified at each degree,
   and a producer-only floating dry run before the one-shot run. It removes
   no degree analytically but de-risks the closure of all 273 and cuts the
   review burden. The dry run needs an explicit root release; I did not run
   it. The committed D38 trees are byte-identical at 159/160/511/512 and at
   63/64, which is the supporting evidence.
4. **I09 phase-aware full-band floor** (floor target 0.2 with finite losses
   at most 3/n; the N5-05 obstruction covers only the phase-blind envelope
   at the 1/4 level). The only lever on the n≤82 barrier; removes no degree
   alone.
5. **I10 endpoint-complete origin sign** (E_n(0)≥−ε via a 1D
   Euler–Maclaurin expansion of the corner value plus a finite exact range).
   Outer 307→277 and far 181→166; alone removes no degree.

**Review cautions for Codex.**

- Order the work by cost: I06 T1 first (bounded MEASURED test), then I07's
  kill test (fails if the relative-bound inflation exceeds 1.5), then I08's
  template check, which is analysis of already-committed receipts.
- The planning scenarios assume improvements that have not been proved.
  Report an onset only if a proof exists; an onset below 320 is a new
  theorem, not a rescaling.
- Keep all frozen records, PD-T271 and the P1–P4 findings as they are. Any
  change to the pack source changes its identity (audit-02 PA1–PA4).
- Fix the PA1–PA4 pack decisions first if the Syvert2 run is still the plan.
  The ideas above do not replace that decision, and I08's dry run is
  complementary to a dress rehearsal.

---

# Idea review (gate, measurements, proposals, retained candidates)

The full idea review follows as drafted by the ideas subagent. The synthesis
above records the orchestrator's review. Section numbers are local to this
part. The scripts and outputs it lists are committed under
`audit-02/code/ideas/`; its path prefix names the auditor's scratch
directory, which is ephemeral.

Rules 1b6aa31. Branch `codex/padua-argmax-bridge-20261105`, read-only head
`1b6aa31ae759022ce89bb8a3be70a881790e259f`. Role: independent idea proposer inside
the INTERIM Claude audit; Claude proposes, Codex implements. Model: Claude Opus 5.5,
effort xhigh (the WORKFLOW row for novel mechanisms). 2026-11-07.

Nothing here is proved unless a line says so. Number labels:

- **MEASURED**: binary64 or mpmath floating evaluation, with no enclosure.
- **ENCLOSED**: rational interval arithmetic, with transcendental base values enclosed by `mpmath.iv`.

Both kinds evaluate the stated *sufficient allowance formulas*, or floating
values of the Padua primitive. They are not proof premises, counterexamples or
cost laws. No git state was changed and no repository file was edited. No pack,
Syvert2, native-certifier or residual-degree job ran. Provisional IDs
`IDEA?argmax-bridge-claude-I06..I10` continue I01–I05 of audit-01-ideas. They
are not final IDs.

## 0. Bottom line

1. **Three regions bind together near 300–320 with the current constants.** I
   transcribed the E14/E13/E15/E12 formulas exactly. The transcription
   reproduces every paper constant (§2.1). With it, the literal recipes first
   close at:
   - half-near, n = 320;
   - annulus/wide [1/2, 1], n = 304;
   - outer (E13, [1, π]), n = 307.

   The corner (E12) closes at 239 and far ρ ≥ π/2 (E15) at 181; neither binds.
   Ideal radial optimisation (exact u, exact x^{3/2}, the E11 majorant, an exact
   segment maximum) moves only the half-near region, to 312, and the wide
   region, to 279. The outer region is unchanged: the E13 gate is already exact
   in v.
2. **The binding constant is the finite-error charge in all three regions, and
   all three need the same shrink.** The uniform factor needed on every
   finite-n error charge (slopes, C4, origin allowance, Cb/Cs/Cl/KD) is:

   | Target N | Required factor | Common onset if achieved |
   |---|---|---|
   | 256 | 0.74–0.79 | — |
   | 200 | 0.52–0.56 | ≈195 |
   | 160 | 0.36–0.40 | — |
   | 128 | 0.24–0.29 | — |
   | ×0.25 with floors ×2 | — | ≈120 |

   Improving the floors alone cannot go below 307, and the outer region does not
   respond to floors (§2.5–2.6).
3. **The true relative error is far smaller than the charges (MEASURED proxy).**
   The proxy is E_true = [S_n(φ)−S_n(0)] − [M_far(φ)−M_far(0)]. At the binding
   phases it satisfies |E_true| ≤ 2.3·10⁻³ for n ≥ 128. The E14 charges there are
   0.16–1.40, a factor of about 480 to 10⁵. n·|E_true|/log n stays at or below
   0.09 for n = 64…2048. The completed-model part of the E14 bound is
   comparatively tight; it loses about 0.04 at the binding phase. So the lever
   is a much sharper relative finite error, not floors, seams or models (§2.7).
   That is my rank-1 proposal, I06.
4. **The finite route is cheap.** Committed D38 and hybrid accounts give 6.3–9.4
   CPU-s per pass at n = 41–160, and 7.4–7.5 CPU-s at 511 in the hybrid (zero
   actual calls). A planning projection for all 273+7 cases × (primary+fresh) is
   **about 1.3–1.5 CPU-hours** in total. This is a projection, not a law. On
   these numbers, certifier CPU is not the bottleneck. Remote provisioning,
   one-shot failure risk and result review are. My cost proposal (I08) therefore
   targets risk and review. It does not target point timings.
5. **Exact template evidence.** In the committed D38 receipts the D36 tree
   preorder strings are byte-identical at n = 159/160/511/512 and at n = 63/64.
   The tree at 42 refines the tree at 63 in two places (47 against 39 internal
   nodes). A few band templates could therefore cover the open window (I08).

Ranked proposals (§3): **I06** EM2-box relative error (highest leverage). **I07**
outer-seam re-anchoring at ρ1 ≈ 5/4 with a wide-relative domain extension.
**I08** cross-degree template verification plus a floating risk map. **I09**
phase-aware full-band floor. **I10** endpoint-complete origin sign. Their
combined planning effect is in §2.6.

## 1. Novelty gate (completed BEFORE any candidate below)

### 1.1 Files read (sha256 prefix, bytes; full unless noted)

| File | sha256[:16] | bytes | Coverage |
|---|---|---:|---|
| AGENTS.md | c44a76f138fce01f | 3572 | full |
| agents/WORKFLOW.md | 65e6b7268f4df4c9 | 32582 | full |
| agents/claude/CLAUDE_ROLES.md | 35c6146f23712d7b | 5754 | full |
| templates/IDEA.md | 38e6a12c923170ed | 1507 | full |
| **state/IDEAS.md** | d7ec3aa6cf36f72e | 312947 | **full, 1154 lines, nine segments**; every heading, alias column and obstruction/disposition table, incl. PR17/PR19/T2–T4/PR25 Padua argmax rows |
| literature/INDEX.md | 1f6f2acea05a6c65 | 327653 | grep only (attribution) |
| results/padua-argmax-bridge-20261105.md | 60cbc1b04cbf3ed3 | 14967 | full |
| T/handoffs/10-interim-audit-syvert2.md | 1c275dcd784727fa | 15964 | full |
| T/handoffs/09-post-audit-campaign.md | cbfe6d99dcb9a2f0 | 5219 | full |
| T/audit-01-ideas.md (my P1–P5) | cb5929c090612def | 35542 | full |
| T/response-01.md | 5fb9c24a4c314c7a | 5360 | full |
| T/campaign-post-audit-20261106.md | 9aea0c52184e3202 | 20590 | full |
| T/report.md | 38fc8e625ca66937 | 33870 | full |
| T/gates.md | 9f29a739d39bb4ee | 14418 | full |
| T/syvert2-delivery.md | 797fe9f5a9b9cd80 | 5395 | full |
| T/independent-checks-final-hybrid-engine.md | f812fd447e8d2868 | 51294 | lines 1–130, 600–800 + cost grep |
| T/margin-anatomy.md | 47039e201cd87b48 | 8733 | full |
| theory/E14-assembly320, -halfnear320, -annular320, -outer320, -wide-signed-outer | 1aaf07a8…, 3def6d97…, f92a3003…, 2bf4f411…, a7f7cd50… | 12425/9548/9198/6241/15112 | full |
| theory/E13-joint-radius-outer | 1cb337046660db65 | 16074 | full |
| theory/E12-corner256, E12-assembly256, E12-assembly256-obstruction | 28c266ee…, af72b447…, 19837168… | 10631/2983/6365 | full |
| theory/E08-allocation-obstruction | 1f33d69a6d19f161 | 7247 | full |
| theory/E09-assembly384 | 4897a470a23637db | 16398 | full |
| theory/E15-analytic-far192 | a3aaf0c23f897e39 | 14634 | full |
| theory/E02-assembly768 | a07b76b3967ecb55 | 32963 | lines 140–259 (floor functions (8), Rad (12)) |
| theory/E01-near-frontier | 6632e54cbb3cd36f | 19887 | lines 1–140 (floor definitions) |
| theory/E03-unified-error | 8e4dcc05b6347433 | 15322 | lines 1–60 (cusp PD-N) |
| theory/E05-cusp-aware-error | b45ae2b2c916e617 | 16736 | grep (microscopic cusp result) |
| theory/E12-signed-outer-coupling | a211b5db5bfc25c8 | 16873 | lines 1–80, 160–260 |
| theory/D37-relative-wide | b769b74207377e5e | 23595 | lines 1–90 |
| theory/D39-cost-and-coverage, D38-calibration-global | 4b53ce1a…, 9db5bd87… | 32802/32159 | D39 lines 1–150; D38 tables |
| theory/N5-large-budget (PD-N N5-05) | 0e86fe06ccf8845c | 12417 | lines 1–40 |
| ideas/E14-assembly320, E15-analytic-far192 | f03d0f6e…, 6631e7c1… | 10692/5942 | full |
| ideas/E02-paired-outer, E12-signed-outer-coupling | 26173788…, a905be8d… | 6142/11408 | P2/P3 rows full; rest grep |
| ideas D30, D24, E13, E04, D29, E01-near-frontier, C02-defect, C01-allclass, E05, D13-relative-remainder, E08-origin-lower, E03-unified, D06 | see §1.3 | — | full candidate/disposition tables (grep of `^\|`/Candidate/defer/kill lines) |
| novelty-gate-N1…N6, -baseline | 0f5ff96a…, …, 19a6e49b… | — | term grep |
| code/post_audit_D01_far/model.py | 6b97477fe05cf03d | 3772 | full (used read-only) |
| effective-2 code/phase_probe.c | 692d4afd89d3bbda | — | lines 1–45 (copied and compiled in scratch) |
| evidence/post_audit_D38/primary-*.json, *-account.json | — | — | parsed read-only (tree strings, CPU) |

(T = topics/padua-argmax-bridge-20261105.)

**Coverage limit.** About 120 D/E idea and attempt files exist. Not every body
line was read. I read the two whole E14/E15 ideas, the candidate/disposition
tables of the shortlisted records and every mechanism-term hit listed in
§1.2. No exhaustive-novelty claim is made.

### 1.2 Searches (rg/grep, case-insensitive, over ideas/ attempts/ theory/ novelty gates, LOG, audit-01*)

- Degree comparison: `monoton* in (n|degree)`, `n+2`, `S_{n+1}`, `consecutive degree`,
  `between degrees`. Hits are scalar allowance n-directions only. There is no
  degree-to-degree identity.
- Degree blocks: `degree[- ]block`, `interval of degrees`, `batch* degrees`. Hits:
  audit-01-ideas (b) and D01 only.
- `Taylor model`, `in 1/n`, `h=1/n`, `continuous/real degree`. Hits: N1/N3/C05/D07
  endpoint h-blocks and IDEA-337 (deferred).
- Tree reuse: `tree reuse`, `same topology`, `fixed topology`, `template tree`.
  **No hits.**
- Projections: `both/two projections`, `add* projections`, `joint defect`. Every
  hit says "projections are never added".
- Origin sign: `E(0)>=0`, `origin nonnegativ`. E08-origin-lower lists it as
  DEFERRED.
- Quadrature order: `Euler–Maclaurin`, `second-order`, `Peano kernel`, `Bernoulli`,
  `second difference`, `midpoint`. Only first-order BV midpoint bounds
  (C06/D05/D07/D37/E14) are used uniformly. Exact first-order plus O(m⁻²) terms
  appear at FIXED phase in E12-A and at the fixed origin in E08. The
  second-difference Shift appears in E02.
- Analytic leaves: `analytic leaf`, `analytic_far`, `per-degree analytic`. Only the
  fixed E15 region n ≥ 192, ρ ≥ π/2 and corner256 in the hybrid engine.
- Seams: `seam`, `split`, `anchor`, `rho1`, `u1`. Splits at 3/4 (D24/D30). E13 is
  anchored at ρ = 1. E13-P5 "finite-domain transfer not pursued".
- Floors: `full-band`, `floor`, `limit integral`. Hits: N5-05 phase-blind quarter
  obstruction, C02/D29/E01 selected bands.
- literature/INDEX.md: `euler.maclaurin|peano kernel|bernoulli|taylor model|validated|interval arith|midpoint|quadrature error`
  gave **no hit**, so there is no LIT record. Padua attribution goes to
  LIT-301/312/313/330/366. These are standard numerical-analysis tools, and no
  priority is claimed.

### 1.3 Shortlist (closest predecessors) and binding obstructions

| Entry | What it fixes for these proposals |
|---|---|
| E03-unified (PD-N): the complete error has a genuine ℓ_n\|α\| linear cusp, nℓ_n = (log n)/π + O(1); no uniform Cρ/n + KHρ²/n bound | I06 must keep ℓ_n\|α\| inside its first-order term and stay off a uniform quadratic through the origin |
| E05 cusp-aware (microscopic domain); D13 full relative target OPEN; D13 idea "differentiate moving roots as smooth: not pursued" | I06 is a box-wise, computer-assisted route to a weaker (box-dependent) form of the OPEN target |
| E12-A: fixed-phase T_n = −(2p/π)L/n + O_φ(1/n), via subtraction of initial logarithms then O(m⁻²) midpoint (E12 (11)–(13)); "not uniform in phase" | I06 makes exactly this structure box-uniform with validated degree-free remainders |
| E02-P3 (DEFERRED): pair L/R profiles before BV to cut the 20 log m/π charge | I06 differs: it computes first-order terms instead of bounding them by signed BV |
| I01/P1 (mine) and D01 kill: componentwise first-order validated constants on the old C06 fixed-R decomposition fail through large mesh/interior compensation | I06 works on the E14 telescope (six fixed rows), with a component-size gate first |
| IDEA-337/I02 (h-Taylor, deferred) | Degree blocks (R-g) and I10's 1D version |
| E13 (anchor ρ = 1, joint geometry), E13-P5, D24/D30 (seam 3/4), D37 (relative wide to ρ ≤ 1), E04 (wide retained), E14-wide (signed T on ρ ≤ 1) | I07's predecessors; I07 is a larger-domain re-proof, not a transfer |
| E01-F1, C02 dense band, D29 floors, N5-05 PD-N (the phase-blind full-band envelope has limit < 0.2475, below 1/4) | I09 targets 0.2 and is phase-aware, so it escapes N5-05's exact scope |
| E08-origin-lower: "Exact E_n(0) ≥ 0" DEFERRED; abandoned shortcuts Δ_n ≥ 0 alone and PD-T271 promotion | I10 supplies a different resume route; it uses neither shortcut |
| D21/D28 static verifier (one supplied tree at one degree), D36 generic engine, hybrid FREEZE 0d9ce0a5… | I08 is cross-degree reuse; no predecessor |
| PD-N079/IDEA-333, PD-N132, PD-N084–086 (state/IDEAS PR17/19/25) | No proposal uses pure quadratic primitive maximality, the a·b_n form or fixed cardinal signs |
| E08-allocation, E12-assembly256-obstruction (old near/outer allocations fail at 384/256) | They concern old majorants. The §2 recipes reproduce the current accepted E14 allocation; their failures below 320 are planning facts of the same kind, not new PD-Ns |

## 2. Quantitative onset sensitivity (computed here)

### 2.0 Formulas, commands and environment

Exact transcription in `ideas2-code/e14_formulas.py`:

- Scalars: L = log n, H = 1+L, m = n+1. T = (4L²−3L)/π². Da, D, Mesh and
  ebar = D+Mesh+1/n (n ≥ 160) or e₋ (32 ≤ n < 160), per E13 (6). j* = 23/250.
- A4, C4, JN, kNx = [(19/2)H + (23/3)L + 677/10]/n + 82/n², and
  kNy = kNx + (17L+27)/n².
- JW, kWx = [(19/2)H + (23/3)L + 155/2]/n + 152/n², and the old E04 kWy_old (used by
  E12). KD.
- Floors Fn/Fs/Fh/Fw from E02 (8) (valid n ≥ 64): Fh up to rB = 21/40, Fw up to
  π/4.
- Recipes:
  - Half-near: E14-halfnear §5, i.e. tangent √x ≤ (5/4)x+1/5,
    u ≥ (47/192)(x²+y²), U ≥ T−ebar+A4+JN/8+j, whole-line (e, f, g), β0 = 1679/8000.
  - Wide: E14-annular §2, i.e. √x ≤ x+1/4, u ≥ 11(x²+y²)/48, (5/12)x^{3/2}.
  - Outer: E13 (2)/(7)–(9) with j*, t* = 221/500, origin allowance e0.
  - Far: E15 (5)/(21) at u0 = 7/24.
  - Corner: E12 (4)–(12).
- "Ideal" variants keep the same finite charges but use exact u, the E11
  majorant κp^{3/2}/√a minus the proved Bbeta lower bound q·b/π²[log(1/b)+3/2]
  (E14-halfnear (2)), exact rJN/rJW, and an exact segment maximum on a grid.

Commands, run in the `ideas2-code/` folder with `PYTHONPATH=../pylib`: Python
3.13.18, mpmath 1.3.0, numpy 2.5.3, scipy 1.18.1, cc -O2.

```
python3 validate_transcription.py      # §2.1
python3 onset_scan.py all              # §2.2 -> onset_scan_out.json
python3 fraction_recipe.py 200 250 300 320   # §2.3 -> fraction_recipe_out.txt (ENCLOSED)
python3 slope_parts.py                 # §2.4
python3 exchange_rates.py              # §2.5 -> exchange_rates_out.json
python3 structural_scenarios.py; python3 reanchor_outer.py; python3 combined_scenarios.py  # §2.6
cc -O2 -std=c11 -shared -fPIC phase_probe_copy.c -lm -o probe.so
python3 looseness_probe.py 128 200 256 320; python3 scaling_probe.py; python3 origin_probe.py  # §2.7
```

All exited 0. The total CPU of every run is about 70 s, well under the 20
CPU-min cap.

### 2.1 Transcription check (MEASURED)

At the E14/E13/E15/E12 bases every stated paper bound is satisfied on the
correct side:

- **n=320:** T 11.7319 > 293/25; ebar 0.15407 < 249/1600; C4 0.013537 < 677/50000;
  kNx 0.55150 < 11031/20000; kNy 0.55272 < 0.5528.
- **Half-near quadratic:** e 1.34483 > 1.3429; f 0.594190 < 0.59428; g 2.4907e-4 < 1/4000.
- **Wide coefficients:** kWx 0.58281 < 583/1000; kWy 0.58403 < 117/200.
- **Outer:** Cb 0.81176 < 209/250; Cs 0.68278 < 71/100; Cl 0.33469 < 7/20; Gb 0.11100 > 3/40;
  K 10.830 > 10; A 1.34578 < 7/5; F 0.06919 > 13/500.
- **Far, n=192:** CEhat 1.598 < 17/10; G 0.19895 > 79/2000.
- **Corner, n=256:** δA 0.57024 > 2293/4200; FA 0.16395 > 2729/21000; δD 1.0117 > 881/1000;
  FD 0.19914 > 49/1000; M 25.393 < 26.

With exact floors the literal half-near recipe gap at 320 is **2.45·10⁻⁴ at
r = 0.259**. The paper certifies more than 1/20000 after relaxing to Lh.

### 2.2 Margin versus n, current constants (MEASURED)

Values are the minimum over r of floor minus upper, at the binding r. For the
wide region it is min over r ∈ [1/2,1] of max(−P, floor−P). For the outer region
it is F. For far192 it is G(7/24). For the corner it is min(FA, FD/2).

| n | half-near recipe | half-near ideal | wide recipe | wide ideal | outer F | far192 G | corner |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 128 | −0.453 @.500 | −0.437 | −0.669 @.90 | −0.580 | −1.970 | −1.211 | −1.060 |
| 160 | −0.291 @.500 | −0.275 | −0.393 @.685 | −0.339 | −1.336 | −0.399 | −0.636 |
| 192 | −0.178 @.475 | −0.164 | −0.247 @.54 | −0.207 | −0.898 | +0.199 | −0.328 |
| 200 | −0.156 @.450 | −0.143 | −0.221 @.53 | −0.181 | −0.808 | +0.326 | −0.264 |
| 224 | −0.104 @.394 | −0.095 | −0.153 @.53 | −0.112 | −0.571 | +0.665 | −0.091 |
| 250 | −0.064 @.344 | −0.056 | −0.091 @.53 | −0.054 | −0.358 | +0.978 | +0.067 |
| 256 | −0.057 @.334 | −0.049 | −0.079 @.50 | −0.042 | −0.314 | +1.044 | +0.100 |
| 280 | −0.031 @.300 | −0.025 | −0.036 @.50 | +0.002 | −0.154 | +1.287 | +0.221 |
| 300 | −0.014 @.278 | −0.008 | −0.005 @.50 | +0.034 | −0.037 | +1.468 | +0.311 |
| 320 | +0.00024 @.259 | +0.0053 | +0.024 @.50 | +0.063 | +0.069 | +1.634 | +0.393 |
| 384 | +0.032 @.212 | +0.036 | +0.098 @.50 | +0.139 | +0.348 | +2.083 | +0.613 |

**First closing integer n (current constants):**

| Region | First closing n |
|---|---|
| half-near recipe | **320** |
| half-near ideal | 312 |
| wide recipe | **304** |
| wide ideal | 279 |
| outer E13 | **307** |
| far E15 | 181 |
| corner E12 | 239 |
| corner E12 with E14-wide kWy, exact q0/Ec | 237 |

Three regions bind within 16 degrees of each other.

### 2.3 Exact Fraction enclosures of the literal recipes (ENCLOSED)

The output is `fraction_recipe_out.txt`. Interval widths are below 10⁻¹⁰, so
one value is shown. "Half-near" is min over [1/8,1/2] of (Fh − upper), the
binding middle class, at the stated r. Fn and Fs are larger there: for example
at n = 200, r = 0.3, Fs ≈ 0.095 against Fh ≈ 0.059.

| n | half-near gap @r | wide: floor−P at r=1/2 / P(3/5) | outer Gb / A²/(4K) / F | corner FA / FD/2 |
|---:|---|---|---|---|
| 200 | −0.15591 @0.451 | −0.21212 / +0.23892 | −0.72285 / 0.08465 / −0.80750 | −0.15763 / −0.26367 |
| 250 | −0.06419 @0.344 | −0.09098 / +0.09538 | −0.29859 / 0.05950 / −0.35808 | +0.13462 / +0.06659 |
| 300 | −0.01382 @0.279 | −0.00462 / −0.00845 | +0.00921 / 0.04569 / −0.03648 | +0.35264 / +0.31100 |
| 320 | +0.00024456 @0.259 | +0.02364 / −0.04273 | +0.11100 / 0.04201 / +0.06919 | +0.42604 / +0.39285 |

Two readings:

- **Outer at 300:** the failure is entirely the square-root/Young term A²/(4K);
  Gb is already positive.
- **Corner at 200:** with the accepted E14-wide kWy instead of kWy_old, FA
  becomes +0.0375. FD/2 then binds through the absolute CEbar.

### 2.4 Which terms make up the slopes (binding constants)

The per-unit-ρ slope kNx at n = 320 / 256 / 200 / 160 is 0.552 / 0.675 / 0.843 / 1.030.
It splits as follows:

| Component | Formula | Share |
|---|---|---|
| Tout | ((23/3)L+47)/n | **52%** |
| ordinary rows | (8H+10)/n | **36%** |
| retained rows | ((3/2)H + 16/5 + 7)/n + 82/n² | 12% |
| Rmesh | 1/(2n) | ~0% |

kWx splits in nearly the same proportions: 51/34/15%.

The ρ-independent offset C4 = A4+20/n² (0.0135 at 320, 0.0225 at 200) uses
13–27% of the middle-class floor Fh(n, 0) (0.1025 / 0.0846). Within Tout the
pieces are:

- the cancellation integral (20 log m + 175/4)/π ≈ 56%;
- the pole/BV term 33 (wide) / 30 (near) ≈ 36%;
- Rlog ≈ 8%.

The outer gate at 300 is dominated by:

- Cb = 0.861, made of D_env 0.124, G_env 0.365, R6_env 0.356 and M_env 0.016;
- Cs = 0.722, of which the six-row term 1.5(48H+24)/(πn) is ≈ 0.54;
- e0 = 0.163, KD = 0.174;

against the loss u1(T+j*) = 1.413. The worst point is the inner seam:
v* = (A/2K)² ≈ 0.0044, i.e. u ≈ u1.

**Floors at small n.** Fh(n, 0) = 0.1282 − [140·0.97/157 + 400·4837/(1875·157)]/n − 776/(3n²)
= 0.1282 − 7.437/n − 258.7/n². Its losses, mainly the 400Rh/(157n) term, make
**Fh(n, 0) < 0 for n ≤ 82** (Fh(64,0) = −0.051, Fh(96,0) = +0.023). No analytic
onset below about 96 is realistic with the current middle-class floor.

### 2.5 Exchange rates: required shrink of all finite-error charges (MEASURED)

`es` multiplies every finite-n error charge of a region. The model (T, j, Ec)
is held fixed. `fs` multiplies the floors.

| target N | half-near es | (fs=2) | (fs=4) | half-near fs alone | wide es | (fs=2) | wide fs alone | outer es |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 300 | 0.920 | 1 | 1 | 1.19 | 0.986 | 1 | 1.09 | 0.971 |
| 280 | 0.840 | 1 | 1 | 1.45 | 0.897 | 1 | 1.84 | 0.884 |
| 256 | 0.743 | 1 | 1 | 1.91 | 0.792 | 0.895 | 3.17 | 0.782 |
| 224 | 0.616 | 0.846 | 1 | 3.10 | 0.655 | 0.738 | impossible | 0.650 |
| 200 | 0.521 | 0.716 | 0.928 | 4.81 | 0.555 | 0.622 | impossible | 0.555 |
| 160 | 0.363 | 0.502 | 0.648 | 10.1 | 0.394 | 0.435 | impossible | 0.404 |
| 128 | 0.235 | 0.328 | 0.425 | impossible | 0.272 | 0.290 | impossible | 0.291 |
| 96 | 0.090 | 0.131 | 0.173 | impossible | 0.154 | 0.155 | impossible | 0.188 |
| 64 | impossible (Fh<0) | — | — | — | 0.077 | 0.077 | — | 0.097 |

Here "impossible" means that floors alone cannot close the region at that N.
The wide primitive part (r > π/4) has no floor, and the outer region does not
depend on floors at all.

### 2.6 Structural what-ifs (MEASURED; every changed input is HYPOTHETICAL)

- **One-sided origin allowance e0 → λe0.** For the outer gate, λ = 1 / 0.5 / 0.25 / 0
  give closure at 307 / 292 / 285 / **277**. For E15 the same λ give 181 / 174 / 170 / 166.
- **Re-anchored E13 at ρ1** (geometry constants a0 = cos(ρ1/2), u1 = 1−a0,
  p0 = max(sin(ρ1/2), 12/25), P0 = 2√(2u1−u1²)). Closure by ρ1:

  | ρ1 | 1 | 1.1 | 1.2 | 1.25 | 1.3 | 1.4 | 1.5 | π/2 |
  |---|---|---|---|---|---|---|---|---|
  | first closing n | 307 | 270 | 240 | **227** | 216 | 196 | 179 | 169 |

- **Relative wide allowance extended to [1, ρ1]**, with E14 coefficient formulas
  inflated by c, and u ≥ (1−cos ρ_hi)/(2ρ_hi²)·(x²+y²) evaluated at the
  conservative ρ_hi = π/2. Inflation c = 1 / 1.25 / 1.5 gives closure at
  **211 / 248 / 283**. The binding r is just above 1, so the result is
  insensitive to ρ1.
- **Combined common onset** (first n at which all three non-corner regions close):

  | Scenario | n |
  |---|---|
  | S0: current | **320** |
  | S1: ideal radial | 312 |
  | S2: S1 + floors ×2 | 307 |
  | S3: S2 + seam 1.25 (c = 1.25) | **254** |
  | S4: S3 with floors ×4 | 248 |
  | S5: all finite errors ×0.5 | **195** |
  | S6: errors ×0.25 and floors ×2 | **120** |

  The corner closes at 239, so it does not bind S0–S4. S5/S6 additionally need
  the corner below 239. Below roughly 96 the Fh losses bind as well.

### 2.7 True slack (MEASURED binary64 proxy, no enclosure)

E_true(φ) = [S_n(φ)−S_n(0)] − [M_far(φ,L) − M_far(0,L)]. S_n comes from
`phase_probe.c` and M_far from the frozen D01 evaluator. Its fixed-cutoff bias
relative to M∞ is ≤ about 10⁻³ (D01) and tiny near the origin. The E14
relative charge is C4 + kx·x + ky·y − u(A4 + rJ − e0).

| n | (0.15,0.11) | (0.26,0) | (0,0.26) | (0.25,0.25) | (0.3,0.2) | (0.5,0.5) | (0.8,0.2) |
|---:|---|---|---|---|---|---|---|
| 128: E_true / charge | −6.1e-5 / 0.368 | +6.6e-4 / 0.369 | +4.9e-4 / 0.371 | −6.6e-4 / 0.676 | −5.3e-5 / 0.676 | −2.3e-3 / 1.402 | +1.7e-3 / 1.407 |
| 200 | −5.3e-5 / 0.244 | +4.3e-4 / 0.245 | +2.8e-4 / 0.246 | −5.4e-4 / 0.450 | −4.7e-6 / 0.450 | −1.7e-3 / 0.933 | +1.1e-3 / 0.938 |
| 256 | −4.2e-5 / 0.194 | +3.5e-4 / 0.195 | +2.0e-4 / 0.196 | −4.7e-4 / 0.360 | +1.3e-5 / 0.360 | −1.5e-3 / 0.745 | +8.4e-4 / 0.749 |
| 320 | −3.5e-5 / 0.158 | +2.7e-4 / 0.159 | +1.5e-4 / 0.159 | −4.1e-4 / 0.293 | +2.3e-5 / 0.293 | −1.3e-3 / 0.608 | +6.7e-4 / 0.611 |

The ratio charge/|E_true| is 480–96000 (median about 900).

**Scaling.** At four phases and n = 64…2048, n·E_true/log n lies in [−0.086, +0.030].
It is negative except on the α-axis (the cusp direction). At ρ = 1 the charge's
counterpart n·k·ρ/L is 17–20. The E14 model part loses only about 0.04 at the
binding phase: at n = 320, (0.15, 0.11), the bound part is −0.082 against the
true −0.124.

**Origin.** The proxy E_n(0) = Λc − M_far(0,L) is **+0.020, +0.015, +0.012, +0.010,
+0.009, +0.007, +0.006, +0.004** at n = 64, 96, 128, 160, 200, 256, 320, 512.
That is about +0.33·log n/n, against the charged e0 = 0.64…0.10.

### 2.8 Finite-certificate cost and template evidence (committed records, read-only)

**Per-case CPU.** CPU through summary per pass, primary/fresh, from the D36
engine D38 accounts:

| n | 42 | 63 | 64 | 159 | 160 | 511 | 512 | 1024 | 2047 |
|---|---|---|---|---|---|---|---|---|---|
| primary / fresh | 6.78/7.13 | 7.64/6.57 | 6.93/7.39 | 9.09/9.12 | 8.89/9.38 | 17.6/19.4 | 17.2/17.3 | 14.1/13.5 | 24.3/25.2 |

The new hybrid engine is cheaper at 511: 7.35 and 7.53, with zero actual calls.
At 41 it records 6.89/6.29.

**Planning projection** (hybrid, 273 open + 7 known, primary+fresh, using about
7 CPU-s at 43–158, about 9–12 at 161–255 with three actual points, and about 7 at
256–319): **≈ 4.8–5.4·10³ CPU-s ≈ 1.3–1.5 CPU-h**. On 40 workers that is a few
minutes. The 67,200 CPU-s envelope is only a ceiling. This projection is not a
cost law.

**Trees.** S/actual calls are 45–64/3 below 256. The D36 preorder strings
(`/tree/preorder`) match as follows:

- byte-identical at 159 = 160 = 511 = 512: `abababababa...b..a..ba...ab...bab....ab...bab....ab..b..bab..b..ab...`;
- identical at 63 = 64;
- 42 refines 63 in two places (47 against 39 internal nodes).

## 3. Ranked proposals

### Rank 1 — IDEA?argmax-bridge-claude-I06: EM2-box, a relative error with exact first-order terms and box-validated second-order remainders

Aliases: singularity-subtracted Euler–Maclaurin on phase boxes; box-uniform
E12-A; computer-assisted relative slope; second-order signed telescope. This
partially **revives my P1/I01**. Three things changed:

- (i) it works on the E14 telescope δ_aE = δ_aE_row + δ_aE_ret + δ_aR_mesh + T_n
  with six fixed rows, not the old C06 fixed-R strip whose mesh/interior
  compensation killed P1 in D01;
- (ii) the first-order term is computed exactly, as E12-A does at fixed phase,
  not bounded by BV;
- (iii) validated numerics are used only for second-order remainders.

**1. Target, domain and distinction.** Fix a finite closed cover of the band
B = {ρ0 ≤ ρ ≤ ρ1}, with ρ0 = 1/32 and ρ1 = 5/4 (I07). It covers both signed
phases, both parities and every coordinate class. Fix a degree N0 (aim 160).
The target, for EVERY integer n ≥ N0 and every box b, each component
X ∈ {δ_aE_row, δ_aE_ret, δ_aR_mesh, T_n} and φ ∈ b, is

  X(φ) ≤ [λ_X(b)·L + γ_X(b)]/m + R_X(b)·(1+L)²/m².

In this bound:

- λ_X and γ_X are box maxima, validated and degree-free, of the **exact
  first-order Euler–Maclaurin functionals** of the singularity-subtracted
  profiles. These are the boundary and hole terms, as in E12 (11)–(13); for
  example the L-coefficient of T at fixed phase is −2p/π plus d-terms. The
  E03/E05 cusp ℓ_n|α| is part of these first-order terms.
- R_X(b) is a validated degree-free bound on the remainder: the variation of
  the derivatives of the subtracted profiles B_X on [0, π] over the box, plus
  the exact digamma/Hurwitz tails of the subtracted singular sums.

The resulting allowance replaces C4 + kNx·x + kNy·y (and kW). The completed
model, the floors and the region ρ < ρ0 keep their current treatment. At
n = 160 the current recipe closes up to ρ ≲ 0.039, which is why ρ0 = 1/32.

How it differs from the closest predecessors:

- E12-A gives a fixed-phase O_φ(1/n), explicitly non-uniform.
- E02-P3 (deferred) uses first-order signed BV after pairing.
- D13/E05 is the uniform analytic mixed target, still OPEN; E05 covers only the
  microscopic domain.
- I01/P1 used first-order validated constants on the old decomposition.

**Separation falsifier.** If on the binding box R_X(b)·(1+L)²/m² at N0 is at
least the current first-order charge of that component, the distinction yields
nothing.

**2. Scoped failures and assumptions.**

- E03's PD-N is respected: there is no uniform quadratic through the origin,
  the cusp is retained, and the boxes stay at ρ ≥ ρ0.
- PD-N079 (pure quadratic primitive) is not used.
- The D01 fixed-cutoff bias does not apply: the target is M∞ and the E14
  telescope.
- The D06 frozen-allowance failure is escaped by a changed estimate order.
- The E12 non-uniformity is escaped only box-wise. No claim is made as the box
  shrinks to the origin.

Assumptions:

- (a) All singular, root-switch (Z = q) and periodic-atom features of every
  profile are phase-dependent but n-independent, and finitely many on each box.
  This holds in the E12/E14 representations.
- (b) The second-order remainder near a feature of width ≳ cρ scales like
  h²/(cρ). This is acceptable for ρ ≥ ρ0 at n ≥ N0, since n·ρ0 ≥ 5.
- (c) PD-T271 and every inherited premise are unchanged.

**3. Cheapest decisive test.**

- **T1 (MEASURED, ≤ 600 CPU-s).** Evaluate the four signed telescope components,
  using the existing D07/D37 operator code, at the 8 phases of §2.7 and
  n ∈ {128, 200, 256, 320, 1024}. *Success:* every |component| ≤ 0.02 at n = 200
  on the binding phases, i.e. within about 10× of the measured
  |E_true| ≤ 2.3·10⁻³. *Kill:* some component ≥ 0.1 with compensating partners.
  The componentwise EM2 then cannot reach ×0.5, and a joint operator must come
  first. Binary64 is adequate for this triage.
- **T2 (MEASURED, ≤ 10 CPU-min).** For the dominant piece, the cancellation
  profile C_s, which carries about 29% of the whole slope, compute
  n²·[X − exact first-order term]/(1+L)² for n = 128…4096. *Success:* bounded by
  50 and non-increasing. *Kill:* growth ∝ n (a missing first-order term) or more
  than 500 on the binding box.
- **T3 (validated, ≤ 2 CPU-h, only after T1/T2 pass).** Arb/MPFR (128-bit)
  enclosure of R_X(b) on the binding box (r ≈ 0.26–0.45).

My own proxy (§2.7) already supports the aim: the true total is 480–10⁵ below
the charges. It cannot decide the kill, because components could cancel.

**4. Effect on the actual gap and Syvert2.** By §2.5–2.6, errors ×0.5 give a
common onset ≈ 195, which **removes 125 of the 273 open degrees (195–319)**.
Errors ×0.25 with floors ×2 (I09) give ≈ 120, which removes **198 of 273**
(120–158 and 161–319) and leaves 75: 43–62 and 65–119. The measured slack allows these factors in principle.
Below about 96 the Fh losses and the corner (closing at 239 with the current
E12, else the hybrid three-point corner) bind. The per-degree pack CPU it saves
is small (§2.8). The main gain is a much smaller computer-assisted range in the
final theorem.

**5. Priority HIGH (leverage); development cost MEDIUM-HIGH.** First task for
Codex: T1 only, as a single read-only diagnostic with a MEASURED receipt and a
600 CPU-s cap. No theorem or record changes.

Template fields:

- Novelty verdict: **variant with difference within documented search**. The
  distinction is box-uniform second-order remainders around exact first-order
  terms.
- Test discriminability: T1 separates "components individually small", where
  EM2 is viable, from "large and cancelling", where a joint operator is needed.
  Neither outcome proves a bound.

### Rank 2 — IDEA?argmax-bridge-claude-I07: re-anchor the outer seam at ρ1 ∈ [6/5, 13/10], with a wide-relative domain extension

Aliases: inner-outer seam shift; anchored E13 at ρ1; wide-relative to
five-fourths.

**1. Target, domain and distinction.** There are two parts.

- (a) Re-prove the E14-wide signed Tout ≤ r[(c1)L + c0]/n + y·db, D37 (3)/(5)
  ordinary/Rmesh and E04 wide retained bounds on the **closed signed diamond
  ρ ≤ ρ1 = 5/4**, with recomputed domain constants.
- (b) Re-anchor E13's joint geometry (1) and gate (7)–(10) at ρ1:
  a0 = cos(ρ1/2), u1 = 1−a0, p0 ≥ sin(ρ1/2), P0 = 2√(2u1−u1²).

Assembly: the wide relative primitive covers [3/5, ρ1], the re-anchored outer
covers [ρ1, π], and E15 already covers [π/2, π] from 181.

How it differs:

- E13 is anchored at ρ = 1, and E14-wide/D37 are on ρ ≤ 1.
- D24/D30 split at 3/4, for the far constant.
- E13-P5 "finite-domain transfer not pursued". This proposal is a new proof on a
  larger domain, not a transfer.

**Separation falsifier.** If the recomputed slope inflation c(ρ1) = new/old is
above 1.4 at ρ1 = 6/5, the gain disappears.

**2. Obstructions and assumptions.** There is an **elementary identity**
(routine, proof in one line): since a = cos(ρ/2)cos(δ/2) and
P/2 = sin(ρ/2)cos(δ/2) (sum-to-product, δ = x−y),

  a − P/2 = √2·cos(δ/2)·cos(ρ/2 + π/4),

and its minimum on a ρ-slice is (1 + cos ρ − sin ρ)/2. That minimum is 0.349 at
ρ = 1 (D37/E14 use 17/64 = 0.266), 0.215 at 1.2, 0.183 at 5/4, 0.152 at 1.3 and
**0 at ρ = π/2**. So D37 §6b's initial no-root margin degrades and vanishes at
π/2. A relative extension *along this proof route* must stop strictly below
π/2; a seam at π/2 for direct use of E15 is excluded for this route, not for the
theorem.

Other recomputed constants:

- a ≥ cos²(ρ1/2) = 0.658, against 49/64;
- t = β/π ≤ 0.398, against 1/π;
- the initial-half arguments stay in (−π, π) because ρ1 < π/2;
- the translated-interval length is π/2 + 2ρ1 < 2π;
- u ≥ 0.219(x²+y²), against 11/48 = 0.229;
- the E11 closed-π/2 model covers ρ1.

E08-allocation (old u-only caps) does not apply, because E13's joint geometry
is used. The inherited PD-T271 dependency remains.

**3. Cheapest decisive test.** Paper first: recompute the roughly 12
domain-dependent constants of E14-wide (V bounds 17/4, 5/4, 5/2, 31/20; holes;
33; D37-6b 175/4 at the new margin; E04 gaps 17/8 and 19/10) at ρ1 ∈ {6/5, 5/4},
and evaluate the resulting inflation c(ρ1).

- *Success:* c ≤ 1.25 at ρ1 = 5/4. The planning scenario then closes the
  relative [1, ρ1] part from 248 and the re-anchored E13 from 227.
- *Kill:* c > 1.5, which closes from 283 or later.

Each scalar check takes under a minute.

**4. Effect.** It removes the outer's own 307 binding, bringing that region to
about 250. **Alone it removes 0 degrees**, because half-near (320/312) and
annulus (304/279) still bind. Combined with ideal radial optimisation and
floors ×2 (I09) the common onset is **254, removing 66 of 273 (254–319)**. It is
also the necessary outer complement of I06, since any onset below about 300
needs it or an equivalent outer improvement.

**5. Priority MEDIUM-HIGH: cheap paper work.** First task: a constant-only paper
note at ρ1 ∈ {6/5, 5/4}, with no job.

Novelty verdict: variant (larger domain plus anchor change) within documented
search.

### Rank 3 — IDEA?argmax-bridge-claude-I08: cross-degree template verification and a floating risk map

This is the certifier cost/risk proposal. Aliases: band template; static
cross-degree cover; producer-free verification; degree-band receipts; dry-run
risk map.

**1. Target and distinction.** Split the open window into bands at every branch
change: 43–62 (D29 F_A), 65–158 (C02 F_B), 161–255 (F_C, three actual points)
and 256–319 (E12 analytic corner). In each band, freeze one D36-midpoint
topology string, namely the producer tree of a band-anchor degree, as the INPUT
METHOD/topology. Every degree in the band then runs only the fresh-verification
path. All S, 13-grid and actual premises are recomputed, with exact predicates.
The fallback to the per-degree producer is declared prospectively, so it is not
a rescue of a failed certified attempt.

Before any Syvert2 run, a **floating producer-only pass at all 273 degrees**
(non-certifying) predicts template validity, tree size and minimum margin.

How it differs: D21/D28 verify one supplied tree at one degree; the pack runs a
per-degree producer followed by a fresh replay. Cross-degree reuse has no
predecessor (§1.2). Evidence: §2.8 byte-identical strings.

**2. Failures and assumptions.** No mathematics changes. The D32/D36
closed-cover implication is degree-generic, and validity is checked per degree.
The heuristic assumption is that leaf predicates relax with n at fixed
normalised boxes; margins grow with n in D38. The band boundaries are forced by
the corner branch at 255/256 and the floor tiers at 63/64 and 159/160.

**3. Cheapest decisive test.** After a root release under AC's existing
authority, a floating dry run with the existing producer, capped at 30 CPU-min.

- *Success:* at least 95% template validity in every band, and minimum floating
  margin at least 10× the arithmetic radius.
- *Kill:* below 80% in any band. The present per-degree producer design is then
  the right one.

I did not run this; it is a numerical sweep that needs its own release.

**4. Effect.** It removes 0 degrees analytically. It de-risks the one-shot,
no-retry closure of **all 273**. Problem bands are found before Syvert2, and
review becomes one topology per band rather than 280 trees. CPU falls modestly:
no producer DFS, and one degree-generic build per band. That is at most about
40% of a total of about 1.3–1.5 CPU-h (§2.8), which is immaterial.

**5. Priority MEDIUM. It is the most directly useful item for actual closure.**
First task: preregister and run the floating dry run. Change the pack only if a
band fails.

Novelty verdict: new within documented search (cross-degree reuse).
Implementation-level.

### Rank 4 — IDEA?argmax-bridge-claude-I09: a phase-aware full-band projected-defect floor (×2 target, lower finite losses)

Aliases: full-band floor; all-row straddling count with the actual numerator;
limit-integral floor with explicit Riemann remainder.

**1. Target and distinction.** For EVERY n ≥ 128, actual r ≤ π/4 (later r ≤ 1)
and every applicable interior-index projection, prove Q ≥ F*(n, r) with:

- F*(∞, 0) ≥ 0.2, against the current min(Fn,Fs,Fh)(∞, 0) = 35/286 ≈ 0.122
  (Fs) and the binding middle-class Fh(320, 0) = 0.1025;
- finite loss at most 3/n, against Fh's 7.44/n + 259/n².

Mechanism: count straddling pairs over ALL physical rows with the exact
phase-aware numerator A(u,v) = a(1+cos v) − (p/2)sin u + (q/2)sin v. Write the
count as a Riemann sum of a degree-free positive limit integrand Q∞(γ, r). Bound
the lattice remainder explicitly. Enclose the limit by validated quadrature and
minimise over the centre angle γ.

How it differs: E01-F1, C02 and D29 use *selected* bands with relaxed
numerators. **N5-05 (PD-N)** kills only the *phase-blind* full-band envelope
(a0 = 15/16, c = 11/15) at the *quarter* level; its limit is below 0.2475, which
exceeds 0.2.

MEASURED context (B1): the true min projected margin is ≈ 0.55 at n = 33–256 for
ρ ≤ 0.1.

**2.** "Projections are never added" is respected (one direction). PD-N086's
fixed cardinal signs are not used. Remaining assumption: the full-band lattice
losses are O(1/n) with smaller constants than the band proof's Rh term.

**3. Cheapest test.** A floating limit-integral computation at r ∈ {0, 1/4, 1/2}
for the worst γ, plus the finite-loss coefficients. This takes minutes.

- *Success:* F*(∞, r) ≥ 0.2 − 0.15r and loss ≤ 3/n.
- *Kill:* limit below 0.15 at r = 1/4, or loss above 8/n.

**4. Effect.** **Alone it is nil:** the common onset moves from 312 to 307,
because the outer region and the wide primitive part bind. It is a combination
component: with I07 the onset is 254/248, and with I06 at errors ×0.25 it is
≈ 120 instead of about 150. It is the only listed lever that removes the
n ≤ 82 barrier (Fh(n,0) < 0).

**5. Priority MEDIUM-LOW.** First task: the floating limit integral. Novelty
verdict: variant with difference (phase-aware full band; escapes N5-05's exact
scope).

### Rank 5 — IDEA?argmax-bridge-claude-I10: endpoint-complete origin sign by a 1D h-expansion plus a finite exact range

Aliases: origin nonnegativity; corner-value 1D Euler–Maclaurin; IDEA-337
restricted to the origin. This partially **revives P2/I02** in one dimension
only.

**1. Target.** E_n(0) = Λc(n) − M∞(0, log n) ≥ −ε(n) with ε ≤ ebar/4, or ≥ 0, for
all n ≥ N0. Start from E08's exact finite identity (Δ_n − κ − (L_n²−1)/m plus the
controlled 1D square error). Expand each 1D cotangent/digamma sum in h = 1/n
with explicit Euler–Maclaurin remainders; after digamma subtraction everything
is smooth. Prove the sign for n ≥ N1 from the expansion. Evaluate the 1D sums
exactly on [N0, N1); this is O(n) per degree with no phase cover.

How it differs: E08-origin-lower DEFERRED this candidate until "endpoint-complete
compensation or another proved sign identity". I10 supplies the resume route by
a 1D validated expansion and a finite exact range. IDEA-337 concerned the whole
field.

**2.** E08's abandoned shortcuts (Δ_n ≥ 0 alone; promoting PD-T271) are not used.
PD-T271 stays as M∞(0)'s constant dependency.

**3. Test.** MEASURED exact evaluation of E_n(0) at n = 32…1024, in under 1
CPU-min. The proxy already gives about +0.33·log n/n > 0.

- *Success:* E_n(0) ≥ 0.25·log n/n throughout.
- *Kill:* any sign change.

**4. Effect.** Outer 307 → 277 and far 181 → 166 (§2.6). The corner δA and δD
also improve. **Alone it removes 0 degrees**, because half-near binds. It
lowers the outer requirement inside I06/I07.

**5. Priority LOW.** First task: the 1D exact evaluation. Novelty verdict:
variant (resume of the deferred E08 candidate by a different route).

## 4. Retained, duplicate, failed and deferred candidates

| Label (IDEA?argmax-bridge-claude-…) | Candidate | Closest prior entry | Escaped / binding obstruction | Kill criterion, outcome and disposition |
|---|---|---|---|---|
| I11 | Exact clipped radial optimisation in E14 recipes: exact u, x^{3/2}, E11 majorant with Bbeta lower bound, segment max | E02 Rad (12); E14 whole-line relaxation | None | MEASURED onset 320→312 (half-near), 304→279 (wide), outer unchanged; **insufficient alone**. Retained minor variant (combination only) |
| I12 | Floors-only improvement | E01-F1/C02/D29 | Outer and wide primitive part are floor-free | MEASURED S2 = 307 (§2.6). **REJECTED: failed (MEASURED planning scope)** as a stand-alone onset lever; no PD-N |
| I13 | Uniform tightening of the existing paper charges (continuing E01–E15) | The E-series itself | — | **equivalent** to the existing program; quantified by the §2.5 exchange rates instead |
| I14 | Corner E12 with the accepted E14-wide kWy and exact q0/Ec | E12-corner256 + E14-wide | None | 239→237; corner not binding. Retained note, no action |
| I15 | True j instead of j* = 23/250 | E06/E07 constants | — | Effect is about u·Δj ≪ uT; negligible. Abandoned |
| I16 | Degree monotonicity, n↔n+1 or n↔n+2 comparison of S_n | audit-01 (d), IDEA-321 (within-n) | No identity linking S_n and S_{n+2} | Identical D38 topologies are geometry, not value monotonicity. **deferred**: resume only with an exact cross-degree identity |
| I17 | Interval-in-1/n degree-block certificates for vertex S values | IDEA-337/I02 | Needs an envelope within about 20× of truth, the same bottleneck as I06 | **duplicate** of IDEA-337 for blocks; deferred until after I06 |
| I18 | Per-degree analytic leaf predicates (E13/E14 recipes evaluated at the actual degree on boxes) | E15-P3; hybrid `analytic_far` | — | Cost value negligible (45–64 S calls/degree; builds dominate). **deferred** |
| I19 | Fewer than 13 mandatory grid samples | D14/D19 norm design | — | Cost negligible. Abandoned |
| I20 | Batched multi-degree invocation with a degree-generic native build | D36 engine | — | Saves at most about 40% of about 1.3–1.5 CPU-h. Folded into I08 (engineering) |
| I21 | P1/I01 componentwise first-order validated constants on the old C06 fixed-R decomposition | I01; D01 | D01 mesh/interior compensation (4.02 vs −4.02 at n = 8192) | Kill stands; **superseded by I06** |
| I22 | Relative-wide extension straight to the seam ρ = π/2 (use E15 directly) | D37/E14-wide | Elementary identity a−P/2 = √2cos(δ/2)cos(ρ/2+π/4) → 0 at π/2 | **REJECTED: failed** for this proof route only (the no-root margin vanishes); I07 uses ρ1 ≤ 13/10. Not a theorem refutation |
| I23 | Sign-pattern (max of signed cardinal polynomials) Taylor with a third-order Bernstein remainder for the noncorner near region | D08/D17/E12 corner technology; PD-T227 | The third-order term Mρ³/6 ≈ 0.073 at ρ = 0.26 (M ≈ 25) consumes the margin; flip terms not uniform | **deferred**: resume with a phase-local norm far below the global M |
| I24 | Seam shift (E13 started at ρ1 > 1) without extending the relative domain | E13 | Leaves (1, ρ1) uncovered | **abandoned** (invalid assembly) |
| — | Operational: run the already-validated hybrid engine for all 280 cases locally (projected 1.3–1.5 CPU-h) | — | — | Not an IDEA (no novelty content); an **AC decision**, recorded once here only |

Each "failed"/"rejected" label applies only to the stated mechanism and scope.
None creates a PD-N here. I22's obstruction is a one-line identity that Codex
may record inside I07's record if it is adopted.

## 5. Recommended Codex sequence (bounded; nothing launched by Claude)

1. **I06-T1** (≤ 600 CPU-s, MEASURED): signed E14 telescope components at the
   §2.7 phases. This decides whether componentwise EM2 is viable before any
   proof work.
2. **I07 paper constants** at ρ1 ∈ {6/5, 5/4}: c(ρ1) and the re-anchored E13
   constants. Cheap, with no job.
3. **I08 dry run** (needs an explicit root release; ≤ 30 CPU-min floating):
   template validity and margins at all 273 degrees. This de-risks the one-shot
   pack whatever happens to the analytic route.
4. Only if I06-T1/T2 pass: the I06-T3 validated enclosure on the binding box,
   then a preregistered box cover.
5. I09 limit integral and I10 1D origin evaluation (minutes each). Use them only
   as combination components.

**What not to do.**

- Do not lower the onset by recipe retuning alone. §2.6 caps that at about 307.
- Do not extend any old quantifier or guard by assertion. In particular, do not
  extend E14-wide past ρ ≤ 1 without the I07 re-proof, or Fh past rB.
- Do not count the planning scenarios as evidence.
- PD-T271, the unwaived P1–P4 chronology findings and every scoped failure
  remain as recorded.

**Note for AC.** On the committed measurements, the finite route closes PD-T099
for about 1.3–1.5 CPU-h of already-validated computation. The analytic
proposals above shrink the computer-assisted part of the final theorem; they
are not needed to close the gap.

## 6. Execution record and limitations

Scripts and outputs are in
`audit-02/code/ideas/ (run from a copy of the scripts; auditor scratch path)`:

- `e14_formulas.py`, `validate_transcription.py`, `onset_scan.py` (+`onset_scan_out.json`)
- `fraction_recipe.py` (+`fraction_recipe_out.txt`), `slope_parts.py`
- `exchange_rates.py` (+json), `structural_scenarios.py` (+json), `reanchor_outer.py` (+json),
  `combined_scenarios.py` (+json)
- `looseness_probe.py`, `scaling_probe.py`, `origin_probe.py` (+jsons)
- `phase_probe_copy.c` (byte copy of sha256 692d4afd…) and `probe.so`

Every run exited 0. Total CPU is about 70 s.

| File | sha256[:16] |
|---|---|
| e14_formulas.py | b9723698650e0d7f |
| validate_transcription.py | 88600fda546505ba |
| onset_scan.py | e078d2a60de9d3dd |
| fraction_recipe.py | 2b21bf317c774480 |
| slope_parts.py | 0e8f11c98028c817 |
| exchange_rates.py | 150b04f9017fdc12 |
| structural_scenarios.py | c54033331db32c83 |
| reanchor_outer.py | 372502dda4c41248 |
| combined_scenarios.py | b31383643407f7ad |
| looseness_probe.py | c4c85f6b3820fd32 |
| scaling_probe.py | 396b51f7780d0615 |
| origin_probe.py | e6a7f5ddda020cd0 |
| onset_scan_out.json | 7e852f2934171d84 |
| fraction_recipe_out.txt | 49bf687925167089 |
| exchange_rates_out.json | 4043e9e414c2ba0f |
| structural_scenarios_out.json | 4cce41a4d2b5e685 |
| reanchor_outer_out.json | 91d9dbb4a55eb9dc |
| combined_scenarios_out.json | a577d827de90aed8 |
| looseness_probe_out.json | b288d2f4845ed21f |
| scaling_probe_out.json | 01906d401278dab5 |
| origin_probe_out.json | a689846da6e7d165 |

**Head change.** During this session the orchestrator's commit
`bd4236d77d0ebc52d0de4a0ff8620a840035d58d` advanced the branch. `git diff --name-only`
from 1b6aa31 shows that it adds only `audit-02/` files and `audit-02-interim.md`. No
input listed in §1.1 changed. I did not read those new audit files, which
keeps this proposal record independent of them.

Limitations:

- The r-minimisations are grid-based (MEASURED). Only §2.3 is enclosed, and it
  covers only the Fh branch and the stated points.
- The M_far proxy has a known fixed-cutoff bias of at most about 10⁻³ (D01).
  All of §2.7 is a binary64 planning proxy.
- All I07/I09/I10 scenario inputs (c, re-anchored geometry, floor and origin
  factors) are hypothetical.
- The cost projection extrapolates nine D38 cases and two hybrid cases; it is
  not a law.
- D/E idea bodies were read only through their tables and term hits (§1.1).
