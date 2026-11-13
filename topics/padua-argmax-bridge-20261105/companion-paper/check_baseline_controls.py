"""Paired silent-mutation controls; read-only on manuscript files and Git.

Run after installing the separately committed FINAL_BASELINE. These controls
test exact source freezing, not the mathematics or the completeness of parsing.
"""
import copy
import re

import check_correspondence as c


def rejected(current, baseline):
    try:
        c.check_source_freeze(current, baseline, 'mutation')
    except ValueError:
        return True
    return False


def main():
    p = c.current_sources(c.ORIGINAL)
    q = c.current_sources(c.HERE)
    bp = c.git_sources(c.ORIGINAL, c.FINAL_BASELINE)
    bq = c.git_sources(c.HERE, c.FINAL_BASELINE)
    c.check_source_freeze(p, bp, 'paper')
    c.check_source_freeze(q, bq, 'companion')
    c.compare_pair(p, q)
    tests = []

    def mutate(name, edit):
        left, right = copy.deepcopy(p), copy.deepcopy(q)
        edit(left)
        edit(right)
        c.require(left != p and right != q, 'mutation changed neither source')
        c.compare_pair(left, right)
        c.require(rejected(left, bp) and rejected(right, bq), name)
        tests.append(name)

    def replace_once(tree, path, old, new):
        c.require(old in tree[path], 'missing mutation target: ' + path)
        tree[path] = tree[path].replace(old, new, 1)

    block = c.environments(p['sections/introduction.tex'].decode(), c.CLAIMS)[0]
    quantified = block.replace('n\\geq2', 'n\\geq3', 1)
    c.require(quantified != block, 'missing theorem quantifier')
    mutate('paired theorem quantifier', lambda t: replace_once(
        t, 'sections/introduction.tex', block.encode(), quantified.encode()))
    display = next(x for x in c.environments(
        p['sections/introduction.tex'].decode(), c.DISPLAYS) if 'j+k' in x)
    changed = display.replace('j+k', 'j-k', 1)
    c.require(changed != display, 'missing numbered-display target')
    mutate('paired numbered formula', lambda t: replace_once(
        t, 'sections/introduction.tex', display.encode(), changed.encode()))
    # The strict freeze also covers prose and unnumbered mathematical text.
    mutate('paired unnumbered formula', lambda t: t.__setitem__(
        'sections/preliminaries.tex', t['sections/preliminaries.tex'] + b'\n\\[0=1\\]\n'))
    mutate('paired bibliography', lambda t: t.__setitem__(
        'references.bib', t['references.bib'] + b'\n% mutation\n'))
    mutate('paired extra TeX file', lambda t: t.__setitem__(
        'silent-extra.tex', b'% mutation\n'))
    mutate('paired main preamble text', lambda t: t.__setitem__(
        'main.tex', t['main.tex'] + b'\n% mutation\n'))
    only = copy.deepcopy(q)
    block = c.environments(only['sections/introduction.tex'].decode(), c.CLAIMS)[0]
    replace_once(only, 'sections/introduction.tex', block.encode(),
                 block.replace('n\\geq2', 'n\\geq3', 1).encode())
    c.require(only != q, 'missing companion-only target')
    try:
        c.compare_pair(p, only)
    except ValueError:
        tests.append('companion-only statement mismatch')
    else:
        raise ValueError('companion-only mutation passed')
    print('PASS:', len(tests), 'baseline controls; ' + '; '.join(tests))


if __name__ == '__main__':
    main()
