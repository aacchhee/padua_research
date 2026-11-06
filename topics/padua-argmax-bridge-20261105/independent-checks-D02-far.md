# Supplementary independent check — D02 far completion

Rules/input: `084a64f6465956f9c75b5538f83752c30318f151`; rules unchanged
from this worker's D01 review at `e6549177fe48c7fea8436cece8a04b411dc544e1`.
Reviewer: distinct Codex subagent `/root/d01_far_review`, continuing the
parent-requested Astra xhigh allocation; actual serving metadata unexposed.
This supplements the still-pending formal Claude audit.

## Scope and prospective computation

Review only the three D02 far support proofs, their exact full-diamond
quantifiers, and the separate OPEN practical target. No author proof,
shared record or Git operation belongs to this worker.

Before execution, authorize at most 20 process CPU-seconds for one
independently written scalar script: replay the published recombination
from hash-pinned D01 inputs; check the boundary digamma telescoping at
R=2 and 64 and the exact gamma/series bias agreement; compare the inherited
one-dimensional boundary cotangent formula with the claimed finite-n
profile on four specified small controls, including both parities and a
near-vertex phase. No native binary, full board, new interior quadrature,
phase cover, fitted rate or computer-proof claim. Mathematical review
does not depend on the measurements. Findings and final coverage follow.

## Verdict and frozen inputs

**ACCEPTED at the written support scope; no unresolved finding.** The
three analytic proofs establish the exact constant/bias, uniform limit
and parameter-dependent finite-n bound, and full boundary identity.
The practical interior O((1+log n)/n) contract remains **OPEN**. This is
neither formal Claude approval nor an additional degree certificate.
No developer edit was requested or made in this review.

All four frozen proof hashes were checked again after the scalar run:

| File in `theory/` | SHA-256 | Disposition |
| --- | --- | --- |
| [D02-far-bias-identity.md](theory/D02-far-bias-identity.md) | `724d554970719fa9659323a0bf50856b50f9c51b838c6dd062994a5dda6488b9` | Accept PROVED scope |
| [D02-far-uniform-limit.md](theory/D02-far-uniform-limit.md) | `7432e666353f54eb08a312ba1b5636c164545827049caa22ab67b46ab6386ef7` | Accept PROVED scope |
| [D02-far-boundary-identity.md](theory/D02-far-boundary-identity.md) | `913b85f2014a20f0d2ac8d80de8d80d2fe1fe2fb4cf35831d0e241a75838eae0` | Accept PROVED scope |
| [D02-far-joint-target.md](theory/D02-far-joint-target.md) | `34b36014aaba155a1f1349b572065142e825183ac79f50caaabac730522f1708` | Correctly OPEN |

The complete [idea](ideas/D02-far-joint.md), hash
`e8fcb923c6a7fef7589dfbbf6ecda4144e1c022fd68a414e459992a7cf085e38`,
and [attempt](attempts/D02-far-joint.md), hash
`d37a357a28d70a72eb1c8146185541011f853b197201a54e2fcbc4b60cae8df0`,
were also read. During review the orchestrator advanced HEAD to
`f1ba23cfbfb557dd491730f9837f5efe413e7c75`; the rules and registry diff
from the recorded D02 input was empty. No mutable Git operation was run.

## Mathematical reconstruction

1. **Finite part, sign and uniform phase limits.** Expanding
   `B0 log²(delta/pi)+2D0 log(delta/pi)` leaves precisely the
   delta-dependent terms `(2U0/pi)log delta+B0 log² delta`.
   Thus subtraction gives `K_epsilon-K_delta=integral_epsilon^delta
   (Z_L+Z_R)/pi` with the displayed sign. N1-05's two-end envelope
   integrates to exactly Q(P,delta), uniformly bounded by Q(2,delta)
   tending to zero. This proves uniform Cauchy convergence, including
   axes and a=0. The fixed-interior regular remainder is bounded and
   phase-continuous, with only the integrable `d ell/pi` central term;
   dominated convergence and uniform limits give continuous K0 and
   C_infty. C08's weighted product, not unweighted endpoint digamma
   values, supplies the closed-diamond E_infty.

2. **R restriction and boundary telescoping.** C08's numerical tail
   estimate is used only for R>=64. Its exact increment identity extends
   algebraically to R>=2: all shifted large digamma arguments in that
   identity are positive and finite even at a=0. Independently, on an
   open edge t in (0,1), the continuous finite row formulas give

       C_R = (p/pi) sum_(k=0)^(R-1)[1/(k+t)+1/(k+1-t)].

   Since D0=p/pi, B0=0 and h_R(s)=-psi(R+s), the two recurrence sums
   cancel exactly to `E_R=p[-psi(t)-psi(1-t)]/pi` for every R>=2.
   The removable right-row pole contributes its finite sinc value;
   setting a times that rational pole to zero would be incorrect.
   Weighted continuation gives E_R=1 at both vertices. Accordingly
   the R2 contract retains exact beta; it does not use the R64 bound.

3. **Interior constants.** On K=[delta/2,2pi-delta/2],
   T<=8a/delta and the two 1-Lipschitz max formulas give Astar and VA.
   The regular pole remainder supplies Vstar and VV, with the matching
   central limits included. The endpoint s curves have at most three
   monotone pieces and total variation <=8a/delta. The integrable
   derivative envelope for R costs at most 3G, and its monotone
   separation derivative costs at most 2(sbar+u)log2. Product variation
   gives `(16a/delta+4sbar)log(pi/delta)`. Adding the inherited central
   variation 20 gives exactly VJ; the supremum gives Jstar. The limit
   `u log(1/u)->0` verifies the stated u=0 value of G. No inverse
   distance to an axis, root switch or phase boundary occurs.

4. **Actual finite-n geometry and all error shares.** The condition
   n>=ceil(2pi R/delta) gives n>=8R, h<delta/(2R), and all first/last R
   rows within the endpoint strips. The retained ordinary cells lie in
   K. There are at most four other special rows, counting two central
   rows and at most two collision rows. The symmetric difference from
   the interior has at most four missing cells plus boundary length h.
   The regular terms sum to `(VA/2+9Astar)L+VW/2+5Wstar+4Vstar` over m.
   Ordinary central sample distances are >=h; the log quadrature charge
   is d log(m)/(pi m). The missing log integral is bounded by
   `4h[1+log(pi/(4h))]`; adding it gives the displayed
   `d[4+5log m]/(pi m)`. Boundary pieces are outside the log support.
   Exact special norms and their one-sided continuous pole bound suffice
   for the two-sided absolute replacement by the triangle inequality.
   D_n is charged once across disjoint ordinary/special subsets; E_n
   bounds all ordinary cancellation errors. No Rhat/r_n approximation
   is introduced. N1-06/07/08 have precisely the required R>=2 and
   degree floors, including their simultaneous endpoint collision case.
   Substitution H_n<=1+L gives every displayed e4 component. Thus the
   n16 example is a valid but coarse contract, not inherited large-n
   proof labeling for the D01 R64/.01 geometry.

5. **Uniform limit and normalization.** For fixed R>=64 and delta>0,
   every vanishing error has uniformly bounded phase coefficients.
   The remaining limsup is bounded by
   `2/(R-1)+1/(R-1)^2+2Q(2,delta)`. Choosing R and delta before taking
   n to infinity proves uniform convergence through every integer n.
   The phase-relative formula then follows from exact S_n(0)=Lambda_c.
   On a=0, B and its subtraction scale by p, and E_R=E_infty gives
   beta=p*b_delta. The gamma expansion agrees with D01's negative scalar.
   PD-T365 yields the constant `p[C(t)+2log(2/pi)]/pi` and residual
   `(2p/pi)log(1+1/n)+e`, with `|e|<=7/(12[n(n+1)]²)`.
   Both vertices give actual/model value 1 and e=0 by continuity.
   Separate evenness covers signs; PD-T365's CRT covers both parities
   and all polynomial collisions. The midpoint retains D01's sharper
   remainder. No boundary neighborhood or practical interior rate follows.

## Source and novelty coverage

All four D02 theory files were read in full. This reviewer also read
C08-far-endpoint-constant and PD-T365's
[full boundary source](../padua-argmax-effective-2-20261105/theory/profile-boundary-cotangent.md)
in full during this continuation, and refreshed the relevant complete
N1-06/07/08 endpoint statements/proofs, the generic cancellation bounds,
regular-part constants, and special-row arguments in C06. The earlier
[D01 review](independent-checks-D01-far.md) records this same worker's
full reading of the original C06 full-profile/compact-error, N1-02/04/05,
N1-06/07/08, PD-T365/PD-T270, D01 midpoint/contract, relevant full
candidate records, handoffs 08/09 and audit-01. Reuse of that reading
is explicit; it is not a claim of redoing every upstream audit in D02.

The full 1112-line state/IDEAS.md read in D01 is unchanged, SHA-256
`68bf789c82967944421e6fc54f8164dbdb91d1096fa10694008261fbd54f9e9d`.
This round refreshed searches for finite part, renormalization, cutoff
bias, bias completion, joint remainder and endpoint tail in that registry,
the closest full candidate files and audit-01. Closest scope remains
IDEA336/337, IDEA455/456/459/461, C06/C08 and D01. D02 is a quantitative
variant within IDEA459/P1: it openly adds the missing constant and proves
its uniform identification. It retains the phase logarithmic term required
by PD-N132 and does not assume a quadratic phase modulus prohibited by
PD-N079. D01's obstruction for the unchanged constant is not contradicted.
The sharp, fitted and cutoff-only alternatives remain distinctly recorded.
No new negative theorem or historical priority claim is made; no external
source theorem or literature novelty assertion requires transfer here.

## Executed independent controls and provenance

Executed once from `/workspace/padua_research`:

```text
python topics/padua-argmax-bridge-20261105/code/post_audit_D02_far_review/check.py
```

The [independent script](code/post_audit_D02_far_review/check.py), SHA-256
`dab1ddbb87187c4233a186ba6fbe913b3e475b626f97e633df580c8740bc6692`,
pins the raw D01 input and receipt, verifies the phase's scalar inputs,
and reconstructs the formulas without importing the developer's code.
Python 3.12.14, SciPy 1.17.0, mpmath 1.3.0 at 60 decimal digits;
process CPU including imports **0.948853 seconds**, no child process.
The 20-second hard CPU limit was not reached. No failed scientific run
or prior numerical attempt occurred in this D02 review.

The [receipt](evidence/d02-far-review.json) is 4254 bytes, SHA-256
`14260f9d61567bf4a813dc17ce69785e90dc2fd6602c43b50e6cbeff2c744661`.
It records input byte identities, exact script identity, environment,
CPU and all outcomes. The author recombination is reproduced:
`E_infty-E64=-3.497741749569627e-7`, estimated total bias
`.0009602664603997517`, and the three recorded residuals after subtraction.
The omitted-strip envelope is `2.1474249332662035e-6`; the old floating
quadrature estimate `1.2291079141658327e-10` is not a rigorous enclosure.
This replay does not tighten that integration or its roundoff.

Six edge telescoping controls used R=2,64 and t=1e-10,1/7,1/2;
discrepancies were <=1.56e-61. Gamma and 12-term odd-zeta bias expressions
agree to 3.35e-61, yielding `b_.01=-.0011500221952874397545875946881965623`.
Four independent evaluations of PD-T365's one-dimensional cotangent sum
used (n,t)=(2,1/7),(3,1/2),(16,1e-8),(17,1/3). All satisfy the proposed
boundary remainder; the largest absolute error/bound ratio is .074696.
These are **MEASURED** floating controls, not interval certificates or an
exhaustive verification. Vertices and all-phase coverage are analytic.

The raw t1c.json remains the existing 5807-byte local working artifact
with hash `08407e19b8a7a7600ae1c4b8aa00800242dbc2a3f1be6e06dec9a6e1b3ff2d5a`;
its archival/retrieval status is inherited from D01. No new large artifact
was produced. A future replay requires those pinned raw bytes; the support
proofs require neither that artifact nor these numerical observations.

## Remaining limits

No native/full-board computation, new interior quadrature, validation of
an entire phase cover, rate fit, sharp joint estimate or onset improvement
was performed or inferred. The explicit error still has the O(a/R) and
strip floors and grows with the finite row cutoff. Uniform convergence
does not establish the OPEN practical rate. Formal Claude review and
ordinary preparation/registration checks remain the orchestrator's work.
