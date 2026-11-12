# PD-T?padua-3d-20261106-codex-T10-01 — exact finite lattice census

ID kind: PD-T. Aliases: shortest-dual census; folded Haar nodes. Split from:none. Split into:none.

## Statement and status

**MEASURED.** The committed code enumerates every row upper Hermite normal form through the first admissible determinant for n1,2,3, obtaining minima2,12,38. It separately checks the prescribed source/scaled/parity candidates through n16, records their exact degree and Π_n rank, and selects minimum folded size within this explicitly bounded catalogue. Unrestricted minima for n4..16 remain OPEN. Cools–Lyness's K-optimality is LITERATURE, not a global-optimality assertion.

## Definitions and assumptions

Rows of integer upper-triangular B span L. q=detB, H={h modZ³:Bh integer}; nodes are cos(2πh) with folded Haar multiplicities/q. N=binomial(n+3,3). Half-period shifts here mean a_j=0 or1/2 in torus units, hence angle shifts0 orπ, not half a sampling-grid spacing.

## Finite reduction and exact computation

Every sublattice of Z³ has a unique upper row HNF with diagonal a,d,f>0, 0<=b<d and0<=c,e<f. The script enumerates these for each q=adf, and tests every nonzero integer vector in the l1 ball of radius2n−1. No passing determinant below the returned minimum remains untested. All minimizers at that determinant are counted. This is a finite exact computation, and independent replay is recorded below. This historical result remains MEASURED as a conservative finite computation report; the new round08 exact claim is recorded separately.

For the rank reduction, expand each tensor Chebyshev polynomial as a sum of characters with frequencies (±α1,±α2,±α3), omitting repeated zero signs. Characters agree on H exactly when their difference is in L, tested as k adj(B) modq. If one of two distinct multi-indices has degree<n, any difference between its frequencies and those of another degree<=n has l1 norm<2n; thus their character supports are disjoint modulo L. Frequencies within any degree<n polynomial are also distinct. These nonzero, disjoint-support columns are independent and independent from the degree-n columns. Therefore only the binomial(n+2,2) top-degree columns require rational elimination. The code performs exact Fraction column elimination of integer frequency multiplicities; scaling a column by2 raised to its nonzero-coordinate count does not affect rank. If the minimum exceeds2n, all columns are independent. This argument is a routine algorithm reduction, not an independent unisolvence theorem for an untested family.

Folding uses integer numerators min(hj,q−hj), preserving multiplicity. A half-period shift multiplies each Chebyshev column by(-1)^(a·α), equivalently changes signs of physical coordinates, so counts, rank and exactness are unchanged for all8 shifts.

## Results and checks

`evidence/t10-census.json` records all83 tested family rows, source matrices for selected full-rank sets, hashes of exact node payloads, the complete HNF search counts, and controls. Padua n1..12 returns(n+1)(n+2)/2 nodes; the audit's q38 degree5 rule returns20 nodes and rank17. Every best full-rank set in this catalogue is the standard parity grid with orders(n,n+1,n+1), not a new mechanism. Its counts are5,12,26,45,75,112,164,225,305,396,510,637,791,960,1160,1377. At n16 the bounded best ratio is1377/969≈1.421; the n16 scaled K seed has2897 nodes.

Frozen producer: `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/t10_lattices.py census --raw "$T10_TMP/census.json" --out topics/padua-3d-20261106/evidence/t10-census.json`, with T10_TMP a fresh configurable directory. Raw catalogue is regenerate-only; hash/size are in the receipt. Independent replay: evidence/independent-r06-t10-global.json reproduces2/12/38 for n1..3 (audit03 companion NV-F11, applied2026-11-06).

## Sources, limits and history

Depends on T9-03's character exactness criterion and provisional LIT T10-01/02/03/04. No arbitrary phase, non-Haar weight, or half-grid shift search is included. Source table transcription is independently checked for degree, not for completeness of its K class. History:2026-11-06 Codex, Sol xhigh assigned, rules7afa6a54; initial finite result.

Dated response03 note2026-11-06: this table is the original bounded
catalogue, not the current unrestricted headline. Round08 separates
determinant, folded count and full-rank count. MEASURED is retained here
without the obsolete absent-replay rationale; no silent status upgrade.
