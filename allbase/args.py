import argparse
from allbase import base


def parse(list_str):
    if len(list_str) == 0:
        return None, None, False, 'no input arguments'

    desc = 'Shows numbers in several bases (hex, oct...).'
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('number',
                        help='the number you want to show',
                        type=str)
    bases_help = "one or more output bases and their order. Use 'h' for" \
        " hex, 'd' for decimal, 'o' for octal and 'b' for binary." \
        " Default: 'hdob'."
    parser.add_argument('-b', '--bases', default='dhob',
                        help=bases_help,
                        type=str)

    namespace = parser.parse_args(list_str)
    valid, reason = _is_valid(namespace)

    if not valid:
        return None, None, False, reason

    num = int(namespace.number)
    bases, ok = base.from_str_list(namespace.bases)

    return num, bases, valid, reason


def _is_valid(args):
    ok, err = _is_valid_number(args.number)
    if not ok:
        return False, err

    return _are_valid_bases(args.bases)


def _is_valid_number(s):
    try:
        n = int(s)
        if n < 0:
            raise ValueError
        return True, None
    except ValueError:
        return False, "need a positive integer, got '{}'".format(s)


def _are_valid_bases(bases):
    for c in bases:
        if base.from_char(c) is None:
            return False, "unknown base: '{}'".format(c)

    return True, None
