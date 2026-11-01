# Independent N8 reflection preflight

Verification record only; no finite-count status upgrade or Claude audit.
Codex `/root/a5_n4_checker`, allocated `gpt-6.1-sol` xhigh. Parent assigned
this bounded preflight while complete N8 count/global evidence remains absent.
Ownership is confined to this new receipt and
`outputs/a5_checker_n8_reflection_preflight.json`. No checker, producer,
continuation, registry, Git or handoff file was changed. No search was run.

## Inputs and scientific scope

Read current supporting theories53,60,61 and Candidate5 in
`attempts/T-A5-n8.md` before the computation. Input head was
`b2804ac2cbb86568b475964f25dbf0ccf48949ff`. The three rule files were reread
earlier at3a3281dd; an actual read-only diff from that head to this head showed
no change. User's local-ID/no-range and root-only Git instructions apply.

Candidate5 records the targeted reflection/symmetry/mirror/half-square/orbit/
parity gate and the full closest shortlist IDEA048, IDEA058,
IDEA206/source17 and source06/PD-T100. This is independent checking of exact
coordinate relabeling for the registered A5 target, not a new mechanism or
novelty claim. The gate explicitly forbids proximity-based root merging and
requires literal replay of every materialized witness by the old checker.
The producer lead was writing new analytic63 during this preflight; its draft
was not an input or trusted dependency of the actual calculation below.
After execution, read the complete newly written63 at SHA256
`3da7ea878203a49f77160684cbae3a07445675c9e35cfc804194614a1c9231c1`.
Its same-mask, convex-hull-injectivity hypothesis and fail-closed distinction
match this preflight's stated scope. This read is not the required Claude
audit or a claimed full adversarial analytic review.

| Read input | SHA256 |
|---|---|
| theory53 | `c402a828a7cff08687ca73766353a7d3712173af5ae2e087cddc43a009f488ab` |
| theory60 | `adfe98bb9f94f23dc16534f2a1e1b34362877c0fc914fa2eb4e89c3baf216d0e` |
| theory61 | `6e0ed4786a9a7b6a40743e12065cefd6be9528d329bec46155048927956bf769` |
| T-A5-n8 including Candidate5 | `ff204424f66b9a37746e532c69d7c24f4dded92cea462fe49d38f2ddaeb9abcf` |

Actual supplied spatial input was the unchanged capped V3 artifact
`/tmp/a5-n8-candidate-v3.json.gz`,243017bytes, SHA256
`4d1210394d674f785c6a7d2647c6e97c7353cb071785ac38a68a42aa79e7032d`.
It is incomplete:8 pending paths and no boundary. Its9 supplied roots were
already independently verified in the separate root integration receipt and
were checked again here. No numerical/source maximum list is an input.

Frozen verifier source remained
`a9cff5748d6c40ee41ac76e4e8a0035e0d5dab95f4de1233dfcc26902cb085a2`;
controls remained
`7f57ed9ba5ad864391aa2e309834d9b61c33f673a6854247d44594cb10ec71d2`.
Before/import/after verifier hashes and before/after controls hashes agree.
The preflight imported only the independent verifier, never a producer.

## Actual exact checks

The verifier independently rebuilt the formal degree12 field, principal
embedding, tensor conversions and45-by45 Vandermonde inverse. Its usual
all2025 cardinal-value identities and polynomial reproduction regressions ran.
For parity labels `(j,k)` with0<=j<=8,0<=k<=9 and j+k even, define
pi(j,k)=(8-j,k). The calculation verified this is a bijective involution and
checked the exact field node identities

`node_pi(i)=(-node_i.x,node_i.y)`

for every one of the45 nodes. It then reflected each entire polynomial by
multiplying the coefficient of x^a y^b by(-1)^a and checked exact polynomial
equality `L_i(-x,y)=L_pi(i)(x,y)` for all45 cardinals. This is coefficient
equality in the independently constructed formal field, not sampling.

Every one of the9 original root records then passed the frozen verifier's
Krawczyk inclusion, root-box injectivity, strict cardinal signs, negative
definite Hessian and distinct-box checks. Root rectangles were classified by
exact rational endpoints: strict left means R_x.upper<0, strict right means
R_x.lower>0, and every other case touches or crosses x=0.

**Observed exact rectangle inventory:9 strictly left,0 strictly right,
0 touching/crossing the axis.** The output records all nine full rational R
rectangles, actual masks and reflected masks. No root coordinate or maxima
count was inferred numerically.

The inline program contained a conditional axis test: for each axis-touching
box it would compare the exact mask with its node-permuted mask, form
`hull(R,J R)`, and call the existing `Verifier.injection` using that same
actual root C. Equality of a root with its reflection would require both mask
invariance and this injectivity inequality, in addition to the already
verified root existence and exact cardinal identities. **No such test was
executed because no supplied R meets the axis.** The output's
`axis_reuse_conditions_passed=true` is therefore vacuous and is explicitly
paired with `axis_reuse_tests_performed=0`. It proves no general axis reuse
rule and authorizes no proximity merge.

## Execution and reproducibility

Actual exit0 in11.099367876seconds; Python3.12.14, SymPy1.14.0,
python-flint0.9.0/FLINT3.6.0,160-bit outward dyadics. Trusted arithmetic is
CPython integers/Fraction and SymPy exact field/matrix/polynomial arithmetic
with its FLINT backend. No floating proof predicate is used. The exact finite
QQ evaluator is present in the imported checker but no boundary Sturm
partition was checked in this preflight.

The executed shell prefix was
`PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B -` from
`/workspace/padua_research`. The inline program first checked the frozen
source hashes and raw input hash, imported `a5_checker_n8`, and performed the
following exact verification operations (metadata/output serialization
omitted):

```python
v = check.Verifier(data["field_embedding"])
labels = [(j,k) for j in range(9) for k in range(10) if (j+k)%2 == 0]
permutation = [labels.index((8-j,k)) for j,k in labels]
check.require(sorted(permutation) == list(range(45)) and
              all(permutation[permutation[i]] == i for i in range(45)),
              "reflection node map not an involutive bijection")
for i,j in enumerate(permutation):
    node,other = v.nodes[i],v.nodes[j]
    check.require(other[0] == -node[0] and other[1] == node[1],
                  "exact node reflection identity failed")
    reflected = check.sp.Poly.from_dict(
        {(a,b): (-c if a%2 else c)
         for (a,b),c in v.cardinals[i].rep.to_dict().items()},
        check.x,check.y,domain=check.FIELD)
    check.require(reflected == v.cardinals[j],
                  "exact full cardinal reflection identity failed")
for row in data["interior_roots"]:
    v.root(row)
for row in data["interior_roots"]:
    root = v.roots[row["id"]]
    bounds = root["bounds"]
    low,high = bounds[0]
    region = "strict_left" if high < 0 else (
             "strict_right" if low > 0 else "sects_axis")
    permuted_mask = sum(1 << permutation[i] for i in range(45)
                        if row["mask"] & (1 << i))
    if region == "sects_axis":
        hull = ((min(low,-high),max(high,-low)),bounds[1])
        box = tuple(check.Interval.bounds(a,b) for a,b in hull)
        error = v.injection(row["mask"],root["C"],box)
        # Axis equality additionally requires permuted_mask == row["mask"].
```

The actual program catches a rejected conditional injectivity test and records
its failure instead of accepting reuse. Input JSON is decoded with the
frozen decoder and duplicate-key rejection. It finally checks unchanged
source bytes and writes the complete inventory/metadata.

Output `outputs/a5_checker_n8_reflection_preflight.json`,7945bytes, SHA256
`426c4131ff63441f2175b4b37ee88772c0392f4ceb9f9fc2fba04f304f1a3634`.

## Limits and next checks

The algebra preflight above passes the cheapest node-bijection kill test and
inventories the actual supplied9 rectangles. By itself it does not verify a mirrored leaf fixture,
complete negative half-square, mirrored full partition, boundary/corners,
global-value file, final evidence size or different-agent full rerun. In
particular `count_certified=false` remains explicit. Any materialized mirror
candidate must pass the entire old checker literally, with unchanged
predicates and every mask/root/cone rechecked. The complete count/global
replay still awaits a matching complete XZ/global pair. Required Claude audit
is separate and remains pending.

## Actual literal replay of the small reflected fixture

After the preceding preflight, the producer lead conveyed root's explicit
authorization for the small, clearly incomplete fixture integration. Root
was informed before execution. No source or acceptance predicate changed.
The following command actually ran from `/workspace/padua_research`, exit0:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a5_checker_n8.py /tmp/a5-n8-reflection-fixture.json.gz --allow-partial --output /tmp/a5_checker_n8_reflection_fixture.json > /tmp/a5_checker_n8_reflection_fixture.stdout 2>/tmp/a5_checker_n8_reflection_fixture.stderr
```

Input is `/tmp/a5-n8-reflection-fixture.json.gz`,140986bytes, SHA256
`682b21facd2763718d0cba167f3c5816916dd5538c46fa03610fd3fde9a69937`.
It proposes9 original plus9 reflected root records and8 supplied leaves; it
does not cover the square or supply edges/corners. The independent checker
imported no reflection/producer helper and rechecked all original predicates.

Observed execution time174.316493089seconds, Python3.12.14, SymPy1.14.0,
python-flint0.9.0/FLINT3.6.0. Before/after checker SHA256 remained
`a9cff5748d6c40ee41ac76e4e8a0035e0d5dab95f4de1233dfcc26902cb085a2`;
the built-in source guard passed. The following supplied witnesses passed:

| Recomputed scope | Observed result |
|---|---|
| full node records and cones |45, all accepted |
| complete node directional breakpoints |3474 |
| distinct supplied root records |18, every original root predicate passed |
| supplied leaves |8 |
| complete ordinary compatible records |516: gradient320, Hessian192, root4 |
| universal-gradient leaves |2, both centered;262144 compatible-pattern occurrences |
| node leaves |2, strict containment in the actual target cones passed |

The output correctly has `verified_supplied_witnesses=true`,
`accepted=false`, `count_certified=false`,
`complete_prefix_partition=false`, `interior_complete=false` and
`boundary_complete=false`. No proposed reflection identity or expected count
was substituted for any witness check. This is integration evidence for the
small materialized fixture, not complete N8 count evidence.

Actual output `/tmp/a5_checker_n8_reflection_fixture.json`,5829bytes, SHA256
`4c4c0d06e4c711873c4853167298fed2d092aeb0bb469b0c0b5027805adf3b46`.
The temporary input/output and stdout/stderr remain retained locally; any
required cold-storage manifest/archive is pending root's evidence handling.
No additional repository output file was written beyond the specifically
assigned preflight JSON and this receipt; the original preflight JSON was
retained unchanged.

The different executor separately reported regeneration of its own proposed
fixture, but this receipt does not promote that message into a replay of its
distinct artifact. Complete half-square/tree, all edge/corner/global evidence,
full unchanged-checker acceptance and actual different-agent full execution
remain required. All N8 count/global targets remain OPEN.
