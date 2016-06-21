import argparse


FORMATS = frozenset('dhob')


def parse():
    desc = 'Shows numbers in several bases (hex, oct...)'
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('number',
                        help='the number you want to show',
                        type=str)
    formats_help = "one or more output formats and their order. Use 'h' for" \
                   "hex, 'd' for decimal, 'o' for octal and 'b' for binary." \
                   " Default: 'hdob'."
    parser.add_argument('-f', '--formats', default='dhob',
                        help=formats_help,
                        type=str)

    args = parser.parse_args()
    valid, reason = _is_valid(args)

    return args, valid, reason


def _is_valid(args):
    ok, err = _is_valid_number(args.number)
    if not ok:
        return False, err

    return _are_valid_formats(args.formats)


def _is_valid_number(n):
    return True, None


def _are_valid_formats(f):
    for c in f:
        if c not in FORMATS:
            return False, "unknown format: '{}'".format(c)

    return True, None
