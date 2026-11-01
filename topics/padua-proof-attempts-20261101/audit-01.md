# Claude audit-01 — padua proof attempts (A1, B5, A5-partial, optional B1)

- Decision: **ACCEPTED for the stated scope. All three PROVED claims are accepted as stated; the B1 note's OPEN status is accepted. No status change is required.** Five minor record/wording findings (F1–F5) and one protocol note (F6) need dispositions in `response-01.md`. They change no claim, proof or checker. The topic may proceed to PR after a documented response, without re-audit, unless that response materially changes a claim, proof, code or evidence.
- Audited candidate: `a09d910ae7d5526b1e216066421a0bee7fc20da4` (branch head; scientific head `8fb28d7f2a13aaeb71814a8a7c4c89a87c095bad`; the final commit changes LOG only). Topic base `cadb35066160e466cb1704b9791ad6f374446422`.
- Rules read at the candidate head: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md` (unchanged from base).
- Upstream refresh on 2026-11-01: `main` = `9739a0c56b7a3976422ce60a8441bfbbfd6554df` (unchanged); `claude/programme-ideas-20261031` = `f4e213390f66a8c9f0c6bd65131b97b78db873c8`, which has moved past the `0ef90ed…` that the developer checked against.
- Auditor: Claude, independent of the Codex developer and of both Codex supplementary agents. Configured model `claude-opus-5-5`, effort xhigh, as requested in the LOG prompt. Reason: a mathematical audit of new all-degree proofs and an interval certificate (Opus 5.5 high/xhigh row). The runtime does not expose a separate receipt of the serving model.
- Role: independent auditor. I did not write any developer file. My Git action is a single local commit adding this record and `audit-support/claude-audit-01/` (no push access in this session; delivered as patch/bundle, see README in cold storage).

## Scope and read coverage

Read in full: LOG, plan, inputs-review, all four attempt notes, all three theory records, `proposed-record-changes.md`, `independent-checks.md`, `independent-checks-a5.md`, `code/a5_exact_certificate.py`, `code/a5_trace.py`. Also read in full: source `OPEN_TARGETS.md`, source THEORY -01 (finite Favard), the frozen `t3_certify.py` (complete) and `t3_degenerate.py` (complete), `m2_common.py`. Read in part: `t3_certify.log` (degenerate notes), `t3_maxima.json` (n=3 edge entries), and the registry rows in `state/IDEAS.md`, `PROOF_STATUS.md` and `ID_CROSSWALK.md` that reference the affected records.

Novelty scope: the topic proposes no new IDEA, makes no novelty or priority claim and creates no PD-N. Its only negative content is the B1 note's failed proof route, which is unregistered and has OPEN status. I therefore did not read the full `state/IDEAS.md`. I checked the gate's cited entries (IDEA-047, IDEA-048, IDEA-069/PD-N005; programme rows 472, 481, 493) and searched mechanism terms (`corner`, `commutant`, `degenerate`, `rhombus`). The inputs-review characterisations match those entries.

Literature: I fetched the CDMV 2008 author preprint (`PDcomp.pdf`) and read its text extraction. Eq. (1) gives weights 1/(2n(n+1)), 1/(n(n+1)), 2/(n(n+1)) (p.3). Eq. (3) is the normalised product-Chebyshev kernel (p.3). The third family is defined by eqs. (6a)/(6b) as A3 ∪ B3 = {(z^n_{2i}, z^{n+1}_{2j})} ∪ {(z^n_{2i+1}, z^{n+1}_{2j+1})} (p.4). Eq. (6c) gives the interpolant with the T_n(x₁)T_n(ξ₁) correction. This confirms the developer's locators and the "third family, not first" relabelling. I did not check Bos et al. 2006 Theorem 2. None of the three proofs depends on either source.

## Mathematical verification

### A1 — PD-T?proof-attempts-codex-01 (PROVED, accepted)

I reconstructed each step independently.
- Discrete Gram: Q_M(cos rt) vanishes for 1 ≤ r ≤ 2M−1. The checkerboard inner product splits into the tensor quadrature plus an alternating term, and the alternating term needs a+c = n and b+d = n+1, which is impossible at total degree ≤ 2n. H is diagonal with entries h_a^(n)h_b^(n+1). The only exceptional coefficient is at (n,0), and it gives the −T_n(z₁)T_n(B₁) correction. This holds for n = 1 as well.
- V H⁻¹Vᵀ = W⁻¹ because V is square, and that gives the cardinal formula.
- The rhombus map (p,q) ↦ (p+q, q−p) is a bijection onto pairs of equal parity with max(|r|,|s|) ≤ n, and pu+qv = rS+sT. The two parity grids give U_{n+1}U_{n+1} + U_nU_n. At t = ℓπ the continuous value is m(−1)^{(m−1)ℓ}.
- At a corner, sin(aθ_c) = 0, so the cosine products collapse.

No gap found.

### B5 — PD-T?proof-attempts-codex-02 (PROVED, accepted)

- The structural mask matches `m2_common.pattern` exactly. P_x ⊆ P_y because π_y = π_x + 1 within a degree.
- I, H_x and H_y lie in 𝒞_y and are independent through the column-zero pivots.
- Distinct x makes the Krylov matrix Qᵀdiag(√w)[x_k^r] invertible, so e₀ is cyclic and E ↦ Ee₀ is injective on the commutant of H_x. Column 0 of P_y allows only rows 0, 1, 2, so dim ≤ 3. The argument uses neither symmetry nor the pattern outside column 0.
- Genericity: Δ = ∏(x_i − x_j)² is a nonzero polynomial, so its zero set has empty interior. The complement is dense and open in every component of the open domain, and the moment-curve witness shows the complement is nonempty in every degree. Rolle/Descartes gives unisolvence of the witness.
- The target asks only for *some* proper real-analytic exceptional set, so a sufficient superset is enough. The record states correctly that it does not classify repeated-x strata.

No gap found.

### A5-partial — PD-T?proof-attempts-codex-03 (PROVED, accepted)

- L₆ = (x−1)(2x²+x+2y²−2)/3 checks directly against all ten node values. Its value and angle gradient vanish at z_σ = (0, acos(σ/√3)).
- The two background sign vectors and the identity g₋(x,y) = g₊(x,−y) reproduce. ∂_y g₊(1, 1/√3) = 0, and λ₃(z_σ) = 1 + 8√3/27 + 4√6/9 ≈ 2.6018623, which equals the stored value in `t3_maxima.json`.
- Interval reduction: cos θ ≥ 1 − θ²/2 and cosine is 1-Lipschitz, so D_σ maps into X × Y. H_tt = (1−x²)f_xx − x f_x and H_pp likewise, with |H_tp| ≤ ρ sup|f_xy|. The Fraction interval class is inclusion-preserving: products take all four endpoint products, and even powers include 0 across zero. The alternating cosine bounds C₄₁ < cos t < C₄₀ hold for 0 < t < 3. Gershgorin bounds both the eigenvalues and the norm.
- On D_σ we have L₆ ≤ 0 and every other cardinal has a fixed sign. So λ₃ = g − L₆ is smooth there, H ≼ −(7/2)I, and z_σ is the unique critical point and strict maximum.
- The frozen `degenerate_max` claims a strict local maximum and no other local maximum in the **1-norm** disc of radius ρ₀ = 0.002 about z_s (docstring, lines 187–207). The l1 disc of radius 0.0021 contains each such disc, because seed error plus ρ₀ < 0.0021 is checked exactly. So the frozen local claim is rigorously true at both decisions.

No gap found in the local theorem.

## Independent execution (actual runs, this session)

Environment: Linux container, Python 3.13.18, SymPy 1.14.0, NumPy 2.3.5, SciPy 1.17.0, mpmath 1.3.0. The repository was cloned at `a09d910`.

**Reruns of the developer checkers.** Each was run separately with the stated command, output to the auditor scratch area.

| Command | Result |
|---|---|
| `python topics/padua-proof-attempts-20261101/code/a1_exact_check.py` | byte-identical to `outputs/a1_exact_check.json` except the `python` version field; all `all_equalities_exact: true` |
| `python …/code/b5_exact_instances.py` | identical except `python` field |
| `python …/code/a5_exact_certificate.py` | identical except `python` field; trace coverage matched |
| `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python …/code/a5_trace.py` | equal to `outputs/a5_trace.json` after removing `python` and `elapsed_seconds`. n=3: 2 calls, both accepted, Z=[6], seeds bit-identical, ρ₀ = 0.002. n=4…8: 0 calls. Candidate counts 15/27/25/41/50/62 reproduce |
| `python …/code/evidence_manifest.py` | reproduces `evidence-manifest.json` except `python` field |

The original-run log agrees: `t3_certify.log` lines 3–6 (n=3: "degenerate maxima 2", notes at (0, .9553166) and (0, 2.186276), Z=[6], μ₀ = 3.5733616, which equals 47/18 + 5√3/9). Its n=4…8 summary lines report "degenerate maxima 0".

**Auditor-written checkers** (`audit-support/claude-audit-01/`). These use deliberately different routes from the developer's.

| Script | Route | Result |
|---|---|---|
| `aud_a1.py` | monomial-basis Vandermonde solved in mpmath at 80 digits (no kernel or Chebyshev basis); U_m by explicit geometric sums (no quotient) | n = 1…10, every node and every corner: cardinal-level difference ≤ 1.4e−79. MEASURED |
| `aud_b5.py` | exact QQ nullity of the **full** linear system [A_x,F] = 0, DF = FᵀD on the full P_y mask (monic LDL pair) | moment-curve witness n = 2…5: dim 3. Seeded random rational distinct-x n = 2…4: dim 3. Padua n = 2 control: dim 6 (reproduces PD-N04). A repeated-x n = 3 instance: dim 3 (distinct x is sufficient, not necessary) |
| `aud_a5.py` | cardinals in the Chebyshev-product basis; mpmath `iv` interval arithmetic **directly in angle variables** on the l∞ box of half-width 0.0022 (a superset of the l1 disc 0.0021), 12×12 sub-boxes | both σ: exact zero gradients of λ₃ and L₆ at the centres; signed cardinals ≥ 0.0059; bracket ≥ 1.66; −λ_max(H_λ) ≥ 3.5696 by Gershgorin, det H > 34.27. Same sign vectors and exact value as the developer |

`aud_a5.py` gives an independent rigorous certificate of the A5 local theorem, on a larger domain and with a different interval engine. Its trusted dependency is the mpmath `iv` rounding implementation.

## Findings

All are **Minor**. None affects a proof or status.

### F1 — B5 finite evidence is described more strongly than it checks

Locations: `theory/proof-attempts-codex-02-generic-commutant.md` ("Checks" table, column "Commutant dimension"), `attempts/T-B5.md`, and the B5 OPEN_TARGETS proposal in `proposed-record-changes.md` ("Exact rational LDL witnesses … support the written reduction").

The "computed reduced rank" is the rank of the last N−3 rows of V⁻¹. That always equals N−3 for any invertible V, so it cannot fail, and it does not check the commutant dimension independently of the proof. The script still checks nontrivial things: unisolvence, LDL positivity, pattern, commutation and pivots. `independent-checks.md` discloses the rank point correctly.

**Required:** label the dimension column "3 (by the proof)". Reword the proposal to say the witnesses check unisolvence, positivity, pattern and commutation, and that the dimension follows from the all-n proof. Optional: cite or adopt a direct nullity check such as `aud_b5.py`.

### F2 — the corner and edge-node degenerate handlers fall out of the remaining-work list

Locations: proposed `-06` Runs-needed replacement and the OPEN_TARGETS A5-partial annotation in `proposed-record-changes.md`.

`t3_degenerate.py` makes its own degenerate-point decisions. The (D) corner certificates add the corner maxima, and the (E) edge-node discs discard regions. Both use floating Taylor data, floating mesh constants M_B and floating sign sets. The proposed `-06` text deletes "valid identities (not tolerance tests) at the degenerate points" and says these handlers "are not covered", but it does not list them as a remaining certification item.

**Required:** add an explicit Runs-needed item: "rigorous versions of the (D) corner and (E) edge-node certificates in `t3_degenerate.py`". Also state in the A5 annotation that obligation (2) is discharged for the `degenerate_max` path only.

### F3 — a MEASURED execution fact sits inside the Statement of a PROVED record

Location: `theory/proof-attempts-codex-03-degenerate-maxima.md`, the Statement paragraph beginning "The reconstructed n=3,…,8 execution…".

The record labels this fact MEASURED, and the "Status by part" table separates it correctly. Keeping it inside the Statement still blurs the PROVED statement.

**Required:** move that paragraph into "Checks/Evidence". Keep the Statement to the two exact representatives and their discs. The proposed `-06` line remains its registered home.

### F4 — proposed OPEN_TARGETS edits replace text instead of appending

Location: the three OPEN_TARGETS blocks in `proposed-record-changes.md`.

Each replaces a whole "Known / Done when / Route" paragraph with a status update. That drops the current route text from the file, including response-02's revised B5 route (ii) (polynomial-minor approach) and the A1 route.

**Required:** append a "Status update after audit" line under each target and keep the existing paragraphs, or move them under a dated history note. The Statement lines are already preserved.

### F5 — shared-registry rows for PR preparation are not listed

AC deferred registry edits, and that deferral is correctly respected. But applying the proposals alone would leave these rows stale or missing:
- `state/IDEAS.md:493` (PD-N04 row says "genericity of dimension 3 OPEN") and `:481` (IDEA-17 row);
- `PROOF_STATUS.md:94, 96, 100`, plus new rows for the three PD-T;
- `ID_CROSSWALK.md:311, 313, 317`, plus the original-to-split mapping −04 → codex-01 that the workflow requires.

**Required:** add a "PR-preparation registry checklist" to `proposed-record-changes.md` naming these rows.

### F6 — protocol notes (no change to claims)

- I re-checked the twelve literal old blocks against the moved upstream head `f4e2133…`. Each occurs exactly once there, as at `0ef90ed…`. Record this in the response, or re-check at application time.
- LOG "Runs needed" says AC's computer is unreachable. In this audit session it is reachable, but `results/padua-proof-attempts-20261101.md` is still unwritten. Under the local-results rule only this topic's orchestrator writes it, so the auditor did not write it. The orchestrator should write it at its next step, or AC can delegate it.
- Commits are authored as Andrey Chesnokov with Agent/Model trailers. The diff is add-only, with 27 paths, all under this topic. Generated outputs total 36,856 bytes, within limits. `git diff --check` is clean.

## Remaining uncertainty

- Trusted dependencies: SymPy exact algebra and Python `Fraction` (developer); mpmath `iv` (auditor). The A5 interval certificate has now been confirmed by two independent engines.
- The trace's "every call" coverage is a deterministic floating re-execution of the frozen code. It matches the original log, but it remains MEASURED execution evidence, as the record says.
- I did not check Bos et al. 2006 Theorem 2.
- Nothing in this audit certifies the A5 counts, the corner argmax (A4) or the corner asymptotics (A2/A3), and nothing upgrades B1.

## Next

The developer writes `response-01.md` with dispositions for F1–F6, then proceeds to PR. Re-audit is needed only if a proof, claim, checker or evidence changes materially. AC alone merges.
