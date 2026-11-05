# Audit 01 — padua-mz-cleanup-20261105 — independent Claude audit of the cleanup candidate

**Status of this file: CHECKPOINT, audit IN PROGRESS.** Sections C2, C3, C4–C6 and the
final verdict are not yet written. Nothing below is an acceptance of the whole candidate.

- Auditor: Claude, configured `claude-opus-5-5` (Opus 5.5); AC requested xhigh effort,
  runtime effort not exposed. Role: independent auditor and topic orchestrator for handoff 02.
- Developer: Codex, gpt-6.1-sol xhigh. The auditor is a different agent.
- Rules read at `902360d26edabc348d1a2b687f3ea44bb33f28e9` (AGENTS.md, agents/WORKFLOW.md,
  agents/claude/CLAUDE_ROLES.md, templates/HANDOFF.md). Unchanged from ad503cb.
- Candidate: `10898ad99882248e5e6f9d76641624146af97454` (head 902360d adds only handoff 02).
  Main/base `aff30e8ad5542c94fab642ae024dc9aab4fa7ad7`, merged in ef9723b. No shared registry,
  rules, templates or `.github/` file differs from main (`git diff aff30e8 HEAD --stat` over those paths is empty).

## C1 — computer-assisted finite indefiniteness (checkpoint: no correctness finding)

### Reduction, read and reconstructed

- **Code reviewed line by line:** `code/rigorous_witness.py` (sha256 `11f7cabc…cd498`, the same hash as every
  committed producer receipt) and `code/independent_witness.py` (`60c1e6db…361f`, also matching).
- **Quotient definition:** under the frozen definitions, λ_-(m,n) is the minimum over Π_n of Q_m(p²)/∫∫p² dxdy,
  with an orthonormal product-Legendre basis for L²(dxdy). So an explicit p with N=∫∫p²>0 and Q_m(p²)<0 gives
  λ_-<0. Q_m(1)=4 gives a positive direction, hence indefiniteness. The tabulated rationals bound the
  **trial quotient** of the stated witness only. They are not eigenvalue brackets, and the records say so.
- **Producer bounds:** I re-derived each one.
  - |p−p̂| ≤ L_C(2ε+ε²), from |P_a|≤1 and the table predicate |P_a−A/S|<1/S.
  - |K−K̂| ≤ L_D(2ε+ε²)+E_D(1+ε)².
  - The energy error δ_K B0 + 2δ_p√((A0+δ_K B0)L_D) + δ_p² L_D. It follows from
    Kp²−K̂p̂² = (K−K̂)p̂² + 2Kp̂(p−p̂) + K(p−p̂)², with Cauchy–Schwarz, Σρ=1 (checked exactly in code) and |K|≤L_D.
  - Scale factors are right: center = q/(ρ_den S⁹), B0 = b/(ρ_den S⁶), and the weight sum = w/(ρ_den S³).
  - Every table entry is certified individually from the ball recurrence, so precision loss can only cause a rejection.
  - The sign test uses certain Arb comparisons. A straddling enclosure raises an error.
- **Alternate checker bounds:** I re-derived these too.
  - Two-product bound (L+uL)(1+δ)²(1+γ)²−L. It is monotone in |a|,|b|≤1, and the nested bound ((1+γ)²−1)|A||C||B|ᵀ holds.
  - Weight error from ρ, rounding of the scale, and kernel error.
  - Final sum error γ_{N+3}Σ|terms|, plus the 2E_p Σ|ŵp̂|, E_p²Σ|ŵ| and E_w terms.
  - The half-angle kernel t_0=2, t_a=−4/(4a²−1), with 4/(1−m²) subtracted at (m/2,0) for even m, equals the
    producer's D with exceptional halving.
  - The trust assumption, the standard IEEE γ_k dot-product model, is stated explicitly in the receipt.
- **Weight convention, independent of the developer's code:** `audit-support/code/kernel_vs_moments.py` solves the
  defining moment system Vᵀw=(h_a h_b) at 80 digits. For m=1..13 (both parities) it matches ρ_jk K(x_j,y_k) with
  halved T_m coefficient to ≤3e-81 (`audit-support/evidence/claude-kernel-vs-moments.txt`).

### Actual executions (fresh cloud container, sandbox only)

- **Environment:** Python 3.13.18, python-flint 0.9.0, NumPy 2.5.4, SciPy 1.18.1 under
  `PYTHONPATH=/tmp/claude-0/deps`, with `OPENBLAS_NUM_THREADS=1`. These library versions differ from the developer's
  (3.12.14 / 2.3.5 / 1.17.0). The developer's large artifacts under `/tmp/mz-cleanup` are **absent** here, so no old
  witness identity is claimed retrieved.
- **Regenerated proposals:** `g1_minimum.py --m 60 400 1101 1240 1600` (receipt `audit-support/evidence/claude-minimum.json`).
  - m60's vector reproduces the developer's sha `62838be1…`.
  - m400, m1101, m1240 and m1600 give different vectors. m1600 is `90a8c0cd…`, not PR23's `a23cb0e6…`.
  - The minima agree with the developer's to ≤3e-11.
- **Certificates:** for each m, `rigorous_witness.py --vector … --scratch … --output …`, then
  `independent_witness.py --witness …`. Receipts are in `audit-support/evidence/claude-{producer,independent}-m*.json`.
  These are **new, separately regenerated certificates for different dyadic witnesses**:

| m | producer energy enclosure | alternate q_center ± error | sign (both) | witness sha256 (gzip) |
|---|---|---|---|---|
| 60 | [0.1885934804891 ± 2.58e-14] | 0.18859348048909605 ± 1.33e-13 | + | 662491797ba699dc… |
| 400 | [0.102818906 ± 3.62e-10] | 0.10281890623374051 ± 3.01e-10 | + | ff6d451f1def8b2c… |
| 1101 | [−0.0350668 ± 4.18e-8] | −0.03506683433961681 ± 5.78e-8 | − | 56007f1e11dbaa2e… |
| 1240 | [−2.71e-5 ± 6.00e-8] | −2.7148059718220147e-5 ± 8.19e-8 | − | 84fad274f80ddb19… |
| 1600 | [−0.0234144 ± 4.95e-8] | −0.02341441659322953 ± 1.74e-7 | − | 69cbcf9713635158… |

  Producer wall times were 0.1, 4.9, 43.8, 52.0 and 107.3 s. Every run enclosed weight sum 4 and had a positive exact norm.
- **Brackets:** `audit-support/code/bracket_check.py` rebuilds each interval outward with Fractions and divides by
  the norm enclosure.
  - On the developer's **committed** receipts, the producer interval and the alternate checker's
    q_center ± q_absolute_error both lie strictly inside each stated rational bracket at 1101, 1240 and 1600
    (`claude-brackets-committed.txt`).
  - The alternate checker's *default printed* `q_enclosure` does **not** imply the bracket at 1240 or 1600. This is
    the caveat the handoff already disclosed.
  - My regenerated certificates also fall inside the same three brackets (`claude-brackets-regenerated.txt`).
- **Third path, MEASURED only:** `audit-support/code/third_path.py` is written from `definitions.md` alone. It imports
  no topic code and no FLINT.
  - The float64 kernel weights satisfy every defining moment equation a+b≤m to ≤1.2e-13 at m1101, 1240 and 1600.
  - The float Q_m(p²) values agree with both rigorous centers to ≤5e-12.
  - The exact norm, recomputed with `fractions.Fraction`, **equals** the producer's `exact-norm.txt` at every m.
- **Extra float probes:** `g1_minimum.py --m 1238 1239` gives 1.2076189966751e-4 at m1238, which reproduces the
  developer's positive value to 7e-12. It gives −0.045942496436 at m1239, an odd degree outside the developer's grid.
  This is MEASURED and auditor-only, and adds no claim.

### C1 findings so far

- **F-C1-1 (minor, provenance).** Each recorded witness identity is the SHA-256 of a gzip container
  (`theory/finite-indefiniteness.md:28-35`, the receipts and `cold-storage.json`).
  - The m60 vector reproduced exactly here, and the exact-norm hash matched exactly (`04e78a32…`).
  - The gzip hash was nevertheless `662491…` instead of `9a1bb58c…`. The container bytes depend on the Python/zlib
    build, so the identity is not portable.
  - Fix: also record the SHA-256 of the decompressed canonical JSON payload, and say that the container hash is
    environment-specific.
- **F-C1-2 (minor, wording).** `theory/finite-indefiniteness.md` says the independent interval "lies inside the
  conservative rational bracket". That holds only for q_center ± q_absolute_error, not for the printed `q_enclosure`.
  Fix: state the reconstruction in the theory record itself, not only in the Astra report.
- **F-C1-3 (editorial).** The proof paragraph of `theory/finite-indefiniteness.md` is written for m1600 only
  ("Pi_1599", "near −0.0234144"). Fix: make it generic, or give all three values.
- **Residual trust:** FLINT/Arb for the producer; FLINT/Arb plus the IEEE/BLAS γ-model for the alternate path; the
  frozen convention, which I independently checked only for m≤13 exactly and at the three large m in float. The
  developer's specific large witnesses remain undelivered (pending), but the theorem's content was regenerated here
  with new witnesses.

## Remaining sections

C2 (odd m), C3 (normalized bounds), C4 (manuscript), measured rows, inventories and the novelty gate are being
audited, with Opus subagent reconstructions running. The verdict and the next handoff are pending.
