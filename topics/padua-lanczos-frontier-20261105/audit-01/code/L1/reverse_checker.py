import hashlib, sys
src = open(sys.argv[1], encoding='utf-8').read()
orig = src
# reverse the three documented packaging edits
src = src.replace('import shlex\nimport sys\n', '', 1)
src = src.replace('PROOF_HASH = "f27a22c4c6f13d03710750f52eef4dc9bac31f27bd009beaa536866fbbe24d9f"',
                  'PROOF_HASH = "9f59217da265a433470bb6030074acf76e63e4ffb0a6590add800666a64de90d"', 1)
cands = []
import itertools
for cmd in ['"python topics/padua-lanczos-frontier-20261105/code/sh_independent.py --output topics/padua-lanczos-frontier-20261105/evidence/sh-independent.json"',
            "'python topics/padua-lanczos-frontier-20261105/code/sh_independent.py --output topics/padua-lanczos-frontier-20261105/evidence/sh-independent.json'"]:
    s2 = src.replace('shlex.join(["python", *sys.argv])', cmd, 1)
    h = hashlib.sha256(s2.encode()).hexdigest()
    print(h, h == '3d996f0f85f006350f5a29af72fd1cf26c25c8894b18db1cf451444f908230b8')
