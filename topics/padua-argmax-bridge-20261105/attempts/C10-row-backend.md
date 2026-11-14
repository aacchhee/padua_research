# C10 prospective faster moment-backend pilot

Rules/input547a473a6e1c1268ff4f1ada7243b12afb02d0bc. Technical implementation optimization of accepted C06/C07; no new mechanism, novelty or degree claim. Accepted old sources remain immutable. C09 cost pilot is the motivation: n128 point helper11.546109CPU seconds and n512 incomplete under its allocated cap. No internal time attribution was proved by C09.

## Contract and gate BEFORE implementation/tests

Candidate: evaluate exactly the SAME centered-cell moment recurrence at the exact input midpoint with rigorous Arb640 operations, then round outward to160 and add the unchanged d*q*2^(1-d)*rad(y)/n input derivative radius exactly once. Coefficient and remainder formulas, phase assembly, guards, retained polynomial, J48/K32/L16/WD96 parameters and whole domain remain unchanged. Every high-precision operation must explicitly take640; global B operators remain160 and must not be used accidentally in recurrence. Arb arithmetic encloses all conditioning error even if640 is insufficient for tightness. No midpoint extraction of a computed uncertain moment and no omitted rounding/error tail.

Fixed total budget<=60CPU seconds including compilers, helper and supervisor. Before cost pilot, run at least8 partial cases covering n2,3,7,33,64, both poles/removable cell endpoints, harmonic transition and interval inputs, against512-bit direct cotangent endpoint hulls; check exact rational moments at bounded n2,7,33,64. A single old/new moment micro-profile at n128,q96,y1/2 may test attribution without claiming general dominance. Require validity and usable small-n radii before cost. Then n32 and128 at fixed phase fractions1/12,1/16 each once, with fresh changed-source C07 copy differing ONLY in its partial-source include. Cost compared with preserved C09 measurements, with scope limits explicit. Stop on failed primitive gate, native guard failure or cap; no replay/cover/newdegree/retry/adaptive tuning. Old exact-rational routine exists only in diagnostics. No production rational-moment fallback.

## Implemented change and validity scope

New `partial.cpp` is derived from the frozen C06 source. Its only result-bearing mathematical change is the implementation of `moments`; the introductory source comment identifies the derivation. All coefficients, input guards, analytic remainder formulas, ordinary160-bit operations and native interfaces are unchanged. New `point.cpp` is byte-identical to frozen C07 except that its include selects this new partial.cpp. The driver asserts that exact single-include difference and both old source hashes before/after execution. There is no changed phase assembly, model, order, symmetry or epsilon.

For the exact midpoint of the input ball, initialize ym with `arb_set_arf`, then compute step, half-step and left/right cell endpoints at explicitMP=640. Precompute the fixed-degree endpoint and half-step powers by640-bit interval multiplication. Compute the same finite moment recurrence and binomial recurrence with explicit640-bit Arb add/subtract/multiply/divide calls. Every intermediate is a ball, not a midpoint approximation. Finally `arb_set_round(...,160)` rounds the entire640-bit ball outward and the unchanged160-bit derivative bound d*q*2^(1-d)*rad(y)/n is added ONCE. All B operators inside the error expression intentionally use160 bits; none are used in the uncertain640-bit recurrence. Integer B initializers and assignments are exact. This avoids accidentally routing high-precision work through the global160-bit operators.

The exact identity underlying the recurrence and its input derivative bound are accepted in C06. Replacing exact rational evaluation by enclosing Arb arithmetic preserves that identity's result by interval inclusion, including numerical conditioning error. There is no assumption that640 bits automatically gives a tight ball. When tightness is inadequate, an otherwise valid returned ball can be wide or fail downstream guards; numerical radius is never suppressed. Cached powers are local to a single moments call, with no cross-call mutable cache or degree-dependent hidden frequency loop.

The original exact-rational source is included only inside namespace Old in controls.cpp, with renamed diagnostic exports. It is used by bounded controls and the one micro-profile. Production pointS/partial/moments never call Old. No rational-moment fallback is installed. The phase assembly still uses exact rational phases and wrap floors as in accepted C07; those are separate from the removed rational polynomial-moment arithmetic.

## Frozen executed gate — one run, no failed gate or retry

Command:

    python topics/padua-argmax-bridge-20261105/code/cheap_rows_C10/control.py

Actual PASS. Driver parent-plus-child CPU3.419798seconds including fresh compilation, primitive/reference controls, micro-profile and both point calls; wall3.422152seconds after driver initialization. Startup/import overhead is outside that timer and small compared with the unused60CPU budget. No process was capped, retried, tuned or repeated. The final successful source was frozen in the unique build snapshot before controls.

Eight partial cases all contain512-bit direct endpoint-reference hulls and overlap old exact-rational-backend enclosures. Direct cotangent sums are monotone decreasing on the guarded input domain, so the hull of exact input-ball endpoints encloses the entire true image. This tests interval as well as point calls, not only a midpoint. Cases cover n2/3/7/33/64, q31/32/33 around the harmonic transition, removable cell endpoints, both1e-30 pole approaches, and a nonzero-width interval. New and old diagnostic radii agree on all eight cases. Regular small-n maximum radius1.1590152589422934e-24. Right-pole conditioning radius1.2196974444544e13 and interval width radius0.9959157165139914 remain explicit; no absolute-small-error claim applies to these inputs.

784/784 moment checks contain independently computed exact rational sums of powers: d0..97, n2/7/33/64, q1/n, midpoint y1/2. This directly checks the mathematical values rather than requiring a narrower new enclosure to contain an arbitrarily wider old rounded ball. One old/new moment profile at n128,q96,y1/2 reports old0.004001CPU seconds, new0.0 at that timer's resolution, with98/98 moment overlaps. The zero reading is an unresolved timer-resolution observation, not zero cost or a micro-profile speedup factor. This simple rational midpoint is not representative of every arc-generated input, so it proves no global time attribution.

Only after those gates passed, n32 and128 point costs ran once each at the fixed exact rational phases1/12,1/16:

| n | C10 point-call CPU | C09 preserved helper CPU | C10 full S radius | retained/direct/blocks |
|---|---:|---:|---:|---|
|32|0.161941s|2.776525s|5.318598735445192e-29|128 / 0 / 140|
|128|0.687725s|11.546109s|3.238262516276731e-31|512 / 0 / 588|

Both diagnostic binary64 lower/upper bounds and radii match preserved C09 values exactly; counts match also. These are new-source successful point enclosures at the same inputs, not new whole-board/argmax certifications. The C09 helper timer additionally includes library load/closure overhead, while C10 times the native call in an already-loaded process after primitive initialization. Therefore this table demonstrates a substantial finite measured cost reduction with a timing-scope limitation; it is not a pure same-process cold-start benchmark, global speed law or certified production throughput. No n512/n2048 timing, full candidate, producer, cover or degree certification occurred. Useful whole-box/gradient/corner/defect integration remains OPEN.

## Frozen outputs and review boundary

- partial.cpp SHA209fa24300219884b97ce267e898b085593534d97ecc31640909c4c772061ac5.
- point.cpp SHA6e2f1920ca293ac5a34f01c6369d94345b0d0c9b8a03d3e58ef15d453fbcf1d9.
- controls.cpp SHA72a66e861a0c7bb2dbc7b9573f70e8c8b3a7e9eacfa55eec41959cfecb65c8c8.
- control.py SHAab3fdfbefba57c135ed4f9e11eb2dc4713b4733be42a61793d542d0d60dac127.

Evidence/c10-row-backend.json is below16KiB and pins local raw `c10-row-backend/check-3suvdexq/controls.json`,52214bytes, SHA0065aa88259f1195a274d691a1f6898b8b9feafda6eaa26cc906239a6e1d4188. Complete raw closure pins203 source/header entries including unchanged old dependencies, four compiler tools,13 tool dependencies, eight linked and eight actual loaded mappings. All loaded identities match before/after. It also pins preprocessed source, exact build argv, compiled binary SHA538c7fa24ba72853a2579f9cbe6030a99c6184898d9c4e132ff2979ef281cfcd, driver and builder. Raw artifacts remain local/regenerable; no remote archival transfer is claimed.

Disposition: bounded developer optimization gate PASS; distinct source/math review required before adoption or any consequential replay. All old C06/C07 sources and receipts remain immutable. No shared file, theorem source, Git state or certified range changed.
