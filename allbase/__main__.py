import sys
from allbase import args
from allbase import tobase

nums, bases, ok, err = args.parse(sys.argv[1:])
if not ok:
    print(err, file=sys.stderr)
    sys.exit(1)

for line in tobase.do(nums, bases):
    print(line)

sys.exit(0)
