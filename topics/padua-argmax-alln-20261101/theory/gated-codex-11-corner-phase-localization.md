# PD-T?argmax-alln-gated-codex-11 — Maximizers approach the actual nonnode corner phases

ID kind: PD-T.
Aliases: direction1 round5 actual-corner localization; nonnode-corner
phase confinement; scaled distance of every global maximizer tends to zero.
Split from: supporting localization obligation for PD-T099 after
gated-codex-09. Split into: none. Exact corner dominance remains OPEN.

## Statement

Let M_n be the nonempty set of global maximizers of the even-checkerboard
Padua Lebesgue function in the physical angle square. Let

\[
 C_n=\{(J\pi/n,K\pi/(n+1)):
       J\in\{0,n\},K\in\{0,n+1\},J+K\text{ odd}\}
\]

be its two physical nonnode corners. With m=n+1,

\[
 \sup_{(\theta,\phi)\in M_n}\ 
 \min_{(\theta_c,\phi_c)\in C_n}
     \{n|\theta-\theta_c|+m|\phi-\phi_c|\}
                           \longrightarrow0.            \tag{1}
\]

Equivalently, for every epsilon>0 there exists an integer N_epsilon
such that every n>=N_epsilon and every global maximizer has an
actual nonnode-corner representation with |alpha|+|beta|<epsilon.
The thresholds are **non-effective in this record**. Neither equality
with the corner nor any finite certification through those thresholds
is asserted. PD-T099 remains OPEN.

## Definitions, assumptions and status

Exact real arithmetic, corrected polynomial kernel and positive physical
weights of PD-T101/185. Lambda_c(n) is attained at the two corners C_n
and supplies a lower bound on the global maximum; its global optimality
is not assumed. Continuity of the finite absolute-polynomial sum on the
compact square ensures M_n is nonempty.

Overall status: **PROVED**, by the uniform phase argument below with
explicitly cited proved dependencies; supplementary independent review
and required Claude audit pending at publication.

| Mathematical part | Status | Evidence / limits |
|---|---|---|
| Uniform scaled localization (1) | PROVED | Global phase entry, local primitive gain and finite noncorner-coset defect |

Candidate disposition: retained assembly variant of IDEA-305 / original
Claude-02 / fallback-04. No novelty or external-source claim.

## Depends on

- Gated-codex-01: exact lambda=S-Delta, Delta>=0 and reflected primitive.
- Gated-codex-02: global S<=a*Lambda_c+C*log(n+1) on the full phase diamond.
- Gated-codex-03: uniform local primitive excess tends to zero.
- Gated-codex-10: Delta>=1/4096 at every physical odd center except an
  actual nonnode corner, for n>=48 and rho<=1/64.
- PD-T159: Lambda_c>=(4/pi^2)log^2 n-54.

The physical odd-coset cover and same-primitive argument below were also
proved in gated-codex-04/09. No explicit but enormous local constants
are needed for this qualitative statement.

## Proof

Every physical angle point has a physical odd-coset representation with
|alpha|+|beta|<=pi. Choose a mesh rectangle containing it, using the
adjacent rectangle at a boundary. The normalized L1 distances to the
two odd vertices sum to 2, so one is <=1; multiplying by pi gives the
diamond. Endpoint-weighted reflection and translation by that odd
vertex identify its majorant with precisely the periodic primitive of
the two phase theorems, retaining the corrected mode.

For any global maximizer z, lambda_n(z)>=Lambda_c(n). Its selected
physical odd representation therefore obeys

\[
 (1-a)\Lambda_c(n)\le C\log(n+1),\quad
 1-a\ge(\alpha^2+\beta^2)/\pi^2.
\]

The explicit quadratic corner growth shows that alpha and beta tend
uniformly to zero over all global maximizers and all these selected
representations. In particular, for every sufficiently large n they
obey rho<=1/64 and lie in the fixed local neighborhood of the local
gain theorem. That theorem gives S_n(z)<=Lambda_c(n)+epsilon_n,
where epsilon_n tends to zero uniformly over these maximizing points.

Suppose some selected center is not an actual nonnode corner. For
sufficiently large n the finite defect theorem gives Delta_n(z)>=1/4096,
and hence

\[
 \lambda_n(z)=S_n(z)-\Delta_n(z)
              \le\Lambda_c(n)+\epsilon_n-1/4096
              <\Lambda_c(n),
\]

contradicting maximality. Thus for every sufficiently large n every
selected center of a maximizer is an actual nonnode corner. At such
an endpoint center,

rho=|alpha|+|beta|=n|theta-theta_c|+m|phi-phi_c|.

The already established uniform convergence rho->0 proves (1), and
its quantified epsilon formulation follows directly. No choice of a
unique maximizing branch, stationary point, smooth absolute value or
continuous nearest-center map was required.

## Scope and remaining obligation

This eliminates all noncorner physical odd cosets as large-degree
global-maximizer centers, including the first four interior cells in
both orientations. It strengthens the four shrinking 4pi/n boxes to
vanishing phase neighborhoods of the two actual nonnode corners.

A maximizer with small nonzero phase is still allowed. To prove PD-T099
one still needs a uniform local corner comparison, equality
classification, an effective threshold where required and the matching
finite-degree coverage. The endpoint cusp of the primitive cannot be
discarded, although it does not appear as a conclusion about the actual
Lebesgue function here. No such corner comparison or later direction is
developed in this theorem.

## Sources, checks and history

Codex, assigned gpt-6.1-sol xhigh, 2026-11-02; runtime metadata not
independently exposed. Rules/snapshot
`2dde541f1e5af239cae6e93e4438b9be89d15d87`, scientific base
`7d308b10d946b607ae0690454f6c0103690775a4`. This is the authorized
round-5 assembly of the finite lattice-line result, retaining the full
round-1 candidate/obstruction gate. No numerical phase/degree scan,
external literature transfer, Git action, shared registry update,
future round or direction-2 work was performed by this worker.
Supplementary independent review and required Claude audit remain
pending at initial publication.
