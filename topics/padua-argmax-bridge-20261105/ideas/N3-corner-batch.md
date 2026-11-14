# IDEA?padua-argmax-bridge-20261105-codex-corner-02 — Common finite corner patch n2–128

Aliases: N3 range corner patch; common kappa 1/16000; phase square 1/128.

- Question/scope: verify the existing corner-radius reduction for every
  integer n in the closed range 2<=n<=128 using one common constant.
- Precise target, fixed before the batch: each independently reconstructed
  energy/corner bound must support kappa>=1/16000. The phase square
  |alpha|,|beta|<=1/128 then fits because 1/16384<1/16000.
- Mechanism/hypotheses: unchanged PD-T227/251/368 and the existing analytic
  reduction. The producer arithmetic and accepted three-case source/data
  remain unchanged. This only extends the finite degree set and uses a
  weaker common constant than the accepted n33/64/128 kappa>1/12500.
- Gate verdict: quantitative range/implementation continuation of
  IDEA-330/454/457, not a new mechanism or novelty claim. The earlier full
  baseline/N3-corner gates and their reading qualifications remain binding.
  Rules read at c000899f3fb10d6ba0f1725341a045fe11ec943a; rule files are
  unchanged from the previously read 714f3cad rules.
- Cheapest decisive test: run the unchanged compiled outward producer once
  per integer degree, verify assembly/counts/common inequality by exact
  rational arithmetic, stop on the first failed case, and request a distinct
  range replay that reconstructs from integer n rather than the bulk output.
- Predeclared budget/kill: at most 1200 total child CPU seconds, including
  compilation. Stop/report a failed threshold or arithmetic/control case;
  do not infer a replacement constant from a hidden fit. A failed target
  remains recorded. A fallback could only be proposed explicitly and must
  still meet kappa>=1/16384 to retain the phase square.
- Evidence/storage: the full rational endpoint table is local bulk only;
  commit one short aggregate receipt with fixed range/threshold, counters,
  source/binary/commands/runtime identities, minimum exact candidate kappa,
  total CPU and the single bulk file's hash/bytes. No split endpoint table.
- Status/disposition at gate: retained quantitative continuation; range
  producer and independent verification PENDING. No full global degree
  claim and no change to the stronger three-case theorem.
- Completed producer disposition: all 127 integer degrees ran/passed the
  fixed target in 5.246695 total child CPU seconds; no failed case or fallback.
  Exact minimum at128 is in `../evidence/n3-corner-batch.json`. The distinct
  integer-input range replay is still PENDING; finite claim CONDITIONAL.
- History: 2026-11-05, Codex, parent-assigned gpt-6.1-sol xhigh (serving
  metadata not independently exposed), bounded helper authorization.
