# PD-N?padua-3d-20261106-codex-U3-C1 — the complete septic nonunique-support list loses its quality gate

ID kind: PD-N. Aliases: all-28 nonunique half-shift quality boundary.
Split from: none. Split into: none. No final ID allocated.

## Statement and definitions

For n=7, N=120 and every one of the 28 explicit tuples z=(1,b,c) in
[the prospective protocol](../u3-continuation-protocol.md), take
X_z={(cos(theta_k),cos(b theta_k),cos(c theta_k)):0<=k<120},
theta_k=(2k+1)pi/240. All 28 pass the stated floating condition/residual
screen, but none matches or beats the inherited QR control on both the
21^3 and 41^3 tensor Lobatto quality meshes. In fact each loses on each
mesh, with

```
min_z L21(X_z) = 136.690399705     L21(QR) = 26.9350723193
min_z L41(X_z) = 136.690399705     L41(QR) = 27.5621519888
min_z max(L21(X_z)/L21(QR), L41(X_z)/L41(QR)) = 5.07481094110.
```

Here L_m is the directly computed floating lower sample of the Lebesgue
function on the entire m^3 mesh; the displayed digits are rounded. No
interval enclosure, continuum norm comparison or certified supremum is
claimed. All 28 also lose to the inherited Leja control on both meshes;
the smallest candidate/control ratio is 2.74409352492.

## Assumptions, status and negative-result scope

Overall status: **MEASURED**. Candidate
IDEA?padua-3d-20261106-codex-U3-C1's specified finite competitive
interpretation is **REJECTED: failed**. The failed mechanism here is the
use of one of these 28 already identified degree-seven half-shifts to pass
the frozen finite QR gate. This is not a rejection of odd-degree cyclic
interpolation, other phases/generators/folds, a mixed partition, the general
cyclic-block inverse route or the asymptotic 3D Padua target.

Nodes, basis order, unscaled product-Chebyshev evaluation, 21/41 meshes and
inherited QR/Leja rules are frozen in the linked protocol. The complete
candidate domain comes from the prior exact full-rank classification in
[interim U3](../interim-audit-01/U3.md), not from new quality selection.
Each tuple is retained, including labels representing symmetry-related
quality values and the old T8 Hdet tuple `(1,17,212)`.

## Depends on, checks and evidence

The [sparse DCT classification](u3-sparse-classification.md) supplies the
exact alias factorization. The [half-shift theorem](t8-r08-halfshift-obstruction.md)
supplies the unchanged count/action reduction; its even-degree exclusion
does not exclude n7. No new load-bearing published theorem is imported.

Actual command, from repository root, after protocol publication
`739982c90e150c586f27e29816b6a735468c9716`:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-3d-20261106/code/u3c_nonunique_quality.py --receipt topics/padua-3d-20261106/evidence/u3c-nonunique-quality.json
```

The [receipt](../evidence/u3c-nonunique-quality.json) records the executed
source hash, inherited dependency hash, complete input identity, actual
versions/threads/command and all 28 compact numerical rows. Before quality,
every count was checked rationally, each actual-node matrix had a nonzero
determinant at both verified splitting primes, and QQ inverse products
and the prior exact inverse sums/norms were checked. These checks retain
the existing finite full-rank conclusions; no new PROVED claim is added.

Observed condition2 ranges from54.5710 to123.9288 and every infinity norm
node residual is at most2.9275e−13, well inside the 1e12/1e−7 screen.
Thus numerical suppression explains none of the losses. Every candidate's
two quality values, maximizers, certificates and exact inverse diagnostics
are preserved in the regenerate-only raw catalogue; its identity is in the
receipt. The compact receipt retains every candidate, not favorable samples.
No external cold-storage delivery is claimed or required for regeneration.

## Sources and limits

Known cosine aliasing and matrix diagnostics; no novelty/priority claim.
[Continuation](../u3-continuation.md) records reading/source coverage and
execution chronology. Large coefficient inverse sums were not used as
Lebesgue lower bounds. The old Hdet quality is reproduced, not relabeled
as an unseen discovery. These lower samples do not compare the true
continuum suprema and do not establish asymptotic growth.

## Open items and history

The prospectively registered q<=1 success gate fails, so this particular
degree-seven quality route stops; one further round is completed and six
of the current seven-round allowance remain unused. A second round needs
a useful quantitative inverse argument or positive competitive evidence
under a fresh scope. The broad U3 stable minimal-family goal stays OPEN.
The distinct [independent receipt](../continuation-review/evidence/u3.json)
reconstructs every full240-parameter coset/count, both actual-node ranks,
both controls and both full meshes with separate scientific code. It
confirms zero gate passes and the same minimum q, with candidate mesh
disagreement at most2.28e−13. This completed supplementary execution
does not replace the preserved formal Claude audit or promote a floating
measurement into a computer proof.

2026-11-07, Codex developer assigned gpt-6.1-sol xhigh; rules/input
`97c323bfae15cf3c76f40802c3ebabedceeb0c60`, runtime metadata unexposed.
The exact candidate scope and gate were published before execution; no
quality-guided source change, threshold change, selector or extension occurred.
