# PD-T?argmax-effective-codex-02 — Finite G2/G3/G4 gate measurements

ID kind: PD-T.
Aliases: extended local corner constant; global primitive phase-grid screen; representative odd-center defect screen.
Split from: none; supporting measurements for OPEN PD-T099.
Split into: none. No theorem or range of PD-T099 is proved by this record.

## Statement

Under the corrected even-checkerboard Padua convention of PD-T101, the following floating-point observations were obtained on the finite sample sets defined below.

1. G2: at both nonnode corners, over seventeen sampled degrees from17 through1000, sampled local remainder maxima K decrease from approximately0.289285 at n17 to0.221483 at n1000. The corresponding axis comparison budget Lc/(4log(n+1)) is approximately0.745401 and1.073029. All816 additional sampled radial comparisons have lambda<Lc.
2. G3: on eleven separate1861-point phase grids, sampled maxima of C decrease from approximately1.593660 at n17 to1.454136 at n200. The negative of the sampled maximum of S−Lc over grid phases with rho>=1/2 increases from approximately0.146893 to0.446730.
3. G4: over3458 noncorner odd-center selections and25365 admissible offset evaluations, the smallest sampled lambda gap is approximately0.552416518 (n199). The smallest sampled total triangle defect is approximately0.552297501 (n200). At n200,496 centers and3267 offsets were sampled; its sampled gap minimum is approximately0.552427897.

These are extrema of the explicitly finite sets only. In particular the observed positive numbers are not lower bounds for continuous neighborhoods, unsampled centers, or unsampled degrees.

## Definitions

Write m=n+1. Nodes have angles `(j*pi/n,k*pi/m)` with j+k even, endpoint-half weights `2*eps_j*eta_k/(nm)`, and corrected cardinal cosine kernel of PD-T101. Lambda is the weighted sum of absolute values of the four-reflection **average** kernel. S averages the four absolute kernel values first. Delta=S−lambda. Lc is lambda at a nonnode corner; nonnode corners are exactly the endpoint-index pairs (J,K) with J+K odd.

For inward phases alpha,beta>=0 at either corner, let rho=alpha+beta, `a=(cos(alpha)+cos(beta))/2`, and let the angle displacement be alpha/n,beta/m toward the square. The local sampled quantity is `K=(lambda-a*Lc)/(rho² log(n+1))`. For signed phases in G3 use rho=|alpha|+|beta| and the same a; `C=(S-a*Lc)/log(n+1)`.

The sample sets are fixed by [screens.py](../code/gates/screens.py):

- G2 degrees:17,18,24,25,48,49,96,97,192,199,200,255,256,511,512,999,1000. Both nonnode corners are evaluated independently. Through n200 use rho=1/64,1/256,1/1024 and alpha/rho=0,1/8,...,1; above n200 use rho=1/64,1/128 and fractions0,1/4,1/2,3/4,1. This gives714 local evaluations. Separately evaluate the three fractions0,1/2,1 at radii1/32,1/16,1/8,1/4,1/2,1,2,pi (816 evaluations). Include34 corner evaluations for normalization:1564 evaluations in total.
- G3 degrees:17,18,24,25,48,49,96,97,192,199,200. At the first nonnode corner returned by the evaluator, translate the61×61 uniform grid on[-pi,pi]² by alpha/n,beta/m and retain |alpha|+|beta|<=pi+1e-12. The grid includes the candidate phases with |alpha|=|beta|=pi/2. Each degree uses1861 distinct phases;20471 phase evaluations total. Torus angles need not be physical angles. Phase signs of maximizers depend on the base corner.
- G4 uses the G3 degrees. At n17,18,24,25 every physical odd center is used except the two nonnode corners. For larger degrees, all edge odd centers are used. Further representative centers come from indices at endpoint distances0..4 and rounded fractions.1,.25,.5,.75,.9, subject to odd sum; each rounded macroscopic fraction pair is additionally shifted by one second-coordinate index if required to make its sum odd. This correction avoids empty macroscopic samples caused by parity. Each center uses offsets(0,0), the four signed axes at1/64, and the four signed diagonal pairs with coordinate magnitudes1/128. Offsets outside the physical square are omitted. Class orientation is vertical if first-coordinate endpoint distance is smaller, horizontal if second-coordinate distance is smaller, diagonal on a tie; minimum distance0 defines edge,1..4 strip, and>4 interior. Full index-generation code, classwise counts and minimizing locations are retained in the evidence.

## Assumptions

Python3.12.14, NumPy2.3.5, float64 arithmetic, one BLAS/OpenMP thread. No interval enclosures or continuous optimization bounds are used. The corrected rhombus identity is evaluated with removable sine limits supplied by sinc and parity-preserving reduction modulo pi.

## Status by part

Overall status: **MEASURED**.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| G2 finite local and radial samples | MEASURED | Both corners/parities at listed degrees only; no continuous K bound or maximal validity radius |
| G3 finite phase-grid extrema | MEASURED |1861 grid points per degree; no interpolation or future-degree error bound |
| G4 finite center/offset extrema | MEASURED | Exhaustive centers only at four listed small degrees; all neighborhoods are sampled finitely |

Candidate / claim disposition: none. No negative theorem is asserted.

## Depends on

PD-T101 corrected cardinal kernel and Padua convention; PD-T215/216 definitions of primitive and phase quantities; PD-T228 supplies the local comparison context only. The float reference `maj.py` from the prior topic is an implementation comparison, not a proof premise establishing numerical enclosure.

## Checks

The unchanged Claude G2/G3 pilots were independently executed by this Codex worker. Their outputs match the previously committed pilot outputs byte for byte. This is an independent replay of those old measurements, not an independent audit of this worker's new screen implementation.

[validate.py](../code/gates/validate.py) compares the new O(n²)-vector evaluator with the dense cosine evaluator on35 random/corner probes at n3,4,17,48,96: maximum absolute discrepancy2.50e-13. Executed longdouble axis repeats at n192,200,999,1000, rho1/64 change K by at most5.90e-11; longdouble has64 mantissa bits here. The two corners' sampled K maxima differ by at most8.43e-9. These are diagnostics, not error bounds for all samples.

Rules/input head:`8a1f394739293953e1566fd24a0a193cc78ff26f`; base:`440d107`. Commands, final source/data hashes, versions and elapsed times are in [the receipt](../outputs/gates-summary.json) and [the attempt](../attempts/gates-g2-g5.md). Final gate elapsed wall times were59.33s,126.40s,192.70s respectively, under shared load; these are not isolated CPU benchmarks.

## Sources

No external literature theorem is transferred. Local mathematical dependencies are identified above.

## Proof or evidence

This is computational evidence only. The compact receipt records per-degree K, C, far margins, G4 classwise minima, sample counts and SHA256 manifests. Full regenerable JSON is outside Git under `/workspace/padua-work/gates/`; root owns cold-storage publication and durable retrieval. A local path and hash alone do not establish long-term availability.

## Scope

The data supports quantitative planning for routes R1/R2/R6. It gives no new PROVED degree, continuous extremum, all-degree constant, effective localization threshold, or universal defect bound. Strict radial comparisons at isolated radii do not prove strict comparison between them. The largest radius of validity remains unidentified; the radial screen stops at rho=pi. No G5 threshold conclusion is part of this record.

## Open items

Bound variation between phase/direction samples; control cancellation rigorously; cover all centers and degrees where needed; supply uniform finite-n remainder estimates and effective localization. PD-T099 remains OPEN. G5's separate planning obligation and its unchanged decision rule are documented in the attempt, without a status upgrade here.

## History

2026-11-03: Codex gates worker, gpt-6.1-sol medium, created as a durable MEASURED home for completed G2/G3/G4 extensions. Original pilot results and their smaller finite scope remain in the Claude pilot record. Supplementary checks do not replace the required Claude audit.
