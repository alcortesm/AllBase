import argparse


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

    return args, are_valid(args)


def are_valid(args):
    return is_valid_number(args.number) & is_valid_format(args.formats)


def is_valid_number(n):
    return True


FORMATS = frozenset('dhob')


def is_valid_format(f):
    for c in f:
        if c not in FORMATS:
            print("unknown format: '{}'".format(c))
            return False

    return True
