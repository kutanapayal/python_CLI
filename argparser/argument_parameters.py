import argparse

my_parser = argparse.ArgumentParser()

#default : arguments are not specified,  value is generally set to None so use default to set it.
#type : By default, all the input argument values are treated as strings so use type to set it.
#choices : creating a domain of allowed values for specific arguments.
#required=True : use the required keyword set to True for an optional argument, then user will be forced to set a value for that args.
#help : give the users even more help when they execute your program with the -h flag.
my_parser.add_argument('-a', action='store', type=int ,default=42,help='set the user given number')
my_parser.add_argument('-b', action='store', choices=['head', 'tail'],required=True,help='set the user choice to head or tail')
my_parser.add_argument('-c', action='store', type=int, choices=range(1, 5),help='set the user choice from 1 to 5')

args = my_parser.parse_args()

print(vars(args))