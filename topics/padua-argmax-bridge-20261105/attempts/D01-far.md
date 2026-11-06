# D01 far: signed-component diagnosis and fixed-strip obstruction

2026-11-06. Rules/input `4cf68980fa0538b53e2aea7174ed6e5782a34908`.
Codex mathematical developer, parent-requested work; serving model/effort
metadata not independently exposed. Technical implementation and execution:
`/root/d01_far_code`. Root alone owns Git and shared state.

Scope: handoff08 B2 / audit01 P1 T1-a,T1-c, within the new post-audit D01
round. The closed campaign stays 15/15. No producer, new degree certificate,
near correction or change to the old M_far/C13 definitions occurred.
The fresh candidate gate is in [ideas/D01-far.md](../ideas/D01-far.md).

## Pre-run contract and implementation

[SPEC](../code/post_audit_D01_far/SPEC.md) was frozen before native
execution; its SHA256 is
`691c5bd548044a42dbdf5a165976eda1b208f340471d75b4d27156016e706dee`.
It defines an exact additive telescope, fixed cutoffs, exact collision
classification and the phase-input identity. The backend accepts rational
multiples of pi: decimal-radian phase labels were converted to recorded
rational normalized phases, then the same actual inputs were used in the
floating model. Only (pi/2,pi/2) is the exact named boundary phase.

The accepted C11 O(n) point backend was snapshotted, leaving original
files unchanged. Side-channel row captures and exact-rational classifications
give endpoint, collision and central rows. Accepted partial-cotangent sums
give the separate ordinary pole norms, so E and D are measured separately.
There is no n8192 O(n^2) board loop. Floating model integration is distinct
from the native bounded arithmetic; the final components remain MEASURED.

N1-08 requires n>=ceil(2*pi*64/.01)=40213, whereas all requested degrees
are smaller. In fact delta*m/pi<R at every case. The first/last R rows
extend beyond the strip and no ordinary endpoint row remains. The signed
Q_actual is therefore zero. The exact telescope still holds, but its mesh
and interior terms necessarily compensate for this geometry. The old
positive error formulas are printed separately with inadmissibility flags.

## Execution and evidence

Commands actually executed by the technical owner:

```
python3 topics/padua-argmax-bridge-20261105/code/post_audit_D01_far/supervise.py
python3 topics/padua-argmax-bridge-20261105/code/post_audit_D01_far/finalize.py
```

One numerical attempt, all 12 cases completed, exit0. Supervisor-inclusive
CPU182.246419s, wall175.624561s, below the 600 CPU-s cap. Metadata-only
finalization used0.024848 CPU-s separately. No numerical failure, retry,
tuning, rescue or extra degree. Python3.12.14, NumPy2.3.5, SciPy1.17.0.

Compact receipt: [evidence/d01-far.json](../evidence/d01-far.json),
14945 bytes, SHA256
`10b8b2800b6ac910ce50eb43f50005b409388f664a3d8dc5ea2d62ab59323c1d`.
It records source identities, exact normalized inputs, numerical intervals,
all signed components and bounds, runtime versions and raw hashes.
The code owner's [README](../code/post_audit_D01_far/README.md) describes
the complete build/native closure. Bulk row arrays and full manifest are
local in `local-output/argmax-bridge-20261105/post-audit-D01/far/`;
physical cold-storage delivery remains pending. The raw manifest is72195B,
SHA256 `10395fec369598ba0cf8a24c22a26eaf41ed2e1b10f12332b08722013ee5b5ab`.
This mathematical owner read the outputs and source; that is review, not
an independent numerical rerun.

Small n32/n128 side-channel totals matched the unchanged native point
entry exactly and overlapped the accepted controls. The midpoint constant
oracle, tightened quadrature and all row partitions passed. Largest
additive telescope discrepancy:8.66e-15. Every represented collision class
was empty; both central rows were retained. Only the prescribed even
degrees were executed, so no new odd-degree/collision coverage is claimed.

## Measured results

Signed S-M_far:

| n | .25,.25 | 1.38,0 | 1.45,1.45 | pi/2,pi/2 |
| ---: | ---: | ---: | ---: | ---: |
|512|.003892419614|.004842103997|.001009722031|.000092163121|
|2048|.001224811935|.001475819596|.000898571241|-.000839248563|
|8192|.000378370361|.000441159810|.000926413590|-.001072314564|

At n8192 the actual signed components are:

| Component | .25,.25 | 1.38,0 | 1.45,1.45 | pi/2,pi/2 |
| --- | ---: | ---: | ---: | ---: |
|endpoint actual minus sinc|-.000476749679|-.000194071015|.002287497694|.041988926866|
|mesh|4.019936864474|2.671821260130|1.007079267505|.553348220366|
|ordinary interior quadrature|-4.019597349698|-2.672130053413|-1.009079267779|-.597173257421|
|central|.000391060484|.000798021104|.000759194834|.000763795586|
|E_actual|.000124533563|.000145998956|-.000120279162|0|
|D_actual|1.12162e-8|4.04859e-9|4.96916e-10|3.98419e-11|
|collision|0|0|0|0|
|Q_actual|0|0|0|0|
|sum of absolute components|8.040526569|5.345089409|2.019325507|1.193274200|

The receipt contains the same full signed mapping at n512 and2048;
these are actual quantities, not the old coarse positive upper bounds.

T1-a success is **NOT PASSED**. The absolute sums greatly exceed2L/n
away from a=0. Its proposed asymptotic O(1)>0.3 kill is **OPEN**: the
large mesh/interior cancellation is caused here by using the fixed R
block below its strip-admissibility domain. It does not establish an
irreducible O(1) obstruction after a justified joint treatment. No T1-b
validated cover is released. In particular the tiny measured E,D,Q
values do not erase the large exact mesh/interior compensation.

## T1-c: what is proved and what is measured

**PROVED**, independently of this run:
[the standalone midpoint identity](../theory/D01-far-midpoint-identity.md)
gives the exact finite-n residual and its strictly negative fixed-delta
limit b_delta. [The scoped obstruction](../theory/D01-far-contract.md)
therefore refutes a uniform C(L+1)/n bound for the unchanged model on
the full closed diamond. The residual is O(delta), not O(delta^2), at
the midpoint phase cusp. No term is added to M_far.

**MEASURED** boundary controls:
b_.01=-.00115002219528744. The independently simplified model constant
agrees with tightened quadrature within1.38e-14. Finite-n S-M agrees
with the exact identity to below2e-14 at n2048/8192; the maximum discrepancy
over the three tested degrees is6.16e-13 (at n512), within the theoretical remainder bound
1/[4n²(n+1)²]. Halving and quartering delta give
-.0005750118689134112 and-.0002875060308652985. These are parameter
sensitivity diagnostics, not adopted replacement models.

**MEASURED** interior control at the represented (1.45,1.45) phase:
tightening quadrature changes the model constant by-4.90e-13; correcting
old K4096 g_R tails changes it by-1.77e-9, with weighted EM remainder
below9.04e-22 (floating roundoff is separate). Thus the observed
approximately9e-4 error is not explained by either numerical effect.
The omitted-strip residual integral restricted to z in[1e-7,.01] is
+.000960616235, quadrature estimate1.23e-10. The z<1e-7 coverage is
OPEN, as is a rigorous identification of the whole interior limiting
residual; fixed-R cancellation and endpoint effects may also survive.
The exact midpoint already settles the uniform-decay question.

## Outcome and cheapest next test

T1-c is resolved: the unchanged full-diamond model has a genuine fixed
cutoff residue. T1-a supplies the requested additive anatomy but does not
pass its componentwise gate. Preserve P1 only with an explicit residual
allowance and a joint mesh/interior estimate appropriate to its actual
small-degree topology. The cheapest next step is a paper reduction that
keeps those cancelling terms together and specifies its margin budget
before any further run. No corrected model, all-phase enclosure, new
threshold or degree certificate is established here.

Runs needed: distinct mathematical audit of the standalone identity and
obstruction, plus an independent consequential numerical check selected
by the orchestrator within its own authorization. No additional native
run is requested or performed by this mathematical subagent.
