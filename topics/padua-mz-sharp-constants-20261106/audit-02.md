# Claude audit-02 — focused audit of response-01 and closing development P1–P4 (draft PR31)

- **Decision: the mathematics and every computer-assisted certificate are ACCEPTED at their stated scopes. Stage → WORK** for a bounded records response to two MAJOR findings, B1 and B2. No finding is BLOCKING.
  - **P3 is ACCEPTED as PROVED:** lim (log N)²λ_min(CC, Π_(N−1)) = π⁴/8, also on Π_N, through all integers N and on both parities. Two independent subagent reconstructions and my own pass all reached this verdict separately.
  - **P1 is ACCEPTED as PROVED:**
    - the elliptic kernel equals the product-cutoff norm limit B;
    - c_minus = −‖B‖ with a simple positive ground state, and 0 < c_plus < ‖B‖;
    - the rectangle reduction;
    - the computer-assisted coarse enclosure −0.47780927999… ≤ c_minus ≤ −0.01316494650…, which certifies no useful digits.
  - **P4 is ACCEPTED as computer-assisted PROVED:** Λ_edge ≥ 1.0044369. B2 asks for one theory record of the closed-form dependency.
  - **P2 is ACCEPTED as MEASURED (PASS_FINITE_TEST), with B1's scope correction.**
  - **Response-01:** A1–A13 are adequately answered, and A3 is correctly left for AC.
- **Audited input:** `2429e750cedb18b0a7903e7ed10dd3296a181204` (handoff 04). Head at audit start: `0e7be6e7c16dd30791d44268ff5d3cfc1d2e2bf9`. `git diff 2429e75 0e7be6e -- theory code evidence` is empty.
- **Rules and base:** rules read at `0e7be6e` (`AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md`, `templates/HANDOFF.md`); they are unchanged from main. Main `76ba421`, refetched and unchanged.
- **Auditor:** Claude, configured `claude-opus-5-5`, xhigh. This was required because the audit covers a new sharp-limit proof, new certificates and changed dispositions. No serving-model receipt is exposed. I am distinct from every Codex developer and every Astra checker.
- **Subagents:** five supplementary Claude Opus 5.5 xhigh subagents, without Git authority or repository edits:
  - P3 (A) and P3 (B), run independently; B reconstructed the proof before reading any check;
  - P1;
  - P2 and P4 with reruns;
  - records, response and novelty.

  Their outputs are in [audit-02-support](audit-02-support/); the harness blocked subagent report files, so their reports were returned to me and are summarized here.
- **Role:** auditor, and topic orchestrator for this step. I edited no developer file.

## Coverage

**Handoff and response.** Handoff 04; `response-01.md`; `independent-checks-response-01.md` (head); `audit-01.md`; the full non-P diff `0205690..2429e75` (S1/S2/S3 theory and idea edits, report, gates, LOG, manuscript-insert, literature-screen, rounds, results file, cold-storage files, `evidence_manifest.py`); the new MEASURED records S1/S2/S3-measured.

**Novelty.** `state/IDEAS.md` is byte-identical to the version read in full for audit-01: `git diff f8942ec 0e7be6e -- state/IDEAS.md` is empty, so that full read still covers it. The records subagent read `novelty-gate-P1.md` through `P4.md` and all P1–P4 idea records. It grep-checked the closest predecessors IDEA-058, 065–071, 385/386, 420, 466 and 469–471, plus terms for Hardy, sinc, Plancherel, Schlömilch, Schur and interval certificates. No priority claim is made in the topic.

**Theory, read in full** (SHA-256 at `2429e75`):

| File | SHA-256 |
|---|---|
| `theory/P1-elliptic-kernel.md` | `c7786f149135cdf839288a280f5946445c51d01a928e37760b14ea1a1c1b56f2` |
| `theory/P1-positive-spectrum.md` | `4a1e0fe2b3db1e6a8ad19e0a1607d3aace86b9aa3c208d09305aeda49570e64b` |
| `theory/P1-rectangle-certificate.md` | `4cee5449c0b1634e4d868a41c474b0c938a5394bc87e8f45e197219508a911a9` |
| `theory/P1-numeric-certificate.md` | `6d27f3c92789e973495d79853924d1c7a2b52669705500aebf7f8d359fe939ee` |
| `theory/P2-measurements.md` | `8855950157467ac74bba3758b606b7fc756a317c56e46ffedbb77d7a7b7c9f4d` |
| `theory/P3-signed-remainder.md` | `17f357a92a448ef2ad49d406111dcd0d7ce57de8519dc712424ae6f9eb4d29ed` |
| `theory/P3-discrete-primitive.md` | `bf0a471590f2b8a385a98bad3df9f4d440f009590099401b6a64dc8a894efb44` |
| `theory/P3-reverse-bound.md` | `fdcdd0e67531344b371e4a2de621a2368ff61473566653686b9466fb08738101` |
| `theory/P4-certified-lower.md` | `c7e001e13272ac95f450d16a72cb3e50756b3a2fc3e8f906b5bfd92b83527135` |
| `theory/S1-measured.md` | `91ee8a6974cd7052ed2d223205665a58b20502ceb4c4f11610d9c5248ae64f1c` |
| `theory/S2-measured.md` | `8332dc4a41cb67bed7a557c9ffc663575b0dc2273d98910eefe7c8ce643f6505` |
| `theory/S3-measured.md` | `08416e4e32237946a70dac354983a586acbdca9bc607c3a1d992d3248eb8fd29` |
| `response-01.md` | `d8bbb0a8f2c2ab69dfa4ae60f1703836699e142afc6cf6989a1be62a3ef50f3f` |

**Code and evidence.** Read and executed by the P1 and P2/P4 subagents: `P1_rectangle.py` and `interval_dyadic.py`, line by line; `P4_rayleigh.py`, `P4_check_grouped.py`; `P2_modes.py`, `P2_summary.py`, `check_P2_summary.py`; the P1/P2/P4 receipts. Dependencies read: PD-T017 (`m2-cardinal-lower.md`), PD-N005 (`m2-l1-obstruction.md`), PD-T013, and S1-01/S1-02 (already accepted).

## Claim-by-claim reconstruction

**P3-01, the signed remainder (‖E‖ ≤ 40): PROVED, accepted.** I checked this myself, and both P3 subagents checked it separately.
- B_k = 1/[2(t−k)] − 1/[2(t+k)] + 1_(k>t)/k.
- The sine turns each pole into (π/2)(−1)^k sinc(t−k).
- On a fixed dyadic block, dt/t ≤ dt/d ≤ 4dt/k. So exact sinc orthogonality is used only where the weight is nearly constant. Signs are retained throughout; the PD-N005 absolute majorant is never used.
- The comparable-scale constants hold: |D_k| ≤ 9/(2t), Σk ≤ 12d², 243 and 972 log 2 < 32². The separated-scale Schur bounds hold: rows ≤ 5/6, columns ≤ 1/3.
- Each k lies in at most three J_j (the file's four is safe).
- **Measured worst-case norm:** about π/2, flat in support length and location; the claimed bound is 40.

**P3-02, the discrete primitive: PROVED, accepted.**
- The harmonic-cell embedding with ‖Z−F‖² ≤ E/3 checks, as does the rescaled Volterra norm 2H_J/π.
- So do the cell oscillation bound ½log(1+1/m) + 1/(4m²) and Σ|S_m|²/m² ≤ 6E.
- **Measured worst-case:** 0.20265·H_J² against (2/π²)H_J² = 0.20264·H_J² at J = 10⁶, under the stated bound.

**P3-03, the reverse bound and the limit: PROVED, accepted.**
- **Cardinal/cotangent split (5):** signs, the c_0 = c_N = 2 factors and the homogeneous coefficient 2t sin(πt)/π all check. |e| ≤ 1+4/(3π) on [−π, 3π/2].
- **Bounds (6) and (8):**
  - Σ1/w_k ≤ 2N²(L+1) from w_k ≥ (1+d_k)/N². I checked numerically that min N²w_k/(1+d_k) = 1.000 (N ≤ 5000) and max N²|w_k − (π/N) sin θ_k| = 0.35 ≤ 3.
  - The cross-edge term gives (9π²/32)(L+1).
- **Good layers (9)–(11):** π⁴/6 + 3 ≤ 2π² checks.
- **Microscopic cells and endpoint columns (12)–(15):** check.
- **Bulk (16):** the DCT-I trapezoid identity, dx ≤ dθ and sin θ_k > 2/L give the bound, and the central node is included.
- **Assembly:** good, microscopic and bulk groups partition all nodes, and the D_N arithmetic checks. C_N/L → 2√2/π², so ‖p‖² ≤ (8/π⁴)L²(1+o(1))Q on Π_N.
- **Squeeze with S1-02:** (π²/2)(π/2)² = π⁴/8, and λ_min(N) ≤ λ_min(N−1).
- **Scope:** no parity dependence and no exchange of limits.
- **Worst-case piece norms at actual CC weights** (N = 256…8192, both parities, the proof's own K and M):

  | Piece | Measured | Claimed bound |
  |---|---|---|
  | Signed error | ≈ 1.0 | 80 |
  | Cross-edge | ≈ 0.18 | ≈ 5 |
  | Cotangent | ≈ 0.27 | ≈ 8 |
  | Bulk | ≈ 1.07 | √(πL/2) |
  | Endpoint pair | ≈ 2.2 | 10√(L+5) |

  The primitive-part norm divided by L rises from 0.271 to 0.277, toward 0.2866. A control test that scales the primitive by 0 or 2 makes the remainder grow like L, so the decomposition test does discriminate.
- **Consistency with the data:** the evidence fits 1/√λ ≈ (2√2/π²)L + 0.84, which reproduces the slow observed approach ((log N)²λ_min = 7.756 at N = 102400).
- **Effectiveness:** the explicit finite bound (2) is valid only for L ≥ 16 and is vacuous at reachable N. The record claims no rate.

**P1-01, the elliptic kernel: PROVED, accepted.**
- The steps run in this order:
  1. Norm convergence B_K → B.
  2. On C_c^∞(D), integration by parts with the radial Laplacian makes the coefficient series absolutely summable, so product-truncated, full and Abel-damped sums agree.
  3. Exchanges at fixed ρ are absolute.
  4. ρ → 1 by positive Poisson regularization and L¹ convergence.
  5. The closed-form operator is bounded (Schur bound 32/π²).
  6. Uniqueness of the bounded extension gives B = C.
- The j+k-even split is termwise exact, and e_0 = 1/2 is the constant Fourier term.
- **Floating checks:** the closed forms match quadrature to about 1e-12. The full row integrals match an absolutely convergent Bessel series to about 1e-11, which independently confirms e_0 and the factor 2 in S_alt. Inner-cell Galerkin spectra approach −0.1336 and +0.0456.

**P1-02, positive spectrum: PROVED, accepted.**
- The kernel vanishes identically on {a+a' < 1, b+b' < 1}. This contains R×R with R = (0, 1/2)², about 37.5% of D's mass.
- The file states this and correctly proves A²f > 0 a.e. instead of pointwise positivity, via the wedge near (1,0).
- **Consequences, all of which check:**
  - |v| attains the top Rayleigh value, so c_minus = −r;
  - A²u = r²u gives u > 0;
  - the eigenspace of A² is one-dimensional, which also excludes −r and so gives c_plus < r.
- c_plus > 0 is inherited from S3-03 and PD-T379.

**P1-03 and P1-04, rectangle reduction and coarse certificate: PROVED (computer-assisted), accepted.**
- **Reduction:** I_t (with κ_1 = 2), E ≤ √(v²−u²)/π, P_R as an upper bound on crossing rectangles, the outer and inner cell covers, the weighted Schur upper bound U, the Rayleigh lower bound L, and ∫_D ab = 1/24 all check.
- **Arithmetic:** pure integer dyadic arithmetic with directed rounding. The Machin π sign is handled, the cosine Taylor tail is valid, and both clipping steps are justified. No elliptic function is evaluated.
- **WORKFLOW computer-proof requirements:** met. There is a proved reduction, exact arithmetic, a committed checker and evidence, and independent reruns by the distinct Astra checker and by this audit.
- The certificate is coarse: L is about 6 times below the floating Rayleigh value. The record correctly claims no digits.

**P4: computer-assisted PROVED, accepted; B2 records issue.**
- **Reduction:** S2-03 defines Λ_edge as a supremum over finite trials, so the exact finite trial gives a valid lower bound. The numerator is exactly 4(Σs_ju_j)² + Σω_ju_j²; the denominator is the closed form C, with a positive enclosed lower endpoint.
- **Trial parsing:** the exact hex trial is parsed through `float.fromhex` and `Fraction`.
- **Scalar enclosures:** Machin, the Si/Cin Taylor tails, the Laplace F/G remainders (40!/x⁴¹ and 41!/x⁴²), Euler's constant cancelling through the Cin(16π) anchor, and the atanh log tail all check.
- **Arithmetic:** outward floor/ceil rounding, including division by a negative integer.
- **Independent checks:** the closed form C was re-derived by hand. An mpmath evaluation at 60 digits gives q = 1.00443691886466728…, inside the dyadic enclosure. A quadrature of ∫t g² dt without the closed form matches it to 1.4e-13, so the margin of 1.9e-8 above 1.0044369 is robust.

**P2: MEASURED, accepted with B1.**
- **Publication order:** the protocol (d03e74d) precedes the code, the Step-1 receipts and the measured b₂ (64f3b76), which precede the summary code (c1e6e59), m1600/1601 (0d97ed6) and m3000/3001 with the summary (2429e75). The protocol blob is unchanged, and P2_modes.py has one version since 64f3b76.
- **Thresholds and criteria:** the summary uses exactly the registered thresholds. The summary bug was fixed before the first commit of `P2_summary.py` and before any main receipt.
- **Controls and labels:** the synthetic controls pass 10 of 10. The audit400 row is correctly labelled an implementation replay. No two-term asymptotic, crossing-degree or K4-revision claim is made.

**Response-01: A1–A13 accepted.**
- Every fix is present, and K0–K5 text is byte-identical in the first 78 lines of `gates.md`, with addenda below.
- Edits to accepted proof files change only wording, citations and pointers. The one exception is the S2-03 status-line removal requested by A5, which leaves no status label (C2).
- The new MEASURED records match the evidence: K1 13.0611359933 / 13.0611326732, K3 1.00443697229…, J512 1.0044369188646673, the K128 extrema and all 16 Padua minima.
- `17ca9f4` (R) precedes every P1–P4 file.

## Actual executions (this audit)

All runs used single-thread BLAS, Python 3.13.18, NumPy 2.5.3 and SciPy 1.18.1; the developer used 3.12.14 / 2.3.5 / 1.17.0. Total about 0.3 CPU-h. There was at most one heavy process at a time, and no Syvert run, upper Padua run or registered-threshold change.

1. `evidence_manifest.py --checks` at `0e7be6e`: exit 0, 90 identities, 77 JSON, 357 local links, 0 missing. It now fails at this audit's output commit because of `audit-02-support/*.json`; see C1.
2. **P1 certificate:**
   - `P1_rectangle.py --N 16 --theta 256` and `--N 8 --theta 64` give interval endpoints bit-identical to the committed and independent receipts ([P1/](audit-02-support/P1/)).
   - The code, protocol and reduction blob hashes at c1e6e59 equal the receipt records.
   - `indep_check.py` (floating, MEASURED) checks the closed forms, row integrals, inner-cell Galerkin spectra and certificate consistency.
3. **P4 certificate:**
   - `P4_check_grouped.py` with the handoff arguments: exit 0, integer endpoints identical to `P4-grouped-check.json` and `check-P4-independent.json`.
   - `P4_rayleigh.py` to scratch: identical to `P4-rayleigh.json`.
   - Own `p4_independent.py`: mpmath at 60 digits plus pole-centred Gauss quadrature with an analytic tail bound ([P24/](audit-02-support/P24/)).
4. **P2 reruns:**
   - `P2_summary.py`: identical apart from the command field.
   - `P2_modes.py validate`: bit-identical error values, in 0.39 s.
   - `P2_modes.py run --m 1600`: 124.4 CPU-s. Q_min, weights and compressions agree within 3e-13, and re-summarising with this m1600 still gives PASS_FINITE_TEST.
   - Synthetic controls on a disposable copy: 10/10. The original receipt is preserved.
   - `p2_preexisting_predictivity.py` (see B1).
5. **P3 numerics:**
   - P3 (A): `p301_remainder.py`, `p302_primitive.py`, `p303_cc.py`, `p303_groups.py`, `p303_discrim*.py` ([P3a/](audit-02-support/P3a/)).
   - P3 (B): `t1_weights.py`, `t2_lemmas.py`, `t3_decomp.py` ([P3b/](audit-02-support/P3b/)).
   - Both cross-validate full-space λ_min against the evidence to < 5e-14 at N = 100…3201.
   - My own CC weight-bound check for N ≤ 1000, run inline, is consistent with these.
6. **Records:** link scan, size and registry diffs ([rec/commands.txt](audit-02-support/rec/commands.txt)). Every new JSON/SVG is under 16 KiB. Outside the topic, only the topic results file differs from main.

## Findings

### B1 — MAJOR: P2's slope test was largely postdictive and is described as fresh

The Q_min values at m = 1400/1401, 1800/1801 and 3000/3001 were already committed in `evidence/S4-padua-essential.json` at `5110954`, before the P2 protocol.
- From those rows alone, the 1400→3000 and 1800→3000 secants (both parities) already differ from b₂ by 0.0030–0.0035.
- Interpolation predicts Q_min(1600) = −0.023421, against −0.023414 measured ([P24/P2-preexisting-predictivity.json](audit-02-support/P24/P2-preexisting-predictivity.json)).
- Only three criteria are genuinely prospective: the mode-2 weight, the L-distance and the branch-difference rate.
- `theory/P2-measurements.md:19,89` and `ideas/P2-protocol.md:68-71` call these "fresh" tests without saying that the slope endpoints were already known.

**Required:** a dated scope addendum in P2-measurements, the P2 idea and protocol records, `report.md` and the results file. It must separate the prospective criteria from the essentially postdictive secant criterion. The PASS outcome and thresholds stay unchanged.

### B2 — MAJOR: P4's closed-form denominator has no durable theory record

P4's lower bound depends on the closed-form C_ij/C_jj formulas for ∫t F_iF_j dt:
- `theory/S2-endpoint-model.md:136-141` calls them "derived formulas to be checked";
- `theory/P4-certified-lower.md:24,35` calls them "accepted";
- their derivation exists only in `independent-checks-S2-model.md:66-100` and `independent-checks-P4.md`.

AGENTS.md and WORKFLOW require a durable theory file with explicit proof status for a result another proof depends on. The mathematics is correct: re-derived by hand and confirmed by quadrature to 1.4e-13. Status of P4 is not withdrawn.

**Required:** add the derivation as a PROVED supporting record, or as a proved section of P4-certified-lower with its own status line. Update both citing lines. This is new proof text, so it is material and receives a focused recheck limited to that derivation.

### C1 — MINOR (caused by this audit): manifest scope

`evidence_manifest.py` excludes only `audit-01-support/`. This audit's `audit-02-support/*.json` therefore breaks `--checks` at the audit output commit, as A13 did before. Generalize the exclusion to `audit-*-support/` and regenerate the manifest intentionally.

### C2 — MINOR: records hygiene

- `theory/S1-model.md:143` and `ideas/S1.md:42` changed "operationally rejected" to "deferred" in place. Add a History line quoting the original wording, per WORKFLOW's split rules.
- `theory/S2-endpoint-model.md:62-69` now has no status label. Add, for example, "registered definition/prediction; proved via S2-05/S2-06".
- **Stale text:**
  - `report.md:3` says P1–P4 is "in progress", and `report.md:75` gives the old 23 Python / 40 JSON scope.
  - `manuscript-insert.md:3` says the audit is pending, and `manuscript-insert.md:11` says the limit is unresolved; P3 now proves it locally.
  - `theory/P3-reverse-bound.md:48-49` says the assembly check is "required".
- Say explicitly in `report.md` and the results file that applying P3 to registry PD-T020 waits for PR preparation, separately from A3, which concerns only PD-T027/PD-T381. The dated block "PD-T020 stays OPEN" at `results/…:43` can be misread.
- `results/…` should say "no useful digits" beside the 24-digit P1 interval.

### C3 — MINOR: novelty records

- Add IDEA-466 ("dyadic outward-enclosure certifier; fixed-point trial-energy witness", `state/IDEAS.md:981`) to the closest entries and separation criteria of `novelty-gate-P4.md:26`, `ideas/P4-rayleigh.md:9` and `ideas/P1-numeric-protocol.md:11`. The "consolidated technical continuation" verdicts stand.
- Fill in the coordinator link to P1/P3 gate provenance that `novelty-gate-P4.md:10-14` promised.

### C4 — MINOR: checker and protocol details

- **Prose hashes:** `P1_rectangle.py:122-123` records hashes of prose files (the protocol and the theory reduction). WORKFLOW says new checkers do not pin prose. Every rerun now shows a mismatch (568fc2… recorded against 020c95… current), which is disclosed. Label these fields "historical (c1e6e59 blob)" or drop them in future checkers. Do not change committed receipts.
- **Summary prerequisites:** `P2_summary.py:34-35` checks only the calibration receipt; validation and overlap are enforced only by procedure. Add a check, or state this in P2-measurements.
- **Wording in P3-reverse-bound.md:**
  - lines 101–103: "nonincreasing for z>0" should read 0<z<2π;
  - lines 235–243: write out dx = sin θ dθ ≤ dθ;
  - lines 87–88 and 110: "left physical half" means θ ∈ [0, π/2], i.e. x ∈ [0, 1].

### NOTES

- **N1.** P3-01: "at most four J_j" is in fact at most three, and |D_k| ≤ 3/(2t) also holds. Both are conservative.
- **N2.** P3's explicit remainder is O(√(L log L)), while the measured remainder is O(1). At reachable N the minimiser's energy lies mostly in microscopic and endpoint nodes, and the good layer holds only 1–4%. So no numerics at N ≤ 10⁵ test the leading constant itself. The limit rests on the proof.
- **N3.** P1-02: simplicity rests entirely on the two-step A² argument. A future claim of pointwise kernel positivity or Jentzsch-type irreducibility would be false.
- **N4.** P1-01 §4: the step ∫∫q(0)dνdν = Z(0) needs a pointwise identification. Tonelli at fixed t gives it; one sentence would suffice.
- **N5.** `P2_modes.py:38` hardcodes `source_head` as the rules SHA, not the code commit. The protocol says "Q smallest algebraic pair", but the code computes one Q eigenpair. The m400 L-distance of 0.00515 > 0.005 is non-test context and is recorded only in `attempts/P2.md`.
- **N6.** Smaller items: undated addendum headings at `gates.md:110,114,118`; dangling "registered windows below" boilerplate in S1/S2/S3-measured; residual missing spaces in new prose; duplicate Closest/Separation fields in S2-core and S3-carrier-variant; t₀ undefined in the added S1-02 (D) text. The response gives 259 links where LOG:166 gives 242.
- **N7, for AC's A3 decision.** P1 and P4 now provide exact, positive-spectrum and one-sided certified information. They do not provide decimal values: the P1 enclosure has no useful digits, and P4 is one-sided. Reading (b) of audit-01 A3 is therefore still not met, and the decision remains AC's.
- **N8, for PR preparation.** PD-T020's original target ("existence/value of sharp rescaled endpoint limit") is met in full by P3 together with S1-02, through all N and both parities. At PR preparation it may become PROVED, linked to P3-03. This is a registry application to be verified at readiness, not an audit action.

## Residual uncertainty

- **Same-family reviewers.** Proofs were reconstructed by me and five Claude subagents, so correlated blind spots are possible. The distinct Astra checks agree on every item.
- **Numerics.** All audit numerics are floating corroboration. The certified quantities rest on reviewed integer arithmetic using Python integers and `isqrt` as trusted dependencies. There is no second rigorous scalar library.
- **P2 rerun.** It reused the developer's algorithm under different library versions; it is not independent arithmetic.
- **Not re-audited here.** S1-02, S3-03 and PD-T379 were accepted in audit-01 and only checked for consistency.
- **Literature.** Coverage is still search-level.
