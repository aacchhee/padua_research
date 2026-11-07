# Does the campaign require Syvert2?

2026-11-07 read-only resource assessment, input head
4a5de2012bad94601c713b2ff5517f2e3fb80af2. No engine/control/degree run.

Observed in this actual session: cpu.max400000/100000 (four CPU-equivalents),
effective affinity0–4 and nproc5; memory.max17179869184 (16GiB); overlay
capacity33770192896B, free29119561728B (27.12GiB) at measurement;
existing local-output2680432658B. Original packed tree49731698B and ZIP
25104521B exist here, unlike the earlier Claude checkout. No storage was
deleted and no archive rebuilt. Filesystem free space is transient. A later mount check found /tmp is a
separate tmpfs:9441329152B capacity,9423917056B free (8.78GiB), and its
writes also compete for memory. It cannot host the14–16GB raw estimate.
Use a short /workspace/p02 root on the measured overlay, not /tmp.

Syvert2 is not mathematically necessary. Its unchanged launcher is unusable
here because of the Syvert2 hostname, beregning, default40workers and
128GiB/64GiB free-space floors. A distinct local operations variant can use
the existing frozen engine and pinned packages without mathematical changes.
Initial two-worker integration is conservative within16GiB; four workers
would each have2GiB virtual-address limit but shared cgroup memory still
needs observation. nproc5 does not override the four-CPU quota.

The existing observed known cases cost roughly6–8 CPU-s/pass; compilation
dominates. If that range happened to hold for560 passes it would mean
3360–4480 engine CPU-s, roughly14–19 ideal minutes at four CPU or28–37 at
two, plus operations. This is arithmetic illustration only, NOT a forecast
or success guarantee for273 unrun degrees. Neither identical caps nor nearby
successful degrees establish uniform success or runtime. Each primary and
fresh pass can consume120CPU-s. Full280*2*120=67200CPU-s is a hard engine
envelope, not a completion prediction: four ideal saturated CPUs correspond
to4h40m, two to9h20m, with compilation/capture/supervision/archive/idle time
additional and failures stopping admissions. Worker wall guards further
bound individual attempts; a session itself may expire sooner.

The prior rough14–16GB raw estimate would fit the measured29.12GB free
space alone (about13–15GB remain). It is not a bound derived from the
engine's scientific caps: preprocessed TUs, compiler dependency capture,
shared libraries, toolchain sizes and absolute paths are host-dependent.
An equally large uncompressed duplicate archive could exceed remaining
space at the upper end. Therefore "everything fits" is presently unproved.
Compression may reduce archive peak substantially, but must be measured.
The new collector precomputes actual compressed payload sizing in bounded
memory before creating a second copy and preserves raw data if the check
fails. It does not deduplicate or drop proof dependencies.

Use the two-known-case rehearsal to measure concurrent RSS, compiler/loader
compatibility, raw and compressed growth and capture costs. Before any
later campaign, budget each preregistered cohort against remaining disk,
reserve the next cohort plus archive peak and1GiB, keep every failed or
interrupted attempt and prohibit retries across roots. Transfer complete
quiescent artifacts only to AC-approved Padua cold storage; no new storage
destination is invented here. Streaming hashing/ZIP uses bounded memory;
streaming to a genuinely approved different volume can avoid local archive
peak if available. This session currently provides no such transfer claim.

Decision: do not rebuild the Syvert2 pack now. Retain it as the immutable
old artifact with unresolved release findings. Review this small new local
operations identity and test known41/511 first. The sandbox appears adequate
for that integration, and may support the full finite campaign, but full
runtime/disk/success feasibility remains conditional on measured evidence
and a separate root release. No residual degree has been attempted here.
