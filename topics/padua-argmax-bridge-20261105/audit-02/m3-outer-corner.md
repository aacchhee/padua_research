# m3 — Interim audit: outer/far error chain, actual-corner squares, far192, chronology

Auditor: Claude Opus 5.5, xhigh (independent mathematical auditor subagent of the handoff-10
Claude orchestrator). Developer of every audited record: Codex. Rules read in full at branch
head `1b6aa31ae759022ce89bb8a3be70a881790e259f` (AGENTS.md, agents/WORKFLOW.md,
agents/claude/CLAUDE_ROLES.md). Branch `codex/padua-argmax-bridge-20261105`. No state-changing
Git command was run and no repository file was edited (`git status --short` is empty). T below
means `topics/padua-argmax-bridge-20261105`.

Labels: [D] my own derivation, [E] my own execution, [I] inspection only.

## 0. Identities and coverage

Frozen proof prefixes match the reviewed identities [E]: E15 first 13855 B = `b420adbd…`,
E12-corner256 first 9921 B = `586c4e07…`, E13 first 15350 B = `d78a57c0…`. The E14 records keep
their first-commit prefixes (`git show 2d45727`/`c5e05a2` vs current head): ideas/E14-assembly320
6730 B `2c7cc448…`, attempts/E14-assembly320 2978 B `bbafcd3c…`, theory/E14-outer320 5565 B
`17baa09b…`, independent-checks-E14-global320 19661 B `2f390ef7…`. checker.py at head:
sha256 `55f4a4b8dab6c679…`.

Read in full: theory E13-joint-radius-outer, E14-outer320, E15-analytic-far192, E12-corner256,
E12-assembly256, E12-assembly256-obstruction, E08-allocation-obstruction; E08-phase-global-error
§§statement–1 and §monotonicity; E09-correlated-outer384 §§1–3; E14-halfnear320 §3;
E14-wide-signed-outer statement/§1–2; checker.py (all) and SPEC.md lines 80–225; checks
E13 (verdict, §7), E14-global320 §§6–7 and P4, E15 (verdict, §§2,4, disposition),
E12-corner-frontier (verdict, §§3,5,6), E14-wide-signed (verdict, §7), E08-origin §5,
E09-correlated-outer (P1, §4, disposition), E09-signed-outer (P1), E09-global384 §7;
canonical disclosures in ideas/E08-origin-lower, attempts/E09-assembly384,
attempts/E09-signed-outer-upper, ideas/attempts E14-assembly320.
Inspection only (statements/dispositions, not proofs): E01-*, E02-*, E03-*, E04-assembly640
(eqs. 3–4), E04-wide-corner1, E08-corner384, E09-signed-outer-upper, E12-signed-outer-coupling,
D13-mesh-support, D37-relative-wide, E06-H-consequences, all other independent-checks-E0x/E1x
via disposition greps.

Novelty scope: this subagent audits mathematics and chronology only; it makes no novelty or
idea claim. I did NOT read the full 1154-line `state/IDEAS.md`. The negative-claim check in §4
is limited to the internal scope of the two named records; a novelty/registry-level check of
negative claims belongs to the orchestrator's main audit.

## 1. Execution record [E]

Scripts in `.../scratchpad/audit2/m3-code/` (absolute:
`/tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit2/m3-code/`).
Formulas were retyped from the theory files, not imported from repository code.
Environment: Python 3.13.18, mpmath 1.3.0 (pip `--target audit2/pylib`; pip printed only
"target exists/root" warnings), `mpmath.iv` outward interval arithmetic at 200 bits.

| Command (cwd m3-code, `PYTHONPATH=audit2/pylib`) | user CPU | exit | output sha256 (16) |
|---|---:|---:|---|
| `python3 -P envelopes.py > envelopes.out` (run twice) | 0.53 s each | 0 | `4218ff20ee78feb2` |
| `python3 -P geometry.py > geometry.out` | 4.52 s | 0 | `ebdfb4803b068d13` |
| `python3 -P obstructions.py > obstructions.out` (twice) | 0.04 s each | 0 | `481b716f98d333d7` |

Script sha256 (16): envelopes `1704c737a5f28cf0`, geometry `5246af3d65ae22e4`, obstructions
`86d1022d2132952d`. Total scientific CPU ≈ 6 s, far below the 15 CPU-min cap. A first attempt
with `python3 -I` exited 127 before running (`/usr/bin/time` absent; `-I` also ignores
PYTHONPATH); it produced no result and was replaced by `-P`.

Interval checks are rigorous enclosures of the stated scalar inequalities; the n-scans and
phase/u grids are MEASUREMENTS only (the proofs of all-n/all-phase directions are §§2–4 [D]).

## 2. Task 1 — E13 envelope and E14-outer320 (gap 13/500, n>=320)

Component list [D], from E13 §2 (T/theory/E13-joint-radius-outer.md:105–221) applied on top of
E08's absolute theorem |S−M∞|<=CEphi+KD·P (E08-phase-global-error.md:41–61):

| E08 component | E13 base (v-free) | sqrt(v) coeff | v coeff | n-dependence |
|---|---|---|---|---|
| ordinary rows Dphi=a·Da+10/n² | D_env=a0·Da+10/n² | – | – | H/n, H/n², 1/n² |
| ordinary P charge KD·P | P0·KD | – | 4KD | H/n |
| outer Gphi: 7L·MA/m | 7L·MA_b/m | η·7L/(πm) | – | L/m |
| outer VB/(2m) (entropy Γ, ℓ, d·log2) | VB_b/(2m) | [η(3γ_b+2ℓ)+6log2]/(2πm) | 12ℓ/(πm) | Γ_b/m, γ_b/m, ℓ/m |
| outer holes (4/m)[7+(P/π)(5+2log2m)] | P0 version | – | 16(5+2log2m)/(πm) | log(2m)/m |
| outer 4d·logπ/(πm), 2CB/m | 2CB_b/m | 12logπ/(πm) | – | 1/m |
| six retained rows C6phi | R6_env (p,q→p0) | η(48H+24)/(πn) | – | L/n, H/n, 1/n² |
| full scalar mesh Mphi | M_env (ce+cd→w0, a→a0) | – | – | L/n, log/(n²) |
| scalar log d·W | – | 3W | – | log m/m |
| actual origin (one-sided) | whole ebar=D+Mesh+1/n (n>=160) | – | – | H/n, L/n |
| cusp | none separate: the cusp is inside CEphi's literal ℓ/Γ terms | | | |

I re-derived that these substitutions are exactly C_b, C_s, C_l of E13 (2) with no leftover
term [D]: each replaced variable enters with a nonnegative coefficient; Γ is increasing and
concave in p (Γ_p=1+log(1+C/p)−C/(p+C)>0, Γ_pp<0), so the tangent at p0 plus
p−p0<=η√v is legal also when p<p0 (γ_b>0); P<=P0+4v and d<=3√v come from E13 (1).
E13 (1) geometry [D]: re-proved every branch (x<=1/2; 1/2<=x<=1 using y>=1−x, i.e. rho>=1;
x>=1 with u<=1/4 and u>=1/4), the identity |p−q|=2√(ce²−a²), and the tangent of
S(u)=2√(2u−u²) at u1 (47·721=33887; integer comparisons as stated). The key margin
u_min=1−cos(1/2)>u1 is 2.2e-5 (cos(1/2)<1−1/8+1/384=337/384). Sampling of the closed diamond
1<=rho<=pi including both seams rho=1, rho=pi [E, measurement]: all six inequalities hold
(min slacks: v 2.2e-5 at (1/2,1/2); p-cap 3.9e-3; |p−q| 4.6e-3; P equality case x=y only
at float noise −4e-16).

Model/origin assembly [D]: Λc−S = [M∞(0)−M∞(φ)] + E(0) − E(φ) >= u(T+j)−t0·p − ebar −
(C_b+P0KD+C_s√v+(C_l+4KD)v); with u=u1+v, p<=p0+η√v, j>j*=23/250, t0<t*=221/500 this is
exactly E13 (8)/E14 (2): Gb+Kv−A√v. K>0 is established before completing the square. ✓

Arithmetic at n=320 [E] (all PASS, interval widths < 1e-50):
Cb=0.81176<209/250, Cs=0.68278<71/100, Cl=0.33469<7/20, KD=0.16480<1/6,
ebar=0.15407<249/1600<5/32, T=11.7319>293/25, Gb=0.11100>3/40, K=10.830>10, A=1.3458<7/5,
**F(320)=0.06919>13/500**. Every intermediate written bound of E14-outer320:39–103 (L, H,
log m, log 2m, W, ℓ<13/3, 1+C/p0<2m, Γ_b, γ_b, MA_b, CB_b, D_env, VB_b, G_env, R6_env, M_env,
the three Cs eta-pieces, (log2+4logπ)/(πm)) also passes. Exact Fractions: the Gb numerator
(E14-outer320:119–120) equals 195191/2400000 exactly; K lower 16193/1500>10; A upper
1373/1000<7/5; 3/40−(7/5)²/40=13/500 exactly; Cb sum 209/250; Cs 141/200.

All n>=320 [D]: re-derived every direction claimed in E13 §3/§4 (L/m, log(2m)/m, (L+r)/n,
ℓ/m via m·ℓ'=ε·cotε<=1<ℓ, Γ_b/m via m·Γ_b'<p0<=Γ_b, γ_b/m via m·γ_b'<1<γ_b, the mesh tail
sign (n−1/2)/(n+1/2)−2log(n+1/2)<0, T'>0 for L>3/8). Hence C_b,C_s,C_l,KD,ebar decrease, T
increases, so Gb,K increase, A>0 decreases, F increases while K>0. The transfer uses the
envelope coefficients at each integer n directly (no CEphi/u order, no S or Λc monotonicity).
Scan n=320…1e12 [E, measurement] confirms the directions; F(1e12)≈36.6.
Measurement only: with the same constants, rigorous K>0,F>0 first holds at n=307 (headroom
at 320; not a claim of a smaller onset).

Seams/literal objects: rho=1 and rho=pi closed in (1) and in the sampling; m=n+1 enters ℓ, W,
Γ, G (my code uses literal m); signed phases via separate absolute values, collisions and the
six labels are inherited from E08 [I]. E14-outer320 (1) is therefore supported.

## 3. Task 2 — E12-corner256 (both closed pi/4 squares, loss 1/30)

Structure [D]. Chart Λn(A,B)=λn(−cos(A/n),−cos(B/m)), h=π/4. Three ACTUAL point losses
(λ<=S, S(0)=Λc):
- axes (h,0),(0,h), rho=h<1: wide finite relative formula (E04-assembly640 eq. 4) with the
  one-sided origin −uE(0)<=u·ebar, Ec(h,0)<κp^{3/2}/√a<6/25, Ec(0,h)=−Bβ<=0, u_A>q0=7/48,
  giving δ_A=q0(T−ebar+j)−1/4−C4−h·kWy (needs T−ebar+j>0; kWx·x+kWy·y<=kWy·rho);
- diagonal (h,h), rho=π/2: E11 closed half-π MODEL plus only the GLOBAL absolute error
  CEbar+KD·P (P=√2<3/2), δ_D=2q0(T+j)−4/15−CEbar−(3/2)KD−ebar.
Squared Peano (D08): with U=V=h²/2=π²/32 the requirement is δ−M·U²/6=δ−Mπ⁴/6144>0,
δ=min(δ_A,δ_D/2); radial coefficient (16/π²)(δ−Mπ⁴/6144). I checked this is identical to
the hybrid checker's n<256 rule (checker.py:94–98) specialised to u'=v'=1/32:
q=32δ, t=Mπ⁴/192, (q−t)/(2π²)=(16/π²)(δ−Mπ⁴/6144) [E exact].
Global norm M(n)=[4L²+(79/5)L]/π²+9/4+CEbar+2KD: built from the absolute E08 corollary and
global C∞<9/4 only; ebar is not used — the remark "global signed norm from absolute premises,
not one-sided origin" is correct [D]. The 9/4 (E07/E06) carries PD-T271.

Arithmetic at n=256 [E] (all PASS): T=10.777>107/10, D<1/6, Gg<5/8 (collected and defining
forms agree), (64+16L)/n+318/n²<61/100, Mesh<11/500, W<7/250, CEbar=1.405<3/2, ebar<1/5,
KD<1/5, C4<9/500, kWy<93/100, M=25.39<26, δ_A=0.570>2293/4200, FA=0.164>1/8,
δ_D=1.012>881/1000, FD=0.199>49/1000, **coefficient 0.1674>1/30** (written chain gives
49/1250). All exact rational chains in E12-corner256:181–216 reproduce; 125·22⁴<2·7⁴·6144;
8(q0−rU)=779/750, 3q0+(79/5)rU=6903/10000; κ<638/1773<9/25; κ/√2<9/35.
All n>=256 [D]: FA's leading part [4(q0−rU)L²−(3q0+(79/5)rU)L]/π² increases for L>=1, its
subtracted costs q0·ebar+C4+h·kWy+rU·CEbar+2rU·KD decrease (kWy=[(49/2)L+587/6]/n+(179+17L)/n²
re-expanded); same for FD. Scan [E, measurement] agrees; FA,FD>0 first at n=239.
Geometry/scope [D]: inward phases A,B>=0 from the corner; closed A=π/4 or B=π/4 edges are
included because the three losses are at the square's corners and D08 interpolates on the
closed square; the square contains A+B<=1/2. Both parities via node-preserving reflection [I].
Hybrid use [D]: for n>=256 NEAR-only leaves satisfy π·high<π/(2·22/7)<1/2 (checker.py:107–108),
so corner-centre points they cover lie inside the square; FAR/SPLIT-far leaves require U<L.
Dependencies: PD-T271 (j>23/250, C∞<9/4, E11 regular part), E11 I4<319/360 (measured
I4=0.874019 [E]), E08 phase-global and origin, E04/D37/E02/E04-wide-retained-origin wide
allowance, D27 adapter, D08 Peano, D32 chart.

## 4. Task 3 — E15 (every n>=192, closed π/2<=rho<=π, gap 3/100)

[D] On rho∈[π/2,π]: a=ce·cd<=cos(π/4)<17/24, so u>7/24=u0 (also at the seam rho=π/2; at
rho=π, a=0, u=1). E09 caps F,Q,C re-derived (cos x>=1−2u squared only when RHS>=0).
CEphi<=CEhat(n,u) by monotone substitution; CEhat/u decreasing (entropy via homogeneous
Ψ(F/u,[(1+c)/u−c])), hence G_n/u increasing, so G_192(u)>=(u/u0)G_192(u0) for u>=u0.
Transfer to n>=192 uses accepted fixed-phase decrease of CEphi (E08 check §5), KD, ebar
(n>=160) and increase of T — legal, no CEhat n-order needed.
[E] At (192,7/24) every written bound of E15 (8)–(20) passes; CEhat=1.598<17/10;
G_192(u0)=0.1990>79/2000; the rational chain (21) equals 79/2000 exactly. Measurement:
G_192(u)/u increasing on a 202-point u grid; G_n(u0) increasing on an n-scan; anchor first
closes at n=181.
Hybrid scope [D]: checker.py:36–42 accepts an f leaf iff n>=192 and 1/2<=al+bl<=1 on a raw
box in normalised phase units (columns a_pi,b_pi, checker.py:216). Every point of box∩{a+b<=1}
has π/2<=π(a+b)<=π — exactly E15's closed region; the guard needs no π rounding. Points above
the hypotenuse are folded copies owned by other leaves. E15 gives S<Λc−79/2000; λ<=S is the
D32 chart premise [I]. The engine's use is within scope. Premises of E15 are exactly those
accepted at the used scope: E09 §2–3 generic lemma (stated "fix any n>=32", accepted in
independent-checks-E09-correlated-outer.md §4), E08 phase-global, E08 origin (n>=160), E06/E07
(PD-T271), C08 [I]. E13/E14 are not premises (E15 adopted 03:36:52 +0100, before E14-outer320).

## 5. Task 4 — scoped negative statements

E08-allocation-obstruction [E exact/interval + D]: P384(e)>25/256 (sum reproduces exactly),
Fh<31260383/348480000<9/100, GO384<−12137/48000; R(1/6,1/6), kNx(384), T(384)<13 bounds
pass. Scope (lines 8–10, 92–103, 132–145) and root NOTE N1 restrict the failure to the OLD
explicit relative upper + selected floor formulas; no actual counterexample, no rejection of
min(Uabs, relative) or of the new E09/E10 tools. Honest.
E12-assembly256-obstruction [E + D]: P256 sum = 21389/230400 = 9/100+653/230400 exactly;
re-derived the Bβ upper (6) in closed form ((a/4)c0²(3/2−log c0+ζ)·4/π²); Bβ quadrature
0.0092772<1/100 [E, measurement]; T(256)<271/25, kNx>10297/15360, u<1/72, c0∈(1/6,12/71).
Lines 9–12 and 131–137 restrict the claim to THIS relative upper with THIS selected-band floor
recipe at x=y=1/6, n=256; E12-assembly256.md:14–16 and the root adoption repeat that it is not
a global256/actual-argmax/all-toolkit failure. Honest. One dependency is unnamed: see m3-4.

## 6. Task 5 — dispositions and premise acceptance

| Record | Disposition | Open condition |
|---|---|---|
| E13 check | ACCEPT math; no new protocol violation | sufficient gate K(N)>0,F(N)>0 must be proved per base (done only at 320 by E14) |
| E14-global320 | first prefix: supports ACCEPT, global HOLD; continuation: FINAL ACCEPT; P4 MAJOR unwaived | P4 |
| E14-wide-signed | ACCEPT; no new violation | Rmesh, rows, origin remain separate charges |
| E15 check | ACCEPT regional | future physical use must verify PD364 chart and whole-cell guard (I checked the guard; chart [I]) |
| E12-corner-frontier | FINAL ACCEPT (corner, scoped failure, OPEN global256) | none |
| E12-signed-coupling | ACCEPT | fixed-phase asymptotics (A) non-uniform by statement |
| E08-phase-global | ACCEPT incl. "explicitly conditional all-n/norm consequences" | needs a separately proved model inequality uT−Q(φ) (supplied by C08+E06/E07) |
| E08-origin | math ACCEPT; P1 MAJOR unwaived | one-sided only; E_n(0)>=0 OPEN |
| E08-frontier | ACCEPT scoped failures; NOTE N1 | its origin hypothesis was conditional then; later accepted |
| E08-corner384 | ACCEPT | none |
| E09-correlated-outer | math ACCEPT; P1 MAJOR unwaived | — |
| E09-signed-outer | math ACCEPT; P1(=P2) MAJOR unwaived | — |
| E09-global384 | FINAL math ACCEPT; P1–P3 MAJOR unwaived; NOTE N1 | — |
| E06-H | ACCEPT incl. conditional (Hmax) implications | discharged by E07-H acceptance (E06-H-consequences:371) |
| E02-paired-outer | ACCEPT; P1 MINOR CLOSED | — |
| E01/E02/E03/E04/E05/E07/E10/E11 others | ACCEPT [I, greps] | none found open |

Downstream premise check [I/D]: every premise cited by E13, E14-outer320, E15, E12-corner256
and the hybrid identities is a record accepted at (at least) the used scope, with one
documentation gap: E12-corner256:94 uses E04-assembly640 eq. (4) at n=256 "component-wise
n>=32", while E04-assembly640:11 states its theorem for n>=640. My spot checks find the
components stated for n>=32 (D37-relative-wide:10,33 closed rho<=1; E04-wide-retained-origin:11;
E02-paired-outer:11), so no gap was found, but no review record explicitly makes this domain
transfer (m3-2). The same transfer was used earlier at 384 (E08-corner384:65–70) and 512
(E07-global-assembly:36).

## 7. Chronology P1–P4 (read fully; not waived)

| ID | What happened (canonical record) | Rule touched | Math validity | Original chronology kept? |
|---|---|---|---|---|
| P1 (E09 global384/outer) | first CEhat u-cap/entropy-homogeneity intuition and early conditional E10 central intuition before full reads of the newly entering E08-origin/E09-signed records; reads complete by 01:30:38 UTC (attempts/E09-assembly384 §"Canonical narrow gate-timing limitation") | WORKFLOW novelty gate, "Generate candidates only after that gate" | none: I re-derived the quotient lemma (§4); no priority claim | yes; single first commit 5152857 (01:39:39 UTC) contains it |
| P2 (E09 signed T) | tentative α-axis monotone-coefficient observation during requested operator inspection, before the LAST fresh search/shortlist read; general proof after gate (attempts/E09-signed-outer-upper:11–20) | same rule | none | yes; single commit 1ebd7a8 |
| P3 (E08 origin) | first operator intuition while adapting E02/E03 sections before four full E02/E03 idea/theory records were read (ideas/E08-origin-lower:89–104) | same rule | none; but this one-sided ebar is a premise of E13, E14-outer320, E15, E12-corner256 | yes; single commit 554b975 |
| P4 (E14 annular) | requested local annular inventory appended AFTER first 155/2 coefficient collection and radial sign reasoning (ideas/E14-assembly320:106–116; attempts:53–69; review :653–691) | explicit narrower root task instruction; family inventory and root proposal were prospective | none in my scope (annular not re-derived) | yes; first-commit prefixes unchanged (§0) |

My assessment: none is BLOCKING (no claimed status is undermined). Under WORKFLOW's literal
scale all four are MAJOR — they "must be fixed before PR", yet elapsed chronology cannot be
repaired, so the only resolution is an explicit AC disposition before readiness. In substance
I rank them P1 > P3 > P4 > P2: P1/P3 breach the binding gate rule for mechanisms that are now
premises of the hybrid's analytic leaves; P4 breaches a root instruction, not WORKFLOW text;
P2 concerns a preliminary observation only. Limitation: E12/E13/E15/E14 idea, theory, attempt
and review files were each first published in one adoption commit, so all pre-publication
orderings rest on self-report and review-time prefix hashes; Git shows no backdating after
first publication but cannot confirm the internal order (m3-6).

## 8. Findings

No BLOCKING or MAJOR mathematical finding in this scope.

- **m3-1 MINOR** — checker.py:28 and :33 dependency identity strings are incomplete. E12's
  list omits the wide finite relative allowance used at the two axis points (E04-assembly640
  eq. 4 and its E04-wide-retained-origin/E02-paired-outer/D37 components), the D27 norm
  adapter and the D08 Peano interpolation (only "E12 global signed-cardinal norm and squared
  Peano" is named). E15's list omits C08's full-coefficient model loss −uT. The strings are
  metadata, not proof gates (SPEC.md:216–217), so nothing changes mathematically. Recommend
  completing the list in prose (SPEC/delivery addendum) rather than editing frozen code.
- **m3-2 MINOR** — E12-corner256:94 transfers E04-assembly640 eq. (4) (theorem headline
  n>=640, E04-assembly640:11) to n=256 as "component-wise n>=32" without a citation table;
  independent-checks-E12-corner-frontier §§3,5 do not record this domain check. The spot
  checks in §6 support it. Add one line naming each component's n>=32, rho<=1 source.
- **m3-3 NOTE** — Symbol clash: κ≈0.91971 is a PD-T271 constant (E06-H-consequences:45–52),
  while κ=4I4/π²≈0.354 in E11/E12 (E12-corner256:45). Both are defined locally; no error.
- **m3-4 MINOR** — The negative statements use an UPPER bound j<1/4 (E08-allocation-
  obstruction:46; E12-assembly256-obstruction:66–67) that rests on the PD-T271 enclosures
  (H0 via κ_PD271). Their scope sections do not name this computer-assisted dependency.
  Add it to both PD-N records.
- **m3-5 NOTE** — Developer and all distinct reviews of E12-corner256, E13, E14-outer320
  and E15 were paper-only; §§2–4 are the first executed rechecks. All pass with large
  headroom: F(320)=0.069 vs 0.026; G_192(u0)=0.199 vs 0.0395; corner coefficient 0.167 vs
  0.0333. Measured first-closing bases (307, 181, 239) are MEASURED cost-reduction leads only;
  each would need its own written base arithmetic and review before any use.
- **m3-6 NOTE** — Chronology verification is limited to post-publication append-only
  checks (§0, §7). Separately, independent-checks-E14-wide-signed §7 treats a local inventory
  written after first checks as no violation, while P4 treats a similar order as MAJOR; the
  difference rests on an explicit root instruction. AC should apply one rule when
  dispositioning.
- **m3-7 NOTE** — E13's header word "conditional outer reduction" names a PROVED
  implication with explicit hypotheses K(N)>0, F(N)>0, not a CONDITIONAL status. The handoff
  correctly says E13 is not a degree-specific theorem until its gate is proved, which E14
  does only at N=320.

## 9. Summary table (task 6)

| Item | Accepted? | Condition / dependency remaining |
|---|---|---|
| E13 envelope (1)–(3) | ACCEPT | inherits E08 CEphi; general n>=32 |
| E13 gate (10) | ACCEPT as implication | sign proved only at N=320 (E14-outer320) |
| E14-outer320 gap 13/500, n>=320 | ACCEPT, root adopted | PD-T271 via j*; E08 origin (P3) |
| E15 gap 3/100 (79/2000), n>=192, closed rho>=π/2 | ACCEPT, root adopted | PD-T271; E09 lemma (P1); E08 origin (P3); D32 chart for λ<=S |
| E12-corner256 loss 1/30 | ACCEPT, root adopted | PD-T271 (j, C∞<9/4); E11 model; wide formula n>=32 transfer (m3-2) |
| E08 phase-global conditional all-n/norm consequences | ACCEPT conditional | supplied model inequality |
| E06 consequences | ACCEPT conditional → discharged by E07 | PD-T271 |
| E08/E12 scoped allocation failures | ACCEPT scoped | PD-T271 upper on j unnamed (m3-4) |
| P1, P2, P3, P4 | unwaived | AC disposition required before readiness (§7) |

## 10. Not re-derived (inspection only or not read)

E08 phase-global CEphi itself (ordinary/retained/outer/mesh/log operator bounds, collisions,
six labels); E08-origin ebar proof; C08 full-coefficient model loss; E06/E07 Hmax, j>23/250,
t0, C∞<9/4 and the PD-T271 Arb enclosures; E11 closed half-π model and Ec majorant; D08
squared Peano interpolation and D27 norm adapter; D32/PD-T364 physical chart (λ=S−Δ<=S),
reflection/parity; E04-assembly640 eq. (4) components beyond the domain spot check; E02/E03
retained-row and paired-outer proofs; E09 signed T, E12 signed coupling, E14-wide-signed
(statements only); E14 half-near/annular/assembly320; E01-corner-frontier, E04-wide-corner1,
E08-corner384 proofs; full state/IDEAS.md; the hybrid engine beyond checker.py's guards
(no engine/native run).
