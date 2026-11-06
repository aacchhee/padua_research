# S4 Padua cost/grid proposal — no new runs

Date2026-11-06. Assigned gpt-6.1-sol medium. Coordinator requested an exact
proposal before registration. Canonical machine-readable protocol:
[S4-padua-proposal.json](../S4-padua-proposal.json).

Use the unchanged pinned matrix-free product-Legendre tensor operator.
No unvalidated fast Legendre conversion is proposed. Upper uses ordinary
ARPACK ncv80 (lower40), with explicit matvec/time caps and residual checks.
Existing K0 replays only covered even minima, so all16 scan rows would run
fresh with seed20261106, including both parities and both extremes where
completed. Pilot800/801 belongs to the prescribed first fit window.

Two disjoint4-point even windows are800,1000,1200,1400 and1800,2200,2600,3000;
odd cases add1, using physical m in logs. Separate signed extrema and
parities fit intercept+slope*log(m/mref), unweighted scaled-column SVD.
Stability requires slopes of the expected sign, magnitude>=1e-4, <=5%
relative drift between windows, and small fit residual relative to the
observed slope contrast. Details and exact acceptance formula are in JSON.
Only stable signs reach the10% K4 comparison. K5 parity equality requires
both stable parity fits plus <=5% slope difference. Both gates remain
finite measured diagnostics. The four-decimal S3 comparison values
−0.1336,+0.0456 describe an uncertified finiteK128 model approximation;
large model truncation drift prevents treating them as certified full norms.

Cost evidence inspected before proposing any run: pinned cleanup
scan-summary.json records minimum1600=93.36s,2000=212.70s,2400=376.77s,
3000=648.40s at122 matvecs. This predicts about1CPUh for16 minima,
with conservative2h allowance. Pinned frontier report states upper600
stopped after640s without completion. Thus upper is a major cost risk,
not a promised affordable scan. At2000matvec cap, worst-case all16 upper
rows are roughly16CPUh; proposal runs even800 FIRST and stops upper immediately if it fails,
without interpreting a partial Ritz value as an extremum. Pilot hard cap is30min or2000matvec, whichever first. A successful pilot
must also forecast totalupper<=16CPUh and anyrow<=6h before extensions,
using2*pilot_time times the sum of cubic degree ratios. No larger upper
run follows a pilot failure unless coordinator first registers a revised
method. Lower can proceed independently. Reserve24CPUh including selected
checks; individual extreme<=6h and session cumulative<=48CPUh.

At3001 the basis dimension is4504501. ncv80 uses about2.88GB for its Krylov
basis; total process forecast4–5GiB including arrays and BLAS temporaries.
Read-only cgroup memory limit is16GiB. At most two degree processes concurrently;
initially one minimum process plus upper even800 pilot, with at most two
large minimum processes thereafter. Other campaign memory remains available. ncv40 minima forecast2–3GiB.
Actual pilot memory and matvec rate must be recorded and forecasts revised
before proceeding if materially worse. NoSyvert or background large runs.

Validation/independent rerun plan covers signed weights at10/11 via
Chebyshev moment systems, dense extrema20/21, first800/801 minima/maxima,
and selected largest affordable completed rows with a distinct seed.
Compact essential evidence retains source/environment/seed/weight/residual
identity; arrays and full debug logs remain local, not Git. No new spectrum
or slope fit has run while writing this proposal.

Coordinator clarification incorporated before registration: upperpilot even800 first, hard30min/2000matvec; upper extension only after successful guarded pilot and bounded conservativeforecast. Scaled fit condition<=100 and rank2 required before any interpretation. No old-history fits used to choose thresholds.
