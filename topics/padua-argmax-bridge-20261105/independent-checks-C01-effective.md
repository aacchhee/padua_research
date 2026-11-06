# C01 explicit global onset: independent mathematical reconstruction

Rules/input: `4b728b04216a5490910780bc609a82b853058426`; main supplied by the coordinator: `f654e32daff27b6846849311092f6daebbbf235b`.
Reviewer: distinct Codex supplementary reviewer, allocated gpt-6-astra high; serving model/effort metadata unexposed. Date: 2026-11-06.

Final author freezes, supplied directly by the author and rehashed before the verdict:

- `theory/C01-effective-global.md`: `d51554d208dd9e2fd92d2ec2f1b7b6f95e27dfa60e237146445ba49c498cb949`.
- `theory/C01-effective-argmax.md`: `158ba6d607949697b9665ae663392613110aebc72e743697c92196d9608f1f42`.

**Verdict: ACCEPTED.** The global numerical lemma and the complete candidate argmax assembly are supported by their written analytic arguments and the stated previously proved dependencies. The candidate assembly's OPEN label is its explicitly declared review boundary; this review finds no remaining mathematical obligation within its statement and supports promotion to PROVED. No author source was changed by the reviewer. Formal Claude audit remains separate.

The accepted actual argmax tail is every integer n>=ceil(exp(10^12)), with exactly the two parity-correct nonnode corners as maximizers. This is an explicit but impractical upper boundary. It leaves the intervening finite gap 41<=n<ceil(exp(10^12)) and all-degree PD-T099 unresolved. Neither a model-validity onset nor a weighted-energy onset is substituted for the argmax conclusion.

## Scope and dependencies read

Read both new proofs in full, and the full records PD-T216 (global primitive), PD-T221 (explicit local envelope), PD-T224 (all-center defect), PD-T228 (reflection-first local corner bound), PD-T229 (older eventual assembly) and PD-T157 (explicit corner leading term). Also read PD-T215 and PD-T364's full exact kernel/reflection/cover derivations during this review session. The new numerical extraction and assembly were reconstructed independently below. Accepted historical dependency statements are retained at their exact scopes; this is not a fresh audit of every earlier dependency's entire transitive tree.

This review excludes historical novelty, priority, literature coverage and the developer's gate completeness. It makes no such claim, so the full IDEAS novelty audit is not invoked. No finite-degree sampling, certificate replay, numerical maximization, fit or external existence theorem is a premise.

## 1. Full-diamond normalization and partition

The odd periodic board has 2n(n+1) entries and F=(-1)^j G/2. Thus S=N^-1 sum |F| agrees exactly with the inherited primitive and its zero-phase value Lambda_c. Folding periodic indices to physical indices produces the four reflected phase evaluations with weights e_j f_r/N. Endpoint duplicate evaluations have half weights; omitting them would change the normalization. Separate evenness of the finite G polynomial proves this folding even for endpoint overshoots and collisions.

The corrected numerator is

    a(1+cos v)-sin(alpha)sin u/2+sin(beta)sin v/2.

The highest exceptional mode stays in x. On the closed diamond, a=cos((alpha+beta)/2)cos((alpha-beta)/2) lies in [0,1], including its boundary zeros. Interior shifted u and v stay in [0,pi] even at a diamond vertex. The endpoint set, diagonal strip and remaining far set form a complete physical-index partition. On the far set F(0,0)=f(u0,v0); all other reference terms retain their polynomial values. Consequently the complete zero-phase reference really is a Lambda_c, without a missing corner or diagonal contribution.

## 2. Explicit diagonal-strip estimate

For a strip pair, every angle between the shifted u and v is within 10pi/n of u0. With s=m sin t and m/n<=65/64, m sin u0<=s+11pi. Splitting at s=1 proves

    (1+m sin u0) min(1,1/s) <=2+11pi<37.

This remains valid at s=0 with the polynomial derivative interpretation. The elementary Chebyshev derivative bounds therefore give |P'_n(cos t)|<=74m^2/(1+m sin u0). The ratio to n^2/(1+n sin u0) is at most (65/64)^2, and 74(65/64)^2<80. The divided-difference mean value theorem applies on the entire cosine interval, also at equality. After the factor 1/2 and corrected cosine, the same 80n/(sin u0+1/n) bound safely encloses |F|.

The unshifted second-index strip has at most 16m/n+1<=69/4<32 indices per first row. The harmonic/chord estimate sum_j 1/(sin u0+1/n)<=nH is valid by pairing j and n-j and using sin(jpi/n)>=2 min(j,n-j)/n. Hence four reflected phases cost <=10240H after normalization. Giving the same allowance to the reference strip is conservative and yields <=20480H. No quotient differentiation or undefined collision value is used here.

## 3. Endpoints and folding

The global derivative bound gives |F|<=(m^2+n^2+1)/2<=m^2. At the lower first endpoint its folded angle is <=pi/n. For second index r>=4 the folded second angle is >=(r-1)pi/m, even when r=m and the phase points outside the original angular square. Thus u/v<=65/192<3/8. From the cosine chord and Taylor inequalities,

    cos u-cos v >=(1/5-9/128)v^2 >v^2/8;
    (1/5-9/128)-1/8=3/640.

The actual phase numerator is bounded in absolute value by 3, regardless of the signs introduced in folding. Therefore |F|<=3m^2/(r-1)^2. The first four indices use the polynomial m^2 bound, and sum_{k>=3} k^-2<=1/2 bounds the tail. Each endpoint row costs <10m^2.

At the upper endpoint, complement both folded angles and replace the index by m-r. The cosine-gap magnitude is identical and the numerator bound remains 3; no symmetry of the exceptional mode is assumed. At a second-coordinate endpoint, the same direct gap argument uses u_small<=pi/m and v_large>=(j-1)pi/n, so their ratio is at most 1/3. This proves the column estimate independently of a kernel transposition.

Four sides and four phase evaluations cost <256 after division by N, even counting intersections twice and discarding half weights. The same bound for the reference costs <=512H in total. These arguments cover the common endpoint collision and exact zero entries without rational substitution.

## 4. Far denominators and all deformation factors

At a far pair the base difference exceeds 8pi/n. Both base distances of u0+v0 from 0 and 2pi are at least that difference. A total coordinate displacement <=2pi/n retains at least three quarters of each relevant distance. Concavity of sine on [0,pi] therefore gives the asserted sine comparison for both half-angle factors. A first-coordinate shift alone retains 7/8. After it the separation exceeds 7pi/n; the second-coordinate shift retains at least 6/7 of both sine factors. Thus each consecutive denominator is at least half its preceding magnitude. These comparisons remain valid when an individual interior shifted angle reaches 0 or pi.

For the first deformation, exact subtraction yields the numerator (1+cos v0)[cos(u0+h)-cos u0]. The bound |cos(u0+h)-cos u0|<=|h|sin u0+h^2/2 and

    sin((u0+v0)/2)>=sin(u0/2)cos(v0/2)

give the displayed cotangent/reciprocal-square estimate with coefficient 2. For the second deformation, its exact numerator is (1+cos(u0+h))[cos(v0+k)-cos v0]. Using the other half-angle product gives the corresponding estimate in v0. Replacing the intervening half-difference by the original one costs (8/7)^2<2, so the combined coefficient 4 is valid. This verifies the finite-deformation inequality directly, without an unbounded derivative through a pole.

At fixed first angle the separated second mesh has at most two points in each half-open distance shell. The sine chord bound therefore gives the squared and first-power sums <=8m^2 and <=4mH; the first mesh has the analogous bounds. No arbitrarily close fractional pole enters because every retained shifted difference exceeds 6pi/n. Summing the four deformation terms gives respectively

    32pi(m/n)H <=192H,
    64pi^2(m/n) <=960H,
    32pi(n/m)H <=128H,
    64pi^2(n/m) <=640H.

The sum is 1920H per phase, 7680H for four phases, hence <8000H. The sine-channel inequality sin u,sin v<=2sin((u+v)/2) holds throughout [0,pi]^2 and gives |g_u|,|g_v|<=|csc((u-v)/2)|. Their normalized cost is <=4H per phase, hence <=16H. The nonnegative factor a allows comparison with a|f0| by the triangle inequality.

The full budget is therefore 512+20480+8000+16=29008 times H, strictly below 30000H. Since H<=2log m, the written proof actually supplies 60000log m, and in particular the stated 10^6log m. Every constant used in this step is numerical. The argument contains no remaining O-term, compactness modulus or existence threshold.

## 5. Whole-square cover and explicit far entry

For a point in any closed physical mesh rectangle, the L1 distances in unit mesh coordinates to its two odd vertices sum to 2. Choosing one at distance <=1 gives a physical odd-center representation with rho<=pi. Boundary points use an adjacent rectangle. This covers every point, including mesh ties, nodes and corners. Positive endpoint reflection and odd translation preserve exactly lambda=S-Delta with Delta>=0, rather than changing the primitive normalization.

For L=log n>=20, PD-T157 and pi^2<10 give Lambda_c>=L^2/4. The full-diamond chord estimate gives 1-a>=rho^2/20. At rho>=1/64, the new global estimate yields

    S-Lambda_c <=-L^2/327680+2*10^6 L<0

for L>=10^12: the exact threshold margin is 10^12-655360000000=344640000000>0. Hence all such phases are excluded strictly, including the entire diamond boundary. No ineffective phase-localization threshold from PD-T225 or PD-T229 is used.

## 6. Complete near envelope and all noncorner classes

The exact statement of PD-T221 applies to both phase signs, all n>=2, rho<=1/64, polynomial collisions and exact zeros. Combining it with the same corner/chord bounds leaves

    -(L^2/80-484000L)rho^2 +2048rho^(3/2)+640H rho/n.

At L>=10^12 the quadratic coefficient is >=A=L^2/160. The threshold margin L-160*484000 is positive. Splitting -A rho^2 into two equal parts and setting t=sqrt(rho) gives the global maxima

    sup[-A rho^2/2+B rho^(3/2)]=27B^4/(32A^3),
    sup[-A rho^2/2+D rho]=D^2/(2A).

The stationary values are sqrt(rho)=3B/(2A) and rho=D/A respectively; allowing every rho>=0 only enlarges the original near domain. Thus both the fractional term and finite-degree cusp are retained.

With B=2048, the exact coefficient 27 B^4 160^3/32 is 60798594969501696000<10^21. The first excess is <=10^-51. With H<=2L the second is <=131072000/n^2; 131072000<2^27 and n>2^30 imply it is <2^-33. Each is <1/16384, so the total near primitive excess is <1/8192.

PD-T224's full statement is finite and uniform over every physical odd noncorner center at n>=48, rho<=1/64. Its proof explicitly treats both parities, the first four indices at each endpoint, the fixed horizontal numerator and the remaining adaptive blocks. Its coefficient is the same signed-half 1/N normalization. Thus it supplies Delta>=1/4096 for the selected representation, with no vertical-edge-only or macroscopic restriction. This gives lambda<Lambda_c-1/8192 at every noncorner class. The new C01 half-radius floor, finite energy sweep and N1 near model are not needed in this assembly.

## 7. Actual corners, zeros and equality

For a remaining odd endpoint center, physical phases are inward, and their absolute sum is precisely the corner phase radius in PD-T228. That theorem averages the four signed polynomial kernel copies before taking each cardinal absolute value. Its absolute symmetric-Taylor remainder is valid even for zero initial cardinals, and the removed collision family has a finite polynomial Hessian bound. Its normalization is lambda=N^-1 sum e_j f_r |sum_four F| and Lambda_c=4N^-1 sum e_j f_r |F0|, consistent with the primitive used above. Thus it does not transfer a merely signed primitive remainder into a cardinal bound.

The explicit strict-corner condition log n>=10^7 is satisfied by L>=10^12. Every punctured inward corner phase 0<rho<=1/64 is therefore strictly excluded. No physical n^-2-radius conversion, unproved energy hypothesis or sign-stability assumption is needed for this use.

At rho=0 the point is the actual nonnode corner, with value Lambda_c. The odd endpoint pairs are always (n,m), and additionally (0,m) for even n or (n,0) for odd n. These become exactly {(-1,-1),(1,-1)} or {(-1,-1),(-1,1)}. The parity-valid x reflection for even n and y reflection for odd n preserves the Padua node set and cardinal space, proving their equal values. Every other physical point was strictly excluded by one of the preceding cases. The conclusion is therefore the actual maximum and exact equality set for every n>=ceil(exp(10^12)).

## Checks, findings and limits

No BLOCKING, MAJOR, MINOR or mathematical NOTE finding. A short independent Python `fractions.Fraction` calculation checked the displayed rational margins, deformation total 1920, global total 29008, threshold products, and both scalar-maximization coefficients; it exited 0. The exact values are given above so they can be checked without that execution. It used no numerical trigonometry, phase sampling or theorem premise and required negligible CPU within the existing 120 CPU-s review allocation. Both final author hashes were verified in that command.

No full cover, additional finite degree, code acceptance, runtime replacement or practical-throughput claim follows. The explicit upper boundary is extraordinarily large and leaves the finite bridge unresolved. The separate inexpensive-certifier research remains scientifically useful; this result alone does not justify an old-tech degree campaign or a Syvert pack. Formal Claude audit and normal publication/disposition steps remain with the coordinator.
