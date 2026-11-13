# M5A s5: independent paired comparison of the formal content of the two comparison files:
# numbered display environments (unstarred equation/align/gather/multline), formal statements
# (theorem-like environments) and sectioning, in order. Whitespace-normalized comparison.
import re, sys
src = sys.argv[1]
def load(name):
    t = open(f"{src}/{name}").read()
    return re.sub(r"(?<!\\)%.*", "", t)
ENV = r"(equation|align|gather|multline|lemma|theorem|proposition|corollary|remark|definition)"
pat = re.compile(r"\\begin\{" + ENV + r"\}(.*?)\\end\{\1\}", re.S)
sec = re.compile(r"\\(sub)*section\{[^}]*\}")
def blocks(t):
    out = [(m.group(1), re.sub(r"\s+", " ", m.group(2)).strip()) for m in pat.finditer(t)]
    secs = [re.sub(r"\s+", " ", s.group(0)) for s in sec.finditer(t)]
    labels = re.findall(r"\\label\{([^}]*)\}", t)
    return out, secs, labels
for tag in ("new", "old"):
    p = load(f"{tag}-paper.tex"); c = load(f"{tag}-companion-paper.tex")
    bp, sp_, lp = blocks(p); bc, sc, lc = blocks(c)
    print(f"[{tag}] paper blocks={len(bp)} companion blocks={len(bc)}; labels paper={len(lp)} companion={len(lc)}")
    print(f"[{tag}] sections equal: {sp_ == sc}  ({len(sp_)})")
    print(f"[{tag}] label sequence equal: {lp == lc}")
    if lp != lc:
        print("   paper-only labels:", sorted(set(lp) - set(lc)))
        print("   companion-only labels:", sorted(set(lc) - set(lp)))
    nd = 0
    for i, (a, b) in enumerate(zip(bp, bc)):
        if a != b:
            nd += 1
            print(f"   DIFF #{i} {a[0]} vs {b[0]}:\n     P: {a[1][:300]}\n     C: {b[1][:300]}")
    print(f"[{tag}] differing paired blocks: {nd} (count mismatch {len(bp) - len(bc)})")

# which paired formal blocks changed between the old and new freeze (paper side)
bo, _, _ = blocks(load("old-paper.tex")); bn, _, _ = blocks(load("new-paper.tex"))
for i, (a, b) in enumerate(zip(bo, bn)):
    if a != b:
        lab = re.findall(r"\\label\{([^}]*)\}", b[1])
        print(f"CHANGED old->new #{i} {b[0]} {lab}:\n   OLD: {a[1][:420]}\n   NEW: {b[1][:420]}")
