import argparse

parser = argparse.ArgumentParser()
parser.add_argument("integer",
                    help="the number you want to show in different bases",
                    type=int)
args = parser.parse_args()

d = args.integer
b = bin(d)
o = oct(d)
h = hex(d)

output = '{b} {o} {d} {h}'.format(
    b, o, d, h)

print(output)


def main():
    pass


if __name__ == "__main__":
    main()
