from sys import stderr
import sys
from allbase import args
from allbase import output_format
from allbase import tobases


a, ok, err = args.parse()
if not ok:
    print(err, file=stderr)
    sys.exit(1)

formats, err = output_format.output_formats_from_str(a.formats)
if err is not None:
    print(err, file=stderr)
    sys.exit(1)

print(tobases.to_bases(int(a.number, 10)))
sys.exit(0)
