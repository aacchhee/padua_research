# PD-T224 (PD-T?argmax-alln-gated-codex-10) — Finite defect at every noncorner odd coset

Final registration: **PD-T224**, 2026-11-03. The provisional identifier in the title remains an alias; mathematical statement and historical evidence are unchanged.

ID kind: PD-T.
Aliases: direction1 round5 middle lattice lines; first-four-cell defect;
noncorner odd-coset exclusion; discrete thin-strip cancellation.
Split from: supporting corner-cell defect obligation for PD-T099 after
gated-codex-08/09. Split into: corner-phase localization is separate
gated-codex-11. The all-degree target remains OPEN.

## Statement

Use the corrected kernel, total triangle defect Delta and exact projected
defects Qv,Qh of gated-codex-01. Let n>=48, m=n+1. Suppose a physical
angle point has a physical odd-coset representation

\[
 \theta=(J\pi+\alpha)/n,\quad \phi=(K\pi+\beta)/m,
 \quad 0\le J\le n,\quad0\le K\le m,\quad J+K\text{ odd},
\]

with rho=|alpha|+|beta|<=1/64. If (J,K) is not a physical nonnode corner,
that is, not a pair of endpoint indices with odd sum, then

\[
                         \Delta_n(\theta,\phi)\ge1/4096. \tag{1}
\]

This bound is finite and uniform in n, center, both phase signs and both
physical coordinates. It includes the first four interior center indices
from every edge endpoint. No limiting integral or numerical sample is a
premise.

## Definitions and assumptions

Exact real arithmetic and the even-checkerboard Padua convention of
PD-T101/185. Physical angles are in [0,pi]^2. With N=nm, the vertical
projection is 1/N times its physical second-row / periodic first-index
point defect sum, with parity j'+k=J mod 2 and second endpoint factor f_k.
The horizontal projection is 1/N times its physical first-row / periodic
second-index sum, with parity k'+j=K mod 2 and first endpoint factor e_j.
These are the exact identities from gated-codex-01/08.

The signed half kernel has numerator

\[
 A(u,v)=a(1+\cos v)-\tfrac12\sin\alpha\sin u
                         +\tfrac12\sin\beta\sin v,
 \quad a=(\cos\alpha+\cos\beta)/2,
\]

and denominator cos u-cos v, up to a common sign in a paired defect.
The polynomial defines all collisions, although none of the selected
terms below is a collision.

## Status by part

Overall status: **PROVED**, by the finite construction below;
supplementary independent mathematical review is complete; Claude audit-01 ACCEPTED the mathematics at its stated scope (record fixes pending).

| Mathematical part | Status | Evidence / limits |
|---|---|---|
| Uniform defect bound (1) | PROVED | Adaptive far-angle block and all four thin lattice-line cases |

Candidate disposition: retained implementation variant of IDEA-305 /
original Claude-02 / fallback-04 and the preceding finite geometry route.
The failed preliminary horizontal q=+1 choice is retained in History.
No historical novelty claim or external source transfer.

## Depends on

Gated-codex-01 for the exact numerator, Delta>=Qv,Qh and projection
normalizations; gated-codex-08 for the adaptive block at physical endpoint
distance >=4pi/n, n>=48 and rho<=1/8. This result uses no primitive
phase bound or local gain estimate.

## Proof

### Uniform numerator and span bounds

Throughout rho<=1/64. In particular a>=255/256 and the two sine
perturbations of a numerator have combined magnitude <=rho/2<=1/128.
If its baseline 1+cos v is at least 1/16, then

\[
 A\ge\frac{255}{4096}-\frac1{128}
       =\frac{223}{4096}>\frac1{32}.                    \tag{2}
\]

We select folded angles in [pi/8,3pi/4]. On that interval both 1-cos w
and 1+cos w are >1/16. Indeed cos(pi/8)<15/16, since
cos^2(pi/8)=(2+sqrt(2))/4<7/8<(15/16)^2; and
1+cos(3pi/4)=1-sqrt(2)/2>1/4. These elementary bounds will be applied
to the actual numerator, including the horizontal fixed numerator.

For an integer endpoint-distance index s in {1,2,3,4}, put
t=(s*pi+-beta)/m in a vertical case, or
t=(s*pi+-alpha)/n in a horizontal case. These numbers are positive.
The cosine span of two folded targets separated by 2t is at most 2t,
and hence

\[
 \text{vertical span}<26/m,\qquad
 \text{horizontal span}<26/n,                           \tag{3}
\]

because 2t<=(8pi+1/32)/m or the corresponding expression over n,
and 8pi+1/32<26. Once a selected angle lies strictly between the targets,
the two half denominators are nonzero and opposite in sign. By (2)–(3),
the paired point defect is at least m/416 vertically or n/416
horizontally: each half has magnitude at least m/832 or n/832, and
the defect is twice their minimum.

### Vertical top and bottom: exact bands and parity

Let l run through all integers n/4<=l<=n/2. There are at least
n/4-1>=n/8 such integers. The selected physical second index is
k=l+q, where q is specified below. Thus 1<=k<=m-1 for n>=48;
every selected row has weight factor f_k=1 and distinct l give distinct
physical rows. The periodic first indices j' are physical-range
interior representatives as well and therefore valid periodic indices.

For the top case K=m-s, s in {1,2,3,4}, set

\[
 t=(s\pi-\beta)/m,\quad \phi=\pi-t,\quad
 j'=n-l,\quad u=\pi-w,\quad w=(l\pi-\alpha)/n,
\]

and take q=1 if s is odd, q=0 if s is even. For the bottom case K=s,
put

\[
 t=(s\pi+\beta)/m,\quad \phi=t,\quad
 j'=l,\quad u=w=(l\pi+\alpha)/n,
\]

and take q=0 if s is odd, q=1 if s is even. In either case
b=k*pi/m and its folded targets are b-t and b+t. More precisely,
the top cosine targets are -cos(b-t),-cos(b+t) and cos u=-cos w;
the bottom targets are cos(b-t),cos(b+t) and cos u=cos w.

The exact normalized displacement m(w-b) is

| Case | q | m(w-b) |
|---|---:|---|
| Top, s odd | 1 | l*pi/n-pi-(m/n)alpha |
| Top, s even | 0 | l*pi/n-(m/n)alpha |
| Bottom, s odd | 0 | l*pi/n+(m/n)alpha |
| Bottom, s even | 1 | l*pi/n-pi+(m/n)alpha |

Its base absolute value is at most 3pi/4 in the first/fourth rows,
and pi/2 in the second/third. The needed strict band inequality is
|m(w-b)|<s*pi-beta at the top, or <s*pi+beta at the bottom.
For the odd-index rows the right-hand integer s is at least 1 and
the base displacement is <=3pi/4 or pi/2. For the even-index rows
s>=2. In all four cases the perturbation, after moving the beta term
to the left, is bounded by

\[
 (m/n)|\alpha|+|\beta|\le(49/48)\rho\le49/3072<\pi/4.
\]

Thus w lies strictly inside (b-t,b+t). The target angles themselves
lie in [pi/8,3pi/4], since

\[
 b-t\ge\frac{(n/4-4)\pi-1/64}{m}\ge\pi/8,
 \quad b+t\le\frac{(n/2+5)\pi+1/64}{m}\le3\pi/4
\]

for n>=48. Consequently the vertical top numerators have baseline
1-cos(b+-t)>1/16; the bottom numerators have baseline
1+cos(b+-t)>1/16. This proves (2) for both halves and excludes every
selected polynomial collision.

For the top parity, j'+k=n+q, whereas odd J+K with K=m-s gives
J=n+s mod 2. The chosen q=s mod 2 makes j'+k=J mod 2.
For the bottom, j'+k=2l+q=q mod 2, and odd J+s gives J=1-s mod 2;
the chosen q=1-s mod 2 is therefore correct. Inserting one selected
point for each of at least n/8 physical rows into the exact Qv sum gives

\[
 Q_v\ge\frac1{nm}\frac n8\frac m{416}=\frac1{3328}.     \tag{4}
\]

### Horizontal top and bottom: reversed meshes and fixed numerator

Let l run through integers m/4<=l<=m/2. There are at least
m/4-1>=m/8. The physical first index is j=l+q with q in {-1,0};
for n>=48 it obeys 1<=j<=n-1, so e_j=1. Distinct l again give
distinct physical rows.

For J=n-s, s in {1,2,3,4}, set

\[
 t=(s\pi-\alpha)/n,\quad\theta=\pi-t,\quad
 k'=m-l,\quad v=\pi-w,\quad w=(l\pi-\beta)/m,
\]

and use q=-1 if s is odd, q=0 if s is even. For J=s put

\[
 t=(s\pi+\alpha)/n,\quad\theta=t,\quad
 k'=l,\quad v=w=(l\pi+\beta)/m,
\]

and use q=0 if s is odd, q=-1 if s is even. Both k' choices are
interior representatives in the periodic second mesh. Write a_j=j*pi/n
for the physical first row. The exact displacements are

| Case | q | n(w-a_j) |
|---|---:|---|
| Top, s odd | -1 | pi-l*pi/m-(n/m)beta |
| Top, s even | 0 | -l*pi/m-(n/m)beta |
| Bottom, s odd | 0 | -l*pi/m+(n/m)beta |
| Bottom, s even | -1 | pi-l*pi/m+(n/m)beta |

The base magnitudes are <=3pi/4 in the first/fourth rows and <=pi/2
in the second/third. After including the alpha term, the perturbation
is at most |alpha|+(n/m)|beta|<=rho<pi/4. Exactly as above, these
bounds prove |w-a_j|<t in every case. The folded target angles
a_j+-t are in [pi/8,3pi/4], because

\[
 a_j-t\ge\frac{((n-19)/4)\pi-1/64}{n}\ge\pi/8,
 \quad a_j+t\le\frac{((n+9)/2)\pi+1/64}{n}\le3\pi/4.
\]

The horizontal half numerators are

\[
 a(1+B)+\tfrac12\sin\beta\sin v
                  -\tfrac12\sin\alpha\sin(\theta\pm a_j),
 \qquad B=\cos v.
\]

Here it is the fixed periodic v, not a target angle, which determines
the baseline. Its w belongs to
[pi/4-1/(64m),pi/2+1/(64m)] subset [pi/8,3pi/4]. Thus 1+B is
1-cos w at the top or 1+cos w at the bottom, both >1/16.
Equation (2) applies without interchanging the corrected mode or
importing the vertical numerator. The band inequalities imply opposite
regular denominators. The span bound (3) therefore gives point defect
at least n/416.

For the top parity, k'+j=m+q, while odd J+K with J=n-s gives
K=m+s mod 2. Both q=-1 for odd s and q=0 for even s satisfy
q=s mod 2. For the bottom, k'+j=2l+q=q mod 2 and odd s+K gives
K=1-s mod 2; the stated q is correct. Hence every point belongs to
the exact horizontal parity sum. The resulting bound is

\[
 Q_h\ge\frac1{nm}\frac m8\frac n{416}=\frac1{3328}.     \tag{5}
\]

### Exhaust all noncorner centers

If 1<=K<=m-1, put s=min(K,m-K). For s<=4, (4) applies in its
top or bottom form. For s>=5 the physical endpoint distance satisfies

\[
 \min(\phi,\pi-\phi)\ge(5\pi-1/64)/m>4\pi/n
\]

for n>=48. Gated-codex-08 then gives Qv>=1/1536. If instead K is
an endpoint, the excluded-corner hypothesis requires 1<=J<=n-1.
Put s=min(J,n-J). For s<=4 use (5); for s>=5 the first-angle
endpoint distance is at least (5pi-1/64)/n>4pi/n, and use the
horizontal part of gated-codex-08. These cases exhaust every physical
odd center other than a nonnode corner. In each case

Delta>=Qv or Qh>=min(1/3328,1/1536)>1/4096,

which proves (1).

## Checks, scope and open items

The finite construction verifies both phase signs, all four endpoint
orientations, both parities, physical index ranges, row weights and
periodic normalizations. The large-degree near-maximizer consequence
needs separate global and local primitive estimates; it is recorded in
gated-codex-11. This theorem gives no defect at an actual nonnode corner
center and no comparison inside that center's small phase diamond.

## Sources, checks and history

Codex, assigned gpt-6.1-sol xhigh, 2026-11-02; runtime metadata not
independently exposed. Rules/snapshot
`2dde541f1e5af239cae6e93e4438b9be89d15d87`, scientific base
`7d308b10d946b607ae0690454f6c0103690775a4`. The full registry/
obstruction gate and shortlist from round 1 remain applicable. This is
the pre-registered round-5 middle-lattice-line candidate, not a literature
transfer. No numerical phase/degree scan or Git operation is a premise.
Supplementary independent review is complete; Claude audit-01 ACCEPTED the mathematics at its stated scope (record fixes pending).

Retained failed preliminary choice: horizontal top, odd s, q=+1.
At alpha=beta=0 and s=1 it gives n(w-a_j)=-l*pi/m-pi, whose
magnitude is at least 5pi/4>pi, so the required first-cell band fails.
The corrected q=-1 choice is used throughout the proof. This refutes
only that selected line as a proof construction, not the defect target
or other lattice-line choices. No new global negative ID is assigned.


### Documentation correction — 2026-11-02

F3: publication-time review labels are updated; the original proof and claim scopes are unchanged.

Current review scope (F3): [Claude audit-01](../audit-01.md) ACCEPTED the mathematics exactly as stated; its record/protocol findings and the protocol check of this response remain pending. Supplementary independent checks are complete and do not replace that Claude audit. No proof status, statement, checker predicate or certificate changes. Earlier publication-time review wording is preserved here as history:

> Supplementary independent review and required Claude audit are pending

Original additional status wording: “supplementary independent mathematical review and required Claude audit pending at initial publication”.
