# IDEA?mz-sharp-codex-P1-04 — coarse rectangle norm instance

Aliases: constant positive Schur vector; angular Darboux certificate.

- Question/scope: execute the already derived finite rectangle certificate
  with h=1. Seek honest coarse bounds on r=||B|| and c_minus=-r; no
  three-digit assertion and no improved c_plus certificate.
- Mechanism/hypotheses: exact positive kernel and rectangle integral of
  theory/P1-rectangle-certificate.md. This is a numerical instance of that
  gated mechanism, not a new analytic mechanism or historical novelty.
- Closest entries/read: P1-rectangle-certificate and its antecedents; P4
  integer interval continuation and IDEA-058. Shared P1 gate covers the
  underlying full-registry scan; technical worker personally read the
  complete rectangle reduction and relevant P4/S2 predecessor records.
- Separation/kill: the distinction from smooth Nyström is literal
  outward-bounded full-rectangle integrals. Missing triangle boundary
  source cells, unbounded singularities or missing elementary enclosures
  erase that distinction and invalidate the instance.
- Literature/search limitations: inherited local kernel proof only; no
  external theorem/priority claim. This creates no new upper mechanism.
- Obstructions: positive full source boundary rectangles are included for
  Schur upper; only lower numerator may omit them. No pointwise elliptic
  diagonal evaluation or unproved quadrature error is used.
- Verdict: technical instance of retained P1 rectangle mechanism.
- Cheapest test: fixed grid N=8 and angular partition T=64.
- Preregistered round 2: N=16,T=256 only if round 1 has 0<L<U and finishes
  under 60 CPU seconds. This is an implementation/progress trigger, not
  an error estimate. No other numerical grid/candidate is authorized.
- Kill/stop: retain a failed check with its exact reason. Stop after those
  two instances or any invalid proof/arithmetic invariant; report broad
  intervals without tuning. Existing global 6h/run,48CPUh,2heavy caps apply;
  this script is single-threaded and has an internal 300 CPU-second cap.
- Discriminability: bounds certify only the reported coarse interval;
  they cannot establish practical digits unless the interval itself does.
- Actual results/evidence: both unchanged planned instances executed after
  c1e6e59dd9155b87d9847155d3455d602a5f84e9 publication. See the dated
  completion pointer at the end; original protocol below is preserved.
- Disposition: retained local PROVED coarse instance after distinct
  reconstruction and actual rerun PASS; sharper digits and a c_plus-
  specific residual certificate remain deferred pending an independently
  checked stronger finite reduction. Neither target is refuted.
- Canonical result: theory/P1-numeric-certificate.md after execution and
  independent checks. Required Claude audit remains separate.

## Frozen numerical protocol

Use exact rational bins W_i=[i/N,(i+1)/N], 0<=i<N. Outer square cells
R_ij=W_i x W_j satisfy i+j<N; these cover D including every boundary
cell. Inner cells satisfy i+j<=N-2. Choose h=1 on all D, so its exact
squared norm is integral_D ab da db=1/24.

For every target bin W_i, source bin W_j and t=0,1, enclose I_t(a;W_j)
uniformly on a in W_i by the angular Darboux formula (1) of the reduction.
Partition theta into T intervals [pi*l/T,pi*(l+1)/T]. Enclose cos on each
interval by monotonicity and endpoint Taylor enclosures. Evaluate
z=t-a*cos(theta), its exact interval square, and each positive square root.
The difference lies in [0,sqrt(v²-u²)]; intersect the naive difference
enclosure with that known interval. Sum interval bounds and multiply by
kappa_t/(pi*T), which is exactly kappa_t/pi² times angular interval width.
Take nonnegative lower endpoints throughout. Pi uses P4's already reviewed
Machin enclosure; sqrt uses exact math.isqrt with outward integer endpoints.
Cos uses its entire Taylor series and twice-next-term bound once the
absolute ratio is <=1/2 and the tail is below 2^-128. Arithmetic is the
unchanged reviewed 256-bit integer interval module.

For upper row Q_ij sum 8[I1(i;sourcea)I0(j;sourceb)+
I0(i;sourcea)I1(j;sourceb)] over all outer source cells. Let U be the
largest upper endpoint over all outer target cells. This proves r<=U.
For each scalar J_t(W_i,W_j), the bound is mass(W_i)*I_t(W_i;W_j),
where mass(W_i)=((i+1)²-i²)/(2N²) exactly. Sum the positive products from
equation (11) over all inner source/target cells, and multiply its lower
endpoint by 24 to obtain L<=r. Record full rational dyadic endpoints,
outward decimal summaries, hashes, command, precision, timings and the
number of source/target cells. Assert 0<=L<=U before reporting [-U,-L]
for c_minus. Inherited c_plus remains 0<c_plus<=r<=U; there is no separate
improved positive spectral enclosure.

Commands from repository root after publication:

```
python topics/padua-mz-sharp-constants-20261106/code/P1_rectangle.py --N 8 --theta 64 --output topics/padua-mz-sharp-constants-20261106/evidence/P1-rectangle-N8.json
```

If and only if the stated round-2 trigger holds, substitute N=16,theta=256
and output P1-rectangle-N16.json. A distinct reviewer must inspect the
scalar/Darboux implementation and actually rerun consequential output.
No result is called a computer-assisted proof before those obligations.

## 2026-11-06 completion pointer

N8,theta64 executed in 0.118 CPU seconds with strict positive lower and
L<U, so the stated N16,theta256 trigger was met. N16 executed in 1.959
CPU seconds and returned r in
[0.013164946500379018110831,0.477809279990884889210594]. No third grid,
source tuning or c_plus-specific calculation was run. Exact commands,
historical protocol hash, receipts and independent review are
in [theory/P1-numeric-certificate.md](../theory/P1-numeric-certificate.md).
This append-only completion pointer changes the current protocol file
hash; receipts refer to its original blob at the published commit.

Distinct scalar/code/reduction review and actual N16 rerun subsequently
PASS with bit-identical endpoints; see independent-checks-P1-numeric.md
and the linked committed independent receipt. Required Claude audit is
separate; the local computer-assisted result claims only this coarse
interval, not practical digits.

## 2026-11-06 audit-02 C3 predecessor clarification

Closest entries also include IDEA-466, “dyadic outward-enclosure certifier;
fixed-point trial-energy witness”; its full
[candidate](../../padua-mz-cleanup-20261105/novelty-gate-math.md#idea-466--dyadic-outward-finite-witness-certifier)
was read for this correction. It certifies one exact dyadic Padua
polynomial's full signed nodal energy with exact positive norm. P1 shares
its outward finite-certificate pattern, but bounds full source rectangles
of the already proved positive integral kernel, using a Schur upper
bound and constant-vector Rayleigh lower bound. Those rectangle-integral
and coverage obligations distinguish the instance; dyadic rounding is
inherited technique, and missing boundary coverage or elementary
enclosures erases the distinction. The technical-instance/consolidated
continuation verdict is unchanged. The frozen numerical protocol above,
thresholds and receipts are preserved; no new execution is claimed.
