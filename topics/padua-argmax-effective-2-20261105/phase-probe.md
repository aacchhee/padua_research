# Preregistered bounded phase evaluation probe

Rules `2fb2f7502bb8d1b46c0fe1089588c46a06df258d`; technical developer
gpt-6.1-sol medium. Status: MEASURED floating evaluation only.

Before executing this probe, preregister **rho1 = 0.1** as the candidate near-coset
radius, based on the inherited S-excess peak near rho = 0.06. This choice is not
a fitted result or a proved defect bound. Samples use rho = 0, .01, .03, .06,
.1, .2, .3 along both axes and four diagonals, with rho = |alpha|+|beta|.

The compiled evaluator computes the complete odd torus sum S and the complete
endpoint-weighted four-reflection node sum lambda, each in O(n²) arithmetic.
Samples include both nonnode corners, admissible odd edge centers one, two and
three geometric lattice indices from corners on all four edges, and central odd
centers. Every sampled center and phase is retained in local raw output. Only
admissible physical angles are included. These are class samples, not minima
over a class or over a phase region. Independent direct cosine-polynomial
validation is planned at n = 3,4,5,6,17,32. Benchmarks use n = 17,32,64,128,256.
At the orchestrator's request, the final run additionally includes the A2
degrees n=48,96,192, using exactly the same sampling rules.

No finite cover, derivative enclosure, box count, outward error bound, or
counterexample certificate is produced. A1/A2/A5 cannot pass from these samples.

## Executed result

The final run used `OPENBLAS_NUM_THREADS=1 python
topics/padua-argmax-effective-2-20261105/code/phase_probe.py`. The script compiles
the C source with `cc -O3 -std=c11 -shared -fPIC ... -lm`, then calls it through
ctypes. Sources, compiler/Python/NumPy/platform versions, raw identities and
degree timing records are pinned in [the compact evidence](evidence/phase-probe.json).
The source was also checked with `cc -std=c11 -Wall -Wextra -Wpedantic
-fsyntax-only`; no diagnostic was emitted. Development reruns preceded the
final source-frozen run; the receipt describes that final run only.

The R_k implementation reduces x to r = x - round(x/pi) pi and uses
`(-1)^(q(k-1)) k sinc(kr)/sinc(r)`, with a small-argument Taylor evaluation of
sinc. Ordinary double arithmetic, trigonometric reduction and the finite Taylor
formula carry unbounded rounding error here; stable evaluation is not a rigorous
enclosure. Kahan summation reduces accumulation error. Direct lambda uses
endpoint factors e,f in {1/2,1} and
`sum_even e*f*abs(sum_four G)/(2*n*(n+1))`.

Independent arithmetic-path validation used the direct cosine polynomial
`sum_(a+b<=n) c_ab cos(au)cos(bv)`, with c_n0=1, and endpoint-weighted four
reflections. At n=3,4,5,6,17,32, 71 admissible points selected from corner,
edge and interior classes gave maximum absolute disagreements 7.11e-15 for
lambda and 1.25e-14 for S. This is validation by the developer using another
formula, not an independent agent rerun or exact-arithmetic proof.

Each benchmark degree has 19 odd-parity centers, 49 distinct phases and 655
admissible center/phase samples. The latter include near-corner interior centers
(1,2) and (2,1) and their reflected admissible counterparts. Corner-center phase
signs are restricted to the physical angle square. Exact (J,K), endpoint
distances dJ,dK, phase and class labels are preserved in the raw JSONL.

| n | Median S evaluation (ms) | All samples wall / CPU (s) | Largest sampled S-Lambda_c |
|---|---:|---:|---:|
|17|0.103|0.0993 / 0.0993|2.68456e-4|
|32|0.342|0.2542 / 0.2540|1.03911e-4|
|48|0.680|0.5033 / 0.5029|7.99764e-5|
|64|1.214|0.8714 / 0.8699|4.76682e-5|
|96|2.705|1.8713 / 1.8698|1.50859e-5|
|128|4.736|3.1145 / 3.1118|-3.55e-15|
|192|10.433|6.7671 / 6.7621|-1.78e-14|
|256|18.339|11.9735 / 11.9686|4.26e-14|

The positive S peaks at n17/32/64 occur on a sampled alpha axis at rho=.01.
Values of order 1e-14 are ordinary floating residuals at rho=0. They do not
establish either sign. The sparse grid may miss a smaller positive peak at
n128/256, and no inference that S globally lies below Lambda_c is warranted.
The operation count follows from the explicit nested loops: 2n(n+1) primitive
evaluations for S, and four primitive evaluations per even-board node for
lambda. These timings benchmark values; they do not estimate certified box
counts or justify the ten-minute exact-cover criterion.

For the preregistered rho<=.1 subset, the following are minima of the sampled
**full** defect S-lambda (not individual summand defects). The row includes
every admissible sampled phase and orientation in the named class. Detailed
per-radius counts and extrema remain in local `degree-details.json`.

| n | Edge d=1 | Edge d=2 | Edge d=3 | Near-corner interior | Central interior |
|---|---:|---:|---:|---:|---:|
|17|1.56716|1.41351|1.21797|2.97153|2.42172|
|32|1.98510|1.74734|1.52689|3.60927|2.70622|
|48|2.27251|1.96452|1.74205|4.05825|2.92270|
|64|2.48272|2.11759|1.89983|4.39305|3.07754|
|96|2.78527|2.33317|2.12745|4.88156|3.29949|
|128|3.00310|2.48642|2.29107|5.23692|3.45792|
|192|3.31329|2.70260|2.52402|5.74643|3.68257|
|256|3.53502|2.85578|2.69053|6.11241|3.84262|

Corner-class sampled minima range from -5.4e-15 to -6.1e-14, consistent with
floating cancellation. Across the full probe, sampled lambda-Lambda_c never
exceeds 5.7e-14; this is a screen without an error bound, not evidence of a
confirmed counterexample or a proof of strict descent. The observed noncorner
defects exceed the sampled S excess, but the comparison cannot be promoted to
a class-wide bound. The intended A2 global/interior enumeration and continuous
phase control remain unresolved.

Raw samples and validation/detail files remain under
`local-output/argmax-effective-2-20261105/phase-probe/`, outside the committed
topic evidence. Their sizes and SHA-256 hashes are in the small receipt.
Archival transfer to AC's chosen Padua cold storage is pending; all raw outputs
can be regenerated from the committed source and command. Only the compact
receipt and this report are proposed for Git.
