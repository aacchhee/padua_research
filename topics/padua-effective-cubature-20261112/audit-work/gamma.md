# Independent audit work: explicit gamma (-07)

Auditor: Codex, gpt-6-astra, high; mathematical audit subagent. Date: 2026-11-13.
Rules and working head: `8b27da5ea2e0d363d2a416482b176466dc33efa9`.
Candidate specified by handoff 03: `895d85fdd995e9f227dabaf8a212ba4d3b188db0`.
No Git mutation and no developer-file edit was made. This record is an input to the orchestrator's audit, not a separate approval or handoff.

Scope: claim -07, the two gamma certificate implementations, their committed receipts, `independent-checks-gamma.md`, and the DGOV normalization. Arithmetic consequences (b)–(d) were independently recomputed. Novelty/priority is outside this bounded assignment; the full IDEAS audit belongs to the orchestrator/other assigned scope. Rules, workflow, Codex role, handoff 03 and relevant theory/literature records were read. No claim of a new mechanism is made here.

## Result

The mathematical scaling and threshold arithmetic check out. The independent Bernstein checker has a sound-looking exact transform, coefficient-radius treatment, finite cover, slab chart and tail reduction on inspection. I found no counterexample to the asserted theorem. However, the developer checker has an unclosed coefficient-rounding proof obligation. In addition, neither full certificate could be rerun in this audit environment because the required ancillary input was unavailable. Accordingly I do not report a fresh certificate PASS or complete computational audit acceptance. The prior independent receipt is reviewed evidence, not a rerun performed by me.

## Findings

### MAJOR G1 — developer certificate does not rigorously enclose its G coefficient conversion

Locations: `code/gamma_certificate.py:297–300`; error-budget claims at `:23–27` and `:119–123`; `theory/explicit-gamma.md:26`, `:80–85` and `:112`.

The Fourier coefficient expressions are formed exactly, but every coefficient passed to the sign checker is then evaluated by ordinary `mpmath` at 60 digits and converted to binary64. No interval, proved evaluation-error bound, or check of correct rounding is retained. The Taylor error budget treats these inputs as correctly rounded coefficients of the exact polynomial. Sixty digits is plausible numerical precision but does not prove that property, particularly for coefficients formed by cancellation. The subsequent Arb calculation checks only G(0), not all the coefficients used in positivity and the tail.

The independent checker avoids this gap: `gamma_certificate_indep.py:209–216` extracts exact dyadic midpoint/radius information from Arb, and `:691–701`, `:631–635` propagate coefficient radii to the sign bound. Thus G1 is a defect in the claim of two rigorous certificate paths, not a refutation of the theorem and not by itself a reason to discard the independent proof path.

Requested fix: evaluate every G coefficient with Arb and propagate certified radii (or rigorously prove and check that each double approximation fits the claimed coefficient-error budget). Alternatively, identify the Bernstein checker as the proof-bearing implementation and label the unvalidated Taylor route as a numerical cross-check. Either change to proof-bearing code/status requires the appropriate focused review. The Taylor floating-point argument should also justify the implementation of powers at `:145` and `:173`: `numpy` power calls are not literally the stated bounded sequence of elementary multiplications.

### MINOR G2 — stale description of completed verification

`theory/explicit-gamma.md:135–140` still lists the completed local certificate as an open item and says success will turn (a) into a local proof, contradicting `:26` and `:100–110`. The header's “LITERATURE-dependent form” at `:5` is likewise stale. Replace this with the actual unresolved audit/retrieval limitations or historical wording; do not describe completed development as still pending.

### Related target mismatch, forwarded to the orchestrator

`theory/explicit-gamma-target.md:8` requires an explicit compactly supported function. The Gaussian-polynomial function of -07 is not compactly supported. The target nevertheless says “CLOSED” at `:14`. The approximation in -02 may establish existence of compactly supported approximants, but -07 does not give an explicit cutoff with a certified retained excess. Reconcile the target statement/history/status or supply that quantitative construction. This is separate from correctness of the L1 version of -07.

## Checks supporting the mathematics

- For f=P exp(-pi|x|²), the per-axis Fourier formulas in the two scripts agree exactly. I executed an exact rational comparison of all 105 coefficients for powers x^(2m), 0<=m<=13: PASS. The formula is `(-1)^l (2m)! / ((2l)!(m-l)!) (4pi)^(l-m)` for u^(2l). It yields the asserted degree-26 sign reversal.
- With alpha=1001/1000, phi(xi)=f(alpha xi/2)/P(0) has integral `8G(0)/(alpha^3 P(0))`; hence `(3/4) int phi - 1 = 6G(0)/(alpha^3 P(0))-1`. P(0)>0 and G(0)>0 are evident from the committed ball receipts, although these particular values were not freshly recomputed without the input.
- The independent Bernstein coefficient formula, nonnegative basis matrices and convex-hull argument are correct. Its 1e-13 error factor exceeds the stated approximately 2.9e-14 stage estimate, with explicit input radii and an additive underflow allowance. I independently generated exact rational Bernstein coefficients for six synthetic 2D/3D boxes and checked that the code's bounds enclosed their exact minima and maxima: PASS. These are code controls, not a replacement for the DGOV certificate rerun.
- The independent fundamental region is x>=y>=z>=0. The bulk exclusion tests retain every box that can meet the domain. In the slab, x=sigma+alpha-y-z and 0<=sigma<=1/8, y<=(alpha+1/8)/2<5/8, z<=(alpha+1/8)/3<1/2 cover the required region. The conservative float slack in the relevance predicates keeps extra boxes. The tail expansion in t, r²=R²(1+t), gives a valid sufficient sign test for all r>=R.
- For the developer's pinned alpha, exact rational comparison confirms `Fraction(float(1001/1000)) <= 1001/1000`: the l1 discard threshold rounds in the safe direction. Its exact-square assertion depends on the actual depth of the boxes; default receipt has no maximum-depth statistic, and no fresh run was available to check it. This is not asserted to be an observed failure.
- The threshold polynomials are correct. At n=108,109 the Fisher differences `37n²-36(n+1)(n+2)` are -72,37. At n=217,218 package differences `37n³-36(n+1)(n+2)(n+3)` are -39059,8504. At n=219,220 the n0(1/72) differences `74n²-73(n+1)(n+2)` are -146,74. Their unique positive roots establish the claimed all-larger-n thresholds. Therefore 109,218,220 are correct for the stated sufficient inequalities.
- The safe literature value b=972913/1000000 satisfies `1/b-1>1/36` by exact Fraction comparison. From the committed gamma midpoint, the effective b is approximately 0.97291258736865446, smaller than Table 6's 0.972912750; this last inversion is a consistency calculation, not a fresh certification of the input.

## Primary source inspection

Retrieved using the web tool, despite shell network denial:

- [DGOV arXiv:1510.02331v3](https://arxiv.org/pdf/1510.02331v3): Theorem 1.1, pp.3–4, has the Fourier normalization and positive-type/nonpositivity hypotheses transcribed locally. Section 6 explains the rigorous verification and alpha blowup; Table 6, p.26, lists the octahedron bound 0.972912750 with alpha=1.001. Page 27 reports the long octahedron verification runtime.
- [README_SOSChecking](https://arxiv.org/src/1510.02331v3/anc/README_SOSChecking): confirms the objective-volume multiplication and alpha^3 correction. Its returned text did not include the promised final solution table, so no claim of checking that table is made.
- [octa-c.dat](https://arxiv.org/src/1510.02331v3/anc/octa-c.dat): read the eight facet rows, corresponding to all sign combinations with right side 1. Thus K-K is the unit l1 ball, K its half-scale octahedron, volume 1/6. The resulting transference factors are correct.

I did not rerun DGOV's Sage/MPFI source checks or independently prove their theorem.

## Execution and retrieval record

Workspace for this scope: `/tmp/padua-audit-gamma`. Python 3.12.14; NumPy 2.3.5; python-flint 0.9.0. `python-flint` was initially missing and was installed into the temporary target `/tmp/padua-audit-gamma/deps`; mpmath was pinned back to 1.3.0 there. No repository dependency files were changed.

Commands actually executed include:

```
curl -fSL --max-time 60 -o /tmp/padua-audit-gamma/octa_double.func.cpp https://arxiv.org/src/1510.02331v3/anc/octa_double.func.cpp
curl -IL --max-time 30 https://export.arxiv.org/src/1510.02331v3/anc/octa_double.func.cpp
curl -fSL --max-time 30 -o /tmp/padua-audit-gamma/arxiv-paper.pdf https://arxiv.org/pdf/1510.02331v3
curl -fSL --max-time 30 -o /tmp/padua-audit-gamma/arxiv-source.tar https://arxiv.org/src/1510.02331v3
```

All shell retrievals failed with HTTP403 (the export endpoint failed at CONNECT). No denial bypass was attempted. Web open of the coefficient evaluator failed with unsupported content type `text/x-c++src`. A web search for the exact filename returned no result. Search of workspace and readable temporary files found no copy. The paper and two textual ancillary records above were inspectable via the web tool, but the evaluator bytes were not downloadable for a hash-checked run.

Executed inline Python controls imported the two pinned scripts, compared their exact one-dimensional Fourier formulas, and checked the independent Bernstein routine against exact rational coefficient extrema on six synthetic boxes. The observed output was:

```
Exact independent FT formula agrees for all 105 coefficients m<=13
Independent Bernstein enclosures contain exact rational extrema of coefficients for 6 synthetic boxes
versions 3.12.14 2.3.5 0.9.0
```

Script SHA-256 values recomputed and matching committed receipts:

- developer: `a6f841e0646956feaaa947695ebf4ac4ae1c07039da40109f7d8ee57a82b8375`
- independent: `635077161ada17c14c8e866ba36dc6d90ea971b52f7b47073431a6a4cc826f76`

## Runs still needed

The audit environment did not execute these data-dependent checks. Do not transcribe the developer/independent receipt as the present auditor's output.

```
PYTHONPATH=/tmp/padua-audit-gamma/deps python -B topics/padua-effective-cubature-20261112/code/gamma_certificate.py --anc /tmp/padua-audit-gamma/octa_double.func.cpp --alpha 1.001 --R 4 --RG 4 --out /tmp/padua-audit-gamma/gamma.json
PYTHONPATH=/tmp/padua-audit-gamma/deps python -B topics/padua-effective-cubature-20261112/code/gamma_certificate_indep.py --input /tmp/padua-audit-gamma/octa_double.func.cpp --out /tmp/padua-audit-gamma/gamma-independent.json
PYTHONPATH=/tmp/padua-audit-gamma/deps python -B topics/padua-effective-cubature-20261112/code/gamma_ft_check.py --anc /tmp/padua-audit-gamma/octa_double.func.cpp
```

Required input hash: `034a1aea4fafbf29743bded0812723ac8c9cf95274225213578145d016a7bc47`. The missing rerun is a concrete audit-coverage/retrieval limitation, distinct from G1 and from a mathematical counterexample. The prior independent computation is documented and its code was inspected; a fresh cross-agent replay remains unperformed.

The control was also saved and rerun successfully with:

```
PYTHONPATH=/tmp/padua-audit-gamma/deps python -B /tmp/padua-audit-gamma/controls.py > /tmp/padua-audit-gamma/controls.txt
```

This command exited 0; the scratch output contains the three PASS/version lines above.

## Preserved audit control and environment

The executed scratch control is preserved byte-for-byte as [`gamma_controls.py`](gamma_controls.py), 1763 bytes, SHA-256 `bf6251ca8c8c2c7c42fa78b1700c1c5fa89343bcb2922c04f12498219f496c0b`. It is an audit-only exact Fourier-formula and synthetic Bernstein-enclosure control; it does not verify the missing DGOV input. Its imported source path is the audited checkout at `/workspace/padua_research`, so reproducing it verbatim assumes that checkout location.

Actual dependency setup used in this audit (all added packages stayed in temporary storage):

```
python -m pip install --target /tmp/padua-audit-gamma/deps python-flint mpmath
python -m pip install --upgrade --target /tmp/padua-audit-gamma/deps mpmath==1.3.0
```

The first command temporarily installed mpmath 1.4.1; the second replaced it with 1.3.0 before the controls ran. The executed control environment was Python 3.12.14, NumPy 2.3.5 (already installed), python-flint 0.9.0 and mpmath 1.3.0. Exact executed command, against the identically hashed scratch copy:

```
PYTHONPATH=/tmp/padua-audit-gamma/deps python -B /tmp/padua-audit-gamma/controls.py > /tmp/padua-audit-gamma/controls.txt
```

For another session, use a disposable virtual environment with those pinned package versions and the preserved copy; the following is a reproduction recipe, not an additional run performed during this audit:

```
python3.12 -m venv /tmp/padua-audit-gamma-replay-venv
/tmp/padua-audit-gamma-replay-venv/bin/python -m pip install numpy==2.3.5 python-flint==0.9.0 mpmath==1.3.0
/tmp/padua-audit-gamma-replay-venv/bin/python -B /workspace/padua_research/topics/padua-effective-cubature-20261112/audit-work/gamma_controls.py
```
