# PD-T?argmax-alln-gated-codex-08 — Adaptive finite projected-defect bound

ID kind: PD-T.
Aliases: direction1 round4 adaptive rectangle; shrinking-strip finite
cancellation; phase-localized defect outside four mesh-scale corner boxes.
Split from: finite projected-defect block PD-T?argmax-alln-gated-codex-05,
removing its fixed compact-angle restriction. Supporting PD-T099 only.
Split into: shrinking-corner reduction is separate gated-codex-09.

## Statement

Use the corrected kernel, physical angles, odd-coset phases, and exact
projected defects Qv,Qh of gated-codex-01. For every integer n>=48,
m=n+1, every physical (theta,phi) in [0,pi]^2 represented as

theta=(J*pi+alpha)/n, phi=(K*pi+beta)/m, J+K odd,

with rho=|alpha|+|beta|<=1/8, the following finite inequalities hold:

\[
 Q_v\ge1/1536\quad\hbox{if}\quad
          \min(\phi,\pi-\phi)\ge4\pi/n,                 \tag{V}
\]
\[
 Q_h\ge1/1536\quad\hbox{if}\quad
          \min(\theta,\pi-\theta)\ge4\pi/n.             \tag{H}
\]

Each bound is uniform in the other coordinate, including its endpoints,
arbitrary moving strip distances, mesh/parity choices and phase signs.
There is no limiting integral or convergence error in (V)–(H).

## Definitions and assumptions

Exact real arithmetic, even-checkerboard Padua convention of PD-T101:
a_j=j*pi/n,b_k=k*pi/m,j+k even, physical weights
w_jk=2e_j f_k/(nm), endpoint factors 1/2. All kernels and defects retain
their finite polynomial values. Write N=nm and
a=(cos alpha+cos beta)/2. The periodicized half kernel has numerator

\[
 A(u,v)=a(1+\cos v)-\tfrac12\sin\alpha\sin u
                              +\tfrac12\sin\beta\sin v.\tag{1}
\]

Its denominator is cos u-cos v and its common sign is immaterial to a
triangle defect. No global maximum or phase-localization hypothesis is
assumed beyond the explicit phase radius in the Statement.

## Status by part

Overall status: **PROVED**, by the complete finite inequalities below;
supplementary independent mathematical review and required Claude audit
pending at initial publication. No numerical experiment is a premise.

| Mathematical part | Status | Evidence / limits |
|---|---|---|
| Both uniform finite projected bounds (V), (H) | PROVED | Positive numerator, collision-free bands and parity-correct counts |

Candidate disposition: retained implementation variant of IDEA-305 /
original Claude-02 / fallback-04 and the existing finite positive block.
No novelty or external-source claim.

## Depends on

Gated-codex-01 for the corrected numerator (1), exact periodicized defect
normalizations and Delta>=Qv,Qh. PD-T101/185 for the finite kernel and
corrected x mode. No phase estimate, asymptotic defect limit, or
unverified literature theorem is used in this result.

## Proof

### Common numerator and finite counting facts

Since 1-cos t<=t^2/2 and rho<=1/8,

\[
 a\ge1-\rho^2/4\ge255/256.
\]

Whenever 1+cos v>=1/2, the numerator in (1) is therefore at least

\[
 a/2-\rho/2\ge255/512-1/16=223/512>3/8.                 \tag{2}
\]

The horizontal numerator is the same expression with the common variable
v and the two first targets theta+-a_j. Thus (2) also applies to it
whenever 1+cos v>=1/2, independently of both phase signs.

A shifted one-dimensional grid of spacing h contains at least ell/h-1
points in any closed interval of length ell. This follows by locating the
first grid point after the interval's lower endpoint. The parity-restricted
periodic first mesh has spacing 2pi/n; the second has spacing 2pi/m.
Our selected intervals lie inside [0,pi], so this infinite-grid count also
counts actual periodic representatives. The physical selected rows are
strictly interior and have endpoint factor 1.

### Exact vertical normalization

For a physical second row k put v+-=phi+-b_k and u_j=j*pi/n+alpha/n.
Let H+-=A(u_j,v+-)/(cos u_j-cos(v+-)), including the common original
polynomial sign, and let d_v=|H+|+|H-|−|H++H-|. Gated-codex-01 gives

\[
 Q_v=\frac1N\sum_{k=0}^{m}f_k
       \sum_{\substack{0\le j<2n\\j+k\equiv J\ (2)}}d_v(u_j,b_k).
                                                               \tag{3}
\]

In particular each selected physical row and each parity-selected
periodic first point contributes d_v/N. The factor follows directly
from G=2 times the signed half kernel, the original 1/4 in Qv, and
endpoint-weighted reflection of the two first-coordinate copies.

Put gamma=min(phi,pi-phi), so 4pi/n<=gamma<=pi/2. If phi=gamma use
b=b'; if phi=pi-gamma use b=pi-b'. In the latter case,

cos(phi+b)=cos(gamma+b'), cos(phi-b)=cos(gamma-b').

Thus in both cases the two denominator targets are exactly cos(gamma+b')
and cos(gamma-b'). A reflected physical b interval has the same length,
spacing and endpoint factors as the original one. We may count with b'
throughout.

### Vertical small-angle case

Suppose 4pi/n<=gamma<=pi/6. Select

\[
 \pi/3\le b'\le\pi/2,\qquad
                 b'-\gamma/2\le u_j\le b'+\gamma/2.     \tag{4}
\]

The folded target angles are b'-gamma and b'+gamma, both in [pi/6,2pi/3].
Their 1+cos values are at least 1/2. The selected u interval lies strictly
between those target angles, with separation at least gamma/2 from each.
Both numerators are >3/8 by (2); the two denominators are nonzero and
opposite in sign. Their total span is

\[
 \cos(b'-\gamma)-\cos(b'+\gamma)
              =2\sin b'\sin\gamma\le2\gamma.
\]

Each half magnitude is therefore at least 3/(16gamma), so

\[
 d_v=2\min(|H+|,|H-|)\ge3/(8\gamma).                    \tag{5}
\]

There are at least m/6-1>=m/12 physical b rows. In each row the selected
periodic interval has length gamma and therefore at least
n*gamma/(2pi)-1>=n*gamma/(4pi) parity-restricted points; the last
inequality uses gamma>=4pi/n. Inserting these counts into (3) gives

\[
 Q_v\ge\frac1{nm}\frac m{12}\frac{n\gamma}{4\pi}
                   \frac3{8\gamma}=\frac1{128\pi}>\frac1{1536}.
                                                               \tag{6}
\]

### Vertical middle-angle case

Suppose pi/6<=gamma<=pi/2. Select

\[
 \pi/12\le b'\le\pi/6,\qquad
                \gamma-b'/2\le u_j\le\gamma+b'/2.       \tag{7}
\]

The target angles gamma+-b' lie in [0,2pi/3]. Hence both numerator
baselines are at least 1/2. The selected interval is strictly inside the
target interval, separated from each endpoint by b'/2. The cosine span
is 2sin gamma sin b'<=1. By (2), each half magnitude is at least 3/8,
and d_v>=3/4. The physical row count is at least m/12-1>=m/24.
The periodic selected interval has length b'>=pi/12, and its
parity-restricted count is at least n/24-1>=n/48 because n>=48.
Thus

\[
 Q_v\ge\frac1{nm}\frac m{24}\frac n{48}\frac34
                         =\frac1{1536}.                 \tag{8}
\]

All boundary cases in (4) and (7) are included: equality at a selected
interval endpoint still leaves positive separation from both pole angles.
At gamma=pi/6 either construction works. Reflected phi values were already
covered by the exact cosine identities, while the sine perturbations
were bounded absolutely in (2). This proves (V).

### Exact horizontal normalization and the two cases

Periodicizing the second mesh instead gives v_r=r*pi/m+beta/m and

\[
 Q_h=\frac1N\sum_{j=0}^{n}e_j
       \sum_{\substack{0\le r<2m\\r+j\equiv K\ (2)}}
                                 d_h(v_r,a_j).           \tag{9}
\]

The common original sign in the two first-coordinate copies is
(-1)^(J+j). Their half numerators are

\[
 A_\pm=a(1+\cos v_r)+\tfrac12\sin\beta\sin v_r
                       -\tfrac12\sin\alpha\sin(\theta\pm a_j),
\]

with denominators cos(theta+-a_j)-cos v_r, up to a common harmless sign.
The identity (9) can also be checked directly: w/4 times a G pair defect
is w/2 times its half defect; summing the two second-coordinate signs
and reflecting their endpoint-half-weight mesh yields exactly e_j/N
times one periodic parity sum. Its parity is r+j=K mod 2, since translating
the second index by K changes the original even board accordingly.

Set gamma=min(theta,pi-theta). Use a_j=a' for theta=gamma and
a_j=pi-a' for theta=pi-gamma. The same reflected
cosine identities give targets cos(gamma+-a'). In the small case select
a' in [pi/3,pi/2], v_r in [a'-gamma/2,a'+gamma/2]. In the middle case
select a' in [pi/12,pi/6], v_r in [gamma-a'/2,gamma+a'/2].
Both selected v intervals lie in [0,7pi/12], hence 1+cos v_r>=1/2.
Consequently A+ and A- are >3/8 by (2). The periodic variable is
strictly between the target angles; the same cosine span and opposite-sign
argument gives d_h>=3/(8gamma) in the small case and d_h>=3/4 in
the middle case. No polynomial collision occurs in the selected sets.

In the small case there are at least n/12 physical rows and at least
m*gamma/(4pi) periodic points per row. The latter uses
gamma>=4pi/n>=4pi/m. Hence Qh>=1/(128pi). In the middle case there
are at least n/24 physical rows and m/48 periodic points per row;
m>=49 suffices for m/24-1>=m/48. Formula (9) therefore gives
Qh>=1/1536. This proves (H), including its reflected-angle case.

## Checks, scope and open items

Finite algebra, sine bounds and exact grid counts only. The adaptive
small-angle factor 1/gamma in the pair defect cancels the selected
periodic interval's gamma width; no limiting Riemann sum is used.
The radius 1/8 is common to all four cases and both orientations.
The other physical coordinate is absent from all estimates, so moving
strips and physical edges are covered uniformly.

This theorem does not localize phases, bound the primitive excess, or
settle any point inside a corner box whose two endpoint distances are
less than 4pi/n. Those obligations are separate. The combined reduction
is stated in gated-codex-09. Independent review and required Claude audit
remain pending; no finite-degree numerical certificate is inferred.

## History

2026-11-02, Codex gpt-6.1-sol xhigh, authorized direction1 round4.
The pre-registered candidate changes the positive rectangle with the
physical angle, extending the fixed-delta finite block. No selected
numerator, reflection, collision or parity-count failure was found in
development. Source/rules snapshot and protocol provenance are recorded
in gated/d1/r04-adaptive-block.md. No new source, shared registry change,
Git operation, future round, or direction-2 work by this worker.
