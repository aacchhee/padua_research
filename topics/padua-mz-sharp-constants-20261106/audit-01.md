# Claude audit-01 — padua-mz-sharp-constants-20261106 (draft PR31)

- **Decision: mathematics ACCEPTED at the stated scopes; stage → WORK.**
  - I found no BLOCKING finding and no mathematical gap in any of the fourteen theory records. I accept every claimed PROVED status at its exact stated scope:
    - S1-01 (Volterra norm) and S1-02 (one-sided bound limsup (log N)²λ_min ≤ π⁴/8);
    - S2-01 to S2-06 (uniform 5/3, η-deficit, endpoint model, fixed-trial limit, qualitative limit Λ_edge, finite certificate);
    - S3-01 (strict carrier improvement), S3-02 (full signed reduction), S3-kernel, S3-03 (compact corner operator B and the common-parity limits) and S3-04 (family ceiling).
  - PD-T020 correctly stays OPEN. No status is upgraded beyond what the developer claims.
  - **Four MAJOR findings (A1–A4) concern interpretation and records, not proofs.** Two of them, A1 and A2, show that the registered numerical KILL outcomes K2 and K4 were read with the wrong meaning. In each case the audit finds an evidenced finite-N or finite-m mechanism that is consistent with the proved theorem. Both gate outcomes stay preserved exactly as registered.
  - Separately, the audit found concrete routes that could close open items (§ "Promising closures"). Following AC's instruction for this continuation, they are handed to Codex as development, together with the response, in [handoff 03](handoffs/03-response-and-work.md).
- **Audited candidate:** `5110954b07fd834982167780daa8cd22bef13ce1` (handoff 02 input). The branch head at audit start was `f8942ec9d489218db52d5a828a6d65952aa0d8bf`. `git diff 5110954 f8942ec` changes only `handoffs/01-work.md` (its status line) and adds `handoffs/02-audit.md`, so no scientific byte differs.
- **Base:** main `76ba4214b100c86a44941f5e9a662ce9ce48efb8`, refetched 2026-11-06 and unchanged; it is the topic's merge base.
- **Rules read** at `f8942ec`: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md`, `templates/HANDOFF.md`.
- **Auditor:** Claude, configured model `claude-opus-5-5`, xhigh as handoff 02 requests (Opus 5.5 xhigh row: novel mechanisms, new sharp constants, and rejected numerical proxies). The runtime exposes no separate serving-model receipt. I am a different agent from every Codex developer and from the supplementary Astra reviewers.
- **Subagents:** five supplementary Claude Opus 5.5 xhigh subagents worked without Git authority or repository edits:
  - S1, S2 and S3 proof reconstruction;
  - registered and from-scratch numerical reruns;
  - the complete novelty and records read.

  Their scripts and outputs are in [audit-01-support](audit-01-support/). The harness blocked subagents from writing report files, so their reports were returned to me and are summarized here; the novelty report is preserved verbatim in [records/novelty-records-findings.md](audit-01-support/records/novelty-records-findings.md). Their reports supplement, and do not replace, this record.
- **Role:** independent auditor, and topic orchestrator for this step only. I did not edit any developer proof, code, evidence or earlier handoff body.

## Read coverage

- **Topic.** Handoffs 01 and 02, `report.md`, `plan.md`, `rounds.md`, `gates.md` (full), `LOG.md` (full), `manuscript-insert.md`, and the results file `results/padua-mz-sharp-constants-20261106.md`. Also the essential evidence `evidence/S4-essential-cc.json`, `S4-padua-essential.json`, `S3-corner-model.json` and `S4-k1-fit.json`.
- **Theory.** All fourteen `theory/*.md` files were read in full between me and the three proof subagents. I personally read S1-02 and S3-03 in full and reconstructed S3-03 §1–5 (tail (5)–(6), corner phases (7)–(8), active-corner table, Gram transfer, (12), compactness, (4)). Dependencies: PD-T013, PD-T014, PD-T015, PD-T017, PD-T018 and PD-T111 in the relevant parts, and the PROOF_STATUS rows for PD-T020, PD-T027 and PD-T381.
- **Ideas and novelty.** The novelty subagent read the **complete `state/IDEAS.md` at `f8942ec` (1112 lines, every obstruction and disposition table)**. It also read targeted `literature/INDEX.md` rows, the LIT-053/054 record, all topic novelty gates (`novelty-gate-S1/S2/S3.md`), `ideas/*.md` and `literature-screen.md`. Its repository-wide synonym searches found no missed predecessor; search terms and shortlist are in its report. Closest predecessors:
  - IDEA-071 and IDEA-054 for the sharp endpoint limit;
  - IDEA-386, whose resume condition S2-01 meets exactly;
  - IDEA-469 and IDEA-470, whose resume condition S3-02/S3-03 meet.
- **Candidate content identities (SHA-256, identical at `5110954` and `f8942ec`):**

| File | SHA-256 |
|---|---|
| `theory/S1-model.md` | `96a1fcccd10413c8a0f749162ce374c89638135e242bbe19be8a844ad1b2573b` |
| `theory/S1-sharp-one-sided.md` | `b8378bed12f010f4d7572a72effa27ab8fde9b303f5f7d079dbc43b03f4f1e5d` |
| `theory/S1-volterra-model.md` | `3ef7fb8cbea9b2fe39677731fc43f1292c78a5043ff7ab0da84288fcb464c491` |
| `theory/S2-endpoint-model.md` | `78428430f103024c044435dbf7742f0fbce5780888c2468f85dbd35c3f0b163d` |
| `theory/S2-eta-deficit.md` | `72f70e50aa67d5c7f3a262cf789984ed4a0283f05eeb11e47a98ef1f0a637a33` |
| `theory/S2-finite-certificate.md` | `f8e895eb3a5061de9fd1e96a603f56047919ba3600634266304b0e2e2358a90f` |
| `theory/S2-fixed-trial-limit.md` | `e11070a2876f3ea87857f00ab471a55713ccdfba13aa5af77e11ef38a6db91c1` |
| `theory/S2-qualitative-limit.md` | `978dfa4332eb8146f69da3b9d83a84188627fd72ec91c5fa50a19ee89e0d5943` |
| `theory/S2-uniform-upper.md` | `3a45f40aad550a50da4871ab2d3554adb60b41513b08b2427e10b203408b9e6b` |
| `theory/S3-carrier-family-ceiling.md` | `296cc8ef799d79e9ed639b71d5995d05f29e0bc360d38e5010ddae62f972eae0` |
| `theory/S3-corner-kernel-hard.md` | `0200a23f0262418fe12cf1458bfbbc11bcb85018dce488a913fc58eae3bd326a` |
| `theory/S3-corner-operator-limit.md` | `94245edd52b601778d386d671a689b667abae9cbedd6481c9ab5a9112f883a83` |
| `theory/S3-full-form-log-model.md` | `8c991ebc077b8f27edaf9baf887c076db7737903f859d5a8de286734d53a2a77` |
| `theory/S3-normalized-carrier-improvement.md` | `4347162a0ed3cfb2c830860530f7a22c500d1d4889a1b395db8728ef76c8bd13` |
| `report.md` | `c842b92362d27a8dd4388f4b19a99cdf861e5fe2fc3228dbe07c4ae0fd818eac` |
| `gates.md` | `6390b9576c60e2ba7fcb1cc9c64a842b1da9b023511d0db2d34eeb7edc118ff3` |
| `manuscript-insert.md` | `38e0ed9a4ebd7e1cda21172d312e08dab85c94f4ed25dc488596e00a1a71dc3b` |

## Independent reconstruction, claim by claim

**S1-01 and S1-02, the CC lower direction — PROVED, accepted.**
- **Volterra lemma.** β²+β′=−a², the boundary terms vanish, and sin(πx/2) attains equality, giving ‖V‖=2/π.
- **Cardinal formula** from (1−x²)T_N′=N sinθ sinNθ.
- **Degree cancellation.** The top coefficient N⁻¹Σa_k/c_k (c_0=c_N=2) cancels under a_(N−k)=−a_k, with a_0=a_N=a_(N/2)=0, for both parities. Numerically |b_N|/max|b| ≤ 1e-16 at 45 values of N.
- **Weight expansion.** |w_k−(π/N)sinθ_k| ≤ 2/(N²−1).
- **(D) partial fractions.** Below t, B_k=½[1/(t−k)−1/(t+k)]. Above t, B_k=1/k+1/(2(t−k))−1/(2(t+k)). The pole pairing is bounded.
- **(G) cotangent identity.** It is exact, with the remainder [e(θ+φ)−e(φ−θ)]/2 ≤ θ·sup|e′| uniformly through the diagonal.
- **(H)–(I).** The Jacobian factor, the sin²→½ average (integration by parts, amplitude derivative O(t⁻²)) and the remainder orders all check.
- **§5 order of limits.** f is fixed, then N→∞, then δ→0, then density. (π²/2)(π²/4)=π⁴/8.
- **Numerical checks.**
  - The trial quotient exceeds the measured λ_min at all 42 registered N; the smallest ratio is 1.69 ([S1/compare.py](audit-01-support/S1/compare.py)).
  - A dense replay reproduces registered λ_min to ≤3e-11 at N=100,101,400,401,1600,1601.
  - The remainder O(N/t) in (H) is attained, so the trial quotients converge only at rate O(1/log N). This is consistent with the theorem and explains slow finite-N behaviour.
- **Minor wording.** See A6.

**S2-01 to S2-06, the CC upper direction — PROVED, accepted.**
- **Completion.** R=M−H+K re-derived with signs from PD-T013, and H is PSD by its moment integral. Each K entry is ≤1/(L_N²−1), with ≤⌈N/2⌉ entries per row, so PD-T015 gives β_N ≤ 2/3 and the 5/3 bound. Numerically, at N=2..120, the identity holds to 1e-16 and βM−K ≥ 0.005.
- **η-deficit.** 1−η=min(λ₋, 2−λ₊).
- **Endpoint model and limit.**
  - Core coefficients and the Jacobian are correct.
  - Density in V needs no trace assumption. The extension of H to V and its Laplace identification are justified.
  - The weak-profile cross terms cancel exactly, and M(g⁺)+M(g⁻) ≤ 1.
  - K is compact, H is lower-semicontinuous by Fatou via the sinh representation, and escaping mass is handled.
  - No spectral limit is inferred from entrywise convergence. λ₁=0.98914<1, so Λ ≥ 1 genuinely uses the j→∞ diagonal argument, which the file supplies.
- **Finite certificate.** I re-derived every Lipschitz, Schur, E_M, E_K and E_H constant, including the odd-N half cell. Monotonicity, compactness and Fatou give u_cont→0. The clipped formula is correct and computable, and ε_N→0. The practical size is a MINOR record gap (A8).

**S3-01 to S3-04 and S3-kernel, the signed Padua direction — PROVED, accepted.**
- **Weights.** The PD-T111 weights with the even-m h_m term match the frozen `weights_dct` to 1e-16 for m=4..1001.
- **Nodal and tensor bounds.** The nodal bound (8) holds with measured ratio 9–47 against the proved 134. The PD-T017 floor and PD-T014 tensor step give 4020 ≤ 4096, and ‖L_m‖ ≤ 120 holds.
- **Kernel and corners.** The kernel error kt²/4 checks, and cross-corner terms cancel through alternating Legendre parity. The r+s+mδ_x+Mδ_y parity selects exactly the two active corners in the table.
- **Corner limits.** In my own reconstruction, cos(2Rπr/m)→(−1)^r and cos(2Rπs/M)→(−1)^s with the stated rates, giving the −16e_re_s(−1)^r active blocks and zero inactive blocks.
- **Transfer.** Signed finite-rank transfer holds via the V*V=G polar argument. Zero padding is valid since N_K ≤ 2K² < dim Π_(m−1) for m ≥ 2K. The two active blocks are identical because the corner Gram does not depend on corner signs; numerically, L_m's low spectrum is exactly doubly degenerate.
- **Limit and errors.** (12) gives the Cauchy property and compactness, and the variational extremes move by at most the norm difference. The matrix square-root bound 2√δ and the assembly of (4) check.
- **S3-04.** U_minus ≈ 0.0333 < 1/24, correctly scoped to the fixed-parameter scalar family.
- **Numerical checks.** ν₁(L_m) is within about 0.001 of B's bottom proxy (−0.13358) at m=100..801 (§ A2), which independently supports the transfer.

## Actual executions (this audit)

All runs used single-thread BLAS, except my own kernel run, which used 4 threads. Environment: Python 3.13.18, NumPy 2.5.3, SciPy 1.18.1 and mpmath 1.4.1; the developer used 3.12.14 / 2.3.5 / 1.17.0. Outputs went to the session scratchpad, and small copies are under [audit-01-support](audit-01-support/). Total about 1.3 CPU-h. No Syvert run, upper Padua campaign or extension of any registered grid was made.

1. **The handoff 02 commands, all exit 0** ([num/runlog.txt](audit-01-support/num/runlog.txt), [num/jdiff.txt](audit-01-support/num/jdiff.txt), [num/tables.md](audit-01-support/num/tables.md)):
   - manifest: 63 identities, 0 missing;
   - K0 cc and carrier: bit-identical values;
   - K1: intercepts agree to 3e-15, and K2 is still KILL_MODEL;
   - K3: intercepts agree to 6e-16;
   - S2_model: bit-identical (J512 1.0044369188646673);
   - S3_corner_model: agrees to 2e-16;
   - Padua fit: identical slopes and the same K4 KILL_HEURISTIC_PROXY and K5 MEASURED verdicts.
   - The replayed `prereg_sha256` differs from the receipt; this is a provenance issue, see A12.
2. **From-scratch CC.** Own Gram/SVD code matches the S4 rows at N=100..801 to ≤9e-12 relative; mpmath at N ≤ 400 to ≤3.4e-14. The S2 subagent's own Gram matches λ_max at N=100..3201 to ≤4e-11.
3. **From-scratch Padua.**
   - Weights solved by exactness match the formula to 9e-16 and sum to 4.
   - Dense extrema at m=10–21 match committed values to ≤1.5e-13.
   - A matrix-free m800 minimum gives 0.040025262150, against committed …1516 (relative 4.6e-11).
4. **From-scratch B_K.**
   - B_K with two collapse directions and orders 200/300 matches the committed K16–128 extrema to ≤3.1e-15.
   - At K=256 and 512, λ_min stays within 3e-5 of −0.13358 and λ_max at 0.04560.
   - The K4 gap is therefore not a K-truncation effect.
5. **S1 trial and fit diagnostics** ([S1/](audit-01-support/S1/)): `trial.py`, `checks2.py`, `fits.py`, `compare.py`, `fullspace.py`, `hardy.py`, about 2 CPU-min. Results are in A1.
6. **S2 constant, fixed-J and feasibility estimates** ([S2/](audit-01-support/S2/)): `constcheck.py`, `uniform_check.py`, `fixedJ_check.py`, `model_mp.py` (40-digit J512 Rayleigh quotient 1.00443691886467), `LN_est.py`, `UN_est.py`, `scan2/3.py`.
7. **S3 spectral diagnostic** ([S3/](audit-01-support/S3/), `lm_spectra2.py`; receipts `small/mid/big.json`). Lowest six eigenpairs of L_m, Q_m restricted to them, and projections of Q_m's minimiser, at m=40..801. Results are in A2.
8. **My own closed-form-kernel check** ([kernel/](audit-01-support/kernel/), output in [Bclosed.out](audit-01-support/kernel/Bclosed.out)); see Promising closures, P1.

## Findings

Severities follow WORKFLOW: BLOCKING, MAJOR, MINOR, NOTE.

### A1 — MAJOR: the K1/K2 outcome is misread; the S1 equality disposition is not a WORKFLOW disposition

**The tension.** The registered K1 intercept, 13.0611 in final window B, lies **above** the PROVED bound limsup (log N)²λ_min ≤ π⁴/8 = 12.1761. The data rise slowly toward it: the measured value is (log N)²λ_min = 7.756 at N=102400.

So if S1-02 holds (accepted above), the K1 three-parameter extrapolation c + a·loglogN/logN + b/logN overshoots the true limsup by at least 0.885 (7.3%). The 7.27% "disagreement" that kills the model in K2 is therefore at least partly a lower bound on the fit's own asymptotic bias. It is not evidence against π⁴/8 being the true limit.

**Supporting post-hoc diagnostics** (MEASURED; they must not revise K2 or any registered threshold, [S1/fits_out.json](audit-01-support/S1/fits_out.json)):
- The K1 intercept falls as the window moves out: 13.218 in window A, 13.061 in window B; 13.199 for all N ≥ 400 and 13.159 for all N ≥ 1600.
- Inverse-power models in 1/L (L=log N) fit window B about 1000 times better than K1. The model 1,1/L,1/L²,1/L³ gives c=12.2168 with rms 1.6e-8; the model 1/L…1/L⁴ gives c=12.2207 with rms 2.5e-9; K1's rms is 1.6e-5.
- With the intercept fixed, c=π⁴/8 fits about 20 times better than c=13.0611 (rms 4.6e-6 against 9.5e-5).

**Records to change.**
- `report.md`, `gates.md` (K2 interpretation), `theory/S1-model.md`, `ideas/S1.md`, `attempts/S1.md`, `manuscript-insert.md` and the results file must state plainly that the K1 intercept exceeds a proved upper bound on the limsup.
- K2's KILL_MODEL is retained as the registered operational outcome. But it carries no evidential weight against c=π⁴/8, and the stopped equality route was stopped on a misspecified numerical test.
- "Operationally rejected" (`ideas/S1.md`, `theory/S1-model.md`) is not a WORKFLOW disposition. Record the S1 equality candidate as `deferred`, with resume condition "a proof of the reverse bound liminf (log N)²λ_min ≥ π⁴/8, or a new prospectively registered numerical protocol". It must not be `REJECTED: failed`, and no PD-N may be created.
- Reopening the equality as a **mathematical target** is a proof of PD-T020's open reverse bound, not a post-gate fitted model revision. It is assigned as development P3 in handoff 03.

### A2 — MAJOR: the K4 outcome is misread; the finite-window minimiser is B's second mode

The theorem determines lim λ_±/log m. It predicts nothing about finite-window slopes dλ_min/d log m at m ≤ 3000, and its explicit errors (4300/log m ≈ 537 at m=3000) are vacuous there. The report treats the 31% gap mainly as unexplained.

The audit diagnostic ([S3/big.json](audit-01-support/S3/big.json), [S3/mid.json](audit-01-support/S3/mid.json); MEASURED float, single thread) explains it:

| m | ν₁(L_m) (twofold) | ν₂(L_m) (twofold) | λ_min(Q_m) | L_m at Q-minimiser | Q-min weight on mode 2 | Q on mode 1 / mode 2 |
|---|---|---|---|---|---|---|
| 400 | −0.13391 | −0.09577 | 0.10282 | −0.0906 | 0.938 | 0.481 / 0.144 |
| 800 | −0.13374 | −0.09565 | 0.04003 (= S4 row) | −0.0914 | 0.951 | 0.387 / 0.078 |
| 801 | −0.13408 | −0.09589 | −0.00581 (= S4 row) | −0.0921 | 0.957 | 0.318 / 0.030 |

- **Fast convergence of L_m is confirmed.** ν₁(L_m) is already at B's bottom proxy (−0.1336) and ν₂ at B's second eigenvalue (≈ −0.0955; [S3/bk_low.py](audit-01-support/S3/bk_low.py)).
- **The correction is strongly mode-dependent.** The O(1) correction Q−log R·L is ≈1.19 on the ground mode (1.12 at odd m), against ≈0.65 on mode 2 (0.60 at odd m), stably over m=400..801.
- **The minimiser is mode 2.** About 95% of the actual minimiser's weight lies on B's second mode, and its L value (−0.091 to −0.092) matches the registered window slopes −0.0915 to −0.0925.
- **The crossing is far away.** The two branches cross only near log R ≈ 0.537/0.038 ≈ 14 (m ~ 2·10⁶). Only beyond that can the minimum branch's slope approach c_minus.
- **Fit for test.** This is consistent with the theorem and is a falsifiable finite-m mechanism; P2 registers it prospectively. The theorem's statement is unaffected.

Records to change: `report.md`, `gates.md` (K4 interpretation), the theory record S3-03 "Checks" and `ideas/S3-corner-operator.md` must say that the K4 proxy test compared a theorem about limits with finite-window slopes. Each should cite this diagnostic as MEASURED audit evidence. The K4 KILL outcome is preserved unchanged and is not a PD-N.

### A3 — MAJOR (decision for AC): mapping the original targets PD-T027 and PD-T381

- **PD-T020** ("existence/value of sharp rescaled endpoint limit") stays OPEN. S1-02 is a supporting one-sided bound and not a part of its own statement. Agreed with the developer.
- **PD-T027** ("sharp endpoint upper limit and uniform endpoint upper gap") decomposes into two conjuncts:
  - the uniform gap, PROVED by S2-01;
  - the sharp limit, whose existence and exact identification as the variational supremum Λ_edge are PROVED by S2-05 (finite J512 value 1.00443692, MEASURED; no certified decimal).
- **PD-T381** ("determine existence and values … including their agreement") has its existence and parity agreement PROVED by S3-03. Its values are characterised as inf/sup σ(B) with a computable 120/K tail, but no certified decimal.

**Options for AC:**
- **(a)** Accept an exact characterization (a fixed explicit variational problem or compact operator with computable convergent approximations) as "identifying the value". Then PD-T027 and PD-T381 become PROVED, linked to S2-01/S2-05 and S3-03 respectively.
- **(b)** Conservative reading. Then each becomes PARTIAL: for PD-T027, the uniform-gap conjunct and existence of the limit are PROVED, and the decimal value is OPEN; for PD-T381, existence and agreement are PROVED and the values OPEN. This requires recording the conjunct decomposition in History without rewording the original targets.

**My recommendation:** decide after the handoff-03 development. P1 (certified enclosure of inf/sup σ(B)) and P4 (certified bracket for Λ_edge) would satisfy reading (b) directly where they succeed. If they fail, (a) is defensible, because the characterizations are fixed, explicit and computable with proved convergent errors. PR preparation must not choose either option without AC's ruling.

### A4 — MAJOR: no durable MEASURED record for the reported numerics

The numbers that `report.md`, the results file and `manuscript-insert.md` report as findings have no registered durable home. Under WORKFLOW ("a distinct measured claim gets its own durable registered home"), each needs a MEASURED theory record with scope, inputs, commands, receipts and limitations, linked from the report:
- K1/K3 fitted constants;
- the Λ_edge J512 proxy;
- the B_K proxies −0.1336 and +0.0456;
- the 16 Padua minima and their window slopes;
- the normalization diagnostic.

Use one compact record per direction, or explicitly state why a number is only an operational gate receipt and is not reported as a finding.

### A5 — MINOR: stale or contradictory text in the S2 records

- `S2-qualitative-limit.md` ("Split into" header; "quantitative obligations remain OPEN"), `S2-fixed-trial-limit.md` and `S2-uniform-upper.md` (open items), and `rounds.md` still call obligations OPEN or pending that later PROVED files settle.
- `S2-endpoint-model.md` repeats S2-05/06's PROVED status instead of linking it.
- `S2-uniform-upper.md:6` says "Split from: supporting sharpened conclusion for PD-T027". The uniform B<2 is a conjunct of PD-T027's own statement, so write "Split from: PD-T027, uniform-gap conjunct". This also matters for A3 (b).

### A6 — MINOR: S1 wording and citations

- **Depends on:** cite "PD-T017 proof §1, with PD-T013 (1)" for w_k=(π/N)sinθ_k+O(N⁻²); this is not in PD-T017's Statement.
- **§1:** "Fix0<a<b<1 containing supp f" should read "with supp f ⊂ (a,b)".
- **(D):** "finitely many small t cases" should read "the bounded range t ≤ t₀", and the file should state that (D) is asserted for noninteger t and extended by continuity.
- **Missing spaces** throughout ("Fix0", "norm2/pi", "is1/u"; the same pattern appears in the report and gates).

### A7 — MINOR: S3 wording

- S3-03 and `ideas/S3-corner-operator.md` should say explicitly that (3) and (4) make no prediction about finite-window slopes (connects to A2).
- S3-02 §1: write a,b ≥ L+1 instead of a,b > R/2.
- S3-03 §3: state that the corner Gram block does not depend on corner signs, which is why the two active blocks are identical.

### A8 — MINOR: S2-06 should state its practical bracket sizes

As specified, the certificate gives:
- L_N = 1 for every N up to about 4.4·10⁶, 1.00356 at N=10⁸ and 1.00442 at N=10¹⁸;
- U_N ≈ 1.08 at N=10⁶ and 1.062 at N=2.7·10⁸.

So ε_N > 0.05 at every N that can be evaluated ([S2/LN_est.out](audit-01-support/S2/LN_est.out), [S2/UN_est.out](audit-01-support/S2/UN_est.out); float estimates of the stated formulas). Record this as a limitation of the PROVED result. Its status is unaffected.

### A9 — MINOR: literature screen

- `literature-screen.md` calls the LIT-054 record absent. `literature/records/mz-widom-1966-screen.md` already has an extraction-level reading (RELATED, DIFFERENT SETTING); cite it.
- Credit the classical Volterra norm 2/π (Halmos) in S1-01 as LITERATURE context, with the local proof retained.
- Before manuscript adoption, screen these, recording coverage limits and making no priority claim:
  - Lubinsky, ["On sharp constants in Marcinkiewicz–Zygmund and Plancherel–Pólya inequalities", PAMS 142 (2014)](https://www.ams.org/journals/proc/2014-142-10/S0002-9939-2014-12270-2), whose scaling-limit mechanism is analogous to S2. The novelty subagent confirmed it exists by search only; it probably treats p≠2 in the bulk.
  - Mehler–Heine and hard-edge Bessel kernel universality (for S3-kernel).
  - Schlömilch series (for P1 below).

### A10 — MINOR: IDs and idea records

- "IDEA-S3-02/03" (the original registration heading) is not in the provisional-ID format.
- `S1-model.md`'s ID kind is ambiguous.
- `ideas/S2-*.md` and `ideas/S3-*.md` lack templates/IDEA.md fields: closest entries, obstructions escaped, verdict, kill test.
- At PR preparation, S2-01 should be registered as the consolidated continuation of deferred IDEA-386, and S3-02/S3-03 as meeting IDEA-470's resume condition, rather than as unrelated fresh IDEAs.
- At PR preparation, update IDEA-054/071/469, MZ obstruction memory `state/IDEAS.md:406`, and the PD-T027 notes at `state/IDEAS.md:938/942`. Do not touch these registries now.

### A11 — MINOR: cold storage

`cold-storage.json` is not in `padua-cold-storage-v1` format, and `tools/cold_storage.py verify` rejects it. Its locators are ephemeral `/tmp` paths, and one entry lacks `source_commit`. Convert it to the tool's format with honest "local pending, not retained" status, or state that the optional raw receipts were not retained.

### A12 — MINOR: preregistration hash replay

`code/S3_corner_model.py` hashes `ideas/S3-corner-operator.md` as it is now. That file was edited after publication `59d02c7`: the title was changed to the provisional-ID format, "CONJECTURAL" became "OPEN and conjectural", and dated sections were appended. A replay therefore reports `03eff691…` instead of the receipt's `c2e8b10a…`.

The changes are disclosed and preserve the prediction, and the original is retrievable as the `59d02c7` blob. Record in the S3 attempt or receipt note that the registration hash refers to that blob, so later replays are not read as tampering.

### A13 — MINOR (caused by this audit): manifest membership

`code/evidence_manifest.py` inventories every `topic/**/*.json`. The audit support JSON outputs under `audit-01-support/` therefore make `evidence_manifest.py --checks` fail with "manifest mismatch … membership changed" at the audit output commit. The handoff-02 run above was executed before those files existed and passed.

The developer response should exclude `audit-01-support/` from the manifest scope, since auditor files are not developer evidence, and regenerate the manifest intentionally, recording the change. The alternative is to inventory these files deliberately. No developer evidence byte is changed by the audit.

### NOTES

- **N1.** The K3 parity difference 3.85e-12 is at float noise (independent CC agreement ~1e-11). It passes the 1e-6 gate and must not be quoted as a finer agreement.
- **N2.** The m801 row lists 6 negative Padua weights, where m ≤ 41 shows 2. In the essential file this is a pattern by parity and size (m800/1000/1200 have 2; m ≥ 1400 and all odd m ≥ 801 have 6); the weights match the formula. No issue found, but it is not separately explained.
- **N3.** Dense N ≤ 3200: λ_min on Π_N equals λ_min on Π_(N−1) to ~1e-13 (the minimiser lies in the parity-(N−1) sector). This is useful for P3.
- **N4.** The temporary 10 MB generated-output allowance is cited from an unmerged branch blob; the citation is canonical in LOG. No action is needed beyond keeping the link.
- **N5.** My audit support adds about 141 kB of scripts and small outputs (each file < 16 KiB except the verbatim novelty report, which is prose).

## Promising closures (handed to Codex as WORK in handoff 03)

These are leads with numerical support, not claims. None is a PROVED result of this audit.

**P1 — certified values of c_±=inf/sup σ(B) through a closed-form kernel.**
- **Kernel.** Write the j+k-even restriction as ½[1+(−1)^(j+k)] and use the Gegenbauer product formula J0(u)J0(v)=(1/π)∫_0^π J0(√(u²+v²−2uv cosφ))dφ. The Schlömilch series Σ_(n≥0)e_n J0(nx)=1/x (0<x<2π) and Σ_(n≥0)e_n(−1)^n J0(nx)=0 (0<x<π), =2/√(x²−π²) (π<x<3π), then give, with respect to ab da db,

      B(a,b;a',b') = −8[S_alt(a,a') S_all(b,b') + S_all(a,a') S_alt(b,b')],
      S_all(a,a') = 2K(k̃)/(π²(a+a')),           k̃² = 4aa'/(a+a')²,
      S_alt(a,a') = 2K(k)/(π²√(aa')) · 1[a+a'>1],  k² = ((a+a')²−1)/(4aa'),

  where K is the complete elliptic integral of the first kind.
- **Numerical support.**
  - Pointwise smoothed partial sums confirm both closed forms to ~1e-11, and S_alt=0 for a+a'<1 to <1e-13.
  - A 1D bilinear test of S_alt agrees with the series to 5e-8.
  - Independent midpoint-Nyström spectra of this kernel (n=40..120) extrapolate to about −0.133…−0.135 and +0.045…+0.046, matching the B_K proxies ([kernel/Bclosed.out](audit-01-support/kernel/Bclosed.out)).
- **Consequences.** The kernel is **pointwise ≤ 0**. If the identification is proved:
  - c_minus=−‖B‖;
  - the ground state is positive and, by irreducibility, simple;
  - ‖B‖ admits a rigorous two-sided enclosure: a Rayleigh quotient of a positive trial from below, and a Schur test sup_x(−Bh)(x)/h(x) with a positive h from above.
  
  c_plus needs a Galerkin method with rigorous residual bounds (Temple/Lehmann, or Kato with a kernel-regularity tail bound). This could settle PD-T381's values under reading (b).

**P2 — a prospective test of the two-branch finite-m mechanism (A2).**
- **Registration first.** Before computing, register these predictions:
  - λ_min(Q_m) follows B's second-mode branch for m ≤ 3000, with Q-min weight on mode 2 > 0.9 and L at the minimiser within 0.005 of ν₂(L_m);
  - Q(mode 1)−Q(mode 2) decreases at 0.038±0.006 per unit log R;
  - each finite-window slope lies within 0.006 of b₂ ≈ −0.0955 rather than within 10% of c_minus.
- **Run.** Reuse `lm_spectra2.py`'s matrix-free construction at m=1600, 1601, 3000, 3001: about 1–2 CPU-h, at most 2 concurrent processes, within the existing 6 h/run and 48 CPU-h ceilings.
- **Kill.** A departure (for example the minimiser leaving mode 2, or the branch-difference rate off by more than 50%) kills the mechanism and must be recorded as a scoped finite-m PD-N candidate only if it is evidenced.
- **Optional theorem target.** Two-term asymptotics λ_±(m)=log R·c_± + d_± + o(1), with d_± from an explicit O(1) corner operator.

**P3 — the reverse CC bound (PD-T020), i.e. lim (log N)²λ_min = π⁴/8.** The S1 subagent's sketch (unaudited) works on Π_N without the degree constraint (N3):
- exact global cot-kernel representation; the bounded e-part costs O(√L) by Cauchy–Schwarz with Σ1/w_k=O(N²L);
- split the homogeneous part H_L=P+E, where P is the primitive (Hardy-type) part;
- P reduces to a discrete log-Hardy inequality with constant (2/π)²(L+O(1))², which follows from the Volterra lemma by a step embedding (measured shift ≈ 0.578, [S1/hardy_out.json](audit-01-support/S1/hardy_out.json));
- E must be shown O(1). The far-field kernels are Schur-bounded, but the pole part π Σ(−1)^k g_k sinc(t−k) needs a signed weighted Plancherel estimate on dyadic blocks; an absolute majorant fails, compare PD-N005;
- assembly then gives ‖p‖² ≤ (8/π⁴)L²(1+O(L^(−1/2)))Q, hence liminf ≥ π⁴/8 on both parities.

The main obstruction is a uniform signed near-diagonal estimate for E with constants tracked, plus bookkeeping for endpoints, microscopic cells and k≈N/2. Optional numerics: only under a **new prospectively registered** protocol (for example structured-solver rows to N=10⁶–10⁷ with an inverse-power ansatz fixed in advance). This does not revise K1/K2.

**P4 — a certified bracket for Λ_edge (lower priority).**
- **Lower side.** An interval-arithmetic Rayleigh quotient certifies Λ_edge ≥ 1.0044369 cheaply.
- **Upper side.** The specified A/Q error is the bottleneck: the best float-estimated upper bound is about 1.018 at Q=2·10⁴ (rigorous Cholesky ~2.7e12 flops, 3.2 GB), and three decimals would need Q ≈ 10⁷. A graded mesh, Toeplitz-plus-Hankel FFT products with Lehmann/Temple bounds, or a dual variational upper principle are the realistic routes to roughly four digits.

## Residual uncertainty

- **Proofs.** They were reconstructed by me and three subagents of the same model family, so correlated blind spots cannot be excluded. The Astra checks are a different family and agree.
- **Numerics.** Every audit numeric is floating-point MEASURED, without enclosures.
- **P1–P4.** These are unaudited development leads. P1's kernel identification in particular needs proof that the product-truncated norm limit equals the closed-form integral operator.
- **Literature.** Coverage is search-level only (A9).
- **Scope of this record.** No registry, final ID, manuscript, main, tag or workflow was touched.
