# G1 batching: prospective exact identity and bounded cost plan

Rules/input SHA `9825d184517db81d0aad8542fbd6639f2164b803`, base
`aff30e8ad5542c94fab642ae024dc9aab4fa7ad7`. Codex technical developer,
requested gpt-6.1-sol medium. Root alone controls Git. Read current rules,
handoff05, attempts/L1 G1, g1-optimization and frozen g1-fit-spec. This is
an exact representation implementation of the saved proposal, with no new
scientific mechanism or novelty claim; the novelty gate exception is scoped
to that implementation. Historical source and all receipts are preserved.

## Identity and invariants registered before coding or runs

For vectors v_j=z_j/D_j with D_j>0 and rational coefficients c_j=a_j/b_j
in reduced form with b_j>0, form L=lcm_j(D_j*b_j) over nonzero c_j.
Then sum_j c_j*v_j is exactly the integer row
sum_j [a_j*(L/(D_j*b_j))]*z_j divided by L. Normalize common content once
after the complete sum. Empty/all-zero sums return the M-entry zero vector
with denominator1. Dimensions must agree even for zero-weight terms.
Signed weights, cancellation and non-coprime denominators are retained.

Use this identity for each basis projection residual u-sum alpha_l*b_l
and each response column coord_axis*g_parent-sum alpha_l*g_l. Coordinate
multiplication and exact dot/norm operations remain unchanged. For each
formed column, all its frozen terms are included; summation order cannot
change a rational value. Consequently the basis residual/norm, pivot score,
X tie choice and recorded ties must remain exactly equal, checked against
fresh scalar construction. The derivative recurrence/source identity and
energy/peak/normal/endpoints are unchanged. All325/625 original nodes, all
source columns and every frozen L/H/Urow/upper endpoint remain mandatory.
No parity compression, gauge change, source truncation or fitting occurs.

## Prospective bounded sequence

1. Extend deterministic primitive controls to signed/zero/repeated terms,
   common factors, cancellation and malformed dimensions. Compare against
   direct fmpq scalar sums.
2. Eight degree4 cases on both grids/four rules, max2 workers and120s per
   case. Each already compares fresh scalar degree2/3/4 basis, norms,
   recurrence/choice data and old endpoint values.
3. Eight maxdegree12 cases, same120s/max2 limits, requiring all88 legacy
   endpoint/choice/tie rows. Compare full uncompressed baselines to v2.
4. Only after success, one rotated BJ14 case, cap180s, comparing all13
   rows including frozen13/14. Record wall/CPU and basis times. If >60s,
   stop before20 and identify the next real measured cost bottleneck.
5. Root conditionally preauthorizes one rotated BJ20 producer only if the
   same source completes BJ14 in<=60s and matches old13/14. Cap600s; all19
   rows must match independent native output at
   /tmp/padua-lanczos-frontier-g1-fast-independent/pilot20-bj/rotated-bj-d20.jsonl.
   No other20 or cap extension is authorized. No fit before all152 rows.

Before each run, save source/input identity, environment and exact argv in
/tmp/padua-lanczos-frontier-g1-batch. Raw regenerated outputs stay there;
repository receipts stay below16KiB. Retain failures/cost stops as evidence,
not scientific rejection. Distinct technical and mathematical reviewers
receive the source/plan; their review/execution is separately recorded.

At registration: no changed source and no new scientific run exist.

## Execution checkpoint: source 4b705ac8

Stable new source SHA-256
`4b705ac8b6f4dced7d08e049d3b4f62fa4cf712a1f5ed34f0627f37875a386ee`
was recorded before the primitive/small runs. Python3.12.14, python-flint0.9.0
from `PYTHONPATH=/tmp/padua-lanczos-frontier-g0/deps`. The first primitive
import and attempted small launch omitted PYTHONPATH and failed before
scientific computation with ModuleNotFoundError; retained in scratch
`failed-no-pythonpath-small`. No source change was needed. Corrected run
passes batched signed/zero/repeated/cancellation rational controls and11
malformed controls; all eight degree4 cases complete, comparing all24 old
endpoint rows and fresh scalar degree2/3/4 basis/norm/recurrence prefixes.
The exact per-case argv/hash/environment were saved before each corrected
launch. Maxdegree12 overlap currently pending; no14/20 completion claimed.

All eight maxdegree12 cases completed under120s/max2 workers and match all88
old endpoint/choice/tie rows. The complete uncompressed baseline dumps are
byte-equal to v2 for every case (all nodes, norms and recurrences). Compact
receipt: `evidence/g1-batch-overlap.json`,10597bytes. Rotated cases now take
30.365–37.660s; these observations are scoped to this run's resource conditions.
The single planned BJ14 benchmark has begun after overlap success. Root
additionally authorizes one degree8 profile capped30s if BJ14 exceeds60s,
solely to identify the remaining bottleneck; no automatic further optimization.

## Actual BJ14 cost stop and authorized profile

The unchanged4b705ac8 source completes rotated BJ14 with all625nodes and119
sources in79.050139s wall/79.006266s CPU, basis1.180068s. All13 endpoint rows,
including old13/14, exactly match the retained frozen benchmark. This fails
root's <=60s producer20 prerequisite. **No producer20 was run.** Native BJ20
remains a separate execution without fresh producer agreement for its new rows.
Receipt: `evidence/g1-batch-benchmark14.json`.

Root-authorized same-source rotated BJ8 cProfile, cap30s, completes in about
5.67s, all625nodes/all44sources and seven old rows. Profiler reports5.734s
total, with5446 V constructor calls consuming3.421s self time (59.7%).
The common-content normalization in V.__init__ is therefore the measured
remaining bottleneck at degree8; linear_combination cumulative1.778s,
scale1.269s and add1.040s overlap those constructor calls and must not be
summed as disjoint costs. Basis costs only0.209s at degree8 and1.180s at14.
The profile is diagnostic finite-scope evidence, not a high-degree complexity
claim. Raw launch, pstats, text and exact receipt are in scratch profile8/.

A possible next bounded implementation would fuse square/scale/energy
addition to normalize once per completed energy vector, or use native
vector-content normalization; this is **unimplemented and unrun**. Any next
round requires root's prospective scope and new validation. This round stops
at the failed60s cost condition rather than relaxing it. No fitting, scientific
kill verdict, all152row completion or asymptotic conclusion follows.

All new scratch files are indexed by `inventory.json` with byte/hash identity;
raw outputs remain temporary outside Git and Windows archive delivery is
pending. Initial missing-PYTHONPATH failures, before-source and batch-source
snapshots, plan bytes, per-run exact argv/environment/source hashes and
completed exact endpoint/baseline outputs are retained.

## One further root-authorized fused-energy revision: prospective plan

Registered after the actual79.050s BJ14 cost stop and degree8 normalization
profile, before changing source or executing a new run. Source4b705ac8 and all
prior receipts remain preserved; root is checkpointing them before edits.
This is one bounded implementation round only; failure stops without an
automatic loop. No new scientific mechanism or novelty claim is introduced.

Let S=z/D, g=y/E, and c=a/b be exact rationals with D,E,b>0. The pointwise
update S+c*g^2 equals the integer row

    z*(L/D) + (y pointwise squared)*a*(L/(b*E^2)),
    L=lcm(D,b*E^2),

with common denominator L. Construct that integer row and normalize once
at the completed update. Zero/negative c and exact cancellation are handled
by the same formula; dimensions are checked before zero shortcuts.

The frozen source-scaled energy identity is
S_h += tau_h^2*g_k^2/d_k, with tau_h^2=sigma_h from the exact base recurrence.
Current code stores E_h=S_h/tau_h^2, updates E_h+=g_k^2/d_k, and applies
sigma_h at collect. This organization will remain: fuse only the existing
response-energy square/scale/add into one primitive with c=1/d_k. The
initial energy1/d_h and collect's source scaling, normal diagonal, peaks,
basis/response column batching, all nodes/sources, ties and endpoint formulas
remain unchanged. No other fusion is included in this prospective round.

Validate the new primitive against direct fmpq pointwise arithmetic with
signed/zero/non-coprime/cancellation values and malformed dimensions. Then
repeat all eight small cases/fresh scalar degree2/3/4 controls and all88 old
rows, at120s per case/max2 workers. Compare complete baseline bytes to the
prior stable implementation. Only after these pass, run one rotated BJ14
cap180s comparing every old row including13/14. The unchanged root condition
allows one BJ20 cap600s only if this same source completes14 in<=60s and
agrees exactly; compare all19 rows with retained native BJ20. Otherwise stop.
Record all source hashes, exact commands/environment and results before runs,
retain all failures/cost stops, and perform no fitting before all152 rows.

Fused-energy source SHA-256
`49b45df9c2c28e3e63e9b886ff873a744ea0f0a44cd5f51fe2e3a345eec81552`
was recorded before new runs and copied to scratch `fused/source-fused.py`.
New direct rational signed/zero/cancellation controls pass and12 malformed
controls reject. All8 small cases pass fresh scalar degree2/3/4 and24 old
endpoint rows. Distinct technical checker inspected the primitive, exact
source-weight placement and single call site, reporting no defect. Old88
and new14 are pending at this checkpoint; no20 has been launched.

Fused round old88 validation completes under120s/max2workers. Every full
baseline is byte-equal to v2 (and hence to prior4b705ac8); all old endpoint,
choice and tie rows agree. Rotated12 times27.499–37.441s; T24 times3.068–4.334s.
Compact receipt: `evidence/g1-batch-fused-overlap.json`. The planned stable-
source14 benchmark is now running after these passes.

## Final fused round outcome: stop under unchanged cost condition

Stable49b45df9 completes rotated BJ14 in72.526631s wall/72.503146s CPU,
basis1.454791s. All13 endpoint/choice/tie rows, including frozen13/14, agree
exactly with the retained old benchmark. Receipt:
`evidence/g1-batch-fused-benchmark14.json`. The unchanged <=60s prerequisite
fails again, so **no producer20 was run and no further optimization loop was
started**. Prior4b705ac8 and both older cost stops remain preserved.

The observed79.050->72.527s change is a finite measurement in this environment,
not a controlled universal speedup or complexity bound. The prior degree8
profile motivated energy fusion; this round did not execute a new profile,
so no new precise hotspot percentages are claimed. Remaining normalization
and native/vector arithmetic are possible next implementation costs, but
further diagnosis/development needs a separate root scope. This bounded
assignment is complete at the honest cost stop. No scientific target is
rejected, no152row completion or fresh native20 agreement is claimed, and
all preregistered fit/operational rules remain unexecuted.
