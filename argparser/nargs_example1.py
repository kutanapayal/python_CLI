import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--input', action='store', type=int, nargs=3)

args = my_parser.parse_args()

print(args.input)

#RUN :
#python nargs_example.py --input 42
#python nargs_example.py --input 42 42 42

