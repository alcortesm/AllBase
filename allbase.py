import argparse


def arg_parse():
    desc = 'Shows numbers in several bases (hex, oct...)'
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('number',
                        help='the number you want to show',
                        type=str)
    formats_help = "one or more output formats and their order. Use 'h' for" \
                   "hex, 'd' for decimal, 'o' for octal and 'b' for binary." \
                   " Default: 'hdob'."
    parser.add_argument('-f', '--formats', default='dhob', help=formats_help)

    return parser.parse_args()


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


def main():
    args = arg_parse()
    print(to_bases(int(args.number, 10)))


if __name__ == "__main__":
    main()
