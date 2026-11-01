# Claude audit-01 — second proof campaign (A2, A5, A4(a), B3, B1)

- **Decision: ACCEPTED for the stated scope, with minor findings.** Every PROVED claim is accepted as stated: A2 01–04; A5 counts and globals for n=3–7 (06/07, 10/11, 16/17, 41/42, 51/52) with their supporting results; the n=8 lower bound 64; A4(a) 70–77 and the g bracket; B3 negative01, support 80 and negative02; B1 90–93. The OPEN statuses of 61/62/65 (n=8 exact counts and global), A3, A4(b)/(c) and the other B1 classes are also accepted. **No status change is required.**
  - No finding is major, and none touches a proof step, checker predicate or certificate.
  - Findings F1–F8 are minor record, wording and integration-proposal items. They need dispositions in `response-01.md`.
  - Re-audit is needed only if a response materially changes a statement, proof, checker or evidence. A wording or proposal-text fix does not count.
- **Audited candidate:** scientific head `4265bb94f987ce77d89cd5e15a8c435cbd1411d0`, branch head `7f226c1cec873fd8069feae1f4749f13d95f5c9d`.
  - `git diff --name-status 4265bb9..7f226c1` shows only `handoffs/01-work.md` (status line only) and the new `handoffs/02-audit.md`.
  - Outside the topic, the candidate equals main `28aaa20861d08074b77efc74eaef75cdcb36234d`: `git diff --stat 28aaa20..7f226c1 -- . ':!topics/padua-proof-attempts-2-20261101'` is empty, and `28aaa20` is the merge base.
- **Rules:** read at `7f226c1cec873fd8069feae1f4749f13d95f5c9d`: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md`, `templates/HANDOFF.md`, `handoffs/02-audit.md`. I also read the accepted Part1 `audit-01.md` as a format reference.
- **Auditor:** Claude, configured `claude-opus-5-5`, effort xhigh, as requested in handoff 02. The reason is the Opus 5.5 xhigh row of the allocation table: an adversarial mathematical audit of all-n proofs, computer proofs and a scoped refutation. The runtime does not expose a separate serving-model receipt.
- **Role:** independent audit orchestrator, distinct from the Codex developer and from the Codex supplementary executors. I wrote no developer file.
- **Sub-auditors:** seven independent Claude sub-auditors, each configured Opus 5.5 xhigh, read-only outside their own `audit-support/claude-audit-01/<target>/` directory and with no Git authority. They covered A2, A4(a), B3, B1, the A5 n≤7 reductions and checkers, the A5 n=8 lower bound plus census plus literature, and the registry/novelty gate.
  - Each was briefed with the claims and files to test, not with my conclusions.
  - I verified their key cited lines myself before relying on them (see "Orchestrator spot checks").
  - Their condensed reports are in `audit-support/claude-audit-01/subaudit-reports/`.
- **Environment:** Linux cloud container (2 cores) with Python 3.13.18, SymPy 1.14.0, python-flint 0.9.0/FLINT 3.6.0, mpmath 1.3.0, NumPy 2.5.3 and SciPy 1.18.1. Development used Python 3.12.14.

## Scope and read coverage

- **Read in full by the orchestrator:**
  - `report.md`, `plan.md`, `inputs-review.md` (first 80 lines in full; the rest by search), both handoffs, the `proposed-record-changes.md` structure and every Old/New block (mechanically, see below), and `evidence-manifest.json`;
  - the relevant LOG sections (header, Runs needed, user-scope resolution, final stop, Windows entry);
  - theory 64.
- **Read in full by the sub-auditors**, per their reports:
  - every target attempt;
  - every durable theory file for their target;
  - every case receipt (`independent-checks*.md`, `independent-execution*.md`);
  - the A2/A4/B3 code;
  - every line of `a5_checker.py` and `a5_checker_n4.py`, plus the n4→n5→n6→n7 checker diffs and the n7 field helper;
  - the A5 schemas;
  - the B1/B3 source statements at their pins.
- **Novelty scope.** The scope contains negative claims (N01, N02), so the full `state/IDEAS.md` was read (all 783 lines and every table, by the registry sub-auditor). Its obstruction/disposition tables and the rows of PROOF_STATUS, ID_CROSSWALK and literature/INDEX relevant to the targets were read or searched.
  - The topic claims no novelty or priority anywhere.
  - No existing registry entry pre-empts or contradicts a Part2 claim.
  - N01 is a declared extension of PD-N039 (IDEAS.md:509; PROOF_STATUS:101).
  - N02 rejects only the full-residual common-cluster mechanism, scoped no more broadly than PD-N039/PD-N040.
  - Every attempt records a real gate: registry scan, closest records, obstructions and a verdict. Truncated registry reads are declared (T-A5-n5:64, T-A5-n8:111). The gate hashes match IDEAS.md `4a7f365d…` and INDEX `3cd4a057…`.
- **Literature checked.**
  - Kolomoitsev–Lomako, arXiv 2009.07114v1 (KL2021), read through WebFetch text: Thm 2.1 and its Padua specialisation, Lemma 3.5 (3.20), Lemma 3.6 (3.29) and (4.5)–(4.6). These match the topic's description in substance, and none is a premise of A2.
  - Białas-Cież–De Marchi–Suder, arXiv 2605.23299v1, Table 3, read through WebFetch of HTML and PDF; both reads agree.
  - Direct PDF downloads were refused by the proxy (HTTP 403). No PDF page was viewed and no third-party text is committed.
- **Not covered:**
  - the producer/search modules;
  - the developer control harnesses (skimmed only);
  - SymPy and FLINT internals;
  - byte-level comparison of developer versus independent certificates;
  - the 153520-leaf n=8 interior proposal and n=8 boundary artifacts (out of scope; their targets are OPEN);
  - Bos et al. 2006 Thm 3 (background only, not a premise).

## Protocol and provenance checks (orchestrator, executed)

- **Manifest.** An auditor script, not the developer generator, read every row of `evidence-manifest.json` at `4265bb9`.
  - All 294 inputs match their `git show COMMIT:PATH` bytes, SHA-256, byte count and Git blob, and each row's commit equals its `pins[source]`.
  - All 378 outputs match the candidate bytes and SHA-256.
  - Exactly two topic files are absent from the outputs: the manifest itself and `handoffs/01-work.md`. Both are excluded by the stated exclusion rules.
- **Size limits.** Generated files (json/jsonl/gz/xz) at the candidate number 197, totalling 4,463,653 bytes; with the manifest itself (188,481 bytes) that is 198 files and 4,652,134 bytes. This reconciles exactly with handoff 02.
  - The largest file is `outputs/a5_n8_interior_candidate.json.gz` at 637,163 bytes, within the 1 MB per-file and 5 MB total limits.
  - The audit commits only what fits the remaining budget (see "Evidence").
- **Proposals.** I parsed all ten literal Old→New blocks mechanically.
  - Each of the nine Old blocks occurs exactly once at its stated pin, at main `28aaa20` and at the candidate. Each Old block is contained in its New block.
  - The tenth target, `results/padua-proof-attempts-2-20261101.md`, is absent at `28aaa20`, as stated.
  - The content of the New blocks is the subject of F1–F3.
- **Commits.**
  - All 42 Part2 non-merge commits under the topic are authored and committed as Andrey Chesnokov <aacchhee@gmail.com>, and every first-parent non-merge commit carries `Agent: Codex`.
  - The only first-parent commits touching paths outside the Part2 topic are the four inherited Part1 commits (`a09d910`, `8fb28d7`, `967131d`, `184b02a`), all under `topics/padua-proof-attempts-20261101/` and now merged in main.
- **User scope.** Topic-only, local IDs, no range, and no RESULTS/root-results/shared/.github writes are all respected.
  - The "(audit pending)" dependency phrase is retained as the user required. Its qualification is accurate: Part1 audit accepted, dispositions complete, PR9 merged, final ID PD-T101.
  - The intended Windows entry in LOG "Runs needed" was correctly not written. AC's current rule is repository-only results tracking, so that local entry should be dropped at PR preparation rather than written (see F3).

## Mathematical verification

All claims below were reconstructed independently, step by step. "Supporting" computations are finite evidence only; no numerical match is used to support an all-n statement.

### A2 — 01–04 (PROVED, accepted)

- **04: |Λ_c − L_n²| ≤ π⁴/2 + 4 + 1/(n+1) < 54.**
  - Reflecting about either non-node corner gives D_n = (−1)^j(2+cos a+cos b)/(cos a−cos b). The only coincidence is (π,π), contributing 1/(n+1).
  - The reflection average turns the positive form into the square of the d_r-weighted odd-cosecant sum (F_n = L_n²), for both parities.
  - The deformation bound runs through (6) → (7) → (8), using lr ≤ n(l−1)+r ⇔ r ≤ n, and sums to π⁴/2. The total is 53.04 < 54.
- **01:** B_n ≥ H_n/2, csc x ≥ 1/x, and 80 log 2 ≥ 54.
- **02:** csc x − 1/x is increasing, L_n ≤ (2/π)log n + 4/π + 1, and 12/π + 63/log 2 = 94.71 < 95.
- **03:**
  - e_m ≤ 1/(2m).
  - ∫₀^{π/2}(csc x−1/x)dx = log(4/π).
  - The monotone quadrature error is ≤ (1+2/π)/n.
  - The total is 54 + 9 + c₁² (≈ 0.926) < 67 ≤ 68, with b = (8/π²)(γ+log(8/π)) = 2·(2/π)c₁.
- **Quantifiers.** No n₀ threshold appears: every inequality holds at n=2, so the analytic proof leaves no small-n gap, and the exact n ≤ 6 regression is supplementary only. Both parities are explicit. No MEASURED value and nothing from A3 is a premise. KL2021 is background or a context remark only.
- **Supporting computations:**
  - certified ball arithmetic (256-bit) on a direct Vandermonde computation, which uses neither A1 nor 04, for n=2…28;
  - an independent implementation of the A1 corner formula on all four corners: every bound in 01–04 holds for n ≤ 300 and at dyadic n up to 4096;
  - Richardson estimates (MEASURED) that approach b = 1.2255221.

### A5 — n=3–7 counts and globals (PROVED, accepted); n=8 lower bound 64 (PROVED, accepted); 61/62/65 OPEN (accepted)

- **Reduction.**
  - λ = max_s P_s on the whole square. At any local maximum, strict or not, every active P_s has its own local maximum, so ∇P_s = 0 and its Hessian is negative semidefinite. Hence a maximum on a crease or at a crossing cannot escape the active-polynomial predicates.
  - Leaf masks come from interval enclosures, so any cardinal whose enclosure contains 0 gets both signs, and every active mask at a crease is enumerated and must be disposed of.
  - Acceptance requires strict signs on the root box.
  - Nodes are never strict maxima (λ ≥ |ΣL_i| = 1). The node-cone radial bound 15 was re-derived.
  - Edge acceptance needs q″ < 0, a sign change and strict inward descent.
  - The checker enumerates all 2^|zeros| active masks at a corner itself.
  - The cubic-only steps are confined to n=3.
- **Checkers.**
  - All sign decisions are exact or outward-rounded; floats are used only for timings.
  - The partition check requires distinct, prefix-free paths with Kraft sum exactly 1.
  - Masks and counts are recomputed, and no certificate count or flag is trusted.
  - Krawczyk is evaluated on an outward superset and must land strictly inside the exact R.
  - Root boxes are strictly disjoint, so each maximum is counted exactly once.
  - No checker imports producer or search code.
  - The source hashes match the pins: n3 `d32810f1…`, n4 `1fe4f74f…`, n5 `6390d465…`, n6 `34d8c0b7…`, n7 `41ab8dd1…`, field helper `76f9ba3d…`.
- **Globals.** The non-strict-plateau exclusion was reconstructed: flat and factor bounds below the cut, node-cone radial ascent, and edge constants ±1 verified exactly. The exact corner identity was reconstructed too. Independent 20-digit corner values are n3 3.7761424, n4 4.4097254, n5 4.9478057, n6 5.4174994, n7 5.8356577.
- **Supporting probes:**
  - checker enclosures contain independent 80-digit cardinal values for n=4–7;
  - in an n=4 mutation probe, all 31 counterfeits were rejected and all 7 valid variants accepted;
  - an n=3 primitive probe.
- **n=8 lower bound.** An auditor-owned verifier (python-flint arb, 320 bits) builds its own cardinals and imports no repository code. It independently confirms all 44 witness records in both committed witness files:
  - every s_i L_i > 0 on R (smallest lower bound 1.06e-5);
  - Krawczyk inclusion, with contraction norm ≤ 3.1e-8;
  - H_xx < 0 and det H > 0;
  - R inside the open square;
  - all 946 pairs disjoint.
  
  It rejected all eight negative fault-injection controls.
  
  The lower-bound-only wording is correct. The progress figures 152000/153520 and 150000/153520 appear only as labelled diagnostics, and no completeness is inferred from them.
- **Census (supporting only).** A numerical census of all strict maxima for n=3–8 used per-sign-region Newton, all-active-sign tests near creases, and Nelder–Mead cross-checks.
  - It reproduces exactly 7/6/2/15, 13/12/2/27, 14/9/2/25, 25/14/2/41 and 33/15/2/50.
  - At n=8 it gives 44/16/2/62 on three grids, and each of the 44 interior maxima lies in exactly one witness box with the same mask.
  - The global maximum is at the two non-node corners for every n.
  
  This supports the OPEN targets 65 and 61 numerically. It proves neither.
- **Literature.** Table 3 of arXiv 2605.23299v1 reads inner 7, 13, 14, 23, 27, 38 and total 15, 27, 25, 39, 42, 56 for n=3–8, so the developer's readings are correct.
  - Plain 8-neighbour grid maxima reproduce the paper's n6 23/39 and n7 27/42 rows. That is a plausible crease-merging mechanism, not a claim about the authors' method; the n8 row is not reproduced this way.
  - The "candidate correction" framing at n6/n7 and the interior-only n8 treatment are justified and properly hedged.

### A4(a) — 70–77 (PROVED at the stated central scope, accepted)

- **70 and 71.**
  - 70: the θ_c collapse on all four edges, with removable limits.
  - 71: D−τ = 2τ(1+z)/(A−z). The single coincidence carries weight 1/N and the true kernel is n−1, which gives the essential 2/[n(n+1)] correction exactly.
- **72:** the tail and half-density bounds give 1/45 < g ≤ 2, uniformly for any β_n → π/2.
- **73:** the IBP boundary terms, the a_k (decreasing for all k, so the alternating bound is valid), S1 = 47/72 and S2 = 1651/2400 all check.
- **Strict bracket, certified independently:** 8S₆₅/π² ∈ [0.548504986190685 ± 3e-21] and 8S₆₄/π² ∈ [0.548525055354043 ± 3e-21], using exact rationals and 256-bit π. Both lie strictly inside the stated decimals. Five representations agree on g ≈ 0.548514842399558.
- **74–76.**
  - The λ = S_n − Δ decomposition and phase localization need only Λ_c/log n → ∞.
  - The local gain is O(s² log n + |s|).
  - The B factorization, the collision placement and the 76 defect bounds all check; the constant 63/64 < cos²(1/8) is tight but true.
- **77:** a sequential assembly, one maximizer per n, with no interchange of limit and supremum. Ties, nearest phases just outside the cell, cell endpoints and cusps are covered.
- **Supporting computations:**
  - 50-digit Padua cardinals for n ≤ 9 confirm 70 on all four edges (20,388 checks), 71 at all 45 (ε,q), and λ = S_n − Δ;
  - float numerics for 32 degrees up to n=400 give n(Λ_c − R_cen − g) ≈ 0.77–0.80.
- **Scope.** Nothing claims R_search, global runner-up identification, or A4(b)/(c).

### B3 — negative01 (PROVED; the specified S(α) is refuted), support 80 and negative02 (PROVED), accepted

- **Source text.** The family was tested against the literal source text of B3 and the PD-N039 n_box definition. Both are identical at `9bd14a6` and `28aaa20`, apart from a Final-ID line.
- **The family is a genuine counterexample, not a surrogate.**
  - It consists of genuine four-positive-atom sections with n=1 and M=4.
  - The pivots satisfy r² = (1−t)/6 and s² = (1−t)(25t+2)/36, both above (1/10)².
  - δ² = 27t²/(2u³), so 0 < δ → 0, and the computed gap is g > h/2 ≥ √δ/10.
  - The count is n_box = 1/2 throughout 0 < t ≤ 1e-6. The reference H(0) lies in 𝒞₁ (PD-T095(b)), at distance d ≤ 7t < g/2, with joint count 1.
- **Quantifiers.**
  - The family defeats every α > 1/2 and every finite C.
  - A half-integer n_box defeats (i)∧(ii) whatever 𝒩 is, so the refutation does not hinge on H(0).
  - Both monomial orders were verified directly.
- **80:** re-derived. **N02:** rejects only the literal common shrinking cluster route.
- **Independent exact check.** An auditor script builds the sections from moments in both orders. It gets the inertia from two independent counts (certified Descartes signs and Jacobi minors), and certifies every whole-interval sign claim with 104 Sturm certificates cross-checked by Arb root isolation; nothing is sampled.
  - This independently machine-checks three steps the developer driver only asserts: eigenvalue localisation, g ≥ h/2 and d ≤ 10t (see F7).

### B1 — 90–93 (PROVED for the precise class, accepted)

- **90:** the detector is an isomorphism for all outward offsets, coincident ones included ((s−a)/(s−a_k) > 0, and equal to 1 at a = a_k); ker τ = (s−a)Π_{k−1}; the transport identity τ(p) = (s/a)^k p(ax/s, ay/s) is multiplicative; and dim R_t ≤ 2t+1.
- **91:** the coalescent witness a_j = c > 2 lies inside the open class domain. The p_t are polynomials in the offsets only, with coefficients from the fixed z_i and w_i, so the quantifier is genuinely "every fixed sample". The collision factor is multiplied in afterwards, in the integral domain ℝ[a].
- **92:** both inclusions follow from rank 2t+1, at most t−1 constraints, and detection.
- **93:**
  - Substitution gives a finite real exponential sum, with f(0) = P₀(c,…,c) > 0.
  - The Rolle zero bound holds on all of ℝ, so the exceptions are finite on the whole half-line.
  - The source match at `9bd14a6` checks out: `orf2d.py:68-76,98,104,128-129`; `window_exact.py` n=10, M=120, T=9.
- **Supporting checks:**
  - exact rational ranks in 17 configurations, including coincident and coalescent offsets and wrong-block controls;
  - mod-p ranks on the source's own nodes;
  - a 45-digit taper scan.

## Independent execution (actual runs, this session)

### Reruns of the developer's own commands

These ran sequentially into new auditor-owned paths (`audit-support/claude-audit-01/`), with `PYTHONDONTWRITEBYTECODE=1 python3 -B` from the repository root. Each output was compared field by field with the developer's recorded output.

| Command (topic-relative) | Exit / wall | Comparison with developer output |
|---|---|---|
| `code/a2_exact_check.py` | 0 / 0.8 s | identical except `python` |
| `code/a2_sanity.py` (MEASURED, long double) | 0 / 0.4 s | identical except `python`, `numpy` and seven last-digit long-double fields (≤ 1e-18 relative) |
| `code/a4reg_exact_check.py --source-sha256 13e8c524…` | 0 / 3.2 s | identical except `python`, `elapsed_seconds` |
| `code/a4reg_complementary_check.py --source-sha256 978bf8e0…` | 0 / 2.1 s | identical except `python`, `elapsed_seconds` |
| `code/a4g_series.py --source-sha256 51095513…` | 0 / 0.05 s | identical except `python`, `elapsed_seconds` |
| `code/b3_four_atom_exact.py --expect-source-sha256 b33647b8… --output …/b3-exact.json` | 0 / 0.9 s | `exact_checks_passed: true`; identical to `outputs/b3_four_atom_independent.json` except `python`, `seconds`; proof payload SHA-256 `8fe7d593…` |
| `code/a5_n8_witness.py outputs/a5_n8_interior_witnesses.json --input-sha256 ca564810… --driver-sha256 bc8ed34a… --output …/n8-witness-standalone.json` | 0 / 4.0 s | `observed_lower_bound: 44`, `lower_bound_certified: true`, `completeness_certified: false` |
| `code/a5_checker.py outputs/a5_n3_certificate.json.gz` | 0 / 273.6 s | identical to `outputs/a5_checker_full-integration.json` except `python`, `elapsed_seconds`; 7/6/2 |
| `code/a5_checker_n4.py outputs/a5_n4_certificate.json.gz --global-file outputs/a5_n4_global.json` | 0 / 200.7 s | identical to `outputs/a5_checker_n4_developer.json` except `python`, `seconds`; total 27; count and global verified |
| `code/a5_checker_n5.py outputs/a5_n5_certificate.json.gz --global-file outputs/a5_n5_global.json` | 0 / 635.1 s | identical to `outputs/a5_independent_n5_developer_certificate_check.json` except `python`, `seconds`; total 25 |
| `code/a5_checker_n6.py outputs/a5_n6_certificate.json.gz --global-file outputs/a5_n6_global.json` | 0 / 789.1 s | identical to `outputs/a5_checker_n6_developer.json` except `python`, `seconds`; total 41 |
| `code/a5_checker_n7.py outputs/a5_n7_certificate.json.xz --global-file outputs/a5_n7_global.json` | 0 / 1518.6 s | identical to `outputs/a5_checker_n7_full-integration.json` except `python`, `seconds`; total 50; count and global verified |

### Auditor-owned independent checks

None of these imports developer code. All exited 0. Earlier trial failures were script defects, fixed before the final runs; they are listed in the sub-audit reports.

| Target | Script (in `audit-support/claude-audit-01/`) | What it establishes |
|---|---|---|
| A2 | `a2/audit_a2_direct.py`, `a2/audit_a2_formula.py`, `a2/audit_a2_compare.py` | certified direct corner values for n=2–28; formula-level bounds for n ≤ 4096; enclosures overlap |
| A4(a) | `a4/audit_a4_identity.py`, `a4/audit_a4_g.py`, `a4/audit_a4_rcen.py`, `a4/audit_a4_n3.py`, `a4/audit_a4_edges_scope.py` | identities 70/71 and λ = S_n − Δ; rigorous g bracket; R_cen convergence; small-n scope |
| A5 | `a5-checker/embed_numeric_check.py`, `a5-checker/n4_mutation_probe.py`, `a5-checker/n3_primitive_probe.py` | checker embeddings; mutation rejection; primitives |
| A5 n=8 | `a5-n8/verify_n8_witnesses.py`, `a5-n8/controls_n8_witnesses.py`, `a5-n8/census_padua_maxima.py`, `a5-n8/naive_grid_maxima.py` | 44/44 independently verified; controls; census for n=3–8; Table 3 mechanism |
| B3 | `b3/b3_audit_independent.py` | whole-interval exact refutation in both orders |
| B1 | `b1/b1_exact_check.py`, `b1/b1_taper_scan.py` | exact and mod-p ranks; taper scan |

`audit-support/claude-audit-01/MANIFEST.json` lists every auditor file with its bytes and SHA-256, and says where it is stored.

## Orchestrator spot checks of sub-auditor findings

I opened each cited location before recording a finding. All were confirmed:

- the hard-coded `'squared_gap_and_reference_inequalities':True` (`code/b3_four_atom_exact.py:129`), set after only two scalar assertions (108–110);
- the hard-coded `denominator_sign = 1 if k > j else -1` (`code/a2_exact_check.py:55-56`);
- the "reconstructed … by hand" wording (theory 03:50);
- "Current77resolves the preregistered" (`proposed-record-changes.md:162`), set against 77:121 and T-A4a.md:35;
- the stale OPEN wording at theory 08:6, 40:40 and T-A5-n6.md:19;
- the contradictory wording at theory 41:59 versus 41:69;
- `checks/decisive-gen1-3.md:18` at `9bd14a6` reading "x + y = 2 + ε_k";
- the run-together words in the New blocks at `proposed-record-changes.md:188,211,234` and in the results proposal.

## Findings (severity-ranked; all minor; none changes a claim, proof, checker or evidence)

### Integration proposals

**F1 — Shared-record proposal text is not fit to apply literally.**
- The B3 and B1 New blocks (`proposed-record-changes.md:188,211,234`), the A5 New blocks (:80, :102) and the results-file proposal (:252–268) contain many run-together words, confirmed at byte level: "PROVEDandREFUTES", "EVERYfixedpositive", "Part2Claudeaudit", "analyticproofs", "N8at least44interior".
- "REFUTED" is used as a status word (report.md:14; results proposal). Prefer "PD-N… PROVED; specified S(α) REJECTED: refuted".
- The OPEN_TARGETS New block at :31 writes the literal "Dependency: `PD-T?proof-attempts-codex-01 (audit pending)`" into a shared record. The required literal label is for topic files; shared records should cite PD-T101.
- The checklists say "IDEA-17", which collides with global IDEA-017 (IDEAS.md:25); the intended entry is IDEA-206. They also use source-local names where final IDs exist: PD-T098, PD-T100, PD-N039, PD-T060.
- The Part2 local "negative01/N01" collides with the programme's N01 in the same paragraph (:188).
- *Disposition:* rewrite every New block as clean prose, using final IDs for every existing record.

**F2 — The A5 PARTIAL wording would relabel PD-T100.**
- The text proposed for programme theory 06 (PD-T100) says "The whole A5 target is PARTIAL" (:80, :102).
- PD-T100 itself is MEASURED (PROOF_STATUS:100), and its n=8 part keeps a MEASURED reference (theory 61:10).
- PARTIAL fits only the OPEN_TARGETS A5 certification item, which is split into PROVED n=3–7 and OPEN n=8.
- *Disposition:* say explicitly that PD-T100's registry status stays MEASURED, and that the split results carry the PROVED cases.

**F3 — The PR-preparation checklists are incomplete.**
- **Split records.** The source "Split into:" lines are not updated: programme −04:8, −05:8, −06:8, N01/N02:8. The crosswalk mappings omit A2 01/02 (:59), A4 71–76 (:168), and programme 06 → 61/64/65 (:133). OPEN_TARGETS.md:19 ("A2/A3 asymptotics … remain OPEN") would go stale.
- **B1 pointers.** PD-N040 (programme N02 record:32, "(ii) … MEASURED (t ≤ 9), not proved"; PROOF_STATUS:102) and IDEA-192 (IDEAS.md:486) get no dated pointer to 90–93. The proposal says only "PD-N040 remains unchanged" (:234, :237); Part1's precedent added pointers.
- **Literature.** No LIT addenda are proposed for the new primary readings:
  - the full KL2021 paper, LIT-379;
  - arXiv 2605.23299v1 Table 3 (LIT-388 stays "UNVERIFIED", INDEX:215, and IDEA-048 still says "arXiv2605.23299 pending", IDEAS.md:88);
  - Bos 2006 Thm 3, LIT-312.
- **Registry entries.** The checklist (:214) does not say where N01, N02 and the B3 candidate C1 enter the IDEAS obstruction and disposition tables. The provisional `IDEA?proof-attempts-2-codex-n4-01/02` still read "active"/"OPEN route" (T-A5-n4:23, :33).
- **IDs.** Integration will need a fresh final-ID reservation under the WORKFLOW procedure, about 42 PD-T and 2 PD-N.
- **Windows entry.** The LOG's intended Windows results entry is superseded by the repository-only rule and should be dropped, not written.
- *Disposition:* complete the checklists. No shared write is needed in this branch until authorized PR preparation.

### Statement and provenance wording

**F4 — B1: the source normalization and the domain hypothesis.**
- **Normalization.** B1's referenced definition, `checks/decisive-gen1-3.md:18` at `9bd14a6`, gives Ldiag as x+y = 2+ε_k. The code, `orf2d.py:93,129`, uses a = 2+√2ε. Theory 93:10-14,23 calls the code form "the literal source" without mentioning the other.
  - The proof holds verbatim for a_j = 2+κε_j with any κ > 0.
  - *Disposition:* add one κ-general sentence to 93.
- **Domain.** The proposed registry sentence (:234) omits the node-domain hypothesis (nodes in [−1,1]², or max(x_i+y_i) < min a_j), on which every sign argument depends (90:10,37; 92:10; 93:10).
  - *Disposition:* restore it in the proposal.

**F5 — A4(a) provenance and quantifier wording.**
- **Provenance.** "Preregistered central-envelope obligation" (:162) and 77:121 ("registered before the mathematical checks") overstate. The R_cen convention was fixed after the first analytic reduction (T-A4a.md:35; a4-input-preparation "Definition issues" 1).
  - *Disposition:* say "registered after the analytic reduction 70/71, before 74–77 and before any numerical run". It helps to note that the window choice is not load-bearing: the same expansion holds for any |t−π/2| ≤ ρ_n with ρ_n → 0 that contains C_n's point.
- **Quantifier.** Theory 76:25-29 quantifies over β_n and s_n, but Δ_n also depends on the edge sign ε_n, which may vary along a maximizing sequence (77:84). The proof is uniform in ε through the reflection.
  - *Disposition:* state the result "for every sequence (ε_n, β_n, s_n)".
- **Dependencies.** 74:149, 75:132 and 77:96 depend on A2-01 (only Λ_c/log n → ∞ is used), and 71:84 depends on A2-04 (3).
  - *Disposition:* cross-reference this audit's A2 acceptance in 77's status line.

**F6 — A2: independence and supplementary-check scope overstated.**
- **Independence.** Theory 03:50 says the route agent "reconstructed … the harmonic/quadrature expansion by hand". independent-checks-a2.md:31,57 show that agent *supplied* it, and its hash-pinned receipt (:15–19) covers only theory 04. So before this audit, 03's 1-D steps (2)–(6) and the text of 01/02 had no check independent of their author. They are now independently re-derived; see above.
- **Stale pin.** independent-checks-a2.md:17 pins theory 04 at `80272d34…` (commit `ba5ff75`). The later edits up to `24b3f74` change only Checks (04:56) and Open items (04:170).
- **Sign rule.** `code/a2_exact_check.py:55-56` hard-codes the sign rule in an abstract cyclotomic field without a certified real embedding. The positive-sum comparison at line 74 is therefore nearly tautological and does not test the sign step of 04 §A. T-A2:53 and 04:56 ("all6 positive-sum identities pass") read as more than this.
- **Locators.** The KL printed-page locators (T-A2:25; 03:54; 04:60) could not be confirmed, since only page-less text was available.
- *Disposition:*
  - reword 03:50 (also T-A2:57, LOG:52);
  - note the non-mathematical later edits in the receipt;
  - describe the regression as "kernel identity + same-mesh square identity; the sign step is analytic";
  - label the page numbers "per developer reading", or confirm them.

**F7 — B3: driver labelling and exposition.**
- `code/b3_four_atom_exact.py:108-110,129` sets `'squared_gap_and_reference_inequalities': True` after two endpoint scalar checks only. Eigenvalue localisation |λ₋| < 8t, g ≥ h/2 and d ≤ 10t are proved in N01's text but not machine-checked by that driver. N01:149 and independent-execution-b3.md:53 say so correctly; the field name invites misreading. All three are now machine-checked on the whole interval by the auditor script.
- N01:111's arithmetic chain is cryptic. The intended chain is (h/2)² = t/40 = 2t·(1/80) > 2t/100 > δ/100.
- The proposal at :186–188 keeps the Old sentence "Nothing here implies S(α) true or false" directly above the refutation.
- *Disposition:*
  - relabel the field or footnote it;
  - add the one-line chain to N01:111;
  - add "(superseded for the specified count by …)" after that Old sentence.

**F8 — A5 records: stale status lines and literature wording.**
- **Stale OPEN wording, never superseded:** theory 08:6 and :96, 09:34 and :94, 40:40 and :91. T-A5-n4.md:23,33 and T-A5-n6.md:19 still show "Status: OPEN; active" without a superseding header, unlike n5 and n7.
- **Theory 41** contradicts itself: :59 calls 25/41 versus 23/39 "a bounded candidate correction", while :69 says "No … paper correction … is inferred".
- **Theory 61:58** says "published 56"; for an arXiv v1 preprint, "reported" or "printed" is more accurate.
- **Labels.** The n3–n6 literature-comparison receipts and records 06/10/16/41/51 quote Table 3 without the explicit LITERATURE label that n7/n8 carry.
- *Disposition:* add dated superseding notes and harmonize the wording. No mathematical change.

### Informational (no disposition required)

- **I1 (A5).** The n4–n7 checkers are one code lineage, so the independent executions re-ran the same code. A common-mode defect would affect all of them. The core review, the mutation probes, the independent n=8 verifier and the census found none. Record this as residual risk.
- **I2 (A5).** The checker verifies predicates, not disposition labels, so the per-label tallies quoted in theory files are certificate-label counts, not invariants. Also, 06's reuse of Part1 theorem 03 for y = ±1/√3 is corroborative only: `check_edges` proves strictness independently.
- **I3 (B3).** The pivots exceed (1/5)² on the interval, so the family refutes S(α) for every p ≤ 1/5. A leading-order scan suggests the failure needs g ≲ 0.64√δ. That is a genuine √δ-scale effect, consistent with refuting α > 1/2 only; nothing is claimed at α = 1/2.
- **I4 (B1).** There is no uniform rank margin along the taper when the sample contains the corner (1,1) (φ₃ ≈ 0.68 ε_min). This is consistent with the explicit refusal to claim stability. The same proof also covers 3 ≤ T ≤ m−1 and odd m. Whether the umbrella B1 should be labelled OPEN or PARTIAL is AC's call; the current OPEN is conservative.
- **I5 (A4).**
  - For n=3, 4, 5 the largest non-corner edge maxima lie on the horizontal edges; for 6 ≤ n ≤ 65 the largest interior-edge maximum equals R_cen. This is additional evidence that R_search ≠ R_cen at small n, and that question belongs to the OPEN A4(b)/(c).
  - For even n the literal midpoint λ(±1,0) is far below R_cen. 72 and 77 correctly use π/2 ± π/(2m).
- **I6 (A2).** The constants are very loose. 01 beats Λ_c ≥ 1 only for n ≥ 114616, and the certified max |Λ_c − L_n²| over the checked range is 1 (n=2). The target asked only for explicit O(1) constants.
- **I7 (literature).** The printed Pad_n definition (eqs. 7–8 of 2605.23299v1) has index inconsistencies, which do not affect the counts.

## Evidence and storage

- **Committed under `audit-support/claude-audit-01/`:**
  - every auditor script;
  - all developer-checker rerun outputs for n3–n7, A2, A4, B3 and the n8 witnesses (JSON, plus the n3 stdout);
  - the auditor B3 exact certificate JSON and the primary n8 verifier JSON;
  - the other auditor outputs of at most 12 kB;
  - `MANIFEST.json`, `COLD_STORAGE.md` and `subaudit-reports/`.
  
  The committed auditor-generated outputs total about 225 kB. That keeps the topic's generated total near 4.9 MB, under the 5 MB limit, with each file under 1 MB.
- **Cold storage:**
  - Fourteen larger auditor outputs (about 0.8 MB, listed in `MANIFEST.json` with SHA-256 and bytes) are kept only in a single archive of the complete auditor directory plus this record. None is needed to reproduce a verdict: each is regenerated by the committed script that produced it.
  - The archive is delivered to AC's Padua cold storage at `Downloads\padua\cold_storage\padua-proof-attempts-2-20261101\claude-audit-01\` through the device bridge. Its SHA-256, bytes and delivery receipt are in `audit-support/claude-audit-01/COLD_STORAGE.md`.
- No developer or independent evidence was overwritten or deleted.

## Remaining uncertainty

- **Common code lineage.** The A5 n4–n7 proofs rest on checker code from one lineage (I1), on the declared trusted base (SymPy exact algebra, FLINT, CPython integers), and on reruns of that same code. The reduction and the checker core were reviewed line by line for n3/n4 and through diffs for n5–n7, not line by line.
- **Not exactly certified:** the stored irrational B1 source parameters, and the exception locations.
- **Literature reads.** The paper readings are model-mediated text reads without PDF page images.
- **No full n=8 rerun.** No n=8 completeness run was attempted, as instructed.

## Outcome and next step

The audit is accepted for the stated scope with minor findings F1–F8. Per WORKFLOW, the findings return the topic to **Stage WORK** for a documented Codex `response-01.md`. After that, PR preparation can proceed without re-audit, unless a response materially changes a claim, proof, checker or evidence. PR12 stays draft until then. Only AC merges.
