# Audit 01 — MZ-CC and MZ-SP manuscripts

- Auditor/orchestrator: Codex, `gpt-6-astra`, high, 2026-11-14. This is the independent Codex audit of Claude development requested by handoff 05, with supplementary disjoint checks. Model/effort are the configured assignment; runtime serving metadata are not independently exposed.
- Rules and audited head: `be28d3267bf6117878190b10f2d29840e524eac7` (AGENTS.md, WORKFLOW and Codex role read). Scientific output head named by the handoff: `a03a4f7`; the later input-head change only publishes the handoff. Base/current main, fetched at start: `b5388c25a2a5ccb8d0faf816ab87023cf347bcd3`, already an ancestor; no reconciliation was needed. No other branch was changed.
- Scope: both complete manuscripts, source correspondence, the two provisional consequences, translated proofs, cited-source coverage, available computer-assisted evidence, clean builds, frozen labels, README/M7/report records, and registry compatibility. No manuscript, source theory, historical referee report or shared registry was edited by this auditor.

## Verdict

**Return to WORK: two MAJOR and three MINOR finding groups.** No unsupported analytic theorem or gap in the two new consequence proofs was found. Both papers build cleanly, their frozen numbering matches, and every executed certificate passes. This does **not** approve submission, archival availability, or replay of the absent PD-T376 witnesses. Draft PR #35 must remain draft pending response and preparation.

The report distinguishes a mathematical theorem from an unsupported availability claim and a misleading finite-measurement sentence. Neither major finding refutes an accepted source theorem. No new result ID or status upgrade is made by this audit.

## Findings

### F1 — MAJOR: present-tense archive claims exceed the actual evidence availability

MZ-CC `tracks/mz-constants/paper/manuscript.tex:1504–1511` says files “are archived” and an archive README lists them. MZ-SP `paper-sp/manuscript.tex:1596–1597`, `1708–1710`, `1736–1739` says witness data and exact norms are archived with a deposit. The comments/DOI placeholders do not qualify these printed claims. The developer's own report §6.2 establishes that no deposit or delivery exists, the historical staging directory is gone, and no archive README was found. This is confirmed in the freshly extracted PDF text. Both README assurances that no deposit claim is made need reconciliation.

**Required response:** distinguish committed code/trial/small receipts from intended future deposit contents; remove unsupported present-tense delivery/README claims. Retain the exact missing-file identities and honest verification limit in report §6.2. Before claiming publicly replayable evidence for Prop 8.2, provide a retrievable package of its exact inputs and replay it, or explicitly resolve the affected publication scope. A historical receipt is not retrieval or a new replay. No deposit creation is requested of an agent; AC reserved it. This audit does not reopen PD-T376's accepted mathematics or pretend its absent arrays were staged.

### F2 — MAJOR: do not transfer a trial interval to the true minimum

MZ-SP `manuscript.tex:1635–1638` says of the minimum that at m=1600 “it lies in the interval” of Prop 8.2. That proposition encloses a trial Rayleigh quotient; it implies only an upper bound on the true minimum, not the lower endpoint. The subsection explicitly labels every number MEASURED and “not enclosures”; this mitigates the reading, but the parenthesis should not suggest that Prop 8.2 brackets the minimum.

**Required response:** remove the parenthesis or say the *computed* minimum agrees with the separately certified trial quotient at the displayed precision. Preserve the explicit trial/eigenvalue distinction immediately after Prop 8.2. No new eigensolve or theorem is needed. The SP mathematical reviewer classified this as MINOR because of the subsection's explicit measured-only disclaimer; the citation reviewer classified it MAJOR. The orchestrator retains MAJOR for the ambiguous interval transfer. This severity disagreement is preserved here for AC.

### F3 — MINOR: the negative raw coefficient has an infimum, not the positive supremum printed

MZ-SP `manuscript.tex:864–866` says the signed energies `-16ab/9` and `8ab/9` have suprema `1/9` and `1/36`. The first signed supremum is zero; its infimum is `-1/9`. The positive quantities are the suprema of the magnitudes. Correct this explanatory sentence. The normalized spectral inequalities and subsequent arguments are correctly signed.

### F4 — MINOR: notation remnants

- CC `manuscript.tex:2181`: use the declared `\mathsf J` in the matrix-index bound, rather than `J`.
- SP `manuscript.tex:762`: the fourth-difference parenthesis says “of h” although the function is `\upsilon`.
- SP Lemma A.4 proof, `manuscript.tex:2161,2169`: the local dimension `N` should be the defined `N_Z` (or the explicit common bound `N_K` where appropriate).
- SP `manuscript.tex:2228`: use the defined `\mathcal E_K` rather than `E_K`.

These are transparent notation corrections, not new inequalities.

### F5 — MINOR: current correspondence/check metadata remain stale

The opening CC correspondence table (`correspondence-cc.md:7–48`) still says results are absent/to add, uses old numbering and calls an already checked corollary pending. The subsequent frozen-numbering table and change history permit reconstruction but do not make the opening “current” map accurate. Refresh it, or explicitly mark the planning table historical and add the final mapping. The two provisional theory records likewise retain stale independent-check-pending/Open-items text alongside their recorded PASS checks. Reconcile current metadata without altering earlier handoff bodies or historical reports. Preserve the source-record/TeX-ID mapping for final-ID preparation.

## Mathematical coverage and decisions

The detailed independent reconstruction is in [CC mathematics](audit-support/cc-math.md) and [SP mathematics](audit-support/sp-math.md). Both complete TeX sources were read in full by the corresponding mathematical reviewer, without relying on the prior Opus referee verdicts. The orchestrator additionally read both provisional records, the main-result/finite-evidence passages, the scalar interval implementation and both certificate assemblies, and reconciled the reports with actual reruns.

- **CC:** the weighted Schur lemma is a proved routine supporting tool; no separate substantive theory ID is required. PD-T529 is weakened to its qualitative fixed-trial limits; PD-T531 is genuinely omitted. The changed PD-T523 route through A.1(c) is valid: O(log N) energy gives an O(log N) interpolation error, negligible against the leading log^(3/2) trial norm. The full-space clause in PD-T546 is retained where interpolation on Pi_N needs it. The Appendix B weak-profile/mass/positive-Fatou factors and Appendix C Gram identities were reconstructed. No usable rate or upper certificate for Lambda_edge is inferred from the finite lower trial.
- **New CC consequence:** `1-eta=min(lambda_minus,2-lambda_plus)` and `lambda_plus<=5/3` give exact dominance once `lambda_minus<=1/3`. Exact U quotients at 57 and 58, together with odd/even monotonicity, prove the N>=57 onset; N=56 does not pass this particular witness. Dividing the accepted endpoint limits proves the condition-number limit. Positivity/unisolvence identifies the full nodal interpolation norm as `lambda_minus(N,N)^(-1/2)`. Restricting the 5/3 bound and combining it with `1+rho` gives the stated hyperinterpolation factor with the explicit product-exactness range. Only the improved numerical condition-limit interval inherits PD-T547's computer assistance.
- **SP:** the first-coordinate marginal stays one-sided. The tighter PD-T534 proof reaches 3360<=4096 and preserves its theorem constants; m>=2K and the explicit finite-rank transfer repair the implicit PD-T535/536 steps without strengthening their scope. The weakened PD-T539 statement is consistent with its proof. The fixed-(a,b) PD-T379 bounds, raw/normalized distinction in substantive statements, two-corner multiplicities and negative-ground-state argument are preserved. The new reproduction bound follows from degree `k<=min(n,m-n)`, continuous mass four and the existing operator norm. The six finite brackets imply eta<0.83 by arithmetic.
- **New SP consequence:** convergence plus the carrier limsup/liminf gives `c_minus<=-c_new` and `c_plus>=c_plus^(379)`; the established norm identity gives `||B||=-c_minus>=c_new`. These are transparent consequences, already partially visible in the source proof, rather than a new operator or carrier mechanism. No decimal value of the spectrum is claimed.
- The declined 23/15 strengthening and fixed-ratio Theta(log m) extension remain outside the manuscripts and this approval scope. They were not silently adopted.

## Registry and literature coverage

The complete 1,278-line / 365,258-byte `state/IDEAS.md` was read across four bounded partitions, with overlap at entry boundaries and all obstruction/disposition tables read in full: [1–324](audit-support/registry-1.md), [321–640](audit-support/registry-2.md), [641–960](audit-support/registry-3.md), [961–1278](audit-support/registry-4.md). Truncated preliminary displays were replaced by bounded complete reads as documented in those reports. Relevant linked candidate records were also read. No conflict, revived rejected mechanism or broadened negative scope was found. The two provisional results combine existing theorems; they make no new mechanism-priority claim. This local compatibility audit is not an exhaustive external historical search.

[Citation/record review](audit-support/citations-records.md) checks every actual citation occurrence against the durable LIT coverage: CC 33 cite commands / 37 key occurrences / 28 keys; SP 22 occurrences / nine keys. No additional attribution overreach was found. External PDFs were not reopened: the audit verifies documented reading coverage and scope, not a new fulltext reading. The developer's published ASV (7)/(8) check is recorded in LOG; canonical LIT-045 and LIT-056 addenda remain preparation tasks. The SP->CC citations resolve to the frozen Cor 3.2, Thm 4.3 and Prop 8.1. The CC->SP pointer is contextual and creates no circular proof dependency. All 53 committed-file size/hash rows in report §6 match. M7's older SP source hash is correctly historical at a0206a8, before a03a4f7's duplicated-phrase deletion.

## Actual reruns and evidence

Small essential evidence and code/input identities are in [reruns.json](audit-support/reruns.json). [summarize_reruns.py](audit-support/summarize_reruns.py) checks fresh receipts, all frozen table labels, final logs, fonts, exact interval equality and bracket counts before producing that record. It does not rerun the underlying checks itself. Full scratch logs/matrices/PDFs remain local regenerable outputs, not claimed cold-storage deliveries.

| Check | Fresh execution and result |
|---|---|
| CC P4 exact producer | 4.25 s; denominator positive; target 1.0044369 passes. Exact quotient endpoints match the committed receipt. |
| CC P4 alternate grouped assembly | 2.77 s; target and overlap pass. Outward quotient `[1.004436918864667280457775,1.004436918864667280457778]` exactly matches its committed receipt. |
| SP P1 rectangles, N=16, theta=256 | 1.35 s; exact endpoints match: `[0.013164946500379018110831,0.477809279990884889210594]`. |
| SP finite brackets m=10,20,30,40,60,80 | Exact native/GMP/FLINT producer rerun for all six rows. Every strict-dominance predicate and endpoint inertia passes; rational intervals match committed receipts. Largest run m=80: 170.82 s. |
| Separately written Fraction pencil at m=10 | Fresh checker compares all 3,050 native entries as rationals and 750 off-block pairs, builds new transforms and passes both blocks' four endpoint counts. No larger Fraction-pencil replay claimed. |
| Existing binary64 reproduction suite | `--suite all --max-N 1280`, exit 0. CC table values agree at printed precision. The historical NumPy `where` divide-by-zero warning at an unused odd moment is observed; it does not affect the exact certificates or promote these measurements to proof. |
| Both papers | Fresh four-pass LaTeX/BibTeX builds: CC 32 pp., SP 50 pp.; no final log warnings/box issues, no BibTeX warnings, no Type 3 fonts. Frozen non-cref labels: 52/52 CC and 56/56 SP match. |

The trusted arithmetic is inspected Python integer/Fraction/dyadic code for P4/P1, plus Python/FLINT/GMP for the moderate exact pencils. NumPy/SciPy only propose trial coefficients/transforms where the exact predicates decide acceptance. The P4 alternate assembly shares the scalar module, which was inspected; the m=10 alternative shares FLINT and the mathematical signed-dominance predicate, not the C pencil assembly. These are fresh independent executions of existing checkers, not claims of completely independent arithmetic implementations. P1's rectangle/Schur finite reduction was checked in the SP proof review. The rectangle repeat uses the existing producer, with its committed earlier independent receipt inspected.

PD-T376's exact coefficient arrays and exact-norm files are absent. Only their committed identities/receipts, printed rational intervals, proved reduction and checker sources were reviewed. No claim of a byte-pinned witness replay, artifact retrieval or delivery is made. This is a substantive remaining evidence-availability limitation, addressed by F1, not a failed sign check.

### Commands actually executed

From the topic clone at the audited head (paths below are repository relative):

```sh
python topics/padua-mz-sharp-constants-20261106/code/P4_rayleigh.py --trial topics/padua-mz-sharp-constants-20261106/evidence/P4-trial-J512.json --output /tmp/mz-audit-P4-producer.json
python topics/padua-mz-sharp-constants-20261106/code/P4_check_grouped.py --trial topics/padua-mz-sharp-constants-20261106/evidence/P4-trial-J512.json --producer /tmp/mz-audit-P4-producer.json --output /tmp/mz-audit-P4-grouped.json
python topics/padua-mz-sharp-constants-20261106/code/P1_rectangle.py --N 16 --theta 256 --output /tmp/mz-audit-P1.json
```

For the following, `PYTHONPATH=/tmp/mz-python` supplied python-flint 0.9.0 (FLINT 3.6.0); `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1` were set:

```sh
python topics/padua-mz-2d-frontier-20261105/code/cert_native.py --m 10 --scratch /tmp/mz-audit-native --output-dir /tmp/mz-audit-native
python topics/padua-mz-2d-frontier-20261105/code/cert_native.py --m 20 30 40 60 80 --scratch /tmp/mz-audit-native --output-dir /tmp/mz-audit-native
python topics/padua-mz-2d-frontier-20261105/code/independent_cert.py --producer-receipt /tmp/mz-audit-native/cert-m10.json --scratch /tmp/mz-audit-native --output /tmp/mz-audit-native/independent-m10.json
python tracks/mz-constants/code/reproduce.py --suite all --max-N 1280 --output /tmp/mz-audit-reproduction.json
bash topics/padua-mz-paper-20261113/tools/build.sh tracks/mz-constants/paper /tmp/mz-audit-cc
bash topics/padua-mz-paper-20261113/tools/build.sh tracks/mz-constants/paper-sp /tmp/mz-audit-sp
python topics/padua-mz-paper-20261113/audit-support/summarize_reruns.py
```

Initial builds exposed missing `algorithm.sty`, `elsarticle.cls` and scalable EC fonts in this fresh environment. No source workaround was used: Debian `texlive-science` / `texlive-publishers` 2024.20250309-2, `cm-super` / `cm-super-minimal` 0.3.4-17 and `pfb2t1c2pfb` 0.3-11+b2 were downloaded/extracted under `/tmp/mz-texdeps`. The packaged font converter populated the Type 1 fonts, and temporary TeX/BST/font search paths and a combined pdftex font map were used. The standard alternative is the corresponding installed packages. Build outputs use pdfTeX 1.40.26, TeX Live 2025/dev/Debian; runtime versions and source/PDF hashes are in the receipt. These dependency repairs were local environment setup, not manuscript fixes.

## Next step and limits

Claude answers F1–F5 in response-01.md, repairs current wording/notation/metadata, then prepares final-ID reservations and shared registries. This first substantive audit makes no auditor in-place corrections. A response containing only wording/metadata corrections within the already explicit measured/analytic scopes should receive a diff-based readiness check; an actual change to a theorem, bound, evidence, status, proof, final-ID mapping or other material item requires focused re-audit under WORKFLOW. Do not repeat the whole audit or strengthen a statement to solve an editorial finding.

Submission metadata, official SIAM-class provenance check, DOI/arXiv placeholders, AC's later deposit and companions remain as already documented in report §5 and BRIEF. Only AC merges. Handoff 06 supplies the full response/preparation instruction after this audit output is committed.
