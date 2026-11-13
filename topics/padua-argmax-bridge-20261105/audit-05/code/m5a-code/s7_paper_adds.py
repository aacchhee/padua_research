# M5A s7: every line added to the paper comparison text (24a98db -> ad908ac) that has no close
# counterpart in the new companion comparison text (review aid for companion fidelity).
import re, difflib, sys
src = sys.argv[1]
diff = open(f"{src}/diff-paper.txt").read().split("\n")
comp = open(f"{src}/new-companion-paper.tex").read()
def norm(s):
    s = re.sub(r"\\(mathsf|mathfrak|mathcal|operatorname|rm|text)\{?", "", s)
    s = re.sub(r"[{}\\$ ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip().lower()
cn = norm(comp)
clines = [norm(l) for l in comp.split("\n")]
cwin = [" ".join(clines[i:i+3]) for i in range(len(clines))]
for i, l in enumerate(diff):
    if l.startswith("+") and not l.startswith("+++"):
        s = norm(l[1:])
        if len(s) < 25 or s in cn:
            continue
        best = max(difflib.SequenceMatcher(None, s, w).find_longest_match(0, len(s), 0, len(w)).size / len(s) for w in cwin)
        if best < 0.6:
            print(f"{i+1}: [{best:.2f}] {l[1:200]}")
