# Supplementary independent checks — A5-partial

- Rules and frozen input commit: `cadb35066160e466cb1704b9791ad6f374446422`.
- Checker: Codex `/root/a1_develop`, requested gpt-6.1-sol xhigh; runtime-resolved metadata not independently exposed. This agent developed A1/B5 but did not develop A5; its A5 execution and inspection are separate from the A5 producers.
- Scope: logging the frozen `degenerate_max` decisions for n=3,…,8; later independent execution of the exact A5 checker and inspection of the written local proof. Required Claude (Opus 5.5 xhigh) audit remains pending. This supplementary record does not accept the PR or certify maxima counts.

## Frozen trace inspection

Inspected `code/a5_trace.py`: it subclasses the frozen certifier, invokes the original `degenerate_max`, records the returned decision and inputs, then returns that decision unchanged. Source imports avoid their `__main__` output writers. The wrapper checks agreement of the resulting candidate counts with `t3_maxima.json`; this is numerical execution agreement, not proof of completeness. Its scope excludes the separately invoked corner and edge-node handlers, exactly as the target's `degenerate_max` location requires.

Trace script SHA-256: `bb9b8be765064de888691635333260635799a73c29d2f149fa3c31e9214f0304`.

| Input, relative to repository root | SHA-256 |
|---|---|
| topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t3_certify.py | `1a1fb00ced54bb3083dce2ff12c56cd10c28499b7e0353ba23e8a6afd5a9d78b` |
| topics/programme-ideas-20261031/checks/code/decisive/gen4-2/leb_common.py | `419970972ae69efcc5e4a1c965fbd49982b67100376d3ff0c46e8629dcb382d0` |
| topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t3_degenerate.py | `cdf8cd3273c9ecffa35542bb572a0dde141bf5d068b77ddda548a9a5bdaee5b4` |
| topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t3_maxima.json | `bf1890f4d23f871f16d2dda41b800e0d70d2025299221296081a925518d48de0` |
| topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t3_certify.log | `4eeb37aa8848202988ebd660b0a332e8812f2adb616d0dacc56cfa1140e7f3a8` |
| topics/programme-ideas-20261031/checks/code/gen4/gen4_tests.py | `9ec69777c75f9ffe8b784b083d6684d47b279091d341c53e9e3b0287078bfb6c` |

## Independent trace execution

Command launched separately from the root producer run:

```text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-proof-attempts-20261101/code/a5_trace.py > topics/padua-proof-attempts-20261101/outputs/a5_trace_independent.json
```

Completed independently with Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0. Compared the parsed output to the producer's `outputs/a5_trace.json` after removing only `elapsed_seconds` from each degree's result: all remaining values agree exactly, including every floating event coordinate, margin and decision.

| n | All calls | Accepted calls | Z for accepted calls | Boxes | Interior / edge / corner candidates |
|---|---|---|---|---|---|
| 3 | 2 | 2 | index 6, node label (2,2), each | 9,345 | 7 / 6 / 2 |
| 4 | 0 | 0 | none | 14,197 | 13 / 12 / 2 |
| 5 | 0 | 0 | none | 31,441 | 14 / 9 / 2 |
| 6 | 0 | 0 | none | 67,141 | 25 / 14 / 2 |
| 7 | 0 | 0 | none | 136,077 | 33 / 15 / 2 |
| 8 | 0 | 0 | none | 261,861 | 44 / 16 / 2 |

Independent trace: `outputs/a5_trace_independent.json`, 4,215 bytes, SHA-256 `d573437f99e12da7a02849029b5d08842fed0d98958576330cb10342d1ffaf7e`.

The literal machine iterates have nonzero theta values (about 10^-18). This is not an exact-zero identity at those machine coordinates. I flagged that distinction to root; the exact checker explicitly proves nearby symbolic representatives and enclosure of the entire floating-radius discs. The floating execution itself remains MEASURED.

## Exact checker and written proof

Independently inspected and executed producer `code/a5_exact_certificate.py`, SHA-256 `ffcc1508176aa0b60a0a709d41a6e736ca0a4b38ec8aa436d5d706f800431c84`:

```text
python topics/padua-proof-attempts-20261101/code/a5_exact_certificate.py > topics/padua-proof-attempts-20261101/outputs/a5_exact_independent.json
```

Default execution was used, including trace coverage; `--skip-trace` was not used. Python 3.12.14, SymPy 1.14.0, exact SymPy polynomial algebra and rational `Fraction` intervals. The run completed successfully and its output is byte-identical to `outputs/a5_exact_certificate.json`. Independent output: 7,011 bytes, SHA-256 `279c8e7ca9c4781bb3c528a21f870162aab8402ea219e3ec339c4b9d676d25f3`. The receipt identifies the frozen producer trace as its finite input and checks the trace's six source-file hashes; my separate trace execution above verifies the same event list independently.

Inspected the interval addition, subtraction, multiplication, reciprocal and integer-power operations; rational bracketing of square roots by squaring; alternating cosine Taylor bounds; exact Vandermonde cardinal construction and L_6 factorization; the transformation of polynomial derivatives to angle Hessians; and Gershgorin bounds for negative definiteness and the zero-cardinal Hessian norm. The coordinate rectangle encloses the angle L1 disc by `1−theta²/2≤cos(theta)≤1` and the Lipschitz bound for cosine. Nonzero cardinal signs are rigorously constant there, and L_6≤0 because x≤1 and its remaining factor has a positive lower bound. Therefore lambda equals g−L_6 throughout the disc. The exact centers have zero angle gradient, so the uniform negative Hessian proves a strict, unique local maximum in that disc.

The two representatives are `(theta,phi)=(0,acos(±1/sqrt(3)))`, each with a rational phi enclosure of width 10^-18. The proved L1 radius is 21/10000, larger than the original binary floating radius plus the exactly bounded seed displacement. The combined background/zero Hessian margin is at least `889361/250000` (>3.5); the directly bounded lambda Hessian margin is at least `1780363/500000` (>3.5). Both certificates passed. No code-inspection finding within this declared local scope.

Read the full written proof `theory/proof-attempts-codex-03-degenerate-maxima.md` at SHA-256 `6c250f523c0ce4856f8f1283a06d33d6859c97ed69b44857de20d1f4584a487e` (its initial metadata still said OPEN pending this independent run). Checked the explicit g_+ polynomial against the independently rerun checker receipt by exact symbolic subtraction, and checked g_-(x,y)=g_+(x,−y). Both differences are identically zero. The written edge derivative, exact centers and center Hessians agree with the independently executed identities. The finite interval reduction, outward-rounded inequalities, sign constancy and strong-concavity conclusion are sound within the stated discs. The exact-representative distinction and the four remaining global counting obligations are stated explicitly.

No mathematical finding in this supplementary A5 scope. The completed independent exact run supplies the previously pending computer-check obligation for this **local** statement; required Claude audit remains separate and pending. A later metadata-only promotion from OPEN to PROVED does not enlarge this checked mathematical statement.

## Remaining obligations

The other four A5 certification obligations and rigorous global arithmetic remain outside this local check. Numerical trace equality never promotes the six counts to certified status.
