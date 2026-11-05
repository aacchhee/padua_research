# Audit-01 — Padua Lebesgue follow-ups (T1–T4) — Claude cross-family audit

- Auditor / orchestrator: Claude, Opus 5.5 (`claude-opus-5-5`), xhigh effort (chosen as handoff 02 asks: novel analytic proofs plus a consequential computer-assisted count). Two sub-auditors under this orchestration, Claude Opus 5.5 high, read-only (reports in [audit-support/claude-audit-01/subreports/](audit-support/claude-audit-01/subreports/)). The developer was Codex, so the audit is cross-family.
- Rules read at branch head `407fe83f5a709ae6d8da986d6eee074a0bcb21fc` (AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md).
- Audited input: `5b2e36710144d5ab8dd1b8ee9dc2e8b0f1e13033` (handoff 02). `git diff 5b2e367 407fe83` touches only LOG.md and the two handoffs; theory, code and evidence are byte-identical. Base/main `440d1079e42c3ef21c40d1cf8870f5b206410c6a` (unchanged on origin at audit time).
- Audited file hashes (SHA-256 at the input SHA, all theory, all code and the main prose/evidence indices): [audited-hashes.txt](audit-support/claude-audit-01/audited-hashes.txt).
- Date: 2026-11-05. Environment of all auditor executions: Python 3.13.18, SymPy 1.14.0, python-flint 0.9.0 / FLINT 3.6.0, mpmath 1.3.0, NumPy 2.5.3, SciPy 1.18.1, 2-core cloud sandbox.

## Decisions

| Scope | Decision |
|---|---|
| T1 PD-T184 (exactly 44 strict interior maxima, n=8) | **Mathematics ACCEPTED, PROVED.** Finite reduction and receipts reviewed; archived proof payload reproduced; the auditor's monolithic run re-verifies all 44 interior roots (§T1.4). |
| T1 PD-T180 (62 = 44 + 16 + 2 on the closed square) | **Mathematics ACCEPTED, PROVED.** The developer's composition is sound (§T1.1). In addition, the auditor regenerated the boundary with an identical proof payload and ran one complete monolithic original `Verifier.run`: `count_certified: true`, 62 (§T1.3–T1.4). |
| T2 t2-01, t2-02 | **ACCEPTED, PROVED** at their written scope (limiting integrals only). |
| T3 t3-01 | **ACCEPTED, PROVED**; numerical enclosures at the five rational positions confirmed. |
| T4 t4-01, t4-02, t4-03 | **ACCEPTED, PROVED**; κ and c brackets independently confirmed by a different rigorous route. PD-T098's full expansion stays OPEN; PSLQ nulls MEASURED only. |
| Split/status discipline, candidate retention, novelty wording, LIT-388 wording | Accepted, with MINOR items F1–F4 below. |
| T2/T3 prospective-gate timing | **Protocol deviation confirmed; not waived and not cured.** Actual impact: minor (F1 only). Separate disposition in §Protocol. Preserved for AC. |
| Evidence / retention / budget | Accepted with MINOR items F5–F9. |
| Stage | **WORK** (minor findings require a developer response). No mathematical finding is open. |

## Read coverage

Orchestrator (in full): handoffs 01/02, LOG, plan, report, all nine theory records, attempts/T1.md, gate-t2-t3.md, gate-t4.md, evidence/t3-verification.md, t1-replay-composition.md, COLD_STORAGE.md, code t1_check_boundary.py, t1_compose.py, t1_payload.py, t1_join.py, t1_boundary.py (head), t3_series.py, t4_constant.py; frozen a5_checker_n8.py `evaluate`, `Interval`, `boundaries`, `run`, `main`; a5_checker_n8_staged(_cached).py; inherited definitions PD-T211 (argmax-alln-codex-04), PD-T212 (argmax-alln-codex-05), PD-T159 (proof-attempts-2-codex-04); state/IDEAS.md lines 1–439; PR20 body; results file. Sub-auditor A (novelty/literature/protocol): state/IDEAS.md lines 440–889 in full with every obstruction/disposition table there, all gates/attempts/plan/report, literature-comparison, all proposals and ALLOCATIONS, LIT-379/LIT-388 records and addenda in literature/INDEX.md, the later-read T2/T3 sources (full T-A4a attempt, full IDEA-206 record, IDEA-303–305 and FINAL_CANDIDATES paragraphs, IDEA-318 original record), base PROOF_STATUS/CURRENT/WORKFLOW sections. Sub-auditor B (T1 evidence): independent-checks-t1.md, gate-t1.md, attempts/T1.md, t1-native-notes.md, COLD_STORAGE.md, ALLOCATIONS.md, all T1 receipts and guard-delta records. Together the complete state/IDEAS.md was read. literature/INDEX.md was read for LIT-379/388 and the coverage addenda, not cover to cover; no novelty or priority claim is made by this audit. Not read: independent-checks-analytic.md beyond its T4 editorial section (the auditor reconstructed the mathematics directly instead).

## Analytic targets — reconstruction

All six records were reconstructed step by step against the literal PD-T211/PD-T212/PD-T159 definitions.

**t2-01.** Vertical: the tangent substitution, the exact switch `2dx/max(U²−x², x²−L²)`, the map to `dy/[x(1+|y|)]` and identity (4) (`(1+pc)²−q²s²=(p+c)²`, `U²+L²=2(s²+q²)/(p+c)²`) check. Pairing b with π−b and the split at s=q give (5); both substitutions and the identification `g=(4/π²)∫F` (equal to PD-T188's form by Fubini) check. `H'=−A`, the weighted-average form (7) and the monotonicity of A(t)/t give F and F(r)/r strictly decreasing, so (2) is strictly increasing in p². Horizontal: the reflection average replacing 1+B by 1, the substitution `B=pc+qsy` (the D factor cancels), the period-π reduction to 2K(R) and `R²=y²+p²(1−y²)` check; the central value 1 via `t=tan(x/2)` and `∫₀¹(−log t)/(1−t²)=π²/8` checks. **Accepted.**

**t2-02.** (3)–(4) (`|K(√(1−t²))−log(4/t)|≤t/2`), the main term with (5), the error integral `π/2−1`, and the band comparison (6) (`min(X+1,Y−1)` vs `min(X,Y)`, band width ≤2d) all check. **Accepted.**

**t3-01.** `a(x)=∫₀¹(1+t)(1+x²t²)^{-1/2}dt`, the expansion with argument in [0,1/2], the tail `3/(2√2)·2^{-N}`, the averaged polynomials P_k, the moments and the M_l recurrence (derivative of `r^{2l−1}√(r²−q²)`), M₀=atanh p and tail (1) check. Centre chart: ratio ≤1, `c_k≤1`, `I_k≤I_0=π²/8`, tail (2). Endpoint chart: the classical-form series (6) is justified locally (ODE plus reduction-of-order uniqueness, normalised by t2-02), with positive brackets and tail (3); the monomial rules check. **Accepted.**

**t4-01.** (4) reproduces from PD-T159 (3)/(5) (the k=n reference row vanishes, so the weights agree). The fixed-offset limit (6) and pairing (7) check. The constants in §2–§3 were re-derived (`|f−H(a,0)/|u||≤2/δ²+π≤6/δ²`, 13/(nδ²), 112M/(nδ²), 32M/(nδ³), the discarded-row bound π⁴(δn+1)/(n+1), the offset tail 4π²/M) and give (8) and 604 n^{-1/5} for n≥32. §4: the cotangent partial fraction, `a_p=2Σ_{r>p}ζ(2r)4^{-r}∈(0,4^{-p}]`, the cancelled l=1 pole, `|b_q|<9^{-q}`, `|c_k|<2·4^{-k}`, and κ=(8/π²)Σc_k/(k+1) with tail 8/[3(K+2)4^{K+1}] check. **Accepted.**

**t4-02.** The cot-pairing (2) for both parities, (3), the bound `|v''|<1` (416/(27π³)·4/3), the midpoint error π²/(96n²), the singular part (2/π)(2H_{2n}−H_n) and (6) give |L_n−A_n|≤1/(4n²). The stated 3/(16n²) is valid but loose (1/(8n²) suffices). **Accepted.**

**t4-03.** `|L²−A²|≤A_n/(2n²)+1/(16n⁴)`, `|A_N²−A_n²|≤(log N+2)/n`, and b=(8/π²)(γ+log(8/π)) agrees with PD-T098. **Accepted.**

### Independent executions (analytic)

All commands were run by the auditor. The auditor's code imports no topic code.

1. [claude_analytic_checks.py](audit-support/claude-audit-01/claude_analytic_checks.py), exit 0, 11.2 s. Output [claude_analytic_checks.json](audit-support/claude-audit-01/claude_analytic_checks.json):
   - **RIGOROUS (Arb).** κ was computed by ball integration of a digamma rewrite of t4-01 (1): `κ=∫₀¹(2/π)[π+2cot(πt/2)(ψ(1/2)−ψ((1+t)/2))]dt`, with [0,2^{-200}] bounded by the integrand range [0,4] (mean value, ψ'≤π²/2). This is a route independent of the developer's zeta-coefficient series. Result `κ∈[0.91971011838849253509951822579023674611 ± 8.7e-39]`, `c∈[1.84616031042392607975983873794781194402 ± 9.4e-39]`. Both lie strictly inside the claimed 30-digit brackets.
   - **MEASURED, mpmath at 40 digits.** The T2 1D formulas at the five T3 positions lie inside all ten claimed 16-digit enclosures. g_v and g_h are strictly decreasing to the centre on a 20-point grid. The t2-02 bounds (1)/(2) hold for d from 0.3 down to 1e-5. The t3 I_k closed form matches both (5) and the log-cosine form for k=1..6 (to ~1e-22). The t4-02 inequality holds for n=1..399 and n=512, 1000, 2047, 4096 (max 4n²|L−A|=0.1745). κ from the integral and from the series agree to 28 digits. a_p∈(0,4^{-p}] holds for p≤80.
   - **MEASURED, float64.** The ORIGINAL PD-T211/212 double integrals with exact switches agree with the 1D formulas to ≤5e-15 at all five positions. Reflection symmetry holds to ≤7e-16. A direct finite corner sum gives Λ_c−L_n²=0.92044 at n=4096/4097 (κ≈0.91971, parity-free drift ~3/n).
2. Reruns of the developer's evaluators (sources unchanged, SHA-256 `55e2a976…`, `7f8f5772…`, `b48d488e…`):
   - `t3_series.py --terms 72 --digits 16`: exit 0, rows identical to `evidence/t3-series-developer.json`.
   - `t3_quadrature.py`: exit 0, identical except the python field and the series-receipt hash.
   - `t4_constant.py --order 64 --bits 320`: kappa ball identical to the developer receipt.
   - `t4_constant.py --order 96 --bits 448`: assertions pass.

   Receipts: [reruns/](audit-support/claude-audit-01/reruns/).

## T1 — degree-eight count

### T1.1 Finite reduction and composition (reviewed)

The interior predicates are the frozen PD-T170 reduction; PD-T184's derivation (strict maximum ⇒ every active P_s stationary with NSD Hessian ⇒ disposed or equal to an accepted root, with injectivity) is correct. Boundary: edge-crease exclusion by the multiplicity-one cover, complete norm/Sturm sign coverage, strict tangential maximum plus strictly negative inward derivative, all-active strict inward corners. Every non-node corner must be accepted as `max` or the run rejects, so acceptance implies an exact count.

The composition (t1-replay-composition.md) is sound:
- `Verifier.boundaries` reads only `cardinals`, `exact_pattern` and `edge_flat_values` (checked by reading the AST and the driver's assertion), so a fresh Verifier built from the same field embedding runs identical predicates.
- The boundary receipt is bound to the archived field certificate, and the typed identity covers `field_embedding`.
- The summary block is executed literally, after a bound-variable rename verified by inverse AST comparison.
- The excluded fields (`metadata`, `summary.seconds`, permitted-but-absent `Pcache`/`boundary_summary.seconds`) are read nowhere by the frozen checker.
- The cached evaluator was checked by the auditor to perform the same ordered per-term products, floor/ceil divisions and sums as the frozen `evaluate`/`Interval.__mul__`.

### T1.2 Reproduced identities

- Archived blob `3f65a77d…`: 637,163 B, SHA-256 `a3b4f278…`.
- The archive's typed proof payload is 18,969,878 B, SHA `e22a9b55…`, recomputed with the committed helper.
- Sub-auditor B independently recomputed:
  - the interior facts `020deb8c…`;
  - the boundary facts `f4f1e990…` and composition facts `075741b1…`;
  - all seven guard-only deltas, with old blob bytes equal to the executed SHAs, AST identity after removing the guard, and 14 `-O`/`-OO` refusals;
  - that no historical receipt was relabelled.
- evidence-manifest.json: all 123 rows match their hashes and sizes. No code/evidence/theory file is unlisted, and no evidence file exceeds 16 KiB.

### T1.3 Auditor boundary regeneration (executed)

`PYTHONPATH=<deps> timeout 9000 python3 -B topics/padua-lebesgue-followups-20261103/code/t1_boundary.py --output <scratch>/boundary-claude.json` (current guard-only producer `a70e2532…`, frozen `a5_n8_boundary.py` `6088db34…`) exited 0 after 2250.7 s:
- edges with 107/107/155/123 patterns;
- 16 edge and 2 corner proposals, 0 unresolved;
- dispositions identical to both developer boundary receipts;
- raw 4,822,048 B, SHA `cf141bab…`.

Its typed proof payload, computed with the committed `t1_payload.proof_payload`, is **4,821,831 B, SHA `1316b929ec142e0274f8c68a37e59a85b2136f8b322077ecd8172918719b54f2` — identical to the developer's lost artifact `adfe1107…`** (evidence/t1-boundary-payload.json). The boundary proof object is therefore reproducible from committed code, independently of the sandbox that held `adfe1107…`.

### T1.4 Monolithic original run (executed)

The auditor wrote [claude_monolithic_n8.py](audit-support/claude-audit-01/claude_monolithic_n8.py) (SHA-256 `75c22c6d…`, unchanged during the run). It builds a literal join of the Git-retrievable archived interior (`a3b4f278…`) and the auditor-regenerated boundary (`cf141bab…`); the summary edge/corner/total fields are copied from the boundary *proposal*. The join is 1,702,179 B, SHA `82826d03…`. The wrapper then calls the **unchanged frozen `a5_checker_n8.main()` without `--allow-partial`**, so the complete original `Verifier.run` executes in one process:
- the embedding;
- 45 node cones;
- the root witnesses and the full leaf partition;
- every leaf and mask;
- `Verifier.boundaries`;
- every final summary/boundary-summary predicate.

The only runtime substitution is the frozen cached evaluator, which the auditor checked line by line to be bit-identical (§T1.1). Frozen source hashes are identical before and after the run.

The command ran from `audit/t1`:

```sh
PYTHONPATH=<deps> timeout 14000 python3 -B claude_monolithic_n8.py --repo <clone> --interior archived-interior.json.gz --interior-sha256 a3b4f278a322338fb65f60922b4251265288148e1a09fd22882215004e81c324 --boundary boundary-claude.json --joined-out joined-claude.json.gz --receipt monolithic-receipt.json
```

It exited 0 after 3117.8 s. [Receipt](audit-support/claude-audit-01/monolithic-receipt.json):
- `accepted: true`, **`count_certified: true`**, `interior_complete`/`boundary_complete`/`complete_prefix_partition: true`;
- 153,520 leaves, 541,882 patterns, 45 node records, 3,474 breakpoints;
- **44 interior + 16 edge + 2 corner = `total_maxima: 62`**;
- 492 edge patterns, 32 active corner masks;
- Python 3.13.18.

The full checker output (20,800 B, SHA `a5d133a6…`) is kept off-repository. Its [typed comparison](audit-support/claude-audit-01/monolithic-facts-comparison.json) shows every interior root value, edge root, corner root and node fact equal to the developer's replay receipts.

This is a **third, cross-family executor and a monolithic full run**. It discharges the developer's acknowledged "no monolithic joined `Verifier.run`" limitation without relying on the composition argument. It also re-establishes the boundary stratum on an artifact independent of the lost `adfe1107…` file. PD-T180 now rests both on the developer's composition and on this direct run.

Scope limits:
- The archived interior, not the fresh one, was used. The two are typed-identical by the developer's two comparisons, and the archive is the input PD-T184's proof already uses.
- The auditor's run used the frozen cached evaluator, as all developer replays did.

## Findings

No BLOCKER. No MAJOR remains open; sub-auditor B's MAJOR (the boundary input existed only in the developer sandbox) is downgraded to F5 by §T1.3/§T1.4. Every item below requires a written developer response. Items marked *proposal* concern unapplied text for later preparation.

| ID | Severity | Location | Finding | Required action |
|---|---|---|---|---|
| F1 | MINOR | gate-t2-t3.md:41-43; preparation/proposed-registry-additions.md:78-79 | T2/T3 closest-entry fields omit IDEA-318 (whose original note records the measured centre-smallest gap and suggests centreward monotonicity) and IDEA-324, and the MEASURED PD-T207/208 profiles. They are in the shortlist line but not in the comparison. | Add them as closest entries with the separation (measured finite profile vs proved limiting-integral ordering); amend the proposal rows. |
| F2 | MINOR | theory/t4-02-one-dimensional-remainder.md (Depends on/Sources) | Does not name PD-T158, whose one-dimensional estimate it sharpens (2/n → 1/(4n²)). | Name PD-T158 as the predecessor estimate; no proof change. |
| F3 | MINOR *proposal* | proposed-record-changes.md:55, :69 (PD-T211, PD-T230) | The new rows replace the "center-minimality OPEN/excluded" wording rather than keeping it with a dated supersession note (WORKFLOW: never silently reword). PD-T212 annotation undecided. | Keep the original clause and append a dated note pointing to t2-01/t2-02; decide PD-T212. |
| F4 | MINOR *proposal* | preparation/proposed-t1-record-updates.md (PD-T184, PD-T180 rows) | The new rows drop the existing audit-01/response-01 links and the OPEN/deadline history wording. | Follow the PD-T181 row pattern (retain history, add the new proof link). |
| F5 | MINOR | COLD_STORAGE.md; theory/t1-closed-count.md (Open items) | Both boundary replays checked `adfe1107…`, which exists only in developer scratch, and regeneration changes the raw SHA. Mitigated by this audit: regeneration reproduces the identical typed payload `1316b929…`, and the auditor's monolithic run accepts it (§T1.3–T1.4). | Record in COLD_STORAGE that the boundary payload identity is regeneration-stable (audit evidence) and name `1316b929…` as the durable mathematical identity; physical delivery stays pending. |
| F6 | MINOR | code/t1_check_boundary.py `frozen_boundary_ast`; t1_compose.py `summary_predicates`; receipts | The pinned AST hashes (`73fc0216…`, `61812bc0…`) are CPython-3.12-specific. Under 3.13.18 they are `aad6c3e2…`/`658c…`, so `t1_compose` rejects valid receipts (confirmed by the auditor). | Document "CPython 3.12.x required for AST pins" in COLD_STORAGE/attempt T1 and the receipts' reproduction notes. |
| F7 | MINOR | attempts/T1.md:39 | Says the developer's interrupted symbolic corner cross-validation (exit 130) has its "receipt preserved", but no such receipt is committed (only the independent exit-143 receipt). | Give the scratch locator/SHA, or reword as "not retained". |
| F8 | MINOR | attempts/T1.md:129; evidence/t1-fresh-join.json | The join receipt carries no exit/session/timestamp/producer field; the 7753 producer binding is only indirect (join assert plus composition check on scratch-only metadata). | Soften the wording or add a small addendum receipt. |
| F9 | MINOR | LOG.md:103 | The "about 4.21 MB" whole-repository generated-data figure does not reproduce. Sub-auditor B gets 4,574,085 B at 5b2e367 including manifests, or 4.19–4.37 MB under other exclusions. All are under 5 MB, but close. | State exact bytes and the counting method. |
| N1 | NOTE | theory/t2-01 (7); theory/t4-01 eq. (1) | Typos: `[A(t)/t],2t\,dt` (comma for thin space); `dt` placed inside the l-sum. | Fix when editing. |
| N2 | NOTE *proposal* | proposed CURRENT paragraph; state/CURRENT.md:82, RESULTS.md:111 | The existing "center-minimality / general-β OPEN" clauses are not marked superseded at the proved scope. Results file line 9 could say "certified candidate correction". | Address at preparation. |
| N3 | NOTE | gate files | No gate carries a timestamp. The gates and the full t2-01 proof first appear together in commit 4cfad03 (11:22:59Z), so gate-before-mechanism ordering rests on the workers' reports. | Record times in future gates. |
| N4 | NOTE | prose only | The per-edge pattern counts 107/107/155/123 were prose-only in the developer receipts. The auditor's regeneration corroborates them, including 123. | None. |

## Protocol disposition — T2/T3 prospective-gate timing

**Confirmed deviation, not waived, not cured by later reading.** The first published gate (commit `4cfad03`, together with the t2-01 proof) already asserted reading "inherited attempts P1-P2-edges/T-A4a". The full T-A4a attempt, the IDEA-206 full record, the IDEA-303–305 registration paragraphs and the FINAL_CANDIDATES shortlist paragraphs were completed later. Commit `b721709` added the timing qualification but left the earlier sentence in place.

Actual impact, determined by sub-auditor A reading those sources: none of them states centre-minimality, g_h(π/2)=1, a general-β series or a κ formula. Every existing record keeps centre-minimality OPEN/excluded. The only consequence is the closest-entry omission F1 (IDEA-318's measured-centre note). No candidate, verdict, obstruction or kill test would change.

Disposition: protocol non-compliance recorded; impact minor; it does not affect the mathematical acceptance and, once F1 is answered, does not by itself block readiness. Whether to accept the topic with this recorded deviation is preserved for AC's decision.

## Retention, scope and limits

- Write scope 440d107..5b2e367: only the topic directory plus results/padua-lebesgue-followups-20261103.md (146 files, all additions). No shared registry, frozen source or merged theory changed (sub-auditor A).
- No final IDs are assigned. Reservations PD-T266–285, PD-N092–099, IDEA356–375 and LIT474–481 remain unassigned. A fresh union recheck (including PR19 and retired reservations) is still required at preparation.
- Not re-executed by the auditor:
  - the fresh V3/V4/V5/reflection chain (its identity to the archive rests on the two committed typed comparisons, whose hashes sub-auditor B recomputed from the archive side only);
  - the two developer-side full interior replays as separate processes (subsumed by §T1.4);
  - the PSLQ searches (MEASURED, not consequential).
- The auditor's bulk T1 artifacts (regenerated boundary 4.8 MB, joined 1.7 MB) stay in this cloud sandbox and are not committed. Their identities are in the monolithic receipt; physical delivery to AC cold storage is pending like the developer's.
- Residual risk: the T1 count's trusted base is CPython integers/Fraction, SymPy exact field algebra and python-flint, now exercised by three executions on two Python versions. The T4 brackets rest on Arb plus two independent analytic reductions. T2/T3 digits rest on exact Fraction/outward Decimal code plus a non-rigorous 40-digit cross-check.

## Commands run by the auditor (summary)

Full commands and outputs are in `audit-support/claude-audit-01/README.md`.
