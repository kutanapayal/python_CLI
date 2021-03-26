import argparse

my_parser = argparse.ArgumentParser()

#nargs='*' : a flexible number of values, which will be gathered into a list
my_parser.add_argument('input',
                       action='store',
                       nargs='*',
                       default='my default value')

args = my_parser.parse_args()

print(args.input)