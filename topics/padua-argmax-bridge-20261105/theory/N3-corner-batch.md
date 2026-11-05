# PD-T?padua-argmax-bridge-20261105-codex-corner-03 — Common finite corner patch for n2–128

ID kind: PD-T. Aliases: N3 range patch; common kappa 1/16000; phase square 1/128.
Split from: none; finite range continuation of the existing corner reduction.
Split into: analytic reduction retained in N3-corner-radius-reduction.md.

## Statement

For every integer n with 2<=n<=128, at either parity-correct nonnode
corner c, in inward physical coordinates h_x,h_y>=0,

    0<H=h_x+h_y<=1/(16000 n^2)
    implies lambda_n(c+h)<=Lambda_c*(1-n^2 H/16)<Lambda_c.

The same conclusion therefore holds on the corner-centered scaled-phase
square |alpha|,|beta|<=1/128 away from its origin. Scaled phases are
alpha=n*xi, beta=(n+1)*eta; physical increments are
h_x=2sin^2(alpha/(2n)), h_y=2sin^2(beta/(2(n+1))).

## Definitions and assumptions

Use precisely PD-T227's nonzero-cardinal weighted energy W_n, including
00 and excluding only k=0,j>0 even. Let ell<=Lambda_c and E>=W_n be
positive outward bounds, u=110(1+bit_length(n))^2, and

    kappa=min(1,1/[8(E/(n^4 ell)+3u/ell)]).

Here bit_length(n)=ceil(log2(n+1)), computed by integer arithmetic.
The producer uses MPFR 4.2.2 correctly rounded pi/cos/basic arithmetic
and GMP 6.3.0 exact rational assembly. The accepted independent path uses
GMP exact rational arithmetic, its separate Machin/Taylor trigonometric
enclosures, compiler and execution; see the independent range report.

## Status by part

Overall status: **PROVED** by the written analytic reduction and distinct
exact reconstruction for all 127 integer inputs n2–128. Required Claude
audit is separate. No full global-degree certificate or B2 verdict follows.

Candidate disposition: retained quantitative range continuation of
IDEA-330/454/457. No new mechanism, priority or optimal-constant claim.
The stronger accepted n33/64/128 kappa>1/12500 theorem is unchanged.

## Depends on

PD-T227 aggregate inequality and exact node formulas; PD-T251 normalized
slopes; PD-T368 global norm upper bound; N3-corner-radius-reduction.md.
The finite computer obligation is the range-wide exact inequality below.

## Reduction to the finite exact check

For each integer n=2..128, reconstruct valid ell,E and verify

    8E+24u*n^4 <= 16000*n^4*ell.                         (R)

Since ell>0 and all quantities are nonnegative, (R) is equivalent to
8(E/(n^4 ell)+3u/ell)<=16000. It therefore proves kappa>=1/16000.
The existing analytic reduction then gives the claimed local loss.
Independent reconstruction may use its own valid ell/E; equality with
the producer's endpoints is unnecessary.

For the phase square, |sin t|<=|t| gives

    n^2 H <= [alpha^2+(n^2/(n+1)^2)*beta^2]/2
            <= (1+n^2/(n+1)^2)/(2*16384)
             <1/16384<1/16000.

Thus the common square fits for every degree in the range. The reflected
second corner follows through the inherited parity-preserving node/weight
permutation. No termwise cardinal sign preservation is used.

## Completed producer evidence

The fixed range/threshold/1200-child-CPU-second cap was recorded before
execution in `../ideas/N3-corner-batch.md`. The wrapper
`../code/n3_corner_batch.py` enforces the unchanged accepted producer
source SHA-256 a0497ca1219850e28f2bf51e72cb4fc8f78cde238b81fd678262d646511402bd,
compiles that C source without arithmetic changes, and calls it once per
integer degree at 256 bits. It checks rational assembly, all mask/node
counts, the n2 mass 3 and W_2=331/18 containment control, the common exact
threshold and the sufficient phase-square inequality. It stops on the
first failed case or CPU cap rather than adapting the constant.

All 127 degrees ran and passed: 362045 nonzero-cardinal contributions,
4096 exact zero-cardinal omissions, no threshold failures or process/
arithmetic errors, no unrun degrees. Total child CPU was 5.246695 seconds;
summed native CPU diagnostics were 4.758418 seconds. These timings are
measurements, not proof predicates. The minimum exact producer kappa was
at n128:

    62766754903414500520426082384448017989234458937242388271583814704618996507603
    /773946533566206611330731790179898724566627752992312031830103344190218641261072962.

Its decimal diagnostic is about 8.1099600788e-5; all threshold decisions
used exact fractions. No measured value supplies an all-degree claim.

Short aggregate receipt: `../evidence/n3-corner-batch.json`, 3601 bytes,
SHA-256 97e20cc877ad5afd0c9dfe96c1e399a42d820b38c18626e2b69bfa54f6acfc88.
It records the input range/count, target constant, outcome counters,
source/wrapper/binary/header identities, commands and versions, and the
single local bulk output identity. Full 127-case rational endpoints stay
local in `local-output/argmax-bridge-20261105/N3-corner-batch/r01/`.
They are run provenance, not unique proof inputs: the independent checker
must reconstruct (R) directly from integer n, so a complete accepted proof
does not depend on retrieving that bulk table. No large table is split or
committed, and no cold-storage retrieval is assumed for the finite reduction.

## Reproduction and checks

Producer invocation and environment are in `../attempts/N3-corner-batch.md`.
The distinct actual range replay is recorded in
`../independent-checks-corner-range.md` and
`../evidence/independent-corner-range.json` (SHA-256
e685674c028bc99e42d547e8b84a2ce5a7e7e67c3cc69f6c29a55ecbcffd23c0).
It freshly compiled the corrected checker and executed each of the 127
integer inputs, independently rebuilding mass/energy bounds. All passed
the common threshold and phase-square condition, with 362045 nonzero
terms, 4096 exact omissions, no failure or unrun degree, and 12.035 child
CPU seconds. No interpolation, extrapolation or producer endpoints were used.

## Scope and open items

The common patch is available for the finite range exactly as stated.
Global finite coverage remains separate; no n37+ global claim and no
all-n effective threshold follows.

## History

2026-11-05, Codex, parent-assigned gpt-6.1-sol xhigh; rules/input
c000899f3fb10d6ba0f1725341a045fe11ec943a. Serving model metadata not
independently exposed. Authorized next bounded corner-helper step, with
the old accepted three-case source/data/theory pins preserved unchanged.

2026-11-05 dated status disposition: independent range reconstruction
passes all127 cases. Original CONDITIONAL developer input SHA-256
41e626ef792867f56b46d82df8bcd940a4645fe948fb99aa2a0c0fa64e04a471
is preserved at source snapshot bcba739. This update changes status and
verification record, not the statement, threshold or proof reduction.
