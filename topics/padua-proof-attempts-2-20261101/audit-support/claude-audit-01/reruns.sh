#!/bin/bash
# Auditor reruns of developer checkers, sequential, into auditor-owned paths.
cd /home/claude/padua_research
T=topics/padua-proof-attempts-2-20261101
A=$T/audit-support/claude-audit-01
export PYTHONDONTWRITEBYTECODE=1
run(){ name=$1; shift; s=$(date +%s.%N); "$@" > $A/$name.stdout 2> $A/$name.stderr; rc=$?; e=$(date +%s.%N); echo "$name rc=$rc secs=$(echo "$e-$s"|bc)" >> $A/rerun-log.txt; }
echo "start $(date -u +%FT%TZ) $(python3 --version)" > $A/rerun-log.txt
run a2_exact python3 -B $T/code/a2_exact_check.py
run a2_sanity python3 -B $T/code/a2_sanity.py
run a4reg_exact python3 -B $T/code/a4reg_exact_check.py --source-sha256 13e8c524c4c21701bdee2a009cda2245d8f289d6a6cca0dba19afec1842f872e
run a4reg_compl python3 -B $T/code/a4reg_complementary_check.py --source-sha256 978bf8e00e09f4671d36d9de0e3c8dae531d34491ed7cdec1741aa6542032fca
run a4g_series python3 -B $T/code/a4g_series.py --source-sha256 510955136172a93206861f3a8252aa36460daa8c7965770d0fd6354209104ab9
run b3_exact python3 -B $T/code/b3_four_atom_exact.py --expect-source-sha256 b33647b8cff4c1b23e9b9089f9822fe307e1f8980786eec043b8bfc9ad3f9b7b --output $A/b3-exact.json
run n8_witness_standalone python3 -B $T/code/a5_n8_witness.py $T/outputs/a5_n8_interior_witnesses.json --input-sha256 ca5648106a89982995232c5555e2bfab62e0a395a743d76aa7e07835e74c30d1 --driver-sha256 bc8ed34a355d585b0cd465d1c07deea76174f399dc27b6174f5eaa319a035b60 --output $A/n8-witness-standalone.json
run n3_checker python3 -B $T/code/a5_checker.py $T/outputs/a5_n3_certificate.json.gz
run n4_checker python3 -B $T/code/a5_checker_n4.py $T/outputs/a5_n4_certificate.json.gz --global-file $T/outputs/a5_n4_global.json --output $A/n4-checker.json
run n5_checker python3 -B $T/code/a5_checker_n5.py $T/outputs/a5_n5_certificate.json.gz --global-file $T/outputs/a5_n5_global.json --output $A/n5-checker.json
run n6_checker python3 -B $T/code/a5_checker_n6.py $T/outputs/a5_n6_certificate.json.gz --global-file $T/outputs/a5_n6_global.json --output $A/n6-checker.json
run n7_checker python3 -B $T/code/a5_checker_n7.py $T/outputs/a5_n7_certificate.json.xz --global-file $T/outputs/a5_n7_global.json --output $A/n7-checker.json
echo "end $(date -u +%FT%TZ)" >> $A/rerun-log.txt
