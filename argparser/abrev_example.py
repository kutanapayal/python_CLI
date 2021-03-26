import argparse

#allow_abbrev=False : default it's true and u can pass para just like --in 42
#add_help=False : want disable auto help feature -h 

my_parser = argparse.ArgumentParser(allow_abbrev=False,add_help=False)
my_parser.add_argument('--input', action='store', type=int, required=True)
my_parser.add_argument('--id', action='store', type=int)

args = my_parser.parse_args()

print(args.input)

#Run:python3 abrev_example.py --input 42 --id 45