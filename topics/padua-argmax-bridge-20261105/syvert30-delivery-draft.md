# Syvert30 delivery draft — artifact identity pending root build

User requested all30 workers within128GB total memory and will launch on
Syvert2. New source is syvert30_pack/; the original498f pack/ZIP stays
immutable. Default `./run` is the unchanged full280 workload,7 known plus273
residual degrees, primary/fresh each once. No residual degree has run here.

The completed two-worker sandbox rehearsal at41/511 is the planning anchor:
16.3s wall,29.675187 waited CPU-s,27.554 engine CPU-s across four passes,
maximum individual wait4 RSS159900KiB. This is not simultaneous aggregate
RSS. Shared capture store was about86MB; the41 pair about57MB and511 pair
about28MB raw; fixed source about50MB; complete two-case compressed return
93599070B, independently data-validated for exact subset[41,511].

Conditional extrapolation, assuming those two known cases represent all
unrun degrees AND ideal30-worker throughput:280pairs*(29.675187/2)=4154.52618
waited CPU-s, about138.5s at30fully busy CPUs; scaling observed wall gives
about152s. This suggests a few minutes only under those explicit assumptions.
Different compiler/hardware, thirty-way capture/filesystem contention,
unrun degree complexity and tail imbalance can change it substantially.
Full hard engine envelope is280*2*120=67200CPU-s (37m20s at ideal30CPU),
plus operations, waits and tail. Neither figure is a promised wall bound or
uniform success claim. Each existing cap still consumes the attempt and
stops admissions on failure.

Thirty times the observed individual maximum is4912128000B (~4.91GB), but
this omits concurrent parent/engine/compiler contributions and unrun-degree
variation; it is NOT an aggregate memory forecast. Kernel memory.max, not
extrapolation, enforces the
strict decimal128000000000B cap for the full workload tree. No minimum-RAM or zero-swap gate is imposed. Host physical RAM and actual
cgroup/affinity are verified on Syvert2 rather than inherited from an old
hardware description.

Raw storage interpolation spans roughly8–16.1GB if every pair resembled511
or41, plus the fixed source/shared store. The two-anchor average is about12GB.
These are estimates, not uniform raw bounds or compression ratios. The collector measures actual compressed archive peak
against available space without a fixed scratch floor or extra reserve. Preserve all raw data and failures if space
is insufficient; use an adequate approved archive volume. No deletion or
cold-storage transfer is claimed.

Launch needs beregning allocating>=30cores and an aggregate cgroup cap:
use an existing bounded scheduler cgroup or working systemd user memory
scope. There is no sudo or silent uncapped fallback. Extract the new ZIP
fresh at your chosen path, then `./run`; no path-length gate applies.
The unchanged engine enforces the actual essential-receipt size limit.
The returned archive is data-validated with this separately trusted new
package; a partial result reports its exact subset without claiming closure
of all273 residual degrees. Root fills source SHA, review disposition, ZIP
hash/bytes, manifest hash and concrete download location before delivery.

Reruns are authorized: after all writers stop, move old outputs to a
timestamped sibling directory and rerun the chosen full/small/large cohort
fresh. Previous results remain retained; no retry framework is added.
