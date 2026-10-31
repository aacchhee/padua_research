# Independent U0 reconstruction and execution report

Rules/base: `d36722823441dc40c6e19d69a174459348dd309c`. Date: 2026-10-31. Role: independent Codex U0 mathematical checker, requested `gpt-6-astra high`; actual runtime model/effort metadata not otherwise exposed. The root assigned only this directory for writes; no Git operation or producer-source mutation was performed. This report supplements the required Claude handoff and does not approve that cross-agent audit on its behalf.

## Conclusion and exact coverage

No unresolved mathematical defect was found in the five producer proof files for Gram/unisolvence, rationality, Dickson squared determinant, quadratic characters, or general code structure at the frozen hashes in `reviewed-hashes.json`. Their written proofs support PROVED under their explicit assumptions. The eight finite code-distance observations and the finite script checks remain MEASURED. The ideal/H-basis/recurrence and arbitrary-length transform claims remain OPEN as explicitly bounded in the producer target record. No novelty verdict is supplied.

The independent universal linear-code bounds are a separate complete proof, `PD-T?charter-u0audit-codex-01` in `code-optimality-bounds.md`: any linear `[10,3]_7` has d<=7, and any linear `[10,6]_7` has d<=4. The root separately read and checked that argument. These bounds do not depend on an external MDS theorem. The respective Padua attainments 7 and 4 were measured; no computer-proof status upgrade is made here.

## Reconstruction order and gate

Before reading the supplied U0 note/code or producer theory, read all rules, the complete IDEAS registry including obstruction and disposition tables, the literature INDEX, and core CURRENT/PROOF_STATUS/PAPER_MAP/ID_CROSSWALK. Wrote `reconstruction.md` from direct torus arithmetic and weighted Fourier sums before the source/producer comparison. Wrote `exact_check.py` without importing any supplied or producer module before reading the producer checker.

Then read the entire supplied finite-field note and all eight ff_padua scripts. Search terms across ideas/theory/topic/literature included Dickson, torus, rationality, discriminant, quadratic, finite field, Griesmer, MDS, and Padua code. Shortlisted U0a–f and read the predecessor records Bos–De Marchi–Vianello–Xu2007, Caliari–De Marchi–Vianello2008, Dencker–Erb2017, van der Hoeven–Schost2013, TFT2004, Lima–Souza2011, Hubert–Singer2022, Ball2012, plus their index/search context. Those records have explicitly limited reading coverage; this checker performed no new original-literature/fulltext inspection. Thus the gate supports preserving known-mechanism provenance and forbids a novelty claim; it is not an exhaustive prior-art clearance. The root's literature work remains a distinct input to acceptance.

## Mathematical challenges and dispositions

- **Roots and rationality:** trace equality identifies only inverse roots. Both checkerboard projections contain every axis coordinate, so the primitive-trace Frobenius condition is necessary as well as sufficient. Sign choices are independent; `n=1` collapses the x-axis split/nonsplit distinction. No defect in the producer's explicit treatment.
- **Gram and discriminant:** reconstructed the jointly twisted Fourier term and its degree obstruction, counted total endpoint incidence `2n+3`, and checked the exceptional `(n,0)` norm. Monic Dickson rather than cosine coordinates give the stated power of 2. `n=1,q=3` works. Both checkerboard parities were tested independently, although producer theorem scope is the canonical even parity.
- **Bad characteristic:** original primitive-root construction fails when the characteristic divides its required orders. This does not prohibit arbitrary unisolvent sets in those fields. Producer discriminant correctly states a separate integral Dickson-coordinate reduction theorem, whose singularity follows from reduction of the integral squared determinant. Cosine-coordinate reduction at 2 is not silently assumed.
- **Quadratic characters:** independently derived split and norm-one parity signs and the distinct `-1` endpoint corrections. The abbreviated `chi((x+1)(y+1))=1` condition loses endpoints and is only valid off the two exceptional lines. Producer states that restriction. Independent checks include the previously untested smallest field 3 and extension field 9.
- **Codes:** dimension and weighted dual follow from the diagonal Gram matrix including `k=n`. The multiplication-map argument proves the distance lower bound without requiring a Gröbner-basis theorem. The supplied eight code distances are separately reproduced. Griesmer alone would not exclude `[10,6,5]_7`; the new independent hand-proof note supplies an elementary projective-arc exclusion instead of importing the source's Ball claim.
- **Transform scope:** the source mixed-radix FFT uses quadratic prime-length leaves. Timings and successful round trips do not establish the unrestricted quasi-linear assertion. Producer leaves that stronger claim OPEN.
- **Runner/evidence:** source `run_all.py` ignores each child's `returncode`, and several scripts merely print a failure marker. A zero driver status alone is insufficient. Separate child executions all returned zero, and their outputs were inspected. The original driver was additionally replayed unchanged after the separate runs. No isolated-import repair was needed.
- **Minor documentation correction:** producer code-structure initially linked optimality as OPEN in open-targets, whereas the final open-targets handed bounds off separately. The stale reference was reported to the producer for correction; the final reviewed hash records the disposition.

## Actual executions

All outputs are staged under `/workspace/padua-cold/charter-unisolvence-20261031/independent-U0`. Exact commands, exit statuses, byte identities, Python/platform/library versions and every artifact hash are in `evidence-manifest.json`. Compact essential observations are in `check-summary.json`. Original supplied files were untouched; eight copied scripts match both original source hashes and the committed `input-code/ff_padua` copies at root-reported checkpoint `5123a32`.

1. For each of `padua_ff.py`, `fast_transform.py`, `quadratic_padua.py`, `discriminant_real.py`, `hs_ff.py`, `padua_codes.py`, actually ran `python -I /workspace/padua-cold/charter-unisolvence-20261031/independent-U0/source-copy/SCRIPT`. Each exit code was 0. The six executions have separate stdout/stderr/status records. Ran with two workers; timing is therefore observational and not a performance comparison.
2. Actually ran the unchanged `run_all.py` from that copy; exit 0 in 39.614 seconds. Its six child logs are preserved separately from the earlier child-status runs. The caution about status propagation remains.
3. Actually ran `python /workspace/padua_research/topics/charter-unisolvence-20261031/independent/u0/exact_check.py`, redirecting stdout to `exact-check.json` and stderr to `exact-check.stderr`; exit 0 and `ALL INDEPENDENT EXACT CHECKS PASSED`. It uses only Python standard-library integer arithmetic and no RNG. Its explicit polynomial fields were checked by testing every nonzero element for `a^(q²-1)=1`, which guarantees an inverse in the quotient ring.
4. Actually ran producer `python -I /workspace/padua_research/topics/charter-unisolvence-20261031/directions/U0/verify_exact.py` independently to `producer-verify-exact.stdout/.stderr`; exit 0, ten JSON rows: two extension checks plus all eight distance rows. This is a separate-agent rerun in addition to the separate implementation in item 3.

Source RNG seeds inspected: Fp2 generator uses 12345; fast dense comparisons use `n*1000+p`, benchmarks use n; hs random labelings use 1. Distance and character checks use no RNG. No seed was altered.

### Observed scope

- Source core: 76 selected prime cases, `1<=n<=10`, all pass; four root-choice canonicity checks true; `(n,p)=(3,13)` partial-rationality vector matches.
- Source transforms: 46 dense/fast comparisons and nine benchmark round trips pass.
- Source characters: 13 primes from 5 to 47 pass.
- Source floating calculation: twelve log-determinant discrepancies, printed maximum `4.3e-16`; this is a log-determinant metric, not relative determinant error.
- Independent direct-root checker: **112** `(q,n,parity)` cases with n<=6 and both parities where the root orders divide `q²-1`, over q in `{3,5,7,9,11,13,17,19,23,29,31,37,41,43,47}`. This includes nonrational point sets and checks the rationality iff condition, distinctness, nonzero determinant and squared formula.
- Independent character construction: q=`3,5,7,9,11,13`; all corrected descriptions match the roots-of-unity sets. The q=9 field is the Frobenius-fixed nine-element subfield of `F_3[t]/(t^4+t+2)`.
- Independent q7 code enumeration: dimensions 3 and 6, respectively 57 and 19,608 projective messages, distances 7 and 4, with explicit minimal messages in the compact summary. Enumeration covers every nonzero scalar class by first-nonzero normalization; scalar multiples have the same Hamming support. These finite observations stay MEASURED by task choice.
- Producer checker separate rerun: all eight rows for q=`7,11,13,17`, degree 1 or 2, match the producer table and witness counts. This supplements the source replay, not a general distance theorem.

## Limits, evidence retention, and handoff

No fulltext-based priority conclusion, arbitrary-field checkerboard iff conclusion, unrestricted transform complexity proof, or general code-distance formula is supplied. The independent helper still has the usual trusted interpreter/arithmetic/code dependencies. Full cold outputs are cloud-local and have not been delivered to AC's Windows cold-storage location. The manifest records retention and retrieval limitations. The committed compact summary plus manifest is small enough for the workflow evidence limits.

The producer's eight final records were read after their initial reconstruction; frozen file identities are in `reviewed-hashes.json`. Material later edits require an impact check. The producer evidence.md prose was not yet present when this scientific review froze; its final prose is outside this frozen coverage. The independent evidence checker was actually executed as `python topics/charter-unisolvence-20261031/independent/u0/check_evidence.py` with exit 0; `evidence-check.json` records PASS for all 43 staged artifacts and eight source files checked at original, cold-copy, and committed paths. Next: root integrates these records, checks the full campaign registries and prior-art dispositions, and requests the distinct Claude audit.
