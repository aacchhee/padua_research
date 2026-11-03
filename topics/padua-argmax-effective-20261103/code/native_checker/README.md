# Independent native certificate replay

This is a separate C++/GMP arithmetic implementation of the existing
PD-T101 constructor and PD-T210 certificate implication. It does not link,
import, call, or copy the native producer arithmetic kernel. The checker
was developed from the theorem and read-only historical Python checker,
`finite_general.py`, `finite_bernstein.py`, and corruption-control definitions.
It deliberately reproduces their 192-bit outward rounding order so that
all metadata and every claimed integer bound must agree exactly.

`kernel.cpp` implements rational Machin and cosine Taylor enclosures,
integer interval recurrence and multiplication, corrected cardinal kernel,
power polynomial construction, both rational Bernstein transforms,
corner lower/upper enclosure intersection, alternating midpoint
subdivision, and strict leaf predicates. All arithmetic on this path uses
GMP integers or rationals. No floating-point arithmetic enters a verdict.
The native input is one frontier path per line (`-` means the root).
Its first output line contains reconstructed metadata; subsequent lines
contain independently reconstructed frontier verdicts. Pending leaves can
have a null verdict and are never claimed as certified bounds.

`check.py` parses the historical v1 JSON/gzip envelope, checks source and
dependency provenance, validates the complete prefix partition, invokes
the compiled replay, and checks exact metadata, every supplied leaf,
statistics, producer non-approval, completeness, and both corner leaves.
The prefix criterion is: a finite nonempty prefix-free frontier F covers
the binary tree iff its proper-ancestor set A has |F|=|A|+1. Every member
of A has at least one child in A∪F, so the equality forces every such
vertex to have both children. The compiled traversal separately rejects
any uncovered child. Partial inputs return accepted=false.

The sole shared machinery is the certificate schema, mathematical formulas,
rounding sequence, pinned source/dependency convention and historical
compatibility rule admitting only removal of the exact n2 optimization
refusal guard. That provenance rule is independently written in the driver;
no reference Python module is imported. This is supplementary development
validation and does not replace the required Claude audit.

Build and replay from the repository root:

```sh
mkdir -p /workspace/padua-work/checker
g++ -O3 -std=c++17 topics/padua-argmax-effective-20261103/code/native_checker/kernel.cpp -lgmpxx -lgmp -o /workspace/padua-work/checker/kernel
python topics/padua-argmax-effective-20261103/code/native_checker/check.py /workspace/padua-work/producer/n17.json.gz --binary /workspace/padua-work/checker/kernel --output /workspace/padua-work/checker/n17-producer.json
python topics/padua-argmax-effective-20261103/code/native_checker/controls.py /workspace/padua-work/producer/n17.json.gz --binary /workspace/padua-work/checker/kernel --output /workspace/padua-work/checker/controls-n17.json
g++ -O3 -std=c++17 topics/padua-argmax-effective-20261103/code/native_checker/unit.cpp -lgmpxx -lgmp -o /workspace/padua-work/checker/unit
/workspace/padua-work/checker/unit
```

The implementation supports 2≤n≤100 and path depths at most 100, matching
the historical constructor. Source/bin hashes are written in receipts.
`controls.py` caches reconstructed arithmetic only for an identical degree
and entire frontier during corruption controls; all metadata and verdict
comparisons are performed anew. Normal command-line replay does not cache.
No Python assertions carry scientific validation, so Python `-O` does not
remove the driver's explicit checks. Regenerable certificates, binaries,
and receipts belong outside Git.
