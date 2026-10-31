# Audit 01 — Claude cross-agent audit of `codex/lattice-unisolvence-20261031`

- Auditor: Claude, independent auditor role (developer was Codex). Model `claude-opus-5-5` (Opus 5.5). AC requested xhigh; the session does not expose its runtime effort setting, so xhigh is the requested, not an observed, value. Reason for this depth: mathematical and adversarial audit of 13 PROVED statements, several negative (PD-N) results and finite computer-assisted screens — the xhigh row of `agents/claude/CLAUDE_ROLES.md`.
- Date: 2026-10-31/11-01 (UTC+1).
- Audited commit: `724269a318cc859b85a1be09db073607ba313bff` (topic head when this audit started; draft PR #4). Rules read at that head: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md`. They are byte-identical to `e949ef06895acd5463cdf8df7e0e5f795218f70f` (the developer's rules SHA) and to current `main` `07c5f54`.
- Hashes: `verify_artifacts.py topics/lattice-unisolvence-20261031/audit-targets.json` at the audited head: 168 entries checked, 0 failures.
- Subagents: none. Every reconstruction, script and rerun below was done by this auditor. Only this report, `claude-audit/` and one LOG entry are added; no developer file is edited.

## Reading coverage and novelty scope

Read in full: `state/IDEAS.md` (all 51 earlier entries, historical seed and contextual tables, prior-art corrections, the old obstruction table, the 12 lattice IDEA rows and the lattice obstruction/disposition table); all 21 lattice theory files under `tracks/lattice-unisolvence/theory/` and the track README; topic `REQUEST.md`, `plan.md`, `progress.md`, `report.md`, `AUDIT_HANDOFF.md`, `COLD_STORAGE.md`, the tail of `LOG.md`; `directions/C3/evidence.md`; `independent/report.md` (Astra) and `protocol/report.md`. Code read: `c3_rank.py`, `c3_lebesgue.py`, `prepare_evidence.py`, `verify_artifacts.py`; the other checkers were exercised by rerun and by independent reimplementation rather than line-by-line review.

The campaign makes no publication-novelty claim, so I did not re-run the literature search. I checked that every theory file states "no novelty claim", that predecessors (lower sets, De Marchi–Usevich/Camargo axis separation, Dencker–Erb, Bos–De Marchi–Vianello, Li–Sun–Xu) are cited as LITERATURE without importing proofs, and that the interpolation/cubature distinction from AC's request is kept. I did not open primary sources; attribution coverage rests on the developer and Astra records.

## Independent reconstruction of each claim

### PROVED statements (13)

| ID | My check | Result |
|---|---|---|
| PD-T?lattice-c0-codex-01 density | Proof read line by line: surjectivity of the character from primitivity, equal fibres, full-block/boundary split, limit. Consequences for d=2,3, k≤6 rechecked. | Correct |
| PD-T?lattice-c0-codex-02 mod-6 table | Recurrence `h_{L+6}=h_L+u` ⇒ uniform increment; base vectors F_0,F_1,F_2; the n≡3,4,5 uniform rows. Brute-force counts for n=0..39 (`indep_c0_c3.py` predecessor check). | Correct; table exact |
| PD-N?lattice-c0-codex-01 short axis | One-line annihilator. | Correct |
| PD-T?lattice-c1-codex-02 mod-4 counts | Increment 2n+7 per entry, 4n+14 per adjacent pair = N_{n+4}−N_n; base counts; complement phases; block relabelling at n≡2. Brute force n=0..40, all four phases. | Correct |
| PD-T?lattice-c1-codex-03 row moments | Column count (n+1)²−N = n(n+1)/2; leading-coefficient lemma (inductive sufficiency, necessity); bijection kernel(B) ↔ kernel(evaluation); n=2 reduction. | Correct over every field |
| PD-T?lattice-c1-codex-04 Gram reduction | g_p sign rule; G=(I+H)/2; central-inversion sign flip in both cases (2n+1≡3 resp. 1 mod 4) kills same-parity blocks; eigenvalues (1±σ)/2; Schur determinant; cardinal-function identity and weighted Cauchy–Schwarz; ΣW_s = G_00 = 1/2; the closed form of S_M. Own numerical implementation n=1..48 (`indep_gram.py`): same-parity blocks ≤3.3e-15, explicit moment formula ≤6.0e-15, determinant identity ≤1.1e-11 in log, Lebesgue bound never violated. | Correct |
| PD-T?lattice-c1-codex-01 quadratic | Exact polynomial identity `det V = −ΔX·Π(v_r−u_r)·R` over ℤ (SymPy); kernel argument; R expansion for phase 0; shifted-phase pair lists. | Correct, sign included |
| PD-N?lattice-c1-codex-01 not an axis product | n=2 value matrix [[0,16],[−180,0]] recomputed exactly; n=3: four 10×10 determinants recomputed **over ℤ**, residues [[469,520],[14,277]] mod 1009, integer cross product nonzero. | Correct |
| PD-N?lattice-c1-codex-02 Chebyshev subsequence | Residue map r↦1−r mod 4 preserves phases 0/2 at n≡2; no fixed node; even-subspace dimension (m+1)²; kernel ≥ (n+2)/4; explicit n=2 kernel polynomial vanishes on all six nodes (exact). Numerical nullity at n=2,6,10 equals the bound (MEASURED side observation). | Correct |
| PD-T?lattice-c3-codex-01 generic witness | Block degrees Σa = C(n+3,4); lifting from one nonzero modular witness; without-replacement Schwartz–Zippel induction (marginal of a sequential without-replacement draw is again of that type; conditional set size ≥ p−max L+1). | Correct |
| PD-T?lattice-c3-codex-02 annihilator certificates | (A) product annihilator; (B) bivariate rank-nullity kernel times removed-layer product. | Correct |
| PD-N?lattice-c3-codex-02 n1 mixed axis | Exact identity `D=(x1−x0)[(y2−y0)(z1−z0)−(z2−z0)(y1−y0)]` over ℤ; predicate and rectangle contradictions; Lobatto singularity at Y=Z=(1,0,−1). | Correct |
| PD-T?lattice-c3-codex-04 n2 axis factorization | Full 12-variable identity `det = −F_X F_Y F_Z` verified exactly in ℤ[x,y,z] by my own fraction-free Bareiss elimination (4608 terms), independent of the developer's normalized CAS run; scale exponent 5 = C(5,4); monotone-real corollary. | Correct, signs and exponents included |

Status classification: each PROVED file has a single substantive statement; the conditional Lebesgue bound inside c1-gram-reduction is a proved implication (not CONDITIONAL). OPEN targets c1-open-family and c3-open-target are correctly not PARTIAL. PD-N files carry the status of their negative statement. I agree with all 21 labels as written.

### Finite computations (independent implementations, not reruns of the developer code)

- **C0 catalogue** (`indep_c0_c3.py`): my own orbit closure (unit scaling, axis reversal with the residue shift, equal-length swaps) and histogram convolution give 77616 raw tuples → 5061 canonical → 39 (d=2) + 412 (d=3) survivors, per-degree totals 23,8,4,1,2,1 and 119,68,78,45,56,46. Every orbit member was checked to have the same count.
- **C3 ranks**: from my own catalogue, 364 reversal representatives; exact ranks at **different primes** 10007, 10009, 32003 and different random axes: 142 full rank / 222 deficient, per degree 50/27, 19/43, 32/46, 18/27, 16/40, 7/39 — identical classification.
- **Certificates** (`certs_AB.py`): exhaustive own search finds exactly 127 cover (A) and 86 further projection (B) certificates; the residue is exactly the developer's nine IDs; no certificate fires on any full-rank representative.
- **Rectangles** (`rect_check.py`): all 426 stored rectangle determinants recomputed from the stored axes with my own elimination (convention: third axis from list A); all match; 114 representatives have a nonzero cross residue (23,18,32,18,16,7 by degree).

## Commands I executed

Environment: Python 3.12.3 (developer 3.12.14), NumPy 2.3.5, SciPy 1.17.0, SymPy 1.14.0, Linux container.

1. Every command in `AUDIT_HANDOFF.md` into a fresh `/tmp/lattice-claude` (`claude-audit/reruns/run.sh`): all exit 0, `git diff --check` clean, `verify_artifacts.py` 168/0. Payload comparison ignoring argv/timing/environment keys (`compare_payloads.py`, output `compare-1thread.txt`): 12 of 13 outputs identical; `lebesgue.json` differs only in the embedded `numpy_config` text; `stability.json` differs (see F3). Rerunning `c1_stability.py` with 2 BLAS threads, as `C1/rounds.md` records for the producer run, reproduces it exactly (`compare-stability-2thread.txt`).
2. From the repository root: `python topics/lattice-unisolvence-20261031/claude-audit/<script>.py` for `indep_c0_c3`, `indep_symbolic`, `indep_gram`, `rect_check`, `nine`, `cert_D`, `cert_D_construct`, `certs_AB`; stdout and small JSON in `claude-audit/outputs/`. Run times 0–295 s.

## Findings

**F1 — Integration (blocks PR stage).** `main` advanced to `07c5f54` (MZ PR #3 merged) after the handoff. `git merge-tree HEAD origin/main` reports content conflicts in nine shared files: `ID_CROSSWALK.md`, `PAPER_MAP.md`, `PROOF_STATUS.md`, `literature/INDEX.md`, `state/CURRENT.md`, `state/IDEAS.md`, `topics/README.md`, `topics/padua-batch-20261031/ALLOCATIONS.md`, `tracks/README.md`. Required: merge `origin/main` (no rebase), reconcile the ledger and final ID allocation with the MZ final ranges now on main, refresh `audit-targets.json`, `provenance.json` and the PR's base statements. No mathematics is affected; a focused registry check is enough afterwards.

**F2 — The nine "unexplained" deficiencies have a universal certificate (scientific; recommended adoption).** All nine residual representatives fail generically by an elementary mechanism that neither (A) nor (B) captures.

*Proposition (auditor; candidate for a developer PD-T).* Let K be any field, n≥1, I a subset of a three-axis index box with within-axis-distinct labels. Fix an axis r and let s,t be the others. For each r-layer v meeting I let P_v be its projected (s,t) index set. Group these layers into classes C of equal P_v, with common set P_C, and put E = Σ_C (|P_C| + |C| − 1). If E < n + C(n+2,2), then S_I is not unisolvent for Π_n(K).

*Proof.* Let U = {g(x_r)+Q(x_s,x_t)}, g in the span of x_r,…,x_r^n and Q ∈ Π_n in (x_s,x_t). The monomial supports are disjoint, so dim U = n + C(n+2,2) and U ⊂ Π_n. A function f = g+Q vanishes on S_I iff g(H_{r,v}) + Q(H_{s,a},H_{t,b}) = 0 for every v and (a,b)∈P_v. Pick a representative v_C in each class. Given the |P_C| equations of v_C, those of another v∈C are equivalent to the single equation g(H_{r,v}) = g(H_{r,v_C}) (subtract, using P_v = P_C ≠ ∅). So vanishing on S_I is E linear conditions on U, and E < dim U yields a nonzero annihilator in Π_n. ∎

Evidence: the certificate fires on all nine (two n=2 cases with E=7<8, classes {0,2} on x; seven n=3 cases with E=12<13, classes {0,2},{1,3} on x or y). It fires on 160 of the 222 deficient representatives in total and on **none** of the 142 full-rank ones (`cert_D.py`). For each of the nine I built f exactly over ℚ from the reduced E-equation system alone and checked that it is nonzero and vanishes on every node (`cert_D_construct.py`). At p = 1000003 each of the nine has rank deficit exactly 1 (MEASURED, `nine.py`). With the developer's 213 this gives a written universal certificate for **all 222** finite-catalogue deficiencies. Consequences to record in response: `c3-deficiency-observations.md`, `c3-open-target.md`, `report.md` and IDEA?lattice-c3-codex-05 currently say the nine "remain OPEN"; `c3-annihilator-certificates.md` (or a new split PD-T) would gain part (C). No novelty claim: this is the standard additive-separation/repeated-fibre trick. The developer may re-derive it and have it independently checked rather than accept my proof.

**F3 — Minor, reproducibility.** `AUDIT_HANDOFF.md` gives `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1` for `c1_stability.py`, but the committed `C1/stability.json` was produced with 2 threads (`C1/rounds.md`, embedded metadata). With 1 thread, two Padua/Leja control rows at n=22 change sample count (6816 vs 6807) and a symmetric tied maximizer; sampled maxima agree to 1e-9. Correct the handoff command (Astra recorded the same effect). No claim changes.

**F4 — Minor, stale status text.** 17 of the 21 theory files still say "independent (Astra) reconstruction pending" or "rerun pending" (e.g. c0-density, c1-gram-reduction, c3-n2-axis-factorization, c3-rectangle-observations "pending at drafting"). The track README, IDEAS and every file say "Claude audit PENDING". The Astra report resolves the first only by an external note. At disposition, add a dated History line in each file pointing to `independent/report.md` and this audit; do not rewrite the original wording.

**F5 — Minor, archival.** Verified on AC's machine (through the linked device, read-only listing) that `Downloads\padua\cold_storage\` contains no `lattice-unisolvence-20261031` folder: the receipt is genuinely missing. The developer's staged ZIP (`7b173b14…`) lived in its own workspace and is not reachable from this session. See the delivery note at the end for what this audit delivered; `COLD_STORAGE.md` should record whichever copy AC accepts as the archive.

**F6 — Observation, upgrade eligibility (not a defect).** The following finite claims now meet the workflow's computer-proof criteria: a proved finite reduction, exact arithmetic, committed checker/evidence, and two separate independent executions (Astra's and this audit's own implementations):
- (i) C0 catalogue completeness within its frozen scope (reduction written in c0-catalogue);
- (ii) generic unisolvence over ℚ, via PD-T?lattice-c3-codex-01(2), of each of the 142 survivors;
- (iii) universal singularity of each of the 213 (A)/(B)-certified representatives;
- (iv) failure of an axis-only rational product for each of the 114 rectangle witnesses.

Keeping them MEASURED is permitted and conservative. If upgraded, split per the rules: a PROVED finite record, with the sampled-rank observations remaining MEASURED.

**F7 — Minor, registry readability.** All 12 lattice IDEA rows in `state/IDEAS.md` carry the identical text "Complete family fields and per-parameter overrides in linked record; IDEA-012/013/029 …; exact kill tests retained". A heading/summary scan under the novelty gate therefore cannot distinguish the entries. Give each row its own one-line closest predecessor and kill test, for example: C1-03 "antipodal cross-block; kill: ‖A_n‖=1 at some n"; C3-04 "isolated n=2 fibre; kill: naive continuation rank-deficient".

No finding concerns the correctness of any PROVED statement, any status label, or the scope of any negative claim. I checked specifically that: the n≡2 mod 4 Chebyshev obstruction is not extended to shifted phases; C3's finite Lebesgue screen is not called an asymptotic negative; and "142 survivors" is not presented as all-axis unisolvence.

## MEASURED side observations (not registered)

- The cross-block gap 1−‖A_n‖ from `indep_gram.py`, n=1..48: odd n (phase 0) decreases from 0.134 (n=1) to 0.0278 (n=47); even n (phase 1) from 0.192 (n=2) to 0.0389 (n=48). This agrees with the developer's 0.0250 (n=63) and 0.0345 (n=64). The slow decay is consistent with either a gap ≍ 1/log n or a positive limit; no fit is offered.
- Sampled Lebesgue values for the parity-adapted family at 4000 random points (n≤48) stay below 50, under the developer's adaptive maxima. These are lower estimates only.
- For the unshifted phase 0 at n=2,6,10 the numerical nullity equals (n+2)/4 exactly, suggesting the PD-N lower bound is sharp.

## Verdict and stage

Mathematics **ACCEPTED** at the stated scopes: all 13 PROVED statements, the 6 MEASURED records and the 2 OPEN targets with their labels, and the negative-result scopes. Developer-code reruns reproduce the committed evidence (F3 aside), and my separate implementations reproduce every consequential count, rank class, certificate set and rectangle witness.

F1 blocks PR readiness, and F2–F7 need responses. Stage → **WORK** for Codex `response-01.md`. F3, F4, F5 and F7 can be resolved without changing any claim. If F2 is adopted as a new or extended PD-T, that is a material mathematical change and returns to AUDIT for a focused check of that record only. After F1, a focused registry/ledger check suffices.

## Residual uncertainty

- Runtime effort is not observable. My reimplementations share the problem definitions with the developer, so a misreading of AC's original definitions would be shared. I checked the definitions against REQUEST.md rather than the code.
- I did not read primary literature. Attribution and "no exact match found" rest on the developer/Astra coverage statements, which are explicitly non-exhaustive.
- The Gram-reduction numerics are floating corroboration of a proof I checked by hand; they are not a certificate.

## Delivery note

This report, `claude-audit/` (8 scripts, `bareiss.py`, outputs, rerun records) and a LOG entry are committed to the topic branch under AC's name with Claude trailers. PR #4's AUDIT section is updated, and it stays draft.

Copied to AC's machine under `Downloads\padua\cold_storage\lattice-unisolvence-20261031\claude-audit-01\`: this report, `claude-audit/`, `SHA256SUMS.txt`, and `lattice-evidence-retrieval-copy-724269a.zip`. The ZIP holds 169 entries: the 168 files pinned by the committed `audit-targets.json`, each hash-checked before zipping and again after extraction, plus that manifest. It is 841824 bytes, SHA-256 `8e75432bea5070776bb025030442adc05ba44f5efd8884ba5408fb546eca8330`. It is **not** the developer's original staged ZIP (`7b173b14…`, 160 files at `61dcbe5`). It is offered for F5 as a verified retrievable copy at the audited head; AC or the developer decides whether it serves as the archive receipt.
