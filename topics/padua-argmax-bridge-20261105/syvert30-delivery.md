# Current Syvert30 delivery — lean runner

AC requested removal of conservative gates after the first preflight failed
on a41-character path. The current update removes that restriction,80GiB
minimum-RAM/host floors, zero-swap policy and fixed scratch/archive reserves.
The actual receipt-size and mathematical checks remain, as do30workers and
the128000000000B aggregate RAM ceiling. Cheap fresh-cohort reruns are authorized.

## Update the existing Syvert2 directory

[Update ZIP](../../../local-output/argmax-bridge-20261105/syvert30-lean-529ee8be/padua30-update.zip):
36,756B, SHA256 `436331e8f3cb6932f30a90e57c21de8369f86e1f6db8de80ba8d99d97aef8835`.
It contains only13changed files. Put it in `~/num_tests`; from the existing
`~/num_tests/padua30`, after the stopped preflight:

```sh
mv outputs "../padua30-preflight-$(date -u +%Y%m%dT%H%M%SZ)"
unzip -o ../padua30-update.zip -d ..
./run_small
```

Then `./run_large` attempts the273residual degrees using30workers. The small
group is41,42,63,64,159,160,511. Both execute primary+fresh per degree.
The existing long path is supported. The failed preflight admitted no degree.

For a fresh installation, [full ZIP](../../../local-output/argmax-bridge-20261105/syvert30-lean-529ee8be/padua30.zip)
is25,094,674B, SHA256 `29f707a9256dfe08bf7d2c0051a1f56de457dfe4d99992c90ad74cbfc9c85528`.
Source `61cf9ab5d143cea993ce2cde6d88302a6c10b7bc`; manifest52,884B SHA256
`c8a2ed7e508df8f781668c186ca53bea472c2a7a1c336c03f14f1cdb069273fc`.
Original7cf/e51b442ZIP remains preserved. A stopped cohort can be rerun by
preserving outputs outside the package and starting that cohort fresh; no
retry framework or prohibition overrides AC's current instruction.

`./finished_cases` reports status. Once stopped, collect the complete return:

```sh
./collect_data --archive-directory /adequate/archive/path
```

The collector checks actual compressed peak space; there is no fixed free-
space floor. Keep raw/build/captured evidence for checking returned degrees.
A partial return reports exactly completed pairs without claiming full closure.

## Time, RAM and disk planning

Finished two-worker41/511 rehearsal:16.306wall seconds,29.675waitedCPU seconds,
27.554engineCPU seconds, maximum INDIVIDUAL reportedRSS159900KiB. All four
proofs and full raw/build/maps/return were independently accepted.
If representative of280pairs, ideal30-core CPU arithmetic gives138.5seconds
(4154.5CPU seconds total). This is a planning estimate; unrun degrees,
server/compiler/I/O differences and imbalance can change it. Existing engine
caps give67200CPU seconds for560passes (37m20s at ideal30CPU), excluding
operations/tail; this is not a wall completion/success promise.

30times the individual peak is4.91GB, an illustration excluding simultaneous
parents/compilers/page cache and unrun-case variation. The kernel128GB cap
sets the total, rather than an extrapolated RSS claim. Compatible Linux,
Python, compiler/loader and at least30allocated cores remain prerequisites;
pinned arithmetic libraries require glibc>=2.38.

Conditional branch-weighted storage proxy:14.26GB raw plus5.87GB compressed,
about20.1GB together; shared86MB capture store counted once. Not a size bound.
The sandbox collector's file timestamps span approximately31.26s for93.6MB;
scaling to the compressed full proxy suggests roughly33minutes collection
at similar throughput, separately from compute. Syvert compression/I/O and
fixed costs may differ. No new benchmark or extra numerical run was made.

## Checks and retention

[Focused source and artifact review](independent-checks-syvert30.md) accepts
the lean diff and independently proves oldZIP+update equals newfullZIP in
EVERYbyte/mode. All244manifest rows,35source paths,21operational pins and
13unchanged scientificFREEZE rows match. This removal-only update repeated
no obsolete policy fixtures or scientific runs. [Receipt](evidence/syvert30/lean-delivery.json).

Full artifacts/checksums/build logs remain offGit under Padua local-output;
external physical cold-storage transfer/durable retrieval remain pending.
No remote numerical execution or new certified degree is claimed here.
Original theorem/global320/residual273 remain unchanged pending returned
certificates and independent scientific review. [Runtime README](syvert30_pack/README.md).
