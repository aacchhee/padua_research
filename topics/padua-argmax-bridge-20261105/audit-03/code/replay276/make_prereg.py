import hashlib, json
from pathlib import Path
A='/tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad'
R=A+'/replay276'; TREE=A+'/audit3/e-run/tree'
todo=json.load(open(R+'/todo.json'))
calls=[]
for n in todo:
    cert=f'{R}/inputs/outputs__all__jobs__{n}__produce__essential-receipt.json'
    data=Path(cert).read_bytes()
    out=f'{R}/out/verify-{n}'
    calls.append({'label':f'verify-{n}','n':n,'mode':'verify','output':out,'certificate':cert,
      'input_bytes':len(data),'input_sha256':hashlib.sha256(data).hexdigest(),
      'command':['/usr/local/bin/python3','-E','-S','-B',TREE+'/topics/padua-argmax-bridge-20261105/code/final_hybrid_engine/engine.py',
                 '--mode','verify','--n',str(n),'--output',out,'--run-once','--certificate',cert]})
reg={
 'status':'AUDITOR PREREGISTRATION before any native call; each call exactly once; no retry/rescue/substitute; authorized by AC (decision 3 of 5, 2026-11-08)',
 'purpose':'Local native fresh-verify replay of the 276 archive primaries not yet replayed off Syvert (degrees 42..319 except 199 and 238, plus control degrees 42,63,64,159,160 already inside that range; 41, 199, 238, 511 were replayed earlier in audit-03 part E)',
 'auditor':'Claude orchestrator claude-sonnet-5-5 (AC-authorized auditor replay; no Opus subagent involved)',
 'repo_head':'f366535e1fa4ede566cb83bdc554220c12b307cf (tree = git archive copy, engine bytes verified identical)',
 'freeze_sha256':'0d9ce0a5dbb7fb37cf1a05f07040b72d046b61b8d36b6a5a8bf137eb7d9914eb',
 'archive_sha256':'b00fd57f85ce6d96a6c1fa01e2307abd815088bb8fcb28b1587657ef142b109a',
 'cwd':TREE,
 'LD_LIBRARY_PATH':TREE+'/local-output/argmax-bridge-20261105/phase-checker/runtime/extracted/usr/lib/x86_64-linux-gnu',
 'runtime_difference':'Ubuntu 24.04 system FLINT 3.0.1 (SONAME libflint.so.18 copied as libflint.so.19), GMP 6.3.0 ubuntu, MPFR 4.2.1, g++ 13.3.0, glibc 2.39, CPython 3.13.18; the pinned Debian FLINT 3.1.3/MPFR 4.2.2/GMP 6.3.0+dfsg-3 are not used (not obtainable here)',
 'caps':'engine-internal unchanged (120 CPU/pass, checker 100, controls 2, safety 110, native 10/15); outer wall 1050 s per call; no 2GiB AS / 260 CPU outer wrapper; 4 concurrent shards on a 4-core machine',
 'shards':4,'shard_rule':'call i goes to shard i mod 4; sequential inside a shard',
 'acceptance':'per call: observed exit 0 via wait4, no timeout, ECHILD after, final-accounting result FRESH_RETAINED_PROOF_VERIFY_ACCEPTED_PENDING_RESULT_REVIEW with first_failure null and complete true, and the fresh essential-receipt fields equal the archive primary for: S_upper_columns,S_upper_rows,analytic_far,corner,floor,lambda_upper_columns,lambda_upper_rows,n,norm,origin_lower_hex,pi_bracket,tree,verification,format,status,scope',
 'failure_rule':'any non-acceptance is recorded as a result and not retried, rescued or substituted; the shard continues with the next call',
 'calls':calls}
Path(R+'/PREREGISTRATION.json').write_text(json.dumps(reg,indent=1))
print(len(calls), hashlib.sha256(Path(R+'/PREREGISTRATION.json').read_bytes()).hexdigest())
