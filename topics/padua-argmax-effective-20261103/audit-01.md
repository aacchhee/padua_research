# Claude audit-01 — effective Padua argmax campaign (handoff 03)

> **DRAFT checkpoint (2026-11-03).** Mathematical review complete; technical replay section pending. Not yet a final audit record.

## Decision

**The mathematics is ACCEPTED at every stated scope, with no status change. The findings below are record, evidence-durability and wording items; none touches a proof step, checker predicate, certificate value or claimed status. Stage moves to WORK for a short developer response (handoff 04).**

- **PROVED, accepted as stated:**
  - codex-06a (exact spectrum of the inward corner-active polynomial);
  - codex-06b (all-degree slopes A_n,B_n <= -n^2 Lambda_c/8 and the explicit radius 0 < h_x+h_y <= 1/(2[n(n+1)]^3));
  - codex-01 (finite global argmax for 17 <= n <= 32, computer assisted);
  - codex-03-spots (three strict whole-cell edge comparisons at n = 13, 17, 24, computer assisted, shared-kernel limitation disclosed);
  - the scoped negative statements PD-N?…-06a (complete spectral positivity fails at n = 3), PD-N?…-06b (affine per-cardinal sign step cannot give a fixed kappa/n^2 radius) and PD-N?…-04 (G7-F fixed-sign individual cardinal representation fails on D(2,3) at n = 4).
- **MEASURED, accepted as MEASURED:** codex-02 (G2/G3/G4), codex-03 (G6 float screen and I-B0), claude-01 (pilot).
- **Original target.** PD-T099 stays **OPEN**: no explicit n0, no all-degree bridge, finite range 2–32 only. n = 40 is not certified; 33–39 were not run. The n^-6 radius is not the fixed phase zone rho <= 1/64 (physical scale n^-2), which stays OPEN together with the weighted-energy premise.
- **Severity.** No CRITICAL or MAJOR finding. Findings F1–F7 are MINOR; N1–N8 are NOTEs.
- **Next.** Codex answers every finding in `response-01.md`. Because no finding needs a change to a statement, proof, predicate or certificate, a Claude protocol check of the response suffices before PR preparation; a full mathematical re-audit is needed only if the response changes one of those.

## Identity, rules and audited candidate

- **Auditor:** Claude, configured `claude-opus-5-5`, effort xhigh, as handoff 03 requested (allocation-table row: adversarial audit of a novel mechanism and of computer proofs). The runtime exposes no separate serving-model receipt. Role: independent audit orchestrator and auditor, distinct from the Codex developer (gpt-6-astra ultra), the Codex technical workers (gpt-6.1-sol medium) and the Codex supplementary reviewer (gpt-6-astra high). I wrote no developer file.
- **Rules:** `AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md`, `templates/HANDOFF.md`, read at the branch head `82feb49a8aa6e7de3c5fc7eac6dfc3625b3499a2`.
- **Audited scientific input:** `d790d58d8ecb5eb4ac455b2b7d638336d3bc0430`. `git diff --stat d790d58 82feb49` touches only `handoffs/02` (status line) and `handoffs/03`, so every audited file is byte-identical at both commits.
- **Main:** `440d1079e42c3ef21c40d1cf8870f5b206410c6a`, refetched 2026-11-03, unchanged and an ancestor; no merge needed.
- **Open PRs (live list 2026-11-03):** draft #19 (this topic, head `82feb49`) and draft #20 (`codex/padua-lebesgue-followups-20261103`, head `771265e`). No other open PR; branch `claude/padua-literature-20261103` has no PR.
- **Audited hashes (sha256):**

| File | sha256 |
|---|---|
| theory/argmax-effective-codex-06-corner-active-spectrum.md | `8e6fa98c4ed820c575a6e2053e620272a364caa35bf0d91b7e7129dd19b5f6ed` |
| theory/argmax-effective-codex-06-uniform-slopes-local-radius.md | `83499891b742f44c5b78283f16e94a023765f72188ef8cdddb366008d7c11201` |
| theory/argmax-effective-codex-06-negative-spectrum.md | `60502d05eb9397a946bace8dd1720072faa1624db19c4dc9c74cb294110a294a` |
| theory/argmax-effective-codex-06-affine-sign-obstruction.md | `7e7f0963879cc1b72977166a407d8038c9e23adaf1891db3d9f61a5f64c9e33a` |
| theory/argmax-effective-codex-04-coarse-cell-sign-obstruction.md | `8c63b4d6069e562431f3d9974b56e1f8d0afad893818800d56fc5d682c5e1648` |
| theory/argmax-effective-codex-01-finite-global-argmax.md | `c8ab85ebacbd3d17a2ebd7d9abb295c5362ccaf1083dc918b3a50655f0266a70` |
| theory/argmax-effective-codex-03-exact-edge-spots.md | `8f8371ea99188fd20ec7f4f12b2f2b2d30e0f2bd34fe766eee0f59a2eb693f3c` |
| theory/argmax-effective-codex-03-comparison-screen.md | `fad8259e0a71a8a095cfb30bd00f76b658c31195251d31ec1c5339440f02b178` |
| theory/argmax-effective-codex-02-gate-measurements.md | `d32799901d25ca6a28d41415b0f0b80977f1e7beeffa7c1475574a9c8212e714` |
| theory/argmax-effective-claude-01-pilot-measurements.md | `923ecf963a4993080e376d693cc7bdf5c5ff6ccf1f0b06a5be2a2ae7d369f640` |
| evidence-manifest.json | `c09d542620be41980d80b844cd8f3550cf59988711e04a27f8504be486632735` |
| code/native_checker/kernel.cpp | `b0c871e7711219edfe3ce01480d8d1de3503a20d9b59f82b63a00eff248bc6e0` (equals the claimed corrected kernel) |
| code/native_producer/producer.c | `ae3002a995c199660ad8c31dd2c7577a8416208ab8b3868c0795ebe728ab72ff` |

## Read coverage

- **Complete:** BRIEF, handoffs 01–03, plan, LOG, report, results file, every file under `theory/`, `ideas/` and `attempts/` (the two native attempts read by the technical sub-auditor and spot-read by me), `literature-g8.md`, `independent-checks-01.md`, `independent-checks-canonical.md`, `independent-math-checks-01.md`, `proposed-record-changes.md`, `ALLOCATIONS.md`, `allocation-scan.json` (summary fields), `COLD_STORAGE.md`, both native READMEs.
- **state/IDEAS.md:** read in full (889 lines), as handoff 03 requires. The unisolvence, MZ, lattice, programme-ideas and bivariate-Lanczos sections were read at row level; the Padua MZ 2D, Lanczos-drift, PR12 and PR17 sections, and every obstruction and disposition table, were read in full. Shortlist read in full: IDEA-206, 290–305, 316–335 and their PR17 canonical register rows; IDEA-257/259–261 (drift-campaign "corner negative witness", a different polynomial; no overlap).
- **Inherited dependencies checked:** PD-T227 record (statement, corner value/gradient formulas and its "useful exact next lemma A_n,B_n <= -n^2 Lambda_c/8" sentence and F15 dated correction); PD-T101, PD-T210, PD-T214, PD-T228, PD-T229, PD-T231 registry rows. PD-T210's leaf implication and PD-T231's univariate reduction were accepted in Claude audit-01 of PR17 and are not reopened.
- **Not read:** the third-party sources themselves (no new LIT record is accepted beyond its stated coverage; see N6).

## Independent checks executed by the auditor

All in a scratch directory outside Git (`/tmp/claude-0/…/scratchpad/audit-math/`), Python 3.13.18, NumPy 2.5.3, float64. These are diagnostics supporting my reading of the written proofs, not proof premises.

1. **codex-06a/06b reconstruction, n = 2–40** (`corner06.py 40`, 16 s). Independent code builds the cardinals from the PD-T101 formula and, for n <= 14, also by a direct linear solve of the interpolation system in the total-degree Chebyshev basis (max discrepancy 7.3e-16; confirms PD-T101 there). For every n = 2–40 it checks: zero mask = {(j,0): j even > 0}; sigma_jk = sign L_jk(c) on nonzero cardinals; zero-row gradients have equal x/y components with sign sigma; the closed-form C_ab against the masked transform (max error 2.6e-14); positivity of every a > 0 coefficient; R_0 = 1+1/N, R_n = 1/N, R_a = R_(n-a); D_b > 0, D_0, and the D_b − D_(m−b) identity (10) for both parities; C_(n−b),b >= 2/m, C_0n >= 8/15, Lambda_c >= 1+2/N+2(n−1)/m; -A_n = sum a^2 R_a, -B_n = sum b^2 D_b; every inequality in (1), (2), (2a); the bounds (5) and (6). All passed.
2. **Inherited PD-T227 formulas used in 06b, n = 2–30** (`t227.py`): |L_jk(c)| = 2w(1−cos(k pi/m))/|cos(k pi/m)−cos(j pi/n)| (rel. error <= 6.6e-12) and the zero-row gradient −2w(−1)^n n/(1−cos(j pi/n)) (<= 5.3e-13).
3. **Radius (3) sanity** (`radius06.py`): at H = 1/(2N^3) and H/3, 21 directions, n = 2,3,4,5,8,12,17: lambda(c+h) <= Lambda_c − n^2 H/6 with positive slack.
4. **PD-N 06b** (`neg06.py`): the closed form of q_n matches L_x/L at (3,1) for n = 3,4,16,32,64,96; q_n/n^3 = −0.303, −0.278, −0.266, −0.262 at n = 16…96, approaching −5/(2 pi^2) = −0.2533.
5. **G2 spot replay** (`g2check.py`, my own evaluator): K(17) = 0.289285, K(24) = 0.277459, K(48) = 0.259348, maximal on the axis at rho = 1/1024; matches codex-02's 0.289285 at n = 17.
6. **G6 exact spots** (`g6float.py`): float target-centre minus sampled source supremum 0.1096 (n13), 0.0653 (n17), 0.0171 (n24), above the certified rational margins 0.0566, 0.0290, 0.0112; exact integers 20·d13, 40·d17, 100·d24 > 2^192 rechecked with Python integers.
7. **Manifest:** `python topics/padua-argmax-effective-20261103/code/evidence_manifest.py` → `verified: true`, 84 files, certificate degrees 17–32.

## Technical replay of native certificates

**PENDING.** The technical sub-auditor's independent native replays, corruption controls and checker-code inspection are still running. This section, and therefore this audit, is incomplete; the decision above is a draft until this section is filled.

## Mathematical review

### codex-06a — exact corner-active spectrum (PROVED, accepted)

I re-derived every step by hand.
- Reflection to j = n−p, r = m−q maps the checkerboard to j+r odd, and T_a(B1)T_b(B2) = (−1)^(a+b) cos(a j pi/n) cos(b r pi/m); with T_a(−cos xi) = (−1)^a cos(a xi) the signs cancel, giving (2). The sign data (−1)^j t_jr, including the t_jm = −1 exception for j < n (the zero row) and t_nm = +1 (the 00 corner cardinal), follow case by case from the four sigma rules.
- (3): both parity sums of f_r cos(b r pi/m) vanish for 1 <= b <= n (trapezoid rule and its alternating twin); the upper-tail telescoping gives −sin(jt)/(2 sin t) whether or not the tail ends at the half-weight point m (checked both endings); the exception contributes −(−1)^b·1_{j≡n, j<n}. (4) likewise.
- (6): with Σ_{j≡n} e_j cos(sj) = 0 the indicator term is +ε/2; cos(n(t±s)) = ε cos t; cot x + cot y = 2 sin t/(cos s − cos t). The algebra closes to (1−ε cos s)/(2(cos t − cos s)). Denominators: s = t would need n | A. b = 0 via (7) and a = 0 (A = n, class weight (−1)^n n/2, shift −εn/2) and a = n, b = 0 (sum 1/2) all check, including C_00 = −1/6 at n = 2.
- Positivity, the sine-concavity bound C_(n−b),b >= 2/m (1−r^2 = (2n+1)/m^2 <= 2/n), C_0n >= 8/15 ⇔ 2(2n−3)(n−2) >= 0, D_b > 0 (C_0b > −2(n−1)/N > −2/m), and the edge-interpolation argument (nodes on y = −1 are i odd with sigma = +1; root count exceeds degree in both parities) are correct.

### codex-06b — all-degree slopes and explicit radius (PROVED, accepted)

- Slopes: −A_n = Σ a^2 R_a by d cos(a xi)/dx = −a^2 at xi = 0; pairing a, n−a with mean square >= n^2/4 gives (n^2/4)(Lambda_c − 1 + 2/N); the 1/3 bound is (n−2)(n−3) >= 0; Lambda_c >= 2 is (n−1)(n−2)/N >= 0. B: odd n pairs D_b = D_(m−b); even n uses identity (10) and the alternating sum Σ_{b=1}^s 2(2b−m)(−1)^(b+1) = −2s = −n, which I checked for s even and odd. The final 3/4 margin is (m^2 − n^2)/4 − (n−1)/2. All correct. The proof uses only one-sided inward directional derivatives, which PD-T227 provides (lambda is not differentiable at c in general).
- Radius: (5) from |cos v − cos u| <= 2 and 1−cos(pi/m) >= 2/m^2; (6) from Σ c_ab = 2N (I recounted: 1 + 2n + (2n−1) + 2n(n−1)); then |g·h| <= w/m^2 <= |l|/2 on H <= 1/(2N^3). Zero cardinals have equal gradient components of the fixed inward sign, so (7) holds. (8) from |T_a^(r)(−1)| <= a^(2r) and Σ w_B = 1; (9) is the exponential series; e/(2m^2) <= 1/6 needs m^2 >= 3e, true for m >= 3. Combining with A,B <= −n^2/3 gives (3). Reflection to the second non-node corner is node-preserving in the right axis for each parity.
- Scope is stated honestly: n^-6 physical, not the fixed rho zone; the weighted-energy premise of PD-T227 stays OPEN.

### Negative statements (PROVED, accepted at their exact scopes)

- **06a-N:** C_01 at n = 3 equals (1/6)(4 − 2√2 − 3) = (1 − 2√2)/6 < 0. Refutes only complete coefficientwise positivity; grouped positivity is the retained 06a.
- **06b-N:** the PD-T227 closed form of q_n and the four elementary limits (n^2 C → pi^2/2, n^2 d → 4 pi^2, n^2(ab−1) → −5 pi^2, n^2(1−a^2) → 9 pi^2) are correct; the second term dominates at order n^3. The statement blocks only the uniform termwise affine sign-preservation step; it rightly says nothing about true cardinal signs, aggregate control, reflection-first bounds or PD-T099.
- **04 (G7-F):** 40 L00(x,0) = 1 − 2T1 − 2T2 + 2T3 + T4 (I recomputed the y-sums 1, −1, −1, 1, 1 and the halved (4,0) mode), = 4(2x^4 + 2x^3 − 3x^2 − 2x + 1) = 4(x^2−1)(2x^2+2x−1); the values 4/405 and −11/4096 and the strict diamond membership (√2 < 23/16) are correct. Scope: only individual fixed-sign cardinal representations on that coarse diamond. The original G7 criterion is correctly diagnosed as ill-posed and preserved; IDEA-319 stays deferred.
- The curve-corner remark (only the node corners lie on gamma) is a correct routine observation.

### codex-01 — finite global argmax 17 <= n <= 32 (PROVED, computer assisted, accepted)

The finite reduction is PD-T210's unchanged implication (bound leaves: every Bernstein l1 coefficient strictly below a certified lower bound for Lambda_c; corner leaves: strict except at the exact corner vertex, whose coefficient is the exact cardinal value). The statement lists exactly the degrees with corrected-kernel acceptance; it does not fill 33–39 around the n = 40 probe. The PD-T099 split is recorded correctly. See the technical section for the replay, controls and code inspection.

### codex-03-spots — three exact edge comparisons (PROVED, computer assisted, accepted)

The Bernstein affine-substitution weight formula, the l1 upper bound over a complete closed binary cover of an outward-enlarged source interval, and the interval-Horner target lower bound are correct. The second inequality is trivial because the target centre lies in the target cell. The shared producer/checker arithmetic kernel is disclosed in the same terms as PD-T210/231; I accept the claim on that basis, as PR17's audit did for PD-T231. Pair selection by measured margins is disclosed and does not affect validity.

### MEASURED records and gates

- G2/G3/G4 and G6 are worded as finite-sample extrema throughout; no sampled constant is used as a uniform bound. My G2 spot replay agrees.
- G5: I agree it is not evaluable. The pre-registered factor-two / 10·n_cert(7 days, port) rule is preserved, and the dated operational clarification in `attempts/gates-g2-g5.md` is added beside it, as handoff 02 required ("add a dated new criterion and keep the old one").
- G1: the labels CPU vs wall, hot path vs full driver, producer-only vs producer-plus-checker, and the two-point fits are honest. See F4.
- G0: met for 17–24 (fresh independent Python production and checking plus native acceptance); 25–32 rest on the native producer plus the separately written native checker, as handoff 02 step 4 specifies for large n.

## Novelty and dispositions

- **06a/06b vs IDEA-330/331 and PD-T227.** PD-T227 itself names "A_n,B_n <= −n^2 Lambda_c/8 … for every n >= 2" as the useful next lemma and keeps it OPEN; IDEA-330's row says "All-n slope uniformity and weighted energy remain OPEN". The new theorem discharges exactly the slope half. Classification as a quantitative variant of IDEA-330/331, closing one recorded obligation, with no historical novelty claim, is correct. I found no earlier registry entry proving it.
- **R5 equivalence to IDEA-320:** correct; max over sign vectors of a fixed Bernstein coefficient is its absolute value, and quantifiers over sign vectors and indices commute. Equivalent, so no PD-N is correct.
- **Native producer/checker:** implementation variants of IDEA-320, with no new criterion; correct.
- **E-C extension and I-B0:** continuation of IDEA-324 and a frozen operationalization of the brief's interior-to-boundary idea; retained OPEN. G6's kill did not fire. Correct.
- **R1/R2:** deferred with explicit resume conditions, not rejected. Correct.
- **Negative records:** each kills only its stated mechanism; no failed proof route is promoted to a theorem rejection.
- **Literature (G8):** coverage limits are explicit, no 1-D theorem is transferred, and nothing in the accepted proofs needs one. The Brutman survey correction (Annals of Numerical Mathematics 4 (1997)) is plausible from the cited copy; I did not open it (N6).

## Findings

All MINOR unless marked NOTE. None affects a proof, predicate, certificate or status.

- **F1 (cold storage, durability).** COLD_STORAGE.md links the verified staging archive by an absolute path in the Codex workspace (`/workspace/padua-work/export/…`). That path does not exist in this audit session, so the 16 raw gate/comparison files and the archive are not retrievable from the repository or from another session, and the Markdown link is dead in Git. Only the compact receipts committed in `outputs/` and `evidence/` survive. The MEASURED records do not depend on those bytes for their stated values, but the record should say plainly that, unless the archive reached AC, the raw files exist only as regenerable outputs (scientific re-measurement, not byte recovery). Response: confirm whether the archive was delivered; otherwise mark it as not retrievable and point to the regeneration commands.
- **F2 (cold-storage destination wording).** COLD_STORAGE.md says "No Windows destination has been selected." WORKFLOW names AC's destination as `Downloads\padua\cold_storage\<slug>\`. Reword as "destination fixed by WORKFLOW; delivery pending".
- **F3 (native bulk certificates).** COLD_STORAGE.md excludes the native producer/checker bulk outputs and defers to the attempt records, but no committed record gives a cold-storage locator or regenerable-only declaration for the non-essential native artifacts (n40 certificate, logs, CPU-benchmark receipts named in the checker README). Add one line stating where they are or that they are regenerable-only.
- **F4 (G1 completeness).** Handoff 02's G1 asked for 24 h / 7 day n_cert for the Python reference and for the port. The Python projection omits checker CPU (disclosed), and the native producer+checker fit uses two points (17, 24). Keep the disclosure; in the report, add one sentence that the Python full-pipeline n_cert was not measured, so G1 is only partly answered for the reference.
- **F5 (status-line wording).** Each theory record and idea record still says "required Claude audit remains pending". Update to cite this audit at preparation; do not edit this audit.
- **F6 (06b history wording).** The statement says "an all-degree local theorem with n0 = 2". Since "n0" denotes the global threshold elsewhere in the campaign, add "(local, physical radius n^-6; not a global n0)" or similar to avoid misreading in RESULTS/PAPER_MAP.
- **F7 (proposed registry text).** In `proposed-record-changes.md`, the new PD-T099/PD-T227/IDEA-330 text says "audit pending". At preparation, replace that with the final IDs and a link to this audit. The PD-T227 annotation should cite the final ID of codex-06b, and keep "weighted energy and the fixed scaled phase radius remain OPEN" verbatim.

NOTEs:
- **N1.** The 06b-N statement starts at n >= 4; index (3,1) is already admissible at n = 3. Harmless.
- **N2.** 06a and 06b float diagnostics agree with mine at a larger range (n <= 40, plus direct solves to n = 14). Developers may cite this audit as an extra diagnostic, not as a premise.
- **N3.** The finite theorem relies on correct execution of the committed checker on GMP, as stated. The checker reproduces the reference rounding sequence, so producer/checker share the specification. That is disclosed.
- **N4.** Concurrent PR20 reserves PD-T266–285, PD-N092–099, IDEA356–375, LIT474–481, disjoint from this topic's ranges. Its proposed registry edits touch PD-T098/211/230 only, so no row collision with this topic's PD-T099/PD-T227/IDEA-330 annotations. Recheck both at preparation.
- **N5.** The G6 exact pairs were chosen from measured minimum gains; that is disclosed and does not affect validity.
- **N6.** I did not open the third-party sources. LIT acceptance is limited to the coverage each record states.
- **N7.** Several records omit spaces before numbers ("range2–32", "n40"), apparently from an editing tool. Cosmetic; fix opportunistically.
- **N8.** The supplementary Codex reviews are development evidence; this audit is the required distinct-agent audit.

## Remaining uncertainty

- The computer-assisted claims rest on correct execution of GMP and the committed checker; agreement between independently written implementations reduces, but does not remove, shared-specification risk (disclosed).
- G2/G3/G4/G6 values are finite samples; no continuous or all-degree bound follows.
- PD-T099 remains OPEN.

## Requested response (handoff 04)

Codex answers F1–F7 in `response-01.md` with a fix, an evidence-based rejection or an explicit unresolved item. Statement, proof, checker and certificate files should not need changes. Then Claude checks the response and the topic moves to PR preparation (final IDs from the reserved ranges after a fresh union scan, registry rows, RESULTS.md section). Only AC merges.
