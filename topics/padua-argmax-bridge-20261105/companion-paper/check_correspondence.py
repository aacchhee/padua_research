"""Check the requested correspondence with the frozen journal manuscript.

This checks preservation and numbering, not mathematical correctness.
Run after building with --artifacts to compare actual TeX label numbers.
"""
from pathlib import Path
import argparse
import hashlib
import re
import subprocess

BASELINE = 'c6e195fa5211d4504fd2638f3c7686368e28daee'
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
ORIGINAL = HERE.with_name('paper')
CLAIMS = r'theorem|lemma|proposition|corollary|definition|remark'
DISPLAYS = r'equation|align|gather|multline|flalign|alignat|eqnarray'


def frozen(path):
    relative = path.relative_to(REPO).as_posix()
    return subprocess.check_output(
        ['git', 'show', BASELINE + ':' + relative], cwd=REPO)


def environments(text, names):
    pattern = r'\\begin\{(' + names + r')\}.*?\\end\{\1\}'
    return [match.group() for match in re.finditer(pattern, text, re.S)]


def labels(text):
    return re.findall(r'\\label\{([^}]+)\}', text)


def group(text, start):
    assert text[start] == '{'
    depth = 1
    for end in range(start + 1, len(text)):
        if text[end] == '{':
            depth += 1
        elif text[end] == '}':
            depth -= 1
            if depth == 0:
                return text[start + 1:end], end + 1
    raise ValueError('Unclosed auxiliary group')


def aux_numbers(path):
    text = path.read_text()
    result = {}
    for match in re.finditer(r'\\newlabel\{([^}]+)\}', text):
        payload, _ = group(text, match.end())
        number, _ = group(payload, 0)
        result[match[1]] = number
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--artifacts', action='store_true')
    args = parser.parse_args()

    # Preserve the complete tracked original paper directory, including its docs.
    tracked = subprocess.check_output(
        ['git', 'ls-tree', '-r', '--name-only', BASELINE,
         ORIGINAL.relative_to(REPO).as_posix()], cwd=REPO, text=True).splitlines()
    for name in tracked:
        path = REPO / name
        assert path.read_bytes() == frozen(path), 'Original changed: ' + name

    all_labels = []
    claims = displays = 0
    for original in sorted((ORIGINAL / 'sections').glob('*.tex')):
        before = frozen(original).decode()
        after = (HERE / 'sections' / original.name).read_bytes().decode()
        assert not any(ord(c) < 32 and c not in '\n\t' for c in after), original.name + ': control character'
        heading = r'\\(?:section|subsection|subsubsection)\*?\{[^\n]*'
        assert re.findall(heading, before) == re.findall(heading, after), original.name + ': headings'
        for names, kind in [(CLAIMS, 'statements'), (DISPLAYS, 'numbered formulas')]:
            left, right = environments(before, names), environments(after, names)
            assert left == right, original.name + ': ' + kind
            if kind == 'statements':
                claims += len(left)
            else:
                displays += len(left)
        assert labels(before) == labels(after), original.name + ': labels'
        controls = r'\\(?:setcounter|addtocounter|stepcounter|refstepcounter|numberwithin|tag)\b[^\n]*'
        assert re.findall(controls, before) == re.findall(controls, after), original.name + ': counters'
        all_labels.extend(labels(before))

    assert len(set(all_labels)) == len(all_labels), 'Duplicate source labels'
    assert (HERE / 'references.bib').read_bytes() == frozen(ORIGINAL / 'references.bib')
    old_main = frozen(ORIGINAL / 'main.tex').decode()
    new_main = (HERE / 'main.tex').read_text()
    for pattern in [r'\\input\{[^}]+\}', r'\\newtheorem[^\n]*',
                    r'\\theoremstyle[^\n]*', r'\\documentclass[^\n]*',
                    r'\\nocite\{[^}]+\}']:
        assert re.findall(pattern, old_main) == re.findall(pattern, new_main), 'Main numbering/input setup'
    print(f'PASS: original {len(tracked)} files intact; same headings, '
          f'{claims} statements, {displays} numbered display environments, '
          f'{len(all_labels)} labels and bibliography.')

    if args.artifacts:
        output = REPO / 'local-output/padua-argmax-bridge-20261105'
        original_pdf = (output / 'paper/main.pdf').read_bytes()
        assert len(original_pdf) == 640116, 'Original PDF size changed'
        assert hashlib.sha256(original_pdf).hexdigest() == (
            '07db86350e74f66a46269965ace65300750f5405ddcd9d30f8daeb59411ca0f0'), 'Original PDF changed'
        left = aux_numbers(output / 'paper/main.aux')
        right = aux_numbers(output / 'companion-paper/main.aux')
        for key in all_labels:
            assert key in left and key in right, 'Missing built label: ' + key
            assert left[key] == right[key], 'Number changed: ' + key
        info = subprocess.check_output(
            ['pdfinfo', str(output / 'companion-paper/main.pdf')], text=True)
        pages = int(re.search(r'^Pages:\s+(\d+)', info, re.M)[1])
        assert pages <= 240, f'Companion exceeds 5 x 48 pages: {pages}'
        print(f'PASS: original PDF unchanged; all {len(all_labels)} built label numbers match; '
              f'companion {pages} pages <= 240.')


if __name__ == '__main__':
    main()
