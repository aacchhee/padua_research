# C12/C15 output-array contract notes

2026-11-06 · D01 response to audit-01 F9. Source inspection only.
The frozen C12/C15 sources and mathematical contracts are unchanged.

Both entry points accept exact rational phase bounds in units of pi on
their guarded first-quadrant triangle, for 2<=n<=4096. A zero return
indicates success; a nonzero return supplies no usable bound. Callers
must allocate the full output/counter arrays and check the return code.

| Entry point | Output slot | Meaning |
|---|---:|---|
| `c12_box` | `out[0]` | Complete outward S upper for the input box |
| | `out[1]` | `relax`, diagnostic relaxation scale |
| | `out[2]` | `tail`, diagnostic budget scale |
| | `out[3]` | `delta`, diagnostic coefficient-range width |
| `c15_global` | `out[0]` | Complete outward S upper for the input box |
| | `out[1]` | `freeze`, maximum diagnostic freeze allowance |
| | `out[2]` | `cube`, diagnostic vertex-range scale |
| | `out[3]` | `tail`, diagnostic budget scale |
| | `out[4]` | `rho`, maximum diagnostic centre-calibration radius |

Only out[0] is the complete S upper. The remaining slots are non-additive
diagnostics, not extra summands, corrections, defect bounds or separate
independent acceptance premises. In C15 each accumulated vertex upper
already includes its freeze allowance before the maximum and final cap;
adding out[1] again would double-count that allowance. The complete
row evaluation already accounts for the retained/tail treatment used by
its upper; the separately reported tail scale is not an omitted term.
C12's relax/tail/delta and C15's cube/tail/rho must likewise not be added
to out[0] to reconstruct the bound. Diagnostic maxima and final caps also
mean the slots are not an additive decomposition of out[0].

C12 requires ten counter slots; C15 requires twelve. The C15 fault-probe
entry point returns the same five-slot output interpretation, but only
its two documented diagnostic counters. It is a forced whole-row rollback
control and does not provide a refinement to combine with another bound.

Sources: [C12 box.cpp](code/cheap_rows_C12_box/box.cpp), `box12` and
`c12_box`; [C15 global.cpp](code/cheap_rows_C15_global/global.cpp),
`global15`, `c15_global` and `c15_fault_probe`. No current result changes.
