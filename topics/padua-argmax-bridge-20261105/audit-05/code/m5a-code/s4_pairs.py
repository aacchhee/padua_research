# M5A s4: for selected old (24a98db) duplicate-pair spans of the companion comparison text,
# list each old sentence whose best fuzzy match in the new (ad908ac) companion is weak.
# The output is a review aid only; every flagged sentence is then inspected by hand.
import re, sys, difflib
src = sys.argv[1]
old = open(f"{src}/old-companion-paper.tex").read().split("\n")
new = open(f"{src}/new-companion-paper.tex").read()

def norm(s):
    s = re.sub(r"\\(mathsf|mathfrak|mathcal|operatorname|rm|text)\{?", "", s)
    s = re.sub(r"[{}\\$ ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip().lower()

def sentences(text):
    text = re.sub(r"%.*", "", text)
    parts = re.split(r"(?<=[.;:])\s+(?=[A-Z\\$(])", text.replace("\n", " "))
    return [p.strip() for p in parts if len(norm(p)) > 25]

new_sents = [norm(s) for s in sentences(new)]
new_norm = norm(new)
pairs = {
 "B01 endpoint R": [(240, 250), (267, 270)],
 "B02 E<=Z": [(270, 275), (282, 287)],
 "B03 c_s bound": [(408, 410), (489, 492)],
 "B04 Lipschitz complement": [(801, 803), (808, 816)],
 "B05 X,Y twice": [(843, 852), (853, 858)],
 "B06 8/pi^2": [(1036, 1050)],
 "B07 3u/pi^2": [(1101, 1105), (1115, 1119)],
 "B08 positive part": [(1133, 1139), (1144, 1153)],
 "B09 -(1/3+g0)a": [(1141, 1143), (1173, 1180), (1190, 1191)],
 "B10 root-free/C*": [(1182, 1201), (1203, 1220)],
 "B11 delta translation": [(1364, 1371), (1373, 1376)],
 "B12 I4": [(1399, 1400), (1408, 1411)],
 "B13 pole estimate": [(1774, 1799), (1800, 1841)],
 "C01 reference ledger": [(2093, 2113), (2115, 2147)],
 "C02": [(2180, 2196), (2197, 2207)],
 "C03": [(2214, 2222), (2224, 2258)],
 "C04 N_s": [(2345, 2353), (2354, 2394)],
 "C05": [(2396, 2407), (2408, 2427)],
 "C06 central sup": [(2433, 2451), (2453, 2494)],
 "C07": [(2553, 2559), (2560, 2583)],
 "C08": [(2603, 2609), (2622, 2651)],
 "C09": [(2689, 2737), (2739, 2745)],
 "C10 uniform const": [(2747, 2785), (2787, 2796)],
 "C11 145rho": [(3089, 3108), (3110, 3157)],
 "C12 half-line r(w)": [(3159, 3209), (3210, 3242)],
 "C13 coefficient/first row": [(3252, 3259), (3261, 3283)],
 "C14": [(3334, 3359), (3361, 3392)],
 "C15": [(3436, 3448), (3450, 3499)],
 "C16": [(3522, 3527), (3529, 3557)],
 "C17": [(3596, 3600), (3602, 3610)],
 "C18 root-free case": [(3690, 3726), (3728, 3777)],
 "C19": [(3778, 3797), (3799, 3833)],
}
sel = sys.argv[2:] if len(sys.argv) > 2 else list(pairs)
for key in pairs:
    if not any(key.startswith(s) for s in sel):
        continue
    print("=" * 100)
    print(key, pairs[key])
    for (a, b) in pairs[key]:
        text = "\n".join(old[a - 1:b])
        for s in sentences(text):
            ns = norm(s)
            if ns in new_norm:
                continue
            best = max((difflib.SequenceMatcher(None, ns, t).ratio(), t) for t in new_sents)
            if best[0] < 0.75:
                print(f"  [{a}-{b}] r={best[0]:.2f} OLD: {s[:260]}")
                print(f"        best NEW: {best[1][:200]}")
