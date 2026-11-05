# G2–G5 quantitative screens and independent pilot replay

Status: **MEASURED** (G2/G3/G4); **OPEN / not evaluable as specified** (G5).
Rules and input: `8a1f394739293953e1566fd24a0a193cc78ff26f`; base `440d107`.
Worker: independent Codex gates subagent, gpt-6.1-sol medium (technical implementation and replay). No Git operations. This is a new execution by a different agent from Claude's pilot, not an independent audit of this worker's new code. No novelty claim or new mechanism is proposed; novelty gate does not apply to these pre-registered measurement extensions.

## Fixed criteria and scope

The G2/G3/G4 criteria and G5 decision rule in handoff 02 remain unchanged. All extrema below are finite sampled extrema, not suprema or infima over continuous regions. No float run certifies any degree.

- G2: `n = 17,18,24,25,48,49,96,97,192,199,200,255,256,511,512,999,1000`. Both actual maximal corners (odd endpoint-index sum) are evaluated independently, covering both parities. Up to n200: radii 1/64,1/256,1/1024 and nine directions f=0,1/8,...,1, with alpha=f*rho,beta=(1-f)*rho. Above n200: radii 1/64,1/128 and five directions, to limit subtractive loss and work. K is `(lambda-a*Lc)/(rho² log(n+1))`, a=(cos alpha+cos beta)/2. Reducing directions is an explicit finite-scope compromise, not a bound between directions.
- G2 validity: three directions f=0,1/2,1 and radii 1/32,1/16,1/8,1/4,1/2,1,2,pi, at both corners and every degree. These are inward phase radii; corresponding angle displacements are alpha/n,beta/(n+1). All sampled gaps were positive. Thus the largest physical validity radius requested by G2 is **not identified**; the scan is censored at phase radius pi. Positivity at isolated radii does not prove positivity between them.
- G3: n17,18,24,25,48,49,96,97,192,199,200; original 61×61 pilot grid on [-pi,pi]² restricted to |alpha|+|beta|<=pi, including the exact two candidate maximizers (pi/2,-pi/2) and its negative. Report far margins at sampled rho>=1/8,1/4,1/2,1. A trial 31×31 grid at higher n was superseded because its first eligible rho>=1/2 point gave a substantially biased comparison to the pilot; the final run uses 61×61 throughout.
- G4: same eleven degrees. All physical odd coset centers for n<=25; above n25, every edge odd center, first-four-strip and interior centers from the index set recorded in `screens.py` (end distances0..4 plus macroscopic fractions .1,.25,.5,.75,.9, with nearest odd-center parity correction at every fraction pair). Nine signed offsets: origin, four axes at1/64, four diagonals at1/128 per coordinate, discarding offsets outside the physical square. Both lambda gap Lc-lambda and total defect Delta=S-lambda are minimized separately within each class. Classes retain vertical/horizontal/diagonal orientation. This covers representative classes, **not every individual noncorner center for n>25**, and does not certify the minimum within any neighborhood. Exhaustive neighborhood coverage remains OPEN.

## Executed commands and evaluator

From repository root, with `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1`:

```text
python3 topics/padua-argmax-effective-20261103/code/g2_pilot.py 17 24 48 96 192 > /workspace/padua-work/gates/g2-replay.out
python3 topics/padua-argmax-effective-20261103/code/g3_pilot.py 17 48 96 > /workspace/padua-work/gates/g3-replay.out
python3 topics/padua-argmax-effective-20261103/code/gates/screens.py g2 --output /workspace/padua-work/gates/g2.json
python3 topics/padua-argmax-effective-20261103/code/gates/screens.py g3 --output /workspace/padua-work/gates/g3.json
python3 topics/padua-argmax-effective-20261103/code/gates/screens.py g4 --output /workspace/padua-work/gates/g4.json
python3 topics/padua-argmax-effective-20261103/code/gates/validate.py > /workspace/padua-work/gates/stability.json
```

The replay outputs match the committed Claude pilot outputs **byte for byte**, despite the environment being Python3.12.14 rather than the pilot's reported3.13. Timings and output hashes are in `outputs/gates-summary.json`. New screens use a flat odd/even-node vector implementation of the PD-T101 corrected kernel:

`g(u,v)=U_(n+1)((u+v)/2)U_(n+1)((v-u)/2)+U_n((u+v)/2)U_n((v-u)/2)-cos(nu)`, where `U_k(t)=sin(kt)/sin(t)`.

Four reflections are summed **before** taking absolute values for lambda, and after absolute values for S. This preserves the exceptional halved x-mode. Sine arguments are reduced modulo pi, retaining the exact parity, and `sinc` supplies removable limits. Arrays have O(n²) entries, never a degree×degree×degree tensor; n1000 has approximately half a million nodes. The evaluator agrees with the original dense `maj.py` evaluator on 35 executed random/corner probes n3,4,17,48,96 to absolute difference<=2.50e-13. This is an implementation check, not an enclosure.

Float64 subtraction of nearby O(log²n) values loses digits as rho shrinks. At n192,200,999,1000 and rho1/64, an executed NumPy longdouble repeat (64 mantissa bits) changes axis K by at most5.90e-11; this does not bound other points or validate all rounding. The two corners' sampled K maxima differ by at most8.43e-9, primarily on the smallest radii. No claim depends on digits at that scale.

## Findings

K sample maxima decrease from0.289285 at n17 to0.221483 at n1000, while the axis budget Lc/(4log(n+1)) rises from0.745401 to1.073029. The local margin remains promising for R6, but samples do not bound K on untested n or phases.

Global C sampled maxima remain near the pilot values and occur with |alpha|=|beta|=pi/2; phase signs depend on the chosen base corner. Finite far margins improve with degree. These are values on the fixed grid; they do not control the narrow interval between the excluded rho<1/2 region and the first eligible grid points, nor the phase interpolation error.

G4 sampled minima lie on the central vertical edge, consistent with the inherited measured runner-up picture. At n200 the sampled minimum gap is 0.552427897 and Delta is 0.552297501 over 496 centers and 3267 offsets. Across all eleven degrees: 3458 centers and 25365 offsets. Comparing them to1/1536 or1/4096 shows headroom in these samples; it does not strengthen PD-T222/224.

## G5: precise missing input

The registered instruction asks for a projected n0 when constants are within a factor2 of truth, followed by comparison with G1's n_cert and the kill threshold10*n_cert(7days,port). No explicit n-dependent remainder function or joint inequality is specified. G2 gives local remainder coefficients, G3 gives finite phase-grid majorant values, and G4 gives sampled defects. Doubling any of these constants does not supply:

1. a uniform bound on the global/local primitive errors between phase samples and at all future n;
2. a finite-n defect convergence rate uniformly over moving centers and signed phases;
3. a quantitative replacement for PD-T223/225's contradiction-based localization;
4. the dependencies of these errors on the chosen radius and corner cutoff.

Consequently there is no mathematical expression whose root defines the projected n0. Infinitely many remainder functions agree with all these finite observations and yield arbitrarily different thresholds (or none). The old rule is retained and its verdict is **not evaluable**, not PASS or KILL. This is a planning-obligation diagnosis, not a refutation of R1/R2 or PD-T099.

Dated operational clarification,2026-11-03: evaluate G5 only after a route supplies an explicit candidate error budget E(n,rho,delta) and states which constants are being enlarged by factor2; solve that stated sufficient inequality and then compare the resulting threshold with the measured-port G1 projection. Until then R1's factor2 kill criterion remains undecided. Root owns route selection and mathematical conclusions.

## Artifacts and limits

Full regenerable data and validation details are under `/workspace/padua-work/gates/`; SHA256,size,versions,timings and compressed summaries are in `outputs/gates-summary.json` (<16KiB). They are scratch artifacts pending the root's chosen Padua cold-storage workflow. Hashes establish identity, not durable retrieval or correctness. No unexecuted work is reported as a run.
