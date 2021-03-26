import argparse

my_parser = argparse.ArgumentParser()

#nargs='+' : like *, but requiring at least one value
my_parser.add_argument('input', action='store', nargs='+')

args = my_parser.parse_args()

print(args.input)