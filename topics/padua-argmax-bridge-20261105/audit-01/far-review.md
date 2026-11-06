# Interim Claude audit: FAR case (C13-far-representation, C13-far-comparison)

Auditor: Claude Opus 5.5, xhigh (subagent; read-only; no git state changed, no repository file edited).
Branch codex/padua-argmax-bridge-20261105 at 02beaef2b22f8232286713dab0a1b7c95582ce13 (HEAD verified).
Rules read: AGENTS.md and agents/WORKFLOW.md at that SHA.
Files audited (SHA-256): C13-far-representation.md 11b27272af82…, C13-far-comparison.md e34aec6ac187…
(both match the hashes in independent-checks-C13-onset.md). Upstream hashes C06-far-compact-error
64d88fd3…, C08-far-weighted-coefficient 6d905b6c…, C08-far-endpoint-constant 3bd4653b…,
C08-far-integral-bound e76a4569…, C08-far-pole-functional 6cb61ebc… match the frozen sources cited
in C08-far-model-comparison.md:199-214.

## Verdict

No BLOCKING or MAJOR finding. (23)-(26) are supported at n>=500000. Every line of (23) is the
unrounded upstream formula; every validity condition holds at n0; C06's complete error list (18) is
reproduced term by term with nothing omitted; (24), (25), (26) are exact equalities of the stated
rationals (Fraction recomputation); the direction of every pi^2<10, k>3/2, u>=191/6144 use is
correct. The proved gap above 1/2000 is 3.205e-4, so every constant matters. I found no slack
failure. A few MINOR/NOTE record items follow.

## 1. Line-by-line check of (23) (own derivation from upstream text; inspection)

| (23) term | Upstream exact formula | Reduction | Validity at n>=5e5 |
|---|---|---|---|
| e_rows=(763L+86237)/n+7082790000/n^2 | N1-round4-rows.md:36-54: e_rows=(3+H_n)/n+(2R-1)[(10R+33+6H_n)/n+200(R+2)(R+1)^2/n^2] | R=64: 127*673=85471, +3, +763H_n; H_n<=1+L gives 763L+86237. 127*200*66*65^2=7082790000. Exact | R>=2, n>=8R=512 (rows.md:10); x=w/(2m)<=pi/16 needs m>=8R. OK |
| e_mesh | N1-round4-mesh.md:43-49: (2R+3)L/(2m)+2C_X+(8+H_R*)/n+1/(2n^2) | 131L/2+318(5+(L+1)/2)+13=(449/2)L+1762; [6+(L+1)/2]*318^2/4=(101124/8)(L+13); 1/(X-1/2)=100pi/(m-50pi)<=101pi/m iff m>=5050pi, 101pi<318; log(X+1/2)<L+1; H_R*=log64.5+1/(8*63.5^2)<5; m->n upward. Exact match to C06:354 | n>=ceil(2piR/delta)=ceil(12800pi)=40213, delta<=pi/4 (mesh.md:11). OK |
| e_collision=(62+8L)/(3n)+6/n^2 | N1-round4-endpoint-block.md:37-38: (2/m)[7+(2/pi)(3+2log(4m/R))]+5/(n^2 m)+1/(nm) | 2/pi<2/3, log(m/16)<L+1: (2/m)(31+4L)/3; 5/(n^2m)+1/(nm)<6/n^2 | same floor as N1-06; uses N1-05(2) at z>=piR/m, z<=pi/4. OK |
| e_interior=(3002L+32803)/n | C06-far-compact-error.md:291-323: 300L+6000 (BV: Var(AL+W)/2 with Var A<600, Var W<12000), 1500L+20000 (5h*sup, sup A<300, sup|W|<4000), 1200L+6800 (4 rows*(300L+1700)), 2L+3 ((5log m+4)/(pi m)<(2L+3)/m) | Sum checked. /m -> /n upward | phase-only bounds (15) need z>=delta/2 (h<delta, m>100pi); first/last 64 rows inside strip needs 64pi/m<1/100, m>6400pi (C06:278 says "because n>=10^6", but only m>20107 is used). OK |
| E=4(L+1)/n+(2/63)(1+1/n) | N1-02 (3) / N1-05 (4): 2(p+q)H_n/n+2a(n+1)/(n(R-1)) | p+q<=2, a<=1, R=64 | N1-02: n>=2, 2<=R<=n (cancellation-quadrature.md:28-29). OK |
| D=[10+(20/3)(L+1)]/n^2 | N1-05 (4), C06-full-profile (7): 10/n^2+20aH_n/(pi n^2) | a<=1, pi>3 | N1-04 needs n>=2 (regularized-pole.md:9); coefficient sum N1-01 n>=2. OK |
| 7/50 | N1-05 (3): Q=(2delta/pi)[7+(P/pi)(5+2log(4pi/delta))] | P<=2, pi>3, log1600<8 gives exactly 21/150=7/50, strict from pi>3 (actual 0.1227) | n>=2, delta<=pi/4; degree-free. OK |

Comparison with C06's complete decomposition: C06-far-compact-error.md:338 gives the total error as
e4+Q+E_n+D_n+E_interior, with e4=e_mesh+e_rows+e_collision (N1-round4-endpoint-block.md:36).
(23) contains exactly these seven pieces. The c_mesh h_R/g_R tails (C06:73-76) are not errors,
because the model uses the exact infinite constants. The special interior rows' pole errors and
N1-08's collision-row pole errors sit inside D or e_collision (any double-count would only be
conservative). Q is charged once: the model's integral starts at delta, so only the discrete
residual over Y rows is deleted. The interior special set has at most four rows: N1-02 board
bijection, at most two collision rows, plus r=m-1,m. No term is omitted.

Upstream rounding at 10^6 that is not reused: C06:323 (3/40, using log10^6<14), C06:342-364
(.032, .104002, .004906, .000059, .11, 9/25), and C06-full-profile's n>=10^6 statement. C13 uses only
the unrounded formulas listed above. I found no upstream estimate that is proved only at n>=10^6
and also used by (23). The only n>=10^6 text in the chain is C06:278, and its actual need is
m>6400pi.

## 2. Monotonicity (inspection and derivation)

Every variable term has the form (cL+d)/n^j with c>=0, d>0, j in {1,2}. The derivative's sign is
c-j(cL+d), which is negative because L>1. The c=0 cases are 7082790000/n^2 and the 1/n part of
(2/63)(1+1/n), and these are trivially decreasing. Both n^-2 terms with large constants qualify:
c=101124/8 with d=13c+1/2, and 7082790000/n^2. The constant 7/50 is constant. L<14 is used only at
n0 (log n0=13.122). The (24) rational equals E_far(n0) with L replaced by 14 exactly (see section 3),
so strictness comes from log n0<14 and strict decrease. d(n) increases (numerator of d' is
28000+16/25). u(4L^2-3L)/10 increases for L>3/8 at every fixed u>=0.

## 3. Executed computations

Scripts are in /tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit/far-code/.
Outputs are in the f*.out files there.

(a) `python3 -I f1_fractions.py` (exact Fractions, 0.015 CPU-s):
- components at n0, L=14: e_rows .22216916, e_mesh .009811365, e_coll .000116000, e_int .149662,
  E .031866095, D 4.4e-10, Q .14.
- E_far = 290652925961/525000000000 (EQUAL to the (24) rational).
- d(n0) = 292000/500001.
- RHS(25) at L=131/10, u=191/6144 = 283876469737/512001024000 (equal to the claim).
- gap = 382900852945861/466667600000000000 = 8.2050e-4 (equal to (26)); gap-1/2000 = 3.2050e-4.
- 49/25+1/3000+49/50 == 8821/3000: True. 6*(23/10)-7/10 = 131/10.

(b) `PYTHONPATH=pylib python3 f2_phase_checks.py` (mpmath 1.3.0, 30 digits, 3.5 CPU-s):
- Interval arithmetic: 1-cos(1/4) is in [0.0310875782893551, 0.0310875782893553], and its lower
  endpoint is >=191/6144=0.0310872396 (True). The analytic proof is the alternating Taylor bound
  1-cos x>=x^2/2-x^4/24, which equals 191/6144 at x=1/4.
- Interval k in [1.51192732073196, 1.51192732073197], and (2k/pi)^2 in [0.926450192, 0.926450192] >9/10.
- MEASURED on a 60-step closed-triangle grid: max[(b_full-b_c)-3(1-a)/pi^2]=0, attained only at the
  origin. On the far grid, max of (b_full-b_c)pi^2/(1-a) is 0.471, compared with the bound 3.
- MEASURED: E_64 and E_128 against E_inf at 9 phases (including near-vertex and a=0.012).
  |E_64-E_inf|<=2.6e-6 against the bound 2.5e-4, and |E_128-E_inf|<=6.3e-7 against 6.2e-5. Max sampled
  E_64 is 1.879, against 49/25+1/3000=1.9603. Here g_R=stieltjes(1,R+t), cross-checked against the
  direct partial sum to 9e-10. This confirms the identification (14) of C08-far-endpoint-constant.
- MEASURED: max Phi_0'' on a (0,1) grid is 5.57 at t=1/2, below the cited one-sided bound 12. The
  integer derivative jump is -2.27, so the atom is negative. Phi_0 on one period lies in
  [0.52125, 1.0], and min=k0/pi agrees with pole-functional (4).

(c) `PYTHONPATH=pylib python3 f3_kdelta.py` (MEASURED, binary64 midpoint/Gauss quadrature, 51 CPU-s).
K_delta at (.25,.25), (.5,0), (1,.7), (1.5,1.5), (.1,2.9), (pi/2,pi/2), (2,.3) gives
-.055, -.051, -.182, -.305, -.112, -.286, -.314. All are far below the proved 49/50.
So C_far is about 1.82 at (1/4,1/4), compared with the bound 2.94. The real far margin is large,
and the 8e-4 tightness is an artifact of the proof's allocation.

(d) `python3 -I f4_rows.py` (MEASURED, n=50000, 2.5 CPU-s). The actual first/last 64 polynomial rows
were compared with the N1-07 profiles ell_r. The total error is 5.7e-5 to 1.9e-3, against e_rows=4.7
at that n. The max single-row error is 1.9e-5, against e_row=3.7e-2. The ell_r formula and its
normalization are confirmed.

(e) `PYTHONPATH=pylib python3 f5_mesh.py` (MEASURED, n=50000, 0.15 CPU-s). The N1-06 mesh sum minus
B0L^2+bL+c_mesh (exact psi/Stieltjes constants, quadrature for the integral of f_L+f_R) gives
|diff| from 4.3e-4 to 1.2e-2, against e_mesh=6.2e-2. The dominant part is the 2C_X term,
which is O(log X/X).

## 4. Derivation of (25) (own)

The input M_far=(4a/pi^2)L^2+b_full L+C_far is checked against C06:15-16. A_n^2=(4/pi^2)(L^2+2kL+k^2)
and b_c:=8k/pi^2. Then

Lambda_c-M_far > (4/pi^2)uL^2 - (b_full-b_c)L + (2k/pi)^2 + d - 1/1000 - C_far
              >= u(4L^2-3L)/pi^2 + (2k/pi)^2 + d - 1/1000 - C_far
              >  u(4L^2-3L)/10 + 9/10 + d - 1/1000 - 8821/3000.

The second step uses b_full-b_c<=3u/pi^2 times L>0. The third step uses 4L^2-3L>0 and u>0
(so 1/pi^2>1/10 lowers it), (2k/pi)^2>9/10, and the upper bound on C_far. The -3L term is factored
before pi^2<10 is applied, so no reversed use of pi^2 is needed. The sign directions are all correct:
an upper bound on M_far and a lower bound on Lambda_c.

b_full-b_c<=3u/pi^2. I rederived identity (10) of C08-far-weighted-coefficient.md:117 from C06's
b_full: U0=(a/pi)[D+2C0-4log pi], with C0=C(1/2)=2gamma+4log2 checked via psi(3/2). I also rechecked
the series (6), the bound Q(y)>=1+(pi^2/8-1)y^2 behind (5), the value 3/4-log2 in (7), and the
inequalities (32/pi^2)(7/4-log2)=3.427<7/2, c_e+c_d<=1+a, t sin t<=2(1-cos t) and a log a<=0.
The result is (2/pi^2)(7/2+4-6)u=3u/pi^2. All of this is phase-only, with no n floor.

C_far=E_64+K_delta. This is exactly c_mesh regrouped (C08-far-model-comparison.md:227-233, checked).
- E_64<49/25+1/3000 rests on C0<4, pi^2>197/20 and 1157/591<49/25 (28925<28959), together with the
  positivity of the weighted factors. The tail sum 1/63^2<1/3000 is measured above as well.
- K_delta<49/50. I checked the split (2) algebra and K_V=c_eH_delta(d)+c_dH_delta(e) by pairing
  v with 2pi-v. The cutoff charge is 2(12/pi^2)(delta+delta^3/48)<27/1000. R<=0 in both J branches.
  For the upper (6), the inequality reverses correctly when multiplied by log sin z<=0.
- I checked the Li2 antiderivative (8) by differentiation, and the value -a*pi^2/3 at pi.
- c=233/375>1/2. From the pole functional, (11) checks by exact integration. H<749/1500 is checked
  (rational arithmetic and 0.4954 numerically). lambda0<1/(2pi), f>=1/2 and (7) cos(pi y/2)>=(3/4)(1-y^2)
  all check.
- The final sum 97701/100000 checks.
All of this is phase-only.

On the far domain a=cos(rho/2)cos((|alpha|-|beta|)/2) lies in [0, cos(1/4)]. The equality a=cos(1/4)
holds only at |alpha|=|beta|=1/4, so min u=1-cos(1/4)>191/6144. Note that a>=0 on the whole diamond,
with a=0 only on rho=pi, so "a<=0" never arises. Monotonicity in u needs only 4L^2-3L>0.

## 5. Coverage (inspection)

- Both parities: N1-04 states "no parity restriction", and N1-07 and N1-06/08 contain no parity split.
- a=0 and the vertices: N1-07 has the w=0 case at r=1, b=-pi, alpha=0. N1-08's double right
  collision (R_r=n, H=1) is checked. The C08 bounds use weighted continuous limits.
- rho=pi: the ell_r/sinc chart and N1-02's v=pi row are central special rows.
- Polynomial collisions: endpoint collisions are in N1-08, interior ones in C06's special rows, at
  most two in total.
- Signed phases: S_n is separately even, because -r mod 2n keeps parity and G is even. I checked this
  directly from the PD-T364 definition of S. The model uses absolute phases.
- rho=1/2 is included in both predicates.
- The far result needs only S: PD-T364 phase-structure.md (4) gives lambda=S-Delta_JK, and Delta>=0
  follows from the triangle inequality with w_jk>0 ((1)-(2)). The S normalization (1/(2N))Sum|G|
  equals C06's (nm)^-1 Sum|F|. Lambda_c=S_n(0,0) by PD-T364 (5).

## Findings

F1 MINOR. C13-far-comparison.md:200-201 states "u=1-a>=191/6144" without its two-line proof. The
proof (the product formula a=cos(rho/2)cos(d/2) and the alternating Taylor bound) lives in
C08-far-model-comparison.md:268-274, whose theorem is stated at n>=10^6, although this step is
phase-only. Add the proof or cite it as phase-only.

F2 MINOR. C13-far-representation.md:68-75 rechecks the N1-06/07/08 floors and h<delta. It does not
explicitly list the N1-02/N1-04/N1-05/N1-01 conditions it uses (n>=2, 2<=R<=n), or the condition
m>6400pi behind "first/last 64 rows remain inside the endpoint strips". The latter replaces C06:278's
"because n>=10^6". All of these hold trivially. Recording them would complete the lower-domain
recheck the file claims.

F3 NOTE. C13-far-representation.md:61-64 states the decreasing-function lemma for c,d>0. Two terms
in (23) have c=0, namely 7082790000/n^2 and (2/63)/n, and they are trivially decreasing. Also
(24)'s rational is exactly E_far at n0 with L=14, so "<" relies on log n0<14. Both points are
correct; this is wording only.

F4 NOTE. C13-far-comparison.md:197-198 groups (2k/pi)^2>9/10 under "C08's ... bounds". It actually
follows from N1-16 k>3/2 and pi^2<10. Correct.

F5 NOTE (allocation, not an error). The proved gap above 1/2000 is 3.2e-4, and about 0.17 of E_far is
degree-flat: 7/50 plus about (2/63). The measurements show large true slack: K_delta is at most -0.05
against the bound 0.98, E_64 is at most 1.88 against 1.96, and b_full-b_c is at most 0.47u/pi^2
against 3u/pi^2. Any future change to a component constant must be re-propagated exactly. The
(2/63)(1+1/n) term could use a<=cos(1/4) on the far domain if margin is ever needed.

## Unchecked upstream steps (stated explicitly)

- C06-far-compact-error sections 1-3 internals: the J identities (9)-(13) and the variation numbers
  behind (8), (14) and (15). I checked only their arithmetic combination into (15)-(17) and their
  phase-only nature.
- N1-07 sections 2-3: the per-index constants were partly rederived. The rest is numerically
  consistent at n=5e4 (measured).
- N1-06 section 3 (12) cancellation algebra: measured consistent only.
- N1-03 (the endpoint estimate behind N1-05 (2)): not read.
- N1-04 proof: statement only.
- N1-01 coefficient sum: line 151 only.
- C04-near-01's distributional Phi_0''<=12: measured only.
- PD-T269's cotangent partial fraction: treated as standard.
- C13-corner-value-lower (22) and its inputs (C07, PD-T270, PD-T269, C08 corner margin) are
  out of FAR scope. I took them as given and checked only how (22) is used.
