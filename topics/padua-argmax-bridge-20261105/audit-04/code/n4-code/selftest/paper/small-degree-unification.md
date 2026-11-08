# One Bernstein certificate scheme for degrees 2–40

This is an evidence and presentation consolidation of the existing finite
argmax results, not a new degree result or a new mathematical certifier.
One unchanged corrected-cardinal constructor, one certificate format and
one exact C++/GMP checker suffice for every integer2<=n<=40. A narrow
initial-cosine-seed metadata reporting correction is needed at2; no
cardinal arithmetic or acceptance predicate changes. Fresh small-degree
certificates replace the need to describe the historical exact-polynomial,
algebraic-field and outward-Bernstein routes separately in the manuscript.
The already accepted witnesses17–40 are reused without another native run.

Status: **evidence consolidation complete, with independently accepted
new witnesses2–16**. The first baseline replay stopped on the
degree2 metadata mismatch, as preserved in the
[independent audit](consolidation-audit.md). No main-theorem quantifier,
canonical record, frozen
engine, historical certificate or historical receipt is changed here.
The main manuscript may continue to state its existing n>=2 scope.

## The single mathematical implication

Use the even-checkerboard Padua nodes and corrected cardinal polynomials
of PD-T101. The cardinal formula has the exceptional halved(n,0) mode.
For even n let E_n={(-1,-1),(1,-1)}; for odd n let
E_n={(-1,-1),(-1,1)}. The node-preserving reflection in the appropriate
coordinate proves that the two values of lambda_n agree; denote their
common value by C_n=Lambda_c(n).

The unchanged PD-T210 implication applies as follows. A finite complete
binary midpoint partition covers the closed square. On each leaf R write
all cardinals in tensor degree(n,n) Bernstein form, with exact real
coefficients c_(B,i,j). Let U_(i,j) be outward upper bounds for
sum_B |c_(B,i,j)|, and let C_- be a certified lower bound for C_n.
Every leaf must satisfy one of the following strict conditions:

1. Every U_(i,j)<C_-.
2. R has one of E_n as a vertex, and U_(i,j)<C_- at every coefficient
   index except the index of that vertex.

Bernstein basis functions are nonnegative and sum to one. Condition1
therefore gives lambda_n<C_n throughout R. Under condition2 the true
coefficient sum at the exceptional vertex is exactly C_n. Everywhere
else its Bernstein weight is strictly below one, while every other
coefficient sum is strictly below C_n. Thus lambda_n<C_n off that
vertex. Complete closed coverage gives max lambda_n=C_n, with equality
exactly at E_n, including subdivision boundaries.

The general-constructor appendix of
[PD-T210](../../padua-argmax-alln-20261101/theory/argmax-alln-codex-03-finite-certificate-correctness.md)
already proves its outward coefficient/corner construction for every
n>=2. There is no degree-specific proof technology in this implication.
The search need only return a complete certificate; its speed or success
at any other degree is not a premise.

## One common implementation

The producer is
[run.py](../../padua-argmax-effective-20261103/code/native_producer/run.py)
with its C/GMP kernel. The checker is the independently authored
[check.py](../../padua-argmax-effective-20261103/code/native_checker/check.py)
and
[kernel.cpp](../../padua-argmax-effective-20261103/code/native_checker/kernel.cpp).
The common invocation uses a
[metadata-only kernel variant](../code/small_degree_unification/metadata_kernel.cpp)
and a [receipt wrapper](../code/small_degree_unification/check.py) that
imports the unchanged strict checker. Neither alters the input certificate.
They use the same v1 format,192-bit outward integer rounding and exact
GMP rational arithmetic. The checker reconstructs the Machin/Taylor cosine
brackets, corrected cardinals, power-to-Bernstein conversion, subdivision
and every strict leaf test. It checks the full prefix partition and both
corner leaves; it requires producer accepted=false. It imports no producer
arithmetic kernel.

All four native entry points retain their existing2<=n<=100 guard.
The phases-engine's separate n>=41 guard is irrelevant to these runs and
is untouched. There is no attempt to remove it or to reuse a higher-degree
phase certificate outside its proof contract.

The producer and strict Python checker are byte-identical to those already
accepted at17–40. The new C++ source differs from its accepted baseline
only in reporting the initial x cosine seed, with the exact two literal
replacements in
[metadata-patch.json](../code/small_degree_unification/metadata-patch.json):

| Source | SHA256 |
|---|---|
| C producer | `ae3002a995c199660ad8c31dd2c7577a8416208ab8b3868c0795ebe728ab72ff` |
| Python producer driver | `718cf9fc39653766c86fe862398a4670d4426215a994f2cb9063d482554fa934` |
| Baseline C++ checker | `b0c871e7711219edfe3ce01480d8d1de3503a20d9b59f82b63a00eff248bc6e0` |
| Metadata-corrected C++ checker | `9b07d16a691261772e3057323dd3fb7e4934adf5bd2d6cb150f0f825db173667` |
| Python checker driver | `b6c7320db2f7cfebf27fe33aa38ffdd45ff719870e3d23e15f845b6e8026eb2e` |

[FREEZE.json](../code/small_degree_unification/FREEZE.json) pins the whole
producer import closure and bounded invocation wrapper. That wrapper
only selects old degrees, enforces resource limits and records outputs;
it does not add a certificate predicate or change arithmetic.

[METADATA-FREEZE.json](../code/small_degree_unification/METADATA-FREEZE.json)
pins the corrected kernel, strict driver and receipt wrapper.
[The compatibility argument](../code/small_degree_unification/N2-METADATA-COMPATIBILITY.md)
proves that all mathematical arithmetic is unchanged and that every
reported field is identical to the baseline for n>=3. Thus the old17–40
acceptance records are valid premises for this common scheme; this is a
source equivalence argument, not a claim of fresh high-degree execution.

## Actual witness inventory

Rules/source input was `0cd099fd2e3944ac8436a890b7ee707a298255b3`.
The bounded recipe was written in
[PREREGISTRATION.md](../code/small_degree_unification/PREREGISTRATION.md)
before any producer, compiler or native execution of this task. It fixed
pilot2,8, then3–7,9–16; precision192,200000boxes, depth48 and100 search
CPU seconds. No rerun or rescue occurred. The two actual stage commands
both exited0. All15 certificates are complete and have accepted=false.
The15 invocations used11.246136 child CPU seconds including compilation;
their summed wall times were11.923868 seconds. These are observations of
this small run, not a degree-growth law.

| n | Strict bound leaves | Corner leaves | Maximum depth |
|---|---:|---:|---:|
|2|2|2|2|
|3|2|2|2|
|4|14|2|4|
|5|14|2|4|
|6|18|2|5|
|7|24|2|6|
|8|32|2|6|
|9|40|2|6|
|10|46|2|7|
|11|48|2|7|
|12|52|2|8|
|13|54|2|8|
|14|56|2|8|
|15|80|2|8|
|16|94|2|8|

The37,197bytes of new essential compressed certificates are retained
under
[certificates/](../code/small_degree_unification/certificates/).
[producer-summary.json](../code/small_degree_unification/producer-summary.json)
records each exact input identity, byte count, bound/corner count, CPU and
wall observation, actual command and direct shell exit. Full per-stage
argv receipts and raw native/build outputs remain off Git under
`local-output/argmax-bridge-20261105/small-degree-unification/`.

[common-witness-index.json](../code/small_degree_unification/common-witness-index.json)
identifies all39 actual witnesses2–40. A static executed inventory loaded
every file through the unchanged checker's strict parser and provenance
function, checked common format, degree, complete/no-pending metadata and
producer accepted=false, matched every17–32 raw hash to the accepted
native summary and every33–40 raw hash to its separate acceptance receipt.
That inventory does not execute native arithmetic or claim a new replay.

The inherited accepted17–32 witnesses and corrected-kernel replays are in
[the native checker summary](../../padua-argmax-effective-20261103/evidence/native-checker-summary.json)
and the audited
[PD-T246 record](../../padua-argmax-effective-20261103/theory/argmax-effective-codex-01-finite-global-argmax.md).
The inherited33–40 witnesses and independent receipts are in
[native-finite-range.md](../theory/native-finite-range.md).
The common index includes their exact raw hashes. They use the very same
strict checker driver and baseline kernel identities above; this is
evidence reuse under the metadata equivalence argument, not a
claim that these expensive cases were rerun in this task.

A distinct reviewer first accepted the exact metadata-only source patch
and source-equivalence argument, then compiled the variant freshly. That
compilation exited0. The fresh2 pilot accepted, after which every member
of the fixed3–16 continuation exited0 and accepted. All15 receipts have
accepted=true, complete_partition=true, all_supplied_bounds_verified=true
and exactly two corner leaves. Post-execution source/input checks passed.
The whole independent compile/replay sequence used19.153825 child CPU
seconds and19.359040 wall seconds. No17–40 native rerun occurred.
[checker-summary.json](../code/small_degree_unification/checker-summary.json)
retains the compact, explicitly attributed record, every input/receipt
identity and actual exit; the
[independent audit](consolidation-audit.md) records the separate execution.
This supplies the common-pipeline proof witnesses without changing the
historical finite argmax statements.

## Portable replay

Compile the existing checker once in a fresh working directory:

```
g++ -O3 -std=c++17 topics/padua-argmax-bridge-20261105/code/small_degree_unification/metadata_kernel.cpp -lgmpxx -lgmp -o WORK/kernel
```

For every integer2<=N<=40 use the same checker command:

```
python -E -S -B topics/padua-argmax-bridge-20261105/code/small_degree_unification/check.py CERTIFICATE --binary WORK/kernel --output WORK/nN-check.json
```

Only the input path changes. For2–16 it is
`topics/padua-argmax-bridge-20261105/code/small_degree_unification/certificates/nN.json.gz`;
for17–32 it is
`topics/padua-argmax-effective-20261103/evidence/nN.json.gz`;
for33–40 it is
`topics/padua-argmax-bridge-20261105/evidence/nN.json.gz`.
The same producer command with `--n N`, `--seconds 100`, `--boxes 200000` and
`--depth 48` regenerates the new small witnesses. The whole fixed pilot/rest
invocations, exact parameters and source pins are recorded above.

## Degree1 and manuscript wording

Degree1 needs only an affine calculation. Its nodes are(1,1),(1,-1),(-1,0),
and its cardinals are(1+x+2y)/4,(1+x-2y)/4,(1-x)/2. Since1+x>=0 on the
square, |a+b|+|a-b|=2max(|a|,|b|) gives

\[
\lambda_1(x,y)=\max\{1,\ |y|+(1-x)/2\}.
\]

Its maximum is2 and equality holds exactly at(-1,1),(-1,-1). This direct
identity does not require a separate numerical certifier. The unchanged
executable intentionally starts at2, so it must not be described as
accepting a degree1 input. Adding this explanatory affine observation
does not change the manuscript's current n>=2 theorem scope.

The finite verification paragraph can now say: “For every degree2<=n<=40
we use one corrected-cardinal Bernstein
certificate scheme and one exact C++/GMP checker. Each complete closed-square
partition has strict bound leaves and two punctured-corner leaves; the same
Bernstein positivity argument proves the maximum and exact equality set.
The remaining degree1 case follows directly from its three affine
cardinals.” The provenance appendix can give the common index instead of
presenting the historical routes as mathematical necessities.
