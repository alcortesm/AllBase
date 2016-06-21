from enum import Enum, unique
from collections import namedtuple


output_format_spec = namedtuple('FormatSpec', ['char', 'base'])


@unique
class output_formats(Enum):
    bin = output_format_spec('b', 2)
    oct = output_format_spec('o', 8)
    dec = output_format_spec('d', 10)
    hex = output_format_spec('h', 16)


def from_str(s):
    l = []
    for c in s:
        found = False
        for f in list(output_formats):
            if f.value.char == c:
                l.append(f)
                found = True
                break
        if not found:
            return None, "unknown format: '{}'".format(c)

    return l, None
