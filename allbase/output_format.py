from enum import Enum, unique
from collections import namedtuple


output_format = namedtuple('FormatSpec', ['char', 'base'])


@unique
class output_formats(Enum):
    bin = output_format('b', 2)
    oct = output_format('o', 8)
    dec = output_format('d', 10)
    hex = output_format('h', 16)


def formats_from_sequence(sequence):
    l = []
    for c in sequence:
        found = False
        for f in list(output_formats):
            if f.value.char == c:
                l.append(f)
                found = True
                break
        if not found:
            return None, "unknown format: '{}'".format(c)

    return l, None


