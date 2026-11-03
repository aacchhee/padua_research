# PD-T?argmax-effective-codex-01 — Finite global argmax continuation

ID kind: PD-T.
Aliases: G0 exact bridge; native finite continuation of PD-T214.
Split from: PD-T099, finite parameter cases only.
Split into: none; isolated capacity probes are listed separately below.

## Statement

For every integer 17<=n<=32, the even-checkerboard Padua Lebesgue function
of PD-T101 attains its global maximum Lambda_c(n) at exactly
(-1,-1),(1,-1) for even n and (-1,-1),(-1,1) for odd n.

Together with the inherited results for2<=n<=16 this gives the continuous
finite range2<=n<=32. No assertion about n>=33 follows from this range.

## Definitions and assumptions

Nodes are (cos(j*pi/n),cos(k*pi/(n+1))) with j+k even. Lambda_c is the
common value at the two parity-correct nonnode corners. The total-degree-n
cardinal kernel includes the exceptional halved (n,0) coefficient.
Acceptance uses exact GMP integers/rationals and outward-rounded integers
at scale2^192. Correct execution of the committed checker is the
computer-assisted premise. No floating comparison enters a leaf verdict.

## Status by part

Overall status: **OPEN at the full finite range pending corrected native replay**.
The17–24 cases have independent reference-Python acceptance. A final
inspection found noncanonical GMP rational operands in the native checker
transform weights. Corrected exact native replays are in progress; earlier
native acceptances alone are not used to close25–32. Claude audit remains pending.

| Part | Status | Evidence |
|---|---|---|
| Finite global equality and exact equality set,17<=n<=32 | OPEN pending corrected replay | Complete canonical certificates under evidence/, independently reconstructed bounds and covers recorded in native-checker-summary.json |

Disposition: finite parameter continuation and implementation variant of
IDEA-320/PD-T210, with no new mathematical criterion or novelty claim.

## Depends on

- PD-T101: corrected cardinal formula, weights and unisolvence.
- PD-T210: rational trigonometric constructor, outward arithmetic,
  tensor Bernstein leaf implication and equality-set argument.
- For the combined range only: PD-T209 at2, inherited PD-T162/166/169/174/177
  at3–7, PD-T181 at8 and PD-T214 at9–16.

The eventual theorem PD-T229 and new corner slopes/radius are not premises.

## Proof and finite reduction

For each listed n, rational Machin and Taylor bounds enclose all cosine
nodes. The corrected cardinal kernel is constructed using outward
arithmetic, then converted to tensor degree-n Bernstein form on the
closed square. Midpoint de Casteljau subdivision retains outward bounds.
Every certificate supplies a finite prefix-free binary frontier. The
checker verifies full coverage, including common split boundaries, and
rejects pending paths, missing children and forged metadata/bounds.

On a bound leaf every coefficient absolute sum is strictly below a
certified lower bound for Lambda_c. Nonnegative Bernstein weights sum
to one, so lambda<Lambda_c throughout that leaf. On a corner leaf all
coefficient absolute sums except the designated corner vertex are
strictly below that lower bound. At the vertex the true coefficient is
exactly the corresponding cardinal value. Its tensor weight can equal
one only at that vertex, proving strict inequality everywhere else in
the leaf. The two exceptional physical vertices are precisely the two
nonnode corners; the node-preserving reflection proves their common
attained value. This is PD-T210's implication without a changed criterion.

The complete covers and independently accepted exact bounds supply every
finite premise for the listed degrees. Thus the maximum and exact
equality set follow. No asymptotic extrapolation is involved.

## Implementations and independent checks

The C/GMP producer implements the expensive cardinal construction,
Bernstein transforms, subdivision and leaf tests. Its Python driver
supplies exact rational seeds/transform constants and the v1 envelope.
The C++/GMP checker independently implements its Machin/Taylor seeds,
cardinal construction, transforms and subdivision. Its Python wrapper
strictly checks the schema, hashes and prefix coverage. It neither
imports nor links the producer's arithmetic kernel.

The two implementations share mathematical formulas, operation order,
192-bit rounding conventions and certificate schema. Both ultimately
depend on PD-T101/210 and GMP; this is not independence from those
mathematical dependencies. The original Python producer/checker share
their own arithmetic, as previously disclosed.

Validation includes every degree9–24 against the unchanged reference
Python checker, exact mathematical-payload comparison after canonical
source regeneration, and a different agent's fresh reference production
and checking at17–24. The supplementary astra high agent rebuilt and replayed the final
native overlap9–24 and endpoint32. The separate sol medium checker author
accepted final9–31; degree32 is explicitly attributed to the supplementary
reviewer, rather than a nonexistent duplicate checker-author execution. The native checker's14 historical and22 additional
malformed controls reject all36 defects; complete and partial positive
cases are distinguished. Source-provenance races found during development
were fixed before the canonical artifacts were regenerated.

The precise executed scopes, source/binary hashes and acceptance hashes
are in [native checker summary](../evidence/native-checker-summary.json),
[independent summary](../evidence/independent-summary.json),
[independent account](../independent-checks-01.md) and the two native
attempt records. Timing fits are measurements, not mathematical premises.

## Essential evidence and replay

Each degree has one small complete certificate `../evidence/nN.json.gz`.
[evidence-manifest.json](../evidence-manifest.json) pins byte counts and
SHA256 identities. The certificates are retained because they are the
essential exact witnesses; bulk regenerated logs remain outside Git.
From the repository root, for any listed degree N:

```sh
g++ -O3 -std=c++17 topics/padua-argmax-effective-20261103/code/native_checker/kernel.cpp -lgmpxx -lgmp -o /tmp/padua-native-checker
python topics/padua-argmax-effective-20261103/code/native_checker/check.py topics/padua-argmax-effective-20261103/evidence/nN.json.gz --binary /tmp/padua-native-checker --output /tmp/padua-nN-check.json
```

Replace N with the integer degree. The unchanged reference checker is
`topics/padua-argmax-alln-20261101/code/part3/finite_general_check.py`.
Do not launch costly pure-Python large-degree replays; the independent
native implementation is the intended larger-degree acceptance path.

## Scope, sources and open items

Only the explicitly listed finite cases. No exact count of local maxima,
all-n comparison, explicit global threshold or complete eventual bridge
is proved. Original PD-T099 remains OPEN. No external one-dimensional
theorem is used. Required Claude topic audit and final registration remain
pending, distinct from completed supplementary checks.

## History

2026-11-03, Codex orchestrator gpt-6-astra ultra; separately configured
producer/checker technical workers gpt-6.1-sol medium; supplementary
independent worker gpt-6-astra high. Rules/input8a1f394, base440d107.
Handoff02 explicitly requested compiled large-degree certification and
independent arithmetic paths. No outside machine was used.
