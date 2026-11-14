# MZ-SP correspondence table (task 1; gate W1)

> **Status of this file (2026-11-14, response to audit-01 F5).** The table immediately below is the **historical planning table** of 2026-11-13. It uses post-split numbering and planned locations, and its "now → target" column shows the state at that time. It is kept unchanged as a record. The **current mapping** is the *Frozen numbering* table at the end of this file (label → number) together with the scope table in [tracks/mz-constants/paper-sp/README.md](../../tracks/mz-constants/paper-sp/README.md) (frozen number → PD IDs → status → exact scope, verbatim/weakened). Every departure from a record's scope is listed in the *Changes log* below and in response-internal-sp.md.
>
> **Final IDs (PR preparation, 2026-11-14).** PD-T?mz-paper-claude-01 = **PD-T684** and PD-T?mz-paper-claude-02 = **PD-T685** ([ledger](ALLOCATIONS.md)). The historical tables below keep the provisional IDs.

As [correspondence-cc.md](correspondence-cc.md), for MZ-SP. Planned numbering from [plan-sp.md](plan-sp.md).

| Current label (post-split no.) | Planned | ID | Record status | Exact scope of the record | In paper (now → target) |
|---|---|---|---|---|---|
| lem:weight-comparison (1.1) | §2 recap | MZ-CC Lemma (part of PD-T017) | PROVED in MZ-CC | | recap, cited → recap, cited |
| prop:counterexample (1.2) | §2 recap | PD-T014/022, PD-T017/018, PD-T019 | PROVED in MZ-CC | λ_+<2; λ_−(N,N−1)→0; λ_−(512,511)<1/4 | recap, cited → recap, cited (label renamed in task 3) |
| thm:padua (2.1) | Thm 3.1 | PD-T021 | PROVED | marginal 2w_j; compression and domination for any degree-N exact real rule; liminf ≥ 1; N=512 consequence | verbatim → verbatim |
| Lemma 2.2 (density) | Lemma 2.3 | PD-T101, PD-T111 | PROVED | integrated cardinal density d_m | verbatim → verbatim |
| thm:padua-weights (2.3) | Thm 4.1 | PD-T295 | PROVED | even m fixed-index limit; whole-grid majorant 4096 | verbatim → verbatim |
| prop:padua-odd-weights (2.4) | Prop 4.2 | PD-T377 | PROVED | odd m; 8192 | verbatim → verbatim |
| thm:padua-carriers (2.5) | Thm 5.1 | PD-N105, PD-N106 | PROVED | even m carriers, limits −16ab/9, 8ab/9 | verbatim → verbatim |
| prop:padua-odd-carriers (2.6) | Prop 5.2 | PD-T378 | PROVED | odd m carriers | verbatim → verbatim |
| cor:padua-ratio (2.7) | Cor 5.3 | PD-N107, PD-T378 | PROVED | sharp threshold over all integers | verbatim → verbatim |
| prop:padua-growth (2.8) | Prop 5.4 | PD-T379 | PROVED | one-sided normalized bounds, all integers | verbatim → verbatim |
| — | Prop 5.5 | PD-T533 | PROVED | strict improvement c_new, both parities, one-sided | absent → **to add**, verbatim |
| — | Prop 5.6 | PD-T537 | PROVED | family ceiling U_− < 1/24 for a+b<1/2; not optimal | absent → **to add**, verbatim |
| thm:padua-operator (2.9) | Thm 7.1 | PD-T297 | PROVED | 2 ≤ ‖H_{m,n}‖ ≤ 28.376… for m≥2, 0≤n<m | verbatim → verbatim |
| — | Thm 6.1 | PD-T534 | PROVED | |Q_m−log(R)L_m| ≤ 4096; ‖L_m‖ ≤ 120; spectral errors | absent → **to add**, verbatim |
| — | Lemma 6.2 | PD-T535 | PROVED | Legendre/Bessel corner kernel limit with error C/m | absent → **to add**, verbatim |
| — | Thm 6.3 | PD-T536 | PROVED | B compact, ‖B−B_K‖ ≤ 120/K; λ_±/log m → c_±, all integers; finite comparison (4) | absent → **to add**, verbatim |
| — | Prop 6.4 | PD-T539 | PROVED | elliptic kernel of B | absent → **to add**, verbatim |
| — | Prop 6.5 | PD-T540 | PROVED | A² positivity improving; c_−=−‖B‖ simple; 0<c_+<‖B‖ | absent → **to add**, verbatim |
| — | Prop 6.6 | PD-T541, PD-T542 | PROVED (PD-T542 computer-assisted) | rectangle reduction; 0.013164… ≤ ‖B‖ ≤ 0.477809…; no useful digits | absent → **to add**, verbatim with the caveat |
| (text, §3) | §8 | PD-T298, PD-T299 | PROVED (computer-assisted) | strict rational brackets at m=60, 80 | verbatim → verbatim |
| prop:padua-finite-negative (3.1) | Prop 8.1 | PD-T376 | PROVED (computer-assisted) | trial-Rayleigh intervals at m=1101, 1240, 1600; no first crossing | verbatim → verbatim |
| Table 2 | §8 | PD-T026 | MEASURED | m=10…40 | measured → measured |
| (comment) | §8 | PD-T380 | MEASURED | 23 rows, fits | companion pointer → optional, MEASURED |
| — | §8 | PD-T538, PD-T543 | MEASURED | 16 minimum rows, slopes ≈ −0.092, mode-2 diagnostic | absent → optional, MEASURED; "finite-window slopes are not the limits" |
| (text) | §9 | PD-T381 | PARTIAL | existence/agreement/characterization PROVED (PD-T534/535/536); **decimal values OPEN** | OPEN part only as open problem |
| (text) | Remark 5.x | PD-T028, PD-T110, PD-T116 | OPEN with binding REJECTED: refuted | | "refuted" (by PD-N105–107, PD-T377/378) → same |

Counts at this checkpoint: 11 numbered statements in the post-split text (incl. the unlabeled density lemma) plus the m60/80 text result, all mapped; 8 planned additions; no omissions.

## Changes log

- 2026-11-13 (handoff 04, MZ-SP part 1; Sonnet 5.5 high worker, verified by the orchestrator's rebuild, 30 pp. clean):
  - CC recap: `lem:weight-comparison` is now a lemma proved in MZ-SP (formula, endpoint weights, bracket error, π−4/3 interior bound, floor (1+d_j)/N²; the unused 5 sinθ/N bound is dropped). `prop:counterexample` is renamed `prop:cc-inputs` and cites MZ-CC (AC: MZ-CC first). Two sentences of the PD-T297 proof are repointed (π−4/3 bound; λ₊<2 via prop:cc-inputs, giving the tensor bound 4).
  - Carriers:
    - `lem:fejer-cosine` (auxiliary, inside the PD-T379 proof; gives J₋(a) in closed form);
    - `prop:padua-growth` extended with the fixed-(a,b) bounds (6), which are already proved inside the PD-T379 proof (verbatim from the record's proof, now stated);
    - new `prop:carrier-improvement` (PD-T533, verbatim, one-sided) and `prop:carrier-ceiling` (PD-T537, verbatim, with its exclusions).
  - New §3 "corner operator": `thm:log-reduction` (PD-T534, verbatim constants 4096, 4300/log m, 120), `lem:corner-kernel` (PD-T535, verbatim), `thm:corner-operator` (PD-T536, verbatim), `rem:finite-comparison` (PD-T536 (4)), `rem:two-corners` (F8, limited to what the proof shows), and Appendix A with complete proofs.
  - **For the audit:**
    1. The paper's proof of PD-T534 tracks constants more tightly (intermediate 840/3360 against the record's 64/65-based constants); the statement keeps the record's 4096/4300.
    2. Record steps tightened in the paper: PD-T535 (8) Taylor expansion about the mean; Rodrigues/generating-function equality derived; PD-T536 (10) needs m ≥ 2K, which is added; the PD-T536 §4 transfer step is made explicit as Lemma A.4.
    3. ε/γ endpoint factors are renamed ε^{(m)}, ε^{(m+1)} in the old weights and carriers text (notation only).
  - Still to do (part 2): PD-T539–542 with Appendix B, the F7 corollary (PD-T?mz-paper-claude-02), §7 remark, finite results, §9, title, abstract, introduction, status box and visible `\id`, the ratio θ→τ rename, the C₀ and M′ renames, and availability.
- 2026-11-13/14 (handoff 04, MZ-SP part 2; Sonnet 5.5 high worker, verified by rebuild: 47 pp. elsarticle preprint 12pt, clean):
  - `prop:elliptic-kernel` (PD-T539; **weakened**: the log-singularity sentence is dropped). `prop:positivity` (PD-T540, verbatim). `prop:rectangles` (PD-T541, verbatim, with unused moduli trimmed). `prop:enclosure` (PD-T542, verbatim, computer-assisted, "fixes no digit"; the worker reran the endpoints bit for bit). `cor:norm-lower` (PD-T?mz-paper-claude-02, verbatim). Appendix B holds the proofs of PD-T539–542.
  - `rem:reproduction` (PD-T113, with the degree argument). **For the audit:** it adds the bound ‖f−Hf‖ ≤ (2+C_P)E_k(f), which PD-T297 and PD-T113 imply but no record states.
  - `prop:no-quadratics` (PD-N051, exact scope).
  - `prop:padua-brackets` merges PD-T107, PD-T298 and PD-T299 into one six-row certified table. **For the audit:** it adds "η<0.83", which is arithmetic on the brackets.
  - `prop:padua-finite-negative` (PD-T376) stays, with its witness arrays to be archived with the deposit. The measured material is in §8.3 with the F9 labels.
  - Front matter: new title, abstract and introduction (main results A–D with pointers), literature (BCDMVX06, SVZ08, Xu96, CDMV07, KLP18, ASV27, Wu26), and the statement that the CC inputs are proved in [MZ-CC]. The status box and visible IDs are removed. Notation follows notation-sp.md (τ, ι, M′, B⁻, **K**, ω_a, ϱ).
  - Open for AC: the Xu96 DOI is not resolver-checked (proxy). Unread CDMV 2005 and An–Ran–Wu are not cited.
  - Still to do: an independent check of the Appendix A/B translations (internal referee round, math) and the exposition round.
- 2026-11-14 (internal referee round): [referee-sp-math.md](referee-sp-math.md) (Opus xhigh: no CRITICAL/MAJOR; enclosure checker rerun bit-identical; brackets match the receipts), [referee-sp-exposition.md](referee-sp-exposition.md) (Opus high), [response-internal-sp.md](response-internal-sp.md). Revisions were applied by a Sonnet worker; no theorem-like number changed. Declined: the unregistered Θ(log m) fixed-ratio statement, demoting Prop 5.8, and replacing derivations by citations. 50 pp., clean.

## Frozen numbering of MZ-SP (2026-11-14, after the internal referee round)

| Label | Number |
|---|---|
| `sec:intro` | 1 |
| `sec:cc-recap` | 2 |
| `lem:weight-comparison` | 2.1 |
| `prop:cc-inputs` | 2.2 |
| `sec:marginal` | 3 |
| `thm:padua` | 3.1 |
| `sec:weights` | 4 |
| `lem:density` | 4.1 |
| `thm:padua-weights` | 4.2 |
| `prop:padua-odd-weights` | 4.3 |
| `sec:carriers` | 5 |
| `thm:padua-carriers` | 5.1 |
| `prop:padua-odd-carriers` | 5.2 |
| `cor:padua-ratio` | 5.3 |
| `rem:refuted` | 5.4 |
| `lem:fejer-cosine` | 5.5 |
| `prop:padua-growth` | 5.6 |
| `prop:carrier-improvement` | 5.7 |
| `prop:carrier-ceiling` | 5.8 |
| `sec:corner` | 6 |
| `thm:log-reduction` | 6.1 |
| `lem:corner-kernel` | 6.2 |
| `thm:corner-operator` | 6.3 |
| `rem:finite-comparison` | 6.4 |
| `rem:two-corners` | 6.5 |
| `sec:structure` | 6.2 |
| `prop:elliptic-kernel` | 6.6 |
| `prop:positivity` | 6.7 |
| `prop:rectangles` | 6.8 |
| `prop:enclosure` | 6.9 |
| `cor:norm-lower` | 6.10 |
| `sec:uniform-norm` | 7 |
| `thm:padua-operator` | 7.1 |
| `rem:reproduction` | 7.2 |
| `prop:no-quadratics` | 7.3 |
| `sec:numerics` | 8 |
| `prop:padua-brackets` | 8.1 |
| `prop:padua-finite-negative` | 8.2 |
| `sec:measured` | 8.3 |
| `sec:open` | 9 |
| `app:corner` | A |
| `app:reduction` | A.1 |
| `lem:triangular-tail` | A.1 |
| `lem:tensor-cc` | A.2 |
| `lem:tail-estimate` | A.3 |
| `app:kernel` | A.2 |
| `app:operator` | A.3 |
| `lem:finite-rank` | A.4 |
| `app:structure` | B |
| `app:arcsine` | B.1 |
| `lem:arcsine` | B.1 |
| `lem:abel` | B.2 |
| `app:elliptic-proof` | B.2 |
| `app:positivity-proof` | B.3 |
| `app:rect-proof` | B.4 |
| `app:certificate` | B.5 |

Later passes (audit fixes) may change wording but should not renumber; any renumbering must be listed here.
