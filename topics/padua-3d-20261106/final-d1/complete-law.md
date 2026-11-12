# PD-T?padua-3d-20261106-codex-D1-03 — critical mean intensity completes an orthogonal law

ID kind: PD-T. Aliases: D1-COMPLETE; Bessel saturation in expectation.
Split from: the completeness obligation of frontier C1.
Split into: none.

## Statement and assumptions

Let O be a bounded measurable subset of R^d of finite positive volume v. Let P be a probability law on locally finite countable sets Lambda for which exp(2pi i lambda.x), lambda in Lambda, are pairwise orthogonal in Lebesgue L2(O) almost surely. Suppose its mean counting measure is v times Lebesgue measure; equivalently, for every nonnegative f in C_c,

    E sum_(lambda in Lambda) f(lambda) = v integral f.

Then the exponentials are complete in L2(O) for P-almost every Lambda. In particular O is spectral. Local finiteness/separation as supplied by D1-02 ensures the counting sums are measurable. Stationarity is sufficient for obtaining this mean measure in D1-02; this lemma only needs the displayed mean measure itself.

## Status and dependencies

Overall status: **PROVED** (local analytic lemma). Standard Fourier-analysis background: Plancherel for the exp(2pi i xi.x) convention, uniqueness of the Fourier transform on L1, Bessel's inequality, Hilbert-space orthogonal projection, monotone convergence. These are used explicitly below; no spectral-set classification theorem is used. No negative-result disposition. The original C1 consequence is a separate source-dependent theorem.

## Proof

Put

    F(y)=(1/v) integral_O exp(2pi i y.x) dx.

Since the indicator of O lies in L1 and L2, F is continuous, and Plancherel gives

    integral_R^d |F(y)|^2 dy = (1/v^2) integral 1_O(x)^2 dx = 1/v.   (1)

The mean-measure identity extends from C_c tests to every nonnegative Borel test: first identify the locally finite mean measure using continuous tests, then use equality of measures and monotone convergence. In particular, for each fixed y,

    E S_Lambda(y) = v integral |F(y-z)|^2 dz = 1,
    S_Lambda(y)=sum_(lambda in Lambda)|F(y-lambda)|^2.               (2)

This is a nonnegative integral, so no integrability or tail exchange is assumed before Tonelli; (1) shows the resulting value is finite. Equivalently one can first multiply the test by increasing continuous compact cutoffs and then take their monotone limit.

For an orthogonal realization, h_lambda(x)=exp(2pi i lambda.x)/sqrt(v) is an orthonormal family. Testing Bessel's inequality against h_y, also of norm one, gives

    S_Lambda(y)=sum |<h_y,h_lambda>|^2 <=1.                         (3)

Thus (2)–(3) imply S_Lambda(y)=1 almost surely for every fixed y. Intersect these probability-one events only over y in Q^d, along with the original probability-one orthogonality event. For any realization in that countable intersection, the orthogonal projection of every h_y, y rational, onto the closed span H of the h_lambda has squared norm one. Pythagoras implies h_y belongs to H.

If g in L2(O) is orthogonal to H, its zero extension to R^d is in L1 because v<infinity. Its Fourier transform vanishes at every rational y. Continuity makes it vanish at every real y, and Fourier uniqueness makes g=0 almost everywhere. Consequently H=L2(O). This holds outside a single null set, proving completeness. QED.

## Scope and history

This uses exact mean intensity and almost-sure orthogonality, not only a density number assigned to a deterministic set. For example removing one point from a lattice spectrum can preserve asymptotic density while destroying completeness; such a deletion has no stationary probability law retaining a positive expected isolated hole at intensity zero. No claim that critical density alone suffices is made.

No numerical work. R3 preregistration published/pushed at `613735e` before root GO and this proof. Codex, assigned gpt-6.1-sol xhigh, 2026-11-12; stationary-translation route credited to root. Closest compactness and spectral-kernel precedents are in sources.md.
