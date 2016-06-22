from sys import stderr
import sys
import allbase.args
from allbase.tobases import to_bases

n, bases, ok, err = allbase.args.parse(sys.argv[1:])
if not ok:
    print(err, file=stderr)
    sys.exit(1)

print(to_bases(int(n, 10)))
sys.exit(0)
