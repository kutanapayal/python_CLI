import argparse

my_parser = argparse.ArgumentParser()

#metavar :  it can be useful to give this value a name that the parser can use to generate the help message
my_parser.add_argument('-v',
                       '--verbosity',
                       action='store',
                       type=int,
                       metavar='LEVEL')

args = my_parser.parse_args()

print(vars(args))

#Run : python3 metavar_example.py -h