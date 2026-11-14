# C11 prospective fixed-order primitive pilot

Rules/input4ca11b81e4906b9789894907618b511a6a702423 (rules unchanged). Technical parameter tuning of accepted C02 mathematics and frozen C10 implementation, not a new mechanism or novelty claim. Only new C11 files owned; all old sources/receipts remain immutable.

## Scope checked and gate BEFORE implementation/tests

C02-row-cotangent.md §1 explicitly assumes every integer J>=1 and gives M_J=389120/(19683*pi^5)*(2J+3)^4*4^(-J); §2's fourth derivative tail proof and corrected midpoint formula apply to J16. No part of this pilot uses the stronger J96 all-row theorem or claims its2^-166 accuracy. Freeze ONE variant J16 instead of48; keep Arb160 main arithmetic, explicit640-bit moments, coefficient640 preparation, K32/L16/WD96 and all guards/assembly unchanged. Every changed smooth tail is recomputed from the formula and carried as radius. No order adaptation, rescue, or second variant.

Total<=30CPU seconds including compiler/helpers/supervisor. Before point costs: eight bounded partial endpoint-image controls at n2/3/7/33/64, same fixed inputs as C10, against512-bit direct cotangent endpoint hulls plus old accepted exact-rational J48 overlap; exact moments through degree33 at n2/7/33/64 and q1/n. Require valid containment, not n2 tightness. Then one point each at n32,128,512,2048, alpha/pi1/12,beta/pi1/16 in that order, stop first guard failure/cap. Desired measured point radius<1e-8; if it fails, report and stop, with no parameter retry. Compare known n32/n128 C10 diagnostic enclosures for overlap, allowing different radii. No large-n reference board, full candidate/cover/degree certification or whole-box adoption. Distinct review is required before use.

## Frozen variant and error contract

C11 partial.cpp differs from the frozen C10 partial.cpp SHA209fa24300219884b97ce267e898b085593534d97ecc31640909c4c772061ac5 in exactly ONE constant: J48 becomes J16. This exact byte transformation is asserted before/after execution. The fresh point.cpp is identical to the C10 include-only copy of accepted C07; its local include now resolves the new C11 partial source. All older files remain unchanged.

C02(1)--(3) are explicitly proved for J>=1, with no hypothesis requiring48 or96. Substituting16 changes the finite polynomial degree to33 and the smooth remainder to

    (7*q*(pi/n)^4/5760)
      *389120/(19683*pi^5)*35^4*4^-16.

This full outward bound is recomputed from J by the unchanged code and added to every successful partial block. The all-row assembly multiplies every complete block ball by the full coefficient balls and sums every ordinary row, so no row truncation or arithmetic radius is dropped. The harmonic K32/L16 remainder, WD96 derivative tail, coefficient uncertainty, explicit640-bit interval moment recurrence and160-bit outward input-radius propagation are unchanged. Coefficients are still prepared through WD96 at640 bits, because the stable derivative evaluator still needs them. There is no adaptive order or hidden exact-rational production fallback.

The main point API remains the guarded C07 rational-phase API on LP64. This tuning does not guarantee an absolute1e-8 bound for all degrees/phases or a whole phase box. In particular, wider n2 results are expected from the explicit analytic formula and are retained rather than relabeled failures. Numerical guard failures would still report failure; none occurred in this finite pilot.

## Executed once, after the local gate

Command:

    python topics/padua-argmax-bridge-20261105/code/cheap_rows_C11/control.py

Result PASS. Total parent-plus-compiler CPU5.928865seconds and wall5.932496seconds after driver initialization, with ample reserve below30CPU. No retry, failed gate, adaptive input/order or budget extension occurred. Startup/import time is outside the driver's elapsed timer; the complete job remains far below the cap.

Eight partial controls all contain512-bit direct cotangent hulls evaluated at the exact input-ball endpoints. Monotonicity on the guarded domain makes this a whole input-image check. They also overlap the frozen accepted exact-rational J48 backend. The fixed cases cover n2/3/7/33/64, q31/32/33, removable cells, both1e-30 pole approaches and a nonzero-width interval. Independent exact rational sums of normalized monomials pass272/272 checks: degree0..33, n2/7/33/64 and q1/n.

At n2,q2,y1/2, the returned radius is3.339952381331557e-7, compared with C10's1.1590152589422934e-24; this is a valid but intentionally wider partial sum. The right-pole conditioned input still has radius1.2196974444544e13 and the interval-input radius remains0.9959157165139914. No claim of uniform absolute accuracy is inferred from these cases.

After those checks, all FOUR fixed point calls succeeded once at alpha/pi1/12,beta/pi1/16:

| n | Point CPU | Point wall | Full S radius | retained/direct/blocks |
|---|---:|---:|---:|---|
|32|0.027631s|0.027639s|1.5326689082380968e-11|128 / 0 / 140|
|128|0.149856s|0.149877s|9.331751561395376e-14|512 / 0 / 588|
|512|0.584558s|0.584630s|4.974002020998141e-16|2048 / 0 / 2432|
|2048|2.455999s|2.456739s|2.4641722629481684e-18|8192 / 0 / 9804|

Every measured point radius meets the predeclared1e-8 desired accuracy. Ordinary row counts are62,254,1022,4094; maximum direct samples per ordinary row is0 in all these generic inputs. Maximum combined-channel block counts are4,6,6,6. These are the native counters, not inferred work estimates.

The n32/n128 outward binary64 enclosures overlap their preserved C10 same-input enclosures, as asserted. Their C10 point-call CPUs were0.161941/0.687725seconds under the same warm-process timing scope, compared with0.027631/0.149856seconds here. The smaller polynomial order reduces finite measured cost while increasing explicitly paid truncation radii. No claim about arbitrary phases, scaling law, cold starts, whole-box throughput or practical complete certification follows. New n512/n2048 POINT evaluations are cost diagnostics only; there is no finite-board reference, phase cover, producer, argmax certificate or extension of the certified degree range.

## Frozen identities and closure

- partial.cpp: bde1ce4850849dd402acc91eb3cee7d40883bbd51d5f7cff13334abc0f4ee23c.
- point.cpp: 6e2f1920ca293ac5a34f01c6369d94345b0d0c9b8a03d3e58ef15d453fbcf1d9.
- controls.cpp: 844e053a70bda2daa6a9ab969d395052eff4f366c438d14fe19226c776d50f56.
- control.py: 5bd4544d26562281d74f46ec58ae5be4cfb3d1523f03274ea5acfafbc171e252.

Small evidence/c11-row-order.json pins local raw `c11-row-order/check-a4xotnid/controls.json`,52788bytes, SHA4912bc984060d6ee032a3ed19f84a68e53b1ee75d42d42a935d6f65667e839f1. Complete raw identity closure includes203 source/header entries, four compiler tools,13 tool dependencies and eight linked/actual loaded mappings. Actual mappings match before/after. Exact build argv, preprocessed unit, compiler, binary SHA3651ac513455e685d9c05ccb5c6ef56cb9afb24b9f8244a2061664ff7467a6e3, driver and builder are pinned. Old exact-rational source is compiled only in the diagnostic Old namespace, with renamed exports; production does not call it. Raw artifacts remain local/regenerable; no remote archival claim.

Disposition: developer fixed-J16 gate PASS, pending distinct source/math review before whole-box adoption or consequential replay. All whole-box root movement, gradients, corner/defect integration, total point success and complete certifier remain OPEN. No shared source, mathematical statement, Git state or certified range changed.
