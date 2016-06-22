from enum import Enum, unique
from collections import namedtuple


BaseSpec = namedtuple('BaseSpec', 'char base str')


@unique
class Bases(Enum):
    bin = BaseSpec('b', 2, 'BIN')
    oct = BaseSpec('o', 8, 'OCT')
    dec = BaseSpec('d', 10, 'DEC')
    hex = BaseSpec('h', 16, 'HEX')

    def __str__(self):
        return self.value.str


def from_str(s):
    l = []
    for c in s:
        found = False
        for f in list(Bases):
            if f.value.char == c:
                l.append(f)
                found = True
                break
        if not found:
            return None, "unknown format: '{}'".format(c)

    return l, None
