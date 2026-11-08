import sys, re
sys.path.insert(0, '.')
from notation_scan import Doc, synctex_pages
from pathlib import Path
repo = Path('/home/user/padua_research'); T='topics/padua-argmax-bridge-20261105'
for name, sub, aux in [('paper','paper','build/paper/main.aux'),('companion','companion-paper','build/companion/main.aux')]:
    d = Doc(name, repo/T/sub)
    auxt = Path('../'+aux).read_text()
    nums = dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]*)\}', auxt))
    bad = 0
    for m in re.finditer(r'\\label\{([^}]+)\}', d.text):
        k = m.group(1)
        if k in nums and re.fullmatch(r'\d+', nums[k]):
            got = d.eq_numbers(m.start())
            if int(nums[k]) not in got:
                bad += 1; print(name, k, nums[k], got)
    print(name, 'eq-number mismatches', bad)
