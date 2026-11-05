# PD-T?nn-mop-stability-codex-D4-04 — finite common Toda closure

ID kind: PD-T (provisional allocation).
Aliases: finite NN exponential flow; common-time multidimensional Toda.
Split from: D4-C3, exact supporting invariant of an OPEN numerical-continuation target.
Split into: none.

## Statement

For two weights on fixed N distinct nodes let w_(s,l)(t)=exp(t x_l)w_(s,l)(0). On any open interval on which every mixed moment matrix through total degree N is nonsingular, the finite NN triangle satisfies

    adot_(nu,j)=a_(nu,j)(b_(nu,j)-b_(nu-e_j,j)),  nu_j>0;
    bdot_(nu,j)=S_(nu+e_j)-S_nu,   S_nu=sum_s a_(nu,s).

Absent a and its derivative are zero. Set S_eta=0 at |eta|=N; no degree-N b values are needed. The exact ODE started at a compatible array equals the moment-defined trajectory until it leaves this normality interval. Each right-hand side evaluation costs O(N^2).

## Definitions

NN convention and stored indices are D4-01. P_eta=F is independent of t for |eta|=N. The source literature commonly uses exp(-t x); the sign here is reversed.

## Assumptions

N>=1, finite fixed support, differentiable exponential weights; mixed normality throughout the stated interval. Positivity alone does not provide this interval (D4-02). The initial NN array is given.

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Finite normality-interval ODE and terminal closure | PROVED | Differentiated orthogonality below |

Candidate / claim disposition: exact algebra retained; no numerical stability disposition inferred.

## Depends on

PD-T286 normal-triangle NN and h-ratio characterization. Elementary uniqueness for polynomial ODEs. Known infinite-domain Toda context LIT-D4-01 is not needed in the proof.

## Proof or evidence

Differentiate the orthogonality equations, using Ldot_s(f)=L_s(xf). For nu of degree k<N, Pdot_nu has degree at most k-1 and satisfies all lower row constraints of the predecessor space. Its expansion in the predecessor polynomials is

    Pdot_nu=-sum_s a_(nu,s) P_(nu-e_s).

Indeed all non-top constraints vanish. At the top row for j, differentiating L_j(x^(nu_j-1)P_nu)=0 gives L_j(x^(nu_j-1)Pdot_nu)=-h_(nu,j). Every predecessor s!=j is orthogonal to this row, and the j predecessor gives h_(nu-e_j,j), so its coefficient is -a_(nu,j). The predecessor polynomials span this space by normality (the same finite-moment basis argument as PD-T286). At degree N, P=F, Pdot=0 and every h_(eta,j)=0; thus a_(eta,j)=0 is the consistent closure, as its denominator h_(eta-e_j,j) is nonzero.

Differentiate h_(nu,j)=L_j(x^nu_j P_nu). Substitute the polynomial derivative. In the remaining term L_j(x^nu_j xP_nu), use successor direction j in the NN recurrence. The successor integrates to zero; the predecessor contributions cancel those from Pdot. Hence hdot_(nu,j)=b_(nu,j)h_(nu,j). Differentiate the h ratio a=h_nu/h_prev to get the a equation.

Let gamma_nu be the subleading coefficient, gamma_0=0. The polynomial derivative gives gammadot_nu=-S_nu, including gamma_degreeN constant and S_degreeN=0. Differentiating b_(nu,j)=gamma_nu-gamma_(nu+e_j) gives the b equation, including the last stored layer. Finite normality makes the moment coefficients differentiable. The displayed vector field is polynomial in the stored coefficients, so local uniqueness identifies its solution with those moment coefficients on the normality interval. There are O(N^2) stored values.

## Checks

`code/integrable_transport.py --mode toda --sizes 4 8 12 16 --dps 220`: rounded-reference initial arrays, exp(0.1x) endpoint, RK4 with 20 and 40 steps. Endpoints and limitations are recorded in `attempts/D4.md`. This is a finite implementation check, not a theorem about RK4 invariants. All initial arrays came from high-precision C4; no IEP solve is supplied by this initialization.

## Sources

LIT-D4-01 §2.3 equation (2.18), common continuous-time Toda equations with opposite time sign. Only that local section's actual reading is claimed; the source's full determinant/Lax proofs were not read. This finite-domain proof is local and independent; no novelty of Toda claimed.

## Scope

Known exact common flow with explicit finite support closure and O(N^2) implementation. Ordinary floating RK4 does not exactly preserve compatibility or moment realizability. The proof provides neither a normality certificate nor a global interval, error bound, or stable starting-data construction. Common flow is constrained by D4-03.

## Open items

Error control on the compatible manifold, a useful source state available from the target input, independent-weight generators, and monitored continuation avoiding nonnormality. Their presence as open items does not lower the status of this exact local identity.

## History

2026-11-05, Codex dispatched gpt-6.1-sol xhigh; source 823cf6a4, round 1. Exact supporting claim split off from the unresolved stable solver.
