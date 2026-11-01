# Independent N8 field regression

Executor: `/root/a5_checker`, separate from the N8 producer implementer. Rules read at `4bd1d65ad36ddded9bf4799c0557d4a6bb83e764`. This is an actual field/cardinal regression, not an N8 certificate verification or a count claim.

Command, from `/workspace/padua_research`:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a5_n8_field.py --output topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n8_field.json
```

The final fresh sequential execution exited zero. Source SHA-256 before and after execution: `764a7d7e50718c04f076ab3bbc86270adad1c47bc902d0b8d4eecf32ebbd2ec2` (6,880 bytes). Output: `outputs/a5_independent_n8_field.json`, 1,895 bytes, SHA-256 `1c7abe81973856f109007f821e48301e34c8bc81c830b1bae7e6a7dada46486b`.

Environment: Python 3.12.14, SymPy 1.14.0, python-flint 0.9.0 / FLINT 3.6.0, SymPy ground type `flint`; bytecode writes disabled. The recorded post-import execution time is 1.394742727279663 seconds. An earlier successful run was superseded by this final sequential, source-pinned execution.

The run constructed 45 nodes and 45 cardinals, checked all 2,025 exact cardinal values and the polynomial partition of unity, and reported 1,828 nonzero coefficients. The unoptimized execution also exercised the source assertions for the two defining polynomial identities, degree-12 primitive field, both inverse conversion matrix identities, all tensor basis unit vectors and native-power conversion round trips, exact Sturm principal-root counts for U7 and U8, and strict endpoint signs of the 160-bit dyadic embedding brackets. No floating-point root choice was used in these interval checks.

I read `theory/proof-attempts-2-codex-60-degree-eight-principal-field.md` and inspected the corresponding exact conversion/embedding code. The coprime degree-4 and degree-3 argument and the U7/U8 factorizations support the stated primitive field and principal real embedding.

After the producer replay, a second, independent inline exact calculation imported no producer code: starting from the12 tensor unit vectors, multiplication by a+b used only a^4=4a²−2 and b³=3b+1. Its columns for powers0 through11 matched EVERY supplied native_to_tensor entry exactly, the determinant was independently990465713, and reduction of the supplied monic degree-12 polynomial at a+b was the zero vector. This calculation exited zero in the same Python/SymPy/flint environment; it left the producer and output artifact unchanged. Thus the consequential matrix, nonzero determinant and defining-polynomial identities printed in60 have an actual independent exact replay in addition to the source's inverse/round-trip checks. This is still a field-only regression and does not replace the required audit or certify an N8 maximum/count.
