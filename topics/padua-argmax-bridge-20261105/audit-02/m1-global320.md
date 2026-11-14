# M1 — Interim Claude audit of the E14 global320 assembly (handoff 10)

Auditor: Claude, Opus 5.5, xhigh effort (chosen because this is an adversarial
mathematical audit of a novel multi-region assembly; WORKFLOW row "Adversarial
audit"). Role: independent auditor (subagent of the Claude interim-audit
orchestrator). No Git state change, no repository edit. Date 2026-11-07.

Rules read in full at the audited head: AGENTS.md, agents/WORKFLOW.md,
agents/claude/CLAUDE_ROLES.md, at
`1b6aa31ae759022ce89bb8a3be70a881790e259f` (branch
codex/padua-argmax-bridge-20261105). This head differs from the handoff-10
input head a68533f1 only in the two handoff files (`git diff --stat`).
Novelty scope: none. This sub-audit checks proofs and evidence only. It adds no
idea, mechanism or negative claim, so the full IDEAS read is left to the
separate ideas record.

Labels: [D] my own derivation, [E] my own execution, [I] inspection only.
T = topics/padua-argmax-bridge-20261105.

## Verdict

**Mathematics: ACCEPT (interim), no BLOCKING or MAJOR mathematical finding.**
I reconstructed the cover, defect/primitive logic, equality set and all-real-n
transfer myself, and recomputed the final scalar chain in exact Fraction and
outward-interval arithmetic. Under the named accepted premises (list below,
including the PD-T271 Arb-trusted constants), these establish the claim. For
every integer n>=320, max lambda_n = Lambda_c(n), attained exactly at
{(-1,-1),(1,-1)} for even n and {(-1,-1),(-1,1)} for odd n. I found 2 MINOR
items and 4 NOTEs.

**Protocol:** the MAJOR chronology findings P1–P4 are summarized below. They are
**not waived**. They do not affect mathematical validity, and they are preserved
honestly in their canonical records.

This audit makes no readiness decision. The branch stays WORK.

## 1. Reconstruction of the assembly [D unless marked]

Framework (PD-T364, read in full) [I]: theta=(J pi+alpha)/n,
phi=(K pi+beta)/m, m=n+1, J+K odd. The domain is
D_JK = {|alpha|+|beta|<=pi} ∩ {-J pi<=alpha<=(n-J)pi, -K pi<=beta<=(m-K)pi}.
On it, lambda = S_n(alpha,beta) - Delta_JK, with Delta_JK >= max(Q_h(J),Q_v(K)) >= 0.
S_n depends only on the phases, not on the centre. The charts cover [0,pi]^2,
ties included.

**Corner centres [D].** The only odd centres with both indices at endpoints are:
- (n,m), since 2n+1 is odd;
- (0,m) iff m is odd, i.e. n even;
- (n,0) iff n is odd.

(0,0) is even, so (1,1) is always a node. These centres are exactly the two
parity-correct nonnode corners. Every other odd centre has at least one interior
index, so at least one legal projected direction.

A noncorner chart never reaches an actual corner with rho<=pi. Reaching
(-1,-1) from (J,K) needs rho=(n-J+m-K)pi, and n-J+m-K is even, so it must be 0.
The case (1,-1) for even n is the same.

**Corner charts.** At (n,m): x=-cos(|alpha|/n) and y=-cos(|beta|/m). So
E12's (A,B) are exactly the inward phases (|alpha|,|beta|) with the literal n
and m. The same holds at (0,m) for even n via x->-x, and at (n,0) for odd n via
y->-y. These reflections preserve the node parity exactly in those parities, and
P_n is reflection invariant, so the cardinals permute and lambda is invariant.

At a corner chart:

| rho | Covered by | Reason |
|---|---|---|
| <=3/5 | E12 square | max(A,B) <= rho <= 3/5 < pi/4 |
| [3/5,1] | annular primitive | S < Lambda_c - 99/2500, Delta >= 0 |
| [1,pi] | outer primitive | S < Lambda_c - 13/500, Delta >= 0 |

The part of the pi/4 square beyond rho=3/5 is covered twice, which is harmless.
No corner chart ever uses a noncorner floor. The window pi/4 > rho > 1/2 asked
about in the brief is not a gap. Corners never use the half-near theorem, and
3/5 < pi/4.

**Complete closed cover of every chart (alpha,beta) in D_JK:**

| Chart / rho | Predicate | Source |
|---|---|---|
| noncorner, [0,1/2] | lambda < Lambda_c - 1/20000 | E14-halfnear320 |
| noncorner, [1/2,3/5] | lambda < Lambda_c - 3/1000 | E14-annular320 §3 |
| corner, [0,3/5] | lambda <= Lambda_c - (A^2+B^2)/30 | E12-corner256 |
| all, [3/5,1] | S < Lambda_c - 99/2500 | E14-annular320 §2 |
| all, [1,pi] | S < Lambda_c - 13/500 | E14-outer320 |

All predicates are closed in rho, so the seams 1/2, 21/40, 3/5, 1 and pi are
double-covered. Axes, clipped edge charts and chart ties are inside D_JK, and
every predicate holds for all signed phases.

**Nodes [D].** A node (j,k) with j+k even, seen from an odd centre, has
rho=(|j-J|+|k-K|)pi with an odd multiplier, so it occurs only at rho=pi. The
outer theorem then gives 1 = lambda <= S < Lambda_c - 13/500. The separate node
paragraph is redundant; see F1.

**Equality and maximum.** Every non-origin point is strictly excluded. At each
corner origin Delta=0 and S(0)=Lambda_c (PD-T364 (5)). Reflection makes the two
corner values equal, and continuity on the compact square gives the maximum. So
the argmax is exactly the stated pair.

**Exceptional x mode, collisions, weights, top coefficient ONE, literal n and m.**
These are framework-level. I inspected that each component claims them [I], and
my independent implementation agrees with them (§5, [E]).

**All-real-n.** Nothing is claimed for noninteger Padua objects. At each integer
n>=320, each component theorem is applied at that integer, inside its own
integer domain (n>=32/64/160/256). Each explicit scalar majorant is then bounded
by its n=320 value, using real-variable monotonicity of that scalar.

Directions I derived [D]:
- kWx = [87+(103/6)L]/n + 152/n^2. Its derivative is
  [(103/6)-87-(103/6)L]/n^2 - 304/n^3 < 0.
- db = (17L+27)/n^2 decreases: the numerator of its derivative is
  17 - 2(17L+27) < 0.
- C4 decreases. kNx and kNy decrease similarly.
- T' = (8L-3)/(pi^2 n) > 0.
- The floors Fn, Fs, Fh, Fw at fixed r improve with n. Their positive factors
  increase, and A0, Rh, Rw > 0 on [0,3/5] (checked [E]), so the losses decrease.
- In the half-near argument, (T+A4+rJN)' > (45/16)/n - (184/15)/n^2 - 78/n^3 > 0.

Directions inherited and accepted [I]: ebar decreasing (E08), E13's Gb and K
increasing and A decreasing, and E12's FA and FD increasing. I also checked all
of these on a log grid from 320 to 1e15 ([E], MEASURED, not a proof).

## 2. Defect/primitive logic and domain compatibility [D/I]

- lambda = S - Delta exactly, with Delta >= max of the eligible projections.
  The proofs only use one floor per eligible direction, or their max. They never
  add the two projections (halfnear §4, annular §3, assembly l.151–163).
- **Half-near.** Upper bound: the E09 near allowance. This uses E09's signed T
  (closed rho<=1/2, n>=32), D13's mesh rho/(2n) (rho<=1/2), E03/E04 near retained
  rows, E08 origin (n>=160) and E11's model on rho<=1/2. Floor: E01's Fn/Fs plus
  E01-F2's Fh on rho<=r<=1/2, n>=64, used at r = the actual rho. **Compatible.**
- **Annulus [1/2,3/5].** Upper bound: the wide allowance on closed rho<=1. This
  uses wide Tout (n>=32), D37's separate Rmesh rho/(2n) (rho<=1), D37's Erow,
  E04's wide retained rows (n>=32, rho<=1) and E11 (rho<=pi/2). Floors: Fn/Fs/Fw
  on rho<=r<=pi/4 (E01-F1), and Fh on rho<=r<=21/40 (E02 extension, n>=64,
  independently accepted). Fh is used only on [1/2,21/40] and Fw on
  [21/40,3/5]. Nothing is enlarged.
- **Scalar log not double-charged.** Rlog sits inside Tout. The old combined
  mesh/log term rho(L+7/3)/n is not added. Rmesh appears once, as the 1/2 in 155/2.
- **Collection.** The constants are 6+10+11+50+1/2 = 155/2, 148+4 = 152 and
  8+3/2 = 19/2 ([E] exact). Collecting them reproduces annular (3), with the
  one-sided origin used only as -uE(0) <= u*ebar.
- **Model bound.** Ec <= (5/12)x^{3/2} follows from E11's
  Ec <= kappa p^{3/2}/sqrt(a) - Bbeta, using:
  - kappa = 4 I4/pi^2 < 638/1773;
  - p <= x;
  - a >= cos^2(1/2) >= (7/8)^2.

  This gives slack 269/49644 [E]. The half-near 3/8 bound uses
  a >= (31/32)^2, with slack 1561/439704.

  The Bbeta >= (1679/8000) y^2 integral is
  ∫_0^b (1-e/b)(-log e) de = (b/2)[log(1/b) + 3/2]. I rederived it, together
  with b <= r (sin x >= 0) and b >= y [D].
- **Corner.** The axis losses use the old complete wide allowance at
  rho = pi/4 < 1, which is legal. The diagonal (pi/4, pi/4) uses only the full
  absolute E08 error with E11's closed pi/2 model, also legal. The global norm
  M(n) comes from absolute premises, not the one-sided origin.

## 3. Exact recomputation of the final scalar chain [E]

Rigorous own enclosures (check320.py, exact Fraction):
- log2: the partial sum 842/1215 + 2/15309 plus a tail of exactly 1/78732.
- log(5/4): the partial sum 488/2187 plus a tail of exactly 1/145800.
- From these, 57679/10000 < L320 < 5769/1000 (slacks 3.1e-4 and 6.8e-4).
- The pi enclosure 157/50 < pi < 22/7 is inherited.

Every displayed rational claim was re-derived, and it PASSES with the exact
slacks below. check_iv.py independently evaluated the literal functions in
40-digit outward interval arithmetic and confirmed every bound.

| Quantity (n=320 unless stated) | Claim | Exact or interval value; slack |
|---|---|---|
| T | > 293/25 | lower 141819452509/12100000000; slack 6.2e-4 |
| D, Mesh, ebar | < 27/200, 7/400, 249/1600 | slacks 9.4e-4, 1.8e-5; ebar bound exact |
| C4 | < 677/50000 | slack 2.6e-6 (needs pi > 157/50; pi > 3 would fail, but is not used) |
| kNx, kNy | < 11031/20000, 11056/20000 | certificates 705963/1280000 and 56602113/102400000 match |
| kWx | < 583/1000 | certificate 373019/640000; slack 1.58e-4 |
| kWy | < 117/200 | certificate 59808113/102400000; slack 9.4e-4 |
| T-ebar+j | > 2331/200 | slack 11/8000 |
| (11/48)·2331/200 - 8/3 | 41/9600 | exact |
| annular d1, d2, l1, l2 | 9/4, 8/3, 11/16, 47/80 | l1 slack 1/3000 |
| e, f, g | 72/59 > 61/50; 3029/4720 < 257/400; 3/5900 | slacks 1/2950, 9/11800; C4+g < 141/10000, slack 5.2e-5 |
| P(1/2), P(3/5), P(1) | 607/20000, -99/2500 | exact; P(1) = -2817/5000; vertex at r = 0.2633 < 1/2 |
| Ah, Bh, Aw, Bw | four-piece forms | exact match with E01/E02 formulas at 320 |
| exact floors | > 17/500 | Fn(3/5) = .075293, Fs(3/5) = .071877, Fh(21/40) = .048713, Fw(3/5) = .035448 (slack 1.45e-3) |
| annular gap | 73/20000 > 3/1000 | exact; slack 7.3e-4 |
| half-near e, f, g | 13429/10000, 29714/50000, 1/4000 | slacks 3.0e-5, 1.9e-5, 7.8e-7 |
| half-near min of Lh minus upper | > 1/20000 | 211651/2634560000 (8.03e-5); 34161^2 < 32·8233·4431 |
| half-near r <= 1/8 branch | gap > 13/1000 | upper .07629, Lh(1/8) = .09094 |
| outer Gb, K, A | > 3/40, > 10, < 7/5 | Gb = 195191/2400000 exact; interval values .1110, 10.83, 1.3458 |
| outer F | > 13/500 | 3/40 - (7/5)^2/40 = 13/500 exactly; interval F = .0692 |
| outer components | KD < 1/6, ..., Cl < 7/20 | all PASS, e.g. Cb = .8118 < .836, Cs = .6828 < .71 |
| corner256 dA, dD | 2293/4200, 881/1000 | exact |
| corner256 FA, FD | 2729/21000, 49/1000 | exact |
| corner256 final | (8/5)(49/2000) = 49/1250 > 1/30 | interval M(256) = 25.393 < 26, KD = .19929 < 1/5 (tight) |
| wide-T aggregation | 39073/1200 < 33; 33+65/4+23/96 = 4751/96 < 50 | exact |

The quadratic line maximum, max over x of
l1·x + l2(r-x) - d1·x^2 - d2(r-x)^2 = -e·r^2 + f·r + g, was verified
symbolically for general d and l (linemax_sympy.py).

**Where PD-T271 enters [I + D].** E06-H-consequences.md:45-80 takes PD-T271's
Arb outward enclosures of kappa_PD271 and Cstar. From them it derives H0 and
j > 23/250 (and t0 < 221/500, which is elementary). Through the Hmax/E06 map
this also gives C∞ < 9/4 globally. j enters the half-near (U), the annulus
(T-ebar+j), the outer (j*) and the corner (dA, dD). C∞ < 9/4 enters the corner
norm M(n). C∞(0) > 4383/2420 (D08/PD-T271) enters only the redundant node
paragraph.

These are n-independent limit constants, so PD-T271's scope trivially covers
n >= 320. Its n >= 32 remainder bound R_n is unused. The result is therefore a
paper proof plus one inherited, Arb-trusted, independently re-run constant
enclosure. The records state this correctly (assembly l.225, outer l.134).

## 4. Named premise chain: existence, scope, use [I; hashes E]

All cited byte-prefix and report hashes match the files at the head
(prefix_hashes.py: 12 MATCH).

The upstream premises E08 phase-global (8886d44e = prefix 15281 B), E08 origin
(bba01a43 = 15142 B), E11 pair (dea44db8 = 10942 B) and E11 pi/2 model
(695800c1 = 10157 B) match. The review hashes 3407c50d, bf146792, 92775b0d,
2c2efa0f, 6272730f and de9a18a2 match their independent-checks files.
461214a5 and b6a9db93 are the E07-H and E06-H **review** hashes (see F2).

| Premise | Stated domain | Used where | Within domain? |
|---|---|---|---|
| E07 Hmax and E06 map (PD-T271) | ΔC∞ <= Ec - ju on closed rho <= 1; C∞ < 9/4 global | halfnear, annulus, corner | yes |
| E08 phase-global absolute | whole closed diamond, n >= 32 | corner diagonal and norm | yes |
| E08 origin lower | E(0) > -ebar, n >= 160 | all regions | yes |
| E09 signed T (47) | closed rho <= 1/2, n >= 32 | halfnear only | yes |
| E10/E11 model | closed rho <= pi/2 | rho <= 1/2, rho <= 1, (pi/4, pi/4) | yes |
| E12 corner | n >= 256, closed pi/4 squares | corners, rho <= 3/5 | yes |
| E13 envelope/gate | closed 1 <= rho <= pi, n >= 32 (ebar variant n >= 160) | outer | yes |
| wide signed T (50) | closed signed rho <= 1, n >= 32 | annulus | yes |
| D37 Erow, Rmesh; E04 wide retained | rho <= 1, n >= 32 | annulus | yes |
| D13 mesh; E03/E04 near retained | rho <= 1/2, n >= 32 | halfnear | yes |
| E01-F1, E01-F2, E02 band extension | n >= 64; r <= pi/4, 1/2, 21/40 | floors | yes |

**No premise is used outside its stated domain.** E15 (n >= 192, rho >= pi/2,
regional only) and E12's axis-only T are not used (assembly l.208-209, confirmed
by grep).

## 5. Independent float sanity run (MEASURED, not proof) [E]

sample320.py implements its own PD-T364 kernel and cardinal formulas. Its
self-tests at n=5,6 all PASS:
- the closed-form G_n matches the direct D_n double sum, including at
  collisions;
- the partition of unity holds;
- the cardinal property holds at every node.

Results at n=320 and n=321:
- Lambda_c(320) = 22.4067100682 and Lambda_c(321) = 22.4251113062.
- S(0) equals Lambda_c exactly.
- Both parity-correct corners agree to within 4e-14.
- Nodes give lambda = 1 to within 6e-13.

With 400 random phases per region, chosen mostly at noncorner centres within L1
distance 8 of the corners, the minimum observed excess over each claimed margin
was:

| Region | n=320 | n=321 |
|---|---:|---:|
| halfnear | 1.087 | 1.682 |
| annulus | 1.625 | 1.837 |
| [3/5,1] S-gap | 0.683 | 0.680 |
| outer | 2.153 | 2.122 |

In the corner squares, (Lambda_c - lambda)/(A^2+B^2) was at least 4.11, against
1/30 needed. There were no violations. The analytic margins are therefore very
conservative, as expected for a sufficient onset.

## 6. Chronology findings P1–P4: summary, not waived [I]

**P1 (MAJOR, unwaived).** Source: independent-checks-E09-global384.md:344-361;
canonical record attempts/E09-assembly384.md. The first CEhat quotient
intuition, and early conditional central-coefficient intuition, came before the
full newly entering E08-origin, E09-signed and E10 records had been read. This
is contrary to "Generate candidates only after that gate."

**P2 (MAJOR, inherited, unwaived).** Source: E09 signed-T P1,
independent-checks-E09-signed-outer.md:90-115. A tentative axis
monotone-coefficient observation came before the last fresh mechanism search and
shortlist read.

**P3 (MAJOR, inherited, unwaived).** Source: E08 origin P1,
independent-checks-E08-origin.md:273-316. Four E02/E03 full operator records
were completed after the first operator intuition.

**P4 (MAJOR, unwaived).** Source: independent-checks-E14-global320.md:653-691;
canonical records ideas/E14-assembly320.md:106-117 and
attempts/E14-assembly320.md:53-77. The explicitly requested local annular
inventory was appended after the first 155/2 collection and radial sign
reasoning. The prior full gate, root's prospective 155/2 proposal and the wide
adoption did precede the work.

**Effect on mathematical validity: none.** These are order-of-work findings. I
re-derived the mathematics independently of chronology (§1–§3).

**Honest preservation: yes.** The author records state the late order in plain
words, without backdating. The first snapshots are hash-preserved (prefix
hashes verified). Every root adoption appendix says P4 and the E08/E09 findings
remain unwaived (assembly l.225, annular l.200, handoff 10 l.43). I do not waive
or downgrade any of P1–P4. See also F4.

## 7. Findings

- **F1 MINOR — node paragraph cites an unnamed premise and is redundant.**
  - Location: T/theory/E14-assembly320.md:178-185.
  - Problem: "C_infty(0)>0" is not given a source. It is in fact the
    D08/PD-T271 limiting-origin lower C∞(0) > 4383/2420 (D27-wide-corner.md:52,
    D24-far-constant.md:30). The step "Lambda_c > 4(log n)^2/pi^2 - ebar" also
    needs the exact form M∞(0,L) = (4/pi^2)L^2 + b_c L + C∞(0), which is
    likewise unnamed.
  - Why it is harmless: the paragraph is logically unnecessary. Nodes occur only
    at rho = pi (§1), where outer320 already gives 1 = lambda < Lambda_c - 13/500.
  - Fix: a dated addendum naming the source, or noting the redundancy. No
    mathematical change.
- **F2 MINOR — citation clarity.** "Hmax461214a5 and consequence mapb6a9db93"
  (E14-assembly320.md:138-139; E12-corner256.md:38) reads as theory identities,
  but these are the SHA256 of independent-checks-E07-H.md and
  independent-checks-E06-H.md. Suggest a one-line clarification.
- **F3 NOTE — two meanings of "kappa".** It is 4·I4/pi^2 ≈ 0.359 in E10/E11/E12
  and E14-halfnear320.md:21, but PD-T271's kappa ≈ 0.9197 in
  E06-H-consequences.md:49-51. There is no mathematical consequence. It is only
  a reader hazard.
- **F4 NOTE — chronology rulings for AC to reconcile.** The same factual pattern
  (local inventory after first checks, with an earlier prospective root
  registration) was ruled "no violation" for the wide T operator
  (independent-checks-E14-wide-signed.md:351-385). It was ruled MAJOR for the
  annulus (independent-checks-E14-global320.md:653-691). The only stated
  difference is the explicit narrower annular task instruction. Both rationales
  are on record. I keep P4 MAJOR and unwaived, and flag the consistency question
  for AC's procedural disposition.
- **F5 NOTE — historical status lines.** E14-assembly320.md:3 still reads
  "Status: OPEN global320 target", and the support files still read "distinct
  review pending". These are the hash-preserved first snapshots. The current
  status is given only in the dated closure (l.53) and the root adoption
  (l.225). This complies with the append-only rule, but readers must read to the
  end.
- **F6 NOTE — tightest exact margins.** All margins are verified and none is
  misused:
  - C4: 2.6e-6.
  - Mesh: 1.8e-5.
  - Half-near final gap: 3.0e-5 above 1/20000.
  - e - 61/50 = 1/2950.
  - kWx: 1.6e-4.
  - Corner KD: 0.19929 against 1/5.
  - Fw(3/5) - 17/500 = 1.45e-3.

  These are tight for the stated rationals. They do not affect validity, and the
  observed true gaps are far larger (§5).

My review agrees with Astra's (independent-checks-E14-global320.md). I read it
only after my own reconstruction. Astra's checks were hand algebra, with no
execution. The checks in §3 and §5 above are new, independent executions.

## 8. Executions (all in .../audit2/m1-code/, Python 3.13.18)

The CPU cap is about 15 minutes. Total CPU used is about 4.3 minutes. Every
script is read-only with respect to the repository.

| # | Command | CPU | Exit | Note |
|---|---|---:|---:|---|
| 1 | `python3 -I check320.py` (first version) | 0.03 s | 1 | Only FAIL was the auditor's own pi>3 variant of C4, which is not a record claim |
| 2 | `python3 -I check320.py` (variant relabelled INFO; record certificate 16678/16076800 checked) | 0.03 s | 0 | 142 PASS; sha bc943fc5…, out 22c0cd3c… |
| 3 | `PYTHONPATH=../pylib python3 check_iv.py` (mpmath 1.3.0 iv, 40 digits) | 0.66 s | 0 | sha e8cb3870…, out 927f6319… |
| 4 | `PYTHONPATH=../pylib python3 linemax_sympy.py` (sympy 1.14.0) | 0.53 s | 0 | out c06bf8ee… |
| 5 | `python3 -I prefix_hashes.py <T>` | <0.1 s | 0 | 12 MATCH; plus an ad-hoc prefix scan of 6 upstream files, about 1 s |
| 6 | `python3 -I sample320.py 20261107 20` (numpy 2.5.3) | 5.2 s | 0 | trial |
| 7 | `python3 -I sample320.py 7 400` | 95 s | 1 | see below |
| 8 | the same, after adding a 1e-11 roundoff tolerance | 152 s | 0 | sha f22f51c9…, out 2f19ffe8… |
| 9 | `python3 -I check_wide.py` (first version) | <0.1 s | 1 | see below |
| 10 | `python3 -I check_wide.py` (corrected) | <0.1 s | 0 | out b36e9b20… |

Run 7 flagged one point at the corner origin, with A, B ≈ 3e-12 and
Lambda_c - lambda = -3.6e-15. This is float64 rounding, below the resolution of
22·2^-52. The output is preserved as sample320_run1_exit1.out (fc7f427a…).

Run 9 failed because of an auditor-script bug: it tested strict inequality with
pi set equal to its upper bound 16/5. The record's claim is correct, because
pi < 16/5 strictly.

## 9. Not independently re-derived (inspection or inherited only)

- **Framework.** PD-T364/PD-T101: the cover lemma, the identity
  lambda = S - Delta, and the endpoint reflection. I only checked them in float
  at n = 5, 6, 320, 321.
- **Floor proofs.** The E01-F1/F2 nearest/small/middle class geometry and the
  E02 band extension. I re-evaluated their formulas, not their proofs.
- **Finite-error proofs.**
  - The E09 signed-T proof (rho <= 1/2).
  - The E14 wide signed-T analysis: right-rectangle sign, BV/atom variation,
    D37 §6b cancellation and E02 Shift. I checked only its constant
    aggregation.
  - D37 Erow and Rmesh; E03/E04 retained rows; D13 mesh.
- **Model and scalar cores.**
  - The E10/E11 model decomposition and the definition of the Bbeta baseline.
  - The E07 scalar Hmax theorem and the E06 consequence map.
  - PD-T271's Arb enclosures.
  - The C08/C04 profile facts.
- **Error and corner machinery.**
  - The E08 phase-global absolute error and the E08 origin lower.
  - E13's geometry and envelope derivation. I re-evaluated only its base
    coefficients.
  - The D08 squared-Peano corner interpolation and the D27 norm adapter.
  - The model-loss inequality M∞(0) - M∞(phi) >= u(T+j) - ...
