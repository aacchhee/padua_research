# C03 improved global tail: independent assembly review

Rules read at `4b728b04216a5490910780bc609a82b853058426`. Reviewer: distinct Codex supplementary reviewer, allocated gpt-6-astra high; serving model/effort metadata unexposed. Date: 2026-11-06.

Frozen assembly: `theory/C03-effective-argmax.md`, SHA256 `80c289597ec411bf6d1eb35052ae9326a88a98b0bfb3b60a047821d08c285a53`.

**Verdict: ACCEPTED, no unresolved finding.** The actual global corner-argmax tail holds for every integer n>=ceil(exp(10^7)), with exactly the two stated parity-correct nonnode corners. The remaining gap 41<=n<ceil(exp(10^7)) is unresolved. This is an explicit but impractical global upper boundary; formal Claude audit remains separate.

## Scope and dependency identities

This is a focused independent reconstruction of the quantitative assembly, not a new mechanism, historical novelty claim or re-audit of every accepted supporting proof. The full frozen C03 source, corrected C04 source and its completed distinct review were read. C01 global/allclass, C02 corner, PD-T157 and PD-T215/364's cover/normalization proofs were already reconstructed or read in full by this reviewer in the preceding reports. No full IDEAS novelty audit is invoked because no novelty verdict is made.

Read-only hashes confirm the exact supporting bytes:

- C01 effective global: `d51554d208dd9e2fd92d2ec2f1b7b6f95e27dfa60e237146445ba49c498cb949`.
- C01 all-class defect: `858634a7f38bbd870fa652e059c1fff72e2102ea3ca374f24506bce0f3f5b9fd`.
- C02 corner half diamond: `57c729c91a1641d00fe93519a1a5c17d341a322775d215868da6653e9fdedf6c`.
- C04 near comparison, corrected and accepted source: `3544d01605560ad498e96648841d8ce9c1a4bfbe69e1b94573112995df6aac1a`.

The completed `independent-checks-C04-near.md` accepts the actual near-model comparison for every integer n with log n>=30, separately from its limiting residual result at n>=10^6. This review uses that accepted actual theorem as a dependency; it does not turn the limiting result into a finite-degree estimate or repeat the full C04 proof audit. The C01 argmax status promotion described by the coordinator made no mathematical change and is not a new premise here.

## Stronger written global constant and far phases

C01's endpoint contribution is <=512, its strip contribution <=20480H, and its far contributions <=8000H+16H. Since H>=1, their sum is <=29008H<30000H. The proof explicitly gives H<=2log(n+1), hence

    S<=a Lambda_c+60000log(n+1).

This stronger constant is present in the written accepted proof; it is not inferred from the looser 10^6 headline or from measurements.

For L=log n>=10^7, PD-T157 and pi^2<10 give Lambda_c>=L^2/4. For any phase in the closed fundamental diamond, put x=|alpha|, y=|beta|, rho=x+y. Then

    a=cos(rho/2)cos((x-y)/2),

with both factors in [0,1]. If rho>=1/2, monotonicity of cosine on [0,pi/2] implies a<=cos(1/4). Taylor's alternating bound gives

    1-cos(1/4)>=1/32-1/6144=191/6144>3/100.

Since Lambda_c is positive and log(n+1)<=L+1, the resulting far comparison is

    S-Lambda_c<=-3L^2/400+60000(L+1)<0.

At L=10^7 the positive opposite is exactly 149999940000. Its derivative is 3L/200-60000, positive already at the endpoint and increasing. Thus the comparison holds at every larger degree and on the entire closed far region, including rho=1/2 and the phase-diamond boundary. No implicit global localization threshold remains.

## Actual near model and every noncorner class

The accepted corrected C04 statement supplies the actual inequality

    M_near(alpha,beta,log n)<=Lambda_c+1/4096

for every integer n with log n>=30 and all nonnegative phases with alpha+beta<=1/2. The degree range n>=ceil(exp(10^7)) meets this condition and N1-15's n>=10^6 model-error domain.

For arbitrary signed phases in the half diamond, separate evenness of S reduces it to S(|alpha|,|beta|). This follows by reflecting the appropriate periodic integer index; parity and the absolute kernel sum are unchanged. Apply the model comparison and error on that positive phase triangle. No evenness of an unverified model formula is required. They give

    S<Lambda_c+1/4096+3/14000.

C01 allclass applies to every admissible physical odd noncorner center at n>=64 and rho<=1/2, both parities and all phase signs. It supplies Delta>1/2048, including classes that are not vertical edges. Thus

    lambda=S-Delta
       <Lambda_c+1/4096+3/14000-1/2048
       =Lambda_c-107/3584000<Lambda_c.

The exact positive margin is 1/4096-3/14000=107/3584000. No finite-energy range, limiting-residual substitution or sampled class minimum is used.

## Cover, actual corners and equality set

In each physical mesh rectangle the two odd vertices are opposite. The two normalized L1 distances from a point to those vertices sum to two, so at least one is at most one. An adjacent rectangle handles physical boundary points. This gives an admissible physical odd-center representation with rho<=pi for every point, including nodes, mesh ties, edges and corners. Translation and endpoint reflection give exactly lambda=S-Delta for that same chart, with Delta>=0. Polynomial values retain every collision.

If the selected chart is far, the preceding strict far bound excludes it. If it is near and noncorner, the all-class estimate excludes it. Otherwise its center is an actual odd endpoint pair. Physical admissibility makes its phases inward; their absolute sum is precisely the radius used in C02's corner theorem. The degree condition log n>=10^7 exceeds the sufficient corner-patch threshold 610000, so every 0<rho<=1/2 is strictly excluded directly. This handles arbitrarily small nonzero phases without carrying a fixed error through the origin. The shared rho=1/2 boundary satisfies both applicable strict estimates.

At rho=0 in an actual-corner chart, the point is that corner and its value is Lambda_c. The odd endpoint pairs are (n,m) and (0,m) for even n, or (n,m) and (n,0) for odd n. Under the cosine map these give exactly {(-1,-1),(1,-1)} or {(-1,-1),(-1,1)}. The parity-valid x or y reflection preserves the node set and permutes cardinal polynomials, proving equal corner values. Every other physical point has already been excluded strictly.

Finally n>=ceil(exp(10^7)) implies L>=10^7, meeting every explicit supporting threshold. No ineffective maximizing-sequence argument, energy assumption or prior global argmax hypothesis is needed.

## Checks and limits

No BLOCKING, MAJOR, MINOR or mathematical NOTE finding. No mathematical program, numerical integral, phase or degree sample, kernel call or certificate replay was run for this assembly review. Only read-only source/hash inspection was executed; all scalar comparisons above were reconstructed algebraically. Frozen author bytes were not edited.

The accepted result improves C01's actual tail from ceil(exp(10^12)) to ceil(exp(10^7)); it does not improve the certified finite range 2–40, establish the actual near-model result at every n>=10^6, make the remaining gap practical, or authorize a backend/campaign release. Source acceptance, further research and formal Claude audit remain separate.
