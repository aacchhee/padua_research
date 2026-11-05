# G1 handoff04 independent optimization plan

Rules read at `bb67c1ee830d468fa33007e15008d5574d00ccf4`; supplied current main `aff30e8` after PR22 integration. Codex technical independent implementation, requested gpt-6.1-sol medium; runtime model/effort not independently exposed. This is a representation optimization of the frozen PD-T136/137 calculation, not a new scientific mechanism or novelty claim. Original checker code, original receipts, all625 rotQ24 nodes, every source, rules, exact endpoints and X tie-breaking remain unchanged.

## Bottleneck inspection and prospective route (before tests)

The original GMP implementation stores each node value as a separately canonicalized `mpq_class`. Each recurrence vector subtraction therefore performs rational denominator multiplication/GCD work separately at625 nodes. All-source propagation repeats this in the inner source/column/projection loops. The previous bounded max20 executions constructed the full basis but completed only37/29/12/13 of230 sources (BJ/mirror/alt/pivot) before1800seconds. This identifies an actual costly path; it does not prove any impossibility or asymptotic cost law.

Proposed distinct port: retain all original nodes explicitly and store each rational vector as one positive common denominator D and an integer numerator vector a, representing v_i=a_i/D. Scalar rational operations then combine denominators once per vector. Dot products accumulate integer products first and construct one rational at the end. Pointwise coordinate products use the frozen rational coordinate numerators and common denominator60 on rotQ24 (12 on T24). Source-response vectors, cumulative source energies, normal diagonals and per-stage row sums use the same representation. Per-node source maxima may remain scalar rationals because they occur outside the expensive propagation inner loop. This port does not use central-pair symmetry and is distinct from any producer symmetry reduction.

Exact representation identities:

- `<a/D,b/E>=(sum_i a_i b_i)/(DE)`.
- For scalar c=p/q, choose F=lcm(D,qE); then `(a/D)-c(b/E)` has numerator `a*(F/D)-p*b*(F/(qE))` and denominator F.
- Coordinate multiplication and component squares multiply integer numerators componentwise and the common denominators accordingly.
- Divide both all numerators and denominator by their common GCD when useful. This changes representation only; integer reconstruction of all values is exact.

Positive residual norms, input scales, full exact Gram checks, source cardinalities and all PD-T137 sums/maxima remain as in the original independent specification. No producer mathematical function imports or floating arithmetic will enter construction or endpoint decisions. Every max/min and pivot equality retains exact integer cross products. The unchanged all-source finite formulas justify the representation conversion; no weighted/gauge/source-model substitution is proposed.

## Bounded validation and decision gates

1. Coordinate with the producer's prospective plan before implementation/tests; preserve distinct implementation/data representation and record any shared input-only artifact. The original accepted88 overlap and T2476 comparisons are reused as evidence; they are not gratuitously rerun.
2. Implement new owned `code/g1_fast_independent*` files only. First tiny validation: fresh maxdegree4 rotQ24 for all four rules plus T24/BJ and pivot; compare exact endpoints/choices/ties against accepted old rows and assert full Gram/positive pivots. Include malformed common-denominator/cardinality/Gram controls. These are backend validation cases, not a new scan.
3. Only after those checks pass, execute one bounded moderate rotQ24/BJ maxdegree14 case, with a prospective300-second cap. Compare its degree13/14 rows exactly with the original703.35-second producer benchmark; retained old2–12 rows provide additional comparison without another old backend execution. Record actual elapsed cost, implementation hash, input identity and any incomplete progress honestly.
4. Report moderate results and a feasible route to root before any degree20 round. No unchanged scalar-GMP rerun, increased old cap, or unapproved max20 work is authorized. If common denominators grow badly or the moderate cap is reached, preserve the failed implementation/cost evidence and return the scope incomplete rather than launching further heavy cases.
5. Raw artifacts stay under `/tmp/padua-lanczos-frontier-g1-fast-independent`; commit only short receipts. No fitting, finite operational verdict, target status change, IEEE statement or mathematical growth claim belongs to this checker assignment.

## Execution status

The producer separately chose common-denominator integer vectors in FLINT. Coordination confirmed independent implementations: this worker wrote C++/GMP `mpz_class` vectors without reading or copying producer implementation code; no producer functions are linked/imported. The shared reduction is the elementary exact representation identity above. Root accepted the stated tiny-control and300-second BJ14 sequence before execution.

All arithmetic numerators and denominators use arbitrary-precision GMP integers, so integer magnitude cannot overflow a machine word. Fixed-width integers are only bounded grid coordinates, degree<=20, column indices<=230 and loop sizes<=625. Every vector denominator is required positive. `reduce` uses the positive common GCD of D and all signed numerators, then divides numerator and denominator together; the all-zero vector becomes denominator1. Dot products, coordinate products, squares and scaled sums therefore preserve every exact rational component. Per-node source maxima retain possibly unreduced positive-denominator pairs and compare by integer cross multiplication; canonicalization is required only when emitting endpoints. The source/model/gauge is unchanged.

Tiny controls completed: six independent maxdegree4 builds (rotQ24 all four rules; T24 BJ/pivot), eighteen endpoint rows matching old accepted evidence exactly. Every build checked full Gram and positive pivots/scales; pivot metadata/ties and all-source dimensions passed. Native scalar-GMP cross-checks verified common-denominator arithmetic primitives exactly, including signed/scaled operations, component products, weighted squares, dot products and zero normalization. Eight malformed native controls were rejected: zero/negative vector denominator, scaled-add/dot dimension mismatch, nonpositive pivot, wrong diagonal norm, nonorthogonal column and zero peak denominator. Per-case elapsed0.033–0.067seconds under two workers. Native source SHA-256 `b6434df51d3df7e04136b1da9f8ee63e6c5f599e609625f415718766db0480dc`.

The approved single rotQ24/BJ maxdegree14 benchmark completed in23.207211843seconds against its300-second cap, with the same source hash after the tiny gate. All13 degree2–14 endpoint rows exactly matched the original producer benchmark, including previously unchecked degree13/14, all four endpoint formulas, dimensions, source class/count, choices and ties. All625 original nodes and119 sources were included. The native basis checked7140 off-diagonal Gram pairings and positive pivots/scales; projector checks passed. This independently verifies the original two BJ13/14 benchmark rows; all122 currently produced unique G1 rows now have independent matching execution, with30 rotated high rows still missing.

The new implementation's23.21-second moderate measurement is a speed improvement relative to the historical703.35-second producer execution, under different concurrent loads; it is not a20 cost guarantee. Proposed next route sent to root: one new rotQ24/BJ degree20 pilot with600-second cap, then separately authorize the remaining rules only after a completed pilot and actual fresh-producer comparison. No degree20 work has started or been approved at this record boundary. Original code/receipts and accepted evidence remain preserved.

Receipts: `evidence/g1-fast-independent-tiny.json` and `evidence/g1-fast-independent-benchmark14.json`. Native source SHA-256 `b6434df51d3df7e04136b1da9f8ee63e6c5f599e609625f415718766db0480dc`; runner SHA-256 `d99b579e6800b4545b899572aa1e7b758bbbb58edfad9f7a223a18f8bff1e884`. GMP6.3.0 and g++14.2.0, no new dependency install.

Actual moderate invocation:

```sh
python -B topics/padua-lanczos-frontier-20261105/code/g1_fast_independent_run.py --out /tmp/padua-lanczos-frontier-g1-fast-independent/benchmark14 --old /tmp/padua-lanczos-frontier-g1/inputs/e1-full-sweep.json --mode benchmark14 --tiny-receipt /tmp/padua-lanczos-frontier-g1-fast-independent/tiny-receipt.json --benchmark-endpoints /tmp/padua-lanczos-frontier-g1/benchmark14/rotated-bj/endpoints.json --receipt /tmp/padua-lanczos-frontier-g1-fast-independent/benchmark14-receipt.json
```


## Prospective authorized BJ20 extension — 2026-11-05, before pilot

After the23.207-second BJ14 match, root authorized **one** new rotated BJ20 pilot with a600-second cap. The C++ backend is unchanged at SHA-256 `b6434df51d3df7e04136b1da9f8ee63e6c5f599e609625f415718766db0480dc`; a separate bounded pilot launcher will preserve the existing tiny/BJ14 runner and receipts. All625 original nodes,230 sources, exact full Gram and the original four endpoints remain required. Complete stages may survive a cap, but no incomplete source subset supplies an endpoint. Original BJ13/14 and old2–12 exact equality checks remain mandatory. No other degree20 rule is authorized at this boundary. Fresh optimized-producer comparison is still required before final acceptance of new rows.

## Authorized BJ20 pilot — completed, fresh producer match pending

The single authorized common-denominator native BJ20 pilot completed in329.174705648seconds against its600-second cap. It used the unchanged C++ backend above and a separate launcher, SHA-256 `0d942826b6e8fbcdcfbaa5e6fe64ca34b2d50254a059950cb096c682fc40f89c`. All625 nodes,230 sources,26565 exact off-diagonal Gram pairings, diagonal norms, positive input scales/pivots, projector nonnegativity/trace, endpoint order and exact upper minimum passed. All19 degree2–20 rows were emitted; old2–12 and original BJ13/14 matched exactly. Raw endpoint JSONL is915817bytes with SHA-256 `0f7c1475a0484aa0905bcdfddf938b4ea2154f58322228e17bb7a91955ca3cf7`, under `/tmp/padua-lanczos-frontier-g1-fast-independent/pilot20-bj/rotated-bj-d20.jsonl`. Short receipt: `evidence/g1-fast-independent-pilot20-bj.json`.

Fresh optimized-producer comparison of the new BJ15–20 rows is pending; native completion alone is not relabeled as a two-implementation match. The producer reports all88 optimized old overlap rows passed but its initial moderate BJ14 cap was reached. Its plan/document was reviewed; its initial representation used a common denominator also for per-node maxima. This independent backend had separately chosen unreduced per-node maximum pairs before code/tests. The exact integer comparison identity was communicated for a prospective producer revision, without sharing/importing implementation code. No further degree20 rule has been authorized or executed by this worker.

Actual authorized pilot invocation:

```sh
python -B topics/padua-lanczos-frontier-20261105/code/g1_fast_independent_pilot.py --out /tmp/padua-lanczos-frontier-g1-fast-independent/pilot20-bj --old /tmp/padua-lanczos-frontier-g1/inputs/e1-full-sweep.json --benchmark-receipt /tmp/padua-lanczos-frontier-g1-fast-independent/benchmark14-receipt.json --benchmark-endpoints /tmp/padua-lanczos-frontier-g1/benchmark14/rotated-bj/endpoints.json --receipt /tmp/padua-lanczos-frontier-g1-fast-independent/pilot20-bj-receipt.json
```
