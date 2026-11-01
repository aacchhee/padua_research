# Response-02 developer report — GROUP E34 (A02-M1, A02-L2)

Developer: Claude Opus 5.5, xhigh (mathematical developer). Repository `/home/claude/padua_research`, head `1df5f89` (branch `codex/padua-lanczos-drift-20261101`). The rules were read from `response02-common.md`, `AGENTS.md` and `agents/WORKFLOW.md` (status, split, disposition and evidence sections). Inputs read in full:

- handoff 07, items 1 and 4;
- `audit-02.md`;
- `checks/audit-02/E34.md`, `checks/audit-02/E34/independent_exact.py` and `evidence/audit-02-e34-checks.json`;
- record 15, `ideas-e3-e4.md` and `directions/E4.md`;
- `e4_closure_check.py`;
- the complete `state/IDEAS.md` (lines 1–783);
- PD-T055 (`bj-universal-reorthogonalization-obstruction-open.md`) and PD-T043 (`closed-loop-dot-product-rounding-carries-coefficient-channel.md`);
- PD-N013 (`reorthogonalization-does-not-restore-graded-spaces.md`) and PD-T053 (reference-free bound), as relevant.

No git state was changed. Only owned files were edited or created. `e4_closure_check.py` is untouched (sha256 b22949c6… unchanged).

## (a) Dispositions

| Finding | Disposition | Files and line ranges (post-edit numbering) | Summary |
|---|---|---|---|
| A02-M1 (E34-R1) | FIXED | `tracks/bivariate-lanczos/theory/drift-codex-e4-15-projection-only-closure-obstruction.md`: 48–52 (Negative statement, new display (13)); 98 (status paragraph); 103 (status row); 153–159 (Checks: audit-02 entry and response-02 checker); 209–219 (proof of the Negative statement); 281 (Further instances: limits bullet); 322–325 (History). `directions/E4.md`: 3, 10, 41–42 (new “Relative-source limit” paragraph), 57. `ideas-e3-e4.md`: 137 (IDEA-15 checks), 236 (History). New: `tracks/bivariate-lanczos/code/drift/e4_response02_check.py`, `topics/padua-lanczos-drift-20261101/evidence/response-02-e4-creator-limit.json` | The equality “δ_(A_m)(t)/u→‖v_m‖” is replaced by the exact form δ_A(t)/u=κ_A‖v_m‖/sqrt(b²+u²‖v_m‖²)→(κ_A/b)‖v_m‖, with (κ_(A_m)/b)‖v_m‖≥‖v_m‖ and equality iff κ_(A_m)=b. The T_3/v_21 instance has κ_Y=b, so equality holds there (verified: squared limits 3/2 for Y and 2 for X, the u→0 values of (9)). For v_20 the squared limit is 88/15, while ‖v_20‖²=22/5. (a)–(d), the no-exact/o(u) conclusion and the status (PROVED) are unchanged. Exact regression added. |
| A02-L2 (E34-R2) | FIXED (definition given; candidate stays deferred; no experiment) | `ideas-e3-e4.md`: 11–16 (response-02 header note); 165–224 (IDEA?drift-claude-17 rewritten); 231–235 (History). Record 15: 306–311 (Open items coherence remark); 326 (History). `directions/E4.md`: 13, 47, 58 | Excluded degenerate readings: D0, projection onto a computed span containing the parent (gives zero or the identity); D1, subtracting the projection onto exact S_t (leaves only drift); D2, replacement by the reference column (reference injection). Defined arms: **R17a**, reorthogonalization in extended precision against the stored columns q̂_0…q̂_(p−1) strictly before the parent's graded index; nonzero iff q̂_0…q̂_p are independent; no outside information; the in-span control. **R17b**, projection of the parent onto R_(≤p)=[r_0…r_p], an extended-precision nested graded reference basis of E_(≤p); |γ_p|=|⟨q̂_p,r_p⟩|≥1/2 is required, which keeps the intended leading monomial; outside information enters only through R_(≤p). Both act only on the multiplicand; storage, coefficients and windows are unchanged. H17, the kill criterion (thresholds unchanged, plus γ_p inconclusive), discriminability, predecessors, separation, cost and resume conditions are restated coherently. The false sentence “B_k(Δparent) can carry the missing component along w” is removed and quoted in History. |

## (b) Commands actually run

All from the repository root.

1. `PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python3 -B tracks/bivariate-lanczos/code/drift/e4_response02_check.py --output <scratch>/trial.json`: PASS, 25 instances, 1.6 s. This was a pre-final trial, before a sampled-rule check was added.
2. **Official:** `PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python3 -B tracks/bivariate-lanczos/code/drift/e4_response02_check.py --output topics/padua-lanczos-drift-20261101/evidence/response-02-e4-creator-limit.json`: `PASS: 25 instances, 5 with kappa_creator > b, 2.2 s`.
   - Code sha256 `6b2c0f8737b1755795d1afd2a8c59449043146ab8315682a3b28293f2f144fdf`.
   - Output sha256 `a6faea9967747b9fe962ce58f5af55fe776bf4b5201f54cc364d738aa2da4526`, 86816 bytes.
   - Python 3.13.18, Linux-6.18.44-fc-v185-x86_64-with-glibc2.39, standard library only.
   - The JSON records the command, code sha256, versions and elapsed time (2.19 s).
3. Rerun to `<scratch>/rerun.json`. The output is identical except `command` and `elapsed_seconds` (deterministic).
4. `sha256sum` of `e4_closure_check.py`: `b22949c6…`, unchanged. The response-01 evidence read by the checker has sha256 `956dfe71…`, which matches the record.

The checker's content:

- **Instances.** 25: the 23 distinct configurations of response-01's 28 instances, plus 2 T_3 cases with a different normal direction.
- **Direct computation.** δ_A² comes from the projector of V_m+span{v_m+ηr} at η∈{1/10, 1/100, −1/1000, 10⁻⁴, 10⁻⁶}, via the rank-one generalized Gram matrix (rank ≤1 asserted). One deterministic non-orthogonal two-pass rule is checked to produce that span.
- **Exact assertions.**
  - u²=η²‖r‖²/‖raw_m‖²; (δ/u)² equals κ²‖v‖²/(b²+u²‖v‖²) exactly.
  - 1/(δ/u)² is affine in u² on all five points; its u²=0 value equals L²=(κ²/b²)‖v‖².
  - The gaps are positive, decrease, and are bounded by L²u²‖v‖²/b².
  - κ_(A_m)²≥b².
- **v_20.** The asserted constants are 22/5, 7/15, 28/45 and 88/15. Audit-02's symbolic δ_X²=672η²/(5(216η²+245)) is reproduced at every η.
- **v_21.** The asserted constants are 28/115 and 3/2; κ_Y²=b², and the limits are 3/2 and 2, consistent with (9)'s 84/(56+345u²) and 112/(56+345u²).
- **Cross-check.** κ²/b² and b² equal response-01's evidence on 23 shared configurations.
- **κ_(A_m)>b** in 5 instances: T_3 (2,0), twice; T_4 XYYY (3,0), 9/5; T_4 XYXY (3,0) and (3,1), 7/4 each. The maximum ratio is 9/5.

No other execution. No experiment for IDEA-17 was run.

## (c) Proposed text for files I do not own

Grep result: the faulty “→‖v_m‖” equality appears **only** in record 15. It is absent from `report.md`, `proposed-record-changes.md`, `local-results-entry.md`, `plan.md` and the results file, so none of them needs a mathematical correction. Status-sync proposals follow.

**C1. `results/padua-lanczos-drift-20261101.md`, line 26.** Replace the PD-N?drift-codex-15 row.

OLD:
```
| [PD-N?drift-codex-15](../tracks/bivariate-lanczos/theory/drift-codex-e4-15-projection-only-closure-obstruction.md) | Core lemma/instance confirmed; correction required | The generalized fixed-degree projection-only closure lemma and its ten-node instance are confirmed. Its ancillary limit equality needs the creator-factor correction A02-M1. The original PD-T055 is OPEN. |
```
NEW:
```
| [PD-N?drift-codex-15](../tracks/bivariate-lanczos/theory/drift-codex-e4-15-projection-only-closure-obstruction.md) | PROVED (core confirmed by audit-02; ancillary limit corrected in response-02, re-audit pending) | The generalized fixed-degree projection-only closure lemma and its ten-node instance are confirmed. The relative-source limit is lim δ_(A_m)/u = (κ_(A_m)/b)‖v_m‖ ≥ ‖v_m‖, not ‖v_m‖ (A02-M1). On T_3/BJ with the source in v_20 the squared limit is 88/15 against ‖v_20‖² = 22/5. Exact regression: [response-02-e4-creator-limit.json](../topics/padua-lanczos-drift-20261101/evidence/response-02-e4-creator-limit.json). The original PD-T055 is OPEN. |
```
In the same file, under Evidence/“Audit and response”, the orchestrator may extend “`…/evidence/response-01-*.json`” to “`…/evidence/response-01-*.json` and `response-02-*.json`”.

**C2. `proposed-record-changes.md`, line 20** (PD-T055 NEW block; the OLD anchor `## Open items` is unchanged, so literal matching is unaffected). In the NEW text, replace

```
Parent-repair and reference-basis rules, including the experiment named in Open items, lie outside that class (deferred, IDEA?drift-claude-17). (U) remains OPEN.
```
with
```
Parent-repair and reference-basis rules, including the experiment named in Open items, lie outside that class (deferred, IDEA?drift-claude-17). That experiment's literal wording is ambiguous: reorthogonalizing the parent against a basis of a computed span that contains it gives zero. IDEA?drift-claude-17 fixes two nonzero readings, neither yet run. R17a uses the stored columns strictly before the parent's graded index and stays in the computed span. R17b projects the parent onto an extended-precision nested reference basis of the exact span of the monomials through its index; that is the only step where information outside the stored columns enters. Both leave exact parents unchanged, so neither evades the fixed-degree lemma. (U) remains OPEN.
```
This is optional; it makes the PD-T055 note consistent with A02-L2.

**C3. `tracks/bivariate-lanczos/code/drift/README.md`.** Insert after line 82 (the end of “## E4 exact closure check (response-01)”), before “## E5 symbolic checks”:

````
## E4 relative-source limit regression (response-02)

```bash
PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python3 -B tracks/bivariate-lanczos/code/drift/e4_response02_check.py --output topics/padua-lanczos-drift-20261101/evidence/response-02-e4-creator-limit.json
```

`e4_response02_check.py` (response-02, audit-02 A02-M1) uses the standard library only (exact `fractions.Fraction`) and runs in about 2 seconds. It checks record 15's corrected limit (13), lim δ_A(t)/u = (κ_A/b)‖v_m‖ with κ_(A_m) ≥ b, on 25 exact instances. δ_A is computed directly from projectors at five source sizes, the closed form is asserted exactly, and the limit is extrapolated from the direct values. It reads `response-01-e4-closure.json` (hash recorded) for a κ²/b² cross-check. It neither imports nor modifies `e4_closure_check.py`, whose hash is pinned in response-01 evidence.
````

**C4. `response-02.md` (orchestrator), suggested disposition rows.**
- A02-M1: FIXED. Record 15 replaces the asserted equality “δ_(A_m)(t)/u→‖v_m‖” by (13), δ_A(t)/u=κ_A‖v_m‖/sqrt(b²+u²‖v_m‖²)→(κ_A/b)‖v_m‖≥‖v_m‖ for A=A_m, equality iff κ_(A_m)=b. The core (a)–(d), the T_3/v_21 instance (κ_Y=b, so the equality holds there), the qualitative no-o(u) result and the PROVED status are unchanged. The exact regression `e4_response02_check.py` → `response-02-e4-creator-limit.json` (25 instances; v_20 gives 88/15 against 22/5) is a developer check, not an independent rerun.
- A02-L2: FIXED as a definition only. IDEA?drift-claude-17 stays deferred and untested. It now defines R17a (an in-span control against the stored prefix q̂_0…q̂_(p−1)) and R17b (projection onto an extended-precision nested reference basis r_0…r_p of E_(≤p); |γ_p|≥1/2; the only entry point of outside information), and excludes the degenerate readings D0–D2. The kill test, resume conditions, predecessors and separation are coherent with these. Record 15's Open items records that both repairs act as the identity on its exact parents.

**C5. `LOG.md`.** At the orchestrator's discretion, add a log line that E34 response-02 produced the checker and evidence above (hashes in (b)).

## (d) For the Codex re-audit

1. **Changed claim (record 15, (13)).** Exact form and limit for **both** operators, not just A_m: δ_A(t)/u=κ_A‖v_m‖/sqrt(b²+u²‖v_m‖²). The proof derives it directly from (11)–(12). The status stays PROVED (analytic); the new checker is corroboration, not a computer proof.
2. **New exact remarks (record 15 Open items; IDEA-17 fixed-degree remarks).**
   - In the exact-prefix setting R17a and R17b return exact parents unchanged, so the rule stays in R.
   - P_(t+1)(v_m+f)=P_(V_m)(v_m+f)+(1+α)w, so product-level reference projection restores S_(t+1) exactly when 1+α≠0, and loses rank at 1+α=0.

   These are one-line proofs, labeled routine, with no status claim.
3. **IDEA-17 definition.** Check that R17a's nonzero condition is independence of q̂_0…q̂_p. Check R17b's leading-monomial argument: B_kE_(≤p)⊆E_(≤k), and the coefficient on monomial k is nonzero iff ⟨q̃_p,r_p⟩≠0, by admissibility triangularity. Check D2's recursive equivalence to reference columns, which needs the recursion down to the exact constant column. The “Effect on the span” paragraph is labeled heuristic and is not a claim. H17's thresholds are unchanged; the new inconclusive condition is min_p|γ_p|<1/2. R17a has a prediction, not a kill criterion.
4. **Measurement-reference choice.** R17b's reference R also serves as the drift reference once u_ext·κ(Φ) is recorded; for the rotated square the PD-N013(c) unrotated frame is added. A reviewer may prefer a fully independent measurement reference; this is a preregistration choice to settle before any run.
5. **Novelty gate for the IDEA-17 change.** The full `state/IDEAS.md`, PD-T055, PD-T043 and PD-N013 were reread. Searches for reference basis, parent repair, parent reorthogonalization and parent column across `tracks/` and `topics/` found only the already-cited records. The verdict is unchanged: a variant continuing PD-T055's open item, no novelty claim.
6. **Final hashes.**
   - Record 15: `e9aabc1119e1c2f55a2789e3d7a175edf8db3a96a6070df6819e4e85b5ae718d` (was 15a307e3…).
   - `ideas-e3-e4.md`: `66137b9562d250f4b6b6e607cb804689994725b63e0284afbcc60416999f53f8` (was 95613f22…).
   - `directions/E4.md`: `0337492c0138a6f1bf6ff955962eb7fc930819f4b0d5946f836e86d614eddf52`.
   - Checker: `6b2c0f87…`. Evidence: `a6faea99…`.
7. **Not done.** No IDEA-17 experiment was run. No edits were made to frozen files or to files I do not own. Historical `final-validation.json`/`protocol-check.json` pins of these files predate response-01 and are left as they are.
