import argparse

parser = argparse.ArgumentParser()
parser.add_argument("integer",
                    help="the number you want to show in different bases",
                    type=int)
args = parser.parse_args()
print(args.integer)


def main():
    pass


if __name__ == "__main__":
    main()
