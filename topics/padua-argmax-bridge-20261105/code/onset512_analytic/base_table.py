#!/usr/bin/env python3
"""Recompute and verify all 60 manuscript comparison-base enclosures.

Read-only, standard-library CLI.  Imports the adjacent, unchanged check.py
exact Fraction interval API (including its optimization guard), composes the
remaining manuscript quantities, and checks both actual TeX tables.  This is
a table reproduction check, not a new theorem or a replacement gate checker;
receipt.json is a separate historical record and is neither read nor written.

Run from any directory with Python's -E -B flags.  --paper and --companion
accept alternate source copies for review or deliberately perturbed tests.
"""

import argparse
from fractions import Fraction as F
import importlib.util
import json
from pathlib import Path
import re
import sys


HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent.parent
DEGREES = (192, 256, 295, 512)
# Names and order match uc:base-values in both manuscripts.
SYMBOLS = (
    ('L', 'L'), (r'\mathfrak T', 'T'), (r'\bar e', 'ebar'),
    ('K_D', 'K_D'), (r'\overline C_E', 'CE'), ('C_4', 'C_4'),
    ('k_{Wx}', 'k_Wx'), ('k_{Wy}', 'k_Wy'), (r'd_\beta', 'd_beta'),
    ('M(n)', 'M(n)'), ('U_*', 'U_*'), ('d_x', 'd_x'), ('d_y', 'd_y'),
    (r'\ell_x', 'l_x'), (r'\ell_y', 'l_y'),
)
NAMES = dict(SYMBOLS)


def load_checker():
    """Load the neighboring source, without depending on sys.path/PYTHONPATH."""
    spec = importlib.util.spec_from_file_location('onset512_exact', HERE / 'check.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def base_values(g, n):
    """Compose (uc:constants), (uc:analytic-norm), and relative-gate bases.

    Eight intervals are supplied by constants(); the other quantities use
    the same outward 2^-128 arithmetic.  No displayed decimal is an input.
    """
    tt, eb, kd, ce, a4, c4, kx, ky = g.constants(n)
    ll = g.log(g.I(n))
    db = (17 * ll + 27) / n**2
    mm = (4 * ll**2 + F(79, 5) * ll) / g.PI**2 + F(9, 4) + ce + 2 * kd
    uu = tt - eb + a4 + F(23, 250)
    dx = F(11, 48) * uu - F(5, 12)
    dy = F(11, 48) * uu
    return dict(zip(NAMES.values(),
                    (ll, tt, eb, kd, ce, c4, kx, ky, db, mm, uu,
                     dx, dy, kx + F(5, 48), ky)))


def parse_table(path):
    """Parse only the labeled table; fail closed on unsupported row syntax."""
    source = path.read_text(encoding='utf-8')
    label = r'\label{uc:base-values}'
    if source.count(label) != 1:
        raise ValueError(f'{path}: expected exactly one {label}')
    after_label = source.split(label, 1)[1]
    begin = re.search(r'\\begin\{tabular\}\{[^\n]*\}', after_label)
    if begin is None or r'\end{tabular}' not in after_label[begin.end():]:
        raise ValueError(f'{path}: missing labeled tabular boundaries')
    body = after_label[begin.end():].split(r'\end{tabular}', 1)[0]
    body = re.sub(r'%[^\n]*', '', body)
    body = re.sub(r'\\(?:toprule|midrule|bottomrule)\b', '', body)
    rows = {}
    columns = None
    decimal = r'-?\d+\.\d{6}'
    enclosure = re.compile(r'\$\[(' + decimal + '),(' + decimal + r')\]\$')
    for row in body.split(r'\\'):
        row = row.strip()
        if not row:
            continue
        cells = [cell.strip() for cell in row.split('&')]
        if cells[0] == 'Quantity':
            if len(cells) != 3 or any(not re.fullmatch(r'\$\d+\$', c) for c in cells[1:]):
                raise ValueError(f'{path}: malformed degree header: {row}')
            columns = tuple(int(c[1:-1]) for c in cells[1:])
            if len(set(columns)) != len(columns) or any(n not in DEGREES for n in columns):
                raise ValueError(f'{path}: unexpected degree header: {row}')
            continue
        symbol = re.fullmatch(r'\$(.+)\$', cells[0])
        if columns is None or len(cells) != 3 or symbol is None or symbol[1] not in NAMES:
            raise ValueError(f'{path}: unexpected table row: {row}')
        for n, cell in zip(columns, cells[1:]):
            match = enclosure.fullmatch(cell)
            if match is None:
                raise ValueError(f'{path}: malformed six-decimal enclosure: {cell}')
            key = (n, NAMES[symbol[1]])
            if key in rows:
                raise ValueError(f'{path}: duplicate entry {key}')
            rows[key] = (match[1], match[2])
    expected = {(n, name) for n in DEGREES for name in NAMES.values()}
    if set(rows) != expected:
        raise ValueError(f'{path}: expected all 60 unique entries, found {len(rows)}')
    return rows


def verify_table(path, values, rounded):
    actual = parse_table(path)
    failures = []
    for n in DEGREES:
        for name in NAMES.values():
            printed = actual[n, name]
            iv = values[n][name]
            enclosed = F(printed[0]) <= iv.lo <= iv.hi <= F(printed[1])
            tight = list(printed) == rounded[str(n)][name]
            if not (enclosed and tight):
                failures.append(dict(degree=n, quantity=name, printed=list(printed),
                                     expected=rounded[str(n)][name],
                                     contains_interval=enclosed, tight_six_decimal=tight))
    return dict(entries=len(actual), status='FAIL' if failures else 'PASS', failures=failures)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--format', choices=('json', 'text'), default='json')
    parser.add_argument('--paper', type=Path,
                        default=TOPIC / 'paper/sections/comparison-unified.tex')
    parser.add_argument('--companion', type=Path,
                        default=TOPIC / 'companion-paper/sections/comparison-unified.tex')
    args = parser.parse_args()
    g = load_checker()  # Preserves check.py's refusal of -O / -OO execution.
    values = {n: base_values(g, n) for n in DEGREES}
    rounded = {str(n): {name: g.decimal_enclosure(iv) for name, iv in values[n].items()}
               for n in DEGREES}
    checks = {}
    for role, path in (('paper', args.paper), ('companion', args.companion)):
        try:
            checks[role] = verify_table(path, values, rounded)
        except (OSError, ValueError) as exc:
            checks[role] = dict(status='FAIL', error=str(exc))
    passed = all(check['status'] == 'PASS' for check in checks.values())
    result = dict(arithmetic='Fraction; outward 2^-128 grid; six-decimal outward enclosures',
                  scope='15 quantities at degrees 192, 256, 295, 512; 60 entries per manuscript',
                  values=rounded, verification=checks, status='PASS' if passed else 'FAIL')
    if args.format == 'json':
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        for n in DEGREES:
            for name in NAMES.values():
                print(f'{n} {name}: [{",".join(rounded[str(n)][name])}]')
        for role, check in checks.items():
            print(f'{role}: {check["status"]} ' + json.dumps(check, sort_keys=True))
        print(f'status: {result["status"]}')
    return 0 if passed else 1


if __name__ == '__main__':
    sys.exit(main())
