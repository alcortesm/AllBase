import sys
from allbase import args
from allbase import tobases

n, bases, ok, err = args.parse(sys.argv[1:])
if not ok:
    print(err, file=sys.stderr)
    sys.exit(1)

print(tobases.to_bases(n))
sys.exit(0)
