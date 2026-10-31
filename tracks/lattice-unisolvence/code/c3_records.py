#!/usr/bin/env python3
"""Assemble compact per-pattern properties and immutable run artifact hashes."""
from __future__ import annotations
import csv
import json
from pathlib import Path
import sys
from c3_rank import sha256


def main():
    root = Path(__file__).resolve().parents[3]
    directory = root / 'topics/lattice-unisolvence-20261031/directions/C3'
    catpath = directory.parent / 'C0/catalogue.json'
    cat = json.loads(catpath.read_text())
    ranks = json.loads((directory / 'ranks.json').read_text())
    structure = json.loads((directory / 'structure.json').read_text())
    obstruction = json.loads((directory / 'obstructions.json').read_text())
    lebesgue = json.loads((directory / 'lebesgue.json').read_text())
    representatives = {r['id']: r for r in ranks['representatives']}
    mapping = {m['pattern_id']: m for m in ranks['mapping']}
    covers = {r['id']: r for r in structure['covers'] if r['layers'] is not None}
    projections = {r['id']: r for r in obstruction['projection_certificates'] if r['certificate'] is not None}
    rectangles = {r['id']: r for r in obstruction['rectangle_tests']}
    symbolic = {r['id']: r for r in structure['symbolic_n1']}
    numerical = {r['id']: r for r in lebesgue['rows']}
    columns = ['pattern_id', 'C0_idea', 'n', 'lengths', 'k', 'a', 'residue',
               'representative', 'reversal_mask', 'N', 'rank_min', 'rank_max',
               'periodicity', 'axis_factorization_or_structure', 'Lebesgue_behavior',
               'annihilator_certificate']
    with (directory / 'pattern-outcomes.tsv').open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=columns, delimiter='\t')
        writer.writeheader()
        for row in cat['patterns']:
            if row['d'] != 3:
                continue
            m = mapping[row['id']]
            rep = representatives[m['representative']]
            ident = rep['id']
            criterion, certificate = 'unknown', 'none found'
            if ident in covers:
                criterion, certificate = 'universal layer-product obstruction', 'structure.json#' + ident
            elif ident in projections:
                criterion, certificate = 'universal projected-count obstruction', 'obstructions.json#' + ident
            elif ident == 'C3-8ea9e9f33e3d':
                criterion = 'PROVED isolated n2 axis-factorized iff; PD-T?lattice-c3-codex-04'
            elif ident in rectangles and rectangles[ident]['nonseparable_witness']:
                criterion = 'axis-only rational product refuted by exact rectangle; useful mixed criterion unknown'
            elif ident in symbolic:
                criterion = 'normalized n1 symbolic axis factors; finite identity, no unbounded-degree claim'
            if ident in numerical:
                numeric = numerical[ident]
                value = numeric['sampled_lebesgue']
                behavior = ('MEASURED mesh lower bound %.12g; growth unknown' % value if value is not None
                            else 'MEASURED numerical singularity/ill-conditioning; exact status unresolved')
            elif ident in covers or ident in projections:
                behavior = 'no interpolation Lebesgue constant under valid universal obstruction'
            else:
                behavior = 'unknown; untested Chebyshev specialization'
            if ident == 'C3-b083ccfa404b':
                criterion = 'PROVED mixed t-s iff; independent-axis predicates impossible; PD-N?lattice-c3-codex-02'
                behavior = 'PROVED exact Lobatto singularity; no interpolation Lebesgue constant'
            writer.writerow({'pattern_id': row['id'], 'C0_idea': row['idea_id'], 'n': row['n'],
                             'lengths': ','.join(map(str, row['lengths'])), 'k': row['k'],
                             'a': ','.join(map(str, row['a'])), 'residue': row['residues'][0],
                             'representative': ident, 'reversal_mask': m['reversal_mask'],
                             'N': rep['N'], 'rank_min': rep['rank_min'], 'rank_max': rep['rank_max'],
                             'periodicity': 'yes: primitive single congruence fibre',
                             'axis_factorization_or_structure': criterion,
                             'Lebesgue_behavior': behavior, 'annihilator_certificate': certificate})
    paths = [catpath] + sorted(directory.glob('*.json')) + [directory / 'pattern-outcomes.tsv']
    paths += sorted((root / 'tracks/lattice-unisolvence/code').glob('c3_*.py'))
    paths = [p for p in paths if p.name != 'artifact-manifest.json']
    manifest = {'schema': 'c3-artifact-manifest-v1',
                'rules_read_sha': 'e949ef06895acd5463cdf8df7e0e5f795218f70f',
                'command': sys.argv, 'generator_sha256': sha256(__file__),
                'files': [{'path': str(p.relative_to(root)), 'bytes': p.stat().st_size,
                           'sha256': sha256(p)} for p in paths],
                'retention': 'essential small reproducibility evidence; orchestrator controls Git',
                'cold_storage': r'C:\Users\andreyac\Downloads\padua\cold_storage\lattice-unisolvence-20261031',
                'cold_storage_receipt': 'not delivered; no cold-storage claim made'}
    (directory / 'artifact-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps({'patterns': len(mapping), 'outcomes_sha256': sha256(directory / 'pattern-outcomes.tsv'),
                      'manifest_sha256': sha256(directory / 'artifact-manifest.json')}, indent=2))


if __name__ == '__main__':
    main()
