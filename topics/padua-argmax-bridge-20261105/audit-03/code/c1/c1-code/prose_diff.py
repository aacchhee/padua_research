"""C1 audit: which sentences of the paper's Sections 1-3 do not occur verbatim (whitespace-normalized) in the companion."""
import re, sys
T = "/home/user/padua_research/topics/padua-argmax-bridge-20261105/"
def norm(s): return re.sub(r"\s+", " ", s).strip()
def sentences(tex):
    tex = re.sub(r"(?m)%.*$", "", tex)
    tex = norm(tex)
    parts = re.split(r"(?<=[.;])\s+(?=[A-Z\\$])", tex)
    return [p for p in parts if len(p) > 25]
for sec in ("introduction", "preliminaries", "corner-unified"):
    P = open(T + "paper/sections/%s.tex" % sec).read()
    C = norm(re.sub(r"(?m)%.*$", "", open(T + "companion-paper/sections/%s.tex" % sec).read()))
    miss = [s for s in sentences(P) if s not in C]
    print("=== %s: %d paper sentences, %d not verbatim in companion" % (sec, len(sentences(P)), len(miss)))
    for s in miss: print("  -", s[:300])
