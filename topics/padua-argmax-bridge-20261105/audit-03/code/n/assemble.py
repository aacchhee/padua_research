import os
here = os.path.dirname(os.path.abspath(__file__))
t = open(os.path.join(here, 'n-notation.template.md')).read()
reg = open(os.path.join(here, 'out/register-table.md')).read().rstrip('\n')
blk = open(os.path.join(here, 'out/blocks-table.md')).read().rstrip('\n')
summ = open(os.path.join(here, 'out-baseline/summary.txt')).read().rstrip('\n')
base = ("```text\n" + summ + "\n```\n\n"
 "Of the 18 paper flags, four join two different meanings in one unit: "
 "$\\delta$ and $b$ in 4.1, $b$ in 4.2, $A$ in 4.3. The others are case splits "
 "or restatements of one object (for example $r$ in 3.2, where the case $r=n$ of $d_r$ is "
 "caught, $c$ in the two cases of the proof of Lemma 4.1, and $Q_0$, $s_L$, "
 "$s_R$, $q_\\pm$ in 4.2). The 67 companion "
 "flags are in `flags-companion.txt`. The scanner's \"base symbols defined in "
 ">1 unit\" is a statistic of the heuristic, not the register count of §1.")
t = t.replace('{{ROWS}}', str(reg.count('\n') - 1)).replace('{{REGISTER}}', reg).replace('{{BLOCKS}}', blk).replace('{{BASELINE}}', base)
open(os.path.join(os.path.dirname(here), 'n-notation.md'), 'w').write(t)
print(len(t.split('\n')), 'lines')
