# Independent finite range corner replay, n2–128

2026-11-05. Distinct Codex checker `/root/check_rows`; coordinator-assigned
gpt-6-astra high under handoff01. Serving model metadata is not independently
exposed. Rules read at `3dda890275a7599caa707b0fb8c0b6e6f6a80643`.
This is an independent mathematical supplement, not the required Claude audit.
Only the new assigned checker wrapper, receipt and this report were written;
raw execution artifacts are local. Existing checker source, earlier reports,
three-degree receipt, developer files and Git/shared files were not edited.

## Disposition

**PASS, finite local scope.** Every integer n from 2 through 128 was actually
executed on the frozen corrected independent exact checker. Its own outward
bounds ell<=Lambda_c and E>=W_n satisfy

    8E + 24u*n^4 <= 16000*n^4*ell,
    u = 110*(1+bit_length(n))^2.

Thus the common kappa>=1/16000 and symmetric scaled-phase square radius
1/128 follow for both parity-correct nonnode corners. For inward physical
distance 0<H<=1/(16000 n^2), the inherited analytic reduction gives

    lambda_n(c+h) <= Lambda_c*(1-n^2 H/16) < Lambda_c.

This verifies the finite computer obligation in the frozen author range
statement. It does not prove a global maximum for any degree, a full-degree
cover, B2/B3, or an all-degree theorem. Status changes/publication remain
with the coordinator. No new mechanism, priority or optimal-constant claim
is made.

## Frozen references and arithmetic independence

The reviewed range statement is `theory/N3-corner-batch.md`, SHA-256
`41e626ef792867f56b46d82df8bcd940a4645fe948fb99aa2a0c0fa64e04a471`.
Its producer aggregate `evidence/n3-corner-batch.json` is
`97e20cc877ad5afd0c9dfe96c1e399a42d820b38c18626e2b69bfa54f6acfc88`.
These were read for the claim, scope and provenance; no producer endpoint
or producer bulk file supplies an arithmetic input to this replay.

The unchanged generic reduction `theory/N3-corner-radius-reduction.md`
remains pinned at
`8cf89c491a4d82df81a69bd1024139d1224bd1f43fd91b1d1fe58a1dd519aee4`.
Its prior independent analytic reconstruction and GMP contract audit are
in `independent-checks-corner.md`, unchanged SHA-256
`e540a6156ea1c18e508b34fff1eddecb4652cc450b9620f54d11dd4530fdd2c8`.
The corrected three-degree receipt remains unchanged at
`573afc5d5ae229b0fa1d47df9b6bf334e47e0e437288a3543826838e5403cb4b`.
All these pins were checked before and after the new execution.

The existing C++ source was compiled unchanged:
`code/check_corner_exact.cpp`, SHA-256
`3646f4e8b6b16957b9e1114f95ad2f0a7c18eec4687b49d5e6f1947a25eea6e3`.
It uses exact GMP integers and directed dyadic interval arithmetic at512
bits, exact Machin arctangent bounds and cosine Taylor remainder bounds,
and the expanded physical-gradient brackets. It imports no developer
kernel and uses no MPFR. The explicit 00 term and exact zero mask
k=0,j>0 even are retained; each remaining cardinal denominator and modulus
is separated from zero before division. The repaired two_w constructor
canonicalizes before arithmetic. The earlier withdrawn source is not used.

The new wrapper reconstructs ell, E, u and kappa solely from each new
checker output and exact integer n. Python Fraction comparisons verify
both the requested inequality and the checker’s unchanged stronger
kappa>1/12500 predicate. No stronger-predicate failure occurred, so no new
constant mode or arithmetic-source change was necessary.

## Exact reduction and checks

Since ell>0, dividing the checked inequality by n^4*ell gives
8(E/(n^4*ell)+3u/ell)<=16000. Hence

    min(1, 1/[8(E/(n^4*ell)+3u/ell)]) >= 1/16000.

The analytic reduction uses W_n<=E and ell<=Lambda_c to bound its
normalized energy and global norm ratios. Its previously reviewed
aggregate Taylor and slope inequality yields the stated loss, without
termwise sign preservation. The node/weight reflection transfers this
local estimate to the second nonnode corner.

For |alpha|,|beta|<=1/128,

    n^2 H <= [alpha^2 + n^2/(n+1)^2*beta^2]/2
            <= [1+n^2/(n+1)^2]/(2*16384)
             < 1/16384 < 1/16000.

The wrapper also verifies this sufficient phase inequality exactly for
each input. Integer checks establish bit_length(n)=ceil(log2(n+1)),
the explicit cardinal/omission counts, and consistency of the checker’s
normalized-energy kappa assembly. The n2 independent rational coefficient
control from the earlier supplement remains Lambda_c=3, W_2=331/18;
these values are enclosed by the newly executed n2 intervals.

## Actual execution and reproducibility

Command:

    python topics/padua-argmax-bridge-20261105/code/check_corner_range.py

The wrapper actually invokes g++ with `-O2 -std=c++17 -Wall -Wextra
-Werror`, links GMP, then calls the fresh executable once for each integer
2,3,...,128 in ascending order. Execution ran from 2026-11-05 21:43:11.552206
UTC to21:43:23.704340 UTC, with12.034997 child CPU seconds including build,
well below the predeclared1200-second cap. Timings are diagnostics only.
Compiler: g++ Debian14.2.0-19; GMP runtime6.3.0. The receipt records exact
build/execute commands, compiler/runtime/platform and binary identity.

All127 requested inputs were attempted, completed and passed; zero failed
or unrun cases. Aggregate contributions:362045 nonzero cardinals and4096
exact zero-cardinal omissions. The exact minimum of the independently
computed lower radius bounds occurs at n128. Its decimal diagnostic is
approximately0.0000810996007879208; the full exact rational is recorded
once in the aggregate receipt. Every decision used exact fractions.

New wrapper SHA-256:
`66fc2d9583260572125bd6c70a943577f94f1dd1ce2755a2c47ad96fffa9a982`.
New executable SHA-256:
`b3b0efdbef5cb74694b7a9327850570ed28ccf5f264d879a1147712fcecd525c`.
New [aggregate receipt](evidence/independent-corner-range.json),6262 bytes,
SHA-256:
`e685674c028bc99e42d547e8b84a2ce5a7e7e67c3cc69f6c29a55ecbcffd23c0`.
It lists all127 integer inputs, outcome counters, exact minimum and pins.

The complete own interval outputs remain in
`local-output/argmax-bridge-20261105/check-corner-range/own-n2-128.jsonl`,
363463 bytes, SHA-256
`47f3d233b5fd7bc46dca8c45a0de2ecc09be4d36988ab83b16f87c44a843bd20`.
No large table or split table is committed. These outputs can be regenerated
from the public integer inputs and frozen independent source; neither
producer bulk retrieval nor agreement with producer endpoints is required.

No unresolved finding remains in this finite local range obligation.
