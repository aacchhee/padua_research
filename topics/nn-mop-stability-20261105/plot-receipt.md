# Conditioning figure — plotting receipt

2026-11-05. Routine presentation follow-up, Codex dispatched gpt-6.1-sol medium; backend model/effort not independently exposed. Rules/input head `823cf6a4ef7c01b4ef3d2a6fec3e9f19d4b4f6f1`; round-1 output published by coordinator as `f75964b`. Only the plotting producer and this receipt are new; frozen D2 files were not edited. No Git/shared-state operation.

## Executed sampled figure

```sh
python topics/nn-mop-stability-20261105/code/plot_conditioning.py --krawtchouk /tmp/conditioning-krawtchouk260.json --hahn /tmp/conditioning-hahn260.json --outputdir /tmp/nn-mop-conditioning-plots-sampled --grid-label sampled8sizes --bound-source topics/nn-mop-stability-20261105/theory/conditioning-lower-krawtchouk.md --bound-sha256 9047c95c8bc8b6ca6ecb0dae5eab6ff1517be428bee501c9f16ee2bff164c53e
```

Exit 0. Two panels show Krawtchouk and Hahn NN versus monic step-line condition numbers at exactly N=4,8,12,16,24,32,48,64. Caption explicitly says sampled 8 sizes; machine grid label is `sampled8sizes`. Numerical values are from each case’s NN/mixed/kappa and step_line/mixed/kappa, without fits or substitutions. These use the same mixed input norm and different representation output field norms: four NN fields and three monic step-line fields. No stability conclusion follows from this figure.

Dashed Krawtchouk curve renders the maximum of the frozen source’s lower bounds (1), (2), (13), evaluated in binary64 for display:

    5^(N−1)/(N−1),
    (4 sqrt(6))^(N−1)/[4(N−1)(N−2)],
    5[(5+2sqrt(6))^(N−2)+(5−2sqrt(6))^(N−2)]/[2(N−1)^2].

The source labels its analytic proof PROVED and mandatory Claude audit pending; the plot preserves that audit qualification. The plotting worker read its statement and addendum for the formulas, not an independent proof audit. No primary papers were used or copied. No novelty/new scientific claim is added.

PNG was visually inspected after rendering: title, family labels, legends, axis scales and caption are readable and unclipped. No additional plot tests were run. The initial renderer emitted a fontconfig cache warning; all three exports completed successfully.

## Identities

Python 3.12.14; matplotlib 3.10.8. PNG uses 220 dpi; PDF/SVG are vector exports. PDF timestamps and manifest creation time can change raw hashes on rerun.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `/workspace/scratch/nn-mop-stability-20261105/topics/nn-mop-stability-20261105/code/plot_conditioning.py` | 8114 | `372588a8d0c8aeb2f2b07fe1433e94647301b52af161e459a588ce0887a5ca16` |
| `/tmp/conditioning-krawtchouk260.json` | 231010 | `f9c1677849676796974ba4c8545f44b29f70c7ca72d84e5d3b7581f9c6581bd6` |
| `/tmp/conditioning-hahn260.json` | 232208 | `38d725745fb21a5e48304c39b31360ec4c9a564ff539cb4a5aef16e171734b1b` |
| `/workspace/scratch/nn-mop-stability-20261105/topics/nn-mop-stability-20261105/theory/conditioning-lower-krawtchouk.md` | 13005 | `9047c95c8bc8b6ca6ecb0dae5eab6ff1517be428bee501c9f16ee2bff164c53e` |
| `/tmp/nn-mop-conditioning-plots-sampled/conditioning-sampled8sizes.png` | 181424 | `e6113789e8d79f2af9a56886eb1b1ce17957bcc58ec637dd22406ea025c50eb9` |
| `/tmp/nn-mop-conditioning-plots-sampled/conditioning-sampled8sizes.pdf` | 21953 | `69df297163d8dc07518485f41d1e82945722ddac37c39432eaede17f515a0e1e` |
| `/tmp/nn-mop-conditioning-plots-sampled/conditioning-sampled8sizes.svg` | 35200 | `91645f9ec9dd3bca6b11785e9cdbbc1132a81185a6942b6059f3bd44180c1241` |
| `/tmp/nn-mop-conditioning-plots-sampled/conditioning-sampled8sizes-manifest.json` | 2987 | `858eeab1da94d07f2032ca9a0c502176f689058e87bd6cf1ccbafd059f797d5c` |

The output manifest records explicit input paths, source-code hashes, derivative-producer hashes, decimal precision, formulas, versions and command arguments. Missing/invalid/empty data, mismatched families or grids, and a changed lower-bound source hash fail explicitly. It never searches for replacement data.

## Full every-integer grid

At this receipt’s creation `/tmp/conditioning-full-krawtchouk260.json` and `/tmp/conditioning-full-hahn260.json` were still empty, because their producer writes complete JSON only on completion. D1 reported remaining work at approximately N45–46 and about 15 minutes; no full-grid figure is claimed. Execute after those explicit inputs are complete (script requires every integer 4..64):

```sh
python topics/nn-mop-stability-20261105/code/plot_conditioning.py --krawtchouk /tmp/conditioning-full-krawtchouk260.json --hahn /tmp/conditioning-full-hahn260.json --outputdir /tmp/nn-mop-conditioning-plots-full --grid-label fullgrid61 --bound-source topics/nn-mop-stability-20261105/theory/conditioning-lower-krawtchouk.md --bound-sha256 9047c95c8bc8b6ca6ecb0dae5eab6ff1517be428bee501c9f16ee2bff164c53e
```

This command is **not yet executed**. Recheck the theorem source if its explicit hash changes; no automatic fallback is permitted. All exports and raw manifests stay under /tmp, off Git, with archival transfer pending the coordinator’s cold-storage procedure. Code and this short receipt are the durable regeneration artifacts.

## Dated completion — full every-integer grid, 2026-11-05

The deferred full-grid command printed above was now executed exactly as recorded and returned exit 0. The earlier pending statements describe the sampled-figure stage and are retained as history; this addendum completes that plotting step. Both explicit 260-dps input JSON files contain all 61 integer sizes N=4,...,64. The manifest records exactly that size grid, `fullgrid61`, and caption “Every integer size N = 4,...,64.” No alternative files, extra experiments or data substitutions were used.

The full-grid PNG was visually inspected: both family titles, NN/monic step-line legends, logarithmic condition-number axis, integer-grid caption and the analytic lower-bound audit qualification are readable and unclipped. The same plotting code and frozen lower-bound source were used unchanged.

| Full-grid artifact | Bytes | SHA-256 |
|---|---:|---|
| `/tmp/conditioning-full-krawtchouk260.json` | 1762900 | `eca8cd52130467cf8e0cb446053751a37d9bc6db227b8fa20ecf7dc28b63df83` |
| `/tmp/conditioning-full-hahn260.json` | 1764070 | `6b4745430e2bad7a99b89e72ec72631b343e20bc83aa6981294a9d50c857634e` |
| `/tmp/nn-mop-conditioning-plots-full/conditioning-fullgrid61.png` | 178595 | `5532ce4bc8e6f37f91b0bdb2f8f07d873c7b48b580344be4c99b995fc690a19f` |
| `/tmp/nn-mop-conditioning-plots-full/conditioning-fullgrid61.pdf` | 22104 | `2ff392f34aa1fb6fe5e74a323fc13f47ae64ddfb0b1442bc88e3ca594273dcfb` |
| `/tmp/nn-mop-conditioning-plots-full/conditioning-fullgrid61.svg` | 35181 | `ab7cb72448f5ad65653cf2ac883f5e86f7433e70d7ca0495571971d62a927125` |
| `/tmp/nn-mop-conditioning-plots-full/conditioning-fullgrid61-manifest.json` | 3384 | `642b4c5606323a7bc72566331f53e273c11ee1d7730222e7bec56f4a1cab147f` |

All PNG/PDF/SVG exports and their manifest remain local under `/tmp/nn-mop-conditioning-plots-full/`, off Git. Existing sampled exports are preserved. No D2 scientific files, shared files or Git state were changed.

## Response prose-pin maintenance — 2026-11-06

The historical commands above identify their original proof version atff783d5.
Response parent links/completed-check metadata changed that prose file's response-d6760d7
SHA-256 to `d3e284444d7caad48d20b01e4da0966bd9fd2c78b6dae307b39e860fe4cde0b3`; formulas(1),(2),(13) are unchanged. A rerender against
that response record must pass that version’s value to --bound-sha256. No numerical
data or figure was reselected/rerendered for a metadata-only correction.

2026-11-06 preparation: final-ID/alias metadata gives the lower-bound record SHA-256 `d76498e95495c6bea8842d946c0bd169d6075c78ef915f82dcfc84c4a63a7aa9`; use that value with --bound-sha256 for a future rerender of this prepared version. The mathematical formulas/data and historical figure artifacts are unchanged; no rerender was performed.
