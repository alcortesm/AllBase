from args import parse
from sys import stderr
from enum import Enum, unique
from collections import namedtuple


def to_bases(n):
    if n < 2 ** 4:
        template = '{0:2d} 0x{0:X} 0o{0:03o} 0b{0:04b}'
    elif n < 2 ** 8:
        template = '{0:3d} 0x{0:02X} 0o{0:03o} 0b{0:08b}'
    elif n < 2 ** 16:
        template = '{0:5d} 0x{0:04X} 0o{0:06o} 0b{0:016b}'
    elif n < 2 ** 32:
        template = '{0:10d} 0x{0:08X} 0o{0:012o} 0b{0:032b}'
    elif n < 2 ** 64:
        template = '{0:20d} 0x{0:016X} 0o{0:024o} 0b{0:064b}'
    else:
        template = '{0:d} 0x{0:X} 0o{0:o} 0b{0:b}'
    return template.format(n)


_format_spec = namedtuple('FormatSpec', ['char', 'base'])


@unique
class _format(Enum):
    bin = _format_spec('b', 2)
    oct = _format_spec('o', 8)
    dec = _format_spec('d', 10)
    hex = _format_spec('h', 16)


def read_formats(formats):
    l = []
    for c in formats:
        found = False
        for f in list(_format):
            if f.value.char == c:
                l.append(f)
                found = True
                break
        if not found:
            return None, "unknown format: '{}'".format(c)

    return l, None


def main():
    a, ok, err = parse()
    if not ok:
        print(err, file=stderr)
        return

    formats, err = read_formats(a.formats)
    if err is not None:
        print(err, file=stderr)
        return

    print(to_bases(int(a.number, 10)))


if __name__ == "__main__":
    main()
