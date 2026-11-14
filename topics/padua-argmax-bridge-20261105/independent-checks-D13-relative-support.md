# Independent D13 endpoint/mesh support and OPEN-target review

Rules/input: `e13a538bda80e6cc785f4835937b2ca338bc1d6f` on
`codex/padua-argmax-bridge-20261105`. Date: 2026-11-06.
Reviewer: distinct Codex subagent, parent-requested `gpt-6-astra`, high;
runtime serving metadata unexposed. This is supplementary independent
mathematical review, not the required final Claude handoff. Root alone
owns Git, shared records, allocation and integration.

## Verdict and frozen scopes

**ACCEPT** the two supporting theorems at their exact written scopes and
the full relative-remainder record as **OPEN**. No BLOCKING, MAJOR or
MINOR finding remains. One zero-phase display convention is noted below;
it does not change any theorem or require a new proof. This is one
coordinated D13 review, not a separate round for each supporting lemma.

| Frozen theory | SHA-256 | Accepted scope |
|---|---|---|
| `theory/D13-endpoint-reference.md` | `bb77f8a933cdeb3f5ac5b3bb06c368c91fd2c8603749bb0f554b906cc5f45dba` | For integer n>=32, alpha,beta>=0, rho=alpha+beta<=1/2, the specified fixed endpoint reference and entire unchanged Delta_2 obey `abs(Q_ep(phi)-a Q_ep(0))<=a*rho*(2H_n+10)/n`; signed sectors use absolute phases. |
| `theory/D13-mesh-support.md` | `21098404d8c65ba4ab46528813ada5ac3c6ce7901b3fb51d8abda4868327ffde` | The literal D07 Rmesh and Rlog, including index m-1=n and exact log(m/n), obey `abs(delta_a Rmesh)<=rho/(2n)` and combined charge `<=rho*(log n+7/3)/n` on the same near domain. |
| `theory/D13-relative-remainder.md` | `83213049256d51c44aa3900187989395456c6ce735dc73969304f7d1dfff72f6` | The full finite target with explicit uniform K1,K2 is OPEN. The exact decomposition is valid; neither support proves the full target or a target case/conjunct. |

The files were hashed against the supplied freeze; no author file was
edited. Supporting record hashes:

- `ideas/D13-relative-remainder.md`:
  `1ec1db2ad9f582ad4d417b4b5d0bcc9b6807d11af9f78dc16d9683df36ce7ff7`.
- `attempts/D13-relative-remainder.md`:
  `edc1878d2a6d2bf20c495d5732753e2c05bc23df91944e976ac3d3d6f0ce559e`.
- `ideas/D13-mesh-support.md`:
  `f587f5f87c025168d385214dcef8009420dc462649f1ca576424f612b0029d85`.
- `attempts/D13-mesh-support.md`:
  `2056679e5116c19a4fb32ed89464dedf2e7583fda435c24b0aaef7e88114d279`.

## Independent endpoint reconstruction

1. **Actual indices and no-wrap domain.** With J=floor(n/2), the left
   labels are 2,...,J and the right labels are 3,...,J, on physical rows
   j and 2m-j. They agree with D05-relative-halfline at R=2, including
   both parities. Since x+abs(s)<=1/(2pi)<1/6, j+s lies between
   11j/12 and 13j/12; j+s<m/2 for the actual J, so delta<1/4 and
   u<pi/4. The actual offsets `(1-s+/-x)/2+delta` stay strictly inside
   (0,1), including either axis and zero. No selected sample collision
   is concealed by a digamma assignment. The shifted arguments satisfy
   y>=j+5/12 and y-delta>=j.

2. **Exact displacement and origin factor.** Substituting the unwrapped
   D04 formula gives `Theta/(nm)-Xi=a*e_j` with exactly the displayed U,
   including `-2log(n/m)`. Thus subtraction of a times the origin is
   `a*(e_j(phi)-e_j(0))`, where a is the actual final phase coefficient.
   No derivative of a is lost: it has already factored out algebraically.
   The phase path differentiates e_j alone. The digamma finite part and
   its differentiated positive series apply on the entire path.

3. **Derivative constants.** The positive-series integral comparisons
   give `psi'<=3/(2j)`, `abs(psi'')<=2/j^2` on every required argument.
   They yield `abs(dot B)<=4b/j` and, keeping the differences paired,
   `abs(dot U)<=3b/(mj)`. The latter uses the additional derivative
   of delta; it is included in the stated partial-s bound. The bound
   `abs(U)<=5/n` follows from D04 on this smaller no-wrap domain.
   For tau=u cot u, the stated f,g bounds and derivatives follow from
   `1-tau<=u^2`, `abs(tau')<=2u` and nu<m/2. In particular the four
   terms in (7) arise respectively from f'B, f dot B, g'U and g dot U.
   Conversion to j uses 12/11 and its square with adequate slack.

4. **Summation and the full tail.** There are 2J-3<m selected labels,
   combined harmonic sum <=2H_n and inverse-square sum <=3/2. These
   give `c*b*(54H_n/m^2+24/m+27/n)`, hence the stated `8rho/n`
   displacement bound after multiplication by actual a. The difference
   between the full Delta_2 and the finite Xi sum is exactly the two
   tails starting at J+1; the right series's original start at 3 has
   not been shifted or dropped. For those tails,
   `abs(d(Xi/a)/d lambda)<=6c*b/j^2` is uniformly summable. Indeed
   the coefficient is at most `48/11+1728/1331<6`. Termwise path
   integration therefore gives `8a*rho/(9J)<=2a*rho/n`, using
   J>=(n-1)/2 and n>=32. Adding the accepted D05 half-line increment
   `2a*rho*H_n/n` proves precisely the submitted endpoint statement.

This proves a reference component only. It does not compare the six
actual polynomial rows to their origin or control the central
complement, weighted single-pole error, or regular quadrature increment.

## Independent mesh reconstruction

1. Expanding the literal D07 definition gives

       Rmesh=-B eps H_2-Z H_n-B Q_n-B L^2-2D L.

   Telescoping really ends at n=m-1. Since B=a B^0 and
   Z=a Z^0+DeltaD, origin subtraction yields exactly D13 (5), including
   the lower `-B eps delta H_2` and the combined coefficient
   `-DeltaD*(H_n+2L)`. Its signs and constants match D07. No new mesh,
   cutoff, endpoint constant or model has been substituted.

2. The h/g finite-limit representations follow by telescoping the
   centered-cell definitions. Their differentiated tails converge
   uniformly on [0,1], and terminal logarithmic derivatives vanish
   uniformly. The four derivatives in (6) have the correct signs.
   Pairing h_n'(v)-h_n'(1-v) gives `(n-1)^-2`; pairing g_n' gives
   `(log(n-1)-1)/(n-1)^2`, because `(2log x-3)/x^3` is positive and
   decreasing for x>=31. The lower H_2 derivative bound <=2 is valid.

3. N1-06's harmonic tail has the negative sign in h_n, giving
   `H_n=-log(n+c)-log(n-c)-E_h`, with
   `0<=E_h<=1/[4(n-1/2)^2]`. Thus `abs(H_n+2L)<1/n^2` as claimed.
   The exact complete U0 has both cosine-weighted Phi terms. Its
   origin subtraction gives `abs(U0-a U0^0)<=12rho/pi+rho^2`, so
   `abs(DeltaD)<=3rho/2` follows on rho<=1/2. This uses a=c_e c_delta
   exactly and requires no derivative through a moving numerator root.

4. Substitution gives D13 (12). The positive-rho normalized upper is
   less than `1/3+13/168+3/64=205/448<1/2` for every n>=32.
   The unchanged D07 Gamma/log mesh bound, multiplied by d/pi with
   d<=rho, contributes `rho*(L+11/6)/n`. Adding the two charges gives
   exactly `rho*(L+7/3)/n`. This is not a general quadrature lemma:
   it concerns only the specifically defined D07 scalar remainders.

**NOTE (zero phase, no gap):** Some intermediate simplifications write
`rho/pi<rho/3`, or end endpoint (8) with `<8rho/n`. These strict
comparisons concern rho>0. At rho=0 the exact subtracted expressions
are zero, as both files explicitly state, and their asserted theorem
bounds are non-strict. No zero-phase counterexample or missing limiting
argument results. Optional display hygiene is to use <= there or label
those strict simplifications rho>0; no author edit was made here.

## Full target, collisions and remaining obligations

Using D05's actual K_fixed and D07's scalar G_n,

    S-M_infty=(S-K_fixed)+(K_fixed-G_n)
                       +(J6-C_2)+Rmesh+(d/pi)Rlog.

Taking delta_a, and using d(0)=0, gives the submitted exact decomposition.
For signed phases all comparison quantities, including d, follow the
record's inherited absolute-phase convention. The polynomial S itself
has the inherited separate evenness. This does not exchange n and m.

The original h_0=1, h_i=2 normalization, exceptional `-cos(nu)` mode,
actual polynomial sample values and fixed six row labels are retained.
Complete weighted Phi(integer)=1 and D05's continuity are sufficient
for the exact model identity at collisions; separately unweighted
reference or pole terms are not asserted continuous there. The selected
D13 endpoint set avoids this issue by its proved strict offsets. In
the unresolved central complement the record correctly requires
complete-expression cancellation or a justified limiting assembly.

The three complete increments still OPEN are delta_a Erow, delta_a Eout
and delta_a Eret. In particular D03 only supplies its bounded
cancellation perturbation on actual ordinary rows. D07's absolute
six-row bounds, including the linked beta=0 polynomial endpoint value,
do not supply the required relative increment. The full regular F
quadrature and missing-cell integrals likewise have no new relative
allowance here. The table therefore does not silently promote endpoint
support to a proof of Erow, nor mesh support to a proof of the target.

D10's positive alpha^(3/2) true-constant term remains present. The target
subtracts that true completed model and asks about a finite-n error;
it is not the rejected quadratic true-constant modulus. PD-N079's
finite-primitive cusp and PD-N132's full logarithmic-coefficient
requirement also remain intact. The abandoned two-absolute-bounds and
entropy-only inferences are accurately scoped. No smooth moving-root
assumption, second near correction, new global onset or new finite
certified range is claimed. The current 16000 onset is unchanged.

## Gate, records and execution coverage

Read AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md. Read the
complete 1135-line state/IDEAS.md in ranged reads, with narrower overlap
reads after truncated broad outputs, including every obstruction and
disposition block and IDEA590--603. Registry SHA-256:
`08e6886269a7bb76eaeb60b57f37935f5a390f37ae1df5d0167cdaac2ed7093a`.
Mechanism searches covered relative/origin, digamma, finite remainder,
moving roots and singular meshes across current ideas, attempts, theory,
LOG, literature INDEX and negative-result indexes. This is not a read
of every unrelated linked theorem. Read literature INDEX's qualification
and relevant Padua/asymptotic/relative search entries; no external source
theorem or historical-priority claim is accepted.

Full immediate predecessor reading included D03 cancellation candidate
and proof; D04 candidate and all three half-line/reference/row proofs;
D05 relative and fixed-row candidates, relative-halfline, fixed-special
rows and outer-profile-variation proofs; D07 global candidate, global
outer/mesh, four-endpoint, central-row and six-row allowance proofs;
D10 candidate and axis obstruction; N1 regularized-pole, endpoint-profile
and h/g mesh proofs; and D02's exact bias/model definition. These are
the actual closest mechanisms. The D13 endpoint theorem fills D05's
explicitly missing displaced-digamma increment; the D13 mesh theorem
is a quantitative relative continuation of D07's absolute scalar bounds.
Neither is merely a relabeling of the inherited D05 or D03 result.

Read both D13 candidates and attempts in full and checked their retained
routes and scope labels. The helper's limited fresh gate coverage is
disclosed rather than represented as its own complete line-by-line
registry read; this review does not rewrite that history. The parent
family gate and prospective LOG justification are recorded, including
the interrupted/resumed bounded paper allocation. No unsupported
retrospective timing or independent-development-as-review claim follows.

Execution was paper-only mathematical reconstruction. Tools performed
repository listing/search/reads, SHA-256 hashing, a required environment
status read, and creation of this report. One initially guessed D07
candidate filename was absent; the actual D07-global-profile candidate
was then found and read. No scalar control, scientific/numerical job,
native call, board/phase/degree evaluation, quadrature, root computation,
fit, test suite or background scientific process was launched. The tiny
scalar allowance was unused: scientific CPU consumption was zero.
No shared file, author file or Git state was changed by this reviewer.
