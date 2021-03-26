import argparse

#nargs='?' : a single value, which can be optional
my_parser = argparse.ArgumentParser()
my_parser.add_argument('input',
                       action='store',
                       nargs='?',
                       default='my default value')

args = my_parser.parse_args()

print(args.input)

#Run -> python nargs_example2.py 42 