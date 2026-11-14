"""Read-only paired manuscript freeze/correspondence and artifact preservation.

Default mode checks the final revised TeX/Bib baseline. --archival checks the
historical source pair in Git and, with --artifacts, the original PDFs.
This checks source preservation/numbering, not mathematical correctness.
"""
from pathlib import Path
import argparse
import hashlib
import re
import subprocess

HISTORICAL_PAPER = 'c6e195fa5211d4504fd2638f3c7686368e28daee'
HISTORICAL_COMPANION = 'ac945041ce73b74c2c4ec29c42ebeb8773e7a9b8'
FINAL_BASELINE = 'e861c752218fc0a6648d4a4a67fea616ba5cbdd1'
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
ORIGINAL = HERE.with_name('paper')
CLAIMS = r'theorem|lemma|proposition|corollary|definition|remark'
DISPLAYS = r'equation|align|gather|multline|flalign|alignat|eqnarray'
ORIGINAL_PDFS = {
    'paper': (640116, '07db86350e74f66a46269965ace65300750f5405ddcd9d30f8daeb59411ca0f0', 48),
    'companion': (1153227, '2ec6b0723ccea6eef1368dfa0c974c4ec679a3279ef84d6ccb696c4a42c7d2f7', 162),
}
COUNTERS = r'\\(?:setcounter|addtocounter|stepcounter|refstepcounter|numberwithin|tag)\b[^\n]*'


def require(condition, message):
    if not condition: raise ValueError(message)


def git_sources(directory, revision):
    """The exact tracked TeX/Bib tree; explanatory/build docs are not frozen."""
    relative = directory.relative_to(REPO).as_posix()
    names = subprocess.check_output(['git', 'ls-tree', '-rz', '--name-only', revision, '--', relative], cwd=REPO).split(b'\0')
    result = {}
    for raw in names:
        if not raw: continue
        name = raw.decode(); path = Path(name)
        if path.suffix not in ('.tex', '.bib'): continue
        result[path.relative_to(relative).as_posix()] = subprocess.check_output(['git', 'show', revision + ':' + name], cwd=REPO)
    require('main.tex' in result and 'references.bib' in result, 'Incomplete source baseline: ' + relative)
    return result


def current_sources(directory):
    return {p.relative_to(directory).as_posix(): p.read_bytes()
            for p in directory.rglob('*') if p.is_file() and p.suffix in ('.tex', '.bib')}


def check_source_freeze(current, baseline, label):
    require(set(current) == set(baseline), label + ': TeX/Bib file set changed')
    for name in sorted(baseline):
        require(current[name] == baseline[name], label + ': TeX/Bib source changed: ' + name)


def environments(text, names):
    pattern = r'\\begin\{(' + names + r')\}.*?\\end\{\1\}'
    return [match.group() for match in re.finditer(pattern, text, re.S)]


def labels(text): return re.findall(r'\\label\{([^}]+)\}', text)


def group(text, start):
    require(text[start] == '{', 'Missing auxiliary group')
    depth = 1
    for end in range(start + 1, len(text)):
        if text[end] == '{': depth += 1
        elif text[end] == '}':
            depth -= 1
            if depth == 0: return text[start + 1:end], end + 1
    raise ValueError('Unclosed auxiliary group')


def aux_numbers(path):
    result = {}; text = path.read_text()
    for match in re.finditer(r'\\newlabel\{([^}]+)\}', text):
        payload, _ = group(text, match.end())
        number, _ = group(payload, 0)
        require(match[1] not in result, 'Duplicate built label: ' + match[1])
        result[match[1]] = number
    return result


def compare_pair(paper, companion):
    sections = sorted(name for name in paper if name.startswith('sections/') and name.endswith('.tex'))
    require(set(sections) == {name for name in companion if name.startswith('sections/') and name.endswith('.tex')}, 'Paired section file sets differ')
    all_labels = []; claims = displays = 0
    for name in sections + ['main.tex']:
        before = paper[name].decode(); after = companion[name].decode()
        for text in (before, after):
            require(not any(ord(c) < 32 and c not in '\n\t' for c in text), name + ': control character')
        heading = r'\\(?:section|subsection|subsubsection)\*?\{[^\n]*'
        require(re.findall(heading, before) == re.findall(heading, after), name + ': headings')
        for names, kind in [(CLAIMS, 'statements'), (DISPLAYS, 'numbered formulas')]:
            left, right = environments(before, names), environments(after, names)
            require(left == right, name + ': ' + kind)
            if kind == 'statements': claims += len(left)
            else: displays += len(left)
        require(labels(before) == labels(after), name + ': source labels')
        require(re.findall(COUNTERS, before) == re.findall(COUNTERS, after), name + ': counters')
        all_labels.extend(labels(before))
    require(len(set(all_labels)) == len(all_labels), 'Duplicate source labels')
    require(paper['references.bib'] == companion['references.bib'], 'Bibliography differs')
    old_main = paper['main.tex'].decode(); new_main = companion['main.tex'].decode()
    patterns = [r'\\input\{[^}]+\}', r'\\newtheorem[^\n]*', r'\\theoremstyle[^\n]*',
                r'\\documentclass[^\n]*', r'\\nocite\{[^}]+\}', COUNTERS,
                r'\\(?:re)?newcommand\s*\{?\\the(?:equation|theorem|section|subsection)\}?[^\n]*']
    for pattern in patterns:
        require(re.findall(pattern, old_main) == re.findall(pattern, new_main), 'Main numbering/input setup')
    return all_labels, claims, displays


def pdf_pages(path):
    info = subprocess.check_output(['pdfinfo', str(path)], text=True)
    match = re.search(r'^Pages:\s+(\d+)', info, re.M)
    require(match is not None, 'Missing PDF page count: ' + str(path))
    return int(match[1])


def preserved_pdf(path, kind):
    size, sha, pages = ORIGINAL_PDFS[kind]; data = path.read_bytes()
    require(len(data) == size and hashlib.sha256(data).hexdigest() == sha, 'Historical ' + kind + ' PDF identity changed')
    require(pdf_pages(path) == pages, 'Historical ' + kind + ' PDF page count changed')


def artifacts(paper_output, companion_output, all_labels, archival=False, original_paper=None, original_companion=None):
    require(paper_output != companion_output, 'Paper and companion output directories must be separate')
    if archival:
        preserved_pdf(paper_output / 'main.pdf', 'paper')
        preserved_pdf(companion_output / 'main.pdf', 'companion')
    else:
        require(original_paper is not None and original_companion is not None, 'Current artifacts require both separately preserved original PDF paths')
        require({paper_output / 'main.pdf', companion_output / 'main.pdf'}.isdisjoint(
                {original_paper, original_companion}), 'New output must not reuse original PDF paths')
        preserved_pdf(original_paper, 'paper'); preserved_pdf(original_companion, 'companion')
    left = aux_numbers(paper_output / 'main.aux'); right = aux_numbers(companion_output / 'main.aux')
    for key in all_labels:
        require(key in left and key in right, 'Missing built label: ' + key)
        require(left[key] == right[key], 'Built number differs: ' + key)
    paper_pages = pdf_pages(paper_output / 'main.pdf'); companion_pages = pdf_pages(companion_output / 'main.pdf')
    require(companion_pages <= 5 * paper_pages, f'Companion exceeds 5 x actual paper pages: {companion_pages} > 5 x {paper_pages}')
    print(f'PASS: historical 48/162-page PDFs preserved; all {len(all_labels)} built label numbers match; companion {companion_pages} <= 5 x paper {paper_pages}.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archival', action='store_true', help='Read historical paired TeX/Bib source from its fixed Git commits')
    parser.add_argument('--artifacts', action='store_true')
    parser.add_argument('--paper-output', type=Path)
    parser.add_argument('--companion-output', type=Path)
    parser.add_argument('--original-paper-pdf', type=Path)
    parser.add_argument('--original-companion-pdf', type=Path)
    args = parser.parse_args()
    if args.artifacts and (args.paper_output is None or args.companion_output is None):
        parser.error('--artifacts requires explicit --paper-output and --companion-output')
    if args.artifacts and not args.archival and (args.original_paper_pdf is None or args.original_companion_pdf is None):
        parser.error('current --artifacts requires --original-paper-pdf and --original-companion-pdf')
    if args.archival:
        paper = git_sources(ORIGINAL, HISTORICAL_PAPER); companion = git_sources(HERE, HISTORICAL_COMPANION)
        revision = HISTORICAL_PAPER + ' / ' + HISTORICAL_COMPANION
    else:
        require(re.fullmatch(r'[0-9a-f]{40}', FINAL_BASELINE) is not None,
                'Final paired source baseline is pending: root must commit final TeX/Bib sources, then install that exact commit in a separately reviewed checker update. Use --archival only for historical preservation.')
        paper = current_sources(ORIGINAL); companion = current_sources(HERE)
        check_source_freeze(paper, git_sources(ORIGINAL, FINAL_BASELINE), 'paper')
        check_source_freeze(companion, git_sources(HERE, FINAL_BASELINE), 'companion')
        revision = FINAL_BASELINE
    all_labels, claims, displays = compare_pair(paper, companion)
    print(f'PASS: paired TeX/Bib source baseline {revision}; same headings, {claims} statements, {displays} numbered display environments, {len(all_labels)} labels and bibliography.')
    if args.artifacts:
        artifacts(args.paper_output.resolve(), args.companion_output.resolve(), all_labels, args.archival,
                  args.original_paper_pdf.resolve() if args.original_paper_pdf else None,
                  args.original_companion_pdf.resolve() if args.original_companion_pdf else None)


if __name__ == '__main__':
    try: main()
    except ValueError as error: raise SystemExit(str(error)) from error
