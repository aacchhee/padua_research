# Interim audit: C13 corner pieces (corner-value-lower, corner-comparison)

Auditor: Claude Opus 5.5 (xhigh), independent mathematical subagent. Read-only.
Repository head: 02beaef2b22f8232286713dab0a1b7c95582ce13, branch
codex/padua-argmax-bridge-20261105. I read AGENTS.md. T = topics/padua-argmax-bridge-20261105.
I made no git state changes and edited no repository file.

Files read in full: T/theory/C13-corner-value-lower.md, C13-corner-comparison.md,
C07-corner-positive-deformation.md, C07-corner-million-onset.md, C08-far-corner-margin.md,
C05-corner-quarterangle-bound.md; C02-corner-halfdiamond.md sections 1, 2, 5, 6;
PD-T159 (topics/padua-proof-attempts-2-20261101/theory/proof-attempts-2-codex-04-corner-product-comparison.md);
PD-T269 (topics/padua-lebesgue-followups-20261103/theory/t4-01-corner-defect-limit.md);
PD-T270 (.../t4-02-one-dimensional-remainder.md). I grepped T/independent-checks-C13-onset.md
for context but did not rely on it.

## Verdict

**No BLOCKING or MAJOR finding.** Within the scope below, statements (19), (21), (22) of
C13-corner-value-lower and (20), (5) of C13-corner-comparison hold for every integer n>=500000.
I re-derived each step at that degree floor. Two MINOR record-precision findings and a few NOTEs follow.

## Findings

**M1 (MINOR) — the floor-check list is incomplete although it says it lists every check.**
C13-corner-comparison.md:70-83 ("Here are every numerical floor checks used in that argument").
The C07-million/C05 argument also contains these degree-sensitive steps, which are not listed:
- tau^2<101/100 (C07-million:222-223). It follows from the listed tau^3 bound.
- the (21) bracket <71/10, which depends on tau (C07-million:276-283);
- |X|<=pi/2+1/(4n)<8/5 and |T_B|<8/5 (C07-million:256-257);
- sin T0>=(99/100)T0 at T0<=pi/(4m) (C07-million:301);
- C05 section 1 geometry: m/(2 pi n)<1/6 and |T|<=3Z/2. Both need tau<pi/3 (C05:55-65).
I checked each one by hand: all hold for n>=~3000. The mathematics is not affected.
Repair: add these bullets, or change the claim to "the nontrivial floor checks". The other
items are implied by tau<=1001/1000.

**M2 (MINOR) — the degree-domain lemma's stated form does not cover every function it is used for.**
C13-corner-value-lower.md:57-60 and C13-corner-comparison.md:58-61 say that functions of the form
(c log n+d)/n^j decrease. The functions actually used are:
- (L+2)^2/n, with derivative -(L+2)L/n^2 <0;
- m^2/n^3;
- m*H2/n^3 and m*H2/n^2, with H2=1+log(2(n+1));
- (L+2)/(2n^2).
I checked that each one decreases on n>=n0. For example, m*H2/n^2 is (1+1/n)(1+log2+log(n+1))/n,
and the sign of the second factor's derivative is n/(n+1)-(1+log2+log(n+1))<0. So this is a
wording gap only. Repair: say "each function below decreases (derivatives checked)".

**N1 (NOTE) — some inputs to (19) and (5) are not restated in C13.**
- (19) also needs L_n>=A_n-1/(4n^2)>0 and A_n<=L+2. The second is the PD-T158/159 elementary
  bound, cited in C07-positive-deformation:86 but not in C13. I verified it independently:
  2k/pi<2 by interval arithmetic.
- The comparison's Lambda_c>=A_n^2-eps (C13-corner-comparison:65-68) also needs Delta_corner>=0
  (C07 pairing), or d(n)>0. Both are proved, and value-lower:18-19 says so implicitly. It would
  be clearer to say Lambda_c=B_n+Delta_corner>=B_n in the comparison file.

**N2 (NOTE) — the C08 extraction is valid below its stated domain.** C08's statement domain
n>=10^6 (C08:127) is used only for its final ">1/2". The first inequality in C08 (8),
Delta>(16n/25-28000)/(n+1), needs only n>=40 (PD-T269 section 2) and the all-n>=2 C07 pairing.
C13's extraction at value-lower:80-92 is therefore legitimate.

**N3 (NOTE) — tau is defined differently in two files.** In C07-positive-deformation:31,
tau=n/m. In C07-million, C05 and the C13 comparison, tau=m/n. They are separate files, so
nothing conflicts, but a reader moving between them could be misled.

**N4 (NOTE) — the final margin is thin but exact:**
p(131/10)-1/6 = 10987/64000-32000/192000 = 961/192000 ≈ 0.0050.

## Task 1: (19) and the B_n identity (own derivation)

**What PD-T270 states.** t4-02:12-21: for every integer n>=1, both parities, with
L_n = (2/n) sum_{r odd<=n} d_r csc(r pi/(2n)) and d_n=1/2,
|L_n - A_n| <= 1/(4n^2).
This L_n is the one-dimensional same-mesh cosecant (Chebyshev) sum, exactly as defined in PD-T159:18-22.

**Derivation of (19).**
- Put e=1/(4n^2). Then L_n>=A_n-e>0, so L_n^2>=A_n^2-2A_n e = A_n^2-A_n/(2n^2).
- B_n = n L_n^2/m + 1/m >= (n/m)(A_n^2-A_n/(2n^2)) >= A_n^2-A_n^2/m-A_n/(2n^2).
- Use A_n<=L+2 (it needs (2/pi)k<2, and k=1.51193 by interval) and 1/m<1/n. This gives
  B_n >= A_n^2-(L+2)^2/n-(L+2)/(2n^2), which is (19) exactly.
- At n0, with L<14: 256/500000+8/500000^2 = 5.12e-4 <1/1000. Both terms decrease (see M2).

**The identity.**
- PD-T159 (3): Lambda_c = (4/(nm)) sum_{j+k odd, 0<=j,k<=n} eps_j eta_k f(a_j,b_k) + 1/m,
  where eta_n=1.
- PD-T159 (4)-(5): L_n^2 = F_n = (4/n^2) sum eps_j eps_k f(a_j,a_k). Hence
  n L_n^2/m = (4/(nm)) sum eps eps f(a_j,a_k).
- So Lambda_c = B_n + Delta, with Delta = (4/(nm)) sum[eps_j eta_k f(a_j,b_k) - eps_j eps_k f(a_j,a_k)].
  This is the PD-T269 (4) signed deformation. Nothing is counted twice: the 1/m is the (n,m)
  endpoint only, and the k=n reference row is zero.
- This Delta is the signed same-mesh deformation, not PD-T364's triangle defect.
- Measured cross-check: the C02 representation, (4/N) sum_O e f |F0|, and the PD-T159 formula
  give the same Lambda_c(2000)=34.577387.

## Task 2: (21) Delta_corner > d(n) (own derivation)

**C07 pairing (re-derived for every n>=2).**
- Ordering: b_k>a_j iff n(k-j)>j, which holds for j<k<=n. Hence 0<=v<d.
- The increments in C07 (4) are exact. q(x) is nondecreasing on [0,pi) because
  tan(x/2)>=tan(tau x/2)>=tau tan(tau x/2).
- This gives (1+A)v>=(1+B)u. With d(d-v)<=d(d+u), each unordered pair sum is >=0.
- At k=n the second increment is 0. The extra eta_n-eps_n=1/2 terms are >=0.
- So every discarded unordered pair, and the endpoint excess, is nonnegative for all n>=2.
- Measured: the minimum unordered pair is >0 at n=64, 501 and 2000.

**PD-T269 section 2 (re-derived).** With M=1 and delta=1/10, the domain is n>=2(M+1)/delta=40.
- |f(a,a+u)-H0/|u|| <= 6/delta^2. This uses |dH/du|<=2/(9delta^2/4), R<=2 and
  H0|R-1|/|u|<=pi/2.
- The (n+1)/n mismatch costs <=1/(n delta^2). The total is 13/(n delta^2) per orientation.
- |h_+-|<=1/delta^2 and |h_+-'|<=(1/2+1/pi)/delta^3<2/delta^3.
- The orientations match: d_{j,j+1} pairs with h_+(j/n), and d_{j+1,j} with h_-((j+1)/n)
  (s=-1, row j+1).
- Both rows lie in [1/10,9/10] because J = ceil(n/10)..floor(9n/10)-1. All weights are 1,
  because j+1<=floor(9n/10)<n.

**Constants.**
- Per pair: 26/delta^2+2/delta^3 = 2600+2000 = 4600.
- Mesh: the missing length is <2/n, at |h|<=200, which costs 400/n. Left-endpoint error is
  n*4000/(2n^2) = 2000/n. Total 2400/n.
- Then sum_J(d+d) >= n[n∫h-2400-4600|J|/n] >= n(n∫h-7000), using |J|<=n.
  So Delta >= (n/m)(4∫h-28000/n), and 28000 = 4*(2400+4600).
- The two orientations combine to h = 2t^2 cot(pi t/2)/(pi(1-t^2)) >= 4t/pi^2, by the
  PD-T269 (10) positive series. So 4∫h >= 32/(5pi^2) > 16/25.
- Hence Delta > (16n/25-28000)/(n+1). At n0 this is 292000/500001 (exact Fraction).
  d(n) increases, since its derivative numerator is 28000+16/25.
- Measured float: 4∫h = 0.702810. The retained sum at n=5e5 is 0.702816, against d(n)=0.584.

## Task 3: C07-million and C05 degree-dependent steps (own audit at n0=500000)

**Section 1.** tau=1+1/n<=1001/1000. The C05 (3) offsets need m/(2pi n)<1/6 (see M1).
- The new R class r=j+1 has j<n/2 and g=1-j/n>1/2.
- The base value of |T| is pi(n-j)/(2nm) = pi g/(2m) (checked).

**Section 2.**
- The j=0 term is (6/5)^4 = 2.0736 <21/10.
- The constant part is (108/125)(1+log J).
- (11) holds by convexity: h(x)-h(0)<=x h'(x), and h' is increasing.
- The step q0-(J+1)/n >= 1/3-1/(2n) >= 999/3000 needs n>=3000.
- 27(1000/999)^3<28, (28-216/125)/2<14, and the total is 16.964<17.
- The log coefficient is 33/32+108/125 = 7581/4000 (exact), and the constant 20.514<21.
- No step uses log n>=13.8 or n>=10^6. A2 and A3 are carried over from C05 section 3. Their only
  degree step is (1-120/n)^(-2)<101/100 for j<=100, since 100/(n q0)=120/n. At n0 this is
  1.00048. The j>100 tails 3/80000 and 9/100 do not depend on the degree.

**Section 3 (normalization re-derived).**
- 2r2/(N n^2) times 1/(2P|T|^3) gives 16tau^3/pi^4. The other two terms give 4tau^3/pi^2.
- tau^3<101/100 and pi^2>197/20 give 6464/38809 and 404/985. All four products pass.

**(13) harmless terms.** I re-derived all four coefficients: 30m^2/(pi^2 n^3), 18mH2/(25n^3),
3456mH2/(25pi^2 n^3) and 8/(nm).
- At n0, H2 = 14.8155 (interval) <16, and the total is 6.08e-6 <1/100.
- At larger n, H2 grows, but mH2/n^3 still decreases (M2). The bound therefore improves with n,
  as claimed.

**Section 4.**
- (16): 3000/999-6/5 = 1.8030 <181/100, and 51/25+69/121+181/100 <9/2.
- T part: 25tau^2/pi^2 = 2.5635 <8/3 (re-derived: (25/9)(4/pi^2)(9/2)/2*tau^2).
- P part: 108mH2/(25n^2) = 1.28e-4 <1/100. The C13 form 108tau*16/(25n) is also <1/100.
- The sine-channel pairing over the four copies gives r2/(2n^2 m) sum(...) (re-derived).

**Section 5.**
- s bounds: cos 0.8 = 0.6967 >=17/25 and tan 0.8 = 1.0296 <=6/5, so |s|<=25/17,
  |s'|<=0.757 and |s''|<=1.19.
- V' and V'' bounds re-derived: 3n/2+7/4 and 3n^2/2+7n/2+23/8. The 1.51 forms need n>=175
  and n>=352.
- Product-rule costs re-derived. The bracket is 7.046 <7.1 at tau=1001/1000.
- (22): (71/80)n+1/2 <=(9/10)n needs n>=40.
- F0 on B re-derived. y0^2/(x0^2-y0^2) = n^2/(2n+1), giving F0<25pi n/99<n.

**Section 6.**
- |E''| <= (9/10+1/2) n rho^2.
- The symmetric-pair Taylor weight is 1.
- B has at most n/2+1 indices, and rho^2<=2r2. This gives (14/5)(n+2)/(n+1)<3.
- The total is L/3+15.01 <=L/3+16, with L=log(n+1). This matches the C13 coefficient log(n+1)/3+16.

**Answer to "does any step use n>=10^6?"** Only the old texts state it: C05:170 for the
(1-120/n) bound, C05:231 and C07-million:189 for "H2<16 at endpoint", C07-million:266 for the
V bounds, and C07-million (26). Each of these is valid at n0 as shown above. Section 7's
ell>69/5 is replaced in C13 by L>131/10, which is valid at n0: log n0 = 13.12236 (interval).

## Task 4: final arithmetic (exact Fraction and interval)

- 1-cos t >= t^2/2-t^4/24 >= (47/96)t^2 for t<=1/2. Each of A and B is <=1/2, so
  1-a >= 47r2/192.
- The chain:
  lambda <= aLam+c r2 = Lam-(1-a)Lam+c r2 <= Lam-[(47/192)Lam-c]r2.
  This uses Lam>=0 and 1-a>=0.
- Lam >= B_n >= A_n^2-eps, A_n^2 >= (4/pi^2)(L+3/2)^2 > (2/5)(L+3/2)^2, and
  c = log(n+1)/3+16 <= (L+1)/3+16. The direction of every inequality is correct.
- p(131/10) = 10987/64000 (exact). p'(L) = (47/240)(L+3/2)-1/3 >0.
- So lambda <= Lam-(10987/64000)r2 < Lam-r2/6 for r2>0.

## Task 5: geometry and parity (inspection)

- The physical point is z = (-cos(A/n), -cos(B/(n+1))), i.e. theta = pi-A/n and phi = pi-B/m
  (C02:13-17, C07-million:14).
- The proof covers all signed phases with |g|+|d|<=1/2. This includes both axes and the closed
  boundary A+B=1/2.
- Equality holds only at the origin, where lambda = Lambda_c by definition. Every r2>0 is strict.
- Parity:
  - (-1,-1) has p+q = 2n+1 odd, so it is a nonnode corner.
  - Even n: the x reflection maps p to n-p and preserves the checkerboard. (1,-1) has p+q = n+1,
    which is odd, so it is a nonnode.
  - Odd n: the y reflection preserves the checkerboard because m is even. (-1,1) has p+q = n odd.
  - The other corners are nodes in each parity.
- The nearest node in the patch would need phase pi >1/2, so no node is in the patch.
- I accepted interpolation-uniqueness invariance of the corrected space (C02:406-411) by inspection.

## Executed computations (all in scratchpad/audit/corner-code/, python3 -I)

- exact_checks.py (Fraction plus mpmath iv; PYTHONPATH arg scratchpad/audit/pylib): **ALL PASS**,
  0.05 s CPU. Key outputs:
  - p(131/10)=10987/64000; d(n0)=292000/500001;
  - log n0 in [13.12236337740432, ...];
  - k in [1.5119273207319686, ...]; H2(n0) = 14.81551255796227;
  - (13) = 6.0802e-6; P part = 1.2801e-4; 4∫h = 0.7028103 (mp.quad, measured).
- measure.py (float64, MEASURED only), 0.8 s:
  - n=5e5: L_n-A_n = 1.8e-13 <= 1e-12; B_n-(A^2-eps) = +2.86e-4; retained pair sum 0.702816,
    d=0.584.
  - n=1e6: retained sum 0.702813.
  - Delta at n=64/501/2000: 1.125/0.970/0.937, with minimum unordered pair >0.
- patch_measure.py (float64, MEASURED, outside the claimed domain), 17.8 s:
  - at n=2000 and 2001, for 7 phases on or inside the triangle,
    (aLam+[log m/3+16]r2-lambda)/r2 ≈ 16.9 and (lambda-Lam)/r2 ≈ -6.9 to -7.0;
  - the U/V identity (17) matches the direct divided difference, relative error <=3e-12.
- regular_formula.py: (6) matches the defining F at random regular points, relative error 1.6e-12.
- sums_measure.py at n=1000/4000:
  - A1 = 18.8/21.3, against bounds 34.1/36.7;
  - A2 = 4.34 (<6), A3 = 4.95 (<7);
  - sum(g-1/6)^-2/m = 2.99 (<4.5).

## Not independently checked (honest scope)

- PD-T101/185/228 corrected kernel and the C02 section 1 four-copy orbit normalization. I read
  these but did not re-derive them. The measured Lambda_c agreement supports the normalization.
- C02 section 5 identity (17): spot-checked numerically only.
- C05 section 2 derivative majorant (6)/(7) (the X, Y, U, V bounds): read, not re-derived.
- The C05 section 3 positive-class and l>=3 constants (13/5, 31/10, 1/10, 1/5, (33/16)(L/2+5/8)+89/40):
  arithmetic of the first terms checked; measured sums are consistent.
- The C05 section 4 counting bounds (sum P^-2 <= 288m^2H2/(25pi^2), sum Z^-2, sum(P|T|)^-1, #R).
- The PD-T270 midpoint and harmonic proof: read, not re-derived; the measured error is consistent.
- The N1-16 proofs of log10>23/10 and log2<7/10 (both confirmed true by interval arithmetic).
