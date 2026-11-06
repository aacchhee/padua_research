import json, sys, hashlib
sys.set_int_max_str_digits(10**6)
S = sys.argv[1]
def load(p): return [ {k:v for k,v in json.loads(x).items() if k!='elapsed_seconds'} for x in open(p)]
for r in ('bj','mirror','alt','pivot'):
    a = load(f'{S}/D36d8/checker-{r}.jsonl'); b = load(f'{S}/refl8/refl-{r}.jsonl'); c = load(f'{S}/D36d8/producer-{r}.jsonl')
    print(r, len(a), len(b), 'reflection==scalar' if a==b else 'MISMATCH', 'producer==scalar' if a==c else 'MISMATCH', 'ties', a[-1]['pivot_ties'])
    # prefix check vs deg16 producer runs if present
    try:
        p16 = load(f'{S}/D36p16/producer-{r}.jsonl')[:7]
        if len(p16)==7: print('   deg2-8 prefix of fresh deg16 producer == deg8 run:', p16==c)
    except FileNotFoundError: pass
