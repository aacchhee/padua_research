# M5A s5b: label-keyed comparison of formal blocks, old (24a98db) vs new (ad908ac), paper side.
import re, sys
exec(open("s5_blocks.py").read().split("for tag in")[0])
def keyed(t):
    d = {}
    for kind, body in blocks(t)[0]:
        labs = re.findall(r"\\label\{([^}]*)\}", body)
        d[labs[0] if labs else kind + body[:30]] = (kind, body)
    return d
o = keyed(load("old-paper.tex")); n = keyed(load("new-paper.tex"))
print("order old:", list(o)[:6], "... new:", list(n)[:6])
for k in n:
    if k not in o: print("NEW ONLY", k)
    elif o[k] != n[k]:
        print("CHANGED", k)
for k in o:
    if k not in n: print("OLD ONLY", k)
