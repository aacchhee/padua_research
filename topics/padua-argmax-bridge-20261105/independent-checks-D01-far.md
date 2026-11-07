# D01-far supplementary independent review

2026-11-06. Rules/input HEAD:
`e6549177fe48c7fea8436cece8a04b411dc544e1`.
Role: distinct Codex supplementary mathematical and computational reviewer,
requested gpt-6-astra xhigh; serving model/effort metadata is not independently
exposed. This check does not replace the separate formal Claude audit.
No author proof, source, shared record or Git state was changed by this reviewer.

**Verdict: ACCEPTED at the written scopes**, after one MINOR reporting
correction, now closed. No unresolved BLOCKING or MAJOR finding. The positive
midpoint identity and its scoped negative consequence are analytically
supported; the twelve-case diagnostic remains MEASURED. This is neither
a new onset result nor approval to launch a validated phase cover.

## Frozen inputs and coverage

| Record | Reviewed SHA-256 |
|---|---|
| [Midpoint identity](theory/D01-far-midpoint-identity.md) | `85d982389f53073d318fb4e3995d1297dcf9d51d95c27e32a278dbbbb4d30a47` |
| [Scoped obstruction](theory/D01-far-contract.md) | `60ab4c5534c5b90bc2e9b5d16ac00d209f158cded7796951dafbab7492758340` |
| [Pre-run SPEC](code/post_audit_D01_far/SPEC.md) | `691c5bd548044a42dbdf5a165976eda1b208f340471d75b4d27156016e706dee` |
| [Author receipt](evidence/d01-far.json) | `10b8b2800b6ac910ce50eb43f50005b409388f664a3d8dc5ea2d62ab59323c1d` |

Read AGENTS/WORKFLOW/CODEX, handoffs 09 and 08, the D01 idea/attempt/SPEC,
audit-01-ideas P1, and the relevant LOG history. Read the full original
C06-far-compact-error and C06-far-full-profile sources, N1-02/04/05/06/07/08,
PD-T365 and its PD-T270 midpoint-remainder dependency. Reconstructed the
new identity from these formulas; no broad re-audit of unrelated upstream
estimates or C13's proof is claimed.

Read all 1112 lines of state/IDEAS.md, including all obstruction/disposition
tables (SHA-256 `68bf789c82967944421e6fc54f8164dbdb91d1096fa10694008261fbd54f9e9d`).
Read full shortlisted C06-far/C08-far-comparison candidate records,
IDEA-336/337, H2-H3's IDEA-455/456/459 records, and PD-N132. Searches across
the registry, literature INDEX, bridge/effective-2 ideas, theory, attempts
and logs used fixed strip/cutoff, nondecay/non-decay, midpoint bias/residue,
uniform vanishing, digamma and gamma constant. This is a bounded repository
scope comparison; no full literature-index/fulltext review or historical
priority claim is made.

The closest existing negative result, PD-N132, omits the phase-dependent
linear logarithm. D01 keeps that logarithm and detects the remaining
nonzero fixed-cutoff constant. Its separation is therefore real at the
stated formula level. The diagnostic is the existing P1 test, not a new
general mechanism. P1 already permits an explicit epsilon_0 residual;
that broader proposal is not refuted. No candidate, theorem or negative
ID was newly allocated by this review.

Read the complete D01 model/native/build/run/supervise/finalize sources,
original c06_far_profile_diagnostic.py, and C11 point.cpp/partial.cpp.
Reviewed all twelve author receipt rows and their input/domain/CPU labels.
Actually reran only the two n=512 cases specified below.

## Mathematical reconstruction

1. **Normalization and parity.** Original S is `(2nm)^-1 sum |G|` on
   the odd board; the C11 row variable is `F=(-1)^delta G/2`, hence
   `S=(nm)^-1 sum |F|`. No factor of two is lost in D01. PD-T365's
   two-element CRT fibers contain exactly one odd-board point because
   adding `(n,n+1)` changes parity. Its midpoint `S=L_[n(n+1)]` and
   PD-T270 remainder apply to every integer n, independently of parity.
   D01 uses the model formula at small n without importing C06's
   large-degree approximation theorem.
2. **Boundary algebra.** At alpha=beta=pi/2, `a=c_e=0`, `c_d=U0=p=q=1`,
   `C=0`, `D=1/2`, and the cancellation integral is identically zero.
   Consequently `B0=0`, `D0=1/pi`, `b_full=4/pi`, and the g_R term
   vanishes exactly. Periodicity/reflection of Phi_0 gives
   `B(v)=[-psi(t)-psi(1-t)-2log pi]/(2pi)`, `t=v/(2pi)`.
3. **Removable sinc values and R cancellation.** On the positive-beta
   branch every surviving sine argument is a nonzero integer multiple
   of pi, giving `ell_r=1/[pi(r+1/2)]`. On the negative branch only
   `j=r-1` has sinc(0)=1; its doubled contribution and `sin(b)/w`
   give `ell_r=1/[pi(r-1/2)]`. Together with ell_0=2/pi this proves
   `C_R=(2/pi) sum_{k=0}^{R-1}(k+1/2)^-1` with the correct R versus
   R-1 endpoints. N1-06's convergent harmonic identity yields
   `h_R(t)=-psi(R+t)`. Thus
   `C_R+c_mesh=(2/pi)[-psi(1/2)+log(delta/pi)]` exactly. No
   zero-times-infinity or finite-tail approximation is used.
4. **Integral, convergence and sign.** Integrating B gives the stated
   log-Gamma difference with factor 2/pi. N1-04's absolutely convergent
   series expands as `1/t+2gamma+2 sum zeta(2k+1)t^(2k)`; on every
   compact interval below 1 the uniformly summable series permits
   termwise integration. The normalization at zero gives equation (8).
   After subtraction from PD-T365, the limit is precisely
   `b_delta=(4/pi)[(gamma-log pi)eps+sum zeta(2k+1)eps^(2k+1)/(2k+1)]`.
   The written strict sign argument is valid: `gamma-log pi<-1/12`,
   while the positive series divided by eps is less than
   `eps^2/[2(1-eps^2)]<1/12` for `0<eps<1/600`. It also gives the
   uniform cubic tail and the linear-in-delta leading coefficient.
5. **Finite n and exact negative scope.** `log(n(n+1))=2log n+log(1+1/n)`
   gives the stated `(2/pi)log(1+1/n)` correction, retaining the
   `1/(4n^2(n+1)^2)` remainder. At fixed delta=.01 the error tends
   to a strictly negative constant, contradicting any finite uniform
   `C(1+log n)/n` bound on the full closed diamond. This does not
   contradict a fixed positive C06 error, the existing n>=500000 proof,
   an error with a residual allowance, or a different model. The
   interior phase (1.45,1.45) is outside this limiting-identity theorem.

The analytic proof has no numerical premise. The positive identity is
substantive and correctly split into its own provisional PD-T dependency;
the PD-N contains its narrowly quantified consequence.

## Signed telescope, source controls and actual execution

The SPEC's partition P/K/T/O is exhaustive and disjoint, with collisions
classified by rational offsets, and P taking precedence. At all twelve
requested cases `delta*m/pi<R`, so the ordinary endpoint set Z is empty.
The exact mesh term is therefore `-P_end(L)` and Q_actual=0. Adding and
subtracting the full retained-interior integral still gives the displayed
telescope. Its large mesh/interior compensation is explicit; it is not
an instance of N1-08's estimate below n>=40213. Success T1-a fails for
this telescope. The asymptotic componentwise kill remains OPEN because
these samples do not isolate irreducible limiting components.

Native inspection found only the stated side-channel assignments in the
generated point code; its four retained rows recompute finiteF for capture
without changing the total's arithmetic. The review script reconstructed
those exact replacements and byte-compared the result. The pole split is
`ceil(n/2-t)`, with an exact zero harmless in the remaining block, and all
ordinary offsets avoid actual poles. Both actual rows and separate pole
norms are normalized by nm. In E/D, the cancellation integral is divided
by pi*m, and the regularized profile by m, as required.

Actually executed:

```
python3 topics/padua-argmax-bridge-20261105/code/post_audit_D01_far_review/check.py
```

One execution, exit 0, **10.716354 CPU seconds**, measured in the Python
process from before imports; no child process or compiler was launched.
The process limit was 38 CPU seconds under the parent's 40-second cap.
Read-only shell/source inspections are outside that numerical meter.

The script reused the hash-verified native artifact, checked its actual
loaded native dependency paths/hashes, reran d01_rows/d01_poles and the
unchanged c07_point entry, then independently summed the original finite
polynomial and all separate cotangent norms in long double. The two inputs
were n=512 and normalized phases
`8314533651872855/18014398509481984` in both coordinates (the represented
1.45 target), and exactly 1/2 in both coordinates (the midpoint). The same
recorded rational phases feed native, direct and model paths.

| Control | Observed maximum/result |
|---|---:|
| Native total versus unchanged c07_point and author's stored intervals | Exactly equal in both cases |
| Direct polynomial row versus native row midpoint | 4.14e-17 |
| Direct finite pole norm versus native midpoint | 1.49e-18 |
| Maximum native row/pole half-width | 5.56e-17 / 1.74e-18 |
| Independently reconstructed component versus author component | 5.03e-13 |
| Signed telescope closure | 2.52e-15 |
| Counts per case: ordinary / endpoint / collision / central | 896 / 128 / 0 / 2 |

The component comparison uses a fresh tighter model quadrature, sharing
the reviewed model's formulas; it is not an independently implemented
general-phase integrator. Both runs gave no quadrature warnings. A separate
60-digit midpoint digamma integral, finite harmonic endpoint sum and zeta
series agreed to 2.13e-61, yielding

    b_.01 = -0.00115002219528743975458759468819656229538366380857...

A direct one-dimensional cotangent sum at N=262656 gives a measured
finite remainder about 6.32473e-13, below the theorem's 3.62381e-12 bound.
High-precision Stieltjes evaluations independently checked both interior
g_R constants: the six-term EM discrepancy is below 3.84e-27, within
the displayed remainder below 9.32e-21. Binary64 roundoff is about
2.28e-15 and is correctly separate from that analytic tail bound.
These controls support the artifact diagnosis without promoting either
SciPy estimates or high-precision agreement to a proof.

The full author twelve-case run was **not** repeated. Its source and
supervisor receipt support the recorded 182.246419 CPU seconds, with
metadata finalization separate. No odd degree, nonempty collision class,
nonzero central-log coefficient or all-phase cover was independently
executed here. The source's sampled phases all have `(q-p)_+=0`, so the
absence of a general central-log subtraction in this restricted evaluator
does not invalidate these measurements; it gives no general-phase coverage.

## Findings and disposition

**F1 — MINOR, closed.** The original attempt lines 119–120 and README
lines 86–87 said the finite-n oracle discrepancy was below 2e-14 without
restricting the tested degrees. The unchanged author receipt gives
6.15793006863985e-13 at n512, versus less than 2e-14 at n2048/8192.
The finite e_n term makes this expected; it is not evidence against (1).

Returned to the parent before any correction. The developer changed only
those two passages to state the degree restriction, overall maximum and
the theoretical finite remainder. Checked the exact old/new diff and
preserved pre-edit snapshots in
`local-output/argmax-bridge-20261105/post-audit-D01/far/minor-oracle-wording.json`.
Accepted corrected hashes:

- attempt: `7b4c113f88033a8dddfbfde36bb118c9a6fc9a22a08c1d244ef870173ba46363`;
- README: `d6b4e58b7f9edbbba3f928563134f27f78959e5c1055a434fa2e02dd5b483105`.

Both frozen theorem hashes, executable source and author receipt remained
unchanged. This closes F1 by focused record review, with no extra scientific
execution. No other actionable finding was identified within this scope.

## Evidence and remaining limits

[Independent receipt](evidence/d01-review-far.json): 8665 bytes,
SHA-256 `6f3a23f11b600797f140f15043d04bab323fbb318b6e9978319dde1bbd36542a`.
It records the executable source hash, native binary and loaded closure,
actual inputs, versions, numerical outputs, CPU scope and two raw-array
identities. The [review script](code/post_audit_D01_far_review/check.py)
is preserved; the two 71042-byte NPZ files are in the existing local Padua
output tree, not Git. Physical cold-storage delivery remains pending.

This was an independently authored finite-sum check with a reused native
binary, not a fresh native build. Full Python package trees were not pinned.
The broad interior limiting bias, a useful joint small-degree mesh/interior
estimate, validated phase-local residual allowance and any lower effective
onset remain OPEN. Formal Claude audit remains separate.
