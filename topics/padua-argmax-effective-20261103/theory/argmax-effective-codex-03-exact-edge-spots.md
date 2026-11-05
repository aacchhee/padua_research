# PD-T?argmax-effective-codex-03-spots — Three strict whole-cell edge comparisons

ID kind: PD-T.
Aliases: G6 exact spots; degree 13/17/24 E-C instances; target-center comparison.
Split from: none. These are finite instances of IDEA-324, separate from the measured G6 screen.
Split into: none. All-degree E-C and PD-T099 remain OPEN.

## Statement

Use PD-T101's even-checkerboard Padua cardinals. For m=n+1, write

    E_n(j,k) = sup_{k-1 <= t <= k+1}
                 lambda_n(cos(j*pi/n),cos(t*pi/m)).

The following strict inequalities hold:

| n | j | source k | target k' | delta |
|---:|---:|---:|---:|---:|
|13|0|9|7|1/20|
|17|0|11|9|1/40|
|24|24|11|13|1/100|

For each row,

    E_n(j,k) < lambda_n(cos(j*pi/n),cos(k'*pi/m)) - delta
             <= E_n(j,k') - delta.

These are three eligible centreward comparisons. No assertion that they exhaust the comparisons at their degrees is made.

## Definitions

The nodes and exceptional halved x mode are exactly those of PD-T101. The edge is x=1 when j=0 and x=-1 when j=n. Both cells are closed. The target is the specified center point, not an assumed maximizing phase.

## Assumptions

The accepted cardinal formula and PD-T210's outward integer constructor are trusted mathematical dependencies. Every arithmetic acceptance test uses integers or exact Fraction arithmetic at scale S=2^192; no float acceptance or optimizer completeness is assumed. Correct execution of the pinned checker is the computational premise.

## Status by part

Overall status: **PROVED**, computer assisted at the three displayed finite instances. Written finite reduction, exact arithmetic, small repository certificate and actual different-agent checker execution with corruption controls are complete. Required Claude topic audit is pending.

| Mathematical part | Status | Evidence |
|---|---|---|
| Three strict inequalities with the displayed rational deltas | PROVED | Seven Bernstein leaves, exact target lower bounds, independent checker acceptance and exact integer margin comparisons |

Candidate disposition: retained finite E-C continuation. No all-degree statement is upgraded, and no negative result is inferred from the untested comparisons.

## Depends on

- PD-T101: corrected cardinal formula, positive weights and node conventions.
- PD-T210: soundness of the general 192-bit outward constructor and subdivision rules.
- PD-T231: predecessor finite E-C proof; its generic univariate reduction is repeated below. Its n=7/12 conclusion is not assumed to imply these degrees.

## Proof and finite reduction

Restrict each cardinal to the physical edge x=cos(j*pi/n), obtaining a univariate polynomial P_B(y) of degree at most n. The inherited general constructor encloses its power coefficients at scale S. Edge substitution involves only exact signs and interval additions.

Let [a,b] enclose the exact source physical interval [cos((k+1)pi/m),cos((k-1)pi/m)], using outward cosine bounds for its two endpoints. Enlarge to [a,b], substitute y=a+(b-a)z, and convert each polynomial to degree-n Bernstein coefficients. The exact coefficient multiplying the power coefficient of y^i at Bernstein index r is

    sum_{h=0}^{min(i,r)} binom(i,h) binom(r,h)/binom(n,h)
                            * a^(i-h) * (b-a)^h.

This follows by expanding the affine substitution and the elementary identity for z^h in the Bernstein basis. Exact Fraction weights followed by outward integer rounding enclose every converted coefficient c_(B,r). Since the Bernstein basis is nonnegative and sums to one,

    sum_B |P_B(y)| <= max_r sum_B |c_(B,r)|
                   <= max_r sum_B max(|lo_(B,r)|,|hi_(B,r)|)/S.

The checker recomputes this upper bound on every outward de Casteljau child. At n=13 and17 the leaves `0,1` cover the entire source interval; at n=24 the leaves `0,10,11` do so. These are complete closed binary covers including their common endpoints. Consequently the largest leaf bound U/S bounds the entire source supremum, regardless of cardinal zeros or undiscovered local extrema.

At the target center, outward cosine enclosures and interval Horner evaluation enclose each P_B. Sum the minimum absolute values in these intervals, using zero when an interval contains zero, to get the exact lower bound T/S for the target lambda value. Thus

    target lambda - E_n(j,k) >= (T-U)/S.

The exact checked integers T-U, in the order of the statement, are

    355475074073257551938068791061021617047529569804920044838
    181790752601154368530363037499160237314572357709472642095
     70464731831848770905574364008802755171420832596658620444.

Multiplication by20,40,100 respectively gives integers strictly greater than

    S=6277101735386680763835789423207666416102355444464034512896.

Therefore the target-minus-source margins strictly exceed the stated deltas. Each target center is inside its target cell. This proves both inequalities in the statement. ∎

## Checks and essential evidence

Producer [g6_exact_spots.py](../code/comparison/g6_exact_spots.py) SHA256 `a35096d3614a0e9413a8bf8e24cfed48912da79e61120a044224464d69a0e2f6`; strict checker wrapper [g6_exact_check.py](../code/comparison/g6_exact_check.py) SHA256 `74b0255f467b0d045f614e4486b7c60d54e6da2df5e6e3ee2ead73197c463caa`.

Executed from the repository root:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-argmax-effective-20261103/code/comparison/g6_exact_spots.py --float-input /workspace/padua-work/comparison/g6.json --output /workspace/padua-work/comparison/g6-exact.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-argmax-effective-20261103/code/comparison/g6_exact_check.py /workspace/padua-work/comparison/g6-exact.json --controls --output /workspace/padua-work/comparison/g6-exact-independent.json
```

The parent's gpt-6.1-sol medium gates worker wrote and actually ran the producer; CPU times were0.506741203,1.624429368,8.512108619 seconds. The gpt-6-astra ultra comparison mathematics worker inspected the inherited checker and wrapper, then actually executed the second command in a separate process: accepted=true, all three pairs and seven leaves,11.364958529 CPU seconds. All11 malformed controls were rejected: missing row/leaf, duplicate leaf, nonedge index, wrong target, invalid path, forged upper bound, forged target, changed source hash, forged scale and pending leaf. The wrapper pins exactly the three identities, scale, producer and inherited source hashes; it does not invoke the old top-level checker, which correctly remains specific to n=7/12 and its E-P witnesses.

The inherited `d3_edge_check.check_pair` checks only that the reconstructed
margin is strictly positive; its acceptance alone does not check the
displayed deltas 1/20, 1/40 and 1/100. Those deltas rest on the separate
exact integer comparisons displayed above.

The independent mathematical worker additionally executed exact integer assertions `20*d13>S`, `40*d17>S` and `100*d24>S`; all passed. This arithmetic is also checkable from the displayed integers without trusting another artifact.

| Essential artifact | Bytes | SHA256 |
|---|---:|---|
|[Certificate](../evidence/g6-exact.json)|4424|`496060af0278cbf973f967a4c3ddc325b8c9a6deb530c7fc39a77b1837a463d6`|
|[Independent checker receipt](../evidence/g6-exact-independent.json)|2311|`e0fbb0fc0bf6a502e579cfb730e6dbdc6d67ee5d9a212ca4c7673301130520e7`|

These small artifacts are preserved in the repository's `evidence/` directory with unchanged bytes. The full floating screen merely chose the pairs and is not a proof premise. The final producer binds its actual full-screen input hash `cd2718db479893d2c1f4027fb2e96c10b5045ac609af4bea8731b3bab5ce42da` for provenance. The checker can be rerun directly on `topics/padua-argmax-effective-20261103/evidence/g6-exact.json`; the earlier executed command above preserves the original working-output provenance.

Producer and checker share the inherited outward arithmetic and cardinal-constructor kernel. This is an actual different-agent checker execution, not a separately implemented arithmetic kernel or a separate-source reconstruction. The limitation is the same type explicitly disclosed in PD-T210/231; no independent-arithmetic claim is made.

## Sources

Accepted local kernel and interval/Bernstein theory only. No 1-D literature theorem, fitted rate or unproved phase comparison is used.

## Scope

Only the three listed instances are proved. They are stronger than the corresponding three E-C inequalities because they compare to a target-center value with explicit positive margins. They do not locate the cell maximizers, prove other pairs or degrees, establish interior-to-boundary domination, or close the all-degree bridge.

## Open items

All-degree E-C and a useful all-n phase-alignment comparison remain OPEN. The required Claude topic audit remains pending. No additional exact scan is needed to support the finite statement above.

## History

2026-11-03, rules/input `8a1f394739293953e1566fd24a0a193cc78ff26f`, base `440d107`. Parent authorized three exact spots after the larger measured screen. Pair selection was informed by measured minimum gains, not preregistered blindly. A first producer used a partial float-output snapshot; it was rerun against the completed full output before the frozen independent acceptance. The three inequalities and exact leaves were unchanged. No old topic or registry was edited.
