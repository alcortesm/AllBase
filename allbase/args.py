import argparse
from allbase import base


class _ArgumentParser(argparse.ArgumentParser):

        def error(self, message):
            raise argparse.ArgumentError(None, message)


def parse(list_str):
    if len(list_str) == 0:
        return None, None, False, 'no input arguments'

    desc = 'Shows numbers in several bases (hex, oct...).'
    parser = _ArgumentParser(description=desc)

    parser.add_argument('numbers', metavar='N',
                        type=int,
                        nargs='+',
                        help='the numbers you want to show')
    bases_help = "one or more output bases and their order. Use 'h' for" \
        " hex, 'd' for decimal, 'o' for octal and 'b' for binary." \
        " Default: 'hdob'."
    parser.add_argument('-b', '--bases', default='dhob',
                        help=bases_help,
                        type=str)

    try:
        namespace = parser.parse_args(list_str)
    except argparse.ArgumentError as e:
        return None, None, False, e.args[1]

    valid, reason = _is_valid(namespace)
    if not valid:
        return None, None, False, reason

    bases, ok = base.from_str_list(namespace.bases)

    return namespace.numbers, bases, valid, reason


def _is_valid(args):
    ok, err = _are_valid_numbers(args.numbers)
    if not ok:
        return False, err

    return _are_valid_bases(args.bases)


def _are_valid_numbers(nums):
    for n in nums:
        if n < 0:
            return False, "need positive integers, got '{}'".format(n)

    return True, None


def _are_valid_bases(bases):
    for c in bases:
        if base.from_char(c) is None:
            return False, "unknown base: '{}'".format(c)

    return True, None
