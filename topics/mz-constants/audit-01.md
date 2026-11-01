# Audit 01 — MZ constants (cross-agent mathematical audit)

- Auditor: Claude, independent auditor (the other agent from the Codex developer). Model: Opus 5.5, xhigh effort, as requested in the handoff prompt `Claude (Opus 5.5 xhigh): Continue codex/mz-constants-20261031.` The runtime reports the model; the effort level is taken from the session request.
- Reason for this choice: `agents/WORKFLOW.md` assigns Opus 5.5 high or xhigh to mathematical audit and xhigh to adversarial audit of novel mechanisms. This package has both. A separate Claude subagent (Opus 5.5) checked the registry, ID ledger, batch rehearsal, manifests and file limits. Its findings are integrated in §5 and were re-checked by the auditor where marked.
- Date: 2026-10-31 (Europe/Oslo evening).
- Rules read at the branch head `fdf0648cbaa9fb722c611d709e638de7dfe86368`: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md`, and `topics/mz-constants/AUDIT_HANDOFF.md`.
- Audited candidate: branch `codex/mz-constants-20261031` at head `fdf0648cbaa9fb722c611d709e638de7dfe86368`. The base is `d36722823441dc40c6e19d69a174459348dd309c`, equal to current `origin/main`. PR [aacchhee/padua_research#3](https://github.com/aacchhee/padua_research/pull/3). The theory-file SHA-256 values match `audit-targets.json` (§5).
- Read in full: all 21 theory files in `tracks/mz-constants/theory/`; `paper/manuscript.tex` (all 925 lines) and `paper/README.md`; `topics/mz-constants/{LOG,report,AUDIT_HANDOFF}.md`; `state/IDEAS.md` in full, including both obstruction tables and the disposition table; `directions/M3/IDEAS.md` (IDEA-073/074/075); `literature/INDEX.md`; and the An–Wu record.
- Read in part: `independent-astra-01.md` (finding tables and dispositions); `reproduced-spectra.md` tables; the M1/M2 direction records (sections cited by the theory files).
- Novelty scope: in scope. The full IDEAS.md read was done; §4 records the novelty assessment. This audit makes no priority verdict.
- **Verdict: CHANGES REQUESTED.**
  - There is no High finding, and no mathematical error was found. Every PROVED statement in scope was reconstructed line by line and found correct as stated, with correct hypotheses and statuses.
  - Medium findings M1–M2 affect what the registry and manuscript present as the headline results, and which prior art must be screened. They do not affect validity.
  - Protocol finding P1 (Medium, §5) concerns a split batch ledger that must be reconciled before any member PR is ready. P2–P7 are Low or Informational bookkeeping items.
  - Under the workflow, findings set the stage to WORK. Codex answers in `response-01.md`. The proposed change in M1 adds a one-line corollary; that addition needs a focused re-audit only.

## 1. Independent checks actually run

All ran in this session, in a fresh clone at `fdf0648`. The environment was a Linux x86_64 container with a Python 3.12.3 venv, NumPy 2.3.5 and SciPy 1.17.0 (the same NumPy/SciPy versions the handoff records). The developer's own scripts were run unmodified. The supplied input zip came from AC's machine; SHA-256 `d55a843c…74bcaa8` matches the LOG, and `sha256sum -c SHA256SUMS.txt` passed for all 21 entries.

| Check | Command (abridged) | Result |
|---|---|---|
| M1 exact/floating | `python tracks/mz-constants/code/m1_exact_check.py --max-n 40 --float 2 3 4 5 6 10 20 40 80 160 320` | EXACT PASS for N=2..40; N=5 margin −2/35. All EXACT/MEASURED lines are identical to `astra-m1-replay.txt`. |
| M2 endpoint | `python tracks/mz-constants/code/m2_endpoint.py --exact 512 --measure 8 … 1024` | `RQ_lt_1_4: true`, `Q=524288/262143`. The JSONL is identical to `astra-m2-replay.jsonl` apart from the Python patch-version string. |
| M3 exact | `python tracks/mz-constants/code/m3_exact_check.py --max-n 25 --measure 20 40 80 160` | `EXACT: 324 pairs … PASS`. Measured lines are identical to `astra-m3-replay.txt`. |
| Full reproduction | `OPENBLAS_NUM_THREADS=1 … reproduce.py --suite all --max-N 1280 --output <local>` | 637 numeric fields. **Bitwise equal** to the committed `reproduction.json` (max relative difference 0). Only timestamps, paths and the command field differ. One harmless `RuntimeWarning` comes from the supplied `cc_mz_large.py`: `np.where` evaluates 2/(1−k²) at k=1. |
| Protocol checker | `python tracks/mz-constants/evidence/protocol-check.py` (after restoring the ignored notes from the verified zip) | 86/86 manifest entries `current`. Counts: PD-T 16, PD-N 5, IDEA 25, LIT 19; statuses PROVED 17, OPEN 3, MEASURED 1. The only broken local link is the ignored PDF. |
| **Auditor's own checker** (independent code, no campaign imports) | `python -I tracks/mz-constants/evidence/claude-audit-01-check.py --fits` → `claude-audit-01-check.json` | E1: the closed-form CC weights agree with a moment solve to 8.0e−16 (N≤30), and are positive for N<200. E2: **exact** Fraction check of every off-diagonal sign of A_ρ=(1+ρ)M−R for all 0≤n<N≤60 (539,400 entries, 0 violations), extending the developer's N≤25. E3: exact U_{N−1} norms for N≤60. E4: exact telescoping row sums (Mb)_i and floor ratios for N≤40. M1/M2/M3 are MEASURED, below. |
| Padua compression (own code) | same script, M2 section | Weights come from the total-degree moment solve on the Padua set, N=2..14. There are 1–2 negative weights. Marginal error is ≤2.0e−15 against 2w_CC. λ_min^P≤λ_min^CC and λ_max^P≥λ_max^CC hold in every case. |
| Manuscript build | the README sequence (pdflatex, bibtex, pdflatex ×2) into ignored `local-output/` | 14 pages, with no LaTeX/BibTeX warnings and no undefined references. TeX Live 2023 here; the developer used 2025/dev. Page 1 was inspected visually. |
| Primary source | arXiv 2202.13691v3 (An–Wu), §2 and Cor. 4.1 | Confirmed: η∈[0,1) is assumed; Thm 2.2 has the factor 1/√(1−η)+1; §4 *assumes* η=3/4 for CC; Cor. 4.1 covers m-point CC with n+2≤m≤2n+1 and gives the bound 3√V E_{m−1−n}. So m=513, n=511 is the boundary case m=n+2. The manuscript and LIT-046 are accurate. |

Committed auditor evidence: the checker `tracks/mz-constants/evidence/claude-audit-01-check.py` (8,768 B, SHA-256 `5c75cb8d62b3d8100595fa2dfb929f754e686d168e9a8232e91ae424cc24e546`) and its output `claude-audit-01-check.json` (7,767 B, `8cd7499032d311726131d71439640e10d988dbc499cff6275488296e5798e904`). The checker writes nothing into the tree; its output was redirected.

## 2. Mathematical reconstruction (handoff items 1–7)

Each item was re-derived from the definitions and not from the developer's prose. "OK" means the stated hypotheses, quantifiers, constants and status are correct.

| ID | Claim | Points re-derived | Result |
|---|---|---|---|
| PD-T013 | Exact CC weights, aliasing, defect sign | Discrete orthogonality with γ_0=γ_N=½; the cardinal expansion; the even-N half term cos(Nθ)/(N²−1) as the halved r=N/2 term; endpoint brackets 1/N and N/(N²−1); D_ij=2/(r²−1)−2/(s²−1)>0 exactly for even s>N, n≤N−1 | OK |
| PD-T014 | 0<Q_N(p²)≤(2−2/(πN))∫p² on Π_{N−1} | The A=2M−R entry formula (2); r−d=2(N−max(i,j))≥2; the |a|-replacement inequality; the floor chain v^TMv≥N^{-1}a^TEa≥(2/πN)a^TMa | OK, but the constant is dominated (M1) |
| PD-T015 | N^{-1}E⪯M⪯(π/2)E | Zero infinite row sums (Σ_{h∈2ℤ}μ_{|h|}=0); tail start m_i with parity of i and m_i−i≥2; telescoping to (2); the Gershgorin-type identity; ∫q²sinθ≤∫q² | OK |
| PD-T016 | T_N quotient 2(4N²−1)/(4N²−2)>2 | Direct | OK |
| PD-T017 | ∫p²≤K_N Q_N(p²) on Π_N | Fourier series of (π/2)sinθ; tail bounds; worst case 2/3 at N=2; endpoint c_k=2 cardinal factor; sinθ≤2sin((θ+θ_k)/2); min(π,1/u)≤(π+1)/(1+u), with equality at u=1/π; cell factor 2; cell mass π²m_j/N²; row bound m_j≤m_k+|j−k| giving A_jk+1/m_k; column bound h_N; Schur product | OK (proves λ_min(CC,N)≥1/K_N, stronger than stated) |
| PD-T018 | λ_min(N,N−1)≤128000/(log N)² | Degree, parity and endpoint cancellation; identity (1); interior nodal values; Abel tail ≤1; head bounds 2Kθ≤π and H_K; C_M≤3+logπ−log(Nθ) with M+1≥N/2; Q≤125H_{⌊N/2⌋}; on E=[N^{-1/2},1/4], C_M≤−L/4 once L≥20; the IBP bound 1/(N·N^{-1/2}); I≥L/8; J≤L; L²≥12800; small-L fallback λ_min≤1 | OK (non-vacuous only for log N>357; see L2) |
| PD-T019 | Exact U_{N−1} norms | U_r²=ΣU_{2s}; ∫U_{2s}=2/(2s+1); endpoint values ±N | OK (also exact-checked N≤60) |
| PD-N004 | η_512>3/4 | S_8>201/100; integral comparison; e≤87/32; (11/4)^4<1025/17; 4·512²/(512²−1)<401/100 | OK; the refutation scope is correctly limited to N=512 |
| PD-N002/003/005/006 | Scoped failed mechanisms | The 2×2 minor for N≥5 and the N=3,4 rank-one remark; the N=5 row (−2/3, 14/15, −34/105), margin −2/35; ∫|ℓ_0|=1/N; top DCT coefficient (1/N)Σ″(−1)^k v_k | OK; statuses PROVED and dispositions correctly scoped |
| PD-T021 | Padua marginal 2w_CC and compression | The univariate cardinal argument; the isometry J; Q^P[(Jp)(Jq)]=Q_N(pq) uses only nodal values, so no extra exactness is assumed; signed weights are allowed | OK (also checked numerically, §1) |
| PD-T022 | λ_+≤1+max(2n/N−1,0)² | The aliased entry; d/r≤1−2δ/r≤1−2δ/N=t; (d²−1)/(r²−1)≤d²/r²; strictness from −(1+ρ)/(s²−1) | OK (exact-checked N≤60) |
| PD-T023 | λ_−≥(1−n/N)²/C_* | Fejér coefficients; plateau through \|k\|=n; degree N−1; no alias since \|l−k\|≤n+N−1<2N; the n=0 convention; mF_m≤min(m²,π²/d²); \|K\|≤C_0N/(ε(1+Nd)²) with C_0=2(1+π)²; ν 1-Lipschitz; shells of at most 2 nodes; Σ_k(1+kπ)^{-3/2}≤1+2/π; column integral 2C_0/(εN); (9)–(10) with the endpoint overcount | OK |
| PD-T024 | Fixed-θ strong constants | Combination; n≤θN<N | OK |
| PD-T025 | Upper-Gram hyperinterpolation bound | Weighted Cauchy–Schwarz duality; L_n r=r for r∈Π_k, k≤n; exactness of products of degree ≤n+k; CC k≤min(n,N−n) | OK; the generic mechanism is correctly labelled known context (ASV) |
| PD-T020/027/028 | OPEN targets | Statements and the distinction from the comparison theorems | Correctly OPEN; not hidden by administrative status (but see L1) |

Handoff items 1–7 are all confirmed:
- (1) N indexes N+1 nodes, the ADE is N or N+1, and full degree T_N exceeds 2.
- (2) D is entrywise nonnegative but not PSD.
- (3) The all-N weight bounds and the Schur normalisations hold.
- (4) The U witness is admissible, the endpoint cancellation and sine/cosine bounds hold, and the L≥128 split with its small-N fallback is correct.
- (5) The Fejér plateau, the no-alias range, the n0 convention, the shell counts and the half-circle factors hold.
- (6) An–Wu is conditional (verified against the primary text). The N=512 case is the boundary m=n+2, and the ordinary quadrature hyperinterpolant is distinct from inverse-Gram least squares.
- (7) η_CC→1 does follow, since 1−λ_−≤η<1 with λ_−→0. However, it gives no rate for 1−η, and the Padua result is only a liminf.

No status upgrade or downgrade is required by the mathematics.

## 3. Findings

### M1 (Medium) — The fixed-ratio theorem PD-T022 strictly improves PD-T014's headline constant; the registry and manuscript present the weaker bound as the explicit result

Locations:
- `m1-upper-bound.md` (statement (1));
- `manuscript.tex:43` (abstract), `:116` (eq. main-upper), `:255-258` (Theorem 2.3), and `:774-775` (eq. Bcc);
- `report.md:10` (rank 2);
- `m3-hyperinterpolation.md` (definition of B);
- `paper/README.md` scope table.

Evidence. At n=N−1, PD-T022 gives ρ=(1−2/N)², so
λ_+(N,N−1) ≤ 1+(1−2/N)² = 2−4/N+4/N².

For every N≥2, 4/N−4/N² > 2/(πN), because 4−4/N ≥ 2 > 2/π. So PD-T022 is strictly stronger than PD-T014's 2−2/(πN) at every N. For example, at N=3 it gives 1.111 against 1.788. The auditor checked this inequality numerically for N≤10⁴ (`M1_T022_strictly_below_T014_all_N2_10000: true`) and analytically as above.

Consequences:
- The min in PD-T025's B and in manuscript eq. (Bcc) always selects 1+ρ.
- PD-T015's only use, the quantitative constant in PD-T014, is superseded.
- No record notices this. A search for 4/N, (1−2/N), "supersed" and "dominat" across directions, theory, report and the Astra audit found nothing relevant.

Nothing stated is false. The issue is that the package's ranked result #2 and its abstract present a dominated constant, and PD-T015 is classified as a substantive supporting result whose role is now only an alternative proof. A referee would notice this immediately.

Requested disposition (developer's choice of wording):
1. Add to PD-T022, or as a corollary in PD-T014 citing PD-T022, the explicit endpoint bound λ_+(N,N−1)≤2−4/N+4/N². Use it in the abstract, eq. (main-upper), the report and README rankings, and PD-T025's B (which simplifies to 1+ρ).
2. Keep PD-T014 as the strict qualitative threshold with its own short sign proof. Either retain PD-T015 explicitly as an independent supporting inequality, or record why its classification changes. That is a classification decision for the developer, which the auditor will check.
3. The added corollary is a new claim and needs a focused re-audit.

### M2 (Medium) — Unscreened prior-art family directly relevant to PD-T017/PD-T018: weighted mean convergence of Lagrange interpolation and converse quadrature-sum inequalities with mismatched weights

Locations: `literature-search.md` (43 queries); `literature/records/mz-classical-mz-screen.md`; manuscript §1 "Attribution and coverage limits".

Evidence:
- The search and records cover three sources only, at abstract or metadata level: Lubinsky–Máté–Nevai 1987, Mastroianni–Totik 2000 and the Lubinsky 1998 survey.
- No query or record covers the classical literature on weighted L^p convergence of Lagrange interpolation at Jacobi/Chebyshev-type nodes. That literature includes Erdős–Feldheim (1936), Askey (1972), the Nevai series (in particular *Mean convergence of Lagrange interpolation. III*, Trans. AMS 282 (1984), which gives necessary and sufficient conditions for generalized Jacobi nodes), and follow-up work by Mastroianni–Russo, Xu, Lubinsky and others.
- That literature studies exactly inequalities of the form ∫|L_N f|^p u ≤ C Σ_k λ_k |f(x_k)|^p (u/w)(x_k), and their failure.
- PD-T017 on Π_N is the classical setting: the full interpolation space, the Lebesgue weight u=1, and nodes of Chebyshev–Lobatto type. The endpoint logarithm is the typical borderline behaviour of Askey–Nevai-type conditions.
- The auditor's own targeted search (2026-10-31) reached abstracts only. It found neither a matching statement nor an exclusion. For example, the Nevai III abstract states necessary and sufficient conditions but no constants, and the Lubinsky converse-MZ preprint (lubinsky.math.gatech.edu, paper 147) covers A_p weights without a borderline log statement.

This is not a validity issue, and the package already declares novelty unresolved. However, the named threats in the manuscript and report do not include this family. It is the most likely place for an equivalent or stronger form of PD-T017, and possibly PD-T018.

Requested disposition:
- Add this family to the M0 record as a named pending-reference gap, with the specific papers.
- Run a short targeted screen (Nevai 1984; Askey 1972; Lubinsky's converse-MZ papers for Lobatto nodes) before any wording beyond "self-contained proof".
- Add it to manuscript §1's threat list.
- An explicit "unresolved, named" disposition is acceptable for PR readiness. Silence is not.

### L1 (Low) — Stale conditional in PD-T028

`open-padua-target.md`, "Proof or evidence", says that compression gives liminf η_Padua ≥ 1 "once the CC endpoint convergence is established." That convergence is already established: PD-T021 proves the liminf unconditionally from PD-T018, and the manuscript states it unconditionally. Reword so that the open file does not suggest that a proved consequence is conditional.

### L2 (Low) — State the non-vacuity range of PD-T018 and how the finite tables relate to the log⁻² order

The witness is used only for log N ≥ 128. The explicit bound 128000/(log N)² is below 1, and hence informative compared with the trivial λ_−≤1, only for log N > 357. In other words, the comparison constant is vacuous for every computable N. This is correct mathematics, but neither the theory file nor the manuscript says it. "Loose" understates it.

Separately, the measured λ_−·(log N)² rises from 3.53 to 6.02 across Table 1 (N=40…1280). Read at face value, the table does not display a log⁻² law.

The auditor's MEASURED diagnostic (`M3_fits` in the evidence JSON) shows that the data are nevertheless consistent with the proved order:
- c/(log N+b)² with c≈13.25 and b≈3.45 fits N=40…1280 within 0.17%;
- fitted on that range, it predicts the auditor's new N=2560 and 5120 values within 0.32% and 0.49%;
- the best a/(log N+b) law misses by 3.5% in-sample and by 6.2–9.3% out of sample.

Requested: one sentence in PD-T018 and in manuscript §3 or §6 stating the vacuity range, and that the finite values do not exhibit the asymptotic constant. Optionally cite this diagnostic as a MEASURED note under PD-T020. It is *not* an estimate of c_*, because the slow-shift fit is model-dependent.

### L3 (Low) — PD-T017 states a weaker consequence than it proves

The theorem bounds ∫p² on Π_N. Its "Consequently" line gives λ_min(CC,N−1)≥1/K_N, while the proof gives λ_min(CC,N)≥1/K_N (Gram on Π_N). The manuscript has the same wording. This is harmless, but stating the full-space consequence makes the comparison with the classical interpolation literature in M2 cleaner.

### Informational

- I1. Reproduction is exact: 637/637 numeric fields are bitwise equal to the developer's JSON, and the M1/M2/M3 outputs are identical to Astra's replays. This is the auditor's own execution, not a reading of earlier output.
- I2. An–Wu has been verified against the primary arXiv v3 text (§1). The manuscript's description and the m=n+2 boundary are correct. The published-version comparison stays pending, as recorded.
- I3. Manuscript §6 checks Padua marginals at construction degrees 10, 20 and 31, while Table 2 uses 10, 20, 30 and 40. This is consistent with `reproduced-spectra.md`, but a reader may take 31 for a typo. Consider adding a parenthetical "(odd and even)".
- I4. The pending-review wording inside the theory files (for example, "Runs needed: independent Astra…" in PD-T018/PD-T026) is covered by each file's dated review-update header. This is acceptable under the no-silent-rewording rule; no action is needed.

## 4. Novelty and candidate discipline

The full IDEAS.md read covered seeds IDEA-052…059, local IDEA-060…076, the seed disposition table and the MZ obstruction table. Every PD-N file corresponds to a retained IDEA with a scoped disposition: IDEA-060→PD-N002, 061→PD-N003, 068→PD-N004, 069→PD-N005 and 070→PD-N006. Equivalent or known-context candidates (IDEA-072 marginal, IDEA-075 generic upper-Gram) stay IDEA dispositions without PD-N files, as AC's L5 decision requires. The deferred targets M4–M6 are retained with resumption conditions and are not falsely rejected.

The separation criteria and kill tests in M3/IDEAS.md were checked against the proofs. The IDEA-073 kill test is correct, but its separation statement ("variant with a specified quantitative difference from M1") should now also record that it dominates IDEA-063's quantitative role (see M1).

No novelty claim is made anywhere, and the auditor makes none. The historical-overlap risk is high for M2's order theorem (see audit M2), and moderate for M3, where classical filtered/de la Vallée Poussin reconstruction and weighted MZ apply.

## 5. Protocol, registry and allocation

Verified by the auditor directly:
- `protocol-check.py` reports 86/86 manifest entries current at `fdf0648`, with 21 source entries verified. The registry counts (PD-T 16, PD-N 5) and status counts (17 PROVED, 3 OPEN, 1 MEASURED) agree with the theory-file headers read in §2.
- The largest committed public file is 67,983 B (`batch-registry-resolution.patch`). The conservative public total is 864,564 B, within the 1 MB per-file and 5 MB total limits.
- No third-party fulltext is tracked: `sources/.gitignore` excludes `notes/` and `reports/`, and the auditor restored them only locally, from the hash-verified zip.
- The only broken local link is the ignored PDF, which is expected.
- Windows cold-storage delivery for the developer's artifacts remains pending, as `cold-storage.md` states. The auditor did not attempt it, because those artifacts exist only in the developer's workspace.

**Delegated registry/ledger review.** A separate Claude subagent (Opus 5.5) ran this review read-only at `fdf0648`. The auditor re-checked P1, P2, P3, P6 and P8 directly (the commands are noted in each), and accepts the subagent's results as listed. Severity uses this report's scale.

### P1 (Medium; blocks readiness) — Two different ledgers exist at the shared path `topics/padua-batch-20261031/ALLOCATIONS.md`

The two versions:
- **This branch's ledger** names the "root Codex MZ orchestrator" as allocation owner. Its member table lists the charter, MZ and Lanczos only.
- **`claude/programme-ideas-20261031`** (head `a02bc35`, commit `8f500db`, 20:57 UTC) independently created a ledger at the same path. It declares itself the single ledger, uses a different owner rule ("whichever member branch next reaches PR preparation…"), and still lists MZ as "Provisional IDs only… pinned `e9761aa`".

Auditor check: `git merge-tree --write-tree --name-only origin/claude/programme-ideas-20261031 HEAD` gives `CONFLICT (add/add)` on that file.

No final ID collides yet; programme-ideas uses only provisional labels. However, WORKFLOW requires one ledger and one owner, and conflicting reservations must be resolved before any affected PR becomes ready.

Requested:
- Reconcile into one ledger with one recorded owner.
- Add the programme-ideas member row.
- Record that the next free ranges are PD-T029, PD-N007, LIT-061 and IDEA-077, after MZ.
- Propagate the reconciled ledger to every member branch.

### P2 (Low) — PROOF_STATUS rows use placeholder text

`PROOF_STATUS.md:9–29`:
- Every MZ row's "Depends on" reads "explicit local dependencies in file".
- Every "Status by mathematical part" reads "exact statement in canonical theory".

The theory files list real dependencies, for example PD-T014→PD-T013/015, PD-T024→PD-T022/023 and PD-T021→PD-T018/PD-N004.

Auditor check: `sed -n 9,29p PROOF_STATUS.md`.

Requested: put the ID lists in the column, as PR #2's rows do. Readers are told to check the registry before using a row as a dependency.

### P3 (Low) — Dispositions are missing from PD-N rows and from `state/IDEAS.md`

- The PD-N rows (`PROOF_STATUS.md:25–29`) read "scoped mechanism failure/refutation; see theory". They should name what was killed, for example "IDEA-060 REJECTED: refuted (see PD-N002)". The full set is 060 refuted, 061 failed, 068 refuted, 069 failed and 070 failed.
- `grep -c REJECTED state/IDEAS.md` returns 0 (auditor-checked). IDEA-060…076 are link stubs. The seed disposition table still shows IDEA-053/054 as "active" and IDEA-055 as "deferred", although they are developed and PROVED.

Requested: add a current disposition table for IDEA-052…076 to `state/IDEAS.md`, using the allowed vocabulary. IDEA-064, 067 and 072 are "equivalent" while supporting PROVED results, so state whether that is an IDEA disposition or a known-mechanism note. No candidate was dropped: all 65 provisional labels are mapped.

### P4 (Low) — Split-from / split-into links do not reciprocate

- PD-T019's split into PD-T018 and PD-N004 is not mirrored in their headers.
- PD-T027 and PD-T028 cite filenames, not PD-T014 and PD-T021.
- PD-T015 does not name PD-T014 as its parent.

`ID_CROSSWALK.md:77–80` is consistent with the intended structure. Requested: use IDs, and make each pair point at the other.

### P5 (Low) — Registry rule text is lost on integration

The branch deletes main's four-paragraph PROOF_STATUS preamble, including the `REJECTED: refuted (see PD-Nnnn)` convention. PR #2 also replaces it, so after both are integrated the rule text is gone. After integration, both the patched PROOF_STATUS (lines 3 and 23) and ID_CROSSWALK (lines 3 and 130) also claim different single ledgers.

This is a registry-documentation change that needs AC's awareness and a fix during ledger reconciliation (P1).

### P6 (Low) — Stale pins

- `LOG.md:7` still says "no IDs reserved yet" (auditor-checked).
- The ledger, `final-id-map.json` (`competing_pr2_head`) and `batch-rehearsal.json` (`charter_source`) all pin PR #2 at `eb7bdcd`. PR #2 is now at `3bd9d4e` (auditor-checked with `git rev-parse`).

The shared-registry blobs are identical at both heads, so the rehearsal still holds. Requested: refresh the pins, and re-rehearse after PR #2's response.

### P7 (Informational) — Formatting, PR wording and template deviation

- Missing spaces glue numbers and hashes to words in `integration-impact.md:3,9,11` and `state/IDEAS.md:275–277` (for example "SHA256654f052a…"). This makes copy errors likely.
- PR #3's body says "No merge sequence is requested now". It needs an explicit decision request to AC at readiness.
- `cold-storage.md` uses SHA-256 plus the base SHA instead of the template's blob IDs, and says so at line 10. This is acceptable.

### Verified clean (subagent; P-checks re-run by the auditor where noted)

- **Theory headers.** All 21 header IDs and statuses match PROOF_STATUS.
- **Crosswalk.** 65/65 crosswalk rows match `final-id-map.json`, with no duplicate finals. All 19 LIT IDs appear in INDEX and in their records.
- **Ranges.** The MZ ranges (PD-T013–028, PD-N002–006, LIT-042–060, IDEA-052–076) are disjoint from PR #2's ranges, and nothing is renumbered.
- **Rehearsal.**
  - `merge-tree` of PR #2 (both heads) against MZ gives exactly the 9 conflicts recorded in `batch-rehearsal.json`; main+MZ is clean.
  - The resolution patch's pre-image matches, its SHA-256 and size match the record, and a dry-run application produced the recorded post-image blobs.
  - The result has 34 unique PD rows and no conflict markers.
- **Hashes.** `audit-targets.json` pins 123/123 files, all matching by SHA-256 and size.
- **Evidence.** Every committed evidence file matches a manifest entry.
- **Commits.** All 7 commits carry `Agent:`/`Model:` trailers, and no rule, agent, template or `.github` file changed.

Not checked:
- the local-only rehearsal commits `be1665d` and `b21e395` (their results were reproduced independently instead);
- Windows delivery;
- when the programme-ideas ledger was pushed relative to the MZ allocation.

`claude/bivariate-lanczos-20261031` will conflict textually with MZ in `literature/{CORPUS,INDEX}.md` and `state/IDEAS.md`; it has only provisional IDs.

## 6. Remaining uncertainty

- The auditor did not read the 13 KB of direction records for M1/M2 line by line beyond the parts the theory files cite. The proofs were reconstructed from the theory files and the manuscript, which are the durable records.
- Historical fulltexts (Sloan–Smith, Mastroianni–Milovanović, the classical MZ and interpolation papers) were not inspected. The novelty status remains unresolved.
- Windows cold-storage delivery is not attested by this audit; see §5.
- The auditor's numerics are floating MEASURED values, except the Fraction checks E2–E4, which are exact finite instances. None is used as proof of a universal statement.

## 7. Requested next step

Stage returns to **WORK**. Codex answers M1, M2, L1–L3 and P1–P6 in `response-01.md`, without editing this report. M1's corollary is a material addition; the auditor will re-audit only the changed statements and files. M2 can be closed by a named, recorded pending-reference disposition. Only AC merges.
