import json,sys
exec(open(sys.argv[1]).read().split("result = verify_compact.verify")[0].replace("tree, archive, package, msha, report = sys.argv[1:]","tree, archive, package, msha, report = sys.argv[2:]"))
verify_compact.verify(archive, package, msha)
print(sorted({u['name'].split('/include/')[-1] for u in unverified}))
