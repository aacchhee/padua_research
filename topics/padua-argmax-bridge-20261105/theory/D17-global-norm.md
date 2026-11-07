# PD-T?argmax-bridge-codex-D17-norm — Global model norm with true constant8/3

ID kind: PD-T. Aliases: D09 norm with D10 constant; global signed-family
majorant. Split from: D17 actual-corner application. Split into: none.

## Statement and definitions

For every integer n>=32, put m=n+1,L=log n and let U_F(n) be EXACTLY
D05-outer-comparison(2) at R2,delta pi/8, with conservative inputs
a=p=d=1,P=2,|U0|=8,H_n<=1+L. Keep ALL positive mesh/row/collision/
interior/strip/pole terms. Define

    M(n)=[4L^2+(79/5)L]/pi^2+8/3+U_F(n).            (1)

For the corrected common primitive S_n and physical Padua Lebesgue
function lambda_n, S_n<M(n) on ALL real phases and lambda_n<M(n)
on the physical square. The non-strict upper M(n) also bounds every
complete signed board polynomial and every complete signed cardinal
polynomial with coefficient magnitudes<=1. After the actual-corner
substitutions(-cos(alpha/n),-cos(beta/m)), the signed-cardinal bound
is GLOBAL for all real alpha,beta.

Status: **PROVED**, analytic developer quantitative application;
distinct mathematical review pending. No scalar evaluation is needed
for the all-n statement. All corrected endpoint/collision/exceptional
highest-x-mode conventions are those of PD-T101/PD-T364 and D09.

## Dependencies and proof

The accepted D09-global-norm proof gives the exact finite period
lattice/evenness adapter and the coefficient inequality

    4a/pi^2<=4/pi^2,
    b_full<=b_c+3/pi^2<(79/5)/pi^2.

For clarity, k_shift=gamma+log(8/pi)<8/5 because the accepted elementary
gamma<3/5 and pi>3,e>8/3 imply log(8/pi)<1; b_c=8k_shift/pi^2.
Thus b_c+3/pi^2<(64/5+3)/pi^2=(79/5)/pi^2. D10-global-constant
independently proves C_infty<8/3 on the full closed phase diamond.
D05's full error is valid for every n>=32. Since L>=0, on that diamond

    S_n<=M_infty+U_F<M(n).

To ensure GLOBAL means the full real domain required by D08, recall the
accepted exact finite reindexing: translations by pi(p,q),p+q even,
preserve S_n, as do separate sign reflections. Reducing
(alpha+beta)/(2pi) and(alpha-beta)/(2pi) into[-1/2,1/2] maps any real
pair to |alpha'|+|beta'|<=pi. The same S_n value therefore lies on the
closed diamond. No n,m coordinate exchange or asymptotic limit is made.

Every signed board polynomial is dominated pointwise by S_n. PD-T364
provides a complete physical odd-center cover and lambda=S_n-Delta,
Delta>=0, so lambda<=S_n<M. Every signed cardinal polynomial is
dominated by lambda. Its actual-corner substitution stays in the square
for ALL real phases, giving the final global signed-family norm.

This is the accepted D09 argument with its former123/40 constant
replaced by the independently accepted sharper8/3, not a new norming
principle. D14's finite sampling theorem is not used without actual
sample data; no4096 samples are assumed or evaluated.

## Scope and history

This supplies a global NORM, not the value or location of an unknown
maximizer. No global argmax, degree certificate, point/kernel computation,
runtime or model-dependency removal follows. The actual-corner application
is separate. 2026-11-06, parent-requested Codex Sol xhigh; serving metadata
unexposed. Input/rules d85007b (full SHA in the canonical D17 attempt).


### Supplementary review closure — 2026-11-06

Distinct independent reconstruction ACCEPTED this unchanged developer
scope; [independent-checks-D17-analytic-corner.md](../independent-checks-D17-analytic-corner.md),
report SHA25628dbf04a53286706475e5264dec2676ea7a9d09c298e691a5157bc10f5c94c2b.
Native replay versus directed scalar scope, CPU samples, provenance and
trusted dependencies are distinguished in the report. The earlier pending
wording is historical. Final Claude audit remains separate.
