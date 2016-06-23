class Base():

    def __init__(self, base, repr, to_str_fn):
        self.base = base
        self.repr = repr
        self.to_str_fn = to_str_fn

    def __repr__(self):
        return self.repr

    def to_str(self, n):
        return self.to_str_fn(n)


bin = Base(2, 'BIN', lambda n: "0b{0:b}".format(n))
oct = Base(8, 'OCT', lambda n: "0o{0:o}".format(n))
dec = Base(10, 'DEC', lambda n: "{0:d}".format(n))
hex = Base(16, 'HEX', lambda n: "0x{0:x}".format(n))
all = {
    'd': dec,
    'h': hex,
    'o': oct,
    'b': bin
}


def from_char(char):
    if char in all:
        return all[char]

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
