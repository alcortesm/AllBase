class Base():

    def __init__(self, base, repr, prefix, to_str_fn):
        self.base = base
        self.repr = repr
        self.prefix = prefix
        self.to_str_fn = to_str_fn

    def __repr__(self):
        return self.repr

    def to_str(self, n, sz):
        return self.prefix + self.to_str_fn(n, sz)

    def size(self, n):  # how long will the string be for number n?
        return len(self.to_str_fn(n, 0))

bin = Base(2, 'BIN', '0b', lambda n, sz: '{0:0{1}b}'.format(n, sz))
oct = Base(8, 'OCT', '0o', lambda n, sz: '{0:0{1}o}'.format(n, sz))
dec = Base(10, 'DEC', '', lambda n, sz: '{0:{1}d}'.format(n, sz))
hex = Base(16, 'HEX', '0x', lambda n, sz: '{0:0{1}x}'.format(n, sz))
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
