# PD-T?nn-mop-stability-codex-D2-02 — alternating-path spectral diagnostic

ID kind: PD-T. Aliases: fixed-step-line recovery; anchored path diagnostic.
Split from: none. Split into: none. Overall status: **MEASURED**.

## Statement

The supplied high-precision diagnostic converts a computed NN array on the
N−1 triangle to one alternating-path N-by-N Hessenberg matrix, recovers its
spectral nodes and two normalized weight vectors, and compares them to the
input. At several large-N cases these spectral data have substantial imaginary
nodes or negative weights, so even this diagnostic cannot be read as a nearby
positive-real input perturbation. It is never automatically a full-array NN
backward error: the construction uses a strict subset of the NN data.

## Definitions and assumptions

The path starts with e1 and alternates: nu_k=(ceil(k/2),floor(k/2)).
Masses of both measures are fixed to one. Computed floating coefficients
are embedded exactly into mpmath before spectral arithmetic. Nodes are sorted
by real part then imaginary part and compared in this order to sorted input
nodes; this is an explicit pairing diagnostic, not an optimized matching.
The output also gives componentwise relative normalized-weight error and its
maximum with node error (`mixed_input_diagnostic`), matching the D1 mixed
metric in the chosen normalized-mass gauge. It remains a path diagnostic.
The output records imaginary-node/weight magnitudes, minimum real weight and
mass residual as well as node/weight errors. Complex/negative recovered data
are not admitted silently to the positive-real input domain.

## Local derivation used by the implementation

Write Q_k=P_(nu_k), S_nu=a1_nu+a2_nu, and d_nu=b2_nu−b1_nu.
PD-T289 gives P_(eta+e1)−P_(eta+e2)=d_eta P_eta. Substituting this
into the NN recurrence at nu_k gives

    x Q_k = Q_(k+1) + b_k Q_k + S_(nu_k) Q_(k−1) + g_k Q_(k−2),
    b_k = b1_(nu_k) for k even, b2_(nu_k) for k odd,
    g_k = −a1_(nu_k) d_(nu_(k−2)) for k even,
    g_k =  a2_(nu_k) d_(nu_(k−2)) for k odd.

Omit absent lower terms. Assemble H with column k given by these coefficients,
subdiagonal one, and truncate after k=N−1. The polynomial recurrence then
makes det(xI−H)=Q_N. For true compatible data Q_N is the support polynomial.
The transpose convention is explicit: columns represent multiplication.

Path orthogonality implies normalized functionals l1=(1,0,...,0) and
l2=(1,d_0,0,...,0) in the Q basis: Q1=x−b1_0, hence L2(Q1)=d_0,
while every Qk for k>=2 is orthogonal to both measures. The d_0 value is
an additional NN anchor. A step-line alone leaves mu2→mu2+c mu1 ambiguous.
For a simple diagonalizable H=V diag(lambda) V^-1 the spectral masses are
(l_j V)_i (V^-1 e0)_i. This is the formula evaluated by `path_recovery.py`.
These routine identities explain the implementation; no new general inverse
or realizability theorem is claimed here.

## Status by part

| Observation | Status | Evidence |
|---|---|---|
| Recovery from HP true arrays at N4/8/12 matches inputs to <=2.43e-98 | MEASURED | Local six-case check in D2 receipt |
| Path spectral diagnostics for all four algorithms, twelve inputs | MEASURED | D2 receipt and raw JSON |
| Whole-array nearest-positive-input backward error | OPEN | Not computed by this diagnostic |

No candidate rejection or broad negative theorem is proposed.

## Depends on

PD-T289's NN and successor-difference identities. Numerical eigenvalue and
matrix inversion routines in mpmath. Simple diagonalization is an operative
numerical assumption; the diagnostic reports failures rather than asserting
all arbitrary computed arrays have simple real positive spectral data.

## Checks and sources

`../code/path_recovery.py`, called by `stage_isolation.py`; executed commands,
actual results and hashes are in `../attempts/D2.md`. Primary paper fulltexts
are unread by this worker. The approach resembles the high-precision spectral
backward diagnostics reported in LIT-119/347, but it is not a reproduction of
those algorithms, norms or configurations.

## Scope and open items

Path data discard off-path entries. For the even N>=4 in the recorded
grid they also never read b2 at nu_(N-2) or b1 at nu_(N-1); the opposite
parity swaps those two unused b fields. The origin still uses both fields
for its extra d0 anchor. Small recovered-input error neither
proves exact compatibility of the full NN array nor bounds the distance to
its nearest compatible array. Changing the path could change the diagnosis.
The second-measure anchor and mass gauges must be retained in comparisons.
General well-posedness, closest positive input, derivative certification and
independent rerun remain separate D1/D5/audit obligations. Local raw evidence
has not been transferred to cold storage.

## History

2026-11-05, Codex dispatched gpt-6.1-sol medium; input/rules
823cf6a4ef7c01b4ef3d2a6fec3e9f19d4b4f6f1. Added finite diagnostic with explicit
path/full-array and positivity qualifications.
