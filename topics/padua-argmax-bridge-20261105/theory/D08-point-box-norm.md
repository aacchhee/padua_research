# PD-T?argmax-bridge-codex-D08-norm — Exact odd-grid square mean and a global primitive bound

ID kind: PD-T. Aliases: corrected odd-grid Parseval; parity-alias exclusion;
independent global phase norm. Split from: D08 point-to-box norm input.
Split into: interpolation contracts are in D08-point-box.md.

## Statement

For every integer n>=2, put m=n+1, N=nm, h_0=1,h_a=2 for a>0, and

    D_n(u,v)=sum_(a+b<=n) h_a*h_b*cos(au)*cos(bv),
    G_n(u,v)=D_n(u,v)-cos(nu),
    Gamma^-={(j,r):0<=j<2n,0<=r<2m,j+r odd},
    u_j=(j*pi+alpha)/n, v_r=(r*pi+beta)/m,
    S_n(alpha,beta)=(1/(2N))*sum_Gamma^- |G_n(u_j,v_r)|.

The exceptional coefficient (n,0) in G_n is one. For ALL real phases,

    (1/(2N))*sum_Gamma^- G_n(u_j,v_r)^2
                      =2N-sin^2(alpha),                         (1)
    S_n(alpha,beta)<=sqrt(2N-sin^2(alpha))<=sqrt(2N).             (2)

The actual corrected Padua Lebesgue function consequently satisfies

    lambda_n(x,y)<=sqrt(2N),   (x,y) in [-1,1]^2.                (3)

Thus sqrt(2N) is an independent GLOBAL norm input for both D08 box
contracts. No location/value of a maximizer or numerical sample is used.

Status: **PROVED**, analytic developer result; distinct review pending.
The bound is coarse and supplies no practical cover or argmax onset.

## Proof

Write A_full for the average over all 4N shifted tensor-grid points.
For any trigonometric polynomial f,

    (1/(2N))*sum_Gamma^- f
       =A_full f-A_full[(-1)^(j+r)*f].                          (4)

The Fourier support of G_n lies in |k_x|+|k_y|<=n, so that of G_n^2
lies in |k_x|+|k_y|<=2n. The twisted tensor average in (4) can retain
only modes

    k_x=n mod 2n,  k_y=m mod 2m.

Every such mode has |k_x|+|k_y|>=n+m=2n+1. Hence none is present,
and the twisted average of G_n^2 is zero. This uses the odd parity
filter exactly; discarding a possible alias merely by inspection of
the separate frequency bounds would be insufficient.

It remains to compute A_full G_n^2. On the second mesh the cosine
modes 0<=b<=n<m have the exact discrete inner products

    average_r cos(bv_r)cos(b'v_r)=0 if b!=b',
                                    1 if b=b'=0,
                                  1/2 if b=b'>0.

These follow by product-to-sum and the finite geometric series; all
nonzero frequencies have magnitude below 2m. On the first mesh the
same relations hold for 0<=a,a'<n. Cross products with a=n vanish
unless a'=n, while

    cos(nu_j)=(-1)^j*cos alpha,
    average_j cos(nu_j)^2=cos^2 alpha.                         (5)

The only total-degree mode with a=n is (n,0). Every other mode
coefficient h_a*h_b contributes h_a*h_b to the square mean, because
h_a^2 times its ordinary cosine norm is h_a, and likewise for b.
The finite weighted triangular count is

    sum_(a+b<=n) h_a*h_b
       =1+4n+4*n*(n-1)/2=2N+1.

Remove this count's exceptional contribution h_n*h_0=2, and insert
the actual corrected coefficient-one contribution cos^2 alpha from
(5). Thus

    A_full G_n^2=(2N+1)-2+cos^2 alpha=2N-sin^2 alpha.

Together with the zero twisted average, this proves (1). There are
exactly 2N odd-grid points, so Cauchy-Schwarz applied to their normalized
average gives S_n^2<=the left side of (1), proving (2).

The accepted exact reflection identity PD-T364 gives lambda<=S_n in
every physical odd-center phase chart, with finite polynomial collision
values and the endpoint multiplicities already included. Those charts
cover the square. Applying (2) in any such chart proves (3). In fact
no bounded chart is needed for this use: (2) holds for every real phase.
The same result follows directly by the identical parity-average
calculation on the even reflected board before the triangle inequality.

## Globalizing a separately proved model upper

The following elementary adapter is useful if a sharper bound is later
supplied. Direct reindexing of the finite odd-board sum gives periods

    (alpha,beta)->(alpha+2pi,beta),
    (alpha,beta)->(alpha+pi,beta+pi).

Separate reflection of j or r also proves separate evenness of S_n.
The period lattice contains (pi,pi) and (pi,-pi). Write
s=(alpha+beta)/(2pi), t=(alpha-beta)/(2pi), and reduce s,t modulo
integers into [-1/2,1/2]. The resulting congruent phases obey

    |alpha|+|beta|=2pi*max(|s|,|t|)<=pi.

Thus a proved upper on the entire closed diamond is GLOBAL; by evenness
it suffices on alpha,beta>=0, alpha+beta<=pi. In particular a rigorously
bounded accepted D05 model plus its complete error may supply a smaller
M_S. This file does not assert such a model supremum or its useful size.
The explicit independent bound (2) needs none of that later work.

## Verification, scope and provenance

Analytic finite Fourier algebra only. No numerical/code/native job,
board, quadrature or independent execution ran. The normalization 1/(2N),
odd parity and exceptional coefficient one are essential to (1).
No point maximum, unknown argmax or fitted profile supplies M.

Rules/input `d4956aea3bda9d5ff9917a5b410778fc7adf4fb7`, 2026-11-06.
Parent-assigned ordinary Sol xhigh analytical cap; serving metadata
unexposed. Fresh gate and alternatives are in the owned D08 idea/attempt.
Root owns Git/shared records. Distinct review is required; no old source
or proof is changed.


### Supplementary review closure — 2026-11-06

Distinct Astra xhigh reconstruction ACCEPTED the preceding unchanged
developer text, with no unresolved finding. See
[independent-checks-D09-point-box.md](../independent-checks-D09-point-box.md),
report SHA256486f58f8a7d460134922c26c02889e1eca69f482359ed66d7618b34d8b43535a.
This closes the pending supplementary mathematical review only; successful
point premises, source adoption, complete covers and final Claude audit
remain separate obligations. No numerical instance ran for this proof.
