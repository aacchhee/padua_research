# PD-T248 — Bounded whole-cell and first-strip comparison screen

ID kind: PD-T.
Aliases: G6; extended E-C numerical gate; I-B0 representative rectangle screen. PD-T?argmax-effective-codex-03.
Split from: none; continuation of IDEA-324's measured support, with separately defined I-B0 variant.
Split into: exact spot inequalities have a separate record; the n4 sign obstruction is PD-N086.

## Statement

In the deterministic float64 screen described below, for every integer n from13 through60, all1536 eligible directed centreward vertical-edge cell comparisons had positive measured target-minus-source maxima. The smallest difference was0.0027806941162857868 at n60. No reversal below-1e-6 was found.

At the six degrees13,17,24,32,48,60, a separate first-strip screen covered182 rectangles matched to their vertical-edge cells. The largest numerical rectangle-minus-edge excess was3.412381488487881e-12. No excess above1e-6 and no local-optimizer nonconvergence were reported. This is a bounded search result, not an inequality between true suprema.

## Definitions

Use PD-T101's even-checkerboard cardinals and lambda=sum|L_B|. Put m=n+1 and angle mesh coordinates qx=n theta/pi,qy=m phi/pi.

For j in {0,n} and k in {2,...,n-1} with j+k odd, E(j,k) is the true supremum of lambda on qx=j, qy in[k-1,k+1]. E-C compares k with an eligible k'=k±2 satisfying |k'-m/2|<|k-m/2|. The numerical estimates of these suprema are the objects measured here.

I-B0 compares the same edge cell with the rectangle qx in[0,1] when j=0, or[n-1,n] when j=n, and qy in[k-1,k+1]. The rectangle contains its edge interval, so a true domination theorem would assert equality of their suprema, rather than a strictly positive edge-minus-rectangle gap.

## Assumptions

NumPy float64 and SciPy local optimization; no interval bounds or completeness theorem. Each edge uses65 equally spaced samples, preserves both endpoints and refines every detected local grid maximum with bounded scalar optimization. Each rectangle uses9 by17 samples and bounded Nelder–Mead from the best three distinct grid points and the optimized edge point, maxiter180, xatol1e-8 and fatol1e-10.

The edge and full-square evaluators are inherited from alln `code/part3/tests_common.py`, using PD-T101/PD-T185's corrected kernel with removable-limit handling. The measured validation at n2,3,4,8,16 compares against the older coefficient evaluator; maximum absolute discrepancy7.771561172376096e-15. This agreement is not an error enclosure.

## Status by part

Overall status: **MEASURED**.

| Mathematical part | Status | Scope |
|---|---|---|
| No numerical E-C reversal | MEASURED |1536 directed comparisons, all n13…60 |
| No numerical I-B0 excess above1e-6 | MEASURED |182 rectangles, six stated degrees only |

Candidate dispositions: E-C and I-B0 **retained / OPEN**. G6's exact-refutation kill did not fire. All-n E-C, all-n I-B0, horizontal strips, deeper interior cells and the global target remain unresolved. PD-N080's different E-P statement stays refuted.

## Depends on

PD-T101 corrected kernel; PD-T185 edge formula; PD-T231 for the inherited definition and background finite proof, not as a premise for these new numerical values. No 1-D source theorem or asymptotic estimate is transferred.

## Checks

Code: [g6_screen.py](../code/comparison/g6_screen.py). Developer: parent's gpt-6.1-sol medium gates worker. Python3.12.14, NumPy2.3.5, SciPy1.17.0. Deterministic grids; evaluator control RNG seed20261101 is inherited from validate(). Executed from the repository root:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-argmax-effective-20261103/code/comparison/g6_screen.py --output /workspace/padua-work/comparison/g6.json
```

The first completed run took 136.222249444 wall seconds and wrote only degree summaries. A second actual execution took 150.265638840 wall seconds and retained every comparison, source/target value and phase, rectangle maximizing point and optimizer status. Its final artifact is `/workspace/padua-work/comparison/g6.json`, 577726 bytes, SHA256 `cd2718db479893d2c1f4027fb2e96c10b5045ac609af4bea8731b3bab5ce42da`. Large output remains local Padua working storage pending the parent's cold-storage handoff; no invented archive locator is used.

The different gpt-6-astra comparison worker actually reran the same frozen script with `--degrees 13 17 24 60 --ib-degrees --output /workspace/padua-work/comparison/g6-independent-ec.json`. All 96 E-C comparison rows agree exactly with the full run, including values and optimized phases. This bounded replay took 1.124009720 wall seconds; its output is 32537 bytes, SHA256 `5f2d90212d3dc69f71bbef2872ac1886c274af356e2d1d323efbae642bf0c4bf`. It does not independently replay the other degrees or I-B0. Both executions share the same float evaluator and optimizer.

Source identity: `g6_screen.py` SHA256 `8e5ccfcf2dda1b1eb168bb1f8eeae15da4e3af33ee09743f52e4f977cff24896`; inherited `tests_common.py` SHA256 `c17e4ed6473b90ed2fa887d0bd2d0b3cf5f6625bbf0d75153a6fa07e26e2a3b7`; inherited `maj.py` SHA256 `705139a65f225f66ed30f5c7f197cda9f54137c42fb10c8b6f452ab83c78909c`.

## Sources

Local theory and executable definitions only. G8 remains a prerequisite before importing a 1-D theorem into any future proof. This round makes no source-transfer or priority claim.

## Evidence

| n | E-C comparisons | Smallest measured gain | I-B0 rectangles | Largest measured excess |
|---:|---:|---:|---:|---:|
|13|8|0.10959945560320339|11|3.0730973321624333e-13|
|17|12|0.06525305830852446|15|8.881784197001252e-14|
|24|20|0.01722854800540574|22|1.1617373729677638e-12|
|32|28|0.009261785197846706|30|9.325873406851315e-13|
|48|44|0.004210293961730116|46|3.412381488487881e-12|
|60|56|0.0027806941162857868|58|2.7622348852673895e-12|

The full external output supplies all other degrees and all individual row data. Values here are descriptive float64 numbers, not rational lower margins.

## Scope

The test neither proves nor refutes a universal ordering. A missed source or target extremum can change a numerical difference; positive margins do not certify completeness. No larger all-degree search was performed. The I-B0 result concerns matched *first inward rectangles*, not PD-T207's offset bands or every interior cell.

## Open items

Find an exact comparison handling the distinct maximizing phases for E-C, and a uniform interior-to-boundary map or rigorous bound for I-B0. Exact spot results are kept separate and do not upgrade this measurement. Claude [audit-01](../audit-01.md) and [response-check-01](../response-check-01.md) accept the stated scope. Full independent numerical replay remains uncompleted; any bounded different-agent replay is reported at its actual scope.

## History

2026-11-03. Mathematics assigned gpt-6-astra ultra; technical worker gpt-6.1-sol medium. Rules/input `8a1f394739293953e1566fd24a0a193cc78ff26f`, base `440d107`. The attempt froze E-C and I-B0 definitions before execution. The parent subsequently retained representative I-B0 degrees for the bounded resource budget, while keeping every E-C degree13…60. The earlier intended broader I-B0 range is preserved in the attempt; it is not reported as executed.

## Final registration — 2026-11-05

Final IDs and preserved provisional aliases: [id-map](../final-id-map.json). Claude [audit-01](../audit-01.md) and [response-check-01](../response-check-01.md) accept the existing stated scopes; no claim, proof or epistemic status changes at registration.
