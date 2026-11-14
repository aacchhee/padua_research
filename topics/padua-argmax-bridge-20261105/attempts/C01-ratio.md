# C01 ratio mathematics — attempt ledger

2026-11-06. Rules/input `4b728b04216a5490910780bc609a82b853058426`.
Assigned Sol xhigh mathematical developer; serving metadata unexposed.
Own only `theory/C01-ratio-*.md`, `ideas/C01-ratio.md`, this file. No Git,
shared registry, old source, cover job or subagent operation by this worker.

## Preregistered analytic work, before new arithmetic or code

Gate and every retained candidate: `../ideas/C01-ratio.md`. The inherited
PD-T364 sinc identity is already exact; this work supplies a bounded-cost
derivative chart and a complete finite fallback contract. Target k>=1,
including k>=512 and later larger integer degrees, with machine integer
overflow treated explicitly rather than extrapolating the current API.

1. Prove exact turn parity, entire continuation and derivative formula.
2. Prove uniform sinc and jet Taylor remainders with fixed |argument|<=4,
   and denominator positivity for |residual|<=3/2.
3. Prove all exact pole-crossing intervals arising from quadrant root boxes
   fit those charts; actual rounded code still checks literal guards.
4. Supply global caps and collision/zero/nonfinite/intersection contracts.
5. Freeze the proof for a distinct review before replacement code is used.

Optional exact-arithmetic diagnostic budget <=30 CPU seconds, no numerical
cover. No arithmetic test has run at this preregistration. Code owner is
`/root/c01_fast_code`, who owns dependency inspection and timing records.

## Initial source findings

v3 computes both degree-growing harmonic sums before attempting quotient
refinement; changing refinement alone leaves the cubic board work intact.
MPFR producer's value kernel already has a sinc chart, while its derivative
fallback enumerates harmonics. These facts establish implementation
predecessors, not a new mathematical mechanism. Projected profiles remain
cubic even after all ratio loops disappear.

An early specification was sent to the implementation owner while final
shortlisted reading was being completed; it was explicitly a variant of
the existing formula and no replacement code was authorized or run. The
complete candidate gate precedes the new durable proof and any experiment.

## Frozen result and exact diagnostic

`../theory/C01-ratio-enclosures.md` proves the all-k enclosure contract,
including a fixed J32 chart and the exact geometry bound covering genuine
pole crossings at every n>=2. Distinct review requested from coordinator
before adoption. No replacement implementation or leaf replay occurred.

Executed standard-library exact control, after preregistration:

```python
from math import factorial
assert 4**66 * 2**182 < factorial(67)
assert 66 * 4**65 * 2**178 < factorial(67)
for k in range(1, 513):
    q = [k-1-2*j for j in range(k)]
    assert sum(map(abs, q)) == k*k//2
    assert sum(x*x for x in q) == k*(k*k-1)//3
```

Actual exit0, all assertions PASS; measured Python process CPU0.016099733s
for the strict version above. An earlier diagnostic also printed float
log2 sizes and checked the weaker2^-170 remainder inequalities; those
floats are not proof premises. The symbolic proof, not k<=512 sampling,
establishes the identities for every k.

Remaining: independent reconstruction; a new separately reviewed backend;
selected old-case tightness/cost receipts with k>=512; then only whatever
consequential replay the coordinator explicitly preregisters. A valid
coarse fallback can lose a leaf, so correctness alone does not assert old
tree acceptance. Total projected profiles still have cubic arithmetic.

## 2026-11-06 independent-review response

Reviewer accepted the jet formulas/global caps but found §4's application
to actual root boxes broader than its widths<=pi hypothesis: the saved
root endpoint is pi_hi>pi. Added a dated correction to the proof, retaining
the first frozen text/hash. The corrected exact statement uses phase
widths<=P<16/5, proving w<=5P/12<4/3<3/2 and k*w<=5P/4<4 for
n>=2,1<=k<=n+1. Literal rounded residual/Taylor guards remain compulsory;
no guarantee for arbitrary outward Pi or huge degrees/turns is asserted.

Read-only standard-library gzip/JSON/Fraction check of both saved n32
inputs found pi_hi=7074237752028441/2251799813685248<16/5, exit0.
No core formula, implementation source, old receipt or old-topic file
changed. Coordinator owns publication, review disposition and Git.
