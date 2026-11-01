# PD-T?argmax-alln-claude-02 — Float64 corner-gap profiles along the edges and near-edge strips, and n = 2 scans

ID kind: PD-T.
Aliases: edge gap profile; horizontal-edge gap ≈ 1; n = 2 scan.
Split from: none (supporting evidence for the OPEN target PD-T099; complements PD-T192).
Split into: none.

## Statement

In the float64 runs listed under Checks (Padua conventions of PD-T101), the following were observed.

1. **Vertical edges x = ±1.** The corner gap Λ_c(n) − (cell maximum of λ_n) over the cells strictly between the two edge-end cells is minimal at the central cell. The minimum is 0.6387, 0.5832, 0.5665 and 0.5571 at n = 12, 24, 48, 96. At 25 % of the edge the gap is 1.061, 0.844, 0.856 and 0.867. In the first cells at the node-corner end it is 1.924, 2.273, 2.682 and 3.135.
2. **Horizontal edges y = ±1.** The analogous minimum is 0.954 (0.938 on y = −1), 0.973, 0.986 and 0.993 at n = 12, 24, 48, 96, attained near the centre.
3. **Offset bands.** On one-cell-thick angle bands at offsets i = 1,…,5 from x = +1 or y = +1, maximised over the full other coordinate, the maxima found lie on a boundary with a perpendicular edge (n = 24, 48). Their gaps are between 1.09 and 2.49. These are separate bands between the i-th and (i+1)-st mesh lines, rather than cumulative strips 1–5 cells wide; code also prints i = 0 separately.
4. **n = 2.** On the 161×161 angle grid, max λ_2 = 3.00000 = Λ_c(2). The grid's non-corner edge maximum (2.9996) and interior maximum (2.9987) occur at grid points adjacent to a maximal corner, so they reflect continuity at the corner, not a separate competitor. A 4001-point scan of each edge finds λ_2 ≥ 3 − 1e-9 only at the corners (max 3 on x = ±1 and y = −1; 7/3 on y = +1).

No limit, rate or universal statement is claimed. In particular, part 4 is not a certificate for n = 2.

## Definitions

Cell = an interval between consecutive edge Lobatto ordinates, kπ/(n+1) on vertical edges and jπ/n on horizontal edges. Λ_c(n) is the non-node corner value (PD-T101). λ_n is evaluated by the reflected-lattice formula of `code/maj.py`, which was checked against Vandermonde inversion for n = 3, 4 in PD-T?argmax-alln-claude-01.

## Assumptions

Float64 NumPy/SciPy. Cell maxima come from a grid search (24 points per cell on edges) followed by bounded scalar refinement; strip maxima from an 8×8-per-cell grid followed by Nelder–Mead. No enclosures.

## Status by part

Overall status: **MEASURED**.

| Part | Status | Evidence / remaining gap |
|---|---|---|
| 1 vertical edges | MEASURED | outputs/edgeprofile.out; consistent with the proved limit gap g ≈ 0.5485 (PD-T192); not a proof of the profile |
| 2 horizontal edges | MEASURED | outputs/edgeprofile.out |
| 3 strips | MEASURED | outputs/strips.out; local optimiser |
| 4 n = 2 scans | MEASURED | outputs/maj_n2.out and outputs/n2_edges.out; certification needed (plan P0) |

## Depends on

PD-T101 (corner value). PD-T192 is used only for comparison.

## Checks

The commands were run from `topics/padua-argmax-alln-20261101/code/` (environment as in outputs/environment.txt):

```text
python3 edgeprofile.py 12 24 48 96 > ../outputs/edgeprofile.out
python3 strips.py 24 48 > ../outputs/strips.out
python3 maj.py 2 > ../outputs/maj_n2.out
python3 n2_edges.py > ../outputs/n2_edges.out
```

These were developer runs. Independent edgeprofile/strips/n2_edges replays now match byte-for-byte, as recorded in [independent-checks-claude-records.md](../independent-checks-claude-records.md). The standalone maj.py whole-square scan was not independently rerun. The Codex source/scope review is [independent-checks-claude-observations-audit.md](../independent-checks-claude-observations-audit.md).

## Sources

None.

## Proof or evidence

Evidence only: the committed outputs above.

## Scope and open items

These observations motivate plan v2 §3–§4 (P0, P1, P2, P5) and tests T1 and T5. A whole-edge theorem would supersede parts 1–2 (plan P1/P2). An exact certificate for n = 2 would supersede part 4.

## History

2026-11-01, Claude (claude-opus-5-5): created during handoff 01 (plan update after PR #12).

2026-11-01, Codex gpt-6.1-sol xhigh, responding to independent Astra scope finding C-01: the original part3 wording was "strips 1–5 cells wide adjacent to x = +1 or y = +1". It is corrected to one-cell-thick bands at offsets i = 1,…,5, matching the unchanged code/output. No numerical evidence or epistemic status changed. The independent replay paragraph now distinguishes completed six-script coverage from the unrerun standalone scan. The separate exact degree-two proof codex-02 closes P0 without upgrading these floating observations.
