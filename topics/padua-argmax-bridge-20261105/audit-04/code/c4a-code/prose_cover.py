"""C4A: paper sentences of Sections 1-3 that do not occur (whitespace-normalized) in the companion; independent rewrite."""
import re, sys
T = sys.argv[1]
def norm(s): return re.sub(r"\s+", " ", s).strip()
def strip(t): return norm(re.sub(r"(?m)(?<!\\)%.*$", "", t))
for sec in ("introduction", "preliminaries", "corner-unified"):
    P = strip(open(T + "/paper/sections/%s.tex" % sec).read())
    C = strip(open(T + "/companion-paper/sections/%s.tex" % sec).read())
    sents = [s for s in re.split(r"(?<=[.;:])\s+", P) if len(s) > 30]
    miss = [s for s in sents if s not in C]
    print("=== %s: %d paper sentences; %d not verbatim in companion" % (sec, len(sents), len(miss)))
    for s in miss: print("  -", s[:400])
