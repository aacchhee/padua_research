import sys, json
sys.argv=[sys.argv[0],sys.argv[1],sys.argv[2]]
src=open(sys.argv[0].replace('neg2.py','negatives.py')).read()
head=src.split('# N01')[0]
exec(head)
def lower(j): j['S_upper_rows'][0][2]='0x1p-4'
def raise_c(j): r=j['S_upper_rows'][5]; r[2]=(float.fromhex(r[2])+1.0).hex()
def lam_low(j): j['lambda_upper_rows'][0][2]='0x1p-4'
for tag,fn,deg in [('N22 lowered S endpoint both n100 records',lower,100),('N23 raised contained S endpoint +1.0 both n100 records',raise_c,100),('N24 lowered actual-lambda endpoint both n100 records',lam_low,100)]:
    d=fresh(tag.split()[0])
    for m in ('produce','verify'): edit_json(d/f'phase/inputs/n{deg:04d}-{m}.json',fn)
    refresh(d)
    run(tag+', refreshed, integrity only',d,[],'accept')
    run(tag+', refreshed, replay',d,['--degrees',str(deg)],'reject')
json.dump(results,open(work/'negatives2.json','w'),indent=1)
