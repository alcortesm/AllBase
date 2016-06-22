from enum import Enum, unique


class Base():

    def __init__(self, char, base, repr):
        self.char = char
        self.base = base
        self.repr = repr

    def __repr__(self):
        return self.repr


@unique
class Bases(Enum):
    bin = Base('b', 2, 'BIN')
    oct = Base('o', 8, 'OCT')
    dec = Base('d', 10, 'DEC')
    hex = Base('h', 16, 'HEX')


def from_char(char):
    for b in list(Bases):
        if b.value.char == char:
            return b

    return None


def from_str_list(s):
    l = []
    for c in s:
        b = from_char(c)
        if b is None:
            return None, "unknown base: '{}'".format(c)
        else:
            l.append(b)

    return l, None
