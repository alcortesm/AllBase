import sys
from allbase import args
from allbase import tobase

nums, bases, ok, err = args.parse(sys.argv[1:])
if not ok:
    print(err, file=sys.stderr)
    sys.exit(1)

results = tobase.do(nums, bases)
for r in results:
    print(r)

sys.exit(0)
