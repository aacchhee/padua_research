# Response-02 group E5 — developer report (Claude Opus 5.5 high)

Scope: audit-02 A02-L3 (E5-R2-F1) and A02-L4 (E5-R2-F2), record PD-T?drift-codex-30.
Inputs read: response02-common.md; handoff 07 (item 5 and the full text); audit-02.md rows 92–93/132/168; checks/audit-02/E5.md (complete); record 30 (complete); record 32 (complete); directions/E5.md; ideas-e5.md; PD-T069 record (bivariate-lanczos-claude-313, Statement); response01_e5_checks.py. I did not use evidence/audit-02-e5.json as an input to my own check: the checker is independent of the auditor's script, and only the value prefix is compared.
No git state was changed.

## (a) Dispositions

| Finding | Disposition | Files / lines changed | Summary |
|---|---|---|---|
| A02-L3 / E5-R2-F1 | FIXED | record 30 :146 (Remark paragraph), History :169; directions/E5.md :18, History :63 | `a_-=(4pi^3/9)(5-sqrt(2))`, `a_+=(4pi^3/9)(5+sqrt(2))`, noted as (2/3)pi^3 times the r-endpoints. The r-interval, the limit `a^2(81a^2-360pi^3a+368pi^6)/18` and the constant 219.5413805… are unchanged. The checker verifies these exactly and shows that the superseded formula reverses the order. |
| A02-L4 / E5-R2-F2 | FIXED | record 30 :146 (Remark paragraph), status row :54, overall status :48, corroboration sentence at end of :150, Open item :158, History :170; directions/E5.md :18, :54, History :63 | The a<=0 statement is now eventual-only. For fixed a<0 the limit is >0, so the path is eventually positive. a=0 is the node, with P_n=0. The finite counterexample a*=20pi^3/9-512pi at n=4 is stated explicitly (zeta_4(a*)=zeta_4(a) by 2pi-periodicity; Arb-384 certifies P_4=-0.10421866…<0), together with the general frozen a*=20pi^3/9-2pi n0^4. The Statement, the rate and the sharper constant are unaffected. |

Record 30 edits are all in-line, so no line numbers shifted: :146 is the edited a<=0/labels paragraph, :150 the corroboration paragraph, :169–170 the History lines. ideas-e5.md does not repeat the wording and is not changed. record 32 is not touched; its fixed-A/eventual distinctions are preserved and cited as a parallel.

New files:
- `tracks/bivariate-lanczos/code/drift/e5_response02_check.py` (224 lines, sha256 `983d9d9342c41f33c5cdcc11bc850bf0bc8042e6178435803ee063cd2163bd04`).
- `topics/padua-lanczos-drift-20261101/evidence/response-02-e5-checks.json` (4364 bytes, sha256 `955b36da510c92e3bf144cde8e0c59700e46c0f57cc03762079993450f823377`). It records the command, code sha256, Python 3.13.18, SymPy 1.14.0, python-flint 0.9.0 and the elapsed time (0.49 s).

Final hashes: record 30 `2d16144db9996ed7ed2d9e9a60c02e188b91c81e2ece2b79df6e31d25a71705b` (pinned inside the evidence JSON); directions/E5.md `72e54ee2349888d2026a38fe74c9484c056ec9fbf1e3385212fd0dcb5f923f35`. response01_e5_checks.py was not edited.

## (b) Commands run

From the repo root:

```
PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python3 -B tracks/bivariate-lanczos/code/drift/e5_response02_check.py > topics/padua-lanczos-drift-20261101/evidence/response-02-e5-checks.json
```

The exit code was 0, with result PASS. The final run came after all record-30 edits, so the record-30 hash in the JSON is final. An earlier dry run of the same code, written to the scratchpad, was also a PASS.

Checker content:
- **Definition pin (D).** The exact g_m/P_n strings are asserted in record 30 and in PD-T069 (claude-313, "Final ID: **PD-T069**"), and both file hashes are recorded. The definitions match: `P_n = 9(g_1^2 − ½g_0g_2) + (g_2^2 − g_1g_3)` and `g_m = T_{n−m}(x)T_m(y) − T_m(x)T_{n+1−m}(y)`.
- **L3 (SymPy exact, plus Arb enclosures).**
  - a_∓ = (2π³/3)(10/3 ∓ 2√2/3) holds exactly, and a_+ − a_- = 8√2π³/9 > 0.
  - Q(a_±)=0, and Q = a²(81/18)(a−a_-)(a−a_+).
  - Q(20π³/9) = −6400π¹²/729.
  - √2πa_- = 2√2π⁴(10−2√2)/9 = (4π⁴/9)(5√2−2), with Arb value [219.5413805002682767984686 ± 1.1e-23].
  - a_- = 49.41417173…, a_+ = 88.39150240….
  - The superseded formula gives "a_-" > "a_+".
- **L4 (Arb, prec 384).**
  - a* = [−1539.5926015706412043695927… ± 9e-30] < 0, certified. The exact reason is that a*<0 iff π²<230.4.
  - SymPy exact: a*/256 − (a/256 − 2π) = 0, and both coordinate differences cos(π/4+a*/256)−cos(π/4+a/256) and cos(π/5+…)−cos(π/5+…) simplify to 0. The Arb point balls overlap, the difference is < 1e-100, and the point lies in (−1,1)².
  - P_4(ζ_4(a*)) = [−0.1042186626401180416335899566856822703075 ± 1.64e-42]. The ball radius is 4.6e-113 and the ball is strictly negative. This holds both from the raw Chebyshev three-term recurrence on the point balls and from the cosine form, and both representations overlap the main-a value. The audit prefix −0.10421866 is matched.
  - The leading limit Q(a*) = 2.759…e13 > 0, certified, so the a* path is eventually positive.
  - As an illustration that no claim uses, the certified per-n signs of P_n(ζ_n(a*)) for n=4..12 are −,−,+,+,+,+,+,+,+.

## (c) Proposed text for files I do not own

1. `results/padua-lanczos-drift-20261101.md:19` (PD-T?drift-codex-30 row). Anchor: «A response-01 remark (mathematics confirmed by audit-02; notation/scope corrections pending) sharpens the constant to 2√2π⁴(10−2√2)/9 ≈ 219.5.» Replace with:
   «A response-01 remark (mathematics confirmed by audit-02; endpoint-label and eventual-only a≤0 scope corrections A02-L3/L4 applied in response-02, re-audit pending) sharpens the constant to 2√2π⁴(10−2√2)/9 ≈ 219.5.»
   The results file does not repeat the a_± formula or the a≤0 sentence. This is a status-only update.
2. `tracks/bivariate-lanczos/code/drift/README.md`, "## E5 symbolic checks" code block. After the line `python -B tracks/bivariate-lanczos/code/drift/response01_e5_checks.py > /workspace/padua-drift-runs/reproduce/response-01-e5-checks.json`, add:
   `PYTHONPATH=/workspace/padua-drift-runs/python-deps python3 -B tracks/bivariate-lanczos/code/drift/e5_response02_check.py > /workspace/padua-drift-runs/reproduce/response-02-e5-checks.json`
   After the paragraph ending «…rather than through `PYTHONPATH`.», add:
   «`e5_response02_check.py` (response-02, audit-02 A02-L3/L4) needs python-flint (Arb). It checks the record-30 endpoint labels exactly and certifies with 384-bit Arb that the ball for P_4 at the fixed parameter a*=20π³/9−512π is strictly negative. It reads record 30 and PD-T069 to pin the P_n definition, so its recorded record-30 hash changes if record 30 is edited.»
3. `topics/padua-lanczos-drift-20261101/report.md`: grep finds no a_± or a≤0 wording, and the corollary is not described there. No change is needed. The E5 paragraph at :100–117 remains correct.
4. response-02.md entries for A02-L3/L4: take them from table (a) and section (d). The old→new wording is quoted in record 30 History :169–170.
5. LOG.md: optionally add the line «E5 response-02: record30 a_± labels fixed (A02-L3); a≤0 statement made eventual-only with Arb-certified n=4 counterexample a*=20π³/9−512π (A02-L4); checker e5_response02_check.py → evidence/response-02-e5-checks.json PASS.»

No other current file repeats the faulty wording. A grep for `a<=0|a≤0|5∓|a_(±)|no witness` outside the frozen audit/response-01 files finds only record 30. `checks/response-01/E5-developer-report.md:154` ("the sign argument for a≤0") is frozen and is left unchanged.

## (d) For the Codex re-audit

- **Scope change.** Record 30's Remark no longer claims "no witness" for a≤0. It now claims only:
  - for fixed a<0, the leading limit is >0, so the path is eventually positive and supplies no eventual negative witness;
  - for a=0, the point is the node, where P_n=0.

  It explicitly states that finite-n negatives exist for some a≤0. The new mathematical assertions inside the Remark are:
  - the exact identity ζ_4(a*)=ζ_4(20π³/9);
  - the Arb-certified P_4<0. This is a finite computer-assisted sign whose reduction is cosine periodicity plus the raw definition, and whose trusted software is Arb/python-flint and SymPy;
  - the general frozen a*=20π³/9−2πn0⁴ for large n0, which follows from the main Statement.
- **Status.** The Remark's status stays PROVED as a minor routine corollary, excluded from aggregation. The main Statement is unchanged.
- **Metadata.** The status row, the overall status, the Open item and directions/E5.md :54 now say "audit-02 confirmed; response-02 corrections; re-audit pending".
- **Illustration.** The n=4..12 sign list is certified per n but is illustration only, and no claim uses it.
- **Environment.** Python here is 3.13.18, while the audit used 3.12.14; python-flint 0.9.0 is the same.
