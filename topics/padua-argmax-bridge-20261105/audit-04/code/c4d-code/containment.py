# Check that every sentence of the paper section occurs (whitespace-normalized) in the companion section.
import re, sys
T = "/home/user/padua_research/topics/padua-argmax-bridge-20261105"
def norm(s):
    s = re.sub(r'%.*', '', s)
    return re.sub(r'\s+', ' ', s).strip()
for sec in ["localization-unified", "certification-unified"]:
    p = open(f"{T}/paper/sections/{sec}.tex").read()
    c = open(f"{T}/companion-paper/sections/{sec}.tex").read()
    pn, cn = norm(p), norm(c)
    # split on sentence ends ". " followed by capital/backslash, keep math intact roughly
    sents = re.split(r'(?<=[.;])\s+(?=[A-Z\\$])', pn)
    miss = [s for s in sents if len(s) > 25 and s not in cn]
    print(f"== {sec}: {len(sents)} paper fragments, {len(miss)} not found verbatim in companion")
    for s in miss:
        print("  -", s[:300])
