# D08 analytic-onset attempt

Input `cbfdb044e184731984e3bf8be487008a86e68c37`, 2026-11-06.
Parent-requested Codex Sol xhigh, bounded30min from17:12:11 UTC.
Gate and full prospective scalar protocol: ../ideas/D08-onset.md.

## Primary40000 outcome — recorded BEFORE fallback execution

Scalar source SHA256
`526240b1a574033e5ec8653d2427e1375a0aa042fee7affe644d272085ea473a`
was frozen before the one primary command

    python code/post_audit_D08_onset/evaluate.py 40000

at17:19:21 UTC. Exit0, process CPU .023095888 seconds, five exact
Fraction controls passed. No kernel/native/board/quadrature/phase-grid
call. Directed interval result under the documented Decimal arithmetic
contract, not measured phase values:

- Near allowance Ehat in[.011538619525005,.011538619525006], below1/80.
- Corrected far model margin in[.049713235437608,.049713235437609].
- Full-phase far error in[.076045380578702,.076045380578703].
- Resulting far comparison slack in[-.037870764666100,-.037870764666099].

The primary gate FAILS: its VALID far coefficient/constant allowance
does not cover its far representation plus corner error. This is not
a counterexample to the actual argmax or true model accuracy. The near
gate survives. The invalid parent5/4 weighted coefficient shortcut
was already rejected exactly at the midpoint and was never evaluated
as a premise. The correct linear loss coefficient is147/484.

The preregistered fallback50000 is now permitted with unchanged source,
formula and constants. No precision change, parameter retuning or
source rescue is authorized by this disposition. Remaining results
will be added after that separate command.

## Unchanged fallback50000 outcome

Executed only after the preceding primary-failure record:

    python code/post_audit_D08_onset/evaluate.py 50000

Exit0, process CPU .022575894 seconds. Aggregate scalar CPU for both
commands .045671782 seconds, five exact Fraction controls per call.
No other numerical helper or kernel job. Directed endpoint results:

| Quantity | Primary40000 | Fallback50000 |
| --- | ---: | ---: |
| Ehat near upper | .011538619525006 | .009374512828106 |
| Full far error upper | .076045380578703 | .061683200165682 |
| Valid far model margin lower | .049713235437608 | .107768594441076 |
| Far comparison slack lower | -.037870764666100 | .036710881447289 |
| Near physical comparison slack lower | .006171760949989 | .010499974343788 |

The unchanged preregistered fallback PASSES. The all-degree arguments
are analytic monotonicity proofs, not extrapolation from these points.
All input radians/normalizations are the accepted exact coefficients;
this run evaluates scalar majorants, not actual phase samples.

The numeric trusted base is the documented correct-rounding contract
of Decimal arithmetic/ln plus the inspectable interval implementation.
Pi uses exact rational alternating Machin bounds. The D06 source
SHA9ab068b7... is read as data, hash-checked, and ONLY its arithmetic
and component definitions are AST-selected. Its old top-level program,
old cases, mpmath phase calculations and main are not executed.

## Five separate developer proofs

- theory/D08-near-representation.md: combine exactly the accepted D07
  E_D04+Eglobal+Bmesh+(d/pi)Blog+B6, full near closed domain n>=32;
  phase-independent Ehat is decreasing and<1/80 for all n>=40000.
  Its new near allowance has no old e_rows or I_n.
- theory/D08-near-constant-bridge.md: match B_M=B0,b_M=b_full exactly,
  then take n->infinity ONLY inside old valid domains. This gives
  |C_infty-T|<=eta0<.001; fixed truncation biases are not set to zero.
- theory/D08-near-comparison.md: use only the phase-only C04 T bound,
  prove a fresh T-T0-G<1/32+1e-6 for L>=21/2, and subtract C02's
  actual noncorner physical defect>1/16. Near noncorner exclusion is
  strict by>1/250 for every n>=40000. The signed defect is unchanged.
- theory/D08-far-comparison.md: use the VALID C08 coefficient inequality,
  n-independent C_infty<123/40, and origin constant>4383/2420. The
  latter depends on accepted PROVED PD-T271 D_infty>.9, whose complete
  source/receipt/independent/Claude provenance is consolidated by the
  other owner in attempts/D08-corner-limit.md. No finite corner lower
  follows from that constant alone. Finite Lambda is compared instead
  by the new near Ehat at zero. The full far D05 allowance is valid
  fromn32 at its own R2/deltaπ8 geometry. With its own decreasing-error
  proof and increasing margin, S_n<Lambda_c−1/100 for every n>=50000.
- theory/D08-global-argmax.md: apply PD-T364's FULL closed physical
  odd-center cover, the preceding two exclusions, and D02 actual inward
  corners(n>=10000). This yields the exact two parity-dependent
  nonnode corners as the global equality set for every n>=50000.

All five are developer **PROVED** claims awaiting distinct review;
the constant provenance is an existing accepted dependency, not a
conditional conjecture. The source/arithmetic application needs its
own independent check. No final IDs/shared statuses are assigned here.

## Retained failure and limits

The parent5/4 weighted coefficient proposal fails EXACTLY at the
midpoint, where b_full=4/pi>5/4. Root acknowledged the misquotation.
The actual accepted inequality is b_full−b_c<=3(1−a)/pi^2, so the
coarse far linear factor is147/484. No17/484 formula was adopted.
Primary40000 fails the resulting sufficient FAR gate; this does not
prove the true maximum or a sharper allowance fails there. We do not
rescue primary by changing constants, origin-specific error or precision.

The newly split global theorem is sufficient at50000, not asserted
minimal. The finite gap41..49999, the full relative S_n-a*S_n(0)
comparison, interval certifier/runtime, all-degree target and old finite
degree certificates are unchanged. All old M_far/M_near parameters,
one near correction, sources/proofs and n500000 theorem statements
stay frozen. Root owns integration, shared records, IDs and publication.

## Frozen scalar artifacts

- evaluate.py SHA256
  `526240b1a574033e5ec8653d2427e1375a0aa042fee7affe644d272085ea473a`;
- budget-40000.json SHA256
  `22e19221a350128df306ae219ee743aba0925a8c173bb28b0c5fc779aeb3f363`;
- budget-50000.json SHA256
  `37c7fcc5f77d45b06c6515d077ecced117a41a14a30b7d70d0c29a7f84561b2e`.

The mathematical files will be frozen together for root's distinct
review within the30min block; no heavy follow-up is queued here.

Developer block stopped with five separate PROVED claims frozen for
distinct review. All written decimal evidence endpoints are closed
outward bounds; strict budget gaps follow from rational separation.
